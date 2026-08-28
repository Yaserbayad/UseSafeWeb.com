# TSK-0141 — Provisional Minimum Product Scope and Non-Goals

**Task:** TSK-0141 — Freeze minimum product scope and non-goals  
**Acceptance:** ACC-0141  
**Lifecycle:** L4 — Product Definition, Requirements & Experience Design  
**Status:** PROVISIONAL SCOPE FREEZE / INTERNAL / BEHAVIORALLY UNVALIDATED  
**Date:** 2026-08-28  
**Authority:** TSK-0139 + DEC-0050/CR-0003 + current owner-frozen decisions  

## 1. Scope-freeze boundary

This document freezes the **smallest provisional first-product scope for L4 definition/design**. It does not authorize implementation, integrated build, participant use, legal completion, payment activation, public launch or LG-06 PASS.

**No real-participant behavioral validation has occurred.** Capabilities derived from assumed parent needs are explicitly marked **P — provisional/unvalidated**. They are not called validated, proven, preferred or user-tested.

`RSK-0002` remains OPEN. Real behavioral evidence may later require scope reduction, modification, reordering or pivot.

## 2. Inclusion test

A capability belongs in the provisional minimum product only if at least one of these bases applies and no stronger constraint excludes it:

- **O — Owner-approved:** directly required by a current explicit owner decision/frozen architectural or product baseline.
- **M — Mandatory:** necessary for current safety, privacy, security, technical correctness, truthful state, recovery, accessibility, or basic operability of the approved concept.
- **P — Provisional/unvalidated need:** a conservative, reversible capability needed to express/test the current product hypothesis, explicitly subject to later real-user validation.

A capability is excluded when it is not needed for the minimum journey, materially increases identity/data/operational complexity without current evidence, violates a frozen non-goal, belongs to a deferred exception, or depends on behavioral evidence that does not exist.

## 3. Frozen provisional first-product statement

The first product is an **accountless-first UseSafeWeb First Phone Safety Setup experience** that helps a parent move through a narrow Phone → Internet → one relevant Service journey, activates/verifies the approved encrypted AdGuard-backed baseline-protection path, presents truthful protection/coverage states, and provides understandable recovery/removal guidance without surveillance, browsing-history features or unrestricted DNS administration.

The public website/trust surface and setup/product surface share one brand/design system but remain distinct user surfaces. Persistence, accounts and a parent dashboard are not required in the active baseline.

## 4. Included minimum capabilities

| ID | Capability | Basis | Why it is in the minimum | Evidence/authority boundary |
| --- | --- | --- | --- | --- |
| MIN-01 | Public trust/landing entry that explains UseSafeWeb, intended first-phone job, major limits and how to start | O + M | DEC-0001/0002/0007/0008 freeze identity, product framing, SAFE INDEPENDENCE and trust posture; truthful expectation-setting is mandatory | Does not prove that the positioning converts or is preferred |
| MIN-02 | Accountless start and setup journey with no mandatory UseSafeWeb login | O | DEC-0042 and TSK-0146 explicitly freeze accountless-first | Does not prove parents prefer accountless use |
| MIN-03 | Minimal non-identifying setup routing inputs needed to choose supported path, such as device family and relevant setup branch | M + P | A setup flow cannot route correctly without minimum context; data minimisation constrains collection | Exact field usability/wording remains unvalidated |
| MIN-04 | Supported iPhone/Android path selection and current platform-specific setup instructions | O + M | Current product/device decisions and technical acceptance already support both intended families; correct instructions are necessary to operate | Parent ability to follow instructions remains unvalidated |
| MIN-05 | Native-safeguards-first flow with explicit already-configured / skip handling | O + P | DEC-0009 freezes native-first shape; avoiding forced repetition is part of the current hypothesis | Incremental value and friction reduction remain unvalidated |
| MIN-06 | Approved encrypted baseline DNS-protection setup path backed by AdGuard | O + M | AdGuard and encrypted DNS are frozen; current technical evidence proves viable supported paths | This proves technical feasibility, not product value |
| MIN-07 | Baseline-protection verification and truthful failure/uncertain state | M | Product must not claim protection without evidence; technical failures and unsupported states require safe truth | Presentation/comprehension remains unvalidated |
| MIN-08 | One genuinely relevant service-safeguard guidance branch, with `not applicable/not covered` instead of artificial completion | O + P | DEC-0009 freezes one-relevant-service shape and bounded orchestration hypothesis | Whether users value this incremental service layer remains unvalidated |
| MIN-09 | Protection Map / protection-state model distinguishing verified, parent-confirmed, action-needed, not-covered, uncertain/error and removed states as applicable | O + M | Truth-state distinction is a frozen trust/safety boundary | Real-parent comprehension remains unknown |
| MIN-10 | Coverage-limit explanations integrated into the journey | M + P | Complete-safety claims are prohibited; material limitations must be exposed | Wording effectiveness/comprehension remains unvalidated |
| MIN-11 | Removal, recovery, reinstall/reconfigure and normal-DNS restoration guidance for supported paths | M | Reversibility/recovery are safety and operability requirements; technical removal/recovery is already proven | Parent self-service success remains unvalidated |
| MIN-12 | False-positive, compatibility and unsupported/conflict help path using privacy-minimal diagnostics | M + P | Filtering can create compatibility issues; support must preserve privacy/truth and reversibility | Real issue rate/support burden remains unknown |
| MIN-13 | Self-service help embedded around expected failure points, with exceptional escalation only where necessary | O + M | DEC-0048 freezes self-service; privacy/safety require bounded escalation routes | Actual ordinary-help demand remains unvalidated |
| MIN-14 | Responsive, accessible public/setup surfaces with explicit loading/error/uncertain/recovery states | M | Accessibility and correct failure-state behavior are product quality requirements independent of behavioral validation | Later usability/accessibility testing still required where its own AC requires it |
| MIN-15 | Shared coherent brand/design/terminology system across public and setup surfaces | O | DEC-0044 makes brand/UX first-class work | Brand preference/trust impact is not yet user-validated |
| MIN-16 | Externalized/localizable product/content structure supporting English, Turkish and Arabic plus RTL readiness | O | DEC-0045 requires first-release multilingual capability while separating technical language capability from market activation | Does not activate official non-UK market/support/legal commitments |
| MIN-17 | Current-source/version ownership for device/service instructions and protection claims | M | Platform instructions and safety claims can become stale; source/version governance is required for correctness | No claim that content format is behaviorally optimal |
| MIN-18 | Privacy-minimal operational/product state sufficient to complete and verify the immediate setup journey without a persistent identity profile | O + M | Accountless-first and minimisation rules require value without mandatory persistent identity | Exact ephemeral/session design remains later architecture work |

## 5. Explicit first-product non-goals / exclusions

The following are **not** part of the active minimum product unless their separate trigger and owner authority are satisfied:

| Exclusion | Current disposition | Why excluded |
| --- | --- | --- |
| Mandatory UseSafeWeb account, Google sign-in or other customer authentication | DEFERRED — EXC-0001 | Accountless-first is frozen; no validated persistence/identity need exists |
| Persistent parent dashboard / persistent device list | DEFERRED — EXC-0001 | Adds identity/data/state complexity without current validated need |
| Customer-facing AdGuard administrative/control plane | DEFERRED / not in active baseline | Parent should not manage raw DNS administration; unnecessary complexity and risk |
| Browsing history, DNS query history, top-domain/activity reporting | PROHIBITED/EXCLUDED | Violates privacy-minimal/non-surveillance trust boundary |
| Covert monitoring, message reading, contact/photo/location/social-content surveillance | PROHIBITED/EXCLUDED | Explicit non-surveillance boundary |
| Child account, child app/profile or behavioral profile | DEFERRED/EXCLUDED — EXC-0005 | No current minimum need; materially expands safety/privacy/identity scope |
| Broad service catalogue / arbitrary app-control platform | DEFERRED | Current shape is one genuinely relevant service only |
| GROW lifecycle automation / AI parenting automation | DEFERRED — EXC-0005 | SET UP + minimum PROTECT is the active scope; demand/persistence not proven |
| Community/UGC, school portal or institutional administration | DEFERRED/EXCLUDED | Outside current consumer first-phone minimum and may change legal/safety scope |
| Native mobile app | DEFERRED — EXC-0005 | No current need that justifies another application/platform surface |
| Full parental-control suite | EXCLUDED | Product is orchestration + baseline protection, not a replacement surveillance/control suite |
| Complex paywall, premium safety tiers or safety-feature gating | EXCLUDED | Core product stays free; safety is not paywalled |
| Supporter payment checkout in the current L4 minimum | CONDITIONAL / NOT CURRENTLY AUTHORIZED | DEC-0011 defines a future optional post-value model, but payment activation requires later value/legal/tax/privacy/security/provider gates |
| Paid acquisition machinery | DEFERRED — EXC-0002 | Product must not depend on paid acquisition; earned distribution remains baseline |
| High-availability/multi-node infrastructure as a product requirement | DEFERRED — EXC-0004 | Lean recoverable topology is current baseline; no measured need for HA complexity |
| Official non-UK market activation merely because Turkish/Arabic UI exists | DEFERRED — EXC-0003/0007 | Language capability is not market/legal/support authorization |
| Broad/raw DNS configuration features or alternative filtering backend | EXCLUDED/DEFERRED | AdGuard is frozen and raw administration is not a customer job in the current product |
| Persistent identifiable child/family analytics or behavioral monetization | PROHIBITED | Conflicts with DEC-0012 and trust/privacy boundaries |

## 6. Minimum journey boundary

The provisional minimum journey is deliberately narrow:

1. **Discover / understand / trust / start** on the public surface.
2. **Route** to the supported accountless setup path with minimum inputs.
3. **Phone** — present relevant native safeguards first; recognise already-configured/not-applicable paths.
4. **Internet** — configure and verify the approved encrypted UseSafeWeb/AdGuard baseline path.
5. **Service** — guide one genuinely relevant service safeguard where applicable.
6. **Understand** — show truthful Protection Map plus material limitations.
7. **Recover** — provide clear false-positive, conflict, removal/reinstall and unsupported-state help.
8. **Complete quietly** — no mandatory account creation, payment ask, engagement loop or surveillance dashboard.

This sequence is a **provisional product hypothesis**. It is not represented as a real-user-validated journey.

## 7. Data and state boundary

The L4 product definition must assume the minimum data/state necessary for the immediate setup/verification journey and defer persistent identity until EXC-0001 is legitimately activated.

Active product design therefore must:

- avoid requiring parent/child names, exact child DOB, routine location, messages, contacts, photos, social content or browsing/query history;
- avoid persistent identity solely to make the product architecture convenient;
- keep technical verification separate from parent confirmation;
- surface stale/unknown/unsupported states rather than manufacture certainty;
- design removal/recovery without requiring account access;
- leave exact implementation/session-storage architecture to later authorized architecture work rather than inventing it in L4.

## 8. Scope-control rules

During provisional L4:

1. new scope is rejected by default unless it passes the O/M/P inclusion test and current authority;
2. **P** items remain clearly provisional and must identify the later evidence that could invalidate them;
3. a synthetic flow may verify internal completeness/logic but cannot upgrade a P item to validated need;
4. mandatory technical/safety/privacy capability is not removed merely because behavioral evidence is deferred;
5. deferred exceptions remain out of scope until their exact trigger and approval are proven;
6. if a downstream task requires real-participant frequency, preference, comprehension, persistence or assistance evidence, that task remains deferred rather than changing this scope to fake its input;
7. this scope does not authorize L5/L6 or implementation work.

## 9. Revalidation triggers

Re-evaluate this scope when any of the following occurs:

- L3 real-participant validation is reactivated or CR-0003 expires on 2027-08-27;
- real-user evidence contradicts a P-class assumption;
- a verified security/privacy/legal/technical blocker invalidates an included path;
- an EXC-0001/0003/0004/0005 trigger is genuinely satisfied and the Project Owner authorizes expansion;
- supported platform/service capabilities materially change;
- a later gate identifies scope that cannot meet accessibility, reliability, recovery, privacy, security or self-service acceptance.

Any affected downstream PASS must be reopened when its evidence no longer supports the revalidated scope.

## 10. ACC-0141 traceability

ACC-0141 requires every included capability to map to an explicitly unvalidated current-need assumption, mandatory operation/safety requirement, or explicit owner-approved architectural decision; preserve an accountless-first minimum; keep authentication/dashboard/AdGuard control plane deferred; exclude surveillance/activity history/child accounts/advanced scope; and avoid describing capabilities as behaviorally validated.

- Sections 2 and 4 give every included capability an **O/M/P** basis.
- P means **provisional/unvalidated**, never behaviorally validated.
- Sections 5 and 7 preserve DEC-0042 / EXC-0001 and privacy/non-surveillance exclusions.
- Sections 6 and 8 keep the first product minimum and prevent synthetic evidence from becoming user evidence.
- Section 9 binds later real evidence to re-evaluation rather than protecting the provisional freeze.

**TSK-0141 result: PASS candidate subject to independent verification and runtime read-back.**
