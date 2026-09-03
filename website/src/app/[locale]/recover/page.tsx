import { notFound } from 'next/navigation';
import { CorePageGuard } from '@/components/core-page-guard';
import { SetupPage, operationalMetadata } from '@/components/setup-page';
import { getContent, getJourneyContent, isLocale } from '@/lib/i18n';

export const metadata = operationalMetadata;

export default async function Page({ params, searchParams }: {
  params: Promise<{ locale: string }>;
  searchParams: Promise<{ platform?: string | string[] }>;
}) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();
  const query = await searchParams;
  const platform = typeof query.platform === 'string' ? query.platform : undefined;
  if (platform !== 'android' && platform !== 'iphone') notFound();

  const c = getContent(locale);
  const content = getJourneyContent(locale, 'recover').value;

  return (
    <SetupPage
      kicker={content.kicker}
      title={content.title}
      summary={content.summary}
      noteTitle={content.noteTitle}
      noteBody={content.noteBody}
      actions={[
        { href: `/${locale}/help`, label: c.dns.helpLabel, secondary: true },
        { href: `/${locale}/setup/route`, label: c.dns.backLabel, secondary: true },
      ]}
    >
      <CorePageGuard locale={locale} expectedPhase="recover" />
    </SetupPage>
  );
}
