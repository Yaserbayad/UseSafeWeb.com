import enGB from '@/content/en-GB.json';
import trTR from '@/content/tr-TR.json';
import ar from '@/content/ar.json';
import manifest from '@/content/locale-manifest.json';

export const locales = ['en-GB', 'tr-TR', 'ar'] as const;
export type Locale = (typeof locales)[number];
export type ContentBundle = typeof enGB;

const bundles: Record<Locale, ContentBundle> = {
  'en-GB': enGB,
  'tr-TR': trTR,
  ar,
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
