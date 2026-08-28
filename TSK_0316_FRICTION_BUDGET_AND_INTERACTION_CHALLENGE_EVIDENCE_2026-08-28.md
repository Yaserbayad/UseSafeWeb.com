# TSK-0316 — Friction budget verification evidence

**Task:** TSK-0316 — Define a friction budget and challenge every click, field, choice, confirmation, account, and manual step  
**Acceptance:** ACC-0316  
**Verification:** VER-0316 independent guarded interaction/authority audit  
**Date:** 2026-08-28  
**Result:** PASS candidate pending authoritative runtime reconciliation/read-back

## Exact evidence index

- Friction contract: `TSK_0316_FRICTION_BUDGET_AND_INTERACTION_CHALLENGE_2026-08-28.md`
- Contract blob: `07df8b1909809a069e3ddba1ff10b688d2f5a5e0`
- Contract commit: `5486ea1cebe8f533171edae128f47d22ad83d6fb`
- TSK-0315 service blueprint blob: `f428f346d6e994d093b651d7b934e8610498c350`
- TSK-0320 protection-state contract blob: `1146f7622f434590dde1253d11f14fb6a87e19de`
- TSK-0229 accountless data contract blob: `3fa48b11b6c7704ecc3748bcd865f77aa54f5605`
- TSK-0408 DNS platform contract blob: `52860ce167fc8a31962cd412772e428d280c8184`
- WBS blob: `dce5b829c4d447eac180ae1e896e0019292cf971`
- Current hard dependency: `TSK-0315 = PASS`.

## Authority/precondition audit

- TSK-0316 is L4 / A3 / AUTO_ALLOWED / HIGH with sole hard dependency TSK-0315, now runtime PASS.
- ACC-0316 is a design-minimisation acceptance and can be satisfied without representative-parent evidence under DEC-0050/CR-0003.
- The artifact explicitly refuses fabricated click counts, completion-time targets, abandonment/conversion claims, or assertions that the journey is behaviorally optimal.
- `RSK-0002` remains OPEN and the contract is explicitly provisional internal L4 design only.
- The artifact does not bypass OS authorization, truthful protection-limit disclosure, legal/safeguarding controls, privacy deletion/retention, owner gates, future real-participant validation, release or launch authority.

## ACC-0316 clause audit

ACC-0316 requires: `Each retained interaction has a decision/technical/safety reason; removable steps are removed; platform constraints are explicit; unsupported one-click claims are absent.`

### Each retained interaction has a reason — PASS

The contract defines five allowable friction classes: irreducible decision, irreducible platform action, truth/evidence confirmation, conditional compatibility detail, and recovery/help. It then audits every TSK-0315 interaction and maps retained/conditional interactions to a concrete reason. Start separates public information from setup; native/DNS/service actions change actual protection state; confirmations exist only when system verification is unavailable; verification protects truth; Protection Map exposes evidence/limits; help/reset/remove are recovery functions.

The model is purpose-based rather than count-based, which is correct under current evidence because Android/iPhone OS flows differ and no representative-parent evidence supports a universal numerical budget.

### Removable steps are removed/conditionalized — PASS

The default path removes or conditionalizes friction that currently has no independent necessity:

- no mandatory account/login/contact/payment;
- no forced onboarding carousel or dedicated mandatory How-it-works/trust progression screen;
- no forced locale question where a safe default is available;
- no universal OS/version question;
- no default new/already-used phone question until TSK-0143 proves a routing branch;
- no generic DoH-versus-DoT chooser when platform routing determines the mechanism;
- no mandatory external-service step when none applies;
- no Protection Map acknowledgement checkbox;
- no mandatory extra Finish/Exit click when completion/deletion can safely occur from the final map;
- no duplicate confirmations, surveys, marketing prompts, browsing-history diagnostics or unrestricted support notes.

The removal of a separate mandatory trust screen does **not** remove trust/protection-limit content: the contract explicitly requires concise essential limits/privacy beside or before Start and at the point of impact. The conditional removal of an explicit Finish control also does not waive deletion or legal obligations: it applies only if final-map rendering can safely execute completion/J1 deletion; a later owning technical/legal requirement can reinstate an explicit action.

### Platform constraints are explicit — PASS

Android is correctly treated as a platform-required Private DNS action using the accepted provider hostname; the contract does not assume a web page can silently change Android system DNS. Apple is correctly treated as a profile/OS authorization action; the contract does not assume silent profile installation or treat profile presence as system verification. VPN/browser/app/network conflicts are kept visible as potentially uncertain and remain owned by TSK-0409 rather than being optimized away.

### Unsupported one-click claims are absent — PASS

The contract distinguishes a one-click CTA from a one-click underlying platform operation. It explicitly prohibits `Protect this phone in one click`, automatic activation claims where OS action is still required, universal Android/iPhone claims, all-app/network claims, `Install and forget`, and `Fully protected`.

### Truth/evidence boundary — PASS

Parent confirmation is retained only when it changes state and system verification is unavailable; it yields TSK-0320 S2 and never S1. DNS verification remains mandatory as a system/evidence function, with automatic execution preferred where technically feasible and a deliberate Check/Recheck only where needed.

### Accountless/privacy boundary — PASS

The TSK-0229 schema is explicitly treated as an upper bound rather than a form specification. Fields are displayed only when needed for current routing. Identity, exact child DOB/age, location/school, service usernames, stable device fingerprint, browsing history, raw diagnostics and hypothetical-future analytics fields remain excluded. Safe transient derivation is allowed only without persistent profiling.

## Adversarial findings and unresolved uncertainty

1. **The minimized journey is not proven usable.** Removing forced screens/confirmations is a design simplification, not evidence that parents will comprehend the resulting experience. `RSK-0002` remains the controlling uncertainty.
2. **The exact need for device/version/phone-state fields is unresolved.** The contract correctly makes them conditional on TSK-0143/TSK-0409 rather than prematurely removing or mandating them.
3. **The mandatory Finish control is not categorically prohibited.** It is removed only from the default budget if completion/deletion can occur safely without it. A later legal/technical requirement can make it necessary; the current artifact does not override such a requirement.
4. **Trust/limit disclosure cannot be optimized away.** The separate forced screen is removed, not the content. Any later design that hides material limits behind a link or after activation would contradict this contract and the TSK-0320 truth model.
5. **OS security friction is not product waste.** Android settings and Apple profile authorization remain irreducible until current technical evidence proves a safe supported automation mechanism.
6. **No universal interaction count is defensible today.** No current evidence supports a fixed click/screen/time target, so the purpose-based budget is the strongest truthful design constraint available.

No current authoritative requirement was found that mandates a persistent account, forced marketing/education progression, protocol chooser, Protection Map acknowledgement checkbox, or explicit Finish click independently of a later technical/legal need.

## Stable verification decision

The durable contract directly satisfies every ACC-0316 clause while preserving TSK-0315/0320 truth requirements, TSK-0229 privacy/accountless controls, TSK-0408 platform reality, and DEC-0050/CR-0003 evidence limits.

**Stable outcome: TSK-0316 = PASS candidate pending authoritative runtime reconciliation and post-write read-back.**

## Recompute requirement

After runtime reconciliation, recompute the current L4 queue. TSK-0317 is expected to become dependency-ready but remains HUMAN_ONLY under Layer 5. TSK-0409 remains HIGH/A3/AUTO_ALLOWED and should be evaluated as the likely next executable task only after fresh runtime read-back.
