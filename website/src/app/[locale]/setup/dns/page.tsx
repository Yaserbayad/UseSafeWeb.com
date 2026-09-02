import { notFound } from 'next/navigation';
import { CoreActionButton } from '@/components/core-action-button';
import { SetupPage, operationalMetadata } from '@/components/setup-page';
import { getContent, isLocale } from '@/lib/i18n';

export const metadata = operationalMetadata;

export default async function Page({
  params,
  searchParams,
}: {
  params: Promise<{ locale: string }>;
  searchParams: Promise<{ platform?: string | string[] }>;
}) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();

  const query = await searchParams;
  const platform = typeof query.platform === 'string' ? query.platform : undefined;
  if (platform !== 'android' && platform !== 'iphone') notFound();

  const c = getContent(locale);
  const isIphone = platform === 'iphone';
  return (
    <SetupPage
      kicker={c.dns.kicker}
      title={isIphone ? c.dns.iphoneTitle : c.dns.androidTitle}
      summary={isIphone ? c.dns.iphoneIntro : c.dns.androidIntro}
      noteTitle={c.dns.noteTitle}
      noteBody={c.dns.noteBody}
      actions={[
        { href: `/${locale}/help`, label: c.dns.helpLabel, secondary: true },
        { href: `/${locale}/setup/route`, label: c.dns.backLabel, secondary: true },
      ]}
    >
      {!isIphone && (
        <ol className="sw-instruction-list">
          {c.dns.androidSteps.map((step) => (
            <li key={step}>
              {step.includes(c.common.dnsHostname) ? <span className="sw-technical">{step}</span> : step}
            </li>
          ))}
        </ol>
      )}
      {isIphone && <p className="sw-technical">{c.common.dohUrl}</p>}
      <div className="sw-actions">
        <CoreActionButton
          locale={locale}
          deviceFamily={platform}
          event={{ type: 'CONTINUE_DNS' }}
          href={`/${locale}/verify?platform=${platform}`}
          label="I saved this DNS setting — check protection"
          dataAttribute="data-core-continue-dns"
        />
      </div>
    </SetupPage>
  );
}
