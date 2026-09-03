import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { stripTypeScriptTypes } from 'node:module';

const root = resolve(import.meta.dirname, '../..');
const modulePath = resolve(root, 'src/lib/dns-verification-browser.ts');

async function loadApi() {
  const source = readFileSync(modulePath, 'utf8');
  const js = stripTypeScriptTypes(source, { mode: 'strip' });
  return import(`data:text/javascript;base64,${Buffer.from(js).toString('base64')}`);
}

function jsonResponse(body) {
  return new Response(JSON.stringify(body), { status: 200, headers: { 'Content-Type': 'application/json' } });
}

const scope = 'ab'.repeat(16);
const challenge = 'cd'.repeat(16);
const probeHost = `${challenge}.verify.usesafeweb.com`;
const requestToken = 'request-token-value';
const observationToken = 'observation-token-value';

test('browser accepts only semantically consistent dnsPath/reasonCode pairs from the trusted result route', async () => {
  const api = await loadApi();
  const cases = [
    { dnsPath: 'verified-fresh', reasonCode: 'EVIDENCE_CONFLICT', verifierVersion: 'private-rewrite-v1' },
    { dnsPath: 'failed', reasonCode: 'TECH_VERIFIED', verifierVersion: 'private-rewrite-v1' },
    { dnsPath: 'not-run', reasonCode: 'VERIFICATION_SERVICE_ERROR', verifierVersion: 'private-rewrite-v1' },
    { dnsPath: 'verified-stale', reasonCode: 'TECH_VERIFIED', verifierVersion: 'private-rewrite-v1' },
  ];
  for (const result of cases) {
    let call = 0;
    const fetchImpl = async () => {
      call += 1;
      if (call === 1) return jsonResponse({ challenge, probeHost, requestToken, expiresAt: 120_000 });
      if (call === 2) return jsonResponse({ observationToken });
      return jsonResponse(result);
    };
    assert.equal(await api.runDnsVerification(scope, fetchImpl, 5_000), null, `${result.dnsPath}/${result.reasonCode}`);
    assert.equal(call, 3);
  }
});
