import { notFound } from 'next/navigation';
import { CoreActionButton } from '@/components/core-action-button';
import { CorePageGuard } from '@/components/core-page-guard';
import { SetupPage, operationalMetadata } from '@/components/setup-page';
import { evaluateProtection, type ProtectionEvidence } from '@/lib/core-state-machine';
import { isLocale } from '@/lib/i18n';

export const metadata = operationalMetadata;

const evidenceRows: Array<{ label: string; evidence: ProtectionEvidence }> = [
  {
    label: 'Device setup',
    evidence: { coverage: 'covered', configured: true, technical: null, action: null, uncertainty: null, removal: null },
  },
  {
    label: 'DNS verification',
    evidence: { coverage: 'covered', configured: true, technical: null, action: null, uncertainty: 'VERIFY_UNREACHABLE', removal: null },
  },
  {
    label: 'Other services and apps',
    evidence: { coverage: 'not-covered', configured: false, technical: null, action: null, uncertainty: null, removal: null },
  },
];

export default async function Page({ params, searchParams }: {
  params: Promise<{ locale: string }>;
  searchParams: Promise<{ platform?: string | string[] }>;
}) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();
  const query = await searchParams;
  const platform = typeof query.platform === 'string' ? query.platform : undefined;
  if (platform !== 'android' && platform !== 'iphone') notFound();

  return (
    <SetupPage
      kicker="Protection Map"
      title="What is protected, what still needs proof, and what is not covered"
      summary="SafeWeb separates parent-confirmed setup from technical verification. No account, journey completion, or configuration flag can manufacture a verified protection claim."
      noteTitle="Evidence first"
      noteBody="Only fresh qualifying technical evidence can produce Protected / verified. This task does not have that evidence yet."
    >
      <CorePageGuard locale={locale} expectedPhase="protection" />
      <div className="sw-card-grid">
        {evidenceRows.map(({ label, evidence }) => {
          const result = evaluateProtection(evidence);
          return (
            <section className="sw-card" data-protection-state={result.state} key={label}>
              <h2>{label}</h2>
              <p><strong>{result.primary}</strong></p>
              <p>{result.supporting}</p>
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
          label="Troubleshoot"
          dataAttribute="data-core-troubleshoot"
        />
        <CoreActionButton
          locale={locale}
          deviceFamily={platform}
          event={{ type: 'COMPLETE' }}
          href={`/${locale}/complete?platform=${platform}`}
          label="Finish setup"
          dataAttribute="data-core-complete"
          secondary
        />
      </div>
    </SetupPage>
  );
}
