import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { ContentPage } from '@/components/content-page';
import { getContent, isLocale } from '@/lib/i18n';

export const metadata: Metadata = { robots: { index: false, follow: false } };
export default async function Page({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();
  const c = getContent(locale);
  return <ContentPage section={c.status} actions={[{ href: `/${locale}/help`, label: c.common.nav.help }]} />;
}
