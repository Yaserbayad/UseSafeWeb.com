# TSK-0297 — Current Brand Guidelines and Asset-Governance Revalidation — Post-CR-0008

**Task:** TSK-0297 — Publish concise brand guidelines, source/editable asset library, versioning, ownership, and usage rules  
**Acceptance / Verification / Evidence:** ACC-0297 / VER-0297 / EVD-0297  
**Lifecycle / Priority / Authority:** L4 / MEDIUM / A3 / AUTO_ALLOWED  
**Date:** 2026-09-02 UTC  
**Candidate disposition:** CURRENT PASS pending independent verification, durable evidence publication, guarded runtime reconciliation and exact read-back.

## 1. Revalidation trigger

TSK-0297 historically passed on 2026-08-29 because its README and asset manifest made brand output deterministic and all active manifest source paths/blobs were current at that time.

A later dependency-current audit correctly reopened it after direct predecessor TSK-0300 was reaccepted with current protection-state copy. Artifact inspection found the active TSK-0297 package still bound several superseded sources:

- pre-correction TSK-0300 README blob `4baa67f565c14c3034fca47bb5fad0b9ff71b091`;
- historical TSK-0299 verbal artifact `TSK_0299_PROVISIONAL_VERBAL_SYSTEM_2026-08-29.md`, blob `a4ff2314ff02c407249e8b5d4d6b9600b89403b3`;
- historical TSK-0320 artifact `TSK_0320_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-08-28.md`, blob `1146f7622f434590dde1253d11f14fb6a87e19de`;
- pre-dual-mode public/product template blobs `0146960a0f5b2abfe2458f0210ed750f0147d3b9` / `169acf5c8fc2c1f841111b99b8da1cfb6e9c5836`;
- pre-protection-copy-correction status template blob `f4f3b32957c978fe9ea00704bd285a20e3c56aef`;
- historical state labels `Verified`, `You confirmed this is set up`, and `Status uncertain` as if they were current primary copy.

Those conditions violate the same source-currency/no-guessing boundary that originally justified ACC-0297 PASS. The package therefore required current revalidation rather than blind PASS preservation.

## 2. Current package

### Guidelines

`brand/guidelines/TSK-0297/README.md`

- version `2.0.0`;
- blob `e79121fd95932a6f4b2550f5f05b84c6e9c7aeac`;
- update commit `113f9de234f14f85b8d14a29e929e32bc565989d`.

Version 2.0.0 is intentionally MAJOR under the package's own versioning rule because current TSK-0320 primary protection-state copy and CR-0006 dual-mode surface bindings require consumers of v1.0.0 to change active output/source selection.

### Asset manifest

`brand/guidelines/TSK-0297/ASSET_MANIFEST.json`

- schema remains `usesafeweb.brand-assets.v1`;
- guideline version `2.0.0`;
- blob `c31eb9674eee9cf330b1af4764088f51e9c398fe`;
- update commit `280f68a13e3d965887ae59edba66718c3d4c1c7f`.

The manifest records v1 package blobs as superseded provenance and separately records obsolete authority bindings with explicit replacements. Historical source revisions are not misrepresented as deprecated identity assets.

## 3. Current authority bindings

The package now binds:

- compatible strategic brand-role/prohibited-expression scope from `TSK_0298_EVIDENCE_GROUNDED_BRAND_STRATEGY_2026-08-29.md`, blob `73d8587ef9bb37d92b44f102d5a33545b416c44b`, while explicitly refusing its superseded sequencing/account-scope statements where current authority conflicts;
- identity rules `brand/identity/TSK-0301/README.md`, blob `b8ffd2ed234465a238558a7b94e56274de49696a`;
- corrected current shared-system README `a54a2b653720160261b034149cadff62bc399102`;
- current TSK-0300 correction evidence `a3e39896b67098ced321cb9e4b82c65c440806e4`;
- current TSK-0299 dual-mode verbal system `ff30500b933b9ecc92325659d49ea4e671d296d2`;
- current TSK-0320 protection-state/copy system `bdc6bacc424669708f410466f3cfd5527f1c2b3c`.

The current primary state copy is exactly:

1. `Protection verified`;
2. `Setup confirmed`, plus `Protection has not yet been technically verified.`;
3. `Action needed`;
4. `Not covered`;
5. `Protection status could not be verified`;
6. `Removed`.

Account/session/dashboard/device ownership remains continuity state only and cannot be rendered as technical verification.

## 4. Current active asset/source inventory

Identity masters remain unchanged:

- primary `f93958e3e4a16f9056693072c1b9b8b31fcda852`;
- inverse `c38709e4239a2d36b340b4d9d630df85a17bb494`;
- monochrome `ef9b6e0d52926f24c7e81bccb4489569067b852f`;
- `Sw` monogram `49f20bae1d92bb04f125e988cb4cc3ea8a822b9e`.

Shared implementation sources remain unchanged:

- tokens `cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f`;
- components `831e92a74b6dda04252d93242cb33bd491a02381`.

Current six active reference templates are:

- help `3193c0d1e11367204d6c46fd862fec5a91245b64`;
- partner `03bb1fd67b9a9824bc856d1f312977d7767619a8`;
- product `872920b6f7af6561a1015e1d8fea55dcf95f1249`;
- public `309f6a1f38474f78cd8a241aad3028fd495f9b8e`;
- social `cabdd12851fce1dbd5a3c6326ec6dec63f843958`;
- status `8f9971edfc87b2da8174330b9b4be68338a96fb4`.

No approved identity master, token/component source, help/partner/social template, palette, typography stack or logo selection rule was redesigned.

## 5. Current deterministic generation contract

A human or AI must be able to produce a compliant asset without guessing by resolving, in order:

1. requested surface/context/locale/output format;
2. exact current source authority and blob from `ASSET_MANIFEST.json`;
3. exact logo variant by surface/contrast/space rule;
4. current TSK-0300 token/component/template source;
5. current TSK-0320 state/copy when protection truth is present;
6. current TSK-0299 claims/voice/lifecycle language;
7. explicit dual-mode boundary: accountless core first-class, optional account continuity non-coercive, no identity-to-protection inference;
8. required derivative provenance (`guideline_version`, `source_path`, `source_blob`, `output_format`).

Representative decisions are explicit for public light header, small dark status/icon, Arabic RTL, optional account/dashboard and lifecycle surfaces.

## 6. Deprecation and supersession traceability

Actual asset records use `ACTIVE` or `DEPRECATED`. A deprecated asset must be retained with replacement, reason, deprecation date and authorizing commit/evidence; new use and silent deletion are prohibited.

Source-authority revisions are tracked separately. The v2 manifest retains:

- v1 README/manifest blobs;
- old TSK-0300 README binding and replacement;
- old TSK-0299 path/blob and current replacement;
- old TSK-0320 path/blob and current replacement.

This preserves historical reconstruction without making obsolete bindings selectable current assets.

## 7. Font/source library boundary

The approved font stack remains `Avenir Next, Segoe UI, Helvetica Neue, Arial, sans-serif` as a CSS/system-font policy only.

TSK-0297 continues to prohibit embedded, committed, exposed or delivered `.ttf`, `.otf`, `.woff`, `.woff2` and `.eot` files. The editable/source library consists of repository SVG/CSS/HTML/JSON/Markdown sources and does not require raster or font duplication without a consuming need.

## 8. Independent verification contract

Current VER-0297 must independently prove:

1. WBS contract: L4 / MEDIUM / A3 / AUTO_ALLOWED, direct dependency TSK-0300, ACC/VER/EVD IDs current;
2. TSK-0300 corrected current PASS/evidence is durable;
3. README/manifest exact current package blobs and version agree;
4. every active manifest path exists and its blob matches current `main`;
5. current TSK-0299 and TSK-0320 artifacts are selected, and old bindings appear only in supersession provenance;
6. public/product/status active blobs are the current dual-mode/copy-corrected blobs;
7. exact current primary state copy plus S2 limitation is represented in README/manifest;
8. accountless core/optional-account/no-ownership-as-verification/no-auto-linkage rules are explicit;
9. identity masters and shared tokens/components remain unchanged;
10. deterministic representative asset decisions resolve without ambiguous alternatives;
11. deprecation policy is structurally complete and any `DEPRECATED` entry has all required provenance;
12. no forbidden font binary is tracked or exposed by the package;
13. no remote asset/tracker/script/font artifact is introduced by TSK-0297;
14. source files remain unchanged during verification;
15. no build/legal/privacy/user-validation/publication/payment/market/production/launch/gate/successor PASS is inferred.

## 9. Candidate disposition

The historical TSK-0297 design intent remains useful, but its active source/copy bindings were stale. Version 2.0.0 repairs those bindings, preserves approved identity/source assets, and makes supersession explicit.

**ACC-0297 current candidate: PASS pending independent VER-0297, durable EVD-0297, guarded runtime reconciliation and exact read-back.**
