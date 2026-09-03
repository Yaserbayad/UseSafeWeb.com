'use client';

import { useEffect, useState } from 'react';
import { classifyAutomatedChecks, type AutomatedVerificationOutcome } from '@/lib/automated-verification';
import {
  clearDnsVerificationProof,
  readDnsVerificationProof,
  revalidateDnsVerificationProof,
  type BrowserDnsVerificationCheck,
} from '@/lib/dns-verification-browser';
import { readCoreSession } from '@/lib/core-session';
import type { DeviceFamily, Locale } from '@/lib/core-state-machine';

function outcomeFromCheck(check: BrowserDnsVerificationCheck | null): AutomatedVerificationOutcome {
  return classifyAutomatedChecks(check
    ? { support: 'supported', service: 'healthy', dnsPath: check.dnsPath, configured: true, removed: false }
    : { support: 'supported', service: 'unknown', dnsPath: 'not-run', configured: true, removed: false });
}

export function DnsVerificationCard({
  locale,
  deviceFamily,
  label,
  stateLabels,
  reasonCopy,
}: {
  locale: Locale;
  deviceFamily: DeviceFamily;
  label: string;
  stateLabels: Record<string, string>;
  reasonCopy: Record<string, string>;
}) {
  const [outcome, setOutcome] = useState<AutomatedVerificationOutcome>(() => outcomeFromCheck(null));
  const [checking, setChecking] = useState(true);

  useEffect(() => {
    let active = true;
    const run = async () => {
      const state = readCoreSession(window.sessionStorage, Date.now());
      const proof = readDnsVerificationProof(window.sessionStorage);
      if (!state || state.phase !== 'protection' || state.locale !== locale || state.deviceFamily !== deviceFamily || !proof) {
        clearDnsVerificationProof(window.sessionStorage);
        if (active) {
          setOutcome(outcomeFromCheck(null));
          setChecking(false);
        }
        return;
      }

      const check = await revalidateDnsVerificationProof(state.scope, proof);
      if (!active) return;
      if (!check || check.dnsPath === 'verified-stale') {
        clearDnsVerificationProof(window.sessionStorage);
      }
      setOutcome(outcomeFromCheck(check));
      setChecking(false);
    };
    void run();
    return () => { active = false; };
  }, [deviceFamily, locale]);

  const supporting = outcome.action ?? reasonCopy[outcome.reasonCode] ?? reasonCopy.default;

  return (
    <section
      className="sw-card"
      data-verification-outcome={outcome.outcome}
      data-protection-state={outcome.state}
      aria-live="polite"
      aria-busy={checking}
    >
      <h2>{label}</h2>
      <p><strong>{stateLabels[outcome.state]}</strong></p>
      <p>{supporting}</p>
      <p className="sw-technical">{outcome.reasonCode}</p>
    </section>
  );
}
