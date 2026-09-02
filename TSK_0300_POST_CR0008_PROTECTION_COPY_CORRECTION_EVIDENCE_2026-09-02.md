# TSK-0300 — Protection-State Copy Correction Evidence — Post-CR-0008

**Task / Acceptance / Verification / Evidence:** TSK-0300 / ACC-0300 / VER-0300 / EVD-0300  
**Date:** 2026-09-02 UTC  
**Result:** PASS candidate for guarded runtime reconciliation; no successor or lifecycle-gate PASS inferred.

## 1. Immutable evidence index

- Canonical WBS blob: `b27a0c5df2f5636d8ed71051e9e26a68959a2616`.
- Canonical relationship-index blob: `c108d2c162bcea2ee4cc01def46d0487a9501032`.
- Pre-reconciliation runtime blob: `235cca98f7a3e1432b88e4581de5d0a80602195a`.
- Correction revalidation artifact: `TSK_0300_POST_CR0008_PROTECTION_COPY_CORRECTION_REVALIDATION_2026-09-02.md`, blob `172e4b82c7c106c48291c6a6a75aca6848ca4d0c`, publication commit `e9b04150de7c053d919493fba9eb296eed9b4430`.
- Corrected shared-system README: `brand/system/TSK-0300/README.md`, blob `a54a2b653720160261b034149cadff62bc399102`, correction commit `7246b9bf4ad93d5467abcd4959d2f503ad9e3b7c`.
- Corrected status reference: `brand/system/TSK-0300/templates/status.html`, blob `8f9971edfc87b2da8174330b9b4be68338a96fb4`, correction commit `97ef01c8a0dd0143378eeb4a0ef32b756fe19417`.
- Current TSK-0299 semantic owner: `TSK_0299_POST_CR0008_DUAL_MODE_VERBAL_SYSTEM_2026-09-01.md`, blob `ff30500b933b9ecc92325659d49ea4e671d296d2`.
- Current TSK-0320 semantic owner: `TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md`, blob `bdc6bacc424669708f410466f3cfd5527f1c2b3c`.
- Independent verifier script: `.github/scripts/verify_tsk0300_copy_correction.py`, blob `154f84b453694861f58df1a5dcf19ea372644fb5`.
- Independent read-only workflow: `.github/workflows/verify-tsk0300-copy-correction.yml`, blob `85278743149c6017f7ea0d4ad899c4094d0f3249`.
- Diagnostic PR: `#45`; trigger-only branch `diag/tsk0300-copy-correction`.
- Independent run/job: `33592292946 / 100128578252`, conclusion **SUCCESS**.

## 2. Current-contract verification

The verifier reparsed the canonical WBS and proved:

- TSK-0300 is L4 / HIGH / A3 / AUTO_ALLOWED;
- dependency is exactly TSK-0301;
- ACC/VER/EVD IDs are ACC-0300 / VER-0300 / EVD-0300;
- acceptance still requires public/product/help/status/partner/social references, one token source, implementation values and accessibility states.

It also proved durable PASS support for TSK-0301 plus current TSK-0299 and TSK-0320 support.  
**Result: PASS.**

## 3. Protection-state contradiction resolution

The current semantic owner TSK-0320 requires the six primary labels:

1. `Protection verified`;
2. `Setup confirmed`;
3. `Action needed`;
4. `Not covered`;
5. `Protection status could not be verified`;
6. `Removed`.

S2 additionally requires `Protection has not yet been technically verified.`

The independent verifier proved both the corrected README canonical-state section and corrected status template contain the current labels/S2 limitation, and the stale historical primary labels are no longer presented as the current canonical/reference labels. The status template also keeps explicit evidence/limitation text and non-color-only presentation.  
**Result: PASS.**

## 4. Preservation verification

The independent verifier hash-locked and proved unchanged:

- `tokens.css` `cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f`;
- `components.css` `831e92a74b6dda04252d93242cb33bd491a02381`;
- public reference `309f6a1f38474f78cd8a241aad3028fd495f9b8e`;
- product reference `872920b6f7af6561a1015e1d8fea55dcf95f1249`;
- help `3193c0d1e11367204d6c46fd862fec5a91245b64`;
- partner `03bb1fd67b9a9824bc856d1f312977d7767619a8`;
- social `cabdd12851fce1dbd5a3c6326ec6dec63f843958`;
- TSK-0301 identity README `b8ffd2ed234465a238558a7b94e56274de49696a`;
- primary/inverse/monochrome/monogram masters `f93958e3e4a16f9056693072c1b9b8b31fcda852` / `c38709e4239a2d36b340b4d9d630df85a17bb494` / `ef9b6e0d52926f24c7e81bccb4489569067b852f` / `49f20bae1d92bb04f125e988cb4cc3ea8a822b9e`.

Exactly six reference templates remain and each consumes the shared token/component layer and TSK-0301 identity authority. No remote script/style URL was introduced and no font binary is tracked.  
**Result: PASS.**

## 5. Dual-mode/current-scope verification

The public/product references still prove:

- primary accountless `Start setup` / `Finish without account` paths;
- optional `Sign in / Manage devices` / `Sign in to manage devices` continuity;
- no automatic anonymous J0/J1 import/linkage;
- account/session/dashboard/device presence is not protection verification.

The correction therefore preserves current CR-0006 dual-mode scope rather than reverting to accountless-only semantics.  
**Result: PASS.**

## 6. Independent execution result

Read-only GitHub-hosted run `33592292946`, job `100128578252`, completed **SUCCESS** with all explicit markers:

- `TSK0300_COPY_INPUT_HASHES=PASS`
- `TSK0300_COPY_WBS_CONTRACT=PASS`
- `TSK0300_COPY_PREDECESSOR_SUPPORT=PASS`
- `TSK0300_COPY_CURRENT_SEMANTIC_OWNERS=PASS`
- `TSK0300_COPY_STATE_REFERENCE=PASS`
- `TSK0300_COPY_SIX_CONTEXTS=PASS`
- `TSK0300_COPY_DUAL_MODE_REFERENCE=PASS`
- `TSK0300_COPY_NO_FONT_BINARIES=PASS`
- `TSK0300_COPY_PRESERVATION_FENCE=PASS`
- `TSK0300_COPY_ACC=PASS`
- `TSK0300_COPY_VER=PASS`
- `TSK0300_COPY_EVD_READY=PASS`
- `TSK0300_PROTECTION_COPY_CORRECTION=PASS`

The workflow had `contents: read` and could not mutate canonical project state.

## 7. Disposition

**ACC-0300 = PASS. VER-0300 = PASS. EVD-0300 = SATISFIED** for the corrected current L4 shared-brand-system acceptance boundary, pending guarded runtime synchronization and exact read-back.

This evidence does not implement or deploy a product, change owner-approved identity, activate auth/persistence, authorize participant/publication/payment/market/production/launch work, pass a lifecycle gate, or infer any successor PASS. Because TSK-0310 directly depends on TSK-0300, TSK-0310 must receive a current predecessor/materiality refresh after this corrected TSK-0300 state is durably reconciled.
