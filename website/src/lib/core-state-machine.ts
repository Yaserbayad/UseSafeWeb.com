export type Locale = 'en-GB' | 'tr-TR' | 'ar';
export type DeviceFamily = 'android' | 'iphone';
export type CorePhase = 'route' | 'native' | 'dns' | 'verify' | 'protection' | 'troubleshoot' | 'recover' | 'removed' | 'complete';
export type ProtectionState = 'protected/verified' | 'configured/parent-confirmed' | 'action-needed' | 'not-covered' | 'uncertain/error' | 'removed';
export type ReasonCode =
  | 'TECH_VERIFIED'
  | 'CONFIG_CONFIRMED_NO_TECH_VERIFY'
  | 'TECH_VERIFY_NEGATIVE'
  | 'REMEDIATION_REQUIRED'
  | 'OUT_OF_SCOPE'
  | 'UNSUPPORTED_PATH'
  | 'VERIFY_STALE'
  | 'VERIFY_TIMEOUT'
  | 'VERIFY_UNREACHABLE'
  | 'VERIFICATION_SERVICE_ERROR'
  | 'EVIDENCE_CONFLICT'
  | 'BYPASS_OR_CONTEXT_UNCERTAIN'
  | 'REMOVED_BY_PARENT'
  | 'REVOKED'
  | 'REINSTALLED_AWAITING_VERIFY';

type TechnicalEvidence = { result: 'positive' | 'negative' | 'indeterminate'; fresh: boolean };
export type ProtectionEvidence = {
  coverage: 'covered' | 'not-covered';
  configured: boolean;
  technical: TechnicalEvidence | null;
  action: string | null;
  uncertainty: ReasonCode | null;
  removal: 'REMOVED_BY_PARENT' | 'REVOKED' | null;
  accountOwned?: boolean;
  journeyComplete?: boolean;
};

export type ProtectionEvaluation = {
  state: ProtectionState;
  reasonCode: ReasonCode;
  action: string | null;
};

export type CoreState = {
  schemaVersion: 1;
  scope: string;
  createdAt: number;
  hardExpiresAt: number;
  locale: Locale;
  phase: CorePhase;
  loginRequired: false;
  deviceFamily?: DeviceFamily;
};

export type CoreEvent =
  | { type: 'SELECT_DEVICE'; deviceFamily?: DeviceFamily }
  | { type: 'CONTINUE_NATIVE'; deviceFamily?: DeviceFamily }
  | { type: 'CONTINUE_DNS'; deviceFamily?: DeviceFamily }
  | { type: 'VERIFICATION_RESULT'; deviceFamily?: DeviceFamily }
  | { type: 'OPEN_TROUBLESHOOT'; deviceFamily?: DeviceFamily }
  | { type: 'OPEN_RECOVERY'; deviceFamily?: DeviceFamily }
  | { type: 'REMOVE_CONFIGURATION'; deviceFamily?: DeviceFamily }
  | { type: 'RESTART_SETUP'; deviceFamily?: DeviceFamily }
  | { type: 'COMPLETE'; deviceFamily?: DeviceFamily };

export type OptionalAccountState = {
  capabilityEnabled: boolean;
  status: 'unavailable' | 'entry' | 'authenticated' | 'expired' | 'logged-out';
  route?: string | null;
};

const locales = new Set<Locale>(['en-GB', 'tr-TR', 'ar']);
const phases = new Set<CorePhase>(['route', 'native', 'dns', 'verify', 'protection', 'troubleshoot', 'recover', 'removed', 'complete']);
const baseKeys = ['createdAt', 'hardExpiresAt', 'locale', 'loginRequired', 'phase', 'schemaVersion', 'scope'];

function evaluation(state: ProtectionState, reasonCode: ReasonCode, action: string | null = null): ProtectionEvaluation {
  return { state, reasonCode, action };
}

export function evaluateProtection(evidence: ProtectionEvidence): ProtectionEvaluation {
  if (evidence.removal) return evaluation('removed', evidence.removal);
  if (evidence.coverage === 'not-covered') return evaluation('not-covered', 'OUT_OF_SCOPE');
  if (evidence.uncertainty) return evaluation('uncertain/error', evidence.uncertainty);
  if (evidence.technical) {
    if (!evidence.technical.fresh) return evaluation('uncertain/error', 'VERIFY_STALE');
    if (evidence.technical.result === 'positive') return evaluation('protected/verified', 'TECH_VERIFIED');
    if (evidence.technical.result === 'negative') {
      return evaluation('action-needed', evidence.action ? 'REMEDIATION_REQUIRED' : 'TECH_VERIFY_NEGATIVE', evidence.action);
    }
    return evaluation('uncertain/error', 'EVIDENCE_CONFLICT');
  }
  if (evidence.action) return evaluation('action-needed', 'REMEDIATION_REQUIRED', evidence.action);
  if (evidence.configured) return evaluation('configured/parent-confirmed', 'CONFIG_CONFIRMED_NO_TECH_VERIFY');
  return evaluation('action-needed', 'REMEDIATION_REQUIRED');
}

function isLocale(value: unknown): value is Locale {
  return typeof value === 'string' && locales.has(value as Locale);
}

function isDevice(value: unknown): value is DeviceFamily {
  return value === 'android' || value === 'iphone';
}

function exactCoreKeys(candidate: Record<string, unknown>): boolean {
  const expected = candidate.phase === 'route' ? baseKeys : [...baseKeys, 'deviceFamily'];
  const actual = Object.keys(candidate).sort();
  const sorted = [...expected].sort();
  return actual.length === sorted.length && actual.every((key, index) => key === sorted[index]);
}

function isCoreState(value: unknown, nowMs: number): value is CoreState {
  if (!value || typeof value !== 'object' || Array.isArray(value)) return false;
  const candidate = value as Record<string, unknown>;
  if (candidate.schemaVersion !== 1 || candidate.loginRequired !== false) return false;
  if (typeof candidate.scope !== 'string' || !/^[0-9a-f]{32}$/.test(candidate.scope)) return false;
  if (!Number.isSafeInteger(candidate.createdAt) || !Number.isSafeInteger(candidate.hardExpiresAt)) return false;
  const createdAt = candidate.createdAt as number;
  const hardExpiresAt = candidate.hardExpiresAt as number;
  if (createdAt < 0 || hardExpiresAt <= createdAt || nowMs < createdAt || nowMs >= hardExpiresAt) return false;
  if (!isLocale(candidate.locale) || typeof candidate.phase !== 'string' || !phases.has(candidate.phase as CorePhase)) return false;
  if (!exactCoreKeys(candidate)) return false;
  if (candidate.phase !== 'route' && !isDevice(candidate.deviceFamily)) return false;
  return true;
}

export function createCoreState(locale: Locale, scope: string, createdAt: number, hardExpiresAt: number): CoreState {
  if (!isLocale(locale) || !/^[0-9a-f]{32}$/.test(scope)) throw new TypeError('invalid core identity');
  if (!Number.isSafeInteger(createdAt) || !Number.isSafeInteger(hardExpiresAt) || createdAt < 0 || hardExpiresAt <= createdAt) throw new TypeError('invalid core lifetime');
  return { schemaVersion: 1, scope, createdAt, hardExpiresAt, locale, phase: 'route', loginRequired: false };
}

function withPhase(state: CoreState, phase: CorePhase, deviceFamily = state.deviceFamily): CoreState {
  if (phase === 'route') {
    return { schemaVersion: 1, scope: state.scope, createdAt: state.createdAt, hardExpiresAt: state.hardExpiresAt, locale: state.locale, phase, loginRequired: false };
  }
  if (!deviceFamily) throw new Error('device selection required');
  return { ...state, phase, loginRequired: false, deviceFamily };
}

export function transitionCoreState(state: CoreState, event: CoreEvent, nowMs: number): CoreState {
  if (!isCoreState(state, nowMs)) throw new Error('core state expired or invalid');
  switch (`${state.phase}:${event.type}`) {
    case 'route:SELECT_DEVICE':
      if (!isDevice(event.deviceFamily)) throw new Error('device selection required');
      return withPhase(state, 'native', event.deviceFamily);
    case 'native:CONTINUE_NATIVE': return withPhase(state, 'dns');
    case 'dns:CONTINUE_DNS': return withPhase(state, 'verify');
    case 'verify:VERIFICATION_RESULT': return withPhase(state, 'protection');
    case 'verify:OPEN_TROUBLESHOOT': return withPhase(state, 'troubleshoot');
    case 'protection:OPEN_TROUBLESHOOT': return withPhase(state, 'troubleshoot');
    case 'troubleshoot:OPEN_RECOVERY': return withPhase(state, 'recover');
    case 'recover:REMOVE_CONFIGURATION': return withPhase(state, 'removed');
    case 'removed:RESTART_SETUP': return withPhase(state, 'route');
    case 'protection:COMPLETE': return withPhase(state, 'complete');
    default: throw new Error(`invalid core transition: ${state.phase} -> ${event.type}`);
  }
}

export function resumeCoreState(raw: string, nowMs: number): CoreState | null {
  try {
    const parsed = JSON.parse(raw);
    return isCoreState(parsed, nowMs) ? parsed : null;
  } catch {
    return null;
  }
}

export function optionalAccountTransition(state: OptionalAccountState, event: 'ENTER' | 'RETURN' | 'EXPIRE' | 'LOGOUT' | 'DASHBOARD'): Required<OptionalAccountState> {
  if (!state.capabilityEnabled) return { capabilityEnabled: false, status: 'unavailable', route: null };
  switch (event) {
    case 'ENTER': return { capabilityEnabled: true, status: 'entry', route: '/account' };
    case 'RETURN': return { capabilityEnabled: true, status: 'authenticated', route: '/dashboard' };
    case 'EXPIRE': return { capabilityEnabled: true, status: 'expired', route: '/account' };
    case 'LOGOUT': return { capabilityEnabled: true, status: 'logged-out', route: null };
    case 'DASHBOARD': return state.status === 'authenticated'
      ? { capabilityEnabled: true, status: 'authenticated', route: '/dashboard' }
      : { capabilityEnabled: true, status: state.status, route: '/account' };
  }
}

export function coreRequiresLogin(_accountState: OptionalAccountState): false {
  return false;
}
