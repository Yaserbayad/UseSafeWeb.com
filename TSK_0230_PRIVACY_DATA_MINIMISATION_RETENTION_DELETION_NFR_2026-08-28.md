# TSK-0230 — Privacy, Data-Minimisation, Retention and Deletion NFRs

**Task:** TSK-0230 — Define privacy, data-minimisation, retention, and deletion NFRs  
**Acceptance:** ACC-0230  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** INTERNAL PROVISIONAL L4 PRIVACY/DATA NFR CONTRACT / IMPLEMENTATION OR PUBLIC RELEASE NOT AUTHORIZED  
**Date:** 2026-08-28  
**Authority:** REQ-0018/0019/0020/0021/0022/0023 + INT-0006/0007 + DEC-0042 + TSK-0229 + TSK-0042 + TSK-0313/0320 + current VALIDATION_READINESS_GATE + current actual DNS runtime evidence + DEC-0050/CR-0003  
**Verification state:** PASS candidate pending independent verification and runtime reconciliation.

## 1. Scope and legal-status boundary

This contract defines the minimum privacy/data non-functional requirements for the active **accountless-first provisional L4 product** and the already-running technical DNS service. It does not activate Experiment 1, create a legal-compliance attestation, approve the final LIA/DPIA, resolve the UK representative/ICO-fee branch, authorize public operation, or create a new persistent data store.

The current canonical `VALIDATION_READINESS_GATE.md` already records the project’s **provisional purpose-specific Article 6(1)(f) legitimate-interests position** for the narrow service/pilot processing, and records lawful-basis documentation as complete for the present planning baseline. It separately keeps final LIA/DPIA residual-risk approval, final participant-facing notice/contact release, and ICO/UK-representative resolution deferred/open. TSK-0230 preserves that exact distinction.

Therefore:

- `Article 6(1)(f) — legitimate interests (existing provisional project position)` in this document means **the current documented basis to design against**, not a fresh legal opinion or owner/legal approval;
- no row may silently substitute consent merely because children are involved;
- no row uses the newer distinct concept of a **recognised legitimate interest** unless a later current legal review proves a specified statutory condition applies;
- special-category/criminal-offence data is not authorized as routine product data by this contract;
- real-participant processing remains prohibited while LG-03/G-02 is DEFER/non-PASS.

`RSK-0002` remains OPEN: none of these NFRs prove representative-parent comprehension, preference, value, self-service success or acceptable support burden.

## 2. Current-source legal/privacy principles checked on 2026-08-28

The following current first-party sources were checked before freezing this contract:

1. ICO — Children’s Code, Annex C, lawful basis for processing:  
   https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/annex-c-lawful-basis-for-processing/
   - a valid lawful basis is required for each distinct processing activity;
   - the basis depends on the specific purpose/context;
   - legitimate interests may be considered for core child-related processing, but children’s interests receive particular weight and safeguards/necessity must be demonstrated;
   - consent is not automatically the correct/default basis for core service processing.

2. ICO — data minimisation:  
   https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/data-minimisation/
   - personal data must be adequate, relevant and limited to what is necessary for the stated purpose.

3. ICO — storage limitation:  
   https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/storage-limitation/
   - personal data must not be kept longer than necessary; retention must be justified by purpose rather than assumed from a generic statutory period.

4. Quad9 DNS service privacy policy, version 1.1 published 2026-06-24:  
   https://quad9.net/privacy/policy/
   - current provider policy governs the upstream DNS recipient; Quad9 states it does not retain information that correlates DNS queries with a specific end user/IP, while it may create non-user-correlatable aggregate DNS telemetry.

These sources are corroborative legal/recipient facts only. Canonical project decisions and the current validation gate remain the project’s authority for the existing UseSafeWeb legal position.

## 3. Single-authority rule

TSK-0230 does **not** become a second mutable data schema.

- **TSK-0229** owns the exact J0/J1 accountless journey field allowlist, TTL, deletion and no-linkage semantics.
- **TSK-0042** owns support/exception/recovery behavior and the diagnostic/safeguarding routing boundary.
- **TSK-0313/TSK-0320** own Protection Map application/state semantics.
- **VALIDATION_READINESS_GATE.md** and PKG-04 legal/privacy authority own the current lawful-basis/LIA/DPIA/gate disposition.
- **Actual runtime evidence** owns what the deployed DNS/Nginx/AdGuard path is currently doing.
- **TSK-0230** adds the privacy/NFR metadata required by ACC-0230: purpose, lawful basis, source, recipient, retention, deletion mechanism, access control and prohibited use for every allowed/conditional data element.

If a lower-level implementation later differs from this contract, `INT-0007` requires actual runtime/data-flow reality to be reconciled rather than editing the inventory to normalize an unapproved implementation.

## 4. Global NFR invariants

The following are mandatory across every data element/class:

1. **Necessity first:** no personal field or persistence exists merely because it is convenient to implement.
2. **Purpose bound:** one field/class must not silently acquire analytics, marketing, profiling or monetization purposes.
3. **Accountless by default:** no mandatory parent/child identity, login, account, dashboard or stable device/customer identifier.
4. **No browsing history:** identifiable browsing history, DNS-query history, visited-domain history, URLs/top-domain reports and equivalent activity history are prohibited as product, experiment, analytics, support or monetization datasets.
5. **No child profile:** no persistent behavioral, interest, inferred-risk, location, message/contact/photo or social-content profile.
6. **No cross-session stitching:** no cookie/IP/fingerprint/token scheme may link separate anonymous journeys into a household identity graph.
7. **Minimum recipients:** data goes only to the service/runtime or provider that is necessary for the defined purpose.
8. **Shortest defensible retention:** delete when the purpose ends; a maximum is not a target duration.
9. **Deletion is testable:** every persistent/temporary store must have a deterministic deletion mechanism and read-back/absence verification where technically applicable.
10. **No GitHub user data:** GitHub may contain schemas, aggregate/anonymised findings and non-sensitive technical evidence only — never live journey tokens, participant/contact records, raw diagnostic data, DNS/query history or safeguarding disclosure content.
11. **Least privilege:** human access is exceptional; runtime service identities get only the minimum access needed to operate.
12. **Change triggers:** adding a field, recipient, new purpose, longer retention, account identity, telemetry linkage, access logging, new region/vendor, or materially different diagnostic collection requires privacy/data-flow impact review before use.
13. **No legal inference from technical PASS:** a technical or L4 PASS cannot make LG-03/LG-05/LG-06 or final LIA/DPIA/legal approval PASS.

## 5. Accountless J0 session-only data classes

TSK-0229 keeps J0 in the browser/session and does not define a durable server record. The rows below are privacy metadata only; they do not alter its schema semantics.

| Data element/class | Purpose / necessity | Lawful basis position | Source | Recipient | Retention | Deletion mechanism | Access control | Prohibited use |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| J0 current screen/step | Render the immediate journey and next safe action | Article 6(1)(f) existing provisional position where this is personal data; otherwise not-applicable | Parent browser/session | Parent browser/UI runtime only | Active session only | Browser/session destruction; explicit reset/start-over clears immediately | Browser session; no routine human access | Cross-session analytics, profiling, identity reconstruction |
| J0 temporary routing selections | Choose current supported instructions without persistent identity | Article 6(1)(f) existing provisional position | Parent input/session | Parent browser/UI runtime | Active session only | Session destruction/reset | Browser session only | Marketing segmentation, nationality inference, stable user profile |
| J0 temporary presentation state | Preserve immediate UI state/error/help presentation | Article 6(1)(f) where personal; otherwise not-applicable | Product runtime/session | Parent browser/UI runtime | Active session only | Session destruction/reset | Browser session only | Behavioral analytics, session replay, engagement profile |
| J0 locally computed Protection Map state | Show current truthful Phone/Internet/Service state during the active journey | Article 6(1)(f) existing provisional position | Current journey evidence | Parent browser/UI runtime | Active session only unless an explicitly permitted J1 record is required | Session destruction/reset | Browser session only | Permanent protection-history profile, marketing or risk scoring |

## 6. J1 optional anonymous short-lived field matrix

J1 is permitted **only if later architecture proves a server-side anonymous record is necessary** for safe completion, verification, setup-artifact delivery or an explicitly supported short resume path. Its existence is not presumed by this L4 contract.

For all J1 rows below:

- lawful basis is the existing provisional **Article 6(1)(f) legitimate-interests** position for minimum accountless service delivery, subject to final LIA/DPIA/gate review before real participant/public processing;
- recipient is the minimum UseSafeWeb application runtime **only if J1 is implemented**; no third-party application-data processor is currently selected by this contract;
- default human access is **none**; only least-privileged service processes and tightly controlled incident administration may access a record when genuinely necessary;
- hard retention is **<=24 hours from creation, non-sliding**, with early deletion on completion/reset/exit and other TSK-0229 triggers; if asynchronous early cleanup is required, it must complete within the current **15-minute maximum**;
- no J1 field may be backed up into a durable product backup under the current baseline.

| J1 field | Purpose / necessity | Source | Recipient | Retention / deletion | Access control | Prohibited use |
| --- | --- | --- | --- | --- | --- | --- |
| `journey_token` | Address the transient anonymous record without identity | Product cryptographic generator | J1 runtime only | <=24h hard TTL; early-delete with record; never reuse | Service-only; full token must not be logged | Embed identity, cross-session stitching, analytics/user ID |
| `created_at` | Enforce deterministic TTL | Product runtime | J1 runtime | Same as record | Service-only | Behavioral timeline/profile |
| `hard_expires_at` | Enforce non-sliding expiry | Product runtime | J1 runtime | Same as record | Service-only | Extend automatically from activity |
| `locale` | Render correct language/RTL | Parent selection/device-independent UI choice | J1 runtime | Same as record | Service-only | Infer nationality/location/market eligibility |
| `device_family` | Route iPhone/Android/unsupported path | Parent selection | J1 runtime | Same as record | Service-only | Fingerprinting or persistent device registry |
| `platform_version_band` | Select current supported instruction band where necessary | Parent/device-reported coarse band | J1 runtime | Same as record | Service-only | Exact device fingerprint or build profiling |
| `phone_state` | Route new/already-used handling | Parent selection | J1 runtime | Same as record | Service-only | Purchase/history profiling |
| `journey_step` | Resume/render immediate path | Product state | J1 runtime | Same as record | Service-only | Clickstream/event-history reconstruction |
| `native_safeguard_state` | Render/route the current native-safeguard step truthfully | Parent confirmation/current controlled state | J1 runtime | Same as record | Service-only | Infer child behavior/risk or claim technical verification from confirmation |
| `dns_method` | Route exact supported DNS mechanism | Product routing state | J1 runtime | Same as record | Service-only | Unique AdGuard client/device identity |
| `baseline_protection_state` | Render current verified/unverified/failed/removed DNS state | Current verifier/product state | J1 runtime | Same as record | Service-only | Historical browsing/protection tracking across journeys |
| `service_category` | Route zero-or-one relevant service branch | Parent-declared relevance | J1 runtime | Same as record | Service-only | Service-account identity, popularity profiling, marketing segmentation |
| `service_safeguard_state` | Render current parent-confirmed/service guidance state | Parent confirmation/product state | J1 runtime | Same as record | Service-only | Claim system verification where only parent-confirmed |
| `protection_map_state` | Render current Phone/Internet/Service truth state | Derived from controlled current states | J1 runtime | Same as record | Service-only | Persistent safety score/profile |
| `support_route_state` | Route current setup/support problem to the right self-service path | Product/support state | J1 runtime | Same as record | Service-only; exceptional diagnostics remain separate | Free-text personal support dossier, raw diagnostics |
| `completed_at` | Trigger prompt early deletion after completion | Product runtime | J1 runtime | Delete promptly on completion; <=15min only if async cleanup required | Service-only | Long-term completion history/engagement analytics |

## 7. DNS/runtime data-element matrix — current actual service

The current production data-path evidence establishes:

**supported device -> UseSafeWeb Azure West Europe endpoint -> same-host Nginx/AdGuard -> Quad9 `dns10` recursive resolver -> response**.

Nginx access logging is explicitly off; AdGuard query/file logging and statistics are off; `dns.anonymize_client_ip=true`. This contract therefore distinguishes **transient processing needed to deliver DNS** from **persistent datasets**, which remain prohibited by default.

| Data element/class | Purpose / necessity | Lawful basis position | Source | Recipient | Retention | Deletion mechanism | Access control | Prohibited use |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DNS query name / DNS request payload in transit | Resolve/filter the requested domain and return the DNS answer; technically integral to the approved DNS service | Article 6(1)(f) existing provisional core-service position; necessity and child-interest balancing remain subject to final LIA/DPIA/gate review | Supported child device through encrypted resolver path | UseSafeWeb Nginx/AdGuard; then current upstream Quad9 `dns10` as necessary recursive recipient | **UseSafeWeb: no persistent query/file log or statistics dataset.** Transient request processing only. Quad9 provider processing is governed by its current policy and must be re-reviewed on provider/policy change | UseSafeWeb request memory/state expires with request/service processing; no retained history exists to delete. Provider-side lifecycle governed by Quad9 current policy | Resolver service processes only; no customer/admin browsing-history interface | Browsing history, support metric, product analytics, personalization, profiling, marketing, monetization, child-risk scoring |
| Source IP/network connection metadata in transit | Deliver encrypted network request/response and operate the endpoint | Article 6(1)(f) existing provisional minimum-service/security position where personal data is processed | Network connection | UseSafeWeb host/network stack and resolver process; upstream Quad9 receives the UseSafeWeb resolver connection rather than a UseSafeWeb customer identity record | Nginx access log OFF; AdGuard persistent query/statistics OFF; `dns.anonymize_client_ip=true`; no normal per-client history | No normal persistent record to delete; transient network/process state expires. Any exceptional diagnostic copy follows §9 | Network/service process only; no customer-visible history | Identity graph, device tracking, user analytics, marketing, behavioral attribution |
| Nginx critical error-log record, if generated | Diagnose critical service/security failures; not a normal request-history mechanism | Article 6(1)(f) existing provisional minimum service-security position **only to the extent a record contains personal data**; non-personal error metadata is outside personal-data lawful-basis scope | Nginx/service failure condition | Local production host error-log files; authorized operations/incident handling only | Current runtime: `crit` severity only, daily logrotate, `rotate 14`, compressed/delayed compression; no access log. Retention target is **no longer than the evidenced 14 daily rotations and shorter when no longer necessary** | System logrotate removes generations beyond policy; incident-specific copies are prohibited unless separately governed and must be deleted when the incident purpose ends | Target NFR <=`0640`, owner/service+admin group only. Current `/var/log/nginx/error.log` = `0640 www-data:adm`; current custom `/var/log/nginx/usesafeweb-doh-error.log` = `0644 root:root` and is an explicit pre-activation deviation in §11 | Product analytics, browsing/query history, user profiling, support-research dataset, marketing, indefinite incident archive |
| DNS/filter configuration and non-secret service health state | Operate/recover the service and prove approved configuration | Normally not end-user personal data as designed; if a future field embeds personal/user data, it becomes prohibited until separately reviewed | Governed configuration/runtime | Authorized infrastructure/operations and secret-safe Git evidence where applicable | Versioned governed configuration retained as operational evidence; no user/query data may be embedded | Governed configuration replacement/deletion; secret/runtime backups follow their own approved recovery policy | Restricted admin/service access; Git contains non-secret configuration/evidence only | Embedding client identity, query history, secrets or support/user records |

### Quad9 recipient rule

Quad9 remains the current upstream recipient only for the recursive DNS function. Current policy version 1.1 (2026-06-24) states that Quad9 does not retain information enabling DNS queries to be correlated with a specific end user/IP, while non-user-correlatable aggregate DNS telemetry may exist. UseSafeWeb does not convert that provider statement into a guarantee of permanent future behavior: **any material Quad9 policy/service/endpoint change triggers recipient/privacy reassessment before participant/public use**.

## 8. Ordinary support data

The active accountless baseline does **not** create a persistent general customer-support database.

- Immediate routing/help state stays inside J0/J1 `support_route_state` and follows the same expiry/deletion/no-linkage rules.
- A persistent ticketing/contact system is not authorized merely because TSK-0042 defines an issue taxonomy.
- If a future staffed/ticketing system is justified under EXC-0008 or another current trigger, its exact fields, lawful basis, recipients, retention, access and deletion must be approved **before collection**; TSK-0230 does not pre-authorize it.
- Repeated issue metrics may be aggregate/non-identifying only unless a separately approved measurement contract requires otherwise.

## 9. Exceptional diagnostic data — conditional incident-only class

Exceptional request-level diagnostics are **not** an ordinary product field/store. They exist only when the accepted exceptional-diagnostic procedure is invoked for a concrete incident after lower-data checks fail.

| Data element/class | Purpose / necessity | Lawful basis position | Source | Recipient | Retention | Deletion mechanism | Access control | Prohibited use |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Exact diagnostic field allowlist approved for one incident | Diagnose a specific unresolved technical/privacy/security fault that cannot be established with lower-data evidence | Existing Article 6(1)(f) service/security position may apply to necessary ordinary personal diagnostic data, subject to the incident necessity/balancing record. **Special-category/criminal-offence data is not authorized by this row; if encountered, stop and route for separate legal/safeguarding basis assessment.** | Exact affected technical path/parent only as approved | Approved incident responders and exact approved diagnostic storage only | Fixed UTC window from incident record; stop at resolution or approved end, whichever comes first | Delete dataset plus copies/exports; record deletion verification before closure | Named/restricted responders only; no broad support/team access | Analytics, training corpus, product history, browsing-history feature, profiling, marketing, reuse in unrelated incidents, GitHub raw data |

Ordinary support may not invoke this class merely because request-level logging is convenient.

## 10. Safeguarding disclosure/incident data — not a routine product element

UseSafeWeb does not solicit or store safeguarding disclosures as product data. If a disclosure/concern is received incidentally:

- ordinary product troubleshooting stops;
- the dedicated child-safety escalation procedure controls immediate handling;
- no standing product analytics/support lawful basis is asserted for retaining disclosure content;
- only the minimum facts necessary for the applicable emergency/safeguarding/legal route may be processed under the separately applicable lawful basis identified for that incident;
- any special-category/criminal-offence processing requires the corresponding current legal condition and is **not pre-authorized by TSK-0230**;
- disclosure content must not enter GitHub, ordinary support metrics, J0/J1 product history, marketing or analytics.

A non-identifying aggregate count that the safeguarding route was invoked may exist only if a later approved measurement/incident contract proves necessity and re-identification risk is controlled.

## 11. Current actual-runtime deviation register

### DVR-0230-01 — custom Nginx critical error-log file mode

Fresh privacy-safe runtime inspection on 2026-08-28 directly observed:

- `/var/log/nginx/error.log`: size `0`, mode `0640`, owner `www-data:adm`;
- `/var/log/nginx/usesafeweb-doh-error.log`: size `0`, mode `0644`, owner `root:root`;
- both are `crit`-severity error-log targets;
- Nginx access logging is explicitly off;
- logrotate covers `/var/log/nginx/*.log` daily with `rotate 14` and `create 0640 www-data adm`.

**Disposition:** the custom DoH error-log file’s current `0644` mode is broader than this contract’s least-privilege target (`<=0640`, service/admin only). The file is currently empty and real-participant/public processing remains unauthorized, so current evidence does **not** establish an actual participant-data exposure. However, this is a **known pre-activation implementation deviation** and must be remediated and reverified before any gate may rely on the error-log access-control NFR as implemented.

TSK-0230 PASS, if granted, means the **NFR is correctly defined and the deviation is truthfully registered**; it does not certify the current custom error-log permission as compliant.

## 12. Deferred Experiment-1/research data is outside the active product store

`EXPERIMENT_01_PARTICIPANT_RECORD_SCHEMA.md` remains a **pre-experiment template**, not an active data store. No real participant record may be created while the validation-readiness gate is DEFER/non-PASS.

If/when L3 is legitimately reactivated:

- only the approved pseudonymous participant fields may be collected;
- contact data stays separate from the metric record;
- contact details are deleted promptly after the 14-day follow-up and no later than the approved follow-up +30-day maximum;
- participant-level pseudonymous experiment metrics are aggregated/anonymised and deleted no later than the approved Experiment-close +90-day maximum;
- GitHub receives aggregate/anonymised findings only;
- identifiable DNS/domain history remains prohibited.

Those retention periods belong to the accepted Experiment-1 privacy/retention authority and are not imported into J0/J1 or public product data.

## 13. Explicit prohibited data elements/classes

The following have **no routine product lawful basis or authorized retention** under the active baseline and therefore must not be collected/stored as product state:

- child or parent name solely for product use;
- email/phone solely to complete the accountless journey;
- exact child DOB;
- school/home address/postcode or routine/precise location;
- device serial/IMEI/advertising ID/hardware fingerprint;
- Apple/Google/social usernames or credentials;
- messages, contacts, photos or social-content history;
- browsing history, URL history, DNS query history, visited-domain history, top-domain/activity reports;
- raw routine diagnostic logs;
- persistent parent/child/device profile;
- cross-session identity graph;
- behavioral advertising/marketing profile;
- payment/card data in the current provisional product/Experiment-1 path;
- unrestricted free-text support notes;
- persistent per-user allowlist/history/dashboard;
- inferred sensitive/behavioral child attributes from DNS or service-use data.

If a future owner-approved scope change genuinely requires any currently prohibited data class, the old prohibition does not silently disappear: a new purpose/necessity/lawful-basis/recipient/retention/access/deletion assessment and gate impact review is mandatory before collection.

## 14. Rights, transparency and no-linkage handling

Privacy rights must be supported without creating extra identity solely to make rights administration convenient.

- If transient J1 state exists and the user presents the valid token, the implementation may locate/delete the matching record within the already-authorized token scope.
- After J0/J1 deletion/expiry, the system must not reconstruct identity/history from IP, cookies, fingerprints or logs to answer a request.
- For normal DNS requests, the accepted design retains no UseSafeWeb per-user query-history dataset to retrieve.
- Any exceptional diagnostic dataset must record its own incident owner/location/window/deletion evidence so it can be controlled while it exists.
- Notices must describe specific verified practice; generic “no logs” statements are prohibited because critical operational error logging exists even though access/query logging and AdGuard query history are off.
- Child/parent transparency must explain the service’s DNS-processing purpose and limits without implying full online-safety coverage.

## 15. Implementation/verification requirements

A later implementation or privacy gate must be able to prove at least:

1. no persistent field exists outside the authorized data contract without an approved change;
2. J0 is session-only;
3. J1, if implemented, rejects fields outside TSK-0229 and obeys <=24h non-sliding TTL;
4. J1 early deletion completes synchronously or within the approved <=15-minute async maximum;
5. deleted/expired journey state cannot be re-linked through IP/cookies/fingerprints/account identity;
6. normal DNS query/file logging remains off;
7. Nginx access logging remains off unless a separately governed necessity case exists;
8. AdGuard statistics remain off and `dns.anonymize_client_ip` remains enabled;
9. normal DNS request/query data cannot be queried as a user history;
10. every persistent log/store has a stated purpose, retention and deletion control;
11. Nginx critical error logs follow bounded rotation and least-privilege permissions;
12. DVR-0230-01 is remediated/read-back verified before participant/public reliance;
13. no raw user/diagnostic/query/safeguarding data is committed to GitHub;
14. exceptional diagnostics cannot start without incident-specific necessity/scope/window/access/approval/deletion controls;
15. exceptional diagnostic data is deleted with recorded verification;
16. no persistent customer-support store exists unless separately authorized;
17. no browsing/query/activity-history analytics event exists;
18. no telemetry event contains a stable parent/child/device identity in the accountless baseline;
19. provider/region/data-path changes trigger INT-0006/INT-0007 privacy reassessment;
20. actual runtime/config/storage inspection matches this inventory before the relevant activation/release gate.

## 16. Revalidation/change triggers

Reopen affected TSK-0230 requirements and downstream evidence when any of the following occurs:

- a new product/application field or event is proposed;
- J1 is actually implemented or its schema/TTL changes;
- an account/auth/dashboard trigger is activated;
- Nginx access logging is enabled;
- error-log severity/path/permissions/retention changes;
- AdGuard query logging/file logging/statistics/anonymisation changes;
- new analytics/support/ticketing/observability vendor receives user-related data;
- DNS upstream/provider/privacy policy changes;
- data region/hosting/application topology changes;
- a new market is officially activated;
- real Experiment-1/L3 processing is reactivated;
- a material incident reveals unplanned persistence/recipient/access;
- current ICO/UK/EU legal guidance materially changes the documented basis or safeguards;
- real-user evidence contradicts the data-minimisation/usability assumptions.

## 17. ACC-0230 traceability

ACC-0230 requires:

> Each data element has purpose, lawful basis, source, recipient, retention, deletion mechanism, access control, and prohibited use; identifiable browsing history remains excluded.

Coverage:

- §§5–6 map every currently permitted accountless J0/J1 element/class.
- §7 maps every current personal-data-relevant DNS/runtime class and its actual recipient/retention/access boundary.
- §9 maps the only approved exceptional diagnostic data class.
- §10 explicitly refuses to treat safeguarding disclosure content as routine product data with a pre-baked basis.
- §11 records the current error-log permission deviation rather than falsely certifying compliance.
- §12 separates deferred research data from active product data.
- §13 gives prohibited classes no routine authorization, including identifiable browsing/DNS/domain history.
- §§14–16 make deletion, rights/transparency, verification and change triggers testable.

**TSK-0230 result: PASS candidate for the provisional internal L4 NFR-definition acceptance only, subject to independent verification, GitHub read-back and runtime reconciliation. DVR-0230-01 remains a pre-activation implementation deviation and final legal/participant gates remain non-PASS.**
