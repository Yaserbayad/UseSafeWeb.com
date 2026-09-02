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
      kicker="Removed"
      title="This setup is marked removed"
      summary="SafeWeb no longer treats this device setup as enrolled. Starting again creates a new accountless setup path; verification must be earned again."
      noteTitle="No stale verification"
      noteBody="A previous verification result cannot be reused after removal or reinstall."
    >
      <CorePageGuard locale={locale} expectedPhase="removed" />
      <div className="sw-actions">
        <CoreActionButton
          locale={locale}
          deviceFamily={platform}
          event={{ type: 'RESTART_SETUP' }}
          href={`/${locale}/setup/route`}
          label="Start setup again"
          dataAttribute="data-core-restart"
        />
      </div>
    </SetupPage>
  );
}
