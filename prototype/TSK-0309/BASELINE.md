# TSK-0309 — Implementation-Ready Experience Baseline

**Version:** 2.0.0-post-cr0006  
**Status:** frozen internal L4 implementation contract candidate pending independent verification  
**Owner:** UX  
**Action authority:** A3 / AUTO_ALLOWED  
**Decision basis:** `DEC-0052 / CR-0005`, `DEC-0053 / CR-0006`, `DEC-0054 / CR-0007`  
**Human-validation claim:** none; pre-L8 human/user validation remains excluded by DEC-0052.

## 1. Purpose and source of truth

This baseline freezes the current Version-1 dual-mode experience for engineering handoff. The accepted representative implementation is now `prototype/TSK-0333/`, not the historical accountless-only `prototype/TSK-0310/` baseline.

The current product contract is:

- the complete core setup/protection/recovery journey remains usable without login;
- optional parent Google sign-in/account/session continuity is available;
- minimum parent/device ownership persistence and a lightweight dashboard/device-management experience are included;
- account/device ownership never substitutes for technical DNS/Protection Map verification;
- account lifecycle, device lifecycle, anonymous-state lifecycle and physical DNS removal remain distinct;
- mandatory login for core value, browsing/query/activity history, child accounts/profiles and unrestricted customer DNS administration remain excluded.

## 2. Frozen dual-mode journeys

### Accountless core

The accepted prototype covers discovery, supported-platform routing, native safeguard state, DNS setup, verification, optional relevant-service state, Protection Map, troubleshooting, false-positive/help/limitations paths, DNS removal, connectivity recovery and reset/reconfigure. No login is required to obtain or remove core protection value.

### Optional account and continuity

The accepted prototype additionally covers account entry, Google provider pending/success/cancel/error states, first session/account creation, returning session, dashboard, explicit device save/add, device detail/manage, reverify/reinstall/replace/revoke/delete-record, session expiry/reauthentication, logout, data-use/account view, account deletion, destructive confirmation, and unknown destructive-operation reconciliation.

No automatic J0/J1 import, linkage, promotion or expiry extension is authorized. Saving a device requires explicit signed-in intent. Account deletion does not claim DNS removal; deleting a saved device record does not claim physical configuration removal; revoke/unlink does not imply technical removal.

## 3. Truth-state contract

Only the accepted evidence states may represent protection status: `Verified`, `You confirmed this is set up`, `Action needed`, `Status uncertain`, `Not covered`, and `Removed`.

Invariants:

- `Verified` requires current qualifying technical evidence;
- parent confirmation, account presence and device ownership never create `Verified`;
- uncertainty/not-covered never imply success;
- removal cannot silently become verified;
- destructive operations with an unknown result are not automatically replayed;
- saved-record state and physical/configuration state are represented separately;
- there is no overall safety score or complete-safety claim.

## 4. Privacy and security boundary

The accountless path remains privacy-minimal and independent of persistent identity. The optional account path is limited to the minimum identity/session/device-ownership continuity required by the current L4 contract. This baseline does not authorize browsing/query/activity history, raw DNS history, child identity/profile, unrestricted AdGuard administration, credential collection in product support, or hidden anonymous-to-account linkage.

Exact provider/vendor approval, production session/token/cookie implementation, persistent datastore schema/retention/access/backup, authz/IDOR enforcement and production security validation remain L5-L7 work and are not inferred from this L4 freeze.

## 5. Accessibility, responsive and interaction acceptance

The authoritative current prototype has final no-overlay TSK-0321 evidence showing:

- focused 320 px / 200% text reflow PASS;
- full current TSK-0333 Chromium regression PASS;
- full post-CR-0007 TSK-0321 mechanical accessibility suite PASS;
- authoritative product source identity unchanged during review.

Keyboard/focus, skip navigation, responsive layouts, RTL/reduced-motion behavior, text alternatives/semantic state and truthful error/recovery behavior remain binding implementation requirements. Mechanical automated evidence is not represented as real-user or assistive-technology behavioral validation.

## 6. Defect disposition

No unresolved critical/high L4 functional, responsive, accessibility, privacy/security-boundary, recovery or truth-state defect is established by the current accepted TSK-0333 + TSK-0321 evidence set. The 320 px / 200% reflow defect found during accessibility review was remediated in authoritative `prototype/TSK-0333/prototype.css` and retested successfully.

Therefore this freeze reuses the accepted integrated prototype rather than inventing another UX implementation. Any later contradictory evidence reopens the affected acceptance.

## 7. Current accepted source/version set

Representative dual-mode prototype:

- `prototype/TSK-0333/index.html` — blob `934dc19d00cc9dd32e1ebc20c604373d153d4013`
- `prototype/TSK-0333/model.mjs` — blob `fc25e4b1facc303840311e8ce186612eb8799212`
- `prototype/TSK-0333/app.mjs` — blob `98659ba74a86d539b89664708bbcb830292486f8`
- `prototype/TSK-0333/prototype.css` — blob `385dc5269de79b7baca9aa597b9ecf4cca8a95f2`

Current acceptance evidence:

- `TSK_0321_POST_CR0007_FINAL_ACCESSIBILITY_EVIDENCE_2026-09-01.md` — blob `433800f2fd4a54c1fba2c42826579675df20bd75`
- current WBS source at rebaseline start — blob `b57104a71ab814d0f67e7fb8b0fd388d1f6aacfa`
- CR-0006/0007 change authority — `Plans/Master/Registers/EXCEPTIONS_CHANGE_CONTROLS.md`.

## 8. Change control and non-inference

A material change to core/account journey, truth-state semantics, account/persistence scope, destructive lifecycle meaning, platform setup/removal, privacy/security boundaries, accessibility behavior or supported platform behavior requires fresh disposition and evidence.

This L4 baseline does not prove provider/security/privacy architecture, implementation, real-user behavior, legal completion, release, payment, production activation, publication, launch or LG-06 PASS. Those remain separate evidence/gate decisions.