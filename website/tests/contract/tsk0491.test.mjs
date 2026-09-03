import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';

const root = resolve(import.meta.dirname, '../..');
const repoRoot = resolve(root, '..');
const packagePath = resolve(root, 'package.json');
const lockPath = resolve(root, 'package-lock.json');
const policyPath = resolve(root, 'DEPENDENCY_SECURITY_POLICY.md');
const workflowPath = resolve(repoRoot, '.github/workflows/accept-tsk0491-dependency-sbom-20260903.yml');

const pkg = JSON.parse(readFileSync(packagePath, 'utf8'));
const lock = JSON.parse(readFileSync(lockPath, 'utf8'));

function policyText() {
  assert.equal(existsSync(policyPath), true, 'missing dependency inventory/update policy');
  return readFileSync(policyPath, 'utf8');
}

test('TSK-0491 keeps the npm dependency tree locked and inventories every direct dependency', () => {
  assert.equal(lock.lockfileVersion, 3);
  assert.deepEqual(lock.packages?.['']?.dependencies, pkg.dependencies);
  assert.deepEqual(lock.packages?.['']?.devDependencies, pkg.devDependencies);

  const policy = policyText();
  for (const [name, requested] of Object.entries({ ...pkg.dependencies, ...pkg.devDependencies })) {
    assert.equal(policy.includes(`| ${name} | ${requested} |`), true, `missing ${name} ${requested} inventory row`);
  }
  assert.match(policy, /container images[^\n]*none/i);
});

test('TSK-0491 documents Security ownership and deterministic update/severity disposition', () => {
  const policy = policyText();
  assert.match(policy, /Owner:\*\*\s*Security/i);
  assert.match(policy, /critical/i);
  assert.match(policy, /high/i);
  assert.match(policy, /moderate/i);
  assert.match(policy, /low/i);
  assert.match(policy, /lockfile/i);
  assert.match(policy, /npm audit/i);
  assert.match(policy, /review/i);
  assert.match(policy, /exception/i);
});

test('TSK-0491 exposes a lockfile-derived SPDX application SBOM command through the aggregate contract suite', () => {
  assert.equal(pkg.scripts?.sbom, 'npm sbom --package-lock-only --sbom-format=spdx --sbom-type=application');
  assert.match(pkg.scripts?.['test:contract'] ?? '', /tsk0491\.test\.mjs/);
});

test('TSK-0491 generates and validates the SBOM in CI without a live target dependency', () => {
  assert.equal(existsSync(workflowPath), true, 'missing TSK-0491 acceptance workflow');
  const workflow = readFileSync(workflowPath, 'utf8');
  assert.match(workflow, /npm run sbom > .*sbom\.spdx\.json/);
  assert.match(workflow, /SPDX-2\.3/);
  assert.match(workflow, /npm audit --audit-level=high/);
  assert.doesNotMatch(workflow, /deploy|production|wrangler|ssh|kubectl/i);
});
