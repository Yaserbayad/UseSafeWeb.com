# TSK-0044 — AdGuard API Compatibility/Credential/Failure NFR Verification Evidence

**Task:** TSK-0044 — Define AdGuard API compatibility, credential-isolation and failure NFRs  
**Acceptance:** ACC-0044  
**Verification:** VER-0044 — independent version/API/security/failure-semantics audit  
**Evidence:** EVD-0044  
**Date:** 2026-08-28  
**Result:** PASS candidate pending GitHub read-back and guarded runtime reconciliation

## 1. Exact evidence index

- NFR contract: `TSK_0044_ADGUARD_API_COMPATIBILITY_CREDENTIAL_FAILURE_NFR_2026-08-28.md`
- NFR contract blob: `07ab5539d11ff25d591adeada34e7f30854caa90`
- Contract creation commit: `7454946649a0b0bc6b33470817309844e486386e`
- Selected runtime before execution: `CURRENT_STATE.md` blob `a0687a64a9c6c7aa27809b436f02dbac47ff1f71`; current state selects TSK-0044 and states direct dependencies TSK-0484, TSK-0538 and TSK-0146 are PASS.
- WBS blob: `dce5b829c4d447eac180ae1e896e0019292cf971`; guarded selector directly asserted TSK-0146 `Execution_State=PASS`, exact ACC-0044 wording, A3/AUTO_ALLOWED and WBS-order precedence over TSK-0046.
- Current approved AdGuard safe configuration: `infrastructure/adguard-server/approved-adguard-config-v1.json`, blob `e9975c4e75c2a68131f049da942468d8d1952d8d`.
- Current secure-admin evidence: TSK-0201 blob `ae06672e1cebdf87d006b85b80e5a7977f4e69b9`.
- Current privacy evidence: TSK-0204 `aa84d93d33d789fe4ff74ea12bcc2e5ffccd5b06`, TSK-0205 `47fb0e0e6b64ceab965b2ca0ee259b40a98032c6`, TSK-0206 `5905136433d930c2325a877e10a45e8540ac6a80`.
- Direct predecessors TSK-0484 and TSK-0538 remain current accepted stable state.

## 2. Exact upstream version/contract verification

Official AdGuardTeam/AdGuardHome source was checked for the **exact installed version** rather than relying on master/current API behavior.

- Official ref: `refs/tags/v0.107.79`.
- Annotated tag object: `314ec91cd14765fa8f878de4bb19fa546b5c40c4`.
- Tag target commit: `05ba17b282da1c4393d6a4ba4db0cf519194a362`.
- Version-pinned OpenAPI: `AdguardTeam/AdGuardHome@v0.107.79/openapi/openapi.yaml`.

The pinned OpenAPI explicitly establishes:

- server base `/control`;
- global HTTP Basic-Auth security scheme;
- `GET /status`, `GET /dns_info`, `POST /dns_config`;
- current query-log API at `GET /querylog/config` and `PUT /querylog/config/update`;
- current statistics API at `GET /stats/config` and `PUT /stats/config/update`;
- `GET /filtering/status`;
- TLS status/configuration/validation surfaces;
- query-log config requires `enabled`, `interval`, `anonymize_client_ip`, and `ignored`;
- statistics config requires `enabled` and `interval`.

The contract correctly distinguishes these API fields from persisted configuration fields that remain necessary for complete privacy verification, especially `querylog.file_enabled=false` and persisted `dns.anonymize_client_ip=true`.

**Result: PASS.**

## 3. Private/restricted administration-path audit

ACC-0044 requires a private/restricted AdGuard administration path.

The contract preserves the currently evidenced architecture:

- AdGuard admin/API at `127.0.0.1:3000` only;
- plain DNS at `127.0.0.1:53` only;
- public customer encrypted DNS through the separate Nginx DoH/DoT ingress;
- no `/control` exposure to browsers/phones/public DNS clients;
- current operator automation only through the governed on-host path.

Current TSK-0201 evidence independently proves the root-only credential file, authenticated local control access, unauthenticated HTTP 401, loopback admin listener and attributable governed mutation chain.

The NFR goes further by explicitly denying direct `/control` credentials/reachability to public website, accountless UI, customer devices, profiles, telemetry and ordinary self-service support.

**Result: PASS.**

## 4. No customer-authentication/persistent-datastore dependency audit

The contract makes the current architecture explicit:

- no per-parent/per-device AdGuard admin identity;
- no customer-facing AdGuard API credential;
- no mandatory UseSafeWeb account;
- no mandatory persistent dashboard/datastore;
- no persistent AdGuard client record created merely to support accountless setup;
- shared resolver identity remains infrastructure, not customer identity.

The customer journey does not require the AdGuard admin API. Setup and protection verification use the public resolver and approved product-state verifier contracts.

**Result: PASS.**

## 5. Secret storage/isolation/rotation audit

ACC-0044 requires secret storage/rotation requirements.

The contract requires:

- current root-restricted on-host credential boundary (`0600 root:root` from accepted evidence);
- no secret in Git, logs/evidence, browser bundles, product telemetry or downloadable setup material;
- no AdGuard admin secret in the default customer-facing application runtime;
- protected private runtime delivery only if a future narrowly-scoped control adapter is proven necessary;
- command/log redaction discipline;
- atomic/reversible rotation sequence with new-credential verification before old-secret invalidation;
- no repeated blind rotation after ambiguous failure;
- no invented calendar rotation cadence absent evidence, while compromise/suspicion/access-policy triggers remain binding.

**Result: PASS.**

## 6. API/config timeout and retry audit

ACC-0044 requires explicit timeout/retry behavior.

The contract defines provisional finite loopback defaults:

- connect timeout 1s;
- ordinary read/health total timeout 3s;
- bounded config/test total timeout 5s unless the pinned operation is proven to need an explicit longer bound;
- finite subprocess/service-control timeouts.

Retry policy is operation-class aware:

- read-only GET: max 2 transient retries;
- 401/403: no retry with same credential;
- 400/422/schema error: no blind retry;
- proven non-mutating validation POST: at most one retry;
- mutation: no blind retry after ambiguous timeout/disconnect/5xx; read actual state first.

The contract labels these as provisional internal loopback budgets, not public service SLOs, and permits evidence-based tuning with regression coverage.

**Result: PASS.**

## 7. Partial-failure/idempotency reconciliation audit

The contract does not falsely assume a project-wide AdGuard idempotency-key feature. Instead it mandates:

1. pre-read affected state/version;
2. validate a bounded delta;
3. verify recovery/rollback source;
4. execute one mutation;
5. exact API + persisted-config read-back;
6. privacy/security/listener/health/functional verification;
7. classify verified desired state vs confirmed original state vs mixed/unknown state;
8. stop/reconcile mixed or ambiguous state before rollback/repair/retry;
9. never accept HTTP success/write acknowledgement alone.

For restart/config-file transitions it additionally requires pre-change hash/backup, syntax validation, post-restart health, rollback and read-back. This is consistent with the accepted TSK-0201 two-phase bind transition.

**Result: PASS.**

## 8. Opaque setup/configuration identifier audit

ACC-0044 requires the NFR to address opaque identifiers **if technically required**.

The contract makes a direct bounded decision: **none is currently required** by the shared accountless AdGuard integration.

It prohibits manufacturing identity via AdGuard persistent clients, internal UIDs/filter IDs, IP, fingerprint or profile content.

If later technical necessity is proven, the contract requires a reopened owning data/interface contract and constrains the identifier to >=128-bit random entropy, opacity, one-operation/journey scope, short TTL/non-reuse, no identity derivation, no ordinary full-form logging/analytics and TSK-0229/0230 no-linkage/retention controls.

This satisfies the conditional acceptance clause without inventing a datastore merely to hold IDs.

**Result: PASS.**

## 9. Explicit privacy-boolean audit

The NFR explicitly fail-closes on the current required privacy state:

- query log enabled = false;
- query-log file persistence = false;
- statistics enabled = false;
- client-IP anonymisation = true;
- ECS disabled/no custom ECS identity;
- admin bind loopback-only;
- plain DNS bind loopback-only;
- no persistent customer AdGuard clients.

The verification-source table deliberately combines control API and persisted/live configuration because v0.107.79 API responses alone do not prove `querylog.file_enabled` on disk.

Missing fields, parse errors, version mismatch or unverifiable disk state become uncertain/error rather than an optimistic default.

**Result: PASS.**

## 10. Version/contract regression audit

The contract defines an explicit compatibility gate for every AdGuard version/material interface change:

- installed version must equal approved version under test;
- exact official tag/commit/OpenAPI pinned;
- required paths/methods/security behavior retained;
- schemas/required field types/semantics parsed;
- privacy fields enforceable;
- persisted schema paths rechecked;
- deprecated endpoints not newly adopted when current replacements exist;
- isolated/reversible admin/privacy/filter/upstream/TLS regression before production reliance;
- recovery scripts/artifacts updated and proven where needed.

Unexpected drift blocks integration/mutation rather than weakening validation.

**Result: PASS.**

## 11. Safe-unavailable behavior audit

The contract separates three failure planes:

1. **admin API unavailable but public resolver healthy:** do not falsely mark customer protection failed;
2. **public verification unavailable/uncertain:** do not substitute admin health or parent confirmation for technical verification; use TSK-0320 truthful state and TSK-0042 recovery;
3. **administrative mutation unavailable/auth/schema/version/read-back failure:** stop unrelated mutations, preserve only independently valid product evidence, trigger runbook, reconcile/rollback from known-good state, and use TSK-0538 recovery if DNS service is impaired.

Unsafe fallbacks are explicitly prohibited: public `/control`, plaintext public administration, query-history inspection, privacy-control disablement, or inventing a customer account/database.

**Result: PASS.**

## 12. Interface misuse/error-surface audit

A future internal adapter is required to normalize failures into bounded non-sensitive codes rather than exposing raw AdGuard/server details to customers. Customer-facing copy remains owned by the product/recovery state contract.

The implementation assertion set requires an endpoint allowlist and prohibits generic `/control/*` proxying, preventing the application interface from silently expanding as upstream AdGuard adds endpoints (Hyrum-law exposure control).

**Result: PASS.**

## 13. Testability audit

Section 13 defines 24 implementation assertions covering:

- public/control isolation;
- secret absence and unauthenticated rejection;
- allowlisted control surface;
- schema validation;
- all privacy booleans/persisted state;
- accountless/no-client-record behavior;
- timeouts/retries;
- ambiguous-mutation reconciliation;
- version drift;
- conditional opaque identifiers;
- separate admin/customer evidence planes;
- truthful verifier failure;
- credential rotation;
- recovery invariants;
- no account/customer-auth/database dependency.

The contract therefore supplies measurable downstream verification rather than qualitative intent only.

**Result: PASS.**

## 14. Verification disposition

**VER-0044 independent audit result: PASS for ACC-0044's provisional internal L4 interface/NFR-definition scope.**

The read-back contract at blob `07ab5539d11ff25d591adeada34e7f30854caa90` satisfies every ACC-0044 clause using exact v0.107.79 upstream interface evidence plus current accepted UseSafeWeb runtime/config/privacy evidence.

The following remain OPEN/non-PASS and are not converted by this result:

- any implementation of a future AdGuard adapter;
- any new control-plane credential or credential rotation;
- any customer account/auth/dashboard or persistent product datastore;
- `DVR-0230-01`, `DVR-0484-01`, `GAP-0484-02`;
- real-user/behavioral evidence (`RSK-0002`);
- final legal/privacy/participant gates;
- implementation/build/publication/launch.

**Runtime may move TSK-0044 to PASS only after this evidence file is persisted/read back and a guarded reconciliation verifies the current selection, exact contract/evidence/WBS/runtime preconditions.**
