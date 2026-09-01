# TSK-0299 — Post-CR-0008 Acceptance Evidence

**Task:** TSK-0299 — Define tone, voice, terminology, trust language, protection-state language, and communication examples  
**Acceptance / Verification / Evidence:** ACC-0299 / VER-0299 / EVD-0299  
**Lifecycle / Priority / Authority:** L4 / HIGH / A3 / AUTO_ALLOWED  
**Date:** 2026-09-01  
**Disposition:** PASS — subject to durable `CURRENT_STATE.md` synchronization and independent read-back.

## 1. Current acceptance boundary and reopening reason

The historical TSK-0299 PASS was reopened under DEC-0053/CR-0006 because `TSK_0299_PROVISIONAL_VERBAL_SYSTEM_2026-08-29.md` explicitly prohibited implying that an account, persistent device profile or dashboard existed in the Version-1 baseline. CR-0006 subsequently activated the optional parent-account/session/lightweight-dashboard/device-management branch while preserving a fully usable accountless core. The historical artifact also used protection-state labels superseded by the current TSK-0320 contract.

Historical evidence remains preserved for unchanged tone, voice, plain-language, non-alarmist, non-surveillance, claims-limitation and localization principles. No historical evidence was deleted or rewritten.

## 2. Canonical execution inputs

Current immutable identities used by the independent verifier:

- WBS: `Plans/Master/WBS/master-wbs.csv`, blob `b27a0c5df2f5636d8ed71051e9e26a68959a2616`.
- Relationship graph: `Plans/Master/RELATIONSHIP_INDEX.yaml`, blob `c108d2c162bcea2ee4cc01def46d0487a9501032`.
- Pre-synchronization runtime: `CURRENT_STATE.md`, blob `d427e03dfe343187c17fe4383cd3893084a599d3`.
- Historical TSK-0299 artifact: blob `a4ff2314ff02c407249e8b5d4d6b9600b89403b3`.
- Current hard-dependency artifact TSK-0298: `TSK_0298_EVIDENCE_GROUNDED_BRAND_STRATEGY_2026-08-29.md`, blob `73d8587ef9bb37d92b44f102d5a33545b416c44b`; runtime TSK-0298 is current accepted PASS.
- Current TSK-0318 IA: blob `975e2e7a8e85e9408e0bbbc2be226f3fdd012db3`.
- Current TSK-0319 help/recovery design: blob `dec2b556745c635656fa0f18945c63c47120f6ff`.
- Current TSK-0320 protection-state/copy contract: blob `bdc6bacc424669708f410466f3cfd5527f1c2b3c`.

Exact WBS contract proven before execution:

- L4 / HIGH / A3 / `AUTO_ALLOWED` / `PLANNED`;
- hard dependency: `TSK-0298`;
- `ACC-0299 / VER-0299 / EVD-0299`;
- acceptance requires plain-language, child-aware, non-alarmist, non-technical parent-facing design; current approved claims/non-surveillance constraints; reuse across surfaces/locales; L8-only human comprehension validation under DEC-0052; and no implied pre-product human validation or deferred legal completion.

## 3. Current accepted candidate

Artifact: `TSK_0299_POST_CR0008_DUAL_MODE_VERBAL_SYSTEM_2026-09-01.md`

- version: `2.0.0-post-cr0008`;
- publication commit: `284a566c9ff282e35bc2500f1060a0869262bb37`;
- blob: `ff30500b933b9ecc92325659d49ea4e671d296d2`.

The candidate preserves the compatible historical verbal system while updating the current contract for:

- complete accountless core plus optional account/session/dashboard/device management;
- optional sign-in as continuity/device management, never stronger protection;
- no automatic J0/J1-to-account linkage or TTL extension;
- current TSK-0320 S1–S6 labels and supporting copy;
- account/provider/session failure language with accountless continuation;
- dashboard/device language that never implies browsing/query/activity surveillance or technical verification from ownership;
- distinct Start over / logout / unlink-revoke / device-record deletion / account deletion / physical DNS removal consequences;
- unknown consequential outcomes that require reconciliation rather than blind retry;
- coherent public, accountless-product, account/dashboard, help, status and privacy/settings language;
- English/Turkish/Arabic plus RTL semantic invariants without implying non-UK market activation;
- explicit RSK-0002/L8 behavioral-validation limitation and legal/privacy/provider/implementation/publication non-inference.

## 4. Independent deterministic verification

Verifier: `.github/workflows/verify-tsk0299-post-cr0008.yml`

- workflow publication commit: `7929e14cef821710a6440afcadcdfd2028572f76`;
- workflow blob: `fb3d23d300c6154d95f23ae4d8275ddb22f969b8`;
- permissions: `contents: read`;
- runner: GitHub-hosted Ubuntu 24.04;
- checkout: current `main` at verifier execution;
- run: `33571984135`;
- job: `100067714979`;
- conclusion: **SUCCESS**.

Observed verifier outputs:

- `TSK0299_WBS_CONTRACT=PASS`
- `TSK0299_CURRENT_DEPENDENCY=PASS`
- `TSK0299_DUAL_MODE_SCOPE=PASS`
- `TSK0299_PLAIN_CHILD_AWARE_NONALARMIST=PASS`
- `TSK0299_CURRENT_STATE_COPY=PASS`
- `TSK0299_ACCOUNT_TRUST_LANGUAGE=PASS`
- `TSK0299_LIFECYCLE_SEPARATION=PASS`
- `TSK0299_CROSS_SURFACE_REUSE=PASS`
- `TSK0299_LOCALIZATION_RTL=PASS`
- `TSK0299_CLAIMS_NONSURVEILLANCE=PASS`
- `TSK0299_BEHAVIORAL_LEGAL_NONINFERENCE=PASS`
- `TSK0299_SUCCESSOR_INTEGRITY=PASS`
- `TSK0485_PRESERVED_INPUT=PASS`
- `TSK0318_PRESERVED_INPUT=PASS`
- `TSK0319_PRESERVED_INPUT=PASS`
- `TSK0299_ACCEPTANCE=PASS`

The verifier independently re-hashed every bound input and reproduced the exact artifact/WBS/graph/runtime identities listed above before running semantic assertions and `git diff --check`.

## 5. ACC-0299 proof

ACC-0299 is satisfied for the current L4 design boundary because the independently verified artifact:

1. uses parent-facing plain language and a calm, respectful, child-aware, non-alarmist voice;
2. keeps technical implementation detail secondary to the user action;
3. expresses current dual-mode Version-1 scope without mandatory login for core value;
4. preserves current protection truth exactly from TSK-0320;
5. prevents account/dashboard/device ownership from being described as technical verification;
6. explicitly excludes surveillance, browsing/query/activity history, child accounts/profiles and broad DNS administration;
7. provides reusable current CTA, status, trust, failure, lifecycle and recovery language across all current surface classes;
8. preserves exact destructive-operation object/consequence separation and unknown-outcome reconciliation;
9. preserves English/Turkish/Arabic+RTL semantic strength and optionality without inferring market activation; and
10. explicitly retains RSK-0002 and the absence of pre-L8 representative-parent comprehension evidence or deferred legal completion.

## 6. Successor and preserved-state impact

- TSK-0301 is the direct WBS successor and still has two hard dependencies: `TSK-0302; TSK-0299`. This evidence does not make TSK-0301 PASS and does not prove TSK-0302 current validity.
- TSK-0316 remains a separately reopened current-scope requalification candidate until independently resolved.
- TSK-0485, TSK-0318 and TSK-0319 were immutable current runtime inputs during independent verification. No runtime mutation occurred in the verifier.

## 7. Non-inference

This acceptance is L4 verbal-system design PASS only. It does not prove representative-parent comprehension, implementation/build, provider integration/acceptance, legal/privacy completion, public publication, payment, participant activation, named-market activation, LG-06 or any downstream gate/task, production behavior or launch.

**Stable outcome before runtime synchronization:** ACC-0299 / VER-0299 / EVD-0299 are independently proven PASS. TSK-0299 must not be treated as durably synchronized runtime PASS until `CURRENT_STATE.md` is updated, written to GitHub, read back and verified while preserving TSK-0485 and synchronized TSK-0318/TSK-0319 sections byte-for-byte.
