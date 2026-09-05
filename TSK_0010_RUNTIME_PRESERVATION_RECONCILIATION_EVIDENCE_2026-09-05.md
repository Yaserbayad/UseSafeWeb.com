# TSK-0010 Runtime Preservation Reconciliation Evidence

Date: 2026-09-05
Purpose: preserve valid historical runtime PASS state while executing TSK-0010 without changing product scope or baseline semantics.
Verifier: ChatGPT Project Governor

## Authority and source boundary

- Current SERIAL LIGHT checkpoint before reconciliation: `CURRENT_STATE.md`, revision `27`, blob `c2175c5b5e3a5797f38638e36503f76d6cafbd60`, baseline version `1`, project status `ACTIVE`.
- Frozen planning authority: commit `20e2763c0be2124378e3158ac559aed826bc6765`.
- Frozen WBS: `Plans/Master/WBS/master-wbs.csv`, blob `357c5e1be3b455e7efddd329d6a2468e3125b502`.
- Immutable legacy checkpoint: `CURRENT_STATE.md@20e2763c0be2124378e3158ac559aed826bc6765`, blob `d45c7b1f98ceba6265944aabd970c250dc7be2d2`.
- Current checkpoint policy `POL-003` states that migrated WBS execution snapshots are superseded by later explicit current-runtime records in that immutable legacy checkpoint plus the current owner deferrals.

This reconciliation therefore repairs serialization loss only. It does not create new acceptance, rerun completed work, change scope, change the frozen WBS, advance a lifecycle gate, or alter baseline semantics.

## Why reconciliation is required

The current JSON checkpoint contains several `WAITING` records that the immutable legacy checkpoint explicitly recorded as current `PASS` with durable evidence. TSK-0010 requires preservation of actual evidence/status. Leaving those records `WAITING` would contradict both `POL-003` and the immutable legacy runtime record.

Two generic verification attempts initially failed before any checkpoint mutation. A Convergence Guard diagnostic isolated the failure to the proof parser, not to project state:

- First preservation verifier: run `33980412024`, job `101344520042` — failed before mutation.
- Diagnostic inventory: run `33980492151`, artifact `9973598156` — identified omitted accepted-stable tasks and parser misses.
- Second preservation verifier: run `33980571655`, job `101344936096` — failed before mutation.
- Exact failure trace: run `33980615850`, job `101345052785`, artifact `9973633064`, digest `sha256:8efc9659a7998a226e47230115ce8daedf440f851b8676c40fc4ae396ea59ca1` — succeeded and isolated exactly two failed predicates: `TSK-0437 proof_ok` and `TSK-0441 proof_ok`.

Every global predicate in the failure trace passed: checkpoint/blob identity, legacy checkpoint identity, WBS identity, schema, project identity, governance mode, revision, baseline version, ACTIVE state, restore/exclusion counts, disjointness, absence of owner-deferred restores, and completeness of accepted-stable classification. Every restore item also matched its current frozen ACC identity. The other 30 restore items passed the automated proof predicate.

The two parser misses were then verified directly from the immutable legacy checkpoint:

- `TSK-0437 / ACC-0437`: legacy PASS section records host-security baseline revalidation after TLS-proxy installation and Ubuntu patch repair; evidence `TSK_0437_POST_TLS_PATCH_REVALIDATION_EVIDENCE_2026-08-28.md`, blob `b23bb28960efe28526626b36dfa2d52339a521e8`; reconciliation run `33159129601`, job `98809042724`: PASS.
- `TSK-0441 / ACC-0441`: legacy PASS section records independent public-DNS verification from system, Cloudflare, Google and Quad9 resolvers with exact A `52.157.109.120` and no AAAA/CNAME; evidence `TSK_0441_PUBLIC_DNS_EVIDENCE_2026-08-28.md`, blob `91369bbe33eb608361e8b7b771ceca0a5cd42d50`; verification run `33156757093`, jobs `98801252982` and `98801253193`: PASS.

This confirms the repeated verifier failure class as a validation/proof-boundary implementation defect. No project-state contradiction was found.

## Exact historical PASS restore set

The following 32 runtime records are proven current historical PASS under the immutable legacy checkpoint and retain the same ACC identity in the current frozen WBS/checkpoint. All are currently serialized as `WAITING`; none is covered by a later owner deferral.

| Task | ACC | Immutable legacy proof location |
|---|---|---|
| TSK-0026 | ACC-0026 | legacy checkpoint line 307 direct current-PASS assertion |
| TSK-0027 | ACC-0027 | line 578 direct current-PASS assertion |
| TSK-0028 | ACC-0028 | lines 588-591 accepted-stable section / line 590 direct assertion |
| TSK-0139 | ACC-0139 | lines 604-609 accepted-stable section / line 181 direct assertion |
| TSK-0165 | ACC-0165 | lines 439-448 accepted-stable section |
| TSK-0166 | ACC-0166 | lines 367-378 accepted-stable section |
| TSK-0167 | ACC-0167 | lines 582-587 accepted-stable section / line 584 direct assertion |
| TSK-0168 | ACC-0168 | lines 379-388 accepted-stable section |
| TSK-0169 | ACC-0169 | lines 449-458 accepted-stable section |
| TSK-0202 | ACC-0202 | lines 329-336 accepted-stable section |
| TSK-0207 | ACC-0207 | lines 535-548 accepted-stable section / line 537 direct assertion |
| TSK-0214 | ACC-0214 | lines 389-400 accepted-stable section |
| TSK-0225 | ACC-0225 | lines 401-414 accepted-stable section |
| TSK-0227 | ACC-0227 | lines 415-426 accepted-stable section |
| TSK-0228 | ACC-0228 | lines 427-438 accepted-stable section |
| TSK-0298 | ACC-0298 | lines 871-878 accepted-stable section / line 873 direct assertion |
| TSK-0302 | ACC-0302 | lines 905-912 accepted-stable section / line 907 direct assertion |
| TSK-0374 | ACC-0374 | lines 3241-3252 accepted-stable section / line 3243 direct assertion |
| TSK-0428 | ACC-0428 | lines 549-558 accepted-stable section / line 551 direct assertion |
| TSK-0429 | ACC-0429 | lines 337-356 accepted-stable section; ACC-0429 explicitly fully satisfied |
| TSK-0430 | ACC-0430 | lines 357-366 accepted-stable section; ACC-0430 explicitly fully satisfied |
| TSK-0431 | ACC-0431 | line 305 direct recovery-acceptance PASS assertion |
| TSK-0437 | ACC-0437 | legacy PASS section plus evidence blob `b23bb28960efe28526626b36dfa2d52339a521e8`, run `33159129601` / job `98809042724` |
| TSK-0441 | ACC-0441 | legacy PASS section plus evidence blob `91369bbe33eb608361e8b7b771ceca0a5cd42d50`, run `33156757093`, jobs `98801252982` / `98801253193` |
| TSK-0442 | ACC-0442 | line 499 current PASS summary; TLS evidence blob `cb11394af1e80f15d85bda5d9b000bbf0efd6d20` |
| TSK-0443 | ACC-0443 | line 499 current PASS summary; renewal/monitoring acceptance remains PASS |
| TSK-0510 | ACC-0510 | line 306 direct current-PASS assertion; LG-03 remains non-PASS |
| TSK-0511 | ACC-0511 | lines 509-522 accepted-stable section / line 511 direct assertion |
| TSK-0512 | ACC-0512 | lines 523-534 accepted-stable section / line 525 direct assertion |
| TSK-0513 | ACC-0513 | line 594 direct current-PASS assertion |
| TSK-0514 | ACC-0514 | lines 497-508 accepted-stable section / line 499 direct assertion |
| TSK-0559 | ACC-0559 | lines 680-685 accepted-stable section / line 682 direct assertion |

Restore IDs, exactly:

`TSK-0026, TSK-0027, TSK-0028, TSK-0139, TSK-0165, TSK-0166, TSK-0167, TSK-0168, TSK-0169, TSK-0202, TSK-0207, TSK-0214, TSK-0225, TSK-0227, TSK-0228, TSK-0298, TSK-0302, TSK-0374, TSK-0428, TSK-0429, TSK-0430, TSK-0431, TSK-0437, TSK-0441, TSK-0442, TSK-0443, TSK-0510, TSK-0511, TSK-0512, TSK-0513, TSK-0514, TSK-0559`.

## Explicit non-PASS/exclusion set

These 8 records remain non-PASS and are not altered by this reconciliation:

- `TSK-0243` — current public DNS/TLS/proxy target proof still incomplete.
- `TSK-0360` — current target evidence required.
- `TSK-0369` — current target verification required.
- `TSK-0399` — remains dependency-blocked while its prerequisite is non-PASS.
- `TSK-0455` — later owner sequencing explicitly keeps it WAITING.
- `TSK-0483` — historical AdGuard-engine evidence does not prove the later public Nginx DoH/DoT ingress boundary.
- `TSK-0499` — later owner-deferred and target verification remains outstanding.
- `TSK-0630` — later owner-deferred/non-PASS.

Exclude IDs, exactly:

`TSK-0243, TSK-0360, TSK-0369, TSK-0399, TSK-0455, TSK-0483, TSK-0499, TSK-0630`.

## Current owner-override protection

No restore ID intersects the current owner-deferral set preserved by checkpoint policies POL-005 through POL-007:

`TSK-0455, TSK-0631, TSK-0633, TSK-0634, TSK-0635, TSK-0637, TSK-0640, TSK-0630, TSK-0421, TSK-0415, TSK-0416, TSK-0370, TSK-0499, TSK-0242`.

Those later owner instructions remain authoritative and unchanged.

## Lifecycle/gate preservation

The legacy G-02 gate maps to current LG-03, but the integrated-product-first sequencing decision retired the old pre-product LG-03 path from active progression. This reconciliation does **not** mark LG-03 PASS. The correct current disposition remains `NOT_APPLICABLE TO ACTIVE PRE-PRODUCT PATH` / non-PASS as recorded by the frozen current-state interface and legacy/current decisions.

Likewise, restoring `TSK-0026`, `TSK-0510`, or any other historical task PASS does not by itself satisfy, bypass, or advance a lifecycle gate.

## Reconciliation disposition

The minimum correct checkpoint repair is:

1. keep `checkpoint_revision=27`, baseline version `1`, and the ACTIVE project state as the source boundary;
2. for exactly the 32 restore IDs above, change the runtime state from `WAITING` to `PASS`, remove the obsolete `wait` object, and attach a structured acceptance reference to this evidence plus the immutable legacy checkpoint;
3. leave all other runtime items unchanged, including the 8 exclusions and all later owner deferrals;
4. increment checkpoint revision by exactly one;
5. preserve baseline version `1` because no product/governance semantics are changed;
6. reread and validate the resulting checkpoint before adoption.

Result: **RUNTIME PRESERVATION RECONCILIATION VERIFIED**. The restore set represents preserved historical truth, not newly claimed completion.
