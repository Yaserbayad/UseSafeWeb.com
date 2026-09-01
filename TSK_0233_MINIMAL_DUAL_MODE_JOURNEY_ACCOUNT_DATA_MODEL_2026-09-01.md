# TSK-0233 — Minimal Dual-Mode Journey/Account Data Model, Storage, Retention and Deletion Flows

**Version:** 1.0.0  
**Date:** 2026-09-01  
**Lifecycle:** L5 — Architecture, Technical Design & Delivery Readiness  
**Task:** TSK-0233 — Design minimal dual-mode journey/account data model, storage, retention, and deletion flows  
**Acceptance:** ACC-0233 / VER-0233 / EVD-0233  
**Authority:** current CR-0008 modular plan; DEC-0053/CR-0006; DEC-0054/CR-0007; DEC-0055/CR-0008  
**Dependencies:** TSK-0235 current PASS; TSK-0230 current PASS  
**Status represented:** current L5 architecture candidate. This artifact does not claim implementation, final UK legal/data readiness, production processing authority, deployment, participant activation, LG-07 PASS, or launch.

## 1. Decision and acceptance boundary

UseSafeWeb Version 1 uses four strictly separated data domains:

1. **J0 — accountless browser/session state:** preferred, transient state for the active setup journey.
2. **J1 — optional anonymous transient server state:** only if implementation proves it necessary; maximum 24-hour non-sliding lifetime and no durable backup.
3. **AUTH — optional parent authentication/server-session state:** only when a parent chooses optional account/dashboard value; provider/session details remain subject to TSK-0356.
4. **A — minimal persistent parent/device ownership domain:** only the minimum parent identity reference, ownership/settings/lifecycle state, current protection metadata and server-side AdGuard linkage required for the approved lightweight dashboard/device-management capability.

The ordinary DNS data plane remains separate. No DNS question, requested/visited domain, URL, browsing history, top-domain history or child-activity history enters J0, J1, AUTH or A.

**Core value never requires identity.** The full accountless setup/protection path remains usable without creating or signing into an account wherever its own technical dependencies are healthy.

**No J1-to-account migration exists in this contract.** Sign-in/account creation creates or uses the separate AUTH/A domains. It does not convert, attach, copy, stitch or extend J0/J1 state. If a future requirement proves that explicit transfer is necessary, that transfer requires a new field-by-field approved contract before implementation.

## 2. Governing privacy/storage rules

1. Every stored field has a requirement/control reference and a necessary product/security/lifecycle purpose.
2. TSK-0230 lawful-basis status vocabulary is reused exactly: `LI_CONDITIONAL`, `CONTRACT_CONDITIONAL`, `LEGAL_OBLIGATION_CONDITIONAL`, `NOT_PERSONAL_OR_SYNTHETIC`, `BLOCKED_NO_VALID_BASIS_OR_CONTRACT`, `PROHIBITED`.
3. A conditional lawful-basis status is a design candidate, not final production legal authorization. `RSK-0001` remains OPEN.
4. If a required production retention period, backup period, recipient, legal basis or deletion guarantee is not yet supported by current evidence, processing is fail-closed until that condition is frozen; no duration or legal conclusion is invented.
5. Persistent identifiable query/file logging remains OFF under CON-0007.
6. Identifiable per-client statistics remain OFF/excluded under CON-0008.
7. `ClientID` is an opaque DNS-control reference only and is never authentication or authorization.
8. A cached/persisted Protection Map value is never self-validating technical evidence. Current technical verification remains independent from account/device ownership.
9. Deleted content must not survive as a shadow profile, audit payload, analytics identity, backup resurrection or reconciliation history.
10. INT-0007 remains downstream acceptance: the implemented database, logs, caches, backups, recipients, deletion behavior and runtime configuration must later be inspected against this contract.

## 3. Logical storage model

### 3.1 J0 — accountless browser/session state

J0 is the default accountless storage tier. It is session-scoped and contains only current routing/presentation/setup state. Durable browser persistence such as unrestricted `localStorage` is not part of this contract; if later needed, each field must independently satisfy this same inventory and expiry/deletion boundary.

| Field | Requirement/control | Purpose / lawful-basis status | Storage & access | Retention | Deletion | Backup |
|---|---|---|---|---|---|---|
| `current_step` | REQ-0019; TSK-0230 D01 | Render active journey; `LI_CONDITIONAL` or `NOT_PERSONAL_OR_SYNTHETIC` according to actual linkability | Browser session only | Active session only | Session destruction or explicit reset | None |
| `route_selection` | REQ-0019; TSK-0230 D01 | Route supported path; same status rule as D01 | Browser session only | Active session only | Session destruction/reset | None |
| `locale` | REQ-0019; TSK-0230 D01/D05 | Render language/RTL; same status rule as actual value/linkability | Browser session only | Active session only | Session destruction/reset | None |
| `platform_family` | REQ-0019; TSK-0230 D06 | Select correct platform instructions; `LI_CONDITIONAL` or non-personal where genuinely non-linkable | Browser session only; coarse enum | Active session only | Session destruction/reset | None |
| `native_safeguard_state` | REQ-0019; TSK-0230 D08 | Current routing/copy only; `LI_CONDITIONAL` | Browser session only | Active session only | Session destruction/reset | None |
| `dns_method` | REQ-0019; TSK-0230 D09 | Select approved DNS setup route; `LI_CONDITIONAL` | Browser session only | Active session only | Session destruction/reset | None |
| `service_category` | REQ-0019; TSK-0230 D10 | Route the one approved relevant service safeguard; `LI_CONDITIONAL` | Browser session only; coarse enum | Active session only | Session destruction/reset | None |
| `protection_map_state` | REQ-0030; TSK-0230 D02/D11 | Render current truth state; `LI_CONDITIONAL` or non-personal where genuinely non-linkable | Browser session only; six-state enum from TSK-0313 | Active session only | Session destruction/reset | None |
| `support_route_state` | REQ-0019; TSK-0230 D12 | Route current issue to self-service; `LI_CONDITIONAL` | Browser session only; bounded enum | Active session only | Session destruction/reset | None |

J0 stores no account ID, provider subject, persistent device ID, AdGuard ClientID, IP-as-product-field, token/secret, free text, DNS query/domain/URL or browsing/activity history.

### 3.2 J1 — optional anonymous transient server state

J1 is permitted only where later implementation demonstrates a real server-side need such as a safe short resume or bounded setup/verification operation. The approved TSK-0229 allowlist remains controlling.

| Field | Requirement/control | Purpose / lawful-basis status | Storage & access | Retention | Deletion | Backup |
|---|---|---|---|---|---|---|
| `journey_token` | REQ-0019; TSK-0230 D03 | Address one anonymous transient record; `LI_CONDITIONAL` | Server-only, random high-entropy opaque token | Maximum 24h from creation, non-sliding | Completion/reset/exit/integrity/orphan trigger; synchronous where possible and within 15m; TTL independently enforced | **None; J1 excluded from durable backups** |
| `created_at` | TSK-0230 D04 | Enforce hard lifetime; `LI_CONDITIONAL` | Server-only | Same as J1 | Delete with J1 | None |
| `hard_expires_at` | TSK-0230 D04 | Enforce non-sliding expiry; `LI_CONDITIONAL` | Server-only | Same as J1 | Delete with J1 | None |
| `locale` | TSK-0230 D05 | Render correct localized route; `LI_CONDITIONAL` | Journey-scoped server access | Same as J1 | Delete with J1 | None |
| `device_family` | TSK-0230 D06 | Route correct supported instructions; `LI_CONDITIONAL` | Coarse enum; journey-scoped | Same as J1 | Delete with J1 | None |
| `platform_version_band` | TSK-0230 D06 | Version-safe instruction routing; `LI_CONDITIONAL` | Coarse bounded value only | Same as J1 | Delete with J1 | None |
| `phone_state` | TSK-0230 D07 | Route already-configured/current phone state; `LI_CONDITIONAL` | Controlled enum | Same as J1 | Delete with J1 | None |
| `journey_step` | TSK-0230 D07 | Resume current step without event history; `LI_CONDITIONAL` | Single current controlled value | Same as J1 | Delete with J1 | None |
| `native_safeguard_state` | TSK-0230 D08 | Render current safeguard state; `LI_CONDITIONAL` | Controlled enum | Same as J1 | Delete with J1 | None |
| `dns_method` | TSK-0230 D09 | Route current DNS method; `LI_CONDITIONAL` | Controlled enum | Same as J1 | Delete with J1 | None |
| `baseline_protection_state` | TSK-0230 D09 | Preserve current bounded truth state only; `LI_CONDITIONAL` | Current state only, no history | Same as J1 | Delete with J1 | None |
| `service_category` | TSK-0230 D10 | Route one relevant service safeguard; `LI_CONDITIONAL` | Coarse enum | Same as J1 | Delete with J1 | None |
| `service_safeguard_state` | TSK-0230 D10 | Render current service state; `LI_CONDITIONAL` | Current enum only | Same as J1 | Delete with J1 | None |
| `protection_map_state` | TSK-0230 D11 | Render current six-state result; `LI_CONDITIONAL` | Current enum only; not technical proof by itself | Same as J1 | Delete with J1 | None |
| `support_route_state` | TSK-0230 D12 | Route current issue; `LI_CONDITIONAL` | Controlled current state | Same as J1 | Delete with J1 | None |
| `completed_at` | TSK-0230 D13 | Trigger prompt deletion after completion; `LI_CONDITIONAL` | Server-only | Until J1 deletion only | Delete with J1 immediately after necessary response/artifact | None |

**J1 prohibited fields/joins:** parent/account/provider identity, stable customer/device ID, AdGuard ClientID, email, phone, child identity/profile, IP-as-product-field, fingerprint, analytics identifier, browsing/domain/query/URL history, raw diagnostics, free text, payment data, marketing attribution, account foreign key or any `journey_token -> account` lookup table.

### 3.3 AUTH — optional parent authentication and server session

AUTH exists only for optional account features. TSK-0356 owns the final Firebase/Google/session architecture; this task freezes only the minimum data boundary required by ACC-0233.

| Field/state | Requirement/control | Purpose / lawful-basis status | Storage & access | Retention | Deletion/revocation | Backup |
|---|---|---|---|---|---|---|
| Provider identity token | REQ-0040; TSK-0230 D14 | Establish optional parent identity; `CONTRACT_CONDITIONAL` or `LI_CONDITIONAL` only if later current legal/terms assessment supports it | Transient server validation path; never product database/browser localStorage | Validation/exchange only | Discard after session establishment/failed validation | None |
| Server-managed session credential | REQ-0040; TSK-0230 D15 | Secure authenticated optional-account session; `CONTRACT_CONDITIONAL` or `LI_CONDITIONAL` subject to current basis assessment | Server-managed Secure/HttpOnly/SameSite session boundary; exact mechanism TSK-0356 | Session lifetime only; exact duration frozen by TSK-0356 before implementation | Logout, expiry, revocation, disabled/deleted account | No product-history backup; any underlying provider/session mechanism follows approved TSK-0356 contract |
| Provider subject reference | REQ-0037; TSK-0230 D14 | Stable minimum link between provider identity and the optional parent account; `CONTRACT_CONDITIONAL` or `LI_CONDITIONAL` only after current basis assessment | Server-side persistent A-domain mapping only | While account relationship is active; no historical inactive profile by default | Delete/unlink with account subject to provider/deletion contract | Only if included in an approved A-domain backup under section 6 |

**Not stored by default in the UseSafeWeb product database:** provider display name, profile photo, full provider profile, contacts, child identity, arbitrary OAuth claims, raw identity/access/refresh tokens, password or SMS credential. Email is not persisted merely because the provider supplies it; a later task must prove a necessary product/security/legal purpose before adding it.

### 3.4 A — persistent parent/device ownership domain

The persistent product store is logical at this task. TSK-0233 defines its minimum schema and lifecycle; datastore product/runtime pinning remains downstream architecture/implementation work and must not change these field/privacy constraints.

#### `ParentAccount`

| Field | Requirement/control | Purpose / lawful-basis status | Access | Retention | Deletion | Backup |
|---|---|---|---|---|---|---|
| `parent_id` | REQ-0037; TSK-0230 D16 | Opaque internal ownership root; `CONTRACT_CONDITIONAL` or `LI_CONDITIONAL` subject to current basis assessment | Server-side account/ownership services only | While account relationship is active | Delete after governed account deletion/reconciliation completes | Conditional A-domain backup only under section 6 |
| `provider_subject` | REQ-0040; TSK-0230 D14 | Map server-validated provider identity to one parent account; same conditional status | Auth/ownership service only | While account relationship is active | Delete/unlink with account and provider-side action as supported | Conditional A-domain backup only |
| `account_status` | REQ-0037; TSK-0230 D14 | Control active/deleting lifecycle safely; same conditional status | Auth/ownership service | Active deletion lifecycle only; no indefinite historical status ledger | Remove with final account deletion; temporary deletion state removed on completion | Conditional only while primary record is eligible |
| `created_at` | REQ-0019; TSK-0230 D14/D25 | Minimum lifecycle/reconciliation timestamp; same conditional status | Server only | While account is active; no retention after deletion unless separately justified as D25 evidence | Delete with account unless transformed to separately authorized content-free D25 evidence | Conditional only while primary record is eligible |
| `row_version` | REQ-0019; reliability necessity | Optimistic concurrency/idempotency for ownership mutations; same conditional status | Server only | While account record exists | Delete with account | Conditional only while primary record is eligible |

#### `ParentDevice`

| Field | Requirement/control | Purpose / lawful-basis status | Access | Retention | Deletion | Backup |
|---|---|---|---|---|---|---|
| `device_id` | REQ-0037; TSK-0230 D16 | Opaque product device record ID; `CONTRACT_CONDITIONAL` or `LI_CONDITIONAL` subject to current basis assessment | Server-side ownership service; parent-scoped reads through authorization | While parent-device relationship is active | Delete on governed device removal/account deletion after reconciliation | Conditional A-domain backup only |
| `parent_id` | REQ-0037; TSK-0230 D16 | Enforce parent ownership server-side; same conditional status | Server-side authorization only | Same as device relation | Delete with device/account | Conditional A-domain backup only |
| `nickname` | REQ-0037; TSK-0230 D16 | Optional parent-friendly identification of owned device; same conditional status | Parent-owner scoped app/server only | While device relation active or until parent clears it | Clear/delete with device/account or parent edit | Conditional A-domain backup only |
| `platform_family` | REQ-0037; TSK-0230 D16 | Route supported device-management/setup behavior; same conditional status | Parent-owner scoped app/server | While relation active | Delete with device/account | Conditional A-domain backup only |
| `lifecycle_status` | REQ-0037; TSK-0230 D16 | Coordinate active/revoking/deleting/reconciling state; same conditional status | Server; bounded parent-facing projection | Only current lifecycle state; no history ledger | Delete after final removal/reconciliation | Conditional only while primary record is eligible |
| `adguard_client_id` | CON-0007; CON-0008; TSK-0230 D17 | Server-side linkage needed to provision/revoke intended DNS client; same conditional status | **Server-side only**; never authorization; not exposed as customer/admin credential | Active configured-device lifecycle only | Revoke/remove/reconcile then delete mapping on device/account removal | Conditional A-domain backup only if required for recoverable current configuration; no query data |
| `settings_profile_id` | REQ-0041; TSK-0230 D16 | Identify approved curated settings profile, not arbitrary AdGuard policy | Server + parent-owner bounded UI | Current active device relation | Delete with device/account | Conditional A-domain backup only |
| `settings_version` | REQ-0041; TSK-0230 D16 | Reproduce current curated-setting contract | Server + parent-owner bounded UI | Current active device relation | Delete with device/account | Conditional A-domain backup only |
| `protection_state` | REQ-0030; TSK-0230 D18 | Cache only the latest parent-facing Protection Map state for dashboard continuity; same conditional status | Parent-owner scoped reads; server writes/evaluation | **Latest current record only** while device active; freshness rules must invalidate stale positive state | Delete with device/account; expiry/freshness removes current positive claim | Conditional A-domain backup only; restore never makes state technically verified without fresh evidence |
| `protection_reason_code` | REQ-0030; TSK-0230 D18 | Explain current bounded truth state without DNS history; same conditional status | Parent-owner scoped | Latest current record only | Delete with device/account/current state | Conditional A-domain backup only |
| `verifier_version` | REQ-0030; TSK-0230 D18 | Trace which current verifier contract produced a technical result | Parent-owner bounded UI/server | Latest current record only | Delete with device/account/current state | Conditional A-domain backup only |
| `evaluated_at` | REQ-0030; TSK-0230 D18 | Enforce freshness; not behavioral timeline | Parent-owner scoped | Latest current record only | Delete with device/account/current state | Conditional A-domain backup only |
| `evidence_fresh_until` | REQ-0030; TSK-0230 D18 | Prevent stale positive protection claim | Server evaluation + parent-owner display | Latest current record only | Delete with device/account/current state | Conditional A-domain backup only; restore must re-evaluate |
| `row_version` | REQ-0019; reliability necessity | Concurrency/idempotency for device mutations | Server only | While device exists | Delete with device | Conditional only while primary record is eligible |
| `created_at` | REQ-0019; lifecycle necessity | Minimum lifecycle ordering/reconciliation | Server only | While device exists | Delete with device | Conditional only while primary record is eligible |
| `updated_at` | REQ-0019; lifecycle necessity | Minimum last-current mutation timestamp; not activity history | Server only | Current device record only | Delete with device | Conditional only while primary record is eligible |

There is **no** `DeviceHistory`, `DnsQuery`, `Domain`, `VisitedUrl`, `TopDomain`, `ChildActivity`, `BrowsingEvent`, `JourneyToAccount`, `ClientHistory`, unrestricted raw AdGuard configuration, or child-profile table.

## 4. Explicit no-linkage and explicit-save rule

### 4.1 Default: no anonymous-to-account linkage

J0/J1 have no `parent_id`, `provider_subject`, `device_id`, `adguard_client_id` or persistent analytics identity. A has no `journey_token` field. No table, cache, log or analytics projection may map the two domains.

Sign-in/account creation does not extend J1 TTL and does not import J1 history. J1 expires/deletes independently even if the same browser later signs in.

### 4.2 Optional account-mode device creation

If a signed-in parent chooses to add/save a device, the application creates a **fresh A-domain device record from explicitly submitted/confirmed allowlisted values** required for that account-mode operation. It does not import the J1 record or preserve a J1 event trail.

Allowed fresh inputs are limited to the A-domain fields above: optional nickname, supported platform family, selected approved curated settings and the server-generated/managed ownership/ClientID/lifecycle fields. Current protection evidence must be evaluated independently; a J1 value or parent confirmation cannot silently become `protected_verified`.

A future proposal to copy any additional J0/J1 field into A requires a separately approved field-level purpose/necessity/basis/retention/deletion/backup contract and privacy/security review before implementation.

## 5. Access and authorization model

1. J0 is confined to the active same-origin browser session.
2. J1 is server-side and addressed only by its random journey token; possession of a token does not authorize A-domain access.
3. AUTH establishes the parent identity/session; authenticated identity alone still does not authorize arbitrary device records.
4. Every A-domain device read/write/delete/revoke/reinstall/replace/settings operation resolves `parent_id` from the verified server session and enforces `ParentDevice.parent_id == authenticated parent_id` server-side.
5. Browser-supplied `parent_id`, `device_id`, `ClientID`, provider subject or ownership claim is untrusted input.
6. `adguard_client_id` is never authorization and is not a customer-visible admin credential.
7. Only the typed allowlisted server-side AdGuard adapter may use the ClientID/control-plane linkage.
8. Cross-parent/IDOR access must fail closed and is later proven by implementation/security acceptance; this design does not self-certify runtime enforcement.

## 6. Retention and backup contract

| Domain/data | Current retention rule | Backup rule | Fail-closed condition |
|---|---|---|---|
| J0 | Active browser/session only | Never | Durable browser persistence requires a separately accepted field contract |
| J1 | Maximum 24h non-sliding; delete earlier on completion/reset/exit/integrity/orphan trigger, synchronously where possible and within 15m | **Never** | Any implementation unable to enforce TTL/early deletion/no-backup cannot use J1 |
| AUTH token exchange | Validation/exchange only | Never | Raw provider credentials/tokens must not become product history |
| Server session | Exact approved session lifetime from TSK-0356 | No product-history backup | TSK-0356 must freeze revocation/expiry before implementation |
| Active `ParentAccount` / `ParentDevice` primary rows | Only while the optional account/device relationship is active and required for approved ownership/settings/lifecycle value | May be backed up only after an exact production backup retention/access/encryption/deletion/restore contract is approved | **Until exact backup retention and deletion-propagation/restore semantics are frozen, production A-domain backup processing is `BLOCKED_NO_VALID_BASIS_OR_CONTRACT` rather than assigned an invented period** |
| Current Protection Map metadata | One current freshness-bounded record only while device relation is active | If restored, it is stale/non-verified until fresh evidence re-evaluates it | No history series or restored positive state may masquerade as fresh verification |
| ClientID mapping | Active governed device/control-plane lifecycle only | Only as part of an approved current-state recovery backup, never query/history data | Remove/revoke/reconcile on device/account deletion; stale mapping cannot authorize or prove protection |
| Deletion/reconciliation operation state | Only while an operation is incomplete/reconciling | No backup by default unless recovery of an in-flight operation is specifically justified downstream | After success, delete subject-linked operation state; any retained completion evidence must meet D25 below |
| D25 content-free completion evidence | Only if a current accountability/security/legal purpose and basis is established | No deleted content; no browsing/query data | Exact retention must be frozen before production; otherwise durable D25 storage is blocked |

The phrase “while active” is a purpose boundary, not permission for indefinite inactive retention. Deleted/revoked relationships do not remain as historical product rows merely for convenience.

## 7. Deletion, revoke and reconciliation flows

### 7.1 J0 reset/session end

1. Parent exits/resets or browser session ends.
2. J0 values are destroyed.
3. No server/account deletion is claimed because J0 is a separate domain.

### 7.2 J1 expiry/early deletion

1. Completion/reset/exit/integrity/orphan trigger requests immediate deletion.
2. Delete synchronously where possible; bounded cleanup completes within 15 minutes.
3. Independent hard TTL deletes the record no later than 24 hours after creation.
4. Account sign-in/activity cannot extend the timer.
5. No backup can restore J1.

### 7.3 Device revoke/remove

1. Verify server session and parent ownership.
2. Create the smallest in-flight reconciliation state required to make the mutation idempotent/recoverable.
3. Request the typed server-side AdGuard adapter to revoke/remove/reconcile the intended current ClientID/client configuration.
4. On a definite safe completion, delete the `ParentDevice` row, settings/current-state metadata and ClientID mapping.
5. Remove subject-linked in-flight reconciliation state.
6. If a current justified D25 completion record is approved, retain only content-free operation metadata under its independently frozen period; otherwise retain nothing durable after completion.
7. **Do not claim that the DNS/profile was removed from the physical phone.** Physical device configuration removal is a separate user/device operation and technical verification state.
8. On an ambiguous/partial control-plane result, deny normal management assumptions, show truthful `uncertain/reconciling` state, retry only bounded/idempotent operations, and reconcile before declaring deletion complete.

### 7.4 Account deletion

1. Require the current downstream reauthentication/confirmation rule.
2. Revoke/expire UseSafeWeb sessions.
3. Enumerate only devices whose server-side ownership resolves to the deleting `parent_id`.
4. Revoke/remove/reconcile each corresponding current AdGuard ClientID through the typed server-side adapter.
5. Delete all owned `ParentDevice` records, settings and current Protection Map metadata after their control-plane disposition is known or safely fenced for reconciliation.
6. Delete the `ParentAccount` row and provider-subject mapping.
7. Perform provider-side deletion/revocation/unlinking exactly as the approved TSK-0356/provider contract supports; do not fabricate provider deletion.
8. Delete subject-linked in-flight operation state after reconciliation.
9. Retain only separately approved content-free D25 evidence, if any; never retain deleted account/device content as an audit copy.
10. Propagate deletion into approved backups according to the future exact backup deletion/restore contract; until that contract exists, production A-domain backup use remains blocked.
11. **Do not claim physical DNS/profile removal from the phone solely because server/account data was deleted.**

### 7.5 Restore/recovery

1. Restore only current permitted A-domain fields from an approved protected backup.
2. Apply deletion/reconciliation records or equivalent restore-time exclusion mechanism so already-deleted accounts/devices are not resurrected.
3. J0/J1 are never restored.
4. DNS query/domain history is never restored because it is never an approved stored dataset.
5. Restored Protection Map metadata is treated as stale/non-verified until fresh technical evidence satisfies current verification rules.
6. Restore completion does not itself prove the physical device is configured or protected.

## 8. Data-flow boundaries

```mermaid
flowchart LR
  B[Parent browser] -->|J0 only; no login needed| APP[UseSafeWeb Next.js server]
  APP -. optional anonymous need .-> J1[(J1 TTL store <=24h; no backup)]
  B -. optional sign-in .-> IDP[Google/Firebase provider]
  IDP -. identity validation .-> APP
  APP -->|server session + ownership checks| A[(Minimal ParentAccount / ParentDevice store)]
  APP -. typed allowlisted control .-> AGC[Private AdGuard control plane]
  DEV[Managed device] -->|encrypted DNS; separate data plane| DNS[UseSafeWeb DNS / AdGuard]
  DNS --> Q9[Quad9 dns10 DoH]

  J1 -.-X A
  DNS -.-X A
```

`J1 -X A` means no direct or implicit data join. `DNS -X A` means ordinary DNS query/domain history does not enter the account store. The only permitted DNS-control relation is the server-side opaque `adguard_client_id` used to manage the parent-owned current client configuration; it contains no query history and grants no authorization by itself.

## 9. Field-to-acceptance trace

| ACC-0233 element | Contract evidence | Result |
|---|---|---|
| Every anonymous journey/session field maps to requirement + lawful purpose | J0/J1 field tables include requirement/control and lawful-basis status | PASS candidate |
| Every optional parent identity/device-ownership field maps to requirement + lawful purpose | AUTH, `ParentAccount`, `ParentDevice` field tables | PASS candidate |
| Anonymous state minimized/scoped/expiring | J0 session-only; J1 exact allowlist, non-sliding ≤24h and early deletion ≤15m | PASS candidate |
| Persistent account/device data limited to ownership/settings/lifecycle | A-domain schema contains only minimum identity/ownership/settings/current-state/lifecycle/concurrency fields | PASS candidate |
| Explicit access | Section 5 plus per-field access columns | PASS candidate |
| Explicit retention | Sections 3 and 6; unresolved production periods fail closed instead of being invented | PASS candidate |
| Explicit deletion | Section 7 plus per-field deletion columns | PASS candidate |
| Explicit backup handling | J0/J1 no backup; A-domain backup blocked until exact production retention/deletion/restore contract exists | PASS candidate |
| No DNS/domain browsing-history store | Explicit prohibited schemas/fields; separate DNS data plane | PASS candidate |
| Core value does not require identity | Section 1; AUTH/A optional only | PASS candidate |

## 10. Deterministic acceptance assertions

A compliant implementation/reviewer must be able to prove all of the following:

1. J0 fields are session-scoped and contain no persistent account/device/DNS identity.
2. J1 contains only the approved anonymous allowlist, has no account/provider/device/ClientID foreign key and has a maximum 24-hour non-sliding expiry.
3. J1 early deletion is synchronous where possible and completes within 15 minutes; J1 is excluded from durable backups.
4. No `journey_token -> account/device` lookup, migration table, analytics identity join, fingerprint/IP stitching or automatic sign-in conversion exists.
5. Optional account-mode device creation uses fresh allowlisted inputs and server-generated ownership/control identifiers rather than importing J1 history.
6. `ParentAccount` stores only the minimum opaque parent/provider/lifecycle/concurrency fields in this contract; provider profile expansion is not implicit.
7. `ParentDevice` stores only minimum ownership, optional nickname/platform, curated settings, current lifecycle, current freshness-bounded Protection Map metadata, concurrency fields and server-side ClientID linkage.
8. Every A-domain device operation checks authenticated parent ownership server-side; ClientID alone never authorizes access.
9. No DNS question/domain/URL/browsing/top-domain/child-activity table, event history or unrestricted AdGuard configuration store exists.
10. Persistent identifiable query/file logging is off and identifiable per-client statistics remain off/excluded.
11. Protection metadata stores one current freshness-bounded state, not a history; restored/cached data cannot create `protected_verified` without fresh qualifying technical evidence.
12. The complete accountless core remains available without identity/account creation.
13. Device deletion/revocation, account deletion, AdGuard control-plane reconciliation and physical phone DNS/profile removal are represented as separate truthful operations.
14. Partial/ambiguous mutations become bounded reconciliation/uncertain state; no duplicate client, cross-parent access, fabricated deletion or fabricated protection success is allowed.
15. J0/J1 are never restored from backup and already-deleted A-domain state cannot be resurrected by restore.
16. A-domain production backup use is blocked until exact backup retention, access/encryption, deletion propagation and restore semantics are frozen under current authority.
17. Any durable D25 deletion-completion evidence is content-free, purpose/basis-limited and has an exact approved retention period before production; otherwise it is not stored.
18. All conditional lawful-basis labels remain conditional; this artifact does not close `RSK-0001` or authorize real England participant processing.
19. INT-0007 still requires later runtime/database/cache/log/backup/config inspection against this logical contract.
20. No downstream implementation, deployment, LG-07/LG-08/LG-09, participant activation or launch PASS is inferred from this design artifact.

## 11. Deviations, unresolved facts and downstream bindings

- **Datastore product/runtime:** deliberately not selected here. The logical schema and constraints are frozen; datastore selection/runtime pinning must preserve them and is downstream architecture/implementation work.
- **Firebase/Google/session details:** TSK-0356 must establish the then-current provider/session architecture, exact session lifetime, revocation behavior, vendor/privacy/terms/price/transfer facts and migration trigger before implementation acceptance.
- **Persistent backup period:** no exact period is invented. Production A-domain backup processing is fail-closed until the exact retention/access/encryption/deletion propagation/restore semantics are current and accepted.
- **D25 accountability evidence period:** no exact period is invented. Durable completion evidence is prohibited until a necessary current purpose/basis and exact retention are approved.
- **Final UK legal/data readiness:** unresolved under `RSK-0001`; REQ-0018 remains controlling for real England participants. This design is not legal sign-off.
- **Actual processing reality:** INT-0007 remains mandatory. Later implementation/release acceptance must inspect actual schemas, recipients, logs, caches, backups, deletion and runtime configuration; this artifact alone cannot prove production compliance.

## 12. ACC-0233 disposition

The design supplies a field-level, purpose-linked dual-mode model with strict anonymous/persistent separation, minimum persistent ownership/settings/lifecycle data, explicit access/retention/deletion/backup behavior, fail-closed treatment of unresolved production retention/legal facts, no J1-to-account history conversion, no DNS/domain browsing-history store and no mandatory identity for core value.

**TSK-0233 is ready for independent verification against ACC-0233 / VER-0233 / EVD-0233.**
