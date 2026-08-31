import { createRequire } from 'module';

const require = createRequire(import.meta.url);
const playwrightModule = process.env.TSK0331_PLAYWRIGHT_MODULE || 'playwright';
const { chromium } = require(playwrightModule);
const base = process.env.TSK0331_BASE_URL || 'http://127.0.0.1:8031/prototype/TSK-0331/index.html';

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 320, height: 900 } });
const errors = [];
page.on('console', msg => { if (msg.type() === 'error') errors.push(`console:${msg.text()}`); });
page.on('pageerror', err => errors.push(`page:${err.message}`));

function req(condition, message) {
  if (!condition) throw new Error(message);
}
async function state() {
  return page.locator('#state-view').getAttribute('data-state');
}
async function goto(hash, query = '') {
  await page.goto(`${base}${query}#${hash}`, { waitUntil: 'networkidle' });
  req((await state()) === hash, `state-${hash}`);
}

// Functional + rollback: explicit account deletion entry/confirmation/cancel/pending.
await goto('delete-entry');
req(await page.getByText('does not remove UseSafeWeb protection from physical devices').isVisible(), 'delete-entry-physical-separation');
await page.getByRole('button', { name: 'Continue', exact: true }).click();
await page.waitForFunction(() => document.querySelector('#state-view')?.dataset.state === 'delete-confirm');
req(await page.getByText('Confirm the consequence').isVisible(), 'delete-confirm-consequence');
await page.getByRole('button', { name: 'Cancel', exact: true }).click();
await page.waitForFunction(() => document.querySelector('#state-view')?.dataset.state === 'account');
req((await state()) === 'account', 'delete-cancel-rollback');

await goto('delete-confirm');
await page.getByRole('button', { name: 'Delete account', exact: true }).click();
await page.waitForFunction(() => document.querySelector('#state-view')?.dataset.state === 'delete-pending');
req(await page.getByText('Do not submit the deletion again while the result is pending.').isVisible(), 'pending-duplicate-protection');

// Unknown outcome: fail closed, authoritative recovery, no duplicate destructive action.
await goto('delete-unknown');
req(await page.getByText('There is no automatic replay.').isVisible(), 'unknown-no-replay');
req(await page.getByRole('button', { name: 'Delete account again' }).isDisabled(), 'unknown-delete-disabled');
await page.getByRole('button', { name: 'Check account status' }).click();
await page.waitForFunction(() => document.querySelector('#state-view')?.dataset.state === 'recovery');
req(await page.getByText('Retry only after the previous result is known').isVisible(), 'authoritative-recovery');

// Session expiry must never replay the destructive action after re-authentication.
await goto('session-expired');
req(await page.getByText('was not automatically repeated').isVisible(), 'session-no-auto-replay-copy');
await page.getByRole('button', { name: 'Continue with Google' }).click();
await page.waitForFunction(() => document.querySelector('#state-view')?.dataset.state === 'account');
req((await state()) === 'account', 'reauth-safe-account-return');

// Provider and ownership failures are account-only and fail closed.
await goto('provider-error');
req(await page.getByText('does not alter current physical protection truth').isVisible(), 'provider-protection-neutral');
req(await page.getByRole('button', { name: 'Continue without account' }).isVisible(), 'provider-accountless-exit');
await goto('ownership-mismatch');
req(await page.getByText('Ownership mismatch fails closed').isVisible(), 'ownership-fail-closed');
req(!(await page.locator('body').innerText()).toLowerCase().includes('other account email'), 'no-cross-account-identity');

// Device record deletion/unlink are distinct from physical removal.
await goto('remove-record-confirm');
req(await page.getByText('does not remove UseSafeWeb protection from the physical device').isVisible(), 'record-vs-physical');
await page.getByRole('button', { name: 'Remove from dashboard' }).click();
await page.waitForFunction(() => document.querySelector('#state-view')?.dataset.state === 'remove-record-success');
req(await page.getByText('Physical UseSafeWeb protection is unchanged.').isVisible(), 'record-delete-protection-unchanged');

await goto('unlink-confirm');
req(await page.getByText("does not remove UseSafeWeb protection from the physical device").isVisible(), 'unlink-vs-physical');
await page.getByRole('button', { name: 'Unlink device' }).click();
await page.waitForFunction(() => document.querySelector('#state-view')?.dataset.state === 'unlink-pending');
await page.getByRole('button', { name: 'Confirmed success' }).click();
await page.waitForFunction(() => document.querySelector('#state-view')?.dataset.state === 'unlink-success');
req(await page.getByText('Physical UseSafeWeb protection is unchanged.').isVisible(), 'unlink-protection-unchanged');

await goto('remove-protection-confirm');
await page.getByRole('button', { name: 'Confirm physical removal' }).click();
await page.waitForFunction(() => document.querySelector('#state-view')?.dataset.state === 'remove-protection-success');
req(await page.getByText('UseSafeWeb protection removed').isVisible(), 'physical-removal-confirmed');
req(await page.getByText('The account and saved dashboard record remain unchanged').isVisible(), 'physical-removal-account-record-unchanged');

// Reconfiguration and replacement must not carry stale/old truth forward.
await goto('reconfigure');
req(await page.getByText('Earlier protection evidence may no longer be current').isVisible(), 'reconfigure-stale-evidence');
req(await page.getByText('A new Verified state requires the owning current technical check').isVisible(), 'reconfigure-reverify');
await goto('replace-new');
req(await page.getByText('fresh unverified status').isVisible(), 'replacement-fresh-state');
req(await page.getByText('inherits no Verified or parent-confirmed state').isVisible(), 'replacement-no-inheritance');

// Confirmed account-deletion copy defines deleted/retained scope narrowly.
await goto('delete-success');
req(await page.getByText('Account deleted', { exact: true }).isVisible(), 'delete-success-heading');
req(await page.getByText('Physical UseSafeWeb protection on devices is unchanged').isVisible(), 'delete-success-protection-neutral');
req(await page.getByText('unrelated J0/J1 state').isVisible(), 'delete-success-j0j1-separate');

// Mobile / keyboard / accessibility: use the true default load, not a synthetic state hash.
await page.goto(base, { waitUntil: 'networkidle' });
req((await state()) === 'account', 'default-account-state');
let overflow = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth);
req(!overflow, 'horizontal-overflow-320');
await page.keyboard.press('Tab');
req(await page.locator('.skip-link').evaluate(el => el === document.activeElement), 'skip-link-first-focus');
await page.keyboard.press('Enter');
req(await page.locator('#main').evaluate(el => el === document.activeElement), 'skip-link-target');

// State navigation focus goes to the new state heading.
await goto('account');
await page.getByRole('button', { name: 'Delete account', exact: true }).click();
await page.waitForFunction(() => document.querySelector('#state-view')?.dataset.state === 'delete-entry');
req(await page.locator('#state-view h2').evaluate(el => el === document.activeElement), 'state-heading-focus');

// Responsive no-overflow contract.
for (const width of [320, 768, 1024, 1440]) {
  await page.setViewportSize({ width, height: 900 });
  await goto('device');
  overflow = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth);
  req(!overflow, `horizontal-overflow-${width}`);
}

// RTL preserves state semantics.
await page.setViewportSize({ width: 390, height: 900 });
await goto('delete-confirm', '?lang=ar');
req(await page.locator('html').getAttribute('dir') === 'rtl', 'rtl-dir');
req(await page.locator('html').getAttribute('lang') === 'ar', 'arabic-lang');
req(await page.getByRole('button', { name: 'Delete account', exact: true }).isVisible(), 'rtl-destructive-control');

// Privacy/scope audit of ordinary rendered surfaces.
for (const hash of ['account', 'device', 'delete-entry', 'recovery', 'ownership-mismatch']) {
  await goto(hash);
  const body = (await page.locator('body').innerText()).toLowerCase();
  for (const forbidden of ['top sites', 'raw adguard', 'provider password', 'child profile']) {
    req(!body.includes(forbidden), `forbidden-surface-${hash}-${forbidden}`);
  }
}

req(errors.length === 0, errors.join(';'));
console.log('TSK0331_BROWSER_FUNCTIONAL=PASS');
console.log('TSK0331_BROWSER_NEGATIVE_SECURITY=PASS');
console.log('TSK0331_BROWSER_CONFIGURATION_TRUTH=PASS');
console.log('TSK0331_BROWSER_PRIVACY=PASS');
console.log('TSK0331_BROWSER_ROLLBACK_RECOVERY=PASS');
console.log('TSK0331_BROWSER_RESPONSIVE=PASS');
console.log('TSK0331_BROWSER_KEYBOARD=PASS');
console.log('TSK0331_BROWSER_RTL=PASS');
console.log('TSK0331_BROWSER_NO_CONSOLE_ERRORS=PASS');
await browser.close();
