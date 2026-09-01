# TSK-0318 — Post-CR-0008 Acceptance Evidence

**Task:** TSK-0318 — Design the public website IA and product/setup IA as distinct but connected systems  
**Acceptance / Verification / Evidence:** ACC-0318 / VER-0318 / EVD-0318  
**Lifecycle / Priority / Authority:** L4 / HIGH / A3 / AUTO_ALLOWED  
**Date:** 2026-09-01  
**Disposition:** PASS — subject to durable CURRENT_STATE.md synchronization and independent read-back

## 1. Why TSK-0318 was reopened

DEC-0053/CR-0006 changed Version-1 scope from the historical accountless-only IA assumption to a dual-mode product: complete accountless core plus optional parent account/session/lightweight dashboard/device management.

The historical TSK-0318 candidate was directly invalidated for current acceptance because it explicitly prohibited Login/Dashboard/Account surfaces and stated that no account/session lifecycle was introduced by navigation. Those clauses contradict the current product boundary.

Historical evidence is preserved for compatible facts; it is not erased or rewritten.

## 2. Exhaustive HIGH-L4/AUTO_ALLOWED validity reconciliation relevant to selection

Canonical read-only frontier audit used:

- WBS blob: `b27a0c5df2f5636d8ed71051e9e26a68959a2616`
- relationship graph blob: `c108d2c162bcea2ee4cc01def46d0487a9501032`
- pre-execution runtime blob: `c4594837623b2462fea250fb360aed8fcabc90f3`

The exact `Lifecycle_Stage=L4 + Priority=HIGH + Action_Authority=AUTO_ALLOWED` set contains 23 tasks:

`TSK-0147, TSK-0148, TSK-0149, TSK-0187, TSK-0229, TSK-0298, TSK-0299, TSK-0300, TSK-0301, TSK-0307, TSK-0308, TSK-0310, TSK-0311, TSK-0315, TSK-0316, TSK-0317, TSK-0318, TSK-0319, TSK-0327, TSK-0408, TSK-0409, TSK-0558, TSK-0628`.

Artifact-specific current-validity findings:

- `TSK-0229`: **current PASS**. Post-CR-0006 revalidation explicitly keeps J0/J1 anonymous/transient state separate from the optional persistent account domain; account activity cannot extend J1 and no automatic anonymous-to-account join is authorized.
- `TSK-0628`: **current PASS**. Its current post-CR-0006/0007 support model already includes sign-in/session, dashboard/device management and account/device lifecycle. Its hard dependencies TSK-0319 and TSK-0331 are current PASS after the TSK-0319 durable synchronization repair.
- `TSK-0299`: historical PASS **stale for current acceptance** because the accepted verbal artifact says not to imply an account/persistent device profile/activity dashboard exists. Current scope now includes optional account/dashboard/device continuity, while the accountless-core language remains compatible.
- `TSK-0316`: historical PASS **stale for current acceptance** because its friction budget models the accountless-only journey and does not challenge the newly approved optional sign-in/session/dashboard/device lifecycle. The prohibition on mandatory login before core value remains compatible.
- `TSK-0318`: historical PASS **stale for current acceptance** because the artifact directly prohibited Login/Dashboard/Account navigation and any account/session lifecycle.
- `TSK-0327`: retained current PASS; no current contradictory evidence was found against its internal/automated findings-disposition acceptance.

Selection rule application:

1. No higher safety/legal/security blocker distinguished the reopened L4 candidates.
2. TSK-0628 was eliminated from the open-winner comparison because it is already current PASS.
3. TSK-0299 and TSK-0316 require later current-scope requalification, but their immediate accepted downstream semantic owners — identity/visual system and platform install/verification/removal mechanics — remain materially usable under the optional-account activation and do not themselves own the missing account IA.
4. TSK-0318 owns the exact page/screen navigation boundary changed by CR-0006. Its own accepted artifact directly conflicts with the currently required optional sign-in/session/dashboard/device/account lifecycle and directly feeds the public-to-setup/localization experience chain.
5. Therefore the governing dependency-chain constraint plus customer-value rule selects **TSK-0318** before the other reopened stale artifacts. WBS/task-order tie-breaking is not reached because the material dependency/customer-surface contradiction is stronger for TSK-0318.

No task was marked PASS from this selection analysis alone.

## 3. Current artifact

Current candidate:

`TSK_0318_POST_CR0008_DUAL_MODE_PUBLIC_PRODUCT_SETUP_IA_2026-09-01.md`

- version: `2.0.0-post-cr0008`
- publication commit: `31cbd3af8175dd8c82d9e58828b6cf0ee4a1f168`
- blob: `975e2e7a8e85e9408e0bbbc2be226f3fdd012db3`

The artifact supersedes only account-exclusion-dependent current acceptance clauses. It preserves the historical artifact as evidence and preserves compatible accountless-core, public/product separation, privacy and recovery facts.

## 4. Current predecessor and authority basis

The verifier required the exact WBS contract:

- Lifecycle: L4
- Priority: HIGH
- AI capability: A3
- Action Authority: AUTO_ALLOWED
- hard dependency: TSK-0315
- ACC/VER/EVD: ACC-0318 / VER-0318 / EVD-0318

The direct predecessor `TSK-0315` is current PASS under the post-CR-0007 dual-mode service blueprint. Current runtime also contains the required supporting accepted states for TSK-0229, TSK-0331 and TSK-0319.

Current TSK-0315 artifact consumed by the IA:

- `TSK_0315_POST_CR0007_DUAL_MODE_END_TO_END_SERVICE_BLUEPRINT_2026-08-31.md`
- blob `97cf09f294c757f80ad5c0fbe6110ed8d471159c`

## 5. Independent deterministic verification

Verifier workflow:

- `.github/workflows/verify-tsk0318-post-cr0008.yml`
- publication commit: `20051481abea660a128252638b0c515eeff395ae`
- workflow blob: `dfd62f49e59117073bca809fca034a19c93d165e`
- permissions: `contents: read`
- checkout: current `main`
- runner: GitHub-hosted Ubuntu 24.04

Successful run/job:

- run: `33571019275`
- job: `100064770925`
- conclusion: **SUCCESS**

Observed verification output:

- `TSK0318_WBS_CONTRACT=PASS`
- `TSK0318_CURRENT_PREDECESSOR=PASS`
- `TSK0318_DUAL_MODE_SCOPE=PASS`
- `TSK0318_IA_MATRIX_ROWS=38`
- `TSK0318_SEO_PRIVACY_ACCESSIBILITY=PASS`
- `TSK0318_LIFECYCLE_SEPARATION=PASS`
- `TSK0318_SCOPE_NEGATIVES=PASS`
- `TSK0318_SUCCESSOR_IMPACT=PASS`
- `TSK0485_PRESERVED_INPUT=PASS`
- `TSK0319_PRESERVED_INPUT=PASS`
- `TSK0318_ACCEPTANCE=PASS`

Verified source identities in that run:

- artifact blob `975e2e7a8e85e9408e0bbbc2be226f3fdd012db3`
- WBS blob `b27a0c5df2f5636d8ed71051e9e26a68959a2616`
- graph blob `c108d2c162bcea2ee4cc01def46d0487a9501032`
- runtime input blob `c4594837623b2462fea250fb360aed8fcabc90f3`

## 6. ACC-0318 proof

The accepted candidate contains 38 unique page/screen matrix rows:

- 9 public website surfaces (P01–P09),
- 14 accountless product/setup surfaces (C01–C14),
- 15 optional parent-account/dashboard/device lifecycle surfaces (A01–A15).

For every row the verifier proved all ACC-0318 fields are present and non-empty:

- one purpose,
- primary entry,
- primary exit / next action,
- content owner,
- explicit SEO/index decision,
- privacy requirement,
- accessibility requirement.

The verifier additionally proved current-scope coverage and negative boundaries:

- complete accountless core without login;
- optional sign-in/session/dashboard/device management;
- safe accountless continuation on auth cancel/failure/provider outage;
- no automatic J0/J1-to-account linkage;
- separate logout/revoke/device-record delete/account delete/anonymous reset/physical DNS removal semantics;
- truthful Protection Map/current verification semantics;
- setup, verification, troubleshooting, reset, reinstall/reconfigure, removal, recovery, not-covered and uncertainty paths;
- no browsing/query/activity-history route;
- no child-account/profile route;
- no raw/broad DNS administration route;
- no payment gate before core value;
- no overall safety score/all-clear route;
- explicit NOINDEX rules for operational/account surfaces;
- keyboard/focus, semantic status/error and RTL/localization structure requirements.

## 7. Successor impact and preserved evidence

This PASS does **not** automatically reclassify any successor.

- Historical TSK-0310 evidence remains useful for the accountless public-to-setup core path; this acceptance does not claim it implements the optional account/dashboard branch.
- TSK-0311 retains its own localization/externalization acceptance boundary; newly implemented account/dashboard copy must independently use those mechanics.
- TSK-0299 and TSK-0316 remain separately reopened current-scope requalification candidates.
- TSK-0628 remains current PASS; no re-execution was required.

No LG-06/gate, architecture, authentication-provider, persistent schema, implementation, legal/privacy completion, participant, payment, production, publication, market or launch PASS is inferred.

## 8. Stable outcome before runtime synchronization

ACC-0318 / VER-0318 / EVD-0318 are independently proven **PASS** for the current dual-mode L4 IA design boundary.

The task must not be treated as durably synchronized runtime PASS until `CURRENT_STATE.md` is updated, written to GitHub, independently read back, and verified to preserve the existing TSK-0485 and synchronized TSK-0319 current PASS sections unchanged.
