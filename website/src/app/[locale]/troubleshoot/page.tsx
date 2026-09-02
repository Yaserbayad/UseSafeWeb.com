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
      kicker="Troubleshooting"
      title="Protection could not be fully verified"
      summary="Review the supported setup, confirm the DNS setting is still present, and retry later when qualifying technical verification is available."
      noteTitle="Do not guess"
      noteBody="An unavailable verification result stays uncertain. It does not become protected because setup was completed."
    >
      <CorePageGuard locale={locale} expectedPhase="troubleshoot" />
      <div className="sw-actions">
        <CoreActionButton
          locale={locale}
          deviceFamily={platform}
          event={{ type: 'OPEN_RECOVERY' }}
          href={`/${locale}/recover?platform=${platform}`}
          label="Recovery and removal options"
          dataAttribute="data-core-recover"
        />
      </div>
    </SetupPage>
  );
}
