import { createHash } from 'node:crypto';
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
const sha256Pattern = /^[0-9a-fA-F]{64}$/;

function unavailable(status: 404 | 503): Response {
  return new Response(null, { status, headers: noStoreHeaders });
}

export async function GET(): Promise<Response> {
  if (process.env.USESAFEWEB_IOS_PROFILE_DELIVERY_ENABLED !== 'true') {
    return unavailable(404);
  }

  const payloadUuid = process.env.USESAFEWEB_IOS_PROFILE_PAYLOAD_UUID;
  const dnsPayloadUuid = process.env.USESAFEWEB_IOS_PROFILE_DNS_PAYLOAD_UUID;
  const expectedSha256 = process.env.USESAFEWEB_IOS_PROFILE_EXPECTED_SHA256;
  if (!payloadUuid || !dnsPayloadUuid || !expectedSha256 || !sha256Pattern.test(expectedSha256)) {
    return unavailable(503);
  }

  try {
    const profile = generateSafeWebIosDohProfile({ payloadUuid, dnsPayloadUuid });
    const actualSha256 = createHash('sha256').update(profile, 'utf8').digest('hex');
    if (actualSha256 !== expectedSha256.toLowerCase()) {
      return unavailable(503);
    }
    return new Response(profile, { status: 200, headers: profileHeaders });
  } catch {
    return unavailable(503);
  }
}
