'use client';

import { useCallback, useEffect, useSyncExternalStore } from 'react';
import { useRouter } from 'next/navigation';
import { CoreActionButton } from '@/components/core-action-button';
import { SetupPage } from '@/components/setup-page';
import { clearCoreSession, readCoreSession } from '@/lib/core-session';
import { getContent, getJourneyContent, getVersionedInstruction, type Locale } from '@/lib/i18n';

type CleanupPlatform = 'android' | 'iphone';

const subscribe = () => () => {};
const getServerSnapshot = () => false;

export function RevocationGatedCleanup({ locale, platform }: { locale: Locale; platform: CleanupPlatform }) {
  const router = useRouter();
  const getAuthorizedSnapshot = useCallback(() => {
    const state = readCoreSession(window.sessionStorage, Date.now());
    return Boolean(state && state.locale === locale && state.deviceFamily === platform && state.phase === 'cleanup');
  }, [locale, platform]);
  const authorized = useSyncExternalStore(subscribe, getAuthorizedSnapshot, getServerSnapshot);

  useEffect(() => {
    const state = readCoreSession(window.sessionStorage, Date.now());
    if (!state || state.locale !== locale || state.deviceFamily !== platform || state.phase !== 'cleanup') {
      clearCoreSession(window.sessionStorage);
      router.replace(`/${locale}/setup/route`);
    }
  }, [locale, platform, router]);

  // Server/pre-hydration rendering stays empty; only a valid current browser-session cleanup phase exposes removal UI.
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
