import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';

const websiteRoot = resolve(import.meta.dirname, '../..');
const repoRoot = resolve(websiteRoot, '..');
const pkg = JSON.parse(readFileSync(resolve(websiteRoot, 'package.json'), 'utf8'));

function readRepo(path) {
  return readFileSync(resolve(repoRoot, path), 'utf8');
}

test('TSK-0453 pins deterministic formatting and keeps lint/type checks locally runnable', () => {
  assert.equal(pkg.devDependencies?.prettier, '3.9.6');
  assert.equal(pkg.scripts?.format, 'prettier --write .');
  assert.equal(pkg.scripts?.['format:check'], 'prettier --check .');
  assert.equal(typeof pkg.scripts?.lint, 'string');
  assert.equal(typeof pkg.scripts?.typecheck, 'string');
  assert.equal(existsSync(resolve(websiteRoot, '.prettierrc.json')), true);
  assert.equal(existsSync(resolve(websiteRoot, '.prettierignore')), true);
  assert.match(pkg.scripts?.['test:contract'] ?? '', /tsk0453\.test\.mjs/);
});

test('TSK-0453 defines review ownership for critical and governance paths', () => {
  const owners = readRepo('.github/CODEOWNERS');
  assert.match(owners, /^\/\.github\/\s+@Yaserbayad$/m);
  assert.match(owners, /^\/Plans\/Master\/\s+@Yaserbayad$/m);
  assert.match(owners, /^\/infrastructure\/\s+@Yaserbayad$/m);
  assert.match(owners, /^\/website\/src\/app\/api\/\s+@Yaserbayad$/m);
  assert.match(owners, /^\/website\/src\/lib\/ios-doh-profile\.ts\s+@Yaserbayad$/m);
});

test('TSK-0453 change/review policy includes generated/config impact and bounded exceptions', () => {
  const policy = readRepo('.github/CHANGE_REVIEW_POLICY.md');
  const template = readRepo('.github/pull_request_template.md');

  assert.match(policy, /generated/i);
  assert.match(policy, /configuration/i);
  assert.match(policy, /exception/i);
  assert.match(policy, /owner/i);
  assert.match(policy, /expir/i);
  assert.match(policy, /branch protection|ruleset/i);
  assert.match(template, /generated/i);
  assert.match(template, /configuration/i);
  assert.match(template, /exception/i);
  assert.match(template, /expiry/i);
});

test('TSK-0453 CI runs formatting, linting, and type checking on pull requests and main without deployment', () => {
  const workflow = readRepo('.github/workflows/accept-tsk0453-quality-review-rules-20260903.yml');
  assert.match(workflow, /pull_request:/);
  assert.match(workflow, /- main/);
  assert.match(workflow, /npm run format:check/);
  assert.match(workflow, /npm run lint/);
  assert.match(workflow, /npm run typecheck/);
  assert.doesNotMatch(workflow, /deploy|wrangler|production/i);
});
