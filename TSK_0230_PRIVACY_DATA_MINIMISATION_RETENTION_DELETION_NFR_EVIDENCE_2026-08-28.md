# TSK-0230 — Privacy/data NFR verification evidence

**Task:** TSK-0230 — Define privacy, data-minimisation, retention, and deletion NFRs  
**Acceptance:** ACC-0230  
**Verification:** VER-0230 independent guarded privacy/data/actual-runtime audit  
**Evidence:** EVD-0230  
**Date:** 2026-08-28  
**Result:** PASS candidate pending authoritative runtime reconciliation/read-back

## 1. Exact evidence index

- NFR contract: `TSK_0230_PRIVACY_DATA_MINIMISATION_RETENTION_DELETION_NFR_2026-08-28.md`
- NFR contract blob: `011caaa84dd3dec13bb608be30b15ec92a24f19e`
- NFR contract creation commit: `a2844ec2def584c13142b61eba8393793f5ca4f6`
- Runtime data-footprint inspection: `TSK_0230_RUNTIME_DATA_FOOTPRINT_INSPECTION_2026-08-28.md`
- Runtime inspection blob: `48d38b95f43e186624041d6c511412272f93305f`
- Accepted runtime inspection run: `33193644558` / job `98925167227` — SUCCESS.
- WBS blob: `dce5b829c4d447eac180ae1e896e0019292cf971`
- Current validation-readiness gate blob: `1aef1c806a3fa4abcaf9e2feffa0ea093ec10ff9`
- TSK-0229 accountless data contract blob: `3fa48b11b6c7704ecc3748bcd865f77aa54f5605`
- TSK-0042 support/recovery contract blob: `bf9e1ece69b5ccfc38c1cb44d69de6545b7865dc`
- TSK-0042 independent evidence blob: `e8698c39c13eb8d346ac195d60ff9d2d4288d2f6`
- TSK-0313 Protection Map requirements blob: `521c9cc5073aa289281acade12a66a9e979e197d`
- TSK-0320 protection-state contract blob: `1146f7622f434590dde1253d11f14fb6a87e19de`
- TSK-0206 client-IP anonymisation evidence blob: `5905136433d930c2325a877e10a45e8540ac6a80`
- TSK-0207 privacy-persistence evidence blob: `1c16db063e2e84d300b547075721d33c2e020e32`
- TSK-0428 Azure/data-path evidence blob: `bbcd27772f8a9cad8248c48e9290b52baf71056f`
- TSK-0512 filtering regression evidence blob: `cc21f4574a2ca7e721a7da961baef727350af1d3`
- Pilot privacy notice blob: `331f263388dfacfa73b6e9e556277d4230864ce8`
- Retention/deletion checklist blob: `5c2d6edbfbabe9ed0fb9c309e7afca8c96fa9c9f`

## 2. Current first-party source verification

Current authoritative source checks were performed on 2026-08-28 before the contract was frozen.

### ICO — Children’s Code Annex C, lawful basis

Source:  
https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/annex-c-lawful-basis-for-processing/

Current guidance states that a valid lawful basis is required for each distinct processing activity and must be selected from the actual purpose/context. For core processing, legitimate interests may be considered, with particular weight given to children’s interests and the need for safeguards; consent is not automatically the appropriate basis for processing integral to the core service.

**Audit implication:** the contract correctly preserves the project’s already-documented purpose-specific Article 6(1)(f) position and explicitly refuses to treat it as final LIA/DPIA/legal approval. It does not invent a consent requirement or incorrectly relabel ordinary legitimate interests as the separate recognised-legitimate-interests basis.

### ICO — data minimisation

Source:  
https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/data-minimisation/

Current guidance requires personal data to be adequate, relevant and limited to what is necessary for the stated purpose.

**Audit implication:** the contract’s field allowlist, no-linkage rule, no-history rule, session-first model, transient DNS processing and incident-only diagnostic class are aligned with the current principle.

### ICO — storage limitation

Source:  
https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/storage-limitation/

Current guidance requires controllers to justify retention from purpose and not keep personal data longer than necessary; the UK GDPR does not provide one generic retention period for all data.

**Audit implication:** the contract reuses the purpose-specific TSK-0229 J0/J1 limits, incident-specific diagnostic window, and actual bounded operational-log rotation instead of inventing a universal duration.

### Quad9 DNS privacy policy

Source:  
https://quad9.net/privacy/policy/

Current policy is version 1.1, published 2026-06-24. Quad9 states that it does not retain data that correlates DNS queries to specific end users/IP addresses; non-user-correlatable aggregate DNS telemetry may exist.

**Audit implication:** the contract correctly lists Quad9 as the current external recursive-DNS recipient and treats provider policy/endpoint change as a reassessment trigger instead of asserting permanent provider behavior.

## 3. Authority and eligibility audit

The guarded TSK-0230 selection directly asserted the current WBS row before runtime selection:

- Lifecycle: `L4`;
- Priority: `MEDIUM`;
- AI capability: `A3`;
- Action authority: `AUTO_ALLOWED`;
- hard dependencies: exactly `TSK-0313; TSK-0042`;
- ACC-0230 requires each data element to have purpose, lawful basis, source, recipient, retention, deletion mechanism, access control and prohibited use, with identifiable browsing history excluded.

Both direct predecessors were current PASS before selection. TSK-0187 remained real-behavior-bound and TSK-0140 remained owner-review-bound. TSK-0230 is therefore eligible as an internal provisional NFR-definition task under CR-0003.

## 4. Lawful-basis/gate separation audit

The current canonical validation-readiness gate records the project’s provisional purpose-specific Article 6(1)(f) legitimate-interests position and separately keeps final LIA/DPIA residual-risk approval, participant notice/contact release, and ICO/UK-representative matters unresolved/deferred.

The TSK-0230 contract preserves that distinction in §§1–2 and throughout the data matrix. It explicitly states that an L4/technical PASS cannot make the legal/participant gate PASS.

**Result: PASS.** No unsupported legal conclusion or gate bypass is introduced.

## 5. ACC-0230 element completeness audit

ACC-0230 requires, for **each allowed/conditional data element**, all of:

1. purpose;
2. lawful basis;
3. source;
4. recipient;
5. retention;
6. deletion mechanism;
7. access control;
8. prohibited use;
9. identifiable browsing history excluded.

### J0 data classes

Section 5 contains four J0 data classes. Each row explicitly provides all eight required metadata dimensions. J0 is session-only and does not create a durable server-side record.

**Result: PASS.**

### J1 field allowlist

Section 6 maps all 16 fields owned by TSK-0229:

`journey_token`, `created_at`, `hard_expires_at`, `locale`, `device_family`, `platform_version_band`, `phone_state`, `journey_step`, `native_safeguard_state`, `dns_method`, `baseline_protection_state`, `service_category`, `service_safeguard_state`, `protection_map_state`, `support_route_state`, `completed_at`.

A binding preamble applies the lawful-basis position, recipient boundary, human-access default, <=24h non-sliding TTL, early-deletion/<=15-minute async-cleanup limit and backup exclusion to **every row**. Each individual row then supplies the field-specific purpose, source, recipient, retention/deletion reference, access and prohibited use.

This reuses TSK-0229 rather than creating a second mutable schema.

**Result: PASS.**

### Current DNS/runtime data classes

Section 7 maps:

- DNS query/request payload in transit;
- source IP/network connection metadata in transit;
- Nginx critical error-log records, if generated;
- non-secret DNS/filter configuration and service-health state.

Every row supplies the required ACC-0230 metadata. Query and source-IP rows are explicitly transient on UseSafeWeb under the current normal path, not persistent user-history datasets.

**Result: PASS.**

### Ordinary support

Section 8 correctly establishes that there is **no currently authorized persistent general support database**. Immediate support state is already represented by J0/J1 `support_route_state`. A future ticket/contact store requires a separate pre-collection data contract.

**Result: PASS — no missing current allowed data element is silently invented.**

### Exceptional diagnostics

Section 9 maps the conditional incident-only diagnostic field allowlist to purpose, existing provisional lawful-basis position where applicable, source, exact incident recipients, fixed incident retention/deletion, restricted access and prohibited reuse. It explicitly refuses to pre-authorize special-category/criminal-offence processing.

**Result: PASS.**

### Safeguarding disclosure

Section 10 correctly classifies safeguarding disclosure content as **not a routine product data element**. It does not manufacture a standing product lawful basis; instead, it requires the dedicated incident/safeguarding route to establish any necessary incident-specific lawful basis/condition. This is more accurate than inventing a generic Article 6/9 basis for unknown future facts.

**Result: PASS — prohibited/incident-only data is not falsely represented as ordinary allowed product data.**

## 6. Actual-runtime reconciliation audit

The accepted read-only production inspection run `33193644558` / job `98925167227` directly established without reading any request/log record:

- target fingerprint matches accepted `adguardvm`;
- Nginx `access_log off;`;
- Nginx error logs are `crit` severity only;
- `/var/log/nginx/error.log`: size 0, mode `0640`, owner `www-data:adm`;
- `/var/log/nginx/usesafeweb-doh-error.log`: size 0, mode `0644`, owner `root:root`;
- `/etc/logrotate.d/nginx` rotates `/var/log/nginx/*.log` daily, `rotate 14`, compression/delaycompress, and creates `0640 www-data adm` files;
- AdGuard query logging disabled;
- AdGuard file query logging disabled;
- AdGuard statistics disabled;
- persisted `dns.anonymize_client_ip=true`.

The contract reflects these facts exactly and does not claim that the custom error-log file’s current `0644` permission satisfies the least-privilege target.

### DVR-0230-01 disposition

The custom critical DoH error log is currently empty but mode `0644 root:root`, broader than the NFR target `<=0640`, service/admin only.

The contract records this as an explicit **pre-activation implementation deviation**, with required remediation/read-back verification before participant/public reliance on the access-control NFR. Because TSK-0230 is a definition task, real participant/public processing remains unauthorized, and no current participant data is evidenced in that zero-byte file, the deviation does not invalidate completion of ACC-0230’s NFR-definition requirement.

It **does** remain a current implementation gap and must not be described as compliant implementation evidence.

**Result: PASS for NFR definition / deviation truthfulness; implementation deviation remains OPEN.**

## 7. Browsing-history exclusion audit

The contract prohibits identifiable browsing history, DNS-query history, visited-domain history, URL/top-domain activity reports and equivalent datasets in:

- global invariants;
- DNS runtime processing;
- ordinary support;
- exceptional diagnostics reuse;
- explicit prohibited classes;
- implementation verification assertions.

This is consistent with REQ-0021, TSK-0229, TSK-0207 and current AdGuard/Nginx runtime evidence.

**Result: PASS.**

## 8. Retention/deletion audit

The contract does not invent a single universal retention period. It correctly binds retention to purpose and existing authoritative controls:

- J0: active session only;
- J1: <=24h non-sliding hard TTL, early delete on completion/reset/exit, <=15-minute async-cleanup maximum where required;
- normal DNS query/source-IP history: no persistent UseSafeWeb dataset under the accepted normal runtime;
- critical Nginx error logs: no longer than the current 14 daily rotations and shorter when no longer necessary;
- exceptional diagnostics: exact incident window, delete at resolution/end and verify deletion;
- deferred Experiment-1 contact/participant records: remain controlled by their own existing Experiment/privacy retention authority and are not imported into product state.

**Result: PASS.**

## 9. Rights/transparency/change-control audit

Sections 14–16 require privacy rights to be supported without creating extra identity/linkage, prohibit generic inaccurate “no logs” claims, and require reassessment on new fields, recipients, logging, providers, regions, accounts, analytics, diagnostics, markets or real-participant activation.

This satisfies the INT-0006/INT-0007 requirement that product controls follow actual data-flow reality and current legal/privacy authority.

**Result: PASS.**

## 10. Verification disposition

**VER-0230 independent guarded audit result: PASS for ACC-0230’s provisional internal L4 NFR-definition scope.**

The read-back contract at blob `011caaa84dd3dec13bb608be30b15ec92a24f19e` satisfies every ACC-0230 metadata dimension for every currently allowed or conditional data element/class and explicitly excludes identifiable browsing history.

The following remain non-PASS/open and are **not** converted by this result:

- `DVR-0230-01` custom Nginx error-log file permission remediation;
- final LIA/DPIA residual-risk approval;
- final participant notice/contact release;
- ICO/UK-representative deferred branch;
- real-participant activation and L3 behavioral evidence (`RSK-0002`);
- LG-03/LG-05/LG-06;
- implementation/build, payment, publication and launch.

**Runtime may move TSK-0230 to PASS only after this evidence file is persisted/read back and the reconciliation mutation verifies the exact contract/evidence/runtime/WBS preconditions.**
