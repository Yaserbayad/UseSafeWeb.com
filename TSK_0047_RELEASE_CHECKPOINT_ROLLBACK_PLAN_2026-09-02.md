# TSK-0047 — Incremental Release, Checkpoint and Rollback Plan

**Version:** 1.0.0  
**Date:** 2026-09-02  
**Authority:** Derived L5 release-readiness artifact. WBS, current decisions/gates, and `CURRENT_STATE.md` remain authoritative.

## Release model

- `main` is the canonical durable branch. Material changes use bounded topic branches/PR-quality review where useful, then merge only after applicable automated checks pass.
- Development proceeds in small vertical slices from the accepted TSK-0048 backlog. A slice may span web, server, DNS/config and tests when necessary to deliver one independently verifiable outcome.
- **CR-0007 / DEC-0054 controls environment semantics:** after integrated readiness, production is the only active lifecycle environment. CI/ephemeral preview/test environments are allowed and disposable. A persistent staging or separate pilot lifecycle is **not mandatory** and may exist only if an explicit current trigger/owner decision opens it.
- L6 implementation cannot start until LG-07 is actually PASS. This document does not grant that gate.

## Versioning and change classes

| Class | Typical change | Version/change treatment | Required checkpoint |
|---|---|---|---|
| C1 | Docs, tests, non-runtime planning/tooling | patch/change record | lint/validator/review; no production claim |
| C2 | Web/content/config change with bounded reversible behavior | patch/minor as semantically appropriate | focused + regression tests; privacy/truth/accessibility checks |
| C3 | Auth/session/ownership/datastore/AdGuard/DNS/security/recovery behavior | minor/major based on compatibility | full affected VAT set, negative/security/privacy/recovery evidence, rollback target |
| C4 | Breaking interface/schema/security boundary/product-scope change | explicit major/change-control review | owner-controlled scope/architecture decision where applicable; all invalidated evidence reopened |
| C5 | Production activation/release | immutable release identifier tied to source/config/content/filter versions | applicable lifecycle gate, health checks, rollback proof, evidence bundle |

## Branch and change flow

1. Re-read current WBS/task/dependencies/gates/authority before material implementation.
2. Implement the smallest eligible vertical outcome; do not combine unrelated mutable authority changes.
3. Run deterministic local/CI checks and the task-specific acceptance suite.
4. For security/privacy/recovery-sensitive changes, obtain the independent evidence required by the canonical acceptance contract.
5. Merge/persist only after checks pass and stale-head conditions are reconciled.
6. Record source commit plus configuration/content/filter/schema versions needed to reconstruct the release.
7. Recompute the governed frontier after each accepted state mutation.

## Environment and promotion checkpoints

### E0 — Local / isolated development
- Synthetic/non-sensitive fixtures only unless a later task explicitly authorizes otherwise.
- No production secrets committed or embedded.
- Build/lint/type/unit/contract/security checks run deterministically.

### E1 — CI / ephemeral integrated verification
- Disposable environment or isolated test execution; no persistent staging requirement.
- Run affected TSK-0516 VAT cases, including accountless-core regression and all security/privacy/recovery cases touched by the change.
- Verify config migration forward and rollback where state/config changes are involved.
- Environment teardown/rebuild must not create a second mutable authority store.

### E2 — Production release/activation
- Available only when all applicable gates authorize it; LG-07 is a prerequisite for starting L6 build and later gates continue to control production activation/public release.
- Source/config/content/filter versions are immutable/reconstructable.
- Pre-deploy backup/recovery inputs exist where stateful or DNS configuration can be affected.
- Deployment health gate checks web, DNS/DoH, TLS, critical accountless journey, auth/session if included, privacy-safe telemetry and error rate.
- Production ramp/validation follows CR-0007; no separate mandatory pilot environment is inferred.

## Configuration and data migration rules

- Prefer backward-compatible additive changes; schema/config migrations are versioned and deterministic.
- Every destructive or non-backward-compatible migration must define preconditions, backup/snapshot where technically applicable, rollback/restore method, and failure-reconciliation behavior before execution.
- AdGuard/DNS configuration changes are diffable, validated against privacy settings/upstream/filter invariants, and retain a known-good rollback input.
- Auth/session/device ownership migrations must preserve cross-parent isolation and fail closed on ambiguous mappings.
- Never migrate or create browsing/query/activity history because it is outside product scope.

## Test gates

A release is blocked when any applicable condition fails:
- task-specific ACC/VER/EVD;
- affected TSK-0516 VAT cases;
- accountless core remains usable without login;
- authz/CSRF/IDOR/cross-parent isolation;
- secrets/credential isolation and no sensitive evidence leakage;
- deletion/revocation/recovery and partial-failure convergence;
- DNS/AdGuard correctness, TLS and Protection Map truth;
- privacy-minimal logging/events;
- accessibility/performance requirements applicable to changed surfaces;
- deterministic build/config validation and rollback evidence.

## Rollback triggers

Immediate stop/rollback or fail-safe action is required for:
1. cross-parent/ownership bypass, IDOR, authentication/session or CSRF security failure;
2. committed/exposed secret, private key, admin credential or prohibited browsing/query history;
3. false `verified` protection status or material DNS filtering/availability regression;
4. destructive deletion/revocation/data migration that cannot reconcile to the documented safe state;
5. DNS/DoH/TLS outage or unacceptable degradation beyond the approved health threshold;
6. severity-1/2 or unresolved Critical/High blocking failure;
7. failed health gate, incompatible dependency/config version, or unrecoverable deployment drift.

## Rollback procedure

- Stop further promotion/change propagation.
- Select the last independently verified source/config/content/filter release target; never guess a rollback target.
- Restore application/configuration and, where required, database/DNS configuration from the approved recovery input.
- Revoke/rotate compromised credentials rather than merely reverting code if exposure occurred.
- Run the minimum health + privacy/security + affected VAT set needed to prove recovery.
- Record trigger, affected versions, actions, verification result, residual impact and next eligible corrective task.
- If safe rollback cannot be proven, fail closed and mark the affected governed task BLOCKED rather than declaring recovery.

## Evidence retention

For every material release/checkpoint retain only privacy-safe evidence needed to reconstruct the decision: source commit, relevant artifact/config hashes or versions, environment class, test/run identifiers, verifier result, release/rollback target, timestamp and deviations/disposition. Never retain production secrets or raw DNS/browsing history in evidence.

## Release-class authority

- Reversible planning/docs/tests and ordinary non-production repository work remain `AUTO_ALLOWED` when their current WBS row says so.
- Implementation/deployment actions remain governed by each task’s current Action Authority and lifecycle gate; this plan does not elevate authority.
- Production activation, material spend, owner-only resource decisions, human-only tasks, secrets/account access and irreversible consequences remain fenced exactly by current authority.
- CR-0009 legal/regulatory/compliance conclusions remain owner-external for sequencing only; no legal approval is inferred.

## LG-07 handoff

TSK-0047 proves that implementation has a coherent versioning, branch/change, environment, migration, test-gate, rollback and evidence-retention model. It does **not** prove implementation or deployment has occurred and does not mark LG-07 PASS. After acceptance, the L5 frontier must be recomputed, including the HUMAN_ONLY TSK-0587 resource boundary and any other current eligible prerequisites.
