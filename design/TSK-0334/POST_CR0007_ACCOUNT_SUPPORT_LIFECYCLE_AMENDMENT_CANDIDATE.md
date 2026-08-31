# TSK-0334 — Post-CR-0007 Account / Dashboard Support-Lifecycle Amendment — HUMAN_ONLY Candidate

**Version:** 1.0.0-post-cr0007  
**Task:** TSK-0334 — Design support, false-positive, removal, and reconfiguration flows  
**Acceptance:** ACC-0334  
**Status:** HUMAN_ONLY current-scope amendment candidate; **not approved / not PASS**  
**Date:** 2026-08-31

## 1. Purpose

This amendment updates the previously owner-approved TSK-0334 support-flow design for the current Version-1 product scope: complete accountless core plus optional parent account/session/minimum device persistence/lightweight dashboard.

It does **not** invalidate still-correct technical support behavior for setup verification, false positives, physical DNS removal/recovery, reconfiguration, unsupported paths, privacy-minimal diagnostics or truthful Protection Map states. It supersedes only the historical clauses that treated any account system/persistent device record as out of scope.

Current-scope sources:

- current post-CR-0007 TSK-0325 parent journey/service blueprint;
- current TSK-0329 optional Google sign-in/account/session interaction prototype;
- current TSK-0142 dashboard/device-management requirements;
- current post-CR-0007 TSK-0332 dashboard/device-management prototype;
- DEC-0053/CR-0006 and DEC-0054/CR-0007.

No provider/vendor/security/privacy architecture or implementation is approved here.

## 2. Current ACC-0334 interpretation

ACC-0334 requires **each major support category** to have:

1. an accessible path;
2. a minimal diagnostic request;
3. a clear protection consequence;
4. an escalation option;
5. a success state.

The five historical categories remain applicable:

- `SUP-01` setup/verification troubleshooting;
- `SUP-02` false positive / legitimate destination blocked;
- `SUP-03` physical UseSafeWeb protection removal and connectivity recovery;
- `SUP-04` reconfiguration / start setup again;
- `SUP-05` unsupported / uncertain / limitations.

Current Version-1 adds three account/dashboard support categories:

- `SUP-06` account sign-in/session/provider access problem;
- `SUP-07` saved device record / ownership / unlink / dashboard-management problem;
- `SUP-08` account/device deletion or lifecycle-result problem.

## 3. Global current-scope invariants

All eight support categories must preserve these rules:

- the complete core remains usable without login;
- provider/account/session/dashboard/device-record presence never establishes technical `Verified` protection;
- provider/account/session failure affects account-only access and does not rewrite physical DNS/protection truth;
- anonymous J0/J1 state is not automatically linked/promoted/imported into an account;
- logout, account deletion, dashboard-record deletion, unlinking, J0/J1 deletion and physical UseSafeWeb removal are distinct operations;
- an uncertain destructive-operation result must remain uncertain until authoritative state is resolved;
- no support flow requests passwords, tokens, child identity, browsing/query/activity history, raw DNS logs or broad device/network dumps by default;
- no support flow creates raw/unrestricted DNS administration or broad per-domain allow/block controls;
- ownership mismatch fails account-only operations closed; support cannot override authorization;
- a support acknowledgement/ticket/reference never upgrades protection or deletion state;
- no automatic replay of a destructive operation after re-authentication or recovery;
- Help remains accessible from signed-out core states and account-only failure states.

## 4. SUP-06 — Account sign-in / session / provider access problem

### Entry

A parent cannot enter or return to the optional account/dashboard because of provider unavailability, cancellation, network/unknown callback outcome, session creation failure, session expiry/revocation, account/provider disabled state, or ambiguous identity binding.

### Accessible path

`Sign in` / `Account` / expired-session state → **Get help** → **Account or sign-in problem**.

Signed-out **Start setup** and core Help remain available.

### Minimal diagnostic request

Use current in-memory account-flow context where available. Allowed diagnostic envelope:

- coarse problem class (`provider unavailable`, `sign-in cancelled`, `session ended`, `unknown result`, `account unavailable`);
- non-sensitive correlation/reference code if a later approved implementation provides one;
- provider type (`Google`) when needed to distinguish the route.

Do not request provider password/token, child identity, full provider profile, browsing history or raw session material.

### Protection consequence

**None by itself.** Account/session/provider failure does not change the physical device’s current protection state or an existing Protection Map result.

### Recovery / escalation

- retry sign-in only when safe and without duplicating account creation;
- resolve an unknown callback/result from authoritative account state before retrying a mutation;
- ambiguous identity fails closed: no silent merge, duplicate account, password/SMS fallback or support-side identity override;
- exceptional escalation may carry only the allowed diagnostic envelope to a separately approved operational route.

### Success state

One truthful outcome:

- account-only access restored to the authorized existing account/dashboard;
- parent returns to a known signed-out state and can use the accountless core;
- account/provider remains unavailable with a clear stop/help route.

No success state implies stronger protection.

## 5. SUP-07 — Saved device record / ownership / unlink problem

### Entry

A signed-in parent encounters a missing/deleted/revoked record, ownership mismatch, stale dashboard record, unlink failure/unknown result, or cannot resume an authorized saved device-management path.

### Accessible path

Dashboard/device detail/Manage → **Help** → **Device record or ownership problem**.

### Minimal diagnostic request

Use the authenticated account context and selected device record internally. Ask only for a parent-facing device nickname/platform if needed to disambiguate among the parent’s own authorized records. Do not ask for child identity or network/activity history.

### Protection consequence

- missing/unlinked/deleted dashboard record does **not** prove physical UseSafeWeb removal;
- record presence does **not** prove current protection;
- ownership mismatch does not alter the physical device state; it blocks the account-only operation.

### Recovery / escalation

- ownership/authorization mismatch fails closed; support cannot transfer ownership or expose another account’s record;
- stale record may route to current **Check again**, reconfigure, unlink or record deletion according to the owning flow;
- unknown unlink/deletion outcome remains **We could not confirm the result** until authoritative state is resolved;
- escalation uses only record reference/account context required by an approved support implementation, never raw DNS history.

### Success state

One truthful outcome:

- authorized record access restored;
- record intentionally unlinked/deleted and dashboard reflects that result;
- record remains unavailable with a clear account-only stop/help path;
- parent uses accountless setup/help for the physical device independently.

## 6. SUP-08 — Account/device deletion or lifecycle-result problem

### Entry

Account deletion, dashboard-record deletion, revoke/unlink, or another account lifecycle operation is pending, failed, timed out or has an unknown result; or the parent is unclear about the difference between deleting account data and physically removing protection.

### Accessible path

Account/Delete account entry or Device/Manage destructive action → consequence screen → **Help** when failure/uncertainty occurs.

### Minimal diagnostic request

Use the authenticated account/action context and a non-sensitive operation/reference identifier if the implementation has one. Do not request password/token, child identity, browsing/query history or raw DNS logs.

### Protection consequence

- account deletion concerns persistent account/device-management records only as defined by the owning deletion contract;
- dashboard-record deletion concerns that saved record only;
- J0/J1 anonymous-state deletion remains separate;
- physical UseSafeWeb protection removal requires the owning physical removal flow and cannot be claimed from account/data deletion success;
- logout ends session access only.

### Recovery / escalation

- destructive operations are not automatically replayed after re-authentication;
- unknown outcomes require authoritative read-back before retry;
- repeated equivalent destructive requests are blocked until current state is known;
- support may explain consequences but cannot bypass authorization or invent deletion completion;
- escalation carries only minimum operation/account references to an approved operational route.

### Success state

A confirmed lifecycle result stated narrowly, for example:

- **Account deleted** — only after the owning account deletion contract proves it;
- **Removed from dashboard** — only the saved record consequence;
- **Device unlinked** — management association consequence only;
- **UseSafeWeb protection removed** — only after the physical removal contract proves it;
- **Result not confirmed** — if authoritative state remains unknown.

## 7. Shared accessibility and language contract

The amendment inherits current mobile-first/WCAG 2.2 AA behavior:

- semantic headings/landmarks;
- keyboard-operable controls and visible focus;
- programmatic state changes announced/focused appropriately;
- no color-only meaning;
- explicit destructive consequences before action;
- English/Turkish/Arabic+RTL capability with identical lifecycle semantics;
- account/support failures use parent-facing language and do not expose provider tokens, internal storage IDs or administration terminology.

## 8. Current deterministic review matrix

| ID | Scenario | Required result |
| --- | --- | --- |
| `TC-0334-C01` | Provider unavailable | Account-only error; core still available; protection unchanged. |
| `TC-0334-C02` | User cancels Google sign-in | Known signed-out state; no product account mutation. |
| `TC-0334-C03` | Callback outcome unknown | Resolve authoritative account state before retry; no duplicate account. |
| `TC-0334-C04` | Session expired | Re-auth for account-only action; no destructive auto-replay; protection unchanged. |
| `TC-0334-C05` | Ambiguous identity | Fail closed; no merge/duplicate/password/SMS fallback. |
| `TC-0334-C06` | Device ownership mismatch | Account-only operation denied; no cross-account data exposure. |
| `TC-0334-C07` | Saved record missing | Explain record state; do not claim physical protection removal. |
| `TC-0334-C08` | Unlink outcome unknown | Remain uncertain; authoritative read-back before retry. |
| `TC-0334-C09` | Record deletion succeeds | Remove dashboard record only; do not claim physical DNS removal. |
| `TC-0334-C10` | Account deletion pending/fails | No false completion; preserve exact current account state. |
| `TC-0334-C11` | Account deletion succeeds | State only approved persistent-account/data consequence; no physical protection claim. |
| `TC-0334-C12` | Logout | End session only; account/device/J0-J1/DNS lifecycles unchanged. |
| `TC-0334-C13` | Parent needs physical removal | Route to SUP-03; account/record deletion is not a substitute. |
| `TC-0334-C14` | Account problem plus configured device | Signed-out help/setup remains available; physical state unchanged. |
| `TC-0334-C15` | Support diagnostic request | Minimum context only; no passwords/tokens/history/raw DNS/child identity. |
| `TC-0334-C16` | Arabic mobile support state | Same consequence/recovery semantics under RTL. |

## 9. Human decision boundary

TSK-0334 remains `HUMAN_ONLY` in the current WBS. This candidate can be prepared and independently checked autonomously, but **cannot be accepted or marked PASS without explicit Project Owner approval**.

Owner approval, if granted, should bind the exact historical base candidate plus this exact amendment and mean only:

- the still-valid historical technical support flows remain accepted;
- the account/dashboard exclusions in the historical candidate are superseded by this amendment;
- SUP-06/07/08 become part of the accepted TSK-0334 current support-flow design;
- no provider/vendor/security/privacy architecture, implementation, live support operation, production deletion or behavioral evidence is approved.

## 10. Non-inference

Preparation or later approval of this amendment does not infer TSK-0331, TSK-0333, LG-06, implementation/build, provider/vendor/security/privacy architecture, production operations or real-user validation.
