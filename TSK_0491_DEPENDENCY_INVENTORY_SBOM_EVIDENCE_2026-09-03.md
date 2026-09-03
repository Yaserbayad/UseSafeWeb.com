# TSK-0491 — Dependency inventory, update policy, lock files, and SBOM evidence

**Task:** `TSK-0491 — Establish dependency inventory, update policy, lock files, and SBOM generation`  
**Acceptance / verification / evidence:** `ACC-0491 / VER-0491 / EVD-0491`  
**Evidence date:** 2026-09-03  
**Verifier:** GitHub Actions clean runners plus independent canonical GitHub read-back/review

## Authority and prerequisite

- Current WBS authority: L6 / MEDIUM / Security / A3 / `AUTO_ALLOWED`.
- Hard dependency: `TSK-0380`; current durable runtime authority records TSK-0380 PASS.
- Current linked authority: `REQ-0055`, `REQ-0056`, `CON-0009`, `CON-0028`, `RSK-0007`, `INT-0015`.
- This evidence changes no WBS, dependency, gate, requirement, risk, interface, action-authority, or lifecycle semantics.

## Canonical source implementation

Canonical source publication is GitHub `main` commit:

- commit: `59113366b14eca72101c1bc12bec0985cfd186c0`
- tree: `e6c8b05171b48df857f6393b6453baf93534b6bd`
- source PR: `#91`, expected-head squash merged only after the full exact-head regression matrix reached terminal success.

Exact canonical source blobs read back from that commit:

| Artifact | Git blob |
| --- | --- |
| `website/package.json` | `860b3045edf9bbba9e885f96367fe70bd92f4a35` |
| `website/package-lock.json` | `6ff91d845bc5f3099b6a00f5f43673eed80a3ba5` |
| `website/DEPENDENCY_SECURITY_POLICY.md` | `9f05741929e03e886e60daee35c12c63a78631e9` |
| `website/tests/contract/tsk0491.test.mjs` | `c7edfac073d8547b141ff3c68e2245751d42c9e6` |
| `.github/workflows/accept-tsk0491-dependency-sbom-20260903.yml` | `c7aa69093f6f18ba14fb464963ddff33a174a502` |

The dependency lockfile was not rewritten by TSK-0491; it remains the previously accepted exact dependency-tree authority at blob `6ff91d845bc5f3099b6a00f5f43673eed80a3ba5`.

## ACC-0491 implementation boundary

### Direct dependency and image inventory

The tracked executable dependency surface is the `website/` npm application. The Security-owned policy inventories every current direct runtime/development dependency from `package.json` and binds exact resolved versions to committed `package-lock.json` state.

Repository inspection for the current tracked execution surface found no Dockerfile, Compose definition, Python/Rust/Go dependency manifest, or workflow container/service/image reference. The accepted current image inventory is therefore **none**. The policy requires any future container image to be added to the inventory and pinned by immutable digest before satisfying this control.

### Deterministic lock and SBOM generation

`website/package.json` exposes:

`npm sbom --package-lock-only --sbom-format=spdx --sbom-type=application`

The CI acceptance workflow uses the frozen TSK-0380 toolchain (Node `22.23.2`, npm `10.9.8`), verifies the exact WBS and lockfile blobs, performs `npm ci`, generates an SPDX SBOM from committed lockfile state, parses it as SPDX `2.3`, and requires a non-empty package list.

The implementation is grounded in the official npm CLI v10 documentation matching the frozen npm 10 toolchain:

- `https://docs.npmjs.com/cli/v10/configuring-npm/package-lock-json/`
- `https://docs.npmjs.com/cli/v10/commands/npm-sbom/`
- `https://docs.npmjs.com/cli/v10/commands/npm-audit/`

### Update, severity, ownership, and exceptions

`website/DEPENDENCY_SECURITY_POLICY.md` makes Security the control owner and defines:

- routine dependency-freshness review;
- manifest + lockfile change discipline;
- `npm outdated` / `npm audit` review;
- Critical, High, Moderate, and Low severity disposition;
- blocking treatment for unresolved Critical/High findings unless a current explicit time-bounded exception exists;
- required exception fields including package/version, advisory/reason, severity, exposure, compensating control, owner, approval authority, decision date, and expiry/review date.

No unresolved dependency vulnerability exception is required by the accepted source evidence: both full and production-only audits returned zero vulnerabilities in the final verified runs.

## Test-first evidence

### RED

Initial RED run/job:

- run: `33763374342`
- job: `100674959853`

Canonical planning validation passed. The focused TSK-0491 contract failed only on the intentionally absent dependency-policy/SBOM controls, establishing the pre-implementation gap.

### Final feature/PR verification

Final PR source head: `ff8263eae6169a2fc5fa8b10702a4d7293b2ccf8`.

The exact-head PR regression matrix reached terminal SUCCESS across all 12 registered workflows before merge. The TSK-0491 task gate itself was:

- run: `33764883108`
- job: `100680073956`
- result: **SUCCESS**

That job verified, among other things:

- modular master-plan validator PASS;
- focused TSK-0491 contract `4/4` PASS;
- aggregate contract suite `105/105` PASS;
- Prettier check PASS;
- lint completed with zero errors and one pre-existing non-blocking `_accountState` warning in `core-state-machine.ts` not introduced by TSK-0491;
- typecheck PASS;
- Next.js production build PASS;
- SPDX 2.3 SBOM generated and parsed with a non-empty package list;
- `npm audit --audit-level=high`: zero vulnerabilities;
- `npm audit --omit=dev --audit-level=high`: zero vulnerabilities;
- clean-worktree/diff checks PASS.

## Clean-main confirmation

After guarded squash publication, all 12 workflows triggered by exact canonical `main` commit `59113366b14eca72101c1bc12bec0985cfd186c0` reached terminal SUCCESS. There were zero failed, queued, or in-progress workflows at the acceptance barrier.

The clean-main TSK-0491 gate was:

- run: `33765234931`
- job: `100681290132`
- result: **SUCCESS**

The final inherited browser-heavy clean-main gate was TSK-0359:

- run: `33765234882`
- job: `100681289522`
- result: **SUCCESS**, including its real-browser TSK-0359 and inherited accountless/locale acceptance step.

## VER-0491 independent disposition

Independent review of PR #91 and canonical read-back found no blocking correctness, security, architecture, or scope issue in the four-file TSK-0491 source change. The accepted source change does not modify application runtime behavior, the dependency lockfile, infrastructure, profiles, telemetry transport, deployment configuration, or any live target.

**ACC-0491 disposition:** PASS.  
**VER-0491 disposition:** PASS.  
**EVD-0491 disposition:** this document plus the exact GitHub source/run/blob references above provides durable reconstructable evidence.

## Explicit non-inference and preserved fences

TSK-0491 PASS proves only the current dependency inventory/update-policy/lockfile/SBOM acceptance boundary. It does **not** prove or authorize deployment, live-device/profile/certificate activity, service removal/revocation, participant processing, telemetry activation, public/production activation, market/launch action, a service-revocation interface, `TSK-0374` PASS, `TSK-0417` PASS, or `TSK-0499` PASS.

PR #86 remains a separate draft/unmerged TSK-0417 source-only checkpoint and is not consumed by this evidence.
