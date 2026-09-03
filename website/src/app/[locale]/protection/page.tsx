import { notFound } from 'next/navigation';
import { CoreActionButton } from '@/components/core-action-button';
import { CorePageGuard } from '@/components/core-page-guard';
import { SetupPage, operationalMetadata } from '@/components/setup-page';
import { getCurrentAutomatedVerification } from '@/lib/automated-verification';
import { evaluateProtection, type ProtectionEvidence } from '@/lib/core-state-machine';
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

  const content = getJourneyContent(locale, 'protection').value;
  const automated = getCurrentAutomatedVerification();
  const evidenceRows: Array<{ label: string; evidence: ProtectionEvidence; dnsVerification?: boolean }> = [
    {
      label: content.deviceSetupLabel,
      evidence: { coverage: 'covered', configured: true, technical: null, action: null, uncertainty: null, removal: null },
    },
    {
      label: content.dnsVerificationLabel,
      evidence: automated.evidence,
      dnsVerification: true,
    },
    {
      label: content.otherServicesLabel,
      evidence: { coverage: 'not-covered', configured: false, technical: null, action: null, uncertainty: null, removal: null },
    },
  ];
  const stateLabels = content.stateLabels as Record<string, string>;
  const reasonCopy = content.reasonCopy as Record<string, string>;

  return (
    <SetupPage
      kicker={content.kicker}
      title={content.title}
      summary={content.summary}
      noteTitle={content.noteTitle}
      noteBody={content.noteBody}
    >
      <CorePageGuard locale={locale} expectedPhase="protection" />
      <div className="sw-card-grid">
        {evidenceRows.map(({ label, evidence, dnsVerification }) => {
          const result = evaluateProtection(evidence);
          const supporting = result.action ?? reasonCopy[result.reasonCode] ?? reasonCopy.default;
          return (
            <section
              className="sw-card"
              data-protection-state={result.state}
              data-dns-verification-state={dnsVerification ? automated.checkState : undefined}
              data-parent-confirmation={dnsVerification ? automated.parentConfirmation : undefined}
              key={label}
            >
              <h2>{label}</h2>
              <p><strong>{stateLabels[result.state]}</strong></p>
              <p>{supporting}</p>
              <p className="sw-technical">{result.reasonCode}</p>
            </section>
          );
        })}
      </div>
      <div className="sw-actions">
        <CoreActionButton
          locale={locale}
          deviceFamily={platform}
          event={{ type: 'OPEN_TROUBLESHOOT' }}
          href={`/${locale}/troubleshoot?platform=${platform}`}
          label={content.troubleshootLabel}
          dataAttribute="data-core-troubleshoot"
        />
        <CoreActionButton
          locale={locale}
          deviceFamily={platform}
          event={{ type: 'COMPLETE' }}
          href={`/${locale}/complete?platform=${platform}`}
          label={content.completeLabel}
          dataAttribute="data-core-complete"
          secondary
        />
      </div>
    </SetupPage>
  );
}
