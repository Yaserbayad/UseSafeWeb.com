import { notFound } from 'next/navigation';
import { SetupPage, operationalMetadata } from '@/components/setup-page';
import { getContent, isLocale } from '@/lib/i18n';

export const metadata = operationalMetadata;
export default async function Page({ params, searchParams }: { params: Promise<{ locale: string }>; searchParams: Promise<{ platform?: string | string[] }> }) {
  const { locale } = await params; if (!isLocale(locale)) notFound(); const c = getContent(locale); const query = await searchParams; const platform = query.platform === 'iphone' ? 'iphone' : 'android';
  return <SetupPage kicker={c.native.kicker} title={platform === 'iphone' ? c.native.iphoneTitle : c.native.androidTitle} summary={platform === 'iphone' ? c.native.iphoneBody : c.native.androidBody} noteTitle={c.native.noteTitle} noteBody={c.native.noteBody} actions={[{ href: `/${locale}/setup/dns?platform=${platform}`, label: c.native.continueLabel }, { href: `/${locale}/compatibility`, label: c.native.supportLabel, secondary: true }]} />;
}
