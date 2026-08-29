# TSK-0297 — Brand Guidelines Acceptance Evidence

**Task:** TSK-0297 — Publish concise brand guidelines, source/editable asset library, versioning, ownership, and usage rules  
**Acceptance:** ACC-0297  
**Verification:** VER-0297  
**Evidence:** EVD-0297  
**Date:** 2026-08-29  
**Verifier:** ChatGPT / SERIAL LIGHT governed repository review  
**Repository/environment:** `Yaserbayad/UseSafeWeb.com` / `main`  
**Disposition:** **PASS**

## Artifact/version evidence

- Guideline version: `1.0.0`
- Status: `provisional_internal_l4`
- Owner: Brand
- `brand/guidelines/TSK-0297/README.md` — blob `89e915678e85f7f301e8fa4b05c335cd803dd9d4`
- `brand/guidelines/TSK-0297/ASSET_MANIFEST.json` — blob `11e26ee46ebb60762c085513e50f8e40ec1f4854`
- Artifact commits: README `3bf21934b8a394375d885fb1c159198ca6b359f7`; manifest `4bff6545bc400df267ac82915602bb73a94bd0f8`.
- Compare from pre-task head `769da15d19e51da2be7839faf9e6f82eb662d28c` to artifact head `4bff6545bc400df267ac82915602bb73a94bd0f8`: exactly the two TSK-0297 package files were added.

## Current source/exact authority evidence

The manifest was checked against current `main` immediately before/after publication; referenced blobs match the accepted source authorities:

- Brand strategy: `TSK_0298_EVIDENCE_GROUNDED_BRAND_STRATEGY_2026-08-29.md` — `73d8587ef9bb37d92b44f102d5a33545b416c44b`
- Identity rules: `brand/identity/TSK-0301/README.md` — `b8ffd2ed234465a238558a7b94e56274de49696a`
- Primary wordmark — `f93958e3e4a16f9056693072c1b9b8b31fcda852`
- Inverse wordmark — `c38709e4239a2d36b340b4d9d630df85a17bb494`
- Monochrome wordmark — `ef9b6e0d52926f24c7e81bccb4489569067b852f`
- `Sw` monogram — `49f20bae1d92bb04f125e988cb4cc3ea8a822b9e`
- Shared system: `brand/system/TSK-0300/README.md` — `4baa67f565c14c3034fca47bb5fad0b9ff71b091`
- Tokens — `cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f`
- Components — `831e92a74b6dda04252d93242cb33bd491a02381`
- Help template — `3193c0d1e11367204d6c46fd862fec5a91245b64`
- Partner template — `03bb1fd67b9a9824bc856d1f312977d7767619a8`
- Product template — `169acf5c8fc2c1f841111b99b8da1cfb6e9c5836`
- Public template — `0146960a0f5b2abfe2458f0210ed750f0147d3b9`
- Social template — `cabdd12851fce1dbd5a3c6326ec6dec63f843958`
- Status template — `f4f3b32957c978fe9ea00704bd285a20e3c56aef`
- Verbal/claims system: `TSK_0299_PROVISIONAL_VERBAL_SYSTEM_2026-08-29.md` — `a4ff2314ff02c407249e8b5d4d6b9600b89403b3`
- Protection-state/copy model: `TSK_0320_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-08-28.md` — `1146f7622f434590dde1253d11f14fb6a87e19de`

## ACC-0297 verification

### 1. Compliant asset generation without guessing — PASS

The README fixes source precedence, exact name, deterministic logo selection by surface/context, token/component ownership, typography policy, EN/TR/AR direction rules, exact protection-state labels, claims boundaries, accessibility rules, derivative provenance and surface mappings.

Representative task checks:

1. **Public header / light background:** resolves to `safeweb-wordmark-primary.svg` + TSK-0300 tokens + visible name `SafeWeb`; shield/tagline/certification additions are prohibited. **PASS**.
2. **Small dark status/icon:** resolves to monochrome off-white or `Sw` only when genuinely icon-only; maroon-on-deep-green is explicitly rejected for small/critical use. **PASS**.
3. **Arabic RTL setup/status:** surrounding Arabic may be RTL; `SafeWeb` remains Latin LTR and untranslated; critical state is expressed in text and cannot rely on color alone. **PASS**.

### 2. Deprecated assets traceable — PASS

`ASSET_MANIFEST.json` defines `ACTIVE` / `DEPRECATED`, retains deprecated records, prohibits new use, and requires replacement, reason, date and authorizing commit/evidence for deprecation. Silent deletion/overwrite is prohibited.

### 3. No font files exposed as user deliverables — PASS

Current `brand/guidelines/TSK-0297/` directory contains exactly `README.md` and `ASSET_MANIFEST.json`; there is no `.ttf`, `.otf`, `.woff`, `.woff2` or `.eot`. The manifest additionally fixes `deliver_font_binaries=false` and lists those extensions as forbidden. The source library references existing SVG/CSS/HTML masters rather than packaging font binaries.

## VER-0297 verification

- **Approved brief:** package preserves the TSK-0298 brand role, non-surveillance positioning, evidence limits and prohibited-expression boundary. **PASS**.
- **User/evidence boundary:** `RSK-0002` remains explicitly OPEN; no parent preference/comprehension/trust finding is invented. **PASS**.
- **Claims/state:** TSK-0299 and TSK-0320 remain authoritative; verified vs parent-confirmed vs action-needed/not-covered/uncertain/removed semantics are not collapsed. **PASS**.
- **Accessibility:** accepted contrast values are preserved; maroon/deep-green ≈1.3:1 is explicitly unsuitable for small/normal/critical content; critical state cannot rely on color alone. **PASS**.
- **Source currency:** all manifest source paths/blobs match current canonical sources checked on `main`. **PASS**.
- **Surface acceptance:** public/product/setup/help/status/partner/social and compact/RTL contexts have deterministic source/identity/boundary rules. **PASS**.
- **Manifest structure:** JSON structure and required schema/version, 4 identity assets, 6 surface templates, font prohibition, derivative provenance and retained-deprecation assertions were independently parsed/asserted; result `MANIFEST_STRUCTURE=PASS`, `MANIFEST_REFERENCE_COUNT=PASS`. **PASS**.

## Deviations / retained limits

- `RSK-0002` remains OPEN.
- Real-parent and native-speaker behavioral validation remain outside this task and are not inferred.
- This PASS is only the current L4 brand-guideline/source-asset-governance contract. It does not authorize or imply legal/privacy completion, L5/L6 build, participant processing, public release, payment, market activation or launch readiness.

## Final acceptance decision

All applicable ACC-0297 requirements and VER-0297 checks have direct, current, reconstructable evidence. **TSK-0297 = PASS**.