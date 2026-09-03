import { notFound } from 'next/navigation';
import { CorePageGuard } from '@/components/core-page-guard';
import { DnsVerificationPanel } from '@/components/dns-verification-panel';
import { SetupPage, operationalMetadata } from '@/components/setup-page';
import { getJourneyContent, getVersionedInstruction, isLocale } from '@/lib/i18n';

// TSK-0359 provenance compatibility: INS-AND-VERIFY-01 / INS-IOS-VERIFY-01 selection is delegated to the TSK-0374 versioned release map.
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
  const instruction = getVersionedInstruction(locale, platform, 'verify');
  const uncertaintyInstruction = getVersionedInstruction(locale, 'common', 'uncertain');
  const stateLabels = protectionContent.stateLabels as Record<string, string>;
  const reasonCopy = protectionContent.reasonCopy as Record<string, string>;

  if (instruction.status !== 'ready' || uncertaintyInstruction.status !== 'ready') {
    const failed = instruction.status !== 'ready' ? instruction : uncertaintyInstruction;
    return (
      <SetupPage
        kicker={content.kicker}
        title={content.title}
        summary={content.noteBody}
        noteTitle={content.noteTitle}
        noteBody={content.noteBody}
        actions={[
          {
            href: `/${locale}/troubleshoot?platform=${platform}`,
            label: protectionContent.troubleshootLabel,
            secondary: true,
          },
        ]}
      >
        <CorePageGuard locale={locale} expectedPhase="verify" />
        <p data-content-release={failed.releaseId} data-content-status={failed.status}>
          <span className="sw-technical">{failed.status}</span> {stateLabels['uncertain/error']}
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
      <CorePageGuard locale={locale} expectedPhase="verify" />
      <p
        data-instruction-id={instruction.instructionId}
        data-instruction-source-locale={instruction.sourceLocale}
        data-content-release={instruction.releaseId}
        data-content-status={instruction.status}
      >
        {instruction.value}
      </p>
      <p
        data-instruction-id={uncertaintyInstruction.instructionId}
        data-instruction-source-locale={uncertaintyInstruction.sourceLocale}
        data-content-release={uncertaintyInstruction.releaseId}
        data-content-status={uncertaintyInstruction.status}
      >
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
