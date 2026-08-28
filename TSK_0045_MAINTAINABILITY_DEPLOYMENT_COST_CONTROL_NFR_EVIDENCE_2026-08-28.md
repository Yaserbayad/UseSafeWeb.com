# TSK-0045 — Maintainability/Deployment/Cost-Control NFR Verification Evidence

**Task:** TSK-0045 — Define maintainability, deployment, and cost-control NFRs  
**Acceptance:** ACC-0045  
**Verification:** VER-0045 — independent deployment/version/rollback/maintenance/cost audit  
**Evidence:** EVD-0045  
**Date:** 2026-08-28  
**Result:** PASS candidate pending GitHub read-back and guarded runtime reconciliation

## 1. Exact evidence index

- NFR contract: `TSK_0045_MAINTAINABILITY_DEPLOYMENT_COST_CONTROL_NFR_2026-08-28.md`
- Contract blob: `cec8ba92151318cc399586ea230ccc399eea6e8b`
- Contract creation commit: `9ad23a477cc4bf9bb92636ec3bfe7591f91aef84`
- Current selected runtime: `CURRENT_STATE.md` blob `94396bc060d990dd4e06e566d209a5f175a858e9`; TSK-0045 selected L4 / MEDIUM / A3 / AUTO_ALLOWED with TSK-0314 current PASS.
- WBS blob: `dce5b829c4d447eac180ae1e896e0019292cf971`.
- Current external authority checked 2026-08-28: GitHub deployment-environment/concurrency documentation and Microsoft Azure Cost Management tag/budget documentation.

## 2. Eligibility/scope audit

The post-TSK-0314 queue identified TSK-0045 as the only unflagged dependency-ready AUTO_ALLOWED L4 candidate. The guarded selector completed successfully before contract execution.

The contract defines requirements only. It does not make planning-era reconciliation workflows permanent production deployment architecture, mutate Azure, authorize spend, deploy the future app or activate participants/launch.

**Result: PASS.**

## 3. Repeatable-deployment audit

ACC-0045 requires repeatable deployment. Sections 2–3 define one versioned GitHub source path per deployable component and an 11-step deployment sequence covering source pin, target identity, authority, pre-state, recovery readiness, prechecks, bounded mutation, read-back, regression, evidence and runtime reconciliation.

The contract preserves the current direct-Ubuntu DNS baseline and separates the future web/app deployment boundary. Same-environment deployments must be serialized and successful command exit alone cannot satisfy acceptance.

Current GitHub documentation independently supports the use of deployment environments, branch/secret/protection restrictions and concurrency as available implementation controls.

**Result: PASS.**

## 4. Versioning audit

Section 4 requires each deployed state to bind Git commit SHA, artifact/config/service version where meaningful, material third-party dependency versions, environment identity and execution record.

It correctly uses SemVer only where an external application/API compatibility contract exists and keeps internal configuration/policy artifacts on explicit schema/artifact versions plus Git identity instead of forcing artificial SemVer.

**Result: PASS.**

## 5. Rollback/drift audit

Section 5 requires rollback design before deployment, including trigger, known-good source, protected inputs, schema/data compatibility, safe window and post-rollback verification. Automatic rollback is limited to deterministic/tested/authorized cases; otherwise the operation stops in a truthful failed/uncertain state.

Section 6 prevents undocumented production drift and requires emergency/manual changes to be verified and reconciled into the owning canonical GitHub source before acceptance. Drift detection does not require DNS-query/client history.

**Result: PASS.**

## 6. Documentation-ownership audit

Section 7 assigns documentation by owning responsibility rather than creating a parallel documentation owner. It covers DNS/SRE, security/privacy, future software/platform, user setup/product+platform, architecture/interface and operations/finance cost definitions.

Every critical runbook must include scope, owner, covered systems, prerequisites/authority, safe procedure, rollback/recovery, verification, privacy/secrets prohibitions and change triggers.

**Result: PASS.**

## 7. Dependency-update-cadence audit

Section 8 defines observable review cadences once a component is active:

- security/vendor notices at least weekly plus immediate review of received material alerts;
- routine dependency/version consolidation at least monthly;
- OS updates in the existing weekly TSK-0538 maintenance review;
- AdGuard/Nginx/certificate/DNS critical dependencies on security/support events plus monthly stable/security-release review;
- future app dependency/security scanning per change where available plus monthly upgrade review.

These are detection/review cadences, not blind automatic-upgrade mandates. Update action remains risk-, regression- and authority-gated; no fabricated fixed emergency remediation duration is introduced.

**Result: PASS.**

## 8. Cost-tag audit

Section 9 defines non-sensitive low-cardinality Azure tags for Project, Environment, Component, ManagedBy and controlled Purpose.

Current Microsoft Cost Management guidance confirms that tags used in cost/usage records are not simply guaranteed by resource-group/subscription placement: resource tags are not implicitly inherited to child resources, some resource types do not emit tags into cost data, and Cost Management tag inheritance is a separate configurable capability.

The NFR therefore correctly requires verification in actual usage/cost data and explicit treatment of untaggable/unallocated charges instead of assuming inheritance.

Tags explicitly prohibit personal data, participant identifiers, secrets and security-sensitive values.

**Result: PASS.**

## 9. Budget/alert audit

No current project authority freezes an infrastructure monthly currency amount. The contract truthfully records that amount as **UNFROZEN / OWNER VALUE REQUIRED** and refuses to reuse the separate GTM budget by inference.

Once a numeric infrastructure budget is owner-approved, the contract requires actual-cost alerts at 50%, 80% and 100% plus forecast-at-100% where supported.

Current Microsoft Azure Cost Management documentation confirms budgets support actual/forecast notifications and that budget threshold breaches do **not** by themselves stop Azure resources or consumption. The contract preserves this distinction and forbids automatic service termination without separate owner-approved safe action.

Cost-data processing latency is also recognized, so the budget is not treated as a real-time circuit breaker.

**Result: PASS.**

## 10. Monthly-cost-report audit

Section 11 defines 15 reproducible report inputs, including period/scope/currency, actual and MTD cost, budget status, forecast, variance, environment/component allocation, untagged charges, drivers, discounts/credits, anomalies, capacity context, planned changes, deviations and evidence timestamp/data latency.

It distinguishes `UNFROZEN`/missing data from zero and prohibits invented per-user economics when valid user/revenue denominators do not exist.

**Result: PASS.**

## 11. Cost-decision/security audit

Section 12 makes a cost alert an analysis trigger rather than permission to remove critical resources or weaken safeguards. Waste/size/storage optimization remains action-authority- and reliability/security/privacy-gated. Owner action is required for Azure control-plane/consequential spend outside AUTO_ALLOWED scope.

The single-node/no-HA baseline remains unchanged absent evidence-driven governed change.

**Result: PASS.**

## 12. Evidence/privacy audit

Section 13 restricts durable GitHub deployment/cost evidence to non-secret operational identities, hashes, versions, aggregate cost facts and decisions. Tokens, credentials, private keys, sensitive billing identifiers, raw invoice personal data, participant/customer data and DNS/query history are prohibited.

**Result: PASS.**

## 13. Verification disposition

**VER-0045 independent audit result: PASS for ACC-0045's provisional internal L4 maintainability/deployment/cost-control-NFR-definition scope.**

The read-back contract at blob `cec8ba92151318cc399586ea230ccc399eea6e8b` satisfies every ACC-0045 domain: repeatable deployment, versioning, rollback, documentation ownership, dependency update cadence, cost tagging/budget controls and monthly cost-report inputs.

The following remain OPEN/non-PASS and are not converted by this result:

- any future web/app deployment;
- Azure control-plane mutation or infrastructure purchase;
- an owner-approved numeric infrastructure budget;
- implementation of new cost tags/budgets/reports;
- real-user/behavioral evidence (`RSK-0002`);
- final legal/privacy/participant gates;
- publication/launch.

**Runtime may move TSK-0045 to PASS only after this evidence file is persisted/read back and guarded reconciliation verifies current selection, exact contract/evidence/WBS/runtime preconditions.**
