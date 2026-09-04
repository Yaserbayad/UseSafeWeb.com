import { createHash } from 'node:crypto';

const maximumEntries = 4096;
const consumed = new Map<string, number>();

function digest(requestToken: string, observationToken: string): string {
  return createHash('sha256').update(requestToken).update('\0').update(observationToken).digest('base64url');
}

export function consumeDnsVerificationPair(
  requestToken: string,
  observationToken: string,
  expiresAt: number,
  nowMs: number,
): boolean {
  if (!Number.isSafeInteger(expiresAt) || expiresAt <= nowMs) return false;
  for (const [key, expiry] of consumed) {
    if (expiry <= nowMs) consumed.delete(key);
  }
  const key = digest(requestToken, observationToken);
  if (consumed.has(key)) return false;
  if (consumed.size >= maximumEntries) return false;
  consumed.set(key, expiresAt);
  return true;
}
