# TSK-0311 — Localization Architecture Acceptance Evidence

**Task:** `TSK-0311 — Define translation keys/files, locale metadata, plural/date rules, content ownership, localized instruction variants, and fallback behavior`  
**Acceptance:** `ACC-0311`  
**Date:** 2026-08-29  
**Disposition:** **PASS candidate for runtime reconciliation**

## Exact evidence set

- Artifact: `TSK_0311_LOCALIZATION_CONTENT_ARCHITECTURE_2026-08-29.md`, exact Git blob `ef746d64c7878eb7d0f1b8fdf2356721728041c4`, publication commit `7eb43368af724887405cf3be9cf9363465834b02`.
- Queue derivation: read-only workflow run `33241609024`, job `99071804111`, printed current WBS row for TSK-0311 as L4 / HIGH / A3 / `AUTO_ALLOWED`, dependency only `TSK-0318`, acceptance `ACC-0311`.
- Dependency: current runtime TSK-0318 PASS.
- Inputs: approved TSK-0318 IA, TSK-0307 source-backed instruction catalogue, TSK-0320 state/copy contract, TSK-0559 content/localization standard, TSK-0314 accessibility NFR, TSK-0229 accountless data contract.

## ACC-0311 checks

ACC-0311 requires: **English baseline uses externalized content; no hard-coded UI copy blocks Turkish/Arabic; locale fallback and content versioning are testable.**

| Check | Result | Evidence |
| --- | --- | --- |
| English baseline externalized | **PASS** | Contract prohibits user-facing production UI copy in component/source code and defines external locale namespaces/files with `en-GB` as canonical authored baseline. |
| Turkish/Arabic not blocked by hard-coded UI | **PASS** | Stable semantic keys are shared across locales; `tr-TR` and `ar` use the same namespaces; Arabic RTL rules and technical-literal isolation are explicit. |
| Locale metadata explicit | **PASS** | Manifest fields include locale/language/region/direction/fallback/status/marketActivation/contentVersion/lastVerified/owner. |
| Fallback deterministic and testable | **PASS** | Exact locale → `en-GB` → visible internal missing-key failure; critical copy cannot silently disappear or be runtime-machine-translated. |
| Content versioning testable | **PASS** | Separate schema/content versions, semantic version rules, release records and changed-key metadata are defined. |
| Plural/date/number rules defined | **PASS** | Locale-aware CLDR/Unicode-equivalent runtime behavior is required; English branching and preformatted English date strings are prohibited. |
| Current instruction variants bound to source authority | **PASS** | Nine TSK-0307 catalogue IDs are mapped conceptually to stable UI keys; locale layer cannot independently rewrite support/truth semantics. |
| Content ownership explicit | **PASS** | General UI, technical instructions, state copy, troubleshooting, privacy, accessibility and localized variants have accountable/review owners. |
| Accessibility/localization interaction explicit | **PASS** | Accessible names, non-color state, reflow/text expansion, RTL focus order and screen-reader copy are governed. |
| Market/support scope cannot expand via localization | **PASS** | `marketActivation=false`; localized variants cannot broaden platform support or evidence state. |
| Implementation verification is defined | **PASS** | Twelve concrete assertions cover bundle parsing, key completeness, hard-coded-copy scan, fallback, instruction binding, RTL, locale formatting, versioning, accessibility and privacy. |
| Privacy boundary preserved | **PASS** | Locale/version records contain no user/device identity, browsing/query history, credentials or raw diagnostics. |

## Adversarial check

- The artifact does not claim locale files are implemented in a production app.
- It does not claim Turkish/Arabic linguistic, native-speaker or representative-parent validation.
- It does not activate a Turkish/Arabic market or widen supported devices/services.
- It does not duplicate TSK-0307 instruction semantics or TSK-0320 protection-state authority.
- It does not use machine translation as a safety/privacy/legal/setup fallback.
- `RSK-0002` remains OPEN and `REQ-0022` remains unresolved.

## Conclusion

Every current ACC-0311 condition is supported by durable, testable design evidence. **TSK-0311 qualifies for runtime PASS** for provisional internal L4 localization architecture only.

This PASS does not authorize product implementation/build, public publication, market activation, participant processing, payment, legal completion or launch.