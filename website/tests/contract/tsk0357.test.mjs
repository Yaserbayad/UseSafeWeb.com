import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { stripTypeScriptTypes } from 'node:module';

const root = resolve(import.meta.dirname, '../..');
const modulePath = resolve(root, 'src/lib/journey-state.ts');
const boundaryPath = resolve(root, 'src/components/journey-state-boundary.tsx');
const resumePath = resolve(root, 'src/components/journey-resume-panel.tsx');
const storageKey = 'usesafeweb:j0:v1';
const DAY_MS = 24 * 60 * 60 * 1000;

function loadApi() {
  assert.equal(existsSync(modulePath), true, 'missing privacy-minimal J0 state module');
  const source = readFileSync(modulePath, 'utf8');
  const javascript = stripTypeScriptTypes(source, { mode: 'strip' });
  const url = `data:text/javascript;base64,${Buffer.from(javascript).toString('base64')}`;
  return import(url);
}

function fakeStorage(initial = {}) {
  const data = new Map(Object.entries(initial));
  return {
    getItem(key) {
      return data.has(key) ? data.get(key) : null;
    },
    setItem(key, value) {
      data.set(key, String(value));
    },
    removeItem(key) {
      data.delete(key);
    },
    dump() {
      return Object.fromEntries(data);
    },
  };
}

function deterministicRandom(bytes) {
  bytes.fill(0xab);
  return bytes;
}

const expectedBaseKeys = ['createdAt', 'hardExpiresAt', 'journeyStep', 'locale', 'schemaVersion', 'scope'];

test('TSK-0357 production state and client-boundary files exist without a server-state route', () => {
  assert.equal(existsSync(modulePath), true, 'missing journey-state.ts');
  assert.equal(existsSync(boundaryPath), true, 'missing journey-state-boundary.tsx');
  assert.equal(existsSync(resumePath), true, 'missing journey-resume-panel.tsx');
  for (const path of ['src/app/api/journey/route.ts', 'src/app/api/journey/[token]/route.ts']) {
    assert.equal(existsSync(resolve(root, path)), false, `unexpected server-side J1 persistence route: ${path}`);
  }
});

test('J0 creation is anonymous, scoped with 128 random bits, and hard-expires non-sliding within 24 hours', async () => {
  const api = await loadApi();
  const state = api.createJourneyState('en-GB', 1_000, deterministicRandom);
  assert.deepEqual(Object.keys(state).sort(), expectedBaseKeys);
  assert.equal(state.schemaVersion, 1);
  assert.equal(state.scope, 'ab'.repeat(16));
  assert.match(state.scope, /^[0-9a-f]{32}$/);
  assert.equal(state.createdAt, 1_000);
  assert.equal(state.hardExpiresAt, 1_000 + DAY_MS);
  assert.equal(state.locale, 'en-GB');
  assert.equal(state.journeyStep, 'route');
});

test('controlled route updates preserve scope and original hard expiry while storing only approved current setup state', async () => {
  const api = await loadApi();
  const storage = fakeStorage();
  const first = api.recordJourneyLocation(
    storage,
    { pathname: '/en-GB/setup/route', platform: null },
    10_000,
    deterministicRandom,
  );
  assert.ok(first);
  const expiry = first.hardExpiresAt;
  const scope = first.scope;

  const native = api.recordJourneyLocation(
    storage,
    { pathname: '/en-GB/setup/native', platform: 'android' },
    20_000,
    deterministicRandom,
  );
  assert.ok(native);
  assert.equal(native.scope, scope);
  assert.equal(native.hardExpiresAt, expiry, 'ordinary activity must not slide hard expiry');
  assert.deepEqual(Object.keys(native).sort(), [...expectedBaseKeys, 'deviceFamily'].sort());
  assert.equal(native.deviceFamily, 'android');
  assert.equal(native.journeyStep, 'native');

  const dns = api.recordJourneyLocation(
    storage,
    { pathname: '/en-GB/setup/dns', platform: 'android' },
    30_000,
    deterministicRandom,
  );
  assert.ok(dns);
  assert.equal(dns.scope, scope);
  assert.equal(dns.hardExpiresAt, expiry);
  assert.deepEqual(Object.keys(dns).sort(), [...expectedBaseKeys, 'deviceFamily', 'dnsMethod'].sort());
  assert.equal(dns.deviceFamily, 'android');
  assert.equal(dns.dnsMethod, 'android_private_dns_dot');
  assert.equal(dns.journeyStep, 'dns');

  const persisted = JSON.parse(storage.dump()[storageKey]);
  for (const forbidden of [
    'email',
    'phone',
    'parent',
    'child',
    'account',
    'ip',
    'query',
    'domain',
    'history',
    'url',
    'diagnostic',
    'freeText',
  ]) {
    assert.equal(
      Object.keys(persisted).some((key) => key.toLowerCase().includes(forbidden.toLowerCase())),
      false,
      `forbidden persisted field ${forbidden}`,
    );
  }
});

test('invalid, unknown-field, inconsistent, and expired state is deleted rather than resumed', async () => {
  const api = await loadApi();
  const valid = api.createJourneyState('en-GB', 100, deterministicRandom);
  const cases = [
    '{not json',
    JSON.stringify({ ...valid, email: 'parent@example.invalid' }),
    JSON.stringify({ ...valid, journeyStep: 'dns' }),
    JSON.stringify({ ...valid, hardExpiresAt: valid.createdAt + DAY_MS + 1 }),
    JSON.stringify({ ...valid, hardExpiresAt: 99 }),
  ];
  for (const raw of cases) {
    const storage = fakeStorage({ [storageKey]: raw });
    assert.equal(api.readJourneyState(storage, 100), null);
    assert.equal(storage.getItem(storageKey), null, 'invalid state must be deleted');
  }
  const expired = fakeStorage({ [storageKey]: JSON.stringify(valid) });
  assert.equal(api.readJourneyState(expired, valid.hardExpiresAt), null);
  assert.equal(expired.getItem(storageKey), null, 'expired state must be deleted at the hard boundary');
});

test('reset deletion is immediate and storage failure degrades to URL-only accountless flow', async () => {
  const api = await loadApi();
  const storage = fakeStorage();
  api.recordJourneyLocation(storage, { pathname: '/tr-TR/setup/route', platform: null }, 1_000, deterministicRandom);
  assert.ok(storage.getItem(storageKey));
  api.clearJourneyState(storage);
  assert.equal(storage.getItem(storageKey), null);

  const blocked = {
    getItem() {
      throw new Error('storage blocked');
    },
    setItem() {
      throw new Error('storage blocked');
    },
    removeItem() {
      throw new Error('storage blocked');
    },
  };
  assert.equal(api.readJourneyState(blocked, 1_000), null);
  assert.equal(
    api.recordJourneyLocation(blocked, { pathname: '/en-GB/setup/route', platform: null }, 1_000, deterministicRandom),
    null,
  );
  assert.doesNotThrow(() => api.clearJourneyState(blocked));
});

test('resume href is derived only from validated controlled state and cannot become an arbitrary URL', async () => {
  const api = await loadApi();
  const storage = fakeStorage();
  api.recordJourneyLocation(storage, { pathname: '/ar/setup/route', platform: null }, 1_000, deterministicRandom);
  api.recordJourneyLocation(storage, { pathname: '/ar/setup/native', platform: 'iphone' }, 2_000, deterministicRandom);
  const state = api.recordJourneyLocation(
    storage,
    { pathname: '/ar/setup/dns', platform: 'iphone' },
    3_000,
    deterministicRandom,
  );
  assert.ok(state);
  assert.equal(api.resumeHref(state), '/ar/setup/dns?platform=iphone');
  assert.equal(api.resumeHref(state, 'en-GB'), '/en-GB/setup/dns?platform=iphone');
  assert.equal(
    api.recordJourneyLocation(
      storage,
      { pathname: 'https://evil.invalid/', platform: 'iphone' },
      4_000,
      deterministicRandom,
    ),
    null,
  );
});

test('client integration uses sessionStorage only and wraps query-reading tracker in Suspense', () => {
  assert.equal(existsSync(boundaryPath), true);
  assert.equal(existsSync(resumePath), true);
  const boundary = readFileSync(boundaryPath, 'utf8');
  const resume = readFileSync(resumePath, 'utf8');
  const layout = readFileSync(resolve(root, 'src/app/[locale]/layout.tsx'), 'utf8');
  const start = readFileSync(resolve(root, 'src/app/[locale]/start/page.tsx'), 'utf8');
  assert.match(boundary, /^['"]use client['"]/);
  assert.match(boundary, /usePathname/);
  assert.match(boundary, /useSearchParams/);
  assert.match(boundary, /sessionStorage/);
  assert.doesNotMatch(boundary + resume, /localStorage|indexedDB/);
  assert.match(layout, /<Suspense[^>]*fallback=\{null\}/);
  assert.match(layout, /JourneyStateBoundary/);
  assert.match(start, /JourneyResumePanel/);
  for (const locale of ['en-GB', 'tr-TR', 'ar']) {
    const content = JSON.parse(readFileSync(resolve(root, `src/content/${locale}.json`), 'utf8'));
    assert.equal(typeof content.start.resumeLabel, 'string');
    assert.equal(typeof content.start.resetLabel, 'string');
    assert.equal(typeof content.start.resumeNote, 'string');
  }
});
