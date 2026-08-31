# TSK-0325 — Post-CR-0007 Parent Journey / Service Blueprint Acceptance Evidence

**Task:** TSK-0325 — Create end-to-end parent journey and service blueprint  
**Acceptance:** ACC-0325  
**Verification:** VER-0325  
**Evidence:** EVD-0325 current post-CR-0007 acceptance review  
**Date:** 2026-08-31  
**Verifier:** governed post-publication analytical verification, separate from artifact authoring  
**Result:** PASS CANDIDATE PENDING DETERMINISTIC VERIFICATION AND RUNTIME RECONCILIATION

## 1. Exact current artifacts

- Normative parent-journey blueprint: `prototype/TSK-0325/SERVICE_BLUEPRINT.md`
- Version: `2.0.0-post-cr0007`
- Current blob read back from `main`: `7763a6d16760d85df3ad23789f764d3e431849ef`
- Current publication commit: `5fb1819992282d01f377544b5ec9c7e9ce6d9a7b`
- Non-authoritative acceptance projection: `prototype/TSK-0325/ACCEPTANCE_MATRIX.json`
- Projection blob: `9826c7ab39e087002c6e0a51d7353e52ca6cc34b`
- Projection publication commit: `3b383eff9c8045b56ae5a37e72e2da265ba7c7e2`

## 2. Why revalidation was required

Historical TSK-0325 v1.0.0 was accepted on 2026-08-29 under DEC-0052/CR-0005. Its eight ACC path classes were valid, but the artifact assumed no current persistent parent/device continuity and therefore did not represent the optional account/session/dashboard scope activated by DEC-0053/CR-0006.

Current WBS still defines ACC-0325 as the eight-path/touchpoint-trace contract and references current `CON-0010`, which now requires optional parent account/minimum persistence/lightweight dashboard while preserving the login-free core. Therefore the historical PASS could not be reused without impact reconciliation.

The v2 artifact preserves the accepted eight-path spine and adds only the currently required parent-account/device touchpoints. It consumes the current TSK-0315 full dual-mode service blueprint rather than duplicating its 25-stage service matrix.

## 3. Eligibility and dependency

Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c` defines TSK-0325 as:

- L4 / priority MEDIUM;
- hard dependency `TSK-0326`;
- A3 / `AUTO_ALLOWED`;
- ACC-0325 / VER-0325 / EVD-0325;
- requirement references REQ-0028 / REQ-0029 / CON-0010 / CON-0017;
- interfaces INT-0009 / INT-0010.

`TSK-0326` remains `NOT_APPLICABLE + PASS` only as the verified CR-0005 exclusion of pre-product human validation. CR-0006/CR-0007 did not reactivate that human-testing task; no behavioral evidence is inferred from the exclusion.

Current supporting source TSK-0315 is now post-CR-0007 PASS and supplies the full dual-mode service-design baseline. Current TSK-0312 and TSK-0142 supply account/session and dashboard/device-management requirements.

**Eligibility result: PASS.**

## 4. ACC-0325 clause-by-clause review

| ACC requirement | v2 artifact evidence | Result |
| --- | --- | --- |
| Normal path | Path A maps the supported accountless core from discovery through Protection Map, explicitly allowing completion with no account. | PASS |
| Already-configured path | Path B skips duplicate native/DNS work without bypassing current verification or strengthening account/history evidence. | PASS |
| Unsupported path | Path C stops unsupported scope, exposes Not covered/uncertain truth and refuses fabricated fallback setup. | PASS |
| Failed-activation path | Path D distinguishes known repair from uncertainty/unsupported state and routes to reverify or removal/recovery. | PASS |
| False-positive path | Path E preserves DNS-path-vs-filter-correctness truth, uses narrow correction and prohibits broad dashboard bypass control/history collection. | PASS |
| Resume path | Path F covers legitimate accountless transient resume plus optional authenticated continuity while forbidding automatic J0/J1 promotion and stale verification reuse. | PASS |
| Removal path | Path G distinguishes physical DNS removal/recovery from dashboard record/account/J0-J1 lifecycle and requires new verification after reinstall. | PASS |
| Support path | Path H supplies state-neutral, source-current, privacy-minimal self-service across accountless and account/session/device paths. | PASS |
| Every touchpoint maps to requirements | Section 3 contains 17 touchpoints. Each maps REQ-0028 plus applicable REQ-0029 and current CON-0010/CON-0017/INT-0009/INT-0010; account/device touchpoints additionally bind TSK-0312/TSK-0142. | PASS |

## 5. Current optional-account reconciliation

The artifact correctly treats account continuity as an overlay rather than a ninth mandatory core path:

- TP-08 optional account entry;
- TP-09 sign-in/session;
- TP-10 dashboard/device list;
- TP-11 device management;
- TP-17 account/device lifecycle.

These touchpoints preserve current authority:

- Google social sign-in is planned; no local password/SMS expansion;
- account cancel/error/provider outage leaves accountless core usable;
- stored ownership/history does not create `Verified`;
- no automatic J0/J1 promotion/linkage;
- logout, revoke/unlink, device-record deletion, account deletion and physical DNS removal remain distinct operations.

No material product-scope expansion was introduced.

## 6. Requirement/interface review

### REQ-0028 — necessity

The v2 touchpoint catalogue gives each interaction a bounded purpose and trace. New account/device touchpoints exist only because current CR-0006 scope requires the corresponding continuity/lifecycle function. **PASS.**

### REQ-0029 — supported technical setup

Platform routing, DNS setup/verification, troubleshooting, removal/recovery and device reconfiguration remain tied to current source-backed supported methods; unsupported paths do not improvise. **PASS.**

### CON-0010 — optional account + login-free core

The full core remains usable without login. Optional account/session/dashboard functions are represented without becoming a gate. **PASS.**

### CON-0017 — localization boundary

English/Turkish/Arabic+RTL technical capability is inherited without implying non-UK market activation. **PASS.**

### INT-0009 / INT-0010

The artifact gives downstream IA/UX/engineering/QA a deterministic path taxonomy, touchpoint goals/traces, state invariants and exception/recovery outcomes. **PASS for TSK-0325 scope.**

## 7. Privacy/evidence truth review

The artifact explicitly prohibits browsing/query/activity history, child accounts/profiles and raw/unrestricted AdGuard administration. Parent confirmation and account/device persistence cannot become technical verification. Current contradictory evidence overrides historical optimistic status. **PASS.**

## 8. Behavioral-evidence boundary

No parent/user validation result is claimed. `TSK-0326 NOT_APPLICABLE+PASS` represents only the current exclusion of pre-L8 human testing, not behavioral evidence. RSK-0002 remains OPEN/non-blocking before L8.

## 9. Contrary-evidence review

No current canonical source inspected contradicts v2. The historical v1 accountless-only assumption is explicitly superseded only where CR-0006 activated optional account/device continuity; its still-valid path semantics are preserved.

The updated artifact does not infer current TSK-0328 IA PASS, TSK-0329 prototype PASS, implementation/build, provider/security architecture, legal/privacy compliance, LG-06 or any later gate PASS.

## 10. Analytical disposition

Every current ACC-0325 clause is present in the exact persisted v2 normative artifact; the 17-touchpoint trace reconciles current optional-account/device scope without weakening the login-free core, privacy or technical evidence rules.

**Analytical result: ACC-0325 PASS candidate.**

TSK-0325 remains non-PASS under current CR-0006/0007 semantics until a separate deterministic verifier proves the exact persisted artifact/projection/current authority and the result is durably recorded/read back before runtime reconciliation.
