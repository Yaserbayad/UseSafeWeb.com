export const JOURNEY_STORAGE_KEY = 'usesafeweb:j0:v1';
export const JOURNEY_MAX_AGE_MS = 24 * 60 * 60 * 1000;

export type JourneyLocale = 'en-GB' | 'tr-TR' | 'ar';
export type JourneyStep = 'route' | 'native' | 'dns';
export type DeviceFamily = 'android' | 'iphone';
export type DnsMethod = 'android_private_dns_dot' | 'ios_doh_profile';

export type JourneyState = {
  schemaVersion: 1;
  scope: string;
  createdAt: number;
  hardExpiresAt: number;
  locale: JourneyLocale;
  journeyStep: JourneyStep;
  deviceFamily?: DeviceFamily;
  dnsMethod?: DnsMethod;
};

type StorageLike = Pick<Storage, 'getItem' | 'setItem' | 'removeItem'>;
type RandomFill = (bytes: Uint8Array) => Uint8Array;
type JourneyLocation = { pathname: string; platform: string | null };

const locales = new Set<JourneyLocale>(['en-GB', 'tr-TR', 'ar']);
const baseKeys = ['createdAt', 'hardExpiresAt', 'journeyStep', 'locale', 'schemaVersion', 'scope'];
const keysByStep: Record<JourneyStep, string[]> = {
  route: baseKeys,
  native: [...baseKeys, 'deviceFamily'],
  dns: [...baseKeys, 'deviceFamily', 'dnsMethod'],
};

function isLocale(value: unknown): value is JourneyLocale {
  return typeof value === 'string' && locales.has(value as JourneyLocale);
}

function isDeviceFamily(value: unknown): value is DeviceFamily {
  return value === 'android' || value === 'iphone';
}

function isDnsMethod(value: unknown): value is DnsMethod {
  return value === 'android_private_dns_dot' || value === 'ios_doh_profile';
}

function expectedDnsMethod(device: DeviceFamily): DnsMethod {
  return device === 'android' ? 'android_private_dns_dot' : 'ios_doh_profile';
}

function defaultRandomFill(bytes: Uint8Array): Uint8Array {
  globalThis.crypto.getRandomValues(bytes);
  return bytes;
}

function createScope(randomFill: RandomFill): string {
  const bytes = new Uint8Array(16);
  randomFill(bytes);
  return Array.from(bytes, (value) => value.toString(16).padStart(2, '0')).join('');
}

function hasExactKeys(value: Record<string, unknown>, step: JourneyStep): boolean {
  const actual = Object.keys(value).sort();
  const expected = [...keysByStep[step]].sort();
  return actual.length === expected.length && actual.every((key, index) => key === expected[index]);
}

function validateJourneyState(value: unknown, nowMs: number): JourneyState | null {
  if (!value || typeof value !== 'object' || Array.isArray(value)) return null;
  const candidate = value as Record<string, unknown>;
  if (candidate.schemaVersion !== 1) return null;
  if (typeof candidate.scope !== 'string' || !/^[0-9a-f]{32}$/.test(candidate.scope)) return null;
  if (!Number.isSafeInteger(candidate.createdAt) || !Number.isSafeInteger(candidate.hardExpiresAt)) return null;
  const createdAt = candidate.createdAt as number;
  const hardExpiresAt = candidate.hardExpiresAt as number;
  if (createdAt < 0 || hardExpiresAt <= createdAt) return null;
  if (hardExpiresAt - createdAt > JOURNEY_MAX_AGE_MS) return null;
  if (!Number.isSafeInteger(nowMs) || nowMs < createdAt || nowMs >= hardExpiresAt) return null;
  if (!isLocale(candidate.locale)) return null;
  if (candidate.journeyStep !== 'route' && candidate.journeyStep !== 'native' && candidate.journeyStep !== 'dns') return null;
  const step = candidate.journeyStep;
  if (!hasExactKeys(candidate, step)) return null;

  if (step === 'route') {
    return candidate as JourneyState;
  }
  if (!isDeviceFamily(candidate.deviceFamily)) return null;
  if (step === 'native') {
    return candidate as JourneyState;
  }
  if (!isDnsMethod(candidate.dnsMethod) || candidate.dnsMethod !== expectedDnsMethod(candidate.deviceFamily)) return null;
  return candidate as JourneyState;
}

export function createJourneyState(
  locale: JourneyLocale,
  nowMs: number,
  randomFill: RandomFill = defaultRandomFill,
): JourneyState {
  if (!isLocale(locale) || !Number.isSafeInteger(nowMs) || nowMs < 0) {
    throw new TypeError('invalid journey creation input');
  }
  return {
    schemaVersion: 1,
    scope: createScope(randomFill),
    createdAt: nowMs,
    hardExpiresAt: nowMs + JOURNEY_MAX_AGE_MS,
    locale,
    journeyStep: 'route',
  };
}

export function parseJourneyState(raw: string, nowMs: number): JourneyState | null {
  try {
    return validateJourneyState(JSON.parse(raw), nowMs);
  } catch {
    return null;
  }
}

export function readJourneyState(storage: StorageLike, nowMs: number): JourneyState | null {
  try {
    const raw = storage.getItem(JOURNEY_STORAGE_KEY);
    if (raw === null) return null;
    const state = parseJourneyState(raw, nowMs);
    if (state === null) storage.removeItem(JOURNEY_STORAGE_KEY);
    return state;
  } catch {
    return null;
  }
}

function writeJourneyState(storage: StorageLike, state: JourneyState): boolean {
  try {
    storage.setItem(JOURNEY_STORAGE_KEY, JSON.stringify(state));
    return true;
  } catch {
    return false;
  }
}

export function clearJourneyState(storage: StorageLike): void {
  try {
    storage.removeItem(JOURNEY_STORAGE_KEY);
  } catch {
    // Storage can be disabled by browser/privacy policy; URL-only setup must remain usable.
  }
}

export function recordJourneyLocation(
  storage: StorageLike,
  location: JourneyLocation,
  nowMs: number,
  randomFill: RandomFill = defaultRandomFill,
): JourneyState | null {
  const match = /^\/(en-GB|tr-TR|ar)\/setup\/(route|native|dns)$/.exec(location.pathname);
  if (!match || !isLocale(match[1])) return null;
  const locale = match[1];
  const step = match[2] as JourneyStep;
  let current = readJourneyState(storage, nowMs);
  if (current === null) current = createJourneyState(locale, nowMs, randomFill);

  const base = {
    schemaVersion: 1 as const,
    scope: current.scope,
    createdAt: current.createdAt,
    hardExpiresAt: current.hardExpiresAt,
    locale,
  };

  let next: JourneyState;
  if (step === 'route') {
    next = { ...base, journeyStep: 'route' };
  } else {
    if (!isDeviceFamily(location.platform)) return null;
    if (step === 'native') {
      next = { ...base, journeyStep: 'native', deviceFamily: location.platform };
    } else {
      next = {
        ...base,
        journeyStep: 'dns',
        deviceFamily: location.platform,
        dnsMethod: expectedDnsMethod(location.platform),
      };
    }
  }

  return writeJourneyState(storage, next) ? next : null;
}

export function resumeHref(state: JourneyState, localeOverride?: JourneyLocale): string {
  const locale = localeOverride && isLocale(localeOverride) ? localeOverride : state.locale;
  if (state.journeyStep === 'route') return `/${locale}/setup/route`;
  if (!isDeviceFamily(state.deviceFamily)) return `/${locale}/setup/route`;
  const platform = state.deviceFamily;
  if (state.journeyStep === 'native') return `/${locale}/setup/native?platform=${platform}`;
  if (state.journeyStep === 'dns' && state.dnsMethod === expectedDnsMethod(platform)) {
    return `/${locale}/setup/dns?platform=${platform}`;
  }
  return `/${locale}/setup/route`;
}
