# TSK-0320 — Protection state model verification evidence

**Task:** TSK-0320 — Freeze the protection-state model and copy rules  
**Acceptance:** ACC-0320  
**Verification:** VER-0320 independent guarded evidence/copy audit  
**Date:** 2026-08-28  
**Result:** PASS candidate pending authoritative runtime reconciliation/read-back

## Exact evidence index

- State/copy contract: `TSK_0320_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-08-28.md`
- Contract blob: `1146f7622f434590dde1253d11f14fb6a87e19de`
- Contract commit: `1629cd4a716a467091ceeb8ed7ee58e068959b93`
- TSK-0315 blueprint blob: `f428f346d6e994d093b651d7b934e8610498c350`
- TSK-0315 evidence blob: `72d375ed4b783b56572012a0e48716b1314c0be6`
- TSK-0229 accountless data contract blob: `3fa48b11b6c7704ecc3748bcd865f77aa54f5605`
- TSK-0408 DNS identity/evidence contract blob: `52860ce167fc8a31962cd412772e428d280c8184`
- WBS blob: `dce5b829c4d447eac180ae1e896e0019292cf971`
- Requirements register blob: `12c3bf6a227ad6ae61e167546a2b8a35d01321d1`
- Constraints register blob: `125c10fba67cf4448d9b14ef268327c298e568cb`
- Interfaces register blob: `b01b47e48fcd1bd5b9697e0ab35b496059e7eb6c`
- Current runtime pre-reconciliation: TSK-0315 PASS; TSK-0320 selected CRITICAL/A3/AUTO_ALLOWED.

## Authority and precondition audit

- TSK-0320 has sole hard dependency TSK-0315, now runtime PASS.
- WBS classifies TSK-0320 L4 / A3 / AUTO_ALLOWED / CRITICAL.
- ACC-0320 requires exact evidence and transition rules and does not require representative-parent/usability evidence; it is eligible under DEC-0050/CR-0003.
- The contract explicitly carries missing behavioral evidence and open `RSK-0002` and forbids claims that the wording is user-validated.
- No implementation, participant, legal, payment, release, launch or gate authority is inferred.

## ACC-0320 clause audit

ACC-0320 requires: `Protected/verified, configured/parent-confirmed, action-needed, not-covered, uncertain/error, and removed states have exact evidence and transition rules; no confirmation masquerades as verification.`

### Protected / verified — PASS

S1 has a strict evidence threshold: an approved verifier for the exact supported mechanism must currently succeed, with no known contradiction. Parent confirmation, profile/config presence, unknown-path DNS resolution or a prior session cannot produce S1. Current use is explicitly bounded to exact supported DNS combinations until another owning capability proves an equivalent verifier.

### Configured / parent-confirmed — PASS

S2 requires parent confirmation/completion without sufficient system verification and has explicit copy: `You confirmed this is set up` plus `UseSafeWeb has not independently verified this setting.` The contract explicitly prohibits `Verified`, `Protected` or equivalent system-evidence wording for S2.

### Action needed — PASS

S3 covers applicable but incomplete setup, skipped applicable action, deterministic failure with a known repair, and previously active configuration requiring reconfiguration/reverification. It carries no positive protection claim and requires an exact next action when known.

### Not covered — PASS

S4 is based on authoritative supported-scope exclusion, no approved relevant safeguard, or intentional product-scope exclusion. It cannot be used to cosmetically hide a failed supported setup, and it does not imply another layer compensates for the gap.

### Uncertain / error — PASS

S5 is mandatory for inconclusive/conflicting evidence, bypass possibility with insufficient detection, technical error, or materially changed context not reverified. Its default copy explicitly tells the parent not to rely on the layer until checked; stale S1/S2 cannot be preserved merely because setup previously succeeded.

### Removed — PASS

S6 requires approved removal/reset completion or parent-confirmed removal where system verification is unavailable and no contradiction exists. The protection claim is immediately withdrawn. Fresh accountless journeys are not forced to retain historical removal state.

### Transition rules — PASS

The contract defines generic and DNS-specific transitions, including not-started→action-needed, parent-confirmed→verified after successful verifier, positive→uncertain on conflicting evidence, any active state→removed after removal, removed→action-needed on reconfiguration, and correct handling of unsupported versus failed-supported branches.

### No confirmation masquerading as verification — PASS

This boundary is structural, copy-level and test-level: S1 has an independent system-evidence gate; S2 copy names the parent as evidence actor; profile/provider presence is insufficient; fourteen QA assertions include explicit tests that parent confirmation and profile presence never yield S1.

## Cross-contract consistency audit

### TSK-0315 blueprint

PASS. The six-state model preserves the blueprint's provisional evidence classes and does not expand the journey. It keeps Phone/Internet/Services independently truthful and allows journey completion with visible gaps rather than forcing all-green success.

### TSK-0408 DNS contract

PASS. Android hostname/provider entry and Apple profile presence remain configured/unverified until approved technical verification succeeds. VPN/browser/app/network conflict with insufficient detection is S5; unsupported combinations are S4; removal is S6; normal DNS recovery after removal does not restore UseSafeWeb protection.

### TSK-0229 accountless data contract

PASS. The model does not require persistent per-device protection history or identity. Verification is framed as current-session/current-check truth; no fabricated universal persistence TTL is added. DNS verification does not require browsing/query history or persistent device identity.

### Claims / trust boundary

PASS. The contract explicitly prohibits overall safety scores, `Fully protected`, `Your child is safe`, surveillance implications, and positive state retention under uncertainty/removal. Language/translation may not strengthen evidence.

## Adversarial findings and unresolved uncertainty

1. **Copy comprehension is not validated.** Exact labels are provisionally frozen for design coherence, but representative-parent comprehension remains unknown under `RSK-0002`. Reopen wording if later L3 evidence contradicts it.
2. **S1 availability is intentionally narrow.** Current system-verification authority is strongest for accepted DNS mechanisms; native/service layers remain S2 unless their owning task later proves a verifier.
3. **S4 versus S3 is a critical distinction.** Unsupported/out-of-scope is S4; a supported mechanism that failed with a known repair is S3. Implementations must not use S4 to hide product failures.
4. **S5 must dominate stale optimism.** If evidence becomes conflicting or context materially changes, the implementation must demote a prior positive state until reverified; no persistence convenience may preserve S1.
5. **No exact time validity is fabricated.** The contract correctly uses current-session/current-check semantics and event-based reverification triggers rather than inventing a universal “verified for N hours” rule.
6. **State labels do not finalize visual treatment.** Icons/colors/accessibility presentation remain later design-system work and must preserve evidence-strength distinctions.

No current authoritative evidence supports weakening the parent-confirmed/system-verified distinction, adding an overall safety score, or persisting a long-lived per-device protection history in the active accountless baseline.

## Stable verification decision

The durable contract directly satisfies all ACC-0320 clauses, is consistent with current accountless/DNS/service-blueprint authority, contains exact evidence/copy/transition rules, and preserves the mandatory CR-0003/`RSK-0002` limitation.

**Stable outcome: TSK-0320 = PASS candidate pending authoritative runtime reconciliation and post-write read-back.**

## Recompute requirement

After runtime reconciliation, recompute the eligible L4 queue. TSK-0319 becomes dependency-ready but remains HUMAN_ONLY; TSK-0316 and TSK-0409 remain HIGH/A3/AUTO_ALLOWED candidates. Select only after applying current priority, WBS order, acceptance and CR-0003.
