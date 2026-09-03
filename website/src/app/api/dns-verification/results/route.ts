import { readBoundedUtf8Body } from '@/lib/bounded-request-body';
import {
  DNS_VERIFICATION_MAX_HTTP_BODY_BYTES,
  toApprovedDnsVerificationEvent,
  verifyDnsVerificationObservation,
} from '@/lib/dns-verification-proof';

export const runtime = 'nodejs';

const noStoreHeaders = { 'Cache-Control': 'no-store' } as const;
const challengePattern = /^[0-9a-f]{32}$/;

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

function parseBody(value: unknown): { scope: string; challenge: string; observationToken: string } | null {
  if (!value || typeof value !== 'object' || Array.isArray(value)) return null;
  const body = value as Record<string, unknown>;
  const keys = Object.keys(body).sort();
  if (keys.length !== 3 || keys[0] !== 'challenge' || keys[1] !== 'observationToken' || keys[2] !== 'scope') return null;
  if (typeof body.scope !== 'string' || !challengePattern.test(body.scope)) return null;
  if (typeof body.challenge !== 'string' || !challengePattern.test(body.challenge)) return null;
  if (typeof body.observationToken !== 'string' || body.observationToken.length === 0 || Buffer.byteLength(body.observationToken, 'utf8') > 2048) return null;
  return { scope: body.scope, challenge: body.challenge, observationToken: body.observationToken };
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

  const verified = verifyDnsVerificationObservation(
    body.observationToken,
    secret,
    Date.now(),
    body.scope,
    body.challenge,
  );
  if (!verified) return error(403, 'PROOF_NOT_AUTHORIZED', 'DNS verification proof is not valid for the current check.');

  return response(200, toApprovedDnsVerificationEvent(verified));
}
