# TSK-0376 — Accountless state-machine acceptance evidence

**Date:** 2026-09-03  
**Task:** `TSK-0376` — Implement minimal accountless state machine  
**Verification:** `VER-0376`  
**Evidence:** `EVD-0376`  
**Acceptance:** `ACC-0376`  
**Result:** __RESULT__

## Canonical authority and implementation

- Canonical repository/branch: `Yaserbayad/UseSafeWeb.com` / `main`.
- Canonical implementation base: `ca6848be9605e62e59f811fbbf661ff319df34ec`.
- Accepted feature head: `b423c0304354b22b3151e1660f3e06299ff11f0a`.
- Feature acceptance run/job: `33730514968` / `100569122644` — success.
- Implementation PR: `#78`.
- Canonical implementation merge: `ce48a5f5fd754e95775a7fab571dba1b2d65ee81`.
- Clean-main acceptance run/job: `33730835303` / `100570144399` — success.
- Canonical WBS blob asserted by the acceptance workflow: `eb35f3b10356396c5117e3f47d0b0378953e2157`.
- `website/src/lib/core-state-machine.ts` blob: `8bebd5f429cdaf03c416c9c64e93fc7ed804ee6a`.
- `website/src/lib/journey-state.ts` blob: `9f7a9dcf4a18e001869350d956c68bd5fc492632`.
- `website/src/components/dns-verification-panel.tsx` blob: `6eeba1ff230ba672a8bf053fa2500a10227e4d91`.
- `website/tests/contract/tsk0376.test.mjs` blob: `2c83ae1bfecf59545518b383e6cdb323749a8847`.
- `.github/workflows/accept-tsk0376-accountless-state-machine-20260903.yml` blob: `7297bcd05032da3c388da66daac38dc27a6c4e5a`.

## Acceptance evidence

The exact clean-main run `33730835303` checked out `ce48a5f5fd754e95775a7fab571dba1b2d65ee81` and passed the repository-structure validator, canonical Master-Plan validator, focused TSK-0376 contract, complete current website contract suite, lint, typecheck, production build, dependency audits, `git diff --check`, and clean-worktree guard.

Observed clean-main results:

- Master-Plan validation: PASS — 641 tasks, 858 dependency edges, 4,587 relationship entities, 18,152 relationship targets, 0 broken links, 0 generated missing task IDs.
- Focused `tsk0376` contract: 6/6 PASS, 0 failures.
- Complete website contract suite: 74/74 PASS, 0 failures.
- Lint: PASS with 0 errors and one non-blocking existing unused-parameter warning in `core-state-machine.ts`.
- Typecheck: PASS.
- Next.js production build: PASS; 58 static pages generated.
- `npm audit --audit-level=high`: 0 vulnerabilities.
- `npm audit --omit=dev --audit-level=high`: 0 vulnerabilities.
- Final acceptance marker: `TSK0376_ACCOUNTLESS_STATE_MACHINE_ACCEPTANCE=PASS`.
- Same exact clean-main implementation head also passed TSK-0243 run `33730835298`, TSK-0359 run `33730835373`, TSK-0360 run `33730835390`, TSK-0375 run `33730835265`, and TSK-0629 run `33730835322`.

## ACC-0376 / VER-0376 mapping

1. **All state transitions are defined/tested.** The canonical core state machine defines the Phone → Internet → Services progression and the supported setup, verification, troubleshooting, recovery/removal, restart, and completion transitions; focused contract test 1 proves the canonical happy path.
2. **Illegal transitions are rejected.** The transition default fails closed and focused contract test 2 verifies illegal events throw rather than silently advancing or no-oping.
3. **Parent-confirmed and verified evidence are separate.** `evaluateProtection` maps configuration-only evidence to `configured/parent-confirmed` and fresh positive technical evidence to `protected/verified`; focused contract test 3 verifies the separation and rejects evidence-free `VERIFICATION_RESULT` events.
4. **Resume/retry does not duplicate completed work.** Focused contract tests 4 and 5 prove deterministic replay/resume, a bounded retry limit of 3, non-sliding 24-hour expiry, safe malformed/expired restart, and no retained parallel verification model.
5. **No manufactured verification state.** Negative/uncertain verification cannot enter Services, retry does not retain verification evidence, and the client adapter binds trusted classifier evidence into `VERIFICATION_RESULT`; focused tests 3, 4, and 6 cover these boundaries.
6. **Journey-0 privacy/accountless constraints remain intact.** State remains `sessionStorage`-only/accountless, exact-key validated, hard-expired at 24 hours, safely deleted/restarted when malformed or expired, and excludes browsing/query/domain/hostname/raw-DNS history fields; focused tests 5 and 6 plus the immutable Journey-0 source blob prove the retained-state boundary.

## Security, privacy, rollback, and side effects

- No account or identity state is required for the core journey.
- No browsing/query/domain/hostname/raw-DNS history is introduced into retained journey/core state.
- Positive technical verification still requires trusted fresh technical evidence; client-only/evidence-free events cannot manufacture `protected/verified`.
- Retry is bounded at 3 and deterministic.
- The accepted implementation and this evidence publication are source/repository-only. Ordinary source rollback is available by reverting the relevant commits; no deployment or external runtime side effect is required to reverse this repository state.
- No profile was distributed, no participant data was processed, no runtime or market was activated, and no downstream lifecycle gate is activated by this evidence record.

## Guarded runtime publication

- Starting canonical implementation head: `ce48a5f5fd754e95775a7fab571dba1b2d65ee81`.
- Exact pre-mutation `CURRENT_STATE.md` blob: `7e8230993f5a3fa487857754d095a8f9598b36b5`.
- Publication guard run: `__SYNC_RUN_ID__`.
- Publication timestamp: `__SYNC_TIMESTAMP__`.
- Responsible verifier: governed ChatGPT execution using canonical GitHub authority plus GitHub Actions acceptance/guard runs and post-merge canonical read-back.
- Deviations: one non-blocking lint warning (`_accountState` unused) observed in the accepted clean-main run; no acceptance failure and no security/privacy deviation identified.

Runtime `PASS` is valid only after the guarded evidence/state publication is merged to canonical `main` and both this evidence artifact and `CURRENT_STATE.md` are independently read back from canonical GitHub.