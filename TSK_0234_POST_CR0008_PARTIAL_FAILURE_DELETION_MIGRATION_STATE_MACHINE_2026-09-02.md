# TSK-0234 — Post-CR-0008 Auth / Datastore / AdGuard Partial-Failure, Deletion and Migration State Machine

**Task:** TSK-0234 — Design auth, datastore and AdGuard partial-failure, deletion and migration flows  
**Acceptance / Verification / Evidence:** ACC-0234 / VER-0234 / EVD-0234  
**Lifecycle / Priority / Authority:** L5 / MEDIUM / A3 / AUTO_ALLOWED  
**Version:** 1.0.0-post-CR0008  
**Date:** 2026-09-02 UTC  
**Gate:** contributes to LG-07 Architecture, Security, Privacy and Delivery Readiness  
**Direct predecessors:** TSK-0356 current PASS; TSK-0232 current PASS; TSK-0410 current PASS

## 1. Decision

Freeze the Version-1 partial-failure and convergence model below for the optional parent-account/device path.

The core rule is:

> **No cross-system operation becomes terminal success until the minimum durable local operation state and every required observed external effect agree. An ambiguous effect is a reconciliation state, not permission to retry blindly or report success.**

This applies across Firebase Authentication/session authority, the future minimum product datastore, and the private typed AdGuard adapter.

The complete accountless core remains independent. Failure of Firebase/account datastore/account-only AdGuard administration must not create mandatory login, shared credentials, browser AdGuard access, cross-parent fallback, or browsing/query-history collection.

This is an L5 state-machine/design decision only. It does not select/provision a datastore, configure Firebase, deploy the AdGuard private control route, mutate a live AdGuard client, migrate a real account, decommission a service, process real users, resolve UK legal/data readiness, pass LG-07, or authorize L6.

## 2. Predecessor contracts consumed without weakening

### 2.1 Authentication/session — TSK-0356

- Optional Google/Firebase identity only; accountless core remains complete without login.
- Fresh verified Firebase identity creates the server session; protected account routes are revocation-aware.
- Provider/revocation uncertainty fails account-only authority closed.
- Authentication never substitutes for parent/device ownership.
- Local logout and global/security revocation are distinct.
- No silent account merge by email.

### 2.2 Ownership/datastore boundary — TSK-0232

- One parent owns zero-or-more devices; every current device has exactly one current parent.
- Every device operation enforces server-side owned-resource authorization.
- `parent_id`/`device_id` are opaque; ClientID never grants authorization.
- `row_version` or equivalent compare-and-swap prevents stale overwrite.
- Duplicate create/provision requires durable/reconstructable idempotency/reconciliation state.
- Device/account deletion must reconcile required external AdGuard disposition before final local deletion.
- Restore cannot resurrect deleted authority or stale positive protection evidence.

### 2.3 AdGuard adapter — TSK-0410

- Private typed v0.107.79 adapter only; no raw `/control/*` browser proxy.
- Consequential mutation sends at most one request before required exact observation.
- Timeout/disconnect/5xx/ambiguous acknowledgement means outcome unknown; observe before any retry.
- Terminal success requires local ownership/binding truth plus exact observed AdGuard name/ClientID/privacy/profile state.
- Managed clients explicitly preserve `ignore_querylog=true` and `ignore_statistics=true`.
- ClientID rotation/deletion does not prove physical device-profile removal or current Protection Map verification.

## 3. State domains are separate

Do not collapse distinct truth into one `status` field.

### 3.1 Parent-account lifecycle

Logical states required by this design:

- `ACTIVE` — current authenticated account operations may proceed subject to session/ownership checks.
- `DELETION_PENDING` — no new device-creating/ownership-expanding operation; required deletion effects are being reconciled.
- `PROVIDER_MIGRATION_PENDING` — future authorized identity-provider migration is incomplete; old authority remains governed as specified below and no ambiguous identity is accepted.
- `RECOVERY_REQUIRED` — account-only authority or provider mapping cannot currently be established safely; mutations fail closed.
- `DELETED` — represented by absence/tombstone semantics owned by the later deletion/backup contract; not a live account authority state.

These are logical outcomes; a later implementation may use equivalent names/representation.

### 3.2 Device/binding operation lifecycle

A current device may have:

- `NO_BINDING` — no persistent AdGuard client is expected.
- `CREATE_PENDING`
- `ACTIVE`
- `UPDATE_PENDING`
- `ROTATION_PENDING`
- `DELETE_PENDING`
- `RECONCILING`
- terminal binding absence after proven delete.

A pending/reconciling binding is **not** technical Protection Map `Verified`. Protection evidence remains a separate TSK-0041/TSK-0313/TSK-0411 truth domain.

### 3.3 Cross-system operation record

Before any consequential AdGuard/provider mutation, durable operation state must identify only the minimum needed to converge safely:

- opaque operation ID;
- operation type;
- owning `parent_id` and, where applicable, owned `device_id`;
- expected local `row_version`;
- expected old/new opaque binding identifiers where required;
- phase/state;
- target contract/version;
- coarse last-result/error class and bounded timestamps needed for timeout/reconciliation;
- no DNS queries/domains/browsing history, provider tokens, session-cookie values, AdGuard admin credential or child profile.

If this minimum state cannot be durably written, **do not start the external consequential mutation**.

## 4. Universal convergence algorithm

For every cross-system create/update/rotate/delete/migration operation:

1. authenticate current authority where the operation requires a live parent session, or prove a previously authorized durable deletion/reconciliation operation;
2. perform server-side ownership authorization for the exact resource;
3. read current local row/version and operation state;
4. read external state when needed to classify the starting condition;
5. write/confirm the bounded pending operation **before** the consequential external effect;
6. perform at most one consequential external request while the outcome is unresolved;
7. observe/read back external state;
8. classify it as `DESIRED`, `ORIGINAL/ABSENT`, `CONFLICTING/MIXED`, or `UNAVAILABLE/UNKNOWN`;
9. commit local terminal state only when external observation and expected local compare-and-swap both agree;
10. if local terminal commit fails after external success, preserve/recover the pending operation and re-observe before finalization; do not repeat the external mutation merely because the local response was lost;
11. if outcome remains conflicting/unknown, stay non-terminal and route to reconciliation/repair;
12. report only the actual stable state to the user.

Rollback follows the same algorithm against an explicitly defined safe target. **Never send a blind inverse request as “rollback.”**

## 5. Failure matrix

| Failure / ambiguity | Accountless core | Account/dashboard authority | AdGuard/account mutation | Required stable response |
| --- | --- | --- | --- | --- |
| Google/Firebase sign-in unavailable | remains available if its own dependencies are healthy | no new sign-in/session | none requiring new account authority | truthful account-sign-in unavailable; no DNS-state change inferred |
| Session/revocation verification unavailable or ambiguous | remains available | fail protected account actions closed under current baseline | no new mutation | preserve existing DNS service truth separately; do not accept cached/request identity as substitute |
| Session invalid/revoked/disabled/deleted | remains available | deny/clear affected account session | no parent-requested mutation | reauthentication/support/global lifecycle as applicable |
| Datastore unavailable before operation state is written | remains available where datastore-independent | device/account ownership cannot be proven | **do not mutate AdGuard/provider** | account-only operation unavailable; retry after datastore recovery and fresh authz |
| Datastore becomes unavailable after external mutation | remains available | do not claim terminal local state | do not repeat mutation blindly | recover pending operation, observe external state, then CAS-finalize when datastore returns |
| AdGuard admin/control route unavailable | DNS baseline may remain healthy if data plane is healthy | local account reads only where current datastore truth is sufficient; no fresh technical verification inferred | no mutation | pending/failed-safe; accountless DNS remains independently truthful |
| AdGuard DNS data plane unavailable | accountless DNS protection is degraded/unavailable | dashboard may still load local ownership, but stale positive technical state must not be presented as current | admin mutation only if separately safe/needed; no false “protection active” claim | verifier/operations truth downgrades affected protection state |
| Consequential AdGuard timeout/disconnect/5xx | remains as actually healthy/unhealthy | pending/reconciling | observe exact AdGuard state before retry | desired -> finalize; original -> bounded fresh attempt may be allowed; mixed -> reconcile |
| Duplicate create request/response loss | unchanged | one logical device only | no second unintended client | unique/idempotent operation resolves to original/current state |
| Stale/missing ClientID binding | unchanged | record is not authoritative proof of active binding | no arbitrary new client generation | classify stale/absent, reconcile or explicit reprovision; withdraw stale positive evidence |
| Local row-version conflict | unchanged | no stale overwrite | no new effect until reread | typed conflict; reread authoritative state and recompute |
| Partial account deletion | unchanged | account is `DELETION_PENDING`; no new ownership-expanding ops | reconcile all required client/provider effects | do not show deleted until required terminal conditions are proven |
| Provider migration ambiguous | unchanged | old/new identity relationship not guessed | no device ownership transfer based on email | remain migration/recovery pending; human/support recovery if identity proof cannot be established |
| Service decommission partial | only services actually shut down are unavailable | no false completion | drain/reconcile each owned effect under plan | preserve removal instructions and residual-state evidence until complete |

## 6. Provider outage and identity failure

### 6.1 No authority fallback

When Firebase/Google identity or required revocation verification cannot establish authority:

- do not trust email, display name, browser parent ID, device ID, ClientID, a prior dashboard URL, IP address or local browser state as substitute identity;
- do not expose an emergency shared password or AdGuard credential;
- do not mutate account/device ownership;
- accountless setup/help/removal remains available if independently healthy;
- physical DNS behavior remains a separate technical fact and is not changed merely because the account provider is down.

### 6.2 Existing pending operations

A previously authenticated operation whose durable record proves its parent/device provenance may be reconciled by server-side recovery logic without requiring the browser to replay the original request. Reconciliation may only converge the already-authorized operation to its known safe target; it cannot expand scope, select another device, or create new ownership.

## 7. Datastore outage and transaction boundary

The future datastore is the ownership/idempotency authority for optional-account mutations. Therefore:

1. **No durable operation record -> no consequential external mutation.**
2. If the datastore is unavailable before authorization/operation persistence, account/device mutation fails closed.
3. If an external mutation happened after a pending record was durably stored but terminal local commit failed, the next recovery run reads the same operation, observes external state and converges; it does not create a new operation/ClientID just because the response failed.
4. A stale `row_version` prevents terminal overwrite even if the external target reached desired state; this becomes reconciliation requiring a fresh authoritative local decision.
5. Read-only dashboard data may be served only if the application can still prove current session and stored ownership safely; implementation may instead fail account surfaces closed. There is no requirement to create a weak unauthenticated cache merely for availability.
6. Accountless core dependencies must not be routed through this datastore merely to make the optional dashboard work.

## 8. AdGuard outage, timeout and stale ClientID

### 8.1 Administrative-control outage

If the private AdGuard administrative route is unavailable but the DNS data plane is healthy:

- existing DNS resolution may continue;
- no create/update/rotate/delete can be declared complete;
- dashboard ownership data may remain visible, but ClientID/binding presence does not become technical verification;
- actions requiring current AdGuard observation return pending/unavailable rather than fabricating success.

### 8.2 Data-plane outage

If the actual DNS service is unavailable/degraded, current technical protection truth must downgrade according to the owning verification/Protection Map contract. An available dashboard or stored `ACTIVE` binding cannot override target observation.

### 8.3 Stale binding classifications

When local state says a binding exists but exact AdGuard observation is:

- **absent** -> `RECONCILING`/stale; do not claim active; explicit repair/reprovision decision may generate a new binding only after current authorization and operation setup;
- **desired exact match** -> candidate for local reconciliation, but technical device-path verification still separate;
- **drifted privacy/profile** -> fail active-health acceptance and repair through the governed update path;
- **conflicting/multiple/unexpected identity** -> fail closed, no automatic delete/adoption; operator/reconciliation review required;
- **unknown/unavailable** -> preserve pending/uncertain state; no blind mutation retry.

## 9. Duplicate creation

### 9.1 Parent account

A verified current provider subject maps to at most one current parent. Duplicate account-create requests must return/reconcile the same authorized account or a typed conflict; they may not create another parent because the first response was lost.

### 9.2 Device / ClientID

For one logical Add Device action:

- one server-generated device ID;
- one stable operation identity;
- one generated ClientID/name pair while unresolved;
- exact collision/starting-state check before add;
- one add request before observation;
- exact post-add observation before active state;
- duplicate request with same idempotency context returns/reconciles original/current state;
- another independent Add Device action is a new resource only after the product intentionally accepts it as such.

No duplicate prevention relies on nickname, email, child identity or ClientID secrecy.

## 10. Partial update / ClientID rotation

For settings repair/update/rotation:

1. reauthenticate/authorize as required and capture current local `row_version`;
2. observe exact current AdGuard binding;
3. write `UPDATE_PENDING` or `ROTATION_PENDING` operation;
4. perform one canonical adapter update;
5. after ambiguous result, search old/new IDs as applicable;
6. `DESIRED` -> CAS-finalize local state;
7. proven `ORIGINAL` -> one later fresh authorized attempt may be possible;
8. mixed/conflicting -> `RECONCILING`, no normal progression;
9. stale local version -> do not overwrite; reconcile current local owner intent against external state;
10. rotation never claims old physical profile removal and never creates `Verified` protection by itself.

## 11. Partial device unlink/revoke/delete

Device unlink/dashboard deletion and physical DNS removal remain distinct.

For persistent binding deletion:

1. current owner authorization or a previously authorized deletion operation is required;
2. local device enters `DELETE_PENDING` before the external delete;
3. exact search proves expected binding or already-absent state;
4. one delete request may be sent for the unresolved operation;
5. exact absence closes the AdGuard-side effect;
6. only then may local binding/device state be removed according to the current product-data contract;
7. if external state is unknown/present/conflicting, keep sufficient minimal reconciliation authority and do not terminally delete the local provenance needed to finish safely;
8. user copy separately explains whether the physical phone DNS/profile still needs removal.

If policy eventually permits “unlink dashboard record but keep the DNS configuration,” that is an explicit different lifecycle action and must not be silently substituted for revoke/delete.

## 12. Partial account deletion

Account deletion is a coordinated state machine:

1. require current recent authentication under TSK-0356;
2. atomically transition parent to `DELETION_PENDING` and block new ownership-expanding operations;
3. enumerate device records **server-side by current parent ownership**;
4. for each managed device, reconcile persistent AdGuard binding deletion through TSK-0410;
5. keep unresolved device operations pending rather than deleting the ownership evidence needed for safe reconciliation;
6. after required device/control effects are proven, remove device current-state/settings/binding records under the approved deletion contract;
7. globally revoke Firebase refresh-token authority where required by the accepted account-deletion contract;
8. request provider-user deletion only under the current approved provider API/lifecycle and do not infer success from a local record change;
9. delete the local provider-subject/parent record only when the required local/external sequence is at its defined safe terminal boundary;
10. apply the separately approved backup-deletion/restore policy before production backup processing exists;
11. no deleted content is preserved merely as an audit copy; only separately approved content-free completion/provenance evidence may remain;
12. never claim that the physical phone DNS/profile was removed unless the separate device-removal evidence supports that statement.

An interrupted deletion resumes from durable operation/device states. It does not start a second deletion tree.

## 13. Account-provider migration

No provider migration is currently required or authorized for real users. This section freezes the **safe architecture if a future owner-approved migration trigger occurs**.

### 13.1 Migration invariants

- preserve internal `parent_id` and owned-device relationships when the same parent is cryptographically/authentically proven under the approved migration method;
- never match or merge by email/display name alone;
- ClientID/device possession cannot prove identity;
- no anonymous J0/J1 state is imported as part of identity migration;
- no child/browsing/query history is created for migration;
- cross-parent uniqueness/IDOR rules remain in force throughout;
- migration cannot be used to transfer ownership between people without a separately approved transfer capability.

### 13.2 Safe future flow

1. migration feature/provider/schema must first receive its own current security/privacy/vendor/UX authority;
2. authenticate the existing parent through the then-valid recovery/migration proof and authenticate the new provider identity;
3. check that the new provider subject is not already bound to another parent;
4. write `PROVIDER_MIGRATION_PENDING` with only the minimum old/new opaque provider-mapping data and expected row version;
5. preserve the old mapping/authority until the new identity binding is proven and the defined cutover can be completed safely; exact dual-binding representation is a downstream schema decision and reopens TSK-0232/0233 if needed;
6. atomically/equivalently cut over the provider mapping without changing `parent_id` or device ownership;
7. revoke/remove old provider authority as required by the approved migration plan;
8. verify new sign-in/session -> same internal parent -> same owned device set, and prove cross-parent negatives;
9. if proof/cutover is ambiguous, remain migration/recovery pending and require the approved recovery route rather than guessing by email.

If the old provider becomes unavailable before identity can be safely proven, that is a **recovery/human identity-proof problem**, not authorization to relax ownership rules.

## 14. Service decommission

A future service decommission is consequential and requires separate owner authority. The safe technical sequence is nevertheless defined so later execution cannot invent a destructive order.

### 14.1 Optional account/dashboard decommission while DNS service remains

1. stop new account/device enrollment and new persistent-client creation;
2. communicate a truthful bounded decommission/removal path under the then-current launch/legal/support authority;
3. reconcile active/pending device bindings according to the approved keep-DNS-versus-revoke policy; do not assume physical profile removal;
4. revoke account sessions/provider authority as applicable;
5. complete parent/device data deletion and approved backup deletion propagation;
6. remove the private account-management adapter/credentials only after no required reconciliation remains;
7. accountless DNS may remain only if separately intended/operable/authorized.

### 14.2 Whole DNS-service decommission

Whole DNS shutdown is outside current Action Authority and requires explicit owner/operational/public-impact authorization. Before shutdown, the plan must account for configured devices that may fail closed or lose DNS when the endpoint disappears, provide current platform-specific removal/reconfiguration instructions, and preserve no false claim that remote server deletion removed profiles from devices.

No decommission path is allowed to retain browsing/query history as “closure evidence.”

## 15. Rollback and reconciliation rules

- Roll back to a **defined observed state**, not a guessed previous response.
- Reconciliation reads local operation/ownership state and external AdGuard/provider state before choosing a corrective effect.
- A retry is allowed only after the previous outcome is classified and the next effect is idempotent/reconcilable under current authority.
- Never generate new identities repeatedly while an old operation is unresolved.
- Never delete the local ownership/operation evidence required to identify and safely remove an orphaned external object.
- A recovered/restored datastore rechecks provider authority, parent/device uniqueness, ClientID uniqueness and live AdGuard state before account mutations resume.
- Restored Protection Map data is stale until current technical verification re-establishes it.
- A current contradiction reopens a prior positive local assumption; historical “success” does not outrank current target observation.

## 16. Security / privacy invariants under every failure

No failure mode may:

1. grant Parent A access to Parent B’s device/client;
2. authorize by ClientID, email, nickname, device ID possession or browser-supplied parent ID;
3. expose AdGuard Basic-Auth/admin controls to the browser;
4. fall back to a shared password or public `/control` route;
5. enable query logging or identifiable per-client statistics for diagnosis;
6. preserve DNS query/domain/browsing history in operation/reconciliation records;
7. convert dashboard/account/binding existence into technical Protection Map `Verified`;
8. silently re-enable a deleted/revoked parent/device binding after restore/provider return;
9. silently link anonymous J0/J1 state into an account;
10. weaken current global AdGuard privacy/upstream/filtering controls merely to recover account functionality.

Exceptional diagnostic DNS logging remains separately governed, time-boxed and outside ordinary partial-failure handling.

## 17. Downstream deterministic acceptance catalogue

A conforming implementation must prove at least:

1. accountless core remains usable during Firebase/account-only outage where its own dependencies are healthy;
2. provider/revocation uncertainty grants zero account-only authority;
3. datastore unavailable before operation persistence causes zero external mutation;
4. external success + lost local final commit converges without duplicate external mutation;
5. AdGuard admin outage does not create browser admin fallback;
6. DNS data-plane outage overrides stale local positive protection state;
7. duplicate parent create does not produce a second parent;
8. duplicate device/client create does not produce a second unintended binding;
9. stale ClientID/absent external binding does not remain falsely Active/Verified;
10. update timeout observes before retry;
11. rotation ambiguity checks old/new IDs and does not generate endless replacements;
12. delete ambiguity preserves reconciliation authority and never terminally lies;
13. account deletion interrupted at each step resumes safely without cross-parent effect;
14. stale row-version cannot overwrite newer local state;
15. Parent A cannot exploit any recovery/retry/delete/migration route against Parent B;
16. provider migration never merges by email and preserves internal ownership only after required identity proof;
17. restore does not resurrect deleted account/device/binding or stale `Verified` state;
18. service-decommission flows distinguish server-side client deletion from physical-device profile removal;
19. no failure/retry/reconciliation path emits DNS query/domain/browsing history or raw provider/session/admin secrets;
20. terminal success is withheld whenever required local/external truth remains unknown or contradictory.

## 18. ACC-0234 trace

| ACC-0234 requirement | Evidence | Disposition |
| --- | --- | --- |
| provider outage | Sections 5–6 | SATISFIED |
| datastore outage | Sections 5, 7 | SATISFIED |
| AdGuard outage / timeout | Sections 5, 8 | SATISFIED |
| duplicate creation | Section 9 | SATISFIED |
| stale ClientID | Section 8.3 | SATISFIED |
| partial update | Section 10 | SATISFIED |
| partial delete | Sections 11–12 | SATISFIED |
| rollback / reconciliation | Sections 4, 15 | SATISFIED |
| account-provider migration | Section 13 | SATISFIED |
| service decommission | Section 14 | SATISFIED |
| no silent cross-parent access | Sections 6, 12–13, 16–17 | SATISFIED |
| no browsing logs | Sections 3.3, 16–17 | SATISFIED |

## 19. Candidate stable disposition

**Candidate ACC-0234 = PASS**, subject to VER-0234 read-back/reviewer inspection of this exact artifact and durable runtime synchronization.

This candidate PASS means the L5 partial-failure/deletion/migration state machine is defined and reconciled with current auth, ownership and AdGuard contracts. It does **not** mean a datastore/provider/private control route is implemented, failure tests have run, a real account/device has been processed, provider migration/decommission is authorized, legal/backup readiness is complete, LG-07 has passed, L6 is authorized, or public activation is permitted.
