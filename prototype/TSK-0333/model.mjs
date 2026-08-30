export const SCREEN = Object.freeze({
  HOME: 'home',
  ROUTER: 'router',
  NATIVE: 'native',
  DNS: 'dns',
  VERIFY: 'verify',
  SERVICE: 'service',
  MAP: 'map',
  TROUBLESHOOT: 'troubleshoot',
  FALSE_POSITIVE: 'false-positive',
  HELP: 'help',
  LIMITS: 'limits',
  REMOVE: 'remove',
  RECOVERY: 'recovery',
  RESET_LOST: 'reset-lost'
});

export const EVIDENCE_STATE = Object.freeze({
  VERIFIED: 'verified',
  PARENT_CONFIRMED: 'parent-confirmed',
  ACTION_NEEDED: 'action-needed',
  NOT_COVERED: 'not-covered',
  UNCERTAIN: 'uncertain',
  REMOVED: 'removed'
});

export const STATE_COPY = Object.freeze({
  [EVIDENCE_STATE.VERIFIED]: Object.freeze({
    label: 'Verified',
    supporting: 'SafeWeb verified this protection step is active on your current setup.'
  }),
  [EVIDENCE_STATE.PARENT_CONFIRMED]: Object.freeze({
    label: 'You confirmed this is set up',
    supporting: 'SafeWeb has not independently verified this setting.'
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
    label: 'Status uncertain',
    supporting: 'We can’t verify this protection right now. Check it before relying on this layer.'
  }),
  [EVIDENCE_STATE.REMOVED]: Object.freeze({
    label: 'Removed',
    supporting: 'SafeWeb DNS is no longer active on this device.'
  })
});

export function createJourney(screen = SCREEN.HOME) {
  return {
    screen,
    returnTo: null,
    platform: null,
    nativeState: EVIDENCE_STATE.ACTION_NEEDED,
    dnsState: EVIDENCE_STATE.ACTION_NEEDED,
    serviceState: EVIDENCE_STATE.NOT_COVERED,
    serviceApplicable: false,
    dnsConfigured: false,
    lastVerification: null,
    recoveryChecked: false,
    changedCondition: false,
    lastEvent: 'journey_created'
  };
}

function clone(state) {
  return { ...state };
}

function requireScreen(state, ...allowed) {
  if (!allowed.includes(state.screen)) throw new Error(`Action not allowed from ${state.screen}`);
}

function returnable(next, state, destination) {
  next.returnTo = state.screen;
  next.screen = destination;
}

export function transition(state, action, payload = {}) {
  if (action === 'RESET') return createJourney();
  if (action === 'SIMULATE_LOST_STATE') return createJourney(SCREEN.RESET_LOST);
  const next = clone(state);
  next.lastEvent = action.toLowerCase();

  switch (action) {
    case 'START':
      requireScreen(state, SCREEN.HOME, SCREEN.RESET_LOST);
      next.screen = SCREEN.ROUTER;
      break;

    case 'CHOOSE_PLATFORM': {
      requireScreen(state, SCREEN.ROUTER);
      const platform = payload.platform;
      if (!['android', 'iphone', 'other'].includes(platform)) throw new Error('Unsupported platform choice');
      next.platform = platform;
      if (platform === 'other') {
        next.nativeState = EVIDENCE_STATE.NOT_COVERED;
        next.dnsState = EVIDENCE_STATE.NOT_COVERED;
        returnable(next, state, SCREEN.LIMITS);
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

    case 'REVIEW_NATIVE':
      requireScreen(state, SCREEN.MAP);
      next.screen = SCREEN.NATIVE;
      break;

    case 'DNS_CONFIGURED':
    case 'DNS_ALREADY_CONFIGURED':
      requireScreen(state, SCREEN.DNS);
      next.dnsConfigured = true;
      next.dnsState = EVIDENCE_STATE.PARENT_CONFIRMED;
      next.lastVerification = null;
      next.changedCondition = false;
      next.screen = SCREEN.VERIFY;
      break;

    case 'VERIFY_RESULT': {
      requireScreen(state, SCREEN.VERIFY);
      const result = payload.result;
      if (!['verified', 'action-needed', 'uncertain', 'not-covered'].includes(result)) throw new Error('Invalid verification result');
      next.lastVerification = result;
      next.changedCondition = false;
      if (result === 'verified') {
        if (!state.dnsConfigured) throw new Error('Verification success requires the supported DNS configuration path');
        next.dnsState = EVIDENCE_STATE.VERIFIED;
        next.screen = SCREEN.SERVICE;
      } else if (result === 'action-needed') {
        next.dnsState = EVIDENCE_STATE.ACTION_NEEDED;
        returnable(next, state, SCREEN.TROUBLESHOOT);
      } else if (result === 'uncertain') {
        next.dnsState = EVIDENCE_STATE.UNCERTAIN;
        returnable(next, state, SCREEN.TROUBLESHOOT);
      } else {
        next.dnsState = EVIDENCE_STATE.NOT_COVERED;
        returnable(next, state, SCREEN.LIMITS);
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
      returnable(next, state, SCREEN.HELP);
      break;

    case 'OPEN_LIMITS':
      returnable(next, state, SCREEN.LIMITS);
      break;

    case 'OPEN_TROUBLESHOOT':
      requireScreen(state, SCREEN.MAP, SCREEN.HELP);
      returnable(next, state, SCREEN.TROUBLESHOOT);
      break;

    case 'OPEN_FALSE_POSITIVE':
      requireScreen(state, SCREEN.MAP, SCREEN.HELP);
      returnable(next, state, SCREEN.FALSE_POSITIVE);
      break;

    case 'RETURN':
      requireScreen(state, SCREEN.HELP, SCREEN.LIMITS, SCREEN.TROUBLESHOOT, SCREEN.FALSE_POSITIVE);
      next.screen = state.returnTo || SCREEN.HOME;
      next.returnTo = null;
      break;

    case 'MARK_CONDITION_CHANGED':
      requireScreen(state, SCREEN.TROUBLESHOOT);
      next.changedCondition = true;
      break;

    case 'RETRY_AFTER_CHANGE':
      requireScreen(state, SCREEN.TROUBLESHOOT);
      if (![EVIDENCE_STATE.ACTION_NEEDED, EVIDENCE_STATE.UNCERTAIN].includes(state.dnsState)) throw new Error('Retry is not relevant to the current DNS state');
      if (state.changedCondition !== true) throw new Error('Retry requires a changed condition');
      next.lastVerification = null;
      next.changedCondition = false;
      next.returnTo = null;
      next.screen = SCREEN.VERIFY;
      break;

    case 'REMOVE_DNS':
      if (!state.dnsConfigured && state.dnsState !== EVIDENCE_STATE.REMOVED) throw new Error('SafeWeb DNS is not known to be configured in this journey');
      next.returnTo = null;
      next.screen = SCREEN.REMOVE;
      break;

    case 'CONFIRM_REMOVED':
      requireScreen(state, SCREEN.REMOVE);
      next.dnsConfigured = false;
      next.dnsState = EVIDENCE_STATE.REMOVED;
      next.lastVerification = null;
      next.changedCondition = false;
      next.recoveryChecked = false;
      next.screen = SCREEN.RECOVERY;
      break;

    case 'RECOVERY_OK':
      requireScreen(state, SCREEN.RECOVERY);
      next.recoveryChecked = true;
      next.screen = SCREEN.MAP;
      break;

    case 'RECONFIGURE':
      requireScreen(state, SCREEN.MAP, SCREEN.RECOVERY);
      if (state.dnsState !== EVIDENCE_STATE.REMOVED) throw new Error('Reconfigure is available after removal');
      next.dnsState = EVIDENCE_STATE.ACTION_NEEDED;
      next.dnsConfigured = false;
      next.lastVerification = null;
      next.recoveryChecked = false;
      next.screen = SCREEN.DNS;
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
  if (state.dnsState === EVIDENCE_STATE.VERIFIED) {
    if (state.lastVerification !== 'verified') throw new Error('Verified DNS requires current qualifying verification evidence');
    if (!state.dnsConfigured) throw new Error('Verified DNS cannot survive removal');
  }
  if (state.dnsState === EVIDENCE_STATE.REMOVED && state.dnsConfigured) throw new Error('Removed DNS cannot remain configured');
  if (state.platform === 'other' && state.dnsState === EVIDENCE_STATE.VERIFIED) throw new Error('Unsupported platform cannot be verified');
  return true;
}

export function stateCopy(value) {
  const copy = STATE_COPY[value];
  if (!copy) throw new Error(`Unknown evidence state: ${value}`);
  return copy;
}
