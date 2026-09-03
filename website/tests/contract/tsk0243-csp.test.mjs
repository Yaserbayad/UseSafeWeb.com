import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

const root = resolve(import.meta.dirname, '../..');
const nextConfig = readFileSync(resolve(root, 'next.config.ts'), 'utf8');

test('CSP permits only the dedicated verification subdomain family for cross-origin DNS probes', () => {
  assert.match(nextConfig, /connect-src 'self' https:\/\/\*\.verify\.usesafeweb\.com/);
  assert.doesNotMatch(nextConfig, /connect-src[^\n]*https:\/\/\*\.usesafeweb\.com(?:\s|["'])/);
  assert.doesNotMatch(nextConfig, /connect-src[^\n]*https:\/\/\*(?:\s|["'])/);
});
