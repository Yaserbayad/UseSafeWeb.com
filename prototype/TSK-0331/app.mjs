const view = document.querySelector('#state-view');
const title = document.querySelector('#page-title');
const live = document.querySelector('#live-status');

const params = new URLSearchParams(location.search);
const lang = ['en', 'tr', 'ar'].includes(params.get('lang')) ? params.get('lang') : 'en';
document.documentElement.lang = lang;
document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';

const pageTitles = {
  en: 'Manage safely',
  tr: 'Güvenle yönetin',
  ar: 'إدارة آمنة',
};

function button(label, state, cls = '', disabled = false) {
  return `<button class="${cls}" data-state="${state}"${disabled ? ' disabled' : ''}>${label}</button>`;
}
function status(label, tone = '') {
  return `<span class="status ${tone}">${label}</span>`;
}
function actions(primary, secondary = '') {
  return `<div class="actions">${primary}${secondary}${button('Help', 'recovery')}</div>`;
}
function consequence(items) {
  return `<ul class="summary">${items.map(([label, value]) => `<li><strong>${label}</strong><span>${value}</span></li>`).join('')}</ul>`;
}

const states = {
  account: () => `<div class="grid two">
    <section class="card"><h2>Account</h2><p class="muted">Account access is optional. Core setup and protection remain available without login.</p>${consequence([
      ['Account access', 'Signed in'],
      ['Physical protection', 'Unchanged by account actions'],
      ['Anonymous J0/J1', 'Separate lifecycle']
    ])}${actions(button('Delete account', 'delete-entry', 'danger'), button('Log out', 'session-expired'))}</section>
    <section class="card"><h2>Devices</h2><p>Manage saved device records separately from physical UseSafeWeb protection.</p>${button('Open device', 'device', 'primary')}</section>
  </div>`,

  'delete-entry': () => `<section class="card danger-zone"><h2>Delete your account</h2><p>This starts removal of your UseSafeWeb account and account-owned management data. It does not remove UseSafeWeb protection from physical devices.</p>${consequence([
    ['Will be targeted for deletion', 'Account record, account-owned saved device records, account management associations, account-scoped settings and active sessions under the owning deletion contract'],
    ['Not implied deleted', 'Physical UseSafeWeb configuration and unrelated anonymous J0/J1 state'],
    ['Retention', 'Any future required limited retention must come from the owning approved data/legal contract; no period is invented here']
  ])}${actions(button('Continue', 'delete-confirm', 'danger'), button('Cancel', 'account'))}</section>`,

  'delete-confirm': () => `<section class="card danger-zone"><h2>Permanently delete your UseSafeWeb account?</h2><div class="notice danger"><strong>Confirm the consequence</strong><ul class="check-list"><li>Account and account-owned saved device records will be removed under the approved deletion process.</li><li>Signed-in account access will end.</li><li>Physical UseSafeWeb protection is separate and will not be removed.</li><li>Anonymous J0/J1 state remains on its own expiry/deletion lifecycle.</li></ul></div>${actions(button('Delete account', 'delete-pending', 'danger'), button('Cancel', 'account'))}</section>`,

  'delete-pending': () => `<section class="card"><h2>Deleting account — result being confirmed</h2><p aria-busy="true">Do not submit the deletion again while the result is pending.</p>${status('Pending', 'warning')}<p class="prototype-note">Prototype outcome controls exercise confirmed success, confirmed failure and unknown-result recovery.</p><div class="actions">${button('Confirmed success', 'delete-success')}${button('Confirmed failure', 'delete-failed')}${button('Result unknown', 'delete-unknown')}${button('Help', 'recovery')}</div></section>`,

  'delete-success': () => `<section class="card"><h2>Account deleted</h2><p>The account-domain deletion is confirmed. Physical UseSafeWeb protection on devices is unchanged and can be removed separately.</p>${consequence([
    ['Deleted', 'UseSafeWeb account and account-owned management data according to the owning deletion contract'],
    ['Retained/unchanged by this result', 'Physical device protection; unrelated J0/J1 state; only any separately approved limited retention if applicable']
  ])}${actions(button('Continue without account', 'recovery', 'primary'), button('Physical removal options', 'remove-protection-confirm'))}</section>`,

  'delete-failed': () => `<section class="card"><h2>Account was not deleted</h2><div class="notice warning"><strong>No completion claim</strong><p>The deletion failed. Known account state is preserved until a safe corrected retry or recovery.</p></div>${actions(button('Review recovery', 'recovery', 'primary'), button('Back to account', 'account'))}</section>`,

  'delete-unknown': () => `<section class="card"><h2>We could not confirm whether the account was deleted</h2><div class="notice warning"><strong>Result unknown</strong><p>Another destructive request is blocked until authoritative account state is checked. There is no automatic replay.</p></div>${actions(button('Check account status', 'recovery', 'primary'), button('Delete account again', 'delete-pending', '', true))}</section>`,

  device: () => `<div class="grid two"><section class="card"><h2>Family iPhone</h2><p class="muted">Saved device record. Record presence is not technical verification.</p>${consequence([
    ['Management link', 'Active'],
    ['Protection reference', 'Current technical state is owned by the Protection Map verifier'],
    ['Account action effect', 'Does not change physical protection by itself']
  ])}${actions(button('Unlink device', 'unlink-confirm'), button('Remove from dashboard', 'remove-record-confirm', 'danger'))}</section><section class="card"><h2>Physical device actions</h2><div class="stack">${button('Remove UseSafeWeb protection', 'remove-protection-confirm', 'danger')}${button('Reinstall or reconfigure', 'reconfigure')}${button('Replace device', 'replace-confirm')}</div></section></div>`,

  'unlink-confirm': () => `<section class="card"><h2>Unlink this device?</h2><p>Unlinking ends this account's management link. It does not remove UseSafeWeb protection from the physical device.</p>${actions(button('Unlink device', 'unlink-pending', 'danger'), button('Cancel', 'device'))}</section>`,

  'unlink-pending': () => `<section class="card"><h2>Unlink result being confirmed</h2><p>Duplicate unlink is disabled while the current result is unresolved.</p><div class="actions">${button('Confirmed success', 'unlink-success')}${button('Result unknown', 'unlink-unknown')}${button('Help', 'recovery')}</div></section>`,

  'unlink-success': () => `<section class="card"><h2>Device unlinked</h2><p>The account-to-device management link is removed. Physical UseSafeWeb protection is unchanged.</p>${actions(button('Back to devices', 'device', 'primary'), button('Remove physical protection separately', 'remove-protection-confirm'))}</section>`,

  'unlink-unknown': () => `<section class="card"><h2>We could not confirm the unlink result</h2><p>Authoritative association state must be resolved before another unlink attempt. No automatic replay is allowed.</p>${actions(button('Check current link', 'recovery', 'primary'), button('Unlink again', 'unlink-pending', '', true))}</section>`,

  'remove-record-confirm': () => `<section class="card danger-zone"><h2>Remove this device from your dashboard?</h2><p>Removing this saved device record does not remove UseSafeWeb protection from the physical device.</p>${actions(button('Remove from dashboard', 'remove-record-success', 'danger'), button('Cancel', 'device'))}</section>`,

  'remove-record-success': () => `<section class="card"><h2>Removed from dashboard</h2><p>The selected saved device record is deleted. Physical UseSafeWeb protection is unchanged.</p>${actions(button('Back to devices', 'device', 'primary'), button('Remove physical protection separately', 'remove-protection-confirm'))}</section>`,

  'remove-protection-confirm': () => `<section class="card danger-zone"><h2>Remove UseSafeWeb protection from this device?</h2><p>This is the separate physical-device removal flow. When the owning removal check confirms success, the active UseSafeWeb protection claim is withdrawn.</p>${actions(button('Confirm physical removal', 'remove-protection-success', 'danger'), button('Cancel', 'device'))}</section>`,

  'remove-protection-success': () => `<section class="card"><h2>UseSafeWeb protection removed</h2><p>Physical removal is confirmed. The account and saved dashboard record remain unchanged unless you separately remove them.</p>${consequence([['Physical protection', 'Removed'], ['Saved device record', 'Unchanged'], ['Account', 'Unchanged']])}${actions(button('Set up again', 'reconfigure', 'primary'), button('Back to device', 'device'))}</section>`,

  reconfigure: () => `<section class="card"><h2>Reinstall or reconfigure</h2><p>Start a fresh supported setup. Earlier protection evidence may no longer be current and will not be silently retained.</p><div class="notice"><strong>Verification required</strong><p>A new Verified state requires the owning current technical check. Partial failure routes to Help with a truthful Needs attention, Status uncertain or Not covered state.</p></div>${actions(button('Start fresh setup', 'device', 'primary'), button('Cancel', 'device'))}</section>`,

  'replace-confirm': () => `<section class="card"><h2>Replace this device?</h2><p>The new device starts independently. The old device record and protection state are not silently copied.</p>${actions(button('Start replacement', 'replace-new', 'primary'), button('Cancel', 'device'))}</section>`,

  'replace-new': () => `<section class="card"><h2>New replacement device</h2><p>This device starts with a fresh unverified status. It inherits no Verified or parent-confirmed state and no browsing/query/activity history.</p>${consequence([['New protection state', 'Not yet verified'], ['Old device', 'Unchanged until a separate lifecycle action'], ['History', 'Not copied or stored by this product flow']])}${actions(button('Continue setup', 'reconfigure', 'primary'), button('Back to devices', 'device'))}</section>`,

  'session-expired': () => `<section class="card"><h2>Sign in again to manage your account</h2><p>Your account session ended. Any destructive action was stopped and was not automatically repeated. Physical protection truth is unchanged.</p>${actions(button('Continue with Google', 'account', 'primary'), button('Continue without account', 'recovery'))}</section>`,

  'provider-error': () => `<section class="card"><h2>Account access is unavailable</h2><p>A provider failure affects account-only access. It does not alter current physical protection truth.</p>${actions(button('Try account access later', 'account', 'primary'), button('Continue without account', 'recovery'))}</section>`,

  'ownership-mismatch': () => `<section class="card"><h2>This saved device cannot be managed from this account</h2><p>Ownership mismatch fails closed. No other account identity, device detail or internal authorization data is exposed.</p>${actions(button('Back to my devices', 'device', 'primary'), button('Start setup without account', 'recovery'))}</section>`,

  recovery: () => `<section class="card"><h2>Check current state before retrying</h2><p>Safe recovery reads the authoritative current account/device operation state first, then classifies confirmed success, confirmed failure, pending or unknown.</p>${consequence([
    ['Retry rule', 'Retry only after the previous result is known and the retry is safe/idempotent'],
    ['Protection rule', 'Account/device recovery never infers a physical protection change'],
    ['Privacy', 'No browsing/query/activity history, raw DNS log, child identity or provider secret is requested']
  ])}${actions(button('Back to account', 'account', 'primary'), button('Back to device', 'device'))}</section>`,
};

function stateFromHash() {
  const key = location.hash.replace(/^#/, '') || 'account';
  return states[key] ? key : 'account';
}

function render({ focus = false } = {}) {
  const key = stateFromHash();
  title.textContent = pageTitles[lang];
  view.innerHTML = states[key]();
  view.dataset.state = key;
  live.textContent = `Lifecycle state: ${key.replaceAll('-', ' ')}`;
  if (focus) {
    const heading = view.querySelector('h2');
    if (heading) {
      heading.tabIndex = -1;
      heading.focus();
    }
  }
}

document.addEventListener('click', event => {
  const control = event.target.closest('[data-state]');
  if (!control || control.disabled) return;
  const next = control.dataset.state;
  if (!states[next]) return;
  if (location.hash === `#${next}`) render({ focus: true });
  else location.hash = next;
});

window.addEventListener('hashchange', () => {
  const key = location.hash.replace(/^#/, '');
  if (states[key]) render({ focus: true });
});

render();
