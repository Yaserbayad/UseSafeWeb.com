import { createPrototype, transition, stateCopy, SCREEN, EVIDENCE_STATE, INVARIANTS } from './model.mjs';

const app = document.querySelector('#app');
const main = document.querySelector('#main-content');
const announcer = document.querySelector('#prototype-announcer');
let state = createPrototype();
let initialRender = true;

const button = (label, action, attrs = '', secondary = false) =>
  `<button type="button" class="sw-button${secondary ? ' sw-button--secondary' : ''}" data-action="${action}" data-testid="action-${action.toLowerCase().replaceAll('_','-')}" data-event-key="${action.toLowerCase()}" ${attrs}>${label}</button>`;
const secondary = (label, action, attrs = '') => button(label, action, attrs, true);
const section = (id, kicker, title, body, actions = '') => `<section class="prototype-screen" data-screen="${id}" data-testid="screen-${id}">
  <header class="prototype-screen__header"><p class="sw-kicker">${kicker}</p><h1 tabindex="-1">${title}</h1></header>
  <div class="prototype-content">${body}</div>${actions ? `<div class="prototype-actions">${actions}</div>` : ''}
</section>`;
const callout = (title, body) => `<aside class="prototype-callout"><strong>${title}</strong><p>${body}</p></aside>`;
const privateNotice = () => `<p class="prototype-meta">Optional account continuity only. Core setup, verification, help, recovery and removal remain usable without login.</p>`;

function stateCard(layer, value) {
  const copy = stateCopy(value);
  return `<article class="prototype-state-card" data-testid="map-${layer.toLowerCase()}" data-evidence-state="${value}">
    <h2>${layer}</h2><p class="prototype-state-label">${copy.label}</p><p>${copy.supporting}</p>
  </article>`;
}

function renderHome() {
  return section('home','UseSafeWeb','Set up protection without creating an account',
    `<p>UseSafeWeb guides a parent through Phone, Internet and supported Services, then shows a truthful Protection Map.</p>
     ${callout('Core value never requires login','Start setup, verify, understand, troubleshoot, recover and remove UseSafeWeb while signed out. Sign in is optional continuity.')}
     <div class="prototype-grid"><article><h2>Accountless core</h2><p>No parent or child identity is required for the safety setup journey.</p></article><article><h2>Optional continuity</h2><p>Google sign-in can provide a small device dashboard without turning account presence into technical evidence.</p></article></div>`,
    button('Start setup','START') + secondary('Sign in with Google','OPEN_ACCOUNT_ENTRY') + secondary('Privacy boundaries','OPEN_DATA_USE'));
}

function renderRouter() {
  return section('router','Setup','Which phone are you setting up?',
    `<p>Choose the current supported device path. UseSafeWeb selects the approved DNS instructions; the parent does not choose a protocol.</p>`,
    button('Android','CHOOSE_PLATFORM','data-platform="android"') + button('iPhone','CHOOSE_PLATFORM','data-platform="iphone"') + secondary('Another or managed device','CHOOSE_PLATFORM','data-platform="other"'));
}

function renderNative() {
  const family = state.platform === 'iphone' ? 'Apple Screen Time / Content & Privacy Restrictions' : 'the current Android family safeguard';
  return section('native','Phone','Check the phone safeguard',
    `<p>Review ${family}. UseSafeWeb does not silently change platform controls.</p>${callout('Evidence boundary','Your confirmation becomes “You confirmed this is set up”, never technical “Verified”.')}`,
    button('I confirmed this is set up','NATIVE_CONFIRMED') + secondary('This still needs attention','NATIVE_ACTION_NEEDED'));
}

function renderDns() {
  const isAndroid = state.platform === 'android';
  const instruction = isAndroid
    ? `<ol><li>Open Android Private DNS.</li><li>Choose the provider-hostname option.</li><li>Enter <code data-testid="android-dns-value">dns.usesafeweb.com</code>.</li><li>Save and return.</li></ol>`
    : `<p>Use the approved iOS DNS profile flow. The exact DoH Server URL is <code data-testid="iphone-doh-value">https://dns.usesafeweb.com/dns-query</code>.</p>`;
  return section('dns',`Internet · ${isAndroid ? 'Android' : 'iPhone'}`,isAndroid ? 'Set Android Private DNS' : 'Use the approved DNS profile',
    `${instruction}<p>Configuration presence alone is not technical verification.</p>`,
    button('I completed this setting','DNS_CONFIGURED') + secondary('It was already configured','DNS_ALREADY_CONFIGURED'));
}

function renderVerify() {
  return section('verify','Internet verification','Check what current evidence proves',
    `<p>Only qualifying current technical evidence can produce <strong>Verified</strong>. These prototype controls are deterministic fixtures and send no data.</p>`,
    button('Verification succeeds','VERIFY_RESULT','data-result="verified"') + secondary('Known repair needed','VERIFY_RESULT','data-result="action-needed"') + secondary('Evidence uncertain','VERIFY_RESULT','data-result="uncertain"') + secondary('Not supported','VERIFY_RESULT','data-result="not-covered"'));
}

function renderService() {
  return section('service','Services','Add only an approved relevant service safeguard',
    `<p>Zero applicable services is valid. UseSafeWeb does not infer services from browsing history, activity history or raw DNS data.</p>`,
    button('No approved service applies','SERVICE_NONE') + secondary('Prototype one approved service','SERVICE_CONFIRMED'));
}

function renderMap() {
  const save = state.authStatus === 'signed-in' && !state.device.exists ? button('Save this device explicitly','SAVE_DEVICE_EXPLICIT') : '';
  return section('map','Protection Map','Current evidence, layer by layer',
    `<p data-testid="map-no-score">This is an evidence map, not a safety score. One layer never certifies another.</p>
     <div class="prototype-map">${stateCard('Phone',state.nativeState)}${stateCard('Internet',state.dnsState)}${stateCard('Service',state.serviceState)}</div>
     ${state.authStatus === 'signed-in' ? privateNotice() : '<p>You can exit here without signing in.</p>'}`,
    save + secondary('Blocked site or service','OPEN_FALSE_POSITIVE') + secondary('Help','OPEN_HELP') + secondary('Limitations','OPEN_LIMITS') + secondary('Optional account','OPEN_ACCOUNT_ENTRY'));
}

function renderTroubleshoot() {
  const canRetry = state.changedCondition;
  return section('troubleshoot','Troubleshoot','Use one safe changed-condition check',
    `<p>${stateCopy(state.dnsState).supporting}</p><p>Check only the relevant condition such as VPN, Private Relay, managed policy, captive portal or resolver conflict.</p>`,
    (!canRetry ? button('I changed the relevant condition','MARK_CONDITION_CHANGED') : button('Check again','RETRY_AFTER_CHANGE')) + (state.dnsConfigured ? secondary('Remove UseSafeWeb DNS','REMOVE_DNS') : '') + secondary('Back','RETURN'));
}

function renderFalsePositive() {
  return section('false-positive','Support','A legitimate site or service seems blocked',
    `<p>A content problem does not automatically change the DNS-path evidence state. A future support route may use only the single destination the parent identifies and minimum context.</p>${callout('Privacy','Do not request browsing history, activity history, raw DNS logs, child profile data, credentials or broad network dumps.')}`,
    (state.dnsConfigured ? secondary('Remove UseSafeWeb DNS','REMOVE_DNS') : '') + secondary('Back','RETURN'));
}

function renderHelp() {
  return section('help','Help','Choose the issue you are solving',
    `<p>Help is available signed out and never changes protection state by acknowledgement alone.</p>`,
    secondary('Setup or verification issue','OPEN_TROUBLESHOOT') + secondary('Blocked site or service','OPEN_FALSE_POSITIVE') + secondary('Limitations','OPEN_LIMITS') + secondary('Back','RETURN'));
}

function renderLimits() {
  return section('limits','Compatibility & limits','Know what is unsupported or uncertain',
    `<ul><li>Unsupported paths stop truthfully.</li><li>Managed controls, VPNs and resolver conflicts can make status uncertain.</li><li>Parent confirmation is not technical verification.</li><li>No whole-child safety claim or score is created.</li></ul>`,
    secondary('Back','RETURN'));
}

function renderRemove() {
  return section('remove','Removal','Remove UseSafeWeb DNS',
    `<p>Physical protection removal is separate from logout, account deletion, record deletion and revoke/unlink.</p>`,
    button('I completed physical DNS removal','CONFIRM_REMOVED'));
}

function renderRecovery() {
  return section('recovery','Recovery','Check ordinary connectivity after removal',
    `<p>Connectivity recovery does not restore UseSafeWeb verification. The Internet layer remains Removed until a new setup and qualifying verification occur.</p>`,
    button('Ordinary connectivity works','RECOVERY_OK') + secondary('Set up again','RECONFIGURE'));
}

function renderResetLost() {
  return section('reset-lost','Restart','The transient setup state is unavailable',
    `<p>UseSafeWeb does not reconstruct an earlier positive state from hidden persistence. Start cleanly.</p>`,button('Start again','START'));
}

function renderAccountEntry() {
  return section('account-entry','Optional account','Sign in only if you want continuity',
    `${privateNotice()}${callout('Google route','The prototype models the planned Google sign-in interaction. It does not implement provider architecture or collect a provider password.')}`,
    button('Sign in with Google','START_GOOGLE_SIGNIN','data-mode="returning"') + secondary('Prototype first account','START_GOOGLE_SIGNIN','data-mode="new"') + secondary('Continue without account','START'));
}

function renderSignIn() { return renderAccountEntry(); }

function renderProviderPending() {
  return section('provider-pending','Google sign-in','Resolve the provider result',
    `<p>Provider/session results affect account access only. They do not create, upgrade or remove physical protection.</p>`,
    state.providerMode === 'new'
      ? button('Provider succeeds · new parent','PROVIDER_SUCCESS_NEW') + secondary('Provider unavailable','PROVIDER_ERROR') + secondary('Cancel','PROVIDER_CANCEL')
      : button('Provider succeeds · returning parent','PROVIDER_SUCCESS_RETURNING') + secondary('Provider unavailable','PROVIDER_ERROR') + secondary('Cancel','PROVIDER_CANCEL'));
}

function renderFirstSession() {
  return section('first-session','First session','Create the minimum parent account explicitly',
    `<p>No saved device is created automatically. No J0/J1 setup state is imported, promoted, linked or extended.</p>${callout('Minimum identity','Provider-bound stable identity and internal account ID only as implementation necessities; email/display image are not required by this interaction contract.')}`,
    button('Create account','CREATE_ACCOUNT') + secondary('How data is used','OPEN_DATA_USE'));
}

function renderAccountError() {
  return section('account-error','Account access','Sign-in is unavailable',
    `<p>This is an account-only error. Core setup, verification, help, recovery and removal remain available signed out.</p>`,
    button('Retry Google sign-in','START_GOOGLE_SIGNIN','data-mode="returning"') + secondary('Start setup','START') + secondary('Help','OPEN_HELP'));
}

function deviceSummary() {
  if (!state.device.exists) return '<p data-testid="dashboard-empty">No saved devices yet. Saving is optional.</p>';
  const status = state.device.lastKnown ? 'Earlier result — check again to know current status' : 'No current verification result';
  return `<article class="prototype-device-card" data-testid="device-card"><h2>${state.device.nickname}</h2><p>${status}</p><p>Saved record presence is not technical verification.</p>${button('Open device','OPEN_DEVICE')}</article>`;
}

function renderDashboard() {
  return section('dashboard','Dashboard','Your devices',
    `${privateNotice()}${deviceSummary()}${callout('No surveillance','No browsing history, activity history, raw DNS logs, child profile, top-sites view or broad DNS administration is available.')}`,
    button('Add device','ADD_DEVICE') + secondary('Account','OPEN_ACCOUNT') + secondary('Start new setup','START') + secondary('Help','OPEN_HELP'));
}

function renderDeviceDetail() {
  return section('device-detail','Saved device',state.device.nickname,
    `<p>Account ownership and saved-record presence do not establish current protection.</p><div class="prototype-map">${stateCard('Phone',state.nativeState)}${stateCard('Internet',state.dnsState)}${stateCard('Service',state.serviceState)}</div>`,
    button('Check again','REVERIFY_DEVICE') + secondary('Manage','OPEN_MANAGE') + secondary('Blocked site or service','OPEN_FALSE_POSITIVE') + secondary('Dashboard','OPEN_DASHBOARD'));
}

function renderDeviceManage() {
  return section('device-manage','Manage device','Bounded device management',
    `<p>Each lifecycle action has a narrow consequence. Dashboard data actions do not claim physical protection removal.</p>`,
    button('Reverify','REVERIFY_DEVICE') + secondary('Reinstall / reconfigure','REINSTALL_DEVICE') + secondary('Replace device','REPLACE_DEVICE') + secondary('Revoke / unlink','REVOKE_DEVICE') + secondary('Delete saved record','DELETE_DEVICE_RECORD') + secondary('Physically remove UseSafeWeb DNS','REMOVE_DNS'));
}

function renderReauth() {
  return section('reauth','Session ended','Sign in again to restore account access',
    `<p>Session expiry does not change physical protection. No destructive action is automatically replayed after reauthentication.</p>`,
    button('Reauthenticate','REAUTHENTICATE') + secondary('Start setup without account','START'));
}

function renderAccount() {
  return section('account','Account','Parent account',
    `<p>Account access is optional. Logout ends the session only. Account deletion is separate from physical DNS removal and J0/J1 deletion.</p>`,
    secondary('Data use','OPEN_DATA_USE') + button('Logout','LOGOUT') + secondary('Delete account','OPEN_DELETE_ACCOUNT') + secondary('Dashboard','OPEN_DASHBOARD'));
}

function renderDataUse() {
  return section('data-use','Privacy','What this prototype does not collect',
    `<ul><li>No browsing history or activity history.</li><li>No raw DNS history or raw DNS logs.</li><li>No child profile or child identity.</li><li>No provider password/token.</li><li>No broad DNS administration.</li></ul><p>Anonymous J0/J1 state remains separate from account/device records.</p>`,
    secondary('Back','RETURN'));
}

function renderLogoutPending() {
  return section('logout-pending','Logout','End this account session?',
    `<p>Logging out does not remove UseSafeWeb from the device and does not alter physical protection evidence.</p>`,
    button('Confirm logout','CONFIRM_LOGOUT') + secondary('Back to account','OPEN_ACCOUNT'));
}

function renderDeleteEntry() {
  return section('delete-entry','Delete account','Delete the parent account?',
    `<p>Account deletion targets account-domain records defined by the owning deletion contract. It does not claim physical UseSafeWeb removal and does not delete unrelated anonymous J0/J1 state.</p>`,
    button('Continue to confirmation','CONFIRM_ACCOUNT_DELETE') + secondary('Back to account','OPEN_ACCOUNT'));
}

const lifecycleCopy = {
  'replace-device': ['Replace saved device','The replacement starts fresh and inherits no Verified or parent-confirmed protection state.'],
  'revoke-device': ['Revoke / unlink saved device','This changes the account-side association only; it does not remove physical UseSafeWeb DNS.'],
  'delete-device-record': ['Delete saved dashboard record','This removes the saved record only; it does not set physical protection to Removed.'],
  'account-delete': ['Delete account','This deletes account-domain data only after confirmed execution; physical protection and J0/J1 are separate.']
};

function renderLifecycleConfirm() {
  const [title,copy] = lifecycleCopy[state.pendingLifecycle] || ['Confirm lifecycle action','Review the consequence before continuing.'];
  return section('lifecycle-confirm','Confirmation',title,
    `<p>${copy}</p>${callout('Fail closed','If the result becomes unknown, do not repeat the destructive action. Resolve authoritative state first.')}`,
    button('Confirm action','CONFIRM_LIFECYCLE') + secondary('Simulate unknown result','SIMULATE_LIFECYCLE_UNKNOWN'));
}

function renderLifecycleUnknown() {
  return section('lifecycle-unknown','Unknown result','We could not confirm the destructive result',
    `<p>No automatic replay is allowed. Resolve authoritative account/device state before deciding whether another mutation is safe.</p>`,
    button('Resolve as applied','RESOLVE_UNKNOWN','data-result="applied"') + secondary('Resolve as not applied','RESOLVE_UNKNOWN','data-result="not-applied"'));
}

const renderers = {
  [SCREEN.HOME]: renderHome, [SCREEN.ROUTER]: renderRouter, [SCREEN.NATIVE]: renderNative, [SCREEN.DNS]: renderDns,
  [SCREEN.VERIFY]: renderVerify, [SCREEN.SERVICE]: renderService, [SCREEN.MAP]: renderMap, [SCREEN.TROUBLESHOOT]: renderTroubleshoot,
  [SCREEN.FALSE_POSITIVE]: renderFalsePositive, [SCREEN.HELP]: renderHelp, [SCREEN.LIMITS]: renderLimits, [SCREEN.REMOVE]: renderRemove,
  [SCREEN.RECOVERY]: renderRecovery, [SCREEN.RESET_LOST]: renderResetLost, [SCREEN.ACCOUNT_ENTRY]: renderAccountEntry,
  [SCREEN.SIGN_IN]: renderSignIn, [SCREEN.PROVIDER_PENDING]: renderProviderPending, [SCREEN.FIRST_SESSION]: renderFirstSession,
  [SCREEN.ACCOUNT_ERROR]: renderAccountError, [SCREEN.DASHBOARD]: renderDashboard, [SCREEN.DEVICE_DETAIL]: renderDeviceDetail,
  [SCREEN.DEVICE_MANAGE]: renderDeviceManage, [SCREEN.REAUTH]: renderReauth, [SCREEN.ACCOUNT]: renderAccount,
  [SCREEN.DATA_USE]: renderDataUse, [SCREEN.LOGOUT_PENDING]: renderLogoutPending, [SCREEN.DELETE_ENTRY]: renderDeleteEntry,
  [SCREEN.LIFECYCLE_CONFIRM]: renderLifecycleConfirm, [SCREEN.LIFECYCLE_UNKNOWN]: renderLifecycleUnknown
};

function render({ focusHeading = true } = {}) {
  const renderer = renderers[state.screen];
  if (!renderer) throw new Error(`No renderer for ${state.screen}`);
  app.innerHTML = renderer();
  document.body.dataset.screen = state.screen;
  document.body.dataset.authStatus = state.authStatus;
  announcer.textContent = `Current screen: ${state.screen}`;
  if (focusHeading && !initialRender) app.querySelector('h1')?.focus();
  initialRender = false;
}

function dispatch(action, payload = {}) {
  state = transition(state, action, payload);
  render();
}

app.addEventListener('click', (event) => {
  const target = event.target.closest('[data-action]');
  if (!target) return;
  const payload = {};
  if (target.dataset.platform) payload.platform = target.dataset.platform;
  if (target.dataset.result) payload.result = target.dataset.result;
  if (target.dataset.mode) payload.mode = target.dataset.mode;
  dispatch(target.dataset.action, payload);
});

document.querySelector('.prototype-topbar').addEventListener('click', (event) => {
  const target = event.target.closest('[data-global-action]');
  if (!target) return;
  const action = target.dataset.globalAction;
  if (action === 'RESET') { state = createPrototype(); render(); }
  if (action === 'START_SETUP') { state = createPrototype(); dispatch('START'); }
  if (action === 'ACCOUNT_ENTRY') { state = transition(state,'OPEN_ACCOUNT_ENTRY'); render(); }
  if (action === 'DASHBOARD') {
    if (state.authStatus === 'signed-in') dispatch('OPEN_DASHBOARD');
    else { state = transition(state,'OPEN_ACCOUNT_ENTRY'); render(); }
  }
  if (action === 'TOGGLE_RTL') {
    const rtl = document.documentElement.dir !== 'rtl';
    document.documentElement.dir = rtl ? 'rtl' : 'ltr';
    document.documentElement.lang = rtl ? 'ar' : 'en-GB';
    target.setAttribute('aria-pressed', String(rtl));
    announcer.textContent = rtl ? 'Arabic right-to-left layout enabled' : 'English left-to-right layout enabled';
  }
});

document.querySelector('#skip-link').addEventListener('click', () => {
  requestAnimationFrame(() => main.focus());
});

// Deterministic browser-verification API. No transport and no persistence.
window.__TSK0333_TEST__ = Object.freeze({
  getState: () => JSON.parse(JSON.stringify(state)),
  dispatch: (action,payload={}) => dispatch(action,payload),
  reset: () => { state=createPrototype(); render(); },
  invariants: [...INVARIANTS]
});

render({ focusHeading: false });
