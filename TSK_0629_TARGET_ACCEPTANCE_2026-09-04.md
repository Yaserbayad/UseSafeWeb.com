# TSK-0629 — Target acceptance evidence — 2026-09-04

**Task:** TSK-0629 — Implement privacy-safe automated checks that confirm what can be technically verified and clearly label everything else  
**Acceptance:** ACC-0629  
**Verification:** VER-0629  
**Evidence:** EVD-0629  
**Disposition:** **PASS**  
**Canonical basis before publication:** `main@9bbc3984167d2c33c2eb6649acfb841a2fcc2f78`  
**WBS blob:** `142a0d45b381136567d78545f063333f1e74901f`

## Why the former TODO gap is resolved

The prior source evidence correctly kept TSK-0629 TODO because, at that time, the accepted source slice had no approved trusted producer of fresh E1 DNS-path evidence. That historical statement is now superseded for TSK-0629 acceptance by the subsequently implemented privacy-safe DNS-verification path and its isolated target proof.

Current canonical product source connects the user-facing verification surfaces to the producer:

- `website/src/components/dns-verification-panel.tsx` blob `60e0276024836be599a6be7915022321fabcf98c` calls `runDnsVerification(...)` and maps its DNS-path result through `classifyAutomatedChecks(...)`.
- `website/src/components/dns-verification-card.tsx` blob `d552826d70ef40a8fb26294278b45cb463f5f80b` does the same for Protection Map.
- `website/src/lib/dns-verification-browser.ts` blob `03f76ee87ad455f0cda5d2cb6558cb0daf6916e0` implements the bounded request -> DNS probe -> signed result flow; it accepts only exact approved result fields and fails closed on malformed/unreachable evidence.
- `website/src/app/api/dns-verification/results/route.ts` blob `ec2de11b8c65a95357db013d319485ee4370130a` verifies the issued request and signed DNS observation before projecting the approved event.
- `website/src/lib/automated-verification.ts` blob `1caabf798ef0c2872a771ee97888a61c945836da` retains a conservative standalone fallback, while the live verify/Protection Map components use the connected `runDnsVerification(...)` producer path above.

## Exact-current source requalification

Read-only branch: `verify/tsk0629-current-source-rebind-20260904`  
Exact verification head: `761779ef0b8f89669d22416390f286061d8d3ab7`  
Canonical source parent: `5f08f91aa8e95c0650bff9ddf876de9da9dd573d`  
GitHub Actions run/job: `33896808860 / 101101264905` — **SUCCESS**.

The workflow proved exact source binding, then completed:

- focused TSK-0629 contract suite: **7/7 PASS**;
- lint: zero errors;
- TypeScript type-check: PASS;
- production build: PASS;
- production and full npm audits: **0 vulnerabilities**;
- real-browser fail-closed/recovery acceptance: `TSK0629_BROWSER_ACCEPTANCE=PASS`;
- `TSK0629_CURRENT_SOURCE_REBIND=PASS`;
- clean repository and no production/material mutation.

No `website/` file changed from that verified canonical parent through current `main@9bbc3984167d2c33c2eb6649acfb841a2fcc2f78`; PR #105 changed only CURRENT_STATE.md and the TSK-0489 evidence record. Therefore the requalified product bytes remain the current canonical product bytes.

## Trusted E1 target evidence

The bounded isolated target proof is durably recorded in `TSK_0243_ISOLATED_TARGET_PARTIAL_EVIDENCE_2026-09-04.md`.

Exact source head: `5a60d95197948d5d46f96224765345e10c73dcde`  
GitHub Actions run/job: `33888891780 / 101075410406` — **SUCCESS**.

The proof built the current application, started a disposable isolated AdGuard Home/DNS/TLS/proxy target, exercised the real browser request -> DNS rewrite -> TLS-authenticated probe -> signed result -> classifier -> Protection Map path, and observed:

- `TSK0243_EPH_ACTUAL_SYSTEM_DNS_REWRITE=PASS`;
- `TSK0243_EPH_TLS_HOST_AUTHENTICATION=PASS`;
- `TSK0243_EPH_REQUEST_PROBE_RESULT=PASS`, with exact approved result `{dnsPath, reasonCode, verifierVersion}` and `dnsPath=verified-fresh`;
- `TSK0243_EPH_WRONG_ORIGIN_HOST_PATH_FAIL_CLOSED=PASS`;
- `TSK0243_EPH_TAMPER_FAIL_CLOSED=PASS`;
- `TSK0243_EPH_BROWSER_REAL_DNS_TLS_PROTECTION_MAP=PASS`, including `working` and `protected/verified` on the real connected path;
- `TSK0243_EPH_RATE_LIMIT=PASS`;
- `TSK0243_EPH_QUERY_HISTORY_STORAGE_ABSENT=PASS`;
- `TSK0243_PUBLIC_FALSE_POSITIVE_GUARD=PASS`;
- `TSK0243_LIVE_ADGUARD_UNCHANGED=PASS`;
- `TSK0243_EPHEMERAL_TEARDOWN=PASS`.

The TSK-0243 proof head and the exact-current TSK-0629 source have byte-identical relevant website implementation for this acceptance path; subsequent canonical changes through `9bbc3984167d2c33c2eb6649acfb841a2fcc2f78` did not alter website source.

## ACC-0629 mapping

- **Working:** the isolated real-browser E1 path produced `verified-fresh`, then `working / protected/verified`.
- **Failed / uncertain:** exact-current contracts and browser tests prove failed, stale, conflict, unreachable, malformed, unsupported and not-run evidence cannot manufacture a positive state and route to controlled recovery where applicable.
- **Removed:** exact-current classifier tests prove removed evidence maps deterministically to `removed` and does not infer technical success.
- **No browsing history:** the classifier is exact-field allowlisted; the target proof confirms no DNS-verification query-history/session-storage leakage and AdGuard query logging/statistics remain disabled in the disposable proof.
- **Parent confirmation separate:** configuration/parent confirmation is a separate field and cannot manufacture technical verification; technical success requires fresh DNS-path evidence.
- **Actionable recovery:** non-positive recoverable states route through the controlled troubleshooting transition, proven by focused contract and browser acceptance.

## VER-0629 mapping

- **Functional:** real DNS rewrite, TLS probe, signed result, browser verify and Protection Map positive path passed.
- **Negative:** wrong-origin/host, tamper, malformed/untrusted evidence, query spoof and false-positive guards fail closed.
- **Configuration:** exact source/runtime bindings, signing configuration requirements, origin/host restrictions and rate limiting were exercised.
- **Security/privacy:** exact-field projection, signed request/observation verification, no query-history storage, no raw diagnostic expansion and clean audits passed.
- **Rollback/recovery:** disposable target teardown passed; live AdGuard config/state/privacy hashes and PID were unchanged; application recovery/fail-closed states passed.

## EVD-0629 record

- Artifact/version: exact canonical source blobs and the isolated target workflow/head above.
- Exact environments: GitHub-hosted exact-current source requalification plus isolated self-hosted Ubuntu 24.04 / AdGuard Home v0.107.79 target proof.
- Verification outputs: runs/jobs `33896808860 / 101101264905` and `33888891780 / 101075410406`.
- Verification date: 2026-09-04.
- Responsible verifier: governed GitHub Actions execution with canonical read-back by the Project Governor.
- Deviations: no production/public deployment was used or required for ACC-0629. TSK-0243 remains TODO because its own stricter verification contract still requires the remaining production/public externally routed DNS/TLS/proxy trust-boundary evidence.

## Material-action and non-inference boundary

TSK-0629 PASS records the automated-check product behavior only. It does **not** mark TSK-0243 PASS and creates no deployment, production/public DNS/proxy/certificate/profile/service mutation, participant processing, payment, telemetry activation, market activation, launch, or other fenced material-action authority. The isolated target was disposable and teardown/live-target guards passed.
