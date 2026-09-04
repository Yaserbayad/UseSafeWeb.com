type RuntimeEnvironment = Readonly<Record<string, string | undefined>>;

export type ServerRuntimeConfig = {
  publicOrigin: string;
  releaseSha: string;
  signingSecret: string;
};

const verifierVersion = 'private-rewrite-v1' as const;

function invalidRuntimeConfiguration(): never {
  throw new TypeError('invalid server runtime configuration');
}

function parsePublicOrigin(value: string | undefined): string {
  if (typeof value !== 'string') invalidRuntimeConfiguration();
  try {
    const url = new URL(value);
    if (url.protocol !== 'https:' || url.origin !== value || url.username || url.password)
      invalidRuntimeConfiguration();
    return value;
  } catch {
    invalidRuntimeConfiguration();
  }
}

export function readServerRuntimeConfig(env: RuntimeEnvironment = process.env): ServerRuntimeConfig {
  const publicOrigin = parsePublicOrigin(env.USESAFEWEB_PUBLIC_ORIGIN);
  const signingSecret = env.USESAFEWEB_DNS_VERIFICATION_SIGNING_SECRET;
  const releaseSha = env.USESAFEWEB_RELEASE_SHA;
  if (
    typeof signingSecret !== 'string' ||
    Buffer.byteLength(signingSecret, 'utf8') < 32 ||
    typeof releaseSha !== 'string' ||
    !/^[0-9a-f]{40}$/.test(releaseSha)
  ) {
    invalidRuntimeConfiguration();
  }
  return { publicOrigin, releaseSha, signingSecret };
}

export function publicRuntimeStatus(env: RuntimeEnvironment = process.env): {
  ready: boolean;
  releaseSha: string | null;
  verifierVersion: typeof verifierVersion;
} {
  try {
    const config = readServerRuntimeConfig(env);
    return { ready: true, releaseSha: config.releaseSha, verifierVersion };
  } catch {
    return { ready: false, releaseSha: null, verifierVersion };
  }
}
