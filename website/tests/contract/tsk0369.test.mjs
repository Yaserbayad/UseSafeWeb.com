import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { stripTypeScriptTypes } from 'node:module';

const root = resolve(import.meta.dirname, '../..');
const supportPath = resolve(root, 'src/lib/support-capture.ts');
const routePath = resolve(root, 'src/app/api/support-capture/route.ts');

const dataUrl = (source) => `data:text/javascript;base64,${Buffer.from(source).toString('base64')}`;

async function loadSupportApi() {
  const source = readFileSync(supportPath, 'utf8');
  return import(dataUrl(stripTypeScriptTypes(source, { mode: 'strip' })));
}

const now = 1_000;

const validFeedback = {
  reportType: 'feedback',
  rootCause: 'instructions_unclear',
  journeyStage: 'phone',
  deviceClass: 'android',
};

const validFalsePositive = {
  reportType: 'false_positive',
  rootCause: 'filter_false_positive',
  journeyStage: 'internet',
  deviceClass: 'iphone',
  diagnosticHostname: 'Example.COM.',
};

test('accepts only the minimal categorical support contract and normalizes bounded diagnostics', async () => {
  const api = await loadSupportApi();
  assert.equal(api.SUPPORT_CAPTURE_MAX_AGE_MS, 24 * 60 * 60 * 1000);

  const feedback = api.parseSupportCapture(validFeedback);
  assert.deepEqual(feedback, validFeedback);

  const falsePositive = api.parseSupportCapture(validFalsePositive);
  assert.equal(falsePositive.diagnosticHostname, 'example.com');
  assert.deepEqual(Object.keys(falsePositive).sort(), [
    'deviceClass',
    'diagnosticHostname',
    'journeyStage',
    'reportType',
    'rootCause',
  ]);

  assert.deepEqual(api.toSupportMetricDimensions(falsePositive), {
    reportType: 'false_positive',
    rootCause: 'filter_false_positive',
    journeyStage: 'internet',
    deviceClass: 'iphone',
  });
});

test('fails closed on free text, identity, browsing fields, arbitrary keys, and URL-shaped diagnostics', async () => {
  const api = await loadSupportApi();
  for (const forbiddenField of [
    'details',
    'message',
    'email',
    'accountId',
    'childId',
    'ipAddress',
    'queryHistory',
    'browsingHistory',
    'url',
  ]) {
    assert.throws(
      () => api.parseSupportCapture({ ...validFeedback, [forbiddenField]: 'x' }),
      /invalid support capture/i,
      forbiddenField,
    );
  }

  assert.throws(
    () => api.parseSupportCapture({ ...validFalsePositive, diagnosticHostname: 'https://example.com/path?q=child' }),
    /invalid support capture/i,
  );
  assert.throws(
    () => api.parseSupportCapture({ ...validFeedback, diagnosticHostname: 'example.com' }),
    /invalid support capture/i,
  );
  assert.throws(
    () => api.parseSupportCapture({ ...validFalsePositive, diagnosticHostname: 'a'.repeat(254) }),
    /invalid support capture/i,
  );
});

test('root-cause categories are fixed, metric-safe, and report-type compatibility is enforced', async () => {
  const api = await loadSupportApi();
  assert.deepEqual(api.SUPPORT_REPORT_TYPES, ['support', 'feedback', 'false_positive', 'abandonment']);
  assert.deepEqual(api.SUPPORT_ROOT_CAUSES, [
    'instructions_unclear',
    'unsupported_or_compatibility',
    'verification_failed',
    'filter_false_positive',
    'network_conflict',
    'privacy_concern',
    'other',
  ]);
  assert.throws(
    () => api.parseSupportCapture({ ...validFeedback, rootCause: 'filter_false_positive' }),
    /invalid support capture/i,
  );
  assert.throws(
    () => api.parseSupportCapture({ ...validFalsePositive, rootCause: 'instructions_unclear' }),
    /invalid support capture/i,
  );
  assert.throws(
    () => api.parseSupportCapture({ ...validFeedback, reportType: 'incident' }),
    /invalid support capture/i,
  );
});

test('transient capture expires without sliding and opaque deletion receipt removes the record', async () => {
  const api = await loadSupportApi();
  const ids = ['01234567-89ab-4def-8123-456789abcdef'];
  const store = api.createSupportCaptureStore({
    createId: () => ids.shift(),
    maxRecords: 4,
  });

  const created = store.capture(validFalsePositive, now);
  assert.match(created.receiptId, /^[0-9a-f-]{36}$/);
  assert.equal(created.expiresAt, now + api.SUPPORT_CAPTURE_MAX_AGE_MS);
  assert.equal(store.size(now), 1);
  assert.equal(store.delete(created.receiptId, now + 1), true);
  assert.equal(store.delete(created.receiptId, now + 2), false);
  assert.equal(store.size(now + 2), 0);

  const expiringStore = api.createSupportCaptureStore({
    createId: () => '11111111-2222-4333-8444-555555555555',
    maxRecords: 4,
  });
  const expiring = expiringStore.capture(validFeedback, now);
  assert.equal(expiringStore.size(expiring.expiresAt - 1), 1);
  assert.equal(expiringStore.size(expiring.expiresAt), 0);
  assert.equal(expiringStore.delete(expiring.receiptId, expiring.expiresAt), false);
});

test('capacity is bounded and does not create a hidden persistent support database', async () => {
  const api = await loadSupportApi();
  let idCounter = 0;
  const store = api.createSupportCaptureStore({
    createId: () => `${String(idCounter++).padStart(8, '0')}-1111-4111-8111-111111111111`,
    maxRecords: 2,
  });
  store.capture(validFeedback, now);
  store.capture({ ...validFeedback, reportType: 'support' }, now + 1);
  assert.throws(() => store.capture(validFeedback, now + 2), /support capture capacity reached/i);
  assert.equal(store.size(now + 2), 2);

  const source = readFileSync(supportPath, 'utf8');
  assert.doesNotMatch(source, /localStorage|indexedDB|from ['"]node:fs['"]|writeFile|appendFile|sqlite|postgres|mysql/i);
});

test('privacy notice and no-store POST/DELETE route are present, default-off, and expose no public listing endpoint', async () => {
  const api = await loadSupportApi();
  assert.match(api.SUPPORT_CAPTURE_PRIVACY_NOTICE, /24 hours/i);
  assert.match(api.SUPPORT_CAPTURE_PRIVACY_NOTICE, /delete/i);
  assert.match(api.SUPPORT_CAPTURE_PRIVACY_NOTICE, /not.*browsing history/i);

  const routeSource = readFileSync(routePath, 'utf8');
  assert.match(routeSource, /export\s+async\s+function\s+POST/);
  assert.match(routeSource, /export\s+async\s+function\s+DELETE/);
  assert.doesNotMatch(routeSource, /export\s+async\s+function\s+GET/);
  assert.match(routeSource, /readBoundedUtf8Body/);
  assert.match(routeSource, /Cache-Control['"\s,:]+no-store/i);
  assert.match(routeSource, /USESAFEWEB_SUPPORT_CAPTURE_ENABLED/);
  assert.match(routeSource, /SUPPORT_CAPTURE_DISABLED/);
  assert.doesNotMatch(routeSource, /console\.(?:log|info|debug)\s*\(/);
});
