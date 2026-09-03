import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { stripTypeScriptTypes } from 'node:module';

const root = resolve(import.meta.dirname, '../..');
const read = (path) => readFileSync(resolve(root, path), 'utf8');
const json = (path) => JSON.parse(read(path));

const journeyPath = 'src/content/journey-content.json';
const bindingsPath = 'src/content/instruction-bindings.json';
const fallbackModulePath = 'src/lib/locale-fallback.ts';
const localizedPages = [
  'src/app/[locale]/verify/page.tsx',
  'src/app/[locale]/protection/page.tsx',
  'src/app/[locale]/troubleshoot/page.tsx',
  'src/app/[locale]/recover/page.tsx',
  'src/app/[locale]/removed/page.tsx',
  'src/app/[locale]/complete/page.tsx',
];
const locales = ['en-GB', 'tr-TR', 'ar'];
const instructionIds = [
  'INS-AND-SETUP-01',
  'INS-AND-VERIFY-01',
  'INS-AND-REMOVE-01',
  'INS-IOS-SETUP-01',
  'INS-IOS-VERIFY-01',
  'INS-IOS-REMOVE-01',
  'INS-COMMON-UNCERTAIN-01',
  'INS-COMMON-NOTCOVERED-01',
  'INS-COMMON-RECOVERY-01',
];

async function loadFallbackApi() {
  assert.equal(existsSync(resolve(root, fallbackModulePath)), true, 'missing deterministic locale fallback module');
  const source = read(fallbackModulePath);
  const js = stripTypeScriptTypes(source, { mode: 'strip' });
  return import(`data:text/javascript;base64,${Buffer.from(js).toString('base64')}`);
}

test('TSK-0359 localization artifacts exist and package contract runs this task', () => {
  for (const path of [journeyPath, bindingsPath, fallbackModulePath, ...localizedPages]) {
    assert.equal(existsSync(resolve(root, path)), true, `missing ${path}`);
  }
  const pkg = json('package.json');
  assert.match(pkg.scripts['test:contract'], /tsk0359\.test\.mjs/);
});

test('deterministic fallback resolves requested locale first, then declared fallback, and fails visibly when no value exists', async () => {
  const api = await loadFallbackApi();
  const fallback = { 'en-GB': null, 'tr-TR': 'en-GB', ar: 'en-GB' };
  assert.deepEqual(api.resolveLocaleValue('ar', { ar: 'عربي', 'en-GB': 'English' }, fallback, 'en-GB'), { value: 'عربي', sourceLocale: 'ar' });
  assert.deepEqual(api.resolveLocaleValue('tr-TR', { 'en-GB': 'English' }, fallback, 'en-GB'), { value: 'English', sourceLocale: 'en-GB' });
  assert.throws(() => api.resolveLocaleValue('tr-TR', {}, fallback, 'en-GB'), /missing localized value/i);
  assert.throws(() => api.resolveLocaleValue('tr-TR', { 'en-GB': 'English' }, { 'en-GB': 'tr-TR', 'tr-TR': 'en-GB' }, 'en-GB'), /fallback cycle/i);
});

test('journey content externalizes all TSK-0358 operational surfaces for English, Turkish and Arabic', () => {
  const content = json(journeyPath);
  assert.equal(content.schemaVersion, '1.0.0');
  assert.equal(content.defaultLocale, 'en-GB');
  assert.deepEqual(content.supportedLocales, locales);
  for (const section of ['verify', 'protection', 'troubleshoot', 'recover', 'removed', 'complete']) {
    assert.ok(content.sections[section], `missing section ${section}`);
    for (const locale of locales) {
      const value = content.sections[section][locale];
      assert.ok(value, `${section} missing ${locale}`);
      for (const field of ['kicker', 'title', 'summary', 'noteTitle', 'noteBody']) {
        assert.equal(typeof value[field], 'string', `${section}.${locale}.${field} missing`);
        assert.ok(value[field].trim().length > 0, `${section}.${locale}.${field} empty`);
      }
    }
  }
  const serialized = JSON.stringify(content);
  assert.equal(serialized.includes('UseSafeWeb'), false, 'visible product copy must use current SafeWeb identity');
  assert.equal(/100% safe|completely safe|fully protected/i.test(serialized), false, 'premature safety claim');
});

test('instruction bindings preserve all nine current TSK-0307 IDs and exact current provenance', () => {
  const bindings = json(bindingsPath);
  assert.equal(bindings.schemaVersion, '1.0.0');
  assert.equal(bindings.sourceArtifact, 'TSK_0307_POST_CR0008_CURRENT_SOURCE_BACKED_INSTRUCTION_CATALOGUE_REVALIDATION_2026-09-02.md');
  assert.equal(bindings.sourceCommit, '330e9d13b9d479212ca6c49df3431f19f7107ba5');
  assert.equal(bindings.lastVerified, '2026-09-02');
  assert.deepEqual(Object.keys(bindings.instructions).sort(), [...instructionIds].sort());
  for (const id of instructionIds) {
    const item = bindings.instructions[id];
    assert.ok(item.purpose, `${id} missing purpose`);
    assert.deepEqual(Object.keys(item.variants).sort(), [...locales].sort(), `${id} locale variants incomplete`);
    for (const locale of locales) assert.ok(item.variants[locale].trim().length > 0, `${id} ${locale} variant empty`);
  }
  const serialized = JSON.stringify(bindings);
  assert.match(serialized, /dns\.usesafeweb\.com/);
  assert.equal(serialized.includes('UseSafeWeb DNS'), false, 'stale visible brand must not return');
});

test('i18n layer uses declared fallback and instruction bindings rather than silent locale/string selection', () => {
  const source = read('src/lib/i18n.ts');
  assert.match(source, /resolveLocaleValue/);
  assert.match(source, /journey-content\.json/);
  assert.match(source, /instruction-bindings\.json/);
  assert.match(source, /getJourneyContent/);
  assert.match(source, /getInstructionVariant/);
  assert.match(source, /sourceLocale/);
});

test('new operational pages consume externalized content and contain no hard-coded visible page/action copy', () => {
  for (const path of localizedPages) {
    const source = read(path);
    assert.match(source, /getJourneyContent/,
      `${path} must consume TSK-0359 externalized content`);
    for (const prop of ['kicker', 'title', 'summary', 'noteTitle', 'noteBody', 'label']) {
      assert.doesNotMatch(source, new RegExp(`${prop}\\s*=\\s*["']`), `${path} hard-codes ${prop}`);
    }
    assert.doesNotMatch(source, /UseSafeWeb/, `${path} contains stale visible brand`);
  }
  const protection = read('src/app/[locale]/protection/page.tsx');
  assert.doesNotMatch(protection, /label:\s*['"]/, 'Protection Map row labels must be localized');
  const complete = read('src/app/[locale]/complete/page.tsx');
  assert.doesNotMatch(complete, />\s*[A-Za-z][^<{]*</, 'completion page contains literal visible English JSX');
});

test('DNS and recovery surfaces select current instruction IDs by locale and platform without duplicate instruction rendering', () => {
  const dns = read('src/app/[locale]/setup/dns/page.tsx');
  assert.match(dns, /getInstructionVariant/);
  assert.match(dns, /INS-AND-SETUP-01/);
  assert.match(dns, /INS-IOS-SETUP-01/);
  assert.doesNotMatch(dns, /label="I saved this DNS setting/);
  assert.equal((dns.match(/\{instruction\.value\}/g) ?? []).length, 1, 'DNS setup must render the exact source-bound instruction only once');
  const verify = read('src/app/[locale]/verify/page.tsx');
  assert.match(verify, /INS-AND-VERIFY-01/);
  assert.match(verify, /INS-IOS-VERIFY-01/);
  const recover = read('src/app/[locale]/recover/page.tsx');
  assert.match(recover, /INS-AND-REMOVE-01/);
  assert.match(recover, /INS-IOS-REMOVE-01/);
});

test('Protection Map state machine no longer owns user-facing English/legacy-brand copy', () => {
  const source = read('src/lib/core-state-machine.ts');
  assert.doesNotMatch(source, /primary:\s*string|supporting:\s*string/);
  assert.doesNotMatch(source, /Protection verified|Protection status could not be verified|Protection has not yet been technically verified|UseSafeWeb/);
});

test('locale manifest is the single authority for direction and non-activating language availability', () => {
  const manifest = json('src/content/locale-manifest.json');
  const journey = json(journeyPath);
  const browser = read('tests/browser/tsk0359-browser.mjs');
  assert.equal(manifest.locales.ar.direction, 'rtl');
  assert.equal(manifest.locales['en-GB'].direction, 'ltr');
  assert.equal(manifest.locales['tr-TR'].direction, 'ltr');
  for (const locale of locales) assert.equal(manifest.locales[locale].marketActivation, false, `${locale} must not imply market activation`);
  assert.equal(Object.hasOwn(journey, 'marketActivation'), false, 'journey content must not duplicate market-activation authority');
  assert.match(browser, /locale-manifest\.json/);
  assert.doesNotMatch(browser, /journey\.marketActivation/);
});
