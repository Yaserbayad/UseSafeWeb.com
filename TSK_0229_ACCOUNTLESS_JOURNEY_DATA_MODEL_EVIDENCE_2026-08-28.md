# TSK-0229 — Accountless journey data contract verification evidence

**Task:** TSK-0229 — Define and approve the accountless journey data model, expiry, deletion, and no-linkage rules  
**Acceptance:** ACC-0229  
**Verification:** VER-0229 independent guarded repository audit  
**Date:** 2026-08-28  
**Result:** PASS candidate pending runtime reconciliation/read-back  

## Exact evidence index

- Contract artifact: `TSK_0229_ACCOUNTLESS_JOURNEY_DATA_MODEL_EXPIRY_DELETION_NO_LINKAGE_2026-08-28.md`
- Contract artifact blob after correction: `3fa48b11b6c7704ecc3748bcd865f77aa54f5605`
- Contract correction commit: `465552b56f8ebeb6a24fb2edbb97df38440f26f0`
- WBS blob: `dce5b829c4d447eac180ae1e896e0019292cf971`
- Runtime blob before PASS reconciliation: `8eea72ba49a689138060d6823db6ed802f35faed`
- Requirements register blob: `12c3bf6a227ad6ae61e167546a2b8a35d01321d1`
- Risk register blob: `d15165b0e06f559fc7281fab12873d0cb32144d9`
- Decision/trigger register blob: `577732f6fc5168b392224063a312c28f5495a3bd`
- Layer-5 execution/evidence rules blob: `a3586d011b6bb48d7f6119f58429cfdde99e34c2`
- Current hard dependency from runtime: `TSK-0146 = PASS`.

## Authority and boundary audit

- DEC-0042 requires the active product baseline to remain accountless-first; optional persistence/account capability remains separately triggered and approved.
- DEC-0050/CR-0003 permits bounded internal L4 definition/design while real-participant L3 is deferred through 2027-08-27; it requires missing behavioral evidence and `RSK-0002` to remain explicit and forbids downstream claims that behavioral validation occurred.
- `RSK-0002` is OPEN and critical: provisional L4 assumptions may be wrong about completion, incremental value, comprehension, support burden, persistence, or parent-perceived duplication.
- The task is A3 / AUTO_ALLOWED and its hard dependency `TSK-0146` is recorded PASS in current runtime.
- This audit does not authorize implementation/build, real-participant processing, legal completion, payment activation, public release, launch, LG-05 PASS or LG-06 PASS.

## ACC-0229 audit

ACC-0229 requires: only fields necessary for the active journey; no browsing history or persistent child profile; expiry/deletion and diagnostic boundaries testable.

### Necessary/minimised state

PASS. The contract prefers J0 browser/session-only state and permits J1 only if later architecture demonstrates server-side necessity for safe completion, verification, a setup artifact, or an explicitly supported short resume path. J1 is allowlisted and rejects silent field expansion. No mandatory account, contact field, stable customer/device identifier or persistent identity is introduced.

The J1 allowlist is conservative: routing/status fields are either required for an active transient record or conditional/optional. The contract remains an upper-bound schema, not authority to persist every optional field; later implementation must still demonstrate necessity.

### Prohibited history/profile/linkage

PASS. The contract explicitly excludes parent/child identity, exact child age/DOB, addresses/school, account/service identifiers, persistent device identifiers, stored IP product-state, browsing/URL/DNS/domain/activity history, messages/contacts/photos/social content, raw diagnostics, payment data, marketing attribution, unrestricted free text, participant identity, cross-session stitching and household-profile inference.

### Expiry and deletion

PASS. J0 is session-only. Any J1 record has a fixed non-sliding hard expiry no later than 24 hours after creation, with defined early-deletion triggers, preferred synchronous deletion, an asynchronous cleanup upper bound of 15 minutes, independent TTL cleanup, token non-reuse, deletion read-back and restart-safety invariants. These values are explicitly provisional minimisation defaults rather than behavioral findings; shortening is allowed, while lengthening requires current evidence/review/authority.

### Diagnostic/logging/backup separation

PASS. Raw request/DNS diagnostics are outside J1 and require a separately governed exceptional-diagnostic process. Full live tokens, form payloads, IP-token linkage, per-user clickstream/session replay, persistent journey profiles and raw DNS/domain history are prohibited telemetry. J1 is excluded from durable backups by default; any future inability to exclude it requires separate necessity, privacy and restore/deletion evidence.

### Testability

PASS. Fourteen explicit implementation invariants cover schema allowlisting, no identity/history, opaque token behavior, fixed TTL, early deletion, no sliding expiry, no linkage, no token logging, diagnostic separation, backup exclusion, deletion read-back, restart safety and accountless completion.

## Contrary evidence and unresolved uncertainty

No current real-participant behavioral evidence proves that the chosen transient-state model, 24-hour maximum TTL, 15-minute cleanup bound, routing fields or lack of persistence are optimal for parents. That is not a failure of ACC-0229 because the current acceptance is an internal data-contract/minimisation criterion, but it is a material limitation under DEC-0050/CR-0003. The corrected contract now states this explicitly and preserves `RSK-0002`.

No evidence was found that requires a persistent parent identity, child profile, browsing/query history or cross-session behavioral profile for the active provisional journey. Future architecture or real-user evidence may justify a narrower/shorter contract; any broader persistent identity, linkage, analytics, backup retention or longer TTL is a material change requiring re-evaluation.

## Stable verification decision

All current ACC-0229 clauses are directly supported by the corrected durable artifact and consistent with the current accountless/privacy authority. The initial artifact omitted the mandatory CR-0003/RSK-0002 limitation; that defect was corrected and read back before this decision.

**Stable outcome: TSK-0229 = PASS candidate pending authoritative runtime reconciliation and post-write read-back.**

## Work unlocked for recomputation

Do not assume a successor solely from memory. After runtime reconciliation, recompute the eligible L4 queue from current WBS/dependencies/authority. The pre-reconciliation runtime identifies `TSK-0408` as the next HIGH technical candidate after TSK-0229, subject to a fresh eligibility check.
