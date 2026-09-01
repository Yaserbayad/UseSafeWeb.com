# TSK-0299 — Dual-Mode Verbal System — Post-CR-0008

**Task:** TSK-0299 — Define tone, voice, terminology, trust language, protection-state language, and communication examples  
**Acceptance / Verification / Evidence:** ACC-0299 / VER-0299 / EVD-0299  
**Lifecycle / Priority:** L4 / HIGH  
**AI capability / Action Authority:** A3 / AUTO_ALLOWED  
**Version:** 2.0.0-post-cr0008  
**Date:** 2026-09-01  
**Status:** CURRENT CANDIDATE FOR INDEPENDENT ACCEPTANCE; no implementation, publication, legal completion, market activation or launch is inferred  
**Hard dependency:** current TSK-0298 PASS  
**Current supporting authority:** DEC-0052/CR-0005; DEC-0053/CR-0006; DEC-0054/CR-0007; DEC-0055/CR-0008; REQ-0024/0025/0026; CON-0017/0023; INT-0008; current TSK-0229, TSK-0315, TSK-0318, TSK-0319 and TSK-0320.

## 1. Objective, supersession and evidence boundary

This artifact supersedes the **account-exclusion-dependent and stale protection-state wording** in `TSK_0299_PROVISIONAL_VERBAL_SYSTEM_2026-08-29.md` for current acceptance. The historical artifact remains valid evidence for compatible tone, plain-language, non-alarmist, non-surveillance, claims-limitation and localization principles.

DEC-0053/CR-0006 changed Version-1 scope after that artifact was accepted. Current UseSafeWeb is dual-mode:

1. the complete **accountless core** First Phone Safety Setup remains usable without login; and
2. an **optional parent account** adds sign-in/session continuity, a lightweight dashboard and bounded device-management/lifecycle functions.

The historical rule `Do not imply an account, persistent device profile or activity dashboard exists in the current baseline` is therefore superseded. Current language must describe the optional account/dashboard truthfully **without** turning it into a mandatory gate, surveillance product, technical verification signal, broad parental-control console or automatic import of anonymous journey state.

Current TSK-0320 also supersedes the historical short state labels where they differ. This verbal system uses the current state/copy contract exactly and does not invent a competing protection-state vocabulary.

`RSK-0002` remains OPEN. Under DEC-0052/CR-0005, representative-parent comprehension/usability validation occurs only after integrated-product readiness in L8. This artifact is internal L4 design-conformance evidence only. It does not claim that parents understand, prefer, trust, complete or value the language, and it does not establish deferred legal/privacy completion.

## 2. Verbal-system invariants

1. **Plain language first.** Technical terms appear only when required to complete, verify, troubleshoot or remove a supported action.
2. **Calm, non-alarmist framing.** State material risk and consequence without fear, urgency theatre, shame or guilt.
3. **Child-aware, not child-surveillance language.** The child is never framed as a monitored data source or adversary.
4. **One next action at a time.** Headings and CTAs describe the actual user action or decision.
5. **Evidence truth outranks reassurance.** Protection language follows current TSK-0320 evidence state exactly.
6. **Accountless core stays first-class.** Copy never implies sign-in is required for setup, verification, troubleshooting, removal or recovery.
7. **Optional account is continuity, not stronger protection.** Account ownership, dashboard presence and stored device data never imply current technical protection.
8. **Anonymous and persistent state stay separate.** Sign-in never implies automatic J0/J1 import, promotion, linkage or TTL extension.
9. **Lifecycle operations say exactly what they change.** Logout, unlink/revoke, device-record deletion, account deletion, anonymous reset/deletion and physical DNS removal are never described as equivalent.
10. **No browsing/query/activity history.** No copy implies that the dashboard shows visited sites, DNS queries, messages, location or child activity.
11. **No broad DNS administration.** Parent-facing language never suggests access to AdGuard administration, arbitrary policy editing, query logs or a raw DNS console.
12. **Localization preserves semantics.** English, Turkish and Arabic/RTL variants must preserve actor, evidence strength, optionality, scope, uncertainty and destructive-operation consequence.
13. **No unsupported readiness claim.** Language availability, route existence or an internal design artifact is not proof of market, provider, legal, implementation, publication or launch readiness.

## 3. Voice model

### 3.1 Calm

State the condition and next action without dramatization.

**Prefer:** `Protection status could not be verified. Check the current setup before relying on this protection.`  
**Avoid:** `Your child may be in danger — fix this immediately.`

### 3.2 Clear

Use ordinary words, short sentences and explicit actions.

**Prefer:** `Open Private DNS and enter the approved UseSafeWeb hostname.`  
**Avoid:** `Configure the encrypted resolver endpoint using the applicable provider mechanism.`

### 3.3 Respectful

Treat the parent/caregiver as capable. Explain consequences without blame.

**Prefer:** `You can continue without signing in.`  
**Avoid:** `Responsible parents should create an account.`

### 3.4 Protective, not controlling

Frame the product as bounded safeguards supporting safer independence.

**Prefer:** `Add sensible guardrails for a first phone.`  
**Avoid:** `Control everything your child does online.`

### 3.5 Truthful

Use uncertainty when evidence is uncertain, even when a positive message would feel easier.

**Prefer:** `Setup confirmed. Protection has not yet been technically verified.`  
**Avoid:** `Protected` because a profile, account, device record or previous check exists.

### 3.6 Practical

Lead with the smallest safe next action and keep removal/recovery reachable.

**Prefer:** `Update this setting, then verify again.` when current evidence supports that remedy.  
**Avoid:** generic retry loops or speculative device changes.

### 3.7 Quietly trustworthy

Trust comes from explicit boundaries, minimised data, reversible actions and honest status.

**Prefer:** `You can complete the core setup without an account.`  
**Avoid:** `Completely anonymous. We collect nothing.`

## 4. Canonical descriptors and message hierarchy

### 4.1 Primary product descriptor

**First Phone Safety Setup**

Use this as the primary parent-facing descriptive category. Do not lead with `DNS service`, `parental-control suite`, `monitoring platform` or infrastructure language.

### 4.2 Short explanatory descriptor

**A clear setup path for sensible first-phone safeguards.**

### 4.3 Expanded explanatory descriptor

**UseSafeWeb helps you put sensible first-phone safeguards in place across the phone, internet baseline and one relevant service — with clear limits and without turning the experience into child surveillance.**

### 4.4 Internal brand line

**Clear guardrails for safer first-phone independence.**

`Safer` is bounded comparative language, not a guarantee of safety. `Guardrails` means limited safeguards with visible limits, not monitoring or total control.

### 4.5 Message hierarchy

1. **Parent outcome:** `Put sensible first-phone safeguards in place through one clear setup path.`
2. **Three bounded layers:** Phone / Internet / Service.
3. **Protection truth:** what UseSafeWeb technically verified, what setup was confirmed, what needs action, what is not covered, what is uncertain and what was removed.
4. **Account choice:** core setup works without login; optional sign-in adds continuity and bounded device management only.
5. **Privacy/control/limits:** no browsing/query/activity history; separate lifecycle actions; clear removal/recovery and unsupported conditions.
6. **Technical detail:** only the platform-specific detail required at the current step.

No surface should invert this hierarchy by leading with provider, database, DNS infrastructure, account mechanics, fear or legal/compliance theatre.

## 5. Parent-facing writing rules

1. Address the user as **you** unless a neutral instruction is clearer.
2. Use **your child** only when child context is materially needed; do not repeatedly frame the child as a monitored subject.
3. Prefer **safeguard** over **control** for the overall product.
4. Prefer **set up** as a verb and **setup** as a noun/adjective.
5. Prefer **check** for an ordinary CTA; reserve `verify/verified` for the exact technical-evidence meaning or when explaining that distinction.
6. Prefer **Not covered** when the current scope is unsupported; do not cosmetically turn unsupported scope into partial success.
7. Prefer **Protection status could not be verified** when evidence is materially uncertain; do not use `probably`, `should be working` or stale positive status.
8. State physical-removal consequences explicitly and separately from web/account operations.
9. Do not put technical terms in headings when the parent can act without them.
10. Do not convert design assumptions into findings: no `parents find`, `parents prefer`, `proven simple`, `validated with families` or equivalent without later real evidence.
11. In accountless-core copy, do not invent personalization/account state. In optional-account copy, describe only the bounded account/device continuity that current IA authorizes.
12. Do not imply official Turkish/Arabic market/support/legal readiness merely because localized content exists.
13. Do not invent support channels, response times, certifications, statistics, testimonials, endorsements or provider acceptance.
14. Do not use account/dashboard copy as a protection badge. A device listed in the dashboard may still be S2, S3, S4, S5 or S6.
15. Destructive or ownership-changing copy must name the target object: **web setup**, **device record**, **account**, **management link**, or **UseSafeWeb DNS configuration**.

## 6. Canonical terminology

| Canonical term | Parent-facing meaning/use | Avoid or restrict |
| --- | --- | --- |
| **UseSafeWeb** | Product/service identity. | Do not present as a generic DNS/security stack. |
| **First Phone Safety Setup** | Primary product descriptor. | `Parental-control suite`, `child-monitoring platform`, `DNS service` as the main category. |
| **parent/caregiver** | Intended adult user role. | `administrator`, `operator`, `monitor` in ordinary copy. |
| **first phone** | Child's first independently used smartphone context. | Do not imply a legally fixed age threshold. |
| **safeguard** | A bounded protective setting/action. | `guarantee`, `shield`, `total protection` when implying absolutes. |
| **Phone / Internet / Service** | Three bounded Protection Map layers. | Do not imply DNS configures the Phone/Service layers. |
| **UseSafeWeb DNS** | Supported encrypted DNS protection path. | Transport jargon unless needed for the exact step. |
| **Protection Map** | Evidence/coverage summary across layers. | `Safety score`, `protection score`, `all-clear`. |
| **accountless core** | Complete core setup/protection journey usable without login. | `guest mode` if it suggests a crippled or temporary inferior product. |
| **optional parent account** | Optional continuity/session/device-management capability. | `required account`, `child account`, `family surveillance account`. |
| **Sign in** | Enter optional account continuity. | `Unlock protection`, `secure your child` or other copy implying stronger safety. |
| **Dashboard** | Lightweight view of authorized managed-device records and bounded lifecycle actions. | `activity dashboard`, `monitoring dashboard`, `DNS admin console`. |
| **device record** | Persistent dashboard record for an authorized managed device. | `child profile`, `browsing profile`, `protection proof`. |
| **managed device** | Device record the signed-in parent is authorized to manage in the bounded product sense. | Do not imply OS-level MDM, surveillance or unremovable control. |
| **Add device** | Start a fresh supported device setup/management flow. | Do not imply automatic import of the current anonymous journey. |
| **check protection** | Run the current approved verification path. | `scan activity` or language implying browsing inspection. |
| **Protection verified** | S1 only: current qualifying technical evidence exists. | Never from account/device ownership, profile presence or parent confirmation. |
| **Setup confirmed** | S2: configuration/parent confirmation exists without qualifying technical verification. | `Verified`, `Protected`, `Protection active`. |
| **Action needed** | S3: a concrete safe action is required. | Positive protection badge as the primary state. |
| **Not covered** | S4: current authoritative scope is unsupported/out of scope. | `Protected elsewhere` unless separately proven. |
| **Protection status could not be verified** | S5: current status is materially uncertain/error. | `Probably protected`, `likely active`. |
| **Removed** | S6 for the exact removed/revoked configuration scope. | Do not retain stale positive protection language. |
| **Start over** | Reset the accountless web journey state only. | Must not imply physical DNS removal or account deletion. |
| **Unlink / revoke management** | Remove the dashboard management association for a device record. | Must not imply physical DNS removal. |
| **Delete device record** | Delete the persistent dashboard record under its data contract. | Must not imply DNS removal or account deletion. |
| **Delete account** | Delete governed account/device-ownership data under its lifecycle contract. | Must not imply anonymous-state deletion or DNS removal. |
| **Remove UseSafeWeb DNS** | Change the physical supported device DNS configuration. | Do not conflate with logout/unlink/delete record/delete account. |
| **recovery** | Restore ordinary connectivity or a supported working state after failure/removal. | Do not imply silent fallback while keeping a protection claim. |

## 7. Current protection-state language — TSK-0320 governs

TSK-0299 does not rename, weaken or cosmetically simplify current TSK-0320 states.

### S1 — `protected/verified`

**Primary copy:** `Protection verified`  
**Default supporting copy:** `UseSafeWeb verified this protection step for this setup.`

Use only when fresh qualifying technical evidence exists for the exact scope. Show material time/scope limits when relevant.

### S2 — `configured/parent-confirmed`

**Primary copy:** `Setup confirmed`  
**Mandatory supporting copy:** `Protection has not yet been technically verified.`

Account/device ownership, saved setup context or parent confirmation never upgrades S2 to S1.

### S3 — `action-needed`

**Primary copy:** `Action needed`  
**Default grammar:** name the concrete next action and consequence, e.g. `Update this setting, then verify again.`

### S4 — `not-covered`

**Primary copy:** `Not covered`  
**Default supporting copy:** `UseSafeWeb does not cover this on your current setup.`

### S5 — `uncertain/error`

**Primary copy:** `Protection status could not be verified`  
**Default supporting copy:** `Retry verification or follow the troubleshooting steps before relying on this protection.`

A stale S1/S2 positive label may not remain visually dominant when current evidence is materially uncertain.

### S6 — `removed`

**Primary copy:** `Removed`  
**Default supporting copy:** `This setup is no longer enrolled through UseSafeWeb.`

For DNS-specific removal, state that UseSafeWeb DNS is no longer configured/claimed active for that device. A later dashboard record does not undo S6.

### Completion language

**Preferred:** `Setup complete. Review what UseSafeWeb verified, what you confirmed, what needs action, and what is not covered.`

Do not use `Your child is safe`, `Fully protected`, `All protected`, an overall safety score, or styling/copy that makes parent confirmation/account ownership look technically verified.

## 8. Dual-mode trust and privacy claim library

### 8.1 Allowed current formulations

- `UseSafeWeb helps you set up sensible first-phone safeguards.`
- `You can complete the core setup without a UseSafeWeb account.`
- `Signing in is optional and adds account continuity and bounded device management.`
- `You can continue without signing in.`
- `Signing in does not automatically import this anonymous setup into your account.`
- `A saved device record is not proof that protection is currently active.`
- `UseSafeWeb shows what it technically verified, what setup was confirmed, what needs action, what is not covered, what is uncertain and what was removed.`
- `UseSafeWeb is designed to minimize identity and journey data.`
- `UseSafeWeb is not a child browsing or activity monitoring product.`
- `The dashboard does not provide browsing, DNS-query or child-activity history.`
- `Starting over resets the web setup journey; it does not remove UseSafeWeb DNS from the phone.`
- `Deleting a dashboard device record does not remove UseSafeWeb DNS from the phone.`
- `Deleting your account does not by itself remove UseSafeWeb DNS from a phone.`
- `You can remove the supported UseSafeWeb DNS configuration and follow recovery guidance.`

These are bounded product-language rules. They do not establish a legal notice, retention period, provider acceptance or implemented runtime behavior unless the owning downstream evidence separately proves it.

### 8.2 Conditional claims

| Claim | Required condition |
| --- | --- |
| `Protection verified` | Current qualifying technical evidence satisfies TSK-0320/owning verifier for the exact scope. |
| `UseSafeWeb DNS is active` | Current technical evidence supports the active intended path; configuration/account presence alone is insufficient. |
| `Setup confirmed` | Current E2 setup/parent-confirmation evidence exists with no hidden contradiction requiring S3/S5. |
| `Supported on this phone/network` | Exact current support matrix covers the tuple. |
| `Sign in with [provider]` | The downstream implementation/provider contract has approved that provider and the exact provider-required branding/copy. TSK-0299 does not pre-approve production provider behavior. |
| `Saved` / `device added` / `unlinked` / `deleted` | The exact persistent operation has durable confirmed completion. Unknown results use uncertainty/reconciliation copy, never optimistic success. |
| `Available in [market]` | Separate named-market/legal/publication authority exists; language capability alone is insufficient. |
| `Free core protection` | Current commercial baseline remains applicable; do not imply pricing can never change. |

When a condition is not proven, omit or downgrade the claim rather than using `probably`, `normally` or `should` to preserve a positive impression.

## 9. Optional account, dashboard and lifecycle language

### 9.1 Account entry

**Heading:** `Sign in to manage devices`  
**Supporting copy:** `Signing in is optional. You can complete setup, check protection, troubleshoot and remove UseSafeWeb DNS without an account.`  
**Primary CTA:** `Sign in`  
**Secondary CTA:** `Continue without account`

Never use `Sign in to activate protection`, `Create an account to stay protected`, or equivalent coercive safety language.

### 9.2 Auth cancel/failure/provider outage

**Cancelled:** `Sign-in was cancelled. You can continue without an account.`  
**Failed:** `Sign-in did not complete. Try again later or continue without an account.`  
**Provider unavailable:** `Account features are temporarily unavailable. Core setup, protection checks, help and removal remain available without signing in.`

Do not claim account creation/session success from a redirect or ambiguous provider result.

### 9.3 Dashboard empty/list

**Empty heading:** `No managed devices yet`  
**Empty action:** `Add device`  
**List explanation:** `Saved device records help you return to bounded setup and management actions. Check current protection before relying on a saved status.`

Never use `Your children`, `Activity`, `Browsing history`, `Live protection feed` or equivalent surveillance framing.

### 9.4 Device detail

Show device nickname/generic label, platform/context where authorized, current evidence state/currentness and bounded actions. Use language such as:

- `Check protection`
- `Reinstall or reconfigure`
- `Replace device`
- `Unlink device`
- `Delete device record`
- `Remove UseSafeWeb DNS`

Do not use `Always protected`, `Monitored`, `Child activity`, or account ownership as a protection badge.

### 9.5 Session expired/revoked

**Heading:** `Sign in again to manage this account`  
**Supporting copy:** `Your account session is no longer active. This does not tell us whether UseSafeWeb DNS is currently configured or verified on a device.`

Core help/removal routes remain available without sign-in.

### 9.6 Unknown consequential result

For add/unlink/delete/account operations whose outcome is ambiguous:

**Heading:** `We couldn't confirm that change`  
**Supporting copy:** `Check the current account or device state before trying again.`

Do not instruct blind replay of a destructive or ownership-changing operation.

## 10. Destructive-operation consequence copy

Each operation must name its exact consequence before confirmation.

| Operation | Required consequence language | Must not imply |
| --- | --- | --- |
| **Start over** | `This resets the current web setup journey. It does not remove UseSafeWeb DNS from the phone.` | DNS removal, account deletion, device-record deletion. |
| **Log out** | `This ends this account session. It does not change the phone's DNS configuration.` | DNS removal or device deletion. |
| **Unlink / revoke device management** | `This removes the account's management association for this device record.` | Physical DNS removal. |
| **Delete device record** | `This deletes the saved dashboard record. It does not remove UseSafeWeb DNS from the phone.` | Account deletion or DNS removal. |
| **Delete account** | `This deletes governed account/device-ownership data under the account lifecycle. It does not by itself remove UseSafeWeb DNS from a phone.` | Anonymous-state deletion or physical DNS removal. |
| **Remove UseSafeWeb DNS** | `This removes the supported UseSafeWeb DNS configuration from this phone. Protection through that configuration will no longer be claimed active.` | Account/device-record deletion. |

If completion is not confirmed, use pending/uncertain language rather than the past-tense success form.

## 11. CTA language system by surface

CTA text names the exact next action. Avoid generic `Continue` when the destination or action can be stated.

### 11.1 Public website

- `Start setup`
- `See how it works`
- `Check compatibility`
- `Read privacy details`
- `Get help`
- `Sign in`
- `Manage devices` only when it routes to the optional account path and does not displace `Start setup` as the core-value entry.

### 11.2 Accountless core setup

- `Start setup`
- `Choose your phone`
- `Set up this safeguard`
- `Set up UseSafeWeb DNS`
- `Check protection`
- `Review Protection Map`
- `Get help`
- `Try again` only after a materially changed condition/current retry rule permits it
- `Remove UseSafeWeb DNS`
- `Start over`
- `Finish without account`
- `Sign in to manage devices`

### 11.3 Optional account/dashboard

- `Sign in`
- `Continue without account`
- `Try sign-in again` only after a changed provider/network/session condition
- `Go to dashboard`
- `Add device`
- `Check protection`
- `Reinstall or reconfigure`
- `Replace device`
- `Unlink device`
- `Delete device record`
- `Account settings`
- `Log out`
- `Delete account`

### 11.4 Recovery/help

- `See troubleshooting steps`
- `Check again` after a changed condition
- `Check service status`
- `Remove UseSafeWeb DNS`
- `Check normal connectivity`
- `Return to setup`
- `Exit setup`

Never use CTA language that implies an unsupported automatic repair, silent account linkage, stronger protection from sign-in, or physical DNS removal from an account-only action.

## 12. Error, uncertainty and point-of-need help grammar

1. **Name the state first:** what failed, is unknown, is unsupported or needs action.
2. **Name one safe next action:** only one that current evidence supports.
3. **State material consequence:** especially for removal, reset, deletion, provider outage or session expiry.
4. **Preserve an escape path:** accountless core Help/Exit/DNS removal remains reachable during account/provider failure.
5. **No blame:** avoid `you entered this wrong` when the cause is not proven.
6. **No speculative fixes:** do not ask the parent to experiment through unverified settings.
7. **No generic retry loop:** retry copy is shown only after changed evidence or an idempotent safe operation.
8. **No surveillance diagnostics:** do not request browsing history, DNS-query history, child messages/location/content or unrelated device inventory.

Reusable patterns:

- **Known action:** `[State]. [Concrete safe action], then check again.`
- **Unsupported:** `Not covered. UseSafeWeb does not cover this on your current setup.`
- **Uncertain:** `Protection status could not be verified. [One safe troubleshooting/recheck route].`
- **Service/provider outage:** `[Feature] is temporarily unavailable. [Unaffected accountless capability] remains available.`
- **Unknown destructive result:** `We couldn't confirm that change. Check the current state before trying again.`
- **Removal complete:** `Removed. UseSafeWeb DNS is no longer configured/claimed active for this phone.`

## 13. Prohibited claim and expression library

The following remain prohibited unless later higher authority explicitly supports a narrower factual statement:

- `Complete protection`, `100% safe online`, `fully protected`, `total internet safety`, `blocks everything harmful`;
- `Your child is safe`, `your child is protected` as an overall outcome;
- `See everything your child does`, `monitor browsing`, `track your child`, `read messages`, `live activity`, `full parental control`;
- `Protection verified`/`Protected` from account ownership, dashboard presence, setting/profile presence, parent confirmation, old evidence or synthetic rehearsal;
- `Impossible to bypass`, `always protected`, `cannot be removed`;
- `We collect nothing`, `zero data`, `completely anonymous` without exact separately proven scope;
- `Legally approved`, `fully compliant`, `GDPR certified`, `certified safe`;
- `Parents love it`, `proven easy`, `validated with families`, `parents understand it`;
- `The safest`, `the only`, `best parental protection`, `unique` without current comparative evidence;
- fear/shame language such as `Your child is in danger unless…`, `Responsible parents must…`, countdown or guilt pressure;
- `Launch-ready`, `available everywhere`, `works on every device/network`, `fully supported`;
- `24/7 support team`, `a specialist is always available` when no such routine staffed service is authorized;
- `Premium protection`, `pay for better safety`, `guaranteed value` under the current free-core baseline;
- `Sign in to activate protection`, `Create an account to stay protected`, `Account verified protection`;
- `Activity dashboard`, `Browsing dashboard`, `Your child's history`, `Top sites`, `Recent queries`;
- `Deleting this device removes protection from the phone` when the operation deletes only the dashboard record;
- `Deleting your account removes UseSafeWeb from all phones`;
- `Saved`/`deleted`/`unlinked`/`account deleted` when durable completion is not actually known.

## 14. Localization and RTL semantic contract

First public-release technical language capability covers English, Turkish and Arabic with RTL support under CON-0017. This is a language/implementation requirement, not official market/legal/support activation.

### 14.1 Translation invariants

Every locale must preserve:

- evidence actor: UseSafeWeb verified vs parent confirmed;
- evidence strength: S1 must not be weakened; S2 must not be strengthened;
- uncertainty: S5 cannot become a reassuring positive phrase;
- optionality: `Sign in` remains optional and `Continue without account` remains a true alternative;
- object scope: web journey vs account vs device record vs DNS configuration;
- destructive consequence: deletion/unlink/removal verbs must point to the exact object affected;
- non-surveillance meaning;
- technical mechanism distinctions where required by platform;
- no automatic accountless-to-account linkage implication;
- no market-activation implication from translation availability.

### 14.2 Canonical semantic keys

Implementations should expose stable semantic keys or equivalent content contracts for at least:

- `product.first_phone_safety_setup`
- `cta.start_setup`
- `cta.finish_without_account`
- `cta.sign_in_manage_devices`
- `cta.continue_without_account`
- `cta.check_protection`
- `state.s1.protection_verified`
- `state.s2.setup_confirmed`
- `state.s2.not_technically_verified`
- `state.s3.action_needed`
- `state.s4.not_covered`
- `state.s5.could_not_verify`
- `state.s6.removed`
- `account.optional_explainer`
- `account.provider_unavailable`
- `account.session_expired`
- `dashboard.no_devices`
- `device.saved_status_not_current_proof`
- `lifecycle.start_over_consequence`
- `lifecycle.unlink_consequence`
- `lifecycle.delete_record_consequence`
- `lifecycle.delete_account_consequence`
- `lifecycle.remove_dns_consequence`
- `operation.unknown_result`

Locale files may adapt grammar/order for natural language and RTL, but not change these semantics.

## 15. Cross-surface verbal contract

| Surface | Primary language job | Required message elements | Forbidden implication |
| --- | --- | --- | --- |
| Public home/how-it-works | Explain bounded value and trust. | First Phone Safety Setup; Phone/Internet/Service; clear limits; Start setup; optional Sign in. | Complete safety, surveillance, login prerequisite. |
| Compatibility/limits | Explain supported boundary. | Exact support/not-covered language; technical detail only as needed. | Universal support. |
| Accountless setup | Guide one safe action at a time. | Plain CTA, current state, help/removal, no identity requirement. | Inferior/temporary guest experience. |
| Protection Map | Present evidence truth. | Current S1–S6 wording and scope/currentness. | Safety score, account ownership as verification. |
| Core completion | Close accountless value and offer optional continuity. | Finish without account first-class; optional Sign in to manage devices. | Sign-in required to keep protection. |
| Sign-in/auth | Explain optional account entry/failure. | Optionality, Continue without account, provider/session truth. | Provider success before evidence; stronger protection from account. |
| Dashboard | Present minimum managed-device continuity. | Device records, currentness, Check protection, bounded lifecycle actions. | Activity/browsing history or live surveillance. |
| Device detail | Present one authorized record and actions. | Current evidence state, reverify/reinstall/replace/unlink/delete/remove separation. | Saved device equals protected. |
| Help/troubleshooting | Resolve the current issue. | State-specific explanation, one safe next action, changed-evidence retry, removal/exit. | Generic loops or speculative fixes. |
| Status/outage | Explain service/provider condition. | What is unavailable, what remains available, current protection uncertainty where relevant. | Outage automatically means protected/unprotected beyond evidence. |
| Privacy/account settings | Explain data/lifecycle at approved claim level. | Minimisation/no-history boundary; exact delete/unlink/account consequences. | Absolute no-data/legal-compliance claims. |

This single verbal system is shared across public website, accountless product, optional account/dashboard, help and status surfaces while allowing each surface to retain its distinct purpose under REQ-0026 and INT-0008.

## 16. Deterministic ACC-0299 assertions

A current independent review must be able to prove all of the following from this artifact and current authority:

1. Parent-facing language is plain, calm, child-aware and non-alarmist.
2. Technical infrastructure is secondary to the parent job and appears only where needed.
3. Current Version-1 dual-mode scope is explicit: complete accountless core plus optional parent account/dashboard/device management.
4. No mandatory login for core setup, verification, troubleshooting, removal or recovery is introduced by copy.
5. Optional sign-in is described as continuity/device management, never stronger protection.
6. Anonymous J0/J1 state is not described as automatically imported, linked, promoted or extended by sign-in.
7. Current TSK-0320 S1–S6 primary/supporting language is preserved without a competing state vocabulary.
8. Account ownership, dashboard presence and device records never imply technical verification.
9. No browsing/query/activity-history, child-account/profile or broad DNS-admin proposition is introduced.
10. Start over, logout, unlink/revoke, device-record deletion, account deletion and physical DNS removal have distinct consequence language.
11. Unknown destructive/ownership-changing outcomes use reconciliation/uncertainty copy, not optimistic success or blind retry.
12. Public, accountless-product, account/dashboard, help and status surfaces all derive from one coherent verbal system while retaining distinct jobs.
13. Reusable CTA language exists for every critical current IA branch, including Finish without account and Continue without account.
14. Provider outage/session-expiry copy preserves accountless help/removal availability and does not change protection truth by inference.
15. Claims remain evidence-matched, non-surveillance and free of complete-safety, false-verification, absolute-privacy, unsupported legal/readiness or fabricated support promises.
16. English/Turkish/Arabic+RTL localization rules preserve evidence strength, actor, scope, optionality and destructive-operation object semantics.
17. Language availability is not presented as official non-UK market/legal/support readiness.
18. `RSK-0002` and the lack of pre-L8 representative-parent comprehension evidence remain explicit.
19. No deferred legal/privacy completion, provider acceptance, implementation, publication, payment, market or launch PASS is inferred.
20. TSK-0301 remains independently dependent on both TSK-0302 and current TSK-0299; no successor becomes PASS merely because this candidate exists.

## 17. Successor impact and non-inference

Current relationship/WBS authority makes TSK-0301 the direct successor of TSK-0299, with a second hard dependency on TSK-0302. This candidate does not satisfy TSK-0301 unless and until TSK-0299 receives durable current PASS and TSK-0302 independently satisfies its own current acceptance.

Historical TSK-0299 evidence remains useful for compatible tone/voice/claim principles only. The historical account-exclusion rule and stale protection-state labels cannot satisfy current acceptance where they conflict with this current dual-mode contract or TSK-0320.

This artifact does **not** make LG-06 or any successor/gate PASS; does not authorize implementation/build, provider integration, public publication, participant activation, payment, named-market activation or launch; and does not establish real-parent comprehension or deferred legal/privacy completion.

**TSK-0299 remains non-PASS until independent verification, durable evidence publication, runtime synchronization and exact GitHub read-back succeed.**
