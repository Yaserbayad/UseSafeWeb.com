'use client';

import Link from 'next/link';
import { useEffect, useState } from 'react';
import { clearJourneyState, readJourneyState, resumeHref, type JourneyLocale } from '@/lib/journey-state';

type Props = {
  locale: JourneyLocale;
  resumeLabel: string;
  resetLabel: string;
  resumeNote: string;
};

export function JourneyResumePanel({ locale, resumeLabel, resetLabel, resumeNote }: Props) {
  const [href, setHref] = useState<string | null>(null);

  useEffect(() => {
    const timer = window.setTimeout(() => {
      try {
        const state = readJourneyState(window.sessionStorage, Date.now());
        setHref(state ? resumeHref(state, locale) : null);
      } catch {
        setHref(null);
      }
    }, 0);
    return () => window.clearTimeout(timer);
  }, [locale]);

  if (!href) return null;

  function resetJourney() {
    try {
      clearJourneyState(window.sessionStorage);
    } finally {
      setHref(null);
    }
  }

  return (
    <aside className="sw-callout" aria-live="polite">
      <p>{resumeNote}</p>
      <div className="sw-actions">
        <Link className="sw-button" data-journey-resume href={href}>
          {resumeLabel}
        </Link>
        <button className="sw-button sw-button--secondary" data-journey-reset type="button" onClick={resetJourney}>
          {resetLabel}
        </button>
      </div>
    </aside>
  );
}
