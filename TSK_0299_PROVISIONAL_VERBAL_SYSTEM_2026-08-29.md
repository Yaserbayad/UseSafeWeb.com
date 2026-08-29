# TSK-0299 — Provisional Verbal System

**Task:** TSK-0299 — Define tone, voice, terminology, trust language, protection-state language, and communication examples  
**Acceptance:** ACC-0299  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Action authority:** A3 / AUTO_ALLOWED  
**Status:** PROVISIONAL INTERNAL L4 VERBAL-SYSTEM DESIGN / BEHAVIORALLY UNVALIDATED / PUBLICATION NOT AUTHORIZED  
**Date:** 2026-08-29  
**Authority:** DEC-0051 / CR-0004 + accepted TSK-0298 brand strategy + TSK-0320 protection-state/copy contract + TSK-0311 localization architecture + TSK-0307 instruction catalogue + TSK-0559 content-quality standard

## 1. Evidence and authority boundary

This artifact defines the reusable verbal system for the current accountless-first **UseSafeWeb First Phone Safety Setup** experience. It is an internal design contract, not representative-parent research, legal approval, publication approval, market activation, implementation authority, payment authority or launch authority.

`RSK-0002` remains OPEN. No representative-parent evidence proves that the wording is optimally understood, preferred, trusted, low-friction or low-support. `TSK-0187` remains the mandatory real-parent behavioral-validation gate, and `TSK-0309` still requires that evidence before real-evidence-based correction/freeze of the implementation-ready experience.

This verbal system must not imply LG-03/LG-04/LG-05/LG-06 PASS, legal completion, participant readiness, L5/L6 build authority, public publication, payment activation, market activation or launch readiness.

## 2. Verbal-system objective

UseSafeWeb language must help a parent/caregiver understand and act without requiring technical expertise, while preserving exact protection truth and limitations.

The verbal system therefore optimizes for:

1. **plain language before technical language**;
2. **one clear next action at a time**;
3. **calm, non-alarmist risk framing**;
4. **child-aware language without surveillance framing**;
5. **evidence-matched protection statements**;
6. **explicit uncertainty and not-covered states**;
7. **privacy-respecting, accountless-first trust language**;
8. **reusable semantic meaning across public, setup, help and localized surfaces**.

Clarity never overrides truth. A shorter sentence is not acceptable if it hides a material limitation or strengthens an evidence claim.

## 3. Canonical descriptors

### 3.1 Primary product descriptor

**First Phone Safety Setup**

Use this as the primary descriptive category for UseSafeWeb in parent-facing product/brand contexts where a category descriptor is needed.

### 3.2 Short explanatory descriptor

**A clear setup path for sensible first-phone safeguards.**

### 3.3 Expanded explanatory descriptor

**UseSafeWeb helps you put sensible first-phone safeguards in place across the phone, internet baseline and one relevant service — without turning the setup into a child-surveillance product.**

The expanded form is suitable only where the surrounding context also preserves the limits defined in this contract.

### 3.4 Internal brand idea / provisional tagline

**Clear guardrails for safer first-phone independence.**

This is the preferred provisional tagline/brand-line candidate inherited from TSK-0298. “Safer” is comparative to an intended safeguard outcome, not a guarantee of safety. “Guardrails” means bounded safeguards with visible limits, not monitoring or total control.

### 3.5 Supporting tagline candidates

These may be used in internal design exploration but do not outrank the primary brand idea:

- **Set up sensible safeguards. See what’s covered.**
- **A clearer start for a child’s first phone.**
- **Simple first-phone safeguards, with clear limits.**

Do not use a tagline that implies total protection, monitoring, guaranteed ease, parent validation, legal certification or universal device support.

## 4. Message hierarchy

The same hierarchy applies across public, setup and help surfaces. Individual surfaces may omit lower layers when not needed, but must not invert the hierarchy by leading with technical infrastructure or fear.

### Level 1 — Parent outcome

Explain the bounded parent job in ordinary language.

**Core message:**

> Put sensible first-phone safeguards in place through one clear setup path.

### Level 2 — What UseSafeWeb coordinates

Explain the three bounded layers without implying that DNS controls everything:

- **Phone** — relevant native safeguards first;
- **Internet** — the supported encrypted UseSafeWeb DNS baseline;
- **Service** — zero or one relevant external-service safeguard when applicable.

### Level 3 — Truth and evidence

Explain that UseSafeWeb distinguishes what it verified, what the parent confirmed, what needs action, what is not covered, what is uncertain and what was removed.

### Level 4 — Limits, privacy and control

Explain material limitations, accountless-first operation, non-surveillance posture, recovery/removal and unsupported conditions.

### Level 5 — Technical detail

Only expose terms such as DNS-over-TLS, DNS-over-HTTPS, profile, provider hostname, resolver or certificate when the parent needs them to complete, verify or troubleshoot a specific supported action.

Technical implementation is never the primary brand proposition.

## 5. Voice model

### 5.1 Calm

Use measured language. State risks and limitations without urgency theatre.

**Prefer:** `This setting is not covered on your current setup.`  
**Avoid:** `Your child could be at risk unless you fix this now.`

### 5.2 Clear

Use short, concrete sentences and explicit actions. One sentence should normally carry one material idea.

**Prefer:** `Open Private DNS and enter dns.usesafeweb.com.`  
**Avoid:** `Configure the encrypted resolver endpoint using the applicable secure DNS provider mechanism.`

### 5.3 Respectful

Treat the parent as capable. Do not shame, scold or imply negligence.

**Prefer:** `You can skip this if it is already set up.`  
**Avoid:** `Responsible parents should already have enabled this.`

### 5.4 Protective, not controlling

Frame safeguards as enabling safer independence, not covert observation or domination.

**Prefer:** `Add sensible guardrails for a first phone.`  
**Avoid:** `Control everything your child does online.`

### 5.5 Truthful

Use the evidence state that actually applies, even when uncertainty is less reassuring.

**Prefer:** `Status uncertain — we can’t verify this protection right now.`  
**Avoid:** `Protected` when only setup presence or parent confirmation exists.

### 5.6 Practical

Prioritize the next useful action and safe exit/recovery.

**Prefer:** `Turn off the conflicting custom DNS, then check again.` only when that action is actually safe/approved for the detected condition.  
**Avoid:** generic retries or long explanations before the next action.

### 5.7 Quietly trustworthy

Trust comes from clear boundaries, privacy restraint and reversible actions.

**Prefer:** `You do not need a UseSafeWeb account for this setup.`  
**Avoid:** `Completely anonymous. We collect nothing.`

## 6. Parent-facing writing rules

1. Address the user as **you** unless a surface requires a neutral instruction.
2. Refer to **your child** only when the sentence genuinely needs child context; do not repeatedly center the child as a monitored subject.
3. Prefer **safeguard** over **control** when describing the overall product.
4. Prefer **set up** as a verb and **setup** as a noun/adjective.
5. Prefer **check** in parent-facing CTA language; reserve **verify/verified** for the exact evidence state or where the distinction is necessary.
6. Prefer **not covered** over euphemisms such as “limited protection” when the capability is outside supported scope.
7. Prefer **status uncertain** over “probably protected”, “should be working” or equivalent optimism.
8. State the consequence of removal explicitly: UseSafeWeb DNS protection is no longer active after removal.
9. Do not force technical detail into headings when the user can act without it.
10. Do not turn product assumptions into findings. Avoid `parents find`, `parents prefer`, `easy for parents`, `proven simple` or equivalent unless later real evidence supports them.
11. Do not imply an account, persistent device profile or activity dashboard exists in the current baseline.
12. Do not imply official Turkish/Arabic market support merely because translated/localized content exists.
13. Do not invent support channels, response times, certifications, statistics, parent quotations or endorsements.

## 7. Canonical product terminology

| Canonical term | Meaning/use | Avoid or restrict |
| --- | --- | --- |
| **UseSafeWeb** | Product/service identity. | Do not rename as a generic DNS/security stack in parent-facing proposition. |
| **First Phone Safety Setup** | Primary descriptive category. | `Parental-control suite`, `child-monitoring platform`, `DNS service` as the primary product category. |
| **parent/caregiver** | Intended adult user role. | `administrator`, `operator`, `monitor` in ordinary parent-facing copy. |
| **first phone** | Child’s first independently used smartphone context. | Do not imply a legally fixed age threshold from the provisional 10–12 design assumption. |
| **safeguard** | Bounded protective setting/control. | `guarantee`, `shield`, `total protection` when implying absolute safety. |
| **Phone / Internet / Service** | Three product layers. | Do not imply the Internet/DNS layer configures Phone/Service controls. |
| **UseSafeWeb DNS** | Parent-facing name for the supported UseSafeWeb encrypted DNS protection path. | Avoid exposing transport jargon unless needed. |
| **Private DNS** | Android platform setting term when the exact supported path applies. | Do not use as a universal iPhone term. |
| **DNS profile** | iPhone configuration-profile concept when the exact supported path applies. | Do not imply silent installation or universal Apple-device support. |
| **check** | Parent-facing action to determine current state. | `scan` where it could imply browsing/content inspection. |
| **verify / Verified** | Reserved for current qualifying technical evidence. | Never use for parent confirmation or mere configuration presence. |
| **You confirmed this is set up** | Parent-confirmed positive state when UseSafeWeb cannot independently verify. | `Verified`, `Protected by UseSafeWeb`. |
| **Action needed** | Applicable incomplete/fixable state. | Do not soften into a positive state. |
| **Not covered** | Unsupported/out-of-scope/not-applicable safeguard state under TSK-0320 semantics. | `Protected elsewhere` unless directly proven. |
| **Status uncertain** | Conflicting/inconclusive/error state. | `Probably working`, `likely protected`. |
| **Removed** | Safeguard/UseSafeWeb configuration intentionally removed. | Do not keep a positive protection label after removal. |
| **Protection Map** | Evidence/coverage summary across layers. | `Safety score`, `protection score`, `all-clear`. |
| **remove** | End the UseSafeWeb DNS configuration. | Avoid `disable safety` or guilt framing. |
| **start over** | Clear/restart transient web journey state only. | Must not imply the device DNS configuration was removed. |
| **recovery** | Restore a working supported state or normal DNS after removal/failure. | Do not imply silent fallback while keeping a protection claim. |

## 8. Protection-state language

TSK-0320 remains the semantic owner. TSK-0299 does not rename or weaken those states.

### S1 — Protected — verified

**Primary label:** `Verified`  
**Default supporting copy:** `UseSafeWeb verified this protection step is active on your current setup.`

Use only when the owning technical verifier satisfies the exact current evidence threshold.

### S2 — Set up — parent confirmed

**Primary label:** `You confirmed this is set up`  
**Default supporting copy:** `UseSafeWeb has not independently verified this setting.`

### S3 — Action needed

**Primary label:** `Action needed`  
**Default supporting copy:** `Finish this step before relying on this protection layer.`

Replace the generic sentence with the exact safe corrective action when known.

### S4 — Not covered

**Primary label:** `Not covered`  
**Default supporting copy:** `UseSafeWeb does not cover this on your current setup.`

### S5 — Status uncertain / error

**Primary label:** `Status uncertain`  
**Default supporting copy:** `We can’t verify this protection right now. Check it before relying on this layer.`

### S6 — Removed

**Primary label:** `Removed`  
**DNS supporting copy:** `UseSafeWeb DNS is no longer active on this device.`

### Completion language

**Use:** `Setup complete. Review what UseSafeWeb verified, what you confirmed, and what is not covered.`

Do not use `Your child is safe`, `Fully protected`, `All protected`, an overall safety score, or an all-green treatment that makes parent confirmation equivalent to technical verification.

## 9. Approved claim library

The following are approved as current bounded formulations when used in the correct context.

### Product-purpose claims

- `UseSafeWeb helps you set up sensible first-phone safeguards.`
- `UseSafeWeb brings the phone, internet baseline and one relevant service safeguard into one clear setup path.`
- `UseSafeWeb shows what it verified, what you confirmed, what needs attention and what is not covered.`

### Accountless/privacy claims

- `You do not need a UseSafeWeb account for the current setup journey.`
- `UseSafeWeb is designed to minimize identity and journey data.`
- `UseSafeWeb is not a child browsing or activity monitoring product.`

These do not authorize absolute `zero data` or `completely anonymous` language.

### Control/recovery claims

- `You can remove the supported UseSafeWeb DNS configuration and follow recovery guidance.`
- `Starting over resets the web setup journey; it does not remove UseSafeWeb DNS from the phone.`

### Scope/limits claims

- `DNS filtering works at the domain-resolution layer. It does not inspect content inside an allowed app or site.`
- `Some VPN, Private Relay, custom DNS, browser/app DNS, managed-network or unsupported-device conditions can make protection unavailable or uncertain.`

## 10. Conditional claim library

These claims require the exact current condition stated below.

| Claim | Condition |
| --- | --- |
| `Verified` / `UseSafeWeb verified this protection step is active` | Current direct technical evidence satisfies TSK-0320/owning verifier for the exact supported path. |
| `Encrypted DNS` | Exact supported Android/iPhone mechanism under the current TSK-0408/0409 contract. |
| `UseSafeWeb DNS is active` | Current evidence supports active state; configuration presence alone is insufficient. |
| `This setting is set up` | Parent confirmation/current setup evidence supports S2 and no contradiction requires S5. |
| `Supported on this phone` | Exact device/OS/network path is inside the current support matrix. |
| `Free core protection` | Current commercial baseline remains unchanged; do not imply pricing can never change. |
| `Available in [market]` | Separate market/legal/publication authority exists. Current language capability alone is insufficient. |

When the condition cannot be demonstrated, downgrade or omit the claim rather than using a qualifying adverb such as `probably`, `normally` or `should` to preserve a positive impression.

## 11. Prohibited claim and expression library

The following remain prohibited unless a later higher-authority change explicitly authorizes a narrower supported statement:

- `Complete protection`, `100% safe online`, `fully protected`, `total internet safety`, `blocks everything harmful`;
- `Your child is safe`, `your child is protected` as an overall outcome claim;
- `See everything your child does`, `monitor browsing`, `track your child`, `read messages`, `full parental control`;
- `Verified` or `Protected` from parent confirmation, setting/profile presence, old evidence or synthetic rehearsal;
- `Impossible to bypass`, `always protected`, `cannot be removed`;
- `We collect nothing`, `zero data`, `completely anonymous` without exact separately proven scope;
- `Legally approved`, `fully compliant`, `GDPR certified`, `certified safe`;
- `Parents love it`, `proven easy`, `validated with families`, `parents understand it`;
- `The safest`, `the only`, `best parental protection`, `unique` without current comparative evidence;
- fear/shame language such as `Your child is in danger unless…` or `Responsible parents must…`;
- `Launch-ready`, `available everywhere`, `works on every device/network`, `fully supported`;
- `24/7 support team`, `a specialist is always available` when no such routine staffed service is authorized;
- `Premium protection`, `pay for better safety`, `guaranteed value` under the current free-core/payment-gated baseline.

## 12. CTA language system

CTA text describes the exact next action. Avoid generic `Continue` when the destination/action can be named.

### Public website

- `Start setup` — primary entry from public information into the operational setup journey.
- `See how it works`
- `Check compatibility`
- `Read privacy details`
- `Get help`

### Setup routing

- `Choose this phone`
- `Set up phone safeguard`
- `Set up UseSafeWeb DNS`
- `Skip this step` only where skipping is actually allowed and consequence is clear.

### Verification/state

- `Check protection`
- `Check again` only after a relevant condition has changed.
- `Fix this`
- `See why this is uncertain`
- `See what’s not covered`

### Recovery/removal

- `Remove UseSafeWeb DNS`
- `Restore normal DNS`
- `Start over` — web journey only.
- `Get recovery help`

### Exit/navigation

- `Back`
- `Exit setup`
- `Return to UseSafeWeb`

Do not use CTAs that imply a result before it exists, such as `Become protected`, `Make my child safe`, `Secure everything`, or `Finish protection` when material S2/S3/S4/S5/S6 states can remain.

## 13. Trust-language patterns

### 13.1 Explain before asking

When requesting a routing fact, explain why only if the reason is not obvious.

**Pattern:** `Choose the phone type so UseSafeWeb can show the supported setup path.`

Do not request identity/contact/child details merely to personalize copy.

### 13.2 Distinguish what UseSafeWeb knows

**System evidence:** `UseSafeWeb verified…`  
**Parent evidence:** `You confirmed…`  
**Unknown:** `We can’t verify…`  
**Scope limit:** `UseSafeWeb does not cover…`

### 13.3 Explain privacy without absolutes

**Pattern:** `You do not need a UseSafeWeb account for this setup. UseSafeWeb is designed to minimize identity and journey data and is not a child browsing-history product.`

### 13.4 Explain removal without pressure

**Pattern:** `You can remove UseSafeWeb DNS at any time. After removal, UseSafeWeb no longer claims DNS protection on this device.`

### 13.5 Explain a limit without fear

**Pattern:** `DNS filtering can block some domains before they load, but it cannot inspect harmful content delivered inside an allowed app or site.`

## 14. Surface examples

These are reusable communication examples, not approved public-release copy and not evidence of parent comprehension.

### Public Home — proposition

**Heading:** `A clearer way to set up a child’s first phone`  
**Body:** `UseSafeWeb guides sensible safeguards across the phone, internet baseline and one relevant service, then shows what is verified, what you confirmed and what is not covered.`  
**Primary CTA:** `Start setup`

### How it works — three layers

**Heading:** `Three layers. One setup path.`  
**Phone:** `Start with relevant safeguards already built into the phone.`  
**Internet:** `Set up the supported encrypted UseSafeWeb DNS baseline.`  
**Service:** `Add one relevant service safeguard when it genuinely applies.`

### Compatibility — unsupported condition

**Heading:** `This setup is not covered yet`  
**Body:** `UseSafeWeb does not have an approved setup path for this device or network condition. Do not rely on UseSafeWeb protection here.`  
**CTA:** `See supported setups`

### Setup — Android DNS

**Heading:** `Set up UseSafeWeb DNS`  
**Body:** `Open Android’s Private DNS setting, choose the custom provider-hostname option and enter dns.usesafeweb.com exactly as shown.`  
**CTA:** `Check protection`

The full source/version-specific instruction remains owned by TSK-0307; this example must not become a second mutable instruction authority.

### Verification — success

**Heading:** `Verified`  
**Body:** `UseSafeWeb verified this protection step is active on your current setup.`

### Verification — parent-confirmed

**Heading:** `You confirmed this is set up`  
**Body:** `UseSafeWeb has not independently verified this setting.`

### Verification — uncertain

**Heading:** `Status uncertain`  
**Body:** `We can’t verify this protection right now. A VPN, Private Relay, custom DNS or another network condition may affect the path.`  
**CTA:** `See why this is uncertain`

### Protection Map — completion

**Heading:** `Setup complete`  
**Body:** `Review what UseSafeWeb verified, what you confirmed, what still needs attention and what is not covered.`

### Removal

**Heading:** `Remove UseSafeWeb DNS`  
**Body:** `Removing UseSafeWeb DNS ends the UseSafeWeb DNS protection claim on this device. You can follow the supported steps to return the phone to its normal DNS policy.`  
**CTA:** `Show removal steps`

## 15. Help and error language

1. Name the issue before the remedy when the cause is known.
2. Do not expose internal codes as the only user-facing explanation.
3. Do not tell the user to retry without a changed condition when TSK-0319 defines a specific repair prerequisite.
4. Never instruct the parent to disable employer/school/security controls merely to obtain a green result unless the exact authoritative troubleshooting path explicitly permits it.
5. Avoid `Something went wrong` as the complete message when a safer specific explanation exists.
6. If the condition is outside current support, use `Not covered`; do not manufacture a workaround.
7. If evidence is inconclusive, use `Status uncertain`; do not convert uncertainty into `Action needed` merely to create a CTA.
8. Recovery language must not silently fall back to plaintext/other DNS while retaining a UseSafeWeb protection claim.

## 16. Localization and reuse contract

TSK-0311 remains the architecture owner. This verbal system supplies semantics, not hard-coded implementation strings.

Rules:

1. `en-GB` is the canonical authored baseline for ordinary UI copy.
2. `tr-TR` and `ar` remain provisional variants; they do not activate markets.
3. Translation must preserve evidence strength. `You confirmed` cannot become `Verified`; `Status uncertain` cannot become certainty; `Not covered` cannot become a weaker limitation.
4. Semantic translation keys describe intent rather than English wording.
5. Technical literals such as `dns.usesafeweb.com`, URLs, version numbers, IDs and checksums are not localized.
6. Arabic uses RTL presentation while technical literals remain directionally isolated.
7. Critical setup/verification/removal strings remain bound to TSK-0307 instruction IDs instead of being independently rewritten.
8. No runtime machine translation may become authoritative fallback for safety/privacy/legal/setup/verification/recovery copy.
9. Native/qualified language and later representative-parent review remain required before any claim of publication-ready localized comprehension.

## 17. Child-aware language rules

- Do not describe the child as a threat, data source, suspect or object of surveillance.
- Do not use shame-based language toward either parent or child.
- Do not imply UseSafeWeb reads messages, images, location, contacts or social content.
- Do not promise that the service prevents every harmful experience.
- Prefer language about **sensible safeguards**, **clear limits** and **safer independence**.
- Where a native/service safeguard is parent-confirmed rather than technically verified, preserve that distinction even if a stronger phrase would sound more reassuring.

## 18. Legal, safeguarding and market-language boundary

This verbal system does not author legal notices, statutory conclusions, consent language, age-policy conclusions, regulator claims or market-specific legal representations.

Where legal/privacy/safeguarding content is required:

- use only current content supplied/approved by the owning legal/privacy/safeguarding authority;
- do not use marketing tone to weaken a mandatory limitation or notice;
- do not label unresolved legal work as complete;
- do not convert UK/England design orientation into an official public-market availability statement;
- do not make `GDPR compliant`, certification or equivalent claims without explicit current evidence/authority.

## 19. Reuse by surface

| Surface | Verbal priority | Required truth boundary |
| --- | --- | --- |
| Public Home | Outcome → bounded layers → trust/limits → Start | No behavioral-validation, total-safety or false-market claim. |
| How it works | Three layers → evidence states → limits | DNS does not become a universal safety layer. |
| Compatibility | Support truth → limitation → safe next action | Unsupported remains Not covered. |
| Privacy | Accountless-first/non-surveillance/minimization | No absolute `zero data` claim. |
| Setup | One action → exact source-backed instruction → next check | Do not over-explain or skip material platform asymmetry. |
| Verification | Evidence state → concise reason → one next action | Verification strength exactly matches TSK-0320. |
| Protection Map | Layer state → evidence/limit → next action | No overall safety score/all-green equivalence. |
| Troubleshooting | Specific issue → changed condition → recheck/recover | No blind retry loop or unsafe workaround. |
| Removal/recovery | Consequence → exact removal/recovery → neutral result | Removal ends the protection claim. |
| Help | Concrete parent problem → source-backed resolution | No invented support channel or universal workaround. |

## 20. Acceptance test matrix

| ACC-0299 clause | Verbal-system proof |
| --- | --- |
| Plain-language parent-facing design | §§2, 5, 6, 12–15 use ordinary wording, concrete actions and technical-detail gating. |
| Child-aware | §17 prohibits surveillance/threat framing and centers safer independence. |
| Non-alarmist | §§5.1, 7, 11, 17 prohibit fear/shame/urgency theatre. |
| Non-technical design rules | Message hierarchy defers technical detail to Level 5; canonical terms prevent DNS jargon-led proposition. |
| Approved claims/non-surveillance constraints | §§9–11 bind TSK-0298/TSK-0320 claim strength and explicit prohibited classes. |
| Reusable across surfaces | §§4, 12–14, 19 define shared hierarchy, CTA patterns and surface examples. |
| Reusable across locales | §16 binds the TSK-0311 semantic-key/fallback/RTL/evidence-strength contract. |
| Representative-parent comprehension remains unproven | §§1, 6, 14, 16 explicitly preserve RSK-0002 and future TSK-0187 evidence need. |
| Legal completion remains unproven | §§1 and 18 preserve deferred legal authority and prohibit compliance/certification inference. |

## 21. Bounded result

The current verbal system is sufficiently complete for provisional internal L4 design use. It defines descriptors, message hierarchy, voice/tone, canonical terminology, protection-state language, approved/conditional/prohibited claims, CTA language, trust patterns, surface examples, localization semantics and legal/behavioral boundaries.

It does **not** prove representative-parent comprehension, native-speaker publication readiness, legal completion, implemented UI quality, accessibility conformance, market readiness or launch readiness.
