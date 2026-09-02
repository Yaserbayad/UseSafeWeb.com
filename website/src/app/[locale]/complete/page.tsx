import { notFound } from 'next/navigation';
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
      kicker="Complete"
      title="Setup complete"
      summary="Setup complete. Review what UseSafeWeb verified, what you confirmed, what needs action, and what is not covered."
      noteTitle="Accountless core remains complete"
      noteBody="You do not need an account to finish, review, troubleshoot, recover, or remove the core setup."
      actions={[{ href: `/${locale}/start`, label: 'Back to setup start', secondary: true }]}
    >
      <CorePageGuard locale={locale} expectedPhase="complete" />
      <section className="sw-card" data-account-capability="deferred">
        <h2>Optional account capability deferred</h2>
        <p>Persistent account and dashboard functionality is not active under the current owner-approved boundary. The accountless core remains available without login.</p>
      </section>
    </SetupPage>
  );
}
