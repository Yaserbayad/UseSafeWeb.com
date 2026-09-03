import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { stripTypeScriptTypes } from 'node:module';

const root = resolve(import.meta.dirname, '../..');
const modulePath = resolve(root, 'src/lib/ios-doh-profile.ts');
const canonicalServerUrl = 'https://dns.usesafeweb.com/dns-query';
const payloadUuid = '11111111-2222-4333-8444-555555555555';
const dnsPayloadUuid = 'AAAAAAAA-BBBB-4CCC-8DDD-EEEEEEEEEEEE';

async function loadApi() {
  assert.equal(existsSync(modulePath), true, 'missing TSK-0360 iPhone DoH profile generator');
  const source = readFileSync(modulePath, 'utf8');
  const js = stripTypeScriptTypes(source, { mode: 'strip' });
  return import(`data:text/javascript;base64,${Buffer.from(js).toString('base64')}`);
}

function verifiedRelease(overrides = {}) {
  return {
    artifactStatus: 'verified',
    version: 2,
    payloadUuid,
    dnsPayloadUuid,
    ...overrides,
  };
}

test('verified iPhone release generates only the canonical SafeWeb DoH profile contract', async () => {
  const api = await loadApi();
  const profile = api.generateSafeWebIosDohProfile(verifiedRelease());

  assert.match(profile, /<key>DNSProtocol<\/key>\s*<string>HTTPS<\/string>/);
  assert.match(profile, new RegExp(`<key>ServerURL<\\/key>\\s*<string>${canonicalServerUrl.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}<\\/string>`));
  assert.match(profile, /<string>com\.apple\.dnsSettings\.managed<\/string>/);
  assert.match(profile, /<string>Configuration<\/string>/);
  assert.match(profile, /<string>com\.usesafeweb\.profile\.doh<\/string>/);
  assert.match(profile, /<string>com\.usesafeweb\.profile\.doh\.dns<\/string>/);
  assert.match(profile, /<string>SafeWeb DNS<\/string>/);
  assert.match(profile, /<string>SafeWeb Encrypted DNS<\/string>/);
  assert.match(profile, /Remove this profile to restore the device's normal DNS settings\./);
  assert.match(profile, new RegExp(`<string>${payloadUuid}<\\/string>`));
  assert.match(profile, new RegExp(`<string>${dnsPayloadUuid}<\\/string>`));
  assert.equal((profile.match(/<integer>2<\/integer>/g) ?? []).length, 2);

  assert.doesNotMatch(profile, /UseSafeWeb DNS|Get UseSafeWeb profile|Turn on UseSafeWeb|first-phone pilot/);
  assert.doesNotMatch(profile, /srv\.usesafeweb\.com|ClientID|credential|password|secret|protected\/verified/i);
});

test('generator fails closed unless release artifact approval is explicit and complete', async () => {
  const api = await loadApi();
  for (const input of [
    verifiedRelease({ artifactStatus: 'pending' }),
    verifiedRelease({ artifactStatus: true }),
    verifiedRelease({ version: 0 }),
    verifiedRelease({ version: -1 }),
    verifiedRelease({ version: 1.5 }),
    verifiedRelease({ version: Number.MAX_SAFE_INTEGER + 1 }),
    verifiedRelease({ payloadUuid: 'not-a-uuid' }),
    verifiedRelease({ dnsPayloadUuid: 'not-a-uuid' }),
    verifiedRelease({ dnsPayloadUuid: payloadUuid }),
  ]) {
    assert.throws(() => api.generateSafeWebIosDohProfile(input));
  }
});

test('generator rejects endpoint overrides, secrets, identifiers, and other undeclared input', async () => {
  const api = await loadApi();
  for (const extra of [
    { serverUrl: 'https://example.invalid/dns-query' },
    { endpoint: canonicalServerUrl },
    { adminUrl: 'https://srv.usesafeweb.com' },
    { clientId: 'child-1' },
    { token: 'secret' },
    { payloadIdentifier: 'com.example.override' },
  ]) {
    assert.throws(() => api.generateSafeWebIosDohProfile(verifiedRelease(extra)));
  }
});

test('generator output is deterministic for the same approved release metadata', async () => {
  const api = await loadApi();
  const input = verifiedRelease();
  assert.equal(api.generateSafeWebIosDohProfile(input), api.generateSafeWebIosDohProfile(input));
});