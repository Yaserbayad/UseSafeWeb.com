# TSK-0352 — Post-CR-0008 AdGuard Persistent ClientID API, Privacy and Lifecycle Contract

**Task:** TSK-0352 — Specify AdGuard API, persistent ClientID, privacy and lifecycle contract  
**Acceptance / Verification / Evidence:** ACC-0352 / VER-0352 / EVD-0352  
**Lifecycle / Priority / Authority:** L4 / MEDIUM / AUTO_ALLOWED  
**Version:** 1.0.0-post-CR0008  
**Date:** 2026-09-02 UTC  
**Candidate disposition:** CURRENT PASS pending independent VER-0352, durable EVD-0352 publication, guarded runtime reconciliation and exact read-back.

## 1. Current authority and task boundary

TSK-0352 depends exactly on current PASS predecessors:

- TSK-0041 — current DNS-protection activation/verification/removal requirements;
- TSK-0142 — current lightweight parent dashboard/device-management requirements.

Compatible current constraints also include TSK-0044 (private AdGuard admin/credential/failure NFR) and TSK-0353 (server-side authentication/authorization/session/IDOR NFR). They constrain this contract but are not TSK-0352 hard dependencies.

Current Version-1 product remains accountless-first with optional parent account/device management. Anonymous setup must not create a persistent AdGuard client. Persistent ClientID capability exists only for an authenticated parent-owned device lifecycle and never substitutes for technical Protection Map verification.

This task defines an API/lifecycle contract only. It does not call a live AdGuard server, create/update/delete a persistent client, expose credentials, activate an account provider, implement a datastore, change the frozen AdGuard version, or infer successor/gate/launch PASS.

## 2. Version-pinned official AdGuard source baseline

Frozen backend: **AdGuard Home v0.107.79**.

Version-pinned official sources used on 2026-09-02:

1. `https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/v0.107.79/openapi/openapi.yaml`
   - OpenAPI title AdGuard Home, API version `0.107`;
   - server base `/control`;
   - global `basicAuth` security;
   - client operations include `/clients/add`, `/clients/update`, `/clients/delete`, `/clients/search`;
   - `Client` has `ids`, `ignore_querylog`, `ignore_statistics` and other client settings;
   - `/clients/search` performs exact matching and accepts `clients[]` entries with `id` equal to IP/CIDR/MAC/ClientID;
   - update uses a current client `name` plus replacement `data: Client`;
   - delete identifies the client by `name`.
2. `https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/v0.107.79/client/src/__locales/en.json`
   - v0.107.79 UI validation states ClientID contains only numbers, lowercase letters and hyphens.
3. Official AdGuard Home Clients documentation (`https://github.com/AdguardTeam/AdGuardHome/wiki/Clients`)
   - persistent ClientIDs are supported for encrypted DNS;
   - for the v0.107-style DoH route a ClientID is appended as `https://example.org/dns-query/<ClientID>`.

The accepted UseSafeWeb/SafeWeb resolver authority supplies base host `dns.usesafeweb.com`. Therefore the current persistent-client DoH endpoint template is:

`https://dns.usesafeweb.com/dns-query/{client_id}`

The endpoint is configuration/routing material, not an account authorization credential and not evidence that protection is active.

## 3. Private server-side API allowlist

The application must never expose generic AdGuard `/control` proxying. The optional-account adapter is restricted to the smallest lifecycle allowlist:

| Logical operation | AdGuard v0.107.79 API | Purpose |
|---|---|---|
| Search exact client identifier | `POST /control/clients/search` | Read/reconcile by stored/generated ClientID before and after mutation |
| Add client | `POST /control/clients/add` | Create one authenticated parent-owned persistent client after all preconditions pass |
| Update client | `POST /control/clients/update` | Reconcile privacy settings or perform governed ClientID rotation using server-known current name |
| Delete client | `POST /control/clients/delete` | Remove the server-owned persistent client by its server-stored AdGuard name after exact ownership/reconciliation proof |

No customer/browser route may select an arbitrary AdGuard endpoint, HTTP method, URL path, body field or admin operation.

The adapter may also use separately accepted read-only health/version/config checks required by TSK-0044 to prove the frozen version and global privacy baseline, but those are infrastructure safeguards rather than customer-callable functions.

## 4. Persistent client data model

For an optional-account managed device, the minimum product-side binding is:

- `parent_id` — opaque internal authenticated parent identifier;
- `device_id` — opaque internal parent-owned device record identifier;
- `adguard_client_name` — opaque server-managed AdGuard client name used for update/delete reconciliation;
- `client_id` — opaque high-entropy AdGuard ClientID used in the direct DoH path;
- `lifecycle_state` — bounded state such as `creating`, `active`, `rotating`, `revoking`, `pending_reconciliation`, `deleted`;
- contract/version marker needed to reconcile version/schema changes;
- minimum opaque operation/reconciliation identifiers required by TSK-0230/0353/0044.

The binding stores no DNS qname/domain/URL/browsing history, child profile, provider token, session cookie, AdGuard admin credential, raw query log or statistics.

`client_id` and `adguard_client_name` must not be derived from email, provider subject, parent ID, child identity, device nickname, IP address, hostname or browsing content.

## 5. ClientID generation contract

A new persistent ClientID is generated **server-side** using a cryptographically secure random source.

Version-1 format:

- exactly **26 lowercase RFC-4648 base32 characters without padding** using alphabet `a-z` and `2-7`;
- approximately 130 bits of random space;
- no email/name/device/parent prefix;
- no uppercase, underscore, slash, dot or other characters outside the v0.107.79 validated numbers/lowercase/hyphen class;
- collision check through exact `/clients/search` before mutation;
- a collision causes regeneration, never reuse.

High entropy reduces collision/guessing risk but does **not** make ClientID an authorization secret. Possession of the DoH URL cannot authorize dashboard/device operations.

`adguard_client_name` is a separate opaque server-managed value, for example `sw-` plus a random lowercase base32 suffix. It is never accepted from a customer request as authorization.

## 6. Canonical AdGuard client configuration

The persistent client exists only to support the accepted parent-owned device route. The adapter constructs the exact v0.107.79 `Client` payload from server-owned state and schema validation.

Mandatory contract fields/invariants:

- exactly one accepted generated ClientID in `ids` for this lifecycle binding;
- `ignore_querylog = true` **explicitly**;
- `ignore_statistics = true` **explicitly**;
- global filtering/protection policy is inherited; no customer-specific unrestricted filtering/upstream/DNS administration is introduced;
- no per-client upstream, custom rule, content-history, child-profile or analytics identity is created by this contract;
- fields omitted only when the exact version-pinned schema/server contract proves the omission safe; privacy flags are never left to their false defaults;
- TSK-0044 global no-query-log/no-statistics/privacy configuration remains independently required even when the per-client flags are true.

Any read-back where either privacy flag is false/missing/ambiguous is not an accepted active device state.

## 7. Create lifecycle

`createManagedDnsClient(parent, device)` is accepted only after:

1. verified server session and current parent authority under TSK-0353;
2. server-side confirmation that the device belongs to that parent;
3. device lifecycle permits creation and no active/pending binding already exists;
4. current frozen AdGuard version/contract and global privacy baseline are proven;
5. generate opaque `adguard_client_name` and 26-character ClientID;
6. exact `/clients/search` proves the ClientID is absent;
7. persist a durable/reconstructable **creating** operation/binding state before the consequential external mutation;
8. call only `POST /control/clients/add` with the canonical client configuration;
9. exact `/clients/search` by ClientID must return one expected persistent client whose name/ID/privacy flags match the candidate;
10. persist the product binding as `active` only after that read-back;
11. only then expose the direct DoH endpoint to the authenticated owner/configuration flow.

If the add response is lost/ambiguous, do not replay `clients/add`. Search exact ClientID/name first and reconcile actual state.

If AdGuard creation succeeds but local commit fails, retain/reconstruct an operation state and reconcile; never silently create a second ClientID/client. If ownership cannot be proven, do not expose the endpoint.

## 8. Read/search lifecycle

All server-side reads are scoped through the authenticated parent/device record before AdGuard search.

The adapter may search AdGuard using only server-stored/generated identifiers. Customer-supplied arbitrary ClientID/name is never trusted as an ownership selector.

Exact `/clients/search` result classification:

- **one exact expected match** — candidate for further verification;
- **zero matches** — absent;
- **multiple/conflicting/unexpected matches** — conflict/uncertain, fail closed and require reconciliation;
- result exists but privacy flags/name/IDs differ from expected — drift, not success.

Dashboard device presence is an ownership/configuration fact only. It does not prove the device currently uses the endpoint or that DNS filtering is technically verified.

## 9. Update / repair lifecycle

Customer-facing device nickname/settings changes do not automatically mutate AdGuard client configuration.

An AdGuard update is allowed only for a contract-owned reason such as:

- repairing `ignore_querylog=true` / `ignore_statistics=true` drift;
- version/schema-required canonical-field reconciliation;
- governed ClientID rotation/replacement.

Before update:

1. authenticate and re-authorize current parent/device ownership;
2. read local binding and exact AdGuard search result;
3. verify the stored AdGuard name maps to exactly the expected ClientID/device binding;
4. derive the complete replacement `Client` object from current canonical state, not browser input;
5. persist a bounded pending operation state;
6. call `POST /control/clients/update` with current server-known `name` and canonical replacement `data`;
7. read back exact ClientID/name/privacy state;
8. commit terminal local state only after exact read-back.

An ambiguous update is reconciled before retry. No partial body patch or blind replay is assumed safe.

## 10. ClientID rotation / replacement

Rotation is used for explicit device replacement/reconfiguration, suspected endpoint disclosure, or another accepted lifecycle trigger.

1. verify parent/device authorization and current binding;
2. generate/search-confirm a new 26-character random ClientID;
3. mark binding `rotating` with old/new opaque IDs;
4. update the existing server-owned AdGuard client to the new ClientID while preserving explicit privacy flags;
5. verify the new ID resolves to the expected client and the old ID no longer identifies that persistent client;
6. update the product binding only after read-back;
7. issue the new DoH endpoint/configuration to the authenticated parent;
8. treat the old physical device/profile configuration as **not automatically removed**.

Rotation/revocation of ClientID removes the product’s persistent ownership association. It does not claim that the public resolver is inaccessible, that an old DNS profile disappeared from a device, or that technical protection is off/on.

## 11. Unlink / revoke / delete lifecycle

Account/device deletion and physical DNS configuration removal are distinct.

To delete the persistent AdGuard binding:

1. verify current authenticated parent/device ownership, or execute from an already-authorized deletion/reconciliation operation;
2. move local binding to `revoking` / `pending_reconciliation` before mutation;
3. search by server-stored ClientID and verify the expected AdGuard name/ownership binding;
4. if the exact client is already absent, treat the AdGuard-side delete as idempotently absent but still reconcile local lifecycle truth;
5. otherwise call `POST /control/clients/delete` using only the **server-read** expected AdGuard name;
6. exact search must prove the persistent ClientID/client is absent;
7. only then mark the AdGuard binding deleted/revoked locally;
8. separately represent whether the physical device DNS/profile configuration is still installed and provide removal/recovery guidance.

A customer-supplied name/ClientID must never directly drive `clients/delete`.

## 12. Account deletion integration

TSK-0353 account deletion may invoke this contract only through server-side enumeration of the authenticated parent’s owned devices.

For every device:

- use its stored binding;
- execute/reconcile the delete lifecycle above;
- preserve exact per-device result (`complete`, `pending_reconciliation`, `failed_safe` or equivalent);
- do not delete another parent’s client even if an identifier is supplied in the request;
- do not claim physical DNS/profile removal from server-side client deletion;
- do not resurrect deleted/revoked bindings through retry, restore or provider return.

Account deletion remains non-terminal if a required persistent-client deletion is unresolved, unless a separately accepted policy explicitly defines a safe terminal tombstone/reconciliation state.

## 13. Direct DoH endpoint contract

For an active persistent ClientID, the current version-pinned route is:

`https://dns.usesafeweb.com/dns-query/{client_id}`

Rules:

- HTTPS only;
- base host remains the accepted resolver host;
- ClientID is path-segment routing data, never placed in generic analytics/logging/support text;
- endpoint is delivered only to the authenticated owning configuration flow;
- endpoint must not contain parent ID, email, nickname or other personal identifier;
- URL construction is percent-encoding-safe by limiting ClientID to the accepted lowercase base32 alphabet;
- a successful DNS response through this endpoint does not itself prove the entire Protection Map; current technical verification rules still apply;
- accountless path remains `https://dns.usesafeweb.com/dns-query` without a persistent ClientID.

This task does not authorize a wildcard DoT/DoQ per-client hostname. Any such route requires separate exact certificate/platform/source acceptance.

## 14. Authorization / IDOR boundary

Every client lifecycle operation runs after TSK-0353 server-side ownership authorization.

Mandatory negatives:

- Parent A cannot search/read/manage Parent B’s stored binding through product APIs by substituting device ID, ClientID, AdGuard name or any internal reference;
- Parent A cannot update/rotate/delete Parent B’s AdGuard persistent client;
- arbitrary ClientID possession cannot become ownership;
- the adapter never offers a generic search-by-arbitrary-client endpoint to customers;
- authorization is rechecked before each consequential AdGuard mutation, including retry/reconciliation paths.

The AdGuard Basic-Auth credential remains restricted to the private adapter/operator boundary under TSK-0044.

## 15. Idempotency, retry and reconciliation

No upstream idempotency key is assumed.

For each create/update/delete/rotate operation:

- persistent operation state provides a stable local operation identity;
- pre-read exact local + AdGuard state;
- perform at most one consequential mutation per unresolved state;
- after timeout/disconnect/5xx/ambiguous acknowledgement, **search/read actual AdGuard state before retry**;
- classify desired state / original state / conflicting-or-mixed state;
- only desired exact state is terminal success;
- original state may allow one fresh, separately authorized retry when safe;
- mixed/conflicting state blocks ordinary progression and requires repair/reconciliation;
- HTTP 200 alone is not terminal evidence;
- 400/401/403/schema/authorization failures are not blindly retried;
- local datastore and AdGuard terminal truth must agree before customer-facing success.

## 16. Rollback and recovery

Rollback is state-based, not “send the inverse request blindly.”

### Create failure

If a new AdGuard client exists but local ownership commit did not finish, reconcile the pending operation. Delete an orphan only when the operation record proves it was created by this operation and no authoritative active binding adopted it.

### Update/rotation failure

Search both old/new IDs as applicable. Restore or complete the canonical desired mapping only after exact observed state. Never generate repeated replacement IDs during an unresolved mutation.

### Delete failure

If delete is ambiguous, search. Absence can close AdGuard-side deletion; presence requires a fresh authorized delete attempt or failed-safe state. Local product deletion cannot report terminal completion while required AdGuard deletion remains unresolved.

### Recovery/backup

Recovery may reconstruct minimum binding/reconciliation state but must not resurrect a deleted ClientID, stale session authority or another parent’s ownership. Any restored active binding is rechecked against live AdGuard state and privacy flags.

## 17. Version compatibility and drift gate

Before implementation/reliance and after any AdGuard upgrade/change:

1. prove installed/target version is exactly the accepted frozen version or separately accepted replacement;
2. re-read the exact official OpenAPI/source for client add/search/update/delete schemas;
3. verify `/control` private Basic-Auth boundary;
4. verify ClientID syntax/routing behavior;
5. verify `ignore_querylog` / `ignore_statistics` fields and semantics;
6. verify exact search/update/delete request shapes;
7. rerun CRUD/rotation/idempotency/authorization/privacy/rollback tests;
8. fail closed on unexplained endpoint/schema/default/ClientID behavior drift.

No future AdGuard endpoint or v0.108+ behavior is automatically imported into this v0.107.79 contract.

## 18. Deterministic implementation acceptance catalogue

A downstream implementation must be able to prove at least:

1. browser/customer cannot call arbitrary `/control`;
2. browser/customer never receives AdGuard admin credentials;
3. accountless setup creates no persistent AdGuard client;
4. new ClientID is server-generated from a cryptographically secure source;
5. ClientID is exactly 26 lowercase base32 characters and identity-independent;
6. collision search occurs before add;
7. add sets `ignore_querylog=true` explicitly;
8. add sets `ignore_statistics=true` explicitly;
9. one exact read-back match is required before active state;
10. absent/conflicting/multiple search results are classified truthfully;
11. customer-supplied arbitrary ClientID/name cannot select an AdGuard object for mutation;
12. Parent A cannot read/manage Parent B binding;
13. Parent A cannot update/rotate/delete Parent B client;
14. ClientID possession is not authorization;
15. ClientID/device ownership is not Protection Map verification;
16. direct DoH endpoint is exactly `https://dns.usesafeweb.com/dns-query/{client_id}`;
17. endpoint exposes no parent/email/nickname identifier;
18. update uses server-known current name and canonical complete data;
19. update read-back re-proves privacy flags;
20. rotation proves new mapping and old persistent mapping disappearance;
21. rotation does not falsely claim physical profile removal;
22. delete uses server-read expected AdGuard name;
23. delete read-back proves absence;
24. already-absent delete is reconciled idempotently;
25. ambiguous mutation is searched/read before retry;
26. HTTP acknowledgement alone is not success;
27. datastore + AdGuard state agree before terminal success;
28. account deletion cannot delete a cross-parent client;
29. recovery does not resurrect deleted/revoked binding;
30. version/schema/ClientID/privacy-field drift blocks the affected integration.

## 19. Non-inference and ownership boundaries

This contract does not:

- implement or deploy the adapter;
- create/update/delete any live AdGuard client;
- authorize arbitrary DNS administration;
- change accountless setup;
- make login mandatory;
- approve a datastore schema beyond the minimum binding needed to define this lifecycle;
- establish legal/privacy compliance or real-user processing authority;
- prove provider/platform/device behavior beyond its exact cited source boundary;
- pass TSK-0352 successors or any lifecycle gate.

**ACC-0352 current result candidate: PASS pending independent VER-0352, durable EVD-0352, guarded runtime reconciliation and exact GitHub read-back.**
