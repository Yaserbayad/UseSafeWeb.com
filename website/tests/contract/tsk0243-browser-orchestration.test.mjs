import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { stripTypeScriptTypes } from 'node:module';

const root = resolve(import.meta.dirname, '../..');
const clientPath = resolve(root, 'src/lib/dns-verification-browser.ts');
const resultRoutePath = resolve(root, 'src/app/api/dns-verification/results/route.ts');
const verifyPanelPath = resolve(root, 'src/components/dns-verification-panel.tsx');
const protectionCardPath = resolve(root, 'src/components/dns-verification-card.tsx');

async function loadClient() {
  assert.equal(existsSync(clientPath), true, 'missing TSK-0243 browser orchestration module');
  const source = readFileSync(clientPath, 'utf8');
  const js = stripTypeScriptTypes(source, { mode: 'strip' });
  return import(`data:text/javascript;base64,${Buffer.from(js).toString('base64')}`);
}

const scope = 'ab'.repeat(16);
const challenge = 'cd'.repeat(16);
const probeHost = `${challenge}.verify.usesafeweb.com`;
const requestToken = 'request-token-value';
const observationToken = 'observation-token-value';

function jsonResponse(body, status = 200, headers = {}) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json', ...headers },
  });
}

test('browser orchestration performs request -> dedicated probe -> server result verification with minimal transport', async () => {
  const api = await loadClient();
  const calls = [];
  const fetchImpl = async (url, options) => {
    calls.push({ url, options });
    if (calls.length === 1) {
      return jsonResponse({ challenge, probeHost, requestToken, expiresAt: 120_000 }, 201);
    }
    if (calls.length === 2) {
      return jsonResponse({ observationToken }, 200, { 'Access-Control-Allow-Origin': 'https://usesafeweb.com' });
    }
    return jsonResponse({ dnsPath: 'verified-fresh', reasonCode: 'TECH_VERIFIED', verifierVersion: 'private-rewrite-v1' });
  };

  const result = await api.runDnsVerification(scope, fetchImpl, 5_000);
  assert.deepEqual(result, {
    check: { dnsPath: 'verified-fresh', reasonCode: 'TECH_VERIFIED', verifierVersion: 'private-rewrite-v1' },
    proof: { challenge, observationToken },
  });
  assert.equal(calls.length, 3);
  assert.equal(calls[0].url, '/api/dns-verification/requests');
  assert.equal(calls[0].options.method, 'POST');
  assert.equal(calls[0].options.credentials, 'same-origin');
  assert.equal(calls[0].options.cache, 'no-store');
  assert.deepEqual(JSON.parse(calls[0].options.body), { scope });

  assert.equal(calls[1].url, `https://${probeHost}/api/dns-verification/probes`);
  assert.equal(calls[1].options.method, 'POST');
  assert.equal(calls[1].options.credentials, 'omit');
  assert.equal(calls[1].options.cache, 'no-store');
  assert.equal(calls[1].options.headers['Content-Type'], 'text/plain');
  assert.equal(calls[1].options.body, requestToken);

  assert.equal(calls[2].url, '/api/dns-verification/results');
  assert.equal(calls[2].options.credentials, 'same-origin');
  assert.deepEqual(JSON.parse(calls[2].options.body), { scope, challenge, observationToken });
});

test('browser rejects arbitrary probe origins before any cross-origin request', async () => {
  const api = await loadClient();
  const calls = [];
  const fetchImpl = async (url, options) => {
    calls.push({ url, options });
    return jsonResponse({
      challenge,
      probeHost: 'attacker.example',
      requestToken,
      expiresAt: 120_000,
    }, 201);
  };
  assert.equal(await api.runDnsVerification(scope, fetchImpl, 5_000), null);
  assert.equal(calls.length, 1);
});

test('network, status, schema, timeout and server-verification failures stay fail-closed', async () => {
  const api = await loadClient();
  assert.equal(await api.runDnsVerification(scope, async () => { throw new TypeError('network'); }, 5_000), null);
  assert.equal(await api.runDnsVerification(scope, async () => new Response('', { status: 503 }), 5_000), null);
  assert.equal(await api.runDnsVerification('bad', async () => { throw new Error('must not fetch'); }, 5_000), null);

  let call = 0;
  const malformed = async () => {
    call += 1;
    if (call === 1) return jsonResponse({ challenge, probeHost, requestToken, expiresAt: 120_000 }, 201);
    if (call === 2) return jsonResponse({ observationToken });
    return jsonResponse({ dnsPath: 'working', reasonCode: 'TECH_VERIFIED', verifierVersion: 'private-rewrite-v1' });
  };
  assert.equal(await api.runDnsVerification(scope, malformed, 5_000), null);
});

test('stored proof is opaque/minimal and every positive restoration requires server revalidation', async () => {
  const api = await loadClient();
  const map = new Map();
  const storage = {
    getItem: (key) => map.has(key) ? map.get(key) : null,
    setItem: (key, value) => map.set(key, value),
    removeItem: (key) => map.delete(key),
  };
  assert.equal(api.DNS_VERIFICATION_STORAGE_KEY, 'usesafeweb:dns-verification:v1');
  api.writeDnsVerificationProof(storage, { challenge, observationToken });
  const raw = map.get(api.DNS_VERIFICATION_STORAGE_KEY);
  assert.deepEqual(JSON.parse(raw), { challenge, observationToken });
  for (const forbidden of ['dnsPath', 'reasonCode', 'working', 'verified', 'scope', 'domain', 'query', 'history', 'ip', 'account', 'child']) {
    assert.equal(raw.toLowerCase().includes(forbidden.toLowerCase()), false, forbidden);
  }
  assert.deepEqual(api.readDnsVerificationProof(storage), { challenge, observationToken });

  const calls = [];
  const check = await api.revalidateDnsVerificationProof(scope, { challenge, observationToken }, async (url, options) => {
    calls.push({ url, options });
    return jsonResponse({ dnsPath: 'verified-fresh', reasonCode: 'TECH_VERIFIED', verifierVersion: 'private-rewrite-v1' });
  }, 5_000);
  assert.deepEqual(check, { dnsPath: 'verified-fresh', reasonCode: 'TECH_VERIFIED', verifierVersion: 'private-rewrite-v1' });
  assert.equal(calls.length, 1);
  assert.equal(calls[0].url, '/api/dns-verification/results');

  map.set(api.DNS_VERIFICATION_STORAGE_KEY, JSON.stringify({ challenge, observationToken, working: true }));
  assert.equal(api.readDnsVerificationProof(storage), null);
});

test('result route verifies HMAC server-side and emits only the approved check projection', () => {
  assert.equal(existsSync(resultRoutePath), true, 'missing observation result verification route');
  const source = readFileSync(resultRoutePath, 'utf8');
  assert.match(source, /export const runtime = ['"]nodejs['"]/);
  assert.match(source, /export async function POST\(/);
  assert.match(source, /readBoundedUtf8Body/);
  assert.match(source, /verifyDnsVerificationObservation/);
  assert.match(source, /toApprovedDnsVerificationEvent/);
  assert.match(source, /USESAFEWEB_DNS_VERIFICATION_SIGNING_SECRET/);
  assert.match(source, /Cache-Control['"]?\s*[:,]\s*['"]no-store['"]/);
  assert.doesNotMatch(source, /x-forwarded-host/i);
  for (const forbidden of ['queryHistory', 'browsingHistory', 'childId', 'accountId', 'clientIp']) {
    assert.equal(source.includes(forbidden), false);
  }
});

test('verify and Protection Map use client components; no bare positive state is accepted from URL or storage', () => {
  assert.equal(existsSync(verifyPanelPath), true, 'missing live DNS verification panel');
  assert.equal(existsSync(protectionCardPath), true, 'missing revalidating DNS Protection Map card');
  const panel = readFileSync(verifyPanelPath, 'utf8');
  const card = readFileSync(protectionCardPath, 'utf8');
  const verifyPage = readFileSync(resolve(root, 'src/app/[locale]/verify/page.tsx'), 'utf8');
  const protectionPage = readFileSync(resolve(root, 'src/app/[locale]/protection/page.tsx'), 'utf8');

  assert.match(panel, /runDnsVerification/);
  assert.match(panel, /readCoreSession\(window\.sessionStorage/);
  assert.match(panel, /writeDnsVerificationProof/);
  assert.match(panel, /aria-live=['"]polite['"]/);
  assert.doesNotMatch(panel, /searchParams|URLSearchParams/);

  assert.match(card, /readDnsVerificationProof/);
  assert.match(card, /revalidateDnsVerificationProof/);
  assert.match(card, /readCoreSession\(window\.sessionStorage/);
  assert.match(card, /aria-live=['"]polite['"]/);
  assert.doesNotMatch(card, /searchParams|URLSearchParams/);

  assert.match(verifyPage, /DnsVerificationPanel/);
  assert.match(protectionPage, /DnsVerificationCard/);
  assert.doesNotMatch(verifyPage, /getCurrentAutomatedVerification\(\)/);
  assert.doesNotMatch(protectionPage, /getCurrentAutomatedVerification\(\)/);
});
