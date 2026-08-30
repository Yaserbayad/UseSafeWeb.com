# TSK-0146 — Version-1 Optional-Account Product Baseline

**Version:** 1.0.0  
**Date:** 2026-08-30  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Authority:** DEC-0053 / CR-0006, with DEC-0052 / CR-0005 sequencing retained  
**Task:** TSK-0146 — Freeze Version-1 optional-account product baseline and accountless core path  
**Acceptance:** ACC-0146  
**Status represented by this artifact:** PRODUCT BASELINE CANDIDATE FOR TSK-0146 VERIFICATION; not LG-06 PASS, build approval, launch approval, or human/user validation

## 1. Purpose and supersession boundary

This artifact freezes the revised Version-1 product scope required after the Project Owner decision of 2026-08-30 that UseSafeWeb Version 1 must support parent accounts.

It supersedes only those clauses of the earlier accountless-only product artifacts and TSK-0146 evidence that treated customer accounts, Google sign-in, persistent parent/device ownership, or a lightweight dashboard as excluded/deferred from Version 1. Earlier evidence remains valid where it does not depend on excluding accounts, including the accountless core journey, AdGuard/DNS baseline, truthful Protection Map model, non-surveillance posture, accessibility/localization direction, self-service model, recovery/removal expectations, and free-core boundary.

No historical artifact is rewritten by this baseline.

## 2. Frozen Version-1 product shape

UseSafeWeb remains **First Phone Safety Setup** for a parent/caregiver around a child's first independently used smartphone. It remains a narrow safety-setup orchestration product rather than a DNS administration product or parental-surveillance suite.

The core experience remains:

1. **Phone** — guide applicable native safeguards first and truthfully handle already-configured, unsupported and not-applicable states.
2. **Internet** — guide activation and verification of the approved encrypted AdGuard-backed DNS protection path.
3. **Services** — guide at most the bounded relevant external-service safeguard defined by current scope.
4. **Protection Map** — show evidence-backed protection status and limits without turning parent confirmation or account ownership into technical verification.
5. **Recovery** — provide false-positive, compatibility, removal, reinstall/reconfiguration and recovery paths.

AdGuard remains infrastructure behind the product, not the customer proposition.

## 3. Dual-mode Version-1 rule

Version 1 has two supported modes that share one product and one truth model.

### 3.1 Accountless core — required

A parent must be able to obtain the complete core safety value without creating or signing into a UseSafeWeb account. The accountless path must support, as applicable to the supported platform and current product contract:

- understand/trust/start;
- platform and setup routing;
- native-safeguard guidance;
- encrypted DNS setup and verification;
- the bounded relevant-service guidance;
- truthful Protection Map output for the current journey;
- coverage-limit explanations;
- false-positive, troubleshooting, removal, reinstall/reconfiguration and recovery guidance.

Authentication-provider or account-datastore failure must not convert these core capabilities into a mandatory-login flow.

### 3.2 Optional parent account — required in Version 1

Version 1 must also provide an optional parent-account experience sufficient for persistence and lightweight device management. The product scope includes:

- account creation/sign-in through the approved authentication path;
- secure authenticated session and return experience;
- logout, session-expiry and revoked-session handling;
- minimum parent identity persistence required to operate the account;
- minimum parent-to-managed-device ownership persistence required to manage devices;
- a lightweight parent dashboard/device list;
- device lifecycle actions required by the approved product, including bounded remove/revoke/recover/reinstall/replacement handling;
- account/device deletion and recovery entry points;
- truthful error states when identity, session, datastore or downstream verification is unavailable.

Google/Firebase is the planned initial authentication route under DEC-0053. This L4 baseline does **not** certify that vendor choice, data flow, session design or security architecture; those remain subject to the current L5 vendor/privacy/security/architecture verification and later implementation/acceptance gates.

## 4. Minimum persistence boundary

Version-1 persistence must be the minimum necessary to operate the optional account and its approved device-management value.

At L4 the permitted product classes are limited to:

- the minimum identity/provider/account-lifecycle information necessary for an optional parent account;
- the minimum opaque parent-owned device identity/ownership and lifecycle information necessary to display and manage that parent's devices;
- the minimum approved product settings/state required for that ownership and lifecycle purpose.

The exact schema, fields, identifiers, retention periods, storage technology, backups and deletion mechanics remain downstream design/architecture obligations; this scope freeze does not invent them.

Accountless journey state and persistent account/device state must remain distinct. An anonymous journey must not be silently converted into persistent identity or linked to a parent account except through an explicit, approved user action and an authorised data-flow design.

## 5. Prohibited data and surveillance boundary

The optional account does not authorize surveillance. Version 1 must not create or expose a persistent product store for:

- DNS query or visited-domain history;
- browsing/activity history or top-domain reporting;
- child behavioral/activity timelines;
- child accounts or persistent child behavioral profiles;
- messages, contacts, photos, location or social-content monitoring;
- unrestricted/raw AdGuard administration data as a parent-facing product feature.

Persistent identifiable query logging remains off under the existing privacy baseline. Account/device ownership must never be used as a route to reconstruct browsing history.

## 6. Lightweight dashboard boundary

The Version-1 dashboard exists only to make the optional account useful for bounded persistence and device lifecycle management. It may expose only approved information necessary for those purposes, such as:

- the parent's managed-device list/labels and ownership relationship;
- current setup/protection state that is supported by the approved evidence model;
- bounded device/settings/lifecycle actions defined by later requirements and architecture;
- removal/revoke/recovery/deletion entry points;
- truthful unsupported/error/uncertain states.

It is explicitly **not**:

- a browsing-history dashboard;
- a DNS-query or top-domain dashboard;
- a child surveillance/activity dashboard;
- an unrestricted AdGuard control panel;
- an engagement feed designed to increase routine monitoring.

Account ownership, device registration or dashboard presence must never be displayed as proof that DNS protection is technically active. Protection Map verification semantics remain authoritative.

## 7. Authentication and session product boundary

Version 1 requires a secure sign-in/session product flow, but detailed security architecture remains L5 work. The product requirements therefore require downstream design and acceptance to cover at minimum:

- sign-in/account creation and safe return;
- session establishment, expiry, logout and revocation;
- clear handling of authentication-provider failure;
- parent-to-device ownership isolation;
- prevention of cross-parent device/data access;
- recovery and deletion paths;
- no browser exposure of AdGuard administrative credentials or unrestricted DNS administration.

Threat-model, CSRF, session-theft/account-takeover, authorization/IDOR, ClientID ownership and related implementation controls must be resolved and verified by their downstream security/architecture/test tasks before later gates can PASS. This artifact defines the product boundary; it does not claim those controls are implemented.

## 8. Deletion, revocation and recovery boundary

The optional account must be reversible and recoverable. Later design/implementation must provide coherent flows for:

- logout and session revocation;
- removal of a managed device from a parent account;
- account deletion;
- bounded account/session recovery;
- device replacement/reinstall/reconfiguration where applicable;
- truthful handling of partial failure between account state, device state and technical DNS state.

Deletion must address the authorised persistent account/device data and its governed backup/retention behavior. Deleting an account or device record must not falsely claim that a device's DNS configuration was removed if that technical action has not actually occurred; conversely, removing DNS protection must not silently imply account deletion.

## 9. Failure and truth model

Version 1 must fail truthfully and preserve the accountless core wherever technically possible.

- **Authentication/provider unavailable:** explain that account functions are unavailable; preserve the accountless core path.
- **Account datastore unavailable:** do not fabricate dashboard/device state; preserve safe accountless setup/recovery guidance where applicable.
- **Session invalid/expired/revoked:** require a valid session for account-owned data; do not leak prior parent/device state.
- **Ownership conflict/unknown device:** do not grant access or infer ownership.
- **DNS verification unavailable or contradictory:** show uncertain/error/action-needed according to the Protection Map model; account presence does not override verification evidence.
- **Partial deletion/recovery failure:** surface the incomplete state and provide a bounded safe recovery path; do not claim completion until verified.

## 10. Explicit Version-1 non-goals

Unless separately reauthorised through the applicable owner decision and gates, Version 1 excludes:

- mandatory login for core safety value;
- browsing/DNS-query/top-domain/activity history;
- child accounts, child app or persistent child behavioral profile;
- unrestricted/raw DNS or AdGuard administration for parents;
- covert or invasive monitoring;
- broad parental-control/surveillance suite scope;
- GROW lifecycle automation or AI parenting automation;
- school/institution administration or community/UGC;
- native mobile application as a product requirement;
- a safety-feature paywall or premium protection tier;
- paid-acquisition machinery as a product dependency;
- expansion of account persistence beyond the minimum approved parent/device ownership purpose without a later explicit scope decision and privacy/security review.

## 11. Carry-forward contracts

The following existing product contracts remain in force unless a later authoritative change explicitly supersedes them:

- UseSafeWeb.com public identity and UseSafeWeb First Phone Safety Setup positioning;
- AdGuard as the frozen backend absent a verified material blocker;
- encrypted DNS and current approved DNS/platform semantics;
- Phone -> Internet -> Services -> truthful Protection Map journey;
- technically verified versus parent-confirmed state separation;
- privacy-minimal diagnostics and no browsing-history product telemetry;
- truthful unknown/not-covered/action-needed/error/removed states;
- responsive/mobile-first and WCAG 2.2 AA target direction;
- English baseline with Turkish and Arabic/RTL structural capability, without implying ungated market activation;
- source/version ownership for technical guidance and protection claims;
- self-service-first support with bounded exceptional escalation;
- free core value with no card/trial/payment required before value.

The earlier TSK-0140 candidate remains historical evidence of these still-valid contracts but is superseded where it excludes the optional Version-1 account/dashboard capability.

## 12. Current residuals and downstream gates

This L4 scope freeze deliberately does not claim completion of downstream work:

- **RSK-0002 remains OPEN:** no parent/user/participant behavioral, usability or comprehension evidence exists before LG-09; none is inferred here.
- Dashboard/account privacy drift and inadvertent query/history exposure remain a material design/build risk and require downstream data-contract and runtime verification.
- Google/Firebase is planned, not yet accepted by this artifact as a completed vendor/privacy/security architecture decision.
- Exact persistent schema, retention, access, backup, deletion and account/device ownership mechanics remain for the authoritative downstream data/architecture tasks.
- Account-specific L4 UX/prototype work must be completed and internally/automatically accepted before LG-06.
- L5 architecture/privacy/security/vendor controls, L6 implementation, and L7 authentication/authorization/IDOR/ClientID/deletion/recovery acceptance remain mandatory before their respective later gates.
- DEC-0052 sequencing remains in force: no real-user validation is claimed or required before LG-09; first real-user testing remains L8 after LG-09 PASS.
- This artifact does not authorize participant processing, public launch, payment activation or any other later-gated consequential action.

## 13. ACC-0146 acceptance mapping

| ACC-0146 element | Frozen Version-1 disposition |
| --- | --- |
| Optional parent account in Version 1 | **INCLUDED** — required optional path. |
| Lightweight dashboard/device management | **INCLUDED** — bounded to minimum ownership/settings/lifecycle value. |
| Complete core setup/protection journey without login | **REQUIRED** — accountless core remains first-class. |
| Minimum identity/device persistence | **DEFINED AS A BOUNDARY** — only necessary parent/account/device ownership/settings/lifecycle data; exact schema downstream. |
| Authentication/session boundary | **DEFINED** — secure sign-in/session/expiry/logout/revocation/failure handling required; detailed architecture downstream. |
| Deletion/recovery boundary | **DEFINED** — account/device deletion, revocation and recovery required with truthful partial-failure handling. |
| Privacy boundary | **DEFINED** — no browsing/query/activity history, child behavioral profile or surveillance expansion. |
| Security boundary | **DEFINED** — parent/device isolation and downstream auth/authz/CSRF/IDOR/account-takeover/ClientID controls mandatory; no implementation claim. |
| Failure boundary | **DEFINED** — auth/datastore failures preserve truthful accountless core where technically possible and never fabricate state. |
| Browsing/activity history | **PROHIBITED**. |
| Child accounts | **PROHIBITED** for Version 1. |
| Broad/unrestricted DNS administration | **PROHIBITED**. |
| Future mandatory login | **OWNER-ONLY CHANGE** — requires a later explicit Project Owner decision. |

## 14. Verification disposition

This baseline is complete enough for independent ACC-0146 verification because it resolves the exact owner change that invalidated the prior accountless-only PASS while preserving all compatible prior scope.

Verification must independently confirm the artifact against the current canonical WBS row, DEC-0053/CR-0006, REQ-0007/REQ-0008/REQ-0011, CON-0001/CON-0002/CON-0010, RSK-0002 and applicable interfaces. Any contradiction or omitted ACC-0146 element reopens this candidate before PASS.
