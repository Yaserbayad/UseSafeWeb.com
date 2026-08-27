# UseSafeWeb — Protection Claims Checklist

**Task:** TSK-0225  
**Gate:** LG-03 Validation Readiness  
**Status:** operational checklist  
**Reviewed:** 2026-08-27

## Purpose

Prevent the setup journey, support responses, Protection Map, and later product UI from overstating what UseSafeWeb can verify or protect. This checklist implements the frozen non-surveillance and truthful-coverage baseline. It does not itself prove that any device is protected; each live claim still requires the relevant technical or parent-confirmation evidence.

## Required state labels

Every material safeguard shown to a parent must use one of these meanings without blending them:

- **Protected — verified:** UseSafeWeb has current direct technical evidence that the protection is active for the stated scope.
- **Configured — parent confirmed:** the parent reports that a native or service safeguard is configured, but UseSafeWeb has not technically verified it.
- **Action needed:** a relevant safeguard is not yet completed or its state cannot currently be established.
- **Not covered:** UseSafeWeb cannot provide or verify the protection for that surface or condition.

Parent confirmation must never be promoted to technical verification.

## Pre-release / pre-session checklist

| Check | PASS condition | Fail-safe disposition |
|---|---|---|
| Truth label | Each safeguard uses exactly one state label whose evidence matches the definition above. | Downgrade to `Action needed` or `Not covered`; do not infer verification. |
| DNS scope | Copy explains that DNS filtering works at domain-resolution level and does not inspect content inside an allowed app/site or guarantee complete online safety. | Remove/qualify the claim before use. |
| Native/app controls | Apple/Google/app/service controls are described as separate layers; DNS activation is not represented as configuring those controls. | Mark the separate control `Action needed` or `Configured — parent confirmed` as appropriate. |
| VPN / alternate secure DNS | If a VPN, alternate encrypted-DNS path, or similar network feature can make the UseSafeWeb DNS path uncertain or bypassed, no `Protected — verified` claim is shown until current behavior is directly tested. | Show `Action needed`/`Not covered`; provide recovery guidance rather than claiming protection. |
| Private Relay / platform privacy routing | Where a platform privacy-routing feature may change DNS/network behavior, the current platform/device path is tested before claiming verified coverage. | Show the limitation explicitly; never assume coverage from configuration alone. |
| Captive portal / network change | Verification is repeated after a network/path change when that change can affect DNS routing. | Mark protection unverified until the external verification succeeds. |
| In-app harmful content | Copy states that DNS cannot reliably block harmful material delivered from an otherwise allowed domain/app/service. | Use `Not covered` for that content scope; point to relevant native/service controls where available. |
| False positive / exception | An exception is narrow, explainable, reversible, and tested; it does not silently disable the whole filtering baseline. | Do not release the exception; use support/recovery flow. |
| Removal | The parent has a clear method to remove the UseSafeWeb DNS configuration and restore the device's normal DNS behavior. | Do not activate until removal/recovery instructions exist for the supported path. |
| Recovery | The user can recover from a broken/unsupported configuration without requiring browsing-history collection. | Mark the path unsupported until recovery is defined. |
| Unsupported state | Any platform/version/network combination without a tested current path is explicitly unsupported or `Not covered`. | No optimistic claim. |
| Complete-safety wording | No wording implies total protection, surveillance, emergency response, or replacement of parental/native/service safeguards. | Block the claim/content until corrected. |
| Evidence freshness | `Protected — verified` is based on current relevant evidence, not historical setup success. | Re-verify or downgrade the state. |

## Verification rules

1. A successful DNS test proves only the tested DNS behavior, not native controls, in-app content safety, or complete device safety.
2. A configured profile or setting is not proof that traffic still follows the expected path; where the claim is material, verify the effective path.
3. A parent statement may support `Configured — parent confirmed` but never `Protected — verified`.
4. If VPN, Private Relay, alternate secure DNS, captive portal behavior, OS/vendor changes, or another network condition makes the state ambiguous, ambiguity is shown to the parent rather than hidden.
5. An exception/removal workflow must be reversible and must state what protection is lost.
6. UseSafeWeb must not require child browsing/domain history to prove these claims.

## Evidence record for a claim review

Record only:

- review date;
- affected platform/path/version where relevant;
- claim or label reviewed;
- evidence type (`technical verification`, `parent confirmation`, `not covered`, or `action needed`);
- reviewer;
- pass/fail and correction;
- link/reference to non-sensitive evidence.

Do not store credentials, private keys, raw child DNS history, or unnecessary personal data in the review record.

## Canonical baseline used

- `VALIDATION_READINESS_GATE.md` — privacy target, protection-label distinctions, DNS limitations and easy-removal requirement.
- `PILOT_PRIVACY_NOTICE.md` — parent/child protection limitations and Protection Map labels.
- `EXPERIMENT_01_CONCIERGE_VALIDATION.md` — Protection Map and facilitation rules.
- Frozen WBS ACC-0225 and constraints REQ-0018 / REQ-0019 / CON-0007 / CON-0008.

## Acceptance result

This checklist explicitly tests the four truth states, DNS limitations, app/service limitations, VPN/alternate-DNS/Private-Relay uncertainty, removal, recovery and exception handling. A failed check blocks or downgrades the corresponding protection claim rather than being waived silently.
