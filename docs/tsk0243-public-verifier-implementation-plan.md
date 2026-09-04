# TSK-0243 Public Verifier Repository Implementation Plan

> **Execution:** Inline in this governed session. Each task uses a failing focused test where behavior is executable, then the minimum implementation, focused verification, regression verification, and an atomic commit.

**Goal:** Make the existing privacy-safe DNS verification protocol deploy-ready without performing any live deployment, DNS, certificate, proxy, AdGuard, participant, telemetry, payment, activation, or launch action.

**Architecture:** Keep the existing Next.js request/probe/result proof flow and add a direct-host release boundary around it. Nginx is the only public challenge-host entry point, AdGuard Home v0.107.79 supplies a narrowly rendered private DNS rewrite, and all secrets/certificates/addresses remain external inputs validated fail-closed. Local integration uses synthetic secrets, an ephemeral CA/certificate, isolated DNS behavior, and loopback services only.

**Tech stack:** Node.js 22.23.2, npm 10.9.8, Next.js 16.3.3, TypeScript, Nginx, systemd, Bash/Python standard libraries, AdGuard Home v0.107.79/schema 34.

## Global constraints

- Preserve the 32-lowercase-hex challenge, `verify.usesafeweb.com` suffix, exact Host/public-Origin checks, HMAC separation, 120-second bounds, and no-persistence behavior.
- Do not edit planning/governance authority or `CURRENT_STATE.md`.
- Do not perform target deployment or any live/material action.
- Do not commit secrets, private keys, certificates, target addresses, or credential URLs.
- Ordinary public DNS must remain unable to manufacture a positive verification observation.
- CI remains GitHub-hosted, `contents: read`, credential-less checkout, and free of deployment authority or external side effects.

## Task 1: Runtime readiness and secret boundary

**Files:**

- Create `website/src/lib/runtime-config.ts` for exact server-only runtime validation.
- Create `website/src/app/api/health/ready/route.ts` for deterministic no-store readiness.
- Modify `website/next.config.ts` to emit standalone production output.
- Create `infrastructure/web-server/usesafeweb-web.service` and `infrastructure/web-server/website.env.example`.
- Create `infrastructure/web-server/validate-runtime.mjs` and `infrastructure/web-server/deploy-release.sh`.
- Test in `website/tests/contract/tsk0243-deployment.test.mjs`.

**Interfaces:** `readServerRuntimeConfig(env)` accepts a server environment mapping and returns validated public origin/signing-secret configuration without exposing the secret. The readiness route returns only status/version markers. The systemd unit consumes `/etc/usesafeweb/website.env`, binds loopback, validates before start, restarts on failure, and never embeds a secret.

- [ ] Add contract tests requiring standalone output, exact Node/npm pins, loopback bind, systemd hardening/restart behavior, external environment file, health behavior, and secret redaction.
- [ ] Run the focused test and confirm RED on missing artifacts.
- [ ] Implement the minimum runtime config, readiness route, service, validator, and atomic release script.
- [ ] Run focused tests, typecheck, and production build until GREEN.
- [ ] Inspect staged diff for secret material and commit `feat: add fail-closed website runtime packaging`.

## Task 2: Nginx challenge-host and TLS boundary

**Files:**

- Create `infrastructure/web-server/nginx/usesafeweb-verifier.conf.template`.
- Create `infrastructure/web-server/render-nginx-config.sh`.
- Create `infrastructure/web-server/verify-nginx-config.py`.
- Test in `tests/tsk0243/test_verifier_package.py`.

**Interfaces:** Renderer requires explicit public origin, loopback app upstream, wildcard certificate, and private-key paths; validates readable certificate material and exact wildcard SAN before producing configuration. Nginx accepts only case-sensitive `^[0-9a-f]{32}\.verify\.usesafeweb\.com$`, only HTTPS, and only exact POST `/api/dns-verification/probes`; the default TLS server rejects handshakes.

- [ ] Add negative tests for malformed/uppercase/arbitrary/direct-IP hosts, unrelated paths, body/time limits, logging prohibition, and fallback signer prevention.
- [ ] Run the focused test and confirm RED.
- [ ] Implement the template, renderer, and verifier with fail-closed TLS checks and rate/request limits.
- [ ] Run focused tests and syntax/static verification until GREEN.
- [ ] Commit `feat: add restricted challenge-host proxy boundary`.

## Task 3: Versioned private AdGuard rewrite overlay

**Files:**

- Create `infrastructure/adguard-server/tsk-0243-verifier-rewrite-v1/template.txt`.
- Create `infrastructure/adguard-server/tsk-0243-verifier-rewrite-v1/render.py`.
- Create `infrastructure/adguard-server/tsk-0243-verifier-rewrite-v1/apply.sh`.
- Create `infrastructure/adguard-server/tsk-0243-verifier-rewrite-v1/README.md` and `VERSION`.
- Extend `tests/tsk0243/test_verifier_package.py`.

**Interfaces:** Renderer accepts one explicit verifier IPv4 address and emits one AdGuard custom-filter rule matching only `[0-9a-f]{32}.verify.usesafeweb.com`, using v0.107.79-supported `$dnsrewrite=NOERROR;A;...`. Apply mode preserves all unrelated user rules and settings, supports verify/apply/remove, requires the pinned target version, uses authenticated loopback control, and rolls back on failed validation.

- [ ] Add RED tests for missing/invalid address, broader wildcard, suffix spillover, privacy-setting changes, missing rewrite, and reversible idempotent removal.
- [ ] Implement renderer and guarded apply/remove pipeline without changing TSK-0413 privacy/upstream/filter fields.
- [ ] Run local rule tests and the current TSK-0413 bundle verifier.
- [ ] Commit `feat: add private verifier DNS rewrite overlay`.

## Task 4: Trust-boundary integration harness

**Files:**

- Create `tests/tsk0243/run_trust_boundary.py` and supporting local fixtures under `tests/tsk0243/fixtures/` only if required.
- Extend `website/package.json` with focused deployment/integration commands.
- Extend `tests/tsk0243/test_verifier_package.py`.

**Interfaces:** Harness generates a temporary secret and CA/wildcard certificate, starts the built Next.js server and an HTTPS challenge proxy on loopback, models private rewrite success and ordinary-DNS failure, and drives request → probe → result with synthetic scope. It records only PASS/FAIL markers and removes all temporary proof/certificate material.

- [ ] Add RED contract assertions for the missing harness and required positive/negative markers.
- [ ] Implement the smallest localhost-only harness covering valid flow, wrong host/origin/path/content-type/body, tamper, stale/replay/conflict, unavailable DNS/proxy, and no-storage assertions.
- [ ] Run the harness twice to prove teardown/rebuild determinism.
- [ ] Commit `test: add ephemeral verifier trust-boundary harness`.

## Task 5: External preflight, functional proof, and operator runbook

**Files:**

- Create `infrastructure/web-server/tsk0243-acceptance.py`.
- Create `infrastructure/web-server/README.md`.
- Extend `tests/tsk0243/test_verifier_package.py`.

**Interfaces:** Default mode is read-only GET/DNS/TLS inspection and expects ordinary public DNS negative behavior. Functional POSTs require `--functional --authority-token TSK-0243-TARGET-PROOF`; output redacts tokens by default and uses stable boundary-specific exit codes. The runbook covers inputs, deployment, health, DNS overlay, wildcard DNS-01 certificate handoff, renewal, rotation, rollback/removal, and prohibited logs/data.

- [ ] Add RED tests proving functional mode cannot run without the explicit authority token and output never exposes synthetic secrets/tokens.
- [ ] Implement read-only and gated functional modes with deterministic exit codes.
- [ ] Document source/version values resolved from Git at execution, external inputs, startup, target proof, rotation, rollback/removal, and remaining target-only evidence.
- [ ] Run focused tests and commit `docs: add verifier deployment and acceptance runbook`.

## Task 6: CI integration and final verification

**Files:**

- Modify `website/package.json` only as required to include new contract commands.
- Modify `.github/scripts/tsk0489-governed-ci.sh` to execute the repository-only TSK-0243 package and integration checks if runtime permits.
- Modify `.github/workflows/accept-tsk0489-governed-ci-promotion-20260904.yml` only if additional runner packages are strictly required.

- [ ] Add/extend governance contract assertions before changing CI.
- [ ] Run repository structure and master-plan validation.
- [ ] Run complete website contracts, format check, lint, typecheck, production build, SBOM, full/production dependency audits, TSK-0453, TSK-0491, TSK-0489 workflow-governance, and the ephemeral trust-boundary test.
- [ ] Run `git diff --check`, secret scans, and confirm no generated artifacts remain.
- [ ] Request an independent code review; fix all critical/important findings test-first.
- [ ] Commit final CI integration, push the branch, open one PR, and wait for every applicable check on the exact final head.
- [ ] Diagnose/fix failures and repeat until the final source SHA is green; do not merge.
