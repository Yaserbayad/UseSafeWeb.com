# TSK-0140 — Provisional Product Brief Candidate

**Canonical task title:** `TSK-0140 — Issue the post-validation product brief`  
**Task status represented by this artifact:** **CANDIDATE / UNAPPROVED / BEHAVIORALLY UNVALIDATED**  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Date:** 2026-08-28  
**Authority:** `DEC-0050` / `CR-0003` plus current accepted L4 evidence  

## 1. Acceptance and authority boundary

This artifact prepares the product brief required by TSK-0140. It **does not satisfy ACC-0140 by itself** and must not be called approved or behaviorally post-validation.

ACC-0140 requires the brief to be reviewed by the Project Owner, product, network, privacy, security, UX, support and finance, with conflicts against canonical decisions resolved before approval. This candidate performs a source-grounded cross-functional **pre-review** only; it does not fabricate Project Owner approval or any human/specialist review that has not actually occurred.

No real-participant Experiment-1 behavioral validation has occurred. `LG-03`, `LG-04`, `LG-05` and `LG-06` remain non-PASS. `RSK-0002` remains OPEN. `REQ-0022` remains intentionally unresolved under the owner legal hold. This brief does not authorize L5/L6 build, participant processing, legal completion, payment activation, public publication or launch.

## 2. Product objective

Define the smallest coherent **UseSafeWeb First Phone Safety Setup** experience that helps a parent/caregiver around a child's first independently used smartphone establish sensible safeguards across:

1. the phone's native safeguards;
2. an encrypted AdGuard-backed internet/DNS baseline; and
3. at most one genuinely relevant external-service safeguard;

while making protection limits and uncertainty explicit and avoiding surveillance, browsing-history features, mandatory account creation and unnecessary operational complexity.

The desired outcome is a coherent, reversible and self-service-oriented first-phone setup experience that can later be behaviorally validated and, only after downstream gates, implemented.

## 3. Target user and evidence status

**Provisional target:** parent/caregiver responsible for setup around a child's first independently used smartphone transition, approximately the 10–12 life stage, initially oriented to the UK/England context.

**Evidence status:** owner-authorized product assumption, not validated demand or behavior. No claim is made about completion rate, willingness to use, trust, comprehension, persistence, support burden, preference or product-market fit.

## 4. Product proposition

UseSafeWeb should function as a narrow orchestration layer rather than a generic DNS product or parental-surveillance suite:

- **Phone:** guide relevant native safeguards first and skip correctly configured/not-applicable work.
- **Internet:** guide activation and verification of the approved encrypted AdGuard-backed baseline protection path.
- **Service:** guide zero or one genuinely relevant external-service safeguard when applicable.
- **Truth:** show a Protection Map that distinguishes system-verified, parent-confirmed, action-needed, not-covered, uncertain/error and removed states.
- **Recovery:** make supported removal, reinstall/reconfiguration, false-positive, compatibility and recovery paths understandable.

This proposition is provisional until real-parent evidence exists.

## 5. Active minimum scope

The provisional first-product scope is accountless-first and includes only capabilities already accepted by current L4 authority:

- public trust/landing entry that explains purpose, limits and start path;
- accountless start with no mandatory UseSafeWeb login;
- minimum non-identifying setup routing context;
- supported Android and iPhone platform-specific setup paths;
- native-safeguards-first routing with already-configured/skip behavior;
- encrypted AdGuard-backed DNS setup and technically truthful verification;
- one relevant service safeguard where actually applicable;
- Protection Map / protection-state model;
- explicit coverage-limit explanations;
- removal, recovery and reinstall/reconfigure guidance;
- privacy-minimal troubleshooting and false-positive/compatibility help;
- self-service help with exceptional escalation only;
- responsive/accessibility requirements and truthful error/uncertain/recovery states;
- coherent brand/design/terminology structure across public and setup surfaces;
- externalized/localizable content architecture for English, Turkish and Arabic/RTL capability without implying official non-UK market activation;
- current-source/version ownership for technical instructions and protection claims;
- privacy-minimal transient journey state without mandatory persistent identity.

## 6. Explicit non-goals and deferred scope

The active product does **not** include, unless separately reauthorized through its exact trigger/gate:

- mandatory authentication, Google sign-in or another customer login;
- persistent parent dashboard or persistent device list;
- customer-facing AdGuard administrative/control plane;
- browsing/DNS-query/top-domain/activity history;
- covert monitoring or message/contact/photo/location/social-content surveillance;
- child account, child app, persistent family/child behavioral profile;
- broad service catalogue or arbitrary app-control platform;
- GROW lifecycle automation or AI parenting automation;
- school/institution administration or community/UGC;
- native mobile application;
- full parental-control suite;
- safety-feature paywall or premium protection tier;
- current supporter-payment checkout;
- paid-acquisition machinery;
- HA/multi-node infrastructure as a current product requirement;
- official non-UK market activation merely because localized content exists;
- broad/raw DNS administration or an alternative filtering backend;
- persistent identifiable child/family analytics or behavioral monetization.

## 7. End-to-end journey baseline

The current provisional journey is:

1. **Discover / understand / trust / start.** Explain what UseSafeWeb does and does not do.
2. **Route.** Collect only the minimum accountless context required to choose a supported path.
3. **Phone.** Present applicable native safeguards first; support already-configured/not-applicable states.
4. **Internet.** Configure and verify the approved encrypted UseSafeWeb DNS path using platform-correct mechanisms.
5. **Service.** Offer at most one parent-declared/currently eligible external-service safeguard or show `not applicable/not covered`.
6. **Understand.** Present truthful Protection Map states and material limitations.
7. **Recover.** Offer false-positive, conflict, unsupported, removal and reconfiguration help.
8. **Finish quietly.** No mandatory account, payment ask, engagement loop or surveillance dashboard.

Journey ordering, wording, comprehension and real completion remain behaviorally unvalidated under `RSK-0002`.

## 8. Technical and platform contract

Current accepted technical design preserves one UseSafeWeb DNS service identity while using platform-specific configuration mechanisms rather than a false universal FQDN workflow:

- Android supported baseline: native Private DNS using the approved DoT hostname semantics where the supported OS/device/network conditions hold.
- iPhone supported baseline: approved DoH Server URL/profile mechanism under the current supported iOS matrix.
- verification truth, certificate expectations, removal/recovery, fallback/failure behavior and environment separation must remain explicit.
- currently accepted support baseline is limited to tested/specified Android 9+ native Private DNS and iPhone/iOS 14+ approved manual DoH-profile paths; untested device families/networks remain not-yet-supported.
- VPN, Private Relay, browser/app custom DNS, captive-portal, managed-network, transport-blocking and IPv6-only/NAT64 limitations remain explicit rather than hidden.

AdGuard remains the frozen filtering backend absent a verified critical blocker. Current accepted upstream/ECS policy remains authoritative and is not redefined by this brief.

## 9. Data, privacy and trust contract

The product remains privacy-minimal and non-surveillance:

- no persistent identity is required for the immediate active journey;
- persistent parent/child/family profiles are prohibited in the current baseline;
- browsing history, DNS query history, visited-domain activity, top-domain reporting and child behavioral surveillance are not product features or success metrics;
- technical verification and parent confirmation remain distinct evidence classes;
- transient journey state must follow the accepted expiry/deletion/no-linkage contract;
- diagnostics/logging/backups remain separately governed and may not become a hidden browsing-reporting path;
- unknown, not-covered, action-needed and error states must be surfaced rather than replaced with false certainty;
- no complete-safety or universal-protection claim is permitted.

## 10. Protection-state and claims rules

Parent-facing state must preserve the accepted protection-state model:

- **Protected / verified** only when the applicable technical evidence threshold is actually satisfied;
- **Configured / parent-confirmed** when the state is based only on the parent's confirmation or configuration presence without sufficient system verification;
- **Action needed** when a correctable step remains;
- **Not covered** for unsupported/non-applicable protection areas;
- **Uncertain / error** when evidence is insufficient or conflicting;
- **Removed** when the supported protection path has been intentionally removed.

Parent confirmation, profile presence or synthetic rehearsal must never masquerade as system verification or behavioral validation.

## 11. Accessibility, localization and content correctness

- WCAG 2.2 AA is the current target requirement, with keyboard/focus, semantic/screen-reader, resize/reflow, contrast/target/motion, responsive and RTL behaviors defined for later implementation/testing.
- English is the baseline content language; Turkish and Arabic/RTL technical capability is required structurally, while official market activation remains separately gated.
- device/service instructions and protection claims require current authoritative sources, explicit platform/version/region applicability, ownership and review triggers.
- unsupported and stale-guidance states must fail truthfully rather than silently presenting outdated instructions.

No implemented accessibility conformance, representative-parent usability, translation quality or non-UK market readiness is claimed by this brief.

## 12. Support and operating model

The accepted direction is self-service first:

- prevent avoidable failures through narrow supported paths and clear limitations;
- expose verification, troubleshooting, false-positive, compatibility, recovery and removal help at the point of need;
- use privacy-minimal diagnostics and automated checks only for facts they can technically verify;
- reserve human/specialist escalation for genuine exceptions, safety/security/legal/safeguarding boundaries or unresolved cases;
- do not create a routine staffed-support model to compensate for unvalidated UX friction.

Actual parent assistance burden and real failure incidence remain unknown until behavioral testing.

## 13. Commercial and cost boundary

- the core protection product remains free;
- no current paywall or supporter checkout is part of this L4 product brief;
- any future supporter-payment flow remains optional, post-value and separately gated by value, legal/tax/privacy/security/provider readiness and owner authority;
- paid acquisition is not a baseline dependency;
- current product definition must stay lean and reversible rather than create implementation commitments to compensate for missing validation evidence.

## 14. Current unresolved assumptions that materially constrain the brief

The following remain open and cannot be converted into positive product claims:

- parent completion/value of the full first-phone orchestration (`UPA-001`);
- exact target-segment fit (`UPA-002`);
- whether native-first reduces rather than adds work (`UPA-003`);
- incremental value of the one-service step (`UPA-004`);
- Protection Map / coverage-limit comprehension (`UPA-005`);
- self-service assistance burden (`UPA-006`);
- 14-day persistence (`UPA-007`);
- real false-positive/compatibility burden (`UPA-008`);
- future need for persistent account/dashboard (`UPA-009/010`, EXC-0001);
- real-parent trust/clarity of brand/language (`UPA-011`);
- legal readiness for participants/public operation (`UPA-015`);
- LG-06/build authority (`UPA-016/017`).

Any direct contradictory evidence must reopen affected provisional downstream PASS rather than being reconciled away.

## 15. Cross-functional pre-review

This section is an analytical conflict check, **not fabricated reviewer sign-off**.

| Function | Pre-review result | Current material boundary |
| --- | --- | --- |
| Product | **No canonical conflict found.** Brief matches TSK-0139/0141 minimum proposition and preserves unresolved assumptions. | Behavioral value/fit remains unvalidated. |
| Network | **No canonical conflict found.** Brief preserves AdGuard, encrypted DNS, platform-specific Android/iPhone mechanisms and known-limit semantics. | No new endpoint/config/build authority; public-ingress abuse gap remains separately open where relevant. |
| Privacy | **No canonical conflict found.** Accountless/minimization/no-history/no-linkage boundaries are preserved. | `REQ-0022` and deferred legal/privacy readiness remain unresolved; no participant/public readiness inferred. |
| Security | **No canonical conflict found.** No mandatory account, unrestricted admin interface, secret exposure or surveillance scope is introduced. | Existing security deviations/gaps remain separately controlled; this brief does not close them. |
| UX | **No canonical conflict found.** Service blueprint, friction budget, truth states, accessibility and platform asymmetry are preserved. | `TSK-0317` is HUMAN_ONLY; representative-parent comprehension/usability remains unavailable. |
| Support / Customer Experience | **No canonical conflict found.** Self-service, recovery/removal and exceptional-escalation model are preserved. | Real support burden remains unknown; no staffed-support commitment is introduced. |
| Finance | **No canonical conflict found.** Free core, no current payment activation, no paid-acquisition dependency and lean reversible design are preserved. | Future payment/cost decisions remain separately gated and owner-controlled. |

The prior TSK-0043 cross-functional requirements review independently found no unresolved critical requirement contradictions across the current baseline; its two controlled interpretation items (`NCF-0043-01`, `NCF-0043-02`) remain applicable.

## 16. Review packet for ACC-0140

A reviewer should explicitly confirm or reject the following without treating provisional assumptions as validated facts:

1. the product objective and target-user assumption are correctly represented as provisional;
2. the active minimum scope is complete enough for current L4 definition but not expanded beyond TSK-0141;
3. non-goals/deferred exceptions are correctly preserved;
4. technical/platform statements do not exceed current accepted evidence;
5. privacy/no-surveillance/accountless boundaries are correct;
6. protection-state/claims rules are truthful;
7. support/operational assumptions are not presented as observed behavior;
8. commercial/payment/market boundaries are correct;
9. all material conflicts with current canonical decisions have been identified/resolved;
10. the brief may be approved as a **provisional internal L4 product brief**, not as behavioral post-validation evidence or build authorization.

## 17. Candidate disposition

**Preparation status:** COMPLETE.  
**Cross-functional analytical pre-review:** no canonical conflict identified across product, network, privacy, security, UX, support and finance lenses.  
**ACC-0140:** **NOT YET PASS**. Mandatory Project Owner review/approval has not been evidenced, and this artifact does not fabricate it. Any additional reviewer/sign-off requirement not demonstrably satisfied by the analytical pre-review also remains open.

**Next required evidence:** Project Owner review of this exact candidate (or an owner-authorized corrected revision), including explicit disposition of any material conflict or requested change and confirmation of what reviewer/sign-off evidence satisfies ACC-0140. Until then, TSK-0140 must remain non-PASS.
