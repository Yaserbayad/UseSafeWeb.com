import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import test from 'node:test';
import { fileURLToPath } from 'node:url';

const repoRoot = fileURLToPath(new URL('../../..', import.meta.url));
const websiteRoot = join(repoRoot, 'website');

function readJson(path) {
  return JSON.parse(readFileSync(path, 'utf8'));
}

function readRepo(path) {
  return readFileSync(join(repoRoot, path), 'utf8');
}

const packageJson = readJson(join(websiteRoot, 'package.json'));
const packageLock = readJson(join(websiteRoot, 'package-lock.json'));

function directManifestEntries() {
  return [
    ...Object.entries(packageJson.dependencies ?? {}).map(([name, declared]) => ({ name, declared, scope: 'runtime' })),
    ...Object.entries(packageJson.devDependencies ?? {}).map(([name, declared]) => ({ name, declared, scope: 'development' })),
  ].sort((a, b) => a.name.localeCompare(b.name));
}

test('TSK-0491 inventories every direct npm dependency with its exact lock-resolved version', () => {
  const inventory = readJson(join(websiteRoot, 'config', 'dependency-inventory.json'));
  assert.equal(inventory.schema_version, 1);
  assert.equal(inventory.owner, 'Security');
  assert.equal(inventory.toolchain.node, '22.23.2');
  assert.equal(inventory.toolchain.npm, '10.9.8');
  assert.equal(inventory.generated_from.package_lock_blob, '6ff91d845bc5f3099b6a00f5f43673eed80a3ba5');

  const expected = directManifestEntries();
  const actual = [...inventory.npm.direct].sort((a, b) => a.name.localeCompare(b.name));
  assert.equal(actual.length, expected.length);

  for (let index = 0; index < expected.length; index += 1) {
    const wanted = expected[index];
    const recorded = actual[index];
    assert.deepEqual(
      { name: recorded.name, declared: recorded.declared, scope: recorded.scope },
      wanted,
      `inventory mismatch for ${wanted.name}`,
    );
    const locked = packageLock.packages[`node_modules/${wanted.name}`];
    assert.ok(locked, `lockfile entry missing for ${wanted.name}`);
    assert.equal(recorded.resolved, locked.version, `resolved version mismatch for ${wanted.name}`);
    assert.match(locked.integrity, /^sha(1|256|384|512)-/i, `integrity missing for ${wanted.name}`);
  }
});

test('TSK-0491 records pinned AdGuard supply-chain input, host package provider inputs, and current image absence', () => {
  const inventory = readJson(join(websiteRoot, 'config', 'dependency-inventory.json'));
  const installer = readRepo('infrastructure/adguard-server/install-adguard.sh');
  const recovery = readRepo('infrastructure/adguard-server/clean-recovery-drill-runtime.sh');

  const version = installer.match(/^ADGUARD_VERSION="([^"]+)"/m)?.[1];
  const sha256 = installer.match(/^EXPECTED_SHA256="([0-9a-f]{64})"/m)?.[1];
  assert.equal(version, 'v0.107.79');
  assert.equal(sha256, 'c48f4a43000665484c5ec28177de11a004759b620dae8f77b2aabefc9ef3687f');
  assert.deepEqual(inventory.external_artifacts, [
    {
      name: 'AdGuardHome',
      version,
      asset: 'AdGuardHome_linux_amd64.tar.gz',
      sha256,
      source: 'official-github-release',
    },
  ]);

  const aptLine = recovery.match(/sudo apt-get install -y -qq ([^\n]+) >\/dev\/null/)?.[1];
  assert.ok(aptLine, 'recovery host package install line missing');
  const expectedPackages = aptLine.trim().split(/\s+/).sort();
  assert.equal(inventory.host_package_inputs.base_os, 'ubuntu-24.04-lts');
  assert.equal(inventory.host_package_inputs.versioning, 'provider-managed-security-channel');
  assert.equal(inventory.host_package_inputs.project_locked, false);
  assert.deepEqual([...inventory.host_package_inputs.packages].sort(), expectedPackages);
  assert.match(inventory.host_package_inputs.disposition, /target-environment evidence/i);

  assert.deepEqual(inventory.container_images, []);
});

test('TSK-0491 documents update ownership, severity handling, immutable inputs, and secret-safe change rules', () => {
  const policy = readRepo('.github/DEPENDENCY_SECURITY_POLICY.md');
  assert.match(policy, /\*\*Owner:\*\*\s*Security/i);
  assert.match(policy, /critical|high/i);
  assert.match(policy, /block(?:s|ed)? promotion/i);
  assert.match(policy, /package-lock\.json/i);
  assert.match(policy, /SBOM/i);
  assert.match(policy, /npm audit fix --force/i);
  assert.match(policy, /must not/i);
  assert.match(policy, /digest/i);
  assert.match(policy, /container image/i);
  assert.match(policy, /Ubuntu 24\.04/i);
  assert.match(policy, /secret|token|private key/i);
  assert.match(policy, /review/i);
});

test('TSK-0491 CI generates and validates a CycloneDX SBOM on pull requests and main without deployment', () => {
  const workflow = readRepo('.github/workflows/accept-tsk0491-dependency-sbom-20260903.yml');
  assert.match(workflow, /pull_request:/);
  assert.match(workflow, /- main/);
  assert.match(workflow, /contents:\s*read/);
  assert.match(workflow, /npm ci --ignore-scripts/);
  assert.match(workflow, /npm sbom --sbom-format cyclonedx --sbom-type application --package-lock-only/);
  assert.match(workflow, /"bomFormat"/);
  assert.match(workflow, /CycloneDX/);
  assert.match(workflow, /npm audit --audit-level=high/);
  assert.doesNotMatch(workflow, /\bdeploy\b|wrangler|production activation/i);
});
