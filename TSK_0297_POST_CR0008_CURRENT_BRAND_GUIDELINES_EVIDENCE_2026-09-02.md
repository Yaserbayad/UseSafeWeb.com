# TSK-0297 — Current Brand Guidelines and Asset-Governance Evidence — Post-CR-0008

**Task / Acceptance / Verification / Evidence:** TSK-0297 / ACC-0297 / VER-0297 / EVD-0297  
**Date:** 2026-09-02 UTC  
**Result:** PASS candidate for guarded runtime reconciliation; no successor or lifecycle-gate PASS inferred.

## 1. Immutable evidence index

- Canonical WBS blob: `b27a0c5df2f5636d8ed71051e9e26a68959a2616`.
- Canonical relationship-index blob: `c108d2c162bcea2ee4cc01def46d0487a9501032`.
- Pre-reconciliation runtime blob: `f12f87cec9993f811d25d5f2f34b9996c4497c67`.
- Current guidelines: `brand/guidelines/TSK-0297/README.md`, version `2.0.0`, blob `e79121fd95932a6f4b2550f5f05b84c6e9c7aeac`, update commit `113f9de234f14f85b8d14a29e929e32bc565989d`.
- Current manifest: `brand/guidelines/TSK-0297/ASSET_MANIFEST.json`, blob `c31eb9674eee9cf330b1af4764088f51e9c398fe`, update commit `280f68a13e3d965887ae59edba66718c3d4c1c7f`.
- Current revalidation artifact: `TSK_0297_POST_CR0008_CURRENT_BRAND_GUIDELINES_REVALIDATION_2026-09-02.md`, blob `7e472d3373fa226584dcea358ed3215f40aa2e7b`, publication commit `2729255c22ddf8860ec6af43e59025eca47676e4`.
- Historical EVD retained as provenance: `TSK_0297_BRAND_GUIDELINES_EVIDENCE_2026-08-29.md`, blob `02b28f3f040d44e495ace63bf074535e4a4bd03d`.
- Current corrected TSK-0300 evidence: `TSK_0300_POST_CR0008_PROTECTION_COPY_CORRECTION_EVIDENCE_2026-09-02.md`, blob `a3e39896b67098ced321cb9e4b82c65c440806e4`.
- Current TSK-0299 dual-mode verbal system: `ff30500b933b9ecc92325659d49ea4e671d296d2`.
- Current TSK-0320 state/copy authority: `bdc6bacc424669708f410466f3cfd5527f1c2b3c`.
- Independent verifier script: `.github/scripts/verify_tsk0297_current_guidelines.py`, blob `ccdb8e65177777500cc2bbe80a68ebff0b3a6a49`.
- Read-only verifier workflow: `.github/workflows/verify-tsk0297-current-guidelines.yml`, blob `cd5bfb7b6bbb96b18a2ccdfc677787df056f11e2`.
- Diagnostic PR `#51`, branch `diag/tsk0297-current-guidelines`; PR changes only a trigger file.
- Independent run/job: `33594493974 / 100135082837`, conclusion **SUCCESS**.

## 2. Current WBS and predecessor proof

The verifier reparsed canonical WBS and proved TSK-0297 is:

- L4 / MEDIUM / A3 / `AUTO_ALLOWED`;
- hard dependency exactly `TSK-0300`;
- `ACC-0297 / VER-0297 / EVD-0297`;
- acceptance requires a human or AI to generate a compliant asset without guessing, deprecated assets to remain traceable, and no font files to be exposed as user deliverables.

The runtime parser independently bound TSK-0300 to its corrected current PASS section, including evidence blob `a3e39896b67098ced321cb9e4b82c65c440806e4`, independent run/job `33592292946 / 100128578252`, and `ACC-0300 = PASS. VER-0300 = PASS. EVD-0300 = SATISFIED.`

Markers:

- `TSK0297_CURRENT_WBS=PASS`
- `TSK0297_CURRENT_TSK0300_PREDECESSOR=PASS`

**Result: PASS.**

## 3. Package/version and source-currency proof

The verifier proved README/manifest agree on guideline version `2.0.0`, and the manifest retains v1 package blobs as superseded provenance rather than presenting them as current output authority.

It then parsed all currently selectable records across `authority_sources`, `identity_assets`, `implementation_sources`, and `surface_templates` and recomputed each path's Git blob from current `main`. All **18 selectable records** matched their manifest blobs exactly.

Markers:

- `TSK0297_CURRENT_PACKAGE_VERSION=PASS`
- `TSK0297_CURRENT_MANIFEST_ACTIVE_BLOBS=PASS`
- `TSK0297_CURRENT_SOURCE_UNCHANGED=PASS`

**Result: PASS.**

## 4. Authority supersession proof

The current package actively binds:

- current TSK-0300 README `a54a2b653720160261b034149cadff62bc399102`;
- current TSK-0300 correction evidence `a3e39896b67098ced321cb9e4b82c65c440806e4`;
- current TSK-0299 path/blob `TSK_0299_POST_CR0008_DUAL_MODE_VERBAL_SYSTEM_2026-09-01.md` / `ff30500b933b9ecc92325659d49ea4e671d296d2`;
- current TSK-0320 path/blob `TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md` / `bdc6bacc424669708f410466f3cfd5527f1c2b3c`.

The old TSK-0299/TSK-0320 files are absent from active authority selection and appear only in explicit supersession records. The old TSK-0300 README blob is likewise recorded only with its replacement. TSK-0298 is explicitly bounded to still-compatible brand-role/prohibited-expression principles and cannot override current CR-0005/6/7/8 authority.

Marker: `TSK0297_CURRENT_AUTHORITY_SUPERSESSION=PASS`.

**Result: PASS.**

## 5. Current surface and protection-copy proof

The six current active surface blobs were independently verified:

- public `309f6a1f38474f78cd8a241aad3028fd495f9b8e`;
- product `872920b6f7af6561a1015e1d8fea55dcf95f1249`;
- help `3193c0d1e11367204d6c46fd862fec5a91245b64`;
- status `8f9971edfc87b2da8174330b9b4be68338a96fb4`;
- partner `03bb1fd67b9a9824bc856d1f312977d7767619a8`;
- social `cabdd12851fce1dbd5a3c6326ec6dec63f843958`.

README and manifest now both represent current TSK-0320 primary copy:

1. `Protection verified`;
2. `Setup confirmed` plus `Protection has not yet been technically verified.`;
3. `Action needed`;
4. `Not covered`;
5. `Protection status could not be verified`;
6. `Removed`.

The historical primary labels are not used as active README state copy.

Markers:

- `TSK0297_CURRENT_SURFACE_BINDINGS=PASS`
- `TSK0297_CURRENT_PROTECTION_COPY=PASS`

**Result: PASS.**

## 6. Dual-mode/deterministic-generation proof

The verifier proved the package requires:

- complete accountless core without login;
- optional account continuity as non-coercive continuity, not stronger protection;
- account/device ownership not to become protection evidence;
- no automatic anonymous-to-account linkage;
- lifecycle operations to name exactly what they change;
- no browsing/query/activity history, child accounts or unrestricted customer DNS administration.

It also proved deterministic representative decisions exist for light public headers, small dark status/icon contexts, Arabic RTL, optional account/dashboard surfaces and lifecycle assets/copy, while preserving the same approved identity and shared TSK-0300 system.

Markers:

- `TSK0297_CURRENT_DUAL_MODE_BOUNDARY=PASS`
- `TSK0297_CURRENT_DETERMINISTIC_SELECTION=PASS`

**Result: PASS.**

## 7. Deprecation, provenance and no-font proof

The manifest's actual asset-state contract remains `ACTIVE` / `DEPRECATED`. Deprecated records must retain replacement, reason, deprecation date and authorizing commit/evidence; new selection and silent deletion are prohibited. Source-authority revisions are kept separately as superseded bindings so historical reconstruction does not make obsolete sources selectable.

The verifier proved the TSK-0297 package itself contains only `README.md` and `ASSET_MANIFEST.json`, forbids `.ttf`, `.otf`, `.woff`, `.woff2`, `.eot`, sets `deliver_font_binaries=false`, contains no selectable remote source, and exposes no selectable font binary.

Markers:

- `TSK0297_CURRENT_DEPRECATION_TRACE=PASS`
- `TSK0297_CURRENT_NO_FONT_DELIVERY=PASS`
- `TSK0297_CURRENT_LOCAL_SOURCE_LIBRARY=PASS`

**Result: PASS.**

## 8. Independent execution result

Read-only GitHub-hosted run/job `33594493974 / 100135082837` completed **SUCCESS** with all explicit verifier markers:

- `TSK0297_CURRENT_INPUT_HASHES=PASS`
- `TSK0297_CURRENT_WBS=PASS`
- `TSK0297_CURRENT_TSK0300_PREDECESSOR=PASS`
- `TSK0297_CURRENT_PACKAGE_VERSION=PASS`
- `TSK0297_CURRENT_MANIFEST_ACTIVE_BLOBS=PASS`
- `TSK0297_CURRENT_AUTHORITY_SUPERSESSION=PASS`
- `TSK0297_CURRENT_SURFACE_BINDINGS=PASS`
- `TSK0297_CURRENT_PROTECTION_COPY=PASS`
- `TSK0297_CURRENT_DUAL_MODE_BOUNDARY=PASS`
- `TSK0297_CURRENT_DETERMINISTIC_SELECTION=PASS`
- `TSK0297_CURRENT_DEPRECATION_TRACE=PASS`
- `TSK0297_CURRENT_NO_FONT_DELIVERY=PASS`
- `TSK0297_CURRENT_LOCAL_SOURCE_LIBRARY=PASS`
- `TSK0297_CURRENT_PRESERVATION_NONINFERENCE=PASS`
- `TSK0297_CURRENT_ACC=PASS`
- `TSK0297_CURRENT_VER=PASS`
- `TSK0297_CURRENT_EVD_READY=PASS`
- `TSK0297_CURRENT_GUIDELINES=PASS`
- `TSK0297_CURRENT_SOURCE_UNCHANGED=PASS`

The workflow had `contents: read` and could not mutate canonical project state.

## 9. Disposition

**ACC-0297 = PASS. VER-0297 = PASS. EVD-0297 = SATISFIED** for the current v2.0.0 L4 brand-guidelines/source-library/versioning/ownership/usage-governance acceptance boundary, pending guarded runtime synchronization and exact read-back.

No identity redesign, build/implementation, legal/privacy completion, real-user/native-speaker validation, publication/payment/market activation, production behavior, lifecycle-gate PASS, launch or successor PASS is inferred.
