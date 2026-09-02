# TSK-0044 — Post-CR-0008 Dual-Mode AdGuard API Compatibility, Credential-Isolation and Failure NFR Revalidation

**Task:** TSK-0044 — Define AdGuard API compatibility, credential-isolation and failure NFRs  
**Acceptance / Verification / Evidence:** ACC-0044 / VER-0044 / EVD-0044  
**Lifecycle / Priority / Authority:** L4 / MEDIUM / A3 / AUTO_ALLOWED  
**Version:** 2.0.0-post-CR0008  
**Date:** 2026-09-02 UTC  
**Candidate disposition:** CURRENT PASS pending independent VER-0044, durable EVD-0044 publication, guarded runtime reconciliation and exact read-back.

## 1. Current authority and revalidation boundary

Current TSK-0044 depends exactly on current PASS predecessors TSK-0484, TSK-0538 and TSK-0146.

The historical `TSK_0044_ADGUARD_API_COMPATIBILITY_CREDENTIAL_FAILURE_NFR_2026-08-28.md` and its independent evidence remain applicable for the unchanged AdGuard v0.107.79 control-plane, secret-isolation, timeout/retry, idempotency/reconciliation, version-regression and privacy-invariant rules. They are stale only where they bound the entire product to an accountless-only architecture and categorically prohibited any persistent customer/device AdGuard client record.

CR-0006 / DEC-0053 now freezes a dual-mode Version-1 product:

- the complete core setup/protection journey remains usable without login;
- an optional parent account, secure session, minimum parent/device ownership persistence and lightweight dashboard/device management are in scope;
- mandatory login for core value remains prohibited;
- browsing/query/activity history, child accounts and unrestricted customer DNS administration remain prohibited.

This revalidation updates the TSK-0044 NFR boundary to that current scope. It does **not** implement an AdGuard adapter, create a persistent client, choose a final persistence schema, activate authentication, expose the control plane, rotate credentials, change the frozen AdGuard backend or infer any successor PASS.

## 2. Frozen AdGuard backend and version-pinned control contract

The project AdGuard backend remains frozen at **AdGuard Home v0.107.79** absent a separately verified critical blocker or governed version-change task.

The historical version-pinned source proof remains authoritative for the exact frozen release:

- official tag `v0.107.79`;
- annotated tag object `314ec91cd14765fa8f878de4bb19fa546b5c40c4`;
- target source commit `05ba17b282da1c4393d6a4ba4db0cf519194a362`;
- version-pinned OpenAPI `AdguardTeam/AdGuardHome@v0.107.79/openapi/openapi.yaml`.

The unchanged contract facts retained from prior accepted evidence include:

- administrative API base `/control`;
- HTTP Basic-Auth control authentication;
- version-pinned status/DNS/query-log/statistics/filtering/TLS administration surfaces;
- API schema validation is necessary but does not replace persisted/live configuration verification;
- unexpected version/schema/field drift is a contract failure, never an optimistic default.

Current upstream AdGuard documentation also continues to distinguish persistent clients and ClientIDs as encrypted-DNS client-identification mechanisms. Their technical existence does not authorize UseSafeWeb/SafeWeb to create them outside the governed optional-account/device lifecycle.

## 3. Control-plane isolation — unchanged and mandatory

The customer plane and operator control plane remain separate.

### 3.1 Customer-facing surfaces

The following receive **no AdGuard admin credential** and no generic `/control` capability:

- public SafeWeb website;
- complete accountless setup journey;
- optional sign-in/account/dashboard UI;
- parent/child browser or device;
- generated setup/profile delivery;
- public encrypted DNS clients;
- product analytics;
- ordinary self-service support.

No browser/mobile/customer request may carry the AdGuard Basic-Auth credential, admin session secret, password hash or a generic server-side `/control/*` proxy token.

### 3.2 Governed server-side control path

Only an approved private server-side operator/adapter boundary may access the AdGuard control API. It must:

- expose only an explicit endpoint/operation allowlist needed by an accepted downstream contract;
- keep credentials outside browser/customer/product records;
- reject arbitrary `/control` proxying;
- validate version, request and response schemas;
- redact authentication material from logs/errors;
- preserve the loopback/private administration boundary;
- apply authorization before any account/device lifecycle mutation.

TSK-0352 remains the downstream owner for the concrete allowlisted persistent-ClientID/API lifecycle contract. TSK-0044 supplies NFR constraints and does not self-approve that implementation.

## 4. Dual-mode AdGuard client and ClientID boundary

### 4.1 Accountless core

Anonymous/accountless setup must not create or require a persistent AdGuard client record, account identity or long-lived device ownership record.

Accountless J0/J1 state remains governed by TSK-0229 and cannot be silently joined, promoted or copied into an optional account after sign-in. A public resolver or product-side short-lived journey identifier is not an AdGuard ownership identifier.

### 4.2 Optional account/device management

A persistent AdGuard client/ClientID may exist **only if** the owning downstream API/lifecycle contract proves it is necessary for optional account/device management and satisfies all current privacy/security/ownership constraints.

If used, the NFR requires:

- server-side creation/update/search/delete only; never browser-side control access;
- high-entropy opaque ClientID generated independently of email, parent ID, child identity, IP, hostname, device nickname or browsing content;
- parent-to-device ownership authorization before every lifecycle operation;
- no arbitrary user-supplied ClientID accepted as an authorization decision;
- ClientID is routing/configuration identity, not proof that protection is active;
- technical Protection Map verification remains separate from account/device ownership;
- `ignore_querylog=true` and `ignore_statistics=true` where supported by the accepted client contract, with the global no-history/no-statistics privacy baseline still enforced independently;
- no DNS qname/domain/URL/browsing history collected to support ownership or dashboard display;
- no child account/profile or unrestricted DNS-administration surface;
- deletion/unlink/revoke/replacement semantics are explicit, idempotent or safely reconcilable, and independently verified before claiming completion;
- account deletion, device-record deletion and physical DNS configuration removal remain distinct truthful operations.

Until TSK-0352 and applicable architecture/security/privacy implementation tasks accept the concrete API contract, this section is a **constraint**, not permission to create persistent clients.

## 5. Secret storage, rotation and credential isolation

The historical secret rules remain current:

- AdGuard admin credentials are restricted server-side secrets;
- no secret value enters Git, evidence, browser bundles, telemetry, downloadable setup material or product/account records;
- default customer-facing runtime receives no AdGuard admin secret;
- only the minimum approved private adapter/operator process may receive the secret;
- shell tracing, authorization-header logging and credential-bearing URLs are prohibited;
- errors are sanitized before crossing the private boundary.

Credential rotation must remain atomic/recoverable:

1. prove current authenticated health and recoverable state;
2. generate protected replacement material;
3. apply through the accepted version-pinned path;
4. verify new credential locally;
5. verify unauthenticated/public access remains rejected;
6. retire the old credential only after read-back proves the new path;
7. update only the approved protected secret store;
8. prove permissions/log hygiene;
9. on ambiguous result, reconcile active credential state before any retry.

No calendar rotation interval is invented by this NFR.

## 6. Privacy and configuration invariants

AdGuard operations fail closed unless the required privacy/security baseline remains provable.

At minimum:

- query logging remains disabled;
- query-log file persistence remains disabled;
- statistics remain disabled;
- client-IP anonymisation remains enabled where applicable to the frozen configuration;
- ECS/custom identity leakage remains disabled under the approved resolver baseline;
- administration and plain-DNS listeners remain private/loopback as approved;
- no query-history/statistics source becomes a product/account/dashboard data source;
- persistent optional-account clients, if later accepted, must themselves be excluded from query log/statistics and remain bound to minimum ownership lifecycle only.

An API field being absent, malformed or semantically changed is `uncertain/error`; it is never assumed safe. Persisted/live configuration must be checked where the API does not prove the complete invariant.

## 7. API/config timeout, retry and ambiguous-mutation rules

The existing bounded loopback defaults remain provisional internal NFRs:

- connection timeout: 1 second;
- ordinary read/health total timeout: 3 seconds;
- bounded configuration/test total timeout: 5 seconds unless the exact operation is proven to need another finite bound;
- all subprocess/service-control calls have finite task-specific timeouts.

Retry rules remain operation-aware:

- read-only GET: at most two transient retries with bounded backoff;
- 401/403: no blind retry with the same credential;
- 400/422/schema/contract failure: no blind retry;
- proven non-mutating validation operation: at most one retry when idempotency/non-mutation is established;
- mutation: no blind replay after timeout, disconnect, 5xx or ambiguous response; read actual target state first.

HTTP/write acknowledgement alone never proves success.

## 8. Idempotency and partial-failure reconciliation

UseSafeWeb/SafeWeb does not assume project-wide upstream idempotency keys. Every accepted mutation must follow:

1. pre-read exact affected state and pinned version;
2. verify actor/account/device authorization when the operation is ownership-scoped;
3. validate the smallest bounded delta;
4. capture the applicable rollback/recovery source;
5. execute one mutation;
6. read back the API state and any required persisted configuration state;
7. verify privacy/security/listener/service-health/functional invariants;
8. classify verified desired state, confirmed original state, or mixed/unknown state;
9. stop ordinary progression on mixed/unknown state and reconcile before rollback/repair/retry.

For optional account/device mutations, datastore and AdGuard state must be reconciled as a distributed lifecycle operation. A product record may not claim ownership/deletion/revoke success merely because one side wrote successfully.

## 9. Authentication/session failure NFRs

Authentication is optional for core value. Therefore:

- auth/provider/session failure must not make the complete accountless core unavailable;
- auth failure must not weaken DNS/privacy/security controls;
- the account/dashboard path reports an explicit unavailable/retry/re-auth state rather than fabricating ownership or protection;
- expired/revoked/invalid sessions cannot mutate AdGuard or persistent device records;
- authorization is re-evaluated server-side for each consequential device operation;
- authentication success alone does not prove device ownership or protection state;
- provider outage does not trigger fallback to public AdGuard control access, shared admin credentials or anonymous persistent-client mutation;
- 401/403/session-invalid responses are not blindly retried as if transient network failures.

Detailed authentication/session/cookie/CSRF/account-takeover NFR ownership remains with TSK-0353.

## 10. Datastore/minimum-persistence failure NFRs

Optional account/device ownership requires minimum persistence but cannot become a hidden dependency of the accountless core.

When the account/ownership datastore is unavailable or ambiguous:

- accountless setup/protection remains available when its independent dependencies are healthy;
- no new ownership-changing AdGuard mutation proceeds without authoritative ownership state;
- stale cached ownership is not accepted for consequential mutation;
- account/dashboard reads may degrade to a truthful unavailable/uncertain state;
- partial datastore + AdGuard mutations are reconciled before retry;
- no success is shown until both owning persistence and relevant AdGuard state meet the accepted terminal condition;
- deletion/revoke/unlink operations preserve a durable/reconstructable recovery/reconciliation trail without retaining prohibited browsing/content data;
- retries are bounded and idempotent/reconcilable;
- provider/datastore outage is observable without logging account secrets, tokens, DNS history or unnecessary personal data.

Detailed schema/storage/retention/backup/access ownership remains downstream and is not invented here.

## 11. AdGuard/control-plane failure NFRs

Failure planes remain distinct:

### 11.1 Admin API unavailable; public DNS healthy

Do not label customer protection failed solely because the private admin API is unavailable. Suspend affected administrative/device-lifecycle mutations, surface operational degradation internally, and preserve independently proven customer-plane state.

### 11.2 Public verification unavailable or indeterminate

Do not substitute admin API health, account ownership or parent confirmation for technical verification. Use the current six-state Protection Map semantics and truthful uncertain/action-needed/not-covered outcomes.

### 11.3 AdGuard service unavailable/degraded

Apply current TSK-0538 reliability/recovery rules. Account/dashboard availability cannot be used to imply DNS protection. Preserve accountless failure/recovery guidance and avoid destructive blind retries.

### 11.4 Auth or datastore unavailable

Keep the accountless core independent. Freeze consequential account/device mutations that cannot be authorized/reconciled and expose truthful bounded optional-account degradation.

## 12. Interface/error-surface constraints

A future internal adapter must expose bounded non-sensitive errors, for example operation category + failure class + retryability/reconciliation state, not raw AdGuard payloads, stack traces, credentials or upstream administrative details.

The customer-facing product must not receive a generic administrative API proxy. New upstream AdGuard endpoints do not automatically become SafeWeb features.

## 13. Version and contract regression gate

Before any AdGuard version or material control-interface change is relied upon:

1. pin the exact installed/target release and official source identity;
2. inspect the exact version OpenAPI/configuration contract;
3. prove every required allowlisted endpoint/method/security mechanism still exists;
4. validate schemas and required field semantics;
5. re-prove global and persistent-client privacy invariants;
6. re-prove admin/customer network and credential separation;
7. re-run persistent ClientID lifecycle tests if that capability has been implemented;
8. re-run failure/reconciliation/rollback tests;
9. update recovery artifacts before production reliance;
10. block the affected integration on unexplained drift rather than relaxing checks.

The frozen backend decision means this gate is normally dormant unless a separately governed version change is authorized or a verified critical blocker forces reassessment.

## 14. Deterministic downstream assertion catalogue

A downstream implementation/acceptance test must be able to prove at least these assertions when applicable:

1. public/customer surfaces cannot reach generic AdGuard `/control`;
2. no browser/product bundle contains the admin credential;
3. unauthenticated administrative access is rejected;
4. only explicitly allowlisted control operations are reachable from the private adapter;
5. exact frozen version/schema identity is checked;
6. missing/changed required fields fail closed;
7. query log remains disabled;
8. query-log file persistence remains disabled;
9. statistics remain disabled;
10. anonymisation/privacy state remains enforced;
11. accountless setup creates no persistent AdGuard client/account ownership state;
12. optional-account persistent ClientID creation is impossible unless the owning downstream contract is accepted;
13. any accepted ClientID is opaque/high-entropy and not identity/content-derived;
14. ownership authorization precedes every consequential device mutation;
15. `ignore_querylog` and `ignore_statistics` are enforced for persistent clients when applicable;
16. account ownership is not treated as protection verification;
17. account deletion, device deletion/revoke and physical DNS removal remain distinct;
18. read operations have finite timeout/retry bounds;
19. ambiguous mutation is read-back/reconciled before retry;
20. partial AdGuard + datastore mutation cannot be labeled success;
21. auth/provider outage preserves the complete accountless core;
22. datastore outage preserves the complete accountless core;
23. invalid/expired/revoked session cannot mutate device/AdGuard state;
24. admin API outage alone does not falsely change independently proven customer protection;
25. public verifier uncertainty is not replaced by admin/account confirmation;
26. service outage uses current TSK-0538 recovery semantics;
27. logs/errors contain no admin secret, session token, DNS history or unnecessary personal data;
28. version/API drift blocks the affected integration;
29. rollback/recovery leaves privacy/listener invariants verified;
30. no generic customer-facing DNS administration is introduced.

## 15. Historical/current reconciliation

Retained from historical TSK-0044:

- exact AdGuard v0.107.79 pin and version-specific API/config reasoning;
- private restricted control plane;
- credential isolation and rotation requirements;
- global privacy booleans and persisted-state verification;
- bounded timeouts/retries;
- no blind mutation replay;
- exact read-back/idempotency/reconciliation rules;
- version/contract regression gate;
- separation of admin-plane and customer-plane evidence;
- no query-history/statistics product data source.

Superseded for current acceptance:

- the statement that the entire product has no optional account/session/dashboard/minimum persistence;
- the categorical prohibition on any persistent AdGuard client record regardless of purpose;
- the assumption that account/auth/datastore failure semantics are out of TSK-0044 scope.

Current replacement rule: accountless remains no-persistent-client and login-free; optional account/device management may use only the minimum separately accepted persistent ClientID mechanism under strict server-side ownership/privacy/security constraints; auth/datastore/AdGuard/verification failure planes are explicit and fail safely.

## 16. Acceptance disposition

TSK-0044 current candidate satisfies the current acceptance boundary by defining:

- private/restricted AdGuard administration;
- secret storage/rotation and browser/customer credential isolation;
- finite API/config timeout/retry rules;
- ambiguous/partial-failure reconciliation and idempotency-by-read-back;
- opaque setup/ClientID requirements where technically required;
- explicit global and optional-client privacy controls;
- exact version/contract regression checks;
- optional customer authentication/session and minimum persistence boundaries without mandatory login for core value;
- safe and distinct behavior when AdGuard, auth, datastore or verification paths are unavailable.

No implementation, credential rotation, persistent-client creation, authentication activation, data-store deployment, real-user processing, publication, market activation, lifecycle gate or successor PASS is inferred.

**ACC-0044 current result candidate: PASS pending independent VER-0044, durable EVD-0044, guarded runtime reconciliation and exact GitHub read-back.**
