# TSK-0328 — Information Architecture and Navigation Acceptance Evidence

**Evidence ID:** EVD-0328  
**Task:** TSK-0328 — Define information architecture and navigation model  
**Date:** 2026-08-29  
**Verifier:** ChatGPT Web / SERIAL LIGHT Governor with independent GitHub Actions execution on `adguardvm`  
**Disposition:** PASS  
**Sequencing:** DEC-0052 / CR-0005

## Artifact/version

- Normative IA/navigation contract: `prototype/TSK-0328/INFORMATION_ARCHITECTURE_NAVIGATION.md` v1.0.0, blob `4efb624005061e242e427994953d0fc00fcd745f`, publication commit `908871d1474645b8939a32a1c94f5433e8c3a716`.
- Non-authoritative machine projection: `prototype/TSK-0328/IA_MAP.json` v1.0.0, blob `2f77c1a844f16cf080817bf4ea31c80bb7067a06`, publication commit `7108fe18205ec95c013ab152c8055a69a25013f5`.
- Final verification workflow: `.github/workflows/verify-tsk0328-v2.yml`, blob `deaa026379874b2d4fa92761f39037608cad8d0e`, commit `bbcb0a9ee335ae082b47710fa42a92dd9082ec60`.

## Exact source/environment

Final verification ran from exact GitHub `main` head `bbcb0a9ee335ae082b47710fa42a92dd9082ec60` on self-hosted runner `adguardvm` and pinned:

- `prototype/TSK-0325/SERVICE_BLUEPRINT.md` — `1701f5f7b13ac8f7fa3092e39005b3da7627c89f`.
- `TSK_0318_PUBLIC_PRODUCT_SETUP_IA_DESIGN_CANDIDATE_2026-08-28.md` — `64f0e6382a5ce166c0aad2ad2e86a3796c5df379`; used only for its owner-approved compatible public-vs-product split, with older naming/sequencing superseded by current authority.
- `prototype/TSK-0309/BASELINE.md` — `76bb848ebdf6a2aee4dd84bc18e8af5ba8a99dbc`.
- `prototype/TSK-0324/UI_COMPONENT_RULES.md` — `0b7012a12070f7eccf45a1bbb2f453fde8507ff6`.
- `content/TSK-0322/PRODUCT_VOICE_CLAIMS_TERMINOLOGY.md` — `d12c1e707f0390915002b27bf3a5073d0135d466`.
- `Plans/Master/WBS/master-wbs.csv` — `f23b4f017d1baf73258fa30ecd71549bbfe1b815`.

WBS authority was rechecked as L4 / PLANNED / MEDIUM / A3 / AUTO_ALLOWED with sole dependency `TSK-0325`; canonical runtime independently proves `TSK-0325` PASS.

## Verification output

Final GitHub Actions run `33271356007`, job `99150274452`: **success**.

Terminal acceptance markers:

- `TSK0328_WBS_AUTHORITY=PASS`
- `TSK0328_DEPENDENCY_TSK0325=PASS`
- `TSK0328_SOURCE_BLOBS=PASS`
- `TSK0328_SYSTEMS=2/2_PASS`
- `TSK0328_PUBLIC_ROUTES=6/6_PASS`
- `TSK0328_SETUP_SCREENS=15/15_GOAL_TRACE_PASS`
- `TSK0328_REQUIRED_PATHS=8/8_PASS`
- `TSK0328_ACCOUNTLESS_NO_UNNECESSARY_SECTIONS=PASS`
- `TSK0328_NAV_STATE_PRIVACY=PASS`
- `TSK0328_ACCESSIBILITY_RTL=PASS`
- `TSK0328_ACC_VER_EVD=PASS`
- `REPOSITORY_CLEAN=PASS`

## ACC-0328 evaluation

ACC-0328 requires architecture that supports normal and exception paths, avoids unnecessary sections/accounts, and maps every screen to a user goal and requirement.

Result: **PASS**.

The accepted model contains exactly two connected systems (public information and operational setup), six public route intents, one generic noindex `/setup` operational route, and 15 independently testable logical setup screens. Every logical screen has one primary user goal, one or more TSK-0325 touchpoint bindings, `REQ-0028`, and the applicable requirement/constraint/interface trace. All eight required TSK-0325 paths are represented: normal, already configured, unsupported, failed activation, false positive, resume, removal, and support.

The architecture explicitly excludes Login/Sign up/Account/Dashboard/Profile, payment-before-value, customer-facing AdGuard administration, browsing/query history, user-specific status URLs, unnecessary onboarding/acknowledgement pages, and duplicated mutable support/instruction/state authority.

## VER-0328 evaluation

Applicable internal/source/automated review passed against the current service blueprint, owner-approved compatible IA predecessor, implementation-ready experience baseline, current UI rules, claims/terminology and WBS. Pre-product parent/user evidence is excluded by DEC-0052 / CR-0005 and is neither fabricated nor claimed.

Navigation/privacy assertions prove that public content cannot manufacture protection state, setup uses transient in-memory state without account/cookie/storage assumptions, Help/Limitations are state-neutral utility detours, browser Back is not treated as an evidence-state machine, Start over is distinct from DNS removal, and lost transient state restarts rather than fabricating persistence.

## Verification-harness deviation and correction

The first verifier run `33271313226`, job `99150159697`, failed at its final prose-string guard after all preceding structural/source/WBS/path/screen/accountless checks had passed. The guard incorrectly required the literal phrase `no mandatory onboarding tour`; the unchanged artifact expresses the same rule structurally as `The current IA has no:` followed by bullet `mandatory onboarding tour`.

This was classified as a verifier false negative. No product/IA artifact was changed. The corrected full verifier replaced that literal-string assertion with the actual document structure and reran the entire acceptance suite successfully in run/job `33271356007` / `99150274452`.

## Deviations and disposition

- The older TSK-0318 IA candidate remains historical design authority only where compatible. Its old visible `UseSafeWeb` naming and CR-0003 sequencing are not propagated; current `SafeWeb` identity and CR-0005 sequencing govern.
- No mandatory standalone Completion screen is introduced; the Protection Map remains the truthful end-of-journey review and the parent may exit without ceremonial acknowledgement.
- No persistence/account reason is created by navigation architecture.
- `TSK-0308` and `TSK-0321` remain HUMAN_ONLY and are not self-certified by this PASS.
- `RSK-0002` remains OPEN. No real-parent/native-speaker comprehension, production implementation, public publication, participant processing, payment, market activation or launch authority is inferred.
