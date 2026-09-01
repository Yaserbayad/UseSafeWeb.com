# TSK-0231 — Architecture Decisions and Rejected Alternatives

**Version:** 1.0.0  
**Date:** 2026-09-01  
**Lifecycle:** L5 — Architecture, Technical Design & Delivery Readiness  
**Task:** TSK-0231 — Record architecture decisions and rejected alternatives  
**Acceptance:** ACC-0231 / VER-0231 / EVD-0231  
**Authority:** current modular Master Planning System; DEC-0053/CR-0006; DEC-0054/CR-0007; DEC-0055/CR-0008  
**Hard dependencies:** TSK-0355; TSK-0411; TSK-0233; TSK-0444; TSK-0354  
**Status represented:** architecture decision consolidation candidate pending deterministic acceptance and canonical runtime read-back.

## 1. Purpose and authority boundary

This record consolidates material architecture decisions already supported by current canonical decisions, registers and accepted L5 dependency evidence. It is an **ADR index/consolidation, not a second mutable decision register, WBS, runtime state store or checkpoint**. It does not create a new owner decision or silently modify scope.

If this document conflicts with the manifest-routed WBS, authoritative registers/decisions, current source architecture artifacts, or verified `CURRENT_STATE.md` evidence, those authorities win and this document must be corrected.

This record does **not** infer implementation, deployment, LG-07/LG-08/LG-09 PASS, participant activation, production processing authority, final legal compliance, public launch or downstream task PASS. `RSK-0001` remains OPEN. `INT-0007` still requires later inspection of actual runtime/configuration/schema/log/cache/backup/deletion reality before release.

## ADR-01 — One TypeScript + Next.js full-stack application

**Context:** Current Version 1 needs one public website/application surface for the accountless setup journey plus optional parent account/session/dashboard functions while keeping deployment and operations small.

**Options:** (A) one TypeScript + Next.js full-stack application under `/website`; (B) separate SPA plus standalone API service; (C) microservices/service mesh; (D) native application as the primary product surface.

**Decision:** Use one production-capable TypeScript + Next.js full-stack application under `/website`, with explicit internal server/client boundaries and one deployable application release candidate.

**Rationale:** This satisfies the owner-selected lean architecture, reduces operational and release complexity, and keeps public, journey, account and server-integration boundaries testable without multiplying services.

**Rejected alternatives:** Separate SPA/API and microservices are rejected for Version 1 because they add service/deployment complexity without an approved need. Native-app-first is outside the approved Version-1 boundary.

**Consequences:** Server-only operations, protected provider calls and AdGuard integration remain inside explicit application server boundaries; browser interactivity is limited to necessary client surfaces. Scaling/re-architecture remains evidence-triggered rather than pre-emptive.

**Evidence:** TSK-0354 accepted architecture, artifact `TSK_0354_VERSION_1_APPLICATION_ARCHITECTURE_2026-09-01.md`, blob `4196c83e95a013c10b5c0a9a13005b97bbe08a59`; TSK-0355 current PASS, artifact `TSK_0355_MINIMUM_OWNER_SELECTED_APPLICATION_ARCHITECTURE_ADR_2026-09-01.md`, blob `bd2d0f2ef36ea9f54796224e68576036859badc5`.

**Owner:** Project Owner; Software Engineering is the implementation custodian within frozen scope.

**Review trigger:** Owner-approved scope change; verified performance/security/operations evidence showing the single deployable cannot satisfy current requirements; or a mandatory platform constraint.

**Links to requirements/risks:** REQ-0036; REQ-0038; REQ-0018; RSK-0001; INT-0007.

## ADR-02 — Dual-mode Version 1: complete accountless core plus optional parent account

**Context:** CR-0006 activated optional parent identity/session, minimum ownership persistence and a lightweight dashboard while preserving the complete accountless safety value.

**Options:** (A) complete accountless core plus optional account/dashboard; (B) mandatory account/login before core value; (C) accountless-only product with no optional persistence; (D) child accounts or broad customer DNS administration.

**Decision:** Preserve the full Phone → Internet → Services → truthful Protection Map/recovery core without login, while allowing an optional parent account/session and bounded device-management/dashboard path.

**Rationale:** This implements DEC-0053/CR-0006 exactly: persistent convenience is optional, while core protection setup is not gated by identity or payment.

**Rejected alternatives:** Mandatory login is rejected; the superseded pre-CR-0006 accountless-only scope is not the current Version-1 scope; child accounts and unrestricted/raw customer DNS administration remain excluded.

**Consequences:** Authentication/provider/datastore failure may degrade optional account functions but must not convert the healthy accountless core into an authenticated-only journey. Account ownership never proves technical protection.

**Evidence:** DEC-0053/CR-0006; current TSK-0354 PASS; current TSK-0233 PASS, artifact `TSK_0233_MINIMAL_DUAL_MODE_JOURNEY_ACCOUNT_DATA_MODEL_2026-09-01.md`, version 1.0.1, blob `156a1811bc4322e16474874e728d23a97a93ec4c`.

**Owner:** Project Owner; Product and Software Engineering are implementation custodians within the frozen boundary.

**Review trigger:** Explicit Project Owner scope change; evidence that optional-account behavior is making core value de facto mandatory-login; or a material security/privacy blocker.

**Links to requirements/risks:** REQ-0037; REQ-0041; REQ-0019; CON-0007; CON-0008; RSK-0001; INT-0006; INT-0007.

## ADR-03 — Separate J0/J1/AUTH/A data domains with no anonymous-to-account linkage

**Context:** The product needs temporary accountless routing state and optional persistent account/device value without building a hidden identity graph or extending anonymous state through sign-in.

**Options:** (A) separated J0 session state, optional anonymous J1 server state, AUTH session boundary and persistent A ownership domain; (B) one shared user/journey database; (C) automatic J1-to-account conversion on sign-in; (D) analytics/fingerprint/IP stitching.

**Decision:** Use J0 as session-only accountless state; permit J1 only if necessary, with a hard non-sliding maximum 24-hour lifetime, early deletion and no durable backup; keep AUTH and the persistent A domain separate; implement **no J1-to-account migration or linkage**.

**Rationale:** Separation gives the optional account feature its necessary ownership state without turning the anonymous journey into durable identity history, and preserves the current minimisation/no-linkage contract.

**Rejected alternatives:** Shared journey/account history, automatic promotion, fingerprint/IP/analytics stitching and persistent anonymous event history are rejected.

**Consequences:** Signing in creates/uses account-domain state independently. Any future explicit transfer requires a new field-by-field approved contract before implementation. J0/J1 are not restored from backups.

**Evidence:** TSK-0233 v1.0.1 blob `156a1811bc4322e16474874e728d23a97a93ec4c`; current TSK-0354 architecture; current TSK-0355 architecture; post-CR-0006 TSK-0229 accepted no-linkage baseline.

**Owner:** Project Owner; Software Engineering and Privacy/Security are custodians of the separation contract.

**Review trigger:** A future approved capability demonstrates that explicit anonymous-to-account transfer is genuinely necessary; any proposed new persistent identifier; or any evidence of cross-domain stitching.

**Links to requirements/risks:** REQ-0019; REQ-0037; REQ-0038; CON-0007; CON-0008; RSK-0001; INT-0006; INT-0007.

## ADR-04 — Minimum persistent ownership store; datastore product remains deliberately deferred

**Context:** Optional account/dashboard functionality requires durable parent-to-device ownership/settings/lifecycle state, but the project forbids unnecessary persistence and the current architecture has not proven a specific datastore product/version necessary.

**Options:** (A) minimum logical persistent A-domain schema with product selection deferred to downstream current evidence; (B) prematurely freeze a database vendor; (C) create a broad product event/history ledger; (D) avoid all persistence and remove the approved optional dashboard value.

**Decision:** Freeze the minimum logical parent/device ownership schema and lifecycle boundary now, while deferring concrete datastore product/runtime selection until downstream architecture/implementation evidence can verify security, privacy, reliability, backup/deletion and operational fit.

**Rationale:** The logical data contract is required now; a vendor choice is not. Deferral avoids inventing technical facts while preserving the approved optional account capability.

**Rejected alternatives:** Premature datastore selection, unnecessary event/history ledgers and eliminating the approved persistent account/device capability are rejected.

**Consequences:** Persistent fields remain limited to approved provider/account reference, opaque ownership/device IDs, optional nickname/coarse platform, curated settings, lifecycle/concurrency metadata, server-only ClientID linkage and one freshness-bounded current protection record. Production A-domain backup processing remains fail-closed until exact backup retention/access/encryption/deletion-propagation/restore semantics are frozen.

**Evidence:** TSK-0233 current PASS; TSK-0354 and TSK-0355 current PASS; REQ-0037/REQ-0038 current requirements.

**Owner:** Project Owner; Software Engineering, Security and Privacy are custodians for downstream datastore selection and implementation evidence.

**Review trigger:** Downstream datastore selection task; production backup design; vendor/price/terms/security change; or evidence that the logical schema is insufficient for an already-approved requirement.

**Links to requirements/risks:** REQ-0019; REQ-0037; REQ-0038; CON-0007; CON-0008; RSK-0001; INT-0007.

## ADR-05 — Encrypted DNS service identity and initially constrained public exposure

**Context:** Supported devices need a stable encrypted DNS endpoint while the service must minimise open-resolver/admin exposure and remain independent of optional accounts.

**Options:** (A) `dns.usesafeweb.com` with DoH at `https://dns.usesafeweb.com/dns-query`, Android Private DNS hostname and Apple DoH support, with public 443 as the initial encrypted path; (B) expose UDP/TCP 53 publicly; (C) expose AdGuard administration publicly; (D) enable public DoT 853 immediately without the required control evidence.

**Decision:** Use `dns.usesafeweb.com` as the stable DNS service identity; use `https://dns.usesafeweb.com/dns-query` for DoH; support the approved Android/Apple configuration paths; keep public UDP/TCP 53 and the AdGuard administration plane closed; defer public DoT 853 until its controls are proven.

**Rationale:** This gives supported devices a clear encrypted endpoint while reducing resolver/admin attack surface and retaining evidence-based expansion.

**Rejected alternatives:** Public plain DNS and public administration are rejected. Public DoT-before-control-proof is deferred rather than assumed safe.

**Consequences:** Browser/app-specific resolvers can bypass system DNS and therefore must map to truthful Not covered/uncertain states when UseSafeWeb cannot be proven. The DNS path remains usable without an account.

**Evidence:** TSK-0411 current PASS, artifact `infrastructure/dns/TSK-0411-DNS-TOPOLOGY-AND-CLIENT-CONFIGURATION-MODEL.md`, blob `52682205c83cac102fa93b4c455dcfb0a3ade672`; TSK-0354 current architecture.

**Owner:** Project Owner; Network/DNS Engineering is the technical custodian.

**Review trigger:** Verified DoT-control readiness; endpoint/provider/network architecture change; material abuse/scaling evidence; or a supported-platform requirement change.

**Links to requirements/risks:** REQ-0018; REQ-0019; CON-0007; CON-0008; RSK-0001; INT-0007.

## ADR-06 — Server-only typed and allowlisted AdGuard control boundary

**Context:** Optional device management may require bounded AdGuard client/configuration operations, but exposing the raw administration interface or treating ClientID as authority would create severe authorization and secret risks.

**Options:** (A) a server-only typed/allowlisted application adapter; (B) browser-to-AdGuard administration calls; (C) generic application proxy to arbitrary `/control/*`; (D) ClientID as an authorization credential.

**Decision:** Keep all AdGuard administration credentials and control operations server-side behind narrow typed/allowlisted application operations. `ClientID` is an opaque DNS-control reference and is **never authentication or authorization**.

**Rationale:** This preserves least-exposed privileges, supports product-level authorization/validation, and prevents raw AdGuard administration from becoming a customer-facing control plane.

**Rejected alternatives:** Browser-admin access, arbitrary control passthrough and ClientID-based authorization are rejected.

**Consequences:** Account-owned device operations must first pass server-side session and ownership authorization. Ambiguous mutations require bounded reconciliation/idempotency behavior rather than fabricated success. Exact transport/version mapping remains with its authoritative downstream interface task.

**Evidence:** Current TSK-0354 PASS; current TSK-0355 PASS; TSK-0233 current persistent-field contract; INT-0012 architecture boundary carried by the accepted application architecture.

**Owner:** Project Owner; Software Engineering, Network/DNS Engineering and Security are implementation custodians.

**Review trigger:** AdGuard API/version incompatibility; a new approved device-control capability; security finding in the adapter boundary; or evidence requiring a different private integration mechanism.

**Links to requirements/risks:** REQ-0019; REQ-0037; CON-0007; CON-0008; RSK-0001; INT-0007.

## ADR-07 — Privacy-first DNS telemetry: no identifiable browsing history

**Context:** The service needs sufficient health/reliability evidence without creating a surveillance product or retaining identifiable browsing/query history.

**Options:** (A) persistent identifiable DNS query/file logging and per-client statistics; (B) privacy-first operation with identifiable query logging off and identifiable per-client statistics excluded, using only separately approved minimal operational evidence; (C) customer-visible domain/top-domain history.

**Decision:** Keep persistent identifiable query/file logging OFF and identifiable per-client statistics OFF/excluded. No product schema/store for DNS queries, domains, visited URLs, browsing/top-domain history or child activity is permitted by this architecture.

**Rationale:** This directly implements CON-0007/CON-0008 and the approved family-safety product boundary while preserving the ability to design minimal, purpose-bound reliability evidence separately.

**Rejected alternatives:** Browsing history, top-domain product metrics, persistent identifiable query logs and identifiable client-statistics history are rejected.

**Consequences:** Technical protection verification must rely on bounded current evidence, not browsing-history collection. Any future telemetry field requires an explicit purpose, necessity, retention, access and privacy review under current authority.

**Evidence:** CON-0007; CON-0008; TSK-0233 current PASS; TSK-0354/TSK-0355 current architecture; DEC-0016 privacy-first DNS baseline.

**Owner:** Project Owner; Network/DNS Engineering, Security and Privacy are custodians.

**Review trigger:** A concrete reliability/security requirement cannot be met with the approved minimal evidence; any request for identifiable query/statistics data; or a material platform/security change.

**Links to requirements/risks:** REQ-0019; CON-0007; CON-0008; RSK-0001; INT-0006; INT-0007.

## ADR-08 — Production plus CI/ephemeral environments; no persistent staging by default

**Context:** DEC-0054/CR-0007 replaced the older mandatory pilot/staging lifecycle with evidence-driven production activation after readiness, while pre-release automated/synthetic verification remains required.

**Options:** (A) production plus disposable CI/ephemeral preview/test environments and bounded production ramp after LG-09; (B) mandatory persistent staging; (C) mandatory separate pilot environment; (D) direct production changes without CI/ephemeral verification.

**Decision:** Maintain PROD plus disposable CI/ephemeral synthetic/test environments. Do not operate persistent staging unless later evidence justifies it. After LG-09 and all applicable gates, bounded/ramped production activation is a production-safety mechanism, not a third environment.

**Rationale:** This matches CR-0007, reduces unnecessary persistent infrastructure and cost, and preserves required verification before active production use.

**Rejected alternatives:** Mandatory persistent staging and a separate mandatory pilot lifecycle are superseded by current owner authority. Unverified direct-to-production change is rejected.

**Consequences:** CI/ephemeral environments use synthetic/test-only data and are cleaned up. Production has its own secrets/endpoints/rollback evidence. No real participant or production-processing authority is inferred from this ADR.

**Evidence:** TSK-0444 current PASS, artifact `infrastructure/TSK-0444-PRODUCTION-CI-EPHEMERAL-ENVIRONMENT-MODEL.md`, blob `ca986677385fcc36348376c7a7899c6ddf90fa2d`; DEC-0054/CR-0007.

**Owner:** Project Owner; Cloud/Platform Engineering is the environment custodian within approved authority.

**Review trigger:** Evidence that a persistent staging environment materially improves safety/correctness; release architecture change; or an applicable platform/legal/security requirement mandates another environment.

**Links to requirements/risks:** REQ-0018; REQ-0019; RSK-0001; INT-0007.

## ADR-09 — Owner-provided Azure VM boundary and direct-host deployment

**Context:** The owner provides separate Azure Ubuntu web/application and DNS VMs. The project needs a minimal deployment boundary without taking unsupported authority over the Azure control plane or introducing container orchestration without need.

**Options:** (A) owner-provided two-VM boundary, direct-host services and Bash-based deployment/recovery; (B) Docker/Kubernetes as mandatory baseline; (C) application automation that owns Azure subscription/control-plane provisioning; (D) co-locate web application and DNS administration on one public service surface.

**Decision:** Keep the owner-provided separate web/app VM and DNS/AdGuard VM boundary, with direct-host deployment/recovery as the baseline. Azure subscription/control-plane ownership remains outside application automation. Containers/orchestration require later evidence before introduction.

**Rationale:** This implements DEC-0013/DEC-0043 and the accepted architecture with the least operational machinery while maintaining service separation and recoverability.

**Rejected alternatives:** Mandatory Docker/Kubernetes, unapproved Azure control-plane automation and collapsing app/DNS administration into one public surface are rejected for the current baseline.

**Consequences:** Secrets/configuration remain externally injected; host/recovery automation must be idempotent, auditable and bounded by its own acceptance. The initial service region remains the current owner-selected Azure West Europe/Netherlands architecture until separately changed.

**Evidence:** DEC-0013; DEC-0043; TSK-0411 current PASS; TSK-0444 current PASS; TSK-0354/TSK-0355 current architecture.

**Owner:** Project Owner; Cloud/Platform Engineering and Network/DNS Engineering are implementation custodians.

**Review trigger:** Owner infrastructure change; verified scaling/recovery/security evidence requiring containers/orchestration; regional expansion trigger; or a mandatory platform constraint.

**Links to requirements/risks:** REQ-0018; REQ-0019; RSK-0001; INT-0007.

## ADR-10 — Legal/data and runtime truth remain downstream release fences

**Context:** L5 architecture can define privacy-preserving boundaries, but it cannot truthfully establish final England participant legal/data readiness or certify actual production processing before the implementation/runtime facts exist.

**Options:** (A) keep legal/runtime verification open and fail closed where exact facts are unresolved; (B) treat architecture intent as final compliance proof; (C) invent retention/recipient/vendor/backup conclusions in advance; (D) allow real England participant processing before readiness evidence.

**Decision:** Keep `RSK-0001` OPEN. Treat current lawful-basis/retention/vendor/backup statements as conditional where the canonical records say they are conditional. Require `INT-0007` inspection of actual runtime/configuration/schema/log/cache/recipient/backup/deletion behavior before release and prohibit real England participant processing before the applicable readiness gate.

**Rationale:** Architecture intent is not production reality or legal sign-off. This preserves source traceability, prevents unsupported conclusions, and keeps discrepancies release-blocking until corrected or explicitly resolved by proper authority.

**Rejected alternatives:** Self-certifying compliance from design documents, invented legal durations/recipients/processing facts, and premature participant processing are rejected.

**Consequences:** Production A-domain backup handling remains fail-closed until exact supported semantics are frozen. Later implementation evidence may require correction/reopening of stale architectural assumptions without implying scope change. No legal approval is fabricated by TSK-0231.

**Evidence:** REQ-0018; REQ-0019; RSK-0001; INT-0006; INT-0007; current TSK-0233 PASS; current TSK-0354/TSK-0355 accepted non-inference boundaries.

**Owner:** Project Owner for product/release authority; Privacy/Legal and technical owners must supply the evidence/facts required by their authoritative downstream gates without fabricated attestations.

**Review trigger:** Material change in processing, recipient, region, vendor, retention, backup/deletion or participant model; authoritative legal/privacy assessment; actual implementation/runtime evidence that contradicts this design; or resolution/reclassification of `RSK-0001`.

**Links to requirements/risks:** REQ-0018; REQ-0019; CON-0007; CON-0008; RSK-0001; INT-0006; INT-0007.

## 2. Rejected-alternative cross-check

The ten ADRs above intentionally preserve these current exclusions/deferments rather than silently reopening them:

- mandatory login before core value;
- automatic anonymous-journey-to-account linkage;
- browsing/query/domain/top-domain/child-activity history;
- ClientID as authentication/authorization;
- public AdGuard administration or arbitrary `/control/*` browser passthrough;
- public plain DNS exposure as the initial client path;
- public DoT 853 before its required controls are proven;
- mandatory microservices, Kubernetes or container orchestration;
- mandatory persistent staging or a separate mandatory pilot lifecycle;
- premature datastore/vendor, backup-retention or final legal-compliance conclusions.

These are architecture consequences of current authority, not independent new owner decisions.

## 3. Acceptance mapping

ACC-0231 requires every material decision to carry context, options, decision, rationale, consequences, evidence, owner, review trigger and requirement/risk links. ADR-01 through ADR-10 each contain those fields, with rejected alternatives additionally explicit.

Verification must bind this exact artifact to the current WBS/ACC/VER/EVD contract and current accepted dependency evidence, confirm the controlling requirement/risk/interface references, run the full modular plan validator, and only then permit a `CURRENT_STATE.md` PASS mutation.

**Non-inference:** this record does not itself make TSK-0231 PASS. PASS requires deterministic acceptance evidence, durable publication, runtime mutation and independent GitHub read-back.