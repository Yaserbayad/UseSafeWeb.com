# TSK-0314 — Accessibility/Responsive/Browser/OS/Device NFR Verification Evidence

**Task:** TSK-0314 — Define accessibility, responsive, browser, OS, and device support NFRs  
**Acceptance:** ACC-0314  
**Verification:** VER-0314 — independent accessibility/support/scope-boundary audit  
**Evidence:** EVD-0314  
**Date:** 2026-08-28  
**Result:** PASS candidate pending GitHub read-back and guarded runtime reconciliation

## 1. Exact evidence index

- NFR contract: `TSK_0314_ACCESSIBILITY_RESPONSIVE_BROWSER_OS_DEVICE_NFR_2026-08-28.md`
- Contract blob: `3c46d565251ecaec6860d87f18f21fbb22ac3e6d`
- Contract creation commit: `59191343ebbd187f253fc51c363af512fb7e8287`
- Current selected runtime: `CURRENT_STATE.md` blob `28004778adb0e4fed57c42f6e45e3b7ca60fae59`; TSK-0314 selected L4 / MEDIUM / A3 / AUTO_ALLOWED with TSK-0046 current PASS.
- WBS: `Plans/Master/WBS/master-wbs.csv`, blob `dce5b829c4d447eac180ae1e896e0019292cf971`.
- Current accepted device/DNS evidence referenced by canonical runtime includes TSK-0511 (Android native Private DNS/DoT and iPhone/iOS DoH profile) and TSK-0514 (external cellular/removal/recovery). These establish current tested DNS paths but are not expanded by TSK-0314.
- Current W3C WCAG 2.2 source: `https://www.w3.org/TR/WCAG22/` and WAI overview `https://www.w3.org/WAI/standards-guidelines/wcag/`.
- Current browser/OS release sources checked 2026-08-28: Chrome Releases August 2026; Firefox Release Notes; Microsoft Edge release schedule/release notes; Apple security releases; Android 17/AOSP build numbers; Android August 2026 Security Bulletin.

## 2. Eligibility and scope-ownership audit

The post-TSK-0046 queue identified TSK-0314 as the only dependency-ready AUTO_ALLOWED L4 candidate with no preflight flag; TSK-0187 remains real/behavior-evidence-bound and TSK-0140 remains owner-review-bound. The guarded selector completed successfully before execution.

The contract is expressly limited to **web/product UI accessibility, responsive behavior and browser/OS/device support**. It does not claim ownership of DNS installation/mechanism compatibility.

Repository search did not locate a dedicated current TSK-0409 artifact by filename/content. The contract therefore does not invent one and instead uses only current canonical runtime/accepted device evidence to state the separation boundary.

**Result: PASS.**

## 3. WCAG-level audit

ACC-0314 requires a target WCAG level. Section 2 freezes **WCAG 2.2 Level AA** for all in-scope public/product web UI.

It correctly requires all applicable A and AA success criteria before an implemented release may claim conformance, does not claim AAA, and does not treat automated scanning as sufficient evidence.

This is aligned with current W3C WCAG 2.2 authority.

**Result: PASS.**

## 4. Keyboard/focus audit

Section 3 makes all required functionality keyboard operable and defines:

- semantic native controls where possible;
- logical focus order;
- no keyboard traps;
- visible focus;
- focused content not fully obscured;
- modal focus entry/containment/return;
- skip-to-main behavior;
- no hover/pointer-only required action;
- accessible alternatives for complex pointer gestures;
- protection against duplicate key/click activation.

These requirements are specific enough for implementation and release tests.

**Result: PASS.**

## 5. Screen-reader/semantic-state audit

Section 4 requires semantic page/landmark/heading/form structure, accessible names/roles/states, programmatic errors/instructions, status announcements and meaningful alternatives for graphics.

Protection Map accessibility preserves the owning state semantics:

- Phone/Internet/Services remain independently exposed;
- S1 verified and S2 configured/parent-confirmed remain distinguishable;
- S3/S4/S5/S6 have explicit textual semantics;
- color/icon/position alone cannot convey state;
- screen-reader-only copy cannot strengthen the visible protection claim.

Therefore accessibility cannot become a backdoor for false verification.

**Result: PASS.**

## 6. Text-resize/reflow audit

Section 5 includes the required measurable behavior:

- 200% text resize without loss of content/functionality except applicable WCAG exceptions;
- reflow at 320 CSS pixels without prohibited two-dimensional scrolling;
- no critical clipping from fixed-height containers;
- translated/enlarged labels/cards wrap and expand;
- zoom/OS scaling cannot hide required controls;
- orientation is not locked absent an essential exception;
- English/Turkish/Arabic-RTL variants are in the reflow matrix.

**Result: PASS.**

## 7. Contrast/target/motion audit

Section 6 defines:

- >=4.5:1 normal text contrast;
- >=3:1 large text and applicable non-text UI contrast;
- no color-only status/error/success meaning;
- WCAG 2.2 AA Target Size (Minimum), 24x24 CSS pixels or valid exception/spacing condition;
- `prefers-reduced-motion` handling;
- no essential animation-only content or unsafe flashing;
- semantic status alternative for loading/verification motion.

**Result: PASS.**

## 8. Responsive/RTL audit

Section 7 defines a mobile-first 320-CSS-pixel-through-desktop baseline, portrait/landscape/tablet/desktop/zoom/text-scaling test shapes, and prevents critical actions from disappearing because of browser chrome or on-screen keyboard changes.

Arabic is treated as real RTL:

- logical CSS properties;
- semantic directional icon handling;
- bidi isolation/direction for URLs/hostnames/code-like technical strings;
- logical DOM/focus order rather than CSS-only visual reversal;
- same accessibility/reflow obligations as English/Turkish.

This is consistent with CON-0017 while explicitly refusing to equate translated availability with market/legal/support activation.

**Result: PASS.**

## 9. Browser/OS version-policy audit

ACC-0314 requires supported browser/OS versions. Section 8 satisfies this in two layers:

1. a durable release-time policy for rapidly changing evergreen browsers/OSes; and
2. a dated 2026-08-28 compatibility snapshot proving the policy is concrete today.

Current external facts checked:

- Chrome 152 promoted to Stable on 2026-08-25; previous stable major 151 remains the immediate previous-major test target;
- Firefox 154 Release was first offered 2026-08-18; previous major 153 is directly documented;
- Microsoft Edge schedule places Edge 152 Stable in the week of 2026-08-27; the contract conservatively requires direct installed-Stable confirmation and retains 151 until that is observed rather than overclaiming rollout status;
- Apple current security releases list iOS/iPadOS 26.6.1, macOS 26.6.2, Safari 26.6.1, with security-maintained iOS/iPadOS 18.7.10 and macOS Sequoia/Sonoma updates;
- AOSP build-number authority lists Android 17 / API 37 and Android 16 as the current/prior major platform families; the August 2026 Android Security Bulletin establishes current patch-level authority.

The normative support policy requires stable/release channels and vendor-security-supported OS versions; preview/beta builds are compatibility observation only. Exact browser/OS versions must be refreshed and bound to each release candidate rather than silently relying on this snapshot.

**Result: PASS.**

## 10. Web-support vs DNS-support audit

The contract repeatedly and correctly distinguishes:

- web UI browser/OS support;
- DNS installation/mechanism support;
- current verification state.

A web-compatible iPhone/Android/desktop does not thereby gain a supported UseSafeWeb DNS mechanism. Likewise an unsupported browser does not prove that an already-configured DNS path is unprotected.

This prevents TSK-0314 from silently broadening current accepted Android/iPhone DNS support or inventing VPN/network coexistence.

**Result: PASS.**

## 11. Device-test-tier audit

Section 9 defines four explicit tiers:

- Tier 0 automated every change;
- Tier 1 release-blocking manual + automated;
- Tier 2 compatibility rotation for previous/secondary combinations;
- Tier 3 unsupported/best-effort observation.

Tier 1 includes current iOS Safari + VoiceOver, Android 16/17 Chrome + TalkBack, Windows 11 Chrome/NVDA and Firefox/keyboard sampling, current macOS Safari + VoiceOver, narrow/reflow/resize conditions, and English/Turkish/Arabic RTL critical flows.

It explicitly states automation cannot certify WCAG conformance.

**Result: PASS.**

## 12. Unsupported-state messaging audit

Section 10 distinguishes four materially different cases:

1. unsupported web/browser/OS;
2. web UI supported but DNS mechanism not covered -> TSK-0320 S4;
3. supported combination but verification inconclusive -> TSK-0320 S5;
4. release-blocking accessibility barrier on a claimed Tier-1 combination.

Unsupported browser status does not imply DNS protection failure; S5 cannot be upgraded to S1/S2 from setup completion/parent confirmation; unsupported/degraded messages themselves must be accessible, translatable and RTL-safe.

**Result: PASS.**

## 13. Release/change-control audit

Sections 11–12 require exact release/build/browser/OS/device/assistive-technology evidence and targeted regression on WCAG changes, browser/OS support changes, DNS support-matrix changes, component/state/RTL changes and material accessibility defects.

No implemented WCAG conformance, public support promise, market activation or participant accessibility evidence is claimed by this definition task.

**Result: PASS.**

## 14. Verification disposition

**VER-0314 independent audit result: PASS for ACC-0314's provisional internal L4 accessibility/responsive/browser/OS/device-support-NFR-definition scope.**

The read-back contract at blob `3c46d565251ecaec6860d87f18f21fbb22ac3e6d` satisfies every ACC-0314 domain: WCAG target, keyboard behavior, screen-reader behavior, text resize/reflow, supported browser/OS policy and current version snapshot, device test tiers and truthful unsupported-state messaging.

The following remain OPEN/non-PASS and are not converted by this result:

- actual web UI implementation;
- implemented WCAG 2.2 AA conformance evidence;
- manual assistive-technology release testing;
- representative-parent accessibility/usability/comprehension evidence (`RSK-0002`);
- any DNS mechanism beyond its separately owned accepted support matrix;
- final legal/privacy/participant/market gates;
- build/publication/launch.

**Runtime may move TSK-0314 to PASS only after this evidence file is persisted/read back and a guarded reconciliation verifies current selection, exact contract/evidence/WBS/runtime preconditions.**
