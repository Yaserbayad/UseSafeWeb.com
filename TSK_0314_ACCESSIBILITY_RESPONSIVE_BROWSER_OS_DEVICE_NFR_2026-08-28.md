# TSK-0314 — Accessibility, Responsive, Browser, OS and Device-Support NFRs

**Task:** TSK-0314 — Define accessibility, responsive, browser, OS, and device support NFRs  
**Acceptance:** ACC-0314  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** INTERNAL PROVISIONAL L4 ACCESSIBILITY/SUPPORT CONTRACT / IMPLEMENTATION OR PUBLIC SUPPORT COMMITMENT NOT AUTHORIZED  
**Date:** 2026-08-28  
**Authority:** TSK-0046 + REQ-0044/REQ-0019 + CON-0017 + INT-0012 + current Protection Map/state/accountless contracts + current accepted device/DNS evidence + DEC-0050/CR-0003  
**Verification state:** PASS candidate pending independent verification and runtime reconciliation.

## 1. Scope and ownership boundary

This contract defines the **web/product UI** accessibility, responsive behavior, browser/OS support policy, device test tiers and unsupported-state messaging for UseSafeWeb.

It does **not** widen or replace the separately owned DNS installation/mechanism support matrix. In particular:

- browser/web-UI support does not prove that a device/OS supports an approved UseSafeWeb DNS configuration mechanism;
- DNS install/verification/removal support remains owned by the platform/DNS contracts and accepted device evidence (including the accepted Android native Private DNS/DoT and iPhone/iOS DoH-profile pilot paths);
- a browser working on a device never upgrades an untested DNS mechanism to supported;
- an unsupported DNS mechanism may still be explained accessibly in the web UI without being claimed supported;
- language availability does not itself activate a country/market/legal/support commitment under CON-0017.

No dedicated current TSK-0409 artifact was located by repository filename/content search during this task, so this contract does not invent detailed TSK-0409 content. It relies only on current canonical runtime evidence and already accepted platform/DNS task evidence for the boundary above.

`RSK-0002` remains OPEN. This task does not supply representative-parent usability, comprehension or accessibility evidence and does not authorize implementation/build, participant testing, publication or launch.

## 2. Accessibility conformance target

### 2.1 Normative target

The target for all public/product web UI in scope is **WCAG 2.2 Level AA**.

Current W3C sources checked on 2026-08-28:

- WCAG 2.2 recommendation/overview: `https://www.w3.org/TR/WCAG22/`
- WAI WCAG 2 overview: `https://www.w3.org/WAI/standards-guidelines/wcag/`

UseSafeWeb must satisfy every applicable Level A and AA success criterion in the implemented release before claiming WCAG 2.2 AA conformance. AAA techniques may be adopted where useful but **no AAA conformance claim** is created by this NFR.

Automated accessibility tooling alone cannot prove conformance; manual keyboard, screen-reader, resize/reflow and visual review are release-blocking parts of the verification contract.

### 2.2 Accessibility is part of correctness

Accessibility failures that prevent a parent from starting, understanding, configuring, verifying, recovering, removing or interpreting Protection Map state are functional failures, not cosmetic defects.

Accessibility must never be traded away to reduce implementation effort, page weight or time-to-release.

## 3. Keyboard and focus behavior

Every interactive function must be fully operable without a pointing device.

Requirements:

1. all controls use native semantic elements where possible;
2. all functionality is reachable and operable with keyboard alone;
3. focus order follows the logical reading/action sequence;
4. no keyboard trap is permitted;
5. visible focus indication must remain clear against the current background/state;
6. focused components must not be fully obscured by sticky headers, dialogs, banners or overlays;
7. modal/dialog focus is moved into the dialog, contained while modal, and returned to the invoking control on close where that remains valid;
8. skip-to-main-content or equivalent direct navigation is available on repeated page structures;
9. hover-only or pointer-gesture-only functionality is prohibited for required actions;
10. drag/complex gestures require an accessible single-pointer/keyboard alternative when applicable;
11. keyboard activation must not trigger duplicate actions merely because both key and click handlers exist.

Protection/setup state changes that occur after an action must move or announce focus only when needed for comprehension; focus must not jump unpredictably.

## 4. Screen-reader and semantic behavior

### 4.1 Semantic structure

Use native HTML semantics first. ARIA supplements semantics only when native behavior cannot express the component.

Every page/flow must provide:

- one meaningful page title and primary heading;
- logical heading hierarchy;
- major landmarks (`main`, navigation, header/footer where applicable);
- accessible names for all interactive controls;
- programmatic form labels, instructions and required/invalid state;
- errors linked to the affected field/control and summarized where multiple errors exist;
- current step/progress conveyed semantically, not only visually;
- status messages exposed through an appropriate live-region/status mechanism when an asynchronous change needs announcement;
- decorative graphics hidden from the accessibility tree;
- informative graphics with equivalent accessible text.

### 4.2 Protection Map and verification semantics

The Phone / Internet / Services Protection Map must expose each layer independently with its exact current TSK-0320 state meaning.

- color, icon or position alone cannot communicate state;
- S1 verified and S2 parent-confirmed/configured must remain distinguishable in accessible text;
- S3 Action needed, S4 Not covered, S5 Status uncertain/error and S6 Removed must have explicit text labels;
- no screen-reader-only text may silently strengthen a claim beyond the visible copy;
- verification progress/failure must be announced without reading raw technical/DNS data to the user.

## 5. Text resize, zoom and reflow

The implementation must meet WCAG 2.2 AA resize/reflow requirements, including:

- text can be resized to **200%** without loss of content or functionality except where a specific WCAG exception applies;
- content reflows without two-dimensional scrolling at a width equivalent to **320 CSS pixels** except content that legitimately requires two-dimensional layout under WCAG;
- no fixed-height control/container may clip translated or enlarged text;
- labels, buttons and cards must expand/wrap rather than truncate critical instructions/status;
- browser zoom and OS text scaling must not hide required controls;
- orientation is not locked unless a genuine essential exception exists;
- English, Turkish and Arabic/RTL expansion must be included in resize/reflow tests.

Internal design preference: target layouts should remain usable at higher zoom/text scaling beyond the minimum whenever practical. That preference is not substituted for the normative WCAG test.

## 6. Contrast, color, target size and motion

### 6.1 Contrast and color

At minimum:

- normal text contrast >=4.5:1;
- large text contrast >=3:1;
- applicable non-text UI/component/state boundaries >=3:1;
- status/error/success cannot be communicated by color alone;
- links within body text must remain distinguishable without relying solely on color unless the applicable contrast/interaction exception is satisfied.

### 6.2 Target size

Interactive targets must satisfy WCAG 2.2 AA **Target Size (Minimum)** requirements, including a minimum 24 by 24 CSS-pixel target or valid spacing/exception condition. The product design should generally use larger comfortable touch targets for primary setup/recovery actions where layout permits.

### 6.3 Motion

- honor `prefers-reduced-motion` for nonessential animation;
- no essential instruction/state may depend on animation alone;
- avoid flashing content that can violate seizure-safety criteria;
- loading/verification motion must have a non-motion semantic status equivalent.

## 7. Responsive and multilingual/RTL behavior

### 7.1 Responsive baseline

The web/product UI is mobile-first and must remain functional from **320 CSS px viewport width** through wide desktop layouts.

Required test shapes include:

- narrow phone portrait;
- phone landscape;
- tablet portrait/landscape;
- desktop/laptop;
- 200% browser zoom/reflow case;
- enlarged OS text case where the browser exposes it.

Critical actions must not be hidden merely because viewport height is small, browser chrome changes, or an on-screen keyboard appears.

### 7.2 Arabic RTL

Arabic UI must use real RTL layout behavior, not mirrored screenshots or manual per-component hacks.

- use CSS logical properties where practical;
- navigation/order follows the language direction while preserving logical task sequence;
- icons with directional meaning are mirrored only when semantics require it;
- numerals, resolver hostnames, URLs, IP-like technical strings, code/config snippets and tokens use safe bidirectional isolation/direction so they remain readable and copyable;
- focus order and DOM reading order remain logical rather than visually reversed through CSS tricks;
- English/Turkish remain LTR.

A translated surface is not considered supported merely because strings fit; it must pass the same accessibility/reflow/state tests.

## 8. Browser and OS support policy

### 8.1 Normative release policy

Because evergreen browser versions change frequently, permanent support is defined by a deterministic **release-time matrix**, not frozen forever to the August 2026 numbers below.

For every release candidate:

- **Chromium desktop:** current Stable major and immediately previous Stable major for Chrome; current Stable and immediately previous Stable major for Edge where available on the supported OS;
- **Firefox desktop:** current Release major and immediately previous Release major;
- **Safari desktop:** current security-supported Safari major on current security-supported macOS, plus the immediately previous Safari/macOS combination when Apple still supplies security updates and the required web features behave correctly;
- **iPhone/iPad web UI:** Safari/WebKit on current security-supported iOS/iPadOS; the active legacy security branch is Tier 2 unless it passes the full Tier-1 release suite;
- **Android web UI:** Chrome current Stable and immediately previous Stable on Android versions still receiving vendor security updates, with Android 16 and Android 17 included in the current release test matrix;
- embedded/in-app browsers are not Tier 1 by default unless separately tested and promoted.

Only stable/release channels count as supported production browsers. Beta/Dev/Canary/preview OS/browser builds are compatibility-observation environments, not production-support proof.

### 8.2 Dated compatibility snapshot — 2026-08-28

This snapshot records what the policy means today and must be refreshed at release time:

| Surface | Current snapshot / test baseline | Support disposition |
| --- | --- | --- |
| Chrome desktop | Chrome 152 Stable is current; test 152 + 151 | Tier 1 browser matrix |
| Edge desktop | Edge 152 release week begins 2026-08-27; current release matrix must verify installed Stable before sign-off; retain 151 until 152 Stable is directly confirmed in target test environment | Tier 1 once stable version is confirmed |
| Firefox desktop | Firefox 154 Release current (2026-08-18); test 154 + 153 | Tier 1 browser matrix |
| Safari/macOS | Safari 26.6.1 current security release; Apple currently lists macOS 26.6.2 plus security updates for Sequoia 15.7.9 and Sonoma 14.8.9 | Tier 1 current Safari/macOS; older supported macOS rotational Tier 2 unless full suite passes |
| iOS/iPadOS web | iOS/iPadOS 26.6.1 current; Apple also publishes iOS/iPadOS 18.7.10 for legacy supported hardware | 26.x Tier 1 candidate; 18.7.x Tier 2 until full suite proves Tier 1 |
| Android web | Android 17 (API 37) is a released AOSP platform; Android 16 remains a current prior major; August 2026 security patch level is current | Android 17 + 16 Tier 1 candidates on security-updated devices |

Current authoritative sources checked 2026-08-28:

- Chrome Releases: `https://chromereleases.googleblog.com/2026/08/`
- Firefox release notes: `https://www.firefox.com/en-US/releases/`
- Edge release schedule/release notes: `https://learn.microsoft.com/deployedge/microsoft-edge-release-schedule`
- Apple security releases: `https://support.apple.com/100100`
- Android 17/AOSP build numbers: `https://source.android.com/docs/setup/reference/build-numbers`
- Android Security Bulletin August 2026: `https://source.android.com/docs/security/bulletin/2026/2026-08-01`

### 8.3 OS/browser support does not equal DNS support

The release matrix above determines whether the **web UI** is supported. The DNS setup flow must separately consult its owning platform/mechanism support authority.

Examples:

- a web page passing in an older iPhone browser does not prove its UseSafeWeb DNS-profile install/verification path is supported;
- Android web compatibility does not prove Private DNS coexistence with a particular VPN/app/network;
- desktop browser support does not imply UseSafeWeb DNS is installed/configured on the desktop OS.

The product must render the correct web UI support state and DNS-mechanism state independently.

## 9. Device and accessibility test tiers

### Tier 0 — automated every change

Release engineering should automate, where the implementation exists:

- semantic/lint checks;
- automated WCAG rule checks (for example axe-equivalent rules);
- keyboard-smoke and focus-order checks for critical flows where reliable;
- viewport/reflow tests at narrow mobile and desktop widths;
- LTR/RTL visual regression for critical states;
- supported browser automation for critical routing/state rendering.

Tier 0 catches regressions but **cannot certify WCAG conformance**.

### Tier 1 — release-blocking manual + automated

Before public release of the web UI, test the entire critical accountless journey on at least:

1. iPhone / current supported iOS Safari + **VoiceOver**;
2. security-supported Android 16/17 device / current Chrome + **TalkBack**;
3. Windows 11 / supported Chrome plus **NVDA** on at least one Chromium run;
4. Windows 11 / supported Firefox + keyboard/manual screen-reader compatibility sampling;
5. current supported macOS / Safari + **VoiceOver**;
6. narrow phone and 320-CSS-pixel reflow/200%-resize conditions;
7. English, Turkish and Arabic RTL critical-flow variants.

Release-blocking manual checks cover keyboard-only operation, visible/unobscured focus, labels/names/roles/states, form errors, async verification announcements, Protection Map semantics, resize/reflow, contrast/state distinguishability and recovery/removal paths.

### Tier 2 — compatibility rotation

Use for the immediately previous supported browser/OS combinations and representative secondary devices/form factors. Test at least the critical start/setup/verification/Protection Map/recovery route plus major accessibility regressions.

A Tier-2 combination may be promoted to Tier 1 only after it passes the full Tier-1 suite and its DNS mechanism (if claimed) is separately supported.

### Tier 3 — unsupported/best-effort observation

Legacy/out-of-support OS versions, obsolete browsers, preview builds and untested embedded/in-app browsers may be observed for graceful behavior but receive **no supported claim**.

Do not spend correctness/security/privacy budget maintaining a Tier-3 platform when the vendor no longer supplies security updates or required web primitives cannot be implemented safely.

## 10. Unsupported, degraded and uncertain messaging

The UI must distinguish the reason support is unavailable instead of collapsing everything into a generic error.

### A. Unsupported web/browser/OS

Use when the web UI itself is outside the supported/tested matrix.

Required meaning:

> This browser or operating-system version is not currently supported/tested for the UseSafeWeb setup experience. Update or use a supported browser/device before relying on this setup flow.

Do not claim that existing DNS protection is absent solely because the browser is unsupported.

### B. Web UI works, DNS setup mechanism not covered

Use when the page is supported but the device/network/DNS configuration combination is not supported by its owning platform matrix.

Map to the appropriate TSK-0320 **S4 Not covered** semantics. Explain the supported alternatives if one exists. Do not improvise a DoH/DoT/profile/VPN workaround.

### C. Support exists but verification is inconclusive

Use TSK-0320 **S5 Status uncertain/error** when the supported combination cannot currently be verified because evidence is conflicting/inconclusive or the verification path failed.

Do not map S5 to S1/S2 merely because setup instructions were followed or the parent confirms completion.

### D. Accessibility barrier discovered

If a release-blocking accessibility defect prevents completion/recovery/understanding on a claimed Tier-1 combination, that combination/flow cannot remain represented as fully supported until the defect is corrected and regression-tested. Provide an accessible alternative path only if it is genuinely equivalent and does not create a hidden human-support dependency.

Unsupported/degraded messages themselves must be accessible, translatable and RTL-safe.

## 11. Release acceptance and regression rules

A web release cannot claim the TSK-0314 supported matrix unless:

1. all applicable WCAG 2.2 A/AA requirements are verified for the implemented critical flow;
2. no critical keyboard/screen-reader/resize/reflow blocker remains on Tier 1;
3. every Tier-1 browser/OS/device combination has current release evidence;
4. exact release browser/OS versions are recorded rather than relying only on this dated snapshot;
5. English/Turkish/Arabic RTL critical-flow checks pass;
6. Protection Map and verification states remain semantically truthful;
7. unsupported/degraded/uncertain paths have accessible copy and recovery;
8. the DNS mechanism support matrix is checked separately before making any setup-support claim;
9. automated accessibility findings have been triaged and manual checks completed;
10. accessibility evidence identifies exact product release/build and test environment.

A browser engine/OS update that changes semantics, focus, storage, profile-download behavior, networking, rendering or assistive-technology interaction triggers targeted regression before continued support is assumed.

## 12. Change/revalidation triggers

Reopen affected TSK-0314 evidence when:

- W3C publishes a materially relevant new normative WCAG version/erratum or project accessibility target changes;
- a Tier-1 browser/OS major changes;
- vendor security support ends for a supported OS/browser;
- a new browser engine/device class is promoted to supported;
- the owning DNS platform/mechanism matrix changes;
- core component/design-system semantics change;
- routing/state/Protection Map behavior changes;
- English/Turkish/Arabic content or RTL layout changes materially;
- real accessibility/usability evidence contradicts an assumption;
- a material accessibility defect/incident is found in production/pilot evidence.

## 13. Testable implementation assertions

A downstream implementation/QA suite must prove at least:

1. WCAG 2.2 AA is the target and no premature conformance claim exists;
2. every critical action works by keyboard only;
3. focus order is logical, visible and not fully obscured;
4. no keyboard trap exists;
5. semantic names/roles/states/labels/errors are correct;
6. async verification/status changes are announced appropriately;
7. Protection Map S1–S6 states are conveyed in text/semantics, not color alone;
8. 200% text resize retains content/functionality;
9. 320-CSS-pixel reflow retains content/functionality except valid WCAG exceptions;
10. contrast and target-size requirements pass;
11. reduced-motion preference is respected for nonessential motion;
12. Arabic RTL critical flow has logical DOM/focus order and safe bidi rendering for technical strings;
13. browser/OS support is derived from a release-time version matrix, not stale memory;
14. Chrome/Firefox current+previous and current Safari/Edge policy are tested as specified;
15. Android/iOS mobile web tests are separate from DNS mechanism support;
16. Tier-1 VoiceOver/TalkBack/NVDA/manual keyboard checks are completed;
17. automated scanning is not accepted as sole WCAG evidence;
18. unsupported web, unsupported DNS and uncertain verification states are distinct;
19. unsupported states never become S1 verified by fallback/confirmation;
20. exact release/build/browser/OS/device/assistive-technology versions are bound to evidence.

## 14. ACC-0314 traceability

ACC-0314 requires:

> Requirements define target WCAG level, keyboard/screen-reader/text-resize behavior, supported browsers/OS versions, device test tiers, and unsupported-state messaging.

Coverage:

- **Target WCAG level:** §2 freezes WCAG 2.2 AA.
- **Keyboard:** §3 defines operation, order, focus, traps and modal/gesture behavior.
- **Screen reader:** §4 defines native semantics, names/roles/states, errors/status and Protection Map semantics.
- **Text resize/reflow:** §5 defines 200% text resize and 320-CSS-pixel reflow plus translation/RTL resilience.
- **Supported browsers/OS versions:** §8 defines a deterministic release policy and a dated 2026-08-28 compatibility snapshot.
- **Device test tiers:** §9 defines Tier 0 automated, Tier 1 release-blocking, Tier 2 rotational and Tier 3 unsupported/best-effort.
- **Unsupported-state messaging:** §10 separates web unsupported, DNS mechanism not covered, verification uncertain and accessibility-blocker states.

## Stable task outcome candidate

**TSK-0314 result: PASS candidate for provisional internal L4 accessibility/responsive/browser/OS/device-support-NFR definition only, subject to independent verification, GitHub read-back and runtime reconciliation.**

This result does not prove implemented WCAG conformance, representative-parent accessibility/usability, a DNS mechanism beyond its owning support matrix, web-app implementation, market activation, publication or launch.
