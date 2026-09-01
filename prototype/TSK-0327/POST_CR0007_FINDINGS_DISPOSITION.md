# TSK-0327 — Current Dual-Mode Critical/High Findings Disposition

**Version:** 2.0.0-post-cr0007  
**Task:** TSK-0327 — Resolve critical usability, trust, and accessibility findings  
**Acceptance:** ACC-0327  
**Verification:** VER-0327  
**Evidence:** EVD-0327  
**Scope authority:** DEC-0053 / CR-0006 and DEC-0054 / CR-0007  
**Disposition:** current-scope acceptance candidate; subject to deterministic verification and runtime reconciliation

## 1. Why the 2026-08-29 disposition required re-evaluation

The accepted 2026-08-29 findings disposition covered the accountless implementation-ready prototype. CR-0006 subsequently added optional parent account/session, minimum device ownership persistence, lightweight dashboard/device management and account/device lifecycle surfaces while preserving the complete accountless core. Therefore the old statement that zero critical/high findings remained could not, by itself, prove the expanded current surface.

The historical artifact and evidence remain valid only for the unchanged accountless portions they directly tested.

## 2. Current evidence set reviewed

The current integrated dual-mode prototype is the TSK-0333 accepted surface:

- `prototype/TSK-0333/index.html` — blob `9395f0e105d20683b5beafa01b02d7b300e79a8d`
- `prototype/TSK-0333/model.mjs` — blob `9b7c239024d8ae24371b687aa39de6fa6b2b62b6`
- `prototype/TSK-0333/app.mjs` — blob `476ea932d95592fabf586f7ba381be0d346117fe`
- `prototype/TSK-0333/prototype.css` — blob `6f8af459a0b0b1c9ec132657dfcd7ebff43090b8`
- analytical acceptance evidence `TSK_0333_POST_CR0007_INTEGRATED_PROTOTYPE_ACCEPTANCE_EVIDENCE_2026-08-31.md` — blob `4de73da09d637a142fc9968873ffdd755fdb07f3`
- deterministic verification evidence `TSK_0333_POST_CR0007_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md` — blob `d1427b8bdd64772aab82683220af9becaf07f2ac`
- final browser run/job `33432762152 / 99621849637` — SUCCESS on `adguardvm`, Node 22.23.2, Playwright 1.62.0, Chromium 151.0.7922.34.

Current upstream product/scope semantics are also supplied by the accepted post-CR-0006/0007 chain, including TSK-0146, TSK-0229, TSK-0329, TSK-0331, TSK-0332, TSK-0334, TSK-0335 and current TSK-0333.

## 3. Findings review

### 3.1 Functional critical paths — PASS

The final TSK-0333 browser campaign passed accountless Android and iPhone setup flows, unsupported-state handling, account creation, explicit device save, returning dashboard, replacement, provider error, session expiry, logout, account deletion, device-record deletion, removal/recovery and unknown destructive-result handling.

One real current-scope defect was discovered during the browser campaign: configured SafeWeb DNS removal was not reachable from the Protection Map. The product controller was corrected to expose the removal action, and the materially different rerun passed `TSK0333_BROWSER_REMOVAL_RECOVERY=PASS`. The defect is therefore closed and no unresolved critical/high functional finding remains in the accepted prototype.

### 3.2 Trust / evidence-state truth — PASS

The accepted prototype preserves the distinction between technical protection evidence and account/device/dashboard state. Account presence, sign-in, session state and saved-device records never create technical `Verified` status. Unknown destructive outcomes remain uncertain until resolved; logout/account deletion/record deletion/DNS removal remain distinct operations. Provider or session failure does not rewrite physical protection truth.

No unresolved critical/high trust-state finding remains.

### 3.3 Accessibility / responsive behavior — PASS for current automated/internal scope

The final browser suite passed keyboard skip-link behavior, 320px and responsive layouts, RTL direction/language handling and zero browser console/page errors. The current static verifier also passed the structured UI, interaction, privacy/lifecycle and responsive/accessibility contract.

TSK-0321 retains the separate HUMAN_ONLY accessibility-review acceptance boundary; this TSK-0327 disposition does not self-certify that downstream human-authority task or claim human comprehension.

No unresolved critical/high barrier is established by the current automated/internal evidence set.

### 3.4 Recovery / removal / lifecycle — PASS

Physical DNS removal and later reconfiguration are reachable and tested. Device-record deletion is explicitly not physical DNS removal. Destructive unknown results do not auto-retry or falsely report success. Account/session failures retain accountless core fallback.

No unresolved critical/high recovery/lifecycle finding remains.

### 3.5 Privacy / security-adjacent product boundaries — PASS for L4 product review

The prototype has no browsing/query/activity history, child profile/account surface, raw/unrestricted DNS administration or automatic J0/J1-to-account linkage. The accepted browser run proved the no-transport prototype boundary, and current account/device operations preserve authorization/truth distinctions defined by the accepted L4 contracts.

This is an L4 product/UX finding disposition only; it does not replace later L5-L7 architecture/security/privacy implementation verification.

## 4. Current deviations and closed diagnostics

The current integrated acceptance campaign recorded:

1. an expected initial RED because the old prototype did not satisfy the expanded dual-mode contract;
2. a real product defect: configured DNS removal was not reachable from the Protection Map — fixed and browser-retested successfully;
3. two verifier-only defects: an ambiguous `Start setup` locator and an overly literal privacy-copy assertion — corrected without weakening product acceptance.

No failed run changed runtime PASS state. No unresolved current critical/high product finding remains after the final successful run.

## 5. ACC / VER / EVD disposition

- **ACC-0327 candidate = PASS:** all current critical/high findings identified by the current internal/automated functional, trust-state, accessibility, responsive and recovery review are fixed or otherwise closed with evidence; no owner-risk acceptance is needed for an unresolved critical/high finding.
- **VER-0327 candidate = PASS:** the current accepted dual-mode source/evidence set and reproducible browser results directly cover the representative current critical paths.
- **EVD-0327 candidate = SATISFIED:** this versioned disposition plus the pinned current TSK-0333 analytical/deterministic evidence identifies exact source/environment, test output, date, verifier context, deviations and disposition.

No human comprehension/usability claim is made before L8. `RSK-0002` remains open/non-blocking before L8.
