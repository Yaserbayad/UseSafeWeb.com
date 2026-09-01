# TSK-0327 — Current Dual-Mode Critical/High Findings Disposition

**Version:** 2.1.0-post-cr0007  
**Task:** TSK-0327 — Resolve critical usability, trust, and accessibility findings  
**Acceptance:** ACC-0327  
**Verification:** VER-0327  
**Evidence:** EVD-0327  
**Scope authority:** DEC-0053 / CR-0006 and DEC-0054 / CR-0007  
**Disposition:** current-scope acceptance candidate; subject to deterministic verification and runtime reconciliation

## 1. Why the historical disposition required re-evaluation

The accepted 2026-08-29 findings disposition covered the accountless implementation-ready prototype. CR-0006 subsequently added optional parent account/session, minimum device ownership persistence, lightweight dashboard/device management and account/device lifecycle surfaces while preserving the complete accountless core. The old statement that zero critical/high findings remained could not, by itself, prove the expanded current surface.

A first post-CR-0007 revalidation on 2026-09-01 used the expanded TSK-0333 prototype and closed its discovered DNS-removal reachability defect. A later authority comparison found one additional real trust/brand-conformance defect in that accepted prototype: it rendered `UseSafeWeb` as the visible brand, while owner-approved TSK-0301/TSK-0297 requires visible brand `SafeWeb`. That defect has now also been corrected and fully regression-tested. This version supersedes the earlier 2.0.0 candidate.

## 2. Current evidence set reviewed

Current integrated dual-mode prototype:

- `prototype/TSK-0333/index.html` — blob `934dc19d00cc9dd32e1ebc20c604373d153d4013`
- `prototype/TSK-0333/model.mjs` — blob `fc25e4b1facc303840311e8ce186612eb8799212`
- `prototype/TSK-0333/app.mjs` — blob `98659ba74a86d539b89664708bbcb830292486f8`
- `prototype/TSK-0333/prototype.css` — unchanged blob `6f8af459a0b0b1c9ec132657dfcd7ebff43090b8`
- original integrated analytical evidence `TSK_0333_POST_CR0007_INTEGRATED_PROTOTYPE_ACCEPTANCE_EVIDENCE_2026-08-31.md` — blob `4de73da09d637a142fc9968873ffdd755fdb07f3`
- original deterministic evidence `TSK_0333_POST_CR0007_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md` — blob `d1427b8bdd64772aab82683220af9becaf07f2ac`
- SafeWeb identity correction evidence `TSK_0333_SAFEWEB_BRAND_REVALIDATION_EVIDENCE_2026-09-01.md` — blob `f3ea3bf41c38050356a6e9e94aa251b07b35c5f3`
- final SafeWeb identity + full browser regression run/job `33479022852 / 99764278062` — SUCCESS on `adguardvm`, Node 22.23.2, Playwright 1.62.0, Chromium 151.0.7922.34.

Identity authority:
- `brand/identity/TSK-0301/README.md` — blob `b8ffd2ed234465a238558a7b94e56274de49696a`; visible brand exactly `SafeWeb`, `UseSafeWeb.com` only domain/project identifier.
- `brand/guidelines/TSK-0297/README.md` — blob `89e915678e85f7f301e8fa4b05c335cd803dd9d4`; same visible-name rule.

Current upstream product/scope semantics remain supplied by the accepted post-CR-0006/0007 chain including TSK-0146, TSK-0229, TSK-0329, TSK-0331, TSK-0332, TSK-0334, TSK-0335 and current corrected TSK-0333.

## 3. Findings review

### 3.1 Functional critical paths — PASS

The current full browser campaign passes accountless Android and iPhone setup flows, unsupported-state handling, account creation, explicit device save, returning dashboard, replacement, provider error, session expiry, logout, account deletion, device-record deletion, removal/recovery and unknown destructive-result handling.

A real defect discovered during the original integrated campaign—configured SafeWeb DNS removal not reachable from the Protection Map—was corrected and the materially different rerun passed `TSK0333_BROWSER_REMOVAL_RECOVERY=PASS`. No unresolved critical/high functional finding remains.

### 3.2 Trust / evidence-state truth — PASS

The accepted prototype preserves the distinction between technical protection evidence and account/device/dashboard state. Account presence, sign-in, session state and saved-device records never create technical `Verified` status. Unknown destructive outcomes remain uncertain until resolved; logout/account deletion/record deletion/DNS removal remain distinct operations. Provider or session failure does not rewrite physical protection truth.

The later visible-brand contradiction was also a trust/conformance defect: `UseSafeWeb` was rendered despite explicit owner-approved identity requiring `SafeWeb`. Bounded correction run/job `33478938540 / 99764031711` replaced only 23 capitalized visible-name occurrences across index/model/controller, preserved lowercase technical endpoint/domain strings, and left CSS untouched. The full current browser regression then passed. No unresolved critical/high trust/identity finding remains.

### 3.3 Accessibility / responsive behavior — PASS for current automated/internal scope

The current full browser suite passes keyboard skip-link behavior, 320px and responsive layouts, RTL direction/language handling and zero browser console/page errors. The visible-name correction was a pure textual substitution and the same full accessibility/responsive checks passed afterward.

TSK-0321 retains the separate HUMAN_ONLY accessibility-review acceptance boundary; this TSK-0327 disposition does not self-certify that downstream human-authority task or claim human comprehension.

No unresolved critical/high barrier is established by the current automated/internal evidence set.

### 3.4 Recovery / removal / lifecycle — PASS

Physical DNS removal and later reconfiguration are reachable and tested. Device-record deletion is explicitly not physical DNS removal. Destructive unknown results do not auto-retry or falsely report success. Account/session failures retain accountless core fallback.

No unresolved critical/high recovery/lifecycle finding remains.

### 3.5 Privacy / security-adjacent product boundaries — PASS for L4 product review

The prototype has no browsing/query/activity history, child profile/account surface, raw/unrestricted DNS administration or automatic J0/J1-to-account linkage. The accepted browser run proves the no-transport prototype boundary, and current account/device operations preserve authorization/truth distinctions defined by accepted L4 contracts.

This is an L4 product/UX finding disposition only; it does not replace later L5-L7 architecture/security/privacy implementation verification.

### 3.6 Brand / identity conformance — PASS

The visible product name is now `SafeWeb` throughout the TSK-0333 index/model/controller. `UseSafeWeb.com` remains a domain/project identifier and lowercase `dns.usesafeweb.com` / `https://dns.usesafeweb.com/dns-query` remain technical endpoint literals. The current revalidation proves the corrected files equal the prior accepted files with only capitalized `UseSafeWeb → SafeWeb` substitution.

No unresolved critical/high identity-conformance finding remains.

## 4. Current deviations and closed diagnostics

The integrated acceptance/revalidation history records:

1. expected initial RED because the old prototype did not satisfy the expanded dual-mode contract;
2. **real product defect:** configured SafeWeb DNS removal was not reachable from the Protection Map — fixed and browser-retested successfully;
3. two verifier-only defects: ambiguous `Start setup` locator and overly literal privacy-copy assertion — corrected without weakening product acceptance;
4. **real product defect:** visible brand rendered as `UseSafeWeb` contrary to owner-approved TSK-0301/TSK-0297 — corrected by a pure visible-name substitution and the entire browser suite re-passed.

No failed run changed runtime PASS state. No unresolved current critical/high product finding remains after the final successful revalidation.

## 5. ACC / VER / EVD disposition

- **ACC-0327 candidate = PASS:** all current critical/high findings identified by the current internal/automated functional, trust-state, accessibility, responsive, recovery and identity-conformance review are fixed/closed with evidence; no owner-risk acceptance is needed for an unresolved critical/high finding.
- **VER-0327 candidate = PASS:** current accepted dual-mode source/evidence, explicit brand authority and reproducible full browser results directly cover representative current critical paths and the corrected identity.
- **EVD-0327 candidate = SATISFIED:** this versioned disposition plus pinned current TSK-0333 analytical/deterministic/brand evidence identifies exact source/environment, test output, date, verifier context, deviations and disposition.

No human comprehension/usability claim is made before L8. `RSK-0002` remains open/non-blocking before L8.
