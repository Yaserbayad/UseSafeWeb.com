# TSK-0308 — Post-CR-0008 Dual-Mode Shared Responsive Design-System Revalidation

**Task:** TSK-0308 — Create the shared responsive design system for public and product surfaces  
**Acceptance / Verification / Evidence:** ACC-0308 / VER-0308 / EVD-0308  
**Lifecycle / Priority / Authority:** L4 / HIGH / A3 / AUTO_ALLOWED  
**Version:** 2.0.0-post-CR0008  
**Date:** 2026-09-02 UTC  
**Candidate disposition:** CURRENT PASS pending independent VER-0308, durable EVD-0308 and guarded runtime reconciliation.

## 1. Revalidation decision

The historically owner-approved TSK-0308 design system remains valid for its shared tokens/primitives, DS-01 through DS-13 composition/state/accessibility/localization rules, responsive breakpoints and evidence-truth behavior. It is stale only where its 2026-08-29 scope explicitly prohibited all Login / Account / Dashboard / Profile components and permanently fixed public/setup navigation to an accountless-only model.

Current `DEC-0053 / CR-0006` and current predecessor TSK-0309 require a dual-mode Version-1 experience: complete accountless core plus optional parent account/session/lightweight dashboard/device management. Therefore current acceptance preserves the approved candidate as immutable provenance and adds a bounded dual-mode addendum rather than redesigning the SafeWeb identity, TSK-0300 token/primitive system or still-valid responsive component semantics.

## 2. Current canonical inputs

- WBS `Plans/Master/WBS/master-wbs.csv` — blob `b27a0c5df2f5636d8ed71051e9e26a68959a2616`.
- Relationship graph `Plans/Master/RELATIONSHIP_INDEX.yaml` — blob `c108d2c162bcea2ee4cc01def46d0487a9501032`.
- Pre-TSK-0308 runtime `CURRENT_STATE.md` — blob `933bc16d90f66a7c8099666bd009cf50f78c5508`.
- Current TSK-0309 dual-mode baseline `prototype/TSK-0309/BASELINE.md` — blob `6302bb2509d04c8269e4df112140d7c416e42eff`.
- Current TSK-0300 acceptance evidence `TSK_0300_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md` — blob `efaf7c80c1723208569b13ba4e725b2e7cad8d1a`.
- Current TSK-0300 shared token source `brand/system/TSK-0300/tokens.css` — blob `cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f`.
- Current TSK-0300 primitive source `brand/system/TSK-0300/components.css` — blob `831e92a74b6dda04252d93242cb33bd491a02381`.
- Owner-approved SafeWeb primary wordmark remains blob `f93958e3e4a16f9056693072c1b9b8b31fcda852`.

Current WBS contract: L4 / HIGH / A3 / `AUTO_ALLOWED`; dependencies `TSK-0309; TSK-0300`; ACC-0308 requires content/error/loading/verification/uncertain/recovery states, tokens, accessibility behavior, localization expansion and implementation specifications.

## 3. Historical evidence preserved for compatible facts

Historical immutable approval package remains provenance for compatible design-system facts:

- `prototype/TSK-0308/SHARED_RESPONSIVE_DESIGN_SYSTEM_CANDIDATE.md` — blob `cd5c217ca7882589617dc94701fe5b6ac0eaf8d4`;
- `prototype/TSK-0308/candidate.css` — blob `de5571379ff240f36b5aecd50f555a07176dbd32`;
- historical reference surface — blob `fe86b9ec2b5d5e5e11cf4d135baca69f6b4a5862`;
- deterministic map — blob `cd83279cdf5381cd7dae3feb177439158c1f9197`;
- requirement/interface trace — blob `5e34ce9c192c6af65ba493cb356adb964c3d30b6`;
- historical acceptance evidence `TSK_0308_SHARED_RESPONSIVE_DESIGN_SYSTEM_ACCEPTANCE_EVIDENCE_2026-08-29.md` — blob `343961f30bc46a20762ad2b0108a4afe9593e5a3`;
- historical technical verification run/job `33273620531 / 99156419342`.

That evidence proved 13/13 component contracts, 6/6 required state classes, 6/6 Protection Map states, 8/8 requirement/interface bindings, Chromium 320/768/1024/1440 rendering, visible focus, reduced motion, RTL/LTR isolation, target-size floor and no console/page errors.

These still-valid facts are retained. The historical blanket account/dashboard exclusion is not retained as current scope evidence.

## 4. Exact contradiction and supersession

The historical candidate contains materially stale current-scope statements including:

- no Login / Account / Dashboard / Profile component is part of the system;
- public navigation may not include account/dashboard entry;
- setup may not expose persistent account navigation;
- the critical journey has no justified account field/interaction;
- setup cannot add an account step.

Current TSK-0309 explicitly requires optional Google sign-in/account/session continuity, dashboard, explicit device save/add/manage/reverify/reinstall/replace/revoke/delete-record, session expiry/reauthentication, logout, account deletion and unknown destructive-operation reconciliation, while preserving the complete login-free core.

Those historical exclusions are therefore superseded for current TSK-0308 acceptance. No other historical design-system principle is invalidated merely by CR-0006.

## 5. Current additive dual-mode artifacts

### Normative addendum

`prototype/TSK-0308/DUAL_MODE_ADDENDUM.md`
- version `2.0.0-post-CR0008`;
- blob `195ace26e6e8586e8e19da85a21d430a4a89a55a`.

It preserves the accountless core and DS-01–DS-13 while adding:

- DS-14 `OptionalAccountEntry`;
- DS-15 `SessionStatus`;
- DS-16 `DeviceManagementList`;
- DS-17 `AccountLifecycleActions`.

### Additive composition CSS

`prototype/TSK-0308/dual-mode-addendum.css`
- blob `67fe4f16a1aca56c7cd03ab28ec807a52e3e23e8`.

The file introduces only layout/composition selectors and consumes existing `var(--sw-*)` values; it defines no brand colors, font family, logo geometry or replacement token system.

### Reference surface

`prototype/TSK-0308/dual-mode-reference.html`
- blob `293945d9e2df823079e8dd73134168773a65a652`.

The internal reference binds current TSK-0300 tokens/components plus historical `candidate.css` and the additive CSS. It demonstrates:

- primary accountless `Start setup`;
- secondary `Sign in / Manage devices`;
- explicit sign-in-optional copy;
- accountless Protection Map evidence-state behavior;
- signed-in state explicitly separated from technical protection verification;
- auth-provider-unavailable state with `Continue without signing in`;
- device rows that distinguish ownership/configuration/protection verification;
- distinct Sign out, Unlink device, Delete device record, Delete account, Reset anonymous web state and Remove SafeWeb DNS operations;
- explicit account-deletion-versus-DNS-removal non-equivalence;
- EN plus Arabic/RTL stress/reference structure;
- no browsing/query/child-activity/raw-admin/query-log/overall-safety-score UI.

## 6. Current binding invariants

1. **Complete accountless core:** no login is required for core setup/protection/recovery/removal.
2. **Optional-account non-coercion:** account entry is secondary and provider/session failure preserves an accountless route.
3. **Identity/protection separation:** session/account/device ownership can never create S1 `Verified`.
4. **Lifecycle truth:** logout, revoke/unlink, device-record deletion, account deletion, anonymous-state reset and physical DNS removal are distinct operations.
5. **Privacy boundary:** no browsing/query/activity history, child profile, raw DNS administration/query log or arbitrary diagnostic surface.
6. **Single token/primitive authority:** TSK-0300 remains the only shared token/primitive authority.
7. **SafeWeb identity:** no identity reselection/redesign occurs.
8. **Responsive/localized:** 320/768/1024/1440 layouts, EN/TR/AR+RTL structural expansion and technical LTR isolation remain binding.
9. **Accessibility:** native controls, semantic headings/lists/statuses, visible focus, text-not-color state meaning, keyboard/DOM order, 200% text/320 reflow and reduced-motion behavior remain required.
10. **No current implementation inference:** this is an L4 design-system contract, not production auth/dashboard implementation.

## 7. Effective current TSK-0308 contract

The effective current shared responsive design system is:

1. the historical owner-approved TSK-0308 candidate for still-valid DS-01–DS-13/state/responsive/accessibility/localization semantics;
2. `DUAL_MODE_ADDENDUM.md` for current dual-mode scope;
3. `candidate.css` plus `dual-mode-addendum.css` for composition;
4. current TSK-0300 `tokens.css` and `components.css` as the sole shared implementation-value/primitive authority;
5. current TSK-0309 dual-mode experience baseline as journey/state/lifecycle predecessor authority.

## 8. Verification plan

Independent VER-0308 must, at minimum:

- parse the exact current WBS row and current TSK-0309/TSK-0300 PASS sections using non-uniform-heading-tolerant logic;
- hash-lock all historical/current source identities listed above;
- prove the historical candidate files remain unchanged;
- prove the obsolete blanket account/dashboard exclusions are superseded only by the addendum, not silently deleted from provenance;
- structurally prove DS-01–DS-13 remain represented by historical proof and DS-14–DS-17 exist in the addendum;
- prove all six ACC state classes remain covered;
- prove TSK-0300 token/component sources remain unchanged and additive CSS contains no raw hex colors or font-family definitions;
- prove the reference surface imports all four expected style layers and the approved SafeWeb wordmark;
- prove accountless primary/optional-account secondary/failure fallback/identity-protection/lifecycle-separation/no-surveillance semantics;
- verify responsive rendering at 320/768/1024/1440, no horizontal overflow, visible focus, RTL rendering and no browser console/page errors.

## 9. Non-inference

This current candidate does not redesign/reselect SafeWeb, change shared brand tokens/primitives, implement authentication/session/datastore/device ownership, activate telemetry, claim real-user/native-speaker behavior, complete legal/privacy review, publish publicly, process participants, activate payment/market, pass LG-06 or infer any successor PASS.

**TSK-0308 current result candidate: PASS subject to independent VER-0308, durable EVD-0308, guarded runtime reconciliation and exact read-back.**
