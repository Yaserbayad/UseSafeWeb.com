import assert from 'node:assert/strict';
import { chromium } from 'playwright';

const base = process.env.BASE_URL ?? 'http://127.0.0.1:3000';
const storageKey = 'usesafeweb:j0:v1';
const DAY_MS = 24 * 60 * 60 * 1000;
const browser = await chromium.launch({ headless: true });
const failures = [];

function record(label, fn) {
  return Promise.resolve().then(fn).catch((error) => failures.push(`${label}: ${error.stack ?? error}`));
}

async function stored(page) {
  const raw = await page.evaluate((key) => sessionStorage.getItem(key), storageKey);
  return raw ? JSON.parse(raw) : null;
}

async function storedAtStep(page, step) {
  await page.waitForFunction(
    ({ key, expectedStep }) => {
      const raw = sessionStorage.getItem(key);
      if (!raw) return false;
      try {
        return JSON.parse(raw).journeyStep === expectedStep;
      } catch {
        return false;
      }
    },
    { key: storageKey, expectedStep: step },
  );
  return stored(page);
}

await record('J0 journey is created only when setup begins and resumes within the same tab session', async () => {
  const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
  const page = await context.newPage();
  const mutations = [];
  page.on('request', (request) => {
    if (!['GET', 'HEAD', 'OPTIONS'].includes(request.method())) mutations.push(`${request.method()} ${request.url()}`);
  });

  await page.goto(`${base}/en-GB/start`, { waitUntil: 'networkidle' });
  assert.equal(await stored(page), null, 'start page must not create state before setup begins');

  await page.locator('a[href="/en-GB/setup/route"]').click();
  await page.waitForURL('**/en-GB/setup/route');
  const route = await storedAtStep(page, 'route');
  assert.ok(route, 'setup route must create J0 state');
  assert.deepEqual(Object.keys(route).sort(), ['createdAt', 'hardExpiresAt', 'journeyStep', 'locale', 'schemaVersion', 'scope']);
  assert.match(route.scope, /^[0-9a-f]{32}$/);
  assert.equal(route.locale, 'en-GB');
  assert.equal(route.journeyStep, 'route');
  assert.ok(route.hardExpiresAt > route.createdAt);
  assert.ok(route.hardExpiresAt - route.createdAt <= DAY_MS);

  await page.locator('a[href="/en-GB/setup/native?platform=android"]').click();
  await page.waitForURL('**/en-GB/setup/native?platform=android');
  const native = await storedAtStep(page, 'native');
  assert.equal(native.scope, route.scope);
  assert.equal(native.hardExpiresAt, route.hardExpiresAt, 'navigation must not slide expiry');
  assert.equal(native.journeyStep, 'native');
  assert.equal(native.deviceFamily, 'android');
  assert.equal('dnsMethod' in native, false);

  await page.locator('a[href="/en-GB/setup/dns?platform=android"]').click();
  await page.waitForURL('**/en-GB/setup/dns?platform=android');
  const dns = await storedAtStep(page, 'dns');
  assert.equal(dns.scope, route.scope);
  assert.equal(dns.hardExpiresAt, route.hardExpiresAt);
  assert.equal(dns.journeyStep, 'dns');
  assert.equal(dns.deviceFamily, 'android');
  assert.equal(dns.dnsMethod, 'android_private_dns_dot');
  assert.deepEqual(mutations, [], `J0 journey must not create server persistence: ${mutations.join(' | ')}`);

  await page.goto(`${base}/en-GB/start`, { waitUntil: 'networkidle' });
  const resume = page.locator('[data-journey-resume]');
  await resume.waitFor({ state: 'visible' });
  assert.equal(await resume.getAttribute('href'), '/en-GB/setup/dns?platform=android');
  await context.close();
});

await record('reset deletes immediately and malformed or expired state cannot be resumed', async () => {
  const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
  const page = await context.newPage();
  await page.goto(`${base}/en-GB/setup/route`, { waitUntil: 'networkidle' });
  assert.ok(await storedAtStep(page, 'route'));
  await page.goto(`${base}/en-GB/start`, { waitUntil: 'networkidle' });
  await page.locator('[data-journey-reset]').click();
  assert.equal(await stored(page), null, 'reset must delete state synchronously');
  assert.equal(await page.locator('[data-journey-resume]').count(), 0, 'resume must disappear after reset');

  const now = Date.now();
  await page.evaluate(({ key, nowMs, dayMs }) => {
    sessionStorage.setItem(key, JSON.stringify({
      schemaVersion: 1,
      scope: 'ab'.repeat(16),
      createdAt: nowMs - dayMs - 1,
      hardExpiresAt: nowMs - 1,
      locale: 'en-GB',
      journeyStep: 'route',
    }));
  }, { key: storageKey, nowMs: now, dayMs: DAY_MS });
  await page.reload({ waitUntil: 'networkidle' });
  assert.equal(await stored(page), null, 'expired state must be deleted on read');
  assert.equal(await page.locator('[data-journey-resume]').count(), 0);

  await page.evaluate((key) => {
    sessionStorage.setItem(key, JSON.stringify({
      schemaVersion: 1,
      scope: 'ab'.repeat(16),
      createdAt: Date.now(),
      hardExpiresAt: Date.now() + 60_000,
      locale: 'en-GB',
      journeyStep: 'route',
      email: 'parent@example.invalid',
    }));
  }, storageKey);
  await page.reload({ waitUntil: 'networkidle' });
  assert.equal(await stored(page), null, 'unknown/personal field must invalidate and delete state');
  assert.equal(await page.locator('[data-journey-resume]').count(), 0);
  await context.close();
});

await record('journey scope is distinct across independent browser sessions', async () => {
  async function startScope() {
    const context = await browser.newContext();
    const page = await context.newPage();
    await page.goto(`${base}/en-GB/setup/route`, { waitUntil: 'networkidle' });
    const state = await storedAtStep(page, 'route');
    await context.close();
    assert.ok(state);
    return state.scope;
  }
  const a = await startScope();
  const b = await startScope();
  assert.notEqual(a, b, 'independent sessions must not share journey scope');
});

await browser.close();

if (failures.length) {
  console.error(`TSK0357_BROWSER_FAILURES=${failures.length}`);
  for (const failure of failures) console.error(`---\n${failure}`);
  process.exit(1);
}

console.log('TSK0357_BROWSER_ACCEPTANCE=PASS');
