# TSK-0538 — Reliability, Observability, Recovery and Service-Level NFRs

**Task:** TSK-0538 — Define reliability, observability, recovery, and service-level NFRs  
**Acceptance:** ACC-0538  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** INTERNAL PROVISIONAL L4 OPERABILITY CONTRACT / PUBLIC SLA OR IMPLEMENTATION NOT AUTHORIZED  
**Date:** 2026-08-28  
**Authority:** REQ-0070/0071 + CON-0018/0022/0023 + INT-0018 + TSK-0484 + current accepted DNS/TLS/privacy/recovery evidence + DEC-0050/CR-0003  
**Verification state:** PASS candidate pending independent verification and runtime reconciliation.

## 1. Scope and operating boundary

This contract defines the minimum reliability/observability/recovery behavior for UseSafeWeb’s current single-node encrypted-DNS service and the future separate web/app runtime when that application is legitimately built.

It does **not**:

- create a public/customer SLA;
- authorize HA, multi-node DNS, active-active topology or new paid monitoring/APM platforms;
- authorize Azure control-plane mutation;
- activate the future web application, participants or launch;
- create routine staffed customer support;
- weaken privacy controls to make operations easier.

`CON-0018` remains binding: initial DNS is one lean AdGuard node and accepts approximately **30 minutes recovery/downtime for failure or planned rebuild**. Near-zero-downtime HA is not justified without new evidence.

`RSK-0002` remains OPEN. These operational targets are not behavioral-validation evidence.

## 2. Operational questions — telemetry must answer these

Every signal retained by this contract must answer at least one of these questions:

1. **Can a supported device reach each approved encrypted DNS transport right now?**
2. **Does a privacy-safe synthetic DNS check return the expected allowed/filtering behavior without reading user traffic?**
3. **Is TLS valid for `dns.usesafeweb.com`, and is renewal at risk before expiry?**
4. **Is the DNS host healthy enough to continue serving, or is resource saturation likely to become user-visible?**
5. **If service fails, can the approved configuration be restored/rebuilt inside the accepted recovery objective without restoring prohibited history?**
6. **For the future web/app, can a parent start the accountless journey and receive the next valid application response without creating invasive telemetry?**
7. **What changed immediately before a service regression, and what exact version/configuration is running?**

A metric/log/alert that answers none of these questions is not justified by this L4 baseline.

## 3. Critical journeys and service boundaries

| Journey / capability | Current status | Success definition | Failure boundary |
| --- | --- | --- | --- |
| DNS DoH | Current technical service | TLS/hostname valid on TCP 443; approved DoH path responds to privacy-safe synthetic query with expected DNS behavior | connect/TLS/path failure, timeout, invalid response, wrong resolver/filter behavior |
| DNS DoT | Current technical service | TLS/hostname valid on TCP 853; approved DoT path responds to privacy-safe synthetic query with expected DNS behavior | connect/TLS/transport failure, timeout, invalid response, wrong resolver/filter behavior |
| DNS filtering correctness | Current technical service | controlled allowed test resolves as expected and controlled blocked test is blocked under the accepted filter policy | unexpected allow/block, upstream/config drift, rollback regression |
| DNS removal/recovery | Supported product requirement / manually evidenced | UseSafeWeb config can be removed and ordinary DNS/internet behavior restored without retaining a UseSafeWeb protection claim | removal fails, ordinary DNS not restored, stale S1 claim persists |
| Certificate lifecycle | Current operational capability | certificate stays valid for hostname/chain; automated renewal path and Nginx reload remain healthy | expiry/hostname/chain failure, renewal/deploy-hook failure |
| Clean DNS recovery/rebuild | Current accepted capability | approved service/config/privacy/filtering/TLS behavior restored on approved target within recovery objective | RTO exceeded, wrong config/version, privacy/filtering/health acceptance fails |
| Accountless web/app start -> setup -> Protection Map | Future conditional capability | when built, parent can receive each critical application response and final truthful map without account or user-history telemetry | endpoint unavailable/error, stale/incorrect state, data/telemetry control failure |

User-level DNS queries, visited domains and browsing history are **not** observability journeys or diagnostic sources.

## 4. Privacy-safe signal contract

### External synthetic signals

Required when the applicable runtime exists:

- public TCP 443 TLS/DoH reachability and transaction success;
- public TCP 853 TLS/DoT reachability and transaction success;
- hostname/chain/expiry validation;
- privacy-safe controlled allowed-domain resolution;
- privacy-safe controlled blocked-test behavior using project-owned/synthetic test input;
- future web/app critical endpoint/start-flow synthetic success after implementation.

Synthetic probes must use fixed controlled test inputs and must not sample or replay participant/customer traffic.

### Internal DNS/platform signals

Minimum:

- AdGuard service active/healthy;
- Nginx service active/healthy;
- loopback admin/DNS/backend listener invariants;
- approved configuration/version/hash or equivalent drift indicator;
- upstream synthetic-resolution health;
- CPU utilization;
- memory utilization/pressure;
- disk utilization/free capacity;
- host/service availability;
- certificate days remaining and renewal/deploy-hook health;
- latest governed backup/recovery evidence age/status where applicable.

### Future web/app signals

When built, minimally use bounded-cardinality RED-style signals:

- request rate by route template/status class;
- error rate by route template/status class;
- latency histogram/percentiles for critical route templates and external dependencies;
- aggregate application health/dependency health.

No metric label may contain user ID, IP, journey token, raw URL/query string, email, device fingerprint, DNS/domain data or free-text error/user content.

### Logging/tracing boundary

REQ-0070 does **not** require centralized logs/APM/distributed tracing. Under the lean baseline:

- use structured operational/security logs only where needed to explain failures;
- keep normal Nginx access logging off under the current privacy contract;
- keep AdGuard query/file logging and identifiable client statistics off;
- never log full journey tokens, DNS query history, request bodies containing user data or secrets;
- distributed tracing remains optional and must not be added merely because it is fashionable; if later justified for the web/app, it must use bounded attributes and no persistent family identity.

`DVR-0230-01` remains OPEN until the custom DoH critical error-log mode is hardened/read-back verified.

## 5. Provisional internal SLIs and SLOs

These are **internal provisional engineering targets**, not customer promises. They are deliberately compatible with the accepted single-node/approximately-30-minute recovery model and must be recalibrated after real operating evidence exists.

Availability calculations count user-visible planned maintenance by default; maintenance is not silently excluded merely to improve the SLO.

| SLI | Definition | Provisional internal SLO | Measurement |
| --- | --- | --- | --- |
| DoH transaction availability | successful valid external synthetic DoH transactions / scheduled DoH transactions | **>=99.9% over rolling 30 days** | independent privacy-safe synthetic probe |
| DoT transaction availability | successful valid external synthetic DoT transactions / scheduled DoT transactions | **>=99.9% over rolling 30 days** | independent privacy-safe synthetic probe |
| DNS synthetic correctness | scheduled allowed+blocked synthetic checks with expected result / all scheduled correctness checks | **>=99.9% over rolling 30 days** | controlled project/synthetic names only |
| DNS transaction latency | end-to-end duration of successful external synthetic encrypted-DNS transactions | **p95 <=1.0 s and p99 <=2.0 s over rolling 24 h**, provisional | external probe histogram; no user traffic |
| TLS validity | scheduled external checks with valid hostname, chain and non-expired certificate / scheduled checks | **100%** | TCP 443 and 853 certificate checks |
| Recovery objective attainment | qualifying recovery drills/incidents restored inside RTO with all acceptance invariants / qualifying recovery drills/incidents | **100% meet <=30-minute RTO** | timed recovery/incident evidence |
| Future web/app critical-path availability | successful synthetic critical application transactions / scheduled transactions after implementation | **>=99.9% over rolling 30 days**, provisional and inactive until app exists | synthetic application probe only |
| Future web/app critical response latency | successful critical-route response duration after implementation | **p95 <=1.0 s, p99 <=2.0 s over rolling 24 h**, provisional | bounded route-template histogram |

### Why 99.9% is provisional rather than a public guarantee

A 99.9% 30-day target provides roughly 43 minutes of error budget, which is consistent with the already accepted approximately-30-minute single-node recovery envelope while still making prolonged/repeated outages visible. It does not justify HA and may be revised only from operating evidence and owner-approved architecture/economic decisions.

## 6. Probe cadence and quality requirements

Provisional minimum cadence once operational:

- external DoH/DoT availability/correctness: **at least every 5 minutes**;
- internal service/host health: **at least every 1 minute** where the mechanism is low-cost and local;
- certificate public validation: preserve the currently proven **daily** check, while local renewal automation remains on its current timer;
- backup/recovery status: check on every backup/recovery workflow and during periodic operations review;
- future web/app synthetic critical path: at least every 5 minutes after deployment.

Probe failures caused by the monitoring system itself must be distinguishable from target failure. Missing probes are `unknown/instrumentation_error`, not automatic service success.

## 7. Alert policy — symptoms first

Two operational severities are used for automated alerts:

- **PAGE:** user-facing critical degradation requiring immediate action/escalation.
- **TICKET:** actionable risk/degradation that should be corrected before it becomes a user-facing incident.

Cause-only metrics are normally ticket/dashboard signals unless they coincide with user-visible symptoms.

### PAGE conditions

Page when any of these occur:

1. DoH or DoT critical-path synthetic transaction fails on **two consecutive 5-minute checks**, or both transports fail on one confirmed check from a valid independent vantage;
2. TLS hostname/chain validation fails on either approved public transport;
3. DNS correctness controlled probe produces an unexpected filtering/resolution result on two consecutive checks, or one confirmed change presents a material safety/privacy risk;
4. service recovery has begun and elapsed outage is approaching the **30-minute RTO** without verified restoration;
5. privacy/security monitoring detects an active critical control failure such as query logging unexpectedly enabled, public admin exposure, secret exposure or equivalent high-impact condition;
6. future web/app critical path, once active, has confirmed widespread 5xx/unavailability across two consecutive checks.

### TICKET conditions

Create/maintain an actionable ticket when:

- certificate has **<=30 days remaining**, preserving the already proven owner-alert threshold;
- certificate renewal/dry-run/deploy-hook health check fails but current certificate remains safely valid;
- disk utilization >=80% for 1 hour or projected exhaustion becomes plausible;
- memory pressure/utilization >=90% for 15 minutes without current endpoint failure;
- CPU utilization >=90% for 15 minutes without current endpoint failure;
- backup/recovery evidence is stale, failed or overdue against the current maintenance cadence;
- configuration/version drift exists without current user-visible failure;
- repeated SLO burn indicates the 30-day error budget will be exhausted even if no single incident is currently paging;
- monitoring itself has a sustained blind spot/missing-data condition.

A resource threshold alone does not page unless it is coupled with a user-visible failure or immediate irreversible risk such as imminent disk exhaustion.

### Alert requirements

Every alert must:

- name the affected journey/signal;
- include first diagnostic query/check and relevant runbook link;
- identify the operational owner;
- avoid participant/user/DNS-history data;
- be test-fired during implementation/acceptance;
- close or downgrade only after the recovery verification condition passes.

## 8. Recovery objectives and fail-safe behavior

### DNS RTO

**RTO: <=30 minutes** from confirmed qualifying single-node service failure/rebuild decision to verified restoration of:

- encrypted DoH/DoT service on approved identity;
- accepted AdGuard version/configuration;
- Quad9 dns10 upstream and ECS-off invariant;
- filtering baseline and rollback behavior;
- query/file logging off, statistics off, anonymisation/privacy baseline;
- restricted administration and required firewall/listener state;
- TLS/hostname validity;
- synthetic health acceptance.

The accepted project-controlled recovery drill completed in 12 seconds, but this contract keeps the owner-approved <=30-minute objective rather than converting one isolated rehearsal into a public promise.

### RPO / data-loss objective

UseSafeWeb intentionally has no recoverable user browsing/query-history dataset.

- User/query-history RPO: **not applicable by design; prohibited data is not backed up/restored.**
- J0/J1 transient journey state is not a durable recovery objective and must not be resurrected from backup.
- Operational configuration RPO: the recoverable state must be the latest **accepted/versioned** non-secret configuration plus current approved protected secret/certificate/recovery material. A material configuration release is incomplete until its recovery source is correspondingly current and verified.

### Failure behavior

- Never fail open to plaintext UseSafeWeb DNS merely to meet availability.
- If protection cannot be verified, user-facing state must become Action needed/Not covered/Uncertain/Removed as owning contracts require.
- If recovery cannot complete safely inside RTO, escalate rather than weakening privacy/security/filtering controls.
- Ordinary DNS recovery/removal guidance must remain available where UseSafeWeb itself is causing connectivity loss.

## 9. Backup scope

Backup/recovery must remain privacy-minimal.

Included only where required for deterministic service reconstruction:

- versioned deployment/recovery scripts and non-secret configuration;
- approved AdGuard/filter configuration and invariants;
- protected secrets/credentials needed for authorized administration/recovery;
- certificate/key material only through approved protected mechanisms where needed;
- Azure-native infrastructure recovery material owned by the owner-controlled boundary;
- runbooks/verification manifests needed to prove restoration.

Explicitly excluded:

- DNS/query/domain/browsing history;
- AdGuard query logs or per-client statistics;
- J0/J1 transient journey records;
- raw product event streams;
- support transcripts/raw diagnostics except a separately governed active incident dataset with its own deletion rule;
- safeguarding disclosure content;
- unnecessary customer/child identity.

A backup is not accepted merely because it completed; restoration must reproduce current approved invariants.

## 10. Restore/rebuild test contract

A qualifying recovery test must begin from an isolated/fresh approved target or equivalently clean state and must prove, end to end:

1. target identity/environment guard;
2. installation/reconstruction from pinned/versioned sources;
3. protected recovery input availability without Git secrets;
4. AdGuard/Nginx/service startup;
5. encrypted DoH and DoT success;
6. correct upstream/ECS/filter baseline;
7. filtering block/allow/exception/rollback regression;
8. privacy persistence invariants;
9. restricted administration/listeners/firewall;
10. TLS identity/chain validation;
11. synthetic endpoint health;
12. measured elapsed recovery time <=30 minutes;
13. post-test health check;
14. evidence that prohibited user/query history was not introduced/restored.

### Provisional cadence

- before any gate relies on recovery for first public/pilot operation;
- after a material change to recovery scripts, protected backup format, AdGuard major behavior, TLS topology or restore path;
- **at least quarterly during active operation** while the single-node architecture remains in use.

Azure-native recovery remains owner-controlled; when a gate requires an Azure-native restore test, direct owner/platform evidence is required rather than an AI claim.

## 11. Maintenance behavior

Routine maintenance must be reversible, evidence-based and preserve service/privacy/security state.

Minimum operational rhythm once active:

- daily certificate check (already implemented for current DNS);
- continuous/scheduled service and endpoint health according to §6;
- at least weekly check for OS/package/AdGuard/filter/certificate/domain/runtime drift and pending security updates;
- at least monthly consolidated maintenance/capacity/cost/vendor review;
- quarterly recovery rehearsal while the single-node model is active;
- immediate review after a material incident, material vendor/platform change or failed control.

For every material maintenance change:

1. identify exact version/config and acceptance invariants;
2. confirm action authority;
3. verify backup/rollback/recovery path where needed;
4. apply only the bounded change;
5. re-run affected health/security/privacy/filtering regression;
6. rollback or reopen if verification fails;
7. record durable evidence and update runbook/regression coverage after incident-caused change.

Major/behavior-changing/high-impact security/data/topology/Azure-control-plane changes retain their applicable owner authority and are not auto-approved by this maintenance contract.

## 12. Incident severity, ownership and escalation

### Severity model

| Severity | Definition | Minimum response |
| --- | --- | --- |
| SEV-1 | Full critical DNS outage, invalid TLS identity, active serious privacy/security exposure, wrong protection behavior with material safety impact, or recovery unable to maintain critical controls | Immediate containment/recovery; owner/security/privacy escalation as applicable; do not preserve optimistic protection claim |
| SEV-2 | One critical transport/path materially degraded, widespread correctness/filtering defect, repeated outage/SLO burn, or recovery trending toward RTO breach | Urgent technical recovery/root cause; affected path may be marked uncertain/not covered; escalate if not bounded |
| SEV-3 | Limited degradation, stale guidance, non-urgent capacity/drift, recoverable monitoring gap | Ticketed correction with bounded owner and verification |
| SEV-4 | Informational/routine maintenance issue without material service/protection impact | Track in normal maintenance; no immediate interruption |

### Ownership

- **DNS/platform incident owner:** SRE/Operations / Network Engineering; AI automation may execute only actions explicitly AUTO_ALLOWED and independently verified.
- **Application incident owner once app exists:** Software/Platform Engineering with SRE/Operations.
- **Privacy/security incident:** Privacy/Security + Project Owner for consequential decisions; technical containment may proceed only within existing action authority.
- **Azure control-plane incident/action:** Project Owner boundary unless explicitly reopened.
- **Safeguarding incident:** dedicated safeguarding procedure; not ordinary SRE/customer support.
- **Public/customer communication:** factual incident input may be prepared from verified evidence; consequential publication follows the applicable authority rather than being auto-issued by this NFR.

Every material incident must be severity-rated, have one current owner, record containment/recovery evidence, verify restored state, and add/update proportional regression evidence before closure.

## 13. No staffed-support SLA

`CON-0022` remains binding. Operational alert response is an internal service-control requirement and does not create a public human support promise.

- No “reply within X hours” customer-support SLA is introduced.
- Self-service status/removal/recovery behavior should remain deterministic where feasible.
- Unusual technical, privacy, security, legal or safeguarding incidents may require owner/human escalation under their existing procedures.

## 14. Service-level review and error-budget behavior

For each 30-day internal SLO window:

- store synthetic success/failure counts, latency histograms/percentiles and monitoring-quality marker only; no user/query identifiers;
- investigate when projected error-budget consumption materially threatens the SLO;
- after an SLO miss, prioritize reliability/root-cause correction before adding scale/complexity;
- a repeated SLO miss is evidence to reconsider topology/capacity, but does not automatically authorize HA spend;
- do not exclude incidents or redefine denominators after the fact to manufacture compliance.

## 15. Testable implementation/acceptance assertions

A later operations/QA suite must prove at least:

1. external DoH and DoT synthetic probes run from a vantage independent of the production process itself;
2. probes use controlled synthetic inputs and never user query history;
3. service availability/correctness/latency SLIs reproduce from stored aggregate monitoring results;
4. missing probe data is distinguishable from success;
5. TLS checks validate hostname, chain and expiry on both 443 and 853;
6. <=30-day certificate condition creates the owner ticket/alert path;
7. page conditions can be test-fired and reach the correct owner/runbook;
8. CPU/memory/disk signals use bounded labels and contain no user data;
9. normal Nginx access/query-history collection remains disabled;
10. AdGuard query/file logging and per-client statistics remain disabled;
11. public admin/plain DNS exposure remains absent;
12. recovery drill restores every §8 invariant inside <=30 minutes;
13. backup/restore excludes query/domain/J0/J1/raw-event history;
14. restored configuration equals the current accepted version/invariants;
15. post-recovery health and filtering/privacy regressions pass;
16. future web/app RED metrics use route templates/status classes, not raw URLs/user IDs;
17. all automated alerts are actionable and mapped to an owner/runbook;
18. cause-only resource pressure does not page unless coupled with user impact/imminent irreversible risk;
19. material incident closure contains restored-state verification and regression/corrective-action linkage;
20. no internal SLO or alert wording is presented as a customer/public SLA without separate authority.

## 16. Current accepted evidence relevant to this contract

Current canonical technical evidence already establishes, among other facts:

- production `adguardvm`, Ubuntu 24.04, Azure West Europe, AdGuard v0.107.79;
- public encrypted resolver identity `dns.usesafeweb.com` on DoH 443 and DoT 853, with plain DNS/admin loopback-only;
- exact Quad9 dns10 upstream and ECS off;
- query/file logging/statistics off and current privacy controls;
- current TLS certificate/renewal/deploy hook, daily expiry check and <=30-day owner alert route;
- successful project-controlled isolated recovery/rebuild measured at 12 seconds with current functional/privacy/security checks;
- direct Project Owner evidence that the owner-managed Azure-native restore was exercised successfully;
- current single-node architecture and approximately-30-minute accepted recovery envelope.

These are implementation facts for the current DNS service, not proof that the future web/app or all TSK-0538 monitoring has already been implemented.

## 17. Revalidation/change triggers

Reopen affected NFRs when:

- DNS topology changes from single node or public ingress changes;
- new region/provider/upstream is introduced;
- web/app becomes implemented or its architecture materially changes;
- SLO evidence repeatedly shows the current target/topology is inappropriate;
- backup/recovery format or path changes;
- certificate/domain/renewal topology changes;
- a new telemetry/APM/logging vendor is proposed;
- monitoring requires user-linked fields not currently permitted;
- public SLA/support promise is proposed;
- major incident shows a missing signal, bad threshold or failed recovery assumption;
- security/privacy NFR changes invalidate an operational signal/control.

## 18. ACC-0538 traceability

ACC-0538 requires critical user journeys, provisional SLI/SLO targets, alert conditions, recovery objectives, backup scope, restore test, maintenance behavior and escalation ownership.

- §3 defines critical journeys.
- §§4–6 define privacy-safe signals and provisional SLIs/SLOs.
- §7 defines actionable alert conditions and ownership/runbook requirements.
- §§8–10 define RTO/RPO, fail-safe behavior, backup scope and restore/rebuild acceptance/cadence.
- §11 defines maintenance behavior.
- §§12–13 define severity, incident ownership/escalation and the no-staffed-support boundary.
- §§14–15 define error-budget and implementation verification behavior.

**TSK-0538 result: PASS candidate for provisional internal L4 reliability/operability-NFR definition only, subject to independent verification, GitHub read-back and runtime reconciliation. No public SLA, HA purchase, new monitoring vendor, implementation or launch is authorized.**
