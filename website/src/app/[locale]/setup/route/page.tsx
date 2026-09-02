import { notFound } from 'next/navigation';
import { SetupPage, operationalMetadata } from '@/components/setup-page';
import { getContent, isLocale } from '@/lib/i18n';

export const metadata = operationalMetadata;
export default async function Page({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params; if (!isLocale(locale)) notFound(); const c = getContent(locale);
  return <SetupPage kicker={c.route.kicker} title={c.route.title} summary={c.route.summary} noteTitle={c.route.noteTitle} noteBody={c.route.noteBody} actions={[{ href: `/${locale}/setup/native?platform=android`, label: c.route.androidLabel }, { href: `/${locale}/setup/native?platform=iphone`, label: c.route.iphoneLabel }, { href: `/${locale}/compatibility`, label: c.route.otherLabel, secondary: true }]} />;
}
