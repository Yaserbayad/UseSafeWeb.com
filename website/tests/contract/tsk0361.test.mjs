import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, existsSync } from 'node:fs';
import { resolve } from 'node:path';

const root = resolve(import.meta.dirname, '../..');
const repoRoot = resolve(root, '..');
const read = (path) => readFileSync(resolve(root, path), 'utf8');
const json = (path) => JSON.parse(read(path));

const requiredFiles = [
  'package.json',
  'tsconfig.json',
  'next.config.ts',
  'eslint.config.mjs',
  'src/app/layout.tsx',
  'src/app/globals.css',
  'src/app/[locale]/layout.tsx',
  'src/app/[locale]/page.tsx',
  'src/app/[locale]/how-it-works/page.tsx',
  'src/app/[locale]/compatibility/page.tsx',
  'src/app/[locale]/protection-and-limits/page.tsx',
  'src/app/[locale]/privacy/page.tsx',
  'src/app/[locale]/help/page.tsx',
  'src/app/[locale]/status/page.tsx',
  'src/app/[locale]/start/page.tsx',
  'src/app/[locale]/setup/route/page.tsx',
  'src/app/[locale]/setup/native/page.tsx',
  'src/app/[locale]/setup/dns/page.tsx',
  'src/app/robots.ts',
  'src/app/sitemap.ts',
  'src/content/locale-manifest.json',
  'src/content/en-GB.json',
  'src/content/tr-TR.json',
  'src/content/ar.json',
  'src/lib/i18n.ts',
  'src/components/site-shell.tsx',
  'src/components/content-page.tsx',
  'src/components/setup-page.tsx',
];

test('TSK-0361 production baseline files exist', () => {
  for (const path of requiredFiles) assert.equal(existsSync(resolve(root, path)), true, `missing ${path}`);
});

test('framework versions and scripts follow the verified Next 16.3.3 scaffold', () => {
  const pkg = json('package.json');
  assert.equal(pkg.private, true);
  assert.equal(pkg.dependencies.next, '16.3.3');
  assert.equal(pkg.dependencies.react, '19.2.8');
  assert.equal(pkg.dependencies['react-dom'], '19.2.8');
  for (const name of ['dev', 'build', 'start', 'lint', 'typecheck', 'test:contract']) assert.ok(pkg.scripts[name], `missing script ${name}`);
  assert.match(pkg.scripts.typecheck, /next typegen\s*&&\s*tsc --noEmit/);
  const dependencyNames = Object.keys({ ...(pkg.dependencies ?? {}), ...(pkg.devDependencies ?? {}) });
  const forbiddenDb = ['prisma', '@prisma/client', 'drizzle-orm', 'better-sqlite3', 'sqlite3', 'pg', 'mysql', 'mysql2', 'mongodb', 'mongoose'];
  for (const name of forbiddenDb) assert.equal(dependencyNames.includes(name), false, `unnecessary database dependency ${name}`);
});

test('generated Next and TypeScript metadata stay outside version control', () => {
  const ignore = readFileSync(resolve(repoRoot, '.gitignore'), 'utf8');
  assert.match(ignore, /^next-env\.d\.ts$/m);
  assert.match(ignore, /^\*\.tsbuildinfo$/m);
});

test('locale manifest keeps English canonical and Turkish/Arabic provisional without market activation', () => {
  const manifest = json('src/content/locale-manifest.json');
  assert.equal(manifest.schemaVersion, '1.0.0');
  assert.equal(manifest.defaultLocale, 'en-GB');
  assert.deepEqual(manifest.supportedLocales, ['en-GB', 'tr-TR', 'ar']);
  assert.equal(manifest.locales['en-GB'].direction, 'ltr');
  assert.equal(manifest.locales['en-GB'].status, 'baseline');
  assert.equal(manifest.locales['tr-TR'].direction, 'ltr');
  assert.equal(manifest.locales['tr-TR'].status, 'provisional');
  assert.equal(manifest.locales.ar.direction, 'rtl');
  assert.equal(manifest.locales.ar.status, 'provisional');
  for (const locale of manifest.supportedLocales) assert.equal(manifest.locales[locale].marketActivation, false);
});

test('localized bundles expose the same critical public/start structure and preserve technical literals', () => {
  const locales = ['en-GB', 'tr-TR', 'ar'];
  const bundles = locales.map((locale) => [locale, json(`src/content/${locale}.json`)]);
  const requiredSections = ['common', 'home', 'howItWorks', 'compatibility', 'limits', 'privacy', 'help', 'status', 'start', 'route', 'native', 'dns'];
  for (const [locale, bundle] of bundles) {
    for (const key of requiredSections) assert.ok(bundle[key], `${locale} missing ${key}`);
    assert.equal(bundle.common.brand, 'SafeWeb');
    assert.equal(bundle.common.dnsHostname, 'dns.usesafeweb.com');
    assert.equal(bundle.common.dohUrl, 'https://dns.usesafeweb.com/dns-query');
    const flattened = JSON.stringify(bundle);
    for (const forbidden of ['browsing history dashboard', 'activity history dashboard', '100% safe', 'completely safe', 'fully protected']) {
      assert.equal(flattened.toLowerCase().includes(forbidden), false, `${locale} contains premature/prohibited claim: ${forbidden}`);
    }
  }
});

test('implementation consumes the approved shared design system rather than defining a parallel palette', () => {
  const css = read('src/app/globals.css');
  assert.match(css, /brand\/system\/TSK-0300\/tokens\.css/);
  assert.match(css, /brand\/system\/TSK-0300\/components\.css/);
  assert.doesNotMatch(css, /#[0-9a-fA-F]{6}/);
});

test('SEO and security configuration preserve public-vs-operational and no-premature-claim boundaries', () => {
  const config = read('next.config.ts');
  for (const header of ['Content-Security-Policy', 'X-Content-Type-Options', 'Referrer-Policy', 'Permissions-Policy']) assert.ok(config.includes(header), `missing security header ${header}`);
  const sitemap = read('src/app/sitemap.ts');
  assert.ok(sitemap.includes('how-it-works'));
  assert.ok(sitemap.includes('compatibility'));
  assert.ok(sitemap.includes('protection-and-limits'));
  assert.ok(sitemap.includes('privacy'));
  assert.equal(sitemap.includes('/start'), false, 'operational start route must not be in sitemap');
  const setup = read('src/components/setup-page.tsx');
  assert.match(setup, /robots:\s*\{\s*index:\s*false/);
});

test('server-first baseline contains no local persistence, analytics transport, or client-only state primitive', () => {
  const paths = requiredFiles.filter((path) => path.endsWith('.tsx') || path.endsWith('.ts'));
  const source = paths.map((path) => existsSync(resolve(root, path)) ? read(path) : '').join('\n');
  for (const forbidden of ['localStorage', 'sessionStorage', 'indexedDB', 'useState(', 'useEffect(', 'dangerouslySetInnerHTML']) {
    assert.equal(source.includes(forbidden), false, `unexpected client/persistence primitive ${forbidden}`);
  }
  assert.equal(source.includes('NEXT_PUBLIC_'), false, 'no public runtime secret/config surface is needed for this baseline');
});
