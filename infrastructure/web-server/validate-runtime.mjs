import { readFileSync } from 'node:fs';
import process from 'node:process';

const fail = (message) => {
  process.stderr.write(`USESAFEWEB_RUNTIME_VALIDATION=FAIL reason=${message}\n`);
  process.exit(78);
};

if (process.version !== 'v22.23.2') fail('node_version');
if (process.env.NODE_ENV !== 'production') fail('node_env');
if (process.env.HOSTNAME !== '127.0.0.1') fail('hostname');
if (process.env.PORT !== '3100') fail('port');
if (process.env.NEXT_TELEMETRY_DISABLED !== '1') fail('telemetry');

const releaseSha = process.env.USESAFEWEB_RELEASE_SHA ?? '';
if (!/^[0-9a-f]{40}$/.test(releaseSha)) fail('release_sha');
let releaseMarker;
try {
  releaseMarker = readFileSync(new URL('./.release-sha', import.meta.url), 'utf8').trim();
} catch {
  fail('release_marker');
}
if (!/^[0-9a-f]{40}$/.test(releaseMarker) || releaseMarker !== releaseSha) fail('release_marker');

if (Buffer.byteLength(process.env.USESAFEWEB_DNS_VERIFICATION_SIGNING_SECRET ?? '', 'utf8') < 32) {
  fail('signing_secret');
}
try {
  const origin = new URL(process.env.USESAFEWEB_PUBLIC_ORIGIN ?? '');
  if (origin.protocol !== 'https:' || origin.origin !== process.env.USESAFEWEB_PUBLIC_ORIGIN) fail('public_origin');
} catch {
  fail('public_origin');
}

process.stdout.write('USESAFEWEB_RUNTIME_VALIDATION=PASS\n');
