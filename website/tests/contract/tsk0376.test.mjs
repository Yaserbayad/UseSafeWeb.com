import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { stripTypeScriptTypes } from 'node:module';

const root = resolve(import.meta.dirname, '../..');
const corePath = resolve(root, 'src/lib/core-state-machine.ts');
const journeyPath = resolve(root, 'src/lib/journey-state.ts');
const sessionPath = resolve(root, 'src/lib/core-session.ts');
const panelPath = resolve(root, 'src/components/dns-verification-panel.tsx');

const dataUrl = (source) => `data:text/javascript;base64,${Buffer.from(source).toString('base64')}`;

async function loadJourneyApi() {
  const source = readFileSync(journeyPath, 'utf8');
  return import(dataUrl(stripTypeScriptTypes(source, { mode: 'strip' })));
}

async function loadCoreApi() {
  let source = readFileSync(corePath, 'utf8');
  if (source.includes("from './journey-state'")) {
    const journeySource = readFileSync(journeyPath, 'utf8');
    const journeyUrl = dataUrl(stripTypeScriptTypes(journeySource, { mode: 'strip' }));
    source = source.replace("from './journey-state'", `from '${journeyUrl}'`);
  }
  return import(dataUrl(stripTypeScriptTypes(source, { mode: 'strip' })));
}

const scope = 'ab'.repeat(16);
const createdAt = 1_000;
const withinLifetime = createdAt + 1_000;
const parentConfirmed = {
  coverage: 'covered',
  configured: true,
  technical: null,
  action: null,
  uncertainty: null,
  removal: null,
};
const verified = {
  ...parentConfirmed,
  technical: { result: 'positive', fresh: true },
};
const failed = {
  ...parentConfirmed,
  technical: { result: 'negative', fresh: true },
};

async function toVerification(api, hardExpiresAt = createdAt + 60_000) {
  let state = api.createCoreState('en-GB', scope, createdAt, hardExpiresAt);
  state = api.transitionCoreState(state, { type: 'SELECT_DEVICE', deviceFamily: 'android' }, withinLifetime);
  state = api.transitionCoreState(state, { type: 'CONTINUE_NATIVE' }, withinLifetime);
  state = api.transitionCoreState(state, { type: 'CONTINUE_DNS' }, withinLifetime);
  return state;
}

test('canonical happy path exposes Phone -> Internet -> Services without a parallel persisted stage or verification model', async () => {
  const api = await loadCoreApi();
  let state = api.createCoreState('en-GB', scope, createdAt, createdAt + 60_000);
  assert.equal(api.coreJourneyStage(state), 'phone');
  state = api.transitionCoreState(state, { type: 'SELECT_DEVICE', deviceFamily: 'android' }, withinLifetime);
  assert.equal(api.coreJourneyStage(state), 'phone');
  state = api.transitionCoreState(state, { type: 'CONTINUE_NATIVE' }, withinLifetime);
  assert.equal(api.coreJourneyStage(state), 'internet');
  state = api.transitionCoreState(state, { type: 'CONTINUE_DNS' }, withinLifetime);
  assert.equal(api.coreJourneyStage(state), 'internet');
  state = api.transitionCoreState(state, { type: 'VERIFICATION_RESULT', evidence: verified }, withinLifetime);
  assert.equal(api.coreJourneyStage(state), 'services');
  assert.equal(state.phase, 'protection');
  assert.equal(state.retryCount, 0);
  assert.equal(Object.hasOwn(state, 'verification'), false, 'verification evaluation must not be duplicated into retained session state');
});

test('illegal transitions are rejected rather than silently advancing or no-oping', async () => {
  const api = await loadCoreApi();
  const state = api.createCoreState('en-GB', scope, createdAt, createdAt + 60_000);
  assert.throws(() => api.transitionCoreState(state, { type: 'CONTINUE_DNS' }, withinLifetime), /invalid core transition/);
  const verification = await toVerification(api);
  assert.throws(() => api.transitionCoreState(verification, { type: 'SELECT_DEVICE', deviceFamily: 'iphone' }, withinLifetime), /invalid core transition/);
});

test('parent confirmation and measured verification remain distinct and an evidence-free UX event cannot manufacture verified/protected state', async () => {
  const api = await loadCoreApi();
  const verification = await toVerification(api);
  assert.throws(
    () => api.transitionCoreState(verification, { type: 'VERIFICATION_RESULT' }, withinLifetime),
    /verification evidence required/,
  );

  const confirmedEvaluation = api.evaluateProtection(parentConfirmed);
  const measuredEvaluation = api.evaluateProtection(verified);
  assert.equal(confirmedEvaluation.state, 'configured/parent-confirmed');
  assert.equal(confirmedEvaluation.reasonCode, 'CONFIG_CONFIRMED_NO_TECH_VERIFY');
  assert.equal(measuredEvaluation.state, 'protected/verified');
  assert.equal(measuredEvaluation.reasonCode, 'TECH_VERIFIED');

  const confirmed = api.transitionCoreState(
    verification,
    { type: 'VERIFICATION_RESULT', evidence: parentConfirmed },
    withinLifetime,
  );
  const measured = api.transitionCoreState(
    verification,
    { type: 'VERIFICATION_RESULT', evidence: verified },
    withinLifetime,
  );
  assert.equal(confirmed.phase, 'protection');
  assert.equal(measured.phase, 'protection');
  assert.equal(Object.hasOwn(confirmed, 'verification'), false);
  assert.equal(Object.hasOwn(measured, 'verification'), false);
});

test('negative/uncertain verification cannot enter Services and recovery retry is bounded and deterministic', async () => {
  const api = await loadCoreApi();
  assert.ok(Number.isSafeInteger(api.CORE_MAX_VERIFICATION_RETRIES));
  assert.ok(api.CORE_MAX_VERIFICATION_RETRIES > 0 && api.CORE_MAX_VERIFICATION_RETRIES <= 5);

  let state = api.transitionCoreState(
    await toVerification(api),
    { type: 'VERIFICATION_RESULT', evidence: failed },
    withinLifetime,
  );
  assert.equal(state.phase, 'troubleshoot');
  assert.equal(api.coreJourneyStage(state), 'internet');
  assert.equal(api.evaluateProtection(failed).state, 'action-needed');

  for (let attempt = 1; attempt <= api.CORE_MAX_VERIFICATION_RETRIES; attempt += 1) {
    const beforeRetry = state;
    const first = api.transitionCoreState(beforeRetry, { type: 'RETRY_VERIFICATION' }, withinLifetime);
    const replay = api.transitionCoreState(beforeRetry, { type: 'RETRY_VERIFICATION' }, withinLifetime);
    assert.deepEqual(replay, first, 'same retry input must be deterministic/idempotent');
    assert.equal(first.retryCount, attempt);
    assert.equal(first.phase, 'verify');
    assert.equal(Object.hasOwn(first, 'verification'), false, 'retry must not retain or manufacture verification state');
    if (attempt === api.CORE_MAX_VERIFICATION_RETRIES) {
      const failedAgain = api.transitionCoreState(first, { type: 'VERIFICATION_RESULT', evidence: failed }, withinLifetime);
      assert.throws(() => api.transitionCoreState(failedAgain, { type: 'RETRY_VERIFICATION' }, withinLifetime), /retry limit reached/);
      break;
    }
    state = api.transitionCoreState(first, { type: 'VERIFICATION_RESULT', evidence: failed }, withinLifetime);
  }
});

test('Journey-0 state is accountless, session-scoped, capped at 24h, and malformed/expired state restarts safely', async () => {
  const journey = await loadJourneyApi();
  const api = await loadCoreApi();
  assert.equal(journey.JOURNEY_MAX_AGE_MS, 24 * 60 * 60 * 1000);

  const randomFill = (bytes) => { bytes.fill(7); return bytes; };
  const state = journey.createJourneyState('en-GB', createdAt, randomFill);
  assert.equal(state.hardExpiresAt - state.createdAt, journey.JOURNEY_MAX_AGE_MS);
  assert.equal(journey.parseJourneyState(JSON.stringify(state), state.hardExpiresAt), null);
  assert.equal(journey.parseJourneyState('{malformed', createdAt), null);

  assert.throws(
    () => api.createCoreState('en-GB', scope, createdAt, createdAt + journey.JOURNEY_MAX_AGE_MS + 1),
    /core lifetime exceeds Journey-0 limit/,
  );
  const core = api.createCoreState('en-GB', scope, createdAt, createdAt + journey.JOURNEY_MAX_AGE_MS);
  assert.deepEqual(api.resumeCoreState(JSON.stringify(core), withinLifetime), core);
  assert.deepEqual(api.resumeCoreState(JSON.stringify(core), withinLifetime), core, 'resume must be deterministic/idempotent');
  assert.equal(api.resumeCoreState(JSON.stringify(core), core.hardExpiresAt), null);
  assert.equal(api.resumeCoreState('{malformed', withinLifetime), null);

  const serialized = JSON.stringify(core).toLowerCase();
  for (const forbidden of ['account', 'household', 'child', 'browsing', 'history', 'dnsquery', 'hostname', 'domain', 'verification']) {
    assert.equal(serialized.includes(forbidden), false, `retained core state contains prohibited/duplicated field ${forbidden}`);
  }
});

test('runtime adapters remain transient/session-only and bind trusted classifier evidence into the verification transition', () => {
  const coreSource = readFileSync(corePath, 'utf8');
  const journeySource = readFileSync(journeyPath, 'utf8');
  const sessionSource = readFileSync(sessionPath, 'utf8');
  const panelSource = readFileSync(panelPath, 'utf8');

  assert.match(coreSource, /JOURNEY_MAX_AGE_MS/);
  assert.match(sessionSource, /sessionStorage|StorageLike/);
  assert.doesNotMatch(`${coreSource}\n${journeySource}\n${sessionSource}`, /localStorage|indexedDB/);
  assert.doesNotMatch(`${coreSource}\n${journeySource}\n${sessionSource}`, /accountId|householdId|childId|queryHistory|browsingHistory|rawDns|hostnameHistory|domainHistory/i);
  assert.match(panelSource, /VERIFICATION_RESULT[\s\S]{0,180}evidence:\s*outcome\.evidence/);
  assert.doesNotMatch(panelSource, /event=\{\{\s*type:\s*['"]VERIFICATION_RESULT['"]\s*\}\}/);
});
