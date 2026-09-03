# TSK-0243 — Verifier request/probe interface source implementation

**Task:** `TSK-0243 — Implement privacy-safe DNS protection verification`  
**Acceptance:** `ACC-0243 / VER-0243 / EVD-0243`  
**Lifecycle / authority:** L6 / A3 / `AUTO_ALLOWED`  
**Date:** 2026-09-03  
**Status:** **PARTIAL SOURCE IMPLEMENTATION / TODO — NOT PASS**  
**Canonical base:** `main` at `c8fb700cbe76355bad5f2f910f7169de9712250b`  
**Verified source head before this evidence update:** `cbaa9c663446e8303045626ccb5397d815077dec`

## 1. Scope completed

This slice adds the server-side request/probe interface needed to consume the previously accepted TSK-0243 proof contract. It is source-only. It does not create or mutate any DNS record/rewrite, TLS certificate, reverse-proxy route, deployed signing secret, external environment, profile distribution, user/participant state, market state, or production activation.

Current source artifacts at the accepted source head include:

- `website/src/lib/dns-verification-proof.ts` — blob `470095e20ee7a51ec06ea02fc561743a78cb5012`
- `website/src/lib/bounded-request-body.ts` — blob `37a56b8a1853aa2fb5dcd8bffdc9a2c48be17ed9`
- `website/src/app/api/dns-verification/requests/route.ts` — blob `327a7a8a743e959382c9fc5110185ff81007c0bb`
- `website/src/app/api/dns-verification/probes/route.ts` — blob `4bf11a4e78260b495f305fbfeb00382af107d7be`
- `website/next.config.ts` — blob `540a2442651bd713a9c0abe00166857a0614b3b4`
- `.github/workflows/accept-tsk0243-dns-verification-20260903.yml` — blob `5b707a516e68a9cd85be4d4da9f9987484a6a0cc`

The source now provides:

1. **domain-separated server-issued probe-request tokens** under protocol `usesafeweb-dns-probe-request-v1`;
2. server-generated CSPRNG 128-bit challenges, so callers cannot select the current verification challenge;
3. exact request binding to anonymous scope, challenge, issue time and a maximum 120-second expiry;
4. a same-origin request-issuance route that accepts only the exact `{ scope }` JSON shape and returns no-store responses;
5. a cross-origin probe route that accepts an opaque text token and derives a positive observation only from a valid signed request token plus the actual request `Host` matching the current challenge hostname;
6. no client-selected `outcome`, `reasonCode`, `challenge` or `probeHost` input on the positive-signing route;
7. a configured exact HTTPS public-origin check and explicit single-origin CORS response with `Vary: Origin`;
8. a narrow CSP `connect-src` allowance for only `https://*.verify.usesafeweb.com`, not `*.usesafeweb.com` generally;
9. a shared streaming request-body reader that enforces the 4,096-byte boundary while reading, including chunked/missing/lying `Content-Length` cases, and rejects malformed UTF-8;
10. server-only signing-secret lookup through `USESAFEWEB_DNS_VERIFICATION_SIGNING_SECRET`, requiring at least 32 bytes and emitting no secret value in responses/tests/evidence;
11. Node Route Handler runtime and POST-only application methods for the two verifier interfaces; no application GET/PUT/PATCH/DELETE route is implemented;
12. structured fail-closed 4xx/503 responses and no-store caching behavior;
13. a CI-local production-server HTTP acceptance that exercises the built handlers without any external DNS/TLS/runtime mutation.

## 2. TDD, review and correction evidence

### Interface contract RED

The first interface contract intentionally failed before implementation. The design was then corrected before GREEN because a JSON cross-origin probe POST would require a CORS preflight and conflict with the intended POST-only verifier interface.

- initial pre-correction RED run/job: `33712594737 / 100515054748`;
- corrected CORS-safe interface RED run/job: `33712688683 / 100515337391` — existing 48 contracts passed; exactly three new interface behaviors failed because probe-request functions/routes did not yet exist.

### Initial interface GREEN

- run/job `33712792241 / 100515650856`: **SUCCESS** on source head `3f15bf624dd2abe93d36f3b2dffefc7e4d199c9e`;
- 51/51 contracts PASS;
- repository/master-plan validators PASS;
- lint 0 errors with the inherited `_accountState` warning;
- type-check and production build PASS;
- both dependency audits report 0 vulnerabilities.

### CSP integration review

Review found that the existing `connect-src 'self'` policy would block the browser from calling the random verification subdomain.

- CSP RED run/job `33712932609 / 100516062008`: 51/52 tests passed; only the missing dedicated verification `connect-src` allowance failed.
- run `33713028525 / 100516347282` then exposed an **over-broad regression assertion** that rejected the dedicated wildcard it had just required. This was a test defect, not a product defect; the assertion was corrected to require `https://*.verify.usesafeweb.com` while rejecting broad `https://*.usesafeweb.com` and generic wildcard connectivity.
- the product CSP change remains one narrow source expression: `connect-src 'self' https://*.verify.usesafeweb.com`.

### Streaming-body security review

Review found a real resource-boundary defect: the initial routes called `request.text()` before validating the actual received body size when `Content-Length` was absent or false, allowing an untrusted chunked body to be buffered before rejection.

- streaming RED run/job `33713186793 / 100516820380`: the corrected CSP regression passed; exactly four streaming-boundary assertions failed because the bounded reader did not exist and the two routes still used whole-body buffering.
- source GREEN run/job `33713306518 / 100517177903`: **SUCCESS** on exact source head `643b92a5f053279fc17de99df1e765809451f55d`.

### Evidence-inclusive source gate

- run `33713501803`: **SUCCESS** on evidence-bearing head `bb3fa6ec30c826fd998e25899f23a6441627c563` before the local HTTP acceptance was added.

### CI-local production HTTP acceptance

A final review improvement added actual local HTTP execution of the built Next production server while remaining entirely inside the disposable GitHub Actions runner.

- run/job `33713591139 / 100518017563`: **SUCCESS** on exact source head `cbaa9c663446e8303045626ccb5397d815077dec`;
- marker `TSK0243_LOCAL_HTTP_VERIFIER_ACCEPTANCE=PASS` was emitted;
- request issuance returned HTTP 201 with `Cache-Control: no-store`, a generated 128-bit challenge and matching probe hostname;
- wrong-origin probe returned HTTP 403;
- wrong-Host probe returned HTTP 403;
- exact current probe Host + configured public Origin + opaque `text/plain` request token returned HTTP 200 with an observation token;
- the accepted probe response included `Cache-Control: no-store`, exact `Access-Control-Allow-Origin: https://usesafeweb.com`, and `Vary: Origin`;
- the first readiness probe briefly saw connection refused before the local Next server was ready; the bounded readiness loop then succeeded and the acceptance completed normally. This is expected startup sequencing, not an application failure.

Final source-head observations on `cbaa9c663446e8303045626ccb5397d815077dec`:

- repository-structure verification: PASS;
- modular Master Plan validation: PASS — 641 tasks, 858 dependency edges, 4,587 relationship entities, 18,152 relationship targets, 0 broken links, 0 generated missing task IDs;
- website contract suite: **56/56 PASS**;
- ESLint: 0 errors; one inherited `_accountState` unused-variable warning in `core-state-machine.ts`;
- Next/TypeScript type-check: PASS;
- Next.js production build: PASS;
- 57/57 static pages generated where applicable; both verifier routes are present as dynamic server routes;
- `npm audit --audit-level=high`: 0 vulnerabilities;
- `npm audit --omit=dev --audit-level=high`: 0 vulnerabilities;
- CI-local verifier HTTP acceptance: PASS;
- `git diff --check`: PASS;
- clean working-tree assertion: PASS.

## 3. Authoritative technical-source basis

Current source behavior was checked against current authoritative documentation:

- Next.js Route Handler API/reference: `https://nextjs.org/docs/app/api-reference/file-conventions/route` — `route.ts` handlers use standard Web `Request`/`Response`, support `POST`, CORS headers, request bodies and `runtime = 'nodejs'`.
- Next.js Backend-for-Frontend guidance: `https://nextjs.org/docs/app/guides/backend-for-frontend` — Route Handlers are externally accessible application endpoints; sensitive data must not be exposed and access boundaries must be implemented explicitly.
- MDN CORS guide: `https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS` — a `POST` with safelisted headers and `text/plain` can qualify as a non-preflighted/simple cross-origin request; an explicit allowed origin should be returned with `Vary: Origin` where response behavior varies by origin.
- MDN `connect-src`: `https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/connect-src` — `connect-src` controls browser `fetch()` and related scripted connections.
- Node.js crypto: `https://nodejs.org/api/crypto.html` — CSPRNG challenge generation, HMAC and timing-safe comparison remain grounded in the accepted first TSK-0243 source slice.
- AdGuard Home configuration/filtering documentation remains the basis for the later target wildcard DNS-rewrite design; no rewrite is implemented by this source slice.

These sources support the source/interface design only. They do not prove the target DNS/TLS/proxy topology exists or that an actual client request reached the positive signer exclusively through the intended UseSafeWeb resolver path.

## 4. Acceptance still missing — why TSK-0243 remains TODO

`VER-0243` still requires target-environment functional, negative, configuration, security/privacy, failure/conflict and rollback evidence. In particular, source code and CI-local HTTP execution cannot establish the key target trust boundary by themselves.

Before TSK-0243 can become PASS, the target environment must independently prove at least:

1. `*.verify.usesafeweb.com` is resolvable/reachable for the approved probe only through the intended UseSafeWeb DNS path and exact approved DNS rewrite/equivalent mechanism;
2. an ordinary/public/non-UseSafeWeb resolver path does not produce a false positive for the same fresh random challenge;
3. TLS authenticates the challenge hostname and the request reaches the intended verifier service with the actual trusted Host preserved;
4. direct/public/reverse-proxy paths cannot invoke the positive signer merely by spoofing `Origin`/`Host` or otherwise bypassing the intended DNS-path boundary; CORS is not treated as an authentication control;
5. the HMAC signing secret is injected only into the intended trusted service, is absent from Git/logs/evidence/client bundles, is minimum-scoped and rotatable;
6. rate/abuse controls and capacity behavior are verified at the actual public/target interface;
7. the real product/browser orchestration issues a request, probes the unique host, consumes the returned observation and maps it through the current TSK-0629 / TSK-0320 state contract without accepting caller-forged evidence;
8. timeout, DNS failure, TLS failure, signer unavailable, malformed, oversized, stale, replayed, wrong-host, wrong-origin, negative and conflicting paths all fail closed and remain recoverable;
9. runtime/event/storage inspection proves no browsing/query/activity history, raw DNS history, persistent client IP, unnecessary identity, secret, request token, challenge or scope is retained in approved product telemetry/history beyond the minimum transient operation;
10. the exact target configuration/version and a tested rollback/removal path are recorded under current `VER-0243 / EVD-0243`.

## 5. Security/trust-boundary limitations

- `Origin`/CORS controls whether conforming browser script can read a cross-origin response; it is **not authentication** and can be spoofed by non-browser clients. The target network/proxy topology must therefore enforce the positive-signer path independently.
- `Host` binding proves that the application received the expected hostname; it does not by itself prove how an arbitrary client resolved or routed that hostname. Target acceptance must prove the DNS/TLS/network path that gives `Host` binding its intended evidentiary meaning.
- The request token is integrity-protected and short-lived but not an encrypted confidentiality token; the random scope remains a correlation value rather than an authorization credential.
- The CI-local HTTP check proves actual built Route Handler behavior on a disposable loopback server only. It is not evidence of deployed DNS resolution, TLS routing, reverse-proxy enforcement, rate limiting or real-device behavior.

## 6. Non-inference / preserved fences

- `TSK-0243` remains **TODO**.
- `TSK-0359` remains durable PASS and is not reopened.
- `TSK-0629` remains TODO until a trusted deployed fresh E1 DNS-path producer is evidenced and integrated end-to-end.
- `TSK-0360` remains TODO pending supported-iPhone and related acceptance evidence.
- `TSK-0455` remains WAITING for a genuinely qualifying owner-provided fresh Ubuntu 24.04 LTS target host/access.
- `TSK-0399` remains ineligible while `TSK-0360` is non-PASS.
- No `GATE-0026` exists or is created.
- No DNS rewrite/record, TLS certificate, reverse-proxy/runtime configuration, deployed signing secret, deployment, profile distribution, production/runtime activation, participant processing, market activation, payment, launch, or unrelated task/gate PASS is inferred or performed.

## 7. Stable outcome

The verifier request/probe **source interface** is implementation-complete for this bounded slice and has passed source-level tests, review, production build and CI-local HTTP execution. It is safe to integrate as durable partial work. TSK-0243 must remain TODO until the target DNS/TLS/proxy trust boundary and end-to-end product path are actually observed and independently accepted.
