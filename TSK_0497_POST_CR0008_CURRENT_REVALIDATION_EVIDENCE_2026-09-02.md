# TSK-0497 — Current Dual-Mode Product Event and KPI Revalidation Acceptance Evidence

**Task:** TSK-0497 — Define minimal product event and KPI catalogue  
**Acceptance / Verification / Evidence:** ACC-0497 / VER-0497 / EVD-0497  
**Lifecycle / Priority / Authority:** L4 / MEDIUM / A3 / AUTO_ALLOWED  
**Evidence date:** 2026-09-02 UTC  
**Disposition:** CURRENT PASS — subject only to guarded runtime reconciliation and exact GitHub read-back.

## 1. Current accepted artifact

- `TSK_0497_POST_CR0008_DUAL_MODE_PRODUCT_EVENT_KPI_CATALOGUE_REVALIDATION_2026-09-02.md`
- version `2.0.0-post-CR0008`
- blob `8c3b26ad0771b09a7e223ffc47f5e81b0ca217c7`
- publication commit `26f8720d7a209aa70bdfb73c8ceee456570db97a`

The artifact revalidates the historical aggregate-by-design KPI contract for the current dual-mode Version-1 scope. It preserves the complete accountless measurement/privacy boundary and removes the obsolete pre-CR-0006 assumption that all account/login/dashboard-related events are categorically out of scope. It does not activate telemetry or approve any new optional-account event schema.

## 2. Canonical input identity

Independent VER-0497 checked the following immutable current inputs:

- `Plans/Master/WBS/master-wbs.csv` — blob `b27a0c5df2f5636d8ed71051e9e26a68959a2616`;
- `Plans/Master/RELATIONSHIP_INDEX.yaml` — blob `c108d2c162bcea2ee4cc01def46d0487a9501032`;
- pre-reconciliation `CURRENT_STATE.md` — blob `c50c9c119f4cd1b1ed0258292a4cda34639cf20e`;
- historical TSK-0497 catalogue — blob `61bcd78bbe7ac2446c9c79e5e2e0765cb4f66b8c`;
- historical TSK-0497 evidence — blob `b26a4cb123929518b7875023530f37256612ac98`;
- current TSK-0230 privacy/data-minimisation/retention/deletion NFR — blob `eda85b062a3a7ba29544de35a8a813c9790092f2`;
- current TSK-0498 privacy-safe decision-linked event contract — blob `6b7a5095122c74ed9ec860b74408dab474576659`.

Verifier marker: `TSK0497_INPUT_HASHES=PASS`.

## 3. Current WBS and dependency proof

VER-0497 parsed the canonical WBS and proved:

- Lifecycle Stage `L4`;
- Priority `MEDIUM`;
- AI capability `A3`;
- Action Authority `AUTO_ALLOWED`;
- direct dependency exactly `TSK-0230`;
- acceptance/verification/evidence IDs exactly `ACC-0497 / VER-0497 / EVD-0497`;
- ACC requires approved purpose, privacy-safe accountless events, minimum-authorised optional-account identifiers only where actually necessary, prohibition of DNS/domain browsing history, child activity, raw tokens/secrets and unnecessary identity, and explicit retention/access/deletion.

Verifier marker: `TSK0497_CURRENT_WBS=PASS`.

Current runtime independently contained current accepted PASS states for TSK-0230 and TSK-0498. Marker: `TSK0497_CURRENT_PRIVACY_EVENT_AUTHORITIES=PASS`.

## 4. Current schema ownership and event catalogue

The current artifact does not create a second event-schema authority. TSK-0498 remains the current L5 event-schema authority and unknown event names/fields fail closed.

VER-0497 structurally proved all twelve currently approved event names are represented and that the catalogue carries the required purpose/prohibition/collection-point/denominator/retention/access metadata.

Markers:

- `TSK0497_STRUCTURE=PASS`;
- `TSK0497_TSK0498_SCHEMA_ALIGNMENT=PASS`;
- `TSK0497_APPROVED_EVENT_METADATA=PASS`.

## 5. Accountless privacy and retention boundary

The verifier proved the current artifact preserves the accountless architecture:

- no stable analytics user/account/device/household identity or fingerprint;
- short-lived accountless linkage with a maximum 24-hour raw boundary;
- sign-in cannot extend or link accountless event history;
- non-linkable aggregate retention bounded by the current TSK-0498 contract;
- synthetic reliability data remains user/client-identity free and separately bounded;
- cost analytics remains aggregate-only;
- DNS qname/domain/URL/browsing/search/child-activity/free-text/raw-diagnostic content is excluded;
- unknown/high-cardinality fields fail closed.

Marker: `TSK0497_ACCOUNTLESS_PRIVACY_RETENTION=PASS`.

## 6. Optional-account current-scope reconciliation

CR-0006 makes optional parent account/session/dashboard/device-management capability current product scope, but does not make account identity an analytics identity.

VER-0497 proved:

- product analytics defaults to zero account/device identifiers;
- account email, provider subject, AdGuard ClientID, session/token identifiers and ownership keys are not product-analytics dimensions;
- an identifier genuinely required for security/lifecycle/operation belongs to its operational/security authority rather than silently becoming product analytics;
- no new optional-account event is approved implicitly;
- optional-account KPI rows remain dormant until an approved source/event contract exists;
- account/session/device operational logs cannot be repurposed as product analytics.

Markers:

- `TSK0497_OPTIONAL_ACCOUNT_BOUNDARY=PASS`;
- `TSK0497_OPTIONAL_KPI_DORMANCY=PASS`.

## 7. Prohibited measurement and KPI quality

VER-0497 proved the current contract prohibits DNS/browsing/search history, child activity, raw IP analytics, session replay, attention/addictive-engagement metrics, cross-session/cross-device identity graphs and marketing/advertising profiles.

It also structurally proved ten current accountless/product KPI rows with source, formula/denominator, window/cohort, owner, guardrail and decision action, plus data-quality rules that prevent absence/missing data from being silently converted into a negative or success result.

Markers:

- `TSK0497_PROHIBITED_MEASUREMENT=PASS`;
- `TSK0497_KPI_CATALOGUE=PASS`;
- `TSK0497_QUALITY_ACCESS_DELETION=PASS`.

## 8. Historical/current reconciliation

The historical TSK-0497 artifact explicitly depended on EXC-0001 remaining inactive and prohibited account/login/password-reset/dashboard events under that older boundary. The current artifact removes that obsolete assumption while preserving compatible aggregate-by-design and non-surveillance rules. Historical event names outside the current TSK-0498 allowlist remain provenance only and are not independently collection-approved.

Marker: `TSK0497_HISTORICAL_CURRENT_RECONCILIATION=PASS`.

## 9. Independent VER-0497

Independent read-only verifier:

- script `.github/scripts/verify_tsk0497_current_revalidation.py` — blob `c1b85b059b74b8a1d1d3b660ab75ff6c4d325cab`;
- workflow `.github/workflows/verify-tsk0497-current-revalidation.yml` — blob `b0ea2fc03440862496f748a1bf5701272d26b77a`;
- workflow permission: `contents: read` only;
- GitHub-hosted Ubuntu 24.04 LTS;
- run `33583778318`;
- job `100103488785`;
- conclusion: **SUCCESS**.

Final verifier markers:

- `TSK0497_INPUT_HASHES=PASS`;
- `TSK0497_CURRENT_WBS=PASS`;
- `TSK0497_CURRENT_PRIVACY_EVENT_AUTHORITIES=PASS`;
- `TSK0497_STRUCTURE=PASS`;
- `TSK0497_TSK0498_SCHEMA_ALIGNMENT=PASS`;
- `TSK0497_ACCOUNTLESS_PRIVACY_RETENTION=PASS`;
- `TSK0497_OPTIONAL_ACCOUNT_BOUNDARY=PASS`;
- `TSK0497_PROHIBITED_MEASUREMENT=PASS`;
- `TSK0497_APPROVED_EVENT_METADATA=PASS`;
- `TSK0497_OPTIONAL_KPI_DORMANCY=PASS`;
- `TSK0497_KPI_CATALOGUE=PASS`;
- `TSK0497_QUALITY_ACCESS_DELETION=PASS`;
- `TSK0497_HISTORICAL_CURRENT_RECONCILIATION=PASS`;
- `TSK0497_NON_INFERENCE=PASS`;
- `TSK0497_CURRENT_ACC=PASS`;
- `TSK0497_CURRENT_VER=PASS`;
- `TSK0497_CURRENT_EVD_READY=PASS`;
- `TSK0497_CURRENT_REVALIDATION=PASS`.

## 10. Acceptance disposition

1. Current WBS/dependency contract — **PASS**.
2. Current privacy/event authorities — **PASS**.
3. Current dual-mode schema ownership and event metadata — **PASS**.
4. Accountless privacy/retention boundary — **PASS**.
5. Optional-account least-data boundary and dormant unapproved KPI sources — **PASS**.
6. Prohibited surveillance/identity measurement classes — **PASS**.
7. KPI definitions, denominators, guardrails, access/deletion and data-quality rules — **PASS**.
8. Historical pre-CR-0006 conflict correctly reconciled — **PASS**.
9. Non-inference boundaries — **PASS**.

**ACC-0497 = PASS. VER-0497 = PASS. EVD-0497 = SATISFIED.**

**TSK-0497 current dual-mode revalidation: PASS, pending only durable runtime reconciliation/read-back.**

## 11. Non-inference

This is L4 measurement/KPI contract acceptance only. It does not activate telemetry, approve a datastore or analytics vendor, approve a new optional-account event, create a lawful basis, authorize real-user processing, prove KPI values, implement authentication/analytics, process participants, publish, activate a market, launch, pass a lifecycle gate or infer any successor PASS.
