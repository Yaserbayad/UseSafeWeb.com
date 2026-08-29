# TSK-0324 — UI Component Rules Acceptance Evidence

**Evidence ID:** EVD-0324  
**Task:** TSK-0324 — Define lightweight visual identity and reusable UI component rules  
**Date:** 2026-08-29  
**Verifier:** ChatGPT Web / SERIAL LIGHT Governor with independent GitHub Actions execution on `adguardvm`  
**Disposition:** PASS  
**Sequencing:** DEC-0052 / CR-0005

## Artifact/version

- Normative UX/UI consumer contract: `prototype/TSK-0324/UI_COMPONENT_RULES.md` v1.0.0, blob `0b7012a12070f7eccf45a1bbb2f453fde8507ff6`, publication commit `cdd9e2987be1c7050682184220b81c75de7e4283`.
- Non-authoritative machine acceptance projection: `prototype/TSK-0324/COMPONENT_CONTRACT.json` v1.0.0, blob `dc1f767025c2b016274d247d997411128105c5e4`, publication commit `96ce10c87483cc8a13e7e88b231d923f7feafcaf`.
- Verification workflow: `.github/workflows/verify-tsk0324.yml`, blob `6d5d4863b49f45f552382583777ebae9ba5b616a`, commit `da117b2d9ceab5a4610ecc238d8804c1709b0453`.

## Exact source/environment

Verification ran on self-hosted `adguardvm` from exact GitHub `main` verification head `da117b2d9ceab5a4610ecc238d8804c1709b0453` and pinned these accepted sources:

- `brand/system/TSK-0300/tokens.css` — `cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f`.
- `brand/system/TSK-0300/components.css` — `831e92a74b6dda04252d93242cb33bd491a02381`.
- `brand/guidelines/TSK-0297/README.md` — `89e915678e85f7f301e8fa4b05c335cd803dd9d4`.
- `TSK_0320_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-08-28.md` — `1146f7622f434590dde1253d11f14fb6a87e19de`.
- `content/TSK-0322/PRODUCT_VOICE_CLAIMS_TERMINOLOGY.md` — `d12c1e707f0390915002b27bf3a5073d0135d466`.
- `prototype/TSK-0309/BASELINE.md` — `76bb848ebdf6a2aee4dd84bc18e8af5ba8a99dbc`.
- `Plans/Master/WBS/master-wbs.csv` — `f23b4f017d1baf73258fa30ecd71549bbfe1b815`.

WBS authority was rechecked as L4 / PLANNED / MEDIUM / A3 / AUTO_ALLOWED with sole dependency `TSK-0322`; canonical runtime independently proves `TSK-0322` PASS.

## Current external source review

Reviewed 2026-08-29 against first-party W3C sources:

- WCAG 2.2 Recommendation: `https://www.w3.org/TR/WCAG22/` — Level AA text contrast baseline (4.5:1 normal text, 3:1 large text) and current WCAG 2.2 success-criterion set.
- W3C Understanding SC 2.5.8 Target Size (Minimum): `https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum` — Level AA 24×24 CSS-pixel target minimum with documented exceptions/spacing alternatives.
- W3C Understanding SC 2.4.13 Focus Appearance: `https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html` — correctly treated as AAA/non-binding stronger focus reference, not mislabeled as AA.

## Verification output

GitHub Actions run `33270916940`, job `99149118903`: **success**.

Computed contrast evidence:

- `#173F35 / #F6F4EF` = **10.62:1** — PASS.
- `#7A2E36 / #F6F4EF` = **8.41:1** — PASS.
- `#F6F4EF / #0F2D23` = **13.46:1** — PASS.
- prohibited critical pair `#7A2E36 / #0F2D23` = **1.60:1** — correctly fenced from small/normal/critical content and authored focus/state meaning.

Terminal acceptance markers:

- `TSK0324_WBS_AUTHORITY=PASS`
- `TSK0324_DEPENDENCY_TSK0322=PASS`
- `TSK0324_SOURCE_BLOBS=PASS`
- `TSK0324_TYPOGRAPHY_SPACING=PASS`
- `TSK0324_CONTRAST_FOCUS=PASS`
- `TSK0324_CONTROLS_FEEDBACK=PASS`
- `TSK0324_PROTECTION_STATES=6/6_PASS`
- `TSK0324_RESPONSIVE_RTL_IDENTITY=PASS`
- `TSK0324_ACCESSIBLE_COMPONENT_SPECS=13/13_PASS`
- `TSK0324_NO_DESIGN_SYSTEM_FORK=PASS`
- `TSK0324_ACC_VER_EVD=PASS`
- `REPOSITORY_CLEAN=PASS`

## ACC-0324 evaluation

ACC-0324 requires typography, spacing, contrast, focus, controls, feedback, four Protection Map states, mobile/desktop behavior, logo/domain use, and accessible component specifications.

Result: **PASS**.

The accepted contract covers every required area. The historical four-state Protection Map minimum is safely subsumed by the current authoritative six-state S1–S6 model rather than dropping current `Status uncertain` or `Removed` semantics. Thirteen reusable component specifications and representative 320/768/1024/1440 responsive behaviors are defined. `SafeWeb`/`UseSafeWeb.com` identity/domain rules are deterministic. Focus, target-size, text-resize, state-semantic, RTL and feedback behavior are implementation/QA-testable.

## VER-0324 evaluation

Applicable internal/source/automated review passed against current brand, claims, protection-state, experience and accessibility sources. No pre-product user/parent/native-speaker evidence is applicable or claimed under DEC-0052 / CR-0005. Existing TSK-0300 token/component sources remain byte-identical; TSK-0324 contains only its Markdown consumer contract and JSON test projection, proving no local CSS/SVG/font/token fork was introduced.

## Deviations and disposition

- One source-era wording mismatch was resolved conservatively: ACC-0324 references four Protection Map states, while current TSK-0320/0322 authority defines six. The artifact supports all six and explicitly records that the historical four-state minimum is satisfied without weakening current semantics.
- Current TSK-0300 maroon/deep-green focus/content pairing is not suitable for critical use. Rather than alter the HUMAN_ONLY/shared-system implementation boundary, TSK-0324 fences dark-brand fields from default interactive-control use and requires a contrast-safe surface, visible UA focus, or an upstream shared-token change before implementation.
- TSK-0300 source files were not modified. This PASS therefore does **not** self-certify `TSK-0308 — Create the shared responsive design system for public and product surfaces`, which remains HUMAN_ONLY.
- `RSK-0002` remains OPEN. No behavioral/comprehension, production implementation, public publication, participant processing, payment, market activation or launch authority is inferred.
