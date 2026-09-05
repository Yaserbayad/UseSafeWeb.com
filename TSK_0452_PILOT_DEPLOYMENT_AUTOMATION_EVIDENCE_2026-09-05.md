# TSK-0452 Pilot Deployment Automation Evidence — 2026-09-05

## Authority and scope

- Project: `UseSafeWeb.com`
- Governance checkpoint at execution: `CURRENT_STATE.md` revision `17`, baseline `1`, project state `ACTIVE`.
- Acceptance: `ACC-0452` / `TSK-0452`.
- Deployment source: immutable repository commit `efe9d4d885d6057b18c5fddea5a0dd2d49d3ec25`.
- Pilot target: `20.71.90.212` (`hmgweb` self-hosted runner), Ubuntu 24.04.
- Transport/execution evidence: `Yaserbayad/erp.hmg.test`, workflow commit `03fc53cb5a030ce3534ede429a19123a28a27bbd`, Actions run `33969593425`, job `101315631105`.

## Release identity

The deployment recorded the following source-bound release identity:

- Source version: `efe9d4d885d6057b18c5fddea5a0dd2d49d3ec25`.
- Web/runtime configuration version: the immutable deployment/configuration set at that source commit, including `infrastructure/web-server/deploy-release.sh`, `usesafeweb-web.service`, `website.env.example`, `validate-runtime.mjs`, `website/.nvmrc`, `website/package.json`, and the deployed Nginx upstream `127.0.0.1:3100`.
- Content version: `instructions-2026-09-02` from `website/src/content/content-release.json`; source catalogue version `1.0.1-post-cr0007`, catalogue blob `79753cc4916d38ed8d2f0ed6d01890e62df3fb04`, instruction-bindings blob `32441b56f5b2daf2c9924584685fd35fb416438e`.
- Filter-policy version: `1.0.0`, status `active-baseline`, from `infrastructure/adguard-server/filter-policy-v1.yaml` (blob `333a4ef8cd34719d66056aa608ab19473f839634`). The approved AdGuard bundle records `VERSION=1.0.0` in `infrastructure/adguard-server/tsk-0413-bundle-v1/VERSION` (blob `3eefcb9dd5b38e2c1dc061052455dd97bcd51e6c`). This web-host deployment did not mutate the DNS filter host; these values are recorded as the source-bound filter identity carried by the release.

## Environment and service authority

- Required isolated runtime: Node `22.23.2`, npm `10.9.8`.
- Official Node archive: `node-v22.23.2-linux-x64.tar.xz`, SHA-256 `d60acfe00a2932254bb0ad20e01b0d74397a0875595de719654b214f4b03f307`; archive verification passed before use.
- Isolated runtime path: `/opt/usesafeweb-runtime/node-v22.23.2-linux-x64`.
- Existing system Node remained `v24.18.0`; system npm remained `10.9.8` before and after deployment.
- Runtime environment: `/etc/usesafeweb/website.env`, `root:root`, mode `0600`.
- Service: `usesafeweb-web.service`, active, with isolated-Node systemd override; hardening verified `User=usesafeweb-web`, `NoNewPrivileges=yes`, `ProtectSystem=strict`.
- Application listener: exactly `127.0.0.1:3100`; no public application listener was introduced.
- Nginx is the public TLS owner and proxies the UseSafeWeb vhost to `127.0.0.1:3100`.

## Validation, readiness and security

The successful workflow run performed the canonical install/build/deploy path and recorded:

- `npm ci --ignore-scripts` completed.
- Full `npm run validate` completed.
- Contract/integration validation: `117/117` tests passed.
- Type/build/lint/style validation passed; Next standalone build completed.
- Release identity, pre-start and runtime validators passed.
- Service restart and direct readiness passed at `127.0.0.1:3100/api/health/ready`.
- Local Nginx HTTPS health passed after verified Nginx worker-generation rollover.
- Public `https://usesafeweb.com/api/health/ready` passed with TLS verification.
- Fail-closed negative validation passed: an invalid `NODE_ENV=development` runtime configuration was rejected with the expected failure code (`78`).
- No system Node replacement occurred.

## Failure-path and rollback proof

- Earlier deployment run `33969374417` encountered a transient old-worker Nginx `502` immediately after reload. Its failure trap restored the prior Nginx configuration and cleaned the first-deployment application state. Follow-up diagnostics (`33969505547`, `33969536020`) established asynchronous Nginx worker rollover as the cause rather than an application crash or wrong Nginx service.
- Successful run `33969593425` corrected the gate by waiting for Nginx worker-generation change before health verification.
- A live rollback drill in the successful run stopped the application, restored the immediately previous Nginx upstream (`127.0.0.1:3000`), waited for worker rollover, observed the previous-state `502`, then restored the deployed upstream (`127.0.0.1:3100`), restarted the service, waited for worker rollover, and reverified local and public HTTPS health.
- Rollback backup retained on target: `/etc/usesafeweb/node_usesafeweb.conf.pre-tsk0452-v3.33969593425`.
- Final recorded state: service active, Nginx upstream `127.0.0.1:3100`, public readiness healthy.

## Protected snapshots and secret handling

- The deployment and rollback workflow mutation surface is limited to the isolated web runtime, application release/current link, runtime environment file, systemd service/drop-in, and UseSafeWeb Nginx vhost configuration.
- It contains no production data-disk snapshot deletion, retention, deactivation, or rollback command. Therefore automated rollback/retention did not remove or deactivate BTS-P11-D053 production data-disk protection snapshots.
- The DNS verification signing secret was generated on the target with `openssl rand`, stored only in the root-owned mode-`0600` runtime environment file, and its value was not printed into the workflow log, repository, or this evidence artifact.
- No credential, token, private key, or runtime secret value is recorded here.

## Acceptance mapping

- `EVL-0452-D01`: dependency/source/target chain verified by checkpoint, immutable source SHA and successful host preflight.
- `EVL-0452-A01`: target `20.71.90.212`, Ubuntu 24.04, approved self-hosted runner authority and source SHA recorded.
- `EVL-0452-A02`: source/config/content/filter identities recorded above.
- `EVL-0452-A03`: isolated runtime, service owner, environment permissions and executing command boundary verified.
- `EVL-0452-B01`: full validation/build/readiness record in Actions run `33969593425`, job `101315631105`.
- `EVL-0452-B02`: listener, systemd hardening, TLS path and unchanged system runtime verified.
- `EVL-0452-B03`: previous-state rollback target/result and protected-snapshot non-interference verified.
- `EVL-0452-C01`: generated runtime secret remained outside Git/log/evidence; runtime configuration was root-owned `0600`.
- `EVL-0452-S01`: failed-health rollback behavior proved by run `33969374417`; corrected successful path and live rollback proved by run `33969593425`.

## Result

`ACC-0452` is satisfied by durable/reconstructable evidence. The pilot deployment is healthy at source `efe9d4d885d6057b18c5fddea5a0dd2d49d3ec25`, and the rollback path was exercised and restored to the healthy deployed state.
