# TSK-0308 — Shared Responsive Design System Candidate

**Version:** 1.0.0-candidate  
**Status:** **CANDIDATE / HUMAN DECISION REQUIRED / NOT PASS**  
**Task:** `TSK-0308 — Create the shared responsive design system for public and product surfaces`  
**Action authority:** `HUMAN_ONLY`  
**Preparation authority:** Project Owner instruction 2026-08-29 to prepare TSK-0308  
**Sequencing:** `DEC-0052 / CR-0005`  
**Build/publication authority:** none

## 1. Decision proposed

Approve one shared responsive composition system for both SafeWeb public and operational setup surfaces, implemented as a **thin composition layer over the already accepted TSK-0300 brand system**.

The candidate does **not** fork or replace TSK-0300. It keeps:

- `brand/system/TSK-0300/tokens.css` as the sole mutable shared token source;
- `brand/system/TSK-0300/components.css` as the existing primitive implementation source;
- TSK-0301 as logo/identity authority;
- TSK-0320/0322 as protection-state and product-language authority;
- TSK-0309 as the frozen journey/accessibility behavior baseline;
- TSK-0324 as the current UI-consumer rules contract;
- TSK-0328 as the current public/setup IA and navigation contract.

TSK-0308 adds only reusable **composition patterns and implementation specifications** needed to make those authorities coherent across public and product surfaces.

## 2. Source bindings

This candidate is prepared against these exact current source blobs:

| Source | Role | Blob |
| --- | --- | --- |
| `brand/system/TSK-0300/README.md` | shared-system ownership/rules | `4baa67f565c14c3034fca47bb5fad0b9ff71b091` |
| `brand/system/TSK-0300/tokens.css` | sole token source | `cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f` |
| `brand/system/TSK-0300/components.css` | shared primitive source | `831e92a74b6dda04252d93242cb33bd491a02381` |
| `prototype/TSK-0309/BASELINE.md` | frozen experience baseline | `76bb848ebdf6a2aee4dd84bc18e8af5ba8a99dbc` |
| `prototype/TSK-0324/UI_COMPONENT_RULES.md` | UI composition/accessibility rules | `0b7012a12070f7eccf45a1bbb2f453fde8507ff6` |
| `prototype/TSK-0328/INFORMATION_ARCHITECTURE_NAVIGATION.md` | public/setup IA/navigation | `4efb624005061e242e427994953d0fc00fcd745f` |
| `content/TSK-0322/PRODUCT_VOICE_CLAIMS_TERMINOLOGY.md` | current terminology/claims | `d12c1e707f0390915002b27bf3a5073d0135d466` |
| `brand/identity/TSK-0301/README.md` | approved identity | `b8ffd2ed234465a238558a7b94e56274de49696a` |
| `Plans/Master/WBS/master-wbs.csv` | task/ACC/VER/EVD authority | `f23b4f017d1baf73258fa30ecd71549bbfe1b815` |

Older source text referring to CR-0003/CR-0004 is historical sequencing only; current `DEC-0052 / CR-0005` governs sequencing.

## 3. Binding design-system principles

1. **One system, two purposes.** Public surfaces explain and route; setup surfaces perform the current task. They share identity, tokens, accessibility and component semantics without becoming the same navigation model.
2. **Mobile-first and whitespace-led.** Critical setup is one-column by default. Larger screens may add supporting context without turning setup into a dashboard.
3. **No token fork.** Candidate CSS may consume `var(--sw-*)` only. New shared values must be routed back to the TSK-0300 owner rather than hard-coded locally.
4. **Evidence truth outranks visual optimism.** Parent confirmation is never styled or labelled as equivalent to system verification.
5. **State meaning is textual.** Color, icons, animation and position are supplementary only.
6. **No mandatory account/dashboard.** No Login, Account, Dashboard, Profile, child-profile, payment, browsing-history or DNS-query-history component is part of this system.
7. **Self-service by default.** Error/recovery/help patterns must resolve ordinary issues without creating a routine staffed-support dependency.
8. **Multilingual from structure, not duplication.** EN/TR/AR+RTL share the same component contracts. `SafeWeb`, domain names and technical endpoints remain isolated LTR.
9. **Implementation and QA must be deterministic.** Each component has semantic structure, states, accessibility behavior, responsive behavior and acceptance assertions.

## 4. Shared responsive surface model

### Public surface

Public pages may use broader composition and stronger brand presence while remaining restrained:

- `BrandHeader`
- `PublicHero`
- `ContentSection`
- `Evidence/limits panel`
- `ActionGroup`
- `Help/Privacy/Compatibility references`
- `Start setup` as the dominant transition action where applicable.

Public primary navigation remains exactly the current IA set: **Home, How it works, Compatibility & limits, Privacy, Help, Start setup**. No account/dashboard/pricing navigation is introduced.

### Product/setup surface

Setup uses task-state composition rather than site chrome:

- `TaskHeader`
- `ScreenTitle`
- `InstructionPanel`
- `TechnicalValue`
- `ActionGroup`
- `FeedbackCallout`
- `ProtectionMap`
- contextual `Help` / `Limitations`
- `Start over` and conditional `Remove SafeWeb DNS` recovery utilities.

The setup surface remains one generic operational route/state container. It does not create per-user indexable routes or persistent account navigation.

## 5. Component catalogue

### DS-01 — `ResponsiveShell`

**Purpose:** shared page boundary for public and setup surfaces.  
**Semantic base:** `main` using existing `.sw-shell`.  
**Behavior:** mobile-first full readable flow; existing page/copy max widths remain authoritative; logical properties only for direction-sensitive spacing.  
**Accessibility:** one primary content region; skip-target capable; no page-level overflow at 320 px.  
**Implementation:** compose existing `.sw-shell`, `.sw-stack`, `.sw-copy`; candidate composition CSS may only add layout classes using current tokens.

### DS-02 — `BrandHeader`

**Purpose:** brand + permitted navigation.  
**Semantic base:** `header` plus `nav` only when navigation exists.  
**Public:** may expose the current six public navigation intents.  
**Setup:** reduced header; branding subordinate to task, with Help/Limitations as utilities rather than marketing navigation.  
**Accessibility:** approved logo/alt, keyboard-operable navigation, visible focus.  
**Exclusions:** Login, Account, Dashboard, Profile, Pricing gate.

### DS-03 — `ScreenHeader`

**Purpose:** identify current task/state.  
**Semantic base:** exactly one `h1` per current screen.  
**Behavior:** programmatic screen changes focus the current `h1` according to TSK-0309.  
**Localization:** no fixed heading height; wraps naturally in EN/TR/AR; technical brand tokens remain LTR-isolated.

### DS-04 — `ContentPanel`

**Purpose:** group one coherent explanation/instruction/limit.  
**Semantic base:** `section`/`article` as appropriate.  
**Behavior:** never used merely to create card-grid decoration; may contain heading + body + one related action.  
**Accessibility:** heading relationship explicit; border is not sole grouping cue.

### DS-05 — `ActionGroup`

**Purpose:** present the smallest necessary choice set.  
**Rules:** one dominant next action; secondary/quiet actions only where required; explicit labels over generic `Continue` when the action is known.  
**Responsive:** inline only when genuine peers fit; otherwise wrap/stack without reordering.  
**Accessibility:** DOM order = reading/visual order; existing focus treatment; target size verified in implementation.

### DS-06 — `LoadingFeedback`

**Purpose:** expose an active technical check or bounded asynchronous operation.  
**Semantic contract:** relevant region sets `aria-busy="true"`; textual `Checking…` or operation-specific label is always present; decorative activity indicator is `aria-hidden`.  
**Behavior:** duplicate submission is suppressed during the same in-flight check; settled result replaces/updates the same logical region.  
**Motion:** animation is optional and disabled under `prefers-reduced-motion: reduce`.

### DS-07 — `VerificationResult`

**Purpose:** render evidence-backed result without overstating scope.  
**S1:** exact label `Verified`; qualifying current technical evidence must be named/summarized.  
**S2:** exact label `You confirmed this is set up`; explicitly states SafeWeb did not independently verify it.  
**Invariant:** S2 can never reuse S1 wording, proof language or equivalent visual hierarchy as evidence.  
**No overall safety score or `Fully protected` state.**

### DS-08 — `ActionNeeded/ErrorFeedback`

**Purpose:** explain a known failure or required correction.  
**Semantic contract:** use ordinary status semantics for non-urgent validation; `role="alert"` only for material errors requiring immediate attention.  
**Content:** what failed/needs attention + one safe next action where known + Help/Limitations/recovery access.  
**Recovery:** identical failed checks are not looped without changed conditions.

### DS-09 — `UncertainOrNotCovered`

**Purpose:** represent insufficient/conflicting evidence or unsupported scope.  
**S5:** exact `Status uncertain`.  
**S4:** exact `Not covered`.  
**Behavior:** no silent optimistic fallback, no invented workaround, no degraded-but-green success treatment.  
**Action:** one safe next check/help route only when source-backed.

### DS-10 — `ProtectionMap`

**Purpose:** show independent Phone / Internet / Service evidence states.  
**Supported states:** complete S1–S6 vocabulary: `Verified`, `You confirmed this is set up`, `Action needed`, `Not covered`, `Status uncertain`, `Removed`.  
**Each item:** layer + exact label + evidence/limitation sentence + at most one immediate action + material non-coverage note where required.  
**Layout:** one column on narrow screens; may become two/three-column only when reading order and independent layer semantics remain clear.  
**No aggregate score, shield/certification badge or all-green completion composition.**

### DS-11 — `RecoveryPanel`

**Purpose:** restore a safe understandable state after failed activation, removal, reset or lost transient state.  
**Variants:** `remove`, `recovery-check`, `start-over`, `state-lost`.  
**Removal:** explicit `Remove SafeWeb DNS`; after exact removal active DNS protection wording is withdrawn and S6 `Removed` applies.  
**Start over:** clears web journey state only and must explicitly not imply device DNS removal.  
**State lost:** restart routing/verification; do not fabricate persistent resume.

### DS-12 — `HelpAndLimitations`

**Purpose:** globally reachable self-service support without mutating evidence state.  
**Behavior:** contextual Help and Limitations are state-neutral utility detours; they preserve current active in-memory journey where available.  
**Constraint:** ordinary completion/recovery must not depend on routine human support. Exceptional owner intervention remains outside this component contract.

### DS-13 — `TechnicalValue`

**Purpose:** show exact hostname/domain/profile or other technical value.  
**Behavior:** selectable/copyable where useful; isolated LTR inside RTL; wraps/bounds locally without page-level overflow; never translated.  
**Examples remain governed by the current instruction catalogue, not hard-coded by this design system.**

## 6. Required state matrix

ACC-0308 explicitly requires content/error/loading/verification/uncertain/recovery coverage. This candidate binds them as follows:

| Required class | Component | Testable outcome |
| --- | --- | --- |
| Content | DS-03/04 | semantic heading/content structure remains readable/responsive |
| Loading | DS-06 | textual busy state + `aria-busy`; no duplicate action |
| Verification | DS-07/10 | S1 only with system evidence; S2 visibly/semantically distinct |
| Error / action needed | DS-08 | failure + safe next action + support/recovery access |
| Uncertain / unsupported | DS-09 | S5/S4 explicit; no optimistic fallback |
| Recovery | DS-11 | removal/reset/lost-state semantics remain distinct and reversible |

## 7. Responsive contract

### 320 px

- one-column critical setup flow;
- no page-level horizontal overflow;
- action groups stack/wrap without logical reordering;
- all state/evidence text remains visible;
- technical values stay within their own container.

### 768 px

- readable copy width remains bounded;
- public content may use a modest two-column composition when useful;
- setup remains task-first; supporting content may sit beside the primary task only if reading order stays correct.

### 1024 px

- public surfaces may use asymmetric content/support layouts;
- Protection Map may use multiple columns only when each item remains independently understandable;
- setup does not gain dashboard navigation or dense admin chrome.

### 1440 px+

- keep TSK-0300 max-width/copy-width bounds;
- additional whitespace is preserved rather than converted to dashboard density.

## 8. Localization and RTL contract

- First public-release structural capability: English, Turkish, Arabic/RTL.
- `SafeWeb`, `UseSafeWeb.com`, domains, URLs, DNS hostnames and code-like technical values remain LTR/untranslated as applicable.
- Use logical CSS properties (`margin-inline`, `padding-inline`, `inset-inline`, logical text alignment where appropriate).
- Component height is content-driven; no fixed-height labels/buttons/callouts that assume English length.
- Buttons and navigation labels wrap without clipping; no ellipsis on critical action/state text.
- Flex/grid children use `min-width: 0` where needed so long Turkish/Arabic content does not force page overflow.
- RTL changes layout direction where semantically appropriate but does not reverse chronological/progress/state evidence meaning.
- Language availability must never imply official non-UK market/legal/support/channel activation before its gate.
- Candidate QA may stress text length/direction mechanically, but such stress text is not a translation or native-speaker validation claim.

## 9. Accessibility contract

Implementation acceptance must include:

1. semantic native controls and logical heading order;
2. complete keyboard operation and visible/unobscured focus;
3. WCAG 2.2 AA text/non-text contrast requirements as applicable;
4. critical meaning independent of color/icon alone;
5. 200% text resize without loss of content/function;
6. 320 px no page-level horizontal overflow;
7. loading/checking exposed programmatically and textually;
8. screen-change focus behavior from TSK-0309;
9. pointer targets meeting the current WCAG 2.2 AA minimum or valid exception/spacing case;
10. S1/S2 evidence distinction perceivable in text and semantics, not only style;
11. error/uncertain/not-covered/recovery paths keyboard reachable;
12. reduced-motion support for optional activity animation;
13. RTL reading/focus order remains logical;
14. exact technical values stay readable/copyable without breaking page layout.

## 10. Necessity / no-account / support controls

Under REQ-0028 every added interaction must map to a current user goal. This design system therefore contains **no generic form-field library by default**. The current critical journey has no justified identity, child-profile, payment, diagnostic-upload or account field.

Under CON-0010 no mandatory account component/navigation is included.

Under CON-0022 ordinary error/recovery components are self-service. A generic `Contact support` dependency is not a completion requirement; exceptional intervention is separately governed.

## 11. Public vs product implementation rules

Both surfaces consume the same tokens/primitives/composites, but purpose remains distinct:

- **Public:** explain proposition, limits, compatibility, privacy and Help; route intentionally to Start setup.
- **Setup:** perform one current task/state at a time; show technical truth, recovery and next action; avoid marketing navigation and dashboard framing.

A public page can never manufacture `Verified` or another operational evidence state. A setup surface cannot silently add signup/payment/account steps.

## 12. Candidate implementation files

- `candidate.css` — composition-only candidate layer; consumes existing `--sw-*` values; no raw brand colors, font families, logo geometry or renamed state tokens.
- `reference.html` — internal representative public/product/state/recovery composition for browser QA; not deployable/public content.
- `DESIGN_SYSTEM_MAP.json` — non-authoritative deterministic projection for verification.

## 13. Owner decision boundary

This package may be structurally/browser tested during preparation, but **TSK-0308 cannot become PASS without explicit Project Owner approval** because WBS Action Authority is `HUMAN_ONLY`.

Approval would accept this candidate as the shared responsive design-system contract for downstream engineering/QA. Rejection or revision must identify the material change needed; the candidate remains non-PASS until a new exact version is explicitly approved and then verified against ACC-0308/VER-0308/EVD-0308.

## 14. Non-inference fence

Preparation/approval of this L4 design system does not by itself prove real-parent/native-speaker usability, legal completion, integrated production build, public publication, participant processing, payment activation, non-UK market/support readiness or launch authority. Human/user validation remains deferred under current CR-0005 sequencing until the integrated product stage.
