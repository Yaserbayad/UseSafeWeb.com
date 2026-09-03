import { randomUUID } from 'node:crypto';

export const SUPPORT_CAPTURE_MAX_AGE_MS = 24 * 60 * 60 * 1000;
export const SUPPORT_CAPTURE_MAX_HTTP_BODY_BYTES = 2048;

export const SUPPORT_REPORT_TYPES = ['support', 'feedback', 'false_positive', 'abandonment'] as const;
export const SUPPORT_ROOT_CAUSES = [
  'instructions_unclear',
  'unsupported_or_compatibility',
  'verification_failed',
  'filter_false_positive',
  'network_conflict',
  'privacy_concern',
  'other',
] as const;
export const SUPPORT_JOURNEY_STAGES = ['phone', 'internet', 'services'] as const;
export const SUPPORT_DEVICE_CLASSES = ['android', 'iphone', 'other_supported', 'unknown'] as const;

export const SUPPORT_CAPTURE_PRIVACY_NOTICE =
  'We keep this support report in temporary server memory for no more than 24 hours. A false-positive report may include one hostname and a coarse device type only for diagnosis; it is not used as browsing history. Keep the receipt to delete the report sooner.';

type SupportReportType = (typeof SUPPORT_REPORT_TYPES)[number];
type SupportRootCause = (typeof SUPPORT_ROOT_CAUSES)[number];
type SupportJourneyStage = (typeof SUPPORT_JOURNEY_STAGES)[number];
type SupportDeviceClass = (typeof SUPPORT_DEVICE_CLASSES)[number];

export type SupportCapture = {
  reportType: SupportReportType;
  rootCause: SupportRootCause;
  journeyStage: SupportJourneyStage;
  deviceClass?: SupportDeviceClass;
  diagnosticHostname?: string;
};

export type SupportMetricDimensions = Omit<SupportCapture, 'diagnosticHostname'>;

export type SupportCaptureReceipt = {
  receiptId: string;
  expiresAt: number;
};

type StoredSupportCapture = {
  capture: SupportCapture;
  createdAt: number;
  expiresAt: number;
};

type StoreOptions = {
  createId?: () => string | undefined;
  maxRecords?: number;
};

const UUID_V4 = /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/;
const ALLOWED_FIELDS = new Set([
  'reportType',
  'rootCause',
  'journeyStage',
  'deviceClass',
  'diagnosticHostname',
]);

function invalidCapture(): never {
  throw new TypeError('invalid support capture');
}

function isPlainRecord(value: unknown): value is Record<string, unknown> {
  if (!value || typeof value !== 'object' || Array.isArray(value)) return false;
  const prototype = Object.getPrototypeOf(value);
  return prototype === Object.prototype || prototype === null;
}

function isEnumValue<T extends readonly string[]>(values: T, value: unknown): value is T[number] {
  return typeof value === 'string' && values.includes(value as T[number]);
}

function normalizeDiagnosticHostname(value: unknown): string | null {
  if (typeof value !== 'string' || value.length < 3 || value.length > 254 || value !== value.trim()) return null;
  let hostname = value.toLowerCase();
  if (hostname.endsWith('.')) hostname = hostname.slice(0, -1);
  if (hostname.length < 3 || hostname.length > 253) return null;
  if (/^\d{1,3}(?:\.\d{1,3}){3}$/.test(hostname)) return null;

  const labels = hostname.split('.');
  if (labels.length < 2) return null;
  for (const label of labels) {
    if (label.length < 1 || label.length > 63) return null;
    if (!/^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$/.test(label)) return null;
  }
  return hostname;
}

function validateNow(now: number): void {
  if (!Number.isSafeInteger(now) || now < 0) throw new TypeError('invalid support capture time');
}

export function isSupportReceiptId(value: unknown): value is string {
  return typeof value === 'string' && UUID_V4.test(value);
}

export function parseSupportCapture(value: unknown): SupportCapture {
  if (!isPlainRecord(value)) return invalidCapture();
  const keys = Object.keys(value);
  if (keys.some((key) => !ALLOWED_FIELDS.has(key))) return invalidCapture();

  const { reportType, rootCause, journeyStage, deviceClass, diagnosticHostname } = value;
  if (!isEnumValue(SUPPORT_REPORT_TYPES, reportType)) return invalidCapture();
  if (!isEnumValue(SUPPORT_ROOT_CAUSES, rootCause)) return invalidCapture();
  if (!isEnumValue(SUPPORT_JOURNEY_STAGES, journeyStage)) return invalidCapture();
  if (deviceClass !== undefined && !isEnumValue(SUPPORT_DEVICE_CLASSES, deviceClass)) return invalidCapture();

  const isFalsePositive = reportType === 'false_positive';
  if (isFalsePositive !== (rootCause === 'filter_false_positive')) return invalidCapture();

  let normalizedHostname: string | undefined;
  if (isFalsePositive) {
    const normalized = normalizeDiagnosticHostname(diagnosticHostname);
    if (!normalized) return invalidCapture();
    normalizedHostname = normalized;
  } else if (diagnosticHostname !== undefined) {
    return invalidCapture();
  }

  const parsed: SupportCapture = { reportType, rootCause, journeyStage };
  if (deviceClass !== undefined) parsed.deviceClass = deviceClass;
  if (normalizedHostname !== undefined) parsed.diagnosticHostname = normalizedHostname;
  return parsed;
}

export function toSupportMetricDimensions(value: unknown): SupportMetricDimensions {
  const parsed = parseSupportCapture(value);
  const dimensions: SupportMetricDimensions = {
    reportType: parsed.reportType,
    rootCause: parsed.rootCause,
    journeyStage: parsed.journeyStage,
  };
  if (parsed.deviceClass !== undefined) dimensions.deviceClass = parsed.deviceClass;
  return dimensions;
}

export class SupportCaptureCapacityError extends Error {
  constructor() {
    super('support capture capacity reached');
    this.name = 'SupportCaptureCapacityError';
  }
}

export function createSupportCaptureStore(options: StoreOptions = {}) {
  const createId = options.createId ?? randomUUID;
  const maxRecords = options.maxRecords ?? 256;
  if (!Number.isSafeInteger(maxRecords) || maxRecords < 1 || maxRecords > 4096) {
    throw new TypeError('invalid support capture capacity');
  }

  const records = new Map<string, StoredSupportCapture>();

  function purge(now: number): void {
    validateNow(now);
    for (const [receiptId, record] of records) {
      if (record.expiresAt <= now) records.delete(receiptId);
    }
  }

  return {
    capture(value: unknown, now = Date.now()): SupportCaptureReceipt {
      validateNow(now);
      const capture = parseSupportCapture(value);
      purge(now);
      if (records.size >= maxRecords) throw new SupportCaptureCapacityError();

      const receiptId = createId();
      if (!isSupportReceiptId(receiptId) || records.has(receiptId)) {
        throw new TypeError('invalid support capture receipt');
      }

      const expiresAt = now + SUPPORT_CAPTURE_MAX_AGE_MS;
      if (!Number.isSafeInteger(expiresAt)) throw new TypeError('invalid support capture expiry');
      records.set(receiptId, { capture, createdAt: now, expiresAt });
      return { receiptId, expiresAt };
    },

    delete(receiptId: unknown, now = Date.now()): boolean {
      validateNow(now);
      purge(now);
      if (!isSupportReceiptId(receiptId)) return false;
      return records.delete(receiptId);
    },

    size(now = Date.now()): number {
      purge(now);
      return records.size;
    },
  };
}
