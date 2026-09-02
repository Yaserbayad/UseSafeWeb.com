export const SCREEN = Object.freeze({
  DISCOVERY: 'discovery',
  ROUTER: 'router',
  NATIVE: 'native',
  DNS: 'dns',
  VERIFY: 'verify',
  SERVICE: 'service',
  MAP: 'map',
  TROUBLESHOOTING: 'troubleshooting',
  REMOVAL: 'removal',
  RECOVERY: 'recovery',
  LIMITATIONS: 'limitations'
});

export const EVIDENCE_STATE = Object.freeze({
  VERIFIED: 'protected/verified',
  PARENT_CONFIRMED: 'configured/parent-confirmed',
  ACTION_NEEDED: 'action-needed',
  NOT_COVERED: 'not-covered',
  UNCERTAIN: 'uncertain/error',
  REMOVED: 'removed'
});

export const STATE_COPY = Object.freeze({
  [EVIDENCE_STATE.VERIFIED]: Object.freeze({
    label: 'Protection verified',
    supporting: 'SafeWeb verified this protection step for this setup.'
  }),
  [EVIDENCE_STATE.PARENT_CONFIRMED]: Object.freeze({
    label: 'Setup confirmed',
    supporting: 'Protection has not yet been technically verified.'
  }),
  [EVIDENCE_STATE.ACTION_NEEDED]: Object.freeze({
    label: 'Action needed',
    supporting: 'Finish this step before relying on this protection layer.'
  }),
  [EVIDENCE_STATE.NOT_COVERED]: Object.freeze({
    label: 'Not covered',
    supporting: 'SafeWeb does not cover this on your current setup.'
  }),
  [EVIDENCE_STATE.UNCERTAIN]: Object.freeze({
    label: 'Protection status could not be verified',
    supporting: 'Retry verification or follow the troubleshooting steps before relying on this protection.'
  }),
  [EVIDENCE_STATE.REMOVED]: Object.freeze({
    label: 'Removed',
    supporting: 'SafeWeb DNS is no longer configured on this device.'
  })
});

export function createJourney() {
  return {
    screen: SCREEN.DISCOVERY,
    returnTo: null,
    platform: null,
    nativeState: EVIDENCE_STATE.ACTION_NEEDED,
    dnsState: EVIDENCE_STATE.ACTION_NEEDED,
    serviceState: EVIDENCE_STATE.NOT_COVERED,
    serviceApplicable: false,
    lastVerification: null,
    recoveryChecked: false
  };
}

function requireScreen(state, ...allowed) {
  if (!allowed.includes(state.screen)) throw new Error(`Action not allowed from ${state.screen}`);
}

function clone(state) {
  return { ...state };
}

export function transition(state, action, payload = {}) {
  if (action === 'RESET') return createJourney();
  const next = clone(state);

  switch (action) {
    case 'START':
      requireScreen(state, SCREEN.DISCOVERY);
      next.screen = SCREEN.ROUTER;
      break;

    case 'CHOOSE_PLATFORM': {
      requireScreen(state, SCREEN.ROUTER);
      const platform = payload.platform;
      if (!['android', 'iphone', 'other'].includes(platform)) throw new Error('Unsupported platform choice');
      next.platform = platform;
      if (platform === 'other') {
        next.dnsState = EVIDENCE_STATE.NOT_COVERED;
        next.returnTo = SCREEN.ROUTER;
        next.screen = SCREEN.LIMITATIONS;
      } else {
        next.screen = SCREEN.NATIVE;
      }
      break;
    }

    case 'NATIVE_CONFIRMED':
      requireScreen(state, SCREEN.NATIVE);
      next.nativeState = EVIDENCE_STATE.PARENT_CONFIRMED;
      next.screen = SCREEN.DNS;
      break;

    case 'NATIVE_ACTION_NEEDED':
      requireScreen(state, SCREEN.NATIVE);
      next.nativeState = EVIDENCE_STATE.ACTION_NEEDED;
      next.screen = SCREEN.DNS;
      break;

    case 'DNS_CONFIGURED':
      requireScreen(state, SCREEN.DNS);
      next.dnsState = EVIDENCE_STATE.PARENT_CONFIRMED;
      next.lastVerification = null;
      next.screen = SCREEN.VERIFY;
      break;

    case 'VERIFY_RESULT': {
      requireScreen(state, SCREEN.VERIFY);
      const result = payload.result;
      if (!['verified', 'action-needed', 'uncertain', 'not-covered'].includes(result)) throw new Error('Invalid verification result');
      next.lastVerification = result;
      if (result === 'verified') {
        next.dnsState = EVIDENCE_STATE.VERIFIED;
        next.screen = SCREEN.SERVICE;
      } else if (result === 'action-needed') {
        next.dnsState = EVIDENCE_STATE.ACTION_NEEDED;
        next.returnTo = SCREEN.VERIFY;
        next.screen = SCREEN.TROUBLESHOOTING;
      } else if (result === 'uncertain') {
        next.dnsState = EVIDENCE_STATE.UNCERTAIN;
        next.returnTo = SCREEN.VERIFY;
        next.screen = SCREEN.TROUBLESHOOTING;
      } else {
        next.dnsState = EVIDENCE_STATE.NOT_COVERED;
        next.returnTo = SCREEN.VERIFY;
        next.screen = SCREEN.LIMITATIONS;
      }
      break;
    }

    case 'SERVICE_NONE':
      requireScreen(state, SCREEN.SERVICE);
      next.serviceApplicable = false;
      next.serviceState = EVIDENCE_STATE.NOT_COVERED;
      next.screen = SCREEN.MAP;
      break;

    case 'SERVICE_CONFIRMED':
      requireScreen(state, SCREEN.SERVICE);
      next.serviceApplicable = true;
      next.serviceState = EVIDENCE_STATE.PARENT_CONFIRMED;
      next.screen = SCREEN.MAP;
      break;

    case 'OPEN_HELP':
      next.returnTo = state.screen;
      next.screen = SCREEN.TROUBLESHOOTING;
      break;

    case 'SHOW_LIMITATIONS':
      next.returnTo = state.screen;
      next.screen = SCREEN.LIMITATIONS;
      break;

    case 'RETURN':
      requireScreen(state, SCREEN.TROUBLESHOOTING, SCREEN.LIMITATIONS);
      next.screen = state.returnTo || SCREEN.DISCOVERY;
      next.returnTo = null;
      break;

    case 'RETRY_AFTER_CHANGE':
      requireScreen(state, SCREEN.TROUBLESHOOTING);
      if (![EVIDENCE_STATE.ACTION_NEEDED, EVIDENCE_STATE.UNCERTAIN].includes(state.dnsState)) throw new Error('Retry is not relevant to the current DNS state');
      if (payload.changedCondition !== true) throw new Error('Retry requires a changed condition');
      next.lastVerification = null;
      next.screen = SCREEN.VERIFY;
      next.returnTo = null;
      break;

    case 'REMOVE_DNS':
      requireScreen(state, SCREEN.MAP, SCREEN.TROUBLESHOOTING, SCREEN.LIMITATIONS, SCREEN.VERIFY, SCREEN.SERVICE);
      next.screen = SCREEN.REMOVAL;
      next.returnTo = null;
      break;

    case 'CONFIRM_REMOVED':
      requireScreen(state, SCREEN.REMOVAL);
      next.dnsState = EVIDENCE_STATE.REMOVED;
      next.lastVerification = null;
      next.screen = SCREEN.RECOVERY;
      break;

    case 'RECOVERY_OK':
      requireScreen(state, SCREEN.RECOVERY);
      next.recoveryChecked = true;
      next.screen = SCREEN.MAP;
      break;

    default:
      throw new Error(`Unknown action: ${action}`);
  }

  assertJourney(next);
  return next;
}

export function assertJourney(state) {
  if (!Object.values(SCREEN).includes(state.screen)) throw new Error('Invalid screen');
  if (![null, 'android', 'iphone', 'other'].includes(state.platform)) throw new Error('Invalid platform');
  for (const key of ['nativeState', 'dnsState', 'serviceState']) {
    if (!Object.values(EVIDENCE_STATE).includes(state[key])) throw new Error(`Invalid ${key}`);
  }
  if (state.dnsState === EVIDENCE_STATE.VERIFIED && state.lastVerification !== 'verified') {
    throw new Error('Verified DNS state requires current qualifying verification evidence');
  }
  return true;
}

export function stateCopy(value) {
  const copy = STATE_COPY[value];
  if (!copy) throw new Error(`Unknown evidence state: ${value}`);
  return copy;
}
