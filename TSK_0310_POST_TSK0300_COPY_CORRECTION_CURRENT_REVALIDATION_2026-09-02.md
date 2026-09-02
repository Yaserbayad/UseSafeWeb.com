# TSK-0310 — Dependency-Complete Revalidation After Current TSK-0300 Protection-Copy Correction

**Task:** TSK-0310 — Build the representative mobile-first public-to-setup prototype before production implementation  
**Acceptance / Verification / Evidence:** ACC-0310 / VER-0310 / EVD-0310  
**Lifecycle / Priority / Authority:** L4 / HIGH / A3 / AUTO_ALLOWED  
**Date:** 2026-09-02 UTC  
**Candidate disposition:** CURRENT PASS pending independent current browser/dependency verification, durable evidence publication, guarded runtime reconciliation and exact read-back.

## 1. Revalidation trigger and preserved boundary

TSK-0310 previously achieved current PASS on 2026-09-02. That PASS was not replayed after a message timeout. A later artifact-specific audit found a genuine contradiction in current TSK-0300 protection-state reference copy, and TSK-0300 was corrected, independently verified and durably reaccepted at runtime commit `93fea25db8c1b6fd70a8fd45e0ff531cf33ea2e1`.

Because TSK-0300 is a direct hard predecessor of TSK-0310, current predecessor proof must be refreshed. Inspection then found the TSK-0310 prototype itself still encoded the superseded pre-CR-0008 protection-state IDs/primary copy. This is material to the Protection Map portion of ACC-0310, so a three-file source correction and fresh rendered verification are required.

The correction does **not** broaden ACC-0310 into optional-account/dashboard implementation. Current TSK-0318 continues to preserve TSK-0310 as the representative accountless public-to-setup core prototype for its own current ACC.

## 2. Current canonical contract and hard dependencies

Current planning inputs:

- WBS blob `b27a0c5df2f5636d8ed71051e9e26a68959a2616`;
- relationship-index blob `c108d2c162bcea2ee4cc01def46d0487a9501032`;
- pre-reconciliation runtime blob `1e68911d10eb648ac57a9e0f80b552f89dd9f823`.

TSK-0310 remains:

- L4 / HIGH / A3 / AUTO_ALLOWED;
- hard dependencies exactly `TSK-0318; TSK-0317; TSK-0320; TSK-0300`;
- ACC-0310 covering discovery, routing, native safeguard, DNS setup/verification, external service, Protection Map, troubleshooting, recovery/removal and limitations;
- VER-0310 requiring functional, negative, configuration, security/privacy and rollback checks.

## 3. Refreshed predecessor proof

### TSK-0300 — current corrected shared brand system

Current correction evidence: `TSK_0300_POST_CR0008_PROTECTION_COPY_CORRECTION_EVIDENCE_2026-09-02.md`, blob `a3e39896b67098ced321cb9e4b82c65c440806e4`.

Current TSK-0300 runtime reacceptance commit `93fea25db8c1b6fd70a8fd45e0ff531cf33ea2e1` proves the corrected shared-system README/status semantics while preserving:

- `tokens.css` blob `cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f`;
- `components.css` blob `831e92a74b6dda04252d93242cb33bd491a02381`;
- owner-approved SafeWeb identity masters;
- accountless core plus non-coercive optional account continuity.

TSK-0310 directly imports the unchanged token/component sources, so no token/component/identity redesign is required.

### TSK-0317 — current platform-path proof

Current evidence: `TSK_0317_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md`, blob `cd001f3ce391634e38ef0c89934cb34f4f347401`.

Its final independent run/job `33576615158 / 100081874297` passed current Android/iPhone install/verify/remove/recover mechanics, endpoint/conflict authority, accountless separation, SafeWeb naming, negative/rollback design and current ACC-0317.

The prototype continues to use:

- Android Private DNS hostname `dns.usesafeweb.com`;
- Apple DoH Server URL `https://dns.usesafeweb.com/dns-query`;
- explicit user/OS-controlled setup/removal;
- configuration/parent confirmation not equal to technical verification;
- truthful conflict/uncertainty paths.

No platform-path source correction is required.

### TSK-0318 — current scope proof

Current artifact `TSK_0318_POST_CR0008_DUAL_MODE_PUBLIC_PRODUCT_SETUP_IA_2026-09-01.md`, blob `975e2e7a8e85e9408e0bbbc2be226f3fdd012db3`, preserves TSK-0310's accountless public-to-setup prototype as evidence for TSK-0310's own ACC while keeping optional account/dashboard IA as a separate branch. No login/dashboard implementation is added to this prototype.

### TSK-0320 — current state/copy proof

Current contract `TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md`, blob `bdc6bacc424669708f410466f3cfd5527f1c2b3c`, supersedes the pre-CR-0008 TSK-0320 file previously cited by TSK-0310.

Canonical six-state identifiers/primary copy relevant to this prototype are now represented as:

- `protected/verified` → `Protection verified`;
- `configured/parent-confirmed` → `Setup confirmed`, with `Protection has not yet been technically verified.`;
- `action-needed` → `Action needed`;
- `not-covered` → `Not covered`;
- `uncertain/error` → `Protection status could not be verified`;
- `removed` → `Removed`.

## 4. Exact prototype source delta

Unchanged accepted sources:

- `prototype/TSK-0310/index.html` blob `5d80dfdefb52042bc34468723354fefd325285e4`;
- `prototype/TSK-0310/prototype.css` blob `004b0b34c0e5d94e3eacbeae25710284ef9a7886`;
- `prototype/TSK-0310/package.json` blob `9cbf9f5102592a0147c531748db49b68e4ee1648`;
- approved primary SafeWeb wordmark blob `f93958e3e4a16f9056693072c1b9b8b31fcda852`.

Corrected current sources:

- `prototype/TSK-0310/model.mjs` blob `cb35f7dbc46ba5d19da18fb09429b59e097e0492`, correction commit `3b7caa197b5f63d2b5232d54565b25a971dc29e0`;
- `prototype/TSK-0310/app.mjs` blob `a235993d5abcaac550b6c01978792092012afb00`, correction commit `b8fc8a60bf3976a1b07d8b65b995fe31ec25065b`;
- `prototype/TSK-0310/browser-acceptance.mjs` blob `5f68400a8bfb063853304e937f744e1ee71032e7`, correction commit `a43867e30a1b8e71d32de58345a103bb60a76d7c`.

The source delta is limited to:

1. canonical current evidence-state IDs and primary/supporting copy;
2. semantic constant use in the troubleshooting retry condition;
3. rendered text that previously said `Verified` / `Status uncertain`;
4. browser assertions updated to current canonical IDs/copy, including explicit S1/S2 checks.

No route, endpoint, platform setup/removal mechanics, network/privacy/storage behavior, CSS, identity, token/component source, login/account behavior or external dependency was added.

## 5. Historical evidence retained but not substituted for fresh verification

Historical rendered-browser evidence `TSK_0310_RENDERED_BROWSER_ACCEPTANCE_EVIDENCE_2026-08-29.md`, blob `02b34756862a62091908e60d32b490059a84a67c`, remains useful proof of the unchanged journey/platform/negative/privacy/rollback mechanics. TSK-0321 accessibility evidence blob `7ab9dd2467ca8ad755ef308c4b2ecade71023be8` remains applicable to unchanged CSS/accessibility remediation.

However, because current source changed in three files, historical 218-check PASS is **not** used as the current VER-0310 result. A fresh rendered-browser execution is required.

## 6. Independent verification contract

Current VER-0310 must independently prove:

1. current WBS/graph/runtime and all four dependency bindings;
2. current TSK-0300 correction evidence and unchanged shared token/components;
3. current TSK-0317 evidence and endpoint/platform compatibility;
4. current TSK-0318 accountless-core scope boundary;
5. current TSK-0320 canonical state IDs/copy;
6. exact current prototype source hashes;
7. no stale primary state copy in the current model/app/browser assertions;
8. rendered functional journey on Android/iPhone/unsupported routes;
9. negative/uncertain/not-covered/retry behavior;
10. configuration truth boundaries and exact DNS endpoints;
11. security/privacy properties: local-only resources, no storage/cookies/service worker, no unexpected external requests, no runtime/page errors;
12. removal/recovery/rollback behavior;
13. mobile/desktop layout checks and existing accessibility-remediated CSS;
14. repository source unchanged by the verifier.

## 7. Candidate disposition and non-inference

**ACC-0310 current candidate: PASS pending independent current VER-0310.**

No optional-account/dashboard implementation, authentication/provider architecture, persistence schema, integrated production build, legal/privacy completion, representative-parent behavior, participant/publication/payment/market activation, production behavior, lifecycle gate, launch, or successor PASS is inferred.
