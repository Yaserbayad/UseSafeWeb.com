# TSK-0309 Implementation-Ready Experience Baseline Evidence — 2026-08-29

## Disposition

`TSK-0309 — Freeze the implementation-ready experience baseline from current internal and automated acceptance evidence`: **PASS**.

The accepted implementation-ready UX baseline is version `1.0.0`. No prototype/product-code correction was required because current accepted target-environment evidence establishes no unresolved critical/high pre-product defect. The representative TSK-0310 implementation is frozen unchanged and is now bound by an explicit design-to-build contract and machine-readable manifest.

This PASS is limited to the current L4 design/experience contract. It does not imply public-release, production-deployment, payment, market-activation, or launch authority.

## Current task contract

- **ACC-0309:** material internally/automatically observed functional, truth-state, responsive, accessibility, recovery/removal, claims and interaction defects have root cause/disposition; all critical/high pre-product defects are corrected/retested; speculative features are excluded; no real-user comprehension claim is required or inferred before L8.
- **VER-0309:** execute in target environment; run functional, negative, configuration, security/privacy and rollback checks; compare to acceptance criteria.
- **EVD-0309:** artifact/version, exact source/environment, verification output, date, verifier, deviations and disposition.
- Owner: UX.
- Authority: A3 / `AUTO_ALLOWED`.
- Dependencies under current semantics: `TSK-0310=PASS`; `TSK-0187=NOT_APPLICABLE+PASS` verified exclusion.

## Accepted baseline artifacts

- `prototype/TSK-0309/BASELINE.md` — Git blob `76bb848ebdf6a2aee4dd84bc18e8af5ba8a99dbc`
- `prototype/TSK-0309/BASELINE_MANIFEST.json` — Git blob `dba23b4593224b81361bab06bc3fa4332015d1b5`
- baseline version: `1.0.0`
- schema: `usesafeweb.experience-baseline.v1`
- status: `frozen_internal_l4`

The baseline binds the existing accepted TSK-0310 prototype rather than forking it. Accepted representative source blobs remain:

- `prototype/TSK-0310/index.html` — `5d80dfdefb52042bc34468723354fefd325285e4`
- `prototype/TSK-0310/model.mjs` — `01343273fd09c3c12d26f0c0eb1ae9a2fce10c91`
- `prototype/TSK-0310/app.mjs` — `a4a0aff8848f8541e2581e333efbf48767c9f0ff`
- `prototype/TSK-0310/prototype.css` — `439ef05dd04da7fccf01cb4b85e317a828389edf`
- `prototype/TSK-0310/browser-acceptance.mjs` — `f791a797f6a64be8b74eb13cbd2e628d5b083007`
- `prototype/TSK-0310/package.json` — `9cbf9f5102592a0147c531748db49b68e4ee1648`

Current governing sources were blob-pinned and verified by the final run, including TSK-0310 rendered acceptance, TSK-0320 protection-state rules, TSK-0299 verbal system, TSK-0300 shared brand system, current WBS, and current Layer-5 rules.

## Frozen design-to-build contract

The baseline makes the current experience deterministic for engineering:

- 11 screens: discovery, routing, native safeguard, DNS setup, verification, service, Protection Map, troubleshooting, removal, recovery and limitations;
- six evidence states: verified, parent-confirmed, action-needed, not-covered, uncertain and removed;
- full critical journey: start, configure, verify, understand, troubleshoot, recover, remove and reset/reconfigure;
- Android Private DNS hostname exactly `dns.usesafeweb.com`;
- iPhone DoH endpoint exactly `https://dns.usesafeweb.com/dns-query`;
- unsupported platforms fail safely to explicit limitations without speculative setup guidance;
- parent confirmation never equals system verification;
- verified state requires qualifying evidence;
- uncertainty/not-covered never imply success;
- removal never silently becomes verified;
- no safety score or complete-safety claim;
- each retained interaction has a documented journey need;
- invalid state transitions are rejected;
- retry requires a changed condition;
- accountless-first, privacy-minimal representative path;
- no mandatory account, customer dashboard, customer-facing AdGuard admin, child account, browsing/activity history, broad DNS admin console, native app, school portal or public integration platform in this baseline;
- no card/trial/payment before core value;
- mobile-first, explicit heading focus/state semantics, no representative horizontal overflow, textual non-color-only state meaning;
- first-public-release language constraint remains English/Turkish/Arabic with Arabic RTL and invariant LTR `SafeWeb` brand token.

Optional persistence/account/dashboard remains outside this baseline unless independently activated by its current exception/owner-authority path.

## First acceptance attempt — verifier defect, not baseline defect

Run/job: `33267164410` / `99139159438`.

The pre-test server health snapshot passed. Source/blob checks progressed until the verifier attempted to read a guessed WBS column named `AI_Action_Authority`, which does not exist in the canonical CSV schema. The WBS row does contain `AUTO_ALLOWED`; the verifier implementation was wrong.

Disposition:

- classified as test-harness/schema lookup defect;
- no baseline or prototype defect established;
- browser suite did not run in this failed attempt;
- unconditional post-test production checks passed: AdGuard/Nginx active, configurations unchanged, listener set unchanged, failed-unit set unchanged, no temporary test listener remained.

The verifier was corrected to assert the canonical row semantically (`AUTO_ALLOWED` present in row values) rather than inventing a column name.

## Final authoritative acceptance run

Workflow run: `33267199945`  
Job: `99139256895`  
Workflow head: `309f0c51347610e6256535fffdabb8425dd7e115`  
Runner/machine: `adguardvm`  
Runner user: `azureusr`  
Node: `22.23.2`  
npm: `10.9.8`  
Playwright: `1.62.0`  
Chromium/Chrome for Testing: `151.0.7922.34`

### Static/source-contract verification — PASS

Terminal markers:

- `TSK0309_BASELINE_MANIFEST=PASS`
- `TSK0309_SOURCE_BLOBS=PASS`
- `TSK0309_SCOPE_INVARIANTS=PASS`
- `TSK0309_WBS_AUTHORITY=PASS`
- `TSK0309_MODEL_CONFORMANCE=PASS`

The verifier proved:

- exact baseline schema/version/status/decision basis;
- exact current artifact and governing-source Git blobs;
- current WBS task/dependency/exclusion semantics;
- exact requirements/interfaces/constraints linkage;
- exact screen/state inventory and platform endpoints;
- scope exclusions and no open critical/high defect disposition;
- no release-authority claim;
- state-model conformance to the frozen manifest.

### Browser / functional / negative / configuration verification — PASS

- retained browser capability reused successfully;
- npm audit: `0 vulnerabilities`;
- `BROWSER_ACCEPTANCE_CHECKS=218`;
- `BROWSER_ACCEPTANCE=PASS`;
- `TSK0309_RENDERED_REGRESSION=PASS`.

The complete rendered suite re-proved Android and iPhone success paths, unsupported paths, invalid transition handling, action-needed/uncertain/not-covered outcomes, retries, Protection Map truth states, removal/recovery, reset, responsive 320 px and 1280 px behavior, heading focus, explicit ARIA busy state, exact DNS configuration values, no fabricated iPhone profile, no speculative unsupported workaround, and no runtime console/page errors.

### Security/privacy verification — PASS

Rendered checks re-proved:

- resources are localhost-only;
- no external page requests;
- localStorage empty;
- sessionStorage empty;
- cookies empty;
- no service worker;
- no representative data-entry controls;
- explicit button types;
- no external tracking/resource dependency in the prototype.

### Rollback / production-invariant verification — PASS

Final markers:

- `TSK0309_ADGUARD_CONFIG_UNCHANGED=PASS`
- `TSK0309_NGINX_CONFIG_UNCHANGED=PASS`
- `TSK0309_LISTENERS_UNCHANGED=PASS`
- `TSK0309_FAILED_UNITS_UNCHANGED=PASS`
- `TSK0309_POST_HEALTH=PASS`.

The temporary localhost browser-test listener was removed. AdGuardHome and Nginx remained active; their configurations and server listener/failed-unit sets were unchanged across verification.

## ACC-0309 evaluation

**PASS.** Current accepted evidence establishes no unresolved critical/high pre-product product/UX defect. The known test deviations were harness defects, were root-caused and corrected, and the final complete suite passed. Speculative/deferred scope is explicitly excluded in the frozen contract. The baseline does not claim evidence it does not possess.

## VER-0309 evaluation

**PASS.** Target-environment functional, negative, configuration, security/privacy and rollback/recovery verification all passed against the exact frozen artifact/source set.

## EVD-0309 evaluation

**SATISFIED.** This record identifies artifact/version, exact source blobs, environment/tool versions, verification run/job and outputs, date, deviations/root cause/corrections, and stable disposition.

## Final disposition

`TSK-0309`: **PASS**.

The implementation-ready experience baseline is frozen at `1.0.0`. No product-code change was justified or made. `RSK-0002` remains an open product-assumption risk under current DEC-0052/CR-0005 semantics; it does not invalidate this internal/automated L4 acceptance. Downstream work must consume this baseline without inventing account/dashboard/persistence scope, protection-state semantics, claims, data collection, or unsupported platform behavior.
