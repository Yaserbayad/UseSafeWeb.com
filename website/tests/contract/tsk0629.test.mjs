import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { stripTypeScriptTypes } from 'node:module';

const root = resolve(import.meta.dirname, '../..');
const modulePath = resolve(root, 'src/lib/automated-verification.ts');

async function loadApi() {
  assert.equal(existsSync(modulePath), true, 'missing TSK-0629 privacy-safe automated-check classifier');
  const source = readFileSync(modulePath, 'utf8');
  const js = stripTypeScriptTypes(source, { mode: 'strip' });
  return import(`data:text/javascript;base64,${Buffer.from(js).toString('base64')}`);
}

const base = {
  support: 'supported',
  service: 'healthy',
  dnsPath: 'not-run',
  configured: true,
  removed: false,
};

test('fresh trusted DNS-path evidence is the only automated route to working/verified', async () => {
  const api = await loadApi();
  const result = api.classifyAutomatedChecks({ ...base, dnsPath: 'verified-fresh' });
  assert.equal(result.checkState, 'working');
  assert.equal(result.parentConfirmation, 'confirmed');
  assert.equal(result.recovery, null);
  assert.deepEqual(result.evidence.technical, { result: 'positive', fresh: true });
  assert.equal(result.evidence.uncertainty, null);
  assert.equal(result.evidence.removal, null);
});

test('parent confirmation remains separate and cannot manufacture a working result', async () => {
  const api = await loadApi();
  const result = api.classifyAutomatedChecks(base);
  assert.equal(result.parentConfirmation, 'confirmed');
  assert.equal(result.checkState, 'uncertain');
  assert.equal(result.evidence.configured, true);
  assert.equal(result.evidence.technical, null);
  assert.equal(result.evidence.uncertainty, 'VERIFY_UNREACHABLE');
  assert.equal(result.recovery, 'troubleshoot');
});

test('failed, stale, conflicting, unsupported and removed checks map fail-closed with actionable recovery', async () => {
  const api = await loadApi();

  const failed = api.classifyAutomatedChecks({ ...base, dnsPath: 'failed' });
  assert.equal(failed.checkState, 'failed');
  assert.deepEqual(failed.evidence.technical, { result: 'negative', fresh: true });
  assert.equal(failed.recovery, 'troubleshoot');

  const stale = api.classifyAutomatedChecks({ ...base, dnsPath: 'verified-stale' });
  assert.equal(stale.checkState, 'uncertain');
  assert.deepEqual(stale.evidence.technical, { result: 'positive', fresh: false });
  assert.equal(stale.recovery, 'troubleshoot');

  const conflict = api.classifyAutomatedChecks({ ...base, dnsPath: 'uncertain' });
  assert.equal(conflict.checkState, 'uncertain');
  assert.equal(conflict.evidence.uncertainty, 'EVIDENCE_CONFLICT');
  assert.equal(conflict.recovery, 'troubleshoot');

  const unsupported = api.classifyAutomatedChecks({ ...base, support: 'not-covered' });
  assert.equal(unsupported.checkState, 'not-covered');
  assert.equal(unsupported.evidence.coverage, 'not-covered');
  assert.equal(unsupported.recovery, null);

  const removed = api.classifyAutomatedChecks({ ...base, removed: true });
  assert.equal(removed.checkState, 'removed');
  assert.equal(removed.evidence.removal, 'REMOVED_BY_PARENT');
  assert.equal(removed.recovery, null);
});

test('service/check uncertainty overrides setup optimism and never preserves a positive claim', async () => {
  const api = await loadApi();
  for (const service of ['degraded', 'unavailable', 'unknown']) {
    const result = api.classifyAutomatedChecks({ ...base, service, dnsPath: 'verified-fresh' });
    assert.equal(result.checkState, 'uncertain', service);
    assert.equal(result.evidence.technical, null, service);
    assert.equal(result.recovery, 'troubleshoot', service);
  }
  const unknownSupport = api.classifyAutomatedChecks({ ...base, support: 'unknown', dnsPath: 'verified-fresh' });
  assert.equal(unknownSupport.checkState, 'uncertain');
  assert.equal(unknownSupport.evidence.uncertainty, 'BYPASS_OR_CONTEXT_UNCERTAIN');
});

test('runtime input is exact-field allowlisted and rejects browsing/history/diagnostic payload expansion', async () => {
  const api = await loadApi();
  for (const extra of [
    { query: 'example.com' },
    { domainHistory: ['example.com'] },
    { browsing: true },
    { diagnostic: 'raw' },
    { accountId: 'parent-1' },
    { childId: 'child-1' },
  ]) {
    assert.throws(() => api.classifyAutomatedChecks({ ...base, ...extra }), /invalid automated verification input/);
  }
  assert.throws(() => api.classifyAutomatedChecks({ ...base, dnsPath: 'verified' }), /invalid automated verification input/);
  assert.throws(() => api.classifyAutomatedChecks(null), /invalid automated verification input/);
});
