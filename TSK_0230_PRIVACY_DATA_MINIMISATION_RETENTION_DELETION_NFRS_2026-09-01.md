# TSK-0230 — Privacy, Data-Minimisation, Retention and Deletion NFRs

**Task:** TSK-0230 — Define privacy, data-minimisation, retention, and deletion NFRs  
**Acceptance:** ACC-0230 / VER-0230 / EVD-0230  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Version:** 1.0.0-post-CR-0008  
**Date:** 2026-09-01  
**Status:** CURRENT L4 NFR CANDIDATE; implementation, legal compliance, participant activation and downstream PASS are not inferred  
**Authority:** CR-0008 modular Master Planning System; current TSK-0313 Protection Map state/evidence contract; current TSK-0042 support/exception/recovery/removal requirements; current TSK-0229 accountless data/no-linkage contract and post-CR-0006 separation amendment; current TSK-0498 privacy-safe event contract; REQ-0018/REQ-0019; CON-0007/CON-0008; RSK-0001; INT-0006/INT-0007.

## 1. Acceptance boundary

This contract defines the privacy NFR that every implementation data element must satisfy before it may be processed by UseSafeWeb.

For **every data element**, the implementation/data inventory must record all of these fields and none may be blank:

1. purpose;
2. lawful-basis status;
3. source;
4. recipient;
5. retention;
6. deletion mechanism;
7. access control;
8. prohibited use.

REQ-0019 additionally requires necessity, rights and safeguards to match actual reality. Therefore those attributes are mandatory in the implementation inventory even though ACC-0230 names the eight fields above.

**Fail-closed rule:** a proposed data element with no documented necessary purpose, no supportable lawful-basis status, an unknown recipient, undefined retention/deletion, excessive access, or an unbounded/prohibited use is **not permitted to be processed**. It must be removed from the design or remain `BLOCKED_NO_VALID_BASIS_OR_CONTRACT` until the missing condition is resolved under current authority.

This task does not establish final UK legal/data readiness. `RSK-0001` remains OPEN, and REQ-0018 continues to prohibit activation of a real England participant before the applicable legal/privacy/technical gate passes.

## 2. Non-negotiable privacy invariants

1. **No identifiable browsing history.** UseSafeWeb must not create or retain identifiable DNS-query, requested/visited-domain, URL, top-domain, browsing, search-term or child-activity history as product, analytics, support, dashboard or monetisation data.
2. **Persistent query/file logging stays off.** CON-0007 remains binding. Exceptional diagnostics are separate, explicitly necessary, time-boxed, access-controlled and deletion-verified.
3. **Identifiable per-client statistics stay off/excluded.** CON-0008 remains binding unless a later specifically justified and authorised exception exists; no browsing/top-domain product metric is permitted.
4. **Accountless and optional-account state are separate domains.** J0/J1 state is not silently linked, copied or promoted into an account/device history. Sign-in cannot extend anonymous retention.
5. **Protection evidence is separate from identity.** Account ownership, device ownership, dashboard presence, parent confirmation, profile presence or stored state never strengthens technical verification under TSK-0313.
6. **Deletion operations are truthful and separate.** Anonymous-state deletion, support-case deletion, account deletion, saved-device-record deletion, dashboard unlink/revoke and physical DNS/profile removal are distinct operations; completion of one must not be represented as completion of another.
7. **Minimum necessary access and recipients only.** Browser/client code receives only data required for its current function; administrative credentials, unrestricted AdGuard control, raw private service data and unnecessary identity never enter the browser.
8. **No hidden data resurrection.** Backup/restore, retry, reinstall, account return or service recovery must not resurrect expired/deleted anonymous state or restore a stale positive protection claim.

## 3. Lawful-basis status model — no invented legal completion

The data model must use one of these statuses for every personal-data element:

- `LI_CONDITIONAL` — Article 6(1)(f) legitimate interests is the current design candidate only where a documented purpose, necessity test and balancing assessment (with particular care for children’s interests) supports it. It is **not live-processing authority** until the current LIA/legal gate confirms the actual processing context.
- `CONTRACT_CONDITIONAL` — Article 6(1)(b) is a candidate only for data objectively necessary to provide an optional parent-requested contractual account/service function and only if the actual current terms/relationship support that basis. Otherwise processing is blocked or another valid basis must be established.
- `LEGAL_OBLIGATION_CONDITIONAL` — permitted only when a specific applicable legal obligation and its required data are actually identified and documented; never used as a generic fallback.
- `NOT_PERSONAL_OR_SYNTHETIC` — only where the record genuinely contains no personal identifier/linkage and cannot reasonably be related back through the system design.
- `BLOCKED_NO_VALID_BASIS_OR_CONTRACT` — not permitted to process until a current valid basis and all other NFR attributes are established.
- `PROHIBITED` — outside current product authority and must not be collected/derived/stored.

Consent must not be assumed merely because a parent participates, signs in, confirms setup or asks for help. A UI confirmation is not a lawful-basis shortcut and is not technical protection evidence.

Current official ICO guidance reviewed for this contract supports purpose/necessity/balancing for legitimate interests, extra care where children are affected, data minimisation, purpose limitation and justified storage limitation. Those general principles do **not** decide the final project-specific lawful basis or a fixed legal retention period; RSK-0001/INT-0006 remain controlling for that conclusion.

## 4. Current data-element NFR inventory

The table below is the minimum current design inventory. `None` means there is no external recipient beyond the current processing component; it does not authorize later disclosure. Any downstream field that is more granular than a row below inherits the row’s constraints and must receive its own inventory entry before processing.

| ID | Data element | Domain | Purpose / necessity | Lawful-basis status | Source | Recipient | Retention | Deletion mechanism | Access control | Rights / safeguards | Prohibited use |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D01 | Current screen/step and temporary routing selections | J0 browser/session | Render the active accountless journey without durable identity | LI_CONDITIONAL or NOT_PERSONAL_OR_SYNTHETIC according to actual value/linkability | Parent/browser interaction | Browser session only | Active browser/session only | Session destruction or explicit reset | Same-origin application/session | No durable server profile; minimise values | Cross-session profiling, marketing, identity inference |
| D02 | Temporary locally computed Protection Map state | J0 browser/session | Render truthful current state during active journey | LI_CONDITIONAL or NOT_PERSONAL_OR_SYNTHETIC according to actual linkability | Current setup/evidence state | Browser session only | Active session only | Session destruction/reset | Same-origin application/session | TSK-0313 evidence-strength rules | Treating cached state as technical verification or history |
| D03 | `journey_token` | J1 anonymous | Address an optional transient server record where architecture proves necessity | LI_CONDITIONAL | Server-generated random value | Accountless application only | Maximum 24h from creation, non-sliding; earlier deletion preferred | Completion/reset/exit/security/orphan trigger; synchronous or within 15m; TTL independently enforced | Server-side least privilege; full token excluded from logs | Opaque, no embedded identity, no reuse | Account/device join, fingerprinting, analytics identity, log exposure |
| D04 | `created_at` / `hard_expires_at` | J1 anonymous | Enforce deterministic expiry/deletion | LI_CONDITIONAL | Server clock | Accountless application/cleanup worker | Same lifetime as J1 | Deleted with J1 | Server-side least privilege | Purpose-limited timestamps | Behavioral timeline, retention extension |
| D05 | `locale` | J1 anonymous | Render correct language/RTL | LI_CONDITIONAL | Parent selection/client locale route | Accountless application/content router | Same lifetime as J1 | Deleted with J1 | Server-side journey scope | Not nationality, location or market-activation evidence | Profiling/geolocation/marketing inference |
| D06 | `device_family` / coarse `platform_version_band` | J1 anonymous | Route technically correct supported instructions | LI_CONDITIONAL | Parent/device routing input | Accountless application/instruction catalogue | Same lifetime as J1 | Deleted with J1 | Journey-scoped server/browser access | Coarse value only; no fingerprint unless separately approved | Hardware fingerprint, stable device identity, ad targeting |
| D07 | `phone_state`, `journey_step` | J1 anonymous | Route already-configured handling and resume current step | LI_CONDITIONAL | Parent interaction | Accountless application | Same lifetime as J1 | Deleted with J1 | Journey-scoped | Controlled enum; no event trail/free text | Behavioral history/clickstream/engagement profile |
| D08 | `native_safeguard_state` | J1 anonymous | Render Phone-step/Protection Map state | LI_CONDITIONAL | Parent confirmation and/or approved evidence | Accountless application | Same lifetime as J1 | Deleted with J1 | Journey-scoped | Parent confirmation remains distinct from system verification | Inflating confirmation into verified protection |
| D09 | `dns_method`, `baseline_protection_state` | J1 anonymous | Route encrypted-DNS setup and show truthful status | LI_CONDITIONAL | Parent selection + approved technical evidence | Accountless application/verifier | Same lifetime as J1 | Deleted with J1 | Journey-scoped; verifier/server only for technical evidence | No domains queried stored; TSK-0313 rules | DNS/query history, ClientID as identity/authorization, false universal claim |
| D10 | `service_category`, `service_safeguard_state` | J1 anonymous | Route at most the approved relevant service safeguard | LI_CONDITIONAL | Parent selection/current catalogue | Accountless application | Same lifetime as J1 | Deleted with J1 | Journey-scoped | Coarse category only; no service credentials/account ID | Service-account profiling/content/history |
| D11 | `protection_map_state` | J1 anonymous | Render current evidence-backed end state | LI_CONDITIONAL | Derived from approved evidence classes | Accountless application | Same lifetime as J1 | Deleted with J1 | Journey-scoped | Six-state TSK-0313 contract; evidence refs minimal | Cached state as permanent proof; browsing/activity derivation |
| D12 | `support_route_state` | J1 anonymous | Route current setup problem to self-service | LI_CONDITIONAL | Current journey/support route | Accountless application/self-service | Same lifetime as J1 | Deleted with J1 | Journey-scoped | Controlled category/status; no free-text payload | Support dossier, raw diagnostics, analytics profile |
| D13 | `completed_at` | J1 anonymous | Trigger prompt deletion after completion | LI_CONDITIONAL | Server/application state | Accountless application/cleanup worker | Until J1 deletion only | Delete J1 immediately after necessary response/artifact | Server-side least privilege | Timestamp is deletion trigger, not engagement metric | Long-term completion history linked to identity |
| D14 | Parent authentication/provider identity minimum | Optional parent account | Authenticate the parent and operate the explicitly optional account/session capability | CONTRACT_CONDITIONAL or LI_CONDITIONAL only after current legal/terms assessment confirms the actual basis | Approved identity provider / parent | Identity/session backend; minimum approved store | While account is active plus only specifically justified bounded lifecycle/security retention | Account deletion/revocation workflow plus provider/session revocation where supported | Server-side authenticated account scope; least privilege | Minimise fields; no child profile; provider tokens/secrets excluded from product records | Mandatory login for core value; analytics join to anonymous history; surveillance |
| D15 | Server-managed session metadata | Optional parent account | Securely maintain/revoke authenticated session | CONTRACT_CONDITIONAL or LI_CONDITIONAL subject to current basis assessment | Authentication/session service | Session backend | Session lifetime plus only bounded security/revocation evidence justified by downstream architecture | Expiry/logout/revocation/account deletion | Secure server-managed session; no browser localStorage auth token | HttpOnly/Secure/SameSite/CSRF requirements downstream | Persistent behavior tracking, cross-account access, marketing identity |
| D16 | Opaque internal parent/device ownership identifiers and minimal device metadata/settings | Parent-owned device | Authorize parent-owned device lifecycle/dashboard operations | CONTRACT_CONDITIONAL or LI_CONDITIONAL subject to current basis assessment | Parent action/application/approved adapter | Parent/device store; allowlisted server-side adapter | While the device relationship is active; any post-delete reconciliation retention must be separately bounded and content-free | Device revoke/remove/delete/replace; account deletion reconciliation | Ownership enforced server-side on every operation; ClientID is never authorization | Opaque IDs; minimum nickname/platform/settings/lifecycle facts only | Cross-parent access, child profile, browsing/activity history, broad AdGuard admin |
| D17 | AdGuard ClientID/configuration linkage needed for an owned device | DNS control-plane linkage | Provision/revoke the intended encrypted DNS client without exposing admin credentials | CONTRACT_CONDITIONAL or LI_CONDITIONAL subject to current basis assessment | Server-side adapter | Private AdGuard admin/control plane + minimum ownership mapping | Active configured-device lifecycle; remove/revoke/reconcile on device/account operation according to downstream contract | Allowlisted delete/revoke/reconciliation; physical device removal separately verified | Private server-side adapter; no browser admin secret; ClientID not authorization | Explicit no-querylog/no-identifiable-statistics controls | DNS history, unrestricted control proxy, using ClientID to bypass ownership |
| D18 | Minimal Protection Map metadata/evidence references for an authorised persistent device | Parent-owned device | Reproduce the displayed state without storing browsing/query data | CONTRACT_CONDITIONAL or LI_CONDITIONAL subject to current basis assessment | Approved evidence evaluator | Parent/device store + application | Only while needed for current device state; cached state must be re-evaluated before presentation | Device/account deletion/revoke; evidence expiry removes positive current claim | Parent ownership + least-privilege service access | Store refs/reason/scope/time/version/freshness, not raw DNS history | Stored state as self-validating verification; activity history |
| D19 | Instruction/catalogue/source/version metadata | Content/configuration | Deliver source-current supported guidance and review stale instructions | NOT_PERSONAL_OR_SYNTHETIC | Maintained product/content sources | Application/content system/QA | Version history per content governance; no user linkage | Supersession/retirement under content governance | Maintainer/CI read-write; user read-only | Source/version/review trigger required | User profiling or inferring protection from content delivery |
| D20 | Privacy-safe decision-linked raw event envelope and approved fields | Product measurement | Answer only approved journey/state/self-service/channel decisions | LI_CONDITIONAL for user-linked ephemeral raw events; NOT_PERSONAL_OR_SYNTHETIC for genuinely non-linkable synthetic/aggregate records | Application/system event | Approved analytics processing boundary only | Raw accountless event/session linkage maximum 24h; then deleted | TTL deletion after aggregation; session/account/device identifier excluded from aggregates | Allowlisted schema; analytics least privilege | TSK-0498 only; unknown fields rejected | Account/email/provider/device join, domains/URLs/DNS query, child activity, arbitrary text, fingerprinting |
| D21 | Non-linkable product aggregates | Product measurement | Reproduce approved aggregate decisions without user identity | NOT_PERSONAL_OR_SYNTHETIC only if genuinely non-linkable | Approved aggregation from D20 | Product/QA decision owners | Maximum 13 months under current TSK-0498 contract | Scheduled aggregate deletion at retention bound or earlier | Aggregate-only analytics access | No session/account/device/person identifier | Re-identification, journey reconstruction, indefinite retention |
| D22 | Synthetic reliability telemetry | Operations | Detect service/recovery failure without observing user browsing | NOT_PERSONAL_OR_SYNTHETIC | Synthetic probes/runbooks | SRE/Operations | Raw maximum 30 days; non-linkable aggregates maximum 13 months under TSK-0498 | Scheduled deletion | Operations least privilege | Fixed allowlisted component/error classes | User/client identity, DNS query/domain capture |
| D23 | Exceptional diagnostic record/ticket | Support/security exception | Resolve a specific issue only when lower-data diagnostics are insufficient | LI_CONDITIONAL or another specifically established current basis; otherwise BLOCKED | Explicit bounded diagnostic action | Named support/security operator/service only | Shortest justified incident-specific window; no default extension from journey/account life | End-of-window deletion with verification; ticket may retain only minimal content-free closure evidence if separately justified | Explicit approval where required; named least-privilege access; time-bounded | D0→D3 escalation; synthetic/config checks first | Product analytics, personalization, marketing, routine browsing/query capture |
| D24 | Minimal privacy-safe operational/security log metadata | Security/operations | Detect/diagnose service/security events and prove governed changes without user browsing history | LI_CONDITIONAL for personal identifiers only when necessary; otherwise NOT_PERSONAL_OR_SYNTHETIC | Server/application/infrastructure | Restricted operations/security | Purpose-specific bounded retention defined by downstream observability design; undefined retention means collection is blocked | Scheduled deletion and incident-specific cleanup | Restricted operator/service access | Redaction, bounded fields, no secrets; prefer synthetic/aggregate signals | DNS/domain history, raw tokens/secrets, user behavior analytics |
| D25 | Minimal deletion/revocation/reconciliation completion evidence | Lifecycle/privacy | Prove a deletion/revoke/reconcile operation completed without retaining deleted content | LI_CONDITIONAL, CONTRACT_CONDITIONAL or LEGAL_OBLIGATION_CONDITIONAL only as actually established | Lifecycle operation | Restricted application/privacy/security record | Only the shortest specifically justified accountability/reconciliation period; downstream implementation must set the exact bound before processing | Scheduled expiry/deletion independent of deleted content | Restricted service/privacy/security access | Opaque operation ID, time, result, scope class/version; no deleted payload | Tombstone as shadow profile; resurrecting deleted data; indefinite audit history by convenience |
| D26 | Backup/recovery metadata for irreplaceable approved state | Recovery/operations | Recover approved account/device/configuration state without restoring prohibited history | Basis follows the underlying allowed record; J1 is excluded by default | Approved backup system | Restricted recovery operators/services | Explicit backup retention set downstream before production; must honor deletion/reconciliation rules | Backup expiry + restore-time deletion reconciliation | Encrypted/restricted recovery access | J1 excluded by default; no query/history data; restore cannot recreate expired state | Backing up prohibited browsing/DNS history or using backup to evade deletion |
| D27 | Identifiable DNS/query/domain/URL/browsing/top-domain/child-activity data | Prohibited | No authorised purpose in current product | PROHIBITED | N/A | None | Zero — do not create/store | Reject/prevent collection; delete immediately if discovered; trigger incident/privacy review as applicable | No routine access because dataset must not exist | Detection controls and privacy drift tests | Any product, dashboard, analytics, support, monetisation, profiling or persistent diagnostic use |

## 5. Retention and deletion rules

### 5.1 Retention is a maximum, not a minimum

No record is retained merely because storage is cheap or an analytics tool defaults to a longer period. When the purpose is complete, deletion may occur earlier.

### 5.2 No invented universal legal TTL

Current privacy law/guidance does not provide one universal period for these data classes. Product-specific durations must be justified against purpose/necessity and current legal/operational reality. A missing exact retention bound blocks implementation of that persistent data element rather than authorizing indefinite retention.

The only exact current internal bounds carried forward here are already frozen by authoritative project contracts:

- J1 anonymous record: **maximum 24 hours from creation, non-sliding**;
- J1 early deletion: synchronous where possible, otherwise **within 15 minutes** of the deletion trigger;
- TSK-0498 accountless raw event/session linkage: **maximum 24 hours**;
- TSK-0498 non-linkable product aggregates: **maximum 13 months**;
- TSK-0498 synthetic reliability raw telemetry: **maximum 30 days**, aggregate maximum **13 months**;
- TSK-0498 cost measurement projection: **maximum 13 months**.

These are product/data-contract maxima, not claims that law mandates those durations.

### 5.3 Separate deletion operations

Implementation must expose and test separate state transitions for:

1. anonymous J0/J1 reset/expiry/delete;
2. support/diagnostic record deletion;
3. optional parent account deletion/session revocation;
4. saved device-record deletion;
5. device/dashboard unlink/revoke/replacement;
6. AdGuard client/control-plane reconciliation;
7. physical DNS/profile/configuration removal from the device;
8. telemetry raw-linkage expiry and aggregate expiry;
9. backup expiry/restore reconciliation.

The UI/API/evidence must identify which operation actually completed. Account deletion cannot claim physical DNS removal; physical DNS removal cannot claim account deletion; a dashboard unlink cannot claim a device stopped using a previously installed configuration until the relevant technical operation is separately verified.

## 6. Recipient and access NFR

1. Every recipient must be a named system role/component/provider class with a necessary purpose; `third parties`, `analytics`, or `internal` alone is not an acceptable inventory value.
2. Browser code receives no AdGuard administrative credential, provider secret, raw authentication token storage, unrestricted device/customer dataset or diagnostic history.
3. Optional parent/device records are accessible only through authenticated server-side ownership checks; modified IDs or ClientIDs cannot grant access.
4. Product analytics cannot join accountless raw event history to parent account/provider/device identity.
5. Support/security diagnostic access is exceptional, named, minimum and time-bounded.
6. Backups are restricted to recovery operators/services and must not broaden ordinary application access.
7. Any new processor/vendor/recipient or material geography change triggers privacy/legal/security reassessment before release under current change-control authority.

## 7. Prohibited-use catalogue

All allowed rows inherit these prohibitions unless a narrower row is even stricter:

- behavioral advertising or sale/monetisation of family data;
- child surveillance, child activity timelines or browsing reports;
- requested/visited domain, URL, query, search-term or top-domain history;
- cross-session fingerprinting or identity stitching;
- converting accountless journey/session identifiers into persistent account/device/customer history;
- using parent/account/device ownership as technical protection verification;
- unrestricted AdGuard administration or arbitrary `/control` proxying;
- indefinite retention for future unspecified use;
- free-text or raw diagnostic accumulation by default;
- copying production secrets, tokens, private keys, credentials or live session values into evidence/Git/analytics;
- using data collected for support/security/recovery as product analytics or marketing data without a separately authorised compatible purpose/basis contract.

## 8. Backup, restore and deletion reconciliation

- J0 is never server-backed up.
- J1 is excluded from durable backups by default under TSK-0229. A later exception requires documented necessity, access/encryption, maximum backup retention, restore-time expiry/deletion reconciliation, privacy approval and test evidence.
- Persistent optional-account/device backups may contain only approved current records and must implement deletion reconciliation so a restore cannot silently recreate a deleted active account/device relationship.
- A restored cached Protection Map value is not evidence. The current state must be re-evaluated from current evidence/freshness before display.
- Backup success alone is not deletion/recovery proof; later INT-0007 runtime inspection must verify actual storage, retention, restore and deletion behavior.

## 9. Rights and notice NFR

For every personal-data row, downstream implementation/legal work must bind the actual applicable rights/notice route to the final confirmed basis and processing reality. At minimum:

- the parent-facing notice must identify the actual purpose/data/recipient/retention/contact/rights relevant to the released function;
- account/device deletion and support/diagnostic deletion routes must be accessible at the point of need;
- an objection/rights request cannot require browsing history or excess identity to process;
- child-readable communication must not imply surveillance or complete safety;
- a lawful-basis/status change, recipient/vendor change, data-category change or retention extension reopens the affected privacy/legal review before release.

No final rights/legal-compliance conclusion is made by this L4 NFR; INT-0006 and RSK-0001 remain controlling.

## 10. Deterministic acceptance assertions

A compliant implementation/data inventory must prove all of the following:

1. Every processed data element has non-empty purpose, lawful-basis status, source, recipient, retention, deletion mechanism, access control and prohibited-use fields.
2. Any element with `BLOCKED_NO_VALID_BASIS_OR_CONTRACT` or `PROHIBITED` is rejected before processing/storage.
3. No schema/store/event/log/dashboard/support record contains identifiable DNS query, requested/visited domain, URL, browsing, top-domain or child-activity history.
4. Persistent identifiable query/file logging is off; identifiable per-client statistics are off/excluded unless a later current specifically justified exception exists.
5. J1 schema remains allowlisted, anonymous and non-linkable; its hard TTL is non-sliding and ≤24 hours.
6. J1 completion/reset/exit/security/orphan deletion is synchronous or completes within 15 minutes; expired tokens do not resolve.
7. Signing in/account creation cannot extend J1 or silently migrate J1 history into a persistent account/device record.
8. Account/device ownership, parent confirmation, ClientID or cached state cannot create `protected/verified`.
9. Optional account/device CRUD is server-side ownership authorised; ClientID is never authorization.
10. Account deletion, device-record deletion/unlink/revoke and physical DNS/profile removal are independently represented and tested.
11. TSK-0498 raw accountless linkage expires by 24h and retained aggregates contain no person/account/device/session linkage.
12. TSK-0498 retained aggregate/reliability/cost data expires by its currently approved maximum period and is deleted earlier when no longer necessary.
13. Exceptional diagnostics require explicit necessity, bounded fields/access/window and deletion verification; they cannot become analytics/history.
14. J1 is absent from durable backups by default; restore cannot resurrect expired/deleted J1.
15. Persistent backup restore reconciles current deletions/revocations before data is treated as active.
16. Operational/security logs contain no secrets or browsing/query/domain history and have a bounded purpose-specific retention before production.
17. Every new recipient/vendor/processor/data category/retention extension triggers the required privacy/legal/security impact review before release.
18. Actual runtime/config/schema/log/backup behavior is later inspected under INT-0007 and deviations from this inventory block release or are corrected; design documentation alone cannot prove runtime compliance.
19. RSK-0001 remains open until separately resolved; this task does not authorize real England participant processing.
20. Evidence for this task contains no real participant data, live journey tokens, account identity, ClientIDs, domains, browsing history, secrets or private keys.

## 11. Change-control triggers

The following are material privacy-contract changes and require impact analysis before implementation/release:

- adding a new personal-data category/field or persistent identifier;
- changing lawful basis/status;
- adding a recipient/vendor/subprocessor or material geography/transfer;
- extending retention or backup retention;
- enabling a new diagnostic/log/statistics field;
- introducing a J1-to-account transfer;
- changing optional-account identity/device persistence;
- enabling identifiable per-client statistics or query/file logging;
- adding browsing/domain/activity analytics or a dashboard history concept;
- changing deletion semantics or restoring data after deletion;
- changing an evidence rule so identity/configuration/confirmation could appear as technical verification.

Changes that conflict with CON-0007/CON-0008 or current prohibited-use rules fail closed and require the appropriate higher-authority owner decision rather than routine engineering approval.

## 12. Traceability and source currency

Direct task controls:

- **REQ-0018:** no real England participant before the applicable validation-readiness legal/privacy/technical gate.
- **REQ-0019:** purposes, data, lawful basis, necessity, recipients, retention, rights and safeguards must match actual reality.
- **CON-0007:** persistent identifiable query/file logging off; exceptional diagnostics time-boxed/deleted.
- **CON-0008:** identifiable per-client statistics off/excluded unless specifically justified; no browsing/top-domain product metric.
- **RSK-0001:** final UK representative/ICO/legal/data readiness remains unresolved; real-participant work remains blocked by the applicable gate.
- **INT-0006:** no unsupported legal conclusion may enter the product baseline.
- **INT-0007:** downstream runtime/config/log/schema evidence must match the inventory/notices/LIA/DPIA; deviations block release or are corrected.
- **ACC-0230 / VER-0230 / EVD-0230:** this document plus independent repository/acceptance validation is the L4 NFR evidence; it is not production/runtime legal-compliance evidence.

Current internal source contracts used:

- `TSK_0313_PROTECTION_MAP_STATE_AND_EVIDENCE_REQUIREMENTS_2026-09-01.md`;
- `TSK_0042_USER_SUPPORT_EXCEPTION_RECOVERY_REMOVAL_REQUIREMENTS_2026-09-01.md`;
- `TSK_0229_ACCOUNTLESS_JOURNEY_DATA_MODEL_EXPIRY_DELETION_NO_LINKAGE_2026-08-28.md`;
- `TSK_0229_POST_CR0006_ACCOUNTLESS_NO_LINKAGE_AMENDMENT_2026-08-30.md`;
- `TSK_0498_PRIVACY_SAFE_DECISION_LINKED_EVENT_CONTRACT_2026-09-01.md`;
- `Plans/Master/Registers/REQUIREMENTS.md`;
- `Plans/Master/Registers/CONSTRAINTS.md`;
- `Plans/Master/Registers/RISKS.md`;
- `Plans/Master/Registers/INTERFACES.md`;
- `Plans/Master/Registers/VERIFICATION_EVIDENCE_ACCEPTANCE.md`.

Current official-source principles reviewed on 2026-09-01: UK ICO guidance on legitimate interests (purpose/necessity/balancing and extra care for children), data minimisation, purpose limitation and storage limitation. These inform the NFR but do not resolve project-specific legal applicability, RSK-0001, Article-27/ICO matters or final LIA/DPIA approval.

## 13. ACC-0230 disposition candidate

ACC-0230 requires each data element to have purpose, lawful basis, source, recipient, retention, deletion mechanism, access control and prohibited use, with identifiable browsing history excluded.

This NFR defines those attributes for every currently authorised data class, fails closed where a final lawful basis/retention/recipient is not yet supportable, preserves exact current J1/telemetry retention contracts, separates anonymous/account/device/support/DNS/deletion domains, prohibits identifiable browsing/query/domain history, and explicitly leaves RSK-0001/current legal readiness unresolved.

**TSK-0230 is ready for independent acceptance verification; PASS is not claimed until ACC-0230/VER-0230/EVD-0230 and the full modular plan validator succeed and the durable runtime update is independently read back.**
