# TSK-0629 — Privacy-safe automated-check source implementation evidence

**Date:** 2026-09-03  
**Task:** TSK-0629 — Implement privacy-safe automated checks that confirm what can be technically verified and clearly label everything else  
**Lifecycle / authority:** L6 / HIGH / A4 / `AUTO_ALLOWED`  
**Hard predecessors:** TSK-0358 PASS; TSK-0320 PASS  
**Disposition:** **TODO — durable source implementation accepted; full ACC-0629 / VER-0629 / EVD-0629 is not yet complete.**

## Canonical source implementation

- Pull request: #64 — `TSK-0629: add privacy-safe automated verification source layer`.
- Final feature head: `fccc55aafb923993ac49c9f6a6ac7ae0f4baddfb`.
- Canonical squash merge: `d00a2ad85ae58c50457724f473da6aab0dfdcf56`.
- Canonical parent before this source slice: `b21c52bd1acbd2a0a8d5fbd9f11b560ed6217bf2`.
- Source scope is limited to the website verification classifier/state mapping, verification and Protection Map integration, controlled recovery transition, and TSK-0629 contract/browser tests.

## Test-first and review evidence

| Evidence | Run / job | Result | Purpose |
| --- | --- | --- | --- |
| Initial classifier RED | `33708880873` / `100503907019` | Expected failure | Inherited 35 contracts passed; five TSK-0629 contracts failed because the privacy-safe classifier did not yet exist. |
| Classifier GREEN | `33708931259` / `100504061968` | SUCCESS | Proved the strict classifier, privacy allowlist and fail-closed mappings before UI integration. |
| Browser integration RED | `33709051788` / `100504428933` | Expected failure | 40/40 contracts/build checks passed; five browser assertions failed because verify/Protection Map had not yet consumed the classifier. |
| Recovery-transition RED | `33709219853` / `100504937120` | 40/41 contracts pass; one intended failure | Proved `verify -> OPEN_TROUBLESHOOT` was not yet a legal controlled transition. |
| Pre-review GREEN | `33709338423` / `100505285643` | SUCCESS | Full source/build/browser acceptance before review cleanup. |
| Review RED | `33709549901` / `100505917901` | 41/42 contracts pass; one intended failure | Proved duplicated current-check construction and feature-marker leakage into the shared action API before correction. |
| Final feature gate | `33709655002` / `100506226449` | SUCCESS | Exact final feature head passed 42 contracts, lint/type-check/build, audits, governance validation and real-browser acceptance. |
| Canonical clean-main TSK-0629 gate | `33709817061` / `100506699183` | SUCCESS | Re-ran the TSK-0629 acceptance on canonical merge SHA `d00a2ad85ae58c50457724f473da6aab0dfdcf56`. |
| Canonical inherited locale/accountless regression | `33709817022` / `100506699008` | SUCCESS | Re-ran TSK-0359 plus inherited TSK-0358/TSK-0361 browser acceptance on the same canonical merge SHA. |

## Implemented and proven source behavior

1. `website/src/lib/automated-verification.ts` provides an exact-field privacy-safe classifier for support, verification-service, DNS-path and removal evidence.
2. Only a trusted `verified-fresh` DNS-path input can map to `working` with fresh positive technical evidence. Configuration, parent confirmation, journey state and account state cannot manufacture verification.
3. Stale positive evidence, negative evidence, service failure, conflict, unknown support, not-run verification, unsupported paths and removal all map deterministically to non-positive states and appropriate recovery/no-recovery behavior.
4. Runtime classifier input is exact-field allowlisted. Query/domain-history/browsing/raw-diagnostic/account/child payload expansion is rejected.
5. Verify and Protection Map consume one canonical `getCurrentAutomatedVerification()` source; the current product source intentionally returns `unknown / unknown / not-run` because no approved fresh E1 DNS-path producer is connected.
6. Query parameters cannot manufacture a positive verification result.
7. Uncertain verification can enter troubleshooting through the controlled accountless state machine rather than bypassing session integrity.
8. The source preserves the existing Protection Map evidence precedence and the no-browsing-history/privacy boundaries.

## Canonical clean-main verification

Run `33709817061` checked out exactly `d00a2ad85ae58c50457724f473da6aab0dfdcf56` on GitHub-hosted Ubuntu 24.04.4 with Node `22.23.2`.

Observed evidence includes:
- master-plan validation PASS: 641 tasks / 858 dependency edges / 0 broken links / 0 generated missing task IDs;
- contract tests: **42 pass / 0 fail**;
- lint: zero errors; one inherited non-error `_accountState` unused-variable warning;
- TypeScript type-check PASS;
- Next.js `16.3.3` production build PASS; 55 pages generated;
- production/all dependency audits: **0 vulnerabilities**;
- pinned Playwright `1.62.1`, axe-core `4.13.0`, Chrome for Testing `151.0.7922.34`;
- `TSK0629_BROWSER_ACCEPTANCE=PASS`.

Independent inherited browser regression run `33709817022` also completed successfully on the same merge SHA.

## Why TSK-0629 remains TODO

Current `ACC-0629` requires the product to confirm what can be technically verified and distinguish working/failed/uncertain/removed states while keeping parent confirmation separate and offering recovery. The source classifier and fail-closed user flow are implemented, but the current product has **no approved trusted producer of fresh E1 DNS-path evidence**. Therefore the canonical implementation intentionally cannot produce an actual positive `working / protected/verified` runtime result today.

A source-level positive test vector is not target evidence and cannot substitute for the missing trusted DNS-path check. Full `VER-0629` still requires functional positive/negative/configuration/security/privacy/rollback evidence against the actual approved verification path in the applicable target environment.

`TSK-0243` is the current L6 privacy-safe DNS-protection verification task whose `ACC-0243` requires deterministic supported-path verification with no query history, cache/failure/conflict handling, approved event data only, and exact Protection Map mapping. Current WBS does **not** declare TSK-0243 as a hard predecessor of TSK-0629. The implementation evidence therefore records a technical enabling relationship for sequencing only; it does not invent or mutate a planning dependency edge.

## Security, privacy and side-effect boundary

- No deployment, DNS-server mutation, profile distribution, production/runtime activation, market activation, participant processing or launch occurred.
- No external verification endpoint was invented.
- No browsing/query/domain history, raw diagnostic content, account identity or child identity was introduced into the verification classifier.
- No new authentication dependency or analytics transport was added.
- URL/query input is not trusted as verification evidence.
- Source rollback is the ordinary revert of canonical merge `d00a2ad85ae58c50457724f473da6aab0dfdcf56`; there is no external runtime rollback for this source-only slice.

## Preserved unresolved fences

- `TSK-0629`: **TODO** until a trusted approved fresh E1 DNS-path producer and full target evidence exist.
- `TSK-0360`: **TODO** pending supported-iPhone and related acceptance evidence.
- `TSK-0455`: **WAITING** for a genuinely qualifying fresh Ubuntu 24.04 LTS target host plus required target access/evidence.
- `TSK-0399`: remains ineligible while `TSK-0360` is non-PASS.
- No `GATE-0026` exists or is created.
