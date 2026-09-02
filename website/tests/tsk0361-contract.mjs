import assert from 'node:assert/strict';
import { readFileSync, existsSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import test from 'node:test';

const here = dirname(fileURLToPath(import.meta.url));
const website = resolve(here, '..');

function read(path) {
  const full = join(website, path);
  assert.ok(existsSync(full), `missing ${path}`);
  return readFileSync(full, 'utf8');
}

function readJson(path) {
  return JSON.parse(read(path));
}

test('pins the approved Next.js application baseline without a local database', () => {
  const pkg = readJson('package.json');
  assert.equal(pkg.dependencies?.next, '16.3.4');
  assert.equal(pkg.dependencies?.react, '19.2.8');
  assert.equal(pkg.dependencies?.['react-dom'], '19.2.8');
  assert.equal(pkg.dependencies?.['radix-ui'], '1.6.7');
  assert.equal(pkg.dependencies?.['@keystatic/core'], '0.6.9');
  assert.equal(pkg.dependencies?.['@keystatic/next'], '5.0.5');

  const allDependencies = Object.keys({ ...pkg.dependencies, ...pkg.devDependencies });
  const forbidden = ['prisma', '@prisma/client', 'sqlite', 'sqlite3', 'better-sqlite3', 'pg', 'postgres', 'mysql', 'mysql2', 'mongoose'];
  for (const dependency of forbidden) {
    assert.ok(!allDependencies.includes(dependency), `unexpected local database dependency: ${dependency}`);
  }
});

test('pins the Next 16 compatible ESLint 9 line used by the verified build', () => {
  const pkg = readJson('package.json');
  assert.equal(pkg.devDependencies?.eslint, '9.39.5');
  assert.equal(pkg.devDependencies?.['eslint-config-next'], '16.3.4');
});

test('pins a deterministic real-browser acceptance harness', () => {
  const pkg = readJson('package.json');
  assert.equal(pkg.devDependencies?.['@playwright/test'], '1.62.1');
  assert.equal(pkg.devDependencies?.['@axe-core/playwright'], '4.13.0');
  assert.equal(pkg.scripts?.['test:e2e'], 'playwright test');
  read('playwright.config.ts');
  read('tests/tsk0361-e2e.spec.ts');
  read('package-lock.json');
});

test('uses the approved standalone self-hosting and repo-root Turbopack boundary', () => {
  const nextConfig = read('next.config.ts');
  assert.match(nextConfig, /output:\s*['"]standalone['"]/);
  assert.match(nextConfig, /poweredByHeader:\s*false/);
  assert.match(nextConfig, /turbopack:\s*\{/);
  assert.match(nextConfig, /root:\s*path\.resolve\(process\.cwd\(\),\s*['"]\.\.['"]\)/);
  assert.match(nextConfig, /X-Content-Type-Options/);
  assert.match(nextConfig, /Referrer-Policy/);
  assert.match(nextConfig, /Permissions-Policy/);
});

test('implements locale-routed English, Turkish and Arabic public/start surfaces', () => {
  const i18n = read('src/lib/i18n.ts');
  assert.match(i18n, /['"]en['"]/);
  assert.match(i18n, /['"]tr['"]/);
  assert.match(i18n, /['"]ar['"]/);
  assert.match(i18n, /rtl/);

  read('src/app/[lang]/layout.tsx');
  read('src/app/[lang]/page.tsx');
  read('src/app/[lang]/start/page.tsx');
  read('src/proxy.ts');
});

test('consumes the canonical SafeWeb design-system sources rather than inventing replacement brand values', () => {
  const globalCss = read('src/app/globals.css');
  assert.match(globalCss, /TSK-0300\/tokens\.css/);
  assert.match(globalCss, /TSK-0300\/components\.css/);
  assert.doesNotMatch(globalCss, /#[0-9a-fA-F]{6}/, 'implementation CSS must consume canonical tokens instead of raw brand colours');
});

test('integrates an accessible component library and browser-editable content adapter', () => {
  const page = read('src/app/[lang]/page.tsx');
  const cms = read('keystatic.config.ts');
  const cmsClient = read('src/app/keystatic/keystatic.ts');
  read('src/app/keystatic/[[...params]]/page.tsx');
  const cmsApi = read('src/app/api/keystatic/[...params]/route.ts');

  assert.match(page, /radix-ui/);
  assert.match(cms, /@keystatic\/core/);
  assert.match(cms, /kind:\s*['"]local['"]/);
  assert.match(cmsClient, /makePage/);
  assert.match(cmsApi, /makeRouteHandler/);
});

test('preserves accountless-first truth and prohibited-data boundaries in public/start copy', () => {
  const text = [
    read('src/content/home/en.json'),
    read('src/content/home/tr.json'),
    read('src/content/home/ar.json'),
    read('src/app/[lang]/start/page.tsx'),
  ].join('\n').toLowerCase();

  assert.match(text, /without (an )?account|hesap olmadan|دون حساب/);
  assert.match(text, /browsing history|tarama geçmiş|سجل التصفح/);
  assert.doesNotMatch(text, /completely safe|fully protected|100% safe/);
});
