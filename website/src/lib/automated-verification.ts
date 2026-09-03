import type { ProtectionEvidence, ReasonCode } from './core-state-machine';

export type SupportCheck = 'supported' | 'not-covered' | 'unknown';
export type ServiceCheck = 'healthy' | 'degraded' | 'unavailable' | 'unknown';
export type DnsPathCheck = 'verified-fresh' | 'verified-stale' | 'failed' | 'uncertain' | 'not-run';
export type AutomatedCheckState = 'working' | 'failed' | 'uncertain' | 'not-covered' | 'removed';
export type RecoveryRoute = 'troubleshoot' | 'recover' | null;

export type AutomatedVerificationInput = {
  support: SupportCheck;
  service: ServiceCheck;
  dnsPath: DnsPathCheck;
  configured: boolean;
  removed: boolean;
};

export type AutomatedVerificationOutcome = {
  checkState: AutomatedCheckState;
  parentConfirmation: 'confirmed' | 'not-confirmed';
  evidence: ProtectionEvidence;
  recovery: RecoveryRoute;
};

const expectedKeys = ['configured', 'dnsPath', 'removed', 'service', 'support'];
const supportValues = new Set<SupportCheck>(['supported', 'not-covered', 'unknown']);
const serviceValues = new Set<ServiceCheck>(['healthy', 'degraded', 'unavailable', 'unknown']);
const dnsPathValues = new Set<DnsPathCheck>(['verified-fresh', 'verified-stale', 'failed', 'uncertain', 'not-run']);

function invalidInput(): never {
  throw new TypeError('invalid automated verification input');
}

function parseInput(value: unknown): AutomatedVerificationInput {
  if (!value || typeof value !== 'object' || Array.isArray(value)) invalidInput();
  const candidate = value as Record<string, unknown>;
  const keys = Object.keys(candidate).sort();
  if (keys.length !== expectedKeys.length || keys.some((key, index) => key !== expectedKeys[index])) invalidInput();
  if (!supportValues.has(candidate.support as SupportCheck)) invalidInput();
  if (!serviceValues.has(candidate.service as ServiceCheck)) invalidInput();
  if (!dnsPathValues.has(candidate.dnsPath as DnsPathCheck)) invalidInput();
  if (typeof candidate.configured !== 'boolean' || typeof candidate.removed !== 'boolean') invalidInput();
  return candidate as AutomatedVerificationInput;
}

function evidenceBase(configured: boolean): ProtectionEvidence {
  return {
    coverage: 'covered',
    configured,
    technical: null,
    action: null,
    uncertainty: null,
    removal: null,
  };
}

function uncertain(configured: boolean, reasonCode: ReasonCode, technical: ProtectionEvidence['technical'] = null): AutomatedVerificationOutcome {
  return {
    checkState: 'uncertain',
    parentConfirmation: configured ? 'confirmed' : 'not-confirmed',
    evidence: { ...evidenceBase(configured), technical, uncertainty: technical ? null : reasonCode },
    recovery: 'troubleshoot',
  };
}

export function classifyAutomatedChecks(value: unknown): AutomatedVerificationOutcome {
  const input = parseInput(value);
  const parentConfirmation = input.configured ? 'confirmed' : 'not-confirmed';

  if (input.removed) {
    return {
      checkState: 'removed',
      parentConfirmation,
      evidence: { ...evidenceBase(input.configured), removal: 'REMOVED_BY_PARENT' },
      recovery: null,
    };
  }

  if (input.support === 'not-covered') {
    return {
      checkState: 'not-covered',
      parentConfirmation,
      evidence: { ...evidenceBase(input.configured), coverage: 'not-covered' },
      recovery: null,
    };
  }

  if (input.support === 'unknown') {
    return uncertain(input.configured, 'BYPASS_OR_CONTEXT_UNCERTAIN');
  }

  if (input.service !== 'healthy') {
    const reason: ReasonCode = input.service === 'degraded' ? 'VERIFICATION_SERVICE_ERROR' : 'VERIFY_UNREACHABLE';
    return uncertain(input.configured, reason);
  }

  switch (input.dnsPath) {
    case 'verified-fresh':
      return {
        checkState: 'working',
        parentConfirmation,
        evidence: { ...evidenceBase(input.configured), technical: { result: 'positive', fresh: true } },
        recovery: null,
      };
    case 'verified-stale':
      return uncertain(input.configured, 'VERIFY_STALE', { result: 'positive', fresh: false });
    case 'failed':
      return {
        checkState: 'failed',
        parentConfirmation,
        evidence: { ...evidenceBase(input.configured), technical: { result: 'negative', fresh: true } },
        recovery: 'troubleshoot',
      };
    case 'uncertain':
      return uncertain(input.configured, 'EVIDENCE_CONFLICT');
    case 'not-run':
      return uncertain(input.configured, 'VERIFY_UNREACHABLE');
  }
}

export function getCurrentAutomatedVerification(): AutomatedVerificationOutcome {
  // Until a trusted internal producer supplies approved fresh E1 DNS-path evidence,
  // the current product must remain fail-closed and offer recovery rather than infer success.
  return classifyAutomatedChecks({
    support: 'unknown',
    service: 'unknown',
    dnsPath: 'not-run',
    configured: true,
    removed: false,
  });
}
