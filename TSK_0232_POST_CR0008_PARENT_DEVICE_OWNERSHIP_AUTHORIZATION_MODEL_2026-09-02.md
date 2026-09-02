# TSK-0232 — Post-CR-0008 Parent / Device Ownership and Authorization Model

**Task:** TSK-0232 — Design minimal parent/device model and ownership authorization boundary  
**Acceptance / Verification / Evidence:** ACC-0232 / VER-0232 / EVD-0232  
**Lifecycle / Priority / Authority:** L5 / MEDIUM / A3 / AUTO_ALLOWED  
**Version:** 1.0.0-post-CR0008  
**Date:** 2026-09-02 UTC  
**Gate:** contributes to LG-07 Architecture, Security, Privacy and Delivery Readiness  
**Direct predecessors:** TSK-0233 current PASS; TSK-0356 current PASS

## 1. Decision and scope boundary

Freeze the **logical**, datastore-independent Version-1 parent/device ownership model and authorization boundary below.

The model exists only for the optional parent-account/dashboard mode already authorized by DEC-0053/CR-0006. The complete accountless setup, verification, Protection Map, troubleshooting, recovery and removal journey remains usable without login wherever its own dependencies are healthy.

This task does **not** select or provision a database product, configure Firebase, implement application routes, mutate AdGuard, create a real parent/device, process real-user data, approve backup processing, resolve UK legal/data readiness, pass LG-07, or authorize L6.

### 1.1 Core invariants

1. One `ParentAccount` owns zero or more `ParentDevice` records.
2. Every `ParentDevice` has exactly one owning `ParentAccount` while the record exists.
3. Version 1 has **no shared/co-parent ownership, device transfer, delegated household role, child account, or cross-parent device view**. Adding any of these reopens this contract.
4. Parent identity is derived server-side from the verified TSK-0356 server session; a request-supplied parent identifier never grants authority.
5. Every device operation performs an ownership check server-side in the same authorization boundary as the resource operation.
6. `adguard_client_id` is an opaque server-side control-plane reference only. It is never authentication, authorization, a bearer credential, a customer-visible administrative secret, or technical proof that protection is active.
7. Internal parent/device identifiers are opaque, random, non-semantic and non-guess-dependent. Identifier secrecy is defense in depth only; authorization never relies on entropy alone.
8. The model stores no DNS question/domain/URL/browsing/top-domain/child-activity history and no persistent child profile.
9. Account/dashboard state and technical Protection Map verification remain distinct truth domains.
10. Deletion/revocation/restore must preserve ownership truth and cannot silently resurrect deleted authority or stale positive protection evidence.

## 2. Authoritative predecessor reconciliation

### 2.1 TSK-0233 data model boundary

Current accepted predecessor:

- `TSK_0233_MINIMAL_DUAL_MODE_JOURNEY_ACCOUNT_DATA_MODEL_2026-09-01.md`
- version `1.0.1`
- blob `156a1811bc4322e16474874e728d23a97a93ec4c`

Binding rules consumed here:

- J0 browser/session state and optional J1 anonymous transient state have no parent/account/provider/device/ClientID linkage;
- sign-in does not migrate/import J0/J1 history into the account domain;
- persistent A-domain data is limited to minimum parent/device ownership/settings/lifecycle/current-protection metadata;
- `ParentAccount` currently requires only opaque parent identity/lifecycle/concurrency fields and minimum provider-subject mapping;
- `ParentDevice` currently requires only opaque device/parent ownership, optional nickname/platform, lifecycle, approved settings references, current freshness-bounded protection metadata, concurrency fields and server-side ClientID linkage;
- every A-domain operation checks parent ownership server-side;
- J0/J1 are never restored from backup;
- A-domain production backup processing is blocked until exact retention/access/encryption/deletion-propagation/restore semantics are frozen;
- physical device DNS/profile removal is separate from deleting server/account records.

### 2.2 TSK-0356 authentication/session boundary

Current accepted predecessor:

- `TSK_0356_POST_CR0008_FIREBASE_AUTH_SERVER_SESSION_ARCHITECTURE_2026-09-02.md`
- version `1.0.0-post-CR0008`
- blob `7dd47124db837ea4eaf6a06661788423d22f3c6e`

Binding rules consumed here:

- base Firebase Authentication / Google is the planned initial optional-account identity route;
- the application uses a server-managed session cookie after server verification of a fresh Firebase ID token;
- protected account routes perform revocation-aware session verification;
- authentication never substitutes for resource ownership authorization;
- Firebase UID/provider subject is identity input only;
- account-only provider/session uncertainty fails closed while the accountless core remains independently usable;
- email, display name and profile image are not ownership keys and are not persisted merely because a provider exposes them.

## 3. Logical entities

The following is the maximum logical entity surface required by this task. A later datastore implementation may represent these structures differently only if all field, uniqueness, authorization, deletion and concurrency semantics remain provably equivalent.

### 3.1 `ParentAccount`

| Field | Required | Contract |
| --- | --- | --- |
| `parent_id` | yes | Opaque internal ownership root; random/non-semantic; generated server-side; never accepted from the browser as authority. |
| `provider_subject` | yes for current optional Google/Firebase account | Minimum server-side mapping from the verified Firebase identity to this parent. Unique within the configured Firebase identity namespace. Never use email as the uniqueness/ownership key. |
| `account_status` | yes | Current lifecycle state only, sufficient to distinguish normal operation from at least deleting/disabled/fail-closed states; no activity-history ledger. |
| `row_version` | yes | Monotonic optimistic-concurrency token or exactly equivalent compare-and-swap version. |
| `created_at` | yes | Minimum lifecycle/reconciliation timestamp; not an activity timeline. |

**Not present by default:** child identity/profile, browsing/query/activity history, provider access/refresh/ID token, Firebase session-cookie value, password, SMS credential, email/display name/photo merely for convenience, marketing profile, arbitrary provider claims.

### 3.2 `ParentDevice`

| Field | Required | Contract |
| --- | --- | --- |
| `device_id` | yes | Opaque internal resource identifier; random/non-semantic; generated server-side. |
| `parent_id` | yes | Required ownership reference to exactly one current `ParentAccount`. Server-populated. |
| `nickname` | optional | Parent-facing convenience label only; never a business/authorization key; no cross-parent search requirement. |
| `platform_family` | yes when needed by approved device-management behavior | Coarse supported-platform value only; no hardware serial/IMEI/advertising identifier. |
| `lifecycle_status` | yes | Current lifecycle/control state only; must support safe active, provisioning/reconciling and revoke/delete semantics without an activity-history ledger. |
| `adguard_client_id` | conditional | Server-side opaque AdGuard control reference after/while provisioning; never authorization; never exposed as a customer/admin secret. |
| `settings_profile_id` | conditional | Reference to an approved curated settings profile, not arbitrary/raw AdGuard administration. |
| `settings_version` | conditional | Version of the approved curated setting contract. |
| `protection_state` | conditional/current-only | Latest freshness-bounded parent-facing state; not self-validating technical evidence. |
| `protection_reason_code` | conditional/current-only | Bounded explanation of current state without DNS history. |
| `verifier_version` | conditional/current-only | Version of verifier that produced current technical evidence. |
| `evaluated_at` | conditional/current-only | Current-evidence timestamp only; not an activity timeline. |
| `evidence_fresh_until` | conditional/current-only | Expiry boundary preventing stale positive protection claims. |
| `row_version` | yes | Monotonic optimistic-concurrency token or equivalent compare-and-swap version. |
| `created_at` | yes | Minimum lifecycle/reconciliation timestamp. |
| `updated_at` | yes | Current-row mutation timestamp only; not an event history. |

**Explicitly prohibited:** DNS query/domain/URL/top-domain data, child activity, device location, contacts/messages/photos/social content, raw diagnostics, unrestricted AdGuard configuration, stable browser fingerprint, hardware serial/IMEI/advertising ID, accountless journey history.

## 4. Cardinality and uniqueness rules

A conforming datastore must enforce these semantics transactionally or with an equivalently safe constraint mechanism:

1. `parent_id` is globally unique within the application datastore.
2. `device_id` is globally unique within the application datastore.
3. A current `provider_subject` maps to **at most one** current `ParentAccount` inside the configured Firebase identity namespace.
4. `ParentDevice.parent_id` must resolve to one current `ParentAccount`; an orphaned device row is invalid.
5. A non-null active/current `adguard_client_id` maps to **at most one** current `ParentDevice`.
6. A `ParentDevice` cannot change `parent_id` in Version 1. Device ownership transfer/shared ownership is out of scope; remove/recreate under a separately approved future lifecycle if ever authorized.
7. Deleting a parent must not blind-cascade through unresolved external AdGuard state. Device/control-plane disposition must be reconciled first or explicitly fenced in a safe deletion state before the parent relationship is finalized.
8. Restoring a datastore cannot bypass current uniqueness/ownership/deletion constraints.

These are logical guarantees, not a mandate for SQL, a particular database engine, or a particular index syntax.

## 5. Internal identifier contract

### 5.1 Parent and device identifiers

- Generate `parent_id` and `device_id` server-side from a cryptographically strong opaque identifier space with **at least 128 bits of randomness/effective unpredictability** (for example UUIDv4 or an equivalently strong random identifier).
- Do not encode email, Firebase UID, platform, child data, account creation time, sequential customer number or other semantics into public/internal resource identifiers.
- Identifiers may be visible to the authenticated parent as route/resource handles if necessary, but visibility never grants authority.
- Do not expose raw datastore primary-key sequencing as a security boundary.

### 5.2 Provider subject

- `provider_subject` is a server-side identity mapping input from the verified TSK-0356 session.
- It is not a user-controlled path parameter for ownership decisions.
- Email/display name is never substituted if the provider subject changes/mismatches.
- Ambiguous provider identity fails account-only operations closed; no silent account merge by email.

### 5.3 AdGuard ClientID

- ClientID belongs to a separate control-plane namespace.
- It is generated/managed only through the later approved TSK-0410 lifecycle contract.
- Possessing/guessing/submitting a ClientID never permits reading or mutating a device record.
- The browser must not be allowed to select another record by ClientID.

## 6. Authorization boundary

### 6.1 Authentication-to-parent resolution

For every account-only request:

1. validate the TSK-0356 server session under the current revocation-aware contract;
2. obtain the immutable verified provider subject/UID from the trusted session result;
3. resolve that subject server-side to the current `ParentAccount`;
4. reject if no active/authorized parent mapping exists or the account is deleting/disabled/otherwise fail-closed;
5. never accept `parent_id`, provider subject, email or ownership state from request input as authority.

### 6.2 Device resource authorization

Every device **list, read, create, rename/update, settings change, provision, verify, reinstall, revoke, unlink, remove, delete, recover or replace** operation must authorize against the authenticated parent.

For existing-resource operations the preferred logical access primitive is:

`device_id = requested_device_id AND parent_id = session_parent_id`

The ownership predicate must be part of the authoritative server-side lookup/mutation boundary, not a client-side filter and not an optional after-check.

Rules:

- list returns only records whose `parent_id` equals the current session parent;
- create ignores/rejects any browser-supplied `parent_id` and server-populates ownership;
- read/update/delete/revoke/recover requires the owned-resource lookup above;
- settings/AdGuard operations require a successfully owned `ParentDevice` **before** ClientID/control-plane access is considered;
- authorization is re-evaluated for every consequential request; earlier access does not create durable future authority;
- generic not-found/unauthorized handling must not reveal whether another parent’s device exists;
- session/account/dashboard presence never creates technical `Verified` protection truth.

### 6.3 Conceptual API surface

Exact route names are implementation detail, but the Version-1 interface should be no broader than equivalent account-scoped resources such as:

- `GET /api/account/devices`
- `POST /api/account/devices`
- `GET /api/account/devices/{deviceId}`
- `PATCH /api/account/devices/{deviceId}`
- bounded lifecycle operations on `/api/account/devices/{deviceId}/...` only where a plain idempotent resource operation cannot truthfully represent the external-control effect.

There is no need for a browser-controlled `/parents/{parentId}/...` authority surface in Version 1. Cookie-authenticated unsafe requests remain subject to the current TSK-0353 CSRF/request-integrity contract.

## 7. Required indexes / access paths

The datastore implementation must provide the equivalent of these bounded access paths and constraints:

| Purpose | Required logical index/constraint |
| --- | --- |
| Session identity -> parent | unique lookup on current `provider_subject` within the configured Firebase identity namespace |
| Parent dashboard/list | index/access path beginning with `parent_id`; if lifecycle filtering is implemented, `(parent_id, lifecycle_status, device_id)` or equivalent |
| Owned device operation | composite owned-resource lookup equivalent to `(parent_id, device_id)`; `device_id` remains globally unique but ownership still participates in authorization |
| AdGuard reconciliation | unique non-null current `adguard_client_id` lookup, server-side only |
| Primary concurrency resource | primary/unique `parent_id` and `device_id` plus current `row_version` available to compare-and-swap mutations |

Do **not** add broad global indexes on nickname, child data, browsing/query fields, provider email or arbitrary profile fields for convenience. No such search requirement exists.

## 8. Concurrency and idempotency

### 8.1 Optimistic concurrency

Every mutable `ParentAccount` and `ParentDevice` row carries `row_version` or an exactly equivalent concurrency token.

For a mutation against an existing resource:

1. authorize ownership from the current server session;
2. read/accept the current expected version under the operation contract;
3. update only if the stored version still matches;
4. advance the version atomically on success;
5. return a bounded conflict (`409` or equivalent typed conflict) on stale version rather than overwriting newer state;
6. re-read authoritative state before any retry of a consequential mutation.

`updated_at` alone is not the concurrency control.

### 8.2 Create/provision idempotency

A browser retry, network timeout or duplicate submit must never produce duplicate parent/device authority or multiple unintended AdGuard clients.

- parent creation is constrained by the unique verified `provider_subject` mapping;
- device creation uses a server-generated `device_id` and a bounded idempotency/reconciliation mechanism sufficient to distinguish retry from a new requested device;
- an idempotency token is an operation-control value, not a permanent activity record or authorization bearer;
- exact operation-state persistence is owned by downstream implementation/reconciliation design, but it may contain only the minimum opaque operation/resource/version/result fields necessary to converge safely;
- a duplicate request either resolves to the original safe result/current state or returns a typed conflict/uncertain state. It must not create a second ClientID/device merely because the first response was lost.

### 8.3 External-control concurrency

Operations that will later call AdGuard use a compare/reconcile pattern:

1. owned device identified and current row version checked;
2. transition to the smallest truthful in-flight/reconciling lifecycle state;
3. call only the allowlisted server-side adapter defined by TSK-0410;
4. read back/reconcile the external result;
5. finalize the local row only after the external disposition is known;
6. on timeout/ambiguous result, hold a non-terminal safe state and reconcile before retrying a non-idempotent effect.

No local “success” flag may be used to fabricate an AdGuard or physical-device outcome.

## 9. Lifecycle, revoke and delete semantics

### 9.1 Device create/provision

- authenticate and resolve current parent;
- accept only allowlisted parent-entered device fields;
- server-generate ownership/resource identifiers;
- create/transition the local record through a truthful provisioning/reconciliation lifecycle;
- later TSK-0410 creates/links the one intended ClientID under idempotent/reconcilable semantics;
- technical protection becomes positive only through the independently accepted verification contract, never because the record or ClientID exists.

### 9.2 Device update

- owned-resource lookup is mandatory;
- update only allowlisted mutable fields;
- use row-version compare-and-swap;
- any control-plane setting change remains non-terminal until external read-back/reconciliation proves the applied result;
- unsupported combinations fail safely rather than exposing raw AdGuard controls.

### 9.3 Device revoke/unlink/delete

A destructive device operation is a state machine, not a blind datastore delete:

1. authenticate current parent and authorize the owned device;
2. enforce expected `row_version` / operation idempotency;
3. mark the smallest current revoke/delete/reconciling state required to prevent conflicting mutations;
4. have the later TSK-0410 adapter revoke/remove/reconcile the exact linked ClientID if one exists;
5. treat timeout/unknown external result as non-terminal and reconcile before declaring completion;
6. after definite safe control-plane disposition, delete the `ParentDevice` row, approved settings/current protection metadata and ClientID mapping;
7. delete subject-linked in-flight state after completion except separately approved content-free completion evidence;
8. never state that the physical phone DNS/profile was removed solely because server-side records/control state were removed.

A retry of the same logical delete after definite completion must be harmless/idempotent or return a truthful already-gone result without recreating state.

### 9.4 Account deletion

Account deletion must:

1. satisfy TSK-0356 recent-authentication/high-risk requirements;
2. transition the account to a deletion/fail-closed state that prevents new device ownership-changing operations;
3. enumerate only device records owned by that `parent_id` server-side;
4. revoke/remove/reconcile each current AdGuard mapping under the same device lifecycle contract;
5. only after required device/control-plane disposition, remove device rows/current settings/protection metadata and the parent/provider-subject mapping;
6. invoke provider-side deletion/revocation only under its accepted contract and never infer provider success from local deletion;
7. preserve no deleted child/account/device content as an audit copy;
8. apply the separately approved backup deletion/restore contract before production backup processing is enabled;
9. never claim physical DNS/profile removal on a phone merely from account deletion.

## 10. Restore and disaster-recovery semantics

Production A-domain backup use remains **blocked** by TSK-0233 until an exact backup retention/access/encryption/deletion-propagation/restore contract is approved. This task defines the ownership requirements any later restore must meet:

1. J0/J1 are never restored.
2. Restore only fields still permitted by the current A-domain schema.
3. Deleted parents/devices must not be resurrected; the future backup/deletion design must carry or reconstruct enough content-free deletion authority to exclude already-deleted state without retaining deleted payload.
4. `provider_subject -> parent_id` uniqueness must be revalidated before restored account authority becomes usable.
5. `parent_id -> device_id` ownership and non-null ClientID uniqueness must be revalidated.
6. Restored ClientID mappings require reconciliation with current AdGuard control-plane reality before mutable operations rely on them.
7. Restored cached Protection Map metadata is treated as stale/non-verified until fresh technical evidence re-evaluates it.
8. A restore cannot create login/account authority if Firebase/provider state says the subject is deleted/disabled/revoked or otherwise fails current authentication truth.
9. Conflict/ambiguity fails account/device mutations closed until reconciled.

## 11. Required negative / adversarial acceptance cases

Later implementation acceptance must include at least two synthetic independent parents, `A` and `B`, with independently owned devices `A1` and `B1`, and prove:

1. A cannot list B1.
2. A cannot read B1 by substituting B1’s `device_id`.
3. A cannot update/rename/change settings on B1.
4. A cannot revoke/unlink/delete/recover/replace B1.
5. A cannot gain access by submitting B’s `parent_id` in path/body/query/header.
6. A cannot gain access by submitting B1’s `adguard_client_id`.
7. Equivalent B -> A1 attempts fail.
8. A stale `row_version` cannot overwrite a newer mutation.
9. Duplicate parent creation for the same current provider subject does not create a second parent authority.
10. Duplicate/retried device create/provision does not create an unintended duplicate device/ClientID.
11. A non-null ClientID cannot be linked to two current device rows.
12. Account/device deleting/reconciling states reject incompatible new mutations.
13. Provider/session invalid/revoked/deleted/ambiguous state grants zero account-only authority.
14. Restored stale protection metadata cannot directly produce a current `Verified` state.
15. Not-found/unauthorized errors do not disclose another parent’s device existence beyond the minimum generic boundary.
16. No test or operational diagnostic emits browsing/query history, raw auth/session bearer values, AdGuard admin secrets or unnecessary persistent user identifiers.

## 12. Failure semantics

| Failure | Required safe state |
| --- | --- |
| Session invalid/expired/revoked | no account/device authority; accountless core remains available if healthy |
| Provider subject has no parent mapping | no implicit merge/create on protected request; explicit account creation flow only |
| Duplicate provider mapping | fail closed; reconcile uniqueness; never choose one by email |
| Device ID not owned by session parent | generic not-found/unauthorized; zero data/effect |
| Browser supplies foreign parent ID | reject/ignore as untrusted; session parent remains authoritative |
| Foreign/stale ClientID supplied | no authority/effect; control-plane access only after owned-device lookup |
| Row-version mismatch | typed conflict; reread before retry |
| Create response lost | detect/reconcile idempotency state; no duplicate record/ClientID |
| AdGuard timeout/ambiguous result | current resource enters/remains reconciling/uncertain; no terminal success claim |
| Local delete succeeds but external state unknown | this ordering is prohibited for final deletion; retain safe reconciliation authority until external disposition is known |
| Restore conflicts with provider/ownership/ClientID truth | fail mutations closed and reconcile; no resurrected authority |

## 13. Privacy and data-minimisation boundary

This task adds **no new product-purpose data category** beyond TSK-0233.

Specifically:

- no child name, DOB, account, school or stable child profile;
- no device IMEI, serial, MAC, advertising ID or location;
- no browsing/query/domain/URL/top-domain/activity history;
- no raw provider token/session-cookie value;
- no email/display name/photo by default;
- no raw/unrestricted AdGuard administration data in the parent-facing model;
- nickname is optional and parent-facing only;
- current protection metadata is freshness-bounded current truth, never a behavioral timeline;
- ClientID is server-side control linkage only;
- logs/metrics/evidence must remain privacy-safe and exclude these prohibited fields.

`RSK-0001` remains OPEN. Conditional lawful-basis terminology in predecessor data models is not final production legal authority.

## 14. Datastore implementation freedom and prohibited shortcuts

A later implementation may use a relational database, document store or another approved persistence mechanism only if it proves the same guarantees.

It may **not**:

- make authorization depend on opaque IDs alone;
- rely on client-side filtering;
- use Firebase UID/email/ClientID as a substitute for an owned-resource authorization check;
- omit transactional/equivalent uniqueness for parent/provider/device/ClientID relations;
- omit an equivalent compare-and-swap concurrency mechanism;
- blind-cascade external control-plane deletion;
- create a permanent request/event/activity ledger merely to implement idempotency;
- add child identity/browsing history/provider-profile data for convenience;
- restore deleted authority or stale positive protection evidence;
- expose arbitrary `/control/*` AdGuard operations through the browser/account interface.

## 15. Downstream contracts unlocked by this model

After durable PASS and a fresh eligibility recomputation:

- `TSK-0410` may consume this ownership boundary together with its other current dependencies to define the allowlisted server-side AdGuard adapter and ClientID lifecycle contract;
- `TSK-0234` still also depends on TSK-0410 and therefore cannot become PASS from this task alone;
- L6 datastore/adapter implementation remains prohibited until LG-07 passes and the task’s own dependencies/authority are satisfied.

## 16. ACC-0232 trace

| ACC-0232 element | Evidence | Disposition |
| --- | --- | --- |
| parent ownership enforced server-side for every device operation | Sections 6, 9, 11, 12 | SATISFIED |
| opaque internal IDs | Sections 3–5 | SATISFIED |
| ClientID never authorization | Sections 1, 3.2, 5.3, 6, 11 | SATISFIED |
| parent/child data minimised | Sections 3, 13 | SATISFIED |
| delete/revoke semantics | Section 9 | SATISFIED |
| restore semantics | Section 10 | SATISFIED |
| indexes | Section 7 | SATISFIED |
| concurrency requirements | Section 8.1 | SATISFIED |
| idempotency requirements | Sections 8.2–8.3, 9, 11 | SATISFIED |

## 17. Candidate stable disposition

**Candidate ACC-0232 = PASS**, subject to VER-0232 read-back/reviewer inspection of this exact artifact and durable runtime synchronization.

This candidate PASS means the minimum logical parent/device ownership and authorization boundary is defined at L5. It does **not** mean a datastore has been selected/provisioned, authorization code exists, cross-parent tests have run, AdGuard has been mutated, backup/legal readiness is approved, a real user/account/device exists, LG-07 has passed, or L6 build is authorized.
