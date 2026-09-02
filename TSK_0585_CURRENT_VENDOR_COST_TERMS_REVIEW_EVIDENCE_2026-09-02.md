# TSK-0585 — Current Authentication / AdGuard Vendor Cost, Licence, Terms and Exit Review Evidence

**Task:** TSK-0585 — Verify authentication free tier, AdGuard licence/API cost, vendor terms and exit triggers  
**Acceptance / Verification / Evidence:** ACC-0585 / VER-0585 / EVD-0585  
**Lifecycle / Priority / Capability / Authority:** L4 / MEDIUM / A3 / AUTO_ALLOWED  
**Evidence date:** 2026-09-02 UTC  
**Disposition:** CURRENT PASS — subject only to guarded runtime reconciliation and exact GitHub read-back.

## 1. Accepted artifact

- `TSK_0585_CURRENT_AUTH_VENDOR_COST_TERMS_EXIT_REVIEW_2026-09-02.md`
- version `1.0.0`
- blob `101fb63ed4367b514a36f5a07ee271be7cd7a5c3`
- publication commit `fd8b89ef42509a092c17a0e140cc8236472cda1c`

## 2. Canonical contract / predecessor proof

Independent VER-0585 hash-locked:

- WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`;
- graph `c108d2c162bcea2ee4cc01def46d0487a9501032`;
- pre-reconciliation runtime `2af7f02479cee28b43c1cffe5478d518b866eea8`;
- TSK-0045 current artifact `0df1b4747afea4521e4e98b0728c83750ed2b547`;
- TSK-0353 current artifact `3cb7c248b6d121e1c8d9db47accdf639998edc93`;
- TSK-0044 current artifact `9e2df58093c592621eb1531dc1c34393a247dd80`.

It proved the exact current task row: L4 / MEDIUM / A3 / `AUTO_ALLOWED`, dependencies exactly `TSK-0045; TSK-0353; TSK-0044`, and `ACC-0585 / VER-0585 / EVD-0585`.

WBS verification method: `Use the approved checklist/test procedure against the exact artifact/environment; retain reproducible outputs and reviewer result.`

WBS evidence requirement: `Artifact/version; exact environment or source; test/review output; date; responsible verifier; deviations and disposition.`

Markers: `TSK0585_INPUT_HASHES=PASS`, `TSK0585_CURRENT_WBS=PASS`, `TSK0585_CURRENT_PREDECESSORS=PASS`.

## 3. Dated official-source result

Final independent run re-fetched the official sources live and proved the current factual record. Official URLs:

- `https://firebase.google.com/pricing`
- `https://firebase.google.com/docs/auth`
- `https://cloud.google.com/identity-platform/pricing`
- `https://firebase.google.com/support/privacy`
- `https://firebase.google.com/terms/`
- `https://firebase.google.com/terms/data-processing-terms`
- `https://github.com/AdguardTeam/AdGuardHome`
- `https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/master/LICENSE.txt`
- `https://github.com/AdguardTeam/AdGuardHome/tree/master/openapi`
- `https://github.com/AdguardTeam/AdGuardHome/blob/master/openapi/README.md`

Final source markers:

- `TSK0585_OFFICIAL_SOURCE_REGISTER=PASS`;
- `TSK0585_LIVE_SOURCE_FETCH=PASS`;
- `TSK0585_LIVE_FIREBASE_BASE_PRICING=PASS`;
- `TSK0585_LIVE_IDENTITY_PLATFORM_LIMITS=PASS`;
- `TSK0585_LIVE_IDENTITY_PLATFORM_PRICING=PASS`;
- `TSK0585_LIVE_AUTH_PROCESSING_LOCATION=PASS`;
- `TSK0585_LIVE_FIREBASE_TERMS=PASS`;
- `TSK0585_LIVE_ADGUARD_LICENSE_API=PASS`.

## 4. Current Firebase/auth cost disposition

The current evidence proves:

- Spark is a no-cost Firebase plan with no payment method required;
- the current planned Google/social Firebase Authentication route can use the no-cost Spark path, subject to current quotas/terms;
- Identity Platform remains optional;
- upgraded Spark Tier-1 providers are currently bounded at 3,000 DAU and SAML/OIDC at 2 DAU;
- upgraded Blaze Tier-1 has a 50,000 MAU no-cost boundary, followed by the current `$0.0055 / $0.0046 / $0.0032 / $0.0025` MAU tiers;
- SAML/OIDC Blaze is 50 MAU no-cost then `$0.015/MAU`;
- phone/SMS/MFA messages are separately billed;
- current Version 1 has no SMS path, so the initial auth estimate includes zero SMS/phone messages.

Marker: `TSK0585_AUTH_COST_THRESHOLDS=PASS`.

The resulting planning assumption is an **initial authentication-service fee of $0 for the current small-scale Google/social path**, not a $0 end-to-end service-cost claim.

## 5. Processing-location correction / legal boundary

Current Firebase official privacy evidence states Firebase Authentication is run only from US data centers and processes data exclusively in the United States.

Therefore the previously open location question is resolved factually as **US-only**. The review does not infer that US-only processing is legally acceptable for every target jurisdiction and does not invent a lawful basis, transfer mechanism, subprocessor conclusion or final privacy/legal approval.

Markers:

- `TSK0585_PROCESSING_LOCATION_NO_GUESS=PASS`;
- `TSK0585_LEGAL_UNRESOLVED_NO_GUESS=PASS`.

## 6. Firebase terms / exit triggers

Current Firebase Terms page was independently verified as carrying the **May 1, 2026** modification date and Firebase Authentication / Google Cloud terms relationship. Data-processing/security terms remain separately relevant.

The accepted artifact records explicit re-review/migration triggers for pricing/threshold changes, Identity Platform upgrade, SMS/MFA/SAML/OIDC addition, processing-location change, material terms/DPA change, legal/privacy rejection, provider API/deprecation/export/delete constraints, reliability/accountless-fallback failure, and new contract/material spend requirements.

Marker: `TSK0585_EXIT_TRIGGERS=PASS`.

## 7. AdGuard Home licence/API/cost disposition

Current official AdGuard Home sources prove:

- official repository describes AdGuard Home as free and open source;
- repository licence is GPL-3.0 / GNU GPL Version 3;
- official project documents its REST API;
- official repository contains OpenAPI materials and API authentication documentation.

The reviewed official self-hosted project materials **do not evidence a separate AdGuard Home API subscription/per-call fee**. This is recorded as an evidence-limited finding, not a perpetual guarantee. GPL obligations remain real and depend on the exact legal/distribution model; no legal interpretation is inferred.

Marker: `TSK0585_ADGUARD_COST_LICENSE_BOUNDARY=PASS`.

## 8. Infrastructure separation

The accepted artifact separately identifies VM/compute, storage/backups, networking, web/account hosting, database, secret/logging/monitoring and CI/runtime infrastructure costs. No auth-service or AdGuard software/API no-cost finding is allowed to become a zero-total-service-cost claim.

Marker: `TSK0585_INFRASTRUCTURE_COST_SEPARATION=PASS`.

## 9. Independent VER-0585

Final independent read-only verifier:

- base verifier `.github/scripts/verify_tsk0585_current_vendor_review.py` — blob `af8b087caec65ca488dba24f23859561c5234bc4`;
- final transport/markdown-robust wrapper `.github/scripts/verify_tsk0585_current_vendor_review_v3.py` — blob `49251cf0cec47c59ff51e7c99210c684c1d92de1`;
- workflow `.github/workflows/verify-tsk0585-current-review.yml` — blob `23d5e7033bf63c24c3c85a0cfc4a18cd65a2ca58`;
- permissions: `contents: read` only;
- environment: GitHub-hosted Ubuntu 24.04 LTS;
- run/job `33590152982 / 100122320757`;
- conclusion **SUCCESS**;
- responsible verifier: isolated GitHub Actions job executing hash-locked project checks plus bounded live official-source retrieval.

Final markers also include:

- `TSK0585_STRUCTURE=PASS`;
- `TSK0585_FACT_MATRIX=PASS`;
- `TSK0585_NON_INFERENCE=PASS`;
- `TSK0585_CURRENT_ACC=PASS`;
- `TSK0585_CURRENT_VER=PASS`;
- `TSK0585_CURRENT_EVD_READY=PASS`;
- `TSK0585_CURRENT_REVIEW=PASS`.

### Diagnostic-only failures retained

Run 1 failed before live-source acceptance because the verifier required the raw GitHub README URL to be written in the human artifact, while the artifact correctly cited the official repository page. No project fact failed.

Run 2 passed all substantive live-source/vendor/cost/licence/legal-boundary checks and failed only because markdown `does **not** activate` did not match a plain-text `does not activate` predicate. No project fact failed.

The final v3 wrapper changes only those transport/markdown-shape predicates; it does not weaken any factual acceptance requirement.

## 10. Acceptance disposition

**ACC-0585 = PASS. VER-0585 = PASS. EVD-0585 = SATISFIED.**

**TSK-0585 current vendor/cost/licence/terms review: PASS, pending only guarded runtime reconciliation and exact GitHub read-back.**

## 11. Non-inference

This evidence does not activate or purchase Firebase/Identity Platform, add SMS/phone authentication, accept vendor contracts, render legal/privacy/licensing approval, purchase infrastructure, change AdGuard Home, process participants, publish, activate a market, launch, pass a lifecycle gate or infer successor PASS.
