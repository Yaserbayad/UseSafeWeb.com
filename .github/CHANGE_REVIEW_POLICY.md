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

## Change scope

Every pull request must identify application/source, generated, configuration, infrastructure, workflow, documentation, and governance impact when applicable. Generated artifacts are changed only when their owning process requires durable publication; otherwise regenerate them during verification and keep them out of Git.

Changes to critical paths declared in `.github/CODEOWNERS` require owner review as repository policy. **GitHub only makes that requirement merge-blocking when the `main` branch is protected by a branch protection rule or ruleset requiring Code Owner review.** CODEOWNERS alone is review-routing metadata, not proof of platform enforcement.

## Exceptions

An exception to a required check or review rule must be explicit, narrow, and time-bounded. Record:

- exception scope and reason;
- accountable owner;
- approval/authority source;
- exact expiry date or terminating condition;
- compensating verification/control;
- follow-up issue/task or removal action.

No permanent or silent bypass is allowed. A failed check is fixed rather than disabled unless a recorded, unexpired exception explicitly authorizes the bounded deviation.

## Current platform enforcement boundary

Source policy and CODEOWNERS can be versioned here. Merge-blocking review enforcement is a GitHub repository setting. Until branch protection/rulesets are verified to require the intended review on `main`, TSK-0453 cannot claim that critical-path review is technically enforced.
