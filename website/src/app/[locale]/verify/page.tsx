import { notFound } from 'next/navigation';
import { CoreActionButton } from '@/components/core-action-button';
import { CorePageGuard } from '@/components/core-page-guard';
import { SetupPage, operationalMetadata } from '@/components/setup-page';
import { classifyAutomatedChecks } from '@/lib/automated-verification';
import { evaluateProtection } from '@/lib/core-state-machine';
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

  // No approved browser-visible DNS-path verifier currently supplies fresh E1 evidence.
  // Keep the production page fail-closed until a trusted internal producer is connected.
  const automated = classifyAutomatedChecks({
    support: 'unknown',
    service: 'unknown',
    dnsPath: 'not-run',
    configured: true,
    removed: false,
  });
  const evaluation = evaluateProtection(automated.evidence);
  const stateLabels = protectionContent.stateLabels as Record<string, string>;
  const reasonCopy = protectionContent.reasonCopy as Record<string, string>;
  const supporting = evaluation.action ?? reasonCopy[evaluation.reasonCode] ?? reasonCopy.default;

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
      <section
        className="sw-card"
        data-automated-verification={automated.checkState}
        data-parent-confirmation={automated.parentConfirmation}
      >
        <h2>{stateLabels[evaluation.state]}</h2>
        <p>{supporting}</p>
        <p>{uncertaintyInstruction.value}</p>
        <p className="sw-technical">{evaluation.reasonCode}</p>
      </section>
      <div className="sw-actions">
        {automated.recovery === 'troubleshoot' ? (
          <CoreActionButton
            locale={locale}
            deviceFamily={platform}
            event={{ type: 'OPEN_TROUBLESHOOT' }}
            href={`/${locale}/troubleshoot?platform=${platform}`}
            label={protectionContent.troubleshootLabel}
            dataAttribute="data-automated-recovery"
          />
        ) : null}
        <CoreActionButton
          locale={locale}
          deviceFamily={platform}
          event={{ type: 'VERIFICATION_RESULT' }}
          href={`/${locale}/protection?platform=${platform}`}
          label={content.actionLabel}
          dataAttribute="data-core-view-protection"
          secondary={automated.recovery === 'troubleshoot'}
        />
      </div>
    </SetupPage>
  );
}
