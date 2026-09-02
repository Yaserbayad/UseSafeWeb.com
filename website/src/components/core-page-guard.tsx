'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { clearCoreSession, readCoreSession } from '@/lib/core-session';
import type { CorePhase, Locale } from '@/lib/core-state-machine';

export function CorePageGuard({ locale, expectedPhase }: { locale: Locale; expectedPhase: CorePhase }) {
  const router = useRouter();

  useEffect(() => {
    const state = readCoreSession(window.sessionStorage, Date.now());
    if (!state || state.locale !== locale || state.phase !== expectedPhase) {
      clearCoreSession(window.sessionStorage);
      router.replace(`/${locale}/setup/route`);
    }
  }, [expectedPhase, locale, router]);

  return null;
}
