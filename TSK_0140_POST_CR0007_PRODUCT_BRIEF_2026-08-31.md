# TSK-0140 — Current Product Brief — Post-CR-0007

**Task:** TSK-0140 — Issue the post-validation product brief  
**Acceptance:** ACC-0140  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Version:** 3.0.0-post-cr0007  
**Status:** CURRENT CANDIDATE FOR OBJECTIVE ACCEPTANCE  
**Date:** 2026-08-31  
**Authority:** DEC-0052/CR-0005 + DEC-0053/CR-0006 + DEC-0054/CR-0007 + current TSK-0146/TSK-0229/TSK-0141/TSK-0138 evidence

## 1. Acceptance and supersession boundary

This is the current implementation product brief after the Version-1 account-scope change and the CR-0007 autonomy/production-lifecycle change. It supersedes the 2026-08-30 post-CR-0006 TSK-0140 candidate as the current acceptance artifact.

The legacy task title says “post-validation,” but no real-parent/user behavioral validation is claimed. DEC-0052/CR-0005 intentionally moved first real-user validation until after LG-09. DEC-0054/CR-0007 then made that first real-user phase bounded live production rather than a separate pilot or staging lifecycle.

Current ACC-0140 is objective: this brief must faithfully translate the frozen current product, privacy, security, technical, commercial and sequencing authority into an internally consistent implementation brief; material scope changes remain separately owner-controlled; and objective evidence review must find no unresolved contradiction before PASS.

CR-0007 removed the prior ceremonial owner-review requirement for this in-scope objective task. That authority change does not itself create PASS. This exact persisted brief still requires fresh post-publication verification against ACC-0140.

## 2. Product objective

UseSafeWeb remains **First Phone Safety Setup**: a lightweight service for a parent/caregiver around a child’s first independently used smartphone. It coordinates a narrow, truthful and reversible safety setup across:

1. relevant native phone safeguards;
2. an encrypted AdGuard-backed baseline internet/DNS protection path; and
3. zero or one genuinely relevant external-service safeguard;

then presents a truthful Protection Map showing what is verified, parent-confirmed, action-needed, not covered, uncertain/error or removed.

The service is an orchestration/product layer, not a generic DNS administration product and not a surveillance suite.

## 3. Target user and evidence status

**Current target:** parent/caregiver responsible for setup around the first independently used smartphone transition, approximately ages 10–12, within the frozen initial UK orientation.

This is current product authority, not proof of behavioral demand, comprehension, completion, persistence, trust, account uptake, support burden or product-market fit. Those real-user questions remain unresolved until authorized L8 live-production evidence after LG-09.

## 4. Frozen Version-1 product shape

Version 1 is **dual-mode**:

- the complete core setup/protection journey remains usable **without login**; and
- an **optional parent account** provides secure sign-in/session capability, minimum parent/device ownership persistence and a lightweight dashboard/device-management experience.

The account option is continuity/management scope. It must never become a prerequisite for the core safety value unless the Project Owner later changes the frozen product boundary.

## 5. Required accountless core

The accountless path must support, without a UseSafeWeb login:

- public trust/landing entry explaining purpose, limits and how to start;
- minimum non-identifying setup routing context;
- supported platform setup paths;
- native-safeguards-first handling, including already-configured/not-applicable/skip states where valid;
- encrypted AdGuard-backed DNS setup using only currently approved supported mechanisms;
- technical protection verification that does not rely on account ownership;
- zero-or-one relevant external-service safeguard step when applicable;
- Protection Map state and material coverage-limit explanations;
- false-positive, conflict, unsupported-state, removal, reinstall/reconfiguration and recovery guidance;
- privacy-minimal troubleshooting;
- self-service help with exceptional escalation only;
- responsive, accessibility, localization and source-currency requirements.

## 6. Required optional parent-account capability

Version 1 must also support a parent choosing an account for bounded continuity and device-management functions:

- planned initial route: Google/Firebase social sign-in, subject to current L5 vendor/privacy/security/architecture verification;
- secure sign-in/session lifecycle requirements;
- minimal required parent identity data only for the approved account function;
- logout, revocation, expiry, recovery, error and deletion behavior;
- minimum parent/device ownership persistence;
- lightweight dashboard/device list;
- bounded device nickname/list plus add/setup/verify/reinstall/replace/revoke/remove flows;
- truthful device/protection status and Protection Map presentation;
- curated controls/help rather than raw AdGuard administration;
- account/device lifecycle behavior that does not conflate account deletion, anonymous-state deletion, DNS configuration removal or technical protection verification.

No password or SMS authentication is introduced by this brief. Exact provider identifiers, session implementation, persistent schema, retention, storage, access, backup, authorization, CSRF/IDOR/ClientID controls and deletion/recovery mechanics remain owned by their downstream L4/L5/L6/L7 tasks and gates.

## 7. Explicit Version-1 non-goals

Version 1 does **not** authorize:

- mandatory login for core safety value;
- browsing history, DNS-query history, visited-domain/top-domain/activity reporting;
- child accounts or persistent child/family behavioral profiles;
- unrestricted/raw customer-facing AdGuard administration;
- covert monitoring of messages, contacts, photos, location or social content;
- broad service catalogue or arbitrary app-control platform;
- GROW automation/AI parenting features;
- school/institution administration;
- community/UGC;
- native mobile app merely for convenience;
- full parental-control-suite scope;
- safety paywall or premium-protection tier;
- current checkout/payment collection as a prerequisite for core value;
- speculative high-availability/multi-node architecture as a product requirement;
- official non-UK market activation merely because localization capability exists;
- an alternative filtering backend absent the separate AdGuard reopen condition.

Any material change to these included/excluded product boundaries remains Project Owner authority.

## 8. Core journey and optional-account branching

The implementation baseline is:

1. **Discover / understand / trust / start.**
2. **Route** using minimum context.
3. **Phone** — guide relevant native safeguards first.
4. **Internet** — configure and technically verify the approved encrypted UseSafeWeb/AdGuard path.
5. **Service** — guide zero or one genuinely relevant external-service safeguard or show truthful not-applicable/not-covered state.
6. **Understand** — present Protection Map and material limits.
7. **Recover / remove** — provide supported false-positive, conflict, unsupported, removal, reinstall and reconfiguration paths.
8. **Optional continuity** — allow a parent to sign in and persist only the bounded account/device state authorized for Version 1.

The optional account must not block completion of steps 1–7. Exact account-entry placement and detailed interaction design remain downstream L4 UX decisions inside frozen scope.

## 9. Data, privacy and trust boundary

The accepted TSK-0229 accountless contract remains controlling for anonymous journey state:

- accountless J0/J1 state remains anonymous/short-lived under its current allowlist and expiry/deletion rules;
- the optional persistent parent-account domain is separate from J0/J1;
- no automatic J1-to-account join, conversion or promotion is authorized;
- any future explicit transfer requires a separately approved downstream dual-mode data-flow contract;
- account sign-in cannot extend anonymous-state expiry;
- account/device deletion, anonymous-state deletion and DNS configuration removal are distinct operations and must be represented truthfully;
- browsing/query/activity history and persistent child/family behavioral profiles remain prohibited;
- account/device ownership never substitutes for technical protection verification;
- diagnostics, logs and backups cannot become a hidden browsing-reporting path.

This brief does not claim final legal/privacy compliance. Actually applicable legal/privacy/consent requirements remain prerequisites at the consequential gate/action where they are required.

## 10. Security boundary

The product brief requires downstream architecture and implementation to prove, rather than assume:

- secure provider integration and session lifecycle;
- authentication and authorization boundaries;
- CSRF/session protections appropriate to the chosen implementation;
- ownership isolation and resistance to IDOR/ClientID-style cross-account/device access failures;
- logout/revocation/deletion/recovery behavior;
- minimum data and secret exposure;
- no customer exposure of AdGuard administrative credentials;
- account/device ownership separated from DNS protection-state proof;
- fail-safe behavior for provider/session outages and uncertain states.

Google/Firebase is a planned route only. Provider acceptance, exact implementation design and security/privacy suitability are not inferred by this L4 brief.

## 11. Technical/platform boundary

- AdGuard remains the frozen filtering backend unless the verified reopen condition is met.
- Encrypted DNS remains mandatory for supported protection paths.
- The product must represent only technically verified DNS/protection state and known limitations; it must not overclaim coverage because an account/device record exists.
- Platform-specific setup, verification, compatibility, certificate/network constraints, unsupported states, removal and recovery require current technical source/test evidence in their owning tasks.
- Account capability must not weaken or bypass the independent DNS/protection evidence model.
- Architecture, hosting, persistence, provider, recovery and release decisions remain subject to their L5-L7 requirements; this brief does not pre-approve them.

## 12. Accessibility, localization and content correctness

- Current accessibility target remains WCAG 2.2 AA under the owning requirements/evidence tasks.
- Accountless and account/dashboard surfaces share the same accessibility, responsive, error, recovery and truth-state expectations.
- English remains the baseline language; Turkish and Arabic/RTL technical capability may be prepared structurally, while each named official non-UK market activation remains separately Project Owner-controlled through LG-16.
- Device/service instructions and protection claims require current authoritative sources, explicit applicability, ownership and review triggers.
- No representative-parent usability/comprehension result is inferred before L8.

## 13. Support and operating model

Self-service remains the operating baseline:

- prevent avoidable failures through narrow supported paths and truthful limits;
- expose verification, troubleshooting, recovery and removal help at point of need;
- productize account/session failure and recovery rather than assuming routine staffed support;
- use privacy-minimal diagnostics only for facts they can technically establish;
- escalate only genuine exceptions or actual safety/security/privacy/legal/platform boundaries.

Real support burden remains unknown until live-production evidence exists.

## 14. Commercial boundary

- core safety value remains free;
- optional account capability is not a paywall;
- no payment method is required before value;
- any later supporter contribution remains post-value and separately controlled by current value, consumer/tax/privacy/security/provider/merchant/identity and authority prerequisites;
- paid acquisition is not a baseline dependency;
- this brief creates no payment, contract, merchant-account, spend or revenue authorization.

## 15. Current unresolved controls

The current TSK-0138 post-CR-0007 register controls unresolved product assumptions. Material implications for this brief are:

- UPA-001..008 and UPA-011 remain real-user behavioral unknowns, not L4-L7 blockers and not fabricated evidence;
- UPA-012 keeps named non-UK market activation owner-controlled;
- UPA-013 keeps payment conditional and non-authorized now;
- UPA-014 distinguishes routine technical scaling inside approved architecture/budget from material HA architecture/spend expansion;
- UPA-015 preserves actually applicable legal/privacy/contact prerequisites without asserting they are satisfied;
- UPA-016 keeps LG-06 non-PASS until every current objective L4 criterion is proven; LG-06 is AUTO_ALLOWED only after that proof;
- UPA-018 keeps UK public expansion unavailable until the full evidence sequence reaches LG-12 PASS and LG-13 AUTO-GO prerequisites;
- UPA-019 keeps advanced scope excluded;
- UPA-020 requires later contradictory direct evidence to reopen stale PASS rather than be reconciled away.

## 16. Lifecycle and gate sequencing

The current active product path is:

1. **L4 / LG-06 — Product, Brand and Experience Freeze.** Evidence-driven/AUTO_ALLOWED inside frozen scope; no PASS until every applicable L4 criterion is durably proven.
2. **L5 / LG-07 — Architecture, Security, Privacy and Delivery Readiness.** AUTO only on evidence-complete PASS.
3. **L6 / LG-08 — Build and Integration Complete.** AUTO for ordinary in-scope work; consequential/nondelegable exceptions remain separately controlled.
4. **L7 / LG-09 — Integrated Production Release Readiness.** Must prove current functional, device/network, UX/truth-state, accessibility/RTL, security/privacy, performance/capacity, self-service, recovery, operations, rollback, defects/residual risks and all actually applicable legal/privacy/consent prerequisites for live users.
5. **L8 — bounded live-production validation.** First real users occur only after LG-09 PASS and applicable prerequisites; bounded/capped/ramped rollout is a production-safety mechanism, not a separate pilot or staging environment.
6. **LG-10 — Initial Production Evidence Complete.** Production evidence must be sufficient for continuation evaluation.
7. **LG-11 — Initial Production Continuation Decision.** Automatically CONTINUE only when frozen thresholds pass; strategic non-proceed dispositions remain Project Owner authority.
8. **LG-12 — UK Public Production Readiness.** Evidence-driven/AUTO_ALLOWED.
9. **LG-13 — UK Public Production Activation.** AUTO-GO only when LG-12 and all current time-sensitive checks pass with no blocker.

There is no mandatory separate pilot/staging lifecycle. Local/dev/CI/synthetic/device/network/security/privacy/accessibility/performance/recovery/rollback verification remains mandatory before production as applicable.

## 17. Retained human authority

This brief does not narrow the current retained Project Owner/nondelegable boundaries. Human authority remains required where current authority says so, including:

- material frozen product/scope-policy change;
- activation of a named official non-UK market;
- organizational/entity/formalization decisions;
- new contracts;
- regulated fees;
- banking/merchant identity;
- legal attestations/signatures;
- material or unbudgeted spend;
- strategic modify/pivot/pause/stop/transfer/resume;
- genuinely irreversible acts requiring human authority.

Routine in-scope technical/design/remediation work does not gain a ceremonial human checkpoint merely because it is consequential in a generic sense; its current WBS/gate Action Authority controls.

## 18. Objective cross-functional contradiction review

This is an objective analytical review against current canonical authority, not fabricated human sign-off.

| Function | Current result | Boundary retained |
| --- | --- | --- |
| Product | **No unresolved canonical conflict found.** Dual-mode Version 1 matches DEC-0053, TSK-0146, TSK-0141 and current TSK-0138. | Material product-scope change remains owner-controlled. |
| Network | **No unresolved canonical conflict found.** Account scope does not change AdGuard/encrypted-DNS/technical-verification truth. | Platform-specific implementation and direct test evidence remain downstream. |
| Privacy | **No unresolved canonical conflict found.** Accountless/persistent separation, minimization, no-history and truthful deletion boundaries are explicit. | Persistent account schema/retention/storage/backup/data-flow and applicable legal prerequisites remain downstream. |
| Security | **No unresolved canonical conflict found.** Provider/session/authz/ownership/deletion/recovery requirements are preserved without pre-approving implementation. | L5-L7 security architecture/build/test acceptance remains mandatory. |
| UX | **No unresolved canonical conflict found.** Core remains login-free while optional account/dashboard scope is required. | Detailed interaction/prototype/accessibility acceptance remains downstream L4 work. |
| Support | **No unresolved canonical conflict found.** Self-service remains baseline and account/session recovery becomes product work. | Real support burden remains unknown until live production. |
| Commercial | **No unresolved canonical conflict found.** Core remains free; optional account is not a paywall; payment remains separately gated. | No payment/provider/merchant/spend authorization is created. |
| Governance/sequencing | **No unresolved canonical conflict found.** CR-0007 objective AUTO gates and production-only lifecycle are represented without inferring missing PASS. | Retained human/nondelegable boundaries remain explicit. |

## 19. Reconciliation from the 2026-08-30 TSK-0140 candidate

| Prior clause/state | Current disposition |
| --- | --- |
| `OWNER REVIEW REQUIRED` / Project Owner approval of this brief required for ACC-0140 | **SUPERSEDED by DEC-0054/CR-0007 and current WBS ACC/Action Authority.** TSK-0140 is A4 / AUTO_ALLOWED and requires objective evidence review, not ceremonial owner approval. |
| Historical owner approval of the pre-CR-0006 brief | Remains historical only and is not reused as current acceptance evidence. |
| Optional account/dashboard was newly introduced by CR-0006 | **RETAINED and current.** Accountless core + optional account/minimum persistence/lightweight dashboard-device management is the frozen Version-1 boundary. |
| Separate pilot/staging-era downstream language | **SUPERSEDED.** First real-user validation occurs as bounded live production after LG-09; no mandatory separate pilot/staging lifecycle exists. |
| LG-06 treated as a Project Owner decision | **SUPERSEDED.** LG-06 is objective evidence-driven/AUTO_ALLOWED, but remains non-PASS until all current criteria are proven. |
| Public UK launch treated as a separate owner GO | **SUPERSEDED for the frozen UK path.** LG-12 readiness and LG-13 GO are automatic only when every current prerequisite passes. |
| Downstream provider/schema/security/privacy/build facts not yet approved | **RETAINED.** This brief does not infer those downstream acceptances. |
| Behavioral evidence absent before L8 | **RETAINED.** Absence is intentional under DEC-0052 and no behavioral result is fabricated. |

## 20. Current disposition

**Artifact preparation:** COMPLETE.  
**Current objective contradiction review:** no unresolved canonical contradiction identified.  
**Behavioral evidence:** intentionally not claimed before L8.  
**LG-06 / downstream gates:** not inferred.  
**ACC-0140:** candidate for fresh independent post-publication verification only.

No task, gate, release, production, payment, publication or launch state changes solely because this brief exists.