function validateLimit(maxBytes: number): void {
  if (!Number.isSafeInteger(maxBytes) || maxBytes < 0) {
    throw new TypeError('invalid request body byte limit');
  }
}

function validateDeclaredLength(request: Request, maxBytes: number): void {
  const raw = request.headers.get('content-length');
  if (raw === null) return;
  if (!/^\d+$/.test(raw)) throw new RangeError('request body too large');
  const declared = Number(raw);
  if (!Number.isSafeInteger(declared) || declared > maxBytes) {
    throw new RangeError('request body too large');
  }
}

export async function readBoundedUtf8Body(request: Request, maxBytes: number): Promise<string> {
  validateLimit(maxBytes);
  validateDeclaredLength(request, maxBytes);
  if (!request.body) return '';

  const reader = request.body.getReader();
  const chunks: Uint8Array[] = [];
  let total = 0;

  try {
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      total += value.byteLength;
      if (total > maxBytes) {
        try {
          await reader.cancel('request body too large');
        } catch {
          // Cancellation is best-effort; the byte limit still fails closed.
        }
        throw new RangeError('request body too large');
      }
      chunks.push(value);
    }
  } finally {
    reader.releaseLock();
  }

  const bytes = new Uint8Array(total);
  let offset = 0;
  for (const chunk of chunks) {
    bytes.set(chunk, offset);
    offset += chunk.byteLength;
  }

  try {
    return new TextDecoder('utf-8', { fatal: true }).decode(bytes);
  } catch {
    throw new TypeError('invalid UTF-8 request body');
  }
}
