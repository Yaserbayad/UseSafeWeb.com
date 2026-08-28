# TSK-0229 — Accountless Journey Data Model, Expiry, Deletion and No-Linkage Rules

**Task:** TSK-0229 — Define and approve the accountless journey data model, expiry, deletion, and no-linkage rules  
**Acceptance:** ACC-0229  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** APPROVED L4 DATA CONTRACT / INTERNAL / IMPLEMENTATION NOT AUTHORIZED  
**Date:** 2026-08-28  
**Authority:** DEC-0042 / TSK-0146 accountless-first + TSK-0141 provisional minimum scope + CR-0003  
**Verification state:** PASS candidate pending independent verification and runtime reconciliation.  

## Provisional evidence limitation — RSK-0002 remains OPEN

Real-participant Experiment-1/L3 behavioral evidence is deferred under DEC-0050/CR-0003. Therefore this L4 contract is a conservative **provisional design contract**, not a behaviorally validated result. There is no current real-participant evidence proving completion behavior, incremental value, comprehension, support burden, persistence, parent-perceived duplication, or that the provisional state/expiry choices are optimal for parents.

`RSK-0002` remains OPEN and materially applies to this artifact. Synthetic/technical evidence and model judgment do not substitute for real-user evidence. When L3 is reactivated on 2027-08-27 or earlier by explicit owner authority, any materially dependent rule must be re-evaluated against real evidence and reopened if contradicted. This artifact does not make LG-05/LG-06 PASS and does not authorize implementation/build, real-participant processing, legal completion, payment activation, public release, or launch.

## 1. Contract objective

Define the smallest testable product-state contract that allows an accountless parent to complete the immediate UseSafeWeb setup journey **without creating a persistent parent identity, child profile, browsing history, DNS-query history, or cross-session behavioral profile**.

This is an L4 data/behavior contract, not a storage-technology decision and not implementation authority. Later architecture may choose an implementation only if it satisfies these invariants.

## 2. Core rule: default no persistent journey record

The active baseline is:

1. prefer in-memory/browser-session state for the immediate journey;
2. do not require server-side persistence merely for implementation convenience;
3. if a server-side anonymous journey record is technically required for safe completion or a deliberately supported short resume path, it must use the minimal model below;
4. no mandatory account, login, email, phone number, parent name, child name or stable customer/device identifier is introduced;
5. a transient network address needed to deliver traffic is not a journey field and must not be persisted as product state;
6. DNS/query/domain history is never part of the journey model.

## 3. Allowed accountless state classes

### J0 — Browser/session-only UI state

Preferred default. Exists only for the active browser/session and is not written to a durable server-side product record.

Allowed uses:
- current screen/step;
- temporary form selections needed for routing;
- temporary presentation state;
- locally computed Protection Map state during the active journey.

Required behavior:
- cleared when the browser/session state is destroyed;
- never treated as durable evidence of protection after the session;
- must not contain secrets, browsing/query history or unnecessary personal data.

### J1 — Optional anonymous short-lived journey record

Permitted **only when later architecture demonstrates that server-side state is necessary** for safe completion, verification, generation of a setup artifact, or an explicitly supported accountless resume mechanism.

J1 is not an account, profile, device registry or analytics identity.

**Provisional privacy-safe default TTL:** maximum **24 hours from creation**, non-sliding. The TTL may be shortened without owner approval when compatibility permits. It may not be lengthened without explicit product/privacy/architecture evidence and current authority.

## 4. J1 field model

Only the fields below are permitted in the base J1 model. A later field requires explicit necessity mapping and data-contract review before implementation.

| Field | Type / allowed values | Required | Necessity | Linkage restriction |
| --- | --- | --- | --- | --- |
| `journey_token` | cryptographically random opaque value; no embedded meaning | yes | Address the transient record without identity | Must not encode parent/child/device/IP/locale facts; not reused after deletion/expiry |
| `created_at` | UTC timestamp | yes | TTL enforcement/audit | No identity meaning |
| `hard_expires_at` | UTC timestamp = creation + ≤24h | yes | Deterministic deletion | Must not slide automatically on activity |
| `locale` | supported UI locale code | yes | Render correct content/RTL | Must not be treated as nationality/location/market evidence |
| `device_family` | `iphone`, `android`, `unsupported_or_unknown` | yes | Route supported technical instructions | No serial, advertising ID, hardware ID or account ID |
| `platform_version_band` | coarse supported/version-routing band or `unknown` | conditional | Choose correct current instructions | Do not store exact build/device fingerprint unless later technically necessary and approved |
| `phone_state` | `new_phone`, `already_used_phone`, `unknown` | optional | Route already-configured handling | No purchase date or child event/date |
| `journey_step` | controlled step enum | yes | Resume/render current path | No free-text activity trail |
| `native_safeguard_state` | controlled state enum | optional | Drive current Phone step / Protection Map | Parent confirmation remains distinct from system verification |
| `dns_method` | controlled supported mechanism, e.g. `ios_doh_profile`, `android_private_dns_dot`, `not_selected`, `unsupported` | optional | Route Internet step | No resolver query history or unique AdGuard client identity |
| `baseline_protection_state` | `not_started`, `configured_unverified`, `verified`, `failed`, `uncertain`, `removed` | optional | Truthful current protection state | Verification evidence must not require browsing/query history |
| `service_category` | approved coarse category or `none_applicable` | optional | Route the one relevant Service branch | No service username/account identifier |
| `service_safeguard_state` | controlled state enum | optional | Protection Map/current branch | No service credentials/content/history |
| `protection_map_state` | controlled per-layer truth states or derivable equivalent | optional | Render truthful end state | No activity/history fields |
| `support_route_state` | controlled category/status only | optional | Recover from a current setup problem | No free-text personal details or diagnostic payload |
| `completed_at` | UTC timestamp | optional | Trigger immediate deletion workflow | Record itself is deleted promptly after completion |

### Allowed controlled state principle

State values describe **setup/protection status**, not user behavior over time. Do not add event histories, clickstreams, domain histories, page-view trails or per-user engagement profiles to J1.

## 5. Explicit prohibited fields and data classes

The accountless journey model must never contain, by default or under an implementation shortcut:

- parent name, child name or household-member names;
- email address or phone number;
- exact child age/date of birth;
- home/school address, postcode or routine/precise location;
- school name;
- account passwords, authentication codes, recovery codes, tokens or service credentials;
- Apple/Google/social/service username or stable account identifier;
- device serial number, IMEI, advertising identifier, hardware fingerprint or persistent app/browser fingerprint;
- stable UseSafeWeb customer/device identifier;
- IP address as a stored product-state field;
- browsing history, URL history, DNS query history, visited-domain history, top-domain/activity data;
- messages, contacts, photos, social content or content-derived child profile;
- raw diagnostic logs;
- payment/card/billing data;
- marketing/ad attribution profile;
- unrestricted free-text notes capable of accumulating personal data;
- participant/research identity or Experiment-1 metric record.

## 6. Expiry and deletion contract

### J0

- lifetime: active browser/session only;
- normal deletion: browser/session destruction;
- explicit reset/restart action: clear J0 immediately;
- no server backup because J0 is not server-persisted product state.

### J1

**Hard TTL:** no later than 24 hours after `created_at`, regardless of activity.

Early deletion triggers:

1. successful journey completion after any immediately necessary response/artifact has been delivered;
2. user selects reset/start over;
3. user selects remove/exit and no further transient operation requires state;
4. integrity/security failure makes the state unsafe to retain;
5. support flow intentionally abandons the transient record;
6. an implementation creates an invalid/orphan record.

Deletion execution requirement:

- prefer synchronous deletion at the trigger;
- if asynchronous cleanup is required, deletion must complete within **15 minutes** of the trigger;
- TTL cleanup must run independently of user return/activity;
- expired/deleted tokens must not resolve to a record and must not be reused.

The 24-hour TTL and 15-minute cleanup bound are **provisional minimisation defaults**, not behavioral findings. Later architecture may shorten them freely. Lengthening requires documented necessity plus privacy/product/architecture review and current authority.

## 7. No-linkage rules

J0/J1 must not be linked to create a persistent identity graph.

Specifically:

- no identity-to-`journey_token` table;
- no stable parent/customer/device ID attached to J1;
- no linkage to AdGuard query history, because such product/query-history state is prohibited;
- no linkage to persistent AdGuard client objects solely for product identity;
- no cross-session stitching using cookies, fingerprinting, IP address, device characteristics or analytics IDs;
- no third-party advertising/behavioral identifier;
- no linking of later anonymous journeys to infer a household profile;
- no GitHub commit, issue, artifact or evidence record containing a live journey token or journey field values from a real user.

If a later approved EXC-0001 account model is activated, it requires a **new data-contract decision**. It may not silently repurpose J1 tokens/history into persistent customer history.

## 8. DNS and technical verification boundary

The product may perform the minimum technical checks required to determine whether the approved encrypted resolver path is functioning, but:

- verification result is stored only as a controlled state such as `verified`, `failed` or `uncertain`;
- the journey record does not store domains queried to perform verification;
- no child browsing/domain history is collected to prove protection;
- no browsing-history dashboard is created;
- existing AdGuard privacy controls remain authoritative for the DNS service;
- diagnostic escalation, if genuinely necessary, is separate from J1 and follows the exceptional diagnostic procedure rather than broadening this model.

## 9. Diagnostic separation

Ordinary setup/support must use configuration/state checks and synthetic tests first.

If request-level diagnostic data is genuinely necessary:

1. invoke the separately governed exceptional-diagnostic process;
2. create a distinct diagnostic ticket/reference rather than adding raw diagnostics to J1;
3. store only the opaque diagnostic ticket reference in ordinary support state if linkage is actually necessary;
4. apply the diagnostic procedure's own field limits, time box and deletion verification;
5. delete diagnostic data independently when its authorized window ends;
6. do not use diagnostic data for analytics, personalization, marketing or product history.

J1's 24-hour TTL does **not** extend an exceptional diagnostic window, and a diagnostic ticket does not justify retaining J1 longer.

## 10. Logging, analytics and observability boundary

Implementation observability may record aggregate service health/errors necessary to operate the system, but product/journey observability must not defeat the accountless model.

Prohibited by default:

- logging full `journey_token` values;
- logging form payloads or full J1 records;
- IP-to-token linkage logs;
- user-level clickstream/session replay;
- persistent per-journey analytics profiles;
- raw DNS/domain/request history as journey telemetry.

Allowed design direction:

- aggregate counters for non-identifying error/step categories where later architecture demonstrates necessity;
- redacted/non-sensitive error codes;
- synthetic monitoring;
- technical service metrics that do not create a family behavioral profile.

Any analytics field must have a separate necessity/purpose/retention definition before implementation; it is not implicitly authorized by J1.

## 11. Backup and recovery boundary

Default rule: **J1 is ephemeral operational state and must not be included in durable product backups.**

If a later architecture cannot technically exclude the transient store from a backup mechanism, that architecture is not automatically compliant with this contract. It must first document:

- why backup inclusion is technically necessary;
- encryption/access controls;
- how expired/deleted records cannot be resurrected into active product state;
- restoration-time TTL/deletion reconciliation;
- maximum backup retention;
- privacy approval and test evidence.

Without that evidence, use a backup design that excludes J1.

## 12. Testable acceptance invariants

A later implementation must be testable against at least these invariants:

1. **Schema allowlist:** an attempted field outside the approved contract is rejected or requires explicit versioned schema approval.
2. **No identity:** no required field can carry parent/child/account identity.
3. **No history:** no field stores browsing/DNS/domain/activity history.
4. **Opaque token:** token contains no semantic/user facts and is not reused.
5. **Hard TTL:** a J1 record cannot remain active beyond its fixed `hard_expires_at` (≤24h after creation).
6. **Early delete:** completion/reset/exit trigger removes state synchronously or within 15 minutes.
7. **No sliding:** ordinary activity cannot extend the hard TTL.
8. **No linkage:** no supported query can join J1 to a persistent parent/child/device profile or DNS history.
9. **No token logging:** production logs/telemetry do not expose full live journey tokens or record payloads.
10. **Diagnostic separation:** ordinary J1 schema cannot accept raw diagnostic/DNS-query payloads.
11. **Backup exclusion:** transient J1 state is absent from durable backups unless a later explicitly approved exception exists.
12. **Deletion read-back:** after deletion/expiry the token returns no active record.
13. **Restart safety:** restoring/restarting services does not extend expired state or recreate deleted tokens.
14. **Accountless completion:** supported immediate journey can complete without account creation or persistent identity.

## 13. Versioning and change rule

This contract is `accountless-journey-data-v1`.

Any future change that adds:

- a persistent identifier;
- identity/contact data;
- a longer TTL;
- cross-session linkage;
- new personal-data category;
- behavioral analytics;
- backup retention of J1;
- linkage to DNS/activity data;
- account/dashboard persistence;

is a **material data-contract change**, not a routine field addition. It requires explicit impact analysis against DEC-0042, EXC-0001, privacy/security requirements, current gates and owner authority where applicable.

## 14. ACC-0229 result

ACC-0229 requires only fields necessary for the active journey, no browsing history or persistent child profile, and testable expiry/deletion/diagnostic boundaries.

This contract:

- provides an explicit allowlisted minimum J1 schema plus preferred J0 no-persistence state;
- prohibits identity, browsing/query history and persistent child/family profiles;
- fixes a non-sliding ≤24-hour hard TTL with immediate/≤15-minute early deletion;
- prohibits cross-session/DNS/identity linkage;
- separates exceptional diagnostics;
- excludes ephemeral state from backups by default;
- defines fourteen implementation-testable invariants;
- explicitly preserves the missing L3 behavioral evidence limitation and open `RSK-0002` required by DEC-0050/CR-0003.

**TSK-0229 result: PASS candidate subject to independent verification and runtime read-back.**
