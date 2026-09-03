import Link from 'next/link';
import type { ReactNode } from 'react';
import { getLocaleMeta, locales, type ContentBundle, type Locale } from '@/lib/i18n';

export function SiteShell({
  locale,
  common,
  children,
}: {
  locale: Locale;
  common: ContentBundle['common'];
  children: ReactNode;
}) {
  const nav = [
    ['how-it-works', common.nav.how],
    ['compatibility', common.nav.compatibility],
    ['protection-and-limits', common.nav.limits],
    ['privacy', common.nav.privacy],
    ['help', common.nav.help],
  ] as const;

  return (
    <>
      <a className="sw-skip" href="#main-content">
        {common.skipLink}
      </a>
      <header className="sw-site-header">
        <Link className="sw-site-brand sw-brand-token" href={`/${locale}`}>
          {common.brand}
        </Link>
        <nav aria-label={common.primaryNavigationLabel}>
          <ul className="sw-nav-list">
            {nav.map(([path, label]) => (
              <li key={path}>
                <Link href={`/${locale}/${path}`}>{label}</Link>
              </li>
            ))}
          </ul>
        </nav>
        <div className="sw-header-actions">
          <nav aria-label={common.languageNavigationLabel}>
            <ul className="sw-language-list">
              {locales.map((target) => (
                <li key={target}>
                  <Link href={`/${target}`} hrefLang={target} aria-current={target === locale ? 'page' : undefined}>
                    {getLocaleMeta(target).language}
                  </Link>
                </li>
              ))}
            </ul>
          </nav>
          <Link className="sw-button" href={`/${locale}/start`}>
            {common.nav.start}
          </Link>
        </div>
      </header>
      <main id="main-content" className="sw-main">
        {children}
      </main>
      <footer className="sw-site-footer">
        <div>
          <strong>{common.footerTitle}</strong>
          <p>{common.footerBody}</p>
        </div>
        <nav aria-label={common.primaryNavigationLabel}>
          <Link href={`/${locale}/privacy`}>{common.nav.privacy}</Link>
          <Link href={`/${locale}/help`}>{common.nav.help}</Link>
        </nav>
      </footer>
    </>
  );
}
