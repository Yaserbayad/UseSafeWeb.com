# TSK-0328 — Post-CR-0007 Reopen Evidence

**Task:** TSK-0328 — Define information architecture and navigation model  
**Date:** 2026-08-31  
**Disposition:** TODO / REOPENED FOR CURRENT ACCEPTANCE

## Current contract

Fresh deterministic inspection of current GitHub authority confirmed:

- lifecycle: `L4`
- priority: `MEDIUM`
- hard dependencies: `TSK-0325; TSK-0315`
- acceptance / verification / evidence: `ACC-0328 / VER-0328 / EVD-0328`
- capability / authority: `A3 / AUTO_ALLOWED`
- requirement references: `REQ-0028; REQ-0029; CON-0010; CON-0017`
- interfaces: `INT-0009; INT-0010`

Current ACC-0328 requires an architecture that supports the accountless core plus optional account sign-in/return/dashboard/account lifecycle, avoids unnecessary gated steps, keeps login optional for core value, and maps each screen to a user goal and requirement.

## Dependency result

Both hard dependencies are current durable PASS in `CURRENT_STATE.md`:

- TSK-0315 — current post-CR-0007 dual-mode end-to-end service blueprint.
- TSK-0325 — current post-CR-0007 parent journey/service blueprint.

## Why the historical TSK-0328 PASS is stale

The existing `prototype/TSK-0328/INFORMATION_ARCHITECTURE_NAVIGATION.md` is version `1.0.0` and explicitly defines an accountless-only architecture. It says, among other things:

- the IA has no Login, Sign up, Account or Dashboard;
- no Login/Dashboard/Account navigation item exists;
- the operational setup system does not become an account dashboard.

Those exclusions conflict with the current CR-0006/DEC-0053 Version-1 scope and current ACC-0328, which require optional account sign-in/return/dashboard/account-lifecycle navigation while preserving the complete login-free core.

Therefore the historical artifact and its historical PASS remain evidence only for still-compatible accountless/public/setup structure; they cannot satisfy current ACC-0328 as a whole.

## Inspection evidence

GitHub Actions run/job `33406511402 / 99535321940` on self-hosted `adguardvm` completed SUCCESS and emitted:

- `TSK0328_WBS_CURRENT_CONTRACT=PASS`
- `TSK0328_DEPENDENCIES_CURRENT_PASS=PASS`
- `TSK0328_HISTORICAL_ARTIFACT_STALE_UNDER_CR0006=PASS`
- `TSK0328_REOPEN_DISPOSITION=TODO`

The inspector did not modify the WBS, runtime, or TSK-0328 artifact.

## Current disposition

TSK-0328 is **reopened as TODO** for an independent current rebuild/revalidation. No TSK-0328 PASS is inferred.

The rebuild must preserve compatible public/setup structure while adding only the currently authorized optional account/session/dashboard/device/account-lifecycle architecture and continuing to prohibit mandatory login for core value, browsing/query/activity history, child accounts/profiles, and raw/unrestricted AdGuard administration.

This reopen does not infer TSK-0329, LG-06, implementation, build, launch, or behavioral-validation PASS.
