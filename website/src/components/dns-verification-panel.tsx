'use client';

import { useEffect, useState } from 'react';
import { CoreActionButton } from '@/components/core-action-button';
import { classifyAutomatedChecks, type AutomatedVerificationOutcome } from '@/lib/automated-verification';
import {
  clearDnsVerificationProof,
  runDnsVerification,
  writeDnsVerificationProof,
  type BrowserDnsVerificationCheck,
} from '@/lib/dns-verification-browser';
import { readCoreSession } from '@/lib/core-session';
import type { DeviceFamily, Locale } from '@/lib/core-state-machine';

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
      const now = Date.now();
      const state = readCoreSession(window.sessionStorage, now);
      clearDnsVerificationProof(window.sessionStorage);
      if (!state || state.phase !== 'verify' || state.locale !== locale || state.deviceFamily !== deviceFamily) {
        if (active) {
          setOutcome(outcomeFromCheck(null));
          setChecking(false);
        }
        return;
      }

      const result = await runDnsVerification(state.scope);
      if (!active) return;
      if (result) {
        writeDnsVerificationProof(window.sessionStorage, result.proof);
        setOutcome(outcomeFromCheck(result.check));
      } else {
        setOutcome(outcomeFromCheck(null));
      }
      setChecking(false);
    };
    void run();
    return () => { active = false; };
  }, [deviceFamily, locale]);

  const supporting = outcome.action ?? reasonCopy[outcome.reasonCode] ?? reasonCopy.default;
  const showRecovery = outcome.state === 'uncertain/error' || outcome.state === 'action-needed';

  return (
    <>
      <section
        className="sw-card"
        data-verification-outcome={outcome.outcome}
        data-protection-state={outcome.state}
        aria-live="polite"
        aria-busy={checking}
      >
        <h2>{stateLabels[outcome.state]}</h2>
        <p>{supporting}</p>
        <p className="sw-technical">{outcome.reasonCode}</p>
      </section>
      <div className="sw-actions">
        {showRecovery ? (
          <CoreActionButton
            locale={locale}
            deviceFamily={deviceFamily}
            event={{ type: 'OPEN_TROUBLESHOOT' }}
            href={`/${locale}/troubleshoot?platform=${deviceFamily}`}
            label={troubleshootLabel}
            dataAttribute="data-core-verify-recovery"
          />
        ) : null}
        <CoreActionButton
          locale={locale}
          deviceFamily={deviceFamily}
          event={{ type: 'VERIFICATION_RESULT' }}
          href={`/${locale}/protection?platform=${deviceFamily}`}
          label={viewProtectionLabel}
          dataAttribute="data-core-view-protection"
          secondary={showRecovery}
        />
      </div>
    </>
  );
}
