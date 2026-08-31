# TSK-0331 — Post-CR-0007 Account / Device Lifecycle Acceptance Evidence

**Task:** TSK-0331 — Design account/device deletion, reinstall, revoke, replacement and recovery flows  
**Acceptance:** ACC-0331  
**Verification:** VER-0331  
**Evidence:** EVD-0331 analytical review  
**Date:** 2026-08-31  
**Result:** PASS CANDIDATE — pending deterministic evidence binding and guarded runtime reconciliation

## 1. Current acceptance contract

ACC-0331 requires: **Flows make consequences explicit, require appropriate confirmation, handle partial/provider failures, offer safe recovery, preserve truthful protection state and define what account/device metadata is deleted or retained.**

Current WBS authority is blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`; TSK-0331 is L4/MEDIUM, dependencies `TSK-0332; TSK-0334`, A4 / `AUTO_ALLOWED`, with `ACC-0331 / VER-0331 / EVD-0331`.

Bounded current-authority inspection run/job `33418610672 / 99575181549` completed SUCCESS and proved both dependencies current durable PASS, exact WBS/graph agreement, and no pre-existing TSK-0331 product artifact.

## 2. Exact verified candidate

- Normative lifecycle prototype: `prototype/TSK-0331/ACCOUNT_DEVICE_LIFECYCLE_FLOWS.md`, version `1.0.0-post-cr0007`, blob `9f5994b31b63a018ea0212ce21083b9dacb39ecc`.
- Structured lifecycle model: `prototype/TSK-0331/LIFECYCLE_STATE_MODEL.json`, blob `442c5a7fb2fb0f5af23ef29878f383fd3cfaa294`.
- Runnable UI shell: `prototype/TSK-0331/index.html`, blob `64bb4fa2f64d76dc4655f55f85304da5c6ffca9a`.
- Responsive/accessibility CSS: `prototype/TSK-0331/prototype.css`, blob `2a0d633efb4f138566d8d05e9fc60632e5409f29`.
- Interaction controller: `prototype/TSK-0331/app.mjs`, blob `9b8df052bc19c15bfa8cc217bb7932a251b80588`.
- Structural verifier: `.github/scripts/verify_tsk0331_post_cr0007_structured_20260831.py`, blob `9b9de230512dda3debc6d75b33cb7bedaaeec6c2`.
- Browser verifier: `.github/scripts/verify_tsk0331_browser_20260831.mjs`, blob `e4940c55dce3f589c04c16a533d0c08eb8ea982f`.
- Verification workflow: `.github/workflows/verify-tsk0331-post-cr0007-structured-20260831.yml`, blob `6cea6ddc3a0f8071180ca1ef2dfa6da083da2ff4`.
- Pre-acceptance runtime: `CURRENT_STATE.md`, blob `b5700eef473850ac49fdc83ea5bfbe7f2c6e54f2`.

## 3. ACC-0331 clause review

| ACC-0331 obligation | Verified design behavior | Result |
| --- | --- | --- |
| consequences explicit | Account deletion, record deletion, unlink/revoke, physical removal, reconfigure and replacement each state the exact narrow consequence and what remains unchanged. | PASS |
| appropriate confirmation | Destructive account/device/physical lifecycle mutations have explicit consequence screens; cancellation returns safely without mutation. | PASS |
| partial/provider failures | Provider unavailable, session expiry, network loss after submit, confirmed failure, unknown result, ownership mismatch, partial physical removal and replacement failure are explicitly modeled. | PASS |
| safe recovery | Unknown destructive outcomes require authoritative state read-back; duplicate destructive requests remain blocked; reauthentication never automatically replays the prior mutation. | PASS |
| truthful protection state | Account/session/provider/record/unlink operations never upgrade, downgrade or remove physical protection truth by themselves; physical `Removed` requires the owning removal result. | PASS |
| deleted/retained metadata defined | Product-visible account deletion targets account-domain records/associations/settings/sessions while explicitly separating physical configuration, J0/J1 and any future separately approved limited retention. Record deletion and unlink have narrower targets. | PASS |

## 4. Security / privacy / lifecycle review

The candidate preserves the controlling Version-1 boundary:

- core setup/protection remains usable without login;
- ownership mismatch fails closed without cross-account identity or record disclosure;
- session expiry halts account-only destructive work and requires fresh confirmation after reauthentication;
- unknown non-idempotent outcomes are never blindly replayed;
- provider/account/session/device-record presence never establishes technical `Verified` protection;
- physical protection removal is distinct from account deletion, record deletion, unlink/revoke, logout and J0/J1 deletion;
- replacement starts a fresh device lifecycle with no inherited Verified/parent-confirmed state or activity history;
- routine flows request no browsing/query/activity history, raw DNS logs, child identity, provider password/token or broad network data;
- no raw/unrestricted DNS administration or broad per-domain controls are introduced.

The deletion/retention wording intentionally does not invent a storage schema, legal retention obligation or retention duration. Any future required retained category/purpose/period remains owned by downstream approved data/legal/privacy/security contracts.

**Analytical result: PASS.**

## 5. Verification history

1. **RED proof** — run/job `33418733004 / 99575585891`: expected failure because `prototype/TSK-0331/ACCOUNT_DEVICE_LIFECYCLE_FLOWS.md` did not yet exist; WBS, dependency-runtime and relationship-graph checks passed first.
2. First GREEN browser run/job `33419145661 / 99576961041`: every structural acceptance check passed. Browser verification then failed on `skip-link-first-focus` because the test started from a synthetic `#account` hash instead of the normal initial page load. The product candidate was unchanged; only the accessibility test setup was corrected to exercise the real default-load keyboard order.
3. **Final run/job `33419292638 / 99577450844`: SUCCESS** at head commit `a8909416ab8e4cb79c6e3fef536a40758be93389`.

## 6. Final deterministic observations

Final structural markers:

- `TSK0331_WBS_CONTRACT=PASS`
- `TSK0331_DEPENDENCY_RUNTIME=PASS`
- `TSK0331_GRAPH_CONTRACT=PASS`
- `TSK0331_STRUCTURED_MODEL=PASS`
- `TSK0331_NORMATIVE_PROTOTYPE=PASS`
- `TSK0331_STATIC_UI_CONTRACT=PASS`
- `TSK0331_STRUCTURED_VERIFICATION=PASS`

Final browser/runtime markers:

- `TSK0331_BROWSER_FUNCTIONAL=PASS`
- `TSK0331_BROWSER_NEGATIVE_SECURITY=PASS`
- `TSK0331_BROWSER_CONFIGURATION_TRUTH=PASS`
- `TSK0331_BROWSER_PRIVACY=PASS`
- `TSK0331_BROWSER_ROLLBACK_RECOVERY=PASS`
- `TSK0331_BROWSER_RESPONSIVE=PASS`
- `TSK0331_BROWSER_KEYBOARD=PASS`
- `TSK0331_BROWSER_RTL=PASS`
- `TSK0331_BROWSER_NO_CONSOLE_ERRORS=PASS`

The successful job ran on self-hosted `adguardvm`, used pinned Node `22.23.2` and temporary verification-only Playwright `1.62.0`/Chromium provisioning, and passed `git diff --check` plus clean-worktree verification. The product dependency tree was not changed for browser verification.

## 7. Browser acceptance scope

The final browser suite directly exercised:

- account deletion entry, explicit confirmation, cancellation rollback and pending duplicate-submit protection;
- unknown deletion outcome, disabled duplicate action and authoritative recovery;
- session-expiry reauthentication without automatic replay;
- provider failure and accountless fallback;
- ownership mismatch fail-closed behavior;
- saved-record deletion versus physical protection removal;
- unlink/revoke versus physical protection removal;
- confirmed physical-removal semantics;
- reconfiguration requiring fresh technical verification;
- replacement with fresh unverified state and no inheritance;
- deleted-versus-retained account/J0-J1 wording;
- 320/768/1024/1440 responsive no-overflow behavior;
- keyboard skip-link and state-heading focus;
- Arabic RTL direction with unchanged destructive semantics;
- ordinary-surface privacy exclusions;
- zero browser console/page errors.

## 8. Non-inference boundary

This evidence proves only the current TSK-0331 L4 interaction design. It does not approve or infer provider/vendor/security/privacy architecture, persistence schema/storage/retention/backup/authz implementation, legal retention obligations, production account/device deletion, production physical-removal execution, build/deployment behavior, TSK-0333, real-user validation, or LG-06 PASS.

`RSK-0002` remains OPEN/non-blocking before L8.

**Analytical disposition:** ACC-0331 PASS candidate, pending deterministic evidence binding and guarded runtime reconciliation/read-back only.
