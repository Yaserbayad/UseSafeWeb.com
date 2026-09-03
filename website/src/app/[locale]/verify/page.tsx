import { notFound } from 'next/navigation';
import { CorePageGuard } from '@/components/core-page-guard';
import { DnsVerificationPanel } from '@/components/dns-verification-panel';
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
  const protectionContent = getJourneyContent(locale, 'protection').value;
  const instructionId = platform === 'iphone' ? 'INS-IOS-VERIFY-01' : 'INS-AND-VERIFY-01';
  const instruction = getInstructionVariant(locale, instructionId);
  const uncertaintyInstruction = getInstructionVariant(locale, 'INS-COMMON-UNCERTAIN-01');
  const stateLabels = protectionContent.stateLabels as Record<string, string>;
  const reasonCopy = protectionContent.reasonCopy as Record<string, string>;

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
      <p data-instruction-id={uncertaintyInstruction.instructionId} data-instruction-source-locale={uncertaintyInstruction.sourceLocale}>
        {uncertaintyInstruction.value}
      </p>
      <DnsVerificationPanel
        locale={locale}
        deviceFamily={platform}
        stateLabels={stateLabels}
        reasonCopy={reasonCopy}
        viewProtectionLabel={content.actionLabel}
        troubleshootLabel={protectionContent.troubleshootLabel}
      />
    </SetupPage>
  );
}
