# TSK-0243 — Isolated Target Partial Evidence — 2026-09-04

## Disposition

- Task: `TSK-0243` — Implement privacy-safe DNS protection verification.
- Runtime status remains: `TODO`.
- Evidence disposition: `PARTIAL_TARGET_EVIDENCE_ONLY`.
- This record does **not** change WBS, dependency, gate, acceptance, verification, evidence, authorization, or material-action semantics.
- Canonical WBS basis at staging: `Plans/Master/WBS/master-wbs.csv` blob `142a0d45b381136567d78545f063333f1e74901f`.
- Hard predecessor `TSK-0358` and lifecycle gate `LG-07` remain durably PASS in the current checkpoint.

## Exact proof source

- Isolated proof branch: `verify/tsk-0243-ephemeral-target-20260904`.
- Exact proof head: `5a60d95197948d5d46f96224765345e10c73dcde`.
- Workflow: `.github/workflows/verify-tsk0243-ephemeral-target-v2-20260904.yml`.
- GitHub Actions run: `33888891780` — `success`.
- GitHub Actions job: `101075410406` — all substantive proof and final-guard steps succeeded.
- Execution environment: isolated disposable target on the governed self-hosted Linux/x64 runner; the workflow used bounded network/mount isolation and teardown guards.

## Verified result

The exact run/job emitted the following PASS markers:

- `TSK0243_V2_TARGET_AND_ROLLBACK_GUARD=PASS`
- `TSK0243_V2_APP_BROWSER_BUILD=PASS`
- `TSK0243_EPH_READY=PASS`
- `TSK0243_EPH_ACTUAL_SYSTEM_DNS_REWRITE=PASS`
- `TSK0243_EPH_TLS_HOST_AUTHENTICATION=PASS`
- `TSK0243_EPH_WRONG_ORIGIN_HOST_PATH_FAIL_CLOSED=PASS`
- `TSK0243_EPH_REQUEST_PROBE_RESULT=PASS`
- `TSK0243_EPH_TAMPER_FAIL_CLOSED=PASS`
- `TSK0243_EPH_BROWSER_REAL_DNS_TLS_PROTECTION_MAP=PASS`
- `TSK0243_EPH_RATE_LIMIT=PASS`
- `TSK0243_EPH_QUERY_HISTORY_STORAGE_ABSENT=PASS`
- `TSK0243_EPH_INNER_ACCEPTANCE=PASS`
- `TSK0243_PUBLIC_FALSE_POSITIVE_GUARD=PASS`
- `TSK0243_EPH_TARGET_PROOF=PASS`

The terminal safety/cleanup guard emitted:

- `TSK0243_LIVE_ADGUARD_UNCHANGED=PASS`
- `TSK0243_EPHEMERAL_TEARDOWN=PASS`
- `TSK0243_DEPLOYMENT_DNS_PROXY_CERT_MUTATION=NONE`
- `TSK0243_PRODUCTION_MUTATION=NONE`
- `TSK0243_PARTICIPANT_PAYMENT_LAUNCH_ACTION=NONE`

The live AdGuard configuration/state/privacy hashes and process identity were unchanged across the proof, and disposable proof state was removed by teardown.

## Acceptance boundary

This is meaningful target-like evidence for the isolated verification path, including DNS rewrite, TLS host authentication, wrong-origin fail-closed behavior, signed result/tamper handling, browser Protection Map behavior, rate limiting, absence of query-history storage, and rollback/teardown guards.

It is **not** sufficient to mark `TSK-0243` PASS. The current `VER-0243` target-environment contract still requires the remaining production/public externally routed DNS/TLS/proxy trust-boundary evidence and the other acceptance evidence required by the canonical WBS. No public or production target was deployed, activated, or mutated by this proof.

## Material-action fence

This evidence grants no deployment or launch authority. Production/public DNS, proxy, certificate/profile, service, participant, payment, activation, launch, or equivalent material action remains governed by the existing durable authority and unresolved gates. No such action occurred in this proof.

## Verification references

- Exact proof source head: `5a60d95197948d5d46f96224765345e10c73dcde`.
- Actions run/job: `33888891780 / 101075410406`.
- Staging canonical base: `0e6e247156d1ed3410159ae69fab4ee9b2e1319e`.
- Evidence status: partial only; `TSK-0243 = TODO`.
