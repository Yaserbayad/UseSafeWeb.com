# TSK-0313 — Protection Map requirements verification evidence

**Task:** TSK-0313 — Specify Protection Map state and evidence requirements  
**Acceptance:** ACC-0313  
**Verification:** VER-0313 independent guarded product/data/state audit  
**Date:** 2026-08-28  
**Result:** PASS candidate pending authoritative runtime reconciliation/read-back

## Exact evidence index

- Requirements contract: `TSK_0313_PROTECTION_MAP_STATE_EVIDENCE_REQUIREMENTS_2026-08-28.md`
- Contract blob: `521c9cc5073aa289281acade12a66a9e979e197d`
- Contract commit: `9383fe436921810a19144153f73f96576a58c868`
- TSK-0041 DNS activation contract blob: `95a5292223f1d2c3c8f79d4c889ad91e917478b2`
- TSK-0041 evidence blob: `66cdc50ae2fbb9ec4501b408837d01aafcba876d`
- TSK-0144 service-guidance contract blob: `f7821c8ef50aa517753c31477b383d660de11f40`
- TSK-0320 state/copy contract blob: `1146f7622f434590dde1253d11f14fb6a87e19de`
- TSK-0229 accountless data contract blob: `3fa48b11b6c7704ecc3748bcd865f77aa54f5605`
- TSK-0315 service blueprint blob: `f428f346d6e994d093b651d7b934e8610498c350`
- WBS blob: `dce5b829c4d447eac180ae1e896e0019292cf971`
- Direct predecessors: `TSK-0041 = PASS`, `TSK-0144 = PASS`, `TSK-0146 = PASS`.

## Authority and ownership audit

TSK-0313 is L4/A3/AUTO_ALLOWED/MEDIUM and its three direct hard predecessors now satisfy current evidence semantics. ACC-0313 does not require representative-parent behavior; it can be evaluated as an internal requirements contract under DEC-0050/CR-0003.

The artifact explicitly avoids a mutable-authority conflict:

- TSK-0320 remains exact owner of six-state semantics/copy/precedence/transitions.
- TSK-0229 remains owner of accountless J0/J1 fields, TTL, deletion and no-linkage rules.
- TSK-0313 owns how the Protection Map product must apply those authoritative contracts across Phone/Internet/Services and how QA can test them.

No second state vocabulary, data store, account model or competing persistence rule is created.

## ACC-0313 clause audit

ACC-0313 requires: `Every Protection Map state has entry/evidence rules, parent-facing copy, transition rules, unsupported behavior, persistence scope, device/journey-state boundary and testable examples; parent-confirmed and system-verified states are never conflated; no account ownership model is assumed in the active baseline.`

### Entry/evidence rules — PASS

All S1–S6 states have explicit entry evidence rules. S1 requires current approved system evidence with no contradiction; S2 requires parent confirmation without independent verification; S3 is applicable/repairable action-needed; S4 is authoritative unsupported/not-applicable scope; S5 is conflicting/inconclusive state; S6 is intentional removal/disablement. Configuration presence, prior session and journey completion cannot manufacture S1.

### Parent-facing copy — PASS

The requirements bind each state to the TSK-0320 exact copy semantics: S1 names system verification; S2 names the parent as evidence actor and explicitly lacks independent verification; S3 gives the required next action; S4 states lack of coverage/applicability; S5 tells the parent the state cannot currently be verified; S6 states the safeguard is no longer active. Complete-safety/surveillance/all-green overclaiming is prohibited.

### Transition rules — PASS

The contract defines not-started→S3, S3→S2/S1, S2→S1 only after a valid verifier, positive→S5 on conflicting evidence, S5 recovery transitions, active→S6 removal and S6→S3 reconfiguration. Journey completion cannot force positive state.

### Unsupported behavior — PASS

Mixed maps are first-class. Unsupported is not a user failure, an unsupported layer does not invalidate separately verified layers, one layer cannot upgrade another, and no filler service/setup path is invented merely to make the map complete.

### Persistence scope — PASS

J0 session state is the default and cannot later serve as durable device evidence. J1 is optional only under the TSK-0229 necessity rule, hard expires ≤24h non-sliding, deletes promptly on completion/reset/exit, contains no history/identity/linkage, and cannot silently become a dashboard/profile.

### Device/journey-state boundary — PASS

A displayed state is explicitly evidence for the current journey/check, not durable device truth. Fresh accountless journeys cannot restore expired historical S1/S2 as current truth; no stable device/customer ID, account ownership map or per-device AdGuard identity is required.

### Testable examples — PASS

The contract provides concrete mixed-state, VPN-conflict, repairable failure, unsupported, removal and stale-guidance examples plus twenty implementation/QA assertions.

### Parent-confirmed versus verified — PASS

The distinction is structural across all three layers. Native/service positive state is currently S2; DNS can become S1 only after exact current verification. DNS success cannot verify native/service controls and profile/menu/account presence cannot become S1.

### No account ownership model — PASS

The Map works without login, parent/customer account, child profile, persistent device registry, account-to-device ownership, persistent per-device AdGuard client identity or browsing/query history. It consumes only current transient state allowed by TSK-0229.

## Cross-contract consistency audit

### TSK-0320 — PASS

TSK-0313 does not redefine labels/precedence or weaken evidence thresholds; it explicitly defers semantic conflicts to TSK-0320.

### TSK-0229 — PASS

Map state fields and persistence stay inside the existing accountless schema/expiry/deletion/no-linkage rules; no new data category is implicitly authorized.

### TSK-0041 — PASS

Internet-layer S1/S3/S4/S5/S6 behavior matches the accepted DNS activation requirements, including Private Relay/VPN/browser/network uncertainty and removal.

### TSK-0144 — PASS

Services layer preserves zero-or-one service, parent-confirmed S2, unsupported/not-applicable S4, uncertainty S5 and no system verifier/credential collection.

### TSK-0315 — PASS

The Map fits the accountless service blueprint and allows truthful completion with mixed states and gaps rather than all-green completion.

## Adversarial findings and unresolved uncertainty

1. **Requirements overlap was a duplication risk.** TSK-0320 already owns exact state/copy semantics. The TSK-0313 artifact avoids a second mutable definition by treating TSK-0320 as semantic authority and owning only application/product/test requirements.
2. **S4 not-applicable versus unsupported requires careful copy.** Both use Not-covered semantics, but reason-specific supporting copy must explain whether the branch does not apply or is unsupported without creating a new seventh evidence state.
3. **Current journey state is intentionally ephemeral.** Lack of a persistent history/dashboard is a product/privacy property, not missing functionality under the active accountless baseline.
4. **Visual design is not frozen here.** The requirement that evidence strength remain distinguishable without color is frozen; icons/colors/components remain later design-system authority.
5. **No real-parent comprehension evidence exists.** `RSK-0002` remains OPEN; the exact labels/examples must be reopened if later L3 evidence contradicts comprehension/usability assumptions.

## Stable verification decision

The durable requirements contract directly satisfies every ACC-0313 clause, respects single-authority ownership of state and data semantics, and introduces no account/persistence/surveillance scope expansion.

**Stable outcome: TSK-0313 = PASS candidate pending authoritative runtime reconciliation and post-write read-back.**

## Recompute requirement

After runtime reconciliation, recompute the provisional-L4 queue from current WBS plus accepted runtime evidence. Do not assume a downstream task is executable merely because this Protection Map requirement is complete; continue to fence human-only, owner-review and representative-parent tasks.
