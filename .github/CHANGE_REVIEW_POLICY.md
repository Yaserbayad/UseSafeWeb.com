# Change and Review Policy

This repository uses deterministic local/CI checks plus explicit review ownership for critical paths.

## Required change checks

For website changes, run from `/website`:

```sh
npm ci
npm run format:check
npm run lint
npm run typecheck
npm run test:contract
```

The TSK-0453 GitHub Actions workflow runs formatting, linting, type checking, and the focused change-policy contract on pull requests and `main`. Existing task-specific workflows continue to own their acceptance boundaries.

Under DEC-0060/CR-0013, the permanent governed promotion context is the TSK-0489 workflow job `governed-ci`, with `promotion-eligibility` proving the same exact head is eligible only after the gate succeeds. It runs on every pull request and every `main` push and invokes the repository-local `npm run validate` entrypoint plus governance validation, dependency/SBOM audits, and the approved synthetic security-control verifier. In the absence of native required-status protection, the governor must re-read the exact pull-request head immediately before merge and may merge only when `governed-ci`, `promotion-eligibility`, and every other path-applicable current check on that exact head have completed successfully. A failed, cancelled, timed-out, action-required, stale, or missing applicable check is not promotion evidence. Any bypass requires explicit owner authority and the bounded exception record required below.

The TSK-0489 workflow is read-only with respect to repository/deployment authority: it does not deploy, activate, mutate participant/service state, perform payment actions, or launch. Passing CI therefore proves source/promotion readiness only and never implies deployment or release authority.

## Change scope

Every pull request must identify application/source, generated, configuration, infrastructure, workflow, documentation, and governance impact when applicable. Generated artifacts are changed only when their owning process requires durable publication; otherwise regenerate them during verification and keep them out of Git.

Changes to critical paths declared in `.github/CODEOWNERS` retain advisory owner-routing metadata for visibility, but owner/Code Owner approval is **not a mandatory merge condition**. Under DEC-0060/CR-0013, ordinary governed `AUTO_ALLOWED` changes are accepted through deterministic automated local/CI quality and change-policy verification instead of a human approval gate.

## Exceptions

An exception to a required check or review rule must be explicit, narrow, and time-bounded. Record:

- exception scope and reason;
- accountable owner;
- approval/authority source;
- exact expiry date or terminating condition;
- compensating verification/control;
- follow-up issue/task or removal action.

No permanent or silent bypass is allowed. A failed check is fixed rather than disabled unless a recorded, unexpired exception explicitly authorizes the bounded deviation.

## Autonomous review boundary

Branch protection or required Code Owner approval is not required by ACC-0453 under DEC-0060/CR-0013. CODEOWNERS remains advisory routing metadata only. Formatting, linting, type checking, focused change-policy contracts, applicable tests/build/audits, generated/configuration impact coverage, and bounded exception documentation remain mandatory. A separate current human-authority, safety, security, legal, identity, contract, material-spend, strategic or irreversible-action boundary still overrides this policy where applicable.
