# TSK-0149 — Distinct Public Website and Product/Setup Outcomes — Post-CR-0007

**Task:** TSK-0149 — Freeze the distinct public website and product/setup outcomes  
**Acceptance:** ACC-0149  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Version:** 1.0.0-post-cr0007  
**Date:** 2026-08-31  
**Status:** CURRENT CANDIDATE FOR INDEPENDENT ACCEPTANCE  
**Authority:** current TSK-0146 / TSK-0140 / TSK-0142 + DEC-0053/CR-0006 + DEC-0054/CR-0007

## 1. Frozen outcome split

UseSafeWeb has one brand and one coherent design system, but two distinct user outcomes:

1. **Public website outcome — discover / understand / trust / decide / start.**
2. **Product/setup outcome — start / configure / verify / understand / recover/manage.**

The public website explains and routes. The product/setup experience performs the operational safety journey and, when the parent chooses it, provides bounded account continuity and device management.

The distinction is functional, not a requirement for separate brands, repositories, domains, applications or design systems.

## 2. Public website outcome

The public website must let a parent:

- understand the First Phone Safety Setup proposition and its limits;
- understand the Phone / Internet / Services model and truthful Protection Map concept without implying complete safety;
- understand current compatibility, privacy/non-surveillance principles and self-service help at an appropriate summary level;
- decide whether to begin the setup journey;
- start the accountless core directly without creating an account or providing payment details;
- optionally reach account sign-in/return where current IA later places that utility, without making it the primary gate to core value.

The public website must not:

- create or imply technical protection state merely because content was viewed;
- contain a mandatory signup/payment step before the core setup journey;
- expose raw AdGuard administration or browsing/query/activity history;
- become the authoritative source for platform procedures, Protection Map state semantics, privacy controls or account lifecycle when another owning contract exists;
- imply that Turkish/Arabic technical availability equals official non-UK market activation.

## 3. Product/setup outcome

The product/setup experience must let a parent:

- intentionally start and route to a supported setup path;
- configure applicable native phone safeguards;
- configure and technically verify the approved encrypted UseSafeWeb DNS path;
- handle zero or one relevant external-service safeguard where applicable;
- understand current Phone / Internet / Services evidence through the truthful Protection Map;
- troubleshoot supported failures, false positives, unsupported/uncertain states and service/provider outages;
- reinstall/reconfigure, remove and recover safely;
- complete the entire core safety journey without login;
- optionally sign in for bounded continuity, session/account lifecycle, minimum device ownership persistence and lightweight dashboard/device management under current TSK-0312/TSK-0142 requirements;
- distinguish account/device-record lifecycle from physical DNS configuration/removal and from technical protection verification.

The product/setup experience must not turn account ownership, dashboard presence or historical setup state into current technical verification.

## 4. Handoff contract

The public-to-product handoff must satisfy all of the following:

- **Start setup** is a clear transition from information/decision to operational work.
- The handoff does not require login, payment, child identity or browsing data.
- Public content does not silently create a persistent parent/device record.
- Product/setup state does not need to be encoded into public URLs, marketing analytics or public content.
- Returning to public information/help must not mutate protection state.
- Optional sign-in/return may be available as a bounded utility, but the accountless core remains independently reachable.

Exact routes/navigation placement remain owned by current TSK-0328 and downstream UX work.

## 5. One brand and design system

Both outcomes must use the same approved UseSafeWeb brand/design system:

- shared identity, typography, color/token system, icon/imagery language and voice;
- shared accessibility, responsive and localization principles;
- shared evidence-strength/trust language and no-complete-safety rule;
- shared components/patterns where their semantics are the same.

The two outcomes may use different navigation density, task hierarchy and interaction patterns because their jobs differ. That difference must not create a second visual identity or conflicting product vocabulary.

## 6. Ownership and duplication rules

The public website owns explanation, trust, decision support and the start handoff. The product/setup surface owns operational state and actions.

Neither surface may fork authoritative facts owned elsewhere. In particular:

- platform setup and verification details remain source-backed by their owning technical requirements;
- Protection Map/evidence-state meaning remains owned by the current state contracts;
- account/session/minimum-intake behavior remains owned by TSK-0312;
- lightweight dashboard/device-management behavior remains owned by TSK-0142;
- accountless J0/J1 versus persistent-account separation remains owned by TSK-0229;
- actual legal/privacy notices remain owned by the applicable privacy/legal publication work.

A summary may exist on another surface, but it must link/reuse current authority rather than become a second mutable definition.

## 7. Required normal and exception outcomes

The outcome split must remain valid for:

- normal supported accountless setup;
- optional account sign-in/return and dashboard continuity;
- provider/sign-in outage while accountless core remains usable;
- unsupported/not-covered platform or service;
- uncertain/failed verification;
- false-positive/support path;
- reinstall/reconfiguration;
- removal and post-removal recovery;
- session expiry/revocation/account deletion;
- device replace/revoke/remove lifecycle;
- lost transient accountless state.

The public website remains informational during those conditions; operational state resolution remains in the product/setup experience or owning external platform flow.

## 8. Explicit non-goals

This freeze does not authorize:

- a second brand/design system;
- separate contradictory public/product terminology;
- mandatory login for core safety value;
- browsing/query/activity history;
- child accounts or surveillance dashboards;
- unrestricted customer DNS administration;
- payment gating of core value;
- provider/vendor/security architecture acceptance;
- implementation/build/deployment/publication or any gate PASS.

## 9. Deterministic acceptance assertions

A later IA/design/build review must be able to prove:

1. A parent can discover, understand, evaluate and start from the public outcome without creating protection state.
2. A parent can enter and complete the core product/setup journey without login.
3. Operational configure/verify/Protection Map/recovery actions occur in the product/setup outcome, not the public information outcome.
4. Optional sign-in/return/dashboard continuity exists without becoming a gate to core value.
5. Public and product/setup surfaces use one coherent brand/design system.
6. Shared terminology and evidence strength do not conflict across surfaces.
7. Public informational navigation cannot silently mutate product protection state.
8. Returning to informational help cannot manufacture verification.
9. No mandatory payment, child identity, browsing history or raw DNS administration is introduced by the handoff.
10. Exact navigation/routes remain downstream and can evolve without changing this functional outcome split.

## 10. ACC-0149 disposition

ACC-0149 requires requirements that clearly separate **discover / understand / trust / decide / start** from **start / configure / verify / understand / recover** while preserving one brand/design system.

Sections 1–9 define that separation, extend the product side to the current optional-account/dashboard scope without gating the accountless core, and preserve one coherent brand/design system.

**Candidate disposition:** ACC-0149 is ready for independent post-publication verification. TSK-0149 remains non-PASS until that verification and durable runtime reconciliation succeed.
