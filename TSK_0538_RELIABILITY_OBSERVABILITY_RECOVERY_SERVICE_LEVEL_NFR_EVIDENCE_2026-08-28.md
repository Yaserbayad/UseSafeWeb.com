# TSK-0538 — Reliability/Observability/Recovery NFR Verification Evidence

**Task:** TSK-0538 — Define reliability, observability, recovery, and service-level NFRs  
**Acceptance:** ACC-0538  
**Verification:** VER-0538 — independent operability/SLO/recovery/privacy audit  
**Evidence:** EVD-0538  
**Date:** 2026-08-28  
**Result:** PASS candidate pending GitHub read-back and guarded runtime reconciliation

## 1. Exact evidence index

- Operability contract: `TSK_0538_RELIABILITY_OBSERVABILITY_RECOVERY_SERVICE_LEVEL_NFR_2026-08-28.md`
- Corrected contract blob: `d81537ef3ef66789528336e101d1e05f30030892`
- Initial creation commit: `c8c6b105c869213cb209b5c05a4e99b3a3d4b72f`
- Guarded correction workflow commit: `3262d0404c417f53a9a267fba9d734a251f00585`; successful run `33198604334` corrected end-to-end RTO semantics and root-capable-runner least-privilege wording before this audit.
- Current selected runtime: `CURRENT_STATE.md` blob `bbe14aff4156fcbc51b448cd58c5d310ae99d58a`; TSK-0538 selected as L4 / A3 / AUTO_ALLOWED / MEDIUM.
- WBS blob: `dce5b829c4d447eac180ae1e896e0019292cf971`
- Direct predecessor TSK-0484: current runtime PASS; contract blob `ebd146f88f51cae67b9515fb94133bcd74c8cf28`, evidence blob `15ad7e97f13210737e014499820690c30232a952`.
- TSK-0431 project-controlled recovery evidence blob: `2df5c05767fe326e38c609d37888f672dcb9dd48` — accepted project-controlled rebuild completed in 12 seconds with functional/privacy/security checks.
- TSK-0431 owner Azure-native restore evidence blob: `e077165e98fa4460fba84466ffe28953ad53dec0`.
- TSK-0443 certificate renewal/alert evidence blob: `c2f3b3b35c9d8e2ec33f473d72c508ebde30348d` — current daily public certificate check and <=30-day owner-alert route.
- Current requirements: REQ-0070 requires privacy-safe external uptime/endpoint, DNS/application health, CPU/memory/disk/availability metrics and actionable service/certificate/storage/resource alerts without mandatory centralized APM; REQ-0071 requires severity, ownership, containment, recovery, communication, verification and corrective action.
- Current constraints: CON-0018 accepts one lean DNS node and approximately 30 minutes recovery/downtime; CON-0022 prohibits a routine staffed customer-support operating model.
- INT-0018 requires operations to detect failure and restore a fresh-server service inside accepted RTO.

## 2. Authority and eligibility audit

The post-TSK-0497 queue contained only three candidates: TSK-0187 with unavailable representative-parent evidence, TSK-0140 with owner-review requirements, and unflagged TSK-0538. The guarded selection workflow succeeded before this task was executed.

TSK-0538 defines internal L4 reliability/operability requirements only. It does not buy/implement HA, add a monitoring vendor, mutate Azure control-plane resources, create a public SLA, create staffed support, activate a web application, recruit participants or launch.

`RSK-0002` remains OPEN.

**Result: PASS.**

## 3. ACC-0538 critical-journey audit

Section 3 explicitly defines success/failure boundaries for:

- public DNS DoH;
- public DNS DoT;
- DNS filtering correctness;
- removal/recovery;
- certificate lifecycle;
- clean DNS recovery/rebuild;
- future conditional accountless web/app start -> setup -> Protection Map.

The future web/app is explicitly marked conditional/unimplemented rather than presented as current behavior.

**Result: PASS.**

## 4. Observability-question and privacy audit

Section 2 starts from seven concrete operational questions rather than collecting telemetry by default. Sections 4 and 15 map necessary signals to those questions while preserving current privacy controls.

Required signals are limited to:

- controlled external synthetic endpoint/correctness/TLS probes;
- service state/config drift/upstream synthetic health;
- CPU/memory/disk/availability;
- certificate and recovery/backup status;
- future bounded-cardinality RED metrics only after the app exists.

Explicit prohibitions/constraints include:

- no user DNS/query/domain/browsing telemetry;
- no user ID/IP/journey token/raw URL/free text metric labels;
- Nginx access logging remains off;
- AdGuard query/file logging and identifiable client statistics remain off;
- no centralized APM/distributed tracing requirement absent evidence;
- `DVR-0230-01` remains open;
- root-capable host monitoring defaults to `contents: read`, non-persisted checkout credentials, minimum sudo and no repository writes; any temporary exception remains `DVR-0484-01` rather than becoming normal architecture.

**Result: PASS.**

## 5. Provisional SLI/SLO audit

ACC-0538 requires provisional SLI/SLO targets. Section 5 supplies measurable internal targets:

- DoH transaction availability >=99.9% rolling 30 days;
- DoT transaction availability >=99.9% rolling 30 days;
- synthetic DNS correctness >=99.9% rolling 30 days;
- encrypted-DNS synthetic latency p95 <=1.0s and p99 <=2.0s rolling 24h;
- TLS scheduled-check validity 100%;
- 100% of qualifying recovery drills/incidents meet <=30-minute RTO;
- future web/app critical-path availability >=99.9% rolling 30 days only after implementation;
- future web/app critical response p95 <=1.0s / p99 <=2.0s only after implementation.

The contract explicitly labels these as **internal provisional engineering targets, not customer promises**. It explains that 99.9% over 30 days is approximately 43 minutes of error budget, compatible with the already accepted approximately-30-minute single-node recovery model without implying HA.

Planned user-visible maintenance counts against availability by default; it is not silently excluded to improve performance figures.

**Result: PASS.**

## 6. Probe cadence/quality audit

Section 6 defines provisional minimum cadence:

- external DoH/DoT availability/correctness at least every 5 minutes;
- low-cost internal service/host health at least every 1 minute;
- preserve current daily public certificate validation;
- backup/recovery status on applicable workflows/operations review;
- future app critical synthetic path at least every 5 minutes after deployment.

Monitoring-system failures must be represented as unknown/instrumentation error, not service success.

This is a provisional NFR cadence, not a fabricated future calendar date, and is compatible with CON-0021.

**Result: PASS.**

## 7. Alert-condition audit

Section 7 defines two **alert urgency** classes:

- PAGE for confirmed user-facing critical degradation;
- TICKET for actionable risk/degradation before it becomes critical.

This is not the incident-state model in Section 12; alert urgency controls notification, while incident severity controls impact/ownership/containment/closure.

PAGE conditions cover confirmed repeated DoH/DoT failure, both transports failing, TLS validation failure, repeated/wrong DNS correctness, RTO-risk recovery, active critical privacy/security failure and future application widespread failure.

TICKET conditions include the already evidenced <=30-day certificate threshold plus renewal risk, bounded disk/memory/CPU pressure, stale/failed recovery evidence, configuration drift, SLO burn and monitoring blindness.

Resource pressure does not page by itself unless accompanied by user-visible impact or imminent irreversible risk. Every alert must identify journey, first diagnostic action, runbook and owner, avoid user/DNS history data and be test-fired before acceptance.

**Result: PASS.**

## 8. Recovery-objective audit

The correction applied before verification makes the DNS RTO unambiguous:

**<=30 minutes end to end from the earliest confirmed user-impact timestamp (first valid failed synthetic probe later confirmed as target failure, or planned rebuild start) through verified restoration.**

Therefore detection/triage consumes the same 30-minute envelope; it is not an extra invisible period.

Restoration requires DoH/DoT, accepted AdGuard/config, Quad9 dns10/ECS-off, filtering/rollback, privacy controls, restricted admin/firewall/listeners, TLS and synthetic health — not merely process startup.

The existing 12-second isolated project-controlled recovery result is correctly treated as evidence of capability, not converted into a public recovery promise.

RPO semantics are also correct for the privacy-minimal architecture:

- browsing/query-history RPO is not applicable because that dataset is prohibited;
- J0/J1 transient state is not restored;
- operational configuration recovery must use the latest accepted/versioned configuration plus protected recovery material; a material release is incomplete until its recovery source is current.

**Result: PASS.**

## 9. Backup-scope audit

Section 9 includes only deterministic reconstruction material: versioned scripts/config, approved filter/AdGuard invariants, protected secrets/credentials/certificate material where needed, owner-controlled Azure recovery material and runbooks/manifests.

It explicitly excludes DNS/query/domain/browsing history, query logs/per-client statistics, J0/J1, raw product event streams, ordinary support transcripts/raw diagnostics, safeguarding disclosures and unnecessary identity.

Backup completion alone is insufficient; restore must reproduce current approved invariants.

**Result: PASS.**

## 10. Restore-test audit

Section 10 defines a 14-point end-to-end clean restore/rebuild acceptance covering identity guard, pinned reconstruction, protected inputs, services, DoH/DoT, upstream/filtering, rollback, privacy, admin/firewall, TLS, synthetic health, elapsed RTO, post-health and absence of prohibited history.

Provisional cadence is:

- before any gate relies on recovery for first public/pilot operation;
- after material recovery-path changes;
- at least quarterly during active operation under the single-node architecture.

Azure-native recovery remains an owner-controlled boundary requiring direct owner/platform evidence where applicable.

**Result: PASS.**

## 11. Maintenance-behavior audit

Section 11 defines a lean rhythm consistent with REQ-0070/CON-0023:

- daily certificate check;
- health according to signal cadence;
- weekly minimum drift/pending-security-update review;
- monthly consolidated maintenance/capacity/cost/vendor review;
- quarterly recovery rehearsal;
- immediate review after material incidents/changes/failed controls.

Every material maintenance change requires exact version/config, action-authority check, recovery/rollback readiness, bounded mutation, affected regression, rollback/reopen on failure and durable evidence.

High-impact security/data/topology/Azure-control-plane changes retain existing owner authority.

**Result: PASS.**

## 12. Incident severity/escalation ownership audit

Section 12 defines SEV-1 through SEV-4 and explicit ownership:

- DNS/platform: SRE/Operations / Network Engineering, with AI actions bounded by WBS authority;
- future app: Software/Platform + SRE;
- privacy/security: Privacy/Security + Project Owner for consequential decisions;
- Azure control-plane: Project Owner boundary;
- safeguarding: dedicated safeguarding route;
- public/customer communication: based on verified facts and applicable consequential authority.

Every material incident must be severity-rated, have one current owner, record containment/recovery, verify restoration and update proportional regression evidence before closure.

Section 13 separately preserves CON-0022: no customer response-time/staffed-support SLA is created.

**Result: PASS.**

## 13. Current-evidence truthfulness audit

Section 16 accurately distinguishes currently proven DNS facts from not-yet-implemented TSK-0538 monitoring/application work. It cites current accepted facts including:

- single production DNS host/current technical identity;
- current DoH/DoT exposure and restricted plain DNS/admin;
- Quad9 dns10/ECS off;
- privacy logging/statistics controls;
- current TLS renewal/daily expiry monitoring with <=30-day owner alert;
- 12-second project-controlled recovery drill;
- direct owner evidence for Azure-native restore;
- approximately-30-minute accepted recovery envelope.

It does not claim future web/app or all new monitoring is already implemented.

**Result: PASS.**

## 14. Verification disposition

**VER-0538 independent audit result: PASS for ACC-0538's provisional internal L4 reliability/observability/recovery/service-level-NFR-definition scope.**

The corrected read-back contract at blob `d81537ef3ef66789528336e101d1e05f30030892` defines every ACC-0538 domain: critical journeys, provisional SLI/SLO targets, alert conditions, recovery objectives, backup scope, restore test, maintenance behavior and escalation ownership.

The following remain OPEN/non-PASS and are not converted by this result:

- implementation of the new uptime/health/resource/SLO monitoring set;
- future web/app observability and SLO evidence;
- `DVR-0230-01` custom DoH critical error-log permission hardening;
- `DVR-0484-01` privileged-runner repository-write separation;
- `GAP-0484-02` direct current public DoH/DoT abuse/rate/concurrency verification;
- any HA/multi-node architecture or public SLA;
- real-user/behavioral evidence (`RSK-0002`);
- final legal/privacy/participant gates;
- implementation/build/publication/launch.

**Runtime may move TSK-0538 to PASS only after this evidence file is persisted/read back and a guarded reconciliation verifies the current selection, exact contract/evidence/WBS/runtime preconditions.**
