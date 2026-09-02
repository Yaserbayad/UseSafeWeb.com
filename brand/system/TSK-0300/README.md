# TSK-0300 — SafeWeb Shared Brand System

**Task:** TSK-0300 — Translate the approved identity into shared tokens, components, templates, and asset conventions  
**Authority:** owner-approved TSK-0301 identity + corrected TSK-0299 verbal system + current TSK-0318 dual-mode public/setup IA + TSK-0320 protection-state model + current TSK-0316 friction contract + accountless-first/no-routine-support constraints  
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

The same owner-approved SafeWeb identity applies to the complete accountless core and the optional parent-account/session/dashboard/device-management continuity surfaces. Optional account capability does not create a second identity, palette, logo, component system or protection-state vocabulary.

## 3. Accessibility rules

The primary light-surface wordmark has strong contrast on the approved off-white field. The approved maroon `Web` on a dark-green field is a large decorative/display treatment only because that color pair is low-contrast.

For small, compact, technical, or accessibility-critical dark-background contexts, use the TSK-0301 monochrome/off-white fallback rather than relying on maroon-on-green.

Brand color never communicates protection state. A state must always be expressed with an explicit textual label and supporting evidence/limitation copy. TSK-0320 remains the semantic authority for protection states.

## 4. Canonical state copy used by reference contexts

Reference UI may demonstrate the current TSK-0320 vocabulary only:

- `Protection verified` — current qualifying technical evidence;
- `Setup confirmed` — configuration/parent confirmation only; mandatory supporting copy: `Protection has not yet been technically verified.`;
- `Action needed`;
- `Not covered`;
- `Protection status could not be verified`;
- `Removed`.

No template may convert these into an overall safety score, `Safe`, `100% protected`, or similar complete-safety claim. Visual treatment is deliberately neutral/non-color-only.

Account ownership, a valid session, dashboard presence, a managed-device record, or stored status never upgrades a protection state without the qualifying current evidence owned by TSK-0320.

## 5. Multilingual / RTL behavior

`SafeWeb` is an invariant Latin-script proper brand token. It is LTR, untranslated, unmirrored and unreordered in English, Turkish and Arabic interfaces. Surrounding Arabic content may be RTL independently.

Shared `.sw-brand-token` / `.sw-logo` rules isolate brand direction in RTL layouts. Templates demonstrate structure only; they are not final translations.

## 6. Reference contexts

Exactly six lightweight internal reference templates are included:

1. `templates/public.html` — public discovery/brand context, including a secondary optional sign-in/manage entry;
2. `templates/product.html` — operational setup/product context, including accountless completion and optional continuity treatment;
3. `templates/help.html` — self-service help/recovery context;
4. `templates/status.html` — evidence-state presentation context;
5. `templates/partner.html` — restrained partner/co-brand reference context;
6. `templates/social.html` — restrained static share-card context.

These are **reference templates**, not deployed pages, a complete IA implementation, publication artifacts or evidence of integrated L5/L6 build completion. The authoritative route/screen inventory remains TSK-0318.

## 7. Surface-specific rules

### Public

Use the full wordmark, plain-language proposition, limits and a primary `Start setup` action. A secondary `Sign in / Manage devices` route may expose the approved optional continuity feature, but it must never replace, visually dominate or gate `Start setup`. Public surfaces do not expose a dashboard, protection history, child profile, raw DNS-query/admin console or payment gate.

### Product/setup

Branding is subordinate to the task. The complete setup/verification/help/removal/recovery core remains accountless-first and state-driven. Optional sign-in/session/dashboard/device-management continuity may appear only at an appropriate explicit choice or authenticated account-only context; cancel/failure/provider outage returns to an accountless-capable route. Product surfaces must not become a marketing dashboard.

Successful sign-in does not automatically join, import, promote, copy or extend J0/J1 state and does not by itself create a managed-device record. Logout, revoke/unlink, dashboard-record deletion, account deletion, anonymous-state deletion and physical SafeWeb DNS removal remain distinct operations.

### Help

Help is self-service by default: source-backed guidance, deterministic checks, recovery/removal and bounded exceptional escalation. Do not promise routine staffed live support.

### Status

Every state must contain textual state + evidence/limitation. No state gets a special brand color that could make color the only carrier of meaning. Account/device ownership or stored dashboard state is not current technical verification.

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

## 9. Dual-mode privacy and continuity conventions

- Accountless core remains fully usable without login.
- Optional account continuity is explicit and non-coercive.
- No automatic J0/J1-to-account linkage, migration, promotion or expiry extension is implied by brand/system references.
- No child account/profile, browsing/query/activity history or unrestricted DNS administration is introduced.
- A managed-device record is minimum bounded continuity metadata, not a child identity and not protection proof.
- Provider/account failure affects account-only functions; it does not change configured DNS truth or remove accountless help/removal paths.
- Destructive/lifecycle labels must name the actual object affected and must not imply that a separate operation completed.

## 10. Governance boundary

This package is a provisional internal L4 brand-system implementation. It does not establish or imply:

- representative-parent comprehension/preference or behavioral validation;
- legal/privacy completion;
- participant activation;
- integrated product build completion;
- public publication authority;
- payment activation;
- official non-UK market/support readiness;
- launch approval.

`RSK-0002` remains OPEN. Current pre-L8 sequencing remains controlling; no behavioral/user evidence is inferred by this internal reference package.
