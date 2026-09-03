import { readBoundedUtf8Body } from '@/lib/bounded-request-body';
import {
  DNS_VERIFICATION_MAX_HTTP_BODY_BYTES,
  createDnsVerificationObservationFromProbeRequest,
} from '@/lib/dns-verification-proof';

export const runtime = 'nodejs';

function signingSecret(): string | null {
  const value = process.env.USESAFEWEB_DNS_VERIFICATION_SIGNING_SECRET;
  return typeof value === 'string' && Buffer.byteLength(value, 'utf8') >= 32 ? value : null;
}

function configuredPublicOrigin(): string | null {
  const value = process.env.USESAFEWEB_PUBLIC_ORIGIN;
  if (typeof value !== 'string') return null;
  try {
    const url = new URL(value);
    if (url.protocol !== 'https:' || url.origin !== value) return null;
    return value;
  } catch {
    return null;
  }
}

function corsHeaders(origin: string): Record<string, string> {
  return {
    'Access-Control-Allow-Origin': origin,
    'Cache-Control': 'no-store',
    Vary: 'Origin',
  };
}

function response(status: number, body: unknown, origin: string): Response {
  return Response.json(body, { status, headers: corsHeaders(origin) });
}

function error(status: number, code: string, message: string, origin: string): Response {
  return response(status, { error: { code, message } }, origin);
}

export async function POST(request: Request): Promise<Response> {
  const publicOrigin = configuredPublicOrigin();
  if (!publicOrigin) {
    return Response.json(
      { error: { code: 'VERIFIER_UNAVAILABLE', message: 'DNS verification is not configured.' } },
      { status: 503, headers: { 'Cache-Control': 'no-store' } },
    );
  }

  const origin = request.headers.get('origin');
  if (origin !== publicOrigin) return error(403, 'ORIGIN_NOT_ALLOWED', 'Probe origin is not allowed.', publicOrigin);

  if (!request.headers.get('content-type')?.toLowerCase().startsWith('text/plain')) {
    return error(415, 'UNSUPPORTED_MEDIA_TYPE', 'Expected text/plain.', publicOrigin);
  }

  let requestToken: string;
  try {
    requestToken = await readBoundedUtf8Body(request, DNS_VERIFICATION_MAX_HTTP_BODY_BYTES);
  } catch (cause) {
    if (cause instanceof RangeError)
      return error(413, 'REQUEST_TOO_LARGE', 'Request body exceeds the allowed size.', publicOrigin);
    return error(400, 'INVALID_REQUEST', 'Probe request must be valid UTF-8 text.', publicOrigin);
  }

  const secret = signingSecret();
  if (!secret) return error(503, 'VERIFIER_UNAVAILABLE', 'DNS verification is not configured.', publicOrigin);

  const host = request.headers.get('host');
  if (!host) return error(403, 'PROBE_NOT_AUTHORIZED', 'Probe request is not authorized.', publicOrigin);

  const observationToken = createDnsVerificationObservationFromProbeRequest(requestToken, host, secret, Date.now());
  if (!observationToken) return error(403, 'PROBE_NOT_AUTHORIZED', 'Probe request is not authorized.', publicOrigin);

  return response(200, { observationToken }, publicOrigin);
}
