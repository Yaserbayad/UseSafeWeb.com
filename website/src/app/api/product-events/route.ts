import { readBoundedUtf8Body } from '@/lib/bounded-request-body';
import {
  PRODUCT_EVENT_MAX_HTTP_BODY_BYTES,
  ProductEventCapacityError,
  createProductEventStore,
} from '@/lib/product-events';

export const runtime = 'nodejs';

const noStoreHeaders = { 'Cache-Control': 'no-store' } as const;
const store = createProductEventStore();

function response(status: number, body: unknown): Response {
  return Response.json(body, { status, headers: noStoreHeaders });
}

function error(status: number, code: string, message: string): Response {
  return response(status, { error: { code, message } });
}

function noContent(): Response {
  return new Response(null, { status: 204, headers: noStoreHeaders });
}

function acceptsJson(request: Request): boolean {
  return request.headers.get('content-type')?.toLowerCase().startsWith('application/json') ?? false;
}

function productEventsEnabled(): boolean {
  return process.env.USESAFEWEB_PRODUCT_EVENTS_ENABLED === '1';
}

async function boundedJson(request: Request): Promise<unknown> {
  const raw = await readBoundedUtf8Body(request, PRODUCT_EVENT_MAX_HTTP_BODY_BYTES);
  return JSON.parse(raw);
}

export async function POST(request: Request): Promise<Response> {
  if (!productEventsEnabled()) {
    return error(503, 'PRODUCT_EVENTS_DISABLED', 'Product event capture is not enabled.');
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
    const accepted = store.capture(body, Date.now());
    if (accepted === null) return response(200, { accepted: true, duplicate: true });
    return response(202, { accepted: true, eventId: accepted.eventId, expiresAt: accepted.expiresAt });
  } catch (cause) {
    if (cause instanceof ProductEventCapacityError) {
      return error(503, 'CAPTURE_UNAVAILABLE', 'Product event capture is temporarily unavailable.');
    }
    return error(400, 'INVALID_REQUEST', 'Request body does not match the approved product event contract.');
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
  if (Object.keys(record).length !== 1 || typeof record.eventId !== 'string') {
    return error(400, 'INVALID_REQUEST', 'Request body does not match the deletion contract.');
  }

  store.delete(record.eventId, Date.now());
  return noContent();
}
