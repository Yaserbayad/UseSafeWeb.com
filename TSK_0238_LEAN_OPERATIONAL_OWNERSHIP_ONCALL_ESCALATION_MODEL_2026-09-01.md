# TSK-0238 — Lean Operational Ownership and On-Call/Escalation Model

**Version:** 1.0.0  
**Date:** 2026-09-01  
**Lifecycle:** L5 — Architecture, Technical Design & Delivery Readiness  
**Task:** TSK-0238 — Define lean operational ownership and on-call/escalation model  
**Acceptance:** ACC-0238 / VER-0238 / EVD-0238  
**Hard dependency:** TSK-0231  
**Authority:** current modular Master Planning System; DEC-0053/CR-0006; DEC-0054/CR-0007; DEC-0055/CR-0008

## 1. Purpose and authority boundary

This document defines the minimum operational ownership, review cadence, incident escalation, human-only boundary, coverage gaps and evidence triggers needed to keep UseSafeWeb.com operable without prematurely creating a staffed operations organization. It is a **derivative operating model**, not a second WBS, runtime state store, decision register, staffing approval, employment decision, procurement approval, service-level promise or checkpoint.

The model preserves the current lean architecture and autonomy policy:

- routine objective work inside frozen scope is AI-autonomous where current Action Authority permits it;
- human intervention is reserved for genuinely nondelegable or owner-controlled acts;
- ordinary user problems are designed toward self-service, automated verification/recovery and product correction rather than routine staffed support;
- no 24/7 human on-call or staffed customer-support promise is created by this model;
- no additional employee, contractor, managed service or vendor is automatically authorized by a trigger in this document;
- no real England participant may be activated while the applicable legal/privacy/technical readiness gate remains unsatisfied;
- `RSK-0001` remains OPEN;
- `INT-0007` still requires later inspection of actual runtime/configuration/schema/log/cache/backup/deletion behavior before release;
- persistent identifiable query/file logging remains OFF and identifiable per-client statistics remain OFF/excluded under `CON-0007` and `CON-0008`.

## 2. Ownership model

### 2.1 Primary operational owner

**Primary operational duty owner: SRE / Operations function.** During the current lean phase this function is normally executed by the authorized AI Governor and project automation for actions that are evidence-based, reversible or otherwise `AUTO_ALLOWED`. It owns routine health review, incident coordination, recovery/rollback execution within authority, operational evidence, recurring maintenance coordination, and routing work to the correct technical custodian.

The SRE / Operations function does **not** acquire human authority merely because it performs technical execution. AI capability, server privilege and Action Authority remain separate.

### 2.2 Backup operational owner

**Backup operational duty owner: Project Owner.** The Project Owner is the fallback coordinator when the primary operational path cannot safely continue, when evidence is materially contradictory, when an actual human-only decision is reached, or when an unresolved cross-domain incident needs owner disposition.

This backup role is not a requirement for the Project Owner to perform routine technical work. Routine safe remediation remains with the primary operational function wherever authority permits.

### 2.3 Human-authority backup gap

For acts that specifically require the Project Owner or another qualified human, **no independently verified second human delegate is currently assigned**. AI/automation is not a substitute for that authority. This is an explicit coverage gap, not an inferred blocker for ordinary autonomous technical work.

If owner unavailability would prevent a required legal signature/attestation, new contract, regulated payment, strategic decision or other nondelegable act at the time it is actually needed, the affected work remains WAITING/BLOCKED as appropriate until a valid human authority path exists.

### 2.4 Domain custodians

| Domain | Primary custodian | Backup/escalation path | Current operating boundary |
|---|---|---|---|
| Service health, releases, recovery, recurring operations | SRE / Operations | Project Owner for genuine authority boundary; relevant technical custodian for diagnosis | Routine tested/reversible work may be autonomous within current authority. |
| Web/application and optional account/dashboard | Software Engineering | SRE / Operations; Security for security findings | Preserve complete accountless core; optional account cannot become mandatory for core value. |
| DNS/AdGuard, filters, encrypted endpoint | Network / DNS Engineering | SRE / Operations; Security for abuse/exposure | AdGuard remains frozen backend; admin/control path stays restricted; no browsing history. |
| Security/abuse | Security | SRE / Operations for containment/recovery; Project Owner only where owner authority is actually required | High/critical paths become release blockers until controlled or validly accepted under current authority. |
| Privacy/data handling | Privacy / Legal control function | SRE / Operations for containment; Project Owner/qualified human for nondelegable legal acts | No unsupported legal conclusion; `RSK-0001` remains OPEN; actual runtime reality must be inspected later. |
| Product/support friction | Product / Customer Experience | Software/UX/Operations depending root cause | Repeated ordinary human help is primarily a product/UX/automation defect, not a reason to promise staffed support. |
| Cost/capacity/vendor operations | Operations / Finance control function | Project Owner for new contract, material/unbudgeted spend or organizational commitment | Routine reversible scaling within approved architecture/budget may be autonomous; material commitment is not. |

## 3. Routine operating cadence

These are **initial design cadences**, not a public SLA and not proof that production monitoring is already implemented. Downstream operations/observability tasks may tighten or replace them based on measured evidence.

| Cadence | Minimum review | Owner | Evidence/output |
|---|---|---|---|
| Event-driven / continuous when active | External/service health, actionable alert conditions, security/privacy control alarms, certificate/endpoint failure signals | SRE / Operations | Privacy-safe alert/event plus runbook/action reference; no browsing/query history. |
| After every material change or incident | Health, rollback/recovery result, exact release/config, new regression need, privacy/security consequence | SRE / Operations + affected custodian | Change/incident evidence and verified stable outcome. |
| Daily during active production ramp or active material incident | Service state, unresolved alerts/incidents, recovery status, blocking defects, capacity/cost anomaly | SRE / Operations | Short operational disposition: continue, remediate, rollback or escalate. |
| Weekly during development/readiness and active production | Open corrective actions, dependency/vendor notices, certificate/domain/backup alert status, exceptional support queue, recurring failures | SRE / Operations | Owned actions with due condition and evidence reference. |
| Monthly | Cost/capacity/headroom, maintenance/dependency status, access/secret-age signals, vendor changes, privacy drift, support burden/root-cause trend, coverage gaps | SRE / Operations + domain custodians | Review record and any evidence-triggered task/gate/risk update. |
| Quarterly or after material topology/security/operations change | Recovery/on-call/incident rehearsal, access/coverage review, operating-model adequacy | SRE / Operations + Security/Privacy as applicable | Rehearsal findings, gaps, corrective actions and staffing/service review trigger if crossed. |

Routine cadence never authorizes collection of DNS/domain browsing history or identifiable per-client statistics.

## 4. Incident escalation model

Severity is based on actual user/control impact, not alert volume. These labels are the L5 operating design and do not replace the detailed downstream incident-response specification.

### SEV-1 — critical control, safety, security, privacy or broad availability failure

Examples include cross-parent access, exposed production secret/admin control, prohibited browsing/query-history collection, materially false protection verification, critical DNS/web outage, destructive corruption without safe recovery, or a legal/privacy gate violation that could cause prohibited processing.

**Default action:** contain first; stop or disable the affected path where safe; revoke/rotate/rollback/recover under existing authority; preserve only minimum privacy-safe evidence; prevent further affected activation; verify the stable result. Route immediately to the relevant Security/Privacy/Network/Software custodian and the Project Owner when an actual owner-only decision is reached.

A SEV-1 is release/activation blocking until the applicable control is verified or a valid higher-authority disposition exists. No AI may fabricate legal approval, signature, consent, provider acceptance or other human fact.

### SEV-2 — major degradation or high-risk partial failure

Examples include substantial service degradation, repeated deployment failure, auth/provider/datastore outage affecting the optional account path, certificate/renewal risk, serious false-positive pattern, capacity saturation trend or recoverable partial AdGuard/client lifecycle failure.

**Default action:** perform bounded diagnosis and tested reversible remediation/rollback/reconciliation within authority; keep Protection Map/user-facing state truthful; escalate to the appropriate custodian if the issue cannot be verified closed or if it crosses a security/privacy/human authority boundary.

### SEV-3 — routine bounded issue

Examples include isolated noncritical defects, ordinary self-service failures, nonurgent content/guidance drift or low-impact operational maintenance.

**Default action:** resolve through normal automation/self-service/product backlog and verify closure. Repetition or trend can elevate the issue or trigger an operating-capacity review.

## 5. Human-only / owner-controlled decisions

The following remain human/owner-controlled where current canonical authority says so; this model does not reclassify them:

1. named official-market activation;
2. organizational/entity/formalization decisions;
3. entering a new contract or equivalent material external commitment;
4. regulated fees or acts requiring a human/legal identity;
5. banking or merchant identity decisions;
6. legal attestations, signatures or statements that cannot truthfully be delegated;
7. material or unbudgeted spend outside already-approved reversible operating authority;
8. strategic modify/pivot/pause/stop/transfer/resume decisions;
9. irreversible acts that actually require human authority;
10. material change to frozen product/scope/policy boundaries;
11. owner-managed Azure control-plane provisioning/configuration where the canonical owner handoff boundary still applies.

The existence of a serious incident does **not** automatically make every technical containment/recovery step human-only. Safe reversible remediation inside approved authority should proceed autonomously when evidence and platform access permit it.

## 6. Current coverage gaps

These are explicit gaps to be carried forward, not reasons to fabricate capability:

| Gap | Current consequence | Resolution/trigger |
|---|---|---|
| No verified second human delegate for Project-Owner-only acts | A genuinely nondelegable act can wait on owner availability | Review when owner absence would block an actually due critical act, or before a lifecycle stage requires continuous human authority coverage. |
| No 24/7 staffed human on-call or routine customer-support team | No public 24/7 response promise; ordinary cases remain self-service/automation-first | Reassess only if measured incident/support demand cannot be handled safely by the lean model. |
| Production observability/alert routes/runbooks are not yet fully implemented and rehearsed | This L5 model is design, not proof of live monitoring | Downstream PKG-13 implementation/rehearsal must prove actual alerting, runbooks and recovery before relying on them. |
| End-to-end TSK-0485 threat/abuse model is not yet PASS | Security architecture is not yet complete | TSK-0485 and its successors must independently pass before later security/readiness gates. |
| `RSK-0001` legal/data readiness remains OPEN | No real England participant activation; no final legal-compliance inference | Resolve the applicable legal/privacy readiness path before the relevant activation gate. |
| `INT-0007` actual runtime/data-flow verification remains downstream | Design claims cannot substitute for implemented reality | Inspect actual fields/logs/recipients/retention/deletion/backups/config before release. |
| Concrete datastore/runtime choice remains downstream | Persistent account/device operations cannot be assumed implemented | Select/verify only when current evidence proves product/security/privacy/recovery fit. |

## 7. Evidence triggers for additional staffing or services

Crossing a trigger opens a **review**, not an automatic hire, purchase, contract or organizational change. The default response order is: automate/simplify/remove root cause → adjust bounded scope/capacity → consider a temporary specialist or managed service → consider ongoing contractor/staff only if evidence still requires it.

1. **Human-authority continuity trigger:** owner absence or single-person dependency repeatedly blocks a genuinely due critical/nondelegable act, incident decision or mandatory operational duty.
2. **Support-load trigger:** repeated ordinary human-help demand cannot be reduced through product/UX/automation/self-service, or routine active support time materially exceeds the current lean expectation of roughly 5–10 minutes per activation as described by `RSK-0005`.
3. **Incident-load trigger:** repeated SEV-1/SEV-2 incidents, concurrent incidents or corrective-action backlog make verified containment/recovery unreliable with current coverage.
4. **Security/privacy expertise trigger:** a high-impact security/privacy/legal issue requires qualified expertise that the current authorized functions cannot safely supply, or a blocking control cannot be independently verified.
5. **Availability/recovery trigger:** measured workload, alert frequency or recovery evidence shows the lean owner/automation model cannot meet an accepted service/recovery objective.
6. **Capacity/operations trigger:** sustained resource/headroom/vendor/maintenance workload crosses the evidence-based scale threshold established by later capacity/observability work and cannot be corrected safely by routine autonomous scaling.
7. **Vendor/service trigger:** a managed external service demonstrably reduces material operational/security/recovery risk or total effort compared with the current lean model and its data/terms/cost/exit consequences have been reviewed.
8. **Coverage-hours trigger:** actual incident/user demand consistently occurs outside available human authority coverage and creates material unresolved risk that automation cannot safely contain.
9. **500-active-user review trigger:** the verified 500-active-user milestone opens the organizational/commercial review required by `REQ-0085`; it is **not an automatic hiring, legal, expansion or spend threshold**.

Any resulting new contract, material/unbudgeted spend, organizational formalization or staffing commitment remains subject to its actual current human authority requirement.

## 8. Escalation decision table

| Situation | Autonomous first action | Escalate when | Human-only consequence |
|---|---|---|---|
| Routine service/deployment failure | Diagnose, retry if safely idempotent, rollback/recover, verify | Repeated/ambiguous non-idempotent outcome, material user/control impact, or missing safe path | None unless a retained owner decision is reached. |
| Security abuse/secret/admin exposure | Contain, revoke/rotate where authorized, block unsafe path, preserve minimum evidence | High/critical unresolved risk, cross-parent exposure, external commitment/notification requiring human authority | Owner/qualified human only for nondelegable risk/legal/contract acts. |
| Privacy/data drift | Stop prohibited collection/exposure, contain access, verify deletion/remediation where authorized | Material incident, uncertain legal obligation, rights/notification/signature requirement | Qualified human/Project Owner for actual nondelegable legal determination/act. |
| DNS/web outage | Run tested recovery/rollback/fail-safe and truthful status guidance | Recovery objective missed, repeated failure, architecture change or material spend required | Owner only for retained strategic/material commitment decisions. |
| Ordinary user issue | Self-service/AI troubleshooting and product defect loop | Exceptional security/infrastructure/legal/safeguarding case or sustained overload | No routine staffed-support promise. |
| Capacity/cost pressure | Routine reversible optimization/scaling within approved bounds | New contract, material/unbudgeted spend, topology/policy change or sustained capacity gap | Project Owner for the retained commitment/change decision. |
| Safeguarding/urgent non-service contact | Minimize data, use approved emergency/referral route, do not treat as ordinary support | Policy-defined safeguarding escalation | Human route where policy or real-world authority requires it. |

## 9. Acceptance evidence and deviations

This model is intentionally lean and does not claim that all downstream operational capabilities already exist. Its present acceptance boundary is architectural/operational design completeness under `ACC-0238`:

- primary operational owner: identified;
- backup operational owner: identified;
- routine cadence: defined;
- incident escalation: defined;
- human-only decisions: explicitly separated from routine autonomous execution;
- coverage gaps: explicit;
- additional staffing/service activation triggers: evidence-based and non-automatic.

Known deviations/gaps are those listed in Section 6 and remain downstream work. None is hidden or converted into a false PASS for another task.

## 10. Non-inference

Acceptance of this model does **not** itself prove or authorize production monitoring, 24/7 coverage, staffing, employment, contracting, purchasing, vendor acceptance, legal readiness, real-participant processing, public launch, implementation, LG-07/LG-08/LG-09 PASS, or any downstream task PASS. `RSK-0001` remains OPEN and `INT-0007` remains a later reality-verification boundary.
