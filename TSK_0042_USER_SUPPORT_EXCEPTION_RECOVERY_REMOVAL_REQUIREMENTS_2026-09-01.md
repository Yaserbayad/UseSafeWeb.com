# TSK-0042 — User Support, Exception, Recovery, and Removal Requirements

**Task:** TSK-0042 — Specify user support, exception, recovery, and removal requirements  
**Acceptance:** ACC-0042 / VER-0042 / EVD-0042  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Version:** 1.0.0-post-CR-0008  
**Date:** 2026-09-01  
**Authority:** current CR-0008 / DEC-0055 owner-frozen modular Master Planning System; current TSK-0041 DNS activation requirements; current TSK-0146 Version-1 dual-mode baseline; current TSK-0320 protection-state truth model; current TSK-0628 no-routine-human-support operating model; current TSK-0498 privacy-safe event contract.  
**Action authority:** A3 / AUTO_ALLOWED.  
**Hard dependencies:** current TSK-0041 PASS; current TSK-0146 PASS.  
**Controls:** REQ-0001; REQ-0002; CON-0020; CON-0021; RSK-0044; INT-0001; INT-0002.  
**Status:** current L4 requirements-freeze candidate only; support implementation, staffing, human response capacity, LG-07, build, production activation, launch, and real-user supportability are not inferred.

## 1. Purpose and boundary

UseSafeWeb support exists to help a parent reach or restore a truthful, safe product state with the least necessary intervention and data. The support model is **self-service first and no-routine-human-support by design**, consistent with current TSK-0628. Ordinary accountless setup, optional sign-in/session/dashboard/device management, verification, recovery, deletion, unlink/revoke, and DNS removal issues must have bounded product/self-service routes wherever the current product supports them.

Human involvement is an **exceptional bounded route**, not the default operating model. It is permitted only when one of the following is true:

1. current self-service cannot safely resolve the issue and escalation is explicitly supported;
2. an actual human/provider/professional/legal/identity authority is required for the specific act;
3. a security/privacy/safety concern requires controlled human review under its owning procedure;
4. an unresolved incident needs evidence that cannot be safely obtained or acted on automatically under current authority.

TSK-0042 does not invent a support team, staffed hours, guaranteed response time, legal advice service, remote device-control service, or unrestricted DNS administration surface. It does not authorize an operator or AI to act beyond current Action Authority.

The complete core support journey remains usable without login. Optional parent account/dashboard/device-management state may support continuity for separately approved account/device functions but cannot strengthen technical protection evidence or become mandatory for core DNS setup, verification, recovery, or removal.

## 2. Support outcome contract

Every support interaction must end in one truthful bounded disposition:

- `resolved_self_service` — the applicable supported issue is resolved through the approved route and any required technical state is re-evaluated;
- `action_remaining` — a concrete safe next action is known but not yet completed;
- `not_covered` — the exact device/path/capability is currently outside approved support;
- `uncertain_error` — current evidence is missing, stale, contradictory, unavailable, or insufficient to classify safely;
- `removed` — evidence establishes removal/revocation of the relevant UseSafeWeb mechanism/scope;
- `exception_escalation` — a bounded exceptional escalation is required; this is not a promise that a human response has occurred or will occur within an invented SLA.

A support-flow completion is not itself technical protection verification. The user-visible Protection Map remains governed by current TSK-0320.

## 3. Protection-state incident routing

Support must preserve the six canonical evidence states:

| Current state | Support meaning | Required support behavior |
|---|---|---|
| `protected_verified` | Fresh qualifying technical evidence currently proves the declared protection scope. | Preserve only while evidence remains fresh and uncontradicted. If the issue changes the relevant context, require re-verification before retaining this state. |
| `configured_parent_confirmed` | Setup/configuration or parent confirmation exists without qualifying technical verification. | Explain that setup is confirmed but protection has not been technically verified; provide verification or supported next action where available. |
| `action_needed` | A current known safe corrective/setup action is required. | Show one bounded next action, then re-evaluate; do not cosmetically convert failure to unsupported or verified. |
| `not_covered` | Current authoritative support/coverage says the path is unsupported/out of scope. | State the limitation and any approved safe alternative/next step; do not invent a fallback mechanism. |
| `uncertain_error` | Current status cannot be classified safely. | Preserve uncertainty prominently, offer bounded diagnostic/retry/recovery steps, and never retain stale positive assurance. |
| `removed` | Evidence establishes removal/revocation for the relevant scope. | State that the relevant UseSafeWeb setup is removed; a later account/device record or parent confirmation cannot restore protection. |

Configuration/profile/ClientID presence, parent confirmation, account ownership, dashboard/device registration, stored status, journey completion, or support-case closure **never creates `protected_verified`**. Fresh qualifying technical evidence is still required.

## 4. Incident taxonomy and required handling

### SUP-01 — Setup help

Use only current supported platform/version/mechanism guidance from the accepted routing/support catalogue.

Requirements:

- route to the exact current mechanism rather than a generic or similar older-version path;
- recognize already-configured state and avoid redundant destructive setup;
- distinguish parent/configuration confirmation from technical verification;
- do not force an unsupported app/VPN/browser fallback;
- do not tell a parent to weaken employer, school, device-management, security, or privacy controls merely to produce a green state;
- stale or unclassified instructions must fail to `uncertain_error`/review rather than be guessed;
- after a material DNS/resolver/network/profile change, require the verification contract that applies to the affected scope.

### SUP-02 — Configuration present but protection not technically verified

Treat this as `configured_parent_confirmed` unless stronger current evidence requires another state.

Support copy must communicate both facts: setup appears/was confirmed, and UseSafeWeb has not technically verified protection. Offer the current technical check where available. An unavailable verifier is not proof of failure or success.

### SUP-03 — Verification negative with known remedy

Use `action_needed` when current reliable evidence identifies a concrete safe remedy. Provide the narrow action and recheck rule. Do not loop the same failed verification without a changed condition or new evidence.

### SUP-04 — Unsupported / not-covered state

`not_covered` is a truthful product result, not a cosmetic failure state.

Requirements:

- identify the bounded unsupported scope/reason category;
- show an approved safe native alternative only if one already exists in current authority;
- do not fabricate a workaround or imply another protection layer compensates unless separately proven;
- a newly released, unknown, vendor-modified, managed, or unclassified path remains `not_covered` or `uncertain_error` according to current support evidence.

### SUP-05 — Uncertain/error/stale/bypass state

Use `uncertain_error` where the effective path is indeterminate, the verifier errors/times out, current guidance is stale, or VPN/Private Relay/browser/app/captive-portal/network changes invalidate prior proof.

Support may request only the minimum bounded facts needed to select a safe next step. Prior `protected_verified` evidence may not remain visible as current assurance when its relevant scope is materially uncertain.

### SUP-06 — Service/endpoint incident

Distinguish a service-side incident from local setup failure when current evidence permits. Prefer synthetic service probes and aggregate operational evidence over user DNS activity. Do not ask parents to generate routine browsing/query history for diagnosis.

If service health is unresolved, present `action_needed` or `uncertain_error` according to the owning state contract and provide safe retry/recovery/removal options.

### SUP-07 — False positive / required service blocked

A false-positive report must not become a route to blanket filtering disablement or browsing-history collection.

Required workflow:

1. accept the bounded symptom/required service needed to understand the specific incident;
2. determine whether the issue is within current support scope;
3. reproduce with synthetic/non-participant evidence where reasonably possible;
4. establish whether UseSafeWeb filtering is actually causal rather than the site/app, upstream, device, browser, VPN, network, or another control;
5. if a correction is justified, use the **narrowest safe explicit reversible exception** under the owning configuration/change authority;
6. re-test the legitimate path and a relevant blocked regression before treating the correction as successful;
7. record the configuration/evidence change through the owning auditable process;
8. keep unresolved impact as `action_needed`, `uncertain_error`, or `not_covered`, never `protected_verified` by convenience.

A parent-provided domain/service identifier may be processed only as purpose-limited incident input when necessary to resolve that specific case. It must not be copied into product analytics, browsing/DNS history, engagement data, or a persistent child/family profile. Retain only as long as the separately authorized support/evidence/security purpose requires; delete earlier when no longer needed. TSK-0042 does not invent a legal retention period.

TSK-0042 creates **no persistent per-parent/per-device personal DNS allowlist** and no unrestricted/raw AdGuard administration surface. Any future individualized exception product requires separate product/privacy/security/architecture authority.

### SUP-08 — Optional account/session/dashboard/device-record issue

Support may help with separately approved sign-in/session/dashboard/device-management functions without making account access a prerequisite for core safety setup/support.

Account ownership or a saved device record never verifies DNS protection. Account/device records, anonymous journey state, support-case state, and physical DNS configuration remain separate domains.

### SUP-09 — Delete / unlink / revoke

The product must identify exactly what is being deleted or revoked and prove completion for that target. See Section 8. A successful account/device-record deletion must not claim physical DNS removal; physical DNS removal must not imply account deletion.

### SUP-10 — Security/privacy/safety concern

Do not expand routine support diagnostics. Route to the separately governed security/privacy/safety incident or disclosure process when its trigger is met. Preserve minimum necessary evidence, access control, auditability, and deletion requirements. Do not fabricate professional/legal conclusions or human review that has not occurred.

## 5. Diagnostic minimisation hierarchy

Support diagnostics must use the least intrusive level that can safely answer the incident question.

### D0 — No-data self-service

Use current instructions, local state, user-visible reason codes, and safe recovery/removal guidance without transmitting additional diagnostic content where possible.

### D1 — Bounded state metadata

Where necessary, allow only bounded diagnostic facts such as:

- coarse supported platform family and exact/current version where required for compatibility;
- approved mechanism/profile/instruction version;
- canonical Protection Map state and bounded reason code;
- technical verifier ID/version and result class (`positive`, `negative`, `indeterminate`, `error`) where a verifier actually ran;
- coarse network/context class needed for the supported matrix;
- bounded indication that a VPN/Private Relay/browser/app resolver conflict is present or unknown;
- event/observation time required for staleness/recovery reasoning.

Do not convert these fields into persistent identity analytics.

### D2 — Synthetic verification/probes

Prefer controlled synthetic DNS/filtering checks and synthetic service probes that demonstrate the technical condition without collecting real browsing activity.

### D3 — Exceptional request-level diagnostics

Request-level diagnostics are **not a routine support feature**. They may be used only through the separately governed exceptional diagnostic procedure when genuinely necessary and authorized. They must be purpose-limited, time-boxed/minimized, access-controlled, and deleted under that procedure.

### Prohibited routine support/analytics data

Do not collect or retain for routine support/analytics:

- DNS questions/query history, browsing history, visited/top domains, URLs/page contents, search terms, or child activity;
- identifiable per-client DNS statistics, client IP as analytics identity, MAC/serial/ad ID/fingerprint;
- child name/account/profile, messages, contacts, photos, location, social content;
- account ID/email/provider subject as an analytics join key;
- free-text support/search contents in product analytics;
- full referrer URLs, arbitrary campaign strings, arbitrary error bodies/stacks/request bodies;
- secrets, tokens, cookies, credentials, authorization headers, private keys.

Operational incident evidence and product analytics are separate. Minimum content that is genuinely required to resolve a specific support case may exist inside the bounded case/evidence process; it must not become a backdoor analytics or DNS-history store.

## 6. Response expectations

TSK-0042 does **not** invent a human service-level agreement.

The product/self-service surface must provide, in the same interaction where reasonably possible:

1. the current truthful state/reason class;
2. one bounded next action, safe retry condition, explicit unsupported result, or escalation state;
3. the consequence of removal/recovery where relevant;
4. visible uncertainty when the current state cannot be proven.

Requirements:

- retries occur only after a changed condition, new evidence, or a materially different corrective action;
- an unresolved issue remains unresolved; silence/abandonment is not resolution;
- exceptional escalation may state only the currently established channel/process. It may not promise “response within X hours/days,” staffed availability, or guaranteed resolution unless a separately accepted service contract proves it;
- a human/provider action cannot be represented as completed before evidence exists;
- support must not block safe removal merely to preserve product retention.

## 7. Escalation contract

Escalation is permitted only when a specific trigger and receiving authority exist. The escalation record must identify:

- bounded issue category and current state;
- why self-service cannot safely complete the next action;
- minimum evidence reference, not unnecessary raw payload;
- required receiving role/process/provider, if one is actually defined;
- any time-sensitive safety/security condition already established by authority;
- exact follow-up check that determines whether the escalation resolved the issue.

If no valid receiving process exists, the product must say the issue is unresolved/unsupported rather than inventing a human queue.

AI/operator actions remain bounded by RSK-0044 and the current action-authority matrix. A support requirement cannot authorize an effectful act that otherwise requires human approval or human-only authority.

## 8. Deletion, unlink, revoke, and physical removal are distinct

The following operations must never be conflated:

1. **Anonymous journey deletion** — removes the approved short-lived accountless journey state according to its owning data contract.
2. **Support-case data deletion** — removes case-specific data/evidence under its owning retention/evidence rules.
3. **Account deletion** — deletes the approved persistent parent account identity/session domain according to its owning lifecycle.
4. **Saved device-record deletion** — removes the dashboard/device ownership/management record; it does not prove physical device configuration changed.
5. **Dashboard unlink/revoke** — removes the approved management/authorization relationship; it is not DNS removal evidence.
6. **Physical UseSafeWeb DNS removal/reset** — removes/resets the approved DNS configuration/profile/provider on the actual target scope and requires evidence appropriate to that mechanism.

Completion must be target-specific and evidence-backed. One operation never silently implies another.

A DNS `removed` state is allowed only when current evidence establishes removal/revocation for the relevant DNS mechanism/scope. Account deletion, dashboard unlink, saved-record deletion, parent confirmation, or expired analytics state cannot by themselves create DNS `removed`.

After physical DNS removal/recovery, normal platform/network DNS functionality should be checked using neutral/synthetic evidence where appropriate. Do not retain a UseSafeWeb protection claim after evidence-backed removal.

## 9. Recovery requirements

Recovery must be safe, reversible, evidence-driven, and bounded to the failed scope.

Requirements:

- identify whether the issue is configuration, verifier, network/browser/VPN/app conflict, service health, unsupported path, false positive, or account/dashboard lifecycle issue before applying a corrective action where possible;
- prefer the smallest reversible correction;
- do not blind-retry materially equivalent failed operations;
- rerun/re-evaluate after a changed condition/new evidence;
- after a material DNS/resolver/profile/network change, fresh verification is required before restoring `protected_verified`;
- if recovery is partial, contradictory, or indeterminate, use `uncertain_error` or `action_needed` rather than stale success;
- preserve unrelated independently proven safeguards/layers rather than globally downgrading them without evidence;
- keep a supported removal/reset path available when safe continuation is unavailable;
- rollback/recovery evidence must remain attributable, auditable, and recoverable under CON-0020.

## 10. Support-burden measurement contract

Support-burden metrics must use the **existing TSK-0498 event vocabulary only**. TSK-0042 introduces no analytics event or property.

Every metric must state source, formula/numerator, denominator, time window/release/cohort as applicable, owner, guardrail, action, and missing-data treatment before decision use. Unknown/missing telemetry is never imputed as success.

### SB-01 — Self-service usage rate

- **Source:** `self_service_opened`.
- **Numerator:** valid deduplicated self-service opens in the chosen window.
- **Denominator:** valid accountless journey sessions in that window, exactly as permitted by TSK-0498.
- **Owner:** Product Analytics / Customer Experience.
- **Guardrail/action:** a rise is not automatically good or bad; inspect topic mix and outcomes before changing guidance.
- **Missing data:** blocked/missing telemetry is reported separately.

### SB-02 — Self-service reported resolution rate

- **Source:** `self_service_outcome` linked to corresponding `self_service_opened` within the approved short-lived accountless session.
- **Numerator:** `outcome=resolved_reported`.
- **Denominator:** corresponding valid opens for the same `topic_id`/release/window.
- **Owner:** Product Analytics / Customer Experience.
- **Guardrail/action:** this is parent-reported self-service outcome, not technical protection verification.
- **Missing data:** no outcome before session expiry is missing/abandoned according to TSK-0498, never resolved.

### SB-03 — Self-service unresolved/escalated rate

- **Source:** `self_service_outcome`.
- **Numerator:** bounded outcomes `unresolved_reported` and/or `escalated`, reported separately and optionally combined only with an explicit formula.
- **Denominator:** corresponding valid `self_service_opened` events.
- **Owner:** Product Analytics / Customer Experience.
- **Guardrail/action:** repeated high unresolved/escalated rates for one approved topic trigger content/routing/recovery review; they do not authorize new personal data collection.

### SB-04 — Not-covered and uncertain/error state rates

- **Source:** `protection_state_evaluated`.
- **Numerator:** exact state `not_covered` or `uncertain_error`, reported separately by bounded layer/reason/release dimensions.
- **Denominator:** all valid evaluations for the applicable layer/release/cohort/window.
- **Owner:** Product Analytics / Product / Privacy Engineering.
- **Guardrail/action:** use to identify support/compatibility friction; never reclassify states to improve the metric.

### SB-05 — Technical verification negative/indeterminate/error rate

- **Source:** `protection_verification_outcome`.
- **Numerator:** exact bounded result class `negative`, `indeterminate`, or `error`, each reported separately unless an explicit decision formula combines them.
- **Denominator:** valid technical verification attempts for the same verifier/scope class/release/window.
- **Owner:** Product Analytics / Network Engineering.
- **Guardrail/action:** parent/configuration confirmation cannot appear as positive technical verification.

### SB-06 — Governed operational recovery outcome rate

- **Source:** `recovery_operation_outcome`.
- **Numerator:** bounded result (`success`, `failed`, `partial`, `rolled_back`) by governed runbook operation type.
- **Denominator:** initiated governed recovery operations of the same type/window.
- **Owner:** SRE / Operations.
- **Guardrail/action:** this is **operational recovery**, not a user-session support-resolution metric.
- **Correlation limitation:** this event intentionally has **no `journey_session_id`**. TSK-0042 therefore does not join it to individual self-service or user verification events and does not claim a per-user “recovery after failed verification” metric.

### SB-07 — Support/channel entry mix

- **Source:** `channel_entry` only where an approved bounded `source_class` legitimately represents the decision question being measured.
- **Denominator:** valid `channel_entry` events or valid accountless journey starts attributed in the same short-lived session, with the KPI stating which.
- **Owner:** Product Analytics / Growth.
- **Guardrail/action:** do not invent arbitrary referrers/UTMs or repurpose this event to encode support text.

### SB-08 — Support/operating cost input

- **Source:** `cost_period_recorded`.
- **Use:** aggregate decision-period/category cost input only.
- **Denominator:** the defined decision period, or a separately specified aggregate outcome denominator for a cost-per-outcome KPI.
- **Owner:** Project Owner / Finance / Product Analytics.
- **Guardrail/action:** never join cost to a person/session/device/account; authoritative accounting retention remains separate.

### Metrics that are **not currently computable**

If the existing event contract lacks the necessary bounded event/field/correlation, the metric must show `not currently computable` / missing-data state rather than silently adding fields. In particular, TSK-0042 does not create a per-user recovery-after-verification-failure metric because the current operational recovery event deliberately has no user journey correlation.

## 11. Data retention and case evidence

Product analytics retention remains exactly the TSK-0498 contract; TSK-0042 does not extend it:

- accountless journey/protection/self-service/channel raw events: maximum 24 hours from journey start;
- retained product aggregates: non-linkable, maximum 13 months;
- synthetic reliability raw: maximum 30 days, with non-linkable aggregate maximum 13 months;
- analytics cost projection: maximum 13 months; authoritative finance retention is separate.

Support-case evidence is not automatically product analytics. Its retention must follow the separately authorized evidence/security/legal purpose actually applicable. Do not use TSK-0042 to invent a universal calendar retention period or to preserve unnecessary domains, free text, identity, or diagnostics.

## 12. Governance and failure behavior

- **REQ-0001:** requirements and acceptance remain traceable through WBS/evidence.
- **REQ-0002 / CON-0021:** an active material scope change requires the current restart/reapproval/change-control path; do not silently broaden support scope.
- **CON-0020:** acceptance/recovery evidence must remain attributable, auditable, and recoverable.
- **RSK-0044:** AI/operator effectful actions remain within granted authority; an L4 support requirement never creates a missing approval token or human act.
- **INT-0001:** stale/invalid/unreconciled governance state stops continuation until canonical state is recovered.
- **INT-0002:** stale/divergent/unreadable repository authority fails closed before task/state mutation.

No support copy or artifact may claim a human escalation, deletion, exception, recovery, technical verification, or removal succeeded without evidence for that exact operation.

## 13. Testable examples

1. **Parent needs setup help on a currently supported Android route:** show current Private DNS hostname instructions; configuration alone yields at most `configured_parent_confirmed`; run current verifier before `protected_verified`.
2. **Profile exists but VPN/browser path is indeterminate:** route `uncertain_error`; do not preserve stale `protected_verified`; provide bounded conflict/recheck guidance.
3. **Known unsupported platform/version:** show `not_covered`; do not invent app/VPN fallback or human promise.
4. **Specific required service appears falsely blocked:** record only the minimum incident input, reproduce synthetically where possible, prove filtering causality, apply the narrowest authorized reversible exception, regression-test, and do not copy the domain into analytics.
5. **Parent deletes dashboard device record:** confirm record deletion only; DNS state remains independently evaluated.
6. **Parent removes UseSafeWeb DNS profile/provider:** verify the target configuration removal/recovery; set DNS layer `removed`; account/device records remain separate.
7. **Self-service route is abandoned:** absence of a successful outcome never counts as resolved.
8. **Operational recovery succeeds:** `recovery_operation_outcome=success` can support operational reliability metrics but cannot be joined to a user support session because the schema intentionally has no journey correlation.
9. **Exceptional issue has no valid human receiving process:** state unresolved/unsupported; do not invent a ticket queue or response SLA.
10. **Support asks for broader diagnostics merely for convenience:** reject; use D0-D2 or the separately governed exceptional diagnostic process if genuinely necessary.

## 14. Deterministic ACC-0042 assertions

TSK-0042 may be accepted only if all of the following are proven against current canonical `main`:

1. exact current WBS title/lifecycle/priority/A3/AUTO_ALLOWED/dependencies/ACC-0042/VER-0042/EVD-0042 and referenced controls are current;
2. TSK-0041 and TSK-0146 are current durable PASS;
3. setup help, false-positive incidents, unsupported-state incidents, remedies, escalation, data-minimized diagnostics, response expectations, deletion, removal, recovery, and support-burden metrics are all explicit;
4. all six current Protection Map states remain truthfully supportable and support completion/parent confirmation/account state cannot create `protected_verified`;
5. false positives require causal confirmation, narrow reversible correction and regression, never blanket filtering disablement or an invented persistent personal DNS administration surface;
6. ordinary support is self-service first/no-routine-human-support, with exceptional human escalation bounded and no fabricated staff availability/SLA;
7. D0-D3 diagnostic minimisation and prohibited routine data are explicit, including no browsing/query/activity history, child surveillance data, persistent analytics identity, secrets, arbitrary free text or backdoor DNS-history analytics;
8. anonymous journey deletion, support-case deletion, account deletion, saved device-record deletion, dashboard unlink/revoke, and physical DNS removal are distinct evidence-backed operations;
9. recovery is reversible, non-looping, re-verifies after material path changes, and fails closed to a truthful lower state when indeterminate;
10. support-burden metrics use only the current TSK-0498 event vocabulary/fields and specify denominator/owner/action/missing-data semantics; unsupported joins/metrics remain explicitly not computable rather than expanding telemetry;
11. current dual-mode Version-1 preserves complete accountless core support while optional account/dashboard state cannot strengthen technical protection evidence;
12. governance/repository failures and Action Authority remain fail-closed under REQ-0001/0002, CON-0020/0021, RSK-0044, INT-0001/0002;
13. no human supportability outcome, implementation, LG-07, build, deployment, production activation, market activation, launch, or real-user validation is inferred;
14. full modular Master Plan validation remains PASS and the CR-0008 owner-frozen planning baseline is unchanged.

**TSK-0042 result:** PASS candidate pending independent deterministic verification, full modular-plan validation, durable `CURRENT_STATE.md` write, and exact GitHub read-back.