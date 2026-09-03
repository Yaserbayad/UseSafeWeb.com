# `/website` — application source root

**Owner:** Software / Frontend / Backend Engineering  
**Interface:** INT-0011 application release candidate; INT-0012 DNS setup/verification integration.

This directory is the canonical home of the approved **TypeScript + Next.js** full-stack application. **TSK-0361** owns implementation of the actual application, framework/dependency versions, build scripts, routes, localization, accessibility, performance, security, SEO and approved content integration. TSK-0454 establishes only the source boundary and therefore does not prematurely pin application dependencies.

## Deterministic local baseline

The supported validation baseline is **Node.js 22.23.2** with **npm 10.9.8**. The Node version is pinned in `.nvmrc`; `package.json` records the npm baseline. From a clean checkout:

```sh
cd website
nvm use
npm ci
npm run validate
```

`npm ci` installs exactly the dependency graph in `package-lock.json` without rewriting the lockfile. `npm run validate` runs the complete baseline quality chain in order: contract tests, lint, type checking, then the production build. The command stops and returns nonzero on the first failing gate. No production environment, secret, live device, profile action, telemetry activation, or deployment is required for this local validation baseline.

If `nvm` is not available, use another Node installation method that provides exactly Node.js 22.23.2 and npm 10.9.8 before running `npm ci`; there is no additional repository-specific setup step.

## Structure

- `src/` — application source owned by feature implementation tasks.
- `public/` — versioned public assets that are safe to ship.
- `config/` — documentation and future non-secret application configuration contracts.
- `tests/` — application-owned unit/integration/browser acceptance tests.

## Data and configuration rules

The Version-1 accountless-first design requires **no local database** merely to establish this repository structure. Any later datastore introduced for the approved optional parent-account boundary must be selected by its owning task and current architecture/privacy/security authority.

Secrets, credentials, private keys and production environment values remain outside Git. Non-secret configuration may be versioned when its owning task defines the exact contract.

## Generated files

Generated build output such as `.next/`, dependency directories, `dist/` and `coverage/` is not source authority and is excluded by the root `.gitignore`. Durable release evidence records exact source/config identities rather than committing generated local output by default.
