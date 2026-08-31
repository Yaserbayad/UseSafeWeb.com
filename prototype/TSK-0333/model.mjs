export const SCREEN = Object.freeze({
  HOME: 'home', ROUTER: 'router', NATIVE: 'native', DNS: 'dns', VERIFY: 'verify', SERVICE: 'service', MAP: 'map',
  TROUBLESHOOT: 'troubleshoot', FALSE_POSITIVE: 'false-positive', HELP: 'help', LIMITS: 'limits', REMOVE: 'remove',
  RECOVERY: 'recovery', RESET_LOST: 'reset-lost', ACCOUNT_ENTRY: 'account-entry', SIGN_IN: 'sign-in',
  PROVIDER_PENDING: 'provider-pending', FIRST_SESSION: 'first-session', ACCOUNT_ERROR: 'account-error', DASHBOARD: 'dashboard',
  DEVICE_DETAIL: 'device-detail', DEVICE_MANAGE: 'device-manage', REAUTH: 'reauth', ACCOUNT: 'account', DATA_USE: 'data-use',
  LOGOUT_PENDING: 'logout-pending', DELETE_ENTRY: 'delete-entry', LIFECYCLE_CONFIRM: 'lifecycle-confirm', LIFECYCLE_UNKNOWN: 'lifecycle-unknown'
});

export const EVIDENCE_STATE = Object.freeze({
  VERIFIED: 'verified', PARENT_CONFIRMED: 'parent-confirmed', ACTION_NEEDED: 'action-needed',
  NOT_COVERED: 'not-covered', UNCERTAIN: 'uncertain', REMOVED: 'removed'
});

export const STATE_COPY = Object.freeze({
  [EVIDENCE_STATE.VERIFIED]: { label: 'Verified', supporting: 'Current qualifying technical evidence confirms this layer for the current context.' },
  [EVIDENCE_STATE.PARENT_CONFIRMED]: { label: 'You confirmed this is set up', supporting: 'UseSafeWeb has not independently verified this setting.' },
  [EVIDENCE_STATE.ACTION_NEEDED]: { label: 'Action needed', supporting: 'A known supported step still needs attention.' },
  [EVIDENCE_STATE.NOT_COVERED]: { label: 'Not covered', supporting: 'UseSafeWeb does not cover this in the current supported setup.' },
  [EVIDENCE_STATE.UNCERTAIN]: { label: 'Status uncertain', supporting: 'Current evidence is incomplete or conflicting; do not rely on an earlier positive result.' },
  [EVIDENCE_STATE.REMOVED]: { label: 'Removed', supporting: 'Owning removal evidence shows this UseSafeWeb protection layer is no longer active.' }
});

export const INVARIANTS = Object.freeze([
  'Core value never requires login.',
  'Account presence never creates Verified.',
  'No automatic J0/J1 import, promotion, linkage, or expiry extension.',
  'No browsing/query/activity history is collected by this prototype.',
  'No broad DNS administration is exposed to a parent.',
  'No automatic replay of destructive lifecycle operations after reauthentication or an unknown result.',
  'Physical removal is distinct from account deletion, record deletion, logout, and revoke/unlink.',
  'Record deletion removes the saved dashboard record only and does not claim physical removal.',
  'Account deletion targets account-domain data only and does not claim physical removal or J0/J1 deletion.'
]);

export function createPrototype(screen = SCREEN.HOME) {
  return {
    screen, returnTo: null, platform: null,
    nativeState: EVIDENCE_STATE.ACTION_NEEDED, dnsState: EVIDENCE_STATE.ACTION_NEEDED, serviceState: EVIDENCE_STATE.NOT_COVERED,
    dnsConfigured: false, lastVerification: null, changedCondition: false, recoveryChecked: false,
    authStatus: 'signed-out', accountExists: false, providerMode: null,
    device: { exists: false, nickname: 'Family phone', recordStatus: 'none', lastKnown: null },
    saveIntent: false, operation: null, pendingLifecycle: null, lifecycleOutcome: null, unknownResult: false,
    lastEvent: 'prototype_created'
  };
}

function clone(state) { return { ...state, device: { ...state.device } }; }
function requireScreen(state, ...allowed) { if (!allowed.includes(state.screen)) throw new Error(`Action not allowed from ${state.screen}`); }
function requireSignedIn(state) { if (state.authStatus !== 'signed-in') throw new Error('Signed-in account access required'); }
function returnable(next, state, destination) { next.returnTo = state.screen; next.screen = destination; }

function applyLifecycle(next, action) {
  if (action === 'replace-device') {
    next.device = { exists: true, nickname: 'Replacement phone', recordStatus: 'saved', lastKnown: null };
    next.nativeState = EVIDENCE_STATE.ACTION_NEEDED; next.dnsState = EVIDENCE_STATE.ACTION_NEEDED; next.serviceState = EVIDENCE_STATE.NOT_COVERED;
    next.dnsConfigured = false; next.lastVerification = null; next.screen = SCREEN.DEVICE_DETAIL;
  } else if (action === 'revoke-device') {
    next.device.recordStatus = 'revoked'; next.screen = SCREEN.DEVICE_DETAIL;
  } else if (action === 'delete-device-record') {
    next.device = { exists: false, nickname: 'Family phone', recordStatus: 'deleted', lastKnown: null }; next.screen = SCREEN.DASHBOARD;
  } else if (action === 'account-delete') {
    next.accountExists = false; next.authStatus = 'signed-out'; next.device = { exists: false, nickname: 'Family phone', recordStatus: 'none', lastKnown: null };
    next.screen = SCREEN.HOME;
  } else {
    throw new Error(`Unknown lifecycle action ${action}`);
  }
  next.pendingLifecycle = null; next.unknownResult = false; next.lifecycleOutcome = action;
}

export function transition(state, action, payload = {}) {
  if (action === 'RESET') return createPrototype();
  if (action === 'SIMULATE_LOST_STATE') return createPrototype(SCREEN.RESET_LOST);
  const next = clone(state); next.lastEvent = action.toLowerCase();

  switch (action) {
    case 'START': requireScreen(state, SCREEN.HOME, SCREEN.RESET_LOST, SCREEN.ACCOUNT_ENTRY); next.screen = SCREEN.ROUTER; break;
    case 'CHOOSE_PLATFORM': {
      requireScreen(state, SCREEN.ROUTER); const platform = payload.platform;
      if (!['android','iphone','other'].includes(platform)) throw new Error('Unsupported platform choice');
      next.platform = platform;
      if (platform === 'other') { next.nativeState = EVIDENCE_STATE.NOT_COVERED; next.dnsState = EVIDENCE_STATE.NOT_COVERED; returnable(next,state,SCREEN.LIMITS); }
      else next.screen = SCREEN.NATIVE;
      break;
    }
    case 'NATIVE_CONFIRMED': requireScreen(state,SCREEN.NATIVE); next.nativeState=EVIDENCE_STATE.PARENT_CONFIRMED; next.screen=SCREEN.DNS; break;
    case 'NATIVE_ACTION_NEEDED': requireScreen(state,SCREEN.NATIVE); next.nativeState=EVIDENCE_STATE.ACTION_NEEDED; next.screen=SCREEN.DNS; break;
    case 'REVIEW_NATIVE': requireScreen(state,SCREEN.MAP,SCREEN.DEVICE_DETAIL); next.screen=SCREEN.NATIVE; break;
    case 'DNS_CONFIGURED': case 'DNS_ALREADY_CONFIGURED':
      requireScreen(state,SCREEN.DNS); next.dnsConfigured=true; next.dnsState=EVIDENCE_STATE.PARENT_CONFIRMED; next.lastVerification=null; next.changedCondition=false; next.screen=SCREEN.VERIFY; break;
    case 'VERIFY_RESULT': {
      requireScreen(state,SCREEN.VERIFY); const result=payload.result;
      if (!['verified','action-needed','uncertain','not-covered'].includes(result)) throw new Error('Invalid verification result');
      next.lastVerification=result; next.changedCondition=false;
      if (result==='verified') { if (!state.dnsConfigured) throw new Error('Verified requires configured path'); next.dnsState=EVIDENCE_STATE.VERIFIED; next.screen=state.operation==='reverify-device'?SCREEN.DEVICE_DETAIL:SCREEN.SERVICE; }
      else if (result==='action-needed') { next.dnsState=EVIDENCE_STATE.ACTION_NEEDED; returnable(next,state,SCREEN.TROUBLESHOOT); }
      else if (result==='uncertain') { next.dnsState=EVIDENCE_STATE.UNCERTAIN; returnable(next,state,SCREEN.TROUBLESHOOT); }
      else { next.dnsState=EVIDENCE_STATE.NOT_COVERED; returnable(next,state,SCREEN.LIMITS); }
      next.operation=null; break;
    }
    case 'SERVICE_NONE': requireScreen(state,SCREEN.SERVICE); next.serviceState=EVIDENCE_STATE.NOT_COVERED; next.screen=SCREEN.MAP; break;
    case 'SERVICE_CONFIRMED': requireScreen(state,SCREEN.SERVICE); next.serviceState=EVIDENCE_STATE.PARENT_CONFIRMED; next.screen=SCREEN.MAP; break;
    case 'OPEN_HELP': returnable(next,state,SCREEN.HELP); break;
    case 'OPEN_LIMITS': returnable(next,state,SCREEN.LIMITS); break;
    case 'OPEN_TROUBLESHOOT': requireScreen(state,SCREEN.MAP,SCREEN.HELP,SCREEN.DEVICE_DETAIL); returnable(next,state,SCREEN.TROUBLESHOOT); break;
    case 'OPEN_FALSE_POSITIVE': requireScreen(state,SCREEN.MAP,SCREEN.HELP,SCREEN.DEVICE_DETAIL); returnable(next,state,SCREEN.FALSE_POSITIVE); break;
    case 'RETURN': requireScreen(state,SCREEN.HELP,SCREEN.LIMITS,SCREEN.TROUBLESHOOT,SCREEN.FALSE_POSITIVE,SCREEN.DATA_USE); next.screen=state.returnTo||SCREEN.HOME; next.returnTo=null; break;
    case 'MARK_CONDITION_CHANGED': requireScreen(state,SCREEN.TROUBLESHOOT); next.changedCondition=true; break;
    case 'RETRY_AFTER_CHANGE': requireScreen(state,SCREEN.TROUBLESHOOT); if (!state.changedCondition) throw new Error('Changed condition required'); next.screen=SCREEN.VERIFY; next.returnTo=null; next.changedCondition=false; break;
    case 'REMOVE_DNS': if (!state.dnsConfigured && state.dnsState!==EVIDENCE_STATE.REMOVED) throw new Error('DNS not known configured'); next.screen=SCREEN.REMOVE; next.returnTo=null; break;
    case 'CONFIRM_REMOVED': requireScreen(state,SCREEN.REMOVE); next.dnsConfigured=false; next.dnsState=EVIDENCE_STATE.REMOVED; next.lastVerification=null; next.screen=SCREEN.RECOVERY; break;
    case 'RECOVERY_OK': requireScreen(state,SCREEN.RECOVERY); next.recoveryChecked=true; next.screen=state.authStatus==='signed-in'&&state.device.exists?SCREEN.DEVICE_DETAIL:SCREEN.MAP; break;
    case 'RECONFIGURE': requireScreen(state,SCREEN.MAP,SCREEN.RECOVERY,SCREEN.DEVICE_DETAIL,SCREEN.DEVICE_MANAGE); next.dnsState=EVIDENCE_STATE.ACTION_NEEDED; next.dnsConfigured=false; next.lastVerification=null; next.operation='reinstall-device'; next.screen=SCREEN.DNS; break;

    case 'OPEN_ACCOUNT_ENTRY': next.screen=SCREEN.ACCOUNT_ENTRY; break;
    case 'START_GOOGLE_SIGNIN': requireScreen(state,SCREEN.ACCOUNT_ENTRY,SCREEN.REAUTH,SCREEN.ACCOUNT_ERROR); next.authStatus='provider-pending'; next.providerMode=payload.mode||'returning'; next.screen=SCREEN.PROVIDER_PENDING; break;
    case 'PROVIDER_SUCCESS_NEW': requireScreen(state,SCREEN.PROVIDER_PENDING); next.authStatus='first-session'; next.accountExists=false; next.screen=SCREEN.FIRST_SESSION; break;
    case 'PROVIDER_SUCCESS_RETURNING': requireScreen(state,SCREEN.PROVIDER_PENDING); next.authStatus='signed-in'; next.accountExists=true; next.device=payload.withDevice===false?next.device:{ exists:true,nickname:'Family phone',recordStatus:'saved',lastKnown:'earlier-result' }; next.screen=SCREEN.DASHBOARD; break;
    case 'PROVIDER_ERROR': requireScreen(state,SCREEN.PROVIDER_PENDING); next.authStatus='error'; next.screen=SCREEN.ACCOUNT_ERROR; break;
    case 'PROVIDER_CANCEL': requireScreen(state,SCREEN.PROVIDER_PENDING); next.authStatus='signed-out'; next.screen=SCREEN.ACCOUNT_ENTRY; break;
    case 'CREATE_ACCOUNT': requireScreen(state,SCREEN.FIRST_SESSION); next.authStatus='signed-in'; next.accountExists=true; next.screen=SCREEN.DASHBOARD; break;
    case 'OPEN_DASHBOARD': requireSignedIn(state); next.screen=SCREEN.DASHBOARD; break;
    case 'ADD_DEVICE': requireScreen(state,SCREEN.DASHBOARD); requireSignedIn(state); next.saveIntent=true; next.screen=SCREEN.ROUTER; break;
    case 'SAVE_DEVICE_EXPLICIT': requireScreen(state,SCREEN.MAP); requireSignedIn(state); next.device={ exists:true,nickname:'Family phone',recordStatus:'saved',lastKnown:state.dnsState }; next.saveIntent=false; next.screen=SCREEN.DEVICE_DETAIL; break;
    case 'OPEN_DEVICE': requireScreen(state,SCREEN.DASHBOARD); requireSignedIn(state); if (!state.device.exists) throw new Error('No saved device'); next.screen=SCREEN.DEVICE_DETAIL; break;
    case 'OPEN_MANAGE': requireScreen(state,SCREEN.DEVICE_DETAIL); requireSignedIn(state); next.screen=SCREEN.DEVICE_MANAGE; break;
    case 'REVERIFY_DEVICE': requireScreen(state,SCREEN.DEVICE_DETAIL,SCREEN.DEVICE_MANAGE); requireSignedIn(state); next.operation='reverify-device'; next.screen=SCREEN.VERIFY; break;
    case 'REINSTALL_DEVICE': requireScreen(state,SCREEN.DEVICE_MANAGE); requireSignedIn(state); next.operation='reinstall-device'; next.dnsState=EVIDENCE_STATE.ACTION_NEEDED; next.dnsConfigured=false; next.lastVerification=null; next.screen=SCREEN.DNS; break;
    case 'REPLACE_DEVICE': requireScreen(state,SCREEN.DEVICE_MANAGE); requireSignedIn(state); next.pendingLifecycle='replace-device'; next.screen=SCREEN.LIFECYCLE_CONFIRM; break;
    case 'REVOKE_DEVICE': requireScreen(state,SCREEN.DEVICE_MANAGE); requireSignedIn(state); next.pendingLifecycle='revoke-device'; next.screen=SCREEN.LIFECYCLE_CONFIRM; break;
    case 'DELETE_DEVICE_RECORD': requireScreen(state,SCREEN.DEVICE_MANAGE); requireSignedIn(state); next.pendingLifecycle='delete-device-record'; next.screen=SCREEN.LIFECYCLE_CONFIRM; break;
    case 'CONFIRM_LIFECYCLE': requireScreen(state,SCREEN.LIFECYCLE_CONFIRM); requireSignedIn(state); applyLifecycle(next,state.pendingLifecycle); break;
    case 'SIMULATE_LIFECYCLE_UNKNOWN': requireScreen(state,SCREEN.LIFECYCLE_CONFIRM); next.unknownResult=true; next.screen=SCREEN.LIFECYCLE_UNKNOWN; break;
    case 'RESOLVE_UNKNOWN': requireScreen(state,SCREEN.LIFECYCLE_UNKNOWN); if (payload.result==='applied') applyLifecycle(next,state.pendingLifecycle); else { next.unknownResult=false; next.lifecycleOutcome='not-applied'; next.pendingLifecycle=null; next.screen=state.authStatus==='signed-in'?SCREEN.DASHBOARD:SCREEN.HOME; } break;
    case 'EXPIRE_SESSION': requireSignedIn(state); next.authStatus='expired'; next.screen=SCREEN.REAUTH; break;
    case 'REAUTHENTICATE': requireScreen(state,SCREEN.REAUTH); next.authStatus='signed-in'; next.screen=SCREEN.ACCOUNT; break;
    case 'OPEN_ACCOUNT': requireSignedIn(state); next.screen=SCREEN.ACCOUNT; break;
    case 'OPEN_DATA_USE': returnable(next,state,SCREEN.DATA_USE); break;
    case 'LOGOUT': requireScreen(state,SCREEN.ACCOUNT,SCREEN.DASHBOARD,SCREEN.DEVICE_DETAIL); requireSignedIn(state); next.screen=SCREEN.LOGOUT_PENDING; break;
    case 'CONFIRM_LOGOUT': requireScreen(state,SCREEN.LOGOUT_PENDING); next.authStatus='signed-out'; next.screen=SCREEN.HOME; break;
    case 'OPEN_DELETE_ACCOUNT': requireScreen(state,SCREEN.ACCOUNT); requireSignedIn(state); next.screen=SCREEN.DELETE_ENTRY; break;
    case 'CONFIRM_ACCOUNT_DELETE': requireScreen(state,SCREEN.DELETE_ENTRY); requireSignedIn(state); next.pendingLifecycle='account-delete'; next.screen=SCREEN.LIFECYCLE_CONFIRM; break;
    default: throw new Error(`Unknown action: ${action}`);
  }

  assertPrototype(next); return next;
}

export function assertPrototype(state) {
  if (!Object.values(SCREEN).includes(state.screen)) throw new Error('Invalid screen');
  if (![null,'android','iphone','other'].includes(state.platform)) throw new Error('Invalid platform');
  for (const k of ['nativeState','dnsState','serviceState']) if (!Object.values(EVIDENCE_STATE).includes(state[k])) throw new Error(`Invalid ${k}`);
  if (state.dnsState===EVIDENCE_STATE.VERIFIED && (!state.dnsConfigured || state.lastVerification!=='verified')) throw new Error('Verified requires current qualifying technical evidence');
  if (state.dnsState===EVIDENCE_STATE.REMOVED && state.dnsConfigured) throw new Error('Removed cannot remain configured');
  if (state.authStatus!=='signed-in' && [SCREEN.DASHBOARD,SCREEN.DEVICE_DETAIL,SCREEN.DEVICE_MANAGE,SCREEN.ACCOUNT,SCREEN.DELETE_ENTRY,SCREEN.LOGOUT_PENDING].includes(state.screen)) throw new Error('Private surface requires signed-in state');
  return true;
}

export function stateCopy(value) { const copy=STATE_COPY[value]; if (!copy) throw new Error(`Unknown evidence state ${value}`); return copy; }
