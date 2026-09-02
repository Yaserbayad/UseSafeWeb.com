import type { MetadataRoute } from 'next';

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [{ userAgent: '*', allow: '/', disallow: ['/*/start', '/*/setup/', '/*/status', '/*/account/'] }],
    sitemap: 'https://usesafeweb.com/sitemap.xml',
    host: 'https://usesafeweb.com',
  };
}
