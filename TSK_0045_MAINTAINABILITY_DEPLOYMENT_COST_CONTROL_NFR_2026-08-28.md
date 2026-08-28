# TSK-0045 — Maintainability, Deployment and Cost-Control NFRs

**Task:** TSK-0045 — Define maintainability, deployment, and cost-control NFRs  
**Acceptance:** ACC-0045  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** INTERNAL PROVISIONAL L4 MAINTAINABILITY/DEPLOYMENT/COST CONTRACT / DEPLOYMENT OR AZURE CONTROL-PLANE CHANGE NOT AUTHORIZED  
**Date:** 2026-08-28  
**Authority:** TSK-0314 + CON-0020/0021/0023 + current GitHub-canonical runtime/deployment/recovery evidence + owner-managed Azure boundary + DEC-0050/CR-0003  
**Verification state:** PASS candidate pending independent verification and runtime reconciliation.

## 1. Scope and authority boundary

This contract defines how UseSafeWeb must remain reproducible, maintainable, rollbackable and cost-visible as the current DNS service and future separate web/application evolve.

It does **not**:

- authorize an Azure control-plane change, resource purchase, resize, deployment or deletion;
- authorize the unbuilt web/app, participants, publication or launch;
- make the temporary governance/reconciliation workflows used during planning a permanent production deployment architecture;
- authorize an infrastructure monthly spend amount that the Project Owner has not approved;
- replace task-specific action authority for production changes;
- create a high-availability/multi-node requirement contrary to CON-0018.

GitHub `main` remains canonical durable source under CON-0020. Azure resource creation/control-plane configuration remains owner-managed unless explicitly reopened. `RSK-0002` remains OPEN.

## 2. Deployment architecture principle

### 2.1 Deterministic, source-controlled deployment

Every deployable service/configuration must have one reproducible deployment path whose required source is versioned in GitHub.

Current DNS service:

- direct Ubuntu host installation remains the accepted baseline;
- AdGuard/Nginx/configuration/recovery logic is represented by versioned scripts, approved configuration artifacts, workflows/runbooks and exact evidence in the repository;
- production mutation occurs only through a governed, target-guarded path permitted by the applicable WBS action authority.

Future web/app:

- remains a separate application/server boundary;
- when legitimately built, its deployment mechanism must be source-controlled and reproducible from a clean approved target;
- no manual production-only step may exist without a documented reason, owner and verification/rollback procedure.

A deployment is not complete merely because a command exited successfully. It must pass read-back and applicable functional/security/privacy/reliability acceptance.

### 2.2 Environment identity

Each deployment workflow must bind to an explicit environment/target identity before mutation. At minimum distinguish:

- `production-dns`;
- `recovery-dns`;
- future `production-webapp`;
- future non-production web/app environment(s) only if actually created/approved.

Environment names do not create the Azure resources themselves.

GitHub deployment environments may be used to restrict branches, secrets and protection rules where they materially improve safety. Current GitHub documentation confirms environments can restrict deployment branches, gate jobs and limit access to environment secrets; concurrency can serialize deployment to one environment. These controls supplement, not replace, WBS/action-authority rules.

## 3. Repeatable deployment contract

Every material deployment/change workflow must implement or invoke the following sequence as applicable:

1. **source pin** — exact Git commit, release/config version and dependency versions are known;
2. **target guard** — exact environment/host identity is verified before privileged mutation;
3. **authority check** — the task/action authority and required gates permit the change;
4. **pre-state capture** — affected version/config/hash/service health and rollback source are recorded;
5. **backup/recovery readiness** — applicable current protected recovery material is available and tested enough for the change risk;
6. **pre-deploy verification** — syntax/config/schema/migration compatibility checks pass before restart/destructive action;
7. **single bounded mutation** — unrelated changes are not bundled for convenience;
8. **post-deploy read-back** — exact intended state is read from the target rather than inferred from workflow success;
9. **regression verification** — affected functional, security, privacy, DNS/filtering, TLS, observability and recovery checks pass;
10. **evidence publication** — secret-safe durable evidence identifies source version, target/environment, test result and resulting state;
11. **runtime reconciliation** — canonical state changes only after acceptance proof and GitHub read-back.

Deployments to the same environment must be serialized. A newer deployment must not silently cancel an in-progress mutation unless the specific operation is proven safely cancellable and the recovery semantics are explicit.

## 4. Versioning contract

### 4.1 Source and release identity

Every deployed state must be traceable to:

- Git commit SHA;
- service/application/configuration version where the artifact has its own version;
- exact third-party runtime dependency version(s) that materially affect behavior;
- target environment/host identity;
- deployment workflow/run identifier or equivalent reconstructable execution record.

### 4.2 Version semantics

- Use semantic versioning for the future public application/API when there is a real externally consumed versioned interface.
- Internal configuration/policy artifacts use explicit schema/artifact versions plus Git blob/commit identity; do not force SemVer where it adds no useful compatibility meaning.
- AdGuard and other third-party components stay pinned to an approved tested release until an update passes its own compatibility/security/privacy regression.
- Generated outputs never outrank their authoritative source definitions.

A version string without exact source/config evidence is insufficient release identity.

## 5. Rollback contract

Rollback must be designed **before** deployment, not after failure.

For each material change define:

- rollback trigger(s);
- exact previous known-good version/configuration;
- protected input needed to restore it;
- whether rollback is data/schema compatible;
- maximum safe rollback window if a later state would make reversal unsafe;
- post-rollback verification.

Automatic rollback is permitted only when the rollback is deterministic, tested, reversible and within the task's action authority. Otherwise stop in a truthful failed/uncertain state and follow the governed recovery path.

Rollback acceptance requires restoration of the applicable functional/security/privacy invariants, not merely process uptime.

For the DNS service, rollback must preserve at minimum the approved resolver identity, encrypted DoH/DoT behavior, filtering policy, Quad9 dns10/ECS-off invariant, privacy logging/statistics controls, restricted administration/listeners, TLS and recovery evidence.

## 6. Drift and hand-edit control

Production must not accumulate undocumented configuration drift.

- Material manual changes are prohibited unless explicitly authorized for incident recovery or owner-only control-plane work.
- Any emergency/manual change that legitimately occurs must be captured, independently verified, and reconciled back into the owning GitHub configuration/runbook/evidence before it becomes an accepted baseline.
- Scheduled/continuous drift checks should compare live service/configuration identity with the approved versioned baseline using privacy-safe fields only.
- Drift detection must never require enabling DNS query history or client statistics.

A live state that differs materially from the canonical approved configuration is a deviation to investigate, not a new baseline by observation alone.

## 7. Documentation ownership

Documentation must be owned by the same responsibility boundary that owns the behavior it documents.

Minimum ownership classes:

| Document class | Owning responsibility | Required update trigger |
| --- | --- | --- |
| DNS deployment/configuration/recovery runbook | Network/SRE operations package | DNS/Nginx/AdGuard/config/recovery-path change |
| Security/privacy operational controls | Security/Privacy owning package | control, data-flow, logging, secret or exposure change |
| Web/app deployment/runbook | Software/Platform package once app exists | application/deployment/runtime change |
| User setup/removal/recovery instructions | Product/UX + owning platform/DNS interface | supported platform/mechanism/copy change |
| Architecture/interface contract | owning architecture/interface package | material boundary/API/topology change |
| Cost-control/report definition | Operations/Finance governance | resource scope/tag/budget/report-input change |

Every operationally required runbook must identify:

- purpose/scope;
- current owner;
- exact systems/components covered;
- prerequisites/authority;
- safe procedure;
- rollback/recovery;
- verification;
- secrets/privacy prohibitions;
- change/revalidation triggers.

Stale documentation discovered during execution is an actionable defect and must not be silently followed because it exists in Git.

## 8. Dependency update cadence

The goal is current, supported dependencies without churn for its own sake.

### 8.1 Detection/review cadence

Once a component is in active implementation/operation:

- **security advisories / vendor security notices:** automated or scheduled check at least weekly, plus immediate review when a material alert is received through an existing channel;
- **routine dependency/version availability:** consolidated review at least monthly;
- **OS security updates:** include in the existing weekly operational maintenance review from TSK-0538;
- **AdGuard, Nginx, certificate tooling and critical DNS dependencies:** review on vendor security/support events and at least monthly for available stable/security releases;
- **future web/app dependencies:** automated dependency/security scanning per change where available, plus monthly upgrade review.

These are review/detection cadences, not automatic-upgrade mandates.

### 8.2 Update decision

Apply an update only after assessing:

- security/support urgency;
- compatibility and behavior change;
- privacy/data-flow change;
- recovery/rollback compatibility;
- test coverage/evidence;
- action authority.

Critical actively exploited or severe applicable vulnerabilities receive priority over the routine cadence, but no fixed remediation duration is fabricated here. The current security task/incident authority determines urgency and whether emergency action is required.

Major/behavior-changing updates require the relevant regression gate before production reliance. Minor/security updates may be automated only when the WBS permits the action and rollback/verification are deterministic.

## 9. Cost-attribution tag contract

All Azure billable resources attributable to UseSafeWeb should be directly cost-identifiable wherever the resource type supports tags/cost reporting.

Minimum non-sensitive tag vocabulary:

- `Project=UseSafeWeb`
- `Environment=production|recovery|staging|development` as applicable to an actually existing approved environment;
- `Component=dns|webapp|backup|monitoring|shared` as applicable;
- `ManagedBy=owner|project-automation` according to actual control boundary;
- `Purpose=<small controlled operational category>` where needed for allocation.

Rules:

1. no personal data, participant identifiers, host secrets, credentials or security-sensitive values in tags;
2. tag values are low-cardinality controlled vocabulary, not free-form notes;
3. environment/component tags must reflect actual resource function rather than future intent;
4. cost analysis/reporting must verify tags on usage records; applying a resource-group/subscription tag alone does not prove child usage is tagged;
5. if Azure Cost Management tag inheritance is explicitly enabled by the owner, verify the resulting usage records rather than assuming inheritance;
6. unsupported/non-taggable charges are allocated by authoritative resource/subscription/invoice metadata and documented separately rather than omitted.

Current Microsoft Cost Management guidance states resource tags are not implicitly inherited from a parent resource group and only appear in usage data while applicable; Cost Management tag inheritance can be enabled but also has scope/resource limitations.

## 10. Budget and alert contract

### 10.1 Numeric amount authority

No current project authority supplied to TSK-0045 freezes an infrastructure monthly budget amount. Therefore:

- **current infrastructure budget amount: UNFROZEN / OWNER VALUE REQUIRED before a numeric Azure budget is claimed**;
- this NFR defines the mechanism and thresholds without inventing currency spend;
- GTM discretionary budget constraints are separate and must not be reused as infrastructure budget by inference.

### 10.2 Required budget behavior once amount is approved

For each materially independent Azure cost scope, create/maintain an owner-approved Cost Management budget where supported. Minimum notification logic:

- actual cost >= **50%** of approved period budget -> informational early-warning;
- actual cost >= **80%** -> review current month forecast/drivers;
- actual cost >= **100%** -> owner-visible over-budget alert and explicit corrective/accept decision;
- forecasted cost >= **100%** -> owner-visible forecast alert when Azure supports it for the scope.

Threshold percentages are control design; the currency amount remains owner authority.

Azure Cost Management budgets/notifications are **monitoring/accountability controls**. Current Microsoft guidance states a budget alert does not by itself stop resources or consumption. No service may be automatically terminated merely because a cost threshold fires unless a separate owner-approved safe action is explicitly designed, tested and authorized.

Cost data delay must be considered: current Azure guidance notes cost/usage data is typically available after processing delay and budgets are evaluated periodically, so budgets are not real-time circuit breakers.

## 11. Monthly cost-report inputs

During active operation, the monthly cost report must be reproducible from Azure Cost Management/billing evidence and include at minimum:

1. reporting period and billing scope/currency;
2. actual period cost and month-to-date cost where applicable;
3. approved budget amount/status if a numeric budget has been owner-frozen; otherwise explicitly `UNFROZEN` rather than zero;
4. forecasted period cost where Azure provides it;
5. variance versus approved budget and previous comparable period, with denominator explicitly available before calculating percentages;
6. cost by environment;
7. cost by component (`dns`, future `webapp`, backup, monitoring, shared/other);
8. material untagged/unallocated charge amount;
9. top material cost drivers/resources/services;
10. reservations/savings/credits/Marketplace effects where applicable to the invoice scope;
11. anomalies or unexpected step changes requiring investigation;
12. capacity/utilization context needed to interpret a resize/scale proposal without using customer browsing/query data;
13. approved/planned cost-changing actions and their authority/status;
14. unresolved cost-control deviations (missing tags, failed budget alert route, unsupported allocation);
15. evidence source/export timestamp and any known cost-data latency/incompleteness.

Do not fabricate per-user CAC/unit economics when real user/revenue/attribution denominators do not exist. Product/GTM economics remain owned by their respective packages.

## 12. Cost-review decision rules

A cost alert or monthly increase triggers analysis, not automatic degradation of critical controls.

Decision order:

1. verify the charge and cost-data freshness;
2. identify resource/component/usage driver;
3. check for accidental/idle/duplicate resources or misconfiguration;
4. remove waste only within applicable action authority and after confirming no required dependency;
5. optimize size/storage/retention only if reliability/security/privacy remain within accepted NFRs;
6. compare projected savings with engineering/operational risk;
7. request owner action for Azure control-plane or consequential spend changes outside AUTO_ALLOWED scope;
8. never lower security, encrypted DNS, privacy, backups/recovery or evidence quality merely to meet a budget percentage.

Near-zero-downtime HA/multi-node spend remains excluded until evidence justifies a governed architecture change.

## 13. Deployment/cost evidence retention

Durable GitHub evidence may retain only non-secret operational facts needed for reproducibility, such as:

- commit/artifact/config version;
- environment/host identity without credentials;
- deployment/run/test result;
- configuration hashes;
- cost totals/aggregates and non-sensitive resource categories;
- budget threshold outcomes;
- approved decisions.

Do not store Azure tokens, credentials, private keys, sensitive billing identifiers, raw invoice personal data, participant/customer data, DNS query history or secret-bearing environment exports in repository evidence.

## 14. Implementation assertions

A downstream deployment/operations implementation must prove at least:

1. production deployment is reproducible from versioned GitHub source plus approved protected inputs;
2. every material deployment binds exact source version and target identity;
3. same-environment deployment is serialized;
4. pre-state and rollback source exist before mutation;
5. workflow success alone cannot satisfy deployment acceptance;
6. target read-back and applicable regression determine success;
7. rollback restores functional/security/privacy invariants;
8. emergency/manual drift is reconciled into the owning canonical artifact before acceptance;
9. documentation owner and revalidation trigger exist for each critical runbook;
10. dependency/security review cadence is observable;
11. dependency update does not bypass compatibility/action-authority gates;
12. Azure cost tags contain no sensitive values and use controlled vocabulary;
13. tag presence is verified in cost/usage reporting rather than inferred from parent tags;
14. infrastructure numeric budget remains `UNFROZEN` until owner-authorized;
15. once approved, budget alerts fire at the defined actual/forecast thresholds or a documented equivalent;
16. budget alerts do not automatically stop critical resources without separate explicit safe authority;
17. monthly report includes actual/forecast/budget/component/environment/untagged/anomaly/action/evidence inputs;
18. unknown/missing cost data is not reported as zero;
19. no customer query/history data is required for deployment or cost control;
20. Azure control-plane actions remain owner-bound unless explicitly reopened.

## 15. Revalidation triggers

Reopen affected TSK-0045 requirements/evidence when:

- deployment topology/mechanism changes;
- future web/app is implemented;
- a new environment or Azure resource class is created;
- rollback/recovery format changes;
- GitHub deployment/security model changes materially;
- dependency/update tooling changes;
- owner freezes or changes infrastructure budget amounts;
- Azure Cost Management/tag/budget behavior changes materially;
- a cost attribution gap or deployment/rollback incident reveals a contract defect;
- an action-authority boundary is changed by the owner.

## 16. ACC-0045 traceability

ACC-0045 requires:

> Requirements define repeatable deployment, versioning, rollback, documentation ownership, dependency update cadence, cost tagging/budgets, and monthly cost-report inputs.

Coverage:

- **repeatable deployment:** §§2–3 define GitHub-canonical source, environment identity and deterministic verified sequence;
- **versioning:** §4 binds commits/artifact/config/dependency/environment identities and appropriate version semantics;
- **rollback:** §5 defines preplanned triggers/source/compatibility/verification;
- **documentation ownership:** §7 assigns responsibility classes and required runbook metadata;
- **dependency update cadence:** §8 defines weekly security/vendor checking and monthly consolidated dependency/version review without blind auto-upgrade;
- **cost tagging/budgets:** §§9–10 define safe tag vocabulary, inheritance verification, owner-authorized numeric budgets and non-destructive alert semantics;
- **monthly cost-report inputs:** §11 defines the complete reproducible input set without fabricated spend/unit economics.

## Stable task outcome candidate

**TSK-0045 result: PASS candidate for provisional internal L4 maintainability/deployment/cost-control-NFR definition only, subject to independent verification, GitHub read-back and runtime reconciliation.**

This result does not authorize deployment, Azure mutation/spend, a numeric infrastructure budget, future web/app implementation, participants, publication or launch.
