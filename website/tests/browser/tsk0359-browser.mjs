import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { chromium } from 'playwright';

const require = createRequire(import.meta.url);
const axeSource = readFileSync(require.resolve('axe-core/axe.min.js'), 'utf8');
const journey = JSON.parse(readFileSync(new URL('../../src/content/journey-content.json', import.meta.url), 'utf8'));
const bindings = JSON.parse(readFileSync(new URL('../../src/content/instruction-bindings.json', import.meta.url), 'utf8'));
const localeManifest = JSON.parse(readFileSync(new URL('../../src/content/locale-manifest.json', import.meta.url), 'utf8'));
const base = process.env.BASE_URL ?? 'http://127.0.0.1:3000';
const coreKey = 'usesafeweb:core:v1';
const locales = [
  { id: 'en-GB', dir: 'ltr' },
  { id: 'tr-TR', dir: 'ltr' },
  { id: 'ar', dir: 'rtl' },
];
const phases = [
  { section: 'verify', phase: 'verify', path: '/verify?platform=android' },
  { section: 'protection', phase: 'protection', path: '/protection?platform=android' },
  { section: 'troubleshoot', phase: 'troubleshoot', path: '/troubleshoot?platform=android' },
  { section: 'recover', phase: 'recover', path: '/recover?platform=android' },
  { section: 'removed', phase: 'removed', path: '/removed?platform=android' },
  { section: 'complete', phase: 'complete', path: '/complete?platform=android' },
];

const browser = await chromium.launch({ headless: true });
const failures = [];

function record(label, fn) {
  return Promise.resolve().then(fn).catch((error) => failures.push(`${label}: ${error.stack ?? error}`));
}

async function setPhase(page, locale, phase, deviceFamily = 'android') {
  await page.goto(`${base}/${locale}/start`, { waitUntil: 'domcontentloaded' });
  const now = Date.now();
  await page.evaluate(({ key, state }) => sessionStorage.setItem(key, JSON.stringify(state)), {
    key: coreKey,
    state: {
      schemaVersion: 1,
      scope: 'ab'.repeat(16),
      createdAt: now - 1_000,
      hardExpiresAt: now + 120_000,
      locale,
      phase,
      loginRequired: false,
      retryCount: 0,
      deviceFamily,
    },
  });
}

async function assertLocalizedPage(page, locale, dir, section, path, phase) {
  await setPhase(page, locale, phase);
  const response = await page.goto(`${base}/${locale}${path}`, { waitUntil: 'domcontentloaded' });
  assert.ok(response);
  assert.equal(response.status(), 200);
  assert.equal(await page.locator('html').getAttribute('lang'), locale);
  assert.equal(await page.locator('html').getAttribute('dir'), dir);
  assert.equal((await page.locator('h1').innerText()).trim(), journey.sections[section][locale].title);
  const body = await page.locator('body').innerText();
  assert.equal(body.includes('UseSafeWeb'), false, 'stale visible product identity');
  const robots = (await page.locator('meta[name="robots"]').getAttribute('content')) ?? '';
  assert.match(robots, /noindex/i, `${path} must stay operational/noindex`);
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  assert.ok(overflow <= 1, `horizontal overflow ${overflow}`);
}

for (const locale of locales) {
  await record(`${locale.id} externalized TSK-0358 operational surfaces`, async () => {
    const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
    const page = await context.newPage();
    for (const item of phases) await assertLocalizedPage(page, locale.id, locale.dir, item.section, item.path, item.phase);
    await context.close();
  });

  await record(`${locale.id} source-bound platform instructions`, async () => {
    const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
    const page = await context.newPage();

    for (const [deviceFamily, setupId, verifyId, removeId] of [
      ['android', 'INS-AND-SETUP-01', 'INS-AND-VERIFY-01', 'INS-AND-REMOVE-01'],
      ['iphone', 'INS-IOS-SETUP-01', 'INS-IOS-VERIFY-01', 'INS-IOS-REMOVE-01'],
    ]) {
      await setPhase(page, locale.id, 'dns', deviceFamily);
      await page.goto(`${base}/${locale.id}/setup/dns?platform=${deviceFamily}`, { waitUntil: 'domcontentloaded' });
      assert.match(await page.locator('body').innerText(), new RegExp(bindings.instructions[setupId].variants[locale.id].replace(/[.*+?^${}()|[\]\\]/g, '\\$&')));

      await setPhase(page, locale.id, 'verify', deviceFamily);
      await page.goto(`${base}/${locale.id}/verify?platform=${deviceFamily}`, { waitUntil: 'domcontentloaded' });
      assert.match(await page.locator('body').innerText(), new RegExp(bindings.instructions[verifyId].variants[locale.id].replace(/[.*+?^${}()|[\]\\]/g, '\\$&')));

      await setPhase(page, locale.id, 'recover', deviceFamily);
      await page.goto(`${base}/${locale.id}/recover?platform=${deviceFamily}`, { waitUntil: 'domcontentloaded' });
      assert.match(await page.locator('body').innerText(), new RegExp(bindings.instructions[removeId].variants[locale.id].replace(/[.*+?^${}()|[\]\\]/g, '\\$&')));
    }
    await context.close();
  });
}

await record('Arabic TSK-0359 operational page remains WCAG 2.2 AA and RTL', async () => {
  const context = await browser.newContext({ viewport: { width: 320, height: 720 } });
  const page = await context.newPage();
  await setPhase(page, 'ar', 'protection');
  await page.goto(`${base}/ar/protection?platform=android`, { waitUntil: 'domcontentloaded' });
  await page.addScriptTag({ content: axeSource });
  const result = await page.evaluate(async () => await window.axe.run(document, {
    runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa'] },
  }));
  assert.deepEqual(result.violations.map((v) => ({ id: v.id, impact: v.impact, nodes: v.nodes.length })), []);
  assert.equal(await page.locator('html').getAttribute('dir'), 'rtl');
  await context.close();
});

for (const locale of locales) {
  assert.equal(localeManifest.locales[locale.id].marketActivation, false, `${locale.id} language availability cannot imply market activation`);
}

await browser.close();
if (failures.length) {
  console.error(`TSK0359_BROWSER_FAILURES=${failures.length}`);
  for (const failure of failures) console.error(`---\n${failure}`);
  process.exit(1);
}
console.log('TSK0359_BROWSER_ACCEPTANCE=PASS');
