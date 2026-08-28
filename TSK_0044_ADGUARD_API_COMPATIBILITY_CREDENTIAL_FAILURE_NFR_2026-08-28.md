# TSK-0044 — AdGuard API Compatibility, Credential-Isolation and Failure NFRs

**Task:** TSK-0044 — Define AdGuard API compatibility, credential-isolation and failure NFRs  
**Acceptance:** ACC-0044  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** INTERNAL PROVISIONAL L4 INTERFACE/NFR CONTRACT / IMPLEMENTATION OR SECRET ROTATION NOT AUTHORIZED  
**Date:** 2026-08-28  
**Authority:** TSK-0484 + TSK-0538 + TSK-0146 + TSK-0201/0202/0204/0205/0206 + current v0.107.79 AdGuard API/configuration contract + DEC-0042/EXC-0001 + DEC-0050/CR-0003  
**Verification state:** PASS candidate pending independent verification and runtime reconciliation.

## 1. Scope and frozen architecture

This contract defines how UseSafeWeb may depend on the current AdGuard Home administrative/configuration interface **without turning AdGuard into a customer identity system or exposing its control plane to parents/devices**.

The current architecture remains:

- customer/device plane: encrypted DNS through `dns.usesafeweb.com` on approved DoH/DoT mechanisms;
- operator control plane: AdGuard Home admin/API on `127.0.0.1:3000` only;
- AdGuard plain DNS backend on `127.0.0.1:53` only;
- public TLS ingress through Nginx; `/control` is not a public customer surface;
- current admin credential is root-protected on the DNS host and is not a browser/mobile credential;
- no mandatory UseSafeWeb customer account, customer authentication, persistent dashboard, AdGuard client record or customer datastore is introduced.

The product journey must not call the AdGuard `/control` API from the browser, phone, public resolver path or ordinary parent setup flow. Customer-facing setup/verification uses the public resolver and the approved product-state/verification contracts, not administrative API access.

`RSK-0002` remains OPEN. This NFR contract is not real-user validation and does not authorize implementation/build/release.

## 2. Exact version/contract pin checked on 2026-08-28

The currently installed and approved server is **AdGuard Home v0.107.79**.

Official upstream tag identity:

- tag: `v0.107.79`;
- annotated tag object: `314ec91cd14765fa8f878de4bb19fa546b5c40c4`;
- target source commit: `05ba17b282da1c4393d6a4ba4db0cf519194a362`;
- version-pinned OpenAPI: `https://github.com/AdguardTeam/AdGuardHome/blob/v0.107.79/openapi/openapi.yaml`.

The v0.107.79 OpenAPI states:

- administrative server base is `/control`;
- global security scheme is HTTP **Basic Auth**;
- `GET /control/status` returns current DNS server status/general settings;
- `GET /control/dns_info` returns general DNS parameters;
- `POST /control/dns_config` sets general DNS parameters;
- `GET /control/querylog/config` and `PUT /control/querylog/config/update` own query-log API configuration;
- `GET /control/stats/config` and `PUT /control/stats/config/update` own statistics API configuration;
- `GET /control/filtering/status` exposes filtering parameters;
- TLS status/configuration/validation endpoints exist under `/control/tls/...`.

The v0.107.79 query-log configuration schema explicitly requires `enabled`, `interval`, `anonymize_client_ip`, and `ignored`. The statistics configuration schema explicitly requires `enabled` and `interval` (plus its controlled ignore configuration where present).

Important compatibility rule: the API schema does **not** replace persisted-configuration verification. The accepted current safe configuration also requires persisted `querylog.file_enabled=false` and persisted `dns.anonymize_client_ip=true`; those invariants must be checked from the supported target configuration/runtime path because a control-API response alone does not prove every disk-level privacy field.

## 3. Administrative trust boundary

### 3.1 Customer-facing components

The following must have **no AdGuard admin credential** and no direct `/control` network reachability by design:

- public website;
- accountless setup UI;
- parent/child browser;
- generated profile/mobileconfig delivery surface;
- public DNS clients;
- ordinary product telemetry/analytics components;
- ordinary self-service support UI.

A browser or customer device must never receive Basic-Auth credentials, an admin session cookie, an AdGuard password hash, or a proxy capability that provides generic `/control` access.

### 3.2 Operator/control components

Only a governed server-side operator path may access `/control`:

- loopback/on-host automation on the DNS host; or
- a future narrowly-scoped local control adapter if a concrete implementation need is proven and separately reviewed.

The current accepted path is the repository-scoped GitHub self-hosted runner on `adguardvm`, authenticated locally using the single `usesafeweb-admin` identity via root-only credential material. Existing evidence proves unauthenticated `/control/status` returns 401 and admin listener is loopback-only.

### 3.3 No direct customer identity mapping

The application must not create one AdGuard admin identity, AdGuard persistent client, API credential or control-plane object per household/device merely to support the accountless journey.

If a future feature genuinely requires per-setup state, it uses the separately governed accountless J0/J1 contract rather than encoding identity into AdGuard control-plane records.

## 4. Minimum allowed control-plane surface

### 4.1 Read/verification operations

The operator/verifier may use the smallest endpoints needed to establish current state, such as:

- `/control/status`;
- `/control/dns_info`;
- `/control/querylog/config`;
- `/control/stats/config`;
- `/control/filtering/status`;
- `/control/tls/status` where TLS state is relevant;
- equivalent version-pinned endpoints proven necessary by a downstream acceptance test.

Read operations must validate response shape/types and required fields before using them in a decision. An unexpected/missing field is a **contract failure**, not a false value/default.

### 4.2 Mutation operations

Administrative mutation is operator/maintenance work only. It must be tied to an eligible WBS task and its action authority; this NFR does not grant mutation authority.

A mutation must target the smallest coherent settings group and must not bundle unrelated privacy/security/filtering changes for convenience.

### 4.3 Disallowed ordinary product use

The customer product must not depend on:

- `/control/querylog` DNS history;
- `/control/stats` user/query statistics;
- persistent AdGuard client records;
- DHCP/rewrite/admin-user management;
- AdGuard self-upgrade endpoints;
- generic administrative proxying;

unless a later governed change explicitly proves a need, preserves privacy/security and obtains the applicable authority. Query/history endpoints remain technically present in AdGuard but are **not product data sources**.

## 5. Explicit privacy/configuration invariants

Any operation or compatibility verifier that can affect DNS behavior must fail closed unless it can prove the current required privacy baseline after the operation.

Current required booleans/state include at minimum:

| Invariant | Required value | Verification source |
| --- | --- | --- |
| Query log enabled | `false` | v0.107.79 query-log config API + persisted/live configuration |
| Query-log file persistence | `false` | persisted/live `querylog.file_enabled` configuration |
| Statistics enabled | `false` | v0.107.79 stats config API + persisted/live configuration |
| Client-IP anonymisation | `true` | v0.107.79 query-log API field and persisted/live `dns.anonymize_client_ip` |
| ECS | disabled / no custom ECS IP | current DNS configuration/runtime |
| Admin bind | loopback only (`127.0.0.1:3000`) | listener/config inspection |
| Plain DNS bind | loopback only (`127.0.0.1:53`) | listener/config inspection |
| Persistent customer AdGuard clients | none under current accountless baseline | current client/config inspection |

Absence of a field, API parsing failure, version mismatch, or inability to verify the persisted privacy state is **uncertain/error**, never assumed safe.

A mutation that would enable query history/statistics, weaken anonymisation/ECS, expose admin/plain DNS, or create customer-linked persistent client state is outside this NFR and requires a separately authorized baseline change.

## 6. Credential storage and isolation

### 6.1 Current accepted secret boundary

The current AdGuard admin credential is stored only in a root-restricted on-host credential file (`0600 root:root` in accepted evidence). The secret value must never be printed into GitHub logs/evidence, committed to Git, returned to a browser, placed in product telemetry, or embedded in downloadable setup material.

### 6.2 Runtime access

- Default customer-facing web/app runtime receives **no AdGuard admin secret**.
- If a future narrow server-side adapter genuinely needs control-plane access, it must run in a private execution boundary and receive the secret through an approved protected runtime secret mechanism; the secret must not be persisted into application/user records.
- Secret-bearing commands must disable shell tracing and must not echo authorization headers or credential-bearing URLs.
- Error output must redact authentication headers, cookies and credential material.

### 6.3 Rotation contract

Credential rotation, when authorized by a task/gate, must be atomic and reversible:

1. establish current authenticated health and a recoverable current configuration;
2. generate replacement material using a cryptographically secure method;
3. apply through the supported version-pinned mechanism;
4. prove the new credential authenticates locally;
5. prove unauthenticated access remains rejected and public admin exposure remains absent;
6. invalidate/remove the old secret only after the new path is verified;
7. update only the approved protected secret location;
8. verify file/secret permissions and ensure no secret entered Git/logs;
9. on ambiguous failure, do not repeatedly rotate; reconcile the actually active credential/state first.

No scheduled rotation interval is invented here; rotate on compromise/suspicion, operator/access change, applicable security policy trigger, or a later evidence-based cadence.

## 7. Timeout and retry NFRs

The local administrative path must never wait indefinitely.

### 7.1 Provisional default budgets

For the current same-host loopback API:

- connection timeout: **1 second**;
- ordinary read/health request total timeout: **3 seconds**;
- bounded configuration/test request total timeout: **5 seconds**, unless a version-pinned operation is proven to require a longer explicit budget;
- every subprocess/service-control call must also have a finite task-specific timeout.

These are internal provisional defaults for a loopback control path, not public service SLOs. They may be adjusted from observed behavior only with a recorded reason and regression coverage.

### 7.2 Retry rules

- **Read-only GET:** at most **2 retries** after transient transport/5xx failure with short bounded backoff; validate the final response.
- **401/403:** no retry with the same credential; treat as credential/access failure.
- **400/422 or schema/contract failure:** no blind retry; correct the input/contract or block.
- **Safe non-mutating validation/test POST:** may retry once only when the exact endpoint is proven non-mutating/idempotent for the pinned version.
- **Mutation:** never blindly retry after timeout, disconnect, 5xx or ambiguous response. Re-read actual target state first.

Retries must not turn an unavailable control plane into a long cascade that exceeds the operational recovery/alert budget.

## 8. Mutation/idempotency and partial-failure reconciliation

AdGuard Home's API contract does not provide a project-wide idempotency-key guarantee. UseSafeWeb therefore enforces idempotency by **pre-state + bounded delta + read-back**, not by assuming HTTP method semantics are sufficient.

For each authorized mutation:

1. **pre-read** exact affected fields and current service/version identity;
2. validate the requested delta against this NFR and task acceptance;
3. capture/verify the applicable recovery/rollback source;
4. execute one bounded mutation;
5. **read back** the exact affected API fields and required persisted configuration fields;
6. verify privacy/security/listener/service-health invariants and the relevant functional test;
7. classify outcome:
   - desired state fully verified -> success;
   - original state clearly remains -> one corrected retry may be permitted if the operation is safely repeatable;
   - mixed/unknown state -> partial/ambiguous failure; stop ordinary progression, reconcile target state, then rollback or repair under authority;
8. never mark success from HTTP 200/write acknowledgement alone.

Where a change requires service restart/config-file transition, use an exact pre-change hash/backup, syntax validation before restart, service health after restart, and rollback/read-back on failure. The accepted TSK-0201 two-phase admin-bind transition is precedent for respecting version-specific bind behavior rather than bypassing validation.

## 9. Setup/configuration identifier rule

### Current decision: no AdGuard-derived setup identifier is required

The current accountless product and shared global DNS service do **not** require a per-parent/per-device AdGuard configuration identifier. The customer uses the shared resolver identity and product-side temporary state; AdGuard remains infrastructure.

Therefore:

- do not create persistent AdGuard clients merely to obtain identifiers;
- do not expose filter-list IDs, internal client UIDs, admin usernames or configuration hashes as customer identifiers;
- do not use IP address, device fingerprint or profile content as an implicit identifier.

### If a future technical mechanism proves an opaque operation ID necessary

It may exist only after the owning data/interface contract is reopened and must be:

- random with **>=128 bits of entropy**;
- opaque and non-semantic;
- not derived from parent/child/device/account/IP/domain data;
- short-lived and scoped to one operation/journey;
- non-reusable after completion/expiry;
- excluded from ordinary logs/analytics in full form;
- subject to TSK-0229/0230 retention/no-linkage controls;
- not evidence that a persistent datastore or customer authentication is needed.

## 10. Version and contract regression gate

Every AdGuard version change or material control-interface change must revalidate the exact adapter contract **before** production reliance.

Minimum compatibility gate:

1. installed binary/version equals the approved release under test;
2. official source tag/commit and OpenAPI contract for that exact version are pinned/readable;
3. required `/control` paths and HTTP methods still exist;
4. Basic-Auth/admin behavior remains compatible with the private control boundary;
5. required response/request schemas parse and required fields retain expected types/semantics;
6. query-log/statistics privacy fields remain explicit and enforceable;
7. persisted configuration schema paths for `querylog.file_enabled`, anonymisation and other critical invariants are rechecked rather than assumed stable;
8. deprecated endpoints are not newly adopted when a current endpoint exists;
9. admin/listener/privacy/filter/upstream/TLS regression suite passes on an isolated/reversible target before production change;
10. recovery artifacts/scripts/configuration are updated and proven compatible where the version changes them.

Unexpected contract drift blocks the affected mutation/integration; it is not solved by dropping validation or defaulting missing fields.

## 11. Safe behavior when AdGuard/control API is unavailable

### Customer/public resolver path

An unavailable **admin API alone** must not cause the customer UI to claim protection failure if independent public resolver verification remains healthy. Admin-plane health and customer-plane protection evidence are separate.

### Setup/verification path

If the approved public DNS verifier cannot establish current protection:

- do not substitute admin API reachability as user verification;
- use the TSK-0320 state semantics (`Action needed`, `Not covered`, or `Status uncertain/error` as applicable);
- provide retry/recovery/removal guidance through TSK-0042;
- never turn parent confirmation into technical verification.

### Administrative mutation path

If `/control` is unavailable, authentication fails, schema validation fails, version is unsupported, or read-back cannot prove the resulting state:

- perform no additional unrelated mutation;
- do not expose admin credentials or broaden admin network access as a workaround;
- preserve the last independently verified customer-facing protection state only while its own evidence remains valid;
- classify the operator action as failed/uncertain and trigger the applicable reliability/security runbook;
- if DNS service itself is impaired, follow the TSK-0538 <=30-minute end-to-end recovery objective and fail-safe state rules;
- rollback/repair only from an evidenced known-good state and within action authority.

### No unsafe fallback

Never fall back to plaintext public DNS administration, public `/control`, query-history inspection, disabled privacy controls, or a customer account/database simply because the admin API is unavailable.

## 12. Error taxonomy exposed by the future adapter

A future internal adapter should normalize AdGuard/version-specific failures into a small non-sensitive internal taxonomy rather than leaking raw server details to the product UI:

- `CONTROL_UNAVAILABLE`;
- `CONTROL_AUTH_FAILED`;
- `CONTROL_CONTRACT_MISMATCH`;
- `CONTROL_INPUT_REJECTED`;
- `CONTROL_MUTATION_AMBIGUOUS`;
- `CONTROL_STATE_MISMATCH`;
- `CONTROL_HEALTH_FAILED`;
- `CONTROL_VERSION_UNSUPPORTED`.

Raw internal error details remain operational evidence only when privacy/security-safe. Customer-facing copy uses the owning product/recovery state contract, not these internal codes verbatim.

## 13. Testable implementation assertions

A later implementation/security/QA suite must prove at least:

1. public/browser/customer components cannot reach or authenticate to `/control`;
2. no AdGuard admin secret is present in browser bundles, downloadable profiles, product telemetry or Git;
3. unauthenticated control access remains rejected;
4. admin listener remains loopback/private only;
5. allowed adapter endpoints are explicitly allowlisted; arbitrary `/control/*` proxying is impossible;
6. API responses are schema/type validated and missing required fields fail closed;
7. query-log enabled is explicitly false after relevant mutations;
8. query-log file persistence is explicitly false from persisted/live configuration;
9. statistics enabled is explicitly false;
10. client-IP anonymisation is explicitly true from API + persisted/live configuration;
11. ECS and other current privacy invariants remain disabled/as approved;
12. no persistent customer AdGuard client is created by an accountless setup;
13. read calls honor finite timeouts and bounded retry count;
14. 401/403/schema errors are not blindly retried;
15. ambiguous mutation failure triggers read-back/reconciliation before any retry;
16. HTTP success alone cannot satisfy mutation acceptance without exact state read-back;
17. partial/mixed state blocks downstream progression until repaired/rolled back and reverified;
18. unsupported AdGuard version/OpenAPI drift fails the compatibility gate before mutation;
19. no opaque setup ID exists unless an owning contract proves necessity; any such ID satisfies >=128-bit/no-linkage/TTL rules;
20. admin-plane outage cannot be translated into an optimistic or pessimistic customer protection claim without independent public verification;
21. verifier outage produces truthful uncertain/action-needed behavior rather than parent-confirmation-as-verification;
22. rotation tests prove new credential works, old credential is invalidated only after verification, and neither secret appears in logs/Git;
23. failure/recovery tests preserve the TSK-0538 RTO/privacy/security invariants;
24. account/customer-auth/database dependencies remain absent from the current adapter boundary.

## 14. ACC-0044 traceability

ACC-0044 requires the private/restricted administration path, secret storage/rotation, API/config timeouts/retries, partial-failure reconciliation, opaque setup/configuration identifiers if technically required, explicit privacy booleans, version/contract regression checks, safe unavailable behavior, and no mandatory customer-authentication or persistent datastore dependency.

- §§1–4 define the private control/customer boundary and allowed surface.
- §§5–6 define explicit privacy booleans and credential isolation/rotation.
- §§7–8 define finite timeout/retry/idempotency/partial-failure reconciliation.
- §9 establishes that no setup ID is currently required and constrains one if future necessity is proven.
- §10 defines exact-version contract regression gates.
- §§11–12 define fail-safe behavior and normalized non-sensitive failures.
- §13 provides testable implementation assertions.
- accountless/no-datastore and all current privacy/security/behavioral gates remain unchanged.

**TSK-0044 result: PASS candidate for provisional internal L4 interface/NFR-definition acceptance only, subject to independent verification, GitHub read-back and runtime reconciliation. No AdGuard mutation, secret rotation, account system, datastore, implementation or release is authorized.**
