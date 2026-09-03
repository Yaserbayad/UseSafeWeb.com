import enGB from '@/content/en-GB.json';
import trTR from '@/content/tr-TR.json';
import ar from '@/content/ar.json';
import instructionBindings from '@/content/instruction-bindings.json';
import journeyContent from '@/content/journey-content.json';
import manifest from '@/content/locale-manifest.json';
import { resolveLocaleValue } from '@/lib/locale-fallback';

export const locales = ['en-GB', 'tr-TR', 'ar'] as const;
export type Locale = (typeof locales)[number];
export type ContentBundle = typeof enGB;
export type JourneySection = keyof typeof journeyContent.sections;
export type InstructionId = keyof typeof instructionBindings.instructions;

type LocalizedValue<T> = T extends Record<string, infer V> ? V : never;

const bundles: Record<Locale, ContentBundle> = {
  'en-GB': enGB,
  'tr-TR': trTR,
  ar,
};

const fallbackMap: Record<Locale, Locale | null> = {
  'en-GB': manifest.locales['en-GB'].fallback as Locale | null,
  'tr-TR': manifest.locales['tr-TR'].fallback as Locale | null,
  ar: manifest.locales.ar.fallback as Locale | null,
};

export function isLocale(value: string): value is Locale {
  return locales.includes(value as Locale);
}

export function getContent(locale: Locale): ContentBundle {
  return bundles[locale];
}

export function getLocaleMeta(locale: Locale) {
  return manifest.locales[locale];
}

export function getJourneyContent<S extends JourneySection>(locale: Locale, section: S) {
  type Value = LocalizedValue<(typeof journeyContent.sections)[S]>;
  const values = journeyContent.sections[section] as unknown as Partial<Record<Locale, Value>>;
  const resolved = resolveLocaleValue(locale, values, fallbackMap, journeyContent.defaultLocale);
  return { value: resolved.value, sourceLocale: resolved.sourceLocale };
}

export function getInstructionVariant(locale: Locale, instructionId: InstructionId) {
  const instruction = instructionBindings.instructions[instructionId];
  const values = instruction.variants as Partial<Record<Locale, string>>;
  const resolved = resolveLocaleValue(locale, values, fallbackMap, journeyContent.defaultLocale);
  return {
    instructionId,
    purpose: instruction.purpose,
    platform: instruction.platform,
    value: resolved.value,
    sourceLocale: resolved.sourceLocale,
  };
}
