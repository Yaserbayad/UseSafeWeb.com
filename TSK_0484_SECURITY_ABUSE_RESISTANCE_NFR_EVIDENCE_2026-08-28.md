# TSK-0484 — Security and Abuse-Resistance NFR Verification Evidence

**Task:** TSK-0484 — Define security and abuse-resistance NFRs  
**Acceptance:** ACC-0484  
**Verification:** VER-0484 — independent threat/control/verification trace audit  
**Evidence:** EVD-0484  
**Date:** 2026-08-28  
**Result:** PASS candidate pending GitHub read-back and guarded runtime reconciliation

## 1. Exact evidence index

- NFR contract: `TSK_0484_SECURITY_ABUSE_RESISTANCE_NFR_2026-08-28.md`
- Contract blob: `ebd146f88f51cae67b9515fb94133bcd74c8cf28`
- Contract creation commit: `95b2dd153b5ce07308bd93b7b702a31eedc0b6ee`
- Current runtime selection: `CURRENT_STATE.md` selects TSK-0484 as L4 / A3 / AUTO_ALLOWED / MEDIUM with hard dependency TSK-0230 current PASS and ACC-0484 exactly requiring threat mapping, measurable controls/verification, and a distinction between public-resolver abuse and user-data security.
- WBS blob: `dce5b829c4d447eac180ae1e896e0019292cf971`
- TSK-0230 NFR contract blob: `011caaa84dd3dec13bb608be30b15ec92a24f19e`
- TSK-0230 evidence blob: `f44b4a41992cac42a7538b3aa424bdf282c38724`
- TSK-0483 resolver-abuse evidence blob: `8a6426707fe9c9c8cd08f6b55e25d6b48bb8b28c`
- TSK-0437 current host/TLS-ingress revalidation blob: `b23bb28960efe28526626b36dfa2d52339a521e8`
- TSK-0201 secure administration evidence: current accepted runtime evidence establishes loopback-only authenticated AdGuard administration and governed GitHub-runner attribution.
- TSK-0442/0443 accepted evidence establishes current resolver TLS identity, renewal, expiry monitoring and deploy-hook behavior.
- TSK-0430/0431 accepted evidence establishes encrypted recovery material and clean recovery/rebuild verification.

## 2. Current primary-source verification

Current sources were rechecked on 2026-08-28.

### OWASP ASVS

Source: https://owasp.org/www-project-application-security-verification-standard/

OWASP currently identifies **ASVS 5.0.0** as the latest stable version and describes ASVS as a basis for testing web-application technical security controls and defining secure-development requirements.

**Audit implication:** the contract correctly uses ASVS as a requirements/verification reference and does not claim ASVS certification or implemented compliance for the unbuilt future application.

### OWASP Input Validation

Source: https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html

Current guidance requires validation of untrusted input as early as possible and recommends allowlisted syntactic/semantic checks including type, range, format and length.

**Audit implication:** SEC-WEB-01 is materially aligned with current primary guidance.

### OWASP XSS Prevention

Source: https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html

Current guidance emphasizes framework escaping/context-appropriate output handling rather than treating untrusted browser data as executable content.

**Audit implication:** SEC-WEB-02 is materially aligned with current primary guidance.

### OWASP SSRF Prevention

Source: https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html

Current guidance treats server-side destinations influenced by untrusted input as a security boundary and recommends strict validation/allowlisting plus controls against redirects/internal destinations.

**Audit implication:** SEC-WEB-04 is materially aligned and remains conditional because arbitrary server-side URL fetching is not in the active product baseline.

### AdGuard Home configuration

Source: https://github.com/AdguardTeam/AdGuardHome/wiki/Configuration

Current AdGuard documentation still defines `ratelimit`, `ratelimit_subnet_len_ipv4`, `ratelimit_subnet_len_ipv6`, `ratelimit_whitelist` and `refuse_any` as anti-DDoS/anti-amplification controls. Defaults documented for current builds are 20 QPS, IPv4 /24 and IPv6 /56.

**Audit implication:** the contract correctly preserves the current accepted engine-level baseline while refusing to infer that it proves the later public Nginx DoH/DoT path.

## 3. Eligibility and authority audit

The current authoritative runtime selects TSK-0484 only after TSK-0230 PASS. The task is internal provisional L4 definition work and is AUTO_ALLOWED. Real-participant evidence, owner/legal gate actions, public release, integrated build and account/auth activation remain outside this task.

`RSK-0002` remains OPEN and the contract states that its security design does not substitute for representative-parent validation.

**Result: PASS.**

## 4. ACC-0484 threat-mapping audit

ACC-0484 requires requirements to map to identified threats.

The contract identifies:

- twelve security assets;
- ten current/future trust boundaries;
- a threat catalogue covering resolver availability/abuse, amplification, malformed ingress, upstream failure, TLS identity, administration, secrets, CI/runner privilege, supply chain, application injection/XSS/SSRF, transient J1 data, privacy/logging drift, diagnostics, recovery integrity and protection-state integrity;
- stable threat IDs used by every downstream NFR table.

Each resolver, administration, CI/supply-chain, data/privacy, future-web and recovery NFR row cites one or more threat IDs.

**Result: PASS.**

## 5. ACC-0484 measurable-control audit

ACC-0484 requires measurable controls and verification.

The contract defines explicit verification/PASS conditions for all NFRs, including:

- public DoH/DoT positive and negative-path tests;
- bounded burst/rate/concurrency and post-test health checks;
- plain-DNS 53 non-public and ANY/reflection checks;
- finite payload/header/timeout/concurrency limits with negative tests;
- upstream failure/recovery verification;
- exact listener/authentication/public-admin tests;
- secret/key permission and Git-secret checks;
- workflow trigger/permissions/credential/concurrency/target-identity audit;
- reproducible dependency/lockfile and reachable-vulnerability gates for the future application;
- privacy-drift tests that must keep access/query/statistics history disabled;
- J1 entropy >=128 bits, non-reuse, expiry, no-linkage and no-full-token logging if J1 exists;
- input/XSS/injection/SSRF/header/error tests for the future application;
- encrypted-backup/recovery integrity regression;
- a minimum 20-item security verification catalogue.

The contract deliberately leaves environment-dependent thresholds to later measured implementation/testing rather than fabricating arbitrary L4 numbers.

**Result: PASS.**

## 6. Required resolver-abuse vs user-data-security separation

This is the most important ACC-0484 distinction.

### Resolver abuse / availability domain

Section 5 isolates threats and controls for high-rate public DoH/DoT traffic, amplification/plain-DNS exposure, path/method abuse, malformed/oversized ingress, upstream retry/failure, shared-NAT self-DoS and resource/cost exhaustion.

TSK-0483 is used only as evidence of AdGuard engine capability/configuration and historical pre-public abuse behavior. The contract explicitly states that it is **not sufficient evidence** for current public encrypted Nginx ingress on 443/853 after TSK-0437.

### User-data / administrative / application / supply-chain domain

Sections 6–10 separately define administration, secret handling, root-capable runner, supply chain, logging/privacy, transient J1, future web/application and recovery-integrity controls.

The contract explicitly states that DNS rate limiting cannot prove data minimisation and privacy logging controls cannot prove availability/abuse resistance.

**Result: PASS.** The required domains are separated in both threat taxonomy and control/verification tables.

## 7. Current evidence truthfulness audit

The contract does not convert partial/historical evidence into current implementation PASS.

It correctly preserves:

- current admin/TLS/host/privacy/recovery controls where direct evidence exists;
- **GAP-0484-02** because public encrypted DoH/DoT abuse/rate/concurrency behavior has not yet been directly accepted on the current Nginx path;
- **DVR-0230-01** because the custom DoH critical error log is currently mode `0644 root:root`, broader than the NFR target <=0640/service-admin only;
- **DVR-0484-01** because the TSK-0230 production-host evidence workflow currently uses `contents: write` and persisted checkout credentials on a root-capable self-hosted runner solely to publish evidence.

No compromise is claimed for DVR-0484-01. The deviation is architectural least-privilege debt, not a security-incident assertion.

**Result: PASS.**

## 8. Frozen-scope / change-authority audit

The contract does not silently authorize:

- account/authentication/dashboard;
- new public API, upload, webhook, callback, arbitrary URL-fetch or AI/LLM feature;
- new analytics or invasive surveillance;
- Azure control-plane changes;
- HA/auto-scaling spend;
- new vendor/upstream;
- public release or real-participant activation.

It requires the affected threat model to reopen when a new boundary is introduced.

**Result: PASS.**

## 9. INT-0015 downstream usability audit

INT-0015 requires a security baseline that engineering/QA can use to verify critical attack paths and block unresolved critical controls.

The contract supplies:

- stable threat IDs;
- measurable NFR IDs;
- explicit verification conditions;
- a release/blocking policy for reachable critical/high vulnerabilities/control failures;
- a 20-item minimum verification catalogue;
- revalidation triggers.

This is sufficient as an implementation/security-acceptance input without claiming the future app already exists.

**Result: PASS.**

## 10. Verification disposition

**VER-0484 independent audit result: PASS for ACC-0484's provisional internal L4 security/abuse-resistance NFR-definition scope.**

The read-back contract at blob `ebd146f88f51cae67b9515fb94133bcd74c8cf28`:

1. maps requirements to explicit threats/trust boundaries;
2. defines measurable controls and verification/PASS conditions;
3. clearly separates public-resolver abuse/availability from user-data/admin/application/supply-chain security;
4. preserves current deviations/gaps instead of self-certifying implementation;
5. leaves RSK-0002 and all human/legal/build/release/participant gates untouched.

The following remain OPEN/non-PASS and are not converted by this result:

- `DVR-0230-01` custom DoH critical error-log permission hardening;
- `DVR-0484-01` repository-write credential exposure within a root-capable production evidence workflow;
- `GAP-0484-02` current public DoH/DoT abuse/rate/concurrency verification;
- future web/application security implementation and testing;
- final legal/privacy/participant gates and representative-parent evidence;
- build/publication/launch authorization.

**Runtime may move TSK-0484 to PASS only after this evidence file is read back and the reconciliation mutation verifies the current selection, exact contract/evidence blobs and unchanged WBS acceptance.**
