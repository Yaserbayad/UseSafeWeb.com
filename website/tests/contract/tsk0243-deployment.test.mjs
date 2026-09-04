import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { stripTypeScriptTypes } from 'node:module';

const website = resolve(import.meta.dirname, '../..');
const repository = resolve(website, '..');
const runtimeConfigPath = resolve(website, 'src/lib/runtime-config.ts');
const healthRoutePath = resolve(website, 'src/app/api/health/ready/route.ts');
const servicePath = resolve(repository, 'infrastructure/web-server/usesafeweb-web.service');
const envExamplePath = resolve(repository, 'infrastructure/web-server/website.env.example');
const validatorPath = resolve(repository, 'infrastructure/web-server/validate-runtime.mjs');
const deployPath = resolve(repository, 'infrastructure/web-server/deploy-release.sh');

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
  assert.doesNotMatch(validator, /console\.(?:log|error).*SIGNING_SECRET/i);

  const deploy = readFileSync(deployPath, 'utf8');
  assert.match(deploy, /10\.9\.8/);
  assert.match(deploy, /npm ci --ignore-scripts --no-fund --no-audit/);
  assert.match(deploy, /npm run validate/);
  assert.match(deploy, /\.next\/standalone/);
  assert.match(deploy, /SERVICE=["']usesafeweb-web\.service["']/);
  assert.match(deploy, /systemctl restart ["']\$\{SERVICE\}["']/);
  assert.match(deploy, /api\/health\/ready/);
  assert.match(deploy, /rollback/i);
});
