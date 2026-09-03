import { readBoundedUtf8Body } from '@/lib/bounded-request-body';
import {
  SUPPORT_CAPTURE_MAX_HTTP_BODY_BYTES,
  SUPPORT_CAPTURE_PRIVACY_NOTICE,
  SupportCaptureCapacityError,
  createSupportCaptureStore,
  isSupportReceiptId,
} from '@/lib/support-capture';

export const runtime = 'nodejs';

const noStoreHeaders = { 'Cache-Control': 'no-store' } as const;
const store = createSupportCaptureStore();

function response(status: number, body: unknown): Response {
  return Response.json(body, { status, headers: noStoreHeaders });
}

function error(status: number, code: string, message: string): Response {
  return response(status, { error: { code, message } });
}

function noContent(): Response {
  return new Response(null, { status: 204, headers: noStoreHeaders });
}

async function boundedJson(request: Request): Promise<unknown> {
  const raw = await readBoundedUtf8Body(request, SUPPORT_CAPTURE_MAX_HTTP_BODY_BYTES);
  return JSON.parse(raw);
}

function acceptsJson(request: Request): boolean {
  return request.headers.get('content-type')?.toLowerCase().startsWith('application/json') ?? false;
}

function captureEnabled(): boolean {
  return process.env.USESAFEWEB_SUPPORT_CAPTURE_ENABLED === '1';
}

export async function POST(request: Request): Promise<Response> {
  if (!captureEnabled()) {
    return error(503, 'SUPPORT_CAPTURE_DISABLED', 'Support capture is not enabled.');
  }
  if (!acceptsJson(request)) {
    return error(415, 'UNSUPPORTED_MEDIA_TYPE', 'Expected application/json.');
  }

  let body: unknown;
  try {
    body = await boundedJson(request);
  } catch (cause) {
    if (cause instanceof RangeError) return error(413, 'REQUEST_TOO_LARGE', 'Request body exceeds the allowed size.');
    return error(400, 'INVALID_REQUEST', 'Request body must be valid UTF-8 JSON.');
  }

  try {
    const receipt = store.capture(body, Date.now());
    return response(201, { ...receipt, privacyNotice: SUPPORT_CAPTURE_PRIVACY_NOTICE });
  } catch (cause) {
    if (cause instanceof SupportCaptureCapacityError) {
      return error(503, 'CAPTURE_UNAVAILABLE', 'Support capture is temporarily unavailable.');
    }
    return error(400, 'INVALID_REQUEST', 'Request body does not match the support capture contract.');
  }
}

export async function DELETE(request: Request): Promise<Response> {
  if (!acceptsJson(request)) {
    return error(415, 'UNSUPPORTED_MEDIA_TYPE', 'Expected application/json.');
  }

  let body: unknown;
  try {
    body = await boundedJson(request);
  } catch (cause) {
    if (cause instanceof RangeError) return error(413, 'REQUEST_TOO_LARGE', 'Request body exceeds the allowed size.');
    return error(400, 'INVALID_REQUEST', 'Request body must be valid UTF-8 JSON.');
  }

  if (!body || typeof body !== 'object' || Array.isArray(body)) {
    return error(400, 'INVALID_REQUEST', 'Request body does not match the deletion contract.');
  }
  const record = body as Record<string, unknown>;
  if (Object.keys(record).length !== 1 || !isSupportReceiptId(record.receiptId)) {
    return error(400, 'INVALID_REQUEST', 'Request body does not match the deletion contract.');
  }

  store.delete(record.receiptId, Date.now());
  return noContent();
}
