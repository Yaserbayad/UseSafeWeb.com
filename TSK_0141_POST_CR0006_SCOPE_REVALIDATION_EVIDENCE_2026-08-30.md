# TSK-0141 — Post-CR-0006 Scope Revalidation Evidence

**Date:** 2026-08-30  
**Task:** TSK-0141 — Freeze minimum product scope and non-goals  
**Acceptance:** ACC-0141  
**Verification:** VER-0141  
**Evidence:** EVD-0141  
**Action authority:** A3 / AUTO_ALLOWED  
**Disposition:** PASS evidence subject to canonical runtime reconciliation/read-back

## Decision

DEC-0053 / CR-0006 invalidated the account-exclusion clauses in the earlier TSK-0141 scope artifact. The current Version-1 scope is now supplied by the already-accepted `TSK_0146_VERSION_1_OPTIONAL_ACCOUNT_PRODUCT_BASELINE_2026-08-30.md`; a duplicate product-scope artifact is intentionally not created.

The older `TSK_0141_PROVISIONAL_MINIMUM_PRODUCT_SCOPE_AND_NON_GOALS_2026-08-28.md` remains historical evidence only for compatible scope such as the first-phone job, accountless core, non-surveillance boundary, truthful Protection Map, recovery, accessibility/localization direction and no-behavioral-validation claim. Its statements that accounts/Google sign-in/dashboard are deferred are superseded.

## Source bindings

- current WBS: `3bb1598a6233a2bbefa52c746a7621867c6c6e89`
- decisions: `9cb2908f4c6f19cb38fce4a8aff71abca3b7b095`
- runtime prestate: `6731369b823c9a3b4c8c5b344ad67b990b68850a`
- historical TSK-0141 artifact: `c72bfd906fdca4a106dcd7d4ff458a2577e32c90`
- current Version-1 product baseline: `TSK_0146_VERSION_1_OPTIONAL_ACCOUNT_PRODUCT_BASELINE_2026-08-30.md`, blob `9d3870d90add696fc352829fb4763c834b8d09af`
- current TSK-0146 evidence: `TSK_0146_VERSION_1_OPTIONAL_ACCOUNT_PRODUCT_BASELINE_EVIDENCE_2026-08-30.md`, blob `b785c4a52217b24cf6eb9f66dce0773ddef7a639`

Current runtime independently records TSK-0139 PASS, satisfying TSK-0141's hard dependency.

## ACC-0141 mapping

- Every included capability remains mapped to current owner authority, mandatory safety/operation needs, or an explicitly provisional current-need assumption.
- Version 1 now **includes optional parent accounts plus lightweight dashboard/device management**.
- The complete core setup/protection journey remains usable without login.
- Mandatory login remains excluded absent a later owner decision.
- Browsing/activity/DNS-query history, child accounts/profiles and unrestricted DNS administration remain excluded/prohibited.
- No capability is represented as behaviorally/user validated before the controlled integrated-product pilot in L8 after LG-09.
- RSK-0002 remains OPEN and is not converted into evidence.

**ACC-0141: PASS.**

## Deterministic verification

Workflow: `Verify TSK-0141 post-CR-0006`  
Workflow commit: `0819051d0540285bed258fd8c6c90a06f6dea185`  
Run/job: `33308167888 / 99248297105`  
Runner: self-hosted `adguardvm`  
Conclusion: **SUCCESS**

Observed outputs:
- `TSK0141_DEPENDENCY=PASS`
- `TSK0141_STALE_PRECR0006_SCOPE_DETECTED=PASS`
- `TSK0141_CURRENT_SCOPE_MAPPING=PASS`
- `TSK0141_ACC0141=PASS`
- `TSK0141_NO_BEHAVIORAL_INFERENCE=PASS`
- `TSK0141_VERIFICATION=PASS`

## Residuals / non-inference

This PASS is an L4 scope freeze only. It does not approve the detailed account requirements, persistent schema, vendor/security/privacy architecture, account UX/prototype, implementation, LG-06, participant processing, release, payment or launch. Those remain controlled by their own tasks and gates.

**TSK-0141 is evidence-ready for current runtime PASS.**
