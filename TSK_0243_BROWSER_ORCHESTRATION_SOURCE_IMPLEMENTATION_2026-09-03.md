# TSK-0243 — Browser orchestration source implementation

**Task:** `TSK-0243 — Implement privacy-safe DNS protection verification`  
**Acceptance:** `ACC-0243 / VER-0243 / EVD-0243`  
**Lifecycle / authority:** L6 / A3 / `AUTO_ALLOWED`  
**Date:** 2026-09-03  
**Status:** **PARTIAL SOURCE IMPLEMENTATION / TODO — NOT PASS**  
**Canonical base:** `main` at `4c0dcdc5ab18291b68bbf1c2276110432885a16f`  
**Accepted feature head before this evidence note:** `795c462c70b95a338333d6e524c2e8b5f6371125`

## 1. Scope completed

This slice completes the browser/product orchestration for the already integrated TSK-0243 proof/request/probe source interfaces without deploying or activating any target DNS, TLS, proxy, web-production, participant, market, profile-distribution, or production-runtime state.

The source now provides:

1. a browser `request -> dedicated probe -> server result verification` flow from the existing anonymous 128-bit journey scope;
2. a same-origin result endpoint accepting only bounded `{requestToken, observationToken}` input;
3. server-side verification of the signed request token first, with expected `scope` and `challenge` derived from that trusted token rather than browser-supplied correlation fields;
4. server-side verification of the observation token against the derived current scope/challenge;
5. browser receipt of only the approved `{dnsPath, reasonCode, verifierVersion}` projection;
6. exact semantic validation of accepted `dnsPath / reasonCode` pairs;
7. fresh verification on both Verify and Protection Map surfaces, including a fresh check after Protection Map reload;
8. fail-closed behavior for malformed input, invalid origin/host, network/status/schema/timeout/result-verification failure, unsupported or contradictory evidence;
9. zero persistence of DNS verification challenge, request token, observation token, verification host, or proof bundle in `sessionStorage` or `localStorage`;
10. no URL/query parameter capable of manufacturing a positive technical-verification state;
11. current controlled recovery navigation using the existing typed `data-core-troubleshoot` marker.

Primary source artifacts in this slice include:

- `website/src/lib/dns-verification-browser.ts`
- `website/src/app/api/dns-verification/results/route.ts`
- `website/src/components/dns-verification-panel.tsx`
- `website/src/components/dns-verification-card.tsx`
- updated Verify and Protection Map pages
- contract and real-browser acceptance coverage

Only a fresh server-verified `verified-fresh / TECH_VERIFIED` result can feed the existing TSK-0629 classifier. Configuration presence, parent confirmation, URL input, account state, previous page state, or stored proof material cannot manufacture a current positive result.

## 2. TDD / review / verification evidence

### Interrupted branch recovery

The pre-existing interrupted branch was reconciled instead of overwritten. Its earlier run `33714970120 / 100522112351` proved all 63 contracts but failed TypeScript because `dns-verification-panel.tsx` used an invented `data-core-verify-recovery` marker outside the typed `CoreActionButton` contract. The source was corrected to the existing `data-core-troubleshoot` marker.

### Privacy/correctness review RED

Pre-merge review then found a more material defect: the interrupted implementation persisted `{challenge, observationToken}` in `sessionStorage` so Protection Map could restore a prior positive proof across navigation. That contradicted the current TSK-0243 privacy-minimal/transient-proof boundary.

A regression-first change required zero persisted proof material and fresh checks on both Verify and Protection surfaces.

- RED run `33716532441 / 100526779886`: **58/63 PASS, 5 FAIL** exactly on the new no-persistence/server-correlation/current-marker assertions.
- The failures proved the old code still returned a stored proof bundle, exported proof-storage helpers, accepted raw scope/challenge at the result route, used proof-storage functions in the UI, and retained one obsolete recovery-marker expectation.

### GREEN source behavior

The implementation was changed so the result route derives correlation from the signed request token, browser proof material remains transient in memory only, and Verify/Protection each perform a fresh check.

Initial corrected GREEN:

- run `33716803122 / 100527579820`: **SUCCESS** on exact head `642c49ae225628c3f09b4e1e2c4ff2f296470a67`;
- 63/63 contracts PASS;
- repository-structure and modular Master Plan validation PASS;
- ESLint 0 errors with the inherited `_accountState` unused-variable warning only;
- Next/TypeScript type-check PASS;
- Next.js 16.3.3 production build PASS with 58/58 static pages generated where applicable;
- `npm audit --audit-level=high`: 0 vulnerabilities;
- `npm audit --omit=dev --audit-level=high`: 0 vulnerabilities;
- `TSK0243_LOCAL_HTTP_VERIFIER_ACCEPTANCE=PASS`;
- `TSK0243_BROWSER_ORCHESTRATION_ACCEPTANCE=PASS`.

### CI-tool hardening

The initial GREEN run used ephemeral `playwright@1.55.0`, whose temporary install reported one high-severity dependency vulnerability even though committed production/all dependency audits were clean. The browser acceptance tooling was therefore updated to current Playwright `1.62.1` before integration.

Final pre-evidence head acceptance:

- run `33716955367 / 100528044267`: **SUCCESS** on exact head `795c462c70b95a338333d6e524c2e8b5f6371125`;
- 63/63 contracts PASS;
- repository/master-plan validators PASS — 641 tasks, 858 dependency edges, 4,587 relationship entities, 18,152 relationship targets, 0 broken links, 0 generated missing task IDs;
- ESLint 0 errors with one inherited `_accountState` warning;
- type-check PASS;
- Next.js 16.3.3 production build PASS, 58/58 static pages generated where applicable;
- committed dependency audits: 0 vulnerabilities for all and production-only dependencies;
- ephemeral Playwright 1.62.1 install: 0 vulnerabilities;
- `TSK0243_LOCAL_HTTP_VERIFIER_ACCEPTANCE=PASS`;
- `TSK0243_BROWSER_ORCHESTRATION_ACCEPTANCE=PASS` using Playwright 1.62.1 / Chrome for Testing 151.0.7922.34.

## 3. Authoritative technical-source basis

- Next.js Route Handlers use standard Web `Request`/`Response` APIs: https://nextjs.org/docs/app/getting-started/route-handlers-and-middleware
- Browser `fetch()` and `AbortController` are the platform primitives used for bounded network requests and cancellation: https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch and https://developer.mozilla.org/en-US/docs/Web/API/AbortController
- Playwright current release documentation: https://playwright.dev/docs/release-notes
- Playwright browser-management guidance: https://playwright.dev/docs/browsers

These sources support the source implementation and CI/browser tooling only. They do not prove the target UseSafeWeb DNS/TLS/network path exists or works.

## 4. Acceptance still missing — why TSK-0243 remains TODO

Current `ACC-0243 / VER-0243 / EVD-0243` is not complete. Target-environment evidence still must prove at least:

1. `*.verify.usesafeweb.com` resolves/reaches the positive signer only through the intended UseSafeWeb DNS path;
2. the same random probe hostname does not false-positive through an ordinary/public resolver path;
3. TLS authenticates the random challenge hostname and the target verifier endpoint;
4. reverse-proxy/network controls prevent direct positive-signer invocation through forged `Origin`, `Host`, or equivalent bypasses;
5. the signing key is injected only into the intended trusted service, remains outside Git/log/evidence/client state, and has an approved rotation/recovery path;
6. actual target rate/abuse controls work at the externally reachable interface;
7. the deployed product/browser request -> probe -> observation -> result -> Protection Map path works against the real intended DNS/TLS route;
8. negative, timeout, DNS/TLS failure, replay, wrong-host, wrong-origin, malformed and conflicting cases fail closed in the deployed target;
9. runtime/event/storage/network inspection proves no prohibited browsing/query history, raw DNS history, unnecessary identity, client IP persistence, challenge/proof persistence, or signing secret leakage;
10. exact target configuration/version and rollback/removal are tested and recorded under current VER-0243 / EVD-0243.

Source/CI checks of `Origin`, `Host`, signed tokens and loopback routing are controls and useful evidence, but they cannot establish real network-path authenticity or public-resolver behavior.

## 5. Preserved fences / stable disposition

- `TSK-0243` remains **TODO**, not PASS.
- `TSK-0359` remains durable PASS and is not rewritten or reopened.
- `TSK-0629` remains TODO until a trusted deployed fresh DNS-path producer is evidenced end-to-end.
- `TSK-0360` remains TODO.
- `TSK-0455` remains WAITING for the genuinely qualifying owner-provided fresh Ubuntu 24.04 LTS target host/access required by its contract.
- `TSK-0399` remains ineligible while `TSK-0360` is non-PASS.
- No `GATE-0026` exists or is created.
- No DNS rewrite/record, TLS certificate, reverse-proxy/runtime configuration, deployed signing secret, web deployment, profile distribution, production/runtime activation, participant processing, market activation, payment, launch, or unrelated task/gate PASS is inferred or performed.

This browser-orchestration slice is suitable for source integration as durable partial TSK-0243 work. It must not advance TSK-0243 to PASS until the missing target evidence above is produced and independently verified.