# TSK-0140 — Post-CR-0006 Product Brief Candidate

**Task:** TSK-0140 — Issue the post-validation product brief  
**Acceptance:** ACC-0140  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** CANDIDATE / OWNER REVIEW REQUIRED / BEHAVIORALLY UNVALIDATED  
**Date:** 2026-08-30  
**Authority:** current TSK-0138 + TSK-0141 + TSK-0146 + DEC-0052/CR-0005 + DEC-0053/CR-0006

## 1. Acceptance and authority boundary

This is the current integrated product-brief candidate after the Version-1 account-scope change. It supersedes the 2026-08-28 TSK-0140 candidate for current acceptance because that artifact explicitly deferred accounts and a persistent parent dashboard.

ACC-0140 requires review by the Project Owner, product, network, privacy, security, UX, support and finance, with canonical conflicts resolved before approval. This candidate performs a current source-grounded cross-functional analytical review; it **does not fabricate Project Owner review/approval** of this exact revised brief.

No real-parent/user behavioral validation has occurred. Under DEC-0052/CR-0005, such validation is not a pre-product requirement and first begins only in L8 after LG-09. `RSK-0002` therefore remains OPEN. This brief does not authorize LG-06, architecture/build gates, participant processing, payment, publication or launch.

## 2. Product objective

UseSafeWeb is a lightweight **First Phone Safety Setup** service for a parent/caregiver around a child's first independently used smartphone. It helps establish sensible safeguards across:

1. relevant native phone safeguards;
2. an encrypted AdGuard-backed baseline internet/DNS protection path; and
3. at most one genuinely relevant external-service safeguard;

while making coverage limits and uncertainty explicit, avoiding surveillance, and remaining reversible/self-service.

Version 1 is **dual-mode**:

- the complete core setup/protection journey works **without login**; and
- an **optional parent account** provides minimum persistence and a lightweight dashboard/device-management experience.

## 3. Target user and evidence status

**Current target:** parent/caregiver responsible for setup around a child's first independently used smartphone transition, approximately ages 10–12, initially oriented to the UK/England context.

This remains an owner-authorized product assumption, not validated demand or behavior. No claim is made about completion, trust, comprehension, persistence, account uptake, support burden, preference or product-market fit before L8 evidence.

## 4. Core product proposition

UseSafeWeb remains a narrow orchestration layer rather than a generic DNS product or parental-surveillance suite:

- **Phone:** guide relevant native safeguards first and recognize already-configured/not-applicable states.
- **Internet:** guide activation and verification of the approved encrypted AdGuard-backed baseline.
- **Service:** guide zero or one genuinely relevant external-service safeguard when applicable.
- **Truth:** show Protection Map states that distinguish technically verified, parent-confirmed, action-needed, not-covered, uncertain/error and removed states.
- **Recovery:** provide supported removal, reinstall/reconfiguration, false-positive and compatibility recovery paths.
- **Optional continuity:** allow a parent to choose an account for minimum device ownership/persistence and lightweight device management without making login a prerequisite for core protection value.

## 5. Required Version-1 scope

### 5.1 Accountless core — required

The following remain fully usable without a UseSafeWeb account:

- public trust/landing entry explaining purpose, limits and start path;
- minimum non-identifying setup routing context;
- supported Android/iPhone setup paths;
- native-safeguards-first flow with already-configured/skip handling;
- encrypted AdGuard-backed DNS setup and truthful technical verification;
- one relevant service safeguard where applicable;
- Protection Map / protection-state model and material coverage-limit explanations;
- removal/recovery/reinstall/reconfiguration guidance;
- privacy-minimal troubleshooting and false-positive/compatibility help;
- self-service help with exceptional escalation only;
- responsive/accessibility/localization/content-source requirements.

### 5.2 Optional parent account — required capability in Version 1

Version 1 must also support a parent choosing an account for bounded continuity features:

- planned initial sign-in route: Google social sign-in; no password/SMS authentication is introduced without later authority;
- secure account/session lifecycle requirements, including sign-in, logout/revocation/deletion and truthful expiry/recovery/error states;
- minimal parent identity fields only as required for the approved sign-in/account function;
- minimum parent/device ownership persistence;
- lightweight parent dashboard/device list;
- device nickname/list plus bounded add/setup/verify/reinstall/replace/revoke/remove flows;
- truthful protection/device status and Protection Map presentation;
- curated product controls/help rather than raw AdGuard administration;
- account lifecycle, deletion and recovery behavior that does not misrepresent DNS configuration removal or anonymous-state deletion.

Exact authentication/session fields, UX placement, provider/privacy/security architecture, persistent schema, retention, storage, access, backup and authorization mechanics belong to their downstream L4/L5/L6/L7 tasks and are **not approved by this brief**.

## 6. Explicit non-goals

Version 1 does **not** authorize:

- mandatory login for core safety value;
- browsing history, DNS-query/visited-domain/top-domain/activity reporting;
- child accounts, child behavioral profiles or surveillance data;
- unrestricted/raw customer-facing AdGuard administration;
- covert monitoring of messages, contacts, photos, location or social content;
- broad service catalogue/arbitrary app-control platform;
- GROW automation/AI parenting, school/institution administration, community/UGC or native mobile app;
- full parental-control suite;
- safety paywall/premium protection tier;
- current payment checkout or paid-acquisition dependency;
- HA/multi-node infrastructure as a current product requirement;
- official non-UK market activation merely because localized UI/content exists;
- alternative filtering backend absent the separate AdGuard reopen condition.

## 7. Dual-mode journey boundary

The baseline journey remains:

1. **Discover / understand / trust / start.**
2. **Route** with minimum context.
3. **Phone** — relevant native safeguards first.
4. **Internet** — configure and verify the approved encrypted UseSafeWeb/AdGuard path.
5. **Service** — one relevant service safeguard or truthful not-applicable/not-covered state.
6. **Understand** — Protection Map and material limits.
7. **Recover** — false-positive/conflict/unsupported/removal/reconfiguration help.
8. **Optional continuity** — a parent may choose account sign-in to persist only the bounded parent/device state authorized for V1.

The account branch must never block completion of steps 1–7. Exact account-entry timing and interaction design are downstream UX decisions and are not silently chosen here.

## 8. Data, privacy and trust boundary

- Accountless J0/J1 journey state remains anonymous/short-lived under the accepted TSK-0229 contract.
- The optional persistent account domain is separate from J0/J1; **no automatic anonymous-state-to-account join/conversion/promotion is authorized** by this brief.
- Any future explicit transfer between anonymous journey state and an account requires its own approved downstream dual-mode data-flow contract.
- Account sign-in cannot extend anonymous J1 expiry.
- Account/device deletion, anonymous-state deletion and DNS configuration removal are distinct operations and must be represented truthfully.
- No browsing/query/activity history or persistent child/family behavioral profile is permitted.
- Account/device ownership never substitutes for technical Protection Map verification.
- Diagnostics/logging/backups remain separately governed and cannot become a hidden browsing-reporting path.

## 9. Technical/platform boundary

The optional account capability does not alter the frozen DNS-protection identity:

- AdGuard remains the filtering backend absent a verified critical blocker;
- Android baseline uses the supported native Private DNS/DoT path where applicable;
- iPhone baseline uses the approved DoH Server URL/profile path;
- verification, certificate, fallback/failure, removal/recovery and environment truth remain explicit;
- VPN, Private Relay, custom DNS, captive portal, managed-network and other known limitations remain surfaced rather than hidden.

Authentication/provider architecture must not weaken or bypass the independent DNS/protection evidence model.

## 10. Accessibility, localization and content correctness

- WCAG 2.2 AA remains the current target with keyboard/focus, semantic/screen-reader, resize/reflow, contrast/target/motion, responsive and RTL acceptance.
- English is baseline; Turkish and Arabic/RTL technical capability is required structurally, while official market activation remains separately gated.
- Device/service instructions and protection claims require current authoritative sources, explicit applicability, ownership and review triggers.
- Account/login/dashboard surfaces inherit the same accessibility/localization/truth requirements as the accountless core.

No representative-parent usability/comprehension or non-UK market readiness is claimed.

## 11. Support and operating model

Self-service remains the operating baseline:

- prevent avoidable failure through narrow supported paths and clear limits;
- expose verification/troubleshooting/recovery/removal help at point of need;
- account/session errors and recovery must be productized rather than assumed to require routine staffed support;
- use privacy-minimal diagnostics only for facts they can technically verify;
- exceptional human/specialist escalation remains bounded to genuine exceptions or safety/security/legal/safeguarding boundaries.

Real support burden remains unknown until L8.

## 12. Commercial boundary

- core protection remains free;
- the optional account is not a paywall for safety value;
- no current supporter checkout is part of this L4 brief;
- any later supporter payment remains post-value and separately gated by evidence, legal/tax/privacy/security/provider readiness and Project Owner authority;
- paid acquisition is not a baseline dependency.

## 13. Current unresolved constraints

Use the current post-CR-0006 TSK-0138 register. In particular:

- UPA-001..008 remain behavioral unknowns for L8 after LG-09;
- UPA-009/010 are resolved/superseded as open decisions: optional V1 account + bounded dashboard are now required while accountless core remains required;
- UPA-011 brand/trust remains behaviorally unknown;
- UPA-012 market activation, UPA-013 payment, UPA-014 HA and UPA-015 legal/participant readiness retain their own triggers;
- UPA-016 LG-06 remains a Project Owner decision after the revised account-inclusive L4 evidence is complete;
- historical UPA-017 is superseded: build no longer waits for pre-product behavioral evidence, but current product/architecture/build gates still apply;
- UPA-018/019/020 keep launch, advanced-scope and contradiction-reopen controls intact.

## 14. Current cross-functional analytical review

This is an analytical conflict check, **not fabricated human reviewer sign-off**.

| Function | Current analytical result | Material boundary |
| --- | --- | --- |
| Product | **No canonical conflict found.** Dual-mode V1 matches DEC-0053, TSK-0146 and current TSK-0141/0138. | Detailed account requirements and UX remain downstream. |
| Network | **No canonical conflict found.** Account scope does not change AdGuard/encrypted-DNS/verification truth. | Account ownership cannot substitute for DNS verification. |
| Privacy | **No canonical conflict found.** Accountless J0/J1 separation, minimum account data and no-history/no-child-profile rules are explicit. | Persistent account schema/retention/storage/backup/data flow require downstream approval. |
| Security | **No canonical conflict found.** Google sign-in is planned, no password/SMS is introduced, and session/authz controls remain mandatory downstream. | Provider/session/CSRF/authz/IDOR/ClientID/deletion/recovery verification is not yet approved. |
| UX | **No canonical conflict found.** Account is optional and core journey remains login-free. | Exact sign-in placement, dashboard interaction and account-recovery UX require downstream decisions/verification. |
| Support | **No canonical conflict found.** Self-service remains baseline; account/session recovery becomes product work. | Real support burden remains unknown until L8. |
| Finance | **No canonical conflict found.** Core remains free; account is not a paywall; payment activation remains separate. | No payment/revenue authorization is created. |

## 15. Owner review packet for ACC-0140

Project Owner review should confirm or reject this **exact current candidate** on these points:

1. Version 1 is correctly represented as accountless core + optional parent account/lightweight dashboard/device management.
2. Account capability is useful continuity scope, not mandatory login or surveillance.
3. Google social sign-in is the planned route but downstream vendor/privacy/security architecture remains separately gated.
4. Mandatory login, browsing/query/activity history, child accounts/profiles and raw DNS administration remain excluded.
5. Accountless J0/J1 and persistent account state remain separate unless a downstream explicit transfer contract is approved.
6. Account ownership never substitutes for technical protection verification.
7. Cross-functional product/network/privacy/security/UX/support/finance boundaries contain no unresolved canonical conflict blocking brief approval.
8. The brief is approved only as an internal L4 product brief; it does not imply behavioral validation, LG-06, build, participant, payment, publication or launch PASS.

Historical owner approval of the 2026-08-28 brief is not reused as approval of this materially revised candidate. DEC-0053 approves the account-scope decision, but ACC-0140 still requires review of the integrated current brief.

## 16. Candidate disposition

**Preparation:** COMPLETE.  
**Current analytical cross-functional review:** no canonical conflict identified.  
**ACC-0140:** **NOT YET PASS — PROJECT OWNER REVIEW OF THIS CURRENT CANDIDATE REQUIRED.**

Until explicit owner approval/rework is recorded, TSK-0140 remains non-PASS and TSK-0312 remains dependency-blocked.
