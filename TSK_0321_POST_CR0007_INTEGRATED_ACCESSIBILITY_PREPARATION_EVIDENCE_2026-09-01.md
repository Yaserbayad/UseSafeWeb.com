# TSK-0321 — Post-CR-0007 Integrated Accessibility Preparation Evidence

**Task:** `TSK-0321 — Review design and content against accessibility requirements`  
**Date:** 2026-09-01  
**Current disposition:** `WAITING / HUMAN_APPROVAL_REQUIRED` after runtime reconciliation; this record does **not** claim PASS.  
**Action Authority:** current WBS `A1 / HUMAN_ONLY`.

## Current authority and dependency boundary

- Current WBS blob: `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`.
- Current TSK-0321 hard dependencies: `TSK-0323`, `TSK-0324`, `TSK-0333`; all are current-qualified durable PASS before this review.
- Current product boundary: accountless core plus optional parent account/session/minimum device persistence/lightweight dashboard under `DEC-0053 / CR-0006`, with `DEC-0054 / CR-0007` autonomy rules.
- Historical 2026-08-29 TSK-0321 approval/PASS is provenance only for the older pre-account surface; it cannot approve or satisfy this changed-scope review.
- Predecision runtime blob before this preparation record: `c86b04508452c3483d4b164d670ab32c538bde42`.

## Exact current integrated prototype reviewed

Authoritative TSK-0333 source remains unchanged during preparation:
- `prototype/TSK-0333/index.html` — `934dc19d00cc9dd32e1ebc20c604373d153d4013`
- `prototype/TSK-0333/model.mjs` — `fc25e4b1facc303840311e8ce186612eb8799212`
- `prototype/TSK-0333/app.mjs` — `98659ba74a86d539b89664708bbcb830292486f8`
- `prototype/TSK-0333/prototype.css` — `6f8af459a0b0b1c9ec132657dfcd7ebff43090b8`

Visible product identity remains `SafeWeb`; lowercase `usesafeweb.com` remains the technical/domain form. Current TSK-0333 brand revalidation evidence is `TSK_0333_SAFEWEB_BRAND_REVALIDATION_EVIDENCE_2026-09-01.md`, blob `f3ea3bf41c38050356a6e9e94aa251b07b35c5f3`, with full current-brand browser regression run/job `33479022852 / 99764278062`: SUCCESS.

## Current accessibility audit and defect discovery

Current browser/axe harness:
- `.github/scripts/verify_tsk0321_post_cr0007_accessibility_browser_20260901.mjs` — blob `b49b1c0aa81c5667b3059863c5bb5511077811f0`.

The harness reviews the actual current integrated prototype across accountless and optional-account surfaces, including keyboard/focus, skip navigation, heading structure, accessible names, target size, axe WCAG A/AA checks, responsive layouts, 200% text reflow, RTL technical-value isolation, reduced motion, evidence-state text, support/removal/recovery, provider/session failures, dashboard/device flows, destructive lifecycle confirmation/unknown-result handling, privacy/no-persistence, no external transport, and browser console/page errors.

Diagnostic history is retained rather than hidden:
1. Run/job `33485399789 / 99784177294` stopped on a strict-locator ambiguity in the verifier; no product assertion failed before that point.
2. Corrected run/job `33485640023 / 99784948005` reached the real current defect: `home-text-resize:200pct-overflow` at 320px viewport with 200% root text.
3. Diagnostic run/job `33485795010 / 99785441417`: SUCCESS and reproduced the failure with `documentScrollWidth=383` for a `320` viewport. Evidence localized the cause to intrinsic nested grid/flex sizing: current `.prototype-screen` was 256px wide while children/actions expanded to approximately 351px; action buttons retained intrinsic minimum width under enlarged text.

This is consistent with the shrinkability class of remediation already proven in the historical 2026-08-29 review, but the current candidate was independently adapted and verified against the dual-mode prototype.

## HUMAN_ONLY remediation candidate

Prepared candidate only; **not applied** to authoritative TSK-0333 source:
- `prototype/TSK-0321/POST_CR0007_REMEDIATION_CANDIDATE.css`
- blob `eb5242880974a936121f362df0d960746a596795`.

The candidate is bounded to layout accessibility:
- allows nested screen/content/grid/map/action/tool items to shrink with `min-width: 0`;
- allows long screen/control text to wrap with `overflow-wrap: anywhere`;
- caps action/tool buttons at `max-width: 100%`.

It changes no product wording, evidence-state semantics, DNS values, account/session/device behavior, lifecycle consequences, persistence, privacy rules, or backend/runtime configuration.

## Deterministic target-browser candidate verification

Focused regression verifier:
- `.github/scripts/verify_tsk0321_200pct_candidate_20260901.mjs` — blob `cfab324aed37e4074f54a906b014eb62d9f5ac74`.

Final preparation workflow:
- `.github/workflows/verify-tsk0321-post-cr0007-remediation-candidate-v2-20260901.yml` — blob `9b7b8f46dd9de0d5c7f2982ce49e5d03450f53f7`.

Final run/job:
- `33486312320 / 99787090076` — **SUCCESS** on self-hosted `adguardvm`.
- Node `22.23.2`, npm `10.9.8`, Playwright `1.62.0`, axe-core `4.10.3`, Chromium `151.0.7922.34`.

The candidate was appended only inside the disposable workflow workspace; GitHub authoritative TSK-0333 CSS remained blob `6f8af459a0b0b1c9ec132657dfcd7ebff43090b8`.

### Focused RED → GREEN proof

- Previous authoritative source: `320` viewport → `383` document scroll width, FAIL.
- Candidate overlay: `TSK0321_200PCT_VIEWPORT=320`.
- Candidate overlay: `TSK0321_200PCT_SCROLLWIDTH=320`.
- `TSK0321_200PCT_REMEDIATION=PASS`.
- `TSK0321_CANDIDATE_FOCUSED_GREEN=PASS`.

### TSK-0333 full current-brand regression under candidate

The exact current SafeWeb-brand assertion adjustment already proven by TSK-0333 brand revalidation was used; product copy was not changed.

All full integrated browser markers passed, including keyboard, Android/iPhone, accountless map, false-positive truth, removal/recovery, unsupported path, new account, explicit device save, returning dashboard, replacement, destructive-result uncertainty/record deletion, provider error, session/logout/account-delete boundaries, RTL/responsive, privacy/no-transport and no console errors.

Final markers:
- `TSK0333_POST_CR0007_BROWSER_VERIFICATION=PASS`
- `TSK0333_CANDIDATE_REGRESSION=PASS`.

### TSK-0321 full current integrated accessibility review under candidate

Final markers:
- `TSK0321_SKIP_LINK=PASS`
- `TSK0321_ACCOUNTLESS_CORE_STATES=PASS`
- `TSK0321_SUPPORT_REMOVAL_RECOVERY=PASS`
- `TSK0321_RTL_TECHNICAL_VALUES=PASS`
- `TSK0321_NEW_ACCOUNT_STATES=PASS`
- `TSK0321_PROVIDER_ERROR_FALLBACK=PASS`
- `TSK0321_DASHBOARD_DEVICE_STATES=PASS`
- `TSK0321_DEVICE_DESTRUCTIVE_LIFECYCLE=PASS`
- `TSK0321_SESSION_EXPIRY_FALLBACK=PASS`
- `TSK0321_ACCOUNT_LIFECYCLE=PASS`
- `TSK0321_PRIVACY_CONTENT=PASS`
- `TSK0321_RESPONSIVE_TEXT_RESIZE=PASS`
- `TSK0321_REDUCED_MOTION=PASS`
- `TSK0321_NO_EXTERNAL_OR_PERSISTENCE=PASS`
- `TSK0321_AUDITED_UNIQUE_SCREENS=28`
- `TSK0321_ACCESSIBILITY_CHECKS=1500`
- `TSK0321_POST_CR0007_MECHANICAL_ACCESSIBILITY_REVIEW=PASS`
- `TSK0321_CANDIDATE_FULL_ACCESSIBILITY=PASS`
- `TSK0321_AUTHORITATIVE_PRODUCT_NOT_MUTATED=PASS`.

No current critical accessibility defect remains in the verified candidate. This is mechanical/target-browser evidence; it does not fabricate real-user or assistive-technology human validation beyond the current L4 task contract.

## Human authority boundary

Because TSK-0321 is `A1 / HUMAN_ONLY`, preparation stops here. The historical approval does not authorize the new post-CR-0007 remediation or its application.

Exact Project Owner resolution command:

`APPROVE TSK-0321 POST-CR-0007 ACCESSIBILITY REMEDIATION AND REVIEW`

If approved, the next governed sequence is strictly:
1. fresh-read authority and exact candidate identity;
2. apply only the verified candidate to authoritative `prototype/TSK-0333/prototype.css`;
3. reread exact resulting GitHub CSS blob/commit;
4. rerun focused 200% verification on authoritative source;
5. rerun full current SafeWeb TSK-0333 browser regression on authoritative source;
6. rerun the full TSK-0321 integrated accessibility suite against authoritative source with no overlay;
7. create final owner-bound acceptance evidence;
8. reconcile TSK-0321 to PASS only if every applicable current acceptance condition is proven; reread runtime commit/blob;
9. recompute downstream eligibility. No successor or gate inherits PASS automatically.

Until that approval and successful post-application verification, TSK-0321 remains non-PASS and no LG-06/downstream readiness is inferred.
