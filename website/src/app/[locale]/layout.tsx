import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { Suspense, type ReactNode } from 'react';
import { JourneyStateBoundary } from '@/components/journey-state-boundary';
import { SiteShell } from '@/components/site-shell';
import { getContent, getLocaleMeta, isLocale, locales } from '@/lib/i18n';
import '../globals.css';

export const metadata: Metadata = {
  metadataBase: new URL('https://usesafeweb.com'),
  title: { default: 'SafeWeb', template: '%s | SafeWeb' },
};

export const dynamicParams = false;

export function generateStaticParams() {
  return locales.map((locale) => ({ locale }));
}

export default async function LocaleLayout({
  children,
  params,
}: {
  children: ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();
  const content = getContent(locale);
  const meta = getLocaleMeta(locale);

  return (
    <html lang={locale} dir={meta.direction}>
      <body>
        <div data-locale-root lang={locale} dir={meta.direction}>
          <Suspense fallback={null}>
            <JourneyStateBoundary />
          </Suspense>
          <SiteShell locale={locale} common={content.common}>
            {children}
          </SiteShell>
        </div>
      </body>
    </html>
  );
}
