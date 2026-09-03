export const PRODUCT_EVENT_SCHEMA_VERSION = '1.0.1' as const;
export const ACCOUNTLESS_RAW_MAX_AGE_MS = 24 * 60 * 60 * 1000;
export const SYNTHETIC_RAW_MAX_AGE_MS = 30 * 24 * 60 * 60 * 1000;
export const MEASUREMENT_MAX_AGE_MS = 13 * 31 * 24 * 60 * 60 * 1000;
export const PRODUCT_EVENT_MAX_HTTP_BODY_BYTES = 4096;

export const PRODUCT_EVENT_NAMES = [
  'journey_started',
  'journey_step_entered',
  'journey_step_outcome',
  'journey_completed',
  'protection_state_evaluated',
  'protection_verification_outcome',
  'self_service_opened',
  'self_service_outcome',
  'synthetic_service_probe_result',
  'recovery_operation_outcome',
  'channel_entry',
  'cost_period_recorded',
] as const;

export const PROTECTION_STATES = [
  'protected_verified',
  'configured_parent_confirmed',
  'action_needed',
  'not_covered',
  'uncertain_error',
  'removed',
] as const;

const ACCOUNTLESS_EVENTS = new Set<string>([
  'journey_started',
  'journey_step_entered',
  'journey_step_outcome',
  'journey_completed',
  'protection_state_evaluated',
  'protection_verification_outcome',
  'self_service_opened',
  'self_service_outcome',
  'channel_entry',
]);
const SYNTHETIC_EVENTS = new Set<string>(['synthetic_service_probe_result', 'recovery_operation_outcome']);
const EVENT_NAMES = new Set<string>(PRODUCT_EVENT_NAMES);
const SURFACES = new Set(['public_web', 'setup_web', 'verification', 'self_service', 'synthetic_probe', 'internal_finance']);
const PROTECTION_STATE_SET = new Set<string>(PROTECTION_STATES);
const UUID_V4 = /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
const TOKEN = /^[a-zA-Z0-9][a-zA-Z0-9._:-]{0,95}$/;
const LOWER_TOKEN = /^[a-z0-9][a-z0-9_:-]{0,63}$/;
const LOCALE = /^[a-z]{2,3}(?:-[A-Z]{2})?$/;
const CURRENCY = /^[A-Z]{3}$/;

const commonKeys = ['event_name', 'schema_version', 'event_id', 'occurred_at', 'release_id', 'surface'] as const;
const eventKeys: Record<string, readonly string[]> = {
  journey_started: [...commonKeys, 'journey_session_id', 'route_id', 'platform_class', 'locale_code', 'channel_source_class'],
  journey_step_entered: [...commonKeys, 'journey_session_id', 'step_id', 'route_id'],
  journey_step_outcome: [...commonKeys, 'journey_session_id', 'step_id', 'outcome', 'reason_code', 'route_id'],
  journey_completed: [...commonKeys, 'journey_session_id', 'route_id', 'completion_variant'],
  protection_state_evaluated: [...commonKeys, 'journey_session_id', 'layer_id', 'state', 'reason_code', 'verifier_version', 'copy_version'],
  protection_verification_outcome: [...commonKeys, 'journey_session_id', 'layer_id', 'verifier_id', 'verifier_version', 'result', 'reason_code', 'duration_bucket_ms'],
  self_service_opened: [...commonKeys, 'journey_session_id', 'topic_id', 'entry_surface', 'protection_state_at_entry'],
  self_service_outcome: [...commonKeys, 'journey_session_id', 'topic_id', 'outcome', 'reason_code'],
  synthetic_service_probe_result: [...commonKeys, 'component', 'probe_region', 'result', 'error_class', 'duration_bucket_ms', 'probe_version'],
  recovery_operation_outcome: [...commonKeys, 'operation_type', 'result', 'failure_class', 'duration_bucket_ms', 'runbook_version'],
  channel_entry: [...commonKeys, 'journey_session_id', 'source_class', 'campaign_key', 'partner_key'],
  cost_period_recorded: [...commonKeys, 'period_id', 'cost_category', 'provider_or_source_class', 'currency', 'amount_minor_units', 'source_reference', 'cost_model_version'],
};

const requiredEventKeys: Record<string, readonly string[]> = {
  journey_started: [...commonKeys, 'journey_session_id', 'route_id', 'platform_class', 'locale_code'],
  journey_step_entered: [...commonKeys, 'journey_session_id', 'step_id', 'route_id'],
  journey_step_outcome: [...commonKeys, 'journey_session_id', 'step_id', 'outcome', 'reason_code', 'route_id'],
  journey_completed: [...commonKeys, 'journey_session_id', 'route_id', 'completion_variant'],
  protection_state_evaluated: [...commonKeys, 'journey_session_id', 'layer_id', 'state', 'reason_code', 'copy_version'],
  protection_verification_outcome: [...commonKeys, 'journey_session_id', 'layer_id', 'verifier_id', 'verifier_version', 'result', 'reason_code', 'duration_bucket_ms'],
  self_service_opened: [...commonKeys, 'journey_session_id', 'topic_id', 'entry_surface'],
  self_service_outcome: [...commonKeys, 'journey_session_id', 'topic_id', 'outcome'],
  synthetic_service_probe_result: [...commonKeys, 'component', 'probe_region', 'result', 'error_class', 'duration_bucket_ms', 'probe_version'],
  recovery_operation_outcome: [...commonKeys, 'operation_type', 'result', 'failure_class', 'duration_bucket_ms', 'runbook_version'],
  channel_entry: [...commonKeys, 'journey_session_id', 'source_class'],
  cost_period_recorded: [...commonKeys, 'period_id', 'cost_category', 'provider_or_source_class', 'currency', 'amount_minor_units', 'source_reference', 'cost_model_version'],
};

function isRecord(input: unknown): input is Record<string, unknown> {
  return !!input && typeof input === 'object' && !Array.isArray(input);
}

function invalid(): never {
  throw new TypeError('Invalid product event.');
}

function exactKeys(record: Record<string, unknown>, allowed: readonly string[], required: readonly string[]): void {
  const allowedSet = new Set(allowed);
  if (Object.keys(record).some((key) => !allowedSet.has(key))) invalid();
  if (required.some((key) => !(key in record))) invalid();
}

function boundedToken(value: unknown, pattern: RegExp = TOKEN): string {
  if (typeof value !== 'string' || !pattern.test(value)) invalid();
  return value;
}

function boundedEnum(value: unknown, values: readonly string[]): string {
  if (typeof value !== 'string' || !values.includes(value)) invalid();
  return value;
}

function validateCommon(record: Record<string, unknown>): void {
  if (!EVENT_NAMES.has(String(record.event_name))) invalid();
  if (record.schema_version !== PRODUCT_EVENT_SCHEMA_VERSION) invalid();
  if (typeof record.event_id !== 'string' || !UUID_V4.test(record.event_id)) invalid();
  if (typeof record.occurred_at !== 'string' || !/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{3})?Z$/.test(record.occurred_at) || !Number.isFinite(Date.parse(record.occurred_at))) invalid();
  boundedToken(record.release_id);
  if (typeof record.surface !== 'string' || !SURFACES.has(record.surface)) invalid();
  if (ACCOUNTLESS_EVENTS.has(String(record.event_name))) {
    if (typeof record.journey_session_id !== 'string' || !UUID_V4.test(record.journey_session_id)) invalid();
  } else if ('journey_session_id' in record) invalid();
}

function validateEventSpecific(record: Record<string, unknown>): void {
  switch (record.event_name) {
    case 'journey_started':
      boundedToken(record.route_id); boundedToken(record.platform_class, LOWER_TOKEN); boundedToken(record.locale_code, LOCALE);
      if ('channel_source_class' in record) boundedEnum(record.channel_source_class, ['direct', 'organic_search', 'school_partner', 'referral', 'owned', 'approved_test', 'unknown']);
      break;
    case 'journey_step_entered':
      boundedToken(record.step_id, LOWER_TOKEN); boundedToken(record.route_id); break;
    case 'journey_step_outcome':
      boundedToken(record.step_id, LOWER_TOKEN); boundedEnum(record.outcome, ['completed', 'failed', 'skipped', 'unsupported', 'retry']); boundedToken(record.reason_code, LOWER_TOKEN); boundedToken(record.route_id); break;
    case 'journey_completed':
      boundedToken(record.route_id); boundedToken(record.completion_variant, LOWER_TOKEN); break;
    case 'protection_state_evaluated':
      boundedToken(record.layer_id, LOWER_TOKEN); boundedEnum(record.state, PROTECTION_STATES); boundedToken(record.reason_code, LOWER_TOKEN); boundedToken(record.copy_version);
      if ('verifier_version' in record) boundedToken(record.verifier_version);
      break;
    case 'protection_verification_outcome': {
      boundedToken(record.layer_id, LOWER_TOKEN); boundedToken(record.verifier_id); boundedToken(record.verifier_version); boundedEnum(record.result, ['positive', 'negative', 'indeterminate', 'error']); const reason = boundedToken(record.reason_code, LOWER_TOKEN); boundedToken(record.duration_bucket_ms, LOWER_TOKEN);
      if (record.result === 'positive' && /parent|confirm/.test(reason)) invalid();
      break;
    }
    case 'self_service_opened':
      boundedToken(record.topic_id); boundedToken(record.entry_surface); if ('protection_state_at_entry' in record && !PROTECTION_STATE_SET.has(String(record.protection_state_at_entry))) invalid(); break;
    case 'self_service_outcome':
      boundedToken(record.topic_id); boundedEnum(record.outcome, ['resolved_reported', 'unresolved_reported', 'escalated', 'abandoned', 'unknown']); if ('reason_code' in record) boundedToken(record.reason_code, LOWER_TOKEN); break;
    case 'synthetic_service_probe_result':
      boundedToken(record.component); boundedToken(record.probe_region); boundedEnum(record.result, ['success', 'failure', 'timeout', 'degraded']); boundedToken(record.error_class, LOWER_TOKEN); boundedToken(record.duration_bucket_ms, LOWER_TOKEN); boundedToken(record.probe_version); break;
    case 'recovery_operation_outcome':
      boundedToken(record.operation_type); boundedEnum(record.result, ['success', 'failed', 'partial', 'rolled_back']); boundedToken(record.failure_class, LOWER_TOKEN); boundedToken(record.duration_bucket_ms, LOWER_TOKEN); boundedToken(record.runbook_version); break;
    case 'channel_entry':
      boundedEnum(record.source_class, ['direct', 'organic_search', 'school_partner', 'referral', 'owned', 'approved_test', 'unknown']); if ('campaign_key' in record) boundedToken(record.campaign_key); if ('partner_key' in record) boundedToken(record.partner_key); break;
    case 'cost_period_recorded':
      boundedToken(record.period_id); boundedToken(record.cost_category, LOWER_TOKEN); boundedToken(record.provider_or_source_class); boundedToken(record.currency, CURRENCY); if (!Number.isSafeInteger(record.amount_minor_units) || Number(record.amount_minor_units) < 0) invalid(); boundedToken(record.source_reference); boundedToken(record.cost_model_version); break;
    default:
      invalid();
  }
}

export type ProductEvent = Record<string, unknown> & { event_name: string; event_id: string; occurred_at: string; release_id: string; surface: string };

export function parseProductEvent(input: unknown): ProductEvent {
  if (!isRecord(input)) invalid();
  const eventName = String(input.event_name ?? '');
  if (!EVENT_NAMES.has(eventName)) invalid();
  exactKeys(input, eventKeys[eventName], requiredEventKeys[eventName]);
  validateCommon(input);
  validateEventSpecific(input);
  return { ...input } as ProductEvent;
}

export function rawRetentionMs(event: ProductEvent): number {
  if (ACCOUNTLESS_EVENTS.has(event.event_name)) return ACCOUNTLESS_RAW_MAX_AGE_MS;
  if (SYNTHETIC_EVENTS.has(event.event_name)) return SYNTHETIC_RAW_MAX_AGE_MS;
  if (event.event_name === 'cost_period_recorded') return MEASUREMENT_MAX_AGE_MS;
  return ACCOUNTLESS_RAW_MAX_AGE_MS;
}

const AGGREGATE_DROP = new Set(['event_id', 'occurred_at', 'journey_session_id', 'source_reference']);
export function toProductAggregateDimensions(event: ProductEvent): Record<string, unknown> {
  const output: Record<string, unknown> = {};
  for (const [key, value] of Object.entries(event)) {
    if (!AGGREGATE_DROP.has(key)) output[key] = value;
  }
  return output;
}

export class ProductEventCapacityError extends Error {
  constructor() { super('Product event capacity reached.'); }
}

type StoredEvent = { event: ProductEvent; expiresAt: number };
export function createProductEventStore(options: { maxRecords?: number } = {}) {
  const maxRecords = options.maxRecords ?? 1024;
  if (!Number.isSafeInteger(maxRecords) || maxRecords < 1 || maxRecords > 10000) throw new TypeError('Invalid product event capacity.');
  const records = new Map<string, StoredEvent>();
  const sessionExpiry = new Map<string, number>();

  function cleanup(now: number): void {
    for (const [eventId, stored] of records) if (now >= stored.expiresAt) records.delete(eventId);
    const liveSessions = new Set<string>();
    for (const stored of records.values()) {
      const sessionId = stored.event.journey_session_id;
      if (typeof sessionId === 'string') liveSessions.add(sessionId);
    }
    for (const [sessionId, expiresAt] of sessionExpiry) if (now >= expiresAt || !liveSessions.has(sessionId)) sessionExpiry.delete(sessionId);
  }

  return {
    capture(input: unknown, now = Date.now()): { eventId: string; expiresAt: number } | null {
      cleanup(now);
      const event = parseProductEvent(input);
      if (records.has(event.event_id)) return null;
      if (records.size >= maxRecords) throw new ProductEventCapacityError();

      const occurredAt = Date.parse(event.occurred_at);
      let expiresAt = occurredAt + rawRetentionMs(event);
      const sessionId = event.journey_session_id;
      if (typeof sessionId === 'string') {
        const existing = sessionExpiry.get(sessionId);
        if (existing !== undefined) expiresAt = existing;
        else sessionExpiry.set(sessionId, expiresAt);
      }
      if (!Number.isFinite(expiresAt) || now >= expiresAt) invalid();
      records.set(event.event_id, { event, expiresAt });
      return { eventId: event.event_id, expiresAt };
    },
    delete(eventId: string, now = Date.now()): boolean {
      cleanup(now);
      if (!UUID_V4.test(eventId)) return false;
      return records.delete(eventId);
    },
    size(now = Date.now()): number { cleanup(now); return records.size; },
    aggregate(now = Date.now()): Record<string, unknown>[] {
      cleanup(now);
      return [...records.values()].map(({ event }) => toProductAggregateDimensions(event));
    },
  };
}

const METRIC_KEYS = [
  'metric_id', 'source_events', 'formula', 'numerator_event', 'denominator_event', 'time_window',
  'release_or_cohort', 'owner', 'guardrail', 'decision_action',
] as const;

export type MetricDefinition = {
  metric_id: string;
  source_events: string[];
  formula: string;
  numerator_event: string;
  denominator_event: string;
  time_window: string;
  release_or_cohort: string;
  owner: string;
  guardrail: string;
  decision_action: string;
};

function invalidMetric(): never { throw new TypeError('Invalid metric definition.'); }
function metricText(value: unknown): string {
  if (typeof value !== 'string' || value.length < 1 || value.length > 240 || /[\r\n]/.test(value)) invalidMetric();
  return value;
}

export function parseMetricDefinition(input: unknown): MetricDefinition {
  if (!isRecord(input)) invalidMetric();
  if (Object.keys(input).length !== METRIC_KEYS.length || METRIC_KEYS.some((key) => !(key in input)) || Object.keys(input).some((key) => !METRIC_KEYS.includes(key as typeof METRIC_KEYS[number]))) invalidMetric();
  if (!Array.isArray(input.source_events) || input.source_events.length < 1 || input.source_events.some((name) => typeof name !== 'string' || !EVENT_NAMES.has(name))) invalidMetric();
  const metric: MetricDefinition = {
    metric_id: metricText(input.metric_id),
    source_events: [...input.source_events] as string[],
    formula: metricText(input.formula),
    numerator_event: metricText(input.numerator_event),
    denominator_event: metricText(input.denominator_event),
    time_window: metricText(input.time_window),
    release_or_cohort: metricText(input.release_or_cohort),
    owner: metricText(input.owner),
    guardrail: metricText(input.guardrail),
    decision_action: metricText(input.decision_action),
  };
  if (!metric.source_events.includes(metric.numerator_event) || !metric.source_events.includes(metric.denominator_event)) invalidMetric();
  return metric;
}

export function computeRateMetric(metricInput: MetricDefinition, counts: Record<string, number>) {
  const metric = parseMetricDefinition(metricInput);
  const numeratorPresent = Object.prototype.hasOwnProperty.call(counts, metric.numerator_event);
  const denominatorPresent = Object.prototype.hasOwnProperty.call(counts, metric.denominator_event);
  const numerator = numeratorPresent ? counts[metric.numerator_event] : null;
  const denominator = denominatorPresent ? counts[metric.denominator_event] : null;
  for (const value of [numerator, denominator]) if (value !== null && (!Number.isSafeInteger(value) || value < 0)) invalidMetric();
  return {
    numerator,
    denominator,
    value: numerator !== null && denominator !== null && denominator > 0 ? numerator / denominator : null,
    missing_denominator: !denominatorPresent,
  };
}
