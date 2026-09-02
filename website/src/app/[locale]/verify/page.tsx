import { notFound } from 'next/navigation';
import { CoreActionButton } from '@/components/core-action-button';
import { CorePageGuard } from '@/components/core-page-guard';
import { SetupPage, operationalMetadata } from '@/components/setup-page';
import { isLocale } from '@/lib/i18n';

export const metadata = operationalMetadata;

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
      kicker="Verification"
      title="Check what is known before relying on protection"
      summary="This step does not invent technical verification. TSK-0358 has no qualifying E1 verifier yet, so the Protection Map will distinguish parent-confirmed setup, unavailable verification, and unsupported coverage."
      noteTitle="Fail-closed verification"
      noteBody="If technical evidence is unavailable, stale, conflicting, or indeterminate, SafeWeb must not label the setup protected or verified."
    >
      <CorePageGuard locale={locale} expectedPhase="verify" />
      <div className="sw-actions">
        <CoreActionButton
          locale={locale}
          deviceFamily={platform}
          event={{ type: 'VERIFICATION_RESULT' }}
          href={`/${locale}/protection?platform=${platform}`}
          label="View Protection Map"
          dataAttribute="data-core-view-protection"
        />
      </div>
    </SetupPage>
  );
}
