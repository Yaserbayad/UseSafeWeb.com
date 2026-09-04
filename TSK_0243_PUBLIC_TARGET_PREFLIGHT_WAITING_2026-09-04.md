# TSK-0243 — Public target preflight and WAITING evidence — 2026-09-04

**Task:** TSK-0243 — Implement privacy-safe DNS protection verification  
**Acceptance:** ACC-0243  
**Verification:** VER-0243  
**Evidence:** EVD-0243  
**Disposition:** **WAITING — public verifier trust boundary is not externally routable; TSK-0243 is not PASS.**  
**Canonical basis:** `main@ef1efc463bd45e6773776ff3475f321888106d48`  
**WBS blob:** `142a0d45b381136567d78545f063333f1e74901f`

## Existing accepted partial evidence

The prior isolated target proof remains valid and unchanged:

- exact source head `5a60d95197948d5d46f96224765345e10c73dcde`;
- GitHub Actions run/job `33888891780 / 101075410406` — SUCCESS;
- DNS rewrite, TLS host authentication, signed-result validation, wrong-origin/tamper fail-closed behavior, real-browser `working / protected/verified` mapping, rate limiting, query-history-storage absence, public false-positive guard, live-AdGuard unchanged guard, and complete disposable teardown all passed;
- durable record: `TSK_0243_ISOLATED_TARGET_PARTIAL_EVIDENCE_2026-09-04.md`;
- disposition remains `PARTIAL_TARGET_EVIDENCE_ONLY` because that proof did not traverse the real public DNS/TLS/proxy/network boundary.

## Exact-current external preflight

Read-only diagnostic branch: `verify/tsk0243-public-preflight-20260904`  
Exact diagnostic head: `8f2bae96a137e5b62eb6c2ac6409b607000f89d2`  
GitHub Actions run/job: `33900198638 / 101112216583` — **SUCCESS**.  
Runner: GitHub-hosted Ubuntu 24.04.4 in Azure `westus3`.  
Permissions: repository contents read only; checkout persisted no credentials.  
Target mutation: **NONE**.

The preflight was intentionally non-mutating. It performed DNS lookups, ordinary TLS handshakes, and GET requests only. It did not issue a DNS-verification request/probe/result POST, did not change DNS/proxy/certificate/AdGuard configuration, and did not activate any participant or product runtime.

Observed public state:

- `usesafeweb.com` resolves to `20.71.90.212`.
- `www.usesafeweb.com` aliases to `usesafeweb.com`.
- `dns.usesafeweb.com` resolves to `52.157.109.120`.
- `verify.usesafeweb.com` has no A/AAAA/CNAME result.
- synthetic challenge host `0123456789abcdef0123456789abcdef.verify.usesafeweb.com` has no A/AAAA/CNAME result.
- authoritative NS observed: `haley.ns.cloudflare.com` and `devin.ns.cloudflare.com`.
- `https://usesafeweb.com/` returned HTTP `502` from the external runner.
- read-only GET to `https://usesafeweb.com/api/dns-verification/requests` also returned HTTP `502`.
- read-only GET to `https://dns.usesafeweb.com/dns-query` returned HTTP `400`, confirming the HTTPS DoH surface is reachable without sending a DNS query.
- TLS handshake for `usesafeweb.com:443` passed with certificate verification OK.
- TLS handshake for `dns.usesafeweb.com:443` passed with certificate verification OK.
- TLS handshake for `dns.usesafeweb.com:853` passed with certificate verification OK.
- the challenge verification host could not be reached because it does not resolve publicly.

The workflow emitted:

- `TSK0243_PUBLIC_DNS_SERVICE_HOST=PRESENT`;
- `TSK0243_PUBLIC_VERIFICATION_WILDCARD=ABSENT`;
- `TSK0243_PUBLIC_TRUST_BOUNDARY_PREFLIGHT=NOT_DEPLOYED_OR_NOT_EXTERNALLY_ROUTABLE`;
- `TSK0243_PUBLIC_PREFLIGHT_MUTATION=NONE`;
- `TSK0243_PARTICIPANT_PAYMENT_LAUNCH_ACTION=NONE`;
- `TSK0243_PUBLIC_PREFLIGHT=PASS`.

## Acceptance disposition

`ACC-0243 / VER-0243 / EVD-0243` are **not complete**. The isolated proof demonstrates the verification implementation and target-like behavior, while the new public preflight proves that the remaining externally routed target boundary is presently unavailable.

The task cannot honestly execute its required target-environment functional/negative/configuration/security/privacy/rollback verification across the real public verifier route because `*.verify.usesafeweb.com` is not externally routable and the public web origin is currently unhealthy (`502`). Creating or changing the required public DNS/TLS/proxy/application route would cross the preserved deployment/material-action fence and is not authorized by this evidence action.

## Deterministic WAITING condition

TSK-0243 is WAITING for a separately authorized target deployment/configuration outcome that makes the real verification path observable without the governor itself crossing the deployment fence. The minimum observable resume condition is:

1. a 32-hex challenge host under `*.verify.usesafeweb.com` resolves externally through public DNS;
2. that challenge host presents the approved TLS/proxy path for `/api/dns-verification/probes`;
3. the public application origin needed for `/api/dns-verification/requests` and `/api/dns-verification/results` is healthy and externally reachable; and
4. the change has its own required deployment/configuration authority and evidence.

Deterministic recheck: rerun the bounded read-only public preflight from an external GitHub-hosted runner. Only after those routing prerequisites pass may a separate authorized functional proof exercise the complete request -> public DNS rewrite -> TLS probe -> signed result -> Protection Map path.

## Preserved boundaries

- TSK-0243 is **WAITING**, not PASS.
- No WBS/dependency/gate/acceptance/verification/interface/requirement semantics are changed.
- CON-0007 and CON-0008 remain controlling: persistent identifiable query logging/file logging and identifiable per-client statistics remain off/excluded.
- No real participant was activated or processed.
- No deployment, public DNS/proxy/certificate/profile/service mutation, AdGuard mutation, payment, telemetry activation, market activation, or launch occurred or is authorized by this record.
