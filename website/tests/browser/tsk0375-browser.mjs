import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { chromium } from 'playwright';

const base = process.env.BASE_URL ?? 'http://127.0.0.1:3210';
const root = resolve(import.meta.dirname, '../..');

function readCanonicalLocales() {
  const source = readFileSync(resolve(root, 'src/lib/i18n.ts'), 'utf8');
  const declaration = source.match(/export const locales\s*=\s*\[([^\]]+)\]\s*as const;/);
  assert.ok(declaration, 'missing canonical locales declaration in i18n.ts');
  const values = [...declaration[1].matchAll(/['"]([^'"]+)['"]/g)].map(([, locale]) => locale);
  assert.ok(values.length > 0, 'canonical locale authority must not be empty');
  return values;
}

const locales = readCanonicalLocales();
const cases = [
  { choice: 'android', href: (locale) => `/${locale}/setup/native?platform=android` },
  { choice: 'iphone', href: (locale) => `/${locale}/setup/native?platform=iphone` },
  { choice: 'other', href: (locale) => `/${locale}/compatibility` },
];
const forbiddenKeys = new Set(['accountId', 'childId', 'domain', 'queryHistory', 'diagnostic']);

function assertMinimalSession(entries) {
  for (const [key, raw] of entries) {
    assert.ok(key === 'usesafeweb:j0:v1' || key === 'usesafeweb:core:v1', `unexpected session key: ${key}`);
    const parsed = JSON.parse(raw);
    for (const field of Object.keys(parsed)) {
      assert.equal(forbiddenKeys.has(field), false, `forbidden session field: ${field}`);
    }
  }
}

const browser = await chromium.launch({ headless: true });
const failures = [];

try {
  for (const locale of locales) {
    for (const testCase of cases) {
      const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
      const page = await context.newPage();
      try {
        const routeResponse = await page.goto(`${base}/${locale}/setup/route`, { waitUntil: 'domcontentloaded' });
        assert.equal(routeResponse?.status(), 200);

        const expectedHref = testCase.href(locale);
        const link = page.locator(`.sw-actions a[href="${expectedHref}"]`);
        await link.waitFor({ state: 'visible' });
        assert.equal(await link.count(), 1, `${locale}/${testCase.choice} route action count`);

        const sessionEntries = await page.evaluate(() => Object.entries(sessionStorage));
        assertMinimalSession(sessionEntries);

        await Promise.all([
          page.waitForURL(`${base}${expectedHref}`),
          link.click(),
        ]);
        assert.equal(page.url(), `${base}${expectedHref}`);
      } catch (error) {
        failures.push(`${locale}/${testCase.choice}: ${error.stack ?? error}`);
      } finally {
        await context.close();
      }
    }
  }
} finally {
  await browser.close();
}

if (failures.length) {
  console.error(`TSK0375_BROWSER_FAILURES=${failures.length}`);
  for (const failure of failures) console.error(`---\n${failure}`);
  process.exit(1);
}

console.log('TSK0375_INTAKE_ROUTING_BROWSER_ACCEPTANCE=PASS');
