# TSK-0329 — Authentication / Account Interaction Acceptance Evidence

**Task:** TSK-0329 — Design and prototype Google sign-in, first-session account creation, and signed-in return interactions  
**Acceptance:** ACC-0329  
**Verification:** VER-0329  
**Evidence:** EVD-0329 analytical review  
**Date:** 2026-08-31  
**Result:** PASS CANDIDATE PENDING DETERMINISTIC VERIFICATION AND RUNTIME RECONCILIATION

## 1. Exact persisted candidate

- Normative prototype: `prototype/TSK-0329/AUTH_ACCOUNT_INTERACTION_PROTOTYPE.md`
- Version: `1.0.0-post-cr0007`
- Prototype blob: `bc9ff6c3240c06e12af977097ccbc05fca9ad8ef`
- Prototype publication commit: `5f31f1fbda52ea538506cabf15d41b0da978449d`
- Structured interaction state model: `prototype/TSK-0329/INTERACTION_STATE_MODEL.json`
- State-model blob: `c4ffbe4c5795b57dc074f41e1480fe610784679d`
- State-model publication commit: `a8d714afc4b83dfa4a9cbf8c3dc9503b7fe6dcea`
- Current pre-acceptance runtime blob: `c080a364ef2eb5d0f3b168928b381a5328b3e751`

## 2. Eligibility / authority

Bounded current inspection run/job `33408418927 / 99541674501` completed SUCCESS and proved the current WBS/graph contract:

- L4 / MEDIUM;
- hard dependencies `TSK-0328; TSK-0312`;
- `ACC-0329 / VER-0329 / EVD-0329`;
- A4 / `AUTO_ALLOWED`;
- `REQ-0028; REQ-0029; CON-0010; CON-0017`;
- `INT-0009; INT-0010`;
- `RSK-0002` remains the linked non-blocking pre-L8 risk.

Both hard dependencies are current durable PASS. The repository contained no pre-existing TSK-0329 product/prototype artifact; this is a fresh current-scope prototype, not a reused historical PASS.

**Eligibility result: PASS.**

## 3. ACC-0329 clause review

| ACC clause | Persisted prototype evidence | Result |
| --- | --- | --- |
| Google sign-in | `AUTH-ENTRY`, provider-pending and callback-resolving states use the planned Google route and explicitly exclude password/SMS/child login. | PASS |
| First-session account creation | `AUTH-FIRST-SESSION` + `AUTH-CREATE-PENDING` explain minimum account purpose/data, require an explicit Create my account action and handle success/failure/unknown outcomes idempotently. | PASS |
| Signed-in return | `AUTH-RETURN` routes authorized existing parents to Dashboard while explicitly refusing to treat record/session presence as technical verification. | PASS |
| Errors/provider outage | `AUTH-ERROR` covers provider unavailable, cancel, network/unknown outcome, ambiguous identity, session creation failure and revoked/disabled account/provider states with accountless continuation. | PASS |
| Logout | `AUTH-ACCOUNT → AUTH-LOGOUT-PENDING` ends session access only and distinguishes account/device/J0-J1/DNS lifecycles. | PASS |
| Session expiry | `AUTH-REAUTH` fails account-only access closed, preserves core access and forbids automatic replay of pending destructive actions after re-authentication. | PASS |
| Account deletion entry | `AUTH-DELETE-ENTRY` explains account/device-management deletion scope versus J0/J1 and physical DNS removal, then hands off to downstream deletion execution. | PASS |
| Intake field states | Section 6 plus structured `intake_states` classify minimum hidden necessities, non-required provider profile fields and prohibited child/password/SMS data. | PASS |
| Back/resume | Section 7 covers back, provider cancel, callback refresh, retry, network loss, expiry, destructive-action re-entry and independent J0/J1 expiry. | PASS |
| Data-use explanation / minimal identity | `AUTH-DATA-USE` and first-session copy explain minimum account identity/purpose, excluded data and lifecycle separation without inventing legal/provider/privacy claims. | PASS |

## 4. Current-scope truth review

The prototype preserves all controlling current product rules:

- complete core value remains usable without login;
- Google is the planned Version-1 account route only, not an accepted provider/security architecture;
- no automatic J0/J1 join, promotion, linkage or expiry extension;
- account/session/dashboard presence never establishes technical `Verified` evidence;
- provider/session failures are account-only and do not change configured DNS truth;
- ambiguous identity fails closed without merge/duplicate/password/SMS fallback;
- logout, account deletion, dashboard/device-record deletion, J0/J1 deletion and physical DNS removal remain distinct;
- no child identity, browsing/query/activity history, raw DNS administration or unnecessary provider-profile intake is introduced.

**Result: PASS.**

## 5. UX/accessibility/localization review

The prototype defines mobile-first, keyboard-accessible, screen-reader-understandable pending/error/destructive-entry states; visible focus/control semantics; no color-only status meaning; and English/Turkish/Arabic+RTL localization capability without inferring non-UK market activation. Provider branding assets/guidelines are intentionally deferred to later approved provider work.

**Result: PASS for L4 interaction-prototype scope.**

## 6. Deterministic coverage

The persisted prototype contains 20 deterministic cases `AUTH-P01` through `AUTH-P20`. The structured state model independently binds:

- 12 logical screens;
- 12 required interaction flows;
- 10 intake-state classifications;
- 6 error classes;
- 13 binding invariants; and
- all 20 acceptance-case identifiers.

These are sufficient inputs for an independent structural/semantic verifier without relying on incidental prose wording.

## 7. Downstream non-inference

This candidate does not approve or infer:

- Google/Firebase vendor, OAuth/OIDC, provider/privacy/security architecture;
- cookie/token/CSRF/session implementation;
- persistent schema/storage/retention/backup/authorization implementation;
- actual account deletion execution;
- implementation/build/deployment/production behavior;
- real-user behavioral validation;
- LG-06 or any later gate PASS.

`RSK-0002` remains OPEN/non-blocking before L8.

## 8. Analytical disposition

Every current ACC-0329 clause is represented in the exact persisted prototype and structured state model with current scope/privacy/evidence/accessibility boundaries preserved.

**Analytical result: ACC-0329 PASS candidate.**

TSK-0329 remains non-PASS until a separate deterministic verifier proves the exact persisted inputs and the result is durably evidenced and reconciled/read back in `CURRENT_STATE.md`.
