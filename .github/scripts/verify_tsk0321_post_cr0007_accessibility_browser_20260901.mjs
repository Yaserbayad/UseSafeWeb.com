import { createRequire } from 'module';

const require = createRequire(import.meta.url);
const playwrightModule = process.env.TSK0321_PLAYWRIGHT_MODULE || 'playwright';
const axeModule = process.env.TSK0321_AXE_MODULE || 'axe-core';
const { chromium } = require(playwrightModule);
const axe = require(axeModule);
const base = process.env.TSK0321_BASE_URL || 'http://127.0.0.1:8033/prototype/TSK-0333/index.html';

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 320, height: 900 } });
const errors = [];
const external = [];
let checks = 0;
const auditedScreens = new Set();

page.on('console', m => { if (m.type() === 'error') errors.push(`console:${m.text()}`); });
page.on('pageerror', e => errors.push(`page:${e.message}`));
page.on('request', r => {
  const u = new URL(r.url());
  if (!['127.0.0.1', 'localhost'].includes(u.hostname)) external.push(r.url());
});

function req(condition, message) {
  checks += 1;
  if (!condition) throw new Error(message);
}

async function dispatch(action, payload = {}) {
  await page.evaluate(({ action, payload }) => window.__TSK0333_TEST__.dispatch(action, payload), { action, payload });
}

async function reset() { await dispatch('RESET'); }

async function currentState() { return page.evaluate(() => window.__TSK0333_TEST__.getState()); }

async function axeAudit(label) {
  const result = await page.evaluate(async () => {
    return axe.run(document, {
      runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'] },
      resultTypes: ['violations']
    });
  });
  req(result.violations.length === 0, `${label}:axe:${result.violations.map(v => `${v.id}:${v.nodes.length}`).join(',')}`);
}

async function auditCurrent(label, expectedScreen, { expectHeadingFocus = true } = {}) {
  const state = await currentState();
  req(state.screen === expectedScreen, `${label}:state-screen:${state.screen}`);
  req(await page.locator(`[data-testid="screen-${expectedScreen}"]`).isVisible(), `${label}:screen-visible`);
  req(await page.locator('#main-content').getAttribute('aria-live') === 'off', `${label}:main-live-not-off`);
  req(await page.locator('#prototype-announcer').getAttribute('aria-live') === 'polite', `${label}:announcer-live`);
  req((await page.locator('#prototype-announcer').textContent()).includes(expectedScreen), `${label}:announcer-current-screen`);
  req(await page.locator('h1').count() === 1, `${label}:h1-count`);
  const h1Text = (await page.locator('h1').textContent())?.trim();
  req(Boolean(h1Text), `${label}:h1-empty`);
  if (expectHeadingFocus) req(await page.locator('h1').evaluate(el => el === document.activeElement), `${label}:h1-focus`);
  req(await page.locator('[tabindex]:not([tabindex="-1"]):not([tabindex="0"])').count() === 0, `${label}:positive-tabindex`);

  const duplicateIds = await page.evaluate(() => {
    const ids = [...document.querySelectorAll('[id]')].map(el => el.id);
    return ids.filter((id, i) => ids.indexOf(id) !== i);
  });
  req(duplicateIds.length === 0, `${label}:duplicate-ids:${duplicateIds.join(',')}`);

  const interactive = page.locator('button:visible, a[href]:visible');
  const count = await interactive.count();
  req(count > 0, `${label}:no-interactive-controls`);
  for (let i = 0; i < count; i++) {
    const el = interactive.nth(i);
    const name = await el.getAttribute('aria-label') || (await el.textContent())?.trim();
    req(Boolean(name), `${label}:interactive-name:${i}`);
    const box = await el.boundingBox();
    req(Boolean(box), `${label}:interactive-box:${i}`);
    if (box) req(box.width >= 24 && box.height >= 24, `${label}:target-size:${i}:${box.width}x${box.height}`);
  }

  const overflow = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth + 1);
  req(!overflow, `${label}:horizontal-overflow`);

  const clippedCritical = await page.evaluate(() => [...document.querySelectorAll('h1,h2,p,li,button,a,code')].filter(el => {
    const s = getComputedStyle(el);
    if (s.display === 'none' || s.visibility === 'hidden') return false;
    return el.scrollWidth > el.clientWidth + 2 && ['hidden','clip'].includes(s.overflowX);
  }).map(el => el.textContent?.trim().slice(0,60)));
  req(clippedCritical.length === 0, `${label}:clipped-critical:${clippedCritical.join('|')}`);

  await axeAudit(label);
  auditedScreens.add(expectedScreen);
}

async function assertKeyboardCycle(label) {
  const focusables = await page.locator('button:visible, a[href]:visible').count();
  req(focusables > 1, `${label}:focusable-count`);
  for (let i = 0; i < focusables + 3; i++) await page.keyboard.press('Tab');
  const active = await page.evaluate(() => ({ tag: document.activeElement?.tagName, text: document.activeElement?.textContent?.trim(), id: document.activeElement?.id }));
  req(['BUTTON','A'].includes(active.tag), `${label}:focus-trap:${JSON.stringify(active)}`);
}

async function auditWidths(label) {
  for (const width of [320, 768, 1024, 1440]) {
    await page.setViewportSize({ width, height: 900 });
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth + 1);
    req(!overflow, `${label}:width-${width}-overflow`);
  }
  await page.setViewportSize({ width: 320, height: 900 });
}

async function auditTextResize(label) {
  await page.evaluate(() => { document.documentElement.style.fontSize = '200%'; });
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth + 1);
  req(!overflow, `${label}:200pct-overflow`);
  const visibleActions = await page.locator('.prototype-actions button:visible').count();
  req(visibleActions > 0, `${label}:200pct-actions-lost`);
  await page.evaluate(() => { document.documentElement.style.fontSize = ''; });
}

await page.goto(base, { waitUntil: 'networkidle' });
await page.addScriptTag({ content: axe.source });
req(await page.locator('#skip-link').isVisible().catch(() => false) === false, 'skip-link-should-be-visually-hidden-before-focus');
await page.keyboard.press('Tab');
req(await page.locator('#skip-link').evaluate(el => el === document.activeElement), 'skip-link-first-focus');
req(await page.locator('#skip-link').isVisible(), 'skip-link-visible-on-focus');
await page.keyboard.press('Enter');
req(await page.locator('#main-content').evaluate(el => el === document.activeElement), 'skip-link-target-main');
console.log('TSK0321_SKIP_LINK=PASS');

await reset(); await auditCurrent('home', 'home');
await dispatch('SIMULATE_LOST_STATE'); await auditCurrent('reset-lost', 'reset-lost');
await reset(); await dispatch('START'); await auditCurrent('router', 'router');
await dispatch('CHOOSE_PLATFORM', { platform: 'android' }); await auditCurrent('native-android', 'native');
await dispatch('NATIVE_CONFIRMED'); await auditCurrent('dns-android', 'dns');
await dispatch('DNS_CONFIGURED'); await auditCurrent('verify-android', 'verify');
await dispatch('VERIFY_RESULT', { result: 'verified' }); await auditCurrent('service', 'service');
await dispatch('SERVICE_NONE'); await auditCurrent('map-accountless', 'map');
const mapLabels = await page.locator('.prototype-state-label').allTextContents();
req(mapLabels.includes('Verified') && mapLabels.includes('You confirmed this is set up') && mapLabels.includes('Not covered'), `map-text-states:${mapLabels.join('|')}`);
req(await page.getByText('This is an evidence map, not a safety score. One layer never certifies another.').isVisible(), 'map-no-score-text');
console.log('TSK0321_ACCOUNTLESS_CORE_STATES=PASS');

await dispatch('OPEN_TROUBLESHOOT'); await auditCurrent('troubleshoot', 'troubleshoot');
await reset(); await dispatch('START'); await dispatch('CHOOSE_PLATFORM', { platform: 'other' }); await auditCurrent('limits-unsupported', 'limits');
await reset(); await dispatch('START'); await dispatch('CHOOSE_PLATFORM', { platform: 'android' }); await dispatch('NATIVE_CONFIRMED'); await dispatch('DNS_CONFIGURED'); await dispatch('VERIFY_RESULT', { result: 'verified' }); await dispatch('SERVICE_NONE');
await dispatch('OPEN_FALSE_POSITIVE'); await auditCurrent('false-positive', 'false-positive');
await dispatch('RETURN'); await dispatch('OPEN_HELP'); await auditCurrent('help', 'help');
await dispatch('RETURN'); await dispatch('REMOVE_DNS'); await auditCurrent('remove', 'remove');
await dispatch('CONFIRM_REMOVED'); await auditCurrent('recovery', 'recovery');
console.log('TSK0321_SUPPORT_REMOVAL_RECOVERY=PASS');

await reset(); await dispatch('START'); await dispatch('CHOOSE_PLATFORM', { platform: 'iphone' }); await dispatch('NATIVE_CONFIRMED'); await auditCurrent('dns-iphone', 'dns');
await page.evaluate(() => window.__TSK0333_TEST__.toggleRtl());
req(await page.locator('html').getAttribute('dir') === 'rtl', 'rtl-dir');
for (const id of ['iphone-doh-value']) {
  const style = await page.getByTestId(id).evaluate(el => ({ direction: getComputedStyle(el).direction, unicodeBidi: getComputedStyle(el).unicodeBidi }));
  req(style.direction === 'ltr', `${id}:rtl-direction`);
}
await page.evaluate(() => window.__TSK0333_TEST__.toggleRtl());
console.log('TSK0321_RTL_TECHNICAL_VALUES=PASS');

await reset(); await dispatch('OPEN_ACCOUNT_ENTRY'); await auditCurrent('account-entry', 'account-entry');
req(await page.getByRole('button', { name: 'Continue without account' }).isVisible(), 'account-entry-accountless-fallback');
await dispatch('START_GOOGLE_SIGNIN', { mode: 'new' }); await auditCurrent('provider-pending-new', 'provider-pending');
await dispatch('PROVIDER_SUCCESS_NEW'); await auditCurrent('first-session', 'first-session');
await dispatch('CREATE_ACCOUNT'); await auditCurrent('dashboard-new', 'dashboard');
req(await page.getByTestId('dashboard-empty').isVisible(), 'dashboard-new-empty');
console.log('TSK0321_NEW_ACCOUNT_STATES=PASS');

await reset(); await dispatch('OPEN_ACCOUNT_ENTRY'); await dispatch('START_GOOGLE_SIGNIN', { mode: 'returning' }); await auditCurrent('provider-pending-returning', 'provider-pending');
await dispatch('PROVIDER_ERROR'); await auditCurrent('account-error', 'account-error');
req(await page.getByRole('button', { name: 'Start setup' }).isVisible(), 'account-error-core-fallback');
await dispatch('START'); req((await currentState()).screen === 'router', 'account-error-fallback-routes-core');
console.log('TSK0321_PROVIDER_ERROR_FALLBACK=PASS');

await reset(); await dispatch('OPEN_ACCOUNT_ENTRY'); await dispatch('START_GOOGLE_SIGNIN', { mode: 'returning' }); await dispatch('PROVIDER_SUCCESS_RETURNING'); await auditCurrent('dashboard-returning', 'dashboard');
req(await page.getByText('Saved record presence is not technical verification.').isVisible(), 'dashboard-record-not-verification');
await dispatch('OPEN_DEVICE'); await auditCurrent('device-detail', 'device-detail');
req(await page.getByText('Account ownership and saved-record presence do not establish current protection.').isVisible(), 'device-detail-record-not-verification');
await dispatch('OPEN_MANAGE'); await auditCurrent('device-manage', 'device-manage');
await assertKeyboardCycle('device-manage-keyboard');
console.log('TSK0321_DASHBOARD_DEVICE_STATES=PASS');

for (const lifecycle of [
  ['REPLACE_DEVICE','Replace saved device'],
  ['REVOKE_DEVICE','Revoke / unlink saved device'],
  ['DELETE_DEVICE_RECORD','Delete saved dashboard record']
]) {
  await reset(); await dispatch('OPEN_ACCOUNT_ENTRY'); await dispatch('START_GOOGLE_SIGNIN', { mode: 'returning' }); await dispatch('PROVIDER_SUCCESS_RETURNING'); await dispatch('OPEN_DEVICE'); await dispatch('OPEN_MANAGE');
  await dispatch(lifecycle[0]); await auditCurrent(`lifecycle-confirm-${lifecycle[0].toLowerCase()}`, 'lifecycle-confirm');
  req(await page.getByRole('heading', { level: 1, name: lifecycle[1] }).isVisible(), `${lifecycle[0]}:confirmation-heading`);
  req(await page.getByRole('button', { name: 'Confirm action' }).isVisible(), `${lifecycle[0]}:confirm-control`);
  await dispatch('SIMULATE_LIFECYCLE_UNKNOWN'); await auditCurrent(`lifecycle-unknown-${lifecycle[0].toLowerCase()}`, 'lifecycle-unknown');
  req(await page.getByText(/No automatic replay is allowed/i).isVisible(), `${lifecycle[0]}:unknown-no-replay-copy`);
  req(await page.locator('[data-action="CONFIRM_LIFECYCLE"]').count() === 0, `${lifecycle[0]}:unknown-repeat-confirm-present`);
}
console.log('TSK0321_DEVICE_DESTRUCTIVE_LIFECYCLE=PASS');

await reset(); await dispatch('OPEN_ACCOUNT_ENTRY'); await dispatch('START_GOOGLE_SIGNIN', { mode: 'returning' }); await dispatch('PROVIDER_SUCCESS_RETURNING');
await dispatch('EXPIRE_SESSION'); await auditCurrent('reauth', 'reauth');
req(await page.getByRole('button', { name: 'Start setup without account' }).isVisible(), 'reauth-core-fallback');
await dispatch('START'); req((await currentState()).screen === 'router', 'reauth-core-fallback-route');
console.log('TSK0321_SESSION_EXPIRY_FALLBACK=PASS');

await reset(); await dispatch('OPEN_ACCOUNT_ENTRY'); await dispatch('START_GOOGLE_SIGNIN', { mode: 'returning' }); await dispatch('PROVIDER_SUCCESS_RETURNING'); await dispatch('OPEN_ACCOUNT'); await auditCurrent('account', 'account');
await dispatch('LOGOUT'); await auditCurrent('logout-pending', 'logout-pending');
req(await page.getByText(/does not remove SafeWeb from the device/i).isVisible(), 'logout-physical-separation');
await reset(); await dispatch('OPEN_ACCOUNT_ENTRY'); await dispatch('START_GOOGLE_SIGNIN', { mode: 'returning' }); await dispatch('PROVIDER_SUCCESS_RETURNING'); await dispatch('OPEN_ACCOUNT'); await dispatch('OPEN_DELETE_ACCOUNT'); await auditCurrent('delete-entry', 'delete-entry');
await dispatch('CONFIRM_ACCOUNT_DELETE'); await auditCurrent('lifecycle-confirm-account-delete', 'lifecycle-confirm');
req(await page.getByRole('heading', { level: 1, name: 'Delete account' }).isVisible(), 'account-delete-confirm-heading');
req(await page.getByText(/physical protection and J0\/J1 are separate/i).isVisible(), 'account-delete-separation');
console.log('TSK0321_ACCOUNT_LIFECYCLE=PASS');

await reset(); await dispatch('OPEN_DATA_USE'); await auditCurrent('data-use', 'data-use');
const privacy = (await page.locator('body').innerText()).toLowerCase();
for (const phrase of ['no browsing history', 'activity history', 'no raw dns history', 'no child profile', 'no broad dns administration']) req(privacy.includes(phrase), `privacy:${phrase}`);
console.log('TSK0321_PRIVACY_CONTENT=PASS');

// Responsive + 200% text checks on representative high-density current screens.
await reset(); await auditWidths('home-responsive'); await auditTextResize('home-text-resize');
await reset(); await dispatch('OPEN_ACCOUNT_ENTRY'); await dispatch('START_GOOGLE_SIGNIN', { mode: 'returning' }); await dispatch('PROVIDER_SUCCESS_RETURNING'); await auditWidths('dashboard-responsive'); await auditTextResize('dashboard-text-resize');
await dispatch('OPEN_DEVICE'); await dispatch('OPEN_MANAGE'); await auditWidths('device-manage-responsive'); await auditTextResize('device-manage-text-resize');
await dispatch('REPLACE_DEVICE'); await auditWidths('lifecycle-confirm-responsive'); await auditTextResize('lifecycle-confirm-text-resize');
console.log('TSK0321_RESPONSIVE_TEXT_RESIZE=PASS');

await page.emulateMedia({ reducedMotion: 'reduce' });
const motion = await page.evaluate(() => {
  const el = document.querySelector('.prototype-screen'); const s = getComputedStyle(el);
  return { animation: s.animationDuration, transition: s.transitionDuration };
});
req(['0s','0.00001s'].includes(motion.animation) || parseFloat(motion.animation) <= 0.01, `reduced-motion-animation:${motion.animation}`);
req(['0s','0.00001s'].includes(motion.transition) || parseFloat(motion.transition) <= 0.01, `reduced-motion-transition:${motion.transition}`);
console.log('TSK0321_REDUCED_MOTION=PASS');

req(external.length === 0, `external-requests:${external.join(',')}`);
req(errors.length === 0, errors.join(';'));
const persisted = await page.evaluate(async () => ({ cookies: document.cookie, ls: Object.keys(localStorage), ss: Object.keys(sessionStorage), idb: await indexedDB.databases() }));
req(persisted.cookies === '' && persisted.ls.length === 0 && persisted.ss.length === 0 && persisted.idb.length === 0, 'browser-persistence-created');
console.log('TSK0321_NO_EXTERNAL_OR_PERSISTENCE=PASS');
console.log(`TSK0321_AUDITED_UNIQUE_SCREENS=${auditedScreens.size}`);
console.log(`TSK0321_ACCESSIBILITY_CHECKS=${checks}`);
console.log('TSK0321_POST_CR0007_MECHANICAL_ACCESSIBILITY_REVIEW=PASS');
await browser.close();
