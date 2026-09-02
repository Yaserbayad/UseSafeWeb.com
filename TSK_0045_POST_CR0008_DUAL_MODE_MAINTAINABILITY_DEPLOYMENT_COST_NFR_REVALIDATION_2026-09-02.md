# TSK-0045 — Post-CR-0008 Dual-Mode Maintainability, Deployment and Cost-Control NFR Revalidation

**Task:** TSK-0045 — Define maintainability, deployment, and cost-control NFRs  
**Acceptance / Verification / Evidence:** ACC-0045 / VER-0045 / EVD-0045  
**Lifecycle / Priority / Authority:** L4 / MEDIUM / A3 / AUTO_ALLOWED  
**Version:** 2.0.0-post-CR0008  
**Date:** 2026-09-02 UTC  
**Candidate disposition:** ACC-0045 current PASS pending independent VER-0045 and guarded runtime reconciliation.

## 1. Current contract and revalidation boundary

Current ACC-0045 requires repeatable deployment, versioning, rollback, documentation ownership, dependency-update cadence, cost tagging/budgets, and monthly cost-report inputs.

Historical TSK-0045 already established a strong deterministic deployment/read-back/rollback/drift/documentation/dependency/cost-control contract. Revalidation is required because:

1. direct predecessor TSK-0314 is now current post-CR-0008 PASS and its accessibility/browser/device support obligations must remain deployment/release invariants;
2. CR-0006 activates optional parent sign-in/session, minimum device ownership persistence and dashboard/account-lifecycle components in addition to the complete accountless core;
3. CR-0007 removes a mandatory pilot/staging lifecycle and maximizes routine evidence-driven automation inside approved architecture/budget while retaining owner authority for named-market activation, new contracts, organizational/identity acts, material/unbudgeted spend and frozen-scope changes;
4. current Azure Cost Management/GitHub deployment-control facts are time-sensitive.

This task defines NFRs only. It does not create Azure resources, freeze a currency budget, deploy software, implement authentication/storage, buy services or authorize launch.

## 2. Deployment architecture and authority

### 2.1 Canonical source and deployment paths

GitHub `main` remains canonical durable source for approved code/configuration/runbooks/evidence. Every deployable service or configuration must have one reproducible, source-controlled deployment path.

Current DNS service:

- direct Ubuntu host deployment remains the accepted AdGuard/Nginx baseline unless an authorized architecture change supersedes it;
- exact source/configuration/dependency versions and target identity are bound before mutation;
- accepted DNS/TLS/filtering/privacy/security/recovery invariants are re-read after change.

Future web/account application when implemented:

- remains a separate application/service boundary from AdGuard administration;
- deployment, database/schema migration, auth-provider configuration and rollback are source-controlled/reconstructable without putting secrets in Git;
- the complete accountless core remains independently deployable/operable when the optional account provider/datastore is degraded where architecture permits;
- account/session/dashboard/device-management deployment cannot expose AdGuard administrative credentials or raw DNS query history.

### 2.2 Current action-authority split

- Owner-provided Azure VM/control-plane creation and other genuinely owner-only cloud/account/identity/contract acts remain owner-controlled under the frozen platform boundary.
- Routine reversible technical deployment, recovery, patching, scaling/tuning and already-budgeted operational action inside the approved architecture/scope are autonomous when current task/gate/security/privacy evidence permits them.
- Material/unbudgeted spend, new contracts/providers, organization/banking/merchant identity, named-market activation, irreversible owner-only acts or frozen-scope change remain human authority.
- No task may convert a human-only platform act into an automated one merely by documenting it here.

## 3. Repeatable deployment contract

Every material deployment/change implements, as applicable:

1. **source pin** — exact commit/artifact/config/schema and material dependency versions;
2. **target guard** — exact environment/host/site identity before privileged mutation;
3. **authority/gate check** — current task/action authority and applicable lifecycle gates permit the operation;
4. **pre-state capture** — current version/config/hash/service health plus rollback source;
5. **recovery readiness** — backup/restore or previous known-good material is available and proportionate to risk;
6. **pre-deploy validation** — syntax/schema/migration/compatibility checks before restart/destructive action;
7. **single bounded mutation** — no unrelated change bundled for convenience;
8. **target read-back** — exact intended state observed from target, never inferred from command/workflow success;
9. **regression** — affected functional, DNS, security, privacy, authorization, accessibility/browser/device, performance/reliability and recovery checks;
10. **evidence publication** — secret-safe immutable/reconstructable proof;
11. **runtime reconciliation** — authoritative state changes only after acceptance proof and GitHub read-back.

Same-target material deployments are serialized. Ambiguous consequential side effects are reconciled before replay rather than blindly retried.

No mandatory staging/pilot environment is created. Pre-release local/CI/synthetic/device/security/accessibility/performance/recovery verification remains mandatory where applicable; first actual users remain live-production users only after LG-09 and all applicable prerequisites.

## 4. Deployment environment identity and GitHub controls

Use only actually existing/approved targets such as:

- `production-dns`;
- `recovery-dns` when a recovery target actually exists;
- future `production-webapp`;
- temporary/local/CI test identities that truthfully describe non-production verification.

Do not create or claim a mandatory `staging` lifecycle/environment solely because historical TSK-0045 mentioned it.

GitHub Actions deployment environments may be used when they materially improve branch restrictions, deployment protection or environment-secret isolation. They supplement, not replace, WBS/gate/action authority. Environment names do not create Azure resources or prove deployment readiness.

Current GitHub documentation reviewed 2026-09-02: `https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments`.

## 5. Versioning and release identity

Every accepted deployed state is traceable to:

- Git commit SHA;
- artifact/config/schema/application version where meaningful;
- exact material third-party dependency/runtime versions;
- target/environment identity;
- deployment/test run or equivalent reconstructable execution record.

Use SemVer for a real public API/application interface when it provides compatibility meaning. Internal policies/configs use explicit schema/artifact versions plus Git identity. Generated outputs never outrank authoritative source.

AdGuard/Nginx/OS/web/auth/datastore dependencies remain pinned to accepted supported versions until their update passes applicable compatibility/security/privacy/recovery regression.

## 6. Rollback and migration contract

Rollback is designed before mutation. Each material change defines trigger, previous known-good state, protected restore input, data/schema compatibility, safe rollback window if relevant, and post-rollback verification.

DNS rollback preserves resolver identity, DoH/DoT/TLS, filtering, upstream/privacy configuration, restricted administration and recovery proof.

Web/account rollback additionally addresses:

- application/API and datastore schema compatibility;
- session/token/provider configuration compatibility;
- ownership/authorization and CSRF/session controls;
- account/device deletion and revoke/unlink terminal truth;
- background/outbox/idempotency/reconciliation state where implemented;
- accountless-core continuity when optional auth/provider/datastore paths fail.

Automatic rollback is allowed only when deterministic, tested, reversible and authorized. Otherwise retain truthful failed/uncertain state and execute governed recovery.

## 7. Drift and hand-edit control

Production must not accumulate undocumented material drift.

- emergency/manual changes require legitimate authority and later source/runbook/evidence reconciliation before becoming accepted baseline;
- drift checks use privacy-safe configuration/version/hash/health fields only;
- DNS query history, browsing/activity history, session secrets, provider tokens or credentials are never enabled/exposed merely for drift detection;
- account/datastore schema/config drift is treated as a deployment defect, not accepted by observation alone.

## 8. Documentation ownership

Critical documentation is owned by the responsibility boundary that owns the behavior.

| Document class | Owning responsibility | Update trigger |
| --- | --- | --- |
| DNS deploy/config/recovery | Network/SRE | DNS/Nginx/AdGuard/config/recovery change |
| Security/privacy controls | Security/Privacy | control/data-flow/logging/secret/exposure change |
| Web/app deployment | Software/Platform when implemented | app/runtime/deployment change |
| Auth/session/provider/datastore lifecycle | Security/Platform + owning architecture | provider/session/schema/ownership/deletion change |
| User setup/removal/recovery | Product/UX + platform/DNS owner | supported platform/mechanism/copy change |
| Accessibility/browser/device support | Product/UX/QA | TSK-0314 matrix/requirement change |
| Performance/reliability operations | SRE/Platform | TSK-0046/0538 boundary change |
| Cost control/report definition | Operations/Finance governance | resource/tag/budget/report-input change |

Every operational runbook records purpose/scope, owner, systems, prerequisites/authority, safe procedure, rollback/recovery, verification, secret/privacy prohibitions and revalidation triggers. Stale documentation is a defect and is not followed merely because it exists in Git.

## 9. Dependency update cadence

Once a component is actively implemented/operated:

- applicable security advisories/vendor security notices: scheduled check at least weekly plus prompt review of material alerts received through existing channels;
- routine stable dependency/version availability: consolidated review at least monthly;
- OS security updates: current weekly operational review cadence;
- AdGuard/Nginx/certificate/DNS critical dependencies: vendor security/support event review plus monthly stable/security-release review;
- future web/auth/datastore dependencies: per-change automated security/dependency checks where available plus monthly upgrade review.

These are detection/review cadences, not automatic-upgrade mandates. Updates require compatibility, security/privacy, schema/data-flow, rollback/recovery and current action-authority review. Severe actively exploited issues outrank the routine cadence without fabricating a universal remediation deadline.

## 10. Cost attribution/tag contract

Use non-sensitive low-cardinality Azure tags where supported, such as:

- `Project=UseSafeWeb`;
- `Environment=production|recovery|development|test` only for actually existing roles;
- `Component=dns|webapp|auth|datastore|backup|monitoring|shared` as applicable;
- `ManagedBy=owner|project-automation` according to actual control authority;
- controlled `Purpose` category when needed.

No personal/participant data, credentials, host secrets, security-sensitive values, raw billing identifiers or free-form operational notes belong in tags.

Current Microsoft Cost Management review on 2026-09-02 confirms:

- resource tags are not implicitly inherited from parent resource groups in cost/usage data;
- Cost Management tag inheritance can apply subscription/resource-group tags to child **usage records** at supported scopes when explicitly enabled;
- inherited-tag updates can take roughly 8–24 hours and apply to current-month usage records under the documented rules;
- unsupported/non-usage charges may not receive inherited tags.

Therefore cost attribution must verify the resulting usage/cost data rather than assume tag propagation.

Sources:
- `https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/understand-cost-mgt-data`
- `https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/enable-tag-inheritance`

## 11. Budget and alert contract

**Current infrastructure currency budget: UNFROZEN.** No numeric Azure monthly budget is invented by this task.

Once an applicable owner-approved/current budget exists, the historical control percentages remain the internal default unless newer budget authority supersedes them:

- actual >=50% — early informational warning;
- actual >=80% — review forecast/drivers;
- actual >=100% — visible over-budget alert and governed corrective/accept decision;
- forecast >=100% — forecast alert where supported.

Azure Cost Management budget/alert behavior is monitoring/accountability evidence, not permission to terminate resources or weaken critical service controls. Any automated cost response must have separate current authority, safe rollback and service-impact verification.

Microsoft Cost Management documentation reviewed 2026-09-02 continues to expose budgets, cost alerts, forecast spend and periodic budget time grains. Source root: `https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/`.

## 12. Monthly cost-report inputs

For active operation, reproducible monthly cost reporting includes at minimum:

1. reporting period, billing scope and currency;
2. actual period/MTD cost where applicable;
3. current approved budget or explicit `UNFROZEN`;
4. forecast cost where available;
5. variance versus valid budget/previous comparable period only when denominators exist;
6. cost by environment;
7. cost by component including DNS/webapp/auth/datastore/backup/monitoring/shared when applicable;
8. untagged/unallocated material charges;
9. top cost drivers/resources/services;
10. credits/reservations/savings/Marketplace effects where applicable;
11. anomalies/unexpected changes;
12. capacity/utilization context relevant to governed resize/scale analysis without DNS/browsing history;
13. approved/planned cost-changing actions with authority/status;
14. tag/budget/reporting deviations;
15. evidence/export timestamp and known cost-data latency/incompleteness.

Do not fabricate per-user unit economics, CAC, revenue attribution or account value without owning evidence.

## 13. Cost/deployment decision order

1. verify source/target/cost-data freshness;
2. diagnose deployment or cost driver;
3. remove proven waste/defect only within current action authority;
4. preserve reliability/security/privacy/accessibility/performance/recovery constraints;
5. execute routine reversible approved-architecture/budget remediation autonomously when allowed;
6. obtain owner authority for new Azure resource/control-plane acts, material/unbudgeted spend, contracts or frozen-scope changes;
7. rerun affected regression/read-back;
8. publish secret-safe proof and reconcile runtime only after verified outcome.

Do not reduce encryption, filtering, privacy, authorization, accessibility, backups/recovery or evidence quality to satisfy cost/performance pressure.

## 14. Implementation assertions

A downstream implementation/operations plan must prove at least:

1. deployment is reproducible from versioned source plus approved protected inputs;
2. exact source and target identity are bound;
3. same-target material deployments are serialized;
4. pre-state/rollback source exist before mutation;
5. workflow success alone is not deployment acceptance;
6. target read-back and applicable regression determine success;
7. accountless core and optional account components have explicit failure/rollback relationships;
8. schema/session/provider/ownership changes have safe migration/reconciliation semantics;
9. emergency/manual drift is reconciled;
10. documentation owners/triggers exist;
11. security/dependency review cadence is observable;
12. dependency updates do not bypass compatibility/action-authority gates;
13. Azure tags contain no sensitive values;
14. usage records, not parent-tag assumptions, prove cost attribution;
15. numeric infrastructure budget remains `UNFROZEN` until current authority freezes one;
16. budget alerts do not automatically terminate critical resources without separate authority;
17. monthly reporting exposes actual/forecast/budget/component/environment/untagged/anomaly/action/evidence inputs;
18. missing/late cost data is not reported as zero;
19. no DNS/browsing/activity history or unnecessary persistent identity is required for deployment/cost evidence;
20. TSK-0314 accessibility/browser/device support and TSK-0046/0538 performance/reliability constraints remain regression invariants.

## 15. Revalidation triggers

Reopen affected proof when deployment topology/mechanism changes; web/auth/datastore implementation materially changes; a new environment or Azure resource class is introduced; rollback/schema/recovery formats change; GitHub deployment/security model changes materially; dependency/update tooling changes; infrastructure budget authority changes; Azure Cost Management tag/budget behavior changes materially; a deployment/cost-control incident exposes a defect; TSK-0314 or TSK-0046/0538 current requirements change; or action-authority boundaries change.

## 16. ACC-0045 traceability

- repeatable deployment — §§2–4;
- versioning — §5;
- rollback — §6;
- documentation ownership — §8;
- dependency update cadence — §9;
- cost tagging/budgets — §§10–11;
- monthly cost-report inputs — §12.

## 17. Non-inference

This L4 NFR-definition revalidation does not deploy/resize/create/delete Azure resources, freeze a numeric budget, build the web/auth/datastore stack, purchase services, complete legal/privacy work, process participants, publish, activate a market, launch, or infer any successor/gate PASS.

**TSK-0045 current result candidate: PASS, subject to independent verification, durable evidence publication, guarded runtime reconciliation and exact GitHub read-back.**
