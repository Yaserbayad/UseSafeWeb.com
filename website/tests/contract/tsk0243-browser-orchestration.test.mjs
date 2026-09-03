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

test('browser orchestration performs request -> dedicated probe -> server result verification with minimal transient transport', async () => {
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
  assert.deepEqual(result, { dnsPath: 'verified-fresh', reasonCode: 'TECH_VERIFIED', verifierVersion: 'private-rewrite-v1' });
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
  assert.deepEqual(JSON.parse(calls[2].options.body), { requestToken, observationToken });
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

test('browser proof material remains transient and no verification token or challenge is persisted', async () => {
  const api = await loadClient();
  const source = readFileSync(clientPath, 'utf8');
  for (const legacyExport of [
    'DNS_VERIFICATION_STORAGE_KEY',
    'writeDnsVerificationProof',
    'readDnsVerificationProof',
    'revalidateDnsVerificationProof',
    'clearDnsVerificationProof',
  ]) {
    assert.equal(Object.prototype.hasOwnProperty.call(api, legacyExport), false, legacyExport);
    assert.equal(source.includes(`export function ${legacyExport}`), false, legacyExport);
    assert.equal(source.includes(`export async function ${legacyExport}`), false, legacyExport);
  }
  assert.doesNotMatch(source, /sessionStorage|localStorage|\.setItem\(|\.getItem\(|\.removeItem\(/);
});

test('result route verifies both signed request and observation server-side and emits only the approved check projection', () => {
  assert.equal(existsSync(resultRoutePath), true, 'missing observation result verification route');
  const source = readFileSync(resultRoutePath, 'utf8');
  assert.match(source, /export const runtime = ['"]nodejs['"]/);
  assert.match(source, /export async function POST\(/);
  assert.match(source, /readBoundedUtf8Body/);
  assert.match(source, /verifyDnsProbeRequest/);
  assert.match(source, /verifyDnsVerificationObservation/);
  assert.match(source, /toApprovedDnsVerificationEvent/);
  assert.match(source, /USESAFEWEB_DNS_VERIFICATION_SIGNING_SECRET/);
  assert.match(source, /Cache-Control['"]?\s*[:,]\s*['"]no-store['"]/);
  assert.match(source, /requestToken/);
  assert.match(source, /observationToken/);
  assert.doesNotMatch(source, /body\.scope|body\.challenge/);
  assert.doesNotMatch(source, /x-forwarded-host/i);
  for (const forbidden of ['queryHistory', 'browsingHistory', 'childId', 'accountId', 'clientIp']) {
    assert.equal(source.includes(forbidden), false);
  }
});

test('verify and Protection Map perform fresh client checks; no bare positive state or proof is accepted from URL or storage', () => {
  assert.equal(existsSync(verifyPanelPath), true, 'missing live DNS verification panel');
  assert.equal(existsSync(protectionCardPath), true, 'missing live DNS Protection Map card');
  const panel = readFileSync(verifyPanelPath, 'utf8');
  const card = readFileSync(protectionCardPath, 'utf8');
  const verifyPage = readFileSync(resolve(root, 'src/app/[locale]/verify/page.tsx'), 'utf8');
  const protectionPage = readFileSync(resolve(root, 'src/app/[locale]/protection/page.tsx'), 'utf8');

  for (const source of [panel, card]) {
    assert.match(source, /runDnsVerification/);
    assert.match(source, /readCoreSession\(window\.sessionStorage/);
    assert.match(source, /aria-live=['"]polite['"]/);
    assert.doesNotMatch(source, /searchParams|URLSearchParams/);
    assert.doesNotMatch(source, /writeDnsVerificationProof|readDnsVerificationProof|revalidateDnsVerificationProof|clearDnsVerificationProof/);
  }

  assert.match(verifyPage, /DnsVerificationPanel/);
  assert.match(protectionPage, /DnsVerificationCard/);
  assert.doesNotMatch(verifyPage, /getCurrentAutomatedVerification\(\)/);
  assert.doesNotMatch(protectionPage, /getCurrentAutomatedVerification\(\)/);
});
