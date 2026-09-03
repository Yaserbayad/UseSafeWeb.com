# TSK-0243 — Privacy-safe DNS verification source contract

**Task:** `TSK-0243 — Implement privacy-safe DNS protection verification`  
**Acceptance:** `ACC-0243 / VER-0243 / EVD-0243`  
**Lifecycle / authority:** L6 / A3 / `AUTO_ALLOWED`  
**Date:** 2026-09-03  
**Status:** **PARTIAL SOURCE IMPLEMENTATION / TODO — NOT PASS**  
**Canonical base:** `main` at `ade4d45c84fd7ab671b55a16ecb7fde0b74411e3`  
**Accepted feature source head before this evidence note:** `9f53ed329485f0578aa7f1a55b67cf32be90976a`

## 1. Scope completed

A source-only trust boundary now exists for a future privacy-safe DNS-path verifier without creating or modifying any live DNS, TLS, AdGuard, web-runtime, participant, market, or production state.

Current source artifact:

- `website/src/lib/dns-verification-proof.ts`
- blob `033b7db0e75e2625d16588bffb37eec4bb750cd8`
- protocol `usesafeweb-dns-path-v1`
- verifier version `private-rewrite-v1`
- verification suffix contract `verify.usesafeweb.com`

The source contract provides:

1. cryptographically generated 128-bit per-check challenges via Node `crypto.randomBytes(16)`;
2. cache-busting probe hostnames of the form `<challenge>.verify.usesafeweb.com`;
3. exact-field observation validation with no query/browsing/activity-history fields;
4. HMAC-SHA256 signed observations using an externally supplied server-side signing secret;
5. constant-time signature comparison;
6. explicit binding to the expected anonymous scope **and current challenge**, preventing reuse of a still-fresh proof from an earlier check;
7. verifier-owned proof expiry with a maximum 120-second lifetime;
8. 2,048-byte token and eight-observation batch limits for untrusted input;
9. deterministic `verified-fresh`, `verified-stale`, `failed`, `uncertain`, and `not-run` reconciliation, with conflicts failing closed;
10. an approved event projection containing only `dnsPath`, `reasonCode`, and `verifierVersion`.

Only `verified-fresh / TECH_VERIFIED` is eligible to feed the existing TSK-0629 / TSK-0320 technical-verification path. Configuration presence, parent confirmation, account state, journey completion, profile presence, or a previous token cannot manufacture current technical verification.

## 2. TDD and verification evidence

### Initial capability RED / GREEN

- RED run `33711097037`, job `100510538662`: inherited contracts passed; new TSK-0243 tests failed because the proof module did not exist.
- Initial GREEN run `33711157301`, job `100510718300`: source contract passed the full gate before adversarial review.

### Security/correctness review corrections

**Replay binding defect**

- Review found that a fresh proof was initially scope-bound but not bound to the current challenge.
- RED run `33711301942`, job `100511165195`: exact regression reproduced; 46/47 passed and the stale-challenge replay assertion failed.
- GREEN run `33711373275`, job `100511394013`: current-challenge binding passed.

**Untrusted-input resource bounds**

- Review found no explicit token-size or observation-count bound.
- RED run `33711457617`, job `100511657883`: 47/48 passed; the new bounds assertion failed as expected.
- GREEN run `33711517533`, job `100511840635`: token and batch bounds passed.

**Cryptographic challenge generation**

- Review found that validating a caller-supplied 128-bit-shaped challenge did not itself guarantee a fresh challenge.
- RED run `33711602449`, job `100512095010`: 47/48 passed; `createDnsVerificationChallenge` was absent.
- Final source GREEN run `33711687383`, job `100512351329`, exact head `9f53ed329485f0578aa7f1a55b67cf32be90976a`: **SUCCESS**.

Final source-head gate observations:

- repository-structure verification: PASS;
- modular Master Plan validation: PASS — 641 tasks, 858 dependency edges, 4,587 relationship entities, 18,152 relationship targets, 0 broken links, 0 generated missing task IDs;
- website contract suite: **48/48 PASS**;
- ESLint: 0 errors; one inherited `_accountState` unused-variable warning in `core-state-machine.ts`;
- Next/TypeScript type-check: PASS;
- Next.js production build: PASS, 55/55 static pages generated where applicable;
- `npm audit --audit-level=high`: 0 vulnerabilities;
- `npm audit --omit=dev --audit-level=high`: 0 vulnerabilities;
- `git diff --check`: PASS;
- clean working-tree assertion: PASS.

## 3. Authoritative technical-source basis

- Node.js `crypto.randomBytes()` is documented as generating cryptographically strong pseudorandom data; `crypto.createHmac()` creates HMAC instances; `crypto.timingSafeEqual()` uses a constant-time comparison suitable for HMAC digests: https://nodejs.org/api/crypto.html
- Current AdGuard Home configuration documentation supports wildcard legacy rewrites such as `*.example.com`, and its DNS rewrite rules can replace matching DNS responses: https://github.com/AdguardTeam/AdGuardHome/wiki/Configuration
- Current AdGuard Home filtering documentation defines `$dnsrewrite` behavior and priority: https://github.com/AdguardTeam/AdGuardHome/wiki/Hosts-Blocklists

These sources support the source contract only. They do not prove that the required UseSafeWeb target DNS/TLS path has been configured or works.

## 4. Acceptance still missing — why TSK-0243 is not PASS

`VER-0243` requires target-environment functional, negative, configuration, security/privacy, failure/conflict and rollback evidence. No such target deployment or observation was authorized or performed in this work.

Before `TSK-0243` can become PASS, the approved target environment must independently prove at least:

1. a dedicated verification hostname/suffix is resolved by the intended UseSafeWeb DNS path using an approved AdGuard rewrite or equivalent mechanism;
2. the same random probe hostname does **not** produce a false positive through an ordinary non-UseSafeWeb/public resolver path;
3. TLS authenticates the challenge hostname/verifier endpoint and the signer secret remains server-only and outside Git/log/evidence;
4. the verifier signs only observations caused by the intended supported DNS path, not arbitrary caller input;
5. fresh challenge probes defeat cache reuse and stale proofs cannot restore a positive state;
6. service unavailable, negative, timeout/stale, malformed, replayed and conflicting results fail closed into the current Protection Map semantics;
7. runtime/event/storage inspection proves no browsing/query/activity history, raw DNS history, client IP persistence, unnecessary identity, secret, or challenge/scope data is retained in approved product events;
8. the target change has a tested rollback/removal path;
9. the exact target configuration/version and evidence are recorded under current `VER-0243 / EVD-0243`.

## 5. Security and trust-boundary limitation

The HMAC contract authenticates proof tokens against untrusted/browser-side tampering and replay across challenge/scope boundaries when the verifier and consumer keep the secret server-side. It does **not** defend against a fully compromised trusted signer/application environment that possesses the HMAC key. Target deployment must therefore restrict signing authority to the intended verifier path, protect/rotate the key, and prove that arbitrary application/client input cannot invoke a positive signer.

## 6. Non-inference / preserved fences

- `TSK-0243` remains **TODO**; source existence and successful CI are not target-environment acceptance.
- `TSK-0359` remains durable PASS and is not reopened or rewritten.
- `TSK-0629` remains TODO until a trusted deployed DNS-path E1 producer is actually evidenced.
- `TSK-0360` remains TODO pending its supported-iPhone and related acceptance evidence.
- `TSK-0455` remains WAITING for a genuinely qualifying owner-provided fresh Ubuntu 24.04 LTS target host/access.
- `TSK-0399` remains ineligible while `TSK-0360` is non-PASS.
- No `GATE-0026` exists or is created.
- No DNS-server mutation, verification DNS record/rewrite, TLS certificate, web deployment, profile distribution, production/runtime activation, participant processing, market activation, payment, launch, or unrelated task/gate PASS is inferred or performed.

## 7. Stable outcome

The safe source contract is complete enough to integrate as **partial durable work**, but `TSK-0243` cannot truthfully advance to PASS until the target DNS/TLS verifier is implemented and observed under the current acceptance contract. After merge/read-back, runtime state should record this as `TODO` with the exact source/evidence/run references above and preserve all existing material-action fences.
