import { notFound } from 'next/navigation';
import type { ReactNode } from 'react';
import { SiteShell } from '@/components/site-shell';
import { getContent, getLocaleMeta, isLocale, locales } from '@/lib/i18n';

export const dynamicParams = false;

export function generateStaticParams() {
  return locales.map((locale) => ({ locale }));
}

export default async function LocaleLayout({ children, params }: { children: ReactNode; params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();
  const content = getContent(locale);
  const meta = getLocaleMeta(locale);
  return <div data-locale-root lang={locale} dir={meta.direction}><SiteShell locale={locale} common={content.common}>{children}</SiteShell></div>;
}
