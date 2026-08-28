# TSK-0144 — One Relevant External-Service Safeguard Requirements

**Task:** TSK-0144 — Specify the one relevant external-service safeguard step  
**Acceptance:** ACC-0144  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** INTERNAL PROVISIONAL L4 SERVICE-GUIDANCE CONTRACT / IMPLEMENTATION OR PUBLIC RELEASE NOT AUTHORIZED  
**Date:** 2026-08-28  
**Authority:** DEC-0009 one-relevant-service baseline + BUSINESS_EVALUATION service-agnostic rule + TSK-0141 MIN-08 + TSK-0138 UPA-004 + TSK-0315 service blueprint + TSK-0316 friction budget + TSK-0320 truth-state contract + DEC-0050/CR-0003  
**Verification state:** PASS candidate pending independent verification and runtime reconciliation.

## Provisional evidence limitation — UPA-004 / RSK-0002 remain OPEN

The project has no representative-parent evidence showing which external service is most relevant, how often a service safeguard is missing, or whether this step creates incremental value. `UPA-004` and `RSK-0002` remain OPEN.

Accordingly, this contract freezes a **selection and truth framework**, not a universal service choice. No TikTok, WhatsApp, YouTube, Roblox, Instagram, Snapchat, gaming platform, messaging app or other service is preselected for every parent merely because it is popular or plausible.

This artifact does not make LG-05/LG-06 PASS and does not authorize implementation/build, real participants, legal completion, payment, public release or launch.

## 1. Frozen one-service rule

The external-service layer may contain **zero or one** guided service safeguard in a single first-phone journey.

- **Zero** is correct when no service is relevant, legally/age-appropriately available, currently supported, or safely guideable.
- **One** is the hard maximum in the active baseline.
- Two or more service setup branches are out of scope and require a later owner-approved product-scope change backed by evidence.

The product must never add a filler service solely so the Protection Map has three green layers.

## 2. Eligibility to show an external-service step

A service is eligible only when **all** applicable conditions are satisfied:

1. **Actual relevance:** the parent indicates that the child currently uses or is genuinely about to use the service within the first-phone setup context. Do not infer use from age, device, market popularity, advertising data or browser/app history.
2. **Age/legal availability:** current authoritative service terms/policy and applicable UK rules do not make the service plainly unavailable for the child's current category. If current law/policy is changing or exact applicability cannot be determined, use `Not covered`/uncertain rather than a workaround.
3. **Approved safeguard exists:** the current UseSafeWeb instruction catalogue contains exactly one approved, bounded safeguard for that service and state.
4. **Current source exists:** the instruction has a current official service/provider source, applicability, last-verified date and review trigger.
5. **Parent can perform it:** the parent has legitimate authority/access to the service/account setting. UseSafeWeb does not request or proxy the service credential.
6. **No material contradiction:** current guidance/device/service state does not contradict the approved instruction.
7. **No duplicate step:** the safeguard is not already correctly configured, or if it is, the parent-confirmed shortcut is used instead of repeating setup.

If any mandatory condition fails, the service step is skipped or shown as S4/S5 as appropriate.

## 3. Minimal relevance input

The product may ask only the smallest service-routing question necessary, for example a controlled selector such as:

- `Which one of these currently supported services will your child actually use?`
- approved supported service choices for the current catalogue;
- `None of these / not sure`.

Rules:

- no free-text app/account inventory by default;
- no request for usernames, handles, email, phone number or credentials;
- no inspection of installed apps, browsing history or DNS history merely to infer relevance;
- no multiple-service checklist that silently expands the one-service scope;
- if no supported choice is genuinely relevant, select no service and continue.

A remembered answer may be held only inside the currently approved accountless journey-state boundary; it must not become a persistent child interest/profile.

## 4. Service routing states

| Route state | Entry rule | Product action | Protection Map state |
| --- | --- | --- | --- |
| `SERVICE_RELEVANT_NEEDS_SETUP` | Parent identifies one supported relevant service and its approved safeguard is not configured. | Present exactly one current approved instruction. | S3 `Action needed` until completion/confirmation. |
| `SERVICE_ALREADY_CONFIGURED_CONFIRMED` | Parent says the approved safeguard is already correctly configured; no contrary evidence. | Skip duplicate setup; optionally show one current-source check link. | S2 `Set up — parent confirmed`. |
| `SERVICE_NOT_RELEVANT` | Parent selects none/not used/not planned. | Skip the service layer quietly; no replacement task. | S4 not-applicable / `Not covered` semantics as defined by TSK-0320. |
| `SERVICE_NOT_SUPPORTED` | Service is relevant but no current approved UseSafeWeb safeguard/instruction exists. | Explain that UseSafeWeb does not currently cover that service. | S4 `Not covered`. |
| `SERVICE_UNCERTAIN` | Service/version/account/region/policy state makes the approved instruction unreliable or applicability unclear. | Do not guess; point to current official service guidance where safe. | S5 `Status uncertain`. |
| `SERVICE_REMOVED_OR_DISABLED` | Parent reports the safeguard was later disabled/removed during the current journey. | Explain consequence and offer current-source reconfiguration if still applicable. | S6 `Removed`, or S3 once reconfiguration starts. |

## 5. How the single service is selected

Use this deterministic order:

1. Build the candidate set from **currently approved service instructions only**.
2. Remove services that are not currently available/applicable for the target branch according to authoritative current rules.
3. Ask the parent which **one** remaining service is actually used/planned, if any.
4. If exactly one is relevant, route to it.
5. If more than one is relevant, do **not** run multiple branches. Use the current product-owned priority rule only if one has been explicitly approved; otherwise present a neutral one-choice selector and state that UseSafeWeb currently guides one service only.
6. If none is relevant/supported, skip and mark Not covered/not applicable.

No hidden model ranking, popularity estimate, ad-tech inference, DNS history or behavioral profile may choose the service for the parent.

## 6. Supported versus unsupported service definition

A service is `SUPPORTED` for this layer only when the instruction catalogue records:

- exact service/provider name;
- exact safeguard outcome being guided;
- supported account/service/device/region state;
- official provider source URL/title;
- last verified date;
- instruction version;
- expected result;
- known limitations;
- parent-confirmation wording;
- fallback/unsupported state;
- content owner;
- review trigger/test reference.

A service is `NOT SUPPORTED` when any required current contract element is absent or stale enough that correctness cannot be established.

Technical existence of a parental/safety setting is not sufficient by itself; UseSafeWeb must have a current bounded instruction and truthful state rule before calling the service supported.

## 7. Parent confirmation and verification truth

For the current external-service layer:

- parent completion/confirmation → TSK-0320 S2 `Set up — parent confirmed`;
- UseSafeWeb does not currently have an approved technical verifier for third-party service-account settings;
- therefore S1 `Verified` is not available merely from a button click, account login, screenshot, installed app or parent assertion;
- UseSafeWeb must never request the service password/token merely to manufacture verification;
- if a future provider API/verifier is proposed, it requires separate privacy/security/authority acceptance before S1 can be used.

The service layer remains independent from UseSafeWeb DNS verification and native-control state.

## 8. Age/policy-change and 2027 UK transition rule

Canonical business authority already keeps the external-service step service-agnostic because UK under-16 social-media policy is changing.

The UK government's current July 2026 response, updated 19 August 2026, states that social media services are to be prohibited from offering their services to under-16s, with the first restrictions expected in **spring 2027**, while exact covered-service detail continues to be implemented through regulations.

Therefore:

1. UseSafeWeb must not freeze a named social-media service into the permanent minimum journey merely because it is currently common.
2. A service's eligibility must be rechecked against current law/regulation/provider age policy before instruction release or reuse.
3. When a service is no longer legally/age-appropriately available for the current child branch, UseSafeWeb does not provide circumvention instructions and does not substitute an account-age workaround.
4. A 2026 service instruction cannot be assumed valid in 2027 without review.
5. The product may legitimately have **no external-service step** for some/all under-16 social-media contexts after the new rules take effect.

Primary current government source:
- https://www.gov.uk/government/consultations/growing-up-in-the-online-world-a-national-consultation/outcome/growing-up-in-the-online-world-government-response-july-2026

## 9. Stale-guidance and content ownership

Every external-service instruction must have a named UseSafeWeb content owner and a deterministic review trigger.

Mandatory re-review triggers include:

- provider changes menu path, account model, age policy, parental/safety control or feature name;
- UK law/regulation changes service availability or relevant age/function rules;
- provider source is removed/redirected or materially contradicts the current instruction;
- exact service/version/region state differs from the approved applicability;
- current target evidence shows the instruction no longer works;
- a security/privacy/safeguarding concern changes the safe recommendation.

When stale:

- remove the service from the selectable supported set until reverified;
- use S4/S5 rather than stale instructions;
- preserve the last-verified record for audit, but do not present it as current guidance.

## 10. Fallback to `Not covered`

`Not covered` is a correct first-class result when:

- parent uses no service in the approved catalogue;
- the relevant service has no current approved safeguard;
- current age/policy state makes guidance inapplicable;
- service account/region/device state is unsupported;
- the instruction is stale and cannot be safely refreshed now;
- the parent does not have legitimate authority/access to change the setting.

The fallback copy must not imply failure by the parent and must not imply that DNS/native layers compensate for the missing service safeguard unless directly proven.

Example semantic form:

`Not covered — UseSafeWeb does not currently guide this service for your setup.`

Final wording remains subject to the product voice/content work; evidence strength cannot be increased in translation.

## 11. Privacy and security boundary

The service step must not collect or persist:

- service username/handle;
- password, token, session cookie, MFA code or recovery secret;
- child messages/posts/content;
- service activity/history;
- installed-app inventory beyond the parent's controlled routing selection;
- browsing/DNS history used to infer service use;
- a persistent interest/profile of the child.

The parent performs provider-account changes directly in the provider's own authenticated surface. UseSafeWeb supplies guidance only under the active minimum baseline.

## 12. Testable acceptance assertions

A later content/prototype/QA audit must prove:

1. no journey shows more than one external-service setup branch;
2. zero service branches is valid;
3. only services with current approved instruction records can be offered as supported;
4. the service is selected from parent-declared relevance, not inferred behavior/history/popularity;
5. already-configured service safeguard skips duplicate setup;
6. parent confirmation yields S2 and never S1;
7. irrelevant service yields a quiet skip/not-applicable outcome;
8. relevant but unsupported service yields S4 `Not covered`;
9. ambiguous/stale service state yields S5 rather than guessed instructions;
10. no credentials/tokens/MFA codes are collected;
11. no child messages/activity/history are collected;
12. service guidance is re-reviewed on provider age/control/menu or UK rule changes;
13. a stale instruction is removed from the supported selector until reverified;
14. a service that becomes unavailable for the child's category is not accompanied by circumvention guidance;
15. no default named service is hard-coded merely from assumed popularity;
16. adding a second service requires a later scope/owner decision rather than an implementation convenience change.

## 13. ACC-0144 result

ACC-0144 requires eligibility, supported/unsupported state, one-service limit, parent confirmation, content update ownership, and fallback to Not covered.

This contract defines each required class, keeps service selection deliberately service-agnostic and parent-declared, incorporates the current UK 2027 policy transition as a mandatory review trigger, and preserves UPA-004/RSK-0002 rather than treating a plausible service choice as validated demand.

**TSK-0144 result: PASS candidate subject to independent verification and runtime read-back.**
