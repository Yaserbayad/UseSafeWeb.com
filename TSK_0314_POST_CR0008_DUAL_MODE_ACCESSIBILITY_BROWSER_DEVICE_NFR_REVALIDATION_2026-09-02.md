# TSK-0314 — Post-CR-0008 Dual-Mode Accessibility, Responsive, Browser, OS and Device-Support NFR Revalidation

**Task:** TSK-0314 — Define accessibility, responsive, browser, OS, and device support NFRs  
**Acceptance / Verification / Evidence:** ACC-0314 / VER-0314 / EVD-0314  
**Lifecycle / Priority / Authority:** L4 / MEDIUM / A4 / AUTO_ALLOWED  
**Version:** 2.0.0-post-CR0008  
**Date:** 2026-09-02 UTC  
**Candidate disposition:** ACC-0314 current PASS pending independent VER-0314 and guarded runtime reconciliation.

## 1. Current contract and revalidation boundary

Current WBS acceptance requires requirements to define:

- target WCAG level;
- keyboard, screen-reader and text-resize/reflow behavior;
- supported browser/OS versions;
- device test tiers;
- unsupported-state messaging.

Current direct dependency is exactly TSK-0046, now current PASS under the post-CR-0008 dual-mode performance/capacity NFR revalidation.

The historical TSK-0314 contract remains substantively strong for WCAG 2.2 AA, keyboard/focus, semantic state, reflow/resize, contrast, target size, motion, responsive/RTL behavior, release-time browser/OS matrices, four test tiers and distinct unsupported/uncertain/accessibility-blocker states. Revalidation is required because:

1. TSK-0046 is now a newer current direct predecessor and explicitly requires performance/capacity work never to weaken accessibility or truthful state behavior.
2. `DEC-0053 / CR-0006` activates optional parent sign-in/session/dashboard/device-management/account-lifecycle surfaces alongside the complete accountless core. The historical release-blocking test wording centered only on the accountless journey.
3. `DEC-0054 / CR-0007` removes mandatory pilot/staging sequencing; pre-release accessibility/browser/device verification remains required, while first real users are live-production users only after LG-09 and all actually applicable prerequisites.
4. Evergreen browser/OS version snapshots are time-sensitive and must be refreshed at each release boundary.

No visual identity redesign, DNS-mechanism redesign, implementation claim or public support commitment is created by this revalidation.

## 2. Accessibility conformance target

All implemented public/product web UI in scope targets **WCAG 2.2 Level AA**.

Current W3C source review on 2026-09-02:

- `https://www.w3.org/TR/WCAG22/`
- `https://www.w3.org/WAI/standards-guidelines/wcag/`

W3C continues to recommend WCAG 2.2 for current accessibility work. Every applicable Level A and AA success criterion must be satisfied before any WCAG 2.2 AA conformance claim. Automated tooling alone cannot prove conformance; manual keyboard, screen-reader, resize/reflow and visual/state review remain necessary where applicable.

Accessibility defects that prevent start, understanding, setup, optional sign-in/account management, verification, troubleshooting, recovery, removal, account/device deletion or truthful Protection Map interpretation are functional defects, not cosmetic issues.

## 3. Keyboard and focus requirements

Every required interaction must be operable without a pointing device.

Requirements:

1. native semantic controls are preferred;
2. all required functionality is keyboard reachable/operable;
3. focus order follows logical task and reading order;
4. no keyboard trap;
5. focus indication remains visible and sufficiently distinguishable;
6. focused elements are not fully obscured by sticky/overlay content;
7. modal/dialog focus enters, remains constrained while modal and returns appropriately on close;
8. repeated navigation provides a skip/bypass mechanism when applicable;
9. hover-only/pointer-gesture-only required actions are prohibited;
10. drag or complex gestures have accessible alternatives where applicable;
11. keyboard/click handling cannot cause duplicate consequential actions;
12. sign-in, device unlink/delete, logout and account deletion confirmation/recovery interactions follow the same focus and duplicate-action protections as accountless setup/removal.

## 4. Screen-reader, semantics and state truth

Use native HTML semantics first; ARIA supplements rather than replaces native semantics.

Every applicable surface must provide meaningful page title/headings/landmarks, accessible control names, programmatic form labels/instructions/invalid state, error association, semantic progress/current step, appropriate asynchronous status announcement, and equivalent accessible text for meaningful non-text content.

### 4.1 Protection and configuration states

Phone / Internet / Services state remains layer-specific and must expose exact current protection/configuration evidence in accessible text. Color/icon/position alone cannot communicate status. Configured/parent-confirmed state must not masquerade as technically verified protection. Account ownership, login/session state or dashboard registration also cannot upgrade protection evidence.

### 4.2 Optional-account surfaces

When implemented, sign-in/session/dashboard/device/account-lifecycle surfaces must expose:

- provider/sign-in progress and failure without making login mandatory for the accountless core;
- session expiry/re-authentication state accessibly;
- owned-device lists and action affordances with meaningful names and ownership context;
- unlink/revoke, dashboard record deletion, account deletion and DNS removal as distinct operations;
- destructive-action confirmation, result and recoverable error state without color-only or timing-only meaning;
- provider/datastore outage state that preserves an accessible accountless continuation when the core is healthy;
- no raw token, secret, DNS query/domain activity history or unnecessary child/profile data in accessible names/status text.

## 5. Text resize, zoom and reflow

Implementation requirements preserve the WCAG 2.2 AA baseline:

- text resize to 200% without loss of required content/functionality except applicable WCAG exceptions;
- reflow without two-dimensional scrolling at the equivalent of 320 CSS px except legitimate WCAG exceptions;
- no fixed-height clipping of translated/enlarged text;
- controls/cards/labels wrap rather than truncate critical instructions/status;
- browser zoom and OS text scaling do not hide required actions;
- orientation is not restricted without a genuine essential exception;
- English, Turkish and Arabic/RTL critical flows are included;
- optional account/session/dashboard/device and deletion/recovery states are included when implemented, not just accountless setup.

## 6. Contrast, target size, motion and performance interaction

Retain at minimum:

- normal-text contrast >=4.5:1;
- large-text contrast >=3:1;
- applicable non-text UI/component boundaries >=3:1;
- no status communicated by color alone;
- WCAG 2.2 Target Size (Minimum) compliance, including 24×24 CSS px or a valid exception/spacing condition;
- `prefers-reduced-motion` support for nonessential animation;
- no essential state/instruction conveyed by animation alone;
- non-motion semantic loading/verification equivalent.

Current TSK-0046 performance/capacity NFR is subordinate to this correctness boundary: page-weight, latency, throughput or capacity improvements cannot remove semantics, focus visibility, accessible status, reflow, minimum targets or required alternative interaction. Accessibility verification must be included in performance regression rather than traded away to meet performance targets.

## 7. Responsive, multilingual and RTL behavior

The public/product UI is mobile-first and remains functional from 320 CSS px through wide desktop layouts.

Required shapes include narrow phone portrait, phone landscape, tablet, desktop/laptop, 200% zoom/reflow and enlarged OS-text cases where exposed.

Arabic uses real RTL layout behavior. Technical hostnames, URLs, identifiers and code/config snippets use safe bidi isolation/direction and remain readable/copyable. DOM/focus reading order remains logical. English/Turkish remain LTR.

Accountless and optional-account/dashboard/device surfaces share these responsive/localization/accessibility requirements. A translated optional-account surface is not supported merely because strings fit.

## 8. Browser and OS support policy

Permanent support is defined by a deterministic **release-time matrix**, not by freezing the September 2026 numbers below.

### 8.1 Release-time policy

For each release candidate:

- **Chrome desktop:** current Stable major plus immediately previous Stable major on supported desktop OSes used by the release matrix.
- **Edge desktop:** current Stable plus immediately previous Stable; from Stable 152 Microsoft uses a two-week major cadence, so release evidence must record exact installed Stable versions rather than infer them from a planned schedule.
- **Firefox desktop:** current Release plus immediately previous Release; Firefox 155 began the new two-week release cadence on 2026-09-01.
- **Safari/macOS:** current security-supported Safari/WebKit on current security-supported macOS, with prior still-security-supported combinations rotated through Tier 2 unless promoted by full Tier-1 evidence.
- **iPhone/iPad web UI:** Safari/WebKit on current security-supported iOS/iPadOS; legacy security branches are Tier 2 unless they pass the full Tier-1 suite.
- **Android web UI:** current Chrome Stable plus immediately previous Stable on Android/device builds still receiving security updates; supported Android major/device combinations must be frozen from current device/security evidence at release time.
- embedded/in-app browsers are not Tier 1 absent explicit full verification.
- Beta/Dev/Canary/preview OS/browser builds are observation environments only, not production-support proof.

### 8.2 Current dated snapshot — 2026-09-02

Current first-party source review establishes:

| Surface | Current source truth on 2026-09-02 | Release-test implication |
| --- | --- | --- |
| Chrome desktop | Chrome 152 Stable updated to 152.0.7977.75/.76 on 2026-09-01 | Current Stable baseline is 152; immediately previous Stable remains the companion compatibility target |
| Firefox desktop | Firefox 155 released 2026-09-01; Mozilla moved to a two-week cadence | Current Release baseline is 155; previous Release remains companion target |
| Edge desktop | Edge 152 Stable released 2026-08-27; Edge 153 Stable is scheduled for week of 2026-09-10 | 152 is current Stable today; do not treat scheduled 153 as current until directly released/observed |
| Apple web | Latest iOS/iPadOS 26.6.1; macOS 26.6.2; Safari 26.6.1 security update available for supported Sonoma/Sequoia | Freeze exact tested Safari/WebKit + OS combination at release time |
| Android | August 2026 Android bulletin remains latest published as of 2026-09-02; AOSP states bulletins publish first Monday unless holiday | Require current vendor/security-patch evidence at release; do not invent an unpublished September patch level |

Sources reviewed:

- Chrome Releases: `https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop.html`
- Firefox 155 enterprise release notes / Mozilla cadence notice
- Edge release schedule: `https://learn.microsoft.com/deployedge/microsoft-edge-release-schedule`
- Edge lifecycle: `https://learn.microsoft.com/deployedge/microsoft-edge-support-lifecycle`
- Apple security releases: `https://support.apple.com/100100`
- Safari 26.6.1 security content: `https://support.apple.com/148286`
- Android Security Bulletin overview and August 2026 bulletin: `https://source.android.com/docs/security/bulletin/asb-overview`, `https://source.android.com/docs/security/bulletin/2026/2026-08-01`

This snapshot is evidence for current requirement definition only. It must be refreshed at release/test time.

## 9. Web support is separate from DNS/setup-mechanism support

A supported browser does not prove the OS/device/network supports a SafeWeb DNS mechanism. DNS install/verification/removal compatibility remains owned by current TSK-0317/TSK-0408/TSK-0409 platform/mechanism evidence.

Examples:

- a supported iPhone Safari version does not itself prove profile installation/verification succeeds under every current device/security policy;
- Android web compatibility does not prove Private DNS coexistence with VPN/app-specific encrypted resolvers or managed policy;
- desktop browser support does not imply SafeWeb DNS is configured on that desktop.

The UI must represent web-surface support, DNS-mechanism support and current protection evidence separately.

## 10. Device and accessibility test tiers

### Tier 0 — automated every relevant change

Where implementation exists: semantic/lint rules, automated WCAG rules, reliable keyboard/focus smoke, narrow/wide reflow, LTR/RTL regression, supported-browser critical routing/state rendering and optional-account surface smoke when those surfaces exist. Tier 0 does not certify conformance.

### Tier 1 — release-blocking manual + automated

Before claiming public web support, the implemented critical journeys require appropriate manual + automated verification across representative supported combinations, including:

- iPhone/current supported iOS Safari + VoiceOver;
- security-supported Android/current Chrome + TalkBack;
- Windows 11/current supported Chrome/Edge + keyboard and NVDA on at least one Chromium path;
- Windows 11/current supported Firefox + keyboard/screen-reader compatibility sampling;
- current supported macOS/Safari + VoiceOver;
- 320 CSS px and 200% resize/reflow;
- English/Turkish/Arabic RTL critical variants;
- complete accountless setup/verify/recover/remove journey;
- optional sign-in/session/dashboard/device/account-deletion journey when implemented.

### Tier 2 — compatibility rotation

Immediately previous supported browser/OS combinations and representative secondary form factors. Critical accountless plus implemented optional-account routes receive targeted regression. Tier 2 may be promoted only by full Tier-1 evidence and separate DNS-mechanism support where claimed.

### Tier 3 — unsupported/best-effort observation

Legacy/out-of-support OS versions, obsolete browsers, preview builds and untested embedded/in-app browsers receive no supported claim. Graceful accessible messaging is still required where technically feasible.

## 11. Unsupported, degraded and uncertain messaging

The UI must distinguish:

1. **Unsupported web/browser/OS** — the UI itself is outside the tested matrix; do not infer existing DNS protection is absent solely from browser support.
2. **Web UI supported, DNS mechanism not covered** — represent current platform/mechanism `Not covered` semantics and offer only verified alternatives.
3. **Supported combination, verification inconclusive** — represent uncertain/error state; setup completion or parent confirmation cannot upgrade it to verified.
4. **Accessibility blocker on a claimed Tier-1 flow** — the affected combination/flow cannot remain represented as fully supported until corrected and regression-tested; an alternative counts only if genuinely equivalent and accessible.
5. **Optional-account unavailable while accountless core is healthy** — sign-in/dashboard/provider/datastore degradation is represented separately and preserves accessible accountless continuation; it is not a whole-service outage or proof that DNS protection failed.

All unsupported/degraded messages are themselves translatable, RTL-safe, keyboard accessible and screen-reader perceivable.

## 12. Release acceptance and regression rules

A release cannot claim the TSK-0314 supported web matrix unless:

1. applicable WCAG 2.2 A/AA criteria are verified for implemented critical routes;
2. no critical keyboard/screen-reader/resize/reflow blocker remains on Tier 1;
3. each claimed Tier-1 browser/OS/device combination has current release evidence;
4. exact tested browser/OS/device versions are recorded;
5. English/Turkish/Arabic RTL critical-route checks pass;
6. Protection Map/setup/account states remain semantically truthful;
7. unsupported/degraded/uncertain/account-provider-failure paths have accessible copy and recovery/continuation;
8. DNS mechanism support is checked separately before a setup-support claim;
9. automated findings are dispositioned and manual checks are complete where required;
10. current TSK-0046 performance tests do not hide accessibility regressions;
11. optional account/session/dashboard/device-management/account-deletion surfaces are included when present;
12. no real-user behavioral evidence is fabricated before the governed L8/live-production-validation boundary.

## 13. Revalidation triggers

Refresh affected proof when:

- WCAG target/current W3C guidance changes materially;
- current/previous browser release cadence or supported OS/security branches change;
- a browser/OS/device combination is added or removed from claimed support;
- DNS mechanism support changes;
- public/product navigation or component architecture changes materially;
- optional account/session/dashboard/device/account-lifecycle surfaces change materially;
- localization/RTL behavior changes;
- TSK-0046 performance/capacity constraints change in a way that could affect accessibility behavior;
- a critical accessibility or support incident occurs;
- a claimed Tier-1 combination no longer receives required vendor security updates.

## 14. ACC-0314 traceability

ACC-0314 requires target WCAG level, keyboard/screen-reader/text-resize behavior, supported browsers/OS versions, device test tiers and unsupported-state messaging.

Current coverage:

- target WCAG level: §2;
- keyboard/focus: §3;
- screen reader/state semantics: §4;
- text resize/reflow: §5;
- responsive/RTL: §7;
- supported browser/OS policy and dated current source snapshot: §8;
- separate web-vs-DNS support boundary: §9;
- device/accessibility tiers: §10;
- unsupported/degraded/uncertain/accessibility/account-provider messaging: §11;
- release regression requirements and current TSK-0046 binding: §12.

## 15. Non-inference

This is L4 requirement-definition revalidation only. It does not prove implemented WCAG conformance, real assistive-technology execution, representative-parent accessibility/usability, current release support for any untested device, DNS mechanism support beyond its owning evidence, public support commitment, build/implementation, real-user processing, legal/privacy completion, publication/payment/market activation/launch, gate PASS or successor PASS.

**TSK-0314 current result candidate: PASS, subject to independent verification, durable evidence publication, guarded runtime reconciliation and exact GitHub read-back.**
