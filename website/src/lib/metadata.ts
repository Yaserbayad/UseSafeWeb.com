import type { Metadata } from 'next';
import type { Locale } from '@/lib/i18n';

const baseUrl = 'https://usesafeweb.com';

export function publicMetadata(locale: Locale, title: string, description: string): Metadata {
  return {
    title,
    description,
    alternates: {
      canonical: `${baseUrl}/${locale}`,
      languages: {
        'en-GB': `${baseUrl}/en-GB`,
        'tr-TR': `${baseUrl}/tr-TR`,
        ar: `${baseUrl}/ar`,
      },
    },
    robots: { index: true, follow: true },
  };
}
