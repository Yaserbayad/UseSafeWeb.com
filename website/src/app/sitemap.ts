import type { MetadataRoute } from 'next';
import { locales } from '@/lib/i18n';

const publicPaths = ['', '/how-it-works', '/compatibility', '/protection-and-limits', '/privacy', '/help'];

export default function sitemap(): MetadataRoute.Sitemap {
  return locales.flatMap((locale) =>
    publicPaths.map((path) => ({
      url: `https://usesafeweb.com/${locale}${path}`,
      changeFrequency: 'weekly' as const,
      priority: path === '' ? 1 : 0.7,
    })),
  );
}
