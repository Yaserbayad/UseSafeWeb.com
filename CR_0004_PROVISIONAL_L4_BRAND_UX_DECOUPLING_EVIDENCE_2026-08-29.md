# CR-0004 — Provisional L4 Brand/UX/prototype dependency decoupling evidence

**Date:** 2026-08-29
**Owner authority:** explicit approval to decouple remaining provisional internal L4 Brand/UX/prototype design from deferred representative-parent behavioral validation while preserving TSK-0187/RSK-0002 and all legal, privacy, participant, build, publication, payment and launch fences.

## Impact-analysis outcome

- `TSK-0298 -> TSK-0187` was the inappropriate early behavioral coupling for provisional internal Brand work.
- It is replaced by `TSK-0298 -> TSK-0139`, the existing explicit provisional L4 owner-authorization bridge.
- `TSK-0309 -> TSK-0187` is intentionally unchanged because TSK-0309 requires real usability/comprehension evidence before implementation-ready experience freeze.
- `ACC-0298` and `ACC-0299` now state provisional design-conformance semantics and cannot be read as representative-parent validation or deferred legal completion.
- `TSK-0187` itself is unchanged and remains representative-parent behavioral validation.
- `RSK-0002` remains OPEN/critical and unchanged.
- `TSK-0301` remains A1/HUMAN_ONLY and still requires explicit owner approval of the identity system.
- LG-03/LG-04/LG-05/LG-06 and all L5/L6, participant, legal, publication, payment, market and launch fences remain unsatisfied/unmodified by CR-0004.
- No existing PASS is invalidated by this amendment; no prior acceptance proof is weakened or replaced.

## Structural verification

```text
VALIDATION PASS
assembly_modules=25
tasks=641
dependency_edges=849
relationship_entities=5178
relationship_targets=20463
broken_links=0
generated_missing_task_ids=0
```

## Post-change planning blob identities before commit

- `Plans/Master/WBS/master-wbs.csv` -> `6a25d63af125116a80f96ac0f1548b1ddb452a34`
- `Plans/Master/RELATIONSHIP_INDEX.yaml` -> `9ed219b4ccb6b05e68c6a264fc2b21b1008b02a4`
- `Plans/Master/Registers/VERIFICATION_EVIDENCE_ACCEPTANCE.md` -> `95729ca2530b28d75970e8637288fe5348b147b9`
- `Plans/Master/Registers/DECISIONS_TRIGGERS.md` -> `39d0fbc6e3b5ee5305f585d26bcea2f35c9a4918`
- `Plans/Master/Registers/EXCEPTIONS_CHANGE_CONTROLS.md` -> `be84f3028040563ef0e8fc7d0dcc27e49c4d3bab`
- `Plans/Master/Layers/LAYER_5_AI_EXECUTION_EVIDENCE_STATE_CONTROL.md` -> `565e34ff8a130894288609f6ba5fc10b3f872797`
- `Plans/Master/MANIFEST.yaml` -> `ac2cb58336d53293f2d808da401f85d0c3728f5a`
- `Plans/Master/Generated/MASTER_PLAN_FULL.md` -> `2a00f9d9f31e9202595fd5ee4de56c951e3ca2dd`
- `Plans/SHA256SUMS.txt` -> `19bcd590506c08a1e2159b2619ef25bc9ed9b3f2`

## Publication/read-back rule

Planning evidence is not adopted for execution until this mutation is committed to `main`, exact changed paths/blobs are fetched back, and `CURRENT_STATE.md` is reconciled in a separate confirmed mutation.
