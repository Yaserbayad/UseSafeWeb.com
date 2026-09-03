import assert from 'node:assert/strict';
import { chromium } from 'playwright';

const base = process.env.BASE_URL ?? 'http://127.0.0.1:3000';
const baseOrigin = new URL(base).origin;
const expectedStatus = process.env.TSK0374_EXPECTED_STATUS;
const expectedRelease = process.env.TSK0374_EXPECTED_RELEASE;
const expectFailure = process.env.TSK0374_EXPECT_FAILURE === '1';

assert.ok(expectedStatus, 'TSK0374_EXPECTED_STATUS is required');
assert.ok(expectedRelease, 'TSK0374_EXPECTED_RELEASE is required');

const cases = [
  ['en-GB', 'android', 'setup/dns', 'INS-AND-SETUP-01'],
  ['en-GB', 'iphone', 'setup/dns', 'INS-IOS-SETUP-01'],
  ['tr-TR', 'android', 'verify', 'INS-AND-VERIFY-01'],
  ['tr-TR', 'iphone', 'verify', 'INS-IOS-VERIFY-01'],
  ['ar', 'android', 'recover', 'INS-AND-REMOVE-01'],
  ['ar', 'iphone', 'recover', 'INS-IOS-REMOVE-01'],
];

const browser = await chromium.launch({ headless: true });
const failures = [];

for (const [locale, platform, route, expectedInstruction] of cases) {
  try {
    const context = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 390, height: 844 } });
    const page = await context.newPage();
    const requested = [];
    const failedRequests = [];
    page.on('request', (request) => requested.push(request.url()));
    page.on('requestfailed', (request) => failedRequests.push(`${request.method()} ${request.url()}`));

    const response = await page.goto(`${base}/${locale}/${route}?platform=${platform}`, { waitUntil: 'networkidle' });
    assert.ok(response, `${locale}/${route} returned no response`);
    assert.equal(response.status(), 200, `${locale}/${route} HTTP status`);

    const marker = page.locator(`[data-content-release="${expectedRelease}"][data-content-status="${expectedStatus}"]`).first();
    assert.equal(await marker.count(), 1, `${locale}/${route} missing expected release/status marker`);

    if (expectFailure) {
      assert.equal(await marker.isVisible(), true, `${locale}/${route} failure status is not visible`);
      const safeLinks = page.locator(`a[href^="/${locale}/help"], a[href^="/${locale}/troubleshoot"], a[href^="/${locale}/setup/route"]`);
      assert.ok((await safeLinks.count()) >= 1, `${locale}/${route} failure has no safe recovery action`);
      assert.equal(await page.locator('[data-instruction-id]').count(), 0, `${locale}/${route} exposed an instruction while fail-closed`);
    } else {
      const instruction = page.locator(`[data-instruction-id="${expectedInstruction}"]`).first();
      assert.equal(await instruction.count(), 1, `${locale}/${route} selected the wrong instruction`);
      assert.equal(await instruction.getAttribute('data-content-release'), expectedRelease);
      assert.equal(await instruction.getAttribute('data-content-status'), 'ready');
    }

    assert.deepEqual(failedRequests, [], `${locale}/${route} emitted failed requests`);
    const offOrigin = requested.filter((url) => {
      const parsed = new URL(url);
      return (parsed.protocol === 'http:' || parsed.protocol === 'https:') && parsed.origin !== baseOrigin;
    });
    assert.deepEqual(offOrigin, [], `${locale}/${route} made an off-origin content request`);
    assert.deepEqual(await context.cookies(), [], `${locale}/${route} created cookies`);
    await context.close();
  } catch (error) {
    failures.push(error.stack ?? String(error));
  }
}

await browser.close();

if (failures.length) {
  console.error(`TSK0374_TARGET_FAILURES=${failures.length}`);
  for (const failure of failures) console.error(`---\n${failure}`);
  process.exit(1);
}

console.log(`TSK0374_TARGET_ACCEPTANCE status=${expectedStatus} release=${expectedRelease} failure=${expectFailure}`);
