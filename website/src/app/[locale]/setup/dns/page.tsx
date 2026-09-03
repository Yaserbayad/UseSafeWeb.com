import { notFound } from 'next/navigation';
import { CoreActionButton } from '@/components/core-action-button';
import { SetupPage, operationalMetadata } from '@/components/setup-page';
import { getContent, getInstructionVariant, getJourneyContent, isLocale } from '@/lib/i18n';

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
  const verifyContent = getJourneyContent(locale, 'verify').value;
  const isIphone = platform === 'iphone';
  const instructionId = isIphone ? 'INS-IOS-SETUP-01' : 'INS-AND-SETUP-01';
  const instruction = getInstructionVariant(locale, instructionId);

  return (
    <SetupPage
      kicker={c.dns.kicker}
      title={isIphone ? c.dns.iphoneTitle : c.dns.androidTitle}
      summary={instruction.value}
      noteTitle={c.dns.noteTitle}
      noteBody={c.dns.noteBody}
      actions={[
        { href: `/${locale}/help`, label: c.dns.helpLabel, secondary: true },
        { href: `/${locale}/setup/route`, label: c.dns.backLabel, secondary: true },
      ]}
    >
      <p data-instruction-id={instruction.instructionId} data-instruction-source-locale={instruction.sourceLocale}>
        {instruction.value}
      </p>
      {isIphone && <p className="sw-technical">{c.common.dohUrl}</p>}
      <div className="sw-actions">
        <CoreActionButton
          locale={locale}
          deviceFamily={platform}
          event={{ type: 'CONTINUE_DNS' }}
          href={`/${locale}/verify?platform=${platform}`}
          label={verifyContent.dnsContinueLabel}
          dataAttribute="data-core-continue-dns"
        />
      </div>
    </SetupPage>
  );
}
