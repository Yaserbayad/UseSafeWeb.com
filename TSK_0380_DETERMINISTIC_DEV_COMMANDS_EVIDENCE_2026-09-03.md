# TSK-0380 — Deterministic development commands acceptance evidence — 2026-09-03

## Disposition

**PASS candidate for `ACC-0380 / VER-0380 / EVD-0380`, pending canonical runtime synchronization in the same guarded publication.**

This evidence is limited to the development-foundation outcome “Implement deterministic local build, lint, test, and validation commands.” It creates no deployment, live-device/profile action, service removal/revocation, participant processing, telemetry activation, market/launch action, `TSK-0374 PASS`, `TSK-0417 PASS`, or `TSK-0499 PASS` conclusion.

## Canonical task contract

- Task: `TSK-0380` — Implement deterministic local build, lint, test, and validation commands.
- Hard predecessor: `TSK-0454` — current durable PASS before execution.
- Authority: A3 / `AUTO_ALLOWED`.
- Acceptance: `ACC-0380` — clean environment setup succeeds; build/lint/type/test/validation commands return nonzero on failure; required versions are pinned/bounded; no undocumented manual step is required.
- Verification: `VER-0380` — functional, negative, configuration, security/privacy, and rollback checks against the exact development environment/source.
- Evidence: `EVD-0380` — exact environment/source, outputs, date, verifier, deviations/disposition.
- Current linked planning entities remain `REQ-0036`, `REQ-0037`, `CON-0010`, `CON-0011`, `RSK-0045`, `INT-0011`, and `INT-0012`.

## Canonical implementation

Canonical source merge: `1ee48aeb28d2fb01411bd971e83a305287baa2fd`.
Canonical tree: `6a9d04c326782dd9b42d99a0d46d446761b1131e`.
Merged PR: `#87`.

Exact published artifacts:

- `website/.nvmrc` — blob `c94711948a665d304dfc7016e1bebc497162b451`; exact Node baseline `22.23.2`.
- `website/package.json` — blob `29acdf46a7b9ef8660f788cde519d62c8f74602c`; exact npm baseline `npm@10.9.8`; deterministic `validate` chain: contract tests -> lint -> typecheck -> build.
- `website/package-lock.json` — unchanged canonical blob `14f9a62607489f965b96d98cdf0d825a363cd8bc`; no dependency mutation was required.
- `website/README.md` — blob `737c0c017fa646c7f91b60e9568e1d457958bd53`; documents clean checkout setup (`nvm use`, `npm ci`, `npm run validate`) and states no repository-specific hidden step.
- `website/tests/contract/tsk0380.test.mjs` — blob `05c77e16cb487f9a942231de9f066be706b1483d`.
- `.github/workflows/accept-tsk0380-deterministic-dev-commands-20260903.yml` — blob `bd04edf5d9cb55ad70d9653b759f27e870306637`; runs on PR/feature branch and canonical `main`.

No application runtime behavior, infrastructure configuration, profile artifact, telemetry route, dependency version, or deployment mechanism changed.

## Test-first evidence

### RED

Run/job `33753371567 / 100641870874` — **EXPECTED FAILURE** on the isolated feature branch.

Repository structure and master-plan validation passed, while the focused TSK-0380 contract failed exactly because the baseline lacked:

1. an exact `.nvmrc` Node pin;
2. a single deterministic `npm run validate` command;
3. documented exact clean-checkout Node/npm/setup/validation steps.

The RED result therefore measured the intended missing capability rather than a repository/planning failure.

### Focused GREEN

Run/job `33753560478 / 100642486359` — **SUCCESS**.

The focused contract passed after the smallest source/tooling change: exact Node/npm baseline metadata, one aggregate validation command, contract registration, and clean-checkout documentation.

### Full branch acceptance

Run/job `33753630320 / 100642709779` — **SUCCESS**.

Exact GitHub-hosted environment:

- Ubuntu 24.04 runner;
- Node `22.23.2`;
- npm `10.9.8`;
- unchanged dependency lock blob `14f9a62607489f965b96d98cdf0d825a363cd8bc`.

Verified on a clean runner:

- canonical WBS hash unchanged;
- repository structure verifier PASS;
- modular master-plan validator PASS;
- `npm ci --no-fund --no-audit` PASS;
- `npm run validate` PASS;
- contract suite `97/97` PASS;
- ESLint PASS with zero errors (one pre-existing unused-variable warning in `core-state-machine.ts`, not introduced by TSK-0380);
- TypeScript typecheck PASS;
- production build PASS;
- `npm audit --audit-level=high` found zero vulnerabilities;
- `npm audit --omit=dev --audit-level=high` found zero vulnerabilities;
- Git diff/worktree remained clean.

Negative/rollback proof deliberately created invalid TypeScript source, required `npm run validate` to return nonzero, removed the probe, reran lint, and verified a clean worktree. This proves failure propagation and rollback without touching any live system.

### Final PR-head regression

Final PR head: `2db511a3230ee22dff7753b348b3508e6de6d1e7`.

Focused TSK-0380 run/job `33753875540 / 100643504418` — **SUCCESS**.

All 10 inherited workflows triggered on that exact PR head completed successfully, including TSK-0359 browser/localization, TSK-0243 browser/orchestration, TSK-0629 browser/accessibility, TSK-0375 intake routing, TSK-0376 accountless state machine, TSK-0360 profile-delivery source, TSK-0369 support capture, TSK-0374 versioned-content source, and TSK-0499 regression checks. These are regression results only and do not promote any fenced partial task to PASS.

### Canonical clean-main acceptance

Canonical merge commit: `1ee48aeb28d2fb01411bd971e83a305287baa2fd`.
Canonical TSK-0380 clean-main run/job `33754242557 / 100644681805` — **SUCCESS**.

All 10 workflows triggered by that exact canonical commit reached terminal clean state with no failure. The slow inherited TSK-0359 real-browser acceptance also completed successfully (`33754242412 / 100644680775`).

## Acceptance assessment

`ACC-0380` is satisfied:

1. **Clean setup succeeds:** exact clean-runner `npm ci` plus validation completed successfully.
2. **Deterministic commands exist:** contract, lint, typecheck, and production build are exposed through one ordered `npm run validate` command.
3. **Failures propagate nonzero:** deliberate invalid TypeScript caused the aggregate command to fail as required.
4. **Versions are pinned/bounded:** `.nvmrc` pins Node `22.23.2`; `packageManager` pins npm `10.9.8`; application dependency lock remains exact and unchanged.
5. **No undocumented manual step:** canonical `/website/README.md` documents the complete clean-checkout sequence and exact supported toolchain baseline.
6. **Security/privacy:** no secret, account data, DNS/query history, participant data, telemetry activation, or live target was required; dependency audits were clean.
7. **Rollback:** the negative probe was removed and the exact worktree returned clean.

No acceptance criterion remains open for this bounded task. `TSK-0380` is therefore eligible for runtime `PASS` once this evidence artifact and the minimal `CURRENT_STATE.md` synchronization are canonically published and read back.

## Non-inference / preserved fences

- no deployment or production activation occurred;
- no live-device/profile/certificate action occurred;
- no service removal/revocation occurred or was invented;
- no participant processing occurred;
- no telemetry activation occurred;
- no market/launch action occurred;
- no `TSK-0374 PASS`, `TSK-0417 PASS`, or `TSK-0499 PASS` is created;
- PR `#86` remains a separate draft/unmerged TSK-0417 source checkpoint.
