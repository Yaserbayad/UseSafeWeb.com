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
      kicker="Recovery and removal"
      title="Recover safely or remove this setup"
      summary="If this setup is no longer wanted or cannot be made trustworthy, remove the device configuration rather than treating an uncertain state as protected."
      noteTitle="Removal is explicit"
      noteBody="Removing this setup changes the Protection Map to Removed. Reinstalling later must be verified again before any verified protection claim."
    >
      <CorePageGuard locale={locale} expectedPhase="recover" />
      <div className="sw-actions">
        <CoreActionButton
          locale={locale}
          deviceFamily={platform}
          event={{ type: 'REMOVE_CONFIGURATION' }}
          href={`/${locale}/removed?platform=${platform}`}
          label="I removed this setup"
          dataAttribute="data-core-remove"
        />
      </div>
    </SetupPage>
  );
}
