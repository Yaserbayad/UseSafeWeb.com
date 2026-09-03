import { notFound } from 'next/navigation';
import { SetupPage, operationalMetadata } from '@/components/setup-page';
import { getContent, isLocale } from '@/lib/i18n';
import { resolveIntakeRoute } from '@/lib/intake-routing';

export const metadata = operationalMetadata;

export default async function Page({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();

  const c = getContent(locale);
  const android = resolveIntakeRoute({ locale, choice: 'android' });
  const iphone = resolveIntakeRoute({ locale, choice: 'iphone' });
  const other = resolveIntakeRoute({ locale, choice: 'other' });

  return (
    <SetupPage
      kicker={c.route.kicker}
      title={c.route.title}
      summary={c.route.summary}
      noteTitle={c.route.noteTitle}
      noteBody={c.route.noteBody}
      actions={[
        { href: android.href, label: c.route.androidLabel },
        { href: iphone.href, label: c.route.iphoneLabel },
        { href: other.href, label: c.route.otherLabel, secondary: true },
      ]}
    />
  );
}
