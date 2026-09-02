import Link from "next/link";
import { notFound } from "next/navigation";
import { directionFor, isLocale, localeLabels, locales, sharedCopy } from "@/lib/i18n";

export function generateStaticParams() {
  return locales.map((lang) => ({ lang }));
}

export default async function LocaleLayout({ children, params }: Readonly<{ children: React.ReactNode; params: Promise<{ lang: string }> }>) {
  const { lang } = await params;
  if (!isLocale(lang)) notFound();
  const ui = sharedCopy[lang];

  return (
    <div className="sw-shell usw-site" lang={lang} dir={directionFor(lang)}>
      <header className="usw-header">
        <Link className="usw-brand sw-brand-token" href={`/${lang}`}>SafeWeb</Link>
        <nav className="usw-language-nav" aria-label={ui.languageNavLabel}>
          {locales.map((locale) => (
            <Link key={locale} href={`/${locale}`} hrefLang={locale} aria-current={locale === lang ? "page" : undefined}>
              {localeLabels[locale]}
            </Link>
          ))}
        </nav>
      </header>
      {children}
      <footer className="usw-footer sw-muted">
        <p>{ui.footer}</p>
      </footer>
    </div>
  );
}
