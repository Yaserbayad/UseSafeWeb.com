# TSK-0335 — Post-CR-0007 Deterministic Acceptance Evidence

**Task:** TSK-0335 — Design Protection Map and coverage-limit interactions  
**Acceptance:** ACC-0335  
**Verification:** VER-0335  
**Evidence:** EVD-0335 deterministic owner-bound acceptance  
**Date:** 2026-08-31  
**Final result:** PASS — pending guarded runtime reconciliation/read-back only

## 1. Exact authority and accepted objects

- Current WBS blob: `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`.
- Current relationship graph blob: `c108d2c162bcea2ee4cc01def46d0487a9501032`.
- Pre-acceptance WAITING runtime blob: `8f053c4c12a90c0c6e0646b824846bfbd6682935`.
- Historical owner-approved base: `design/TSK-0335/PROTECTION_MAP_COVERAGE_LIMIT_INTERACTIONS_CANDIDATE.md`, blob `7c65a697a98961d0df278658e59262ce39874ff5`.
- Current amendment: `design/TSK-0335/POST_CR0007_DUAL_MODE_PROTECTION_MAP_AMENDMENT_CANDIDATE.md`, blob `80db66d9261e6ccf85e0253530819ad262b39497`.
- Current preparation evidence: `TSK_0335_POST_CR0007_CURRENT_SCOPE_PREPARATION_EVIDENCE_2026-08-31.md`, blob `03e7a35b7943586d635975fdc9a53bfd0e99ee44`.
- Owner approval evidence: `TSK_0335_POST_CR0007_OWNER_APPROVAL_EVIDENCE_2026-08-31.md`, blob `f1b6dcaf10ee276593563e1adf732d305e5d5789`.
- Final verifier: `.github/scripts/verify_tsk0335_post_cr0007_final_acceptance_20260831.py`, blob `8b902e15e187e1a0142afb0c6da38dc4f2cf0d31`.
- Final workflow: `.github/workflows/verify-tsk0335-post-cr0007-final-acceptance-20260831.yml`, blob `990cfe9380f6a277299b6f915f0feb23223084a7`.

## 2. Owner authority

The Project Owner explicitly approved at `2026-08-31T19:30:51Z`:

`APPROVE TSK-0335 POST-CR-0007 DUAL-MODE PROTECTION MAP AMENDMENT`

The owner approval evidence binds that command to the exact base/amendment/preparation/runtime identities above.

## 3. Preparation proof

Preparation run/job `33430327495 / 99613846431`: **SUCCESS**.

It proved exact inputs, current WBS contract, graph contract, current TSK-0330 dependency, historical truth contract, dual-mode amendment semantics, privacy/accessibility fences and current-source alignment while preserving the HUMAN_ONLY non-PASS fence.

## 4. Final owner-bound verification

Final run/job `33431191778 / 99616661300`: **SUCCESS** on self-hosted `adguardvm`.

Observed final markers:

- `TSK0335_FINAL_EXACT_BLOBS=PASS`
- `TSK0335_FINAL_WBS_CONTRACT=PASS`
- `TSK0335_FINAL_GRAPH_CONTRACT=PASS`
- `TSK0335_FINAL_WAITING_PRECONDITION=PASS`
- `TSK0335_FINAL_OWNER_APPROVAL_BINDING=PASS`
- `TSK0335_FINAL_PREPARATION_EVIDENCE=PASS`
- `TSK0335_FINAL_ACCEPTANCE_CONTRACT=PASS`
- `TSK0335_FINAL_CURRENT_SOURCE_ALIGNMENT=PASS`
- `TSK0335_FINAL_PRIVACY_VALIDATION_FENCES=PASS`
- `TSK0335_POST_CR0007_FINAL_ACCEPTANCE=PASS`

The workflow also passed `git diff --check` and clean-worktree verification.

## 5. Current accepted semantics

The accepted Protection Map interaction contract now consists of the historical base plus the current dual-mode amendment. It preserves:

- strict technical `Verified` versus parent-confirmed distinction;
- immediate material-gap disclosure;
- independent Phone / Internet / Service layer truth;
- deterministic truth-state checks;
- no overall safety score/certification;
- later L8 comprehension hooks without fabricating L4 human evidence;
- full signed-out/accountless access to the core Protection Map/help/recovery path.

Current optional-dashboard additions require:

- account/session/dashboard/device-record presence never creates `Verified`;
- last-known/stored state is not automatically current;
- account/provider/session failures do not rewrite physical protection truth;
- no automatic J0/J1 import/promotion;
- logout, unlink/revoke, dashboard-record deletion, account deletion, J0/J1 deletion and physical DNS removal remain separate;
- physical `Removed` requires owning physical-removal evidence;
- no browsing/query/activity history, child profiles, raw DNS logs, unrestricted administration or broad per-domain controls.

## 6. Non-inference

This evidence proves TSK-0335 only. It does not prove TSK-0333, LG-06, L5 architecture/security/privacy/vendor acceptance, implementation, production behavior, real-user validation, publication or launch.

`RSK-0002` remains OPEN/non-blocking before L8.

## 7. Disposition

`ACC-0335 / VER-0335 / EVD-0335`: **CURRENT PASS**, subject only to successful guarded runtime reconciliation and GitHub read-back.
