# UseSafeWeb — Experiment 1 Support and False-Positive Intake Process

**Task:** TSK-0169  
**Stage:** L2 preparation for Experiment 1  
**Status:** operational process only — does not authorise recruitment/activation  
**Reviewed:** 2026-08-27

## Purpose

Provide one privacy-safe process for setup problems, DNS/filtering false positives, compatibility failures, removal/recovery questions, and other pilot support issues. The process preserves the experiment's assistance metrics and prevents support/debugging from becoming an unrecorded source of browsing-history collection.

## Mandatory intake record

Every issue receives one record with these fields:

```text
Issue ID:
Participant ID (pseudonymous):
UTC opened:
Journey stage / environment:
Category:
Severity:
Parent-reported symptom:
Privacy-safe evidence reference:
Intervention start/end markers:
Active intervention minutes:
Action taken:
Outcome:
Protection state after action: verified / parent-confirmed / action-needed / not-covered
Diagnostic procedure invoked?: yes/no + ticket ID
Safeguarding procedure invoked?: yes/no + non-sensitive event reference
Closure status: resolved / workaround / unsupported / deferred / escalated
UTC closed:
Closure verifier:
Non-sensitive notes:
```

Do not record child name, exact DOB, browsing/domain history, messages, contacts, photos, location, social content, credentials, tokens, private keys, or raw AdGuard query logs in this intake record.

## Categories

Use one primary category:

- **SETUP** — parent cannot complete an approved setup step.
- **DNS-REACHABILITY** — resolver/profile/path cannot be reached or verified.
- **FALSE-POSITIVE** — a legitimate required domain/service appears blocked by the UseSafeWeb filtering baseline.
- **COMPATIBILITY** — VPN, alternate secure DNS, Private Relay/platform routing, captive portal, OS/app/network behavior, or another interaction prevents reliable operation.
- **REMOVAL-RECOVERY** — parent needs to remove/revert the configuration or recover normal DNS behavior.
- **GUIDANCE** — non-fault question about protection state or supported behavior.
- **PRIVACY-SECURITY** — suspected privacy/security defect or unsafe diagnostic request.
- **SAFEGUARDING** — child-safety concern/disclosure; immediately use `CHILD_SAFETY_ESCALATION_PROCEDURE.md` rather than investigating through product support.
- **OTHER** — rare bounded issue with a clear description; review repeated OTHER issues after the wave.

## Severity

- **S1 — urgent:** immediate safety/privacy/security risk, service behavior that could expose prohibited data, or a safeguarding boundary. Stop the affected path and escalate.
- **S2 — blocking:** participant cannot safely continue activation or baseline protection is materially broken.
- **S3 — degraded:** participant can continue with a bounded limitation/workaround that is truthful and reversible.
- **S4 — informational:** question or minor issue with no material activation/protection impact.

Severity describes support urgency/impact, not child-risk assessment. Safeguarding concerns follow their dedicated procedure.

## Evidence hierarchy

Use the least sensitive evidence that can establish the problem:

1. support description and configuration/state check without request history;
2. synthetic test generated specifically for reproduction;
3. non-identifying service health/configuration evidence;
4. minimal screenshots/config excerpts with identifiers/secrets removed where necessary;
5. only if genuinely necessary, the exceptional diagnostic process below.

**Never ask for browsing history or enable broad query logging as the default way to diagnose a false positive.**

If temporary request-level diagnostic data is genuinely necessary, open and follow `EXCEPTIONAL_DIAGNOSTIC_LOGGING_PROCEDURE.md` (TSK-0227). The support record contains only the diagnostic ticket ID and non-sensitive conclusion, not the raw data.

## False-positive workflow

1. Confirm the reported issue is within the supported pilot scope.
2. Reproduce with a synthetic/non-participant test where possible.
3. Determine whether the block is caused by UseSafeWeb/AdGuard filtering rather than the site/app, upstream, network, device, or unrelated policy.
4. Identify the narrowest safe correction. Do not disable the whole baseline to solve one domain/service issue.
5. If an exception is required, record what protection is reduced and make it reversible.
6. Re-test the legitimate path and at least one relevant baseline blocked-test path so the correction does not silently remove filtering.
7. Update the parent-facing Protection Map truthfully. If effective protection is uncertain, use `Action needed` or `Not covered`, not `Protected — verified`.
8. Record intervention minutes, action, outcome, evidence and closure.

## Setup / compatibility workflow

1. Observe the user's actual block before intervening where practical.
2. Time and classify assistance using `EXPERIMENT_01_FACILITATOR_GUIDE.md`.
3. Use current supported install/removal/recovery guidance; do not improvise a permanent unsupported configuration.
4. If VPN/alternate DNS/Private Relay/network behavior makes the DNS path uncertain, do not claim verified protection until the effective path is directly re-tested.
5. If no safe supported resolution exists, mark the path `unsupported` / `Not covered`, restore normal device behavior where appropriate, and record the limitation.

## Privacy/security escalation

Immediately stop the affected diagnostic/product path and escalate to the Project Owner if support reveals:

- persistent identifiable DNS/query history unexpectedly enabled;
- identifiable per-client statistics outside the approved baseline;
- raw child browsing/domain data copied into an unapproved system;
- exposed credential/token/private key;
- an unsafe request to collect surveillance-style data;
- a material protection claim that cannot be supported by evidence.

Use the applicable security/privacy incident process; do not close the support ticket merely because the user's immediate symptom disappeared.

## Safeguarding boundary

If a support conversation becomes a child-safety concern/disclosure, use `CHILD_SAFETY_ESCALATION_PROCEDURE.md`. Product support must not investigate abuse/grooming or delay an emergency/referral route in order to collect technical evidence.

## Closure criteria

An issue closes only when all applicable conditions are recorded:

- category and severity assigned;
- intervention minutes/reason recorded;
- action and privacy-safe evidence recorded;
- current outcome/protection state is truthful;
- any temporary diagnostic logging is stopped and deletion verified under TSK-0227;
- removal/recovery has restored normal behavior when that was the chosen outcome;
- unresolved limitation is explicitly marked unsupported/deferred/escalated rather than silently accepted;
- closure verifier and UTC closure time recorded.

## Wave review output

Aggregate without participant identity:

- issue count/rate by category and severity;
- assistance minutes by category/stage;
- false-positive count and resolution pattern;
- compatibility/platform clusters;
- unsupported paths;
- privacy/security/safeguarding escalations as non-identifying counts/categories where appropriate;
- repeated product/instruction defects that should be fixed before Wave B.

## Canonical baseline used

- `EXPERIMENT_01_CONCIERGE_VALIDATION.md` — support/intervention/false-positive metrics.
- `EXPERIMENT_01_FACILITATOR_GUIDE.md` — assistance timing and taxonomy.
- `EXCEPTIONAL_DIAGNOSTIC_LOGGING_PROCEDURE.md` — bounded exceptional diagnostic data.
- `PROTECTION_CLAIMS_CHECKLIST.md` — truthful state labels and exception handling.
- `CHILD_SAFETY_ESCALATION_PROCEDURE.md` — safeguarding boundary.
- Frozen WBS ACC-0169 and linked Experiment-1/privacy constraints.

## Acceptance result

Every issue is required to carry participant ID, category, severity, intervention minutes, privacy-safe evidence, action, outcome and closure. Exceptional diagnostics are explicitly routed through TSK-0227, and false-positive resolution is narrow, reversible and re-tested rather than using broad browsing-history collection or blanket filtering disablement.
