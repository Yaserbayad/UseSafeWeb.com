# TSK-0328 — Post-CR-0007 Information Architecture Acceptance Evidence

**Task:** TSK-0328 — Define information architecture and navigation model  
**Acceptance:** ACC-0328  
**Verification:** VER-0328  
**Evidence:** EVD-0328 analytical current-scope review  
**Date:** 2026-08-31  
**Verifier:** governed analytical review separate from artifact publication  
**Result:** PASS CANDIDATE PENDING DETERMINISTIC VERIFICATION AND RUNTIME RECONCILIATION

## 1. Exact persisted candidate

- Normative IA: `prototype/TSK-0328/INFORMATION_ARCHITECTURE_NAVIGATION.md`
- Version: `2.0.0-post-cr0007`
- Normative blob read back from `main`: `527436958a1cd75fc91057410f4347ad56a3f53a`
- Normative publication commit: `6768912443a43f05f948aa562484644cdcf73c47`
- Structured acceptance projection: `prototype/TSK-0328/ACCEPTANCE_MATRIX.json`
- Projection blob read back from `main`: `d3b345a982f98bc7bdb32bc105fda4ac5659e9ab`
- Projection publication commit: `3c4805e1ca7ab346b17203d20e759950762d63d5`
- Pre-acceptance runtime blob: `cd65636a10e0d0f6c72f5062a269cba69279399d`

## 2. Why a rebuild was required

Historical TSK-0328 v1.0.0 was accepted under pre-CR-0006 accountless-only scope. It explicitly excluded Login, Account and Dashboard and stated that the operational setup surface did not become an account dashboard.

DEC-0053/CR-0006 changed Version-1 scope to require optional parent authentication/session, minimum parent/device ownership persistence and lightweight dashboard/device management while preserving the complete accountless core. Current ACC-0328 was correspondingly revised to require optional account sign-in/return/dashboard/account lifecycle navigation.

The historical public/setup structure remained useful where compatible, but the historical PASS could not satisfy the changed acceptance. TSK-0328 was therefore correctly reopened as TODO before this rebuild.

## 3. Eligibility and current authority

Current WBS and runtime define TSK-0328 as:

- lifecycle L4;
- priority MEDIUM;
- hard dependencies `TSK-0325; TSK-0315`;
- A3 / `AUTO_ALLOWED`;
- `ACC-0328 / VER-0328 / EVD-0328`;
- requirement references `REQ-0028; REQ-0029; CON-0010; CON-0017`;
- interfaces `INT-0009; INT-0010`.

Both hard dependencies are current durable PASS under post-CR-0007 runtime sections. The bounded relationship-index inspection run/job `33407284717 / 99537877018` completed SUCCESS and confirmed current TSK-0328 graph registration plus ACC/VER/EVD relationships and downstream TSK-0329 dependency traversal.

**Eligibility result: PASS.**

## 4. ACC-0328 clause-by-clause review

| ACC clause | Persisted v2 evidence | Result |
| --- | --- | --- |
| Normal accountless path | Section 9.1 provides a complete signed-out public → setup → native safeguard → DNS setup → verification → optional service → Protection Map → Exit route. No Sign in or Dashboard is required. | PASS |
| Exception paths | Section 10 covers already configured, unsupported/not covered, failed verification, false positive, account/provider failure, session expiry/revocation, lost accountless state, physical removal, dashboard-record deletion, revoke/unlink and account deletion. | PASS |
| Optional account sign-in | `ACC-ENTRY`, `ACC-SIGNIN`, `ACC-ERROR` and `ACC-REAUTH` are explicit logical screens with goals and traces. Sign-in is secondary/optional and provider failure leaves accountless core available. | PASS |
| Signed-in return | Section 9.3 routes a returning authorized parent to `DASH-HOME → DASH-DEVICE`; stored record presence is explicitly not technical verification. | PASS |
| Dashboard/device lifecycle | `DASH-HOME`, `DASH-ADD`, `DASH-DEVICE`, `DASH-MANAGE`, `DASH-RECORD-DELETE`, `ACC-ACCOUNT` and `ACC-DELETE` cover the required minimum continuity and lifecycle architecture. | PASS |
| Avoid unnecessary gates | Binding rule 7, public/setup navigation and necessity controls prohibit identity/payment/marketing/survey/account screens from the signed-out core path. | PASS |
| Login optional for core value | Binding rules 1-2, Section 9.1 and deterministic case IA-T01 make the full core completable without login. | PASS |
| Every screen maps to user goal and requirement | Sections 6-8 define every public, setup, account and dashboard logical screen with a user goal and required trace; the structured projection independently enumerates the same inventory. | PASS |

## 5. Requirement and interface review

### REQ-0028 — necessity

Every logical screen in the candidate has an explicit user goal and requirement trace. The design rejects routes used only for analytics/SEO/onboarding ceremony/newsletter/waitlist/demographic intake and limits Sign in/Dashboard to continuity value. **PASS.**

### REQ-0029 — technically correct setup/fallback routing

All setup/device-management entries route back to the owning current setup/verification/removal flows. Unsupported paths stop truthfully; account/dashboard presence cannot create a technical fallback or bypass verification. **PASS.**

### CON-0010 — optional account + complete login-free core

The IA now contains the required optional account/dashboard capability without making it a predecessor or gate to Start setup or core completion. **PASS.**

### CON-0017 — multilingual technical capability vs market authority

Public/setup/account/dashboard screens inherit English/Turkish/Arabic+RTL capability while explicitly refusing to infer official non-UK market/legal/support activation. **PASS.**

### INT-0009 — implementation-ready experience structure

Engineering receives explicit experience systems, route families, logical screen IDs, user goals, major exits, exception routes, lifecycle separation and evidence-state rules rather than needing to invent the product architecture during build. **PASS for TSK-0328 scope.**

### INT-0010 — testable experience acceptance

The artifact includes 18 deterministic/synthetic IA cases and the projection provides structured path/screen/invariant data suitable for objective QA/verification. **PASS for TSK-0328 scope.**

## 6. Current product-scope reconciliation

The rebuilt IA carries forward the accepted current upstream contracts:

- TSK-0315: complete accountless core plus optional account/session/dashboard continuity, provider-outage containment, device/account lifecycle separation and truthful technical evidence.
- TSK-0325: all 17 current parent touchpoints and eight accountless path classes, plus the optional account/device overlay.
- TSK-0312: planned Google social sign-in, signed-in/signed-out/error/expiry/revocation/logout/deletion states, minimum intake and no automatic J0/J1 promotion/linkage.
- TSK-0142: dashboard empty/list, add/manage/reverify/reinstall/replace/revoke/remove flows, truthful current/last-known evidence and curated non-surveillance controls.

The IA deliberately does not choose exact OAuth/Firebase mechanics, persistent schema/storage, token/session implementation, authorization implementation, database routing or physical deployment architecture.

## 7. Lifecycle-separation and protection-truth review

The candidate separately names and routes:

- logout;
- revoke/unlink;
- delete dashboard record;
- delete account;
- J0/J1 expiry/deletion; and
- physical UseSafeWeb DNS removal.

No one operation is allowed to claim another completed unless downstream owning workflows actually perform and verify both.

Account/device ownership, dashboard presence, valid session and historical setup remain protection-state neutral. Current qualifying technical verification remains required for `Verified`; contradictory/stale evidence can demote displayed state.

**Result: PASS.**

## 8. Privacy, scope and accessibility fences

The candidate introduces no browsing/query/activity history, child account/profile, raw AdGuard administration, broad per-domain control, mandatory login, payment gate or safety score. It contains no child-identity routing requirement and forbids session/token values in user-visible URLs.

All surfaces inherit WCAG 2.2 AA target, mobile-first responsive behavior and English/Turkish/Arabic+RTL capability without a behavioral-usability claim before L8.

**Result: PASS.**

## 9. Downstream non-inference

The rebuilt IA does not infer:

- TSK-0329 interaction/prototype PASS;
- provider/vendor/security/privacy architecture approval;
- persistent data/schema/storage approval;
- implementation/build/deployment behavior;
- real-user behavioral validation;
- LG-06 or any later gate PASS.

`RSK-0002` remains OPEN/non-blocking before L8.

## 10. Analytical disposition

Every current ACC-0328 clause is represented in the exact persisted v2 artifact and structured projection. The historical accountless-only IA has been superseded only where current optional-account scope requires it; compatible public/setup structure was retained without weakening the login-free core or technical-truth boundaries.

**Analytical result: ACC-0328 PASS candidate.**

TSK-0328 remains non-PASS until a separate deterministic verifier proves the exact persisted artifact/projection/current authority and the resulting evidence is durably recorded and reconciled into `CURRENT_STATE.md`.
