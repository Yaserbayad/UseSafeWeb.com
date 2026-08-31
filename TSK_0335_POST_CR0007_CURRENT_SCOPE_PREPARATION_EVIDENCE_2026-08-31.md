# TSK-0335 — Post-CR-0007 Current-Scope Preparation Evidence

**Task:** TSK-0335 — Design Protection Map and coverage-limit interactions  
**Acceptance:** ACC-0335  
**Verification:** VER-0335  
**Evidence:** EVD-0335 preparation / HUMAN_ONLY boundary  
**Date:** 2026-08-31  
**Disposition:** WAITING — exact current-scope amendment verified; Project Owner approval required

## 1. Current task contract

Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c` defines TSK-0335 as L4 / MEDIUM, dependency `TSK-0330`, A1 / `HUMAN_ONLY`, with `ACC-0335 / VER-0335 / EVD-0335`.

ACC-0335 remains:

> Prototype never labels parent confirmation as verification, exposes material gaps at the right time, supports deterministic internal/automated truth-state checks, and preserves the interaction points needed for later L8 human comprehension validation.

Dependency TSK-0330 is now current-qualified PASS under its post-CR-0007 revalidation.

## 2. Historical owner-approved base

The Project Owner previously approved:

`APPROVE TSK-0335 PROTECTION MAP COVERAGE-LIMIT INTERACTIONS`

at `2026-08-30T09:01:35Z` for exact base candidate:

- `design/TSK-0335/PROTECTION_MAP_COVERAGE_LIMIT_INTERACTIONS_CANDIDATE.md`, blob `7c65a697a98961d0df278658e59262ce39874ff5`.
- Historical preparation evidence blob `27fd622b84351c2eb6690167f7d6dd59b9dd5549`.
- Historical final acceptance evidence blob `0d1c67746dd2d12c397fae306f9f842d9ae4db25`.
- Historical final owner-bound run/job `33303080298 / 99234682891`: SUCCESS.

That approval remains valid for unchanged Protection Map semantics, but it cannot by itself approve the later CR-0006/CR-0007 optional-dashboard scope amendment.

## 3. Current-scope amendment candidate

Prepared amendment:

- `design/TSK-0335/POST_CR0007_DUAL_MODE_PROTECTION_MAP_AMENDMENT_CANDIDATE.md`
- version `1.0.0-post-cr0007`
- blob `80db66d9261e6ccf85e0253530819ad262b39497`

The amendment preserves the historical six-state evidence map and explicitly supersedes only stale product-scope assumptions, principally the old whole-product `no persistent dashboard` boundary and old visible `SafeWeb` naming.

Current dual-mode additions require:

- the same Protection Map truth model in accountless core and optional signed-in dashboard/device-detail contexts;
- saved record/account/session/dashboard presence never establishes S1 `Verified`;
- stored/earlier results are not silently treated as current;
- current S1 still requires current qualifying technical evidence;
- provider/session/account failure is account-only and does not rewrite physical protection truth;
- no automatic J0/J1 import/promotion from sign-in or device saving;
- logout, unlink/revoke, record deletion, account deletion, J0/J1 deletion and physical DNS removal remain distinct;
- physical `Removed` requires owning physical-removal evidence;
- no browsing/query/activity history, child profiles, raw DNS logs, unrestricted administration or broad per-domain controls;
- no overall safety score/certification;
- full accountless Protection Map/help/recovery remains available without login.

Eight deterministic current-scope cases `TC-0335-17..24` extend the historical `TC-0335-01..16` matrix without replacing it.

## 4. Current source alignment

Pinned current sources used by the verifier include:

- current TSK-0328 IA blob `527436958a1cd75fc91057410f4347ad56a3f53a`;
- current TSK-0332 dashboard prototype blob `7b19f726fefd4675f55fcad2ffb5fbf4e1c4aa2d`;
- current TSK-0334 account/dashboard support amendment blob `de423bdb8aeb2b0a0f25a85850be380cfab7e67d`;
- current TSK-0331 dependency-complete corrective evidence blob `3c128d430d2d31998f2e637a292a46ed740464e6`;
- current relationship graph blob `c108d2c162bcea2ee4cc01def46d0487a9501032`;
- pre-preparation runtime blob `f1c209ffd4e6816ca115ca71a3353291bd036f7c`.

## 5. Deterministic preparation verification

Workflow run/job `33430327495 / 99613846431` completed **SUCCESS** on self-hosted `adguardvm`.

Observed markers:

- `TSK0335_EXACT_INPUT_BLOBS=PASS`
- `TSK0335_CURRENT_WBS_CONTRACT=PASS`
- `TSK0335_GRAPH_CONTRACT=PASS`
- `TSK0335_DEPENDENCY_AND_HUMAN_BOUNDARY=PASS`
- `TSK0335_HISTORICAL_TRUTH_CONTRACT=PASS`
- `TSK0335_DUAL_MODE_AMENDMENT=PASS`
- `TSK0335_PRIVACY_ACCESSIBILITY_FENCES=PASS`
- `TSK0335_CURRENT_SOURCE_ALIGNMENT=PASS`
- `TSK0335_PREPARATION_VERIFICATION=PASS`

The workflow also passed `git diff --check` and clean-worktree verification.

## 6. Human decision boundary

TSK-0335 remains **WAITING / non-PASS** because the current WBS Action Authority is `HUMAN_ONLY` and the current-scope amendment changes the previously approved accountless-only scope interpretation.

Recommended exact Project Owner approval:

`APPROVE TSK-0335 POST-CR-0007 DUAL-MODE PROTECTION MAP AMENDMENT`

Alternative:

`REVISE TSK-0335: <specific change>`

No current TSK-0335 PASS, TSK-0333 eligibility, LG-06 PASS, implementation, real-user validation or launch authority is inferred before explicit owner approval and final owner-bound acceptance verification.
