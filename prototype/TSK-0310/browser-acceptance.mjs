import { chromium } from 'playwright';

const BASE = 'http://127.0.0.1:4173/prototype/TSK-0310/';
const passed = [];
const externalRequests = [];
const consoleErrors = [];
const pageErrors = [];

function ok(condition, name, detail = '') {
  if (!condition) throw new Error(`${name}${detail ? `: ${detail}` : ''}`);
  passed.push(name);
  console.log(`CHECK ${name}=PASS${detail ? ` | ${detail}` : ''}`);
}

async function screen(page, expected, label) {
  const root = page.locator(`[data-screen="${expected}"]`);
  await root.waitFor({ state: 'visible' });
  ok(await root.count() === 1, `${label}:screen-${expected}`);
  ok(await page.evaluate(() => document.activeElement?.tagName === 'H1'), `${label}:h1-focus`);
  const overflow = await page.evaluate(() => ({ sw: document.documentElement.scrollWidth, iw: window.innerWidth }));
  ok(overflow.sw <= overflow.iw + 1, `${label}:no-horizontal-overflow`, `${overflow.sw}/${overflow.iw}`);
  ok(await page.locator('#app').getAttribute('aria-busy') === 'false', `${label}:aria-busy-false`);
}

async function reset(page, label = 'reset') {
  await page.locator('[data-global-action="RESET"]').click();
  await screen(page, 'discovery', label);
}

async function start(page, platform, nativeAction = 'NATIVE_CONFIRMED', label = platform) {
  await page.locator('[data-action="START"]').click();
  await screen(page, 'router', `${label}:router`);
  await page.locator(`[data-platform="${platform}"]`).click();
  if (platform === 'other') {
    await screen(page, 'limitations', `${label}:limitations`);
    return;
  }
  await screen(page, 'native', `${label}:native`);
  await page.locator(`[data-action="${nativeAction}"]`).click();
  await screen(page, 'dns', `${label}:dns`);
}

async function configureAndVerify(page, result, label) {
  await page.locator('[data-action="DNS_CONFIGURED"]').click();
  await screen(page, 'verify', `${label}:verify`);
  await page.locator(`[data-action="VERIFY_RESULT"][data-result="${result}"]`).click();
}

async function assertStorageEmpty(page, label) {
  const storage = await page.evaluate(async () => ({
    local: localStorage.length,
    session: sessionStorage.length,
    cookie: document.cookie,
    sw: 'serviceWorker' in navigator ? (await navigator.serviceWorker.getRegistrations()).length : 0
  }));
  ok(storage.local === 0, `${label}:local-storage-empty`);
  ok(storage.session === 0, `${label}:session-storage-empty`);
  ok(storage.cookie === '', `${label}:cookie-empty`);
  ok(storage.sw === 0, `${label}:no-service-worker`);
}

let browser;
try {
  browser = await chromium.launch({ headless: true, channel: 'chromium' });
  console.log(`BROWSER_VERSION=${browser.version()}`);
  const context = await browser.newContext({ viewport: { width: 320, height: 700 } });
  await context.route('**/*', async route => {
    const u = new URL(route.request().url());
    if (u.hostname === '127.0.0.1' || u.hostname === 'localhost') return route.continue();
    externalRequests.push(route.request().url());
    return route.abort('blockedbyclient');
  });
  const page = await context.newPage();
  page.on('console', msg => { if (msg.type() === 'error') consoleErrors.push(msg.text()); });
  page.on('pageerror', error => pageErrors.push(String(error)));

  await page.goto(BASE, { waitUntil: 'networkidle' });
  await screen(page, 'discovery', 'initial');
  ok(await page.title() === 'SafeWeb — Internal mobile-first prototype', 'initial:title');
  ok(await page.locator('meta[name="robots"]').getAttribute('content') === 'noindex,nofollow', 'initial:noindex-nofollow');
  ok(await page.locator('img[alt="SafeWeb"]').count() === 1, 'initial:logo-alt');
  ok(await page.locator('form,input,textarea,select').count() === 0, 'initial:no-data-entry-controls');
  ok(await page.locator('button:not([type="button"])').count() === 0, 'initial:button-types');
  ok((await page.locator('body').innerText()).includes('does not promise complete safety'), 'initial:bounded-claim-copy');
  await assertStorageEmpty(page, 'initial');

  await page.locator('[data-global-action="OPEN_HELP"]').click();
  await screen(page, 'troubleshooting', 'help');
  ok((await page.locator('body').innerText()).includes('VPN, browser/app custom DNS, Private Relay'), 'help:conflict-copy');
  await page.locator('[data-action="RETURN"]').click();
  await screen(page, 'discovery', 'help-return');
  await page.locator('[data-global-action="SHOW_LIMITATIONS"]').click();
  await screen(page, 'limitations', 'limits');
  ok((await page.locator('body').innerText()).includes('Parent confirmation and profile/settings presence do not equal system verification.'), 'limits:verification-boundary');
  await page.locator('[data-action="RETURN"]').click();
  await screen(page, 'discovery', 'limits-return');

  await page.evaluate(() => {
    const b = document.createElement('button');
    b.type = 'button';
    b.dataset.action = 'DNS_CONFIGURED';
    b.id = 'illegal-transition-test';
    b.textContent = 'Illegal transition';
    document.body.appendChild(b);
  });
  await page.locator('#illegal-transition-test').click();
  ok((await page.locator('[role="alert"]').innerText()).includes('Action not allowed from discovery'), 'negative:illegal-transition-blocked');
  ok(await page.locator('[data-screen="discovery"]').count() === 1, 'negative:illegal-transition-preserves-screen');
  await reset(page, 'negative-reset');

  await start(page, 'android', 'NATIVE_CONFIRMED', 'android-success');
  ok((await page.locator('.prototype-code').innerText()).trim() === 'dns.usesafeweb.com', 'android:exact-private-dns-hostname');
  ok((await page.locator('body').innerText()).includes('does not silently change Android system DNS'), 'android:no-silent-os-change');
  await configureAndVerify(page, 'verified', 'android-success');
  await screen(page, 'service', 'android-success:service');
  await page.locator('[data-action="SERVICE_NONE"]').click();
  await screen(page, 'map', 'android-success:map');
  const aPhone = page.locator('.sw-status').filter({ hasText: 'Phone' });
  const aInternet = page.locator('.sw-status').filter({ hasText: 'Internet' });
  const aService = page.locator('.sw-status').filter({ hasText: 'Service' });
  ok(await aPhone.getAttribute('data-evidence-state') === 'parent-confirmed', 'android-map:phone-parent-confirmed');
  ok(await aInternet.getAttribute('data-evidence-state') === 'verified', 'android-map:internet-verified');
  ok(await aService.getAttribute('data-evidence-state') === 'not-covered', 'android-map:service-not-covered');
  ok((await page.locator('body').innerText()).includes('evidence map, not a safety score'), 'android-map:no-safety-score');

  await page.locator('[data-action="REMOVE_DNS"]').click();
  await screen(page, 'removal', 'android-removal');
  ok((await page.locator('body').innerText()).includes('restoring the platform’s normal Automatic policy'), 'android-removal:instructions');
  ok((await page.locator('body').innerText()).includes('Do not silently fall back to plaintext'), 'android-removal:no-false-protection');
  await page.locator('[data-action="CONFIRM_REMOVED"]').click();
  await screen(page, 'recovery', 'android-recovery');
  await page.locator('[data-action="RECOVERY_OK"]').click();
  await screen(page, 'map', 'android-recovery-map');
  const rInternet = page.locator('.sw-status').filter({ hasText: 'Internet' });
  ok(await rInternet.getAttribute('data-evidence-state') === 'removed', 'android-recovery:internet-remains-removed');
  ok((await rInternet.innerText()).includes('Removed'), 'android-recovery:removed-label');

  await reset(page, 'iphone-reset');
  await start(page, 'iphone', 'NATIVE_ACTION_NEEDED', 'iphone-success');
  ok((await page.locator('.prototype-code').innerText()).trim() === 'https://dns.usesafeweb.com/dns-query', 'iphone:exact-doh-url');
  ok((await page.locator('body').innerText()).includes('does not distribute or fabricate a'), 'iphone:no-fabricated-profile');
  await configureAndVerify(page, 'verified', 'iphone-success');
  await screen(page, 'service', 'iphone-success:service');
  await page.locator('[data-action="SERVICE_CONFIRMED"]').click();
  await screen(page, 'map', 'iphone-success:map');
  const iPhone = page.locator('.sw-status').filter({ hasText: 'Phone' });
  const iInternet = page.locator('.sw-status').filter({ hasText: 'Internet' });
  const iService = page.locator('.sw-status').filter({ hasText: 'Service' });
  ok(await iPhone.getAttribute('data-evidence-state') === 'action-needed', 'iphone-map:phone-action-needed-preserved');
  ok(await iInternet.getAttribute('data-evidence-state') === 'verified', 'iphone-map:internet-verified');
  ok(await iService.getAttribute('data-evidence-state') === 'parent-confirmed', 'iphone-map:service-parent-confirmed');

  await reset(page, 'unsupported-reset');
  await start(page, 'other', 'NATIVE_CONFIRMED', 'unsupported');
  ok((await page.locator('body').innerText()).includes('not given speculative client workarounds'), 'unsupported:no-speculative-workaround');
  ok(await page.locator('[data-action="REMOVE_DNS"]').count() === 0, 'unsupported:no-removal-for-unconfigured-route');

  await reset(page, 'negative-path-reset');
  await start(page, 'android', 'NATIVE_ACTION_NEEDED', 'negative-action-needed');
  await configureAndVerify(page, 'action-needed', 'negative-action-needed');
  await screen(page, 'troubleshooting', 'negative-action-needed:troubleshooting');
  ok((await page.locator('h1').innerText()).trim() === 'Action needed', 'negative-action-needed:label');
  ok(await page.locator('[data-action="RETRY_AFTER_CHANGE"]').count() === 1, 'negative-action-needed:retry-offered');
  await page.locator('[data-action="RETRY_AFTER_CHANGE"]').click();
  await screen(page, 'verify', 'negative-action-needed:retry');
  await page.locator('[data-action="VERIFY_RESULT"][data-result="uncertain"]').click();
  await screen(page, 'troubleshooting', 'negative-uncertain');
  ok((await page.locator('h1').innerText()).trim() === 'Status uncertain', 'negative-uncertain:label');
  await page.locator('[data-action="RETRY_AFTER_CHANGE"]').click();
  await screen(page, 'verify', 'negative-uncertain:retry');
  await page.locator('[data-action="VERIFY_RESULT"][data-result="not-covered"]').click();
  await screen(page, 'limitations', 'negative-not-covered');
  ok(await page.locator('[data-action="REMOVE_DNS"]').count() === 1, 'negative-not-covered:removal-available-for-configured-route');

  await reset(page, 'responsive-reset');
  await page.setViewportSize({ width: 1280, height: 800 });
  await screen(page, 'discovery', 'desktop-discovery');
  const frame = await page.locator('.prototype-frame').boundingBox();
  ok(frame && frame.width <= 514, 'desktop:bounded-frame-width', `${frame?.width}`);
  await start(page, 'android', 'NATIVE_CONFIRMED', 'desktop-android');
  await configureAndVerify(page, 'verified', 'desktop-android');
  await screen(page, 'service', 'desktop-android:service');
  await page.locator('[data-action="SERVICE_NONE"]').click();
  await screen(page, 'map', 'desktop-map');
  const cols = await page.locator('.prototype-map').evaluate(el => getComputedStyle(el).gridTemplateColumns.split(' ').filter(Boolean).length);
  ok(cols === 3, 'desktop:three-column-protection-map', `${cols}`);

  const resourceHosts = await page.evaluate(() => performance.getEntriesByType('resource').map(e => new URL(e.name).hostname));
  ok(resourceHosts.every(h => h === '127.0.0.1' || h === 'localhost'), 'privacy:resources-local-only', resourceHosts.join(','));
  await assertStorageEmpty(page, 'final');
  ok(externalRequests.length === 0, 'privacy:no-external-page-requests');
  ok(consoleErrors.length === 0, 'runtime:no-console-errors', consoleErrors.join(' | '));
  ok(pageErrors.length === 0, 'runtime:no-page-errors', pageErrors.join(' | '));

  await context.close();
  await browser.close();
  browser = undefined;
  console.log(`BROWSER_ACCEPTANCE_CHECKS=${passed.length}`);
  console.log('BROWSER_ACCEPTANCE=PASS');
} catch (error) {
  console.error(`BROWSER_ACCEPTANCE=FAIL\n${error?.stack || error}`);
  if (browser) await browser.close().catch(() => {});
  process.exitCode = 1;
}
