# TSK-0374 — Versioned Device/Service Content Delivery Source Implementation — 2026-09-03

## Disposition

`TSK-0374 = TODO — SOURCE IMPLEMENTATION PARTIAL`.

This artifact records durable source-implementation and source-CI evidence only. It does **not** satisfy the complete `ACC-0374 / VER-0374 / EVD-0374` contract and is not a task PASS.

## Current authority and prerequisites

- Current normalized WBS blob: `eb35f3b10356396c5117e3f47d0b0378953e2157`.
- `TSK-0374 — Implement versioned device/service content delivery`: L6 / MEDIUM / A3 / `AUTO_ALLOWED`; hard dependencies `TSK-0375; TSK-0323`.
- Current runtime evidence independently confirms both hard predecessors are PASS: TSK-0375 under its 2026-09-03 accepted state and TSK-0323 under its current post-CR-0007 accepted state.
- `ACC-0374` requires correct content/version selection, visible stale/unsupported states, preserved integrity/version metadata, safe missing-content behavior, and update rollback capability.
- `VER-0374` requires execution in the target environment with functional, negative, configuration, security/privacy, and rollback checks.

## Canonical source implementation

- Source PR: `#84`, `TSK-0374: implement versioned device/service content delivery`.
- Accepted PR head: `daf5b621ded4887a7ad6d1282223c1685bca9d20`.
- Canonical source merge: `6abe13a00fc2c906e0f9d592dd5383da008298c0`.
- Canonical source-merge tree: `907c9ccfe935edb6423799d796eedb570396151d`.
- Current machine catalogue consumed by the source contract: `content/TSK-0323/CATALOGUE.json`, blob `79753cc4916d38ed8d2f0ed6d01890e62df3fb04`.
- Current instruction bindings consumed by the source contract: blob `32441b56f5b2daf2c9924584685fd35fb416438e`.

The merged source provides a thin source-backed versioned delivery layer with deterministic Android/iPhone/common selection, exact release/provenance/integrity metadata, fail-closed stale/withdrawn/malformed/missing/unsupported/integrity-error handling, localized safe recovery, and rollback-capable known-release pinning. It introduces no remote CMS/fetch, persistence, identity, analytics, or browser-facing AdGuard administration.

## Source verification evidence

- Clean-main workflow run: `33743013472` — **SUCCESS**.
- Clean-main acceptance job: `100609046721` (`accept-tsk0374`) — **SUCCESS**.
- Exact tested source commit: `6abe13a00fc2c906e0f9d592dd5383da008298c0`.
- Acceptance workflow blob: `0a514634b96128e3fc4b0e0f2a2c7cf4efa6c056`.
- The clean-main source acceptance executed repository/Master-Plan validation, locked dependency installation, focused TSK-0374 contract coverage, the full current website contract suite, lint, typecheck, production build, dependency audits, diff/clean checks, and emitted the TSK-0374 source-acceptance PASS marker.

The source-merge history also retains test-first diagnostic evidence: the initial RED/GREEN cycle and a review-driven RED/GREEN correction occurred before the accepted source head. Those source cycles do not substitute for target-environment `VER-0374`.

## Remaining acceptance gap

The following required target evidence has **not** been established by this source publication:

- target functional verification;
- target negative/failure verification;
- target configuration verification;
- target security/privacy verification;
- an actual target rollback drill and rollback result.

Until those applicable checks are executed and durably evidenced, `TSK-0374` remains TODO and cannot satisfy downstream hard dependencies that require its PASS.

## Preserved material-action fences

This evidence authorizes or proves none of the following: deployment; participant processing; telemetry/analytics activation; profile/runtime activation; market or launch activation; lifecycle-gate PASS; `TSK-0374` PASS; `TSK-0499` PASS; downstream task PASS; public/production target acceptance; or new spend/contract/legal approval.

Any later consequential target action must independently satisfy its current gate, Action Authority, security/privacy/legal/technical constraints, reversibility/idempotency requirements, and target-evidence contract.

## Publication rule

This file and the minimal `CURRENT_STATE.md` synchronization are the only intended canonical publication changes. Exact publication commit/tree/blob identities are established only by post-merge canonical GitHub read-back; they are not self-referentially guessed here.
