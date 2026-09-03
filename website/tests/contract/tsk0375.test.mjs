import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { stripTypeScriptTypes } from 'node:module';

const root = resolve(import.meta.dirname, '../..');
const modulePath = resolve(root, 'src/lib/intake-routing.ts');
const i18nModulePath = resolve(root, 'src/lib/i18n.ts');
const routePagePath = resolve(root, 'src/app/[locale]/setup/route/page.tsx');

function readCanonicalLocales() {
  const source = readFileSync(i18nModulePath, 'utf8');
  const declaration = source.match(/export const locales\s*=\s*\[([^\]]+)\]\s*as const;/);
  assert.ok(declaration, 'missing canonical locales declaration in i18n.ts');
  const values = [...declaration[1].matchAll(/['"]([^'"]+)['"]/g)].map(([, locale]) => locale);
  assert.ok(values.length > 0, 'canonical locale authority must not be empty');
  return values;
}

const locales = readCanonicalLocales();

async function loadApi() {
  assert.equal(existsSync(modulePath), true, 'missing TSK-0375 intake routing engine');
  const source = readFileSync(modulePath, 'utf8');
  const importPattern = /import\s*\{\s*isLocale\s*\}\s*from\s*['"]@\/lib\/i18n['"];?\s*/;
  assert.match(source, importPattern, 'routing engine must consume canonical i18n locale authority');
  const testSource = source.replace(
    importPattern,
    `const __supportedLocales = new Set(${JSON.stringify(locales)});\nconst isLocale = (value) => __supportedLocales.has(value);\n`,
  );
  assert.notEqual(testSource, source, 'test harness failed to bind canonical locale authority');
  const js = stripTypeScriptTypes(testSource, { mode: 'strip' });
  return import(`data:text/javascript;base64,${Buffer.from(js).toString('base64')}`);
}

test('approved locale/device intake decision table is deterministic and unsupported choice is a clear safe state', async () => {
  const api = await loadApi();
  for (const locale of locales) {
    assert.deepEqual(api.resolveIntakeRoute({ locale, choice: 'android' }), {
      state: 'supported',
      deviceFamily: 'android',
      href: `/${locale}/setup/native?platform=android`,
    });
    assert.deepEqual(api.resolveIntakeRoute({ locale, choice: 'iphone' }), {
      state: 'supported',
      deviceFamily: 'iphone',
      href: `/${locale}/setup/native?platform=iphone`,
    });
    assert.deepEqual(api.resolveIntakeRoute({ locale, choice: 'other' }), {
      state: 'unsupported',
      deviceFamily: null,
      href: `/${locale}/compatibility`,
    });
  }
});

test('invalid or prohibited intake data is rejected and cannot influence routing', async () => {
  const api = await loadApi();
  for (const input of [
    null,
    [],
    {},
    { locale: 'not-a-supported-locale', choice: 'android' },
    { locale: locales[0], choice: 'windows' },
    { locale: locales[0], choice: ['android'] },
    { locale: locales[0], choice: 'android', domain: 'example.com' },
    { locale: locales[0], choice: 'android', accountId: 'parent-1' },
    { locale: locales[0], choice: 'android', childId: 'child-1' },
    { locale: locales[0], choice: 'android', queryHistory: ['example.com'] },
    { locale: locales[0], choice: 'android', diagnostic: 'raw' },
  ]) {
    assert.throws(() => api.resolveIntakeRoute(input), /invalid intake routing input/);
  }
});

test('routing engine source has an exact two-field input boundary, canonical locale dependency, and no persistence or identity dependency', async () => {
  await loadApi();
  const source = readFileSync(modulePath, 'utf8');
  assert.match(source, /Object\.keys\(candidate\)\.sort\(\)/);
  assert.match(source, /\['choice', 'locale'\]/);
  assert.match(source, /isLocale\(locale\)/);
  assert.doesNotMatch(source, /new Set\(\s*\[['"]en-GB['"]/);
  assert.doesNotMatch(source, /sessionStorage|localStorage|cookie|account|child|domain|query|history|diagnostic/i);
});

test('setup route consumes the canonical intake routing engine for all three choices', () => {
  const source = readFileSync(routePagePath, 'utf8');
  assert.match(source, /resolveIntakeRoute/);
  assert.match(source, /choice:\s*'android'/);
  assert.match(source, /choice:\s*'iphone'/);
  assert.match(source, /choice:\s*'other'/);
  assert.doesNotMatch(source, /setup\/native\?platform=android/);
  assert.doesNotMatch(source, /setup\/native\?platform=iphone/);
});
