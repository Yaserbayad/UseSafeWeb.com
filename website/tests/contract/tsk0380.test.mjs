import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';

const root = resolve(import.meta.dirname, '../..');
const packagePath = resolve(root, 'package.json');
const lockPath = resolve(root, 'package-lock.json');
const nodeVersionPath = resolve(root, '.nvmrc');
const readmePath = resolve(root, 'README.md');

const pkg = JSON.parse(readFileSync(packagePath, 'utf8'));
const lock = JSON.parse(readFileSync(lockPath, 'utf8'));
const readme = readFileSync(readmePath, 'utf8');

test('TSK-0380 pins the local Node/npm toolchain and keeps the lockfile authoritative', () => {
  assert.equal(existsSync(nodeVersionPath), true, 'missing .nvmrc exact Node pin');
  assert.equal(readFileSync(nodeVersionPath, 'utf8').trim(), '22.23.2');
  assert.equal(pkg.packageManager, 'npm@10.9.8');
  assert.equal(pkg.engines?.node, '22.23.2');
  assert.equal(lock.lockfileVersion, 3);
});

test('TSK-0380 exposes one deterministic validation command that fails closed through ordered quality gates', () => {
  assert.equal(
    pkg.scripts?.validate,
    'npm run test:contract && npm run lint && npm run typecheck && npm run build',
  );
  assert.match(pkg.scripts?.['test:contract'] ?? '', /tsk0380\.test\.mjs/);
});

test('TSK-0380 documents clean setup and baseline validation without an undocumented manual step', () => {
  assert.match(readme, /Node\.js\s+22\.23\.2/);
  assert.match(readme, /npm\s+10\.9\.8/);
  assert.match(readme, /npm ci/);
  assert.match(readme, /npm run validate/);
  assert.match(readme, /\.nvmrc/);
});
