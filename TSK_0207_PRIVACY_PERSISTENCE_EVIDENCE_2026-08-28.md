# TSK-0207 — Privacy Persistence Verification Evidence

**Task:** TSK-0207 — Verify no persistent identifiable query history or client statistics  
**Acceptance:** ACC-0207  
**Verification:** VER-0207  
**Evidence:** EVD-0207  
**Date:** 2026-08-28  
**Target:** production host `adguardvm`

## Exact environment/artifacts

- Workflow source commit: `d087adddd1bc351d62bfc7fffe49cc14b0d52548`
- Workflow blob: `c97a71d10a8e4d2aad2cc48b8fe4fbee8761953d`
- Runtime-state blob at checkout: `3987dabdeced6ea70e811bc9b7a59dcd0ed46758`
- Approved-config blob: `e9975c4e75c2a68131f049da942468d8d1952d8d`
- Backup-policy blob: `e62b48a3e746b1be90881bbffab3b7680384cc16`
- AdGuard Home version: `v0.107.79`
- Production machine identity was asserted against the accepted `adguardvm` machine-id fingerprint before testing.

## Fresh controlled production test

The assertion step generated one randomized reserved `.invalid` DNS name locally on the production resolver. It then verified, after the request:

- persisted query logging is disabled;
- persisted file query logging is disabled;
- API query logging is disabled;
- the synthetic name is absent from query-log output and query-log item count is `0`;
- no non-empty `querylog.json*` file exists;
- persisted and API statistics are disabled;
- top-client count is `0` and stored statistics query count is `0`;
- persistent client count is `0` and client-IP anonymisation remains enabled;
- approved encrypted backup pairs retained: `1` (within the approved maximum of two);
- every retained archive is root-only `0600` age ciphertext with matching root-only metadata and verified SHA-256;
- the backup directory is root-only and contains no unexpected file/directory class;
- plaintext backup staging count is `0`;
- no stale/raw backup-named copy exists in the AdGuard service/config or UseSafeWeb secret area, and no matching temporary backup artifact exists in `/tmp` or `/var/tmp`;
- unapproved backup artifact count for the controlled project locations is `0`.

The approved encrypted archives contain the configuration package defined by the accepted backup policy; accepted TSK-0430 owner-side decryption already proved the package/member scope and absence of prohibited query history. The retained same-VM encrypted copies are documented residual recovery artifacts, not query/client-history datasets and not proof of node-loss resilience.

## Privacy/legal boundary

REQ-0018 remains respected: no real England participant was activated or processed. The test used a randomized reserved synthetic name only. No participant browsing/domain history, participant identity, device identity, credential, token, private key, or raw query data is stored in this evidence.

REQ-0019/INT-0007 are supported by direct actual-configuration/runtime/storage evidence rather than assumed policy. CON-0007 and CON-0008 remain satisfied.

## Acceptance evaluation

- Persistent raw query/domain history after controlled test: **none — PASS**.
- File query log after controlled test: **none — PASS**.
- Identifiable client/statistics history after controlled test: **none — PASS**.
- Unapproved backup copy in controlled project locations: **none — PASS**.
- Residual operational data: only the documented root-only approved encrypted configuration recovery artifact(s), with no prohibited query/client history — **PASS**.

**Stable outcome: TSK-0207 = PASS.**

This PASS verifies the current synthetic production privacy-persistence condition only. It does not resolve the separately deferred UK representative/ICO work, authorize real-participant activation, or satisfy later legal/release gates.
