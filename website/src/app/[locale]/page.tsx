import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { ContentPage } from '@/components/content-page';
import { getContent, isLocale } from '@/lib/i18n';
import { publicMetadata } from '@/lib/metadata';

export async function generateMetadata({ params }: { params: Promise<{ locale: string }> }): Promise<Metadata> {
  const { locale } = await params;
  if (!isLocale(locale)) return {};
  const content = getContent(locale);
  return publicMetadata(locale, '', content.home.title, content.home.summary);
}

export default async function HomePage({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();
  const content = getContent(locale);
  return <ContentPage section={content.home} actions={[{ href: `/${locale}/start`, label: content.home.primaryLabel }, { href: `/${locale}/how-it-works`, label: content.home.secondaryLabel, secondary: true }]} />;
}
