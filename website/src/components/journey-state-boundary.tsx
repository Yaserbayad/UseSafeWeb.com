'use client';

import { useEffect } from 'react';
import { usePathname, useSearchParams } from 'next/navigation';
import { recordJourneyLocation } from '@/lib/journey-state';

export function JourneyStateBoundary() {
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const platforms = searchParams.getAll('platform');
  const platform = platforms.length === 1 ? platforms[0] : null;

  useEffect(() => {
    try {
      recordJourneyLocation(window.sessionStorage, { pathname, platform }, Date.now());
    } catch {
      // Browser storage can be unavailable; URL-only accountless setup remains usable.
    }
  }, [pathname, platform]);

  return null;
}
