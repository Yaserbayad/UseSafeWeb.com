import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { stripTypeScriptTypes } from 'node:module';

const root = resolve(import.meta.dirname, '../..');
const eventsPath = resolve(root, 'src/lib/product-events.ts');
const routePath = resolve(root, 'src/app/api/product-events/route.ts');
const dataUrl = (source) => `data:text/javascript;base64,${Buffer.from(source).toString('base64')}`;
const UUID_A = '01234567-89ab-4def-8123-456789abcdef';
const UUID_B = '11111111-2222-4333-8444-555555555555';
const UUID_C = 'aaaaaaaa-bbbb-4ccc-8ddd-eeeeeeeeeeee';
const OCCURRED_AT = '2026-09-03T09:00:00.000Z';

async function loadEventsApi() {
  const source = readFileSync(eventsPath, 'utf8');
  return import(dataUrl(stripTypeScriptTypes(source, { mode: 'strip' })));
}

function common(event_name, event_id = UUID_A, surface = 'setup_web') {
  return {
    event_name,
    schema_version: '1.0.1',
    event_id,
    occurred_at: OCCURRED_AT,
    release_id: 'web-2026.09.03',
    surface,
  };
}

const journeyStarted = {
  ...common('journey_started'),
  journey_session_id: UUID_B,
  route_id: 'manual_dns',
  platform_class: 'android',
  locale_code: 'en-GB',
  channel_source_class: 'direct',
};

const stepEntered = {
  ...common('journey_step_entered', UUID_C),
  journey_session_id: UUID_B,
  step_id: 'phone',
  route_id: 'manual_dns',
};

test('accepts exactly the twelve TSK-0498 event names and produces non-linkable aggregate dimensions', async () => {
  const api = await loadEventsApi();
  assert.deepEqual(api.PRODUCT_EVENT_NAMES, [
    'journey_started', 'journey_step_entered', 'journey_step_outcome', 'journey_completed',
    'protection_state_evaluated', 'protection_verification_outcome', 'self_service_opened',
    'self_service_outcome', 'synthetic_service_probe_result', 'recovery_operation_outcome',
    'channel_entry', 'cost_period_recorded',
  ]);
  assert.deepEqual(api.parseProductEvent(journeyStarted), journeyStarted);
  const aggregate = api.toProductAggregateDimensions(api.parseProductEvent(journeyStarted));
  assert.equal(aggregate.event_name, 'journey_started');
  assert.equal(aggregate.route_id, 'manual_dns');
  assert.equal(aggregate.platform_class, 'android');
  assert.equal(aggregate.locale_code, 'en-GB');
  assert.equal(aggregate.channel_source_class, 'direct');
  for (const key of ['event_id', 'journey_session_id', 'occurred_at']) assert.equal(key in aggregate, false, key);
});

test('rejects unknown events, arbitrary fields, identity, browsing, DNS/query, content, secret and free-text payloads', async () => {
  const api = await loadEventsApi();
  assert.throws(() => api.parseProductEvent({ ...journeyStarted, event_name: 'page_view' }), /invalid product event/i);
  for (const field of [
    'domain', 'url', 'dns_query', 'queryHistory', 'browsingHistory', 'childId', 'childName',
    'accountId', 'email', 'providerSubject', 'deviceId', 'clientId', 'ipAddress', 'referrer',
    'message', 'freeText', 'rawToken', 'authorization', 'cookie', 'content',
  ]) {
    assert.throws(() => api.parseProductEvent({ ...journeyStarted, [field]: 'x' }), /invalid product event/i, field);
  }
});

test('preserves six protection states and never converts parent confirmation into positive technical verification', async () => {
  const api = await loadEventsApi();
  assert.deepEqual(api.PROTECTION_STATES, [
    'protected_verified', 'configured_parent_confirmed', 'action_needed',
    'not_covered', 'uncertain_error', 'removed',
  ]);
  const stateEvent = {
    ...common('protection_state_evaluated', UUID_A, 'verification'),
    journey_session_id: UUID_B,
    layer_id: 'internet', state: 'configured_parent_confirmed', reason_code: 'parent_confirmed', copy_version: '1.0.0',
  };
  assert.equal(api.parseProductEvent(stateEvent).state, 'configured_parent_confirmed');
  const verifierEvent = {
    ...common('protection_verification_outcome', UUID_C, 'verification'),
    journey_session_id: UUID_B,
    layer_id: 'internet', verifier_id: 'dns-path', verifier_version: '1.0.0',
    result: 'positive', reason_code: 'parent_confirmed', duration_bucket_ms: 'lt_1000',
  };
  assert.throws(() => api.parseProductEvent(verifierEvent), /invalid product event/i);
});

test('enforces non-sliding 24h accountless retention, 30d synthetic retention, conservative 13m cost retention, dedupe and deletion', async () => {
  const api = await loadEventsApi();
  assert.equal(api.ACCOUNTLESS_RAW_MAX_AGE_MS, 24 * 60 * 60 * 1000);
  assert.equal(api.SYNTHETIC_RAW_MAX_AGE_MS, 30 * 24 * 60 * 60 * 1000);
  assert.ok(api.MEASUREMENT_MAX_AGE_MS <= 13 * 30 * 24 * 60 * 60 * 1000, 'fixed-duration measurement retention must not exceed the conservative 13-month bound');
  const store = api.createProductEventStore({ maxRecords: 4 });
  const t0 = Date.parse(OCCURRED_AT);
  const first = store.capture(journeyStarted, t0);
  const second = store.capture(stepEntered, t0 + 60 * 60 * 1000);
  assert.equal(first.expiresAt, t0 + api.ACCOUNTLESS_RAW_MAX_AGE_MS);
  assert.equal(second.expiresAt, first.expiresAt);
  assert.equal(store.capture(journeyStarted, t0 + 2), null);
  assert.equal(store.delete(UUID_C, t0 + 3), true);
  assert.equal(store.delete(UUID_C, t0 + 4), false);
  assert.equal(store.size(first.expiresAt), 0);

  const synthetic = {
    ...common('synthetic_service_probe_result', UUID_A, 'synthetic_probe'),
    component: 'public_web', probe_region: 'westeurope', result: 'success', error_class: 'none',
    duration_bucket_ms: 'lt_1000', probe_version: '1.0.0',
  };
  assert.equal(api.rawRetentionMs(api.parseProductEvent(synthetic)), api.SYNTHETIC_RAW_MAX_AGE_MS);
  const cost = {
    ...common('cost_period_recorded', UUID_C, 'internal_finance'),
    period_id: '2026-09', cost_category: 'hosting', provider_or_source_class: 'azure', currency: 'EUR',
    amount_minor_units: 1234, source_reference: 'invoice-2026-09', cost_model_version: '1.0.0',
  };
  assert.equal(api.rawRetentionMs(api.parseProductEvent(cost)), api.MEASUREMENT_MAX_AGE_MS);
  assert.throws(() => api.parseProductEvent({ ...cost, journey_session_id: UUID_B }), /invalid product event/i);
});

test('client timestamps cannot extend raw retention and deletion cannot reset an accountless session hard-expiry', async () => {
  const api = await loadEventsApi();
  const t0 = Date.parse(OCCURRED_AT);

  const futureStore = api.createProductEventStore({ maxRecords: 4 });
  const future = futureStore.capture({
    ...journeyStarted,
    occurred_at: new Date(t0 + 48 * 60 * 60 * 1000).toISOString(),
  }, t0);
  assert.ok(future.expiresAt <= t0 + api.ACCOUNTLESS_RAW_MAX_AGE_MS, 'client-controlled occurred_at must not extend retention beyond receipt time + TTL');

  const resetStore = api.createProductEventStore({ maxRecords: 4 });
  const original = resetStore.capture(journeyStarted, t0);
  assert.equal(resetStore.delete(UUID_A, t0 + 60 * 60 * 1000), true);
  const later = resetStore.capture({
    ...stepEntered,
    occurred_at: new Date(t0 + 12 * 60 * 60 * 1000).toISOString(),
  }, t0 + 12 * 60 * 60 * 1000);
  assert.equal(later.expiresAt, original.expiresAt, 'deleting the last raw record must not reset the originating session TTL');
});

test('requires complete KPI metadata and refuses to manufacture percentages without a usable denominator', async () => {
  const api = await loadEventsApi();
  const metric = api.parseMetricDefinition({
    metric_id: 'accountless_completion_rate',
    source_events: ['journey_started', 'journey_completed'],
    formula: 'journey_completed / journey_started',
    numerator_event: 'journey_completed', denominator_event: 'journey_started',
    time_window: 'release_window', release_or_cohort: 'release_id', owner: 'Product Analytics/Product',
    guardrail: 'completion does not imply verified protection', decision_action: 'investigate material route friction',
  });
  assert.deepEqual(api.computeRateMetric(metric, { journey_started: 10, journey_completed: 7 }), {
    numerator: 7, denominator: 10, value: 0.7, missing_denominator: false,
  });
  assert.deepEqual(api.computeRateMetric(metric, { journey_completed: 7 }), {
    numerator: 7, denominator: null, value: null, missing_denominator: true,
  });
  assert.deepEqual(api.computeRateMetric(metric, { journey_started: 0, journey_completed: 0 }), {
    numerator: 0, denominator: 0, value: null, missing_denominator: false,
  });
  assert.throws(() => api.parseMetricDefinition({ ...metric, owner: '', extra: 'x' }), /invalid metric definition/i);
});

test('route is bounded, no-store, default-off, non-listing and contains no third-party analytics or payload logging', () => {
  const routeSource = readFileSync(routePath, 'utf8');
  assert.match(routeSource, /export\s+async\s+function\s+POST/);
  assert.match(routeSource, /export\s+async\s+function\s+DELETE/);
  assert.doesNotMatch(routeSource, /export\s+async\s+function\s+GET/);
  assert.match(routeSource, /readBoundedUtf8Body/);
  assert.match(routeSource, /Cache-Control['"\s,:]+no-store/i);
  assert.match(routeSource, /USESAFEWEB_PRODUCT_EVENTS_ENABLED/);
  assert.match(routeSource, /PRODUCT_EVENTS_DISABLED/);
  assert.doesNotMatch(routeSource, /google-analytics|segment|mixpanel|amplitude|posthog|gtag|analytics\.track/i);
  assert.doesNotMatch(routeSource, /console\.(?:log|info|debug)\s*\(/);
});
