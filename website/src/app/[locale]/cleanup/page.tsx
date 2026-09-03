import { notFound } from 'next/navigation';
import { RevocationGatedCleanup } from '@/components/revocation-gated-cleanup';
import { operationalMetadata } from '@/components/setup-page';
import { isLocale } from '@/lib/i18n';

// TSK-0417: the server route validates only locale/platform. Removal UI is client-rendered only after session state proves prior revocation.
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

  return <RevocationGatedCleanup locale={locale} platform={platform} />;
}
