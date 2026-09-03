import assert from 'node:assert/strict';
import { chromium } from 'playwright';

const base = process.env.BASE_URL ?? 'http://127.0.0.1:3000';
const coreKey = 'usesafeweb:core:v1';

async function setPhase(page, locale, phase, deviceFamily) {
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
      deviceFamily,
    },
  });
}

async function waitForCheck(page, selector, expected) {
  const locator = page.locator(selector);
  await locator.waitFor({ state: 'visible' });
  await page.waitForFunction(({ selector, expected }) => {
    const node = document.querySelector(selector);
    return node?.getAttribute('data-verification-outcome') === expected
      || node?.getAttribute('data-dns-verification-state') === expected;
  }, { selector, expected });
  return locator;
}

const browser = await chromium.launch({ headless: true });
const failures = [];
function record(label, fn) {
  return Promise.resolve().then(fn).catch((error) => failures.push(`${label}: ${error.stack ?? error}`));
}

for (const [locale, deviceFamily] of [['en-GB', 'android'], ['tr-TR', 'iphone'], ['ar', 'android']]) {
  await record(`${locale} verification stays fail-closed with recovery`, async () => {
    const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
    const page = await context.newPage();
    await setPhase(page, locale, 'verify', deviceFamily);
    const response = await page.goto(`${base}/${locale}/verify?platform=${deviceFamily}`, { waitUntil: 'networkidle' });
    assert.equal(response?.status(), 200);

    const panel = await waitForCheck(page, '[data-verification-outcome]', 'uncertain');
    assert.equal(await panel.getAttribute('data-parent-confirmation'), 'confirmed');
    assert.equal(await panel.getAttribute('data-protection-state'), 'uncertain/error');
    assert.equal(await page.locator('[data-core-troubleshoot]').count(), 1);
    assert.equal((await page.locator('body').innerText()).includes('Protection verified'), false);
    await context.close();
  });
}

await record('URL/query input cannot manufacture a positive verification result', async () => {
  const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
  const page = await context.newPage();
  await setPhase(page, 'en-GB', 'verify', 'android');
  await page.goto(`${base}/en-GB/verify?platform=android&support=supported&service=healthy&dnsPath=verified-fresh`, { waitUntil: 'networkidle' });
  const panel = await waitForCheck(page, '[data-verification-outcome]', 'uncertain');
  assert.equal(await panel.getAttribute('data-protection-state'), 'uncertain/error');
  assert.equal((await page.locator('body').innerText()).includes('Protection verified'), false);
  await context.close();
});

await record('Protection Map performs a fresh check and remains fail-closed when no trusted producer is available', async () => {
  const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
  const page = await context.newPage();
  await setPhase(page, 'en-GB', 'protection', 'android');
  await page.goto(`${base}/en-GB/protection?platform=android`, { waitUntil: 'networkidle' });
  const dns = await waitForCheck(page, '[data-dns-verification-state]', 'uncertain');
  assert.equal(await dns.getAttribute('data-parent-confirmation'), 'confirmed');
  assert.equal(await dns.getAttribute('data-protection-state'), 'uncertain/error');
  assert.equal((await dns.innerText()).includes('Protection verified'), false);
  await context.close();
});

await browser.close();
if (failures.length) {
  console.error(`TSK0629_BROWSER_FAILURES=${failures.length}`);
  for (const failure of failures) console.error(`---\n${failure}`);
  process.exit(1);
}
console.log('TSK0629_BROWSER_ACCEPTANCE=PASS');
