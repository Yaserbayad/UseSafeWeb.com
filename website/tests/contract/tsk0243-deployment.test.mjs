import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { copyFileSync, existsSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { stripTypeScriptTypes } from 'node:module';

const website = resolve(import.meta.dirname, '../..');
const repository = resolve(website, '..');
const runtimeConfigPath = resolve(website, 'src/lib/runtime-config.ts');
const healthRoutePath = resolve(website, 'src/app/api/health/ready/route.ts');
const servicePath = resolve(repository, 'infrastructure/web-server/usesafeweb-web.service');
const envExamplePath = resolve(repository, 'infrastructure/web-server/website.env.example');
const validatorPath = resolve(repository, 'infrastructure/web-server/validate-runtime.mjs');
const deployPath = resolve(repository, 'infrastructure/web-server/deploy-release.sh');
const nodeInstallerPath = resolve(repository, 'infrastructure/web-server/install-node-runtime.sh');

async function loadRuntimeConfig() {
  assert.equal(existsSync(runtimeConfigPath), true, 'missing server runtime configuration module');
  const source = readFileSync(runtimeConfigPath, 'utf8');
  const js = stripTypeScriptTypes(source, { mode: 'strip' });
  return import(`data:text/javascript;base64,${Buffer.from(js).toString('base64')}`);
}

test('server runtime configuration fails closed and never returns the signing secret in public status', async () => {
  const api = await loadRuntimeConfig();
  const good = {
    NODE_ENV: 'production',
    USESAFEWEB_PUBLIC_ORIGIN: 'https://usesafeweb.example',
    USESAFEWEB_DNS_VERIFICATION_SIGNING_SECRET: 's'.repeat(32),
    USESAFEWEB_RELEASE_SHA: 'a'.repeat(40),
  };

  assert.deepEqual(api.readServerRuntimeConfig(good), {
    publicOrigin: 'https://usesafeweb.example',
    releaseSha: 'a'.repeat(40),
    signingSecret: 's'.repeat(32),
  });
  assert.deepEqual(api.publicRuntimeStatus(good), {
    ready: true,
    releaseSha: 'a'.repeat(40),
    verifierVersion: 'private-rewrite-v1',
  });
  assert.equal(JSON.stringify(api.publicRuntimeStatus(good)).includes('s'.repeat(32)), false);

  for (const invalid of [
    { ...good, NODE_ENV: 'development' },
    { ...good, USESAFEWEB_DNS_VERIFICATION_SIGNING_SECRET: undefined },
    { ...good, USESAFEWEB_DNS_VERIFICATION_SIGNING_SECRET: 'short' },
    { ...good, USESAFEWEB_PUBLIC_ORIGIN: 'http://usesafeweb.example' },
    { ...good, USESAFEWEB_PUBLIC_ORIGIN: 'https://usesafeweb.example/path' },
    { ...good, USESAFEWEB_RELEASE_SHA: 'latest' },
  ]) {
    assert.throws(() => api.readServerRuntimeConfig(invalid), /runtime configuration/i);
    assert.deepEqual(api.publicRuntimeStatus(invalid), {
      ready: false,
      releaseSha: null,
      verifierVersion: 'private-rewrite-v1',
    });
  }
});

test('readiness route is no-store and derives readiness from server-only validated configuration', () => {
  assert.equal(existsSync(healthRoutePath), true, 'missing readiness route');
  const source = readFileSync(healthRoutePath, 'utf8');
  assert.match(source, /export const runtime = ['"]nodejs['"]/);
  assert.match(source, /export const dynamic = ['"]force-dynamic['"]/);
  assert.match(source, /publicRuntimeStatus/);
  assert.match(source, /status\.ready \? 200 : 503/);
  assert.match(source, /Cache-Control['"]?\s*[:,]\s*['"]no-store['"]/);
  assert.doesNotMatch(source, /signingSecret|DNS_VERIFICATION_SIGNING_SECRET/);
});

test('runtime validator binds the environment release SHA to an installed artifact marker', () => {
  const directory = mkdtempSync(join(tmpdir(), 'usesafeweb-release-marker-'));
  try {
    const validator = join(directory, 'validate-runtime.mjs');
    const marker = join(directory, '.release-sha');
    copyFileSync(validatorPath, validator);
    const releaseSha = 'a'.repeat(40);
    const env = {
      ...process.env,
      NODE_ENV: 'production',
      HOSTNAME: '127.0.0.1',
      PORT: '3100',
      NEXT_TELEMETRY_DISABLED: '1',
      USESAFEWEB_PUBLIC_ORIGIN: 'https://usesafeweb.example',
      USESAFEWEB_DNS_VERIFICATION_SIGNING_SECRET: 's'.repeat(32),
      USESAFEWEB_RELEASE_SHA: releaseSha,
    };

    const missing = spawnSync(process.execPath, [validator], { env, encoding: 'utf8' });
    assert.notEqual(missing.status, 0, 'missing release marker must fail closed');
    assert.match(`${missing.stdout}${missing.stderr}`, /release_marker/);

    writeFileSync(marker, `${'b'.repeat(40)}\n`, 'utf8');
    const mismatched = spawnSync(process.execPath, [validator], { env, encoding: 'utf8' });
    assert.notEqual(mismatched.status, 0, 'mismatched release marker must fail closed');
    assert.match(`${mismatched.stdout}${mismatched.stderr}`, /release_marker/);

    writeFileSync(marker, `${releaseSha}\n`, 'utf8');
    const valid = spawnSync(process.execPath, [validator], { env, encoding: 'utf8' });
    assert.equal(valid.status, 0, valid.stderr);
    assert.match(valid.stdout, /USESAFEWEB_RUNTIME_VALIDATION=PASS/);
  } finally {
    rmSync(directory, { recursive: true, force: true });
  }
});

test('Next.js production output and direct-host service are deterministic and fail visibly', () => {
  const nextConfig = readFileSync(resolve(website, 'next.config.ts'), 'utf8');
  assert.match(nextConfig, /output:\s*['"]standalone['"]/);

  for (const path of [servicePath, envExamplePath, validatorPath, deployPath]) {
    assert.equal(existsSync(path), true, `missing deployment artifact: ${path}`);
  }

  const service = readFileSync(servicePath, 'utf8');
  assert.match(service, /EnvironmentFile=\/etc\/usesafeweb\/website\.env/);
  assert.match(service, /ExecStartPre=.*validate-runtime\.mjs/);
  assert.match(service, /ExecStart=.*server\.js/);
  assert.match(service, /Restart=on-failure/);
  assert.match(service, /RestartSec=5s/);
  assert.match(service, /NoNewPrivileges=true/);
  assert.match(service, /ProtectSystem=strict/);
  assert.match(service, /ReadWritePaths=\/var\/lib\/usesafeweb-web/);

  const envExample = readFileSync(envExamplePath, 'utf8');
  assert.match(envExample, /^HOSTNAME=127\.0\.0\.1$/m);
  assert.match(envExample, /^PORT=3100$/m);
  assert.match(envExample, /^USESAFEWEB_PUBLIC_ORIGIN=$/m);
  assert.match(envExample, /^USESAFEWEB_DNS_VERIFICATION_SIGNING_SECRET=$/m);
  assert.match(envExample, /^USESAFEWEB_RELEASE_SHA=$/m);
  assert.doesNotMatch(envExample, /BEGIN .*PRIVATE KEY|[A-Za-z0-9_-]{48,}/);

  const validator = readFileSync(validatorPath, 'utf8');
  assert.match(validator, /22\.23\.2/);
  assert.match(validator, /\.release-sha/);
  assert.match(validator, /release_marker/);
  assert.doesNotMatch(validator, /console\.(?:log|error).*SIGNING_SECRET/i);

  const deploy = readFileSync(deployPath, 'utf8');
  assert.match(deploy, /10\.9\.8/);
  assert.match(deploy, /npm ci --ignore-scripts --no-fund --no-audit/);
  assert.match(deploy, /npm run validate/);
  assert.match(deploy, /environment_release_binding/);
  assert.match(deploy, /\.next\/standalone/);
  assert.match(deploy, /\.release-sha/);
  assert.match(deploy, /release_path_exists/);
  assert.match(deploy, /SERVICE=["']usesafeweb-web\.service["']/);
  assert.match(deploy, /systemctl restart ["']\$\{SERVICE\}["']/);
  assert.match(deploy, /api\/health\/ready/);
  assert.match(deploy, /rollback/i);
});

test('direct-host deployment uses an isolated pinned Node runtime without changing the host global Node', () => {
  assert.equal(existsSync(nodeInstallerPath), true, 'missing isolated Node runtime installer');

  const installer = readFileSync(nodeInstallerPath, 'utf8');
  assert.match(installer, /v22\.23\.2/);
  assert.match(installer, /d60acfe00a2932254bb0ad20e01b0d74397a0875595de719654b214f4b03f307/);
  assert.match(installer, /node-v22\.23\.2-linux-x64\.tar\.xz/);
  assert.match(installer, /sha256sum/);
  assert.match(installer, /\/opt\/usesafeweb-runtime\/node-v22\.23\.2/);
  assert.doesNotMatch(installer, /(?:ln|cp|mv).*\/usr\/bin\/node/);

  const service = readFileSync(servicePath, 'utf8');
  assert.match(service, /ExecStartPre=\/opt\/usesafeweb-runtime\/node-v22\.23\.2\/bin\/node .*validate-runtime\.mjs/);
  assert.match(service, /ExecStart=\/opt\/usesafeweb-runtime\/node-v22\.23\.2\/bin\/node .*server\.js/);
  assert.doesNotMatch(service, /ExecStart(?:Pre)?=\/usr\/bin\/node/);

  const deploy = readFileSync(deployPath, 'utf8');
  assert.match(deploy, /NODE_BIN=["']\/opt\/usesafeweb-runtime\/node-v22\.23\.2\/bin\/node["']/);
  assert.match(deploy, /NPM_CLI=["']\/opt\/usesafeweb-runtime\/node-v22\.23\.2\/lib\/node_modules\/npm\/bin\/npm-cli\.js["']/);
  assert.match(deploy, /"\$\{NODE_BIN\}" "\$\{NPM_CLI\}" ci --ignore-scripts --no-fund --no-audit/);
  assert.match(deploy, /"\$\{NODE_BIN\}" "\$\{NPM_CLI\}" run validate/);
  assert.doesNotMatch(deploy, /\$\(node --version\)|\$\(npm --version\)/);
});
