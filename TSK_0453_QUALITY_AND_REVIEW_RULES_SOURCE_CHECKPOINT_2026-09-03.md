# TSK-0453 — Quality and Review Rules Source Checkpoint

Date: 2026-09-03
Task: `TSK-0453 — Configure formatting, linting, type checking, commit/change, and code-review rules`
Acceptance: `ACC-0453 / VER-0453 / EVD-0453`
Action authority: `A3 / AUTO_ALLOWED`
Stable disposition: **WAITING — SOURCE/POLICY IMPLEMENTATION VERIFIED; CRITICAL-PATH REVIEW ENFORCEMENT NOT PROVEN**

## Authority and dependency

- Canonical WBS blob: `eb35f3b10356396c5117e3f47d0b0378953e2157`.
- Hard predecessor: `TSK-0380`, current durable PASS before this execution.
- Canonical source merge commit: `b1f3fcad1265b40b5d5b414bb4c31d1f7bad80c2`.
- Canonical source tree: `7d5907146ba63b58d3309cdd6b782853ff55fe3f`.
- Source PR: `#89`, final exact head `b4fc1246d2fbff201cc067fee6b4a543509bc962`, squash-merged with expected-head guard.
- Preserved unrelated fence: PR `#86` remains draft and unmerged; no TSK-0417 real-target action is inferred.

## Verified source/policy controls

Canonical `main` now contains:

- `.github/CODEOWNERS`, blob `0309559dac23702a37e132e70dd17e63b4dfcbee`, assigning explicit owner review routing for `.github`, `Plans/Master`, `CURRENT_STATE.md`, `infrastructure`, website API routes, and the iOS DoH profile implementation.
- `.github/CHANGE_REVIEW_POLICY.md`, blob `47c05655d5381feddabc8f4675c09ff042498582`, requiring deterministic local/CI checks, generated/configuration impact review, and explicit narrow time-bounded exceptions.
- `.github/workflows/accept-tsk0453-quality-review-rules-20260903.yml`, blob `a0a117112aa9153c6bb6695a01f8510631bb585e`, running on pull requests and `main`, with read-only contents permission, clean install, exact Prettier version check, formatting/lint/type/contracts/build/audits, and a negative formatting-failure/rollback probe. It contains no deploy, Wrangler, or production action.
- `website/package.json`, blob `f725be68a7edf82b83620beaf3bb00980bec5f58`, with `npm@10.9.8`, exact `prettier@3.9.6`, `format`, `format:check`, lint/typecheck, and the focused TSK-0453 contract registered.
- `website/package-lock.json`, blob `6ff91d845bc5f3099b6a00f5f43673eed80a3ba5`, deterministically updated for the formatter baseline.
- `website/tests/contract/tsk0453.test.mjs`, blob `6c51a2e69c3912d616aceaec5e776ec8539c8955`, proving source-level formatting, review ownership, generated/configuration coverage, bounded exceptions, and non-deploying CI triggers.

The one-time formatter baseline was produced mechanically with pinned Prettier `3.9.6`; inherited behavior was then independently exercised by all current website acceptance workflows, including browser-heavy suites.

## RED → GREEN evidence

- RED run/job `33755212839 / 100647896639`: expected failure on all four missing controls only; canonical planning validation passed.
- Final branch source gate `33755786032 / 100649749364`: SUCCESS after exact formatter baseline, focused contract, format/lint/type/full contracts/build/audits, deliberate formatter failure propagation, rollback, and clean-worktree checks.
- Final PR-head TSK-0453 run/job `33757539847 / 100655477984`: SUCCESS on exact head `b4fc1246d2fbff201cc067fee6b4a543509bc962`.
- PR-head inherited regression matrix: **11/11 SUCCESS** — `33757540098` TSK-0375; `33757539919` TSK-0360; `33757539847` TSK-0453; `33757539865` TSK-0380; `33757539927` TSK-0369; `33757539915` TSK-0376; `33757539873` TSK-0374; `33757539895` TSK-0499; `33757539852` TSK-0243; `33757539977` TSK-0629; `33757539850` TSK-0359.
- Canonical clean-main TSK-0453 run/job `33758148342 / 100657497458`: SUCCESS on exact merge commit `b1f3fcad1265b40b5d5b414bb4c31d1f7bad80c2`.
- Canonical clean-main inherited regression matrix: **11/11 SUCCESS, zero failures** — `33758148340` TSK-0375; `33758148354` TSK-0360; `33758148342` TSK-0453; `33758148381` TSK-0380; `33758148364` TSK-0369; `33758148408` TSK-0376; `33758148378` TSK-0374; `33758148346` TSK-0499; `33758148380` TSK-0243; `33758148480` TSK-0629; `33758148437` TSK-0359.

No stale lockfile guard was weakened: nine inherited workflows were rebound from the former exact lock blob to the new accepted exact lock blob, while their tests and acceptance logic remained intact.

## Unresolved acceptance boundary

`ACC-0453` requires that **critical paths require review**. Source policy and CODEOWNERS metadata alone do not prove merge-blocking enforcement.

Current canonical GitHub read-back for `main` after source merge reports:

- `protected=false`;
- protection `enabled=false`;
- required-status-check enforcement `off`.

The repository rulesets endpoint is not readable through the current integration/plan and returned HTTP 403, so absence of repository rulesets is **not** inferred. Independently, PR #89 was successfully merged without an approving Code Owner review, so effective critical-path Code Owner approval was not proven as a mandatory merge condition for this execution path.

Current official GitHub documentation confirms the required mechanism:

- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners — requiring Code Owner approval is configured through branch protection by enabling `Require review from Code Owners`; rulesets are an alternative enforcement mechanism.
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule — protected branches can require pull requests, approvals, Code Owner review, and required status checks before merge.

Therefore `TSK-0453` is **WAITING**, not PASS.

### Deterministic resolution condition

Re-evaluate TSK-0453 only when GitHub repository controls can be configured and read back so that `main` demonstrably enforces, for the intended actors and without an unapproved bypass:

1. pull request review for critical CODEOWNERS paths;
2. Code Owner approval as a required merge condition;
3. the intended TSK-0453 quality/status checks as required where applicable;
4. a negative merge/bypass test or equivalent authoritative settings read-back proving the controls cannot be silently bypassed under ordinary governed execution.

Then rerun `VER-0453` against the exact repository configuration and only mark PASS if every applicable `ACC-0453` clause is durably proven.

## Non-inference and preserved fences

This source checkpoint and WAITING disposition do not deploy anything, touch a live device, remove/revoke a profile or service, process participants, activate telemetry, activate production/public service, launch, or create any new service-revocation interface/authority. They do not mark `TSK-0374`, `TSK-0417`, or `TSK-0499` PASS, and they do not make blocked real-target TSK-0417 progression whole-project completion.
