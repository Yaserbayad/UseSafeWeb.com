# TSK-0334 — Post-CR-0007 Current-Scope Preparation Evidence

**Task:** TSK-0334 — Design support, false-positive, removal, and reconfiguration flows  
**Acceptance:** ACC-0334  
**Verification:** VER-0334  
**Evidence:** EVD-0334 preparation evidence only  
**Date:** 2026-08-31  
**Disposition:** WAITING FOR PROJECT OWNER APPROVAL — NOT PASS

## 1. Why the historical approval cannot be reused unchanged

The historical owner-approved TSK-0334 candidate remains valid for its five technical accountless support categories, but it explicitly treated an account system and persistent device identity as out of scope. DEC-0053/CR-0006 subsequently activated optional parent account/session/minimum device persistence/lightweight dashboard in Version 1. Current TSK-0329, TSK-0142 and TSK-0332 now require account/session/device-record support states. Therefore the historical approval cannot by itself prove current-scope ACC-0334.

## 2. Exact current candidate

- Historical base candidate: `design/TSK-0334/SUPPORT_FALSE_POSITIVE_REMOVAL_RECONFIGURATION_FLOWS_CANDIDATE.md`, blob `44fab92b51ae8ed8b6f5f325ba1558bcd297eb5f`.
- Current-scope amendment candidate: `design/TSK-0334/POST_CR0007_ACCOUNT_SUPPORT_LIFECYCLE_AMENDMENT_CANDIDATE.md`, version `1.0.0-post-cr0007`, blob `de423bdb8aeb2b0a0f25a85850be380cfab7e67d`.
- Current WBS blob: `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`.
- Pre-decision runtime blob: `f735ab7b68cd0231dc3515739992242d67f5193e`.
- Candidate verifier: `.github/scripts/verify_tsk0334_post_cr0007_candidate_20260831.py`, blob `0cb80a09ee765e266932a91e7b45b092bc7e7d13`.
- Verification workflow: `.github/workflows/verify-tsk0334-post-cr0007-candidate-20260831.yml`, blob `e1bdede89dc906e5adf60488155a9582228bb85e`.

## 3. Current-scope amendment

The five historical categories remain technically applicable:

- SUP-01 setup/verification troubleshooting;
- SUP-02 false positive;
- SUP-03 physical UseSafeWeb removal/connectivity recovery;
- SUP-04 reconfiguration/start again;
- SUP-05 unsupported/uncertain/limitations.

The amendment adds the three current Version-1 categories required by the optional-account/dashboard scope:

- SUP-06 account sign-in/session/provider access problems;
- SUP-07 saved-device record/ownership/unlink/dashboard-management problems;
- SUP-08 account/device deletion and uncertain lifecycle-result problems.

It preserves the accountless core and establishes that provider/account/session failures are account-only, ownership mismatch fails closed, destructive operations are not automatically replayed, uncertain results require authoritative resolution, and account/record/J0-J1/physical-protection lifecycles remain distinct.

## 4. Deterministic preparation verification

GitHub Actions run/job `33415828154 / 99566111401` completed **SUCCESS** on self-hosted `adguardvm`.

Observed markers:

- `TSK0334_WBS_HUMAN_BOUNDARY=PASS`
- `TSK0334_EIGHT_CATEGORY_COVERAGE=PASS`
- `TSK0334_CURRENT_SCOPE_SEMANTICS=PASS`
- `TSK0334_HUMAN_PASS_FENCE=PASS`
- `TSK0334_PREPARATION_VERIFICATION=PASS`

The workflow also passed `git diff --check` and clean-worktree verification.

## 5. Human authority boundary

Current WBS authority for TSK-0334 is `HUMAN_ONLY`. This preparation evidence proves the candidate is complete enough for the decision; it does **not** authorize acceptance.

The exact required owner decision is whether to approve the historical base candidate plus the current-scope amendment as the current TSK-0334 support-flow design. Approval would supersede only the old account/dashboard exclusions and add SUP-06/07/08; it would not approve provider/vendor/security/privacy architecture, implementation, live support operations, production deletion, TSK-0331, TSK-0333, behavioral validation or LG-06.

## 6. Queue consequence

TSK-0331 depends on `TSK-0332; TSK-0334`. TSK-0332 is current durable PASS. TSK-0334 remains non-current and WAITING for the owner decision above, so TSK-0331 is not eligible until that decision is explicitly made, persisted and read back.

**Final preparation disposition:** WAITING / HUMAN APPROVAL REQUIRED. No PASS is inferred.
