'use client';

import { useEffect, useState } from 'react';
import { CoreActionButton } from '@/components/core-action-button';
import { classifyAutomatedChecks, type AutomatedVerificationOutcome } from '@/lib/automated-verification';
import { runDnsVerification, type BrowserDnsVerificationCheck } from '@/lib/dns-verification-browser';
import { readCoreSession } from '@/lib/core-session';
import { evaluateProtection, type DeviceFamily, type Locale } from '@/lib/core-state-machine';

function outcomeFromCheck(check: BrowserDnsVerificationCheck | null): AutomatedVerificationOutcome {
  return classifyAutomatedChecks(check
    ? { support: 'supported', service: 'healthy', dnsPath: check.dnsPath, configured: true, removed: false }
    : { support: 'supported', service: 'unknown', dnsPath: 'not-run', configured: true, removed: false });
}

export function DnsVerificationPanel({
  locale,
  deviceFamily,
  stateLabels,
  reasonCopy,
  viewProtectionLabel,
  troubleshootLabel,
}: {
  locale: Locale;
  deviceFamily: DeviceFamily;
  stateLabels: Record<string, string>;
  reasonCopy: Record<string, string>;
  viewProtectionLabel: string;
  troubleshootLabel: string;
}) {
  const [outcome, setOutcome] = useState<AutomatedVerificationOutcome>(() => outcomeFromCheck(null));
  const [checking, setChecking] = useState(true);

  useEffect(() => {
    let active = true;
    const run = async () => {
      const state = readCoreSession(window.sessionStorage, Date.now());
      if (!state || state.phase !== 'verify' || state.locale !== locale || state.deviceFamily !== deviceFamily) {
        if (active) {
          setOutcome(outcomeFromCheck(null));
          setChecking(false);
        }
        return;
      }

      const check = await runDnsVerification(state.scope);
      if (!active) return;
      setOutcome(outcomeFromCheck(check));
      setChecking(false);
    };
    void run();
    return () => { active = false; };
  }, [deviceFamily, locale]);

  const protection = evaluateProtection(outcome.evidence);
  const supporting = protection.action ?? reasonCopy[protection.reasonCode] ?? reasonCopy.default;
  const canContinueToServices = protection.state === 'protected/verified' || protection.state === 'configured/parent-confirmed';

  return (
    <>
      <section
        className="sw-card"
        data-verification-outcome={outcome.checkState}
        data-parent-confirmation={outcome.parentConfirmation}
        data-protection-state={protection.state}
        aria-live="polite"
        aria-busy={checking}
      >
        <h2>{stateLabels[protection.state]}</h2>
        <p>{supporting}</p>
        <p className="sw-technical">{protection.reasonCode}</p>
      </section>
      <div className="sw-actions">
        {canContinueToServices ? (
          <CoreActionButton
            locale={locale}
            deviceFamily={deviceFamily}
            event={{ type: 'VERIFICATION_RESULT', evidence: outcome.evidence }}
            href={`/${locale}/protection?platform=${deviceFamily}`}
            label={viewProtectionLabel}
            dataAttribute="data-core-view-protection"
          />
        ) : (
          <CoreActionButton
            locale={locale}
            deviceFamily={deviceFamily}
            event={{ type: 'OPEN_TROUBLESHOOT' }}
            href={`/${locale}/troubleshoot?platform=${deviceFamily}`}
            label={troubleshootLabel}
            dataAttribute="data-core-troubleshoot"
          />
        )}
      </div>
    </>
  );
}
