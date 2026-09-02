# TSK-0044 — Current Dual-Mode AdGuard API Compatibility/Credential/Failure NFR Revalidation Evidence

**Task:** TSK-0044 — Define AdGuard API compatibility, credential-isolation and failure NFRs  
**Acceptance / Verification / Evidence:** ACC-0044 / VER-0044 / EVD-0044  
**Lifecycle / Priority / Authority:** L4 / MEDIUM / A3 / AUTO_ALLOWED  
**Evidence date:** 2026-09-02 UTC  
**Disposition:** CURRENT PASS — subject only to guarded runtime reconciliation and exact GitHub read-back.

## 1. Current accepted artifact

- `TSK_0044_POST_CR0008_DUAL_MODE_ADGUARD_API_COMPATIBILITY_CREDENTIAL_FAILURE_NFR_REVALIDATION_2026-09-02.md`
- version `2.0.0-post-CR0008`
- blob `9e2df58093c592621eb1531dc1c34393a247dd80`
- publication commit `2c14ee2539f3e85cd3fe7e2ed7d7c7a7b73dce9e`

The artifact preserves the proven v0.107.79 private-control/credential/privacy/retry/reconciliation contract and replaces only the stale pre-CR-0006 accountless-only assumptions with the current dual-mode optional-account/device lifecycle constraints.

## 2. Canonical input identity

Independent VER-0044 hash-locked:

- WBS `Plans/Master/WBS/master-wbs.csv` — `b27a0c5df2f5636d8ed71051e9e26a68959a2616`;
- relationship graph — `c108d2c162bcea2ee4cc01def46d0487a9501032`;
- pre-reconciliation runtime — `934a911d491e657f5cfe4991ad6217dc3d447509`;
- current TSK-0044 artifact — `9e2df58093c592621eb1531dc1c34393a247dd80`;
- historical TSK-0044 contract — `07ab5539d11ff25d591adeada34e7f30854caa90`;
- historical TSK-0044 evidence — `19355b7b9ea2bac219ccf79ef9cbfd588cc56ba4`;
- current TSK-0484 security NFR — `285ee390499190137e8aac0fed976975fb79ed80`;
- current TSK-0538 reliability NFR — `44c9c299465e821e2ffd84a54b77e3e615d61925`;
- current TSK-0146 Version-1 product baseline — `9d3870d90add696fc352829fb4763c834b8d09af`.

Marker: `TSK0044_INPUT_HASHES=PASS`.

## 3. Current WBS and dependency proof

VER-0044 parsed the canonical WBS and proved:

- L4 / MEDIUM / A3 / `AUTO_ALLOWED`;
- hard dependencies exactly `TSK-0484; TSK-0538; TSK-0146`;
- IDs exactly `ACC-0044 / VER-0044 / EVD-0044`;
- current ACC requires private/restricted AdGuard administration, secret storage/rotation, timeout/retry limits, partial-failure reconciliation, opaque setup/ClientID constraints, explicit privacy booleans, version/contract regression checks, optional customer authentication/session and minimum persistence boundaries, safe failure behavior across AdGuard/auth/datastore/verification, and no mandatory login for core value.

All three direct predecessor task records were proven durable PASS from current runtime.

Markers:

- `TSK0044_CURRENT_WBS=PASS`;
- `TSK0044_CURRENT_PREDECESSORS=PASS`.

## 4. Frozen version/control-plane compatibility

The current artifact retains the exact frozen AdGuard Home v0.107.79 source pin and historical version-pinned API/config evidence:

- tag `v0.107.79`;
- tag object `314ec91cd14765fa8f878de4bb19fa546b5c40c4`;
- source commit `05ba17b282da1c4393d6a4ba4db0cf519194a362`;
- version-pinned OpenAPI under `AdguardTeam/AdGuardHome@v0.107.79`;
- private `/control` administration with Basic-Auth;
- API schema checks plus persisted/live configuration verification;
- fail-closed behavior on unexplained version/schema/field drift.

Current upstream AdGuard documentation continues to describe persistent clients and ClientIDs as encrypted-DNS client-identification mechanisms. Their existence is treated only as a technical capability; the current project contract separately governs whether/when an optional-account device lifecycle may use them.

Markers:

- `TSK0044_VERSION_CONTROL_CONTRACT=PASS`;
- `TSK0044_UPSTREAM_SOURCE_BOUNDARY=PASS`.

## 5. Private control and secret boundary

VER-0044 proved:

- customer/public/account/dashboard surfaces receive no AdGuard admin credential;
- generic `/control` proxying is prohibited;
- only a private allowlisted server-side path may use the administrative API;
- credentials remain out of browsers, product records, telemetry and customer/downloaded material;
- authorization precedes consequential account/device operations;
- secret rotation remains atomic/recoverable and ambiguous results are reconciled before replay.

Marker: `TSK0044_CONTROL_ISOLATION=PASS`.

## 6. Current dual-mode ClientID boundary

The revalidation preserves a no-persistent-client rule for anonymous/accountless setup while allowing only a **conditional downstream** optional-account persistent ClientID mechanism if TSK-0352 and applicable security/privacy/architecture acceptance prove it necessary.

VER-0044 proved the contract requires, when applicable:

- server-side-only lifecycle operations;
- opaque/high-entropy, non-identity/content-derived ClientID;
- parent-to-device ownership authorization before mutation;
- no arbitrary user-supplied ClientID as authorization;
- ownership/ClientID never substitutes for Protection Map verification;
- `ignore_querylog` / `ignore_statistics` client privacy controls plus independent global no-history/no-statistics verification;
- no DNS browsing/activity history;
- distinct account deletion, device deletion/revoke and physical DNS removal semantics;
- no child account/profile or unrestricted customer DNS administration.

TSK-0352 remains the owner of the concrete allowlisted API/lifecycle contract. TSK-0044 supplies NFRs only.

Marker: `TSK0044_DUAL_MODE_CLIENT_BOUNDARY=PASS`.

## 7. Privacy, timeout/retry and reconciliation proof

VER-0044 proved the current contract retains:

- query log disabled;
- query-log file persistence disabled;
- statistics disabled;
- anonymisation/privacy state enforced;
- no query-history/statistics product source;
- finite 1s connection / 3s ordinary read / 5s bounded config-test provisional loopback budgets;
- no blind retry for auth/schema failures;
- no blind replay of ambiguous mutation;
- pre-read, bounded delta, one mutation, exact read-back and mixed/unknown reconciliation;
- distributed datastore + AdGuard terminal-state reconciliation for optional account/device lifecycle.

Markers:

- `TSK0044_PRIVACY_INVARIANTS=PASS`;
- `TSK0044_TIMEOUT_RETRY=PASS`;
- `TSK0044_RECONCILIATION=PASS`.

## 8. Auth, datastore, AdGuard and verification failure proof

The current acceptance newly requires explicit dual-mode failure boundaries. VER-0044 proved:

- auth/provider/session failure cannot make the complete accountless core unavailable;
- invalid/expired/revoked sessions cannot mutate device/AdGuard state;
- authentication success is neither ownership proof nor protection proof;
- TSK-0353 retains detailed authentication/session security ownership;
- datastore ambiguity freezes consequential ownership-changing mutation and rejects stale ownership;
- partial datastore + AdGuard outcomes are reconciled before retry/success;
- private admin API failure alone does not falsely change independently proven customer protection;
- public verification uncertainty is not replaced by admin/account confirmation;
- AdGuard service degradation uses current TSK-0538 recovery semantics;
- optional-account degradation remains truthful while the independent accountless core stays available when healthy.

Markers:

- `TSK0044_AUTH_FAILURE=PASS`;
- `TSK0044_DATASTORE_FAILURE=PASS`;
- `TSK0044_FAILURE_PLANES=PASS`.

## 9. Historical/current reconciliation

The historical contract explicitly treated the whole product as having no customer authentication, persistent dashboard, AdGuard client record or customer datastore. That assumption is invalid under CR-0006.

The current artifact explicitly supersedes only that scope boundary and the categorical prohibition on every persistent AdGuard client regardless of purpose. It preserves all compatible control-plane, credential, privacy, retry, idempotency, version-regression and evidence-separation rules.

Marker: `TSK0044_HISTORICAL_CURRENT_RECONCILIATION=PASS`.

## 10. Deterministic downstream acceptance surface

The current artifact contains exactly 30 downstream assertions spanning control isolation, secret absence, version/schema checks, privacy booleans, accountless no-persistent-client behavior, optional-account ClientID/ownership controls, timeout/retry/reconciliation, auth/datastore/provider failure, technical verification truth, logging/privacy and rollback.

Marker: `TSK0044_ASSERTION_CATALOGUE=PASS`.

## 11. Independent VER-0044

Independent read-only verifier:

- script `.github/scripts/verify_tsk0044_current_revalidation.py` — blob `0c92fdebb55da98e8f94be649f5bec88f85233e2`;
- workflow `.github/workflows/verify-tsk0044-current-revalidation.yml` — blob `00e367e8dc5456b5052f1f8f6a6daa1fb4cc113b`;
- workflow permission: `contents: read` only;
- GitHub-hosted Ubuntu 24.04 LTS;
- run `33588675744`;
- job `100118011663`;
- conclusion **SUCCESS**.

Final markers:

- `TSK0044_INPUT_HASHES=PASS`;
- `TSK0044_CURRENT_WBS=PASS`;
- `TSK0044_CURRENT_PREDECESSORS=PASS`;
- `TSK0044_STRUCTURE=PASS`;
- `TSK0044_VERSION_CONTROL_CONTRACT=PASS`;
- `TSK0044_CONTROL_ISOLATION=PASS`;
- `TSK0044_DUAL_MODE_CLIENT_BOUNDARY=PASS`;
- `TSK0044_PRIVACY_INVARIANTS=PASS`;
- `TSK0044_TIMEOUT_RETRY=PASS`;
- `TSK0044_RECONCILIATION=PASS`;
- `TSK0044_AUTH_FAILURE=PASS`;
- `TSK0044_DATASTORE_FAILURE=PASS`;
- `TSK0044_FAILURE_PLANES=PASS`;
- `TSK0044_HISTORICAL_CURRENT_RECONCILIATION=PASS`;
- `TSK0044_UPSTREAM_SOURCE_BOUNDARY=PASS`;
- `TSK0044_ASSERTION_CATALOGUE=PASS`;
- `TSK0044_NON_INFERENCE=PASS`;
- `TSK0044_CURRENT_ACC=PASS`;
- `TSK0044_CURRENT_VER=PASS`;
- `TSK0044_CURRENT_EVD_READY=PASS`;
- `TSK0044_CURRENT_REVALIDATION=PASS`.

## 12. Acceptance disposition

**ACC-0044 = PASS. VER-0044 = PASS. EVD-0044 = SATISFIED.**

**TSK-0044 current dual-mode revalidation: PASS, pending only guarded runtime reconciliation and exact read-back.**

## 13. Non-inference

This proves current L4 NFR-definition acceptance only. It does not implement the AdGuard adapter, create/modify a persistent client, approve TSK-0352, activate authentication/session or a datastore, rotate credentials, change AdGuard configuration/version, authorize real-user processing, publish, activate a market, launch, pass a lifecycle gate or infer successor PASS.
