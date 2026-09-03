# TSK-0395 — Landing implementation acceptance evidence

**Date:** 2026-09-03  
**Task:** `TSK-0395 — Build landing page`  
**Acceptance / verification / evidence:** `ACC-0395 / VER-0395 / EVD-0395`  
**Lifecycle / authority:** L6 / BUILD / A4 / `AUTO_ALLOWED`  
**Hard predecessors:** `TSK-0322` PASS; `TSK-0324` PASS; `LG-07` PASS  
**Verifier:** GitHub Actions clean runner plus independent canonical GitHub read-back/review  
**Result:** PASS evidence complete for every applicable current TSK-0395 acceptance and verification requirement.

## Current authoritative contract

Current synchronized WBS/evidence authority requires:

- **ACC-0395:** copy matches approved claims; the primary CTA is clear; positioning is not DNS-led; privacy, limits, and support paths are present; responsive, accessibility, and performance checks pass.
- **VER-0395:** execute in the applicable target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare the results to ACC-0395.
- **EVD-0395:** identify the artifact/version, exact environment/source, test/review output, date, responsible verifier, deviations, and disposition.

Layer-5 permits L4-L7 acceptance from deterministic internal/CI/browser evidence where it proves the contract; real-participant evidence is not required before L8. Rollback/recovery controls apply where applicable and may not be fabricated.

## Canonical implementation and provenance

- Initial landing source merge: PR `#93`, canonical merge `cdaaf73dd33f423d5f2a77a878f9b37e3808090e`.
- Target acceptance/focused reflow correction: PR `#96`.
- Canonical accepted source commit: `ccbed0d70ab0e7f17bdd3809183fef58d73f0d1e`.
- Canonical accepted tree: `eb32301af511cc937970be395a0a3c42b1655877`.
- PR #96 changed only:
  - `.github/workflows/accept-tsk0395-landing-20260903.yml`
  - `brand/system/TSK-0300/components.css`
  - `website/src/app/globals.css`
  - `website/tests/browser/tsk0395-browser.mjs`
- No deployment, public activation, DNS/AdGuard mutation, participant processing, telemetry activation, account mutation, or launch action occurred.

## Canonical-main target acceptance

Dedicated canonical-main workflow:

- workflow: `TSK-0395 landing acceptance`
- run: `33801214869`
- job: `100800898380`
- event/ref: push / `main`
- exact head: `ccbed0d70ab0e7f17bdd3809183fef58d73f0d1e`
- result: **SUCCESS**
- final browser marker: `TSK0395_BROWSER_ACCEPTANCE=PASS`

Exact target environment observed in the canonical run:

- GitHub-hosted Ubuntu `24.04.4 LTS`
- Node `22.23.2`
- npm `10.9.8`
- Next.js `16.3.3`
- React / React DOM `19.2.8`
- Playwright `1.62.1`
- axe-core `4.13.0`
- Chrome for Testing / Chromium `151.0.7922.34` (Playwright Chromium v1234)
- production Next.js build/runtime exercised by real Chromium

The same run also proved repository/master-plan validation, clean formatting, lint with zero errors, typecheck, production build, dependency audits with zero vulnerabilities, and `111/111` contract tests passing.

## ACC-0395 / VER-0395 mapping

| Requirement | Exact accepted evidence | Disposition |
| --- | --- | --- |
| Copy matches approved claims | Contract and real-browser assertions bind the approved first-phone proposition and reject prohibited overclaims such as universal protection, guaranteed blocking, or replacement of parental controls. | PASS |
| Primary CTA is clear | Browser acceptance verifies `Protect this phone` → `/start`, the secondary `See how it works` → `/how-it-works`, usable link semantics, keyboard focusability, and minimum target sizing for the primary CTA. | PASS |
| No DNS-led positioning | English, Turkish, and Arabic contract checks verify first-phone protection positioning rather than DNS-led headline/copy. | PASS |
| Privacy / limits / support paths | Browser acceptance verifies `/privacy`, `/limits`, and `/help` navigation paths. | PASS |
| Responsive checks | Real Chromium verifies `320`, `768`, `1024`, and `1440` px widths in all three locales, no horizontal overflow, and 200% text reflow at 320 px. | PASS |
| Accessibility checks | WCAG 2 A/AA and WCAG 2.2 AA axe checks report zero violations on the tested landing surfaces; non-empty links are keyboard focusable and viewport-visible. | PASS |
| Performance checks | Navigation timing, DOMContentLoaded timing, and transfer size were measured for every locale/viewport combination and were finite/non-negative. ACC-0395/VER-0395 defines no numeric performance budget, and none is invented. | PASS |
| Functional verification | Locale routes render, HTML language/direction, semantic H1/lede, CTA labels/routes, navigation links, and production build behavior are checked in real Chromium. | PASS |
| Negative verification | Unsupported locale `/zz` returns HTTP 404 with `Not Found`; prohibited claims are rejected by contracts. | PASS |
| Configuration verification | `en-GB`, `tr-TR`, and `ar` are exercised in the production runtime, including locale directionality and responsive behavior. | PASS |
| Security/privacy verification | Landing page has no form before setup; cookies remain unchanged; local/session storage remain empty; no off-origin request is emitted; full and production-only npm audits report zero vulnerabilities. | PASS |
| Rollback/recovery verification | This acceptance changed repository source/tests only and never mutated production/public state. Exact Git ancestry and PR provenance make the source change reversibly backout-able through ordinary Git revert. A production rollback drill is not applicable because no production deployment or external material effect occurred. | PASS — applicable source rollback proven; external rollback N/A |

## Performance observations

Canonical real-browser observations (`duration ms / DCL ms / transfer bytes`):

| Locale | 320 | 768 | 1024 | 1440 |
| --- | --- | --- | --- | --- |
| `en-GB` | `111.5 / 73.3 / 3813` | `82.3 / 49.5 / 3813` | `83.6 / 38.2 / 3813` | `84.4 / 34.7 / 3813` |
| `tr-TR` | `94.9 / 59.2 / 3923` | `79.4 / 47.0 / 3923` | `81.7 / 35.7 / 3923` | `78.0 / 78.0 / 3923` |
| `ar` | `86.3 / 86.3 / 4114` | `87.5 / 87.4 / 4114` | `82.0 / 82.0 / 4114` | `75.9 / 75.1 / 4114` |

These measurements satisfy the defined performance check. No canonical ACC-0395/VER-0395 numeric threshold was found, so this evidence does not invent a Core Web Vitals or other unstated budget.

## Deviations and warnings

- One inherited non-error lint warning for `_accountState` remains outside TSK-0395 scope; lint had zero errors.
- One initial server readiness request raced startup; the bounded retry succeeded and the target acceptance continued normally.
- After the intentional unsupported-locale negative path / teardown, the runtime emitted a non-blocking `NoFallbackError` stderr line. The asserted 404 behavior passed and the canonical job remained terminal SUCCESS. This observation is retained rather than concealed.

No deviation invalidates an applicable ACC-0395/VER-0395 requirement.

## Rollback and material-effect boundary

TSK-0395 is a reversible source/build task. Its durable source lineage is PR #93 → `cdaaf73dd33f423d5f2a77a878f9b37e3808090e`, followed by PR #96 → `ccbed0d70ab0e7f17bdd3809183fef58d73f0d1e`. Ordinary Git revert provides the applicable source rollback mechanism. No public runtime was changed, so no external restoration action is required or claimed.

This PASS does **not** authorize or imply deployment, public activation, live DNS/AdGuard changes, real-participant processing, telemetry activation, service removal/revocation, launch, or PASS for any other task. Existing material-action fences remain intact, including the unresolved boundaries around TSK-0374, TSK-0417, TSK-0453, and TSK-0499.

## Final verdict

**PASS.** Every applicable current `ACC-0395 / VER-0395` requirement is backed by exact current canonical source and canonical-main CI/real-browser evidence. Rollback is proven at the applicable source boundary; production rollback is correctly classified not applicable because no production/public mutation occurred.

This file is the durable acceptance artifact for **EVD-0395**. No other task or gate PASS is created or inferred.