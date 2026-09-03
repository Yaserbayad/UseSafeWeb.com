import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { ContentPage } from '@/components/content-page';
import { getContent, isLocale } from '@/lib/i18n';
import { publicMetadata } from '@/lib/metadata';

export async function generateMetadata({ params }: { params: Promise<{ locale: string }> }): Promise<Metadata> {
  const { locale } = await params;
  if (!isLocale(locale)) return {};
  const c = getContent(locale);
  return publicMetadata(locale, '/help', c.help.title, c.help.summary);
}
export default async function Page({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();
  const c = getContent(locale);
  return (
    <ContentPage
      section={c.help}
      actions={[{ href: `/${locale}/compatibility`, label: c.common.nav.compatibility, secondary: true }]}
    />
  );
}
