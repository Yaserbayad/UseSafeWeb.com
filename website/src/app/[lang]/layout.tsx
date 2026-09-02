import Link from "next/link";
import { notFound } from "next/navigation";
import { directionFor, isLocale, localeLabels, locales } from "@/lib/i18n";

export function generateStaticParams() {
  return locales.map((lang) => ({ lang }));
}

export default async function LocaleLayout({ children, params }: Readonly<{ children: React.ReactNode; params: Promise<{ lang: string }> }>) {
  const { lang } = await params;
  if (!isLocale(lang)) notFound();

  return (
    <div className="sw-shell usw-site" lang={lang} dir={directionFor(lang)}>
      <header className="usw-header">
        <Link className="usw-brand sw-brand-token" href={`/${lang}`}>SafeWeb</Link>
        <nav className="usw-language-nav" aria-label="Language">
          {locales.map((locale) => (
            <Link key={locale} href={`/${locale}`} hrefLang={locale} aria-current={locale === lang ? "page" : undefined}>
              {localeLabels[locale]}
            </Link>
          ))}
        </nav>
      </header>
      {children}
      <footer className="usw-footer sw-muted">
        <p>SafeWeb · First phone safety setup · No browsing-history product data.</p>
      </footer>
    </div>
  );
}
