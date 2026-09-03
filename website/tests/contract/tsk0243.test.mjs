import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { stripTypeScriptTypes } from 'node:module';

const root = resolve(import.meta.dirname, '../..');
const modulePath = resolve(root, 'src/lib/dns-verification-proof.ts');
const requestRoutePath = resolve(root, 'src/app/api/dns-verification/requests/route.ts');
const probeRoutePath = resolve(root, 'src/app/api/dns-verification/probes/route.ts');

async function loadApi() {
  assert.equal(existsSync(modulePath), true, 'missing TSK-0243 trusted DNS verification proof module');
  const source = readFileSync(modulePath, 'utf8');
  const js = stripTypeScriptTypes(source, { mode: 'strip' });
  return import(`data:text/javascript;base64,${Buffer.from(js).toString('base64')}`);
}

const secret = 's'.repeat(64);
const scope = 'ab'.repeat(16);
const challenge = 'cd'.repeat(16);
const otherChallenge = 'ef'.repeat(16);
const now = 10_000;

function observation(overrides = {}) {
  return {
    protocol: 'usesafeweb-dns-path-v1',
    verifierVersion: 'private-rewrite-v1',
    scope,
    challenge,
    outcome: 'verified',
    reasonCode: 'TECH_VERIFIED',
    observedAt: now,
    expiresAt: now + 60_000,
    ...overrides,
  };
}

test('cache-safe probe identity generates a fresh 128-bit challenge under the fixed verification suffix', async () => {
  const api = await loadApi();
  assert.equal(api.DNS_VERIFICATION_SUFFIX, 'verify.usesafeweb.com');
  const first = api.createDnsVerificationChallenge();
  const second = api.createDnsVerificationChallenge();
  assert.match(first, /^[0-9a-f]{32}$/);
  assert.match(second, /^[0-9a-f]{32}$/);
  assert.notEqual(first, second);
  assert.equal(api.buildDnsProbeHostname(first), `${first}.verify.usesafeweb.com`);
  assert.throws(() => api.buildDnsProbeHostname('short'), /invalid dns verification challenge/i);
  assert.throws(() => api.buildDnsProbeHostname('zz'.repeat(16)), /invalid dns verification challenge/i);
});

test('only an untampered fresh proof bound to the current scope and challenge can become verified-fresh', async () => {
  const api = await loadApi();
  const token = api.signDnsVerificationObservation(observation(), secret);
  const result = api.verifyDnsVerificationObservation(token, secret, now + 1_000, scope, challenge);
  assert.deepEqual(result, {
    dnsPath: 'verified-fresh',
    reasonCode: 'TECH_VERIFIED',
    observedAt: now,
    verifierVersion: 'private-rewrite-v1',
  });

  const [payload, signature] = token.split('.');
  const tampered = `${payload.slice(0, -1)}${payload.endsWith('A') ? 'B' : 'A'}.${signature}`;
  assert.equal(api.verifyDnsVerificationObservation(tampered, secret, now + 1_000, scope, challenge), null);
  assert.equal(api.verifyDnsVerificationObservation(token, secret, now + 1_000, '12'.repeat(16), challenge), null);
  assert.equal(api.verifyDnsVerificationObservation(token, secret, now + 1_000, scope, otherChallenge), null, 'a fresh proof from an earlier challenge must not be replayable for the current check');
});

test('stale, failed, uncertain and contradictory observations map fail-closed', async () => {
  const api = await loadApi();
  const fresh = api.signDnsVerificationObservation(observation(), secret);
  const stale = api.signDnsVerificationObservation(observation({ observedAt: 1_000, expiresAt: 2_000 }), secret);
  const failed = api.signDnsVerificationObservation(observation({ outcome: 'failed', reasonCode: 'TECH_VERIFY_NEGATIVE' }), secret);
  const uncertain = api.signDnsVerificationObservation(observation({ outcome: 'uncertain', reasonCode: 'EVIDENCE_CONFLICT' }), secret);

  assert.equal(api.verifyDnsVerificationObservation(stale, secret, now, scope, challenge).dnsPath, 'verified-stale');
  assert.equal(api.verifyDnsVerificationObservation(failed, secret, now + 1_000, scope, challenge).dnsPath, 'failed');
  assert.equal(api.verifyDnsVerificationObservation(uncertain, secret, now + 1_000, scope, challenge).dnsPath, 'uncertain');
  assert.equal(api.reconcileDnsVerificationObservations([], secret, now, scope, challenge).dnsPath, 'not-run');

  const conflicting = api.signDnsVerificationObservation(observation({ outcome: 'failed', reasonCode: 'TECH_VERIFY_NEGATIVE' }), secret);
  assert.equal(api.reconcileDnsVerificationObservations([fresh, conflicting], secret, now + 1_000, scope, challenge).dnsPath, 'uncertain');
  assert.equal(api.reconcileDnsVerificationObservations([fresh, conflicting], secret, now + 1_000, scope, challenge).reasonCode, 'EVIDENCE_CONFLICT');
});

test('proof parser rejects expanded fields, invalid timing, unsupported outcomes and weak signing secrets', async () => {
  const api = await loadApi();
  assert.throws(() => api.signDnsVerificationObservation(observation(), 'weak'), /signing secret/i);
  assert.throws(() => api.signDnsVerificationObservation({ ...observation(), queryHistory: ['example.com'] }, secret), /invalid dns verification observation/i);
  assert.throws(() => api.signDnsVerificationObservation(observation({ expiresAt: now + 10 * 60_000 }), secret), /invalid dns verification observation/i);
  assert.throws(() => api.signDnsVerificationObservation(observation({ outcome: 'working' }), secret), /invalid dns verification observation/i);
});

test('untrusted proof input is byte-bounded and observation batches are count-bounded', async () => {
  const api = await loadApi();
  assert.equal(api.DNS_VERIFICATION_MAX_TOKEN_BYTES, 2048);
  assert.equal(api.DNS_VERIFICATION_MAX_OBSERVATIONS, 8);
  assert.equal(api.verifyDnsVerificationObservation('x'.repeat(2049), secret, now + 1_000, scope, challenge), null);

  const token = api.signDnsVerificationObservation(observation(), secret);
  const oversizedBatch = api.reconcileDnsVerificationObservations(Array(9).fill(token), secret, now + 1_000, scope, challenge);
  assert.equal(oversizedBatch.dnsPath, 'uncertain');
  assert.equal(oversizedBatch.reasonCode, 'VERIFICATION_SERVICE_ERROR');

  const malformedBatch = api.reconcileDnsVerificationObservations(null, secret, now + 1_000, scope, challenge);
  assert.equal(malformedBatch.dnsPath, 'uncertain');
  assert.equal(malformedBatch.reasonCode, 'VERIFICATION_SERVICE_ERROR');
});

test('approved event projection excludes challenge, scope, host, address and browsing/domain history', async () => {
  const api = await loadApi();
  const token = api.signDnsVerificationObservation(observation(), secret);
  const verified = api.verifyDnsVerificationObservation(token, secret, now + 1_000, scope, challenge);
  const event = api.toApprovedDnsVerificationEvent(verified);
  assert.deepEqual(Object.keys(event).sort(), ['dnsPath', 'reasonCode', 'verifierVersion'].sort());
  assert.deepEqual(event, {
    dnsPath: 'verified-fresh',
    reasonCode: 'TECH_VERIFIED',
    verifierVersion: 'private-rewrite-v1',
  });
  for (const forbidden of ['challenge', 'scope', 'host', 'ip', 'address', 'domain', 'query', 'history', 'child', 'account']) {
    assert.equal(Object.keys(event).some((key) => key.toLowerCase().includes(forbidden)), false);
  }
});

test('server-issued probe requests generate their own challenge and are scope-bound, short-lived and domain-separated', async () => {
  const api = await loadApi();
  assert.equal(api.DNS_PROBE_REQUEST_PROTOCOL, 'usesafeweb-dns-probe-request-v1');
  assert.equal(api.DNS_PROBE_REQUEST_MAX_LIFETIME_MS, 120_000);
  const first = api.createDnsProbeRequest(scope, secret, now);
  const second = api.createDnsProbeRequest(scope, secret, now);
  assert.match(first.challenge, /^[0-9a-f]{32}$/);
  assert.notEqual(first.challenge, second.challenge);
  assert.equal(first.probeHost, `${first.challenge}.verify.usesafeweb.com`);
  assert.equal(first.expiresAt, now + 120_000);
  assert.equal(typeof first.requestToken, 'string');
  assert.equal(first.requestToken.includes(scope), false, 'scope must not be exposed in plaintext token text');
  assert.deepEqual(api.verifyDnsProbeRequest(first.requestToken, secret, now + 1_000), {
    scope,
    challenge: first.challenge,
    probeHost: first.probeHost,
    expiresAt: first.expiresAt,
  });
  assert.equal(api.verifyDnsProbeRequest(first.requestToken, secret, first.expiresAt), null);
  assert.equal(api.verifyDnsProbeRequest(first.requestToken, 'x'.repeat(64), now + 1_000), null);
  assert.equal(api.verifyDnsVerificationObservation(first.requestToken, secret, now + 1_000, scope, first.challenge), null, 'request token must never validate as a technical observation');
});

test('positive observation is derived only from valid request token plus exact current probe host', async () => {
  const api = await loadApi();
  const issued = api.createDnsProbeRequest(scope, secret, now);
  const positive = api.createDnsVerificationObservationFromProbeRequest(
    issued.requestToken,
    issued.probeHost,
    secret,
    now + 1_000,
  );
  assert.equal(typeof positive, 'string');
  assert.equal(
    api.verifyDnsVerificationObservation(positive, secret, now + 1_001, scope, issued.challenge).dnsPath,
    'verified-fresh',
  );
  assert.equal(api.createDnsVerificationObservationFromProbeRequest(issued.requestToken, 'usesafeweb.com', secret, now + 1_000), null);
  assert.equal(api.createDnsVerificationObservationFromProbeRequest(issued.requestToken, `${otherChallenge}.verify.usesafeweb.com`, secret, now + 1_000), null);
  assert.equal(api.createDnsVerificationObservationFromProbeRequest(issued.requestToken, `${issued.probeHost}:443`, secret, now + 1_000) !== null, true, 'normal HTTPS Host with :443 remains accepted');
  assert.equal(api.createDnsVerificationObservationFromProbeRequest(issued.requestToken, issued.probeHost, secret, issued.expiresAt), null);
});

test('route handlers expose POST-only node interfaces with bounded input, no-store responses and no client-selected positive outcome', () => {
  assert.equal(existsSync(requestRoutePath), true, 'missing DNS verification request route');
  assert.equal(existsSync(probeRoutePath), true, 'missing DNS verification probe route');
  const requestRoute = readFileSync(requestRoutePath, 'utf8');
  const probeRoute = readFileSync(probeRoutePath, 'utf8');

  for (const source of [requestRoute, probeRoute]) {
    assert.match(source, /export const runtime = ['"]nodejs['"]/);
    assert.match(source, /export async function POST\(/);
    assert.doesNotMatch(source, /export (?:async )?function (?:GET|PUT|PATCH|DELETE|OPTIONS)\(/);
    assert.match(source, /Cache-Control['"]?\s*[:,]\s*['"]no-store['"]/);
    assert.match(source, /DNS_VERIFICATION_MAX_HTTP_BODY_BYTES/);
    assert.match(source, /readBoundedUtf8Body/);
    assert.doesNotMatch(source, /request\.text\(\)/);
    assert.doesNotMatch(source, /x-forwarded-host/i);
    for (const forbidden of ['queryHistory', 'browsingHistory', 'childId', 'accountId', 'clientIp']) {
      assert.equal(source.includes(forbidden), false);
    }
  }

  assert.match(requestRoute, /createDnsProbeRequest/);
  assert.match(requestRoute, /JSON\.parse/);
  assert.doesNotMatch(requestRoute, /createDnsVerificationObservationFromProbeRequest/);

  assert.match(probeRoute, /request\.headers\.get\(['"]host['"]\)/);
  assert.match(probeRoute, /request\.headers\.get\(['"]origin['"]\)/);
  assert.match(probeRoute, /USESAFEWEB_PUBLIC_ORIGIN/);
  assert.match(probeRoute, /Access-Control-Allow-Origin/);
  assert.match(probeRoute, /Vary['"]?\s*[:,]\s*['"]Origin['"]/);
  assert.doesNotMatch(probeRoute, /JSON\.parse/);
  assert.match(probeRoute, /createDnsVerificationObservationFromProbeRequest/);
  assert.doesNotMatch(probeRoute, /\b(?:outcome|reasonCode|challenge|probeHost)\s*=/, 'probe route must not derive positive evidence from client-selected body fields');
});
