import assert from 'node:assert/strict';
import { chromium } from 'playwright';

const base = process.env.BASE_URL ?? 'http://127.0.0.1:3000';
const baseOrigin = new URL(base).origin;
const coreKey = 'usesafeweb:core:v1';
const browser = await chromium.launch({ headless: true });
const failures = [];

function record(label, fn) {
  return Promise.resolve()
    .then(fn)
    .catch((error) => failures.push(`${label}: ${error.stack ?? error}`));
}

async function coreState(page) {
  const raw = await page.evaluate((key) => sessionStorage.getItem(key), coreKey);
  return raw ? JSON.parse(raw) : null;
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

function isTransientDnsVerificationRequest(request) {
  if (request.method() !== 'POST') return false;
  const url = new URL(request.url());
  if (
    url.origin === baseOrigin &&
    ['/api/dns-verification/requests', '/api/dns-verification/results'].includes(url.pathname)
  )
    return true;
  return url.hostname.endsWith('.verify.usesafeweb.com') && url.pathname === '/api/dns-verification/probes';
}

await record(
  'accountless core fails closed at uncertain verification and truthful Protection Map remains available only from valid protection state',
  async () => {
    const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
    const page = await context.newPage();
    const unexpectedMutations = [];
    page.on('request', (request) => {
      if (['GET', 'HEAD', 'OPTIONS'].includes(request.method())) return;
      if (!isTransientDnsVerificationRequest(request)) unexpectedMutations.push(`${request.method()} ${request.url()}`);
    });

    await page.goto(`${base}/en-GB/start`, { waitUntil: 'domcontentloaded' });
    assert.equal(
      await page.locator('a[href*="login"],a[href*="account"],a[href*="signin"]').count(),
      0,
      'core start must not require or promote login',
    );
    await page.locator('a[href="/en-GB/setup/route"]').click();
    await page.locator('a[href="/en-GB/setup/native?platform=android"]').click();
    await page.locator('[data-core-continue-native]').click();
    await page.waitForURL('**/en-GB/setup/dns?platform=android');
    await page.locator('[data-core-continue-dns]').click();
    await page.waitForURL('**/en-GB/verify?platform=android');

    const verifyPanel = page.locator('[data-verification-outcome]');
    await verifyPanel.waitFor({ state: 'visible' });
    await page.waitForFunction(
      () =>
        document.querySelector('[data-verification-outcome]')?.getAttribute('data-verification-outcome') ===
        'uncertain',
    );
    assert.equal(await verifyPanel.getAttribute('data-protection-state'), 'uncertain/error');
    assert.equal(
      await page.locator('[data-core-view-protection]').count(),
      0,
      'uncertain verification must not enter Services',
    );
    assert.equal(await page.locator('[data-core-troubleshoot]').count(), 1);
    await page.locator('[data-core-troubleshoot]').click();
    await page.waitForURL('**/en-GB/troubleshoot?platform=android');
    assert.equal((await coreState(page)).phase, 'troubleshoot');

    await setPhase(page, 'en-GB', 'protection', 'android');
    await page.goto(`${base}/en-GB/protection?platform=android`, { waitUntil: 'domcontentloaded' });
    const state = await coreState(page);
    assert.ok(state);
    assert.equal(state.phase, 'protection');
    assert.equal(state.loginRequired, false);
    assert.equal(
      'email' in state ||
        'accountId' in state ||
        'history' in state ||
        'query' in state ||
        'domain' in state ||
        'verification' in state,
      false,
    );
    assert.deepEqual(
      unexpectedMutations,
      [],
      `accountless core must not create persistent or unapproved server mutation: ${unexpectedMutations.join(' | ')}`,
    );

    const cards = page.locator('[data-protection-state]');
    assert.equal(await cards.count(), 3);
    assert.equal(await cards.nth(0).getAttribute('data-protection-state'), 'configured/parent-confirmed');
    assert.equal(await cards.nth(1).getAttribute('data-protection-state'), 'uncertain/error');
    assert.equal(await cards.nth(2).getAttribute('data-protection-state'), 'not-covered');
    assert.equal(
      await page.locator('[data-protection-state="protected/verified"]').count(),
      0,
      'no qualifying E1 exists in TSK-0358',
    );
    assert.match(await page.textContent('body'), /Protection has not yet been technically verified\./);
    assert.match(await page.textContent('body'), /Protection status could not be verified/);

    await page.locator('[data-core-troubleshoot]').click();
    await page.waitForURL('**/en-GB/troubleshoot?platform=android');
    await page.locator('[data-core-recover]').click();
    await page.waitForURL('**/en-GB/recover?platform=android');
    await page.locator('[data-core-remove]').click();
    await page.waitForURL('**/en-GB/removed?platform=android');
    assert.equal((await coreState(page)).phase, 'removed');
    await context.close();
  },
);

await record('completion is accountless and optional account capability stays explicitly deferred', async () => {
  const context = await browser.newContext();
  const page = await context.newPage();
  await setPhase(page, 'en-GB', 'protection', 'iphone');
  await page.goto(`${base}/en-GB/protection?platform=iphone`, { waitUntil: 'domcontentloaded' });
  await page.locator('[data-core-complete]').click();
  await page.waitForURL('**/en-GB/complete?platform=iphone');
  assert.equal((await coreState(page)).phase, 'complete');
  const account = page.locator('[data-account-capability]');
  assert.equal(await account.getAttribute('data-account-capability'), 'deferred');
  assert.equal(await page.locator('a[href*="dashboard"],a[href*="login"],a[href*="signin"]').count(), 0);
  assert.match(await page.textContent('body'), /Setup complete/);
  await context.close();
});

await record(
  'lost or expired core state fails closed to accountless route instead of fabricating progress',
  async () => {
    const context = await browser.newContext();
    const page = await context.newPage();
    await page.goto(`${base}/en-GB/protection?platform=android`, { waitUntil: 'domcontentloaded' });
    await page.waitForURL('**/en-GB/setup/route');
    assert.equal(await coreState(page), null);

    await page.evaluate((key) => {
      sessionStorage.setItem(
        key,
        JSON.stringify({
          schemaVersion: 1,
          scope: 'ab'.repeat(16),
          createdAt: 1,
          hardExpiresAt: 2,
          locale: 'en-GB',
          phase: 'protection',
          loginRequired: false,
          retryCount: 0,
          deviceFamily: 'android',
        }),
      );
    }, coreKey);
    await page.goto(`${base}/en-GB/protection?platform=android`, { waitUntil: 'domcontentloaded' });
    await page.waitForURL('**/en-GB/setup/route');
    assert.equal(await coreState(page), null, 'expired core state must be deleted');
    await context.close();
  },
);

await browser.close();
if (failures.length) {
  console.error(`TSK0358_BROWSER_FAILURES=${failures.length}`);
  for (const failure of failures) console.error(`---\n${failure}`);
  process.exit(1);
}
console.log('TSK0358_BROWSER_ACCEPTANCE=PASS');
