# TSK-0410 — Post-CR-0008 Allowlisted Server-Side AdGuard Adapter and ClientID Lifecycle Contract

**Task:** TSK-0410 — Design allowlisted server-side AdGuard adapter and ClientID lifecycle contract  
**Acceptance / Verification / Evidence:** ACC-0410 / VER-0410 / EVD-0410  
**Lifecycle / Priority / Authority:** L5 / MEDIUM / A3 / AUTO_ALLOWED  
**Version:** 1.0.0-post-CR0008  
**Date:** 2026-09-02 UTC  
**Gate:** contributes to LG-07 Architecture, Security, Privacy and Delivery Readiness  
**Direct predecessors:** TSK-0411 current PASS; TSK-0232 current PASS; TSK-0352 current PASS

## 1. Decision

Freeze a **private, typed, server-side adapter** for the optional parent/device capability. The adapter is the only application boundary permitted to invoke AdGuard Home administrative client-lifecycle operations.

The Version-1 adapter:

- targets exactly **AdGuard Home v0.107.79 / API 0.107** until a separately accepted compatibility change;
- never exposes a raw or generic `/control/*` proxy;
- keeps AdGuard Basic-Auth/admin credentials server-side and outside browser, logs, analytics and Git;
- accepts only an already-authenticated, already-server-authorized parent-owned device context from the TSK-0232 boundary;
- generates/uses persistent ClientIDs only for optional authenticated managed-device lifecycle; accountless DNS continues without a persistent ClientID;
- exposes only typed client search/create/reconcile/update/rotate/delete plus version/privacy-baseline compatibility checks required to protect those operations;
- emits a canonical AdGuard `Client` payload from server-owned state/profile definitions, never arbitrary browser JSON;
- sets and re-verifies `ignore_querylog=true` and `ignore_statistics=true` on every managed persistent client;
- does **not** disable or repurpose the separately approved global **anonymized aggregate operational statistics with 24-hour retention** from TSK-0413; managed-client identifiable statistics/history remain excluded;
- preserves the accepted direct DoH ClientID route `https://dns.usesafeweb.com/dns-query/{client_id}`;
- fails closed on ownership, version, schema, privacy, credential, response-shape or reconciliation uncertainty;
- never treats HTTP acknowledgement, ClientID possession, dashboard state or datastore state as technical Protection Map verification.

This task designs the interface and lifecycle only. It does not implement code, open a network path between application and AdGuard, create/update/delete a live client, rotate a credential, configure production, pass LG-07 or authorize L6.

## 2. Current authoritative source baseline

### 2.1 Project predecessors

Current accepted sources:

- `TSK_0411_DNS_SERVICE_TOPOLOGY_CLIENT_CONFIGURATION_MODEL_2026-09-01.md`, blob `8bd206e3832bafc5b8033dddd3e7913a5e01f7b6`;
- `TSK_0232_POST_CR0008_PARENT_DEVICE_OWNERSHIP_AUTHORIZATION_MODEL_2026-09-02.md`, blob `30de2625f977e4d8017630c15de74ea19fde195c`;
- `TSK_0352_POST_CR0008_ADGUARD_PERSISTENT_CLIENTID_API_LIFECYCLE_CONTRACT_2026-09-02.md`, blob `e5cbbcac2f42810527717549482765b6b1ad72c1`.

Compatible current supporting evidence:

- `infrastructure/adguard-server/TSK-0412-ADGUARD-COMPATIBILITY-REVERIFICATION.md`, blob `1fa96f3264a8c6eb28c0b5ee3085fca60399e8e7`;
- `infrastructure/adguard-server/tsk-0413-bundle-v1/README.md`, blob `5a162a87dd2761ff5a0da587fa660549309a1404`;
- `infrastructure/adguard-server/tsk-0413-bundle-v1/AdGuardHome.public-fragment.yaml`, blob `867ef7162c739106fa42af151cda145f6d16888e`;
- TSK-0142 current dashboard/device-management requirements; browsing/query/activity history, raw AdGuard administration, broad per-domain allow/block administration and unrestricted filter/upstream controls remain non-goals.

### 2.2 Exact official AdGuard v0.107.79 API recheck — 2026-09-02

Exact version-pinned source:

`https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/v0.107.79/openapi/openapi.yaml`

Current exact facts consumed by this design:

- API title `AdGuard Home`, version `0.107`;
- API server base `/control`;
- global API security `basicAuth`;
- `POST /clients/add` -> `clientsAdd`;
- `POST /clients/update` -> `clientsUpdate` with current `name` plus replacement `data: Client`;
- `POST /clients/delete` -> `clientsDelete` with `name`;
- old `GET /clients/find` is deprecated in favor of `POST /clients/search`;
- `POST /clients/search` performs an exact-match search for IP/CIDR/MAC/ClientID;
- `Client.ids` accepts ClientID;
- `Client.ignore_querylog` and `Client.ignore_statistics` exist and default to false on add if omitted, so UseSafeWeb must set them explicitly;
- search responses expose the fields required to verify name/IDs/privacy flags.

Current official AdGuard Knowledge Base also documents persistent ClientIDs for encrypted DNS and URL ClientID routing as `https://example.org/dns-query/my-client`. Therefore the current UseSafeWeb route remains `https://dns.usesafeweb.com/dns-query/{client_id}`.

No v0.108+ server-name ClientID behavior, preview behavior or master-branch-only API is imported into this pinned v0.107.79 contract.

## 3. Trust and network boundary

### 3.1 Browser/application boundary

The browser may call only product APIs. It never receives:

- AdGuard Basic-Auth username/password;
- raw AdGuard client name;
- arbitrary `/control` path/method/body capability;
- global DNS/filter/upstream configuration;
- query log/statistics records;
- another parent’s ClientID or device binding.

A product request reaches the adapter only after the TSK-0356 verified server session and TSK-0232 owned-device authorization succeed.

### 3.2 Application/AdGuard administrative boundary

TSK-0411 keeps AdGuard administration authenticated and loopback-only on the DNS host while the web/application VM is separate. Therefore the adapter requires a separately approved **private/restricted server-to-server control transport** that terminates at that protected administrative boundary. The exact private transport mechanism is implementation/deployment work and is not invented here.

Until that private route is proven, adapter mutations are disabled. The product must never solve control connectivity by publicly exposing TCP 3000 or an unrestricted reverse proxy to `/control/*`.

Basic Auth is necessary for the pinned API but is not the sole network authorization control. Credentials are injected from the governed secret mechanism, least-privilege/restricted to this adapter boundary, rotated/revoked through the owning secret-management process and never committed.

## 4. Public adapter interface

The internal application interface is typed and narrower than AdGuard’s API. Exact programming-language names may change without reopening this ADR if semantics remain equivalent.

```text
assertCompatibleAdGuard() -> CompatibilityResult
searchOwnedBinding(AuthorizedDeviceContext) -> ClientObservation
createOwnedBinding(AuthorizedDeviceContext, CuratedProfileId) -> BindingResult
reconcileOwnedBinding(AuthorizedDeviceContext) -> BindingResult
applyCuratedProfile(AuthorizedDeviceContext, CuratedProfileId, ExpectedVersion) -> BindingResult
rotateClientId(AuthorizedDeviceContext, ExpectedVersion, RotationReason) -> BindingResult
deleteOwnedBinding(AuthorizedDeviceContext, ExpectedVersion) -> BindingResult
```

There is deliberately **no** generic method equivalent to:

- `request(method, path, body)`;
- `search(clientIdFromBrowser)`;
- `updateArbitraryClient(clientJson)`;
- `setUpstream(...)`;
- `setFilterList(...)`;
- `readQueryLog(...)`;
- `readPerClientStats(...)`;
- `setGlobalDnsConfig(...)`.

## 5. `AuthorizedDeviceContext`

The adapter accepts only a server-created context produced after TSK-0232 authorization. Minimum semantics:

- current authenticated `parent_id` derived from the verified server session;
- current owned `device_id`;
- current `row_version` / operation version;
- stored server-side binding state, if present;
- stored server-generated `adguard_client_name` and ClientID only when that binding belongs to this device;
- approved profile/version reference;
- operation/reconciliation identity when a mutation is already pending.

The adapter must not accept browser-provided `parent_id`, AdGuard name or arbitrary ClientID as authority. A ClientID received from a browser is never used to select an AdGuard object for mutation.

## 6. ClientID and AdGuard-name contract

### 6.1 ClientID

Consume the already accepted TSK-0352 format:

- generated server-side using a cryptographically secure random source;
- exactly 26 lowercase RFC-4648 base32 characters without padding (`a-z`, `2-7`), approximately 130 bits of space;
- independent of parent, provider subject, email, child/device nickname, IP address or browsing content;
- exact `/clients/search` collision check before creation/rotation;
- collision -> generate a fresh candidate before mutation;
- ClientID never grants product authorization.

### 6.2 AdGuard client name

- server-generated opaque name in an adapter-owned namespace;
- not derived from parent/email/nickname/child identity;
- stored only server-side because pinned update/delete operations use the current name;
- never accepted from browser input as an object selector;
- exact syntax/version convention is adapter-versioned so a recovered binding can be distinguished from an unrelated operator-created client.

## 7. Curated profile compiler

The account product never edits a raw AdGuard `Client` object. The adapter compiles a versioned `CuratedProfileId` into a **complete canonical v0.107.79 Client payload**.

### 7.1 Current baseline profile

The current safe baseline uses:

- exactly the one server-generated ClientID in `ids`;
- explicit `ignore_querylog=true`;
- explicit `ignore_statistics=true`;
- global UseSafeWeb filtering/upstream policy inherited rather than a user-selected per-client upstream;
- no browser-defined tags, upstreams, filter lists, arbitrary blocked-services list or raw rule text;
- no deprecated `safesearch_enabled` integration in new adapter code;
- only fields proven necessary by the exact version-pinned schema and current approved product profile.

### 7.2 Future curated profiles

A later product-control profile may become valid only when a canonical product/security/privacy decision explicitly defines the parent-understandable control and its exact mapping. Adding a profile requires:

1. versioned profile ID and exact server-owned mapping;
2. evidence that it is within approved product scope;
3. privacy/security review;
4. deterministic input/schema and read-back tests;
5. no raw customer-defined upstream/filter/rule/admin payload;
6. rollback/reconciliation mapping;
7. current AdGuard compatibility verification.

Until then, `applyCuratedProfile` accepts only the current baseline/inherited profile. The existence of an adapter method is not permission to invent a new DNS-control feature.

## 8. Privacy/statistics contract

There are two separate scopes and they must not be conflated.

### 8.1 Managed persistent client

Every add/update/rotation/reconciliation payload explicitly requires:

- `ignore_querylog = true`;
- `ignore_statistics = true`.

A read-back where either is false, missing or ambiguous is **not Active/healthy**. The adapter must repair through the governed update flow or fail closed.

### 8.2 Global operational statistics

TSK-0413 separately freezes:

- persistent/file query logging off;
- client-IP anonymization on;
- global anonymized aggregate operational statistics on with 24-hour retention;
- identifiable per-client statistics/history excluded.

The account-owned client adapter does not read or expose query logs or customer/per-client statistics. It does not disable the approved global aggregate operational-statistics mechanism merely because managed clients set `ignore_statistics=true`.

Any operator-facing aggregate statistics access belongs to the separate observability/operations contract and must contain no browsing-history product or identifiable per-client view.

## 9. Compatibility gate

`assertCompatibleAdGuard()` is a fail-closed prerequisite for a consequential client mutation after deployment/startup/version drift evidence.

It must prove, directly or via current durable deployment evidence tied to the exact target:

1. target build is exactly the accepted AdGuard Home v0.107.79 unless a separately accepted replacement exists;
2. private `/control` Basic-Auth boundary is intact;
3. `clientsAdd`, `clientsSearch`, `clientsUpdate`, `clientsDelete` request/response shapes match the adapter version;
4. exact search semantics by ClientID remain available;
5. `ignore_querylog` and `ignore_statistics` fields and semantics remain present;
6. current global privacy/config bundle is compatible with schema 34 and the target;
7. no public unrestricted AdGuard admin/control exposure exists;
8. current DNS service identity/topology remains compatible with the direct DoH ClientID route.

A mismatch disables the affected mutation path. DNS baseline/accountless service continues independently if healthy; the adapter does not automatically upgrade AdGuard.

## 10. Response validation

No HTTP response is trusted solely because its status is 200.

For a persistent binding to be considered exact desired state, a post-mutation exact `/clients/search` observation must establish:

- exactly one expected ClientID match;
- expected server-managed AdGuard client name;
- expected `ids` set, including no unexpected cross-binding identifier;
- `ignore_querylog=true`;
- `ignore_statistics=true`;
- every profile-owned field equals the canonical compiled value;
- no unexpected per-client upstream/control field that contradicts current policy;
- the local `parent_id/device_id -> binding` relation still matches the operation that initiated the mutation.

Zero matches, multiple/conflicting matches, name mismatch, privacy mismatch, unexpected IDs/profile drift or schema ambiguity is a non-terminal failure/reconciliation state.

## 11. Create lifecycle

`createOwnedBinding`:

1. verify current authorized parent/device context and expected row version;
2. prove no active/pending binding already exists for the device;
3. run the compatibility gate;
4. generate opaque AdGuard name and 26-character ClientID;
5. exact search proves the ClientID is absent;
6. persist/reuse the durable bounded `creating` operation identity before external mutation;
7. compile the canonical profile with both privacy flags explicit;
8. perform **one** `POST /control/clients/add` attempt for that unresolved operation;
9. exact search/read-back classifies actual AdGuard state;
10. mark local binding Active only after one exact desired-state observation and successful local compare-and-swap;
11. only then return the direct DoH endpoint to the authenticated owner flow.

If the HTTP acknowledgement is lost/ambiguous, do not send another add before exact search/reconciliation.

## 12. Search/reconciliation lifecycle

The adapter’s search method accepts only the **server-stored/generated** ClientID from the owned binding/operation context.

Classify exact search as:

- `ABSENT` — zero exact matches;
- `DESIRED` — one exact expected match and all privacy/profile fields match;
- `DRIFTED` — one expected identity but profile/privacy differs;
- `CONFLICT` — multiple results, unexpected name/IDs or incompatible identity;
- `UNAVAILABLE` — timeout/transport/provider error leaves state unknown.

Customer-facing UI receives only a product-safe typed result, never raw AdGuard objects/credentials.

## 13. Update and curated-profile lifecycle

`applyCuratedProfile` or privacy repair:

1. authorize current owned device and expected row version;
2. run compatibility gate;
3. exact search/read current binding;
4. require one expected server-owned name/ClientID relation;
5. compile a **complete replacement `Client`** from server-owned current state and approved profile; do not merge arbitrary browser fields;
6. preserve explicit privacy flags true;
7. persist/reuse a bounded pending operation before mutation;
8. perform one `POST /control/clients/update` using the current server-read name and canonical replacement `data`;
9. exact search/read-back must reach `DESIRED` before local terminal success;
10. local compare-and-swap finalization must still match the initiating device/operation.

No blind JSON patch is assumed safe because the pinned API update contract accepts a replacement `Client` object.

## 14. ClientID rotation/replacement

`rotateClientId`:

1. authorize current parent/device and current expected version;
2. exact search proves the current stored binding;
3. generate/search-confirm a fresh ClientID;
4. persist a rotation operation containing only old/new opaque identifiers and required reconciliation metadata;
5. update the existing server-owned client with the new ClientID and canonical profile/privacy flags;
6. exact search proves the new desired mapping;
7. exact search of the old ID proves it no longer identifies that persistent client;
8. finalize the local binding via compare-and-swap;
9. return the new direct DoH endpoint to the authenticated flow;
10. do not claim the old physical phone/profile was removed or that DNS protection is currently Verified.

An unresolved rotation never generates a second replacement ID merely because a response was lost.

## 15. Delete / revoke lifecycle

`deleteOwnedBinding`:

1. authorize current owned device or continue from a previously authorized deletion/reconciliation operation;
2. verify expected local version/lifecycle state;
3. run compatibility gate where available; if service is unavailable, preserve pending safe state rather than declaring deletion;
4. exact search by stored ClientID;
5. `ABSENT` may be reconciled as AdGuard-side idempotent deletion;
6. otherwise require one expected name/ClientID relation;
7. move local operation to revoking/pending before mutation;
8. perform one `POST /control/clients/delete` using only the **server-read/stored expected name**;
9. exact search must prove absence;
10. only then may the TSK-0232 local device/account deletion sequence remove the binding/record as applicable.

A browser-supplied name/ClientID can never drive delete. Server-side deletion does not prove physical device DNS/profile removal.

## 16. Retry and timeout policy

### 16.1 Bounded transport

Every AdGuard control request must have finite connect/request/deadline limits configured by the implementation and verified against the target. No administrative request may wait indefinitely or outlive the owning product-operation deadline.

Exact millisecond/second values are **not fabricated at L5**; L6 synthetic/target evidence must freeze values that satisfy the current latency/recovery NFR without weakening fail-closed behavior.

### 16.2 Read-only retry

Read-only compatibility/search operations may retry a transient transport/5xx failure **at most two additional attempts** within the caller’s total deadline, using bounded backoff/jitter.

Do not retry 400/schema errors, 401/403 authentication/authorization failures or an observed logical conflict as though they were transient.

### 16.3 Consequential mutation retry

For add/update/delete/rotate:

- at most one consequential request is sent for an unresolved operation before state observation;
- any timeout, disconnect, 5xx or ambiguous acknowledgement is treated as **outcome unknown**;
- exact search/read of actual state occurs before considering another mutation;
- only a proven original/absent state may permit one fresh separately recorded mutation attempt;
- desired state closes success;
- conflicting/mixed state blocks normal progression and enters repair/reconciliation;
- no unbounded automatic mutation retry loop exists.

## 17. Idempotency and local/external convergence

AdGuard v0.107.79 is not assumed to accept a product idempotency key. Product idempotency therefore comes from TSK-0232 durable/reconstructable operation state plus read-before-write/read-after-write reconciliation.

For every mutation:

- one stable local operation identity per logical request;
- owned device and expected row version fixed at operation start;
- one exact desired AdGuard object identity/profile;
- one mutation before required observation;
- no new ClientID/name generated while the same operation is unresolved;
- terminal success only when local ownership/binding truth and observed AdGuard truth agree;
- an orphan may be deleted only when operation evidence proves it was created by this operation and no authoritative current binding adopted it.

## 18. Error taxonomy exposed to product code

Return typed errors/results, not raw HTTP bodies:

- `AUTHORIZATION_DENIED`
- `STALE_LOCAL_VERSION`
- `NO_BINDING`
- `COMPATIBILITY_BLOCKED`
- `ADGUARD_UNAVAILABLE`
- `ADGUARD_AUTH_FAILED`
- `SCHEMA_OR_REQUEST_REJECTED`
- `BINDING_CONFLICT`
- `PRIVACY_DRIFT`
- `PROFILE_DRIFT`
- `OUTCOME_UNKNOWN_RECONCILING`
- `DELETED_OR_ABSENT`
- `SUCCESS`

Error/log data may contain task/operation IDs, adapter version, coarse error class, HTTP status class and timing. It must not contain Basic-Auth values, raw session/provider tokens, DNS queries/domains, customer browsing history or unnecessary ClientIDs/names. If an opaque ClientID is required for a bounded diagnostic correlation, use a non-reversible short-lived correlation value rather than logging the raw ID.

## 19. Recovery and restore

A restored local binding is never trusted as current external truth.

After recovery:

1. verify adapter/version/private-control compatibility;
2. re-authorize/re-establish parent/device mapping under TSK-0232;
3. exact search every binding that must be active/reconciled;
4. verify ClientID/name/profile/privacy flags;
5. deleted/revoked bindings must not be resurrected;
6. unresolved operation state is reconciled before new consequential mutations;
7. restored protection metadata does not create a fresh technical `Verified` state.

The TSK-0413 recovery bundle contains no customer ClientIDs; account-owned binding recovery is therefore a separate minimum product-datastore/reconciliation concern and must remain within TSK-0232/TSK-0233 backup privacy boundaries.

## 20. Security and adversarial tests required downstream

Implementation acceptance must prove at least:

1. browser cannot reach arbitrary `/control/*` or TCP 3000;
2. Basic-Auth secret never appears in browser bundle, logs, errors, analytics, Git or returned JSON;
3. Parent A cannot search/read/update/rotate/delete Parent B’s binding by device ID, parent ID, ClientID or AdGuard name substitution;
4. ClientID possession grants zero account authorization;
5. arbitrary raw `Client` JSON, upstream, filter-list, rule, blocked-service list or admin path is rejected/not representable through product API;
6. accountless setup creates no persistent client;
7. add/update/rotation sets both privacy flags explicitly true;
8. post-mutation read-back rejects false/missing privacy flags;
9. multiple/conflicting search results fail closed;
10. duplicate/retried create does not create a second unintended client;
11. ambiguous add/update/delete/rotation observes state before another mutation;
12. 401/403/schema errors are not blindly retried;
13. pinned-version/schema drift disables mutation;
14. global anonymized 24-hour operational statistics remain a separate infrastructure capability and are not exposed as per-client history;
15. physical-device removal and Protection Map Verified state are not inferred from client deletion/creation/dashboard state.

## 21. Version change / migration trigger

Reopen this contract before an AdGuard version/schema change or if any of these facts change materially:

- client add/search/update/delete path or request/response shape;
- `/control` authentication boundary;
- ClientID syntax or DoH routing behavior;
- `ignore_querylog` / `ignore_statistics` availability/default/semantics;
- global query-log/statistics/anonymization schema;
- update replacement semantics;
- client name/delete selector semantics;
- TSK-0413 privacy configuration;
- TSK-0411 encrypted-DNS/service topology;
- a product requirement proposes broader DNS controls or arbitrary per-client filtering/upstreams.

Migration requires exact-version source review plus CRUD, authorization, privacy, idempotency, recovery and rollback tests. A newer release is never adopted solely because it exists.

## 22. ACC-0410 trace

| ACC-0410 requirement | Evidence | Disposition |
| --- | --- | --- |
| only authorised client lifecycle/curated-setting operations | Sections 4–7, 11–15 | SATISFIED |
| validates inputs and AdGuard responses | Sections 5–7, 10, 18, 20 | SATISFIED |
| admin credentials off browser | Sections 3–4, 18, 20 | SATISFIED |
| direct DoH ClientIDs | Sections 1, 2.2, 6, 11, 14 | SATISFIED |
| no-querylog/no-identifiable-statistics | Sections 7–8, 10–15 | SATISFIED |
| owner-approved anonymized aggregate statistics with 24-hour retention allowed | Sections 1, 8.2, 20 | SATISFIED without exposing per-client history |
| version pin / compatibility tests | Sections 2.2, 9, 20–21 | SATISFIED |
| retries and reconciliation | Sections 11–19 | SATISFIED |

## 23. Candidate stable disposition

**Candidate ACC-0410 = PASS**, subject to VER-0410 reviewer/read-back verification of this exact artifact and durable runtime synchronization.

This candidate PASS means the L5 adapter/interface/lifecycle contract is complete. It does **not** mean the adapter exists in code, the private control transport is deployed, any live ClientID/client has been created/mutated, target timeouts have been load-tested, backup/legal readiness is approved, LG-07 has passed, L6 is authorized or public activation is permitted.
