# TSK-0628 — No-Routine-Human-Support Operating Model

**Task:** `TSK-0628 — Define the no-routine-human-support operating model across setup, verification, troubleshooting, recovery, removal, and lifecycle events`  
**Acceptance:** `ACC-0628`  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Action authority:** `AUTO_ALLOWED`  
**Status:** **PROVISIONAL INTERNAL L4 OPERATING MODEL / IMPLEMENTATION AND PUBLIC USE NOT AUTHORIZED**  
**Date:** 2026-08-29

## 1. Operating objective

UseSafeWeb's current accountless first-phone product is designed so that **ordinary supported problems do not depend on a staffed customer-support interaction**. The default sequence is:

`prevent → automatically check → show the truthful state → give issue-specific in-product help → offer bounded AI assistance where useful → recover/remove safely`

A human route exists only for an exceptional condition whose authority, risk or required external action cannot safely be handled by the ordinary self-service system.

This model implements the existing `EXC-0008` boundary; it does **not** activate a staffed support team, ticketing SLA, chat queue, account system or persistent customer identity.

`RSK-0002` remains OPEN: current evidence does not prove representative parents can self-serve successfully or that support burden will be low in real use. This is a testable operating design, not a behavioral result.

## 2. Governing invariants

1. **Accountless ordinary support.** No login, parent/child name, email, phone number, account recovery or persistent support identity is required for routine help.
2. **No hidden human completion.** A flow is not classified as automatically/self-service resolved when an operator, owner or support person materially completed the user's ordinary task behind the scenes.
3. **Classify before remedy.** Reuse TSK-0042 issue classes and TSK-0319 decision trees; no generic unlimited `Try again` loop.
4. **Evidence before green state.** Parent confirmation, setting/profile presence, AI interpretation or help completion cannot create TSK-0320 `Verified` without the approved technical evidence.
5. **Privacy-minimal by default.** Routine help uses current state/configuration, synthetic checks and non-identifying service health. It does not request browsing/query history, raw DNS logs, credentials, device fingerprints or unrestricted diagnostic dumps.
6. **Changed-condition retry only.** A retry is allowed after new evidence, configuration change, recovered service state or another materially changed condition.
7. **Recovery is first-class.** When a supported repair cannot be established, the product offers truthful `Status uncertain`/`Not covered` and safe removal/recovery rather than progressively invasive troubleshooting.
8. **Do not weaken unrelated controls.** Work/school/security VPNs, device-management restrictions and privacy/security controls are not disabled merely to make UseSafeWeb appear successful.
9. **AI is an assistance layer, not authority.** AI can explain the current approved branch and select from approved help content; it cannot invent a new supported method, alter filtering/service configuration, authorize exceptional diagnostics, claim technical verification or silently escalate scope.
10. **Human escalation is exceptional and explicit.** The reason and owning route must be known; “contact support” is not the default fallback for an ordinary issue.
11. **No public response-time promise.** Current authority defines deterministic product/system response behavior only; staffed-human SLAs remain unapproved.
12. **No behavioral success claim.** Real-parent completion/support-burden outcomes remain deferred under CR-0003/RSK-0002.

## 3. Support layers and allowed responsibilities

| Layer | What it may do | What it may not do |
| --- | --- | --- |
| **Prevention** | Route only supported tuples; use current source-backed instructions; show limitations before action; avoid unnecessary fields/choices; detect stale content triggers. | Hide unsupported states, overclaim universality, or add friction solely to collect data. |
| **Automatic checks** | Use TSK-0319 privacy-safe service-health, support-tuple, DNS-path, filter, conflict, recovery and journey-state checks where implementation later permits. | Inspect browsing history, infer identity, bypass platform security, or convert uncertainty into `Verified`. |
| **In-product help** | Show one issue-specific decision tree/next action tied to current state and current source version. | Present generic endless retry lists or a second independent support/instruction authority. |
| **AI assistance** | Explain approved instructions/states in plain language; ask only the minimum non-sensitive fact needed to choose an existing branch; summarize why a condition is uncertain/not covered; point to approved reset/remove/help. | Invent instructions, ask for credentials/raw history, claim remote device access, mutate DNS/admin state, provide unsupported security-control bypasses, or self-approve exceptional collection/changes. |
| **Recovery/removal** | Clear transient journey state; guide exact Android/iPhone removal; withdraw protection claim; run neutral recovery check. | Treat website reset as device removal or claim UseSafeWeb protection after removal. |
| **Exceptional human/owner/operator** | Handle governed security/privacy/safeguarding incidents, managed-admin boundary, service/configuration changes, authorized false-positive change, exceptional diagnostics or material source/legal/authority decisions. | Become the routine completion path for ordinary supported setup or troubleshooting. |

## 4. Ordinary-issue operating matrix

| Issue class | Prevention | Automatic check | In-product help | AI assistance | Recovery/removal | Human route? |
| --- | --- | --- | --- | --- | --- | --- |
| `SETUP` — supported Android/iPhone step cannot be completed | Route exact current platform; present current TSK-0307 instruction and known limits. | `CHK-SVC-HEALTH`, `CHK-SUPPORT-TUPLE`, then relevant path check. | TSK-0319 Android/iPhone setup tree with one changed-condition retry. | Explain exact field/action and why a state remains unverified; may distinguish hostname vs URL semantics. | If no safe repair remains, guide exact platform removal/recovery. | **No** for ordinary current supported problem. Exceptional only if managed/admin/security boundary applies. |
| `JOURNEY_STATE` — browser/session lost or transient state invalid | Keep J0 default; J1 only under TSK-0229 necessity/expiry rules. | `CHK-JOURNEY-STATE`. | Resume valid state or restart required step; explain web reset vs device configuration. | Explain why restart is required; no identity recovery. | Clear J0/J1 and restart; device removal only if separately requested/needed. | **No**. Persistent recovery need is evidence for EXC-0001 owner review, not routine support. |
| `DNS_REACHABILITY` | Verify support tuple and show known network/transport limits before repeated device changes. | `CHK-SVC-HEALTH` before device troubleshooting; then `CHK-DNS-PATH`. | Issue-specific Android/iPhone/network path; one repair/recheck. | Explain whether evidence points to service, device, network or unresolved cause without pretending certainty. | Safe removal if intended path cannot be restored. | **No** unless service/operator incident or exceptional diagnostics boundary is reached. |
| `FILTERING_FALSE_POSITIVE` | Conservative versioned filter policy and narrow reversible exception process. | Reproduce with synthetic/non-participant evidence and confirm causality where possible. | Explain current state and safe temporary/user-side next step; do not disable filtering broadly. | Collect/structure only the minimum symptom needed to select approved false-positive process; no history request. | If no safe exception is justified, keep truthful limitation/action-needed state. | **Yes, exceptional operator/change route** when a global filtering exception/change is actually justified; governed change + regression proof required. |
| `COMPATIBILITY_CONFLICT` — VPN/Private Relay/custom DNS/captive portal/managed device | Current support matrix and pre-setup limitation disclosure. | `CHK-SUPPORT-TUPLE`, `CHK-CONFLICT` where non-invasive evidence exists. | Show exact known conflict/uncertain/not-covered branch; never invent coexistence. | Explain why a competing resolver/tunnel can prevent a trustworthy result and what approved options exist. | Removal/recovery if UseSafeWeb configuration impairs ordinary connectivity. | **No** for ordinary unsupported/uncertain result. **Yes** only for managed-device administrator action outside user's authority or a security/privacy incident. |
| `REMOVAL_RECOVERY` | Removal link remains reachable from setup/help/Protection Map; consequence stated before action. | `CHK-RECOVERY` after exact platform removal. | Android/iPhone removal tree and post-removal result. | Explain distinction between removed UseSafeWeb protection and restored ordinary connectivity. | Exact platform reset + neutral connectivity check. | **No** unless external management prevents removal or a platform/service defect requires operator action. |
| `STALE_GUIDANCE` | Every instruction has source/version owner and review trigger. | Detect known source/version mismatch where possible; otherwise content review trigger. | Stop serving affected step as current; route `Not covered`/`Status uncertain` and stable reference. | Explain that instruction is withheld because current source support cannot be confirmed; no guessed menu path. | Use only still-current removal/recovery path. | **Yes, bounded content/technical owner review** to re-verify and republish guidance; not a customer-support completion route. |
| `SERVICE_OUTAGE` | Service health and certificate/renewal controls monitored under existing infrastructure evidence. | `CHK-SVC-HEALTH` before device changes. | State service issue/uncertainty; do not tell user to repeatedly reconfigure. | Explain that device troubleshooting is paused while the service condition is unresolved. | Offer removal/recovery if the user needs ordinary connectivity. | **Yes, operator incident route** for infrastructure repair; user remains self-service informed. |
| `GUIDANCE` | Public How-it-works/Compatibility/Privacy and Protection Map use bounded claims. | Usually none. | Source-backed explanation of current coverage/limits. | Explain layers/states and direct to the exact product/help route. | Not normally required. | **No** unless question requires unresolved legal/safeguarding authority. |
| `OTHER/unsupported` | Do not silently widen current scope. | Establish only minimum support facts. | State unsupported/unknown outcome and safe exit. | Explain why no supported branch can be offered without inventing capability. | Remove partial UseSafeWeb configuration if present. | **No routine human completion.** Route to product evidence backlog only if the pattern later becomes material. |

## 5. Exceptional routes

These routes are outside ordinary self-service. They are bounded by owning authority and must never be counted as routine automation success.

| Exceptional condition | Required route | User-facing behavior | Hard boundary |
| --- | --- | --- | --- |
| Suspected privacy/security deviation, secret exposure, prohibited persistence or unsafe diagnostics | Security/privacy incident owner | Stop affected path; present safe next action/removal where possible. | Technical symptom resolution does not close unresolved privacy/security incident. |
| Safeguarding disclosure/concern or immediate danger | Dedicated safeguarding procedure / appropriate emergency direction | Exit product troubleshooting; do not interrogate disclosure through ordinary AI support. | Personal/raw disclosure stays out of GitHub/general analytics. |
| Service-wide outage/certificate/infrastructure fault | Existing operator/runbook path | Show service issue/uncertainty; avoid device-change loop; removal available. | Operator repair is infrastructure operation, not “human customer support.” |
| Managed device/network blocks required change and user lacks authority | Legitimate external device/network administrator | State current UseSafeWeb path is not self-service supported. | Never advise bypassing employer/school/security management. |
| Global filtering false positive requiring approved configuration exception | Governed filtering/change owner | Preserve truthful state until change independently verifies. | Narrow reversible change + allowed/blocked regression; no personalized dashboard/allowlist. |
| Exceptional request-level/identifiable diagnostics genuinely necessary | Separately governed diagnostic procedure | Explain necessity/notice where applicable; continue only after required authority. | Fixed scope/time/fields/access/deletion; never routine; no raw dataset in GitHub. |
| Current instruction/source is materially stale or contradictory | Content + technical source owner | Withhold affected instruction and show uncertainty/not-covered. | Re-publication only after source/applicability re-verification. |
| Material legal/policy/scope question | Owning legal/Project Owner authority | Do not improvise a legal conclusion or broaden product scope. | `REQ-0022` and other current legal fences remain unchanged. |

## 6. AI-assistance contract

AI assistance is optional and subordinate to the deterministic product/help system. It may improve comprehension without creating a second support authority.

### Allowed

- identify the current issue class from the user's current product step and minimum stated symptom;
- explain an approved TSK-0307 instruction or TSK-0319 decision-tree branch in simpler language without changing technical meaning;
- ask one minimum routing question when the branch cannot otherwise be established;
- explain TSK-0320 state/limitation and why evidence is insufficient for `Verified`;
- guide the user to Start over, current Help, exact removal or recovery flow;
- surface the correct exceptional route when a predefined exceptional criterion is met.

### Prohibited

- claiming it inspected or changed a phone/network when it did not;
- silently handing the case to a human while reporting automated resolution;
- requesting passwords, Apple/Google credentials, DNS query history, browsing history, raw logs, device serial/fingerprint or unrelated personal information;
- inventing an alternate DNS/VPN/profile path outside the accepted support matrix;
- generating a new `.mobileconfig` or changing production filtering/service/admin configuration from an ordinary support conversation;
- declaring `Verified` from user wording, profile presence or AI confidence;
- overriding security/privacy/safeguarding/legal escalation rules;
- fabricating response-time promises or account-based case continuity.

If AI cannot select a safe approved branch, it returns the truthful unresolved state and the exact allowed next path; it does not improvise.

## 7. Point-of-need help placement

The product should expose help at the point where it can prevent unnecessary escalation:

- **Router:** unsupported/unknown device or missing support fact.
- **Native safeguard:** setting unavailable/already configured/unsupported.
- **Android/iPhone DNS setup:** input/profile/OS-management problem.
- **Verification:** service health, path/filter result, conflict/uncertainty.
- **Protection Map:** explain state and one next action for each non-green item.
- **Removal:** exact platform removal and consequence.
- **Post-removal:** ordinary connectivity still failed/uncertain.
- **Stale instruction:** current guidance intentionally withheld pending re-verification.

Help must preserve the current task context without requiring a support case or account.

## 8. Lifecycle-event support model

Routine support must also remain self-service during expected lifecycle changes:

| Lifecycle event | System/product response | Human/operator role |
| --- | --- | --- |
| Platform OS/settings/source change | Trigger TSK-0307/TSK-0559 review; stop stale affected instruction; show uncertainty/not-covered. | Content/technical owner re-verifies source and republishes eligible content. |
| UseSafeWeb endpoint/profile/support change | Invalidate affected instruction/verification assumptions and route current users to safe state/recovery. | Governed technical/product change process; no silent customer-facing drift. |
| Certificate renewal/expiry problem | Service-health/verification cannot remain green; show service issue and removal if needed. | Existing certificate runbook/monitoring owns repair. |
| Filtering policy change/false-positive correction | Re-test synthetic allowed/blocked behavior before restored green claim. | Governed narrow change owner only where required. |
| Accountless J0/J1 expiry/deletion | Restart/resume deterministically under TSK-0229; no identity recovery. | None ordinarily. |
| Content/localization source drift | Affected locale/source entry becomes review-needed; fall back only under TSK-0311 critical-copy rules. | Qualified content/technical/language review before publication eligibility. |
| User chooses removal/exit | Exact removal + neutral recovery check + protection claim withdrawn. | None ordinarily. |

## 9. Resolution and measurement semantics

These are definitions for later approved measurement; they do not activate telemetry or participant collection.

- **Prevented:** user never enters the failure branch because current routing/content blocks the invalid action.
- **Automatically checked:** a privacy-safe system check returns a usable result without human intervention.
- **Self-service resolved:** the parent completes the supported remedy/recovery using product/help/optional AI only; no hidden operator action materially completes the task.
- **AI-assisted self-service:** AI explains/selects an already-approved branch but no human/operator completes the ordinary task.
- **Exceptional human/operator route:** predefined exceptional criterion requires an owner/operator/qualified human/external administrator; excluded from automated/self-service resolution numerator.
- **Unresolved:** no safe supported resolution is established; product returns truthful uncertain/not-covered/action-needed/removal state.

If later measurement is authorized, denominators must include all eligible issue occurrences, not only completed ones, and human-assisted cases must remain separately visible. No individual journey history is needed for this design to be valid.

## 10. Failure/circuit-breaker contract

An ordinary issue stops self-service retry when any of the following is true:

1. the same check/remedy failed again without a materially changed condition;
2. support tuple is unsupported/not covered;
3. effective resolver/coverage remains uncertain after the accepted check;
4. service outage or stale guidance makes device action inappropriate;
5. a privacy/security/safeguarding/legal/managed-admin exceptional criterion is met;
6. the next diagnostic would exceed the routine privacy-minimal boundary;
7. the only remaining action would weaken an unrelated security/privacy control;
8. the only remaining action is an operator/configuration change outside ordinary user authority.

The product then selects exactly one truthful outcome: `Action needed`, `Status uncertain`, `Not covered`, safe removal/recovery, or the named exceptional route.

## 11. Testable acceptance assertions

A later implementation/operating rehearsal must be able to prove at least:

1. Every TSK-0042 ordinary issue class maps to prevention, automatic check, in-product help, optional bounded AI assistance, recovery/removal, or a truthful unsupported endpoint.
2. No ordinary supported setup/verification/removal flow requires a human support contact, login, email or phone number.
3. Service health is checked before repeated device reconfiguration when service failure could explain the symptom.
4. Setting/profile presence and parent/AI confirmation cannot create `Verified`.
5. Equivalent retries are blocked unless evidence/condition changes.
6. Routine diagnostics never request browsing/query history, credentials or raw DNS logs.
7. Website journey reset is not represented as device DNS/profile removal.
8. Android and iPhone removal flows withdraw the protection claim and run/offer neutral recovery confirmation.
9. VPN/Private Relay/managed-device uncertainty does not trigger advice to defeat unrelated controls.
10. AI output is constrained to approved support/instruction/state branches and cannot mutate production/admin state.
11. Exceptional human/operator routes are named, criterion-driven and excluded from the self-service-success numerator.
12. No routine staffed-support response-time SLA is exposed.
13. Stale guidance is withdrawn/marked uncertain until source review completes.
14. Safeguarding/privacy/security conditions leave the ordinary troubleshooting path.
15. Removal/exit remains possible from supported failure states without account creation.
16. Any later support-burden measurement preserves denominator, hidden-human and privacy constraints.

## 12. Current bounded result

The current L4 operating model covers setup, verification, troubleshooting, recovery, removal and expected lifecycle events with no routine human-support dependency. All top ordinary issue classes have a prevention/check/help/AI/recovery path or a truthful unsupported endpoint, while human involvement is reserved for explicit exceptional authority/risk conditions.

This artifact does **not** prove real-parent self-service performance, implement in-product checks/help/AI, activate telemetry, establish staffed support, authorize diagnostics collection, process participants, publish the product, or authorize launch.