import { readBoundedUtf8Body } from '@/lib/bounded-request-body';
import {
  DNS_VERIFICATION_MAX_HTTP_BODY_BYTES,
  DNS_VERIFICATION_MAX_TOKEN_BYTES,
  toApprovedDnsVerificationEvent,
  verifyDnsProbeRequest,
  verifyDnsVerificationObservation,
} from '@/lib/dns-verification-proof';

export const runtime = 'nodejs';

const noStoreHeaders = { 'Cache-Control': 'no-store' } as const;

function response(status: number, body: unknown): Response {
  return Response.json(body, { status, headers: noStoreHeaders });
}

function error(status: number, code: string, message: string): Response {
  return response(status, { error: { code, message } });
}

function signingSecret(): string | null {
  const value = process.env.USESAFEWEB_DNS_VERIFICATION_SIGNING_SECRET;
  return typeof value === 'string' && Buffer.byteLength(value, 'utf8') >= 32 ? value : null;
}

function validToken(value: unknown): value is string {
  return (
    typeof value === 'string' &&
    value.length > 0 &&
    Buffer.byteLength(value, 'utf8') <= DNS_VERIFICATION_MAX_TOKEN_BYTES
  );
}

function parseBody(value: unknown): { requestToken: string; observationToken: string } | null {
  if (!value || typeof value !== 'object' || Array.isArray(value)) return null;
  const body = value as Record<string, unknown>;
  const keys = Object.keys(body).sort();
  if (keys.length !== 2 || keys[0] !== 'observationToken' || keys[1] !== 'requestToken') return null;
  if (!validToken(body.requestToken) || !validToken(body.observationToken)) return null;
  return { requestToken: body.requestToken, observationToken: body.observationToken };
}

export async function POST(request: Request): Promise<Response> {
  if (!request.headers.get('content-type')?.toLowerCase().startsWith('application/json')) {
    return error(415, 'UNSUPPORTED_MEDIA_TYPE', 'Expected application/json.');
  }

  let parsed: unknown;
  try {
    const raw = await readBoundedUtf8Body(request, DNS_VERIFICATION_MAX_HTTP_BODY_BYTES);
    parsed = JSON.parse(raw);
  } catch (cause) {
    if (cause instanceof RangeError) return error(413, 'REQUEST_TOO_LARGE', 'Request body exceeds the allowed size.');
    return error(400, 'INVALID_REQUEST', 'Request body must be valid UTF-8 JSON.');
  }

  const body = parseBody(parsed);
  if (!body) return error(400, 'INVALID_REQUEST', 'Request body does not match the DNS verification result contract.');

  const secret = signingSecret();
  if (!secret) return error(503, 'VERIFIER_UNAVAILABLE', 'DNS verification is not configured.');

  const nowMs = Date.now();
  const issued = verifyDnsProbeRequest(body.requestToken, secret, nowMs);
  if (!issued)
    return error(403, 'PROOF_NOT_AUTHORIZED', 'DNS verification request is not valid for the current check.');

  const verified = verifyDnsVerificationObservation(
    body.observationToken,
    secret,
    nowMs,
    issued.scope,
    issued.challenge,
  );
  if (!verified)
    return error(403, 'PROOF_NOT_AUTHORIZED', 'DNS verification proof is not valid for the current check.');

  return response(200, toApprovedDnsVerificationEvent(verified));
}
