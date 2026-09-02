import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { stripTypeScriptTypes } from 'node:module';

const root = resolve(import.meta.dirname, '../..');
const modulePath = resolve(root, 'src/lib/core-state-machine.ts');

async function loadApi() {
  assert.equal(existsSync(modulePath), true, 'missing TSK-0358 core state machine');
  const source = readFileSync(modulePath, 'utf8');
  const js = stripTypeScriptTypes(source, { mode: 'strip' });
  return import(`data:text/javascript;base64,${Buffer.from(js).toString('base64')}`);
}

const baseEvidence = { coverage: 'covered', configured: false, technical: null, action: null, uncertainty: null, removal: null };

test('Protection Map precedence is deterministic and only fresh positive technical evidence yields protected/verified', async () => {
  const api = await loadApi();
  assert.equal(api.evaluateProtection({ ...baseEvidence, configured: true }).state, 'configured/parent-confirmed');
  assert.equal(api.evaluateProtection({ ...baseEvidence, configured: true }).reasonCode, 'CONFIG_CONFIRMED_NO_TECH_VERIFY');
  assert.equal(api.evaluateProtection({ ...baseEvidence, configured: true }).supporting, 'Protection has not yet been technically verified.');

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

test('accountless core transitions cover setup, verification, Protection Map, troubleshooting, recovery/removal and completion without login', async () => {
  const api = await loadApi();
  let state = api.createCoreState('en-GB', 'ab'.repeat(16), 1_000, 10_000);
  const events = [
    ['SELECT_DEVICE', 'native'],
    ['CONTINUE_NATIVE', 'dns'],
    ['CONTINUE_DNS', 'verify'],
    ['VERIFICATION_RESULT', 'protection'],
    ['OPEN_TROUBLESHOOT', 'troubleshoot'],
    ['OPEN_RECOVERY', 'recover'],
    ['REMOVE_CONFIGURATION', 'removed'],
    ['RESTART_SETUP', 'route'],
    ['SELECT_DEVICE', 'native'],
    ['CONTINUE_NATIVE', 'dns'],
    ['CONTINUE_DNS', 'verify'],
    ['VERIFICATION_RESULT', 'protection'],
    ['COMPLETE', 'complete'],
  ];
  for (const [type, phase] of events) {
    state = api.transitionCoreState(state, { type, deviceFamily: type === 'SELECT_DEVICE' ? 'android' : undefined }, 2_000);
    assert.equal(state.phase, phase, `${type} -> ${phase}`);
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
  assert.deepEqual(Object.keys(state).sort(), ['createdAt','hardExpiresAt','locale','loginRequired','phase','schemaVersion','scope'].sort());
  const forbidden = ['email','account','child','query','domain','history','activity','diagnostic','url','ip'];
  for (const key of forbidden) assert.equal(Object.keys(state).some((candidate) => candidate.toLowerCase().includes(key)), false);
});
