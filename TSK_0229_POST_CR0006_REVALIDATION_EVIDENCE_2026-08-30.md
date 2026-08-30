# TSK-0229 — Post-CR-0006 Revalidation Evidence

**Date:** 2026-08-30  
**Task:** TSK-0229 — Define and approve the accountless journey data model, expiry, deletion, and no-linkage rules  
**Acceptance:** ACC-0229  
**Verification:** VER-0229  
**Evidence:** EVD-0229  
**Lifecycle:** L4  
**Action authority:** A3 / AUTO_ALLOWED  
**Disposition:** PASS evidence for TSK-0229, subject to canonical runtime reconciliation/read-back

## 1. Decision

The existing `accountless-journey-data-v1` contract remains the substantive accountless data model. DEC-0053 / CR-0006 does not require it to be redesigned, but it **does** trigger the base contract's material-change rule because Version 1 now includes an optional persistent parent account/dashboard.

The post-CR-0006 amendment `TSK_0229_POST_CR0006_ACCOUNTLESS_NO_LINKAGE_AMENDMENT_2026-08-30.md` resolves that change by preserving J0/J1 unchanged and making the optional account a separate persistent data domain. No persistent-account schema is approved by TSK-0229.

## 2. Artifacts and exact Git objects

- Base contract: `TSK_0229_ACCOUNTLESS_JOURNEY_DATA_MODEL_EXPIRY_DELETION_NO_LINKAGE_2026-08-28.md`
  - version: `accountless-journey-data-v1`
  - blob: `3fa48b11b6c7704ecc3748bcd865f77aa54f5605`
- Post-CR-0006 amendment: `TSK_0229_POST_CR0006_ACCOUNTLESS_NO_LINKAGE_AMENDMENT_2026-08-30.md`
  - version: `1.0.0`
  - publication commit: `a75d88622a818a64761d4292110dcc229cd5d4af`
  - blob: `2955c2762e726f95ec67c33b9abbc5e4b25cb84a`
  - exact-path read-back: PASS
- Current product baseline used by the amendment: `TSK_0146_VERSION_1_OPTIONAL_ACCOUNT_PRODUCT_BASELINE_2026-08-30.md`
  - blob: `9d3870d90add696fc352829fb4763c834b8d09af`

Historical `TSK_0229_CURRENT_REVALIDATION_EVIDENCE_2026-08-29.md`, blob `7c6bd3b888196f2a487c7b7fe14d11e72bec424b`, remains valid evidence for the pre-CR-0006 accountless model and DEC-0052 sequencing, but it cannot by itself resolve the later optional-account activation.

## 3. Canonical source bindings

The deterministic verification was pinned to:

- runtime prestate `CURRENT_STATE.md`: `515638ae5efaa8dfec4e9a8362f28f7efb45cd6e`
- WBS: `3bb1598a6233a2bbefa52c746a7621867c6c6e89`
- requirements: `a2212059f69c4602eb0c05961d5d1639e3543f83`
- constraints: `9464720bff94fd569e3b939568996a26eed83ca1`
- interfaces: `b01b47e48fcd1bd5b9697e0ab35b496059e7eb6c`
- risks: `0ebb7ab97ec4d418e61eaae0fce6a35e3a9e36ec`
- decisions: `9cb2908f4c6f19cb38fce4a8aff71abca3b7b095`

The WBS contract verified TSK-0229 as L4, PLANNED/WAITING before current runtime override, HIGH priority, dependency `TSK-0146`, A3 / AUTO_ALLOWED, and `ACC-0229 / VER-0229 / EVD-0229`. Current runtime independently proves post-CR-0006 TSK-0146 PASS.

## 4. Current authoritative privacy-source review

Official-source review on 2026-08-30 found no contradiction to the minimisation/separation direction:

- GDPR Article 5(1)(c) data minimisation and Article 5(1)(e) storage limitation: `https://eur-lex.europa.eu/eli/reg/2016/679/2016-05-04`.
- GDPR Article 25 data protection by design/default and default processing limited to what is necessary for each purpose: same official EUR-Lex text.
- EDPB Guidelines 4/2019 on Article 25 are still published as the final version: `https://www.edpb.europa.eu/documents/guideline/guidelines-42019-on-article-25-data-protection-by-design-and-by-default_en`.
- EDPB February-2026 DPbDD summary continues to describe privacy-by-design/default as a continuous duty and explicitly prompts designers to consider whether less data can be used: `https://www.edpb.europa.eu/system/files/2026-02/edpb-summary-gdpr-data-protection-design-default_en.pdf`.

This review supports the conservative minimisation/purpose-separation design. It does **not** declare the internal 24-hour J1 TTL or 15-minute cleanup bound legally required, and it is not a final legal-compliance opinion.

## 5. Independent deterministic verification

Workflow: `Verify TSK-0229 post-CR-0006`  
Runner: self-hosted `adguardvm`

### Initial run — diagnostic failure, not accepted

- run: `33307832517`
- job: `99247423588`
- conclusion: FAILURE
- all exact hash/prestate guards passed;
- failure was localized to a verifier assertion that expected the TSK-0146 phrase `Anonymous journey state...` while the actual accepted baseline says `Accountless journey state...`;
- the intended invariant was unchanged; no product/data artifact or canonical runtime state was changed;
- this run supplies diagnostic evidence only and is **not** used as PASS evidence.

### Corrected run — accepted verification

- corrected workflow commit: `c9b28cd392ccfcc9a32fce186c80930445ded067`
- run: `33307917535`
- job: `99247643413`
- conclusion: SUCCESS

Observed outputs:

- `TSK0229_WBS_ELIGIBILITY=PASS`
- `TSK0229_BASE_CONTRACT_PRESERVED=PASS`
- `TSK0229_CR0006_SEPARATION=PASS`
- `TSK0229_ACC0229=PASS`
- `TSK0229_PRIVACY_BOUNDARIES=PASS`
- `TSK0229_DOWNSTREAM_SCOPE_FENCE=PASS`
- `TSK0229_VERIFICATION=PASS`

The corrected test additionally makes explicit that any `LG-06 PASS` text in the amendment is only part of the non-authority disclaimer.

## 6. ACC-0229 review

| ACC-0229 element | Current evidence | Result |
| --- | --- | --- |
| Only active-journey fields necessary | Base J0/J1 contract preserves browser/session-first state and the explicit J1 allowlist. | PASS |
| No browsing history | Browsing/URL/DNS-query/visited-domain/activity history remain prohibited in J1 and may not be transferred to an account/dashboard. | PASS |
| No persistent child profile | Child identity/profile and persistent family/behavioral profile remain excluded. | PASS |
| Expiry testable | J1 retains fixed non-sliding maximum 24-hour hard expiry; account sign-in/activity cannot extend it. | PASS |
| Deletion testable | Existing early-delete/read-back rules remain; anonymous deletion is explicitly independent from account/device deletion and DNS removal. | PASS |
| Diagnostic boundary testable | Raw/request diagnostics remain outside J1 and separately governed/time-boxed/deleted. | PASS |
| No-linkage under new optional account | J0/J1 cannot be automatically converted/joined/promoted to account state; no account identifier is stored in J1; any future explicit transfer requires a separately approved downstream data-flow contract. | PASS |
| Core remains accountless | Authentication/provider/account-store failure cannot make the core journey login-dependent or extend anonymous state. | PASS |

**ACC-0229 result: PASS.**

## 7. Contrary evidence and residuals

The material contrary change was DEC-0053 / CR-0006 itself: the prior contract said activation of account/dashboard persistence required a new data-contract decision. That contradiction has been resolved by the bounded amendment rather than by pretending the old PASS remained sufficient.

Residuals deliberately remain outside TSK-0229:

- the persistent optional-account schema, exact fields, provider identifiers, device-ownership identifiers, storage, retention, backup, deletion and access model remain downstream authoritative work;
- lawful-basis/recipient/rights mapping must match actual implemented reality under REQ-0019 and later privacy/legal tasks;
- `RSK-0001` remains OPEN for later England participant legal/data readiness;
- `RSK-0002` remains OPEN/non-blocking before L8 under DEC-0052 / CR-0005; no human/user validation is inferred;
- persistent identifiable DNS/query logging and top-domain/client history remain prohibited by CON-0007/CON-0008 and the wider product baseline;
- no L5 architecture, implementation, LG-06, participant, release or launch PASS is inferred.

## 8. Work unlocked

A current TSK-0229 PASS satisfies this dependency where referenced, including the TSK-0229 predecessor of the revised dual-mode L4 service blueprint TSK-0315. Eligibility for any successor must still be recomputed against all of its other WBS hard dependencies, lifecycle/gates, runtime evidence and Action Authority.

## 9. Final evidence disposition

The base data model plus the post-CR-0006 separation amendment satisfy all current ACC-0229 requirements with exact-path read-back, current authority review, current official privacy-source review, contrary-evidence disposition and a successful source-hash-bound verifier run.

**TSK-0229 is evidence-ready for runtime state `PASS`.** PASS becomes canonical only after `CURRENT_STATE.md` is updated, committed, reread and verified against this evidence.
