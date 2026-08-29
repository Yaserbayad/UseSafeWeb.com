# TSK-0300 — SafeWeb Shared Brand System

**Task:** TSK-0300 — Translate the approved identity into shared tokens, components, templates, and asset conventions  
**Authority:** owner-approved TSK-0301 identity + accepted TSK-0299 verbal system + TSK-0318 public/setup IA + TSK-0320 protection-state model + current accountless/no-routine-support constraints  
**Status:** provisional internal L4 implementation reference; no public/build/launch authority

## 1. Single implementation source

`tokens.css` is the **sole mutable implementation token source** for this TSK-0300 package. All shared colors, typography, spacing, radii, sizing and focus values are declared there.

`components.css` consumes those values only through `var(--sw-...)`. Reference templates consume both shared stylesheets and do not declare an independent brand palette.

The editable identity masters under `brand/identity/TSK-0301/` remain the **asset authority**. TSK-0300 must reference those masters rather than recreate or fork the logo.

## 2. Approved identity binding

- visible brand: `SafeWeb`;
- `Safe` = primary dark green;
- `Web` = warm maroon;
- `UseSafeWeb.com` appears only where the actual domain/project/technical identifier is required;
- `Use` is not visible brand copy or logo text;
- primary logo is the TSK-0301 wordmark, not a shield/lock/security symbol;
- compact identity uses the approved `Sw` monogram only where the full wordmark is impractical.

## 3. Accessibility rules

The primary light-surface wordmark has strong contrast on the approved off-white field. The approved maroon `Web` on a dark-green field is a large decorative/display treatment only because that color pair is low-contrast.

For small, compact, technical, or accessibility-critical dark-background contexts, use the TSK-0301 monochrome/off-white fallback rather than relying on maroon-on-green.

Brand color never communicates protection state. A state must always be expressed with an explicit textual label and supporting evidence/limitation copy. TSK-0320 remains the semantic authority for protection states.

## 4. Canonical state copy used by reference contexts

Reference UI may demonstrate the current TSK-0320 vocabulary only:

- `Verified` — current qualifying system evidence;
- `You confirmed this is set up` — parent-confirmed, not independently verified;
- `Action needed`;
- `Not covered`;
- `Status uncertain`;
- `Removed`.

No template may convert these into an overall safety score, `Safe`, `100% protected`, or similar complete-safety claim. Visual treatment is deliberately neutral/non-color-only.

## 5. Multilingual / RTL behavior

`SafeWeb` is an invariant Latin-script proper brand token. It is LTR, untranslated, unmirrored and unreordered in English, Turkish and Arabic interfaces. Surrounding Arabic content may be RTL independently.

Shared `.sw-brand-token` / `.sw-logo` rules isolate brand direction in RTL layouts. Templates demonstrate structure only; they are not final translations.

## 6. Reference contexts

Exactly six lightweight internal reference templates are included:

1. `templates/public.html` — public discovery/brand context;
2. `templates/product.html` — operational setup/product context;
3. `templates/help.html` — self-service help/recovery context;
4. `templates/status.html` — evidence-state presentation context;
5. `templates/partner.html` — restrained partner/co-brand reference context;
6. `templates/social.html` — restrained static share-card context.

These are **reference templates**, not deployed pages, publication artifacts or evidence of integrated L5/L6 build completion.

## 7. Surface-specific rules

### Public

Use the full wordmark, plain-language proposition, limits and a `Start setup` action. The current baseline has no Login, Dashboard, Account, Pricing or mandatory checkout navigation.

### Product/setup

Branding is subordinate to the task. The setup surface is accountless-first and state-driven; it must not become a marketing dashboard. Instructions and protection-state truth outrank decorative branding.

### Help

Help is self-service by default: source-backed guidance, deterministic checks, recovery/removal and bounded exceptional escalation. Do not promise routine staffed live support.

### Status

Every state must contain textual state + evidence/limitation. No state gets a special brand color that could make color the only carrier of meaning.

### Partner

SafeWeb remains clearly identifiable. A reference co-brand slot must not imply that a real partner has approved, endorsed or certified the product.

### Social

Use the approved identity and bounded truthful proposition. Do not use `100% safe`, `fully protected`, `verified safe`, market-superiority, certification or fear/shame copy.

## 8. Asset conventions

- Reference the TSK-0301 SVG masters by path; do not inline/copypaste their SVG geometry into templates.
- Do not embed font files, raster logos, scripts, remote stylesheets or remote trackers.
- Keep logo alt text exactly `SafeWeb` where an image conveys brand identity.
- Use the primary master on normal light brand surfaces.
- Use the monochrome master for constrained/small dark use.
- Use the compact monogram only where the full wordmark is impractical.
- Production export formats and deterministic outlined assets may be generated later from approved masters where a consuming implementation actually needs them.

## 9. Governance boundary

This package is a provisional internal L4 brand-system implementation. It does not establish or imply:

- representative-parent comprehension/preference or behavioral validation;
- legal/privacy completion;
- participant activation;
- integrated product build completion;
- public publication authority;
- payment activation;
- official non-UK market/support readiness;
- launch approval.

`RSK-0002` remains OPEN. `TSK-0187` remains mandatory future representative-parent behavioral validation where the WBS requires it. Current CR-0004 / DEC-0051 fences remain unchanged.
