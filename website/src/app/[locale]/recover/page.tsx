import { notFound } from 'next/navigation';
import { CoreActionButton } from '@/components/core-action-button';
import { CorePageGuard } from '@/components/core-page-guard';
import { SetupPage, operationalMetadata } from '@/components/setup-page';
import { getJourneyContent, getVersionedInstruction, isLocale } from '@/lib/i18n';

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

  const content = getJourneyContent(locale, 'recover').value;
  const instruction = getVersionedInstruction(locale, platform, 'remove');

  if (instruction.status !== 'ready') {
    return (
      <SetupPage
        kicker={content.kicker}
        title={content.title}
        summary={content.noteBody}
        noteTitle={content.noteTitle}
        noteBody={content.noteBody}
      >
        <CorePageGuard locale={locale} expectedPhase="recover" />
        <p data-content-release={instruction.releaseId} data-content-status={instruction.status}>
          {content.noteBody}
        </p>
      </SetupPage>
    );
  }

  return (
    <SetupPage
      kicker={content.kicker}
      title={content.title}
      summary={content.summary}
      noteTitle={content.noteTitle}
      noteBody={content.noteBody}
    >
      <CorePageGuard locale={locale} expectedPhase="recover" />
      <p
        data-instruction-id={instruction.instructionId}
        data-instruction-source-locale={instruction.sourceLocale}
        data-content-release={instruction.releaseId}
        data-content-status={instruction.status}
      >
        {instruction.value}
      </p>
      <div className="sw-actions">
        <CoreActionButton
          locale={locale}
          deviceFamily={platform}
          event={{ type: 'REMOVE_CONFIGURATION' }}
          href={`/${locale}/removed?platform=${platform}`}
          label={content.actionLabel}
          dataAttribute="data-core-remove"
        />
      </div>
    </SetupPage>
  );
}
