# TSK-0369 — Minimal support capture source implementation evidence

**Evidence ID:** EVD-0369 source-implementation partial
**Date:** 2026-09-03
**Task runtime disposition:** TODO — source implementation verified; target-environment verification incomplete
**Acceptance authority:** ACC-0369 / VER-0369 / EVD-0369

## Decision

The default-disabled TSK-0369 source implementation is accepted as durable partial evidence only. It is not task PASS. `VER-0369` requires target-environment functional, negative, configuration, security/privacy and rollback evidence that is not supplied by source/CI checks.

## Canonical implementation

- PR: #80
- Accepted feature head: `ec644b20672094b126e2a4233277975fe23806c0`
- Canonical squash merge: `f353e557438ec31f4967fd1bda961e1d95a8f4bb`
- Canonical merge tree: `f2c18ea9cf1d96f519e04cff4332f9d1db0494e5`
- `website/src/lib/support-capture.ts`: `b8ca3edd73a8c517e46cc9acf132acd9859e759c`
- `website/src/app/api/support-capture/route.ts`: `185655fbccf85f0d2e5e5048143c3cfb483735b2`
- `website/tests/contract/tsk0369.test.mjs`: `4a37c7c16dce3f440869efd8ba99f348ee546688`
- `website/package.json`: `32dd6e912f4fddce22565a09982dac9b74b15053`
- `.github/workflows/accept-tsk0369-minimal-support-capture-20260903.yml`: `81709a917f0f667c719b94f4edcbdf2963a2d0d7`

## TDD and review evidence

- Initial RED: run/job `33736223901 / 100587287332`; repository and Master-Plan validators passed, then the six focused tests failed because the implementation did not yet exist.
- Review RED: run/job `33736767793 / 100589069932`; the added default-off activation-fence expectation failed before the route correction.
- Accepted feature-head GREEN: run/job `33736797686 / 100589165631` on exact head `ec644b20672094b126e2a4233277975fe23806c0`.
- Clean-main GREEN: run/job `33737232323 / 100590559641` on exact canonical merge `f353e557438ec31f4967fd1bda961e1d95a8f4bb`.

Clean-main TSK-0369 evidence: focused 6/6; full website contracts 80/80; repository structure and Master-Plan validators PASS; 641 tasks, 858 dependency edges, 4,587 relationship entities, 18,152 relationship targets, 0 broken links and 0 generated missing task IDs; lint zero errors with one inherited non-error warning; typecheck PASS; production build PASS; both dependency audits 0 vulnerabilities; final marker `TSK0369_MINIMAL_SUPPORT_CAPTURE_ACCEPTANCE=PASS`.

## Inherited clean-main regressions

All are terminal-success on canonical merge `f353e557...`:

- TSK-0360 delivery: `33737232387 / 100590559469`
- TSK-0243 DNS verification, including real-browser acceptance: `33737232369 / 100590560009`
- TSK-0375 intake routing: `33737232393 / 100590559433`
- TSK-0359 localization/accountless browser acceptance: `33737232419 / 100590559664`
- TSK-0629 automated checks: `33737232430 / 100590559791`
- TSK-0376 accountless state machine: `33737232454 / 100590559762`

## Accepted source/data boundary

- New capture is disabled unless `USESAFEWEB_SUPPORT_CAPTURE_ENABLED=1`; this evidence does not enable it.
- POST uses bounded UTF-8 JSON and no-store responses; DELETE remains available while collection is disabled so prior deletion receipts are not stranded; there is no public GET/list route.
- Accepted input is categorical and exact-key only. Free text, identity, browsing/query/history fields and arbitrary fields are rejected.
- A false-positive report may include one normalized bounded hostname only; non-false-positive reports cannot include it. The aggregate metric projection removes the hostname.
- Records use a bounded in-memory store, opaque UUIDv4 deletion receipts and a non-sliding hard expiry of at most 24 hours; source contains no filesystem/local-storage/SQL persistence path.

## Remaining acceptance / non-inference

`ACC-0369` is not promoted to PASS because `VER-0369` requires target-environment execution. Remaining evidence includes authorized target deployment/enablement and target functional, negative, configuration, security/privacy and rollback verification, including runtime expiry/deletion, restart/process-topology behavior, concurrency/capacity/abuse behavior and direct inspection that forbidden persistence/logging is absent.

No deployment, runtime/production enablement, participant processing, analytics activation, market activation, launch, lifecycle-gate PASS, downstream task PASS or target acceptance is created or inferred by this evidence.

**Generated for guarded publication:** 2026-09-03T09:20:39Z
