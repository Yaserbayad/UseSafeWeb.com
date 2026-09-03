'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { CoreActionButton } from '@/components/core-action-button';
import { SetupPage } from '@/components/setup-page';
import { clearCoreSession, readCoreSession } from '@/lib/core-session';
import { getContent, getJourneyContent, getVersionedInstruction, type Locale } from '@/lib/i18n';

type CleanupPlatform = 'android' | 'iphone';

export function RevocationGatedCleanup({ locale, platform }: { locale: Locale; platform: CleanupPlatform }) {
  const router = useRouter();
  const [authorized, setAuthorized] = useState(false);

  useEffect(() => {
    const state = readCoreSession(window.sessionStorage, Date.now());
    if (!state || state.locale !== locale || state.deviceFamily !== platform || state.phase !== 'cleanup') {
      clearCoreSession(window.sessionStorage);
      router.replace(`/${locale}/setup/route`);
      return;
    }
    setAuthorized(true);
  }, [locale, platform, router]);

  // Fail closed during server/pre-hydration render and while browser-session evidence is being checked.
  if (!authorized) return null;

  const c = getContent(locale);
  const content = getJourneyContent(locale, 'recover').value;
  const instruction = getVersionedInstruction(locale, platform, 'remove');

  if (instruction.status !== 'ready') {
    return (
      <SetupPage
        kicker={content.kicker}
        title={content.title}
        summary={c.route.noteBody}
        noteTitle={c.route.noteTitle}
        noteBody={c.route.noteBody}
        actions={[
          { href: `/${locale}/help`, label: c.dns.helpLabel, secondary: true },
          { href: `/${locale}/setup/route`, label: c.dns.backLabel, secondary: true },
        ]}
      >
        <p data-content-release={instruction.releaseId} data-content-status={instruction.status}>
          <span className="sw-technical">{instruction.status}</span> {c.route.noteBody}
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
      <p
        data-instruction-id={instruction.instructionId}
        data-instruction-source-locale={instruction.sourceLocale}
        data-content-release={instruction.releaseId}
        data-content-status={instruction.status}
      >
        {instruction.value}
      </p>
      <div className="sw-actions">
        <CoreActionButton
          locale={locale}
          deviceFamily={platform}
          event={{ type: 'REMOVE_CONFIGURATION' }}
          href={`/${locale}/removed?platform=${platform}`}
          label={content.actionLabel}
          dataAttribute="data-core-remove"
        />
      </div>
    </SetupPage>
  );
}
