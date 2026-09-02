# TSK-0311 — Current Dual-Mode Localization / Content Architecture Revalidation Acceptance Evidence

**Task:** TSK-0311 — Define translation keys/files, locale metadata, plural/date rules, content ownership, localized instruction variants, and fallback behavior  
**Acceptance / Verification / Evidence:** ACC-0311 / VER-0311 / EVD-0311  
**Lifecycle / Priority / Authority:** L4 / HIGH / A3 / AUTO_ALLOWED  
**Evidence date:** 2026-09-02 UTC  
**Disposition:** CURRENT PASS — subject only to guarded runtime reconciliation and exact GitHub read-back.

## 1. Current accepted artifact

- `TSK_0311_POST_CR0008_DUAL_MODE_LOCALIZATION_CONTENT_ARCHITECTURE_REVALIDATION_2026-09-02.md`
- version `2.0.0-post-CR0008`
- blob `4f702a61bfccad385be83c1a37a753cdeb1d8b43`
- publication commit `f47c8cddca8906cd4b78640de8f76065c4bc92fa`

The artifact preserves the historically accepted localization architecture and extends only the missing current optional account/session/dashboard/device-lifecycle surface inventory required by current TSK-0318.

## 2. Current WBS / predecessor proof

Independent VER-0311 proved:

- WBS `Plans/Master/WBS/master-wbs.csv` blob `b27a0c5df2f5636d8ed71051e9e26a68959a2616`;
- graph `Plans/Master/RELATIONSHIP_INDEX.yaml` blob `c108d2c162bcea2ee4cc01def46d0487a9501032`;
- pre-reconciliation runtime `CURRENT_STATE.md` blob `974c7e5ebdbf64e382d2d4075490567f11be6fff`;
- L4 / HIGH / A3 / `AUTO_ALLOWED`;
- hard dependency exactly `TSK-0318`;
- exact `ACC-0311 / VER-0311 / EVD-0311` binding;
- current TSK-0318 durable PASS.

Markers:
- `TSK0311_CURRENT_WBS=PASS`;
- `TSK0311_CURRENT_PREDECESSOR=PASS`.

Current predecessor artifact:
`TSK_0318_POST_CR0008_DUAL_MODE_PUBLIC_PRODUCT_SETUP_IA_2026-09-01.md` — blob `975e2e7a8e85e9408e0bbbc2be226f3fdd012db3`.

VER-0311 proved the current IA contains the optional public sign-in/manage-devices entry plus account sign-in/auth-result/dashboard/device/add/reverify/reinstall/replace/revoke/delete/account-deletion/session/accountless-fallback surfaces.

Marker: `TSK0311_DUAL_MODE_IA_INPUT=PASS`.

## 3. Historical localization architecture preserved

Historical architecture:
`TSK_0311_LOCALIZATION_CONTENT_ARCHITECTURE_2026-08-29.md` — blob `ef746d64c7878eb7d0f1b8fdf2356721728041c4`.

Historical evidence:
`TSK_0311_LOCALIZATION_CONTENT_ARCHITECTURE_EVIDENCE_2026-08-29.md` — blob `b9e7770faa0fa94a35d98d8141dec367583233f7`.

Still-valid historical facts preserved:

- en-GB canonical semantic baseline;
- provisional tr-TR and ar locale model;
- semantic externalized keys/files;
- locale manifest and deterministic fallback;
- independent schema/content semantic versioning;
- source-backed instruction ID binding;
- CLDR/Unicode-equivalent plural/number/date behavior;
- RTL and technical-literal isolation;
- accessibility/localization interaction;
- content ownership and privacy boundaries.

The stale historical limitation was its explicit **accountless first-phone product** scope, which omitted the current optional account/session/dashboard/device-lifecycle IA.

Markers:
- `TSK0311_HISTORICAL_PROVENANCE=PASS`;
- `TSK0311_SCOPE_RECONCILIATION=PASS`.

## 4. Current externalized namespace and key coverage

Current logical file model contains all thirteen expected namespaces:

`common`, `navigation`, `setup`, `verification`, `protection-map`, `troubleshooting`, `removal-recovery`, `accessibility`, `account`, `session`, `dashboard`, `device-management`, `account-lifecycle`.

Marker: `TSK0311_EXTERNALIZED_NAMESPACES=13/13_PASS`.

VER-0311 also proved 21 representative current dual-mode key requirements, including:

- public optional-account entry/accountless continuation;
- post-core finish-without-account choice;
- sign-in/auth-result/provider/session-expiry flows;
- dashboard/device state and reverify/reinstall/replace/revoke/delete actions;
- account deletion versus DNS removal truth;
- anonymous-state reset versus account/DNS truth;
- DNS removal versus account/device-record truth.

Marker: `TSK0311_DUAL_MODE_KEY_COVERAGE=21/21_PASS`.

## 5. Current truth / fallback / formatting / accessibility / ownership

VER-0311 proved current localization explicitly preserves:

- optional account remains optional;
- auth/provider failure accountless fallback;
- account/session/device ownership never becomes protection verification;
- logout/revoke/device-record deletion/account deletion/anonymous reset/DNS removal are distinct semantics;
- no automatic anonymous-state linkage/promotion;
- no browsing/query/activity history, child account/profile, raw DNS admin/query-log or overall-safety-score expansion;
- visible `SafeWeb` / `SafeWeb DNS` identity while technical `usesafeweb.com` literals remain exact and LTR-isolated;
- deterministic requested-locale -> en-GB -> visible dev/test missing-key fallback;
- no runtime machine translation for authoritative setup/verification/privacy/security/auth/recovery/destructive copy;
- CLDR/Unicode-equivalent plural/number/date/session-expiry behavior;
- Arabic RTL plus bidi isolation, DOM/focus order, error/action association, destructive accessible names and reflow;
- explicit current ownership for auth/session, dashboard/device-management and destructive account/device lifecycle content;
- independent localization-schema and locale-content versioning with additive compatible expansion.

Markers:
- `TSK0311_DUAL_MODE_TRUTH=PASS`;
- `TSK0311_FALLBACK_FORMATTING_A11Y_OWNERSHIP_VERSIONING=PASS`.

## 6. Current source-backed instruction binding

Current TSK-0307 is separately current PASS and remains the single source-backed owner of platform setup/verification/removal/recovery instruction semantics:

- current TSK-0307 artifact blob `73a7028e247833bfe7e98487d9e079a51d36d424`;
- current TSK-0307 EVD blob `afba74ba076bcc6832199955682462631abea0f0`.

The localization architecture binds those instructions by stable instruction ID and cannot silently retain older copied text. Optional account/session/dashboard product copy is not added to TSK-0307 unless genuinely platform/source-owned.

Marker: `TSK0311_CURRENT_INSTRUCTION_BINDING=PASS`.

## 7. Testability proof

The current artifact defines 18 deterministic implementation acceptance assertions covering parseability, en-GB completeness, hard-coded-copy prevention, tr/ar fallback, current TSK-0307 binding, visible missing-key failure, RTL/bidi isolation, locale-aware formatting, content/schema versioning, semantic non-mutation, accessibility, privacy, accountless alternatives, auth fallback, ownership-versus-verification, distinct destructive operations, account-deletion/DNS-removal truth and SafeWeb/endpoint preservation.

Marker: `TSK0311_TEST_ASSERTIONS=18/18_PASS`.

## 8. Independent VER-0311

Final verifier:

- script `.github/scripts/verify_tsk0311_current_revalidation.py` — blob `7908f574aeffbe7b19c51670a2dee5b49cee08ce`;
- workflow `.github/workflows/verify-tsk0311-current-revalidation.yml` — blob `b5e1dc4d6e34cca83f289e3bca0a0095488abaec`;
- permissions: `contents: read` only;
- GitHub-hosted Ubuntu 24.04 LTS;
- final run `33587275544`;
- final job `100113936593`;
- conclusion: **SUCCESS**.

Final markers:

- `TSK0311_INPUT_HASHES=PASS`;
- `TSK0311_CURRENT_WBS=PASS`;
- `TSK0311_CURRENT_PREDECESSOR=PASS`;
- `TSK0311_HISTORICAL_PROVENANCE=PASS`;
- `TSK0311_DUAL_MODE_IA_INPUT=PASS`;
- `TSK0311_SCOPE_RECONCILIATION=PASS`;
- `TSK0311_LOCALE_MANIFEST=PASS`;
- `TSK0311_EXTERNALIZED_NAMESPACES=13/13_PASS`;
- `TSK0311_DUAL_MODE_KEY_COVERAGE=21/21_PASS`;
- `TSK0311_DUAL_MODE_TRUTH=PASS`;
- `TSK0311_CURRENT_INSTRUCTION_BINDING=PASS`;
- `TSK0311_FALLBACK_FORMATTING_A11Y_OWNERSHIP_VERSIONING=PASS`;
- `TSK0311_TEST_ASSERTIONS=18/18_PASS`;
- `TSK0311_NON_INFERENCE=PASS`;
- `TSK0311_CURRENT_ACC=PASS`;
- `TSK0311_CURRENT_VER=PASS`;
- `TSK0311_CURRENT_EVD_READY=PASS`;
- `TSK0311_CURRENT_REVALIDATION=PASS`.

The initial verifier run failed only because one ownership assertion matched an exact sentence fragment rather than the same semantic rule containing the intervening words `product copy is`. The current artifact/runtime were unchanged; the predicate was made semantic and the complete rerun passed.

## 9. Acceptance disposition

- Current WBS/dependency — **PASS**.
- Historical localization architecture provenance — **PASS**.
- Current dual-mode IA coverage — **PASS**.
- Locale manifest — **PASS**.
- 13/13 namespace coverage — **PASS**.
- 21/21 representative current dual-mode key coverage — **PASS**.
- Truth/fallback/formatting/RTL/accessibility/ownership/versioning — **PASS**.
- Current TSK-0307 source-binding rule — **PASS**.
- 18/18 testability assertions — **PASS**.

**ACC-0311 = PASS. VER-0311 = PASS. EVD-0311 = SATISFIED.**

**TSK-0311 current dual-mode revalidation: PASS, pending only durable runtime reconciliation/read-back.**

## 10. Non-inference

This proves L4 localization/content architecture only. It does not implement production locale files, certify Turkish/Arabic linguistic quality, prove native-speaker/representative-parent behavior, activate a market, implement authentication/session/dashboard/device ownership, complete legal/privacy review, publish, process participants, activate payment, pass LG-06, launch or infer successor PASS.
