# TSK-0375 — Minimal intake routing implementation acceptance evidence

**Date:** 2026-09-03
**Task:** TSK-0375 — Implement minimal intake validation and routing engine
**Lifecycle / authority:** L6 / MEDIUM / A3 / `AUTO_ALLOWED`
**Hard predecessor:** TSK-0358 PASS
**Result:** PASS evidence complete for the current TSK-0375 acceptance contract.

## Canonical implementation

- Pull request: #76 — `TSK-0375: implement minimal intake routing engine`.
- Accepted feature head: `b08d77d042dbf46f530aaef335c083b890ba71fe`.
- Canonical squash merge: `fa4e2917ec8aef93302a36708064019277bbfa6b`.
- Intake-routing blob: `ac718dd21f6c7fc7c0af6e45a4e73f49a3eb75d5`.
- Contract-test blob: `383db75a9a422fba68dcd2811fe817f318e2edf2`.
- Browser-test blob: `067c08ccd82d3485966f05b11c016aa542e6e449`.
- Acceptance-workflow blob: `88884a7e871196bfba5fc876ba7d6b9cf4d5b71b`.
- Production locale validation uses canonical `website/src/lib/i18n.ts`; no duplicated locale list remains in the routing engine or TSK-0375 acceptance layers.

## Direct acceptance evidence

| Evidence | Run / job | Result |
| --- | --- | --- |
| Exact feature-head acceptance | `33723799253` / `100548279575` | SUCCESS |
| Canonical clean-main acceptance | `33724093783` / `100549157999` | SUCCESS |
| Clean-main TSK-0359 regression | `33724093699` | SUCCESS |
| Clean-main TSK-0360 source regression | `33724093742` | SUCCESS |
| Clean-main TSK-0243 regression | `33724093708` | SUCCESS |
| Clean-main TSK-0629 regression | `33724093736` | SUCCESS |

Clean-main TSK-0375 observations: repository structure `183/183` PASS; master-plan validation `0` errors / `0` warnings; contracts `68/68` PASS; lint `0` errors with one inherited non-error React-hooks warning; typecheck PASS; Next.js production build PASS; both dependency audits `0 vulnerabilities`; Playwright `1.62.1`; real Chromium `TSK0375_INTAKE_ROUTING_BROWSER_ACCEPTANCE=PASS`; final `TSK0375_INTAKE_ROUTING_ACCEPTANCE=PASS`; clean git/diff checks PASS.

## ACC-0375 / VER-0375 mapping

1. **Approved combinations are deterministic and tested.** The exact contract accepts only `{choice, locale}`; canonical locales come from `i18n.ts`; Android/iPhone route to native setup and `other` routes to compatibility; contract and browser acceptance cover the approved matrix.
2. **Boundary/error behavior fails closed.** Non-object, array, invalid locale/choice, missing-key, and extra-key inputs are rejected rather than partially routed.
3. **Prohibited data is rejected/not requested.** Extra identity/account, child, domain/query-history, diagnostic, or other unapproved fields fail the exact-key contract; no persistent account/session/history dependency is added.
4. **Unsupported combinations return a clear safe state.** `choice=other` returns `state=unsupported`, no device family, and a locale-scoped compatibility route.
5. **Locale authority is singular.** Production routing imports `isLocale` from `@/lib/i18n`; review removed the duplicated locale list.

## Security, privacy, target environment, and rollback

- No authentication requirement, persistent identity, browsing/query history, raw diagnostic persistence, analytics transport, deployment path, external service, or new sensitive-data category was introduced.
- VER-0375 target evidence is the built Next.js production server exercised by real Chromium on GitHub-hosted Ubuntu; no public/production deployment or participant processing is inferred.
- Malformed/unsupported input cannot manufacture protection/verification state.
- Source rollback is an ordinary revert of merge `fa4e2917ec8aef93302a36708064019277bbfa6b`; TSK-0375 introduced no external runtime side effect.

## Guarded runtime publication

- Starting canonical base: `fa4e2917ec8aef93302a36708064019277bbfa6b`.
- Exact pre-mutation `CURRENT_STATE.md` blob: `ab864134cbe38408e10f4e05c3f1352fa97e9d5f`, `481601` bytes.
- Guarded synchronization run: `33728153747`.
- The guard proves every pre-existing state byte remains identical except the one existing `Updated` timestamp line; one TSK-0375 section is appended. No whole-file reconstruction is used.

## Preserved unresolved fences

- TSK-0360 remains TODO pending required supported-iPhone/device/deployment ACC/VER/EVD evidence.
- TSK-0455 remains WAITING for a genuinely qualifying fresh Ubuntu 24.04 LTS target host and required access/evidence.
- TSK-0399 remains ineligible while TSK-0360 is non-PASS.
- No deployment, configuration-profile distribution, participant processing, runtime activation, market activation, launch, downstream task/gate PASS, or `GATE-0026` is created or inferred.
