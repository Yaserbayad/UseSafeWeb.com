const verificationSuffix = 'verify.usesafeweb.com';
const challengePattern = /^[0-9a-f]{32}$/;
const maxTokenBytes = 2048;
const defaultTimeoutMs = 5_000;

export type BrowserDnsVerificationCheck = {
  dnsPath: 'verified-fresh' | 'verified-stale' | 'failed' | 'uncertain' | 'not-run';
  reasonCode:
    | 'TECH_VERIFIED'
    | 'TECH_VERIFY_NEGATIVE'
    | 'VERIFY_STALE'
    | 'VERIFY_UNREACHABLE'
    | 'VERIFICATION_SERVICE_ERROR'
    | 'EVIDENCE_CONFLICT'
    | 'BYPASS_OR_CONTEXT_UNCERTAIN';
  verifierVersion: 'private-rewrite-v1';
};

type FetchLike = (input: string, init?: RequestInit) => Promise<Response>;

function exactKeys(value: Record<string, unknown>, expected: readonly string[]): boolean {
  const actual = Object.keys(value).sort();
  const wanted = [...expected].sort();
  return actual.length === wanted.length && actual.every((key, index) => key === wanted[index]);
}

function validToken(value: unknown): value is string {
  return typeof value === 'string' && value.length > 0 && new TextEncoder().encode(value).byteLength <= maxTokenBytes;
}

function parseIssuedRequest(value: unknown): { challenge: string; probeHost: string; requestToken: string } | null {
  if (!value || typeof value !== 'object' || Array.isArray(value)) return null;
  const candidate = value as Record<string, unknown>;
  if (!exactKeys(candidate, ['challenge', 'probeHost', 'requestToken', 'expiresAt'])) return null;
  if (typeof candidate.challenge !== 'string' || !challengePattern.test(candidate.challenge)) return null;
  if (candidate.probeHost !== `${candidate.challenge}.${verificationSuffix}`) return null;
  if (!validToken(candidate.requestToken)) return null;
  if (!Number.isSafeInteger(candidate.expiresAt) || (candidate.expiresAt as number) <= 0) return null;
  return {
    challenge: candidate.challenge,
    probeHost: candidate.probeHost,
    requestToken: candidate.requestToken,
  };
}

function parseObservationEnvelope(value: unknown): string | null {
  if (!value || typeof value !== 'object' || Array.isArray(value)) return null;
  const candidate = value as Record<string, unknown>;
  if (!exactKeys(candidate, ['observationToken']) || !validToken(candidate.observationToken)) return null;
  return candidate.observationToken;
}

function parseCheck(value: unknown): BrowserDnsVerificationCheck | null {
  if (!value || typeof value !== 'object' || Array.isArray(value)) return null;
  const candidate = value as Record<string, unknown>;
  if (!exactKeys(candidate, ['dnsPath', 'reasonCode', 'verifierVersion'])) return null;
  if (candidate.verifierVersion !== 'private-rewrite-v1') return null;

  const dnsPath = candidate.dnsPath;
  const reasonCode = candidate.reasonCode;
  if (dnsPath === 'verified-fresh' && reasonCode === 'TECH_VERIFIED') {
    return { dnsPath: 'verified-fresh', reasonCode: 'TECH_VERIFIED', verifierVersion: 'private-rewrite-v1' };
  }
  if (dnsPath === 'verified-stale' && reasonCode === 'VERIFY_STALE') {
    return { dnsPath: 'verified-stale', reasonCode: 'VERIFY_STALE', verifierVersion: 'private-rewrite-v1' };
  }
  if (dnsPath === 'failed' && reasonCode === 'TECH_VERIFY_NEGATIVE') {
    return { dnsPath: 'failed', reasonCode: 'TECH_VERIFY_NEGATIVE', verifierVersion: 'private-rewrite-v1' };
  }
  if (dnsPath === 'not-run' && reasonCode === 'VERIFY_UNREACHABLE') {
    return { dnsPath: 'not-run', reasonCode: 'VERIFY_UNREACHABLE', verifierVersion: 'private-rewrite-v1' };
  }
  if (dnsPath === 'uncertain') {
    if (reasonCode === 'VERIFY_UNREACHABLE')
      return { dnsPath: 'uncertain', reasonCode: 'VERIFY_UNREACHABLE', verifierVersion: 'private-rewrite-v1' };
    if (reasonCode === 'VERIFICATION_SERVICE_ERROR')
      return { dnsPath: 'uncertain', reasonCode: 'VERIFICATION_SERVICE_ERROR', verifierVersion: 'private-rewrite-v1' };
    if (reasonCode === 'EVIDENCE_CONFLICT')
      return { dnsPath: 'uncertain', reasonCode: 'EVIDENCE_CONFLICT', verifierVersion: 'private-rewrite-v1' };
    if (reasonCode === 'BYPASS_OR_CONTEXT_UNCERTAIN')
      return { dnsPath: 'uncertain', reasonCode: 'BYPASS_OR_CONTEXT_UNCERTAIN', verifierVersion: 'private-rewrite-v1' };
    if (reasonCode === 'VERIFY_STALE')
      return { dnsPath: 'uncertain', reasonCode: 'VERIFY_STALE', verifierVersion: 'private-rewrite-v1' };
  }
  return null;
}

async function fetchWithTimeout(
  fetchImpl: FetchLike,
  input: string,
  init: RequestInit,
  timeoutMs: number,
): Promise<Response> {
  if (!Number.isSafeInteger(timeoutMs) || timeoutMs <= 0 || timeoutMs > 30_000)
    throw new TypeError('invalid verification timeout');
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  try {
    return await fetchImpl(input, { ...init, signal: controller.signal });
  } finally {
    clearTimeout(timer);
  }
}

async function consumeObservation(
  requestToken: string,
  observationToken: string,
  fetchImpl: FetchLike,
  timeoutMs: number,
): Promise<BrowserDnsVerificationCheck | null> {
  const response = await fetchWithTimeout(
    fetchImpl,
    '/api/dns-verification/results',
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ requestToken, observationToken }),
      credentials: 'same-origin',
      cache: 'no-store',
    },
    timeoutMs,
  );
  if (!response.ok) return null;
  return parseCheck(await response.json());
}

export async function runDnsVerification(
  scope: string,
  fetchImpl: FetchLike = fetch,
  timeoutMs = defaultTimeoutMs,
): Promise<BrowserDnsVerificationCheck | null> {
  if (typeof scope !== 'string' || !challengePattern.test(scope)) return null;
  try {
    const requestResponse = await fetchWithTimeout(
      fetchImpl,
      '/api/dns-verification/requests',
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ scope }),
        credentials: 'same-origin',
        cache: 'no-store',
      },
      timeoutMs,
    );
    if (!requestResponse.ok) return null;
    const issued = parseIssuedRequest(await requestResponse.json());
    if (!issued) return null;

    const probeResponse = await fetchWithTimeout(
      fetchImpl,
      `https://${issued.probeHost}/api/dns-verification/probes`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'text/plain' },
        body: issued.requestToken,
        credentials: 'omit',
        cache: 'no-store',
        mode: 'cors',
      },
      timeoutMs,
    );
    if (!probeResponse.ok) return null;
    const observationToken = parseObservationEnvelope(await probeResponse.json());
    if (!observationToken) return null;

    return await consumeObservation(issued.requestToken, observationToken, fetchImpl, timeoutMs);
  } catch {
    return null;
  }
}
