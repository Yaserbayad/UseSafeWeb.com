import Link from 'next/link';

type Card = { title: string; body: string };
type Action = { href: string; label: string; secondary?: boolean };

type Section = {
  kicker: string;
  title: string;
  summary: string;
  cards?: Card[];
  noteTitle?: string;
  noteBody?: string;
};

export function ContentPage({ section, actions = [] }: { section: Section; actions?: Action[] }) {
  return (
    <article className="sw-page sw-stack">
      <header className="sw-hero sw-stack">
        <p className="sw-kicker">{section.kicker}</p>
        <h1 className="sw-title">{section.title}</h1>
        <p className="sw-lede">{section.summary}</p>
        {actions.length > 0 && (
          <div className="sw-actions">
            {actions.map((action) => (
              <Link key={action.href} className={action.secondary ? 'sw-button sw-button--secondary' : 'sw-button'} href={action.href}>{action.label}</Link>
            ))}
          </div>
        )}
      </header>
      {section.cards && <div className="sw-card-grid">{section.cards.map((card) => <section className="sw-card" key={card.title}><h2>{card.title}</h2><p>{card.body}</p></section>)}</div>}
      {section.noteTitle && section.noteBody && <aside className="sw-callout"><strong>{section.noteTitle}</strong><p>{section.noteBody}</p></aside>}
    </article>
  );
}
