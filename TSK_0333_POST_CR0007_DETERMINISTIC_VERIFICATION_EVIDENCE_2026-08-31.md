# TSK-0333 — Post-CR-0007 Deterministic Verification Evidence

**Task:** TSK-0333  
**Acceptance:** ACC-0333  
**Verification:** VER-0333  
**Evidence:** EVD-0333 deterministic verification  
**Date:** 2026-08-31  
**Final deterministic result:** PASS — pending guarded runtime reconciliation/read-back only

## 1. Exact current authority and candidate

- WBS: `Plans/Master/WBS/master-wbs.csv`, blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`.
- Relationship graph: `Plans/Master/RELATIONSHIP_INDEX.yaml`, blob `c108d2c162bcea2ee4cc01def46d0487a9501032`.
- Pre-acceptance runtime: `CURRENT_STATE.md`, blob `15948b153c5c0c07b93fc894ac9f4ca6c537cce0`.
- Current dependencies: `TSK-0335; TSK-0334; TSK-0146; TSK-0331`, each current durable PASS.
- Integrated HTML: `prototype/TSK-0333/index.html`, blob `9395f0e105d20683b5beafa01b02d7b300e79a8d`.
- Integrated state model: `prototype/TSK-0333/model.mjs`, blob `9b7c239024d8ae24371b687aa39de6fa6b2b62b6`.
- Integrated controller/UI: `prototype/TSK-0333/app.mjs`, blob `476ea932d95592fabf586f7ba381be0d346117fe`.
- Responsive/accessibility CSS: `prototype/TSK-0333/prototype.css`, blob `6f8af459a0b0b1c9ec132657dfcd7ebff43090b8`.
- Analytical acceptance evidence: `TSK_0333_POST_CR0007_INTEGRATED_PROTOTYPE_ACCEPTANCE_EVIDENCE_2026-08-31.md`, blob `4de73da09d637a142fc9968873ffdd755fdb07f3`.
- Structured verifier: `.github/scripts/verify_tsk0333_post_cr0007_structured_20260831.py`, blob `497d709c40632a9bbd7e1f9513c27699e1f2d0f6`.
- Structured workflow: `.github/workflows/verify-tsk0333-post-cr0007-structured-20260831.yml`, blob `812ab1dbdead44f7cae4d5c9c1c9e7b653766b27`.
- Browser verifier: `.github/scripts/verify_tsk0333_post_cr0007_browser_20260831.mjs`, blob `966cb53e01e58155350fc9a904cf71bd1a30c748`.
- Browser workflow: `.github/workflows/verify-tsk0333-post-cr0007-browser-20260831.yml`, blob `532b1f6c67516e2e449720f791d91af4ee8fe2bc`.

## 2. Current WBS contract

TSK-0333 is L4 / MEDIUM, A3 / `AUTO_ALLOWED`, with `ACC-0333 / VER-0333 / EVD-0333`.

Current ACC-0333 requires the integrated prototype to cover the full accountless core plus optional Version-1 Google sign-in/account/session/dashboard/device-management/lifecycle paths, Android/iPhone DNS setup and verification, Protection Map/support/failure/recovery states, responsive/mobile/RTL/accessibility and privacy boundaries. Core value must never require login, and browsing/activity history plus broad DNS administration must remain absent.

## 3. Historical evidence disposition

The 2026-08-30 TSK-0333 prototype/evidence was not used as current PASS because it was accountless-only and its then-current dependency set did not include the now-required account/device lifecycle chain. It remains historical evidence only for compatible interaction concepts.

## 4. Test-first / incremental verification history

### RED proof

Run/job `33431633072 / 99618110708`: expected FAILURE against the unchanged historical prototype.

Before failure, current WBS, relationship graph and all current dependency-runtime checks passed. Exact failure was:

`TSK0333_INDEX_CURRENT_SCOPE_MISSING=usesafeweb`

This proved the current verifier rejected the stale accountless-only prototype before any product rebuild or runtime mutation.

### Structured incremental convergence

The prototype was rebuilt in explicit slices: current dual-mode state model/shell, then controller/interactions, then responsive/accessibility styling.

Final source-level structured run/job `33432040521 / 99619466660`: **SUCCESS**. The final browser workflow also reran the structured verifier at the accepted current head and passed it.

Observed structured markers:

- `TSK0333_CURRENT_AUTHORITY_BLOBS=PASS`
- `TSK0333_WBS_CONTRACT=PASS`
- `TSK0333_GRAPH_CONTRACT=PASS`
- `TSK0333_DEPENDENCY_RUNTIME=PASS`
- `TSK0333_STRUCTURED_MODEL=PASS`
- `TSK0333_INTERACTION_COVERAGE=PASS`
- `TSK0333_PRIVACY_LIFECYCLE_FENCES=PASS`
- `TSK0333_STATIC_UI_CONTRACT=PASS`
- `TSK0333_POST_CR0007_STRUCTURED_VERIFICATION=PASS`

## 5. Browser campaign and corrections

### Browser run 1 — substantive product defect

Run/job `33432339619 / 99620437461`: FAILURE.

The run first passed keyboard, Android accountless and false-positive-truth checks, then timed out looking for `REMOVE_DNS` from the configured Protection Map. The map did not expose the accepted physical-removal path while DNS was configured.

**Disposition:** real product defect. `prototype/TSK-0333/app.mjs` was corrected to expose `Remove UseSafeWeb DNS` when configured. The browser assertion was not weakened.

### Browser run 2 — verifier-only locator ambiguity

Run/job `33432524365 / 99621051328`: FAILURE after the product fix.

Before failure it passed keyboard, Android, false-positive, removal/recovery, iPhone, unsupported, new account, explicit device save, returning dashboard, replacement, and unknown-result/record-delete checks.

The failure was a Playwright strict-mode ambiguity because a role selector for `Start setup` matched both the global shortcut and the required local provider-error fallback button.

**Disposition:** verifier-only correction. The test was scoped to the screen-local `data-action="START"`. No product semantics changed.

### Browser run 3 — verifier-only privacy literal false negative

Run/job `33432645054 / 99621453921`: FAILURE after all functional scenarios through session/logout/delete and RTL/responsive had passed.

The privacy screen correctly said `No browsing history or activity history.` The verifier required the non-contiguous literal `no activity history`.

**Disposition:** verifier-only semantic correction. Product copy and semantics were unchanged.

### Browser run 4 — final decisive acceptance

Run/job `33432762152 / 99621849637`: **SUCCESS** at head `b7d212cf014d1dc2b0e37be2ac2a97837c000173`.

Environment:

- self-hosted runner `adguardvm`;
- Node `v22.23.2`;
- npm `10.9.8`;
- Playwright `1.62.0` in temporary runner-only directory;
- Chrome for Testing / Chromium `151.0.7922.34`;
- localhost-only static server;
- no product dependency-tree change.

Observed final browser markers:

- `TSK0333_BROWSER_KEYBOARD=PASS`
- `TSK0333_BROWSER_ACCOUNTLESS_ANDROID=PASS`
- `TSK0333_BROWSER_FALSE_POSITIVE_TRUTH=PASS`
- `TSK0333_BROWSER_REMOVAL_RECOVERY=PASS`
- `TSK0333_BROWSER_IPHONE=PASS`
- `TSK0333_BROWSER_UNSUPPORTED=PASS`
- `TSK0333_BROWSER_NEW_ACCOUNT=PASS`
- `TSK0333_BROWSER_EXPLICIT_DEVICE_SAVE=PASS`
- `TSK0333_BROWSER_RETURNING_DASHBOARD=PASS`
- `TSK0333_BROWSER_DEVICE_REPLACEMENT=PASS`
- `TSK0333_BROWSER_UNKNOWN_AND_RECORD_DELETE=PASS`
- `TSK0333_BROWSER_PROVIDER_ERROR=PASS`
- `TSK0333_BROWSER_SESSION_LOGOUT_DELETE_BOUNDARY=PASS`
- `TSK0333_BROWSER_RTL_RESPONSIVE=PASS`
- `TSK0333_BROWSER_PRIVACY_NO_TRANSPORT=PASS`
- `TSK0333_BROWSER_NO_CONSOLE_ERRORS=PASS`
- `TSK0333_POST_CR0007_BROWSER_VERIFICATION=PASS`

The workflow also passed its structured precheck, `git diff --check`, clean-worktree verification, setup-node cleanup and checkout cleanup.

## 6. What current evidence proves

The exact persisted prototype now proves current ACC-0333 by integrating:

- complete signed-out Android/iPhone setup and technical verification;
- deterministic Protection Map truth with strict technical `Verified` versus parent-confirmed separation;
- false-positive/support flows that do not manufacture state;
- physical removal → Removed → neutral recovery without false restoration → fresh reconfigure;
- unsupported/uncertain/action-needed handling;
- explicit optional Google sign-in and first-session account creation;
- returning account/session/error/reauthentication/logout flows;
- lightweight dashboard and explicit device saving;
- device reverify, reinstall/reconfigure, replacement, revoke/unlink and saved-record deletion;
- destructive-action consequence confirmation and fail-closed unknown-result recovery;
- account deletion entry separated from physical protection and J0/J1 lifecycle;
- responsive 320/768/1024/1440 behavior, keyboard/skip-link, RTL and reduced-motion contract;
- no browser persistence or external runtime transport in the prototype;
- no browsing/query/activity history, child profile, raw DNS history/logs, broad DNS administration or safety score.

## 7. Runtime/state fence

No RED or failing browser run mutated `CURRENT_STATE.md`. PASS is authorized only after this deterministic evidence is published, read back, and a guarded reconciliation confirms the pre-acceptance runtime and all accepted artifact/evidence identities remain unchanged.

## 8. Non-inference

This evidence proves **TSK-0333 only**. It does not infer LG-06, L5 architecture/security/privacy/vendor acceptance, production authentication/persistence/deletion behavior, deployment, publication, real-user validation or launch.

`RSK-0002` remains OPEN/non-blocking before L8.

## 9. Disposition

`ACC-0333 / VER-0333 / EVD-0333`: **CURRENT PASS**, subject only to guarded runtime reconciliation and GitHub read-back.
