'use client';

import {
  createCoreState,
  resumeCoreState,
  transitionCoreState,
  type CoreEvent,
  type CoreState,
  type DeviceFamily,
  type Locale,
} from '@/lib/core-state-machine';
import { readJourneyState } from '@/lib/journey-state';

export const CORE_STORAGE_KEY = 'usesafeweb:core:v1';

type StorageLike = Pick<Storage, 'getItem' | 'setItem' | 'removeItem'>;

export function clearCoreSession(storage: StorageLike): void {
  try {
    storage.removeItem(CORE_STORAGE_KEY);
  } catch {
    /* URL-only fallback remains usable. */
  }
}

export function readCoreSession(storage: StorageLike, nowMs: number): CoreState | null {
  try {
    const raw = storage.getItem(CORE_STORAGE_KEY);
    if (raw === null) return null;
    const state = resumeCoreState(raw, nowMs);
    if (!state) storage.removeItem(CORE_STORAGE_KEY);
    return state;
  } catch {
    return null;
  }
}

function persist(storage: StorageLike, state: CoreState): CoreState | null {
  try {
    storage.setItem(CORE_STORAGE_KEY, JSON.stringify(state));
    return state;
  } catch {
    return null;
  }
}

function bootstrapFromJourney(
  storage: StorageLike,
  locale: Locale,
  deviceFamily: DeviceFamily,
  nowMs: number,
): CoreState | null {
  const journey = readJourneyState(storage, nowMs);
  if (!journey || journey.locale !== locale || journey.deviceFamily !== deviceFamily) return null;
  let core = createCoreState(locale, journey.scope, journey.createdAt, journey.hardExpiresAt);
  core = transitionCoreState(core, { type: 'SELECT_DEVICE', deviceFamily }, nowMs);
  return core;
}

export function advanceCoreSession(
  storage: StorageLike,
  locale: Locale,
  deviceFamily: DeviceFamily,
  event: CoreEvent,
  nowMs: number,
): CoreState | null {
  try {
    let current = readCoreSession(storage, nowMs);
    if (!current) current = bootstrapFromJourney(storage, locale, deviceFamily, nowMs);
    if (!current) return null;
    if (current.locale !== locale || current.deviceFamily !== deviceFamily) return null;
    if (current.phase === 'route')
      current = transitionCoreState(current, { type: 'SELECT_DEVICE', deviceFamily }, nowMs);
    return persist(storage, transitionCoreState(current, { ...event, deviceFamily }, nowMs));
  } catch {
    return null;
  }
}
