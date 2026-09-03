import { notFound } from 'next/navigation';
import { CoreActionButton } from '@/components/core-action-button';
import { CorePageGuard } from '@/components/core-page-guard';
import { SetupPage, operationalMetadata } from '@/components/setup-page';
import { getInstructionVariant, getJourneyContent, isLocale } from '@/lib/i18n';

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

  const content = getJourneyContent(locale, 'verify').value;
  const instructionId = platform === 'iphone' ? 'INS-IOS-VERIFY-01' : 'INS-AND-VERIFY-01';
  const instruction = getInstructionVariant(locale, instructionId);

  return (
    <SetupPage
      kicker={content.kicker}
      title={content.title}
      summary={content.summary}
      noteTitle={content.noteTitle}
      noteBody={content.noteBody}
    >
      <CorePageGuard locale={locale} expectedPhase="verify" />
      <p data-instruction-id={instruction.instructionId} data-instruction-source-locale={instruction.sourceLocale}>
        {instruction.value}
      </p>
      <div className="sw-actions">
        <CoreActionButton
          locale={locale}
          deviceFamily={platform}
          event={{ type: 'VERIFICATION_RESULT' }}
          href={`/${locale}/protection?platform=${platform}`}
          label={content.actionLabel}
          dataAttribute="data-core-view-protection"
        />
      </div>
    </SetupPage>
  );
}
