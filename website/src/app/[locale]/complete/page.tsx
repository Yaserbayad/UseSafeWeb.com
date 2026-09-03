import { notFound } from 'next/navigation';
import { CorePageGuard } from '@/components/core-page-guard';
import { SetupPage, operationalMetadata } from '@/components/setup-page';
import { getJourneyContent, isLocale } from '@/lib/i18n';

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

  const content = getJourneyContent(locale, 'complete').value;

  return (
    <SetupPage
      kicker={content.kicker}
      title={content.title}
      summary={content.summary}
      noteTitle={content.noteTitle}
      noteBody={content.noteBody}
      actions={[{ href: `/${locale}/start`, label: content.backLabel, secondary: true }]}
    >
      <CorePageGuard locale={locale} expectedPhase="complete" />
      <section className="sw-card" data-account-capability="deferred">
        <h2>{content.accountTitle}</h2>
        <p>{content.accountBody}</p>
      </section>
    </SetupPage>
  );
}
