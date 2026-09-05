# TSK-0011 Published Plan Read-back Evidence

Date: 2026-09-05
Task: TSK-0011 — Fetch the published modular planning tree from GitHub main and verify exact files, checksums, commit, and authority root
Acceptance: ACC-0011
Verification: VER-0011
Evidence: EVD-0011
Verifier: ChatGPT Project Governor

## Authoritative task and checkpoint source

- Frozen WBS authority: `Plans/Master/WBS/master-wbs.csv` at commit `20e2763c0be2124378e3158ac559aed826bc6765`, WBS blob `357c5e1be3b455e7efddd329d6a2468e3125b502`, row `TSK-0011`.
- Source checkpoint: revision `25`, blob `21a13045d2ad5c6408ca4ec86da76df2ea370755`, baseline version `1`, project status `ACTIVE`.
- Dependency `TSK-0009` was `PASS`; `TSK-0011` was `TODO` during verification.
- Frozen task authority is `AUTO_ALLOWED` and capability A3.

## Approved frozen planning authority

The current owner-frozen planning package is pinned to:

- Frozen authority commit: `20e2763c0be2124378e3158ac559aed826bc6765`.
- Frozen `Plans/` tree: `0ed412e5dd90f5a05238bb6542a061d7b0ce0ccf`.
- `Plans/Master/MANIFEST.yaml` blob: `da35db0fe16009dfb5ce0e24caab05d6d02c84ed`.
- `Plans/SHA256SUMS.txt` blob: `8fbeb7337233adc289ea51e49a0722f33db08323`.
- Historical initial publication commit: `fce408f34470c0a0883ab978685b5265fdec4b97`.

The manifest declares `Plans/Master` as the canonical root, `MASTER_PLAN.md` as the root planning document, `MANIFEST.yaml` as the machine-readable authority map, `CURRENT_STATE` as separate runtime authority, and generated modules as non-authoritative.

## Exact GitHub main read-back

The verification workflow checked out GitHub `main` with full history and compared the complete current `Plans/` tree byte-for-byte with the frozen authority commit.

Read-back identity at verification:

- Branch: `main`.
- Read-back commit: `f25f32aa65ed5a5a75e45fad32698fc26a81c571`.
- Read-back repository tree: `7cfcfc87dc82376a23b0af25d5ca810dfdbe0da8`.
- Read-back `Plans/` tree: `0ed412e5dd90f5a05238bb6542a061d7b0ce0ccf`.
- Read-back manifest blob: `da35db0fe16009dfb5ce0e24caab05d6d02c84ed`.
- Read-back SHA256SUMS blob: `8fbeb7337233adc289ea51e49a0722f33db08323`.

The read-back `Plans/` tree, manifest blob, and checksum blob therefore exactly match the current frozen authority identities.

## File-set and checksum verification

- Entries declared by `Plans/SHA256SUMS.txt`: `64`.
- Files in the frozen `Plans/` Git tree excluding `Plans/SHA256SUMS.txt`: `64`.
- File-set comparison: exact.
- Complete directory comparison between frozen `Plans/` and GitHub-main read-back `Plans/`: exact; no byte differences.
- `sha256sum -c Plans/SHA256SUMS.txt` against frozen authority bytes: PASS for every declared file.
- `sha256sum -c Plans/SHA256SUMS.txt` against current GitHub-main read-back bytes: PASS for every declared file.
- Per-file comparison: every one of the 64 expected SHA-256 values equals both the frozen-file SHA-256 and the GitHub-main read-back SHA-256.
- `MASTER_PLAN.md`: present.
- `MANIFEST.yaml`: present.
- `SHA256SUMS.txt`: present.

The complete durable expected per-file checksum list is the immutable checksum blob `8fbeb7337233adc289ea51e49a0722f33db08323`; the workflow artifact below contains the explicit 64-row expected/frozen/main comparison and is independently reconstructable from the cited immutable commit and blobs.

## Authority-root verification

The read-back manifest was checked for the current authority contract:

- `canonical_root: Plans/Master` — PASS.
- `MASTER_PLAN.md` is the root planning document — PASS.
- `MANIFEST.yaml` is the machine-readable authority map — PASS.
- Runtime state remains separate in `CURRENT_STATE` — PASS.
- `Generated/MASTER_PLAN_FULL.md` remains `derived_non_authoritative` — PASS.

No derived file was promoted to independent planning authority.

## Deterministic validator

The validator shipped in the exact read-back planning package produced:

- `VALIDATION PASS`
- `assembly_modules=25`
- `tasks=641`
- `dependency_edges=858`
- `recurring_hard_predecessors=0`
- `cr0011_invariants=PASS`
- `relationship_entities=4587`
- `relationship_targets=18152`
- `broken_links=0`
- `generated_missing_task_ids=0`

## GitHub Actions evidence

- Verification workflow staging commit: `f25f32aa65ed5a5a75e45fad32698fc26a81c571`.
- Actions run: `33979759038`.
- Job: `101342759961`.
- Job conclusion: `success`.
- Artifact: `9973390487`, name `tsk0011-readback-verification`.
- Artifact digest: `sha256:50cb6f81a34e2a708e2eae8b94a17884dc85ba5c8ce188446bbdfaf808291452`.
- Artifact result: `PASS` for `ACC-0011` and includes the explicit per-file checksum comparison.
- The one-off verification workflow self-deleted successfully after verification.
- After cleanup, `CURRENT_STATE.md` remained unchanged at blob `21a13045d2ad5c6408ca4ec86da76df2ea370755` / revision `25`.

## Acceptance result

ACC-0011 requires the complete approved `Plans/` package to be fetched/read back from GitHub `main`, every declared file/checksum to match the approved bytes, the branch/commit/tree/file identities and authority root to be recorded, and any mismatch to stop ordinary governed execution.

All required parts passed without mismatch.

- ACC-0011: **SATISFIED**.
- Deviations: none observed.
- Disposition: `TSK-0011` may transition from `TODO` to `PASS` through the normal checkpoint mutation and read-back protocol.
