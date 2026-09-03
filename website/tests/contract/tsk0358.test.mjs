import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { stripTypeScriptTypes } from 'node:module';

const root = resolve(import.meta.dirname, '../..');
const modulePath = resolve(root, 'src/lib/core-state-machine.ts');
const journeyPath = resolve(root, 'src/lib/journey-state.ts');
const dataUrl = (source) => `data:text/javascript;base64,${Buffer.from(source).toString('base64')}`;

async function loadApi() {
  assert.equal(existsSync(modulePath), true, 'missing TSK-0358 core state machine');
  let source = readFileSync(modulePath, 'utf8');
  if (source.includes("from './journey-state'")) {
    const journeySource = readFileSync(journeyPath, 'utf8');
    source = source.replace("from './journey-state'", `from '${dataUrl(stripTypeScriptTypes(journeySource, { mode: 'strip' }))}'`);
  }
  return import(dataUrl(stripTypeScriptTypes(source, { mode: 'strip' })));
}

const baseEvidence = { coverage: 'covered', configured: false, technical: null, action: null, uncertainty: null, removal: null };
const parentConfirmedEvidence = { ...baseEvidence, configured: true };

test('Protection Map precedence is deterministic and only fresh positive technical evidence yields protected/verified', async () => {
  const api = await loadApi();
  assert.equal(api.evaluateProtection({ ...baseEvidence, configured: true }).state, 'configured/parent-confirmed');
  assert.equal(api.evaluateProtection({ ...baseEvidence, configured: true }).reasonCode, 'CONFIG_CONFIRMED_NO_TECH_VERIFY');
  assert.equal(api.evaluateProtection({ ...baseEvidence, configured: true }).action, null);

  assert.equal(api.evaluateProtection({ ...baseEvidence, configured: true, technical: { result: 'positive', fresh: true } }).state, 'protected/verified');
  assert.equal(api.evaluateProtection({ ...baseEvidence, configured: true, technical: { result: 'positive', fresh: false } }).state, 'uncertain/error');
  assert.equal(api.evaluateProtection({ ...baseEvidence, configured: true, technical: { result: 'negative', fresh: true }, action: 'Reconfigure DNS, then verify again.' }).state, 'action-needed');
  assert.equal(api.evaluateProtection({ ...baseEvidence, coverage: 'not-covered' }).state, 'not-covered');
  assert.equal(api.evaluateProtection({ ...baseEvidence, uncertainty: 'VERIFY_UNREACHABLE' }).state, 'uncertain/error');
  assert.equal(api.evaluateProtection({ ...baseEvidence, configured: true, technical: { result: 'positive', fresh: true }, removal: 'REMOVED_BY_PARENT' }).state, 'removed');
});

test('account ownership, journey completion, and configuration never manufacture technical verification', async () => {
  const api = await loadApi();
  for (const context of [
    { ...baseEvidence, configured: true, accountOwned: true },
    { ...baseEvidence, configured: true, journeyComplete: true },
    { ...baseEvidence, accountOwned: true, journeyComplete: true },
  ]) {
    assert.notEqual(api.evaluateProtection(context).state, 'protected/verified');
  }
});

test('accountless core transitions cover setup, verification, Protection Map, troubleshooting, ordered recovery/removal and completion without login', async () => {
  const api = await loadApi();
  let state = api.createCoreState('en-GB', 'ab'.repeat(16), 1_000, 10_000);
  const events = [
    [{ type: 'SELECT_DEVICE', deviceFamily: 'android' }, 'native'],
    [{ type: 'CONTINUE_NATIVE' }, 'dns'],
    [{ type: 'CONTINUE_DNS' }, 'verify'],
    [{ type: 'VERIFICATION_RESULT', evidence: parentConfirmedEvidence }, 'protection'],
    [{ type: 'OPEN_TROUBLESHOOT' }, 'troubleshoot'],
    [{ type: 'OPEN_RECOVERY' }, 'recover'],
    [{ type: 'SERVICE_REVOCATION_RESULT', evidence: { ...baseEvidence, removal: 'REVOKED' } }, 'cleanup'],
    [{ type: 'REMOVE_CONFIGURATION' }, 'removed'],
    [{ type: 'RESTART_SETUP' }, 'route'],
    [{ type: 'SELECT_DEVICE', deviceFamily: 'android' }, 'native'],
    [{ type: 'CONTINUE_NATIVE' }, 'dns'],
    [{ type: 'CONTINUE_DNS' }, 'verify'],
    [{ type: 'VERIFICATION_RESULT', evidence: parentConfirmedEvidence }, 'protection'],
    [{ type: 'COMPLETE' }, 'complete'],
  ];
  for (const [event, phase] of events) {
    state = api.transitionCoreState(state, event, 2_000);
    assert.equal(state.phase, phase, `${event.type} -> ${phase}`);
    assert.equal(state.loginRequired, false);
  }
});

test('lost, malformed or expired core state recovers to safe accountless route and never extends the inherited hard expiry', async () => {
  const api = await loadApi();
  const base = api.createCoreState('tr-TR', 'cd'.repeat(16), 1_000, 5_000);
  const advanced = api.transitionCoreState(base, { type: 'SELECT_DEVICE', deviceFamily: 'iphone' }, 2_000);
  assert.equal(advanced.hardExpiresAt, 5_000);
  assert.equal(api.resumeCoreState(JSON.stringify(advanced), 4_999).phase, 'native');
  assert.equal(api.resumeCoreState(JSON.stringify(advanced), 5_000), null);
  assert.equal(api.resumeCoreState('{bad', 2_000), null);
  assert.equal(api.resumeCoreState(JSON.stringify({ ...advanced, email: 'x@example.invalid' }), 2_000), null);
});

test('optional-account state contract is dormant under the current owner fence and cannot block or strengthen core protection', async () => {
  const api = await loadApi();
  const disabled = api.optionalAccountTransition({ capabilityEnabled: false, status: 'unavailable' }, 'ENTER');
  assert.deepEqual(disabled, { capabilityEnabled: false, status: 'unavailable', route: null });
  for (const event of ['ENTER', 'RETURN', 'EXPIRE', 'LOGOUT', 'DASHBOARD']) {
    const result = api.optionalAccountTransition({ capabilityEnabled: false, status: 'unavailable' }, event);
    assert.equal(result.status, 'unavailable');
    assert.equal(result.route, null);
  }
  assert.equal(api.coreRequiresLogin({ capabilityEnabled: false, status: 'unavailable' }), false);
});

test('core state allowlist rejects identity, browsing/activity history, raw diagnostics and arbitrary URLs', async () => {
  const api = await loadApi();
  const state = api.createCoreState('ar', 'ef'.repeat(16), 1_000, 5_000);
  assert.deepEqual(Object.keys(state).sort(), ['createdAt','hardExpiresAt','locale','loginRequired','phase','retryCount','schemaVersion','scope'].sort());
  const forbidden = ['email','account','child','query','domain','history','activity','diagnostic','url','ip','verification'];
  for (const key of forbidden) assert.equal(Object.keys(state).some((candidate) => candidate.toLowerCase().includes(key)), false);
});
