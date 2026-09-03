import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { stripTypeScriptTypes } from 'node:module';

const root = resolve(import.meta.dirname, '../..');
const modulePath = resolve(root, 'src/lib/intake-routing.ts');
const routePagePath = resolve(root, 'src/app/[locale]/setup/route/page.tsx');

async function loadApi() {
  assert.equal(existsSync(modulePath), true, 'missing TSK-0375 intake routing engine');
  const source = readFileSync(modulePath, 'utf8');
  const js = stripTypeScriptTypes(source, { mode: 'strip' });
  return import(`data:text/javascript;base64,${Buffer.from(js).toString('base64')}`);
}

const locales = ['en-GB', 'tr-TR', 'ar'];

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
    { locale: 'fr-FR', choice: 'android' },
    { locale: 'en-GB', choice: 'windows' },
    { locale: 'en-GB', choice: ['android'] },
    { locale: 'en-GB', choice: 'android', domain: 'example.com' },
    { locale: 'en-GB', choice: 'android', accountId: 'parent-1' },
    { locale: 'en-GB', choice: 'android', childId: 'child-1' },
    { locale: 'en-GB', choice: 'android', queryHistory: ['example.com'] },
    { locale: 'en-GB', choice: 'android', diagnostic: 'raw' },
  ]) {
    assert.throws(() => api.resolveIntakeRoute(input), /invalid intake routing input/);
  }
});

test('routing engine source has an exact two-field input boundary and no persistence or identity dependency', async () => {
  await loadApi();
  const source = readFileSync(modulePath, 'utf8');
  assert.match(source, /Object\.keys\(candidate\)\.sort\(\)/);
  assert.match(source, /\['choice', 'locale'\]/);
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
