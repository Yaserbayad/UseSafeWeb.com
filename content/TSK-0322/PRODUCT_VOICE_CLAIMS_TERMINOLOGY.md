# TSK-0322 — Product Voice, Claims, and Terminology Guide

**Version:** 2.0.0-post-cr0007
**Status:** internal L4 product-content contract  
**Owner:** Content  
**Action authority:** A4 / AUTO_ALLOWED
**Current sequencing:** DEC-0053 / CR-0006 + DEC-0054 / CR-0007; DEC-0052 / CR-0005 remains the pre-L8 no-human-evidence rule
**Publication authority:** none

## 1. Purpose

This guide is the current product-facing language contract for SafeWeb public, setup, help, status/Protection Map, recovery/removal, and downstream implementation surfaces.

It consolidates the accepted verbal-system intent from TSK-0299, the protection-state semantics owned by TSK-0320, the visible-identity rule owned by TSK-0297/TSK-0301, and the current dual-mode Version-1 product/experience baseline proven through TSK-0146 and the corrected integrated TSK-0333 prototype.

Where an older accepted artifact still uses stale pre-product sequencing language or uses `UseSafeWeb` as visible product identity, current authority applies:

- visible brand/product identity: **`SafeWeb`**;
- `UseSafeWeb.com`: domain/project/technical identifier, not the visible wordmark;
- product-facing DNS term: **`SafeWeb DNS`** unless the literal domain/endpoint `dns.usesafeweb.com` or `https://dns.usesafeweb.com/dns-query` is technically required;
- current Version 1 is dual-mode: the complete core setup/protection journey remains usable without login, while an optional parent account/session, minimum saved-device ownership persistence, lightweight dashboard/device management, and bounded account/device lifecycle flows are approved under DEC-0053/CR-0006;
- mandatory login for core value, browsing/query/activity history, child accounts/profiles, broad/raw DNS administration, automatic J0/J1-to-account linkage, and treating account/device/dashboard presence as technical verification remain prohibited;
- pre-product human/user validation is not claimed and is not required before L8 under DEC-0052/CR-0005.

This normalization does not change protection-state evidence strength or supported-platform behavior.

## 2. Voice

SafeWeb is:

1. **Calm** — state risk and limits without urgency theatre or fear.
2. **Clear** — use concrete ordinary language and one material idea at a time.
3. **Respectful** — never shame, scold, infantilize, or imply parental negligence.
4. **Protective, not controlling** — describe bounded safeguards, not surveillance or domination.
5. **Truthful** — match every protection statement to the evidence actually held.
6. **Practical** — show the next safe action or recovery path before unnecessary explanation.
7. **Quietly trustworthy** — earn trust through boundaries, privacy restraint, reversibility, and explicit uncertainty.

Clarity never outranks truth. Shorter copy is not acceptable if it hides a material limitation or strengthens an evidence claim.

## 3. Reading-level and child-readable goals

### Parent/caregiver reading goal

- plain general-audience language rather than technical/security jargon;
- one material idea per sentence where practical;
- short concrete action labels instead of generic `Continue` when the action can be named;
- explain the action before transport/protocol terminology;
- expose terms such as DoH, DoT, resolver, profile, provider hostname, certificate, or DNS only when required to configure, verify, troubleshoot, or explain a material limit;
- automated readability scores may be used as advisory checks, but there is **no authorized fixed grade-level number** and no readability score may justify weakening truth, safety, privacy, or limitations.

### Child-readable / child-visible principle

When copy could reasonably be seen by a child:

- use neutral, non-blaming language;
- do not imply the child is suspicious, dangerous, or being watched;
- do not use fear, shame, punishment, threat, or surveillance framing;
- describe settings and outcomes, not judgments about the child;
- avoid unnecessary personal details about the child;
- keep the same evidence strength and limitations as parent-facing copy.

SafeWeb is primarily parent/caregiver-facing; “child-readable” does not create a child account or child-facing product surface.

## 4. Canonical identity and descriptors

| Item | Current rule |
| --- | --- |
| Visible product/brand | `SafeWeb` |
| Domain/project identifier | `UseSafeWeb.com` |
| Parent-facing DNS service term | `SafeWeb DNS` |
| Android exact technical value | `dns.usesafeweb.com` |
| iPhone exact technical value | `https://dns.usesafeweb.com/dns-query` |
| Primary descriptive category | `First Phone Safety Setup` |
| Short descriptor | `A clear setup path for sensible first-phone safeguards.` |
| Preferred internal brand line | `Clear guardrails for safer first-phone independence.` |

`Safer` and `guardrails` are bounded comparative/design language, not a complete-safety guarantee.

Do not translate, mirror, reverse, or alter `SafeWeb` in Turkish or Arabic/RTL surfaces. Surrounding Arabic content may be RTL; `SafeWeb` remains Latin/LTR.

## 5. Canonical product terms

| Use | Meaning | Avoid/restrict |
| --- | --- | --- |
| `parent` / `caregiver` | Intended adult role. | `administrator`, `operator`, `monitor` in ordinary user copy. |
| `first phone` | First independently used smartphone context. | Do not imply a legally fixed age threshold. |
| `safeguard` | Bounded protective setting or control. | `guarantee`, `shield`, `total protection`. |
| `Phone` / `Internet` / `Service` | Three evidence layers. | Do not imply DNS configures native/service controls. |
| `SafeWeb DNS` | Parent-facing supported encrypted-DNS path. | Protocol jargon as the primary product proposition. |
| `Private DNS` | Android platform setting when applicable. | Universal iPhone term. |
| `DNS profile` | iPhone configuration-profile concept only when an approved exact path applies. | Silent installation or universal Apple support. |
| `check` | Parent-facing action to determine current state. | `scan` where it could imply browsing/content inspection. |
| `verify` / `Verified` | Reserved for qualifying current technical evidence. | Parent confirmation or configuration presence. |
| `Protection Map` | Evidence/coverage summary. | `safety score`, `protection score`, `all-clear`. |
| `remove` | Remove SafeWeb DNS/configuration. | `disable safety` or guilt framing. |
| `start over` | Reset transient web journey state. | Must not imply device DNS was removed. |
| `recovery` | Restore a supported working state or normal DNS after removal/failure. | Silent fallback while retaining a positive protection claim. |

## 6. Canonical protection-state labels

TSK-0320 remains semantic authority. These labels and evidence strengths must not be renamed or weakened:

| State | Primary label | Required meaning |
| --- | --- | --- |
| S1 | `Verified` | SafeWeb holds current qualifying technical evidence for the exact supported protection mechanism. |
| S2 | `You confirmed this is set up` | Parent confirmation exists; SafeWeb has not independently verified it. |
| S3 | `Action needed` | Applicable protection is incomplete/failed and a known next action exists. |
| S4 | `Not covered` | SafeWeb does not provide/support this capability on the current setup or no approved safeguard applies. |
| S5 | `Status uncertain` | Current evidence is conflicting, inconclusive, stale, bypass-prone, or unavailable. |
| S6 | `Removed` | The safeguard/SafeWeb configuration is intentionally no longer active. |

### Supporting copy defaults

- S1: `SafeWeb verified this protection step is active on your current setup.`
- S2: `SafeWeb has not independently verified this setting.`
- S3: `Finish this step before relying on this protection layer.`
- S4: `SafeWeb does not cover this on your current setup.`
- S5: `We can’t verify this protection right now. Check it before relying on this layer.`
- S6 DNS: `SafeWeb DNS is no longer active on this device.`

State truth rules:

- parent confirmation never produces `Verified`;
- configuration/profile presence alone never produces `Verified`;
- stale positive evidence must not survive a material contradiction/change;
- removal withdraws the active protection claim;
- journey completion does not imply all layers are protected;
- critical state meaning is textual/semantic, never color-only.

## 7. Completion and Protection Map language

Preferred completion pattern:

`Setup complete. Review what SafeWeb verified, what you confirmed, and what is not covered.`

The Protection Map displays each applicable layer independently and never collapses them into an overall safety score.

Do not use:

- `Your child is safe`;
- `Fully protected`;
- `Protection complete` when material action-needed/not-covered/uncertain/removed states exist;
- an all-green treatment that visually turns parent confirmation into technical verification.

## 8. Approved current claim library

These are approved only in contexts where their ordinary factual conditions remain true:

### Product purpose

- `SafeWeb helps you set up sensible first-phone safeguards.`
- `SafeWeb brings the phone, internet baseline, and one relevant service safeguard into one clear setup path.`
- `SafeWeb shows what it verified, what you confirmed, what needs attention, and what is not covered.`

### Accountless/privacy

- `You do not need a SafeWeb account for the core setup, verification, help, recovery, or removal journey.`
- `SafeWeb is designed to minimize identity and journey data.`
- `SafeWeb is not a child browsing or activity monitoring product.`

These do not authorize `zero data`, `collects nothing`, or `completely anonymous`.

### Optional account continuity

- `You can use SafeWeb without signing in; an optional parent account can provide continuity and a lightweight saved-device dashboard.`
- `A saved device or signed-in account does not by itself mean protection is Verified.`
- `Logging out changes account access only; it does not remove SafeWeb DNS from a device.`
- `Deleting a saved device record is different from removing SafeWeb DNS from the physical device.`

These claims authorize only the bounded current Version-1 account/dashboard scope. They do not authorize browsing/activity history, child profiles/accounts, broad DNS administration, automatic anonymous-to-account linkage, or a stronger protection claim.

### Control/recovery

- `You can remove the supported SafeWeb DNS configuration and follow recovery guidance.`
- `Starting over resets the web setup journey; it does not remove SafeWeb DNS from the phone.`

### Scope/limits

- `DNS filtering works at the domain-resolution layer. It does not inspect content inside an allowed app or site.`
- `Some VPN, Private Relay, custom DNS, browser/app DNS, managed-network, or unsupported-device conditions can make protection unavailable or uncertain.`

## 9. Conditional claims

Use only when the exact current condition is proven:

| Claim | Required condition |
| --- | --- |
| `Verified` / `SafeWeb verified this protection step is active` | Current qualifying technical evidence for the exact supported path. |
| `Encrypted DNS` | Exact supported Android/iPhone mechanism under current endpoint/support authority. |
| `SafeWeb DNS is active` | Current evidence supports active state; configuration presence alone is insufficient. |
| `This setting is set up` | Parent confirmation/current setup evidence supports S2 and no contradiction requires S5. |
| `Supported on this phone` | Exact device/OS/network combination is inside the current approved support matrix. |
| `Free core protection` | Current commercial baseline remains unchanged. |
| `Saved in your dashboard` | The parent is signed in, the device record is explicitly saved/owned, and the product does not present record presence as technical verification. |
| `Signed in` / `Session ended` | Current account/session state only; wording must not rewrite physical protection truth. |
| `Available in [market]` | Separate market/legal/publication authority exists; language availability alone is insufficient. |

If the condition is not demonstrable, downgrade to the truthful state or omit the claim. Do not preserve a positive impression with `probably`, `normally`, `should be`, or equivalent wording.

## 10. Prohibited claims and expressions

The following are prohibited unless later higher authority explicitly approves a narrower evidenced formulation:

- `Complete protection`, `100% safe online`, `fully protected`, `total internet safety`, `blocks everything harmful`;
- `Your child is safe` or `your child is protected` as an overall outcome claim;
- `See everything your child does`, `monitor browsing`, `track your child`, `read messages`, `full parental control`;
- `Verified`/`Protected` derived only from parent confirmation, setting/profile presence, old evidence, or synthetic rehearsal;
- `Impossible to bypass`, `always protected`, `cannot be removed`;
- `We collect nothing`, `zero data`, `completely anonymous` without separately proven exact scope;
- `Legally approved`, `fully compliant`, `GDPR certified`, `certified safe`;
- `Parents love it`, `proven easy`, `validated with families`, `parents understand it` before actual authorized evidence exists;
- `The safest`, `the only`, `best parental protection`, `unique` without current comparative evidence;
- fear/shame language such as `Your child is in danger unless…` or `Responsible parents must…`;
- `Launch-ready`, `available everywhere`, `works on every device/network`, `fully supported` without exact current authority;
- `24/7 support team`, `a specialist is always available` without an authorized staffed service;
- `Premium protection`, `pay for better safety`, `guaranteed value` under the current free-core/payment-gated baseline;
- shield/padlock/certification language or iconography used to imply guaranteed/certified safety;
- wording that makes login/account creation mandatory for core setup, verification, help, recovery, or removal;
- wording that implies browsing/query/activity history, child accounts/profiles, or broad/raw DNS administration exists in the current product;
- wording that treats sign-in, account ownership, saved-device presence, or dashboard presence as technical `Verified`;
- wording that implies automatic J0/J1 import, promotion, linkage, or expiry extension from sign-in/account activity;
- wording that conflates logout, account deletion, saved-record deletion, revoke/unlink, anonymous-state deletion, and physical SafeWeb DNS removal;
- wording that reports an unknown destructive-operation result as success or encourages automatic destructive replay.

## 11. CTA language

Name the exact next action where possible.

Preferred examples:

- `Start setup`
- `See how it works`
- `Check compatibility`
- `Read privacy details`
- `Get help`
- `Check again`
- `Remove SafeWeb DNS`
- `Start over`
- `Review Protection Map`

Avoid generic `Continue` when the exact destination/action can be named. Do not use urgency or guilt as conversion pressure.

## 12. Error, uncertainty, and troubleshooting grammar

1. State what is known.
2. State what is not known/covered when material.
3. Give one safe next action when one exists.
4. Retry only after the relevant condition changed.
5. Do not show success styling/copy while the evidence state is uncertain.
6. Do not expose technical diagnosis before it is useful to the user.
7. Do not imply routine staffed support where the operating model is self-service.

Examples:

- `Status uncertain — we can’t verify this protection right now.`
- `Turn off the conflicting custom DNS, then check again.` only when that exact correction is supported for the detected condition.
- `Not covered — SafeWeb does not cover this on your current setup.`

## 13. Localization / RTL language parity

- English is the source semantic baseline.
- Turkish and Arabic translations must preserve evidence strength, limitation, and action meaning; translation must never strengthen a claim.
- `SafeWeb` remains untranslated Latin/LTR.
- Arabic surrounding UI may use RTL layout.
- Language availability alone does not imply official market/legal/support availability.
- Technical endpoint/domain strings remain exact and LTR.

## 14. Review ownership

| Change | Required owner/reviewer |
| --- | --- |
| Product voice, ordinary terminology, CTA pattern | Content (TSK-0322 owner) |
| Protection-state label/evidence strength | TSK-0320 semantic owner; do not alter locally |
| Visible brand/name/identity | Brand/identity authority (TSK-0297/0301) |
| Shared token/component visual behavior | TSK-0300 / downstream design-system authority |
| Platform-specific instruction/support claim | Owning instruction/support-matrix task/source |
| Data/privacy claim | Privacy/data owner and current evidence |
| Legal/compliance/market claim | Applicable legal/market authority; never infer from this guide |
| Ordinary optional-account/dashboard copy inside the frozen DEC-0053 Version-1 scope | Content (TSK-0322 owner), preserving product/privacy/truth authorities |
| New or materially broader product capability/account/dashboard claim | Project Owner / product-scope authority |
| Public-release claim | Applicable publication/release gate |

Any request that requires changing an upstream semantic authority must be routed to that owner rather than silently overridden here.

## 15. QA assertions

A downstream implementation/content QA suite must be able to assert:

1. visible identity is `SafeWeb` and never silently becomes a different wordmark;
2. parent confirmation never renders the label `Verified`;
3. S1–S6 labels are exact and preserve TSK-0320 evidence semantics;
4. no complete-safety, surveillance, certification, superiority, universal-support, or fabricated-validation claim appears;
5. completion copy does not convert journey completion into overall protection;
6. unsupported branches say `Not covered` and do not invent setup steps;
7. uncertainty is explicit and not styled/copy-framed as success;
8. removal withdraws the SafeWeb DNS active/protection claim;
9. translated copy preserves the same evidence strength;
10. optional account/dashboard copy never implies mandatory login for core value, browsing/query/activity surveillance, child accounts/profiles, broad/raw DNS administration, automatic J0/J1 linkage, or technical verification from account/device/dashboard presence;
11. no language capability implies market/legal/publication authorization;
12. technical endpoint strings remain exact;
13. logout, account deletion, saved-record deletion, revoke/unlink, anonymous-state deletion, and physical SafeWeb DNS removal remain distinct in user-facing language;
14. unknown destructive results remain explicitly uncertain and never imply automatic replay or success.

## 16. Non-inference fence

This guide is an internal L4 content contract. It proves language/claims/terminology consistency against current accepted sources. It does not prove real-user comprehension, native-speaker acceptance, legal completion, public-release readiness, production readiness, payment/market activation, or launch readiness.
