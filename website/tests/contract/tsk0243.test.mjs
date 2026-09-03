import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { stripTypeScriptTypes } from 'node:module';

const root = resolve(import.meta.dirname, '../..');
const modulePath = resolve(root, 'src/lib/dns-verification-proof.ts');

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

test('cache-safe probe identity uses a fresh 128-bit challenge under the fixed verification suffix', async () => {
  const api = await loadApi();
  assert.equal(api.DNS_VERIFICATION_SUFFIX, 'verify.usesafeweb.com');
  assert.equal(api.buildDnsProbeHostname(challenge), `${challenge}.verify.usesafeweb.com`);
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
