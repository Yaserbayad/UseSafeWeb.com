import { createHmac, randomBytes, timingSafeEqual } from 'node:crypto';

export const DNS_VERIFICATION_SUFFIX = 'verify.usesafeweb.com';
export const DNS_VERIFICATION_PROTOCOL = 'usesafeweb-dns-path-v1';
export const DNS_PROBE_REQUEST_PROTOCOL = 'usesafeweb-dns-probe-request-v1';
export const DNS_VERIFIER_VERSION = 'private-rewrite-v1';
export const DNS_VERIFICATION_MAX_LIFETIME_MS = 120_000;
export const DNS_PROBE_REQUEST_MAX_LIFETIME_MS = 120_000;
export const DNS_VERIFICATION_MAX_TOKEN_BYTES = 2048;
export const DNS_VERIFICATION_MAX_OBSERVATIONS = 8;
export const DNS_VERIFICATION_MAX_HTTP_BODY_BYTES = 4096;

export type DnsVerificationOutcome = 'verified' | 'failed' | 'uncertain';
export type DnsPathCheck = 'verified-fresh' | 'verified-stale' | 'failed' | 'uncertain' | 'not-run';
export type DnsVerificationReasonCode =
  | 'TECH_VERIFIED'
  | 'TECH_VERIFY_NEGATIVE'
  | 'VERIFY_STALE'
  | 'VERIFY_UNREACHABLE'
  | 'VERIFICATION_SERVICE_ERROR'
  | 'EVIDENCE_CONFLICT'
  | 'BYPASS_OR_CONTEXT_UNCERTAIN';

export type DnsVerificationObservation = {
  protocol: typeof DNS_VERIFICATION_PROTOCOL;
  verifierVersion: typeof DNS_VERIFIER_VERSION;
  scope: string;
  challenge: string;
  outcome: DnsVerificationOutcome;
  reasonCode: DnsVerificationReasonCode;
  observedAt: number;
  expiresAt: number;
};

export type VerifiedDnsVerification = {
  dnsPath: DnsPathCheck;
  reasonCode: DnsVerificationReasonCode;
  observedAt: number | null;
  verifierVersion: typeof DNS_VERIFIER_VERSION;
};

type DnsProbeRequestPayload = {
  protocol: typeof DNS_PROBE_REQUEST_PROTOCOL;
  scope: string;
  challenge: string;
  issuedAt: number;
  expiresAt: number;
};

export type DnsProbeRequest = {
  challenge: string;
  probeHost: string;
  requestToken: string;
  expiresAt: number;
};

export type VerifiedDnsProbeRequest = {
  scope: string;
  challenge: string;
  probeHost: string;
  expiresAt: number;
};

const observationKeys = [
  'challenge',
  'expiresAt',
  'observedAt',
  'outcome',
  'protocol',
  'reasonCode',
  'scope',
  'verifierVersion',
];
const probeRequestKeys = ['challenge', 'expiresAt', 'issuedAt', 'protocol', 'scope'];
const challengePattern = /^[0-9a-f]{32}$/;
const allowedOutcomeReasons: Record<DnsVerificationOutcome, ReadonlySet<DnsVerificationReasonCode>> = {
  verified: new Set(['TECH_VERIFIED']),
  failed: new Set(['TECH_VERIFY_NEGATIVE']),
  uncertain: new Set([
    'VERIFY_UNREACHABLE',
    'VERIFICATION_SERVICE_ERROR',
    'EVIDENCE_CONFLICT',
    'BYPASS_OR_CONTEXT_UNCERTAIN',
  ]),
};

function invalidObservation(): never {
  throw new TypeError('invalid dns verification observation');
}

function invalidProbeRequest(): never {
  throw new TypeError('invalid dns probe request');
}

function validateSigningSecret(secret: string): void {
  if (typeof secret !== 'string' || Buffer.byteLength(secret, 'utf8') < 32) {
    throw new TypeError('dns verification signing secret must be at least 32 bytes');
  }
}

function parseObservation(value: unknown): DnsVerificationObservation {
  if (!value || typeof value !== 'object' || Array.isArray(value)) invalidObservation();
  const candidate = value as Record<string, unknown>;
  const keys = Object.keys(candidate).sort();
  if (keys.length !== observationKeys.length || keys.some((key, index) => key !== observationKeys[index]))
    invalidObservation();
  if (candidate.protocol !== DNS_VERIFICATION_PROTOCOL || candidate.verifierVersion !== DNS_VERIFIER_VERSION)
    invalidObservation();
  if (typeof candidate.scope !== 'string' || !challengePattern.test(candidate.scope)) invalidObservation();
  if (typeof candidate.challenge !== 'string' || !challengePattern.test(candidate.challenge)) invalidObservation();
  if (candidate.outcome !== 'verified' && candidate.outcome !== 'failed' && candidate.outcome !== 'uncertain')
    invalidObservation();
  if (
    typeof candidate.reasonCode !== 'string' ||
    !allowedOutcomeReasons[candidate.outcome].has(candidate.reasonCode as DnsVerificationReasonCode)
  )
    invalidObservation();
  if (!Number.isSafeInteger(candidate.observedAt) || !Number.isSafeInteger(candidate.expiresAt)) invalidObservation();
  const observedAt = candidate.observedAt as number;
  const expiresAt = candidate.expiresAt as number;
  if (observedAt < 0 || expiresAt <= observedAt || expiresAt - observedAt > DNS_VERIFICATION_MAX_LIFETIME_MS)
    invalidObservation();
  return {
    protocol: DNS_VERIFICATION_PROTOCOL,
    verifierVersion: DNS_VERIFIER_VERSION,
    scope: candidate.scope,
    challenge: candidate.challenge,
    outcome: candidate.outcome,
    reasonCode: candidate.reasonCode as DnsVerificationReasonCode,
    observedAt,
    expiresAt,
  };
}

function parseProbeRequest(value: unknown): DnsProbeRequestPayload {
  if (!value || typeof value !== 'object' || Array.isArray(value)) invalidProbeRequest();
  const candidate = value as Record<string, unknown>;
  const keys = Object.keys(candidate).sort();
  if (keys.length !== probeRequestKeys.length || keys.some((key, index) => key !== probeRequestKeys[index]))
    invalidProbeRequest();
  if (candidate.protocol !== DNS_PROBE_REQUEST_PROTOCOL) invalidProbeRequest();
  if (typeof candidate.scope !== 'string' || !challengePattern.test(candidate.scope)) invalidProbeRequest();
  if (typeof candidate.challenge !== 'string' || !challengePattern.test(candidate.challenge)) invalidProbeRequest();
  if (!Number.isSafeInteger(candidate.issuedAt) || !Number.isSafeInteger(candidate.expiresAt)) invalidProbeRequest();
  const issuedAt = candidate.issuedAt as number;
  const expiresAt = candidate.expiresAt as number;
  if (issuedAt < 0 || expiresAt <= issuedAt || expiresAt - issuedAt > DNS_PROBE_REQUEST_MAX_LIFETIME_MS)
    invalidProbeRequest();
  return {
    protocol: DNS_PROBE_REQUEST_PROTOCOL,
    scope: candidate.scope,
    challenge: candidate.challenge,
    issuedAt,
    expiresAt,
  };
}

function serializeObservation(value: DnsVerificationObservation): string {
  return JSON.stringify({
    protocol: value.protocol,
    verifierVersion: value.verifierVersion,
    scope: value.scope,
    challenge: value.challenge,
    outcome: value.outcome,
    reasonCode: value.reasonCode,
    observedAt: value.observedAt,
    expiresAt: value.expiresAt,
  });
}

function serializeProbeRequest(value: DnsProbeRequestPayload): string {
  return JSON.stringify({
    protocol: value.protocol,
    scope: value.scope,
    challenge: value.challenge,
    issuedAt: value.issuedAt,
    expiresAt: value.expiresAt,
  });
}

function signatureFor(payload: string, secret: string): string {
  validateSigningSecret(secret);
  return createHmac('sha256', secret).update(payload, 'utf8').digest('base64url');
}

function probeRequestSignatureFor(payload: string, secret: string): string {
  validateSigningSecret(secret);
  return createHmac('sha256', secret)
    .update(`${DNS_PROBE_REQUEST_PROTOCOL}\0`, 'utf8')
    .update(payload, 'utf8')
    .digest('base64url');
}

function safeSignatureEqual(actual: string, expected: string): boolean {
  try {
    const actualBytes = Buffer.from(actual, 'base64url');
    const expectedBytes = Buffer.from(expected, 'base64url');
    return actualBytes.length === expectedBytes.length && timingSafeEqual(actualBytes, expectedBytes);
  } catch {
    return false;
  }
}

function resultFromObservation(observation: DnsVerificationObservation, nowMs: number): VerifiedDnsVerification | null {
  if (!Number.isSafeInteger(nowMs) || nowMs < 0 || observation.observedAt > nowMs + 5_000) return null;
  if (nowMs >= observation.expiresAt) {
    return {
      dnsPath: observation.outcome === 'verified' ? 'verified-stale' : 'uncertain',
      reasonCode: 'VERIFY_STALE',
      observedAt: observation.observedAt,
      verifierVersion: DNS_VERIFIER_VERSION,
    };
  }
  if (observation.outcome === 'verified') {
    return {
      dnsPath: 'verified-fresh',
      reasonCode: 'TECH_VERIFIED',
      observedAt: observation.observedAt,
      verifierVersion: DNS_VERIFIER_VERSION,
    };
  }
  if (observation.outcome === 'failed') {
    return {
      dnsPath: 'failed',
      reasonCode: 'TECH_VERIFY_NEGATIVE',
      observedAt: observation.observedAt,
      verifierVersion: DNS_VERIFIER_VERSION,
    };
  }
  return {
    dnsPath: 'uncertain',
    reasonCode: observation.reasonCode,
    observedAt: observation.observedAt,
    verifierVersion: DNS_VERIFIER_VERSION,
  };
}

function normalizeProbeHost(value: string): string | null {
  if (typeof value !== 'string' || value.length > 253) return null;
  const lowered = value.toLowerCase();
  const host = lowered.endsWith(':443') ? lowered.slice(0, -4) : lowered;
  if (host.includes(':') || host.endsWith('.')) return null;
  return host;
}

export function createDnsVerificationChallenge(): string {
  return randomBytes(16).toString('hex');
}

export function buildDnsProbeHostname(challenge: string): string {
  if (typeof challenge !== 'string' || !challengePattern.test(challenge)) {
    throw new TypeError('invalid dns verification challenge');
  }
  return `${challenge}.${DNS_VERIFICATION_SUFFIX}`;
}

export function signDnsVerificationObservation(value: unknown, secret: string): string {
  validateSigningSecret(secret);
  const observation = parseObservation(value);
  const payload = Buffer.from(serializeObservation(observation), 'utf8').toString('base64url');
  return `${payload}.${signatureFor(payload, secret)}`;
}

export function verifyDnsVerificationObservation(
  token: string,
  secret: string,
  nowMs: number,
  expectedScope: string,
  expectedChallenge: string,
): VerifiedDnsVerification | null {
  try {
    validateSigningSecret(secret);
    if (
      typeof token !== 'string' ||
      Buffer.byteLength(token, 'utf8') > DNS_VERIFICATION_MAX_TOKEN_BYTES ||
      typeof expectedScope !== 'string' ||
      !challengePattern.test(expectedScope) ||
      typeof expectedChallenge !== 'string' ||
      !challengePattern.test(expectedChallenge)
    )
      return null;
    const parts = token.split('.');
    if (parts.length !== 2 || !parts[0] || !parts[1]) return null;
    const [payload, signature] = parts;
    if (!safeSignatureEqual(signature, signatureFor(payload, secret))) return null;
    const parsed = JSON.parse(Buffer.from(payload, 'base64url').toString('utf8'));
    const observation = parseObservation(parsed);
    if (observation.scope !== expectedScope || observation.challenge !== expectedChallenge) return null;
    return resultFromObservation(observation, nowMs);
  } catch {
    return null;
  }
}

export function createDnsProbeRequest(scope: string, secret: string, nowMs: number): DnsProbeRequest {
  validateSigningSecret(secret);
  if (typeof scope !== 'string' || !challengePattern.test(scope) || !Number.isSafeInteger(nowMs) || nowMs < 0) {
    throw new TypeError('invalid dns probe request input');
  }
  const challenge = createDnsVerificationChallenge();
  const expiresAt = nowMs + DNS_PROBE_REQUEST_MAX_LIFETIME_MS;
  const value: DnsProbeRequestPayload = {
    protocol: DNS_PROBE_REQUEST_PROTOCOL,
    scope,
    challenge,
    issuedAt: nowMs,
    expiresAt,
  };
  const payload = Buffer.from(serializeProbeRequest(value), 'utf8').toString('base64url');
  const requestToken = `${payload}.${probeRequestSignatureFor(payload, secret)}`;
  if (Buffer.byteLength(requestToken, 'utf8') > DNS_VERIFICATION_MAX_TOKEN_BYTES) {
    throw new Error('dns probe request token exceeds configured limit');
  }
  return { challenge, probeHost: buildDnsProbeHostname(challenge), requestToken, expiresAt };
}

export function verifyDnsProbeRequest(token: string, secret: string, nowMs: number): VerifiedDnsProbeRequest | null {
  try {
    validateSigningSecret(secret);
    if (
      typeof token !== 'string' ||
      Buffer.byteLength(token, 'utf8') > DNS_VERIFICATION_MAX_TOKEN_BYTES ||
      !Number.isSafeInteger(nowMs) ||
      nowMs < 0
    )
      return null;
    const parts = token.split('.');
    if (parts.length !== 2 || !parts[0] || !parts[1]) return null;
    const [payload, signature] = parts;
    if (!safeSignatureEqual(signature, probeRequestSignatureFor(payload, secret))) return null;
    const parsed = JSON.parse(Buffer.from(payload, 'base64url').toString('utf8'));
    const request = parseProbeRequest(parsed);
    if (request.issuedAt > nowMs + 5_000 || nowMs >= request.expiresAt) return null;
    return {
      scope: request.scope,
      challenge: request.challenge,
      probeHost: buildDnsProbeHostname(request.challenge),
      expiresAt: request.expiresAt,
    };
  } catch {
    return null;
  }
}

export function createDnsVerificationObservationFromProbeRequest(
  requestToken: string,
  requestHost: string,
  secret: string,
  nowMs: number,
): string | null {
  const request = verifyDnsProbeRequest(requestToken, secret, nowMs);
  if (!request) return null;
  const host = normalizeProbeHost(requestHost);
  if (host !== request.probeHost) return null;
  const expiresAt = Math.min(request.expiresAt, nowMs + DNS_VERIFICATION_MAX_LIFETIME_MS);
  return signDnsVerificationObservation(
    {
      protocol: DNS_VERIFICATION_PROTOCOL,
      verifierVersion: DNS_VERIFIER_VERSION,
      scope: request.scope,
      challenge: request.challenge,
      outcome: 'verified',
      reasonCode: 'TECH_VERIFIED',
      observedAt: nowMs,
      expiresAt,
    },
    secret,
  );
}

function uncertainResult(reasonCode: DnsVerificationReasonCode = 'EVIDENCE_CONFLICT'): VerifiedDnsVerification {
  return { dnsPath: 'uncertain', reasonCode, observedAt: null, verifierVersion: DNS_VERIFIER_VERSION };
}

export function reconcileDnsVerificationObservations(
  tokens: readonly string[],
  secret: string,
  nowMs: number,
  expectedScope: string,
  expectedChallenge: string,
): VerifiedDnsVerification {
  if (!Array.isArray(tokens)) return uncertainResult('VERIFICATION_SERVICE_ERROR');
  if (tokens.length === 0) {
    return {
      dnsPath: 'not-run',
      reasonCode: 'VERIFY_UNREACHABLE',
      observedAt: null,
      verifierVersion: DNS_VERIFIER_VERSION,
    };
  }
  if (tokens.length > DNS_VERIFICATION_MAX_OBSERVATIONS) return uncertainResult('VERIFICATION_SERVICE_ERROR');
  const verified = tokens.map((token) =>
    verifyDnsVerificationObservation(token, secret, nowMs, expectedScope, expectedChallenge),
  );
  if (verified.some((item) => item === null)) return uncertainResult();
  const results = verified as VerifiedDnsVerification[];
  const latestObservedAt = Math.max(...results.map((item) => item.observedAt ?? -1));
  const latest = results.filter((item) => (item.observedAt ?? -1) === latestObservedAt);
  const signatures = new Set(latest.map((item) => `${item.dnsPath}:${item.reasonCode}`));
  if (signatures.size !== 1) return uncertainResult();
  return latest[0];
}

export function toApprovedDnsVerificationEvent(result: VerifiedDnsVerification): {
  dnsPath: DnsPathCheck;
  reasonCode: DnsVerificationReasonCode;
  verifierVersion: typeof DNS_VERIFIER_VERSION;
} {
  return {
    dnsPath: result.dnsPath,
    reasonCode: result.reasonCode,
    verifierVersion: result.verifierVersion,
  };
}
