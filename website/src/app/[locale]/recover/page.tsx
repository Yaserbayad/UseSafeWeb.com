import { notFound } from 'next/navigation';
import { CoreActionButton } from '@/components/core-action-button';
import { CorePageGuard } from '@/components/core-page-guard';
import { SetupPage, operationalMetadata } from '@/components/setup-page';
import { getContent, getJourneyContent, getVersionedInstruction, isLocale } from '@/lib/i18n';

// TSK-0359 provenance compatibility: INS-AND-REMOVE-01 / INS-IOS-REMOVE-01 selection is delegated to the TSK-0374 versioned release map.
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

  const c = getContent(locale);
  const content = getJourneyContent(locale, 'recover').value;
  const instruction = getVersionedInstruction(locale, platform, 'remove');

  if (instruction.status !== 'ready') {
    return (
      <SetupPage
        kicker={content.kicker}
        title={content.title}
        summary={c.route.noteBody}
        noteTitle={c.route.noteTitle}
        noteBody={c.route.noteBody}
        actions={[
          { href: `/${locale}/help`, label: c.dns.helpLabel, secondary: true },
          { href: `/${locale}/setup/route`, label: c.dns.backLabel, secondary: true },
        ]}
      >
        <CorePageGuard locale={locale} expectedPhase="recover" />
        <p data-content-release={instruction.releaseId} data-content-status={instruction.status}>
          <span className="sw-technical">{instruction.status}</span> {c.route.noteBody}
        </p>
      </SetupPage>
    );
  }

  return (
    <SetupPage
      kicker={content.kicker}
      title={content.title}
      summary={content.summary}
      noteTitle={content.noteTitle}
      noteBody={content.noteBody}
    >
      <CorePageGuard locale={locale} expectedPhase="recover" />
      <p
        data-instruction-id={instruction.instructionId}
        data-instruction-source-locale={instruction.sourceLocale}
        data-content-release={instruction.releaseId}
        data-content-status={instruction.status}
      >
        {instruction.value}
      </p>
      <div className="sw-actions">
        <CoreActionButton
          locale={locale}
          deviceFamily={platform}
          event={{ type: 'REMOVE_CONFIGURATION' }}
          href={`/${locale}/removed?platform=${platform}`}
          label={content.actionLabel}
          dataAttribute="data-core-remove"
        />
      </div>
    </SetupPage>
  );
}
