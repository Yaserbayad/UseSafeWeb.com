import { generateSafeWebIosDohProfile } from '@/lib/ios-doh-profile';

export const runtime = 'nodejs';
export const dynamic = 'force-dynamic';

const noStoreHeaders = { 'Cache-Control': 'no-store' } as const;
const profileHeaders = {
  'Cache-Control': 'no-store',
  'Content-Type': 'application/x-apple-aspen-config',
  'Content-Disposition': 'attachment; filename="SafeWeb-DNS.mobileconfig"',
  'X-Content-Type-Options': 'nosniff',
} as const;

function unavailable(status: 404 | 503): Response {
  return new Response(null, { status, headers: noStoreHeaders });
}

export async function GET(): Promise<Response> {
  if (process.env.USESAFEWEB_IOS_PROFILE_DELIVERY_ENABLED !== 'true') {
    return unavailable(404);
  }

  const payloadUuid = process.env.USESAFEWEB_IOS_PROFILE_PAYLOAD_UUID;
  const dnsPayloadUuid = process.env.USESAFEWEB_IOS_PROFILE_DNS_PAYLOAD_UUID;
  if (!payloadUuid || !dnsPayloadUuid) {
    return unavailable(503);
  }

  try {
    const profile = generateSafeWebIosDohProfile({ payloadUuid, dnsPayloadUuid });
    return new Response(profile, { status: 200, headers: profileHeaders });
  } catch {
    return unavailable(503);
  }
}
