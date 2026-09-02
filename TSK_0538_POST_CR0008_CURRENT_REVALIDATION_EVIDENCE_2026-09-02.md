# TSK-0538 — Post-CR-0008 Dual-Mode Reliability NFR Revalidation Acceptance Evidence

**Task:** TSK-0538 — Define reliability, observability, recovery, and service-level NFRs  
**Acceptance / Verification / Evidence:** ACC-0538 / VER-0538 / EVD-0538  
**Lifecycle / Priority / Authority:** L4 / MEDIUM / A3 / AUTO_ALLOWED  
**Evidence date:** 2026-09-02 UTC  
**Disposition:** CURRENT PASS — subject only to guarded runtime reconciliation and independent read-back.

## 1. Current accepted artifact

- `TSK_0538_POST_CR0008_DUAL_MODE_RELIABILITY_OBSERVABILITY_NFR_REVALIDATION_2026-09-02.md`
- version `2.0.0-post-CR0008`
- blob `44c9c299465e821e2ffd84a54b77e3e615d61925`
- publication commit `7559ded680625af640f6d7797bd296afc97a9b31`

The artifact preserves the accepted lean single-node DNS/accountless reliability baseline and adds only the reliability/observability/recovery boundaries made current by optional parent account/session, parent-device ownership, provider/datastore dependencies and consequential mutation reconciliation.

## 2. Current WBS and direct predecessor proof

Independent VER-0538 used:

- WBS `Plans/Master/WBS/master-wbs.csv`, blob `b27a0c5df2f5636d8ed71051e9e26a68959a2616`;
- graph `Plans/Master/RELATIONSHIP_INDEX.yaml`, blob `c108d2c162bcea2ee4cc01def46d0487a9501032`;
- pre-reconciliation runtime `CURRENT_STATE.md`, blob `db1f55f6d78e2408bab515fa6bcddd0c6cb5ac20`.

It proved:

- L4 / MEDIUM / A3 / `AUTO_ALLOWED`;
- sole hard dependency `TSK-0484`;
- `ACC-0538 / VER-0538 / EVD-0538`;
- current acceptance requires critical user journeys, provisional SLI/SLOs, alerts, recovery objectives, backup scope, restore test, maintenance behavior and escalation ownership.

Current TSK-0484 POST-CR-0008 security NFR revalidation was independently found as durable PASS. Verifier markers:

- `TSK0538_CURRENT_WBS_CONTRACT=PASS`;
- `TSK0538_CURRENT_TSK0484_PREDECESSOR=PASS`.

## 3. Historical accountless-only gap proved

Historical accepted contract:

- `TSK_0538_RELIABILITY_OBSERVABILITY_RECOVERY_SERVICE_LEVEL_NFR_2026-08-28.md`;
- blob `d81537ef3ef66789528336e101d1e05f30030892`.

Historical evidence:

- `TSK_0538_RELIABILITY_OBSERVABILITY_RECOVERY_SERVICE_LEVEL_NFR_EVIDENCE_2026-08-28.md`;
- blob `bd7a9f0d8a54dd28d423587257f1cd226b3e5dbc`.

The structural verifier proved the historical future-web/app critical journey is `Accountless web/app start -> setup -> Protection Map` and that its critical-journey section contains no Optional sign-in, Dashboard/device read, Auth provider failure or Datastore/ownership failure journey. These now-active boundaries are supplied by current TSK-0484 / CR-0006 scope.

Verifier markers:

- `TSK0538_HISTORICAL_ACCOUNTLESS_ONLY_APP_GAP=PASS`;
- `TSK0538_CURRENT_DEPENDENCY_GAP_CLOSURE=PASS`.

This establishes a genuine current acceptance-boundary revalidation rather than a date-only refresh.

## 4. Current critical journeys and on-call questions

The current artifact defines exactly 12 critical journey/failure rows:

1. DoH transaction;
2. DoT transaction;
3. accountless start → setup → verification → Protection Map;
4. accountless recovery/removal;
5. optional sign-in → session establish/refresh;
6. dashboard/device read;
7. device register/update/unlink/delete;
8. logout/session revoke;
9. account deletion;
10. authentication-provider failure;
11. datastore/ownership failure;
12. AdGuard control/verification failure.

Each row has an explicit success boundary and truthful failure/degraded boundary.

The artifact also defines exactly 13 bounded on-call questions spanning DNS/accountless core, optional account/session/dashboard, dependency attribution, consequential-mutation reconciliation, recovery and accepted-version/configuration evidence.

Verifier markers:

- `TSK0538_12_CRITICAL_JOURNEYS=PASS`;
- `TSK0538_13_ONCALL_QUESTIONS=PASS`.

## 5. Current signal/cardinality/privacy contract

Current bounded signal contract includes:

- privacy-safe black-box/synthetic checks;
- bounded RED-style request/operation rate, error/outcome rate and latency histograms;
- bounded dependency outcome/latency for auth provider, datastore, AdGuard control and protection verification;
- bounded mutation/reconciliation and authorization-denial counters;
- structured diagnostic logs with correlation context;
- optional vendor-neutral tracing only when cross-service topology makes it useful.

High-cardinality or privacy-sensitive metric labels are explicitly prohibited, including parent/account/user IDs, email, IP, journey/session token, Firebase/provider subject, device ID/ClientID, raw URL/query strings, DNS/domain/query data and free-text content. Correlation IDs are diagnostic fields, not metric labels or durable customer identities.

Verifier marker: `TSK0538_SIGNAL_AND_CARDINALITY_CONTRACT=PASS`.

## 6. Current SLI/SLO contract

The structural verifier proved exactly 14 current provisional internal SLI/SLO rows covering:

- DoH availability;
- DoT availability;
- DNS correctness;
- DNS latency;
- TLS validity;
- accountless web critical-path availability;
- accountless route latency;
- optional session-establishment availability;
- dashboard/device-read availability;
- account mutation terminal-truth correctness;
- authorization isolation;
- accountless fallback during auth/provider failure;
- recovery objective attainment;
- telemetry critical-path coverage.

The contract preserves historical `>=99.9%` availability and p95/p99 latency targets where applicable, requires `100%` correctness for authorization isolation / account-mutation terminal truth / accountless fallback failure fixtures, and explicitly treats these as internal provisional engineering targets rather than public/customer SLAs.

Verifier marker: `TSK0538_14_PROVISIONAL_SLI_SLO_CONTRACTS=PASS`.

## 7. Alert / recovery / backup / maintenance acceptance

Independent verification proved:

- PAGE vs TICKET severity is explicit;
- paging is symptom-centered and includes accountless failure, optional account critical failure, authorization isolation, deletion/revoke resurrection/live-authority failure and current security/privacy invariant failure;
- tickets cover actionable non-immediate drift, error-budget burn and telemetry blind spots;
- every alert identifies affected journey, symptom, first diagnostic check, owner and runbook;
- DNS RTO `<=30 minutes` is preserved;
- provisional accountless app RTO `<=30 minutes` is defined without inferring HA spend;
- third-party auth-provider recovery time is not fabricated; fail-closed/accountless-fallback/restoration proof is the operability objective;
- persistent ownership/delete/revoke recovery permits zero security-authority regression;
- ambiguous consequential mutation produces reconcile-required state rather than automatic replay/success;
- backup/restore excludes DNS/query/domain/browsing history, J0/J1, raw events, bearer/session material and provider/service-account secrets;
- 12 restore-verification assertions include accountless critical path, ownership isolation, non-resurrection, no silent replay, telemetry restoration and recovery-objective measurement;
- material auth/provider/schema/ClientID/delete/revoke/observability/security/recovery changes reopen affected validation;
- incident/escalation ownership covers eight distinct operational domains.

Verifier markers:

- `TSK0538_ALERT_CONTRACT=PASS`;
- `TSK0538_RECOVERY_OBJECTIVES=PASS`;
- `TSK0538_BACKUP_RESTORE_CONTRACT=PASS`;
- `TSK0538_MAINTENANCE_REVALIDATION_TRIGGERS=PASS`;
- `TSK0538_ESCALATION_OWNERSHIP=PASS`.

## 8. Current external engineering-source bindings

Current 2026-09-02 review is recorded against:

- Google SRE Monitoring Distributed Systems — `https://sre.google/sre-book/monitoring-distributed-systems/`;
- Google SRE Workbook Implementing SLOs — `https://sre.google/workbook/implementing-slos/`;
- OpenTelemetry observability primer — `https://opentelemetry.io/docs/concepts/observability-primer/`;
- OpenTelemetry signals — `https://opentelemetry.io/docs/concepts/signals/`;
- OpenTelemetry metrics — `https://opentelemetry.io/docs/concepts/signals/metrics/`;
- OpenTelemetry logging specification — `https://opentelemetry.io/docs/specs/otel/logs/`;
- Prometheus metric/label naming — `https://prometheus.io/docs/practices/naming/`.

These sources support symptom/user-journey-centered monitoring, provisional SLOs, distinct metrics/logs/traces, histogram latency measurement, structured/correlated logs and bounded label cardinality. They do not select or deploy a monitoring vendor/backend.

Verifier marker: `TSK0538_CURRENT_SOURCE_BINDINGS=PASS`.

## 9. Independent VER-0538

Authoritative final verifier is separated into:

- script `.github/scripts/verify_tsk0538_current_revalidation.py`, blob `b71a66bfac3584d52cc7b3f16c5096962c1a3d2c`;
- workflow `.github/workflows/verify-tsk0538-current-revalidation-v2.yml`, blob `a92aed2c2ccef8b2d9f706995dfedc5d454254df`;
- GitHub-hosted Ubuntu 24.04;
- workflow permission `contents: read`;
- run/job `33579914315 / 100091795138`;
- conclusion **SUCCESS**.

Final terminal markers:

- `TSK0538_IMMUTABLE_INPUT_HASHES=PASS`;
- `TSK0538_CURRENT_WBS_CONTRACT=PASS`;
- `TSK0538_CURRENT_TSK0484_PREDECESSOR=PASS`;
- `TSK0538_HISTORICAL_ACCOUNTLESS_ONLY_APP_GAP=PASS`;
- `TSK0538_CURRENT_DEPENDENCY_GAP_CLOSURE=PASS`;
- `TSK0538_12_CRITICAL_JOURNEYS=PASS`;
- `TSK0538_13_ONCALL_QUESTIONS=PASS`;
- `TSK0538_SIGNAL_AND_CARDINALITY_CONTRACT=PASS`;
- `TSK0538_14_PROVISIONAL_SLI_SLO_CONTRACTS=PASS`;
- `TSK0538_ALERT_CONTRACT=PASS`;
- `TSK0538_RECOVERY_OBJECTIVES=PASS`;
- `TSK0538_BACKUP_RESTORE_CONTRACT=PASS`;
- `TSK0538_MAINTENANCE_REVALIDATION_TRIGGERS=PASS`;
- `TSK0538_ESCALATION_OWNERSHIP=PASS`;
- `TSK0538_CURRENT_SOURCE_BINDINGS=PASS`;
- `TSK0538_CURRENT_ACCEPTANCE_ASSERTIONS=PASS`;
- `TSK0538_CURRENT_ACC=PASS`.

## 10. Diagnostic-only verifier run

Initial read-only inline VER-0538 run/job `33579806900 / 100091473798` passed immutable inputs, exact WBS, current TSK-0484, historical accountless-only gap, current gap closure, all 12 journeys, 13 on-call questions, signal/cardinality and all 14 SLI/SLO rows. It then failed only because the alert matcher expected literal `deleted/revoked` while the accepted contract correctly expresses the security condition as `deletion/revoke` plus `resurrected or still-live authority`.

The accepted artifact was unchanged. The final verifier moved to a structural script and required both actual alert semantics. No requirement was weakened and no governed state changed during the failed run.

## 11. Final ACC / VER / EVD disposition

1. Current direct dependency and WBS contract — **PASS**.
2. Historical accountless-only future-app gap — **PASS**.
3. Current dual-mode reliability gap closure — **PASS**.
4. Twelve critical journeys and thirteen bounded on-call questions — **PASS**.
5. Signal/cardinality/privacy contract — **PASS**.
6. Fourteen provisional measurable SLI/SLOs — **PASS**.
7. PAGE/TICKET actionable alert contract — **PASS**.
8. DNS/accountless/provider/persistent-state recovery objectives — **PASS**.
9. Privacy-minimal backup and 12-step restore verification — **PASS**.
10. Material-change maintenance/revalidation triggers — **PASS**.
11. Eight-domain incident/escalation ownership — **PASS**.
12. Current external source bindings and no-vendor-selection boundary — **PASS**.
13. No TSK-0352/TSK-0353 implementation or successor PASS inferred — **PASS**.

**ACC-0538 = PASS. VER-0538 = PASS. EVD-0538 = SATISFIED.**

**TSK-0538 current dual-mode reliability/observability/recovery/service-level NFR revalidation: PASS.**

## 12. Non-inference

This proves current L4 reliability/observability/recovery/service-level NFR definition acceptance only. It does not prove telemetry implementation, monitoring backend/collector, HA topology, auth/provider/datastore implementation, production SLO attainment, target-environment incident/recovery results, public SLA, legal/privacy completion, TSK-0352, TSK-0353, any later task/gate, participant processing, publication, payment, market activation or launch.
