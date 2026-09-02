# TSK-0310 — Current Dependency-Complete Revalidation

**Task:** TSK-0310 — Build the representative mobile-first public-to-setup prototype before production implementation  
**Acceptance / Verification / Evidence:** ACC-0310 / VER-0310 / EVD-0310  
**Lifecycle / Priority / Authority:** L4 / HIGH / A3 / AUTO_ALLOWED  
**Revalidation date:** 2026-09-02 UTC  
**Candidate disposition:** ACC-0310 current PASS pending independent VER-0310 and guarded runtime reconciliation.

## 1. Current WBS contract

Read-only audit run/job `33577765903 / 100085362798` parsed canonical WBS blob `b27a0c5df2f5636d8ed71051e9e26a68959a2616` and graph blob `c108d2c162bcea2ee4cc01def46d0487a9501032` against runtime blob `2d2e3c9de8f247bcff4f54388002917127c55c24`.

Current contract:

- lifecycle `L4`;
- priority `HIGH`;
- AI capability `A3`;
- Action Authority `AUTO_ALLOWED`;
- hard dependencies exactly `TSK-0318; TSK-0317; TSK-0320; TSK-0300`;
- `ACC-0310 / VER-0310 / EVD-0310`;
- ACC-0310: prototype covers discovery, routing, native safeguard, DNS setup/verification, external service, Protection Map, troubleshooting, recovery/removal, and limitations;
- VER-0310: target-environment functional, negative, configuration, security/privacy, and rollback checks against acceptance;
- EVD-0310: artifact/version, source or exact environment, verification output, date, verifier, deviations and disposition.

The audit proved all four hard dependencies have durable PASS evidence under current authority.

## 2. Historical rendered-browser evidence retained

The accepted rendered-browser evidence remains `TSK_0310_RENDERED_BROWSER_ACCEPTANCE_EVIDENCE_2026-08-29.md`, blob `02b34756862a62091908e60d32b490059a84a67c`.

It records:

- `BROWSER_ACCEPTANCE_CHECKS=218`;
- `BROWSER_ACCEPTANCE=PASS`;
- `RENDERED_ACCEPTANCE=PASS`;
- functional PASS;
- negative-path PASS;
- configuration PASS;
- security/privacy PASS;
- rollback/recovery PASS;
- ACC-0310 PASS;
- VER-0310 PASS;
- EVD-0310 satisfied.

This historical evidence is retained because the current ACC remains the same public-to-setup core acceptance boundary. It is not used to infer optional-account/dashboard implementation.

## 3. Current authoritative prototype source

Current accepted source identities:

- `prototype/TSK-0310/index.html` — blob `5d80dfdefb52042bc34468723354fefd325285e4`;
- `prototype/TSK-0310/model.mjs` — blob `01343273fd09c3c12d26f0c0eb1ae9a2fce10c91`;
- `prototype/TSK-0310/app.mjs` — blob `a4a0aff8848f8541e2581e333efbf48767c9f0ff`;
- `prototype/TSK-0310/prototype.css` — current accessibility-remediated blob `004b0b34c0e5d94e3eacbeae25710284ef9a7886`;
- `prototype/TSK-0310/package.json` — blob `9cbf9f5102592a0147c531748db49b68e4ee1648`;
- `prototype/TSK-0310/browser-acceptance.mjs` — blob `f791a797f6a64be8b74eb13cbd2e628d5b083007`.

The only source difference from the earliest TSK-0310 rendered-browser evidence is the already accepted TSK-0321 accessibility remediation in `prototype.css`. TSK-0321 durable acceptance evidence `TSK_0321_ACCESSIBILITY_REVIEW_ACCEPTANCE_EVIDENCE_2026-08-29.md`, blob `7ab9dd2467ca8ad755ef308c4b2ecade71023be8`, proves the updated stylesheet was applied and the original TSK-0310 rendered regression suite reran `218/218` PASS with `TSK0310_RENDERED_REACCEPTANCE=PASS`; the accessibility suite also recorded `667/667` PASS.

Therefore there is no unresolved source-drift gap requiring prototype reconstruction.

## 4. Current TSK-0300 predecessor proof

Current TSK-0300 evidence is `TSK_0300_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md`, blob `efaf7c80c1723208569b13ba4e725b2e7cad8d1a`.

The prototype imports the current shared brand-system primitives directly:

- `brand/system/TSK-0300/tokens.css` — blob `cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f`;
- `brand/system/TSK-0300/components.css` — blob `831e92a74b6dda04252d93242cb33bd491a02381`.

TSK-0300 current revalidation changed no shared token/component values. Its CR-0006 correction was confined to shared-system public/product reference semantics, so TSK-0310's rendered product source is not invalidated by a token/component fork or identity change.

## 5. Approved SafeWeb identity preserved

`prototype/TSK-0310/index.html` still binds the approved primary SafeWeb wordmark:

- `brand/identity/TSK-0301/safeweb-wordmark-primary.svg` — blob `f93958e3e4a16f9056693072c1b9b8b31fcda852`.

The current page title remains `SafeWeb — Internal mobile-first prototype`. No identity reselection, visual redesign, token redesign, or parallel design system is introduced by this revalidation.

## 6. Current TSK-0317 predecessor proof

Current TSK-0317 evidence is `TSK_0317_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md`, blob `cd001f3ce391634e38ef0c89934cb34f4f347401`.

It preserves the platform mechanics already exercised by TSK-0310 while updating current authority/procedure/naming:

- Android uses the canonical Private DNS provider-hostname route;
- iPhone uses the approved DoH/profile route;
- configuration evidence is not technical protection evidence;
- install/verify/remove/recover remains accountless-capable;
- unsupported/conflicting platform conditions demote or stop claims rather than being hidden;
- current parent-facing generic naming is SafeWeb / SafeWeb DNS.

Canonical endpoint/platform semantics are owned by current TSK-0408 evidence `TSK_0408_CURRENT_ACCEPTANCE_EVIDENCE_2026-09-01.md`, blob `0bbf1d934ecd4a7693baf7de56362391e46dcf55`, which binds `dns.usesafeweb.com`, Android DoT/provider-hostname behavior, Apple DoH/Server-URL behavior, and truthful verification/removal/fallback rules.

No current TSK-0317/0408 requirement contradicts the existing TSK-0310 rendered paths.

## 7. Current TSK-0318 scope proof

Current TSK-0318 artifact is `TSK_0318_POST_CR0008_DUAL_MODE_PUBLIC_PRODUCT_SETUP_IA_2026-09-01.md`, blob `975e2e7a8e85e9408e0bbbc2be226f3fdd012db3`.

Current runtime explicitly preserves TSK-0310's accepted accountless public-to-setup core evidence for **TSK-0310's own current ACC** and separately states that this does not claim the historical TSK-0310 prototype implements the optional account/dashboard branch.

Therefore current dual-mode Version-1 IA does not broaden ACC-0310 into an account/dashboard implementation requirement. Rebuilding the prototype solely to add that separate branch would violate the current task boundary rather than satisfy it.

## 8. Current TSK-0320 state/copy proof

TSK-0320 remains durable PASS:

- contract `TSK_0320_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-08-28.md`, blob `1146f7622f434590dde1253d11f14fb6a87e19de`;
- evidence `TSK_0320_PROTECTION_STATE_MODEL_AND_COPY_RULES_EVIDENCE_2026-08-28.md`, blob `93e32071ce111fddda7df826c3106f1eca3dfc07`.

The accepted six-state evidence semantics remain compatible with the TSK-0310 rendered state-machine and Protection Map checks. No current contradictory state/copy evidence was found.

## 9. Current revalidation conclusion before independent verification

Read-only current-contract audit run/job `33577765903 / 100085362798` produced:

- `TSK0310_IMMUTABLE_INPUT_HASHES=PASS`;
- `TSK0310_CURRENT_WBS_CONTRACT=PASS`;
- all four `CURRENT_PREDECESSOR_PASS` checks PASS;
- `TSK0318_TSK0310_SCOPE_PRESERVATION=PASS`;
- `TSK0310_CURRENT_ACCESSIBILITY_REMEDIATION=PASS`;
- `TSK0310_HISTORICAL_RENDERED_EVIDENCE=PASS`;
- `TSK0310_CURRENT_SAFEWEB_SHARED_SYSTEM_BINDING=PASS`;
- `TSK0310_NEW_PREDECESSOR_EVIDENCE_AVAILABLE=PASS`;
- `TSK0310_ENDPOINT_AUTHORITY_BINDING=PASS`;
- `TSK0310_CURRENT_CONTRACT_AUDIT=PASS`.

Three preceding read-only diagnostic runs are retained only as verifier/audit-shape evidence:

1. first run found the legitimate TSK-0321 stylesheet mutation;
2. second run exposed a non-uniform historical TSK-0321 runtime heading;
3. third run exposed endpoint-proof duplication across authority owners.

None changed product/runtime state. Each correction made the audit more authority-aligned rather than weakening acceptance.

## 10. Deterministic current assertions

1. Current WBS contract and four hard dependencies are exact and current.
2. Historical TSK-0310 rendered-browser evidence remains applicable to the unchanged ACC boundary.
3. Current prototype sources equal the accepted source set plus only the already reaccepted TSK-0321 stylesheet remediation.
4. Current TSK-0300 shared tokens/components are exactly the imported files and are unchanged by its current revalidation.
5. Approved SafeWeb wordmark/identity remains the bound current identity.
6. Current TSK-0317 platform-path semantics are compatible with existing Android/iPhone TSK-0310 paths.
7. Current TSK-0408 owns and confirms endpoint/platform semantics rather than requiring duplicated TSK-0317 prose.
8. Current TSK-0318 preserves TSK-0310's accountless public-to-setup evidence for its own ACC and does not broaden it into optional-account/dashboard implementation.
9. Current TSK-0320 evidence-state/copy semantics remain compatible.
10. No new login, account, child profile, browsing/query/activity history, raw DNS administration, or payment requirement is added to ACC-0310.
11. No identity redesign, shared-token redesign, design-system fork, or prototype rebuild is justified by current evidence.
12. Current browser verification must still independently execute functional, negative, configuration, security/privacy, and rollback checks before runtime PASS reconciliation.

## 11. Candidate disposition

**ACC-0310 current candidate: PASS pending independent current VER-0310.**

No product-source mutation is proposed. The independent verifier must hash-lock current authority/source, run source/model checks, execute the rendered browser suite in an isolated current environment, verify current predecessor compatibility, and fail closed on any genuine contradiction.

## 12. Non-inference

This candidate concerns current L4 public-to-setup prototype acceptance only. It does not prove optional account/dashboard implementation, integrated production build, authentication/provider architecture, persistent schema/storage, legal/privacy completion, representative-parent evidence, participant activity, publication, payment, market activation, production behavior, LG-06, launch, or any successor PASS.
