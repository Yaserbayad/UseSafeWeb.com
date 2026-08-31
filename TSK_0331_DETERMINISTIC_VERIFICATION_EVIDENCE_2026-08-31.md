# TSK-0331 — Deterministic Verification Evidence

**Task:** TSK-0331 — Design account/device deletion, reinstall, revoke, replacement and recovery flows  
**Acceptance:** ACC-0331  
**Verification:** VER-0331  
**Evidence:** EVD-0331 deterministic post-CR-0007 verification  
**Date:** 2026-08-31  
**Final deterministic result:** PASS

## 1. Exact verified authority and artifacts

- WBS: `Plans/Master/WBS/master-wbs.csv`, blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`.
- Relationship graph: `Plans/Master/RELATIONSHIP_INDEX.yaml`, blob `c108d2c162bcea2ee4cc01def46d0487a9501032`.
- Pre-reconciliation runtime: `CURRENT_STATE.md`, blob `b5700eef473850ac49fdc83ea5bfbe7f2c6e54f2`.
- Current hard dependencies: TSK-0332 PASS and TSK-0334 PASS.
- Normative lifecycle prototype: `prototype/TSK-0331/ACCOUNT_DEVICE_LIFECYCLE_FLOWS.md`, version `1.0.0-post-cr0007`, blob `9f5994b31b63a018ea0212ce21083b9dacb39ecc`.
- Structured lifecycle model: `prototype/TSK-0331/LIFECYCLE_STATE_MODEL.json`, blob `442c5a7fb2fb0f5af23ef29878f383fd3cfaa294`.
- Runnable HTML: `prototype/TSK-0331/index.html`, blob `64bb4fa2f64d76dc4655f55f85304da5c6ffca9a`.
- CSS: `prototype/TSK-0331/prototype.css`, blob `2a0d633efb4f138566d8d05e9fc60632e5409f29`.
- Interaction controller: `prototype/TSK-0331/app.mjs`, blob `9b8df052bc19c15bfa8cc217bb7932a251b80588`.
- Analytical evidence: `TSK_0331_POST_CR0007_ACCOUNT_DEVICE_LIFECYCLE_ACCEPTANCE_EVIDENCE_2026-08-31.md`, blob `81ebe13e71d168b4305d9a3791a15be70baa43b9`.
- Structural verifier: `.github/scripts/verify_tsk0331_post_cr0007_structured_20260831.py`, blob `9b9de230512dda3debc6d75b33cb7bedaaeec6c2`.
- Browser verifier: `.github/scripts/verify_tsk0331_browser_20260831.mjs`, blob `e4940c55dce3f589c04c16a533d0c08eb8ea982f`.
- Verification workflow: `.github/workflows/verify-tsk0331-post-cr0007-structured-20260831.yml`, blob `6cea6ddc3a0f8071180ca1ef2dfa6da083da2ff4`.

## 2. Exact WBS contract

TSK-0331 is L4 / MEDIUM, dependencies `TSK-0332; TSK-0334`, `ACC-0331 / VER-0331 / EVD-0331`, A4 / `AUTO_ALLOWED`.

ACC-0331 requires:

> Flows make consequences explicit, require appropriate confirmation, handle partial/provider failures, offer safe recovery, preserve truthful protection state and define what account/device metadata is deleted or retained.

Bounded eligibility inspection run/job `33418610672 / 99575181549` completed SUCCESS and proved the exact WBS/graph contract, both dependencies current PASS and no pre-existing TSK-0331 product artifact.

## 3. Test-first and diagnostic history

1. **RED proof** — run/job `33418733004 / 99575585891`: expected failure `TSK0331_REQUIRED_ARTIFACT_MISSING=prototype/TSK-0331/ACCOUNT_DEVICE_LIFECYCLE_FLOWS.md`; WBS, dependency-runtime and graph checks passed before the missing-artifact fence.
2. Implementation added the normative lifecycle specification, structured state model and runnable responsive interaction prototype.
3. First GREEN run/job `33419145661 / 99576961041`: all structural acceptance checks PASS. The browser suite then failed `skip-link-first-focus` because the test used a synthetic `#account` navigation before checking initial keyboard order. The product files did not change for this failure.
4. Browser verifier correction changed only the test setup to load the actual default URL before the first-Tab skip-link assertion.
5. **Final run/job `33419292638 / 99577450844`: SUCCESS** at head commit `a8909416ab8e4cb79c6e3fef536a40758be93389`.

No runtime PASS was written during RED or failing GREEN verification.

## 4. Final verification environment

- Runner: self-hosted `adguardvm`.
- Node: pinned `22.23.2` through `actions/setup-node@v4`.
- Playwright: pinned `1.62.0`, installed into a temporary verification-only runner directory.
- Chromium: installed into the same temporary verification-only browser path.
- Product dependency tree was not modified to support verification.

## 5. Final observed PASS markers

Structural:

- `TSK0331_WBS_CONTRACT=PASS`
- `TSK0331_DEPENDENCY_RUNTIME=PASS`
- `TSK0331_GRAPH_CONTRACT=PASS`
- `TSK0331_STRUCTURED_MODEL=PASS`
- `TSK0331_NORMATIVE_PROTOTYPE=PASS`
- `TSK0331_STATIC_UI_CONTRACT=PASS`
- `TSK0331_STRUCTURED_VERIFICATION=PASS`

Browser / target-environment:

- `TSK0331_BROWSER_FUNCTIONAL=PASS`
- `TSK0331_BROWSER_NEGATIVE_SECURITY=PASS`
- `TSK0331_BROWSER_CONFIGURATION_TRUTH=PASS`
- `TSK0331_BROWSER_PRIVACY=PASS`
- `TSK0331_BROWSER_ROLLBACK_RECOVERY=PASS`
- `TSK0331_BROWSER_RESPONSIVE=PASS`
- `TSK0331_BROWSER_KEYBOARD=PASS`
- `TSK0331_BROWSER_RTL=PASS`
- `TSK0331_BROWSER_NO_CONSOLE_ERRORS=PASS`

The final workflow also passed `git diff --check` and clean-worktree assertions.

## 6. What was proven

The exact persisted TSK-0331 candidate satisfies ACC-0331 by proving:

- destructive lifecycle consequences are explicit before execution;
- account deletion, saved-record deletion, unlink/revoke and physical protection removal remain separate operations;
- cancellation is safe and leaves the pre-action state unchanged;
- pending/unknown destructive outcomes block duplicate execution;
- unknown non-idempotent outcomes require authoritative state read-back before retry;
- session expiry requires reauthentication and fresh destructive confirmation, with no automatic replay;
- provider failures are account-only and preserve accountless core availability;
- ownership mismatch fails closed without cross-account disclosure/mutation;
- physical protection truth is not rewritten by account/session/provider/device-record operations;
- physical `Removed` is represented only in the separate owning physical-removal flow;
- reinstall/reconfigure requires new current technical evidence rather than silently carrying an earlier positive state;
- replacement creates a fresh unverified lifecycle and inherits no Verified/parent-confirmed state or history;
- account deletion defines the account-domain metadata targeted for deletion and explicitly separates physical configuration, J0/J1 and any future separately approved limited retention;
- saved-record deletion and unlink/revoke have narrower defined metadata/association consequences;
- ordinary flows collect no browsing/query/activity history, raw DNS logs, child identity, provider secret or broad network dump;
- responsive, keyboard, RTL and zero-browser-error behavior was observed in the target browser suite.

## 7. Security / non-idempotent-operation boundary

This is an L4 interaction contract. It explicitly requires production implementations to fail closed on ownership mismatch, avoid automatic replay of destructive operations, resolve unknown results from authoritative state, and preserve exact physical-protection truth. It does not itself implement authentication, authorization, persistence, deletion or physical DNS mutation.

## 8. Non-inference boundary

This evidence proves **TSK-0331 only**. It does not approve or infer provider/vendor/security/privacy architecture, persistent schema/storage/retention/backup/authorization implementation, legal retention obligations, production account/device deletion, production physical-removal execution, build/deployment behavior, TSK-0333, real-user validation, or LG-06 PASS.

`RSK-0002` remains OPEN/non-blocking before L8.

## 9. Disposition

`ACC-0331 / VER-0331 / EVD-0331`: **PASS**, subject only to successful guarded runtime reconciliation and GitHub read-back of `CURRENT_STATE.md`.
