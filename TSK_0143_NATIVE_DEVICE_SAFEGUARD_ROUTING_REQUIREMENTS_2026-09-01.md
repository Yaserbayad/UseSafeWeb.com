# TSK-0143 — Native-Device Safeguard Routing Requirements

**Task:** TSK-0143 — Specify native-device safeguard routing requirements  
**Acceptance:** ACC-0143 / VER-0143 / EVD-0143  
**Lifecycle:** L4 — Requirements Definition → Requirements Freeze  
**Version:** 1.0.0  
**Date:** 2026-09-01  
**Authority:** A3 / AUTO_ALLOWED under the current CR-0008 owner-frozen modular Master Planning System  
**Hard dependency:** current `TSK-0146` PASS  
**Controls:** REQ-0007; REQ-0008; CON-0001; CON-0002; RSK-0002; INT-0003; INT-0004  
**Status:** requirements-freeze candidate only; implementation, device verification, behavioral validation, LG-07, production activation and real-user outcomes are not inferred.

## 1. Product boundary

UseSafeWeb remains **First Phone Safety Setup** for the first independently used smartphone life stage. The core journey remains **Phone -> Internet -> Services -> truthful Protection Map**. Native-device safeguards are routed as part of the Phone layer where they provide relevant first-party/device safety value; they do not replace the Internet/DNS layer or external-service guidance.

AdGuard remains infrastructure behind the product, not the customer proposition. This task does not change the frozen AdGuard backend, DNS mechanisms, filtering policy, optional-account boundary, or accountless core journey.

## 2. Routing principle

For each native safeguard presented by the product, the router must determine exactly one current requirement state from evidence available for that safeguard and supported platform/version:

1. `supported_action_needed` — the safeguard is applicable and supported, and the product has current guidance for enabling/configuring it.
2. `supported_already_configured` — the parent/device indicates the safeguard is already configured; whether this state is technically verified or parent-confirmed is recorded separately.
3. `supported_parent_confirmation_required` — the platform does not provide a safe/available technical verification mechanism for this safeguard, so a parent may confirm completion; this is confirmation evidence only.
4. `supported_verified` — a current task-approved technical verifier has actually established the safeguard state for the relevant scope. This state is allowed only where such a verifier exists and has fresh qualifying evidence.
5. `unsupported` — the platform/version/path is known not to have an approved UseSafeWeb route for this safeguard.
6. `guidance_stale_or_uncertain` — support may exist, but the current guidance/version/evidence is stale, contradictory, unknown, or insufficient to safely direct the parent.
7. `not_applicable` — the safeguard does not apply to the current platform/device/context under the approved requirement catalogue.
8. `removed_or_disabled` — current evidence establishes that a previously configured safeguard has been removed/disabled for the relevant scope.

These are routing-requirement states, not replacements for the six TSK-0320 Protection Map states. The product maps them into the current Protection Map truth model without creating a seventh protection state.

## 3. Supported-platform requirements

For every native safeguard, the versioned guidance catalogue must contain:

- `safeguard_id` — stable product identifier;
- `platform_family` — bounded approved family such as Android or iOS/iPadOS;
- supported OS/version range or explicit version rule;
- applicability conditions;
- current navigation/instruction steps or a current official-source locator;
- `guidance_version` and `reviewed_at` date;
- content owner and next review trigger;
- whether an approved technical verifier exists;
- verifier ID/version and freshness rule if one exists;
- parent-confirmation allowance if technical verification is unavailable;
- unsupported/not-applicable reasons;
- removal/disable/recovery guidance where applicable;
- privacy/data requirements for any evidence collected;
- known conflicts/limitations and the required Protection Map outcome.

A platform/version combination is **supported** only when all required catalogue fields are current enough to route safely. Generic similarity to another OS version is not support evidence.

## 4. Already-configured handling

When the parent says or the device UI indicates that a safeguard is already configured:

1. Do not force the parent through redundant setup steps.
2. If a current approved technical verifier exists, offer/run verification according to that verifier's authority and privacy rules.
3. If verification succeeds, the corresponding layer may map to `protected_verified` only to the scope actually proven.
4. If no technical verifier exists, record only parent/configuration confirmation and map at most to `configured_parent_confirmed` in the TSK-0320 truth model.
5. If the parent/configuration evidence conflicts with current technical evidence, current qualifying technical evidence wins.
6. If evidence is stale, indeterminate or contradictory, route to clarification/recheck and map to `uncertain_error` rather than preserving an optimistic state.
7. Already-configured handling must never create a duplicate persistent child/device profile or browsing-history record.

## 5. Parent-confirmation rules

Parent confirmation is permitted only where the requirement explicitly says technical verification is unavailable, disproportionate, unsafe or not yet implemented for that safeguard.

Parent confirmation must:

- be explicit and tied to one safeguard/context;
- use truthful copy such as **“You confirmed this setting is on”**, not **“We verified this protection”**;
- never be described as system verification;
- never create `protected_verified` by itself;
- remain distinguishable from technical verifier evidence in storage, UI state and telemetry;
- be replaceable by later technical evidence without preserving a contradictory optimistic state;
- expire/recheck when the platform/version/guidance or relevant configuration materially changes;
- not require account creation for core journey value.

Account ownership, device registration, ClientID presence, profile existence, journey completion and dashboard state are not substitutes for technical verification or parent confirmation of the native safeguard itself.

## 6. Unsupported and not-applicable paths

The router must never invent a route for an unrecognized or unsupported platform/version.

### Known unsupported

Show:
- the safeguard is **Not covered on this device/path**;
- a concise reason category;
- any safe official/native alternative already approved by the content catalogue;
- the next action, if one exists;
- no complete-safety implication.

Map the relevant Protection Map layer to `not_covered` unless another independent mechanism for that same layer has qualifying evidence.

### Not applicable

Do not present an unnecessary setup task. Mark it as not applicable in the routing model and keep it out of completion denominators that assume applicability.

### Unknown/uncertain

If the OS/version or instruction validity cannot be determined, do not guess. Route to `guidance_stale_or_uncertain`, show that the guidance needs review/recheck, and map the affected Protection Map layer to `uncertain_error` until current evidence resolves it.

## 7. Stale-guidance and change-control requirements

Guidance becomes stale when any of the following occurs:

- the current OS/version falls outside the reviewed range;
- the vendor materially changes navigation, feature name, eligibility, default behavior or verification behavior;
- the content review deadline/trigger is reached without current review;
- a device/browser/network test contradicts the documented route;
- support evidence is missing for a newly observed platform/version;
- a safety/privacy/security issue makes the current instructions questionable;
- material user/operational evidence later shows the route is wrong or misleading.

When stale:

1. suppress step-by-step instructions that may cause incorrect configuration;
2. preserve only safe, truthful limitation copy;
3. mark the route `guidance_stale_or_uncertain`;
4. require content-owner review against current authoritative platform sources before restoring supported status;
5. invalidate prior guidance-version acceptance for the affected platform/version, without globally invalidating unrelated safeguards;
6. keep any still-valid observed/technical state evidence distinct from the stale instruction itself.

No stale route may silently inherit support merely because a prior version passed.

## 8. Verification limitations and truth-state mapping

The router must separate three evidence classes:

| Evidence class | Example | Maximum truth claim |
|---|---|---|
| Technical verification | approved current verifier observes the relevant effective state | `protected_verified` for the proven scope only |
| Configuration evidence | setting/profile exists or device UI shows configured | `configured_parent_confirmed` unless independently technically verified |
| Parent confirmation | parent explicitly reports/acknowledges completion | `configured_parent_confirmed` only |

Limitations:

- absence of a verifier is not evidence of failure or success;
- inability to inspect a setting must not be called verified;
- parent confirmation must never masquerade as system verification;
- technical verification for one safeguard/layer does not verify another;
- account/device ownership does not verify a native safeguard;
- historical evidence becomes stale after a material relevant configuration/platform change;
- unsupported paths map truthfully to `not_covered` rather than forcing completion;
- verifier failure/indeterminate result maps to `action_needed` or `uncertain_error` according to the current reason/repair contract, never automatically to protected;
- removal/disablement requires evidence appropriate to the relevant safeguard/scope; account deletion alone is not safeguard removal evidence.

## 9. Journey routing contract

For each applicable native safeguard, the customer journey follows:

`detect platform/version/context -> resolve catalogue support -> inspect available current evidence -> choose supported/already-configured/confirmation/unsupported/stale/not-applicable route -> show bounded action/copy -> capture only approved minimum evidence -> compute truthful Protection Map state -> expose recovery/removal/next action`

Mandatory routing behavior:

- accountless users receive the complete core routing experience;
- optional sign-in may persist only the separately approved parent/device state and must not be required to obtain core native-safeguard guidance;
- unsupported/stale routes do not block completion of unrelated independent safeguards;
- one safeguard's completion cannot automatically mark another safeguard complete;
- the Protection Map is the final truth surface and must show evidence quality/limitations in parent-readable language;
- no route introduces child accounts, browsing/query/activity history, unrestricted DNS administration or surveillance behavior.

## 10. Copy requirements

Approved copy patterns:

| Situation | Required semantic copy |
|---|---|
| Supported + action needed | “Turn on [safeguard]” + current bounded steps + why it matters + how to come back/check |
| Already configured, technically verified | “Checked: this setting is on” + verification scope/date/freshness semantics where useful |
| Already configured, parent-confirmed only | “You confirmed this setting is on” + “UseSafeWeb has not technically verified it” |
| Technical check unavailable | “We can guide you, but we cannot automatically verify this setting on this device” |
| Unsupported | “Not covered on this device/path” + concise limitation/alternative |
| Stale/uncertain guidance | “We need to recheck the current steps for this device/version before guiding you” |
| Verification error | “We could not verify this right now” + safe retry/recovery action; never imply protected |
| Removed/disabled | “This safeguard is off/removed for this scope” only when supported by current evidence |

Copy must not claim “fully safe,” “complete protection,” surveillance, emergency protection or technical verification that the evidence cannot support.

## 11. Testable examples

1. **Supported, not configured:** supported iOS/Android route + current guidance + no completion evidence -> route `supported_action_needed`; Protection Map `action_needed`.
2. **Parent says already on, no verifier:** route `supported_parent_confirmation_required` or `supported_already_configured`; record parent confirmation; Protection Map `configured_parent_confirmed`, never `protected_verified`.
3. **Technical verifier positive:** route `supported_verified`; Protection Map `protected_verified` only for the verified safeguard/scope.
4. **Configuration says on, verifier negative:** technical evidence overrides confirmation -> `action_needed` or `uncertain_error`; show recheck/recovery.
5. **Known unsupported OS/version:** route `unsupported`; Protection Map `not_covered`; no fabricated steps.
6. **New OS version with stale instructions:** route `guidance_stale_or_uncertain`; suppress potentially wrong steps; Protection Map `uncertain_error` until reviewed.
7. **Safeguard not applicable:** route `not_applicable`; no unnecessary setup requirement; independent layers unaffected.
8. **Previously configured but removed:** current removal evidence -> `removed_or_disabled`; map the affected layer consistently with TSK-0320; account/device deletion alone is insufficient.
9. **Sign-in occurs after accountless setup:** sign-in may not upgrade parent-confirmed evidence to technical verification or retroactively link anonymous history beyond approved contracts.
10. **Human validation later contradicts a route:** preserve the observation, reopen affected requirement/content evidence, correct and retest; synthetic/internal evidence is never relabelled human validation.

## 12. RSK-0002 / research-evidence boundary

This requirements task is based on current frozen owner/product requirements, canonical technical/experience contracts and internal verification logic. Under RSK-0002 and DEC-0052/CR-0005, no real-parent behavioral, usability or comprehension result is claimed here.

Future L8/live-production human evidence may show that a supported route is confusing, redundant, low-value or burdensome. Such evidence must be recorded separately through INT-0004, with observed evidence distinguished from inference and with contrary findings allowed to reopen the affected route. Until then, internal/synthetic review proves only that these requirements are complete, coherent and testable.

## 13. Deterministic ACC-0143 assertions

TSK-0143 may be accepted only if:

1. exact current WBS metadata, TSK-0146 dependency, A3/AUTO_ALLOWED authority, ACC-0143/VER-0143/EVD-0143 and referenced controls are current;
2. supported platform/version states and the catalogue fields required to call a route supported are explicit;
3. already-configured handling distinguishes technical verification from configuration/parent confirmation;
4. parent confirmation is explicitly permitted/limited and never creates `protected_verified`;
5. unsupported, not-applicable and unknown/stale paths have explicit behavior and truthful Protection Map outcomes;
6. stale-guidance triggers, suppression, review and scope-limited invalidation rules are explicit;
7. technical-verification limitations, freshness, precedence, errors, removal and independent-layer scope are explicit;
8. accountless core value remains available without sign-in and optional account/device ownership cannot substitute for verification;
9. no browsing/query/activity history, child account, surveillance behavior or unrestricted DNS administration is introduced;
10. RSK-0002 is preserved: no internal/synthetic requirement review is called human behavioral/user validation;
11. downstream implementation/device/runtime/LG-07/production/real-user PASS is not inferred;
12. full modular Master Plan validation remains PASS and the CR-0008 owner-frozen planning baseline is unchanged.

**TSK-0143 result:** PASS candidate pending deterministic reviewer verification, full modular-plan validation, GitHub read-back and durable `CURRENT_STATE.md` reconciliation.