import assert from 'node:assert/strict';
import http from 'node:http';
import { chromium } from 'playwright';

const localBase = process.env.LOCAL_BASE_URL ?? 'http://127.0.0.1:3100';
const publicBase = process.env.PUBLIC_BASE_URL ?? 'https://usesafeweb.com';
const publicOrigin = new URL(publicBase).origin;
const localUrl = new URL(localBase);
const coreKey = 'usesafeweb:core:v1';
const retiredProofKey = 'usesafeweb:dns-verification:v1';

function localRequest(path, { method = 'GET', headers = {}, body = null } = {}) {
  return new Promise((resolve, reject) => {
    const request = http.request({
      hostname: localUrl.hostname,
      port: localUrl.port,
      path,
      method,
      headers,
    }, (response) => {
      const chunks = [];
      response.on('data', (chunk) => chunks.push(chunk));
      response.on('end', () => resolve({
        status: response.statusCode ?? 500,
        headers: response.headers,
        body: Buffer.concat(chunks),
      }));
    });
    request.on('error', reject);
    if (body?.length) request.write(body);
    request.end();
  });
}

function responseHeaders(headers) {
  const result = {};
  for (const [key, value] of Object.entries(headers)) {
    if (value === undefined) continue;
    result[key] = Array.isArray(value) ? value.join(', ') : String(value);
  }
  return result;
}

async function installLocalTransport(context, stats) {
  await context.route('**/*', async (route) => {
    const request = route.request();
    const url = new URL(request.url());
    let targetPath;
    const headers = { ...request.headers() };

    if (url.origin === publicOrigin) {
      targetPath = `${url.pathname}${url.search}`;
      headers.host = new URL(publicBase).host;
      if (url.pathname === '/api/dns-verification/requests') stats.requests += 1;
      if (url.pathname === '/api/dns-verification/results') stats.results += 1;
    } else if (url.hostname.endsWith('.verify.usesafeweb.com')) {
      targetPath = '/api/dns-verification/probes';
      headers.host = url.host;
      headers.origin = publicOrigin;
      headers['content-type'] = 'text/plain';
      stats.probes += 1;
    } else {
      await route.abort('blockedbyclient');
      return;
    }

    delete headers['content-length'];
    const body = request.postDataBuffer();
    if (body) headers['content-length'] = String(body.length);
    const response = await localRequest(targetPath, {
      method: request.method(),
      headers,
      body,
    });
    await route.fulfill({
      status: response.status,
      headers: responseHeaders(response.headers),
      body: response.body,
    });
  });
}

async function setPhase(page, phase) {
  await page.goto(`${publicBase}/en-GB/start`, { waitUntil: 'domcontentloaded' });
  const now = Date.now();
  await page.evaluate(({ key, state }) => sessionStorage.setItem(key, JSON.stringify(state)), {
    key: coreKey,
    state: {
      schemaVersion: 1,
      scope: 'ab'.repeat(16),
      createdAt: now - 1_000,
      hardExpiresAt: now + 120_000,
      locale: 'en-GB',
      phase,
      loginRequired: false,
      retryCount: 0,
      deviceFamily: 'android',
    },
  });
}

async function waitForState(page, selector, attribute, value) {
  await page.locator(selector).waitFor({ state: 'visible' });
  await page.waitForFunction(({ selector, attribute, value }) => (
    document.querySelector(selector)?.getAttribute(attribute) === value
  ), { selector, attribute, value });
  return page.locator(selector);
}

async function assertNoPersistedProof(page) {
  assert.equal(await page.evaluate((key) => sessionStorage.getItem(key), retiredProofKey), null);
  const storedValues = await page.evaluate(() => Object.values(sessionStorage));
  for (const value of storedValues) {
    assert.equal(value.includes('observationToken'), false);
    assert.equal(value.includes('challenge'), false);
    assert.equal(value.includes('verify.usesafeweb.com'), false);
  }
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
const stats = { requests: 0, probes: 0, results: 0 };
await installLocalTransport(context, stats);
const page = await context.newPage();

try {
  await setPhase(page, 'verify');
  const response = await page.goto(`${publicBase}/en-GB/verify?platform=android`, { waitUntil: 'networkidle' });
  assert.equal(response?.status(), 200);

  const panel = await waitForState(page, '[data-verification-outcome]', 'data-verification-outcome', 'working');
  assert.equal(await panel.getAttribute('data-protection-state'), 'protected/verified');
  assert.equal(await panel.getAttribute('data-parent-confirmation'), 'confirmed');
  assert.equal(await page.locator('[data-core-troubleshoot]').count(), 0);
  assert.equal(stats.requests, 1);
  assert.equal(stats.probes, 1);
  assert.equal(stats.results, 1);
  await assertNoPersistedProof(page);

  await page.locator('[data-core-view-protection]').click();
  await page.waitForURL(`${publicBase}/en-GB/protection?platform=android`);
  const card = await waitForState(page, '[data-dns-verification-state]', 'data-dns-verification-state', 'working');
  assert.equal(await card.getAttribute('data-protection-state'), 'protected/verified');
  assert.equal((await card.innerText()).includes('Protection verified'), true);
  assert.equal(stats.requests, 2);
  assert.equal(stats.probes, 2);
  assert.equal(stats.results, 2);
  await assertNoPersistedProof(page);

  await page.reload({ waitUntil: 'networkidle' });
  const refreshed = await waitForState(page, '[data-dns-verification-state]', 'data-dns-verification-state', 'working');
  assert.equal(await refreshed.getAttribute('data-protection-state'), 'protected/verified');
  assert.equal(stats.requests, 3);
  assert.equal(stats.probes, 3);
  assert.equal(stats.results, 3);
  await assertNoPersistedProof(page);

  console.log('TSK0243_BROWSER_ORCHESTRATION_ACCEPTANCE=PASS');
} finally {
  await context.close();
  await browser.close();
}
