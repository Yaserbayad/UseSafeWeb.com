# TSK-0325 — Deterministic Verification Evidence

**Task:** TSK-0325 — Create end-to-end parent journey and service blueprint  
**Acceptance:** ACC-0325  
**Verification:** VER-0325  
**Evidence:** EVD-0325 deterministic post-CR-0007 verification  
**Date:** 2026-08-31  
**Final result:** PASS

## 1. Exact verified inputs

- WBS blob: `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`
- Pre-reconciliation runtime blob: `6feab0d1991035304293c25c0af1398e75ff91f7`
- Normative blueprint: `prototype/TSK-0325/SERVICE_BLUEPRINT.md`
- Blueprint blob: `7763a6d16760d85df3ad23789f764d3e431849ef`
- Structured projection: `prototype/TSK-0325/ACCEPTANCE_MATRIX.json`
- Projection blob: `9826c7ab39e087002c6e0a51d7353e52ca6cc34b`
- Analytical evidence: `TSK_0325_POST_CR0007_PARENT_JOURNEY_SERVICE_BLUEPRINT_EVIDENCE_2026-08-31.md`
- Analytical evidence blob: `36d838ad4e9de2f705005a16930d72a768727d68`
- Final verifier: `.github/scripts/verify_tsk0325_post_cr0007_structured_20260831.py`
- Final verifier blob: `bae7ea3714495bb3a11f40dcadfecf3c714c1409`
- Workflow: `.github/workflows/verify-tsk0325-post-cr0007-structured-20260831.yml`
- Workflow blob: `e4741581d8d1a81cba0fc71ea943c965f8881007`

## 2. Final deterministic run

- GitHub Actions run: `33405928577`
- Job: `99533392966`
- Runner: `adguardvm`
- Head commit: `6fccbe97ef5db21f71d2f0bd4ab0ea8b2e8141f4`
- Conclusion: `SUCCESS`

Observed PASS markers:

- `TSK0325_WBS_CONTRACT=PASS`
- `TSK0325_DEPENDENCY_RUNTIME=PASS`
- `TSK0325_PATH_TOUCHPOINT_STRUCTURE=PASS`
- `TSK0325_PROJECTION_LIFECYCLE_CONTRACT=PASS`
- `TSK0325_ARTIFACT_LIFECYCLE_STRUCTURE=PASS`
- `TSK0325_ANALYTICAL_AND_PASS_FENCES=PASS`
- `TSK0325_CURRENT_SCOPE_RECONCILIATION=PASS`
- `TSK0325_INDEPENDENT_VERIFICATION=PASS`

The workflow also completed `git diff --check` and the clean-working-tree assertion without failure.

## 3. Diagnostic history and resolution

Earlier verifier failures are retained as diagnostic evidence and do not invalidate the final candidate artifacts because the normative blueprint, structured projection and analytical evidence blobs remained unchanged throughout the diagnostic sequence.

- Run/job `33403377960 / 99524887781`: failed on a brittle combined prose assertion for lifecycle separation.
- Run/job `33403496536 / 99525276969`: failed on an exact `revoke/unlink` sentence that was not the artifact's literal wording.
- Run/job `33404650885 / 99529094700`: structured verifier proved WBS/dependency/path/projection lifecycle checks, then failed because it expected `J0/J1 deletion` while the artifact used semantically equivalent `J0-J1 deletion` punctuation.
- Run/job `33405778331 / 99532895011`: lifecycle structure passed, then a substring ban falsely treated the explicit negative statement `does not infer current TSK-0328 IA PASS` as a positive downstream PASS claim.
- Run/job `33405928577 / 99533392966`: after replacing those brittle string interpretations with separator-insensitive and negation-aware semantic/structured checks, the full deterministic verifier passed.

No product-design requirement, acceptance criterion, normative blueprint content, structured acceptance projection, WBS definition or runtime state was changed to make the verifier pass.

## 4. Accepted scope proven by this verification

The current TSK-0325 artifact:

- covers all eight ACC-0325 paths: normal, already configured, unsupported, failed activation, false positive, resume, removal/recovery and support/help;
- contains exactly 17 current touchpoints and maps them to the required requirement/constraint/interface traces;
- preserves the complete login-free core journey;
- represents optional account/session/dashboard/device continuity without turning account access into a core-value gate;
- keeps J0/J1 separate from persistent account/device ownership and prohibits automatic promotion/linkage;
- keeps logout/session, revoke/unlink, device-record deletion, account deletion, J0/J1 deletion and physical DNS removal distinct in the applicable lifecycle semantics;
- prevents account/device persistence from becoming technical `Verified` evidence;
- preserves the exclusion of browsing/query/activity history, child accounts/profiles and raw/unrestricted AdGuard administration;
- does not infer TSK-0328, TSK-0329, implementation/build, behavioral validation, LG-06 or any later gate PASS.

## 5. Disposition

`ACC-0325 / VER-0325 / EVD-0325`: **PASS**, subject to successful durable runtime reconciliation and read-back of `CURRENT_STATE.md`.

This evidence proves TSK-0325 only. It creates no automatic successor or gate PASS.
