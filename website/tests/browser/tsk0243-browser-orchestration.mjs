import assert from 'node:assert/strict';
import http from 'node:http';
import { chromium } from 'playwright';

const localBase = process.env.LOCAL_BASE_URL ?? 'http://127.0.0.1:3100';
const publicBase = process.env.PUBLIC_BASE_URL ?? 'https://usesafeweb.com';
const publicOrigin = new URL(publicBase).origin;
const localUrl = new URL(localBase);
const coreKey = 'usesafeweb:core:v1';
const proofKey = 'usesafeweb:dns-verification:v1';

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

async function installLocalTransport(context) {
  await context.route('**/*', async (route) => {
    const request = route.request();
    const url = new URL(request.url());
    let targetPath;
    const headers = { ...request.headers() };

    if (url.origin === publicOrigin) {
      targetPath = `${url.pathname}${url.search}`;
      headers.host = new URL(publicBase).host;
    } else if (url.hostname.endsWith('.verify.usesafeweb.com')) {
      targetPath = '/api/dns-verification/probes';
      headers.host = url.host;
      headers.origin = publicOrigin;
      headers['content-type'] = 'text/plain';
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

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
await installLocalTransport(context);
const page = await context.newPage();

try {
  await setPhase(page, 'verify');
  const response = await page.goto(`${publicBase}/en-GB/verify?platform=android`, { waitUntil: 'networkidle' });
  assert.equal(response?.status(), 200);

  const panel = await waitForState(page, '[data-verification-outcome]', 'data-verification-outcome', 'working');
  assert.equal(await panel.getAttribute('data-protection-state'), 'protected/verified');
  assert.equal(await panel.getAttribute('data-parent-confirmation'), 'confirmed');
  assert.equal(await page.locator('[data-core-verify-recovery]').count(), 0);

  const stored = await page.evaluate((key) => sessionStorage.getItem(key), proofKey);
  assert.ok(stored);
  const proof = JSON.parse(stored);
  assert.deepEqual(Object.keys(proof).sort(), ['challenge', 'observationToken']);
  assert.match(proof.challenge, /^[0-9a-f]{32}$/);
  assert.equal(typeof proof.observationToken, 'string');
  assert.ok(proof.observationToken.length > 40);

  await page.locator('[data-core-view-protection]').click();
  await page.waitForURL(`${publicBase}/en-GB/protection?platform=android`);
  const card = await waitForState(page, '[data-dns-verification-state]', 'data-dns-verification-state', 'working');
  assert.equal(await card.getAttribute('data-protection-state'), 'protected/verified');
  assert.equal((await card.innerText()).includes('Protection verified'), true);

  await page.evaluate((key) => {
    const current = JSON.parse(sessionStorage.getItem(key));
    sessionStorage.setItem(key, JSON.stringify({ ...current, working: true }));
  }, proofKey);
  await page.reload({ waitUntil: 'networkidle' });
  const tampered = await waitForState(page, '[data-dns-verification-state]', 'data-dns-verification-state', 'uncertain');
  assert.equal(await tampered.getAttribute('data-protection-state'), 'uncertain/error');
  assert.equal((await tampered.innerText()).includes('Protection verified'), false);
  assert.equal(await page.evaluate((key) => sessionStorage.getItem(key), proofKey), null);

  console.log('TSK0243_BROWSER_ORCHESTRATION_ACCEPTANCE=PASS');
} finally {
  await context.close();
  await browser.close();
}
