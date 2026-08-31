# TSK-0315 — Dual-Mode Service Blueprint Acceptance Evidence

**Task:** TSK-0315 — Create the dual-mode end-to-end service blueprint for accountless core and optional parent-account lifecycle  
**Acceptance:** ACC-0315  
**Verification:** VER-0315  
**Evidence:** EVD-0315  
**Date:** 2026-08-31  
**Verifier:** Governed post-publication analytical verification, separate from artifact authoring  
**Result:** PASS CANDIDATE PENDING DETERMINISTIC VERIFICATION AND RUNTIME RECONCILIATION

## 1. Exact artifact under review

- Path: `TSK_0315_POST_CR0007_DUAL_MODE_END_TO_END_SERVICE_BLUEPRINT_2026-08-31.md`
- Version: `2.0.0-post-cr0007`
- Blob read back from `main`: `97cf09f294c757f80ad5c0fbe6110ed8d471159c`
- Publication commit: `90bd9e6a4e4891d67e350db6a4001848e7610703`

## 2. Current eligibility

Current WBS `f3c29b5db8b835ef2c896f61335656ea51d8ba1c` defines TSK-0315 as L4, HIGH, A3 / `AUTO_ALLOWED`, with hard dependencies `TSK-0149; TSK-0229; TSK-0142` and ACC-0315 / VER-0315 / EVD-0315.

All three dependencies are current durable PASS:

- TSK-0149 current post-CR-0007 public-vs-product outcome split;
- TSK-0229 current post-CR-0006 accountless/persistent-domain separation;
- TSK-0142 current dashboard/device-management requirements.

The pre-CR-0006 TSK-0315 artifact is accountless-only and is therefore superseded for current acceptance. Its still-valid accountless technical/recovery principles may be reused, but its prohibition on current account/dashboard persistence is not current authority.

**Eligibility result:** PASS.

## 3. Exact ACC-0315 coverage

| Required dimension | Persisted blueprint evidence | Result |
| --- | --- | --- |
| discover/start | Stages 0–1 map public discovery/trust and login-free Start transition. | PASS |
| accountless setup | Stages 1–8 and §5.1 cover route, native safeguard, DNS, service, Protection Map and finish without login. | PASS |
| optional account entry | Stage 9 maps optional Google account entry and cancellation/provider failure. | PASS |
| first-session account creation | Stage 10 maps successful provider sign-in, one account/session and duplicate/partial failure handling. | PASS |
| signed-in return/session | Stage 11 maps valid return, expiry/revocation/invalid session and re-auth/accountless continuation. | PASS |
| lightweight dashboard/device management | Stages 12–17 map empty/list, add/manage, reverify/reinstall, replace, revoke/unlink and record deletion. | PASS |
| native safeguard routing | Stage 3 preserves parent-confirmed versus system-verified truth and unsupported/uncertain handling. | PASS |
| DNS activation/verification | Stages 4–5 preserve platform-specific setup and current technical verification requirements. | PASS |
| relevant service guidance | Stage 6 preserves zero/one relevant service and parent-confirmed/Not covered outcomes. | PASS |
| Protection Map | Stage 7 preserves independent S1–S6 Phone/Internet/Services evidence. | PASS |
| false-positive/support | Stage 20 maps privacy-minimal self-service and narrow correction/reverification. | PASS |
| account/device deletion | Stages 17 and 19 map record deletion and account deletion separately. | PASS |
| revoke | Stage 16 maps revoke/unlink management without claiming DNS removal. | PASS |
| reinstall | Stage 14 maps reinstall/reconfigure and stale-status invalidation. | PASS |
| replacement | Stage 15 prevents inherited S1/S2/history. | PASS |
| recovery/removal | Stages 21–22 and §5.5 map physical DNS removal and post-removal recovery. | PASS |
| provider outage | Stage 23 maps account-only failure containment and continued accountless routes. | PASS |
| exit/reset/lost state | Stage 24 maps exit/reset/transient-state loss separately from physical DNS configuration. | PASS |
| frontstage | Every row in §4 has a frontstage parent experience. | PASS |
| backstage | Every row in §4 has a backstage service/system behavior. | PASS |
| data | Every row has an explicit data boundary; §3 defines domain-level allowlists/exclusions. | PASS |
| owner | Every row assigns a responsible owner class; §6 defines ownership boundaries. | PASS |
| failure | Every row maps failure/uncertainty. | PASS |
| recovery | Every row maps a next safe recovery/action. | PASS |
| no browsing/activity history | Invariants, data domains, stages and prohibited behavior explicitly exclude browsing/query/activity history. | PASS |
| no mandatory login | Invariants, normal path and prohibited behavior explicitly keep the full core login-free. | PASS |

## 4. CR-0006 / CR-0007 reconciliation

The blueprint correctly replaces the old “accountless-only forever” assumption with the current dual-mode V1 scope. Optional account continuity is present, but it does not gate core value and provider failure cannot invalidate configured DNS/accountless functionality.

No owner-controlled material scope expansion is introduced.

## 5. TSK-0229 no-linkage reconciliation

The blueprint explicitly preserves separate J0/J1 and persistent account/device domains:

- no automatic join/copy/promotion;
- account activity cannot extend J1 expiry;
- any explicit save/transfer requires a separately approved downstream field-level data-flow contract;
- no browsing/query/activity history crosses domains;
- account/device ownership never becomes technical verification.

**No-linkage compatibility: PASS.**

## 6. TSK-0142 / TSK-0312 lifecycle reconciliation

The service stages preserve current account/dashboard requirements:

- optional Google sign-in, no password/SMS expansion;
- account/session expiry/revocation/logout/deletion behavior;
- minimum device list/ownership/nickname continuity;
- add/setup/verify/reinstall/replace/revoke/remove lifecycle;
- account/device deletion and physical DNS removal remain distinct;
- account-only authorization failures fail closed without breaking accountless core access.

## 7. Technical truth reconciliation

The blueprint retains current DNS/Protection Map semantics rather than redefining them:

- platform-specific Android/Apple setup remains externally owned;
- configuration presence is not verification;
- DNS S1 requires qualifying current system evidence;
- parent confirmation remains distinct from system verification;
- unsupported/uncertain/action-needed/removed are valid outcomes;
- removal withdraws the current UseSafeWeb DNS protection claim.

## 8. Data minimization / surveillance review

No stage requires browsing history, DNS-query history, top domains, app/activity history, child accounts, location/messages/contacts/photos/social content or raw AdGuard administration. Persistent device continuity is limited to approved account/device ownership/settings/lifecycle/evidence metadata; exact schema/retention/storage remains downstream.

## 9. Deterministic testability

Section 9 supplies 24 objective assertions spanning the entire ACC, including one assertion that every mapped stage has frontstage/backstage/data/owner/failure/recovery. These are synthetic/design-contract checks; no pre-L8 human evidence is inferred.

## 10. Contrary-evidence review

No current authority inspected contradicts the blueprint. The only direct conflict was with the historical accountless-only TSK-0315 artifact, which is explicitly superseded by current CR-0006/0007 scope and current WBS ACC-0315.

## 11. Analytical disposition

Every current ACC-0315 clause is represented in the exact persisted blueprint; all three hard dependencies are current PASS; privacy/evidence/state boundaries are retained; and no downstream implementation/provider/legal/privacy/LG-06 PASS is inferred.

**Analytical result: ACC-0315 PASS candidate.**

TSK-0315 remains non-PASS until a separate deterministic verifier succeeds on the exact persisted artifact/current authority and that proof is durably recorded/read back before runtime reconciliation.
