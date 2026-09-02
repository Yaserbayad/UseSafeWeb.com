'use client';

import { useRouter } from 'next/navigation';
import { advanceCoreSession, clearCoreSession } from '@/lib/core-session';
import type { CoreEvent, DeviceFamily, Locale } from '@/lib/core-state-machine';

type DataAttribute =
  | 'data-core-continue-native'
  | 'data-core-continue-dns'
  | 'data-core-view-protection'
  | 'data-core-troubleshoot'
  | 'data-core-recover'
  | 'data-core-remove'
  | 'data-core-restart'
  | 'data-core-complete';

export function CoreActionButton({
  locale,
  deviceFamily,
  event,
  href,
  label,
  dataAttribute,
  secondary = false,
}: {
  locale: Locale;
  deviceFamily: DeviceFamily;
  event: CoreEvent;
  href: string;
  label: string;
  dataAttribute: DataAttribute;
  secondary?: boolean;
}) {
  const router = useRouter();
  const dataProps = { [dataAttribute]: '' };

  function advance() {
    const state = advanceCoreSession(window.sessionStorage, locale, deviceFamily, event, Date.now());
    if (!state) {
      clearCoreSession(window.sessionStorage);
      router.replace(`/${locale}/setup/route`);
      return;
    }
    router.push(href);
  }

  return (
    <button
      type="button"
      className={secondary ? 'sw-button sw-button--secondary' : 'sw-button'}
      onClick={advance}
      {...dataProps}
    >
      {label}
    </button>
  );
}
