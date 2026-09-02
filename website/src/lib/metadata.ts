import type { Metadata } from 'next';
import type { Locale } from '@/lib/i18n';

const baseUrl = 'https://usesafeweb.com';

export function publicMetadata(locale: Locale, path: string, title: string, description: string): Metadata {
  const suffix = path === '' ? '' : path.startsWith('/') ? path : `/${path}`;
  const localizedUrl = (target: Locale) => `${baseUrl}/${target}${suffix}`;

  return {
    title,
    description,
    alternates: {
      canonical: localizedUrl(locale),
      languages: {
        'en-GB': localizedUrl('en-GB'),
        'tr-TR': localizedUrl('tr-TR'),
        ar: localizedUrl('ar'),
      },
    },
    robots: { index: true, follow: true },
  };
}
