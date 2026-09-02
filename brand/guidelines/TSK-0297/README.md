# TSK-0297 — Brand Guidelines and Asset Governance

**Version:** 2.0.0  
**Status:** `provisional_internal_l4`  
**Owner:** Brand  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Action authority:** A3 / AUTO_ALLOWED  
**Acceptance:** ACC-0297  
**Date:** 2026-09-02  
**Supersedes:** TSK-0297 guideline version 1.0.0 for current source/copy selection; historical v1 remains durable provenance.

## Authority boundary

This package makes approved brand assets and rules deterministic to select, generate, version and deprecate. It does **not** create new identity, token, protection-state, claims, research, legal, build, publication, payment, market or launch authority.

Source precedence is mandatory:

1. `brand/identity/TSK-0301/README.md` and its SVG masters own visual identity and logo rules.
2. Current `brand/system/TSK-0300/README.md`, `tokens.css`, `components.css` and its six active reference templates own reusable system/surface patterns. TSK-0297 may select them but may not fork them.
3. `TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md` owns protection-state semantics/copy; `TSK_0299_POST_CR0008_DUAL_MODE_VERBAL_SYSTEM_2026-09-01.md` owns voice, terminology, trust language and claims boundaries.
4. `TSK_0298_EVIDENCE_GROUNDED_BRAND_STRATEGY_2026-08-29.md` remains usable only for its still-compatible brand role, promise, non-surveillance positioning and prohibited-expression principles. Historical sequencing/account-scope text in that file is superseded where it conflicts with current CR-0005/CR-0006/CR-0007/CR-0008 authority and must not be used to override sources 1–3 or current runtime.
5. This TSK-0297 package owns only asset selection, export provenance, package versioning, ownership routing and deprecation traceability. It may not fork or override sources 1–4.

`RSK-0002` remains OPEN. No representative-parent evidence proves preference, comprehension, trust, completion or support burden. These guidelines are internal/provisional and do not authorize public release.

## Current product/surface boundary

Current Version-1 scope is dual-mode:

- the complete core setup, verification, Protection Map, troubleshooting, recovery and removal journey remains usable without login;
- optional parent sign-in/session continuity and lightweight dashboard/device management may be represented where the current owning source permits it;
- account/session/dashboard/device ownership is never technical protection evidence;
- anonymous J0/J1 state is not automatically imported, promoted, linked or extended by sign-in;
- no browsing/query/activity history, child account/profile or unrestricted customer DNS administration is implied by a brand asset or reference surface.

Brand guidance must not silently revert current surfaces to the old accountless-only product scope, and optional-account continuity must not become a mandatory gate for core value.

## Deterministic asset-generation procedure

For every asset or surface, record **surface, context, locale, output format, source master path/blob, guideline version and derivative status**, then apply these rules in order:

1. **Name:** visible brand is exactly `SafeWeb`. `UseSafeWeb.com` is the project/domain, not the wordmark. Never translate or alter `SafeWeb`.
2. **Logo selection:**
   - light/default surface → `safeweb-wordmark-primary.svg`;
   - single-color, small, accessibility-critical, or dark context where split colors are unsafe → `safeweb-wordmark-monochrome.svg`;
   - large confirmed dark surface only → `safeweb-wordmark-inverse.svg`;
   - compact/icon-only context → `safeweb-monogram.svg` (`Sw`) only.
3. **Logo integrity:** no distortion, redraw, alternate casing, unapproved recolor, tagline lockup, shield, lock or certification device. Do not duplicate SVG geometry into a new source master.
4. **Tokens/components:** consume current `brand/system/TSK-0300/tokens.css` and `components.css`; do not create a parallel token set or local brand-color fork.
5. **Typography:** use the approved stack `Avenir Next, Segoe UI, Helvetica Neue, Arial, sans-serif`. Never embed, commit, expose or deliver font binaries as part of this package.
6. **Locale/direction:** `SafeWeb` remains Latin, LTR and untranslated in EN/TR/AR. Surrounding Arabic may be RTL. Never mirror or reverse the mark for RTL.
7. **Protection truth:** use only the current canonical state semantics/copy owned by TSK-0320:
   - `Protection verified`;
   - `Setup confirmed`, with supporting copy `Protection has not yet been technically verified.`;
   - `Action needed`;
   - `Not covered`;
   - `Protection status could not be verified`;
   - `Removed`.
   Never collapse setup/parent confirmation, account ownership, session state or device registration into technical verification, and never use `Safe`, `100% protected`, `Fully protected` or equivalent guarantees.
8. **Claims/voice:** apply the current TSK-0299 calm, clear, respectful, protective-not-controlling, truthful and practical language. Accountless core remains first-class; optional account continuity is not stronger protection; lifecycle operations must name exactly what they change. Do not imply parent validation, market superiority, surveillance, certification, routine staffed support or capabilities not proven by current authority.
9. **Accessibility:** never rely on color alone for critical state. Use text/semantics plus approved contrast-safe combinations.
10. **Imagery/icons:** avoid shield, padlock, eyes, cameras, tracking/radar, child-surveillance silhouettes, certification badges, fear imagery and cyber-neon security theatre. Prefer restrained, practical, non-surveillance visual language.
11. **Derivatives:** raster or alternate-format exports may be created only for a consuming implementation need. They are never source authority. Record source master path/blob and this guideline version; never silently overwrite a prior derivative.

## Core visual rules

| Element | Approved rule |
| --- | --- |
| Primary green | `#173F35` |
| Deep green | `#0F2D23` |
| Maroon | `#7A2E36` |
| Off-white | `#F6F4EF` |
| Muted sage | `#A7BEAD` |
| Layout character | whitespace-led, mobile-first, dark-green dominant, restrained |
| Prohibited default aesthetic | dense/raw admin dashboard, cyber-security neon, surveillance/control theatre |

### Contrast constraints

Current accepted identity checks:

- `#173F35` / `#F6F4EF` ≈ **10.6:1**;
- `#7A2E36` / `#F6F4EF` ≈ **8.4:1**;
- `#F6F4EF` / `#0F2D23` ≈ **10.6:1**;
- `#7A2E36` / `#0F2D23` ≈ **1.3:1** — unsuitable for small/normal/critical content.

On dark surfaces, use one-color off-white for small or critical identity/state content unless a later authoritative accessibility check approves a different combination.

## Surface selection matrix

| Surface/context | Identity | Current system source | Mandatory boundary |
| --- | --- | --- | --- |
| Public/landing | primary on light; inverse only on large confirmed dark | `public.html` | `Start setup` remains primary; optional sign-in/manage entry may be secondary; no validation/safety guarantee |
| Product/setup | primary or monochrome by contrast/context | `product.html` + components | accountless completion remains available; optional continuity is explicit/non-coercive; truthful state distinctions |
| Help | primary/monochrome | `help.html` | self-service; no fabricated staffed-support promise |
| Status/protection map | monochrome where compact/critical; primary where spacious/light | `status.html` | current TSK-0320 state text/evidence required; never color-only; no safety score |
| Partner | primary/monochrome | `partner.html` | no approval, endorsement or certification implication |
| Social | primary/monochrome by surface | `social.html` | no fear, superiority, fully-protected or certification claims |
| Compact/icon | `Sw` monogram only | identity master | not a replacement for full wordmark where space permits |
| Arabic RTL | same unmirrored Latin LTR mark | matching surface template | surrounding Arabic may RTL; `SafeWeb` remains LTR/untranslated |

## Ownership and change routing

| Change | Authoritative owner/path | TSK-0297 authority |
| --- | --- | --- |
| wordmark geometry, mark, identity colors/rules | TSK-0301 identity package | reference only |
| tokens, components, shared surface templates | current TSK-0300 system package | reference only |
| protection-state semantics/copy | current TSK-0320 | reference only |
| voice, terminology, trust/claims language | current TSK-0299 | reference only |
| still-compatible strategic brand role/prohibited-expression principles | TSK-0298 | reference only; current governance/scope wins on conflict |
| asset inventory, provenance, derivative/export record, deprecation | TSK-0297 | owns |

If a requested asset requires changing an upstream authority, stop and route the change to that owner; do not modify it locally in this package.

## Versioning

- **MAJOR** — breaking owner-approved change to this package contract or an upstream identity/brand/copy contract requiring consumers to change.
- **MINOR** — additive approved asset class, export rule, surface mapping or non-breaking governance capability.
- **PATCH** — non-semantic clarification, metadata/provenance correction or editorial fix.

Version `2.0.0` is MAJOR because current TSK-0320 primary protection-state copy and CR-0006 dual-mode surface bindings require consumers of v1.0.0 to change active output/source selection.

Every derivative/export must record the guideline version and exact source blob(s). Existing derivative identifiers must not be silently repointed to materially different content.

## Deprecation and supersession

Manifest asset records use `ACTIVE` or `DEPRECATED`.

A deprecated asset entry is retained and must record: replacement (or `null`), reason, deprecation date and the commit/evidence that authorized the change. Deprecated assets must not be selected for new work. Never delete or overwrite a deprecated record merely to make the inventory look current.

Authority/source **revisions** are tracked separately from asset deprecation. `ASSET_MANIFEST.json` records the superseded v1 package blobs and obsolete authority/template bindings so historical provenance stays reconstructable without presenting those old bindings as selectable current assets.

## Source/editable library policy

The canonical editable/source library is intentionally lightweight:

- identity masters are the accepted source-controlled SVG files under `brand/identity/TSK-0301/`;
- implementation source is current TSK-0300 CSS/templates;
- `ASSET_MANIFEST.json` supplies stable inventory/provenance and deprecation/supersession metadata;
- no raster duplicate is required without a consuming need;
- no remote asset, tracker, script, embedded font, `.ttf`, `.otf`, `.woff`, `.woff2` or `.eot` belongs in this package.

## Representative deterministic checks

A compliant producer should reach these results without guessing:

1. **Public header, light background:** use `safeweb-wordmark-primary.svg`, current TSK-0300 tokens, visible name `SafeWeb`; keep accountless `Start setup` primary and any optional sign-in/manage entry secondary; do not add shield/tagline/certification/safety claims.
2. **Small dark status/icon context:** use monochrome off-white or the `Sw` monogram when genuinely icon-only; never maroon-on-deep-green for critical/small content; use current TSK-0320 textual state/evidence.
3. **Arabic RTL setup/status:** surrounding Arabic may be RTL; the `SafeWeb` mark remains Latin LTR/untranslated; current protection-state meaning/evidence must remain explicit and cannot rely on color alone.
4. **Optional account/dashboard surface:** use the same SafeWeb identity and TSK-0300 primitives; account/session/device ownership is continuity metadata only and cannot be rendered as `Protection verified` without qualifying technical evidence.
5. **Lifecycle asset/copy:** distinguish sign out, device unlink/revoke, device-record deletion, account deletion, anonymous-state reset/deletion and physical DNS removal; never imply one completed another.

## Non-inference fence

This package is **provisional internal L4**. It proves deterministic brand-asset governance only. It does not prove real-parent or native-speaker validation, legal/privacy completion, integrated build readiness, public-release readiness, payment/market activation, production behavior or launch readiness, and it does not close `RSK-0002`.