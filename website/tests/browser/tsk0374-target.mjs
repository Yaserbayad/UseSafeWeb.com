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
  const label = `${locale}/${route}`;

  try {
    const viewport = { width: 390, height: 844 };
    const contextOptions = { javaScriptEnabled: false, viewport };
    const context = await browser.newContext(contextOptions);
    const page = await context.newPage();
    const requested = [];
    const failedRequests = [];
    const onRequest = (request) => requested.push(request.url());
    const onRequestFailed = (request) => {
      failedRequests.push(`${request.method()} ${request.url()}`);
    };

    page.on('request', onRequest);
    page.on('requestfailed', onRequestFailed);

    const targetUrl = `${base}/${locale}/${route}?platform=${platform}`;
    const gotoOptions = { waitUntil: 'networkidle' };
    const response = await page.goto(targetUrl, gotoOptions);

    assert.ok(response, `${label} returned no response`);
    assert.equal(response.status(), 200, `${label} HTTP status`);

    const releaseSelector = `[data-content-release="${expectedRelease}"]`;
    const statusSelector = `[data-content-status="${expectedStatus}"]`;
    const markerSelector = `${releaseSelector}${statusSelector}`;
    const marker = page.locator(markerSelector).first();
    const markerCount = await marker.count();

    assert.equal(markerCount, 1, `${label} missing release/status marker`);

    if (expectFailure) {
      const markerVisible = await marker.isVisible();
      const safeLinkSelector = [
        `a[href^="/${locale}/help"]`,
        `a[href^="/${locale}/troubleshoot"]`,
        `a[href^="/${locale}/setup/route"]`,
      ].join(', ');
      const safeLinks = page.locator(safeLinkSelector);
      const safeLinkCount = await safeLinks.count();
      const instructionCount = await page.locator('[data-instruction-id]').count();

      assert.equal(markerVisible, true, `${label} failure status is not visible`);
      assert.ok(safeLinkCount >= 1, `${label} failure has no safe recovery action`);
      assert.equal(instructionCount, 0, `${label} exposed a fail-closed instruction`);
    } else {
      const instructionSelector = `[data-instruction-id="${expectedInstruction}"]`;
      const instruction = page.locator(instructionSelector).first();
      const instructionCount = await instruction.count();
      const release = await instruction.getAttribute('data-content-release');
      const status = await instruction.getAttribute('data-content-status');

      assert.equal(instructionCount, 1, `${label} selected the wrong instruction`);
      assert.equal(release, expectedRelease);
      assert.equal(status, 'ready');
    }

    assert.deepEqual(failedRequests, [], `${label} emitted failed requests`);

    const offOrigin = requested.filter((url) => {
      const parsed = new URL(url);
      const isHttp = parsed.protocol === 'http:' || parsed.protocol === 'https:';
      return isHttp && parsed.origin !== baseOrigin;
    });

    assert.deepEqual(offOrigin, [], `${label} made an off-origin content request`);

    const cookies = await context.cookies();
    assert.deepEqual(cookies, [], `${label} created cookies`);
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

const summary =
  `TSK0374_TARGET_ACCEPTANCE status=${expectedStatus}` +
  ` release=${expectedRelease} failure=${expectFailure}`;
console.log(summary);
