import { notFound } from 'next/navigation';
import { JourneyResumePanel } from '@/components/journey-resume-panel';
import { SetupPage, operationalMetadata } from '@/components/setup-page';
import { getContent, isLocale } from '@/lib/i18n';

export const metadata = operationalMetadata;
export default async function Page({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();
  const c = getContent(locale);
  return (
    <SetupPage
      kicker={c.start.kicker}
      title={c.start.title}
      summary={c.start.summary}
      noteTitle={c.start.noteTitle}
      noteBody={c.start.noteBody}
      actions={[{ href: `/${locale}/setup/route`, label: c.start.primaryLabel }]}
    >
      <JourneyResumePanel
        locale={locale}
        resumeLabel={c.start.resumeLabel}
        resetLabel={c.start.resetLabel}
        resumeNote={c.start.resumeNote}
      />
      <div className="sw-card-grid">
        {c.start.cards.map((card) => (
          <section className="sw-card" key={card.title}>
            <h2>{card.title}</h2>
            <p>{card.body}</p>
          </section>
        ))}
      </div>
    </SetupPage>
  );
}
