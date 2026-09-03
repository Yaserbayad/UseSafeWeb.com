import { notFound } from 'next/navigation';
import { CoreActionButton } from '@/components/core-action-button';
import { SetupPage, operationalMetadata } from '@/components/setup-page';
import { getContent, getJourneyContent, getVersionedInstruction, isLocale } from '@/lib/i18n';

// TSK-0359 provenance compatibility: direct getInstructionVariant selection for INS-AND-SETUP-01 / INS-IOS-SETUP-01 is delegated to the TSK-0374 versioned release map.
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
  const instruction = getVersionedInstruction(locale, platform, 'setup');

  if (instruction.status !== 'ready') {
    return (
      <SetupPage
        kicker={c.dns.kicker}
        title={isIphone ? c.dns.iphoneTitle : c.dns.androidTitle}
        summary={c.dns.noteBody}
        noteTitle={c.dns.noteTitle}
        noteBody={c.dns.noteBody}
        actions={[
          { href: `/${locale}/help`, label: c.dns.helpLabel, secondary: true },
          { href: `/${locale}/setup/route`, label: c.dns.backLabel, secondary: true },
        ]}
      >
        <p data-content-release={instruction.releaseId} data-content-status={instruction.status}>
          {c.dns.noteBody}
        </p>
      </SetupPage>
    );
  }

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
      <span
        hidden
        data-instruction-id={instruction.instructionId}
        data-instruction-source-locale={instruction.sourceLocale}
        data-content-release={instruction.releaseId}
        data-content-status={instruction.status}
      />
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
