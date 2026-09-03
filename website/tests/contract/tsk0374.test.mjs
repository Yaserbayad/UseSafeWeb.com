import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { stripTypeScriptTypes } from 'node:module';

const root = resolve(import.meta.dirname, '../..');
const read = (path) => readFileSync(resolve(root, path), 'utf8');
const json = (path) => JSON.parse(read(path));
const modulePath = 'src/lib/versioned-content.ts';
const releasePath = 'src/content/content-release.json';
const bindingPath = 'src/content/instruction-bindings.json';
const pagePaths = [
  'src/app/[locale]/setup/dns/page.tsx',
  'src/app/[locale]/verify/page.tsx',
  'src/app/[locale]/recover/page.tsx',
];

async function loadApi() {
  assert.equal(existsSync(resolve(root, modulePath)), true, 'missing versioned content delivery module');
  const source = read(modulePath);
  return import(
    `data:text/javascript;base64,${Buffer.from(stripTypeScriptTypes(source, { mode: 'strip' })).toString('base64')}`
  );
}

test('TSK-0374 artifacts exist and the full contract suite includes this task', () => {
  for (const path of [modulePath, releasePath, bindingPath, ...pagePaths]) {
    assert.equal(existsSync(resolve(root, path)), true, `missing ${path}`);
  }
  assert.match(json('package.json').scripts['test:contract'], /tsk0374\.test\.mjs/);
});

test('content release pins exact current TSK-0323 and instruction-binding provenance', () => {
  const release = json(releasePath);
  const bindings = json(bindingPath);
  assert.equal(release.schemaVersion, '1.0.0');
  assert.equal(release.activeReleaseId, 'instructions-2026-09-02');
  assert.equal(release.rollbackPolicy, 'pin-known-release');
  assert.deepEqual(Object.keys(release.releases), ['instructions-2026-09-02']);
  const active = release.releases[release.activeReleaseId];
  assert.deepEqual(active, {
    status: 'current',
    sourceCatalogueTask: 'TSK-0323',
    sourceCatalogueVersion: '1.0.1-post-cr0007',
    sourceCatalogueBlob: '79753cc4916d38ed8d2f0ed6d01890e62df3fb04',
    instructionBindingsBlob: '32441b56f5b2daf2c9924584685fd35fb416438e',
    instructionBindingsSchemaVersion: '1.0.0',
    sourceArtifact: 'TSK_0307_POST_CR0008_CURRENT_SOURCE_BACKED_INSTRUCTION_CATALOGUE_REVALIDATION_2026-09-02.md',
    sourceCommit: '330e9d13b9d479212ca6c49df3431f19f7107ba5',
    lastVerified: '2026-09-02',
  });
  assert.equal(bindings.schemaVersion, active.instructionBindingsSchemaVersion);
  assert.equal(bindings.sourceArtifact, active.sourceArtifact);
  assert.equal(bindings.sourceCommit, active.sourceCommit);
  assert.equal(bindings.lastVerified, active.lastVerified);
});

test('platform and purpose map only to approved instruction IDs', async () => {
  const api = await loadApi();
  assert.equal(api.resolveInstructionId('android', 'setup'), 'INS-AND-SETUP-01');
  assert.equal(api.resolveInstructionId('android', 'verify'), 'INS-AND-VERIFY-01');
  assert.equal(api.resolveInstructionId('android', 'remove'), 'INS-AND-REMOVE-01');
  assert.equal(api.resolveInstructionId('iphone', 'setup'), 'INS-IOS-SETUP-01');
  assert.equal(api.resolveInstructionId('iphone', 'verify'), 'INS-IOS-VERIFY-01');
  assert.equal(api.resolveInstructionId('iphone', 'remove'), 'INS-IOS-REMOVE-01');
  assert.equal(api.resolveInstructionId('common', 'uncertain'), 'INS-COMMON-UNCERTAIN-01');
  assert.equal(api.resolveInstructionId('common', 'not_covered'), 'INS-COMMON-NOTCOVERED-01');
  assert.equal(api.resolveInstructionId('common', 'recovery'), 'INS-COMMON-RECOVERY-01');
  assert.equal(api.resolveInstructionId('android', 'recovery'), null);
  assert.equal(api.resolveInstructionId('common', 'setup'), null);
});

test('release selection and delivery fail closed for stale, withdrawn, malformed, unknown, missing, or integrity-mismatched content', async () => {
  const api = await loadApi();
  const current = {
    status: 'current',
    sourceCatalogueTask: 'TSK-0323',
    sourceCatalogueVersion: '1.0.1-post-cr0007',
    sourceCatalogueBlob: 'catalogue',
    instructionBindingsBlob: 'bindings',
    instructionBindingsSchemaVersion: '1.0.0',
    sourceArtifact: 'artifact',
    sourceCommit: 'commit',
    lastVerified: '2026-09-02',
  };
  const releases = { current, previous: { ...current, sourceCommit: 'previous' } };
  assert.deepEqual(api.selectContentRelease(releases, 'current'), {
    status: 'ready',
    releaseId: 'current',
    release: current,
  });
  assert.deepEqual(api.selectContentRelease(releases, 'previous'), {
    status: 'ready',
    releaseId: 'previous',
    release: releases.previous,
  });
  assert.deepEqual(api.selectContentRelease(releases, 'missing'), { status: 'missing_release', releaseId: 'missing' });
  assert.equal(api.selectContentRelease({ stale: { ...current, status: 'stale' } }, 'stale').status, 'stale');
  assert.equal(api.selectContentRelease({ gone: { ...current, status: 'withdrawn' } }, 'gone').status, 'withdrawn');
  assert.equal(
    api.selectContentRelease({ bad: { ...current, status: 'unexpected' } }, 'bad').status,
    'invalid_release',
  );

  const metadata = {
    schemaVersion: '1.0.0',
    sourceArtifact: 'artifact',
    sourceCommit: 'commit',
    lastVerified: '2026-09-02',
  };
  assert.equal(api.validateBindingsMetadata(current, metadata), true);
  assert.equal(api.validateBindingsMetadata(current, { ...metadata, sourceCommit: 'tampered' }), false);
  assert.deepEqual(
    api.resolveContentDelivery({
      releases: { current },
      releaseId: 'current',
      platform: 'android',
      purpose: 'setup',
      availableInstructionIds: ['INS-AND-SETUP-01'],
      bindingsMetadata: metadata,
    }),
    { status: 'ready', releaseId: 'current', instructionId: 'INS-AND-SETUP-01', release: current },
  );
  assert.equal(
    api.resolveContentDelivery({
      releases: { current },
      releaseId: 'current',
      platform: 'android',
      purpose: 'setup',
      availableInstructionIds: [],
      bindingsMetadata: metadata,
    }).status,
    'missing_instruction',
  );
  assert.equal(
    api.resolveContentDelivery({
      releases: { current },
      releaseId: 'current',
      platform: 'android',
      purpose: 'setup',
      availableInstructionIds: ['INS-AND-SETUP-01'],
      bindingsMetadata: { ...metadata, sourceCommit: 'tampered' },
    }).status,
    'integrity_error',
  );
  assert.equal(
    api.resolveContentDelivery({
      releases: { current },
      releaseId: 'current',
      platform: 'common',
      purpose: 'setup',
      availableInstructionIds: ['INS-AND-SETUP-01'],
      bindingsMetadata: metadata,
    }).status,
    'unsupported',
  );
});

test('i18n delivery integration exposes release/status metadata and operational pages stop hard-coding instruction IDs', () => {
  const i18n = read('src/lib/i18n.ts');
  assert.match(i18n, /getVersionedInstruction/);
  assert.match(i18n, /resolveContentDelivery/);
  assert.match(i18n, /contentRelease/);
  for (const path of pagePaths) {
    const source = read(path);
    assert.match(source, /getVersionedInstruction/);
    assert.match(source, /data-content-release/);
    assert.match(source, /data-content-status/);
    assert.equal(/const instructionId\s*=/.test(source), false, `${path} still hard-codes instruction selection`);
  }
});

test('non-ready delivery is visibly fail-closed and retains a localized safe recovery route', () => {
  const setup = read(pagePaths[0]);
  assert.match(setup, /\{instruction\.status\}/, 'setup must visibly expose its non-ready content status');
  assert.match(setup, /href: `\/\$\{locale\}\/help`/, 'setup failure must retain Help');

  const verify = read(pagePaths[1]);
  assert.match(verify, /\{failed\.status\}/, 'verify must visibly expose its non-ready content status');
  assert.match(verify, /protectionContent\.troubleshootLabel/, 'verify failure must retain localized troubleshooting');
  assert.match(
    verify,
    /href: `\/\$\{locale\}\/troubleshoot\?platform=\$\{platform\}`/,
    'verify failure must route to troubleshooting',
  );

  const recover = read(pagePaths[2]);
  assert.match(recover, /getContent/, 'recovery failure needs localized shell actions');
  assert.match(recover, /\{instruction\.status\}/, 'recovery must visibly expose its non-ready content status');
  assert.match(recover, /href: `\/\$\{locale\}\/help`/, 'recovery failure must retain Help');
  assert.match(recover, /href: `\/\$\{locale\}\/setup\/route`/, 'recovery failure must retain a safe restart route');
});

test('versioned delivery has no remote content transport, persistence, identity, or analytics side channel', () => {
  const source = read(modulePath);
  for (const forbidden of [
    /fetch\s*\(/,
    /https?:\/\//i,
    /localStorage/,
    /sessionStorage/,
    /indexedDB/i,
    /document\.cookie/,
    /authorization/i,
    /accountId/i,
    /childId/i,
    /deviceId/i,
    /analytics/i,
    /telemetry/i,
    /product-events/i,
  ])
    assert.equal(forbidden.test(source), false, forbidden.toString());
});
