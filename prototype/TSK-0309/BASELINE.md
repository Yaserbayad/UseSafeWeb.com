# TSK-0309 — Implementation-Ready Experience Baseline

**Version:** 1.0.0  
**Status:** frozen internal L4 implementation contract  
**Owner:** UX  
**Action authority:** A3 / AUTO_ALLOWED  
**Decision basis:** DEC-0052 / CR-0005  
**Human-validation claim:** none; this baseline is accepted from current owner/product/source-backed/internal/automated target-environment evidence.

## 1. Purpose and engineering handoff

This file freezes the current accountless SafeWeb public-to-setup experience for downstream implementation. Engineering must be able to implement the critical experience without inventing states, content semantics, error/recovery behavior, account requirements, or protection claims.

The accepted representative implementation is `prototype/TSK-0310/` and remains the behavioral reference. TSK-0309 does **not** introduce speculative product scope or redesign the accepted prototype merely to create a new artifact.

Current higher authority is DEC-0052 / CR-0005. Any older accepted L4 artifact that still describes CR-0003/CR-0004 or TSK-0187 as a current pre-build behavioral gate is superseded **for sequencing only**. Its valid brand, content, state, accessibility, and product rules remain usable unless separately contradicted by current authority.

## 2. Frozen product boundary

The implementation baseline is accountless-first and minimum:

- no mandatory UseSafeWeb account;
- no Login or customer account/dashboard surface in this baseline;
- no persistent parent identity or customer-facing AdGuard administration;
- no child account;
- no browsing/activity-history product surface;
- no broad DNS administration console;
- no native app, school portal, public API/integration platform, or other deferred scope;
- no card/trial/payment before core value;
- no routine human-support dependency in the critical journey.

Optional persistence/account/dashboard remains outside this baseline and may activate only through its separate current exception/owner-authority path. The owner’s sequencing decision does not itself activate that scope.

## 3. Frozen critical journey

The implementation must cover the complete critical journey required by REQ-0031:

1. **Discovery** — bounded proposition, limitations available, `Start setup` action.
2. **Router** — choose `Android`, `iPhone`, or unsupported/other.
3. **Native safeguard** — explicitly record either parent-confirmed setup or action-needed; never silently alter OS protection settings.
4. **DNS setup** — platform-specific encrypted-DNS instructions.
5. **Verify** — system verification can result in `Verified`, `Action needed`, `Status uncertain`, or `Not covered`.
6. **External service** — optional relevant service state may be parent-confirmed or not covered.
7. **Protection Map** — evidence map for Phone / Internet / Service; never a safety score.
8. **Troubleshooting** — source-backed conflict guidance plus deterministic retry after a changed condition.
9. **Removal** — explicit SafeWeb DNS removal path; never represent plaintext fallback as protected.
10. **Recovery** — confirm ordinary connectivity after removal.
11. **Reset/reconfigure** — return to a clean discovery state.

Global Help and Limitations must be reachable without corrupting journey state, and unsupported routes must fail safely to limitations without speculative client instructions.

## 4. Frozen state semantics

Only these protection/evidence states are implementation-authorized:

| State | Meaning |
| --- | --- |
| `Verified` | Current qualifying system evidence exists for that protection step. |
| `You confirmed this is set up` | Parent confirmed the setting; SafeWeb has not independently verified it. |
| `Action needed` | A required step is incomplete or failed; do not rely on that protection layer. |
| `Status uncertain` | Current evidence cannot establish protection state; do not imply success. |
| `Not covered` | SafeWeb does not cover this layer on the current setup. |
| `Removed` | SafeWeb DNS is no longer active on the device. |

Immutable truth rules:

- parent confirmation is never system verification;
- `Verified` requires current qualifying verification evidence;
- removal cannot silently return to verified state;
- uncertainty and not-covered states remain visible and actionable;
- brand color is never the sole carrier of protection state;
- no overall safety score, `100% safe`, `fully protected`, certification, or equivalent complete-safety claim.

## 5. Platform configuration contract

### Android

- Private DNS hostname: `dns.usesafeweb.com`.
- The product may instruct and verify; it must not silently modify Android system DNS.
- After configuration, system verification is required before Internet protection is shown as `Verified`.

### iPhone

- DoH endpoint: `https://dns.usesafeweb.com/dns-query`.
- The product must not fabricate or distribute an unverified `.mobileconfig` profile.
- Native-safeguard status and DNS verification remain separate evidence states.

### Unsupported / other

- Route to explicit limitations.
- Do not invent untested client workarounds.
- Do not offer a removal action when SafeWeb DNS was never configured through the journey.

## 6. Interaction and friction rules

REQ-0028 applies to every interaction. Each retained action exists only to start, route, record a necessary native-safeguard state, configure/verify DNS, record an optional applicable service, explain evidence, troubleshoot, remove/recover, show limitations, or reset.

The baseline contains no form/input/textarea/select data-entry step and requires no personal data for the representative journey. A downstream implementation must not add identity, profile, child, payment, or diagnostic fields unless separately authorized and necessary under current requirements.

Retries are bounded: retry verification only after a changed condition. Invalid state-machine actions must be rejected rather than silently advancing the user.

## 7. Accessibility, responsive, and localization contract

- mobile-first behavior is mandatory;
- critical screens must not horizontally overflow at the representative 320 px mobile viewport;
- wider layouts must remain bounded and readable rather than stretch uncontrolled;
- screen changes move focus to the current `h1` in the accepted reference behavior;
- application busy state is explicit (`aria-busy`) and must settle correctly;
- buttons have explicit button semantics;
- visible brand identity has meaningful `SafeWeb` alternative text where conveyed by an image;
- critical state meaning is textual, not color-only;
- public/product surfaces ultimately target WCAG 2.2 AA and current mainstream browsers under REQ-0033;
- English, Turkish, and Arabic/RTL availability is a first-public-release constraint; `SafeWeb` remains invariant Latin-script/LTR while surrounding Arabic UI may be RTL;
- technical language availability must not be represented as official non-UK market/legal/support readiness without its separate gate.

## 8. Privacy and security behavior

The representative journey is privacy-minimal:

- no login required;
- no localStorage or sessionStorage persistence;
- no cookies;
- no service worker;
- no remote tracker/resource dependency in the accepted internal prototype;
- no raw DNS query data, browsing history, child identity, or persistent parent identity in this experience baseline;
- test serving is localhost-only and temporary;
- no admin credential or AdGuard administration surface is exposed.

Any implementation that adds persistence, telemetry, cookies, remote third parties, identity, or new data collection must follow the owning privacy/security/data-flow authority and cannot inherit acceptance from this baseline.

## 9. Brand/content binding

Implementation consumes the accepted SafeWeb brand/token system rather than inventing independent styling or claims:

- visible brand is `SafeWeb`;
- `UseSafeWeb.com` is used only as domain/project/technical identifier where required;
- approved identity masters remain authoritative;
- shared brand tokens/components remain the styling source for downstream implementation;
- product/setup branding is subordinate to task clarity and evidence truth;
- self-service help/recovery is the ordinary support model;
- content remains plain-language, child-aware, non-alarmist, and bounded by current claims/non-surveillance rules.

## 10. Defect disposition at freeze

No unresolved **critical/high pre-product defect** is established by current accepted evidence.

Current evidence proves the representative journey’s functional, negative, configuration, security/privacy, responsive and rollback/recovery behavior in rendered Chromium. The first rendered test deviation was a test-fixture isolation defect, not a product defect; it was root-caused, corrected, independently health-checked, and the entire suite then passed.

Therefore TSK-0309 freezes the accepted prototype **without product-code changes**. This is intentional YAGNI/least-change behavior: there is no evidence-backed critical/high correction to make before the implementation handoff.

## 11. Accepted source/version set

Core representative prototype Git blobs:

- `prototype/TSK-0310/index.html` — `5d80dfdefb52042bc34468723354fefd325285e4`
- `prototype/TSK-0310/model.mjs` — `01343273fd09c3c12d26f0c0eb1ae9a2fce10c91`
- `prototype/TSK-0310/app.mjs` — `a4a0aff8848f8541e2581e333efbf48767c9f0ff`
- `prototype/TSK-0310/prototype.css` — `439ef05dd04da7fccf01cb4b85e317a828389edf`
- `prototype/TSK-0310/browser-acceptance.mjs` — `f791a797f6a64be8b74eb13cbd2e628d5b083007`
- `prototype/TSK-0310/package.json` — `9cbf9f5102592a0147c531748db49b68e4ee1648`

Current accepted source authorities include:

- `TSK_0310_RENDERED_BROWSER_ACCEPTANCE_EVIDENCE_2026-08-29.md` — blob `02b34756862a62091908e60d32b490059a84a67c`
- `TSK_0320_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-08-28.md` — blob `1146f7622f434590dde1253d11f14fb6a87e19de`
- `TSK_0299_PROVISIONAL_VERBAL_SYSTEM_2026-08-29.md` — blob `a4ff2314ff02c407249e8b5d4d6b9600b89403b3`
- `brand/system/TSK-0300/README.md` — blob `4baa67f565c14c3034fca47bb5fad0b9ff71b091` (content rules remain usable; its older CR-0004 sequencing note is superseded by current DEC-0052/CR-0005)
- current WBS blob `f23b4f017d1baf73258fa30ecd71549bbfe1b815`
- current Layer-5 rules blob `93b143776a2c49000b2d092c5b812a70bc0963ac`.

## 12. Change control

This `1.0.0` baseline is the L4 design-to-build contract. Downstream implementation must trace states/content/errors/recovery/accessibility to this baseline and its listed authorities.

A change requires explicit disposition when it materially alters the critical journey, state truth, platform setup mechanism, removal/recovery behavior, data/persistence model, account scope, claims, accessibility behavior, localization/RTL behavior, or supported platform behavior. Evidence contradicting an assumption reopens the affected task under ordinary current-evidence precedence.

This baseline is not public-release, production-deployment, payment, market-activation, or launch authority.
