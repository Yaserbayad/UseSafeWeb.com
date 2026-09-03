import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { stripTypeScriptTypes } from 'node:module';

const root = resolve(import.meta.dirname, '../..');
const modulePath = resolve(root, 'src/lib/core-state-machine.ts');
const journeyPath = resolve(root, 'src/lib/journey-state.ts');
const profilePath = resolve(root, 'src/lib/ios-doh-profile.ts');
const deliveryRoutePath = resolve(root, 'src/app/api/ios-doh-profile/route.ts');
const recoverPagePath = resolve(root, 'src/app/[locale]/recover/page.tsx');
const cleanupPagePath = resolve(root, 'src/app/[locale]/cleanup/page.tsx');
const cleanupClientPath = resolve(root, 'src/components/revocation-gated-cleanup.tsx');
const dataUrl = (source) => `data:text/javascript;base64,${Buffer.from(source).toString('base64')}`;

async function loadApi() {
  assert.equal(existsSync(modulePath), true, 'missing core state machine');
  let source = readFileSync(modulePath, 'utf8');
  if (source.includes("from './journey-state'")) {
    const journeySource = readFileSync(journeyPath, 'utf8');
    source = source.replace("from './journey-state'", `from '${dataUrl(stripTypeScriptTypes(journeySource, { mode: 'strip' }))}'`);
  }
  return import(dataUrl(stripTypeScriptTypes(source, { mode: 'strip' })));
}

const baseEvidence = {
  coverage: 'covered',
  configured: true,
  technical: null,
  action: null,
  uncertainty: null,
  removal: null,
};

function reachRecovery(api) {
  let state = api.createCoreState('en-GB', 'ab'.repeat(16), 1_000, 10_000);
  state = api.transitionCoreState(state, { type: 'SELECT_DEVICE', deviceFamily: 'iphone' }, 2_000);
  state = api.transitionCoreState(state, { type: 'CONTINUE_NATIVE' }, 2_000);
  state = api.transitionCoreState(state, { type: 'CONTINUE_DNS' }, 2_000);
  state = api.transitionCoreState(state, { type: 'VERIFICATION_RESULT', evidence: baseEvidence }, 2_000);
  state = api.transitionCoreState(state, { type: 'OPEN_TROUBLESHOOT' }, 2_000);
  return api.transitionCoreState(state, { type: 'OPEN_RECOVERY' }, 2_000);
}

test('TSK-0417 requires service revocation evidence before profile cleanup can reach removed', async () => {
  const api = await loadApi();
  const recovery = reachRecovery(api);
  assert.equal(recovery.phase, 'recover');

  assert.throws(
    () => api.transitionCoreState(recovery, { type: 'REMOVE_CONFIGURATION' }, 2_000),
    /service revocation required|invalid core transition/i,
    'profile cleanup must not be reachable directly from recovery',
  );

  const revoked = api.transitionCoreState(
    recovery,
    { type: 'SERVICE_REVOCATION_RESULT', evidence: { ...baseEvidence, removal: 'REVOKED' } },
    2_000,
  );
  assert.equal(revoked.phase, 'cleanup');

  const removed = api.transitionCoreState(revoked, { type: 'REMOVE_CONFIGURATION' }, 2_000);
  assert.equal(removed.phase, 'removed');
});

test('TSK-0417 rejects missing or profile-removal evidence as a substitute for service revocation', async () => {
  const api = await loadApi();
  const recovery = reachRecovery(api);

  for (const evidence of [
    { ...baseEvidence },
    { ...baseEvidence, removal: 'REMOVED_BY_PARENT' },
  ]) {
    assert.throws(
      () => api.transitionCoreState(recovery, { type: 'SERVICE_REVOCATION_RESULT', evidence }, 2_000),
      /service revocation evidence required|invalid core transition/i,
    );
  }
});

test('profile-removal instructions and action are exposed only after the browser session proves cleanup phase', () => {
  assert.equal(existsSync(recoverPagePath), true, 'missing recovery page');
  const recoverSource = readFileSync(recoverPagePath, 'utf8');
  assert.doesNotMatch(recoverSource, /getVersionedInstruction\(locale,\s*platform,\s*'remove'\)/);
  assert.doesNotMatch(recoverSource, /REMOVE_CONFIGURATION/);

  assert.equal(existsSync(cleanupPagePath), true, 'missing revocation-gated cleanup page');
  const cleanupSource = readFileSync(cleanupPagePath, 'utf8');
  assert.match(cleanupSource, /RevocationGatedCleanup/);
  assert.doesNotMatch(cleanupSource, /getVersionedInstruction/);
  assert.doesNotMatch(cleanupSource, /REMOVE_CONFIGURATION/);
  assert.doesNotMatch(cleanupSource, /instruction\.value/);

  assert.equal(existsSync(cleanupClientPath), true, 'missing client-side cleanup authorization boundary');
  const clientSource = readFileSync(cleanupClientPath, 'utf8');
  assert.match(clientSource, /^'use client';/);
  assert.match(clientSource, /readCoreSession\(window\.sessionStorage, Date\.now\(\)\)/);
  assert.match(clientSource, /state\.phase !== 'cleanup'/);
  assert.match(clientSource, /getVersionedInstruction\(locale,\s*platform,\s*'remove'\)/);
  assert.match(clientSource, /event=\{\{ type: 'REMOVE_CONFIGURATION' \}\}/);
});

test('current iPhone artifact is an Apple encrypted-DNS profile with no client credential or identity-certificate cleanup surface', () => {
  assert.equal(existsSync(profilePath), true, 'missing iPhone DoH profile generator');
  assert.equal(existsSync(deliveryRoutePath), true, 'missing gated iPhone profile delivery route');

  const profileSource = readFileSync(profilePath, 'utf8');
  const deliverySource = readFileSync(deliveryRoutePath, 'utf8');

  assert.match(profileSource, /com\.apple\.dnsSettings\.managed/);
  assert.match(profileSource, /https:\/\/dns\.usesafeweb\.com\/dns-query/);
  assert.doesNotMatch(profileSource, /PayloadCertificateUUID|IdentityCertificate|ClientID|credential|authorization|token/i);
  assert.doesNotMatch(deliverySource, /ClientID|credential|authorization|token|certificate/i);
});
