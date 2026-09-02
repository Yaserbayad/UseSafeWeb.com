import Link from 'next/link';
import type { Metadata } from 'next';

export const operationalMetadata: Metadata = { robots: { index: false, follow: false } };

type Action = { href: string; label: string; secondary?: boolean };

export function SetupPage({ kicker, title, summary, children, noteTitle, noteBody, actions = [] }: {
  kicker: string;
  title: string;
  summary: string;
  children?: React.ReactNode;
  noteTitle?: string;
  noteBody?: string;
  actions?: Action[];
}) {
  return (
    <article className="sw-page sw-setup sw-stack">
      <header className="sw-stack">
        <p className="sw-kicker">{kicker}</p>
        <h1 className="sw-title">{title}</h1>
        <p className="sw-lede">{summary}</p>
      </header>
      {children}
      {noteTitle && noteBody && <aside className="sw-callout"><strong>{noteTitle}</strong><p>{noteBody}</p></aside>}
      {actions.length > 0 && <div className="sw-actions">{actions.map((action) => <Link key={action.href} className={action.secondary ? 'sw-button sw-button--secondary' : 'sw-button'} href={action.href}>{action.label}</Link>)}</div>}
    </article>
  );
}
