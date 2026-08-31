# TSK-0329 — Deterministic Verification Evidence

**Task:** TSK-0329 — Design and prototype Google sign-in, first-session account creation, and signed-in return interactions  
**Acceptance:** ACC-0329  
**Verification:** VER-0329  
**Evidence:** EVD-0329 deterministic post-CR-0007 verification  
**Date:** 2026-08-31  
**Final deterministic result:** PASS

## 1. Exact verified inputs

- WBS blob: `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`.
- Relationship graph blob: `c108d2c162bcea2ee4cc01def46d0487a9501032`.
- Pre-reconciliation runtime blob: `c080a364ef2eb5d0f3b168928b381a5328b3e751`.
- Current TSK-0328 IA blob: `527436958a1cd75fc91057410f4347ad56a3f53a`.
- Current TSK-0312 account/session requirements blob: `8dd71bccbd24ac5f62d5c536e644e7d9209b5832`.
- Normative TSK-0329 prototype: `prototype/TSK-0329/AUTH_ACCOUNT_INTERACTION_PROTOTYPE.md`, version `1.0.0-post-cr0007`, blob `bc9ff6c3240c06e12af977097ccbc05fca9ad8ef`.
- Structured interaction state model: `prototype/TSK-0329/INTERACTION_STATE_MODEL.json`, blob `c4ffbe4c5795b57dc074f41e1480fe610784679d`.
- Analytical evidence: `TSK_0329_AUTH_ACCOUNT_INTERACTION_ACCEPTANCE_EVIDENCE_2026-08-31.md`, blob `8f416952e33c09c3508d88ae5a5873b75f3814ca`.
- Corrected structured verifier: `.github/scripts/verify_tsk0329_post_cr0007_structured_20260831.py`, blob `a3226acb62c8ded1e016246d29843cc27a61fb4a`.
- Verification workflow: `.github/workflows/verify-tsk0329-post-cr0007-structured-20260831.yml`, blob `f88bdd71321c962a0bc290b9a847234b7915bc72`.

## 2. Final deterministic execution

- GitHub Actions run: `33409037262`.
- Job: `99543709479`.
- Runner: `adguardvm`.
- Head commit: `9d97f5d482b20a053f8561751d1d38ee58041212`.
- Conclusion: **SUCCESS**.

Observed PASS markers:

- `TSK0329_WBS_CONTRACT=PASS`
- `TSK0329_GRAPH_CONTRACT=PASS`
- `TSK0329_DEPENDENCY_RUNTIME=PASS`
- `TSK0329_STRUCTURED_MODEL=PASS`
- `TSK0329_ARTIFACT_STRUCTURE=PASS`
- `TSK0329_ANALYTICAL_AND_PASS_FENCES=PASS`
- `TSK0329_CURRENT_SCOPE_RECONCILIATION=PASS`
- `TSK0329_INDEPENDENT_VERIFICATION=PASS`

The workflow also completed `git diff --check` and clean-working-tree verification without failure.

## 3. Diagnostic history

Initial run/job `33408877929 / 99543192828` failed after WBS, graph, dependency/runtime and structured-model checks had already passed. The exact failure was `accessibility semantic missing: screen-reader`.

Root cause was a verifier section-scope false negative: the normative prototype already bound all states as `screen-reader understandable` in Section 2, while the verifier incorrectly required that exact phrase only inside Section 9. The verifier was corrected to evaluate the binding + accessibility contract together.

No normative prototype, state model, analytical evidence, WBS, graph, dependency evidence or runtime content was changed to obtain the final PASS.

## 4. Accepted interaction scope proven

The exact persisted candidate proves current ACC-0329 coverage for:

- Google sign-in as the only planned Version-1 account route, without local password/SMS/child login;
- explicit first-session product-account creation with minimum identity/data-use explanation;
- signed-in return to authorized dashboard continuity without strengthening technical protection evidence;
- provider unavailable, cancellation, network/unknown outcome, ambiguous identity, session creation failure and revoked/disabled states;
- session expiry/revocation and safe re-authentication without automatic replay of destructive actions;
- logout as session termination only;
- account-deletion entry with explicit separation from J0/J1 deletion and physical DNS removal;
- minimum intake classifications that prohibit child identity and password/SMS routes and do not require email/display-name/profile-image by default;
- back, refresh, retry and resume behavior that is idempotent and avoids duplicate account creation;
- accessible mobile-first and English/Turkish/Arabic+RTL-ready interaction semantics.

The complete accountless core remains available without login, and account/session/dashboard state never directly establishes technical `Verified` evidence.

## 5. Non-inference boundary

This evidence proves TSK-0329 only. It does not approve or infer:

- Google/Firebase vendor, OAuth/OIDC, provider/privacy/security architecture;
- cookie/token/CSRF/session implementation;
- persistent schema/storage/retention/backup/authorization implementation;
- actual account deletion execution;
- implementation/build/deployment/production behavior;
- real-user behavioral validation;
- TSK-0331, TSK-0332, TSK-0333, LG-06 or any later gate PASS.

`RSK-0002` remains OPEN/non-blocking before L8.

## 6. Disposition

`ACC-0329 / VER-0329 / EVD-0329`: **PASS**, subject only to successful guarded runtime reconciliation and read-back of `CURRENT_STATE.md`.

No successor or gate becomes PASS automatically from this evidence.
