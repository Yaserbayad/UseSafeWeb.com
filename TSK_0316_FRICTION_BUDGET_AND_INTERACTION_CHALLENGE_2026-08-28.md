# TSK-0316 — Friction Budget and Interaction Challenge

**Task:** TSK-0316 — Define a friction budget and challenge every click, field, choice, confirmation, account, and manual step  
**Acceptance:** ACC-0316  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** INTERNAL PROVISIONAL L4 FRICTION CONTRACT / IMPLEMENTATION NOT AUTHORIZED  
**Date:** 2026-08-28  
**Authority:** TSK-0315 service blueprint + TSK-0229 accountless data contract + TSK-0408 platform DNS contract + TSK-0320 protection-state contract + DEC-0050/CR-0003  
**Verification state:** PASS candidate pending independent verification and runtime reconciliation.

## Provisional evidence limitation — RSK-0002 remains OPEN

There is no representative-parent evidence proving that the retained journey is short enough, easy enough, preferred, or behaviorally optimal. L3 real-participant validation remains deferred through 2027-08-27 or earlier owner reactivation. This friction budget is therefore a **design minimisation contract**, not a measured usability target. `RSK-0002` remains OPEN.

No fabricated click-count, completion-time, abandonment-rate, or conversion target is introduced. This artifact does not make LG-05/LG-06 PASS and does not authorize implementation/build, participants, legal completion, payment, public release or launch.

## 1. Friction-budget rule

The active budget is:

> **One user interaction is allowed only when one current decision, technical action, safety/truth requirement, evidence requirement, or recovery requirement cannot be satisfied safely with less user work. All decorative, duplicated, identity-seeking, engagement-seeking, analytics-seeking, or unsupported “confirmation” friction has a budget of zero.**

This is deliberately purpose-based rather than a fabricated universal screen/click count. Platform-required manual work differs between Android/iPhone and may change over time; a fixed numerical click target would be unsupported without real-user/platform evidence.

## 2. Zero-budget interactions — remove/prohibit

The current core journey has **zero allowance** for:

- mandatory UseSafeWeb account/login/sign-up;
- parent name, child name, email or phone collection merely to start/finish setup;
- persistent child/device profile creation;
- card/trial/payment before core value;
- onboarding carousels or “next/next/next” education that can be delivered at point of need;
- a separate mandatory “How it works” screen when the essential trust/limit message can appear beside Start;
- repeated confirmation of a value already known in current transient state;
- re-entering the same device/platform fact in another step;
- opt-in boxes that are not actually required by the owning legal/product rule;
- marketing newsletter/notification prompts in the setup journey;
- rating/review/referral prompts before or during first setup;
- generic survey questions;
- hidden analytics/behavioral-tracking choices used to create user profiles;
- a mandatory “Finish” click if the final Protection Map can be safely rendered and completion/deletion semantics can execute without it;
- confirmation dialogs for ordinary reversible navigation where there is no material loss/risk;
- a universal DNS FQDN/URL field pretending Android and Apple use the same mechanism;
- requests for real browsing/domain history to prove DNS protection;
- unrestricted free-text support fields by default;
- a mandatory external-service step when no approved relevant safeguard applies;
- forcing unsupported platform paths to continue until they resemble success.

## 3. Budget classes

### B1 — Irreducible decision

Allowed only when the system cannot safely/accurately choose the branch.

Examples:

- selecting/confirming device family when it cannot be safely derived;
- choosing among genuinely different supported paths;
- confirming a native/service safeguard where system verification is unavailable;
- choosing to remove/reset protection.

**Rule:** one interaction per genuine decision; do not ask the same decision in multiple words/screens.

### B2 — Irreducible platform action

Allowed when the OS/service requires an explicit user action that UseSafeWeb cannot safely automate.

Examples:

- entering Android Private DNS provider hostname;
- approving/installing an Apple DNS profile through the current supported OS flow;
- changing a native parental-control setting;
- changing one approved external-service safeguard.

**Rule:** do not count OS security/consent friction as removable product friction, but remove UseSafeWeb steps around it that do not change the technical result.

### B3 — Truth/evidence confirmation

Allowed when needed to distinguish parent-confirmed from system-verified state.

Examples:

- `I set this up` after a native/service action that UseSafeWeb cannot verify;
- explicit retry/recheck after a failed or uncertain technical verification.

**Rule:** never ask for confirmation merely to manufacture a positive state. Parent confirmation yields TSK-0320 S2, not S1.

### B4 — Conditional compatibility detail

Allowed only when current routing/support depends on it and the system cannot safely derive it.

Examples:

- OS/version support band;
- phone `new/already used/unknown` only if native-routing logic proves it changes the required path;
- a relevant service category only if TSK-0144 proves it is needed.

**Rule:** if later platform/routing work shows the field does not change the outcome, remove it.

### B5 — Recovery/help action

Allowed only after a failure, uncertainty, removal request or user-invoked help need.

Examples:

- Retry verification;
- Reset/reconfigure;
- Remove UseSafeWeb DNS;
- Show issue-specific troubleshooting;
- Escalate an exceptional security/privacy/legal/safeguarding condition.

**Rule:** recovery actions must not be part of the happy path merely because they exist.

## 4. Interaction-by-interaction challenge of TSK-0315

| Current blueprint interaction | Decision | Why retained / change | Budget class | Resulting rule |
| --- | --- | --- | --- | --- |
| Public landing → Start | **Retain one Start action** | Explicitly separates informational website from product/setup context. | B1 | One primary Start; no signup/payment gate. |
| Separate Understand/Trust screen | **Remove as mandatory screen** | Essential protection limits/privacy can be concise, visible beside/before Start and again at point of impact. A dedicated forced screen adds no necessary decision. | Zero | Keep content, remove forced progression step unless later evidence proves necessity. |
| Locale | **Default automatically where safe; retain visible switch** | Needed for multilingual rendering, but forcing every user to choose a language is unnecessary when a supported locale can be selected from browser preference/default without persistent profiling. | B4 | No mandatory locale question when a safe default exists; always allow change. |
| Device family | **Retain only if not safely derivable/ambiguous** | Android and Apple use different mechanisms. Wrong inference can cause bad instructions. | B1/B4 | Auto-suggest from non-persistent current client context when reliable; ask/confirm when ambiguous. Do not fingerprint/store. |
| Exact/coarse OS version | **Conditionalize** | Ask only when the supported matrix/instructions differ and current context cannot supply sufficient routing evidence. | B4 | No universal version question. TSK-0409 owns exact need. |
| Phone `new/already used/unknown` | **Conditionalize aggressively** | Current blueprint says this is needed only if native-safeguard routing differs. TSK-0143 has not yet proven necessity. | B4 | Do not include in default intake until TSK-0143 demonstrates a branch. |
| Native safeguard setup | **Retain when applicable** | Real platform action needed for the native-control layer; details remain TSK-0143-owned. | B2 | One coherent instruction sequence; skip/already-configured allowed. |
| Native safeguard completion confirmation | **Retain only when no system verifier exists** | Needed to distinguish incomplete from parent-confirmed state. | B3 | One confirmation; yields S2, never S1. |
| Internet/DNS setup choice | **Retain platform-specific action, remove generic mechanism chooser where only one approved method exists** | Current accepted mechanisms differ by platform but do not require the parent to understand protocol names. | B2 | Route automatically to the one approved method for the exact supported combination; do not ask “DoH or DoT?”. |
| Android DNS setup | **Retain unavoidable OS action** | Current accepted native mechanism requires Android Private DNS provider hostname `dns.usesafeweb.com`; no approved one-click automatic system-change mechanism is established. | B2 | Provide copy/copy-to-clipboard where appropriate, then user completes OS setting. Do not claim one-click setup. |
| Apple DNS setup | **Retain unavoidable OS/profile authorization action** | Current accepted path uses a DoH profile; exact release profile/distribution still requires artifact-level verification. | B2 | Present approved profile path only when supported; OS/user authorization remains explicit. Do not imply silent install. |
| DNS verification | **Retain** | Required to prevent configuration presence/parent confirmation from masquerading as active protection. | B3 / system action | One clear Check/Recheck action only if verification cannot run automatically at the appropriate moment; otherwise run automatically and show result. |
| External-service safeguard | **Conditionalize** | Product permits at most one relevant approved service step; not every user has one. | B4/B2 | Ask only the minimum routing fact needed by TSK-0144; if none applies, skip with Not covered/none-applicable truth. |
| External-service completion confirmation | **Conditional** | Needed only where the parent completes an applicable service step and no verifier exists. | B3 | One confirmation, S2 only. |
| Protection Map review | **Retain outcome; remove extra acknowledgement** | Truthful evidence/gaps must be visible, but the user need not click “I understand” absent an owning requirement. | System/output | Render directly; no mandatory checkbox/confirmation merely for telemetry. |
| Finish button | **Remove from mandatory budget by default** | If final map is rendered and any J1 deletion/completion event can execute safely, another click adds no decision/evidence. | Zero | Treat final-map render/current journey completion as completion unless later technical/legal evidence requires an explicit Finish action. |
| Contextual Help | **Retain on demand** | Needed for failures/uncertainty, not mandatory happy-path progression. | B5 | Help is adjacent to the failing step; no generic forced help tour. |
| Retry verification | **Conditional** | Useful only after a potentially recoverable failure/change. | B5 | Do not loop equivalent failures; each retry needs a changed condition/new evidence. |
| Reset journey | **Conditional** | Needed for wrong routing/state; distinct from device protection removal. | B5 | One reset action with consequence explained; no routine confirmation unless state loss is material. |
| Remove UseSafeWeb DNS | **Retain on demand** | Reversibility is a core safety/recovery requirement. | B5/B2 | Platform-specific removal; protection claim ends. |
| Post-removal connectivity check | **Automate where possible; no mandatory browsing task** | Confirms recovery without asking for browsing history. | System/B5 | Use synthetic/neutral connectivity check; ask only if automation cannot conclude. |
| Exit | **No extra interaction required** | User can leave at any time. | Zero | Session/J1 cleanup follows TSK-0229; do not trap user behind completion. |

## 5. Resulting minimum provisional happy path

This is a **logical action path**, not a promised click count:

1. Parent sees the concise public proposition/limits and selects **Start**.
2. System selects locale by safe default; parent changes it only if desired.
3. System routes device family automatically where reliable; parent confirms/selects only if ambiguous.
4. Native safeguard action appears only if applicable; parent performs it and confirms only if no verifier exists.
5. System routes directly to the one approved DNS mechanism for that exact supported platform.
6. Parent performs the OS-required DNS action.
7. UseSafeWeb verifies automatically where possible; otherwise parent explicitly triggers one Check/Recheck.
8. One external-service step appears only when TSK-0144 says an approved relevant safeguard applies.
9. Protection Map renders immediately with TSK-0320 evidence states and gaps.
10. Journey completion/deletion occurs without a mandatory extra Finish click unless a later technical/legal requirement proves one necessary.

Unsupported or uncertain branches exit this happy path early into truthful S4/S5 plus recovery/help; they are not forced through fake completion.

## 6. Platform constraints — friction that cannot currently be promised away

### Android

Current accepted native DNS path is Android Private DNS provider hostname `dns.usesafeweb.com` using DoT. The product may reduce explanation/copying effort but **must not claim that a web page can silently or universally switch the Android system Private DNS setting**. Manufacturer/version navigation may vary; TSK-0409 will freeze supported combinations/limits.

### Apple

Current accepted iPhone/iPad path uses the UseSafeWeb DoH profile/Server URL. OS/profile installation and authorization are security-sensitive platform actions. The product may prepare the correct profile and clear instructions, but **must not claim silent one-click installation** or treat profile presence as verified protection. The later release `.mobileconfig` still requires direct artifact/current-OS verification.

### VPN / browser / app / network conflicts

No interaction-budget optimization may hide a conflict that can invalidate verification. If current detection cannot establish the intended resolver path, TSK-0320 S5 `Status uncertain` is required. TSK-0409 owns the matrix; this task does not fabricate a universal bypass detector.

## 7. One-click claim policy

Allowed wording is outcome-specific, for example:

- `Start setup`
- `Copy DNS hostname`
- `Install profile` only when the exact profile workflow is currently supported and still requires the platform's own authorization steps
- `Check protection`
- `Remove UseSafeWeb DNS`

Prohibited unsupported wording includes:

- `Protect this phone in one click`
- `Turn on UseSafeWeb automatically` when the OS still requires settings/profile action
- `Works on every Android/iPhone`
- `One setting protects every app/network`
- `Install and forget` when bypass/reverification limits remain
- `Fully protected`

A CTA may be one click; the underlying platform operation must not be falsely described as one-click if it is not.

## 8. Field/data friction rules

The TSK-0229 allowlist is an **upper bound**, not a form specification. A field is displayed only if current routing/technical behavior needs it.

- Never collect identity/contact to reduce technical friction.
- Never add exact DOB/child age, school/location, service usernames, device serial/fingerprint, browsing history or raw diagnostics.
- Prefer derived/transient facts only when derivation is reliable and does not create a persistent fingerprint/profile.
- If a field becomes unnecessary after TSK-0143/0409 routing work, delete it from the UI even if the data contract technically allows it.
- Do not retain a field “for future analytics.”

## 9. Confirmation friction rules

A confirmation is permitted only if it changes truth/state or protects against a material consequence.

**Retain:**

- parent confirmation where no system verifier exists;
- explicit remove/reset where the user is intentionally undoing protection and the consequence must be clear;
- exceptional destructive/data/security actions owned by later authority.

**Remove:**

- “Are you sure?” for ordinary reversible navigation;
- “I understand” after every instruction;
- repeated “Done?” after a verifier can determine the result;
- acknowledgement used only to improve funnel metrics.

## 10. Acceptance assertions

A later prototype/implementation audit must be able to show:

1. every mandatory interaction maps to B1–B5 and a documented current reason;
2. any interaction with no current reason is absent from the default path;
3. account/login/contact/payment are absent before core value;
4. locale selection is not forced when a safe supported default is available;
5. OS/version/phone-state questions appear only when they change routing;
6. no user chooses DoH versus DoT as a protocol decision when platform routing already determines it;
7. Android/Apple platform-required actions remain explicit and are not marketed as universal one-click setup;
8. parent confirmation is requested only when it changes evidence state and never yields Verified;
9. DNS verification runs automatically where feasible or requires at most one deliberate Check/Recheck action per changed condition;
10. external-service friction is absent when no approved relevant safeguard applies;
11. Protection Map has no mandatory acknowledgement checkbox;
12. Finish/Exit does not require an extra click unless a later owning requirement proves necessity;
13. help/retry/reset/removal stay off the normal happy path until invoked/needed;
14. retries do not loop without a changed condition/new evidence;
15. no field is retained for hypothetical future analytics;
16. unsupported/uncertain paths stop optimistic progression rather than adding steps to manufacture success.

## 11. Owner/governance boundaries

This friction budget may remove unnecessary UX interactions, but it cannot remove or bypass:

- OS security/authorization steps;
- truthful Not covered/uncertain/protection-limit disclosure;
- parent-versus-system evidence distinction;
- required legal/safeguarding action owned elsewhere;
- privacy deletion/retention controls;
- owner approvals/gates;
- real-participant validation when reactivated;
- production release/launch authority.

## 12. ACC-0316 result

ACC-0316 requires each retained interaction to have a decision/technical/safety reason, removable steps to be removed, platform constraints to be explicit, and unsupported one-click claims to be absent.

This contract supplies a purpose-based friction budget, zero-budget removals, five allowed budget classes, an interaction-by-interaction challenge, a minimized provisional happy path, explicit Android/Apple constraints, one-click claim rules, field/confirmation rules and sixteen testable assertions. It removes the forced trust screen, forced locale choice, unconditional OS/version/phone-state questions, generic protocol choice, mandatory external-service step, Protection Map acknowledgement and mandatory Finish click unless later evidence proves necessity.

**TSK-0316 result: PASS candidate subject to independent verification and runtime read-back.**
