# TSK-0144 — One relevant external-service safeguard verification evidence

**Task:** TSK-0144 — Specify the one relevant external-service safeguard step  
**Acceptance:** ACC-0144  
**Verification:** VER-0144 independent guarded product/policy audit  
**Date:** 2026-08-28  
**Result:** PASS candidate pending authoritative runtime reconciliation/read-back

## Exact evidence index

- Service contract: `TSK_0144_ONE_RELEVANT_EXTERNAL_SERVICE_SAFEGUARD_REQUIREMENTS_2026-08-28.md`
- Contract blob: `f7821c8ef50aa517753c31477b383d660de11f40`
- Contract commit: `54d01d29a0cebcc9b64b19fdd9807ab96edba4b8`
- BUSINESS_EVALUATION blob: `95255c3ce8cc60daf0b9936c925b6bc691744116`
- TSK-0141 minimum scope blob: `c72bfd906fdca4a106dcd7d4ff458a2577e32c90`
- TSK-0138 assumptions/decisions blob: `d782f26d5d48b0902b044d8bbab48569bdee0ea2`
- TSK-0315 service blueprint blob: `f428f346d6e994d093b651d7b934e8610498c350`
- TSK-0316 friction contract blob: `07df8b1909809a069e3ddba1ff10b688d2f5a5e0`
- TSK-0320 protection-state contract blob: `1146f7622f434590dde1253d11f14fb6a87e19de`
- WBS blob: `dce5b829c4d447eac180ae1e896e0019292cf971`
- Current hard dependency: `TSK-0143 = PASS`.

## Authority audit

Canonical product authority requires one genuinely relevant external-service safeguard and explicitly keeps the step service-agnostic. BUSINESS_EVALUATION states this is because the UK platform context is changing; TSK-0141 MIN-08 keeps exactly one relevant service while saying its incremental value remains unvalidated; TSK-0138 UPA-004 keeps that value assumption UNKNOWN and prohibits broadening the service catalogue without evidence.

Therefore TSK-0144 may define the eligibility/selection/truth/update contract but must not select one universal named service or infer service use from behavior/history/popularity.

## Current UK policy check — 2026-08-28

The UK government's July 2026 `Growing up in the online world` response, updated 19 August 2026, states that social media companies will no longer be able to offer services to under-16s, that the first regulations are intended before Parliament by the end of 2026, and that the first social-media restrictions are expected to enter into force in spring 2027. Exact covered-service detail remains part of the implementation/regulatory process.

Primary source:
- https://www.gov.uk/government/consultations/growing-up-in-the-online-world-a-national-consultation/outcome/growing-up-in-the-online-world-government-response-july-2026

**Disposition:** this is current external evidence capable of invalidating a hard-coded 2026 social-media-service choice. The service-agnostic, current-policy-recheck design is therefore the conservative correct rule.

## ACC-0144 clause audit

ACC-0144 requires: `Requirements define eligibility, supported/unsupported state, one-service limit, parent confirmation, content update ownership, and fallback to Not covered.`

### Eligibility — PASS

The contract requires actual parent-declared relevance, current age/legal availability, a current approved safeguard, current official source, legitimate parent access, no material contradiction and no duplicate setup. It explicitly prohibits inferred service use from age, popularity, advertising data, app inventory, browsing history or DNS history.

### Supported / unsupported state — PASS

A service is supported only if the instruction catalogue has an exact provider/safeguard/applicability/source/version/expected-result/limitation/confirmation/fallback/owner/review record. Missing or stale required elements result in unsupported/uncertain state rather than guessed guidance.

### One-service limit — PASS

The contract freezes zero-or-one service branch as valid and one as the hard maximum. If several supported services are genuinely relevant, the product still runs one branch; it cannot silently grow into a service catalogue.

### Parent confirmation — PASS

Current third-party service-account settings have no approved UseSafeWeb verifier. Completion therefore yields TSK-0320 S2 parent-confirmed only. Credentials/tokens/screenshots cannot be collected merely to manufacture verification.

### Content update ownership — PASS

Every instruction must have a named UseSafeWeb content owner, official provider source, last-verified date and deterministic review trigger. Provider menu/age/account changes, UK rule changes, source contradiction/removal, target evidence, or security/privacy/safeguarding changes force re-review. Stale items are removed from the supported selector until reverified.

### Fallback to Not covered — PASS

No relevant supported service, no current approved safeguard, age/policy inapplicability, unsupported account/region/device state, stale instruction, or lack of legitimate parent authority all produce a valid S4 `Not covered`/not-applicable outcome. No filler service is inserted.

## Cross-contract consistency audit

- **Business/product baseline:** PASS. One service remains a bounded layer, not a broad app-control product.
- **TSK-0316:** PASS. Service questions are shown only when they change routing; no app inventory/free-text catalogue is introduced.
- **TSK-0320:** PASS. S2/S3/S4/S5/S6 truth states are preserved and no service state is falsely system-verified.
- **Accountless/privacy:** PASS. No provider credential, token, child messages/activity/history or persistent interest profile is introduced.
- **Current policy:** PASS. Service eligibility is reviewable and can legitimately reduce to zero as UK rules change.

## Adversarial findings and unresolved uncertainty

1. **No named service is currently justified as a universal default.** The project has no real-parent relevance distribution, and current UK rules are changing materially.
2. **A popular service is not automatically eligible.** Provider age rules, UK law, exact safeguard availability and parent authority must all pass current review.
3. **Zero-service journeys are required.** Forcing a service branch would violate relevance, friction and truth requirements.
4. **No system verification exists for third-party account settings.** Parent confirmation remains the strongest current positive evidence.
5. **2027 can invalidate 2026 instructions.** Current government plans make source/policy review a substantive product requirement rather than ordinary editorial maintenance.
6. **Incremental value remains unknown.** `UPA-004`/`RSK-0002` remain OPEN; this contract cannot claim the service layer improves outcomes.

## Stable verification decision

The durable service contract directly satisfies every ACC-0144 clause, is narrower than the maximum product scope, incorporates current authoritative UK policy as a review trigger, and preserves the missing behavioral evidence instead of selecting a plausible service by assumption.

**Stable outcome: TSK-0144 = PASS candidate pending authoritative runtime reconciliation and post-write read-back.**

## Recompute requirement

After runtime reconciliation, recompute the provisional-L4 queue from current WBS/runtime authority. Do not assume downstream Protection Map or product-brief work is eligible unless every hard predecessor and any human-review acceptance condition is actually satisfied.
