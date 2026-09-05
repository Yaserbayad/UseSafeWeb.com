# TSK-0010 Runtime Rebaseline Evidence

Date: 2026-09-05
Task: TSK-0010 — Update CURRENT_STATE to reference the frozen modular planning system and retain actual LG-03 / legacy G-02 execution state
Acceptance: ACC-0010
Verification: VER-0010
Evidence: EVD-0010
Verifier: ChatGPT Project Governor

## Source checkpoint

- Source checkpoint revision: `28`.
- Source checkpoint blob: `1b2c5e610371610899fd8bca97a5fd3f4332f62b`.
- Baseline version: `1`.
- Project status: `ACTIVE`.
- Governance mode: `SERIAL_LIGHT`.
- `TSK-0010`: `TODO` during verification.
- Dependency `TSK-0011`: `PASS`.

## Frozen planning authority

The live checkpoint and exact GitHub read-back establish the planning authority as:

- `Plans/Master/MASTER_PLAN.md@20e2763c0be2124378e3158ac559aed826bc6765`.
- `Plans/Master/MANIFEST.yaml@20e2763c0be2124378e3158ac559aed826bc6765`.
- Historical initial publication commit: `fce408f34470c0a0883ab978685b5265fdec4b97`.
- Current frozen authority commit: `20e2763c0be2124378e3158ac559aed826bc6765`.
- Frozen `Plans/` tree: `0ed412e5dd90f5a05238bb6542a061d7b0ce0ccf`.
- Manifest blob: `da35db0fe16009dfb5ce0e24caab05d6d02c84ed`.
- `Plans/SHA256SUMS.txt` blob: `8fbeb7337233adc289ea51e49a0722f33db08323`.

The completed `TSK-0011` read-back evidence confirms all 64 declared SHA-256 values and the complete `Plans/` file set match the frozen authority. Its structured checkpoint verification context explicitly records the checksum blob `8fbeb7337233adc289ea51e49a0722f33db08323`.

## Preserved actual runtime evidence and status

A serialization-preservation reconciliation was required because the migrated JSON checkpoint had lost later explicit legacy PASS state. The verified reconciliation restored exactly 32 historical current PASS records while leaving all current owner deferrals and explicit non-PASS boundaries unchanged.

- Reconciliation evidence: `TSK_0010_RUNTIME_PRESERVATION_RECONCILIATION_EVIDENCE_2026-09-05.md`.
- Evidence blob: `e87d1aaca75c155f88348f52adad2b6eb78e589a`.
- Evidence commit: `2d20e5ef4b1f64b5df9b94bc1e7f2054a438c562`.
- Exact failure-boundary trace supporting the reconciliation: run `33980615850`, job `101345052785`, artifact `9973633064`.
- Resulting checkpoint: revision `28`, blob `1b2c5e610371610899fd8bca97a5fd3f4332f62b`.

No product scope, frozen WBS semantics, lifecycle gate, baseline version, owner deferral, or material-action authority was changed by that repair.

## Accountless Version-1 decision

Current checkpoint policy `POL-012` preserves `DEC-0053 / CR-0006`:

- the core remains accountless;
- optional parent account/session, minimum ownership persistence, lightweight dashboard and device management are permitted within Version 1;
- mandatory login for core value, browsing/query/activity history, child accounts, and unrestricted customer DNS administration remain excluded.

This is the required current accountless decision for the rebaseline.

## Recovery/topology decision

Frozen decision `DEC-0043` records the current lean recovery/server topology:

- one AdGuard node initially;
- two separate fresh Ubuntu 24.04 LTS Azure VMs, one DNS/AdGuard and one web/app;
- no initial expensive HA;
- approximately 30-minute recovery target;
- direct-host Bash deployment/recovery under `/infrastructure/adguard-server`;
- Azure-native backup direction;
- restore/rebuild required.

The historical recovery acceptance task `TSK-0431 / ACC-0431` is preserved as `PASS` in revision 28.

## LG-03 / legacy G-02 mapping and current disposition

The frozen `Plans/Master/Governance/CURRENT_STATE_INTERFACE.md` explicitly states that TSK-0010 must retain the **actual LG-03 (legacy G-02) execution state**.

The same frozen interface records:

- current gate: `LG-03`;
- legacy gate: `G-02`;
- current disposition: `NOT_APPLICABLE TO ACTIVE PRE-PRODUCT PATH` under `DEC-0052 / CR-0005`.

This is a sequencing disposition, **not a gate PASS**. Applicable technical/privacy/security controls remain independently required, and first participant activation is after LG-09 in L8.

## Deterministic post-PASS selector evidence

After two verifier failures, a Convergence Guard assertion-by-assertion trace was run rather than making another equivalent retry.

- Trace workflow run: `33980986839`.
- Trace job: `101346042362`.
- Artifact: `9973737334`, `tsk0010-rebaseline-failure-trace`.
- Artifact digest: `sha256:76b50d5af80512474cb31f1c281447e36084616819826790a3db41827cc5b333`.
- Trace conclusion: `success`.
- All identity, schema, baseline, runtime-preservation, accountless, recovery, LG-03 mapping/disposition, and selector predicates passed except one verifier implementation check that searched only the `TSK-0011.reference` string for the checksum blob. The live structured `TSK-0011.verification_context` and exact Git tree both independently contain/confirm that checksum blob, so the failure was a verifier field-selection defect rather than missing evidence.

The trace computed the hypothetical state immediately after `TSK-0010 = PASS` without persisting any derived selector field:

- eligible `TODO` items with all hard dependencies PASS: `0`;
- satisfied non-deferred `WAITING`/`AUTO_ALLOWED` release candidates: `95`;
- deterministic first candidate by `(plan_priority, order, id)`: `TSK-0423`;
- candidate plan priority: `0`;
- candidate order: `423`;
- candidate title: `Implement automated regression that fails on query/file logging, identifiable statistics, missing anonymization, ECS, wrong upstream, public admin, or unapproved filters`;
- candidate action authority: `AUTO_ALLOWED`;
- candidate trigger: `Applicable lifecycle/gate and all hard dependencies satisfied.`;
- candidate preconditions: `Canonical state read; current gate/authority confirmed; required inputs/access available; no unresolved safety/privacy blocker.`

This selector result is **acceptance evidence only**. No mutable `next_work` field is added to `CURRENT_STATE.md`; after the PASS mutation, selection must be recomputed from the reread canonical checkpoint before any next transition.

## Acceptance result

ACC-0010 requires the canonical state to identify the frozen Master Plan/manifest plus publication commit/tree/checksum authority; preserve actual evidence/status; record current accountless/recovery decisions; map LG-03 to legacy G-02; and identify exact eligible readiness work.

All required elements are directly evidenced above under the current frozen semantics while preserving the SERIAL LIGHT rule that derived `next_work` state is not persisted.

- ACC-0010: **SATISFIED**.
- Baseline semantic change: none.
- Lifecycle gate PASS inferred: none.
- Material production action: none.
- Deviations: the verification implementation initially checked the checksum identity in the wrong structured field; the exact failure trace confirmed the underlying checksum evidence and every other acceptance predicate.
- Disposition: `TSK-0010` may transition from `TODO` to `PASS` through the normal checkpoint mutation/read-back protocol.
