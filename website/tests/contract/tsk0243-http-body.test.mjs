import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { stripTypeScriptTypes } from 'node:module';

const root = resolve(import.meta.dirname, '../..');
const modulePath = resolve(root, 'src/lib/bounded-request-body.ts');

async function loadApi() {
  assert.equal(existsSync(modulePath), true, 'missing bounded streaming request-body reader');
  const source = readFileSync(modulePath, 'utf8');
  const js = stripTypeScriptTypes(source, { mode: 'strip' });
  return import(`data:text/javascript;base64,${Buffer.from(js).toString('base64')}`);
}

function streamedRequest(chunks) {
  const encoder = new TextEncoder();
  const body = new ReadableStream({
    start(controller) {
      for (const chunk of chunks) controller.enqueue(encoder.encode(chunk));
      controller.close();
    },
  });
  return new Request('https://verify.usesafeweb.com/probe', { method: 'POST', body, duplex: 'half' });
}

test('bounded reader accepts a valid body at the byte limit without requiring Content-Length', async () => {
  const api = await loadApi();
  const request = streamedRequest(['a'.repeat(2048), 'b'.repeat(2048)]);
  const body = await api.readBoundedUtf8Body(request, 4096);
  assert.equal(Buffer.byteLength(body, 'utf8'), 4096);
  assert.equal(body, `${'a'.repeat(2048)}${'b'.repeat(2048)}`);
});

test('bounded reader stops a chunked body as soon as the byte limit is exceeded', async () => {
  const api = await loadApi();
  const request = streamedRequest(['a'.repeat(4096), 'b']);
  await assert.rejects(api.readBoundedUtf8Body(request, 4096), /request body too large/i);
});

test('bounded reader rejects malformed UTF-8 rather than normalizing untrusted bytes', async () => {
  const api = await loadApi();
  const body = new ReadableStream({
    start(controller) {
      controller.enqueue(new Uint8Array([0xc3, 0x28]));
      controller.close();
    },
  });
  const request = new Request('https://verify.usesafeweb.com/probe', { method: 'POST', body, duplex: 'half' });
  await assert.rejects(api.readBoundedUtf8Body(request, 4096), /invalid utf-8/i);
});
