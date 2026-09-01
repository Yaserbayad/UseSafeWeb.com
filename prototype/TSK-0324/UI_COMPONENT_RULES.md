# TSK-0324 — Lightweight Visual Identity and Reusable UI Component Rules

**Version:** 1.1.0-post-cr0007
**Status:** internal L4 UX/UI consumer contract  
**Owner:** UX/UI  
**Action authority:** A3 / AUTO_ALLOWED  
**Sequencing:** DEC-0053 / CR-0006 + DEC-0054 / CR-0007; DEC-0052 / CR-0005 remains the pre-L8 human-evidence rule
**Human-validation claim:** none  
**Build/publication authority:** none

## 1. Purpose and authority

This contract defines how SafeWeb public/product/help/status surfaces consume the already-accepted visual identity, tokens, component primitives, protection-state semantics, product language and implementation-ready experience baseline without creating a second design system.

Authority order for this contract:

1. current owner-frozen planning authority including DEC-0053 / CR-0006 and DEC-0054 / CR-0007; DEC-0052 / CR-0005 remains applicable to pre-L8 human-evidence claims;
2. `brand/identity/TSK-0301/` for logo masters and identity geometry;
3. `brand/system/TSK-0300/tokens.css` as the **sole mutable implementation-token source** and `components.css` as the existing shared primitive source;
4. `brand/guidelines/TSK-0297/README.md` for deterministic asset/logo/contrast use;
5. `TSK_0320_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-08-28.md` for S1–S6 evidence-state semantics;
6. `content/TSK-0322/PRODUCT_VOICE_CLAIMS_TERMINOLOGY.md` for current visible identity, claims, CTA and terminology;
7. `prototype/TSK-0309/BASELINE.md` for responsive/accessibility/journey behavior;
8. this TSK-0324 contract for downstream UI composition rules only.

Older TSK-0300/0320 sequencing text that references CR-0003/CR-0004 is superseded by current owner-approved sequencing. The still-valid visual/state rules remain usable unless separately contradicted. Current Version 1 is dual-mode: complete core product value remains usable without login, while optional parent account/session, saved-device continuity, and lightweight dashboard/device-management surfaces are allowed. Account, session, saved-device, or dashboard presence never establishes technical verification.

## 2. Non-fork rule

Downstream implementation MUST consume `--sw-*` tokens from TSK-0300. It MUST NOT:

- introduce a parallel brand palette;
- duplicate logo SVG geometry;
- embed or ship font binaries merely to preserve typography;
- locally rename S1–S6 state labels;
- invent state colors that imply stronger evidence;
- replace `SafeWeb` with `UseSafeWeb`, `UseSafeWeb.com`, a shield, padlock, certification mark or alternate wordmark;
- copy TSK-0323 platform instructions into component styling/content rules.

If a consuming implementation genuinely needs a new shared token, the change must be routed to the owning shared-system authority instead of hard-coding a local value.

## 3. Visual character

SafeWeb UI is whitespace-led, mobile-first, calm and task-directed. Core setup surfaces are operational rather than dashboard-like; the optional signed-in dashboard remains lightweight and task-directed rather than dense administration chrome. Public surfaces may carry more brand expression, but proposition and next action outrank decoration.

Avoid:

- dense admin/dashboard chrome;
- cyber-security neon, surveillance or control theatre;
- gradients or shadow-heavy decorative depth without a functional reason;
- rounded-everything styling that erases hierarchy;
- all-green success compositions that convert mixed evidence into an overall positive impression;
- ornamental icon grids or card grids where a simple ordered flow is clearer.

## 4. Typography contract

The only approved font stack is the TSK-0300 token stack:

`Avenir Next`, `Segoe UI`, `Helvetica Neue`, `Arial`, `sans-serif`.

Use the existing token hierarchy:

- `--sw-font-size-sm` for secondary/helper metadata only;
- `--sw-font-size-base` for ordinary body/control text;
- `--sw-font-size-lg` for emphasized supporting text where hierarchy requires it;
- `--sw-font-size-xl` for the page/screen title;
- `--sw-line-height` for reading text;
- `--sw-line-height-tight` for display headings only.

Rules:

1. one `h1` per page/screen;
2. headings follow logical order; visual size never substitutes for semantic heading level;
3. body copy uses real product language, never lorem ipsum or placeholder prose in acceptance surfaces;
4. critical status/supporting text never drops below the approved small token merely to fit;
5. text must remain usable at 200% text resize without loss of content/function;
6. technical endpoint/domain strings may wrap or scroll within their own bounded code/value container but must not force page-level horizontal overflow.

## 5. Spacing and layout contract

Only the existing spacing scale `--sw-space-1` through `--sw-space-8` is used for shared layout spacing. Arbitrary one-off spacing values are not part of the accepted shared system.

Composition rules:

- `sw-shell` is the normal page container; retain `--sw-page-max` and mobile inset behavior;
- `sw-copy` bounds long-form copy to `--sw-copy-max`;
- `sw-stack` is the default vertical rhythm primitive;
- `sw-row` is used only when actions/items are genuinely peers and may wrap safely;
- cards/panels are used to group one coherent concept, not as a default grid aesthetic;
- setup screens prefer one primary task/decision at a time;
- important limits/help remain discoverable without competing visually with the current primary action.

### Representative responsive acceptance

- **320 px:** one-column critical flow; no page-level horizontal overflow; action groups wrap/stack; brand remains legible; state copy remains visible.
- **768 px:** maintain readable copy width; do not stretch instructional content merely because space exists.
- **1024 px:** secondary supporting information may sit beside primary content only when reading/order semantics remain correct.
- **1440 px:** retain the existing max-width/copy-width bounds; do not convert whitespace into dashboard density.

RTL layouts use logical CSS properties and mirror layout flow only where semantically appropriate. `SafeWeb`, domain names and technical endpoints remain isolated LTR/untranslated.

## 6. Contrast and color contract

TSK-0300 tokens remain authoritative. Accepted current contrast evidence from TSK-0297 includes:

- primary green on off-white ≈ 10.6:1;
- maroon on off-white ≈ 8.4:1;
- off-white on deep green ≈ 10.6:1;
- maroon on deep green ≈ 1.3:1 and therefore **must not** carry small/normal/critical content or focus/state meaning.

Current WCAG 2.2 AA source baseline reviewed 2026-09-01:

- normal text: at least 4.5:1;
- large text: at least 3:1;
- interactive/non-text boundaries and state meaning must remain perceivable without color alone;
- pointer targets meet the current AA 24×24 CSS-pixel minimum or a valid WCAG exception/spacing equivalent.

Brand color is not a protection-state scale. Any optional decorative state tint is subordinate to explicit state text, evidence copy and action semantics.

## 7. Focus and keyboard contract

- Native semantic interactive elements are preferred: `<button>` for actions, `<a>` for navigation.
- Every keyboard-operable control retains a visible `:focus-visible` indicator.
- The existing TSK-0300 light-surface focus treatment uses the 3 px focus-width token and maroon focus token; maroon/off-white has accepted high contrast.
- **Dark-brand fields are display/brand fields, not a default container for interactive controls.** The current maroon/deep-green combination is too low-contrast for a reliable authored focus indicator. A consuming surface must keep interactive controls on a contrast-safe surface, retain an unmodified user-agent focus treatment that remains visible, or route an alternate shared focus token back to the shared-system owner before implementation.
- Focus must not be hidden beneath sticky/fixed content.
- Programmatic screen changes move focus to the current screen `h1` using the accepted TSK-0309 behavior.
- Focus order follows reading/task order; no positive `tabindex` ordering.

## 8. Control contract

### Primary action

Use `.sw-button` for the single dominant next action on a step. Its visible label names the action (`Start setup`, `Check again`, `Review Protection Map`) rather than generic `Continue` when a specific action is available.

### Secondary action

Use `.sw-button--secondary` for a peer but lower-priority action such as `See limits` or a reversible alternate path.

### Quiet action/navigation

Use `.sw-button--quiet` or an ordinary link for low-emphasis help/navigation. Quiet styling must not hide a required recovery/limitations path.

### Removal

`Remove SafeWeb DNS` is explicit and reversible. Do not add a friction-only confirmation modal unless a current implementation demonstrates an irreversible/material consequence that requires it. Removal must produce truthful S6 behavior through the owning journey/state contract.

### Disabled controls

Avoid disabled controls as unexplained dead ends. When an action is unavailable, expose the reason in nearby text and either omit the action or retain a semantic disabled control only when preserving layout/context materially helps comprehension.

### Target size

Buttons generated from the existing padding/type tokens must be verified in implementation to meet the WCAG 2.2 AA target-size requirement. Inline text links may use the standard inline-content exception when applicable; clustered navigation links must retain sufficient target size/spacing.

### Optional account/session/dashboard and lifecycle controls

- Sign-in, account and dashboard navigation is optional continuity UI; it must never gate `Start setup`, verification, Help, recovery or removal.
- Session/account status is announced as account state only and must never reuse S1–S6 protection-state styling as evidence of device protection.
- A saved-device card distinguishes saved record metadata from current Protection Map evidence; record presence cannot create `Verified`.
- Logout, account deletion, saved-record deletion, revoke/unlink and physical SafeWeb DNS removal use distinct labels and consequences.
- Destructive account/device actions require the current lifecycle confirmation pattern, keyboard-operable controls, visible focus, and a deterministic return/focus target after completion or cancellation.
- If a destructive provider result is unknown, the UI states uncertainty, blocks duplicate destructive replay and offers authoritative read-back/recovery; it never announces success.
- At 320 px, optional account/dashboard navigation may collapse or wrap but cannot hide the accountless core path, current protection truth, recovery or removal.
- Dashboard/device-management surfaces remain lightweight: no browsing/query/activity history, child profiles/accounts or broad/raw DNS administration.

## 9. Protection Map / state component contract

ACC-0324’s historical “four Protection Map states” minimum is satisfied and superseded in current semantic authority by the complete **six-state S1–S6 model**. The UI MUST support all six without renaming or collapsing them:

| State | Visible label | Visual rule | Required supporting behavior |
| --- | --- | --- | --- |
| S1 | `Verified` | neutral structured state panel; optional positive icon is supplementary only | identify qualifying current SafeWeb evidence; never imply overall safety |
| S2 | `You confirmed this is set up` | visually distinct label from S1; never reuse S1 copy/icon semantics as equivalent proof | state that SafeWeb has not independently verified it |
| S3 | `Action needed` | explicit attention label; no success styling | show one known next action where available |
| S4 | `Not covered` | neutral limitation treatment, not error theatre | explain unsupported/out-of-scope boundary |
| S5 | `Status uncertain` | explicit uncertainty treatment; never preserve stale success emphasis | explain that current evidence is insufficient/conflicting and give safe next check where known |
| S6 | `Removed` | explicit inactive/removal treatment | withdraw active SafeWeb protection claim and expose reconfigure path separately |

Every Protection Map item contains:

1. layer name (`Phone`, `Internet`, `Service` where applicable);
2. exact state label;
3. one evidence/limitation sentence;
4. at most one immediate next action when one is safe/useful;
5. material “does not cover” disclosure where required.

Never render a combined safety score, all-green completion badge, shield, certification mark or copy such as `Fully protected`.

## 10. Feedback components

### Busy / checking

- mark the relevant region `aria-busy="true"` while a qualifying asynchronous check is running;
- retain a textual operation label such as `Checking…`; a spinner alone is insufficient;
- prevent duplicate submission while the same check is in flight;
- once settled, move/update the result in the same logical region without stealing focus unexpectedly.

### Success / verified result

Success feedback is only permitted when the owning evidence contract supports S1. It says what was verified, not that the child/device is “safe.”

### Parent-confirmed result

Confirmation feedback uses S2 language and cannot inherit `Verified` text or equivalent visual proof strength.

### Error / action needed

State what failed/needs attention, expose one safe next action, and preserve the user’s ability to reach Help, Limitations or removal/recovery where applicable.

### Uncertain / unsupported

Use S5/S4 explicitly. Do not silently retry forever, convert uncertainty into success, or invent a workaround.

### Announcements

Use polite status announcements for ordinary asynchronous results. Reserve assertive alert semantics for material errors requiring immediate attention; do not make routine success messages intrusive.

## 11. Reusable component specifications

| Component | Semantic base | Required behavior |
| --- | --- | --- |
| `PageShell` | `main` + shared shell | one primary content region; max-width/mobile insets; RTL-safe logical layout |
| `BrandHeader` | `header` + `nav` where present | approved logo master; `SafeWeb` alt; accountless core navigation remains available; optional sign-in/account/dashboard navigation may appear where current IA permits; visible keyboard focus |
| `ScreenTitle` | `h1` | one per screen; programmatic focus target after screen change |
| `ActionGroup` | grouped buttons/links | one primary action; wraps/stacks safely; keyboard order = visual/reading order |
| `PrimaryButton` | `button` or action link | explicit action label; visible focus; target-size acceptance |
| `SecondaryButton` | `button`/link | same accessibility as primary without competing emphasis |
| `QuietAction` | link/button | help/navigation only; remains discoverable |
| `Panel/Card` | semantic section/article as appropriate | one coherent concept; heading relationship; border not sole critical affordance |
| `ProtectionMapItem` | section/list item | layer + exact S1–S6 label + evidence/limit + optional next action; color never sole meaning |
| `FeedbackCallout` | status/alert semantics by urgency | busy/success/action/uncertain/not-covered/removal semantics remain truthful |
| `HelpLink` | link | point-of-need self-service; state-neutral |
| `LimitationsLink` | link | exposes support/scope boundary; state-neutral |
| `TechnicalValue` | code/text container | exact LTR endpoint/domain inside RTL; selectable; does not force page overflow |

No SafeWeb password/credential field, child profile field, payment field or diagnostic upload is part of the current critical journey. Optional Google sign-in/account continuity uses the separately approved account/session flow and must not create a local credential form. Adding materially broader identity, child, payment, activity-history or diagnostic collection requires separate necessity, privacy and scope authority rather than a local component variant.

## 12. Logo and domain use

- Visible brand is exactly `SafeWeb`.
- Default light surface uses the primary TSK-0301 wordmark.
- Small/single-color/accessibility-critical/dark contexts use the approved monochrome fallback where required.
- Large confirmed dark identity fields may use the approved inverse master; do not use maroon-on-deep-green for small/critical text.
- `Sw` monogram is icon/compact-only when the full wordmark is impractical.
- `UseSafeWeb.com` appears only when the actual domain/project identifier is useful.
- `dns.usesafeweb.com` and `https://dns.usesafeweb.com/dns-query` are exact technical values, never brand copy.
- Never translate, mirror, redraw, recolor or recreate the wordmark locally.

## 13. Accessibility acceptance specification

A downstream implementation is not compliant with this contract unless applicable components satisfy all of the following:

1. semantic controls and meaningful heading structure;
2. complete keyboard operation with visible, unobscured focus;
3. WCAG 2.2 AA text contrast and applicable non-text/target-size requirements;
4. critical state meaning never depends on color alone;
5. screen changes/focus behavior match the frozen TSK-0309 contract;
6. loading/checking state is programmatically exposed and settles correctly;
7. text can resize to 200% without losing content/function;
8. representative 320 px layout has no page-level horizontal overflow;
9. EN/TR/AR and RTL preserve the same task/state evidence semantics;
10. icons, if used, are supplementary for critical meaning or have an accessible name where independently actionable;
11. error/uncertain/not-covered/removal paths remain reachable without mouse-only interaction;
12. no inaccessible low-contrast brand treatment is repurposed for critical copy/focus/state.

## 14. External accessibility source review

Reviewed 2026-09-01 against current first-party W3C sources:

- WCAG 2.2 Recommendation: `https://www.w3.org/TR/WCAG22/` — current Level AA text-contrast baseline, focus-visible/focus-not-obscured requirements and related success criteria.
- W3C Understanding SC 2.5.8 Target Size (Minimum): `https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum` — current Level AA 24×24 CSS-pixel target minimum with documented exceptions/spacing alternatives.
- W3C Understanding SC 2.4.13 Focus Appearance: `https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html` — AAA, used only as non-binding stronger reference for visible focus; this contract does not misstate it as an AA requirement.

## 15. QA projection

TSK-0324 acceptance should assert at minimum:

- typography rules bind only to the current token stack/scale;
- spacing rules bind only to the current shared scale;
- accepted contrast-safe pairs remain above current thresholds and maroon/deep-green remains prohibited for small/critical content;
- focus-visible behavior exists and dark-field focus risk is explicitly fenced;
- primary/secondary/quiet controls and target-size verification are specified;
- feedback covers checking, verified, parent-confirmed, action-needed, not-covered, uncertain and removed states;
- all six current Protection Map states are supported, thereby satisfying the historical four-state minimum without dropping S5/S6;
- 320/768/1024/1440 responsive behavior is specified;
- logo/domain/RTL rules are deterministic;
- accessible component specifications are implementation/QA-testable;
- optional account/session/dashboard/device-lifecycle controls preserve accountless core access, keyboard/focus semantics, truthful protection state, explicit destructive consequences, and uncertainty on unknown destructive results;
- no token/logo/state/claim/account fork is created.

## 16. Non-inference fence

This is an internal L4 UI rules contract. It does not self-certify the HUMAN_ONLY TSK-0308 shared responsive design-system task, does not prove real-parent/native-speaker usability or comprehension, and does not authorize production implementation, public publication, participant processing, payment, market activation or launch. `RSK-0002` remains OPEN.
