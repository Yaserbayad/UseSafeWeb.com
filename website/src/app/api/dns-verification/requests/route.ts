import { readBoundedUtf8Body } from '@/lib/bounded-request-body';
import { DNS_VERIFICATION_MAX_HTTP_BODY_BYTES, createDnsProbeRequest } from '@/lib/dns-verification-proof';

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

async function boundedJson(request: Request): Promise<unknown> {
  const raw = await readBoundedUtf8Body(request, DNS_VERIFICATION_MAX_HTTP_BODY_BYTES);
  return JSON.parse(raw);
}

function parseScope(value: unknown): string | null {
  if (!value || typeof value !== 'object' || Array.isArray(value)) return null;
  const body = value as Record<string, unknown>;
  if (Object.keys(body).length !== 1 || typeof body.scope !== 'string' || !/^[0-9a-f]{32}$/.test(body.scope))
    return null;
  return body.scope;
}

export async function POST(request: Request): Promise<Response> {
  if (!request.headers.get('content-type')?.toLowerCase().startsWith('application/json')) {
    return error(415, 'UNSUPPORTED_MEDIA_TYPE', 'Expected application/json.');
  }

  let body: unknown;
  try {
    body = await boundedJson(request);
  } catch (cause) {
    if (cause instanceof RangeError) return error(413, 'REQUEST_TOO_LARGE', 'Request body exceeds the allowed size.');
    return error(400, 'INVALID_REQUEST', 'Request body must be valid UTF-8 JSON.');
  }

  const scope = parseScope(body);
  if (!scope)
    return error(400, 'INVALID_REQUEST', 'Request body does not match the DNS verification request contract.');

  const secret = signingSecret();
  if (!secret) return error(503, 'VERIFIER_UNAVAILABLE', 'DNS verification is not configured.');

  try {
    const issued = createDnsProbeRequest(scope, secret, Date.now());
    return response(201, issued);
  } catch {
    return error(503, 'VERIFIER_UNAVAILABLE', 'DNS verification is not available.');
  }
}
