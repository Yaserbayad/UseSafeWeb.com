# TSK-0484 — Security and Abuse-Resistance NFRs

**Task:** TSK-0484 — Define security and abuse-resistance NFRs  
**Acceptance:** ACC-0484  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** INTERNAL PROVISIONAL L4 SECURITY NFR CONTRACT / IMPLEMENTATION OR RELEASE NOT AUTHORIZED  
**Date:** 2026-08-28  
**Authority:** REQ-0055/0056 + CON-0009/0023/0028 + INT-0015 + TSK-0230 + current risk register + TSK-0483/0437/0201/0442/0443/0430/0431 direct evidence + DEC-0050/CR-0003  
**Verification state:** PASS candidate pending independent verification and runtime reconciliation.

## 1. Scope and security-state boundary

This contract defines measurable security requirements for the current UseSafeWeb technical DNS service and the future accountless web/application surface. It does **not** claim that the future web application has been built or security-tested, does not authorize public release, does not activate accounts/authentication, and does not turn historical security evidence into proof for a materially changed exposure path.

Security is split into two distinct threat domains:

1. **Public resolver abuse / availability / infrastructure integrity** — hostile traffic, amplification, saturation, public-path misuse, endpoint exhaustion, upstream failure and cost/availability abuse.
2. **User-data / administrative / application / supply-chain security** — query/log disclosure, transient-state theft or linkage, secret/admin compromise, workflow/runner compromise, dependency/code vulnerabilities, application injection/XSS/SSRF, recovery-integrity failure and unsafe diagnostics.

A control that protects one domain cannot be cited as proof for the other. For example, DNS rate limiting does not prove data minimisation, and query logging being off does not prove the public endpoint resists resource exhaustion.

`RSK-0002` remains OPEN; these NFRs are security design requirements, not representative-parent validation.

## 2. Current first-party security references checked on 2026-08-28

The following current primary sources were checked as external security references:

1. OWASP Application Security Verification Standard (ASVS), current stable **5.0.0**:  
   https://owasp.org/www-project-application-security-verification-standard/  
   ASVS provides a current basis for testable web-application technical security requirements and verification.

2. OWASP Input Validation Cheat Sheet:  
   https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html  
   Untrusted input must be validated at the earliest trust boundary for allowed type/format/range/length rather than trusted because it came from a client UI.

3. OWASP Cross-Site Scripting Prevention Cheat Sheet:  
   https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html  
   Untrusted values rendered to a browser must remain data through contextual output encoding/framework escaping rather than executable markup/script.

4. OWASP Server-Side Request Forgery Prevention Cheat Sheet:  
   https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html  
   Server-side URL/network destinations influenced by untrusted input require strict allowlisting/validation and protection against internal/private/redirect/rebinding paths.

5. AdGuard Home official current Configuration reference:  
   https://github.com/AdguardTeam/AdGuardHome/wiki/Configuration  
   Current documentation identifies `ratelimit`, IPv4/IPv6 rate-limit subnet aggregation, `ratelimit_whitelist`, and `refuse_any` as anti-DDoS/anti-amplification controls.

These references supplement the project’s direct target evidence. They do not authorize adding generic controls that conflict with the accountless/minimum product or frozen architecture.

## 3. Current assets and trust boundaries

### Security assets

| Asset | Why it matters |
| --- | --- |
| DNS service availability | Loss of availability can remove expected baseline protection or prevent verification/removal support. |
| Resolver/filter configuration integrity | Unauthorized changes can weaken filtering, redirect traffic, enable logging or break service. |
| DNS request confidentiality/minimisation | Query names and network identifiers can expose sensitive browsing intent if unnecessarily retained/disclosed. |
| Protection-state integrity | A false `Verified` state can create unsafe reliance even when the network path is compromised or uncertain. |
| AdGuard admin credential/control path | Compromise gives control of DNS/filter/privacy settings. |
| TLS private key/domain/DNS identity | Compromise can impersonate or redirect the encrypted resolver. |
| GitHub repository/workflow authority | Production changes and governance evidence depend on trusted code/workflow history. |
| Root-capable self-hosted runner | Compromise can become host/root compromise because the runner has non-interactive sudo. |
| Recovery backup/restore material | Compromise can expose configuration/secrets or restore malicious/stale state. |
| Future J1 journey token/state | If implemented, token theft/linkage could expose transient product state or defeat accountless privacy. |
| Future application source/dependencies | Vulnerable/malicious code can compromise browser, server, state or infrastructure. |
| Exceptional diagnostic data | Temporary request-level data can become an unintended browsing-history leak if over-collected or retained. |

### Trust boundaries

| Boundary | Current/future status | Untrusted side -> trusted side |
| --- | --- | --- |
| TB-01 Public encrypted DNS ingress | Current | Internet -> Nginx DoH 443 / DoT 853 |
| TB-02 Resolver proxy boundary | Current | Nginx -> loopback-only AdGuard DNS service |
| TB-03 Upstream recursive boundary | Current | AdGuard -> frozen Quad9 `dns10` DoH upstream |
| TB-04 Admin boundary | Current | Governed local workflow/root path -> loopback AdGuard admin API 3000 |
| TB-05 GitHub/runner boundary | Current | GitHub trusted repository/workflow -> root-capable production runner |
| TB-06 Secret/key/backup boundary | Current | Authorized owner/ops -> root-only credentials, TLS keys, encrypted backup material |
| TB-07 Accountless browser/application boundary | Future L6 build only | Internet browser -> future web/app VM/API |
| TB-08 J1 transient state boundary | Conditional/future | Browser token -> optional <=24h anonymous application state |
| TB-09 Exceptional diagnostic boundary | Conditional incident only | Affected request/path -> temporary approved diagnostic store/responders |
| TB-10 Recovery boundary | Current capability | Approved backup/repository artifacts -> fresh/recovery host |

If a new public API, account/authentication system, upload, webhook, third-party analytics, AI feature or persistent customer datastore is later introduced, it creates a new trust boundary and **reopens TSK-0484** before implementation/release.

## 4. Threat catalogue — STRIDE + abuse cases

| Threat ID | Domain | STRIDE / abuse case | Asset/boundary | Current evidence position |
| --- | --- | --- | --- | --- |
| THR-RES-01 | Resolver abuse | DoS: high-rate DoH/DoT traffic exhausts resolver/Nginx/CPU/memory/connections | TB-01/02, availability | Engine-level rate control proven historically; current public encrypted ingress not yet directly abuse-tested after Nginx exposure. |
| THR-RES-02 | Resolver abuse | Reflection/amplification or accidental public plain-DNS exposure | TB-01/02 | `refuse_any=true` and old UDP amplification test proven; current UFW/plain 53 non-public directly proven after TLS ingress. |
| THR-RES-03 | Resolver abuse | Endpoint/path/method abuse of DoH virtual host or accidental public admin route | TB-01/04 | `/` and `/control/status` return 404 publicly; admin remains loopback/authenticated. Broader malformed/method/size cases remain a later verification requirement. |
| THR-RES-04 | Resolver abuse | Malformed/oversized DNS/HTTP/TLS inputs consume disproportionate resources or trigger parser defects | TB-01/02 | NFR required; no current comprehensive malformed-input/fuzz acceptance is claimed. |
| THR-RES-05 | Resolver abuse | Upstream failure/retry storm/cost exhaustion creates cascading outage | TB-03 | Quad9 exact upstream and recovery/failure planning exist; public-load behavior remains to be tested. |
| THR-TLS-01 | Resolver identity | Spoofing/tampering via invalid/expired/misissued certificate or DNS/domain change | TB-01/06 | Current certificate acceptance, renewal dry-run, expiry monitor and public DNS checks are proven. |
| THR-ADM-01 | Admin | Spoofing/elevation: public/admin auth bypass or exposed admin surface | TB-04 | Admin 127.0.0.1:3000 only; authenticated 200/unauthenticated 401 proven; public control path 404. |
| THR-ADM-02 | Admin/secrets | Information disclosure: credential/private-key/backup secret reaches Git/log/process/output | TB-04/06 | Root credential 0600, key permissions, secret-safe Git/config and encrypted backup evidence exist. |
| THR-CI-01 | CI/runner | Elevation/tampering: malicious/untrusted workflow/code runs on root-capable self-hosted runner | TB-05 | Trusted-main execution model exists; no evidence of compromise. NFR must forbid untrusted fork/PR code on production runner. |
| THR-CI-02 | CI/runner | Information disclosure/elevation: repository write token persisted on root-capable production runner | TB-05 | Current TSK-0230 evidence workflow uses `contents: write` + `persist-credentials: true`; no compromise is evidenced, but this is broader than preferred least-privilege separation and is registered as DVR-0484-01. |
| THR-SC-01 | Supply chain | Tampering: compromised dependency/package/install script/toolchain enters future web release | TB-07/05 | Future web not built; requirements only. Host package patch state is currently proven. |
| THR-WEB-01 | Application | Tampering/XSS/injection via untrusted form/query/body/route input | TB-07 | Future application only; no implementation claim. |
| THR-WEB-02 | Application | SSRF via server-side fetch of a user-controlled URL/hostname | TB-07/03/host network | Future application only; default product does not require arbitrary URL fetch. |
| THR-WEB-03 | Application | Information disclosure through verbose errors, unsafe client storage, missing browser security controls | TB-07/08 | Future application only. |
| THR-J1-01 | Transient data | Spoofing/disclosure/linkage through guessable/reused/leaked journey token | TB-08 | J1 not currently implemented; TSK-0229 supplies schema/TTL/no-linkage baseline. |
| THR-DATA-01 | User data | Information disclosure/privacy drift: query/access/statistics/history logging enabled | TB-01/02/09 | Fresh evidence: Nginx access log off; AdGuard query/file logs/statistics off; anonymisation on. |
| THR-DATA-02 | User data | Information disclosure: operational error logs too broadly readable/retained | TB-01/06 | Critical-only + rotate 14 proven; custom DoH error log currently mode 0644 — DVR-0230-01 remains open. |
| THR-DATA-03 | User data | Over-collection/retention of exceptional diagnostics or safeguarding content | TB-09 | Dedicated necessity/approval/time-box/deletion procedures exist; no routine collection authorized. |
| THR-REC-01 | Recovery | Tampering/disclosure: malicious/stale/unencrypted recovery artifact restores bad state or exposes secrets | TB-10/06 | Encrypted config backup and clean recovery drill are proven; current recovery identity/evidence chain exists. |
| THR-STATE-01 | Product safety | Tampering/repudiation: protection state claims success without current evidence | TB-07/08 + DNS | TSK-0313/0320 define evidence-backed states; future implementation must enforce them server/UI side. |

## 5. Public resolver abuse and availability NFRs

These controls are intentionally separate from data-security controls.

| NFR | Threats | Requirement | Measurable verification / PASS condition | Current evidence status |
| --- | --- | --- | --- | --- |
| SEC-RES-01 | THR-RES-01 | Public encrypted DNS must have an effective bounded rate/concurrency control at or before the resource being protected. Current AdGuard engine baseline remains `ratelimit=20`, IPv4 `/24`, IPv6 `/56`, zero whitelist unless a later evidence-backed change is approved. | Fresh external/boundary test on **current DoH 443 and DoT 853 paths**: low-rate control traffic succeeds; bounded burst is measurably throttled/limited; service remains healthy; no unbounded connection/resource growth. Exact observed public-path effective limiter must be reported, not inferred from loopback configuration. | **PARTIAL** — engine control proven by TSK-0483 before current TLS ingress; public encrypted path requires TSK-0485 verification. |
| SEC-RES-02 | THR-RES-02 | Plain DNS 53 must remain non-public unless an explicit future architecture/security decision reopens it. `refuse_any=true` remains mandatory while the resolver can receive DNS queries. | External/host listener + firewall scan proves no public 53; config check proves `refuse_any=true`; bounded `ANY` test at applicable resolver boundary has response/query amplification ratio <=1 or explicit refusal/no useful amplified answer. | Plain 53 non-public current PASS; historical ANY ratio 1.00 PASS. Recheck after exposure/topology changes. |
| SEC-RES-03 | THR-RES-03 | Public DoH host exposes only the required DNS path/protocol behavior; AdGuard control/UI routes must never be reachable through the public virtual host. | Negative tests for `/`, `/control/status`, known admin/control paths and unsupported methods return non-success; approved DoH path remains functional. | `/` and `/control/status` 404 currently proven; broader negative suite remains future verification. |
| SEC-RES-04 | THR-RES-04 | DoH/DoT requests must be protocol-valid and explicitly bounded by payload size, request/connection/header timeouts and concurrency; malformed/oversized input must fail closed without stack trace or service instability. | Configuration inspection shows explicit finite bounds; negative tests at/beyond each bound produce deterministic rejection/close; post-test health passes. DNS message body must never exceed the protocol maximum and implementation should use the smallest proven operational cap. | Requirement only; exact safe ingress bounds must be frozen/tested before release. |
| SEC-RES-05 | THR-RES-01/05 | Abuse controls must not silently create a self-DoS for intended supported users behind shared NAT/proxy aggregation. | Low-rate and modest-concurrency test from multiple independent source networks/devices succeeds; rate-limit identity/aggregation behavior through Nginx is directly observed; no unsupported claim that the AdGuard client IP equals the original device IP. | Needs current public-path verification. |
| SEC-RES-06 | THR-RES-05 | Upstream retry/failure behavior must be bounded; no uncontrolled retry loop or silent change to unapproved recursive provider/ECS behavior. | Failure-injection/upstream-unavailable test shows bounded timeout/retry, truthful `Action needed/uncertain` behavior and recovery/removal route; post-test config still exact Quad9 dns10/ECS-off unless approved change. | Upstream identity current PASS; load/failure NFR verification remains later. |
| SEC-RES-07 | THR-RES-01 | Resource/cost exhaustion must trigger an operational stop/throttle path before uncontrolled spend or host collapse. No auto-scaling/HA purchase is authorized by this NFR. | TSK-0485/operations test records CPU/memory/socket/load baseline, bounded test peak, recovery, alert/stop threshold and post-test health. Thresholds must be evidence-derived from the actual VM; they are not invented in L4. | Future measured threshold required. |

## 6. Administrative, secret and configuration-integrity NFRs

| NFR | Threats | Requirement | Verification / PASS condition | Current evidence status |
| --- | --- | --- | --- | --- |
| SEC-ADM-01 | THR-ADM-01 | AdGuard admin interface remains loopback-only and authenticated; no public reverse-proxy/control route. | Listener = `127.0.0.1:3000`; authenticated local status succeeds; unauthenticated status = 401; external/public control paths non-success. | Current PASS evidence exists. |
| SEC-ADM-02 | THR-ADM-01/02 | Only the governed administration/change path may mutate resolver/privacy/filter configuration; each consequential change must be attributable to commit/workflow/run/job and current target identity. | Change audit links exact commit/workflow/run/job + machine fingerprint + before/after config/evidence; no unapproved local/public admin path exists. | Current GitHub-runner/local-admin model proven; apply on every mutation. |
| SEC-ADM-03 | THR-ADM-02 | Admin credentials, TLS private keys, tokens and backup decryption material never enter Git, normal logs, evidence text or public output. | Secret scan of committed release/evidence; runtime file metadata inspection; test output contains placeholders/hashes only; suspected leak => immediate rotation/reissue before reuse. | Current root credential/key/encrypted-backup evidence supports baseline. |
| SEC-ADM-04 | THR-ADM-02 | On-host secret files use least privilege; current admin credential remains `0600 root:root`; private-key access remains restricted to required service/root path. | File owner/mode checks are release/security assertions. Any broadening is blocking until justified and reverified. | Current PASS evidence. |
| SEC-ADM-05 | THR-TLS-01 | DNS hostname/certificate/private-key identity must match the approved resolver; certificate renewal/expiry failure must be detected before expiry. | External TLS hostname/chain test; renewal dry-run; deploy hook; expiry monitor/alert; invalid/expired cert causes verification failure, never green state. | Current PASS evidence from TSK-0442/0443. |
| SEC-ADM-06 | THR-DATA-01 | Security hardening must never enable raw query/access history as a substitute for abuse visibility. | Config/runtime inspection: Nginx access log off; AdGuard query/file logs/stats off; anonymisation on; security metrics are aggregate/non-sensitive. | Current PASS; continuously reverify after security changes. |

## 7. CI/CD, root-capable runner and supply-chain NFRs

The self-hosted production runner is a high-trust boundary because it has non-interactive sudo. A repository/workflow compromise can therefore become a host compromise even when AdGuard admin remains loopback-only.

| NFR | Threats | Requirement | Verification / PASS condition | Current evidence status |
| --- | --- | --- | --- | --- |
| SEC-CI-01 | THR-CI-01 | Production/recovery runners must never execute untrusted fork/PR code, arbitrary user-provided scripts or dynamically fetched executable content. | Workflow audit: production labels are used only from trusted `main`/explicit owner-governed dispatch; no `pull_request`/`pull_request_target` path can execute untrusted code on the root-capable runner. | Requirement; trusted-main baseline stated, repo-wide workflow audit remains required before release. |
| SEC-CI-02 | THR-CI-01 | Every root-capable host job asserts exact target identity before privileged commands and uses serialized host concurrency where conflicting mutations are possible. | Workflow static audit + target run proof of machine fingerprint/label; concurrency group present for host mutations. | Current host workflows generally use fingerprint/concurrency; must be systematic. |
| SEC-CI-03 | THR-CI-02 | Production host execution defaults to `contents: read` and `persist-credentials: false`. Evidence/state publication should be separated from the root-capable host step wherever practical. | Static workflow audit. A host job with repository write token requires a narrowly documented exception: trusted-main-only trigger, no untrusted code, `contents: write` only (no broader scopes), privacy-safe artifact, token never printed, and post-job credential cleanup. | **OPEN hardening deviation DVR-0484-01:** current `inspect-tsk0230-runtime-data.yml` uses `contents: write` + `persist-credentials: true` on the production runner to publish evidence. No compromise is evidenced; future-use pattern must be narrowed/separated. |
| SEC-CI-04 | THR-CI-01/SC-01 | Workflow/action references must be trusted and version-pinned according to the project’s release-security policy; no curl-pipe-shell/unverified binary execution on production runners. | Repo workflow audit identifies every external action/download, version/provenance and approved exception; test/release blocks unknown executable sources. | Future comprehensive audit required. |
| SEC-SC-01 | THR-SC-01 | Future web/app build has one authoritative package-manager/lockfile boundary, reproducible frozen install and explicit install-script policy. | CI clean install from committed lockfile with immutable/frozen mode; competing lockfiles/manager disagreement = fail; unreviewed dependency scripts disabled. | Future app only. |
| SEC-SC-02 | THR-SC-01 | No unmitigated **reachable** critical/high dependency or OS vulnerability may ship; remediation must not be forced blindly across dependency ranges. | Native package-manager/OS audit + reachability/mitigation record; critical/high reachable finding => release block unless owner accepts with compensating control + expiry under REQ-0058. | Ubuntu host currently patched; future app dependency audit required. |
| SEC-SC-03 | THR-SC-01 | New dependencies are minimized and reviewed for necessity, ownership/maintenance, provenance, scripts and transitive impact. | Dependency/lockfile diff review and SBOM/inventory evidence for release candidate. | Future app only. |

## 8. User-data, privacy and security-logging NFRs

Security telemetry must obey TSK-0230; “security” is not a justification to recreate browsing history.

| NFR | Threats | Requirement | Verification / PASS condition | Current evidence status |
| --- | --- | --- | --- | --- |
| SEC-DATA-01 | THR-DATA-01 | Normal request path retains no identifiable DNS/domain history, access log or per-client statistics. | Fresh runtime/config/storage test after security changes: access log off; query/file log off; stats off; anonymisation on; no non-empty query-history file. | Current PASS. |
| SEC-DATA-02 | THR-DATA-02 | Critical operational error logs use minimum severity, bounded retention and local least-privilege access; they never become product analytics. | `crit` only; daily rotation <=14 generations under current baseline; files <=0640 and service/admin group only; no record contents committed to Git. | **PARTIAL:** retention/severity proven; `DVR-0230-01` custom DoH error log is current 0644 and must be fixed/reverified before participant/public reliance. |
| SEC-DATA-03 | THR-DATA-03 | Exceptional request-level diagnostics are incident-specific, necessary, approved, allowlisted, time-boxed, restricted and deletion-verified. | Procedure precondition + synthetic incident test + deletion read-back; raw data never Git/analytics/training. | Procedure exists; later acceptance must test when applicable. |
| SEC-DATA-04 | THR-J1-01 | If J1 is implemented, `journey_token` must be cryptographically random, opaque, non-semantic, non-reused and sufficiently unpredictable to resist online guessing; token is not logged or linked across journeys. | CSPRNG implementation review; token entropy >=128 bits; statistical/format test; expired/deleted/reused token tests; logs contain no full token. | Future conditional J1. |
| SEC-DATA-05 | THR-J1-01 | J1 data remains <=24h non-sliding with early deletion and no identity linkage; security controls cannot lengthen retention for convenience. | Schema/storage/TTL/deletion/no-linkage tests from TSK-0229/0230. | Future conditional J1. |
| SEC-DATA-06 | THR-DATA-01/STATE-01 | Protection state is derived from evidence, not from client-supplied booleans or profile presence. | Negative test tampers with client state/confirmation and cannot produce S1 `Verified`; stale/failed verifier produces uncertain/action-needed. | Requirements frozen; future app verification required. |

## 9. Future accountless web/application security NFRs

These requirements are dormant until the approved L6 application build. They do **not** authorize coding now.

| NFR | Threats | Requirement | Verification / PASS condition |
| --- | --- | --- | --- |
| SEC-WEB-01 | THR-WEB-01 | All external input is server-side validated against an allowlisted schema for type, enum/range, format and explicit maximum length/size; unexpected fields are rejected. | Unit/integration/negative tests at boundary, max and above-max values; malformed/extra fields fail deterministically without persistence. |
| SEC-WEB-02 | THR-WEB-01 | Browser output uses framework auto-escaping/contextual encoding; untrusted values are never inserted as executable HTML/script/URL/CSS without approved sanitizer/encoder. | XSS payload suite produces text/encoded output only; no dangerous DOM sink from untrusted data. |
| SEC-WEB-03 | THR-WEB-01 | Database access, if introduced, is parameterized/typed; no user input is concatenated into SQL/query language, shell, file path or template code. | Static review + injection tests; no direct shell/eval execution path from untrusted input. |
| SEC-WEB-04 | THR-WEB-02 | Arbitrary server-side URL fetch is absent by default. If later genuinely required, scheme/host/destination are allowlisted, redirects controlled, all resolved addresses checked/pinned against private/loopback/link-local/metadata networks, and time/size limits are finite. | SSRF negative suite for localhost/private/link-local/cloud-metadata/DNS-rebinding/redirect cases. |
| SEC-WEB-05 | THR-WEB-03 | Production HTTPS responses use a tested browser-security-header baseline appropriate to the actual app: HSTS, CSP, anti-framing policy, nosniff and a restrictive referrer/permissions policy where applicable. | External header scan + browser test; CSP has no unjustified wildcard/unsafe execution exception. |
| SEC-WEB-06 | THR-WEB-03 | User-facing errors are generic; no stack trace, filesystem path, secret, internal host, token or raw exception data is exposed. | Failure/500/validation tests inspect responses and browser console. |
| SEC-WEB-07 | THR-WEB-01/03 | Public application requests have explicit request/body/header/time/concurrency limits and abuse throttles on resource-expensive endpoints. | Boundary/load tests prove deterministic rejection and stable health. Exact thresholds are frozen from implemented feature cost, not guessed in L4. |
| SEC-WEB-08 | Auth-related threats | **No authentication/login/password-reset/OAuth surface exists in the active accountless baseline.** If EXC-0001 activates, TSK-0484 must reopen and a new authentication/session/authorization threat model must be approved before implementation. | Route/source scan shows no hidden account/auth endpoint in current accountless release candidate. |
| SEC-WEB-09 | THR-WEB-01/03 | No file upload, webhook, callback URL, public API/integration platform or AI/LLM execution surface is introduced without a new threat-boundary review. | Route/feature inventory comparison to approved scope; any such feature without approved change = release block. |

## 10. Recovery and integrity NFRs

| NFR | Threats | Requirement | Verification / PASS condition | Current evidence status |
| --- | --- | --- | --- | --- |
| SEC-REC-01 | THR-REC-01 | Recovery uses only approved versioned code/config and encrypted recovery artifacts; secrets/private keys remain outside Git. | Backup checksum/recipient verification; decrypt only in authorized recovery context; clean-host drill proves approved config/privacy/security after restore. | Current backup/recovery evidence PASS. |
| SEC-REC-02 | THR-REC-01 | Recovery must not restore deleted user/query/diagnostic history or obsolete insecure configuration. | Restore content/scope audit + post-restore privacy/config regression; prohibited history count = 0. | Current config-backup scope designed privacy-minimally; continuously verify. |
| SEC-REC-03 | THR-REC-01/TLS-01 | Post-recovery service cannot be declared healthy until TLS identity, firewall/listeners, admin isolation, DNS/filter/privacy controls and external encrypted resolution pass. | Timed recovery acceptance suite with exact target identity and post-recovery health/evidence. | Current TSK-0431 project-controlled recovery drill PASS; future release versions re-run. |

## 11. Security release/blocking policy

For the relevant future release/security gate:

1. **Critical/high reachable vulnerability or control failure = blocking** unless the Project Owner explicitly accepts the specific residual risk with a compensating control and expiry under REQ-0058.
2. A **privacy/security deviation** that could expose user-related data is blocking for participant/public operation until remediated or explicitly accepted by the authorized gate; L4 definition PASS does not make it implemented.
3. A failed public resolver abuse test is blocking for the affected public endpoint; do not widen exposure or “fix” by weakening privacy controls.
4. No security test may enable persistent browsing/query history merely to gain observability.
5. No security control may silently activate accounts, invasive tracking, new vendors, HA spend, Azure control-plane changes or a broader public API.
6. Ambiguous destructive/non-idempotent remediation stops for evidence/authority rather than blind retry.

## 12. Explicit current deviations / verification gaps

### DVR-0230-01 — custom Nginx error-log mode

Carried from TSK-0230. The custom DoH critical error log is currently zero bytes but mode `0644 root:root`; target NFR is <=`0640`, service/admin only. This must be remediated/reverified before participant/public reliance on SEC-DATA-02.

### DVR-0484-01 — repository write credential on root-capable evidence workflow

Current `.github/workflows/inspect-tsk0230-runtime-data.yml` uses:

- self-hosted `Linux/X64` runner;
- `permissions: contents: write`;
- `actions/checkout` with `persist-credentials: true`;
- non-interactive sudo host inspection;
- trusted-main/path trigger and serialized host concurrency.

No compromise, secret leak or untrusted-trigger path is evidenced. The concern is **least-privilege architecture**: a repository write token is available within a root-capable host job solely so the job can publish its evidence. Future security baseline should prefer a split design in which the host step has read-only repository credentials/no persisted checkout credential and emits a privacy-safe artifact/result for a separate bounded publisher. Until that is implemented, any same-runner write exception must remain trusted-main-only, contents-write-only and free of untrusted code/data execution.

### GAP-0484-02 — current public encrypted resolver abuse path not yet directly accepted

TSK-0483 proved engine-level abuse controls and an 80-query UDP burst/ANY refusal while the resolver was pre-public. Later TSK-0437 opened current public **encrypted** Nginx ingress on 443/853 while keeping plain DNS 53 loopback/non-public.

Therefore TSK-0483 is valid evidence of AdGuard control capability/configuration but is **not sufficient evidence that the present public DoH/DoT ingress is effectively rate-limited and resilient**. SEC-RES-01/04/05/07 require direct current-path verification, expected to be satisfied by the downstream abuse/security verification task rather than inferred here.

## 13. Minimum security verification catalogue

A release/acceptance suite derived from this contract must include at least:

1. external port/listener/firewall scan;
2. public DoH path positive test;
3. public DoT path positive test;
4. public admin/control path negative tests;
5. public DoH/DoT bounded burst/rate/concurrency test;
6. malformed/oversized/unsupported-method ingress tests;
7. ANY/amplification and plain-53 non-public checks;
8. upstream failure/recovery test;
9. TLS hostname/chain/expiry/renewal monitoring test;
10. local admin authentication/listener test;
11. production secret/key permission and Git secret scan;
12. Nginx access/error-log + AdGuard query/statistics privacy-drift test;
13. DVR-0230-01 permission recheck;
14. self-hosted workflow trigger/permissions/credential/concurrency/target-identity audit;
15. future web input/XSS/injection/SSRF/error/header tests when an app exists;
16. dependency/OS vulnerability and supply-chain/lockfile audit;
17. J1 token entropy/non-log/reuse/expiry/no-linkage tests if J1 exists;
18. exceptional diagnostic approval/access/deletion test when invoked;
19. encrypted backup integrity + clean recovery regression;
20. post-security-change Protection Map truth-state regression.

Every test must identify the exact artifact/version/target and preserve privacy-safe evidence. A generic scanner “pass” without threat/control mapping is insufficient for INT-0015.

## 14. Revalidation triggers

Reopen affected TSK-0484 requirements/evidence when any of these occurs:

- public listener/path/topology changes;
- rate-limit/proxy/client-IP behavior changes;
- AdGuard/Nginx/OS major/security-relevant update;
- new upstream or DNS endpoint/profile;
- account/auth/dashboard activation;
- J1 implementation/schema/token change;
- new API, upload, webhook, arbitrary URL fetch, AI/LLM or third-party integration;
- new analytics/support/diagnostic data path;
- new dependency/package manager/build system;
- runner privilege/labels/triggers/token permissions change;
- secret/TLS/domain/backup ownership change;
- security incident, abuse report, saturation/cost anomaly or control failure;
- `DVR-0230-01`, `DVR-0484-01` or GAP-0484-02 remediation changes the relevant boundary.

## 15. ACC-0484 traceability

ACC-0484 requires:

> Requirements map to identified threats, include measurable controls and verification, and distinguish public resolver abuse from user-data security.

- §§3–4 explicitly identify assets, trust boundaries and threat/abuse cases.
- §5 isolates **public resolver abuse/availability** controls and identifies the current public-path verification gap.
- §§6–10 separately define admin/secrets, runner/supply-chain, user-data/privacy, application and recovery security controls.
- Every NFR row identifies its threat(s), required control and measurable verification/PASS condition.
- §12 preserves current deviations/gaps instead of turning design requirements into false implementation evidence.
- §13 produces an exact downstream verification catalogue tied to INT-0015.

**TSK-0484 result: PASS candidate for provisional internal L4 security-NFR definition only, subject to independent verification, GitHub read-back and runtime reconciliation. `DVR-0230-01`, `DVR-0484-01` and `GAP-0484-02` remain open and no build/release/participant/public authorization is inferred.**
