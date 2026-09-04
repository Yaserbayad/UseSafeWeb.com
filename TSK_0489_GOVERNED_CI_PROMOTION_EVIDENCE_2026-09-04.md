# EVD-0489 — Governed CI and conditional promotion evidence

**Task:** TSK-0489 — Implement continuous integration quality and security gates  
**Acceptance:** ACC-0489  
**Verification:** VER-0489  
**Evidence:** EVD-0489  
**Disposition:** **PASS — restored after AG-009 remediation**  
**Current canonical repair merge:** `26a8f786b5e74e665b5c19a9b156b68b5ced10be` (PR #103)

## Supersession notice

The earlier PASS narrative in this evidence file is superseded. PR #99 remains valid historical provenance for a deliberate failing case, the original implementation, and later main validation, but its claimed **exact PR source-head** proof was incorrect: the pull-request workflow tested GitHub's synthetic merge commit rather than the real source-branch SHA and emitted that synthetic merge as the promotion head. AG-009 also exposed repository-write paths that could mutate `main` outside the intended evidence-gated promotion boundary. Those defects invalidated the earlier PASS conclusion until repaired and re-proven.

No scope, requirement, dependency, acceptance, verification, planning-baseline, deployment, activation, participant, payment, telemetry, credential, service-revocation, or launch authority was changed by this remediation.

## Authority and prerequisites

- TSK-0489 remains `A3 / AUTO_ALLOWED` with hard predecessors TSK-0453, TSK-0491, and TSK-0422 current PASS under durable project authority.
- ACC-0489 requires approved checks on pull/change requests and `main`, promotion blocking on failure, retained evidence, and recorded owner authority for any test bypass.
- DEC-0060 / CR-0013 authorize deterministic automated evidence-gated promotion in place of mandatory human/Code Owner review while preserving every genuine human/material-action boundary.
- `.github/CHANGE_REVIEW_POLICY.md` requires exact current PR source-head checks immediately before merge and prohibits stale, failed, pending, skipped-required, or unknown evidence from authorizing promotion.

## AG-009 defect boundary

1. **Synthetic merge mistaken for source head:** PR #99 source head was `5ec96d4e15a9c40337fdb3c0cddf30540db20bc2`, while the governed pull-request job checked out synthetic merge `a4833e06be195c4ab045aca5e623b021d5f602d4` and emitted that synthetic SHA as `TSK0489_PROMOTION_HEAD`. The former exact-source interpretation is therefore invalid.
2. **Direct workflow write surfaces:** historical one-shot workflows included executable `contents: write` / direct-main mutation paths that could change canonical state before the governed gate observed it. Those active entrypoints were archived or removed from `.github/workflows` during PRs #101/#102.
3. **Indirect executable write surface:** after the first cleanup, `.github/workflows/adguard-clean-recovery-drill.yml` still had `contents: write`, credential-persisting checkout, and called `infrastructure/adguard-server/publish-recovery-drill-evidence.sh`, which executed `git push origin HEAD:main`. The original scanner inspected workflow YAML but did not transitively inspect called executables. PR #103 closed this remaining boundary.

## Repair and verification chain

### 1. Exact-source binding and initial governance repair — PR #101

- Final PR source head: `64c61d363cce36374589914c6852857c563066fc`.
- Governed PR run: `33890556819` — success.
- The repaired workflow resolves pull-request source from `github.event.pull_request.head.sha`, push source from `github.sha`, explicitly checks out that source SHA with `persist-credentials: false`, proves `git rev-parse HEAD == source_sha`, rejects a mismatched SHA fail-closed, and emits the real source SHA for promotion.
- Canonical local/CI validation passed 111/111 contract tests, lint with zero errors, typecheck, production build, SPDX SBOM generation/validation, zero-vulnerability npm audits, governance validation, full-history secret scan, security/privacy checks, and clean-tree checks.
- Retained artifact: `9943679620`; digest `sha256:c54f18cd943b3d096f9823e7bd21186d05bd3af39e011786a5954d685ff8026f`.
- PR #101 merged as canonical commit `aae5c44fb0dd5d414f9667cf96a83410bf3708b4`.

### 2. Stale main-workflow cleanup — PR #102

- Final source head: `d583f276dc3c6d62c9162a7fa9f633e6f57e6aff`.
- Obsolete task-specific main acceptance harnesses were removed from the active workflow directory while historical implementation/evidence remained retained.
- Canonical merge became `0e6e247156d1ed3410159ae69fab4ee9b2e1319e`.
- Exactly three applicable workflows ran on that canonical commit and all passed: TSK-0489 run `33892790639`, TSK-0491 run `33892790752`, and TSK-0453 run `33892790746`.
- TSK-0489 retained artifact `9944542795`; digest `sha256:1c631458870644884e75d80d2643feed383710c59c6b12d35d6f7b1bdb2feec9`.

### 3. Controlled RED proof for the remaining indirect writer — PR #103

The workflow-governance audit was first strengthened to follow executables referenced by active workflows before the known recovery writer was removed. This deliberately produced a fail-closed source head.

- Deliberate RED source head: `a15bc79ac5e4675d2fe010bed27fbd36a7f44e35`.
- Governed run: `33894506486` — **failure as required**.
- Promotion job did not run/authorize promotion.
- The strengthened audit detected the exact remaining violations:
  - active write-capable checkout without `persist-credentials: false` in `.github/workflows/adguard-clean-recovery-drill.yml`;
  - direct-main `git push origin HEAD:main` in the transitively called `infrastructure/adguard-server/publish-recovery-drill-evidence.sh`;
  - the same reachable push classified as a write-workflow executable violation.
- Retained failure artifact: `9945173597`; digest `sha256:7fe0d37eb6751a61516e065562e165f72863a44e42bafe587ee298909175adef`.

This is the current negative proof that a discovered bypass blocks promotion rather than being silently accepted.

### 4. Repaired exact-head GREEN proof — PR #103

The obsolete TSK-0431 recovery workflow was preserved under `.github/workflow-archive/tsk0489-ag009/` and removed from the active `.github/workflows` execution surface. The final scanner recursively inspects referenced shell/Python/JavaScript/TypeScript executables and local composite actions from active workflows.

- Final PR source head: `863b4aa12d89d70eff631784124d8cacd5a84a98`.
- Governed run: `33894582672`.
- `governed-ci` job `101094112459`: success.
- `promotion-eligibility` job `101094399784`: success.
- Exact source binding: PASS; mismatched source SHA rejection: PASS.
- Workflow governance: PASS.
- Active workflow count: **112**.
- Active write-surface count: **0**.
- Transitively reachable executable count: **77**.
- Master-plan validation: PASS — 641 tasks, 858 dependency edges, 0 recurring hard predecessors, 0 broken links.
- Local/CI parity: `npm run validate`.
- Contract suite: **111/111 PASS**.
- Lint: zero errors; typecheck and production build: PASS.
- SPDX/dependency audit: PASS; npm vulnerability audits: **0 vulnerabilities**.
- Full-history secret scan and synthetic credential rotation/revocation/break-glass/rollback checks: PASS.
- Security/privacy gate: PASS; clean tree: PASS.
- `TSK0489_PROMOTION_HEAD=863b4aa12d89d70eff631784124d8cacd5a84a98`.
- `TSK0489_PROMOTION_ELIGIBLE=YES`.
- `TSK0489_DEPLOYMENT_AUTHORITY=NONE`.
- Retained artifact: `9945229500`; digest `sha256:aa96baa237ca292a720a570af734252e0ed27b976d598c6b569871c6dbedffb8`.

Immediately before merge, both the PR source head and canonical base were reread and remained unchanged. PR #103 was merged only with expected source head `863b4aa12d89d70eff631784124d8cacd5a84a98` after every applicable exact-head check was successful.

Canonical repair merge: `26a8f786b5e74e665b5c19a9b156b68b5ced10be`.

### 5. Post-merge canonical-main proof

Exactly three applicable workflows ran on canonical `main@26a8f786b5e74e665b5c19a9b156b68b5ced10be`, and all completed successfully:

- TSK-0489 governed CI: run `33894750987`.
  - `governed-ci` job `101094663912`: success.
  - `promotion-eligibility` job `101095129846`: success.
  - `GITHUB_TOKEN` contents permission: read.
  - authoritative source / checkout / promotion head: exact canonical `26a8f786b5e74e665b5c19a9b156b68b5ced10be`.
  - explicit checkout `persist-credentials: false`.
  - source-SHA binding and mismatch rejection: PASS.
  - workflow governance: PASS — **112 active workflows, 0 active write surfaces, 77 transitively reachable executables**.
  - master-plan governance validation: PASS.
  - contract suite: **111/111 PASS**; lint zero errors; typecheck/build PASS.
  - SBOM/dependency audits: PASS; npm vulnerability audits: **0 vulnerabilities**.
  - full-history secret scan: PASS; security/privacy gate: PASS; clean tree: PASS.
  - `TSK0489_PROMOTION_ELIGIBLE=YES`.
  - `TSK0489_PROMOTION_HEAD=26a8f786b5e74e665b5c19a9b156b68b5ced10be`.
  - `TSK0489_DEPLOYMENT_AUTHORITY=NONE`.
  - retained artifact: `9945317612`, size 9016 bytes; digest `sha256:8cee845c82cbce9b4e7fc6afdce47cdefb5cf990688379e6ff92285e44f32189`.
- TSK-0453 quality/review acceptance: run `33894750950` — success.
- TSK-0491 dependency/SBOM acceptance: run `33894751052` — success.

## VER-0489 coverage

- **Functional:** canonical validation, contract suite, lint/typecheck/build, dependency/SBOM gates and exact-head promotion all pass on PR and `main`.
- **Negative:** deliberate PR #103 RED head is blocked; explicit all-zero source-SHA mismatch is rejected with the governed gate fail-closed.
- **Configuration:** workflow token is read-only, checkout is bound to the authoritative SHA with persisted credentials disabled, workflow/reachable-executable scan reports zero active write surfaces, and promotion output is bound to the exact source.
- **Security/privacy:** full-history secret scanning, dependency vulnerability audits, privacy/security checks, external-secret handling, rotation/revocation/break-glass and temporary-secret cleanup all pass.
- **Rollback/recovery:** synthetic rollback passes; obsolete active write harnesses were archived rather than losing historical provenance; the deliberate RED remediation is reversible and no target/live system mutation occurred.

## ACC-0489 disposition

**ACC-0489 is satisfied and TSK-0489 PASS is restored.** Approved governed checks execute on pull/change requests and `main`; failures and source-SHA mismatches fail closed before promotion; executable evidence is retained; no test bypass was used; final promotion is exact-source-head bound; active workflow and transitively reachable executable inspection finds no repository write surface; post-merge canonical `main` reran the applicable checks successfully.

The former PR #99 exact-source-head claim is historical/superseded and must not be used as current PASS proof.

## Material-action fence proof

The final PR and canonical-main runs explicitly record:

- `TSK0489_DEPLOYMENT_ACTION=NONE`
- `TSK0489_ACTIVATION_ACTION=NONE`
- `TSK0489_PARTICIPANT_ACTION=NONE`
- `TSK0489_SERVICE_MUTATION=NONE`
- `TSK0489_PAYMENT_ACTION=NONE`
- `TSK0489_LAUNCH_ACTION=NONE`
- `TSK0489_MATERIAL_ACTION_FENCES=PASS`

This PASS does **not** authorize deployment, activation, participant processing, service mutation/revocation/removal, credential mutation, payment, telemetry activation, launch, or any other separately fenced material action.
