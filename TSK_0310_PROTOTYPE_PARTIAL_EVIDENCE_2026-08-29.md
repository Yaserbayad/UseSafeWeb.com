# TSK-0310 — Prototype Partial Verification Evidence

**Task:** TSK-0310 — Build the representative mobile-first public-to-setup prototype before production implementation  
**Date:** 2026-08-29  
**Acceptance:** ACC-0310 — Prototype covers discovery, routing, native safeguard, DNS setup/verification, external service, Protection Map, troubleshooting, recovery/removal, and limitations.  
**Verification:** VER-0310 — Execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria.  
**Disposition:** **INCOMPLETE — TSK-0310 is not PASS.** Source/model verification passed; target-browser execution remains unverified because the available self-hosted runner has no browser runtime.

## 1. Authority and scope

TSK-0310 is an `AUTO_ALLOWED`, provisional internal L4 prototype task under DEC-0051/CR-0004. Its current hard dependencies are TSK-0300, TSK-0317, TSK-0318 and TSK-0320, all previously recorded PASS when TSK-0310 was selected in `CURRENT_STATE.md`.

This evidence does not satisfy representative-parent validation, legal/privacy completion, participant activation, integrated L5/L6 build, public publication/release, payment, market activation or launch. `RSK-0002` remains OPEN and TSK-0187 remains mandatory where required.

## 2. Prototype artifact read-back

GitHub `main` read-back confirms the current prototype package:

| Artifact | Git blob |
| --- | --- |
| `prototype/TSK-0310/model.mjs` | `01343273fd09c3c12d26f0c0eb1ae9a2fce10c91` |
| `prototype/TSK-0310/index.html` | `5d80dfdefb52042bc34468723354fefd325285e4` |
| `prototype/TSK-0310/prototype.css` | `439ef05dd04da7fccf01cb4b85e317a828389edf` |
| `prototype/TSK-0310/app.mjs` | `a4a0aff8848f8541e2581e333efbf48767c9f0ff` |

Implementation commits are `136c4d9b4c9c13dd199ebaaf4f2687a19bdd3ece`, `b05db45726f24d2b7388799df98a1624932d682f`, `092890426eabf48c6cf1798be88a6a801144e0f6`, and `9018c39ac5a4f867fffb16651f2bbf5d0ac17fd9`.

## 3. Verification run 1 — harness environment failure

Temporary read-only verifier commit: `2cb0b6f3e13b438200baac12d1310e4a9e7d947d`.  
GitHub Actions run: `33259227542`; job: `99118182711`.  
Result: **FAIL before prototype assertions** because the self-hosted `adguardvm` runner shell did not have `node` on PATH (`node: command not found`). The browser step was skipped. This is verifier-environment evidence, not a product failure.

The verifier was corrected by adding `actions/setup-node@v4` with Node 22 only; prototype code was not changed.

## 4. Verification run 2 — source/model checks PASS; browser unavailable

Corrected verifier commit: `123fdee8666c3b5bbf15dd316f83637927ca6250`.  
GitHub Actions run: `33259265518`; job: `99118278984`.  
Runner: self-hosted `adguardvm`.  
Node provisioned: `v22.23.2`.

### Source/configuration/security-privacy checks

The source/model step completed **SUCCESS** and printed `MODEL_TESTS=PASS`. It verified:

- JavaScript syntax for `model.mjs` and `app.mjs`;
- required prototype and shared-brand assets exist;
- prototype is `noindex,nofollow`;
- exact prototype DNS identifiers `dns.usesafeweb.com` and `https://dns.usesafeweb.com/dns-query` are present;
- no static use in the prototype sources of `localStorage`, `sessionStorage`, `document.cookie`, `XMLHttpRequest`, `fetch(`, analytics, pixels or trackers;
- illegal out-of-order transition is rejected;
- Android and iPhone representative routes execute at the state-model level;
- native and DNS configuration confirmation remain `parent-confirmed`, not `verified`;
- only an explicit simulated verifier result can transition the DNS state to `verified`;
- removal transitions DNS to `removed` and recovery does not silently restore `verified`;
- reset returns the initial journey state;
- retry after action-needed requires a changed condition;
- uncertain and not-covered paths retain their distinct states;
- unsupported/other device routing becomes `not-covered`/limitations;
- parent-confirmed copy explicitly states it is not independently verified;
- unknown actions are rejected.

These checks provide durable positive evidence for functional state semantics, negative-path guards, configuration references, privacy constraints and rollback/reset/removal logic at the model/source level.

### Target-browser execution

The isolated headless-browser step did not execute because no `chromium`, `chromium-browser`, `google-chrome`, `google-chrome-stable`, or `microsoft-edge` executable was available on the self-hosted runner. Machine output: `BROWSER_RUNTIME=UNAVAILABLE`; step exit code `2`.

No browser assertion failed because none ran. Therefore rendered DOM behavior, browser exceptions, local-resource loading, and end-to-end click-path execution remain unverified.

## 5. Cleanup

The temporary verifier was removed from `main` in commit `fd4a7310aec97046caacf25d958a74e1ef5645a6`; read-back of `.github/workflows/verify-tsk0310.yml` returned 404, confirming cleanup. The historical workflow runs/commits remain durable evidence.

## 6. Stable disposition

- ACC-0310 artifact coverage appears implemented and is supported by source/model evidence, but **VER-0310 is not complete** because its target-environment execution requirement has not been proven.
- **TSK-0310 must remain non-PASS.**
- Safe completion requires an approved isolated browser-capable verification environment. Do not install a browser on the AdGuard runner merely to close this evidence gap, and do not incur hosted-runner cost without applicable authority.
- Once an approved browser-capable environment exists, rerun the same functional/negative/configuration/security-privacy/removal-reset checks against the rendered prototype, capture the exact environment/result, then independently decide PASS or correction based on that evidence.
