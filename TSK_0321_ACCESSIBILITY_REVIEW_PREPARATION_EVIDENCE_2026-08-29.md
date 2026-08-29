# TSK-0321 — Accessibility Review Preparation Evidence

**Date:** 2026-08-29  
**Task:** `TSK-0321 — Review design and content against accessibility requirements`  
**Acceptance:** `ACC-0321`  
**Verification:** preparation verification only; final `VER-0321` remains subject to HUMAN_ONLY owner disposition and verification of the approved remediation on the authoritative prototype  
**Evidence:** preparation evidence only; final `EVD-0321` not yet claimed  
**Action Authority:** `HUMAN_ONLY`  
**Disposition:** **REVIEW PREPARED / REMEDIATION VERIFIED AS OVERLAY / OWNER DECISION REQUIRED / NOT PASS**

## 1. Authority and scope

WBS authority requires the review to check every critical screen/state, record conformance evidence and remediation, and leave no unresolved critical accessibility barrier. TSK-0321 is L4, MEDIUM priority, depends on `TSK-0323; TSK-0324`, uses `ACC-0321 / VER-0321 / EVD-0321`, has AI capability A1 and Action Authority `HUMAN_ONLY`.

Current dependency/source context was pinned before review:

- `content/TSK-0323/DEVICE_SERVICE_INSTRUCTION_CATALOGUE.md` — blob `bbe9ed90b205f2ca852ebdaefedf054446dd7f91`;
- `prototype/TSK-0324/UI_COMPONENT_RULES.md` — blob `0b7012a12070f7eccf45a1bbb2f453fde8507ff6`;
- accepted TSK-0310 prototype:
  - `index.html` — `5d80dfdefb52042bc34468723354fefd325285e4`;
  - `model.mjs` — `01343273fd09c3c12d26f0c0eb1ae9a2fce10c91`;
  - `app.mjs` — `a4a0aff8848f8541e2581e333efbf48767c9f0ff`;
  - `prototype.css` — `439ef05dd04da7fccf01cb4b85e317a828389edf`;
- accepted TSK-0308 shared responsive system remains applicable.

No authoritative TSK-0310 source was modified during preparation.

## 2. Reusable review harness

`prototype/TSK-0321/accessibility-review.mjs` — blob `0cfca762a0d83be7716194e13e940876e71534b4`.

The harness performs 667 deterministic checks across the critical journey and states, including:

- document language, main landmark and logo alternative text;
- heading order and one-H1-per-screen;
- programmatic focus to screen H1 after transitions;
- native keyboard-operable controls and no positive tabindex;
- visible focus and minimum 24 CSS-pixel button target floor;
- contrast checks;
- textual evidence-state labels rather than color-only meaning;
- 200% text enlargement/reflow and critical-text clipping;
- 320/768/1024/1440 responsive overflow/bounded-frame behavior;
- Android/iPhone technical-value direction isolation under RTL stress;
- reduced motion;
- negative/uncertain/not-covered/removal/recovery states;
- no external requests, console errors or page errors.

## 3. Baseline review findings

Initial complete browser review run `33277211438`, job `99165918877`, on retained Chromium capability found 7 failures:

- five acceptance failures: 200% text enlargement caused page overflow on discovery, router, Android DNS, map and limitations;
- two design-conformance failures: Android/iPhone technical DNS values inherited RTL direction when the older prototype was mechanically mirrored.

All other tested semantics, keyboard behavior, normal-size responsive layouts, state truth, focus behavior, contrast, reduced motion, privacy/network and runtime checks passed.

The review therefore did **not** self-certify TSK-0321 and remediation was prepared separately.

## 4. Remediation candidate

`prototype/TSK-0321/REMEDIATION_CANDIDATE.css` — blob `5363c391cfdf96e4b454abb78f9ca4d8680caed1`.

The candidate is deliberately narrow and is **not applied** to authoritative TSK-0310 before owner approval. It:

1. allows shell/grid/action children to shrink with `min-width: 0`;
2. allows screen text to wrap under extreme enlargement with inherited `overflow-wrap: anywhere`;
3. permits topbar wrapping and badge wrapping;
4. isolates technical DNS values as `direction:ltr; unicode-bidi:isolate`.

The RTL rule aligns with the already accepted TSK-0308/TSK-0324 technical-value contract rather than introducing a new design rule.

## 5. Evidence-based debugging history

Remediation was narrowed using repeated full-suite and discriminating diagnostics rather than blind retries:

- initial 200% overflow was reduced while RTL failures were fully removed;
- shell `min-width:0` reduced the failure set to discovery/router/limitations and made Android DNS/map reflow pass;
- diagnostic run `33277574896`, job `99166885568` proved the remaining grid items had already shrunk to 224px, while long text retained `overflow-wrap:normal` and its `scrollWidth` exceeded the available width;
- the final candidate therefore added only inherited screen wrapping rather than changing typography, spacing, content or layout structure.

This closed the convergence WATCH condition with a direct observable verification gate.

## 6. Final candidate verification

Final full candidate-overlay verification:

- GitHub Actions run `33277610648`;
- job `99166984554`;
- runner `adguardvm`;
- Chromium `151.0.7922.34`;
- Playwright `1.62.0`;
- candidate blob `5363c391cfdf96e4b454abb78f9ca4d8680caed1`;
- accepted TSK-0310 source blobs unchanged.

Terminal results:

- `A11Y_CHECKS=667`;
- `A11Y_FAILURES=0`;
- `A11Y_ACCEPTANCE_FAILURES=0`;
- discovery 200% reflow PASS;
- router 200% reflow PASS;
- Android DNS 200% reflow PASS;
- map 200% reflow PASS;
- limitations 200% reflow PASS;
- Android technical-value RTL/LTR isolation PASS;
- iPhone technical-value RTL/LTR isolation PASS;
- contrast PASS (`body 13.46`, `heading 10.62`, `kicker 8.41`, `primary 10.62`, `focus 8.41`);
- 320/768/1024/1440 responsive checks PASS;
- visible focus, headings, keyboard-compatible controls, target floor, all evidence states, reduced motion, no external requests, no console/page errors PASS;
- `TSK0321_FULL_ACCESSIBILITY_CANDIDATE=PASS`;
- `POST_TEST_HEALTH=PASS`;
- `NO_TEST_LISTENER=PASS`;
- `REPOSITORY_CLEAN=PASS`.

AdGuard Home and Nginx were active before/after; the test server was loopback-only and removed.

## 7. Noncritical review notes

Two findings remain recorded but are not critical barriers to this internal prototype review:

- `A11Y-LIVE-001`: `main#app` currently uses broad `aria-live=polite` while screen transitions also focus H1. This can cause duplicate announcements in some assistive technologies. Production recommendation: retain H1 focus and scope live announcements to asynchronous feedback/status regions unless later manual screen-reader review demonstrates benefit from the broad region.
- `A11Y-SKIP-001`: the internal prototype has no visible skip link. Production repeated-navigation shells should provide a keyboard bypass mechanism; the existing `#app` main target can support it.

These are preserved for integrated-product accessibility verification and are not silently discarded.

## 8. HUMAN_ONLY boundary

The technically verified remediation candidate has not been applied to authoritative TSK-0310. Therefore TSK-0321 remains **WAITING / non-PASS** pending explicit Project Owner disposition.

Recommended exact approval:

`APPROVE TSK-0321 ACCESSIBILITY REMEDIATION AND REVIEW`

Approval authorizes applying the exact remediation candidate to the authoritative TSK-0310 prototype, rerunning the existing TSK-0310 rendered-browser acceptance plus the full 667-check TSK-0321 review against actual source, and—only if all applicable ACC/VER/EVD evidence remains proven—publishing final TSK-0321 acceptance evidence and reconciling runtime PASS.

Alternative owner disposition:

`REVISE TSK-0321: <specific change>`

No real-user/native-speaker validation, legal/privacy completion, production build, public publication, participant processing, payment, market activation or launch authority is inferred. `RSK-0002` remains OPEN and CR-0005 sequencing remains unchanged.
