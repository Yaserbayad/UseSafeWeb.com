# TSK-0310 Rendered Browser Acceptance Evidence — 2026-08-29

## Disposition

`TSK-0310 — Build the representative mobile-first public-to-setup prototype before production implementation`: **PASS**.

This disposition is limited to the current internal L4 prototype and its current ACC-0310 / VER-0310 contract. It does not imply representative-parent validation, legal/privacy completion, production implementation authority, public publication, payment, market activation, or launch readiness. `RSK-0002` remains OPEN and CR-0004 fences remain unchanged.

## Acceptance contract

Current WBS contract:

- **ACC-0310:** prototype covers discovery, routing, native safeguard, DNS setup/verification, external service, Protection Map, troubleshooting, recovery/removal, and limitations.
- **VER-0310:** execute in the target environment; run functional, negative, configuration, security/privacy, and rollback checks; compare to acceptance criteria.
- **EVD-0310:** artifact/version; source or exact environment; verification output; date; verifier; deviations and disposition.
- Owner: UX. Action Authority: A3 / `AUTO_ALLOWED`.

## Accepted prototype and repeatable verification assets

Current core prototype blobs at final verification:

- `prototype/TSK-0310/index.html` — `5d80dfdefb52042bc34468723354fefd325285e4`
- `prototype/TSK-0310/model.mjs` — `01343273fd09c3c12d26f0c0eb1ae9a2fce10c91`
- `prototype/TSK-0310/app.mjs` — `a4a0aff8848f8541e2581e333efbf48767c9f0ff`
- `prototype/TSK-0310/prototype.css` — `439ef05dd04da7fccf01cb4b85e317a828389edf`

Repeatable browser-verification assets:

- `prototype/TSK-0310/package.json` — `9cbf9f5102592a0147c531748db49b68e4ee1648`; Playwright pinned to `1.62.0`.
- `prototype/TSK-0310/browser-acceptance.mjs` — `f791a797f6a64be8b74eb13cbd2e628d5b083007`.
- `.github/workflows/tsk0310-browser-install-and-acceptance.yml` — final verification workflow blob `af9fc1f6bc6e9cfef2b65c0ee42c0c5043795e6c`.

Earlier non-browser model verification remains complementary evidence in `TSK_0310_PROTOTYPE_PARTIAL_EVIDENCE_2026-08-29.md`, blob `edde3ebc641e392b6bde6cdc0896a4e3d60d8317`.

## Owner-authorized browser environment

The Project Owner explicitly authorized bounded browser-test capability on operational runner `adguardvm`, with the browser allowed to remain installed through the current testing tranche and to be removed afterward when no longer required. The authorization was persisted to `CURRENT_STATE.md` before installation.

Final verified environment:

- Runner/machine: `adguardvm`
- Runner user: `azureusr`
- OS baseline: Ubuntu 24.04 LTS
- Node: `22.23.2`
- npm: `10.9.8`
- Playwright: `1.62.0`
- Browser: Google Chrome for Testing / Chromium `151.0.7922.34`, Playwright Chromium revision `1234`
- Browser path: `/home/azureusr/.cache/usesafeweb-playwright/chromium-1234/chrome-linux64/chrome`
- npm install/audit: 2 packages installed in the verification workspace; 3 audited; `0 vulnerabilities`.

Initial browser provisioning installed 73 required Ubuntu browser/runtime packages, upgraded 0, removed 0, and reported approximately 300 MB additional OS disk usage. The browser download was approximately 184.3 MiB plus Playwright FFmpeg approximately 2.3 MiB. No AdGuard or Nginx configuration change was authorized or performed.

## Initial rendered run and diagnostic correction

Initial run:

- Workflow run: `33262868889`
- Job: `99127705834`
- Workflow head: `1d5d1ddcb186d823405f4d9e89feccf4ebed696a`

Results before the harness failure:

- `PRE_INSTALL_HEALTH=PASS`
- Playwright install/audit: PASS, 0 vulnerabilities
- Chromium `151.0.7922.34`: installed and launched successfully
- `CHROMIUM_INSTALL=PASS`
- Numerous rendered checks passed through the Android DNS configuration surface.

The run then failed because the test harness deliberately injected an out-of-app invalid-transition button and did not remove that test fixture. The next unscoped `DNS_CONFIGURED` locator therefore matched both the real app button and the synthetic fixture. This was a **test-harness false negative**, not prototype evidence of failure.

Root-cause correction:

- harness correction commit: `53b23b4def67902b7ecf65a1b012db47814a79f3`
- synthetic invalid-transition fixture is explicitly removed and its removal is asserted;
- the normal DNS configured action is scoped to `#app`;
- workflow hardening commit: `65bd352c531cfb8f4d7d980898fa331276d847d3` makes post-test production health verification execute with `always()` so future browser failures cannot skip production-invariant observation.

Independent post-failure production-health recovery check:

- Run: `33262985208`
- Job: `99128001397`
- Runner: `adguardvm`
- `ADGUARD_HEALTH=PASS`
- `NGINX_HEALTH=PASS`
- `ADGUARD_CONFIG_UNCHANGED=PASS`
- `NGINX_CONFIG_UNCHANGED=PASS`
- `LISTENERS_UNCHANGED=PASS`
- `NO_TEST_LISTENER=PASS`
- `FAILED_UNITS_UNCHANGED=PASS`
- `CHROMIUM_PRESENT=PASS`
- observed browser version: `151.0.7922.34`
- terminal marker: `TSK0310_POST_FAILURE_HEALTH=PASS`

## Final rendered acceptance run

Final authoritative rendered run:

- Workflow run: `33263045598`
- Job: `99128162008`
- Workflow head: `65bd352c531cfb8f4d7d980898fa331276d847d3`
- Runner/machine: `adguardvm`
- Browser: `151.0.7922.34`
- Playwright: `1.62.0`
- Browser was reused from the owner-authorized installation; no second OS dependency installation was required.

Terminal verification markers:

- `PRE_TEST_HEALTH=PASS`
- `CHROMIUM_CAPABILITY=PASS`
- `BROWSER_ACCEPTANCE_CHECKS=218`
- `BROWSER_ACCEPTANCE=PASS`
- `RENDERED_ACCEPTANCE=PASS`
- `ADGUARD_CONFIG_UNCHANGED=PASS`
- `NGINX_CONFIG_UNCHANGED=PASS`
- `LISTENERS_UNCHANGED=PASS`
- `NO_TEST_LISTENER=PASS`
- `FAILED_UNITS_UNCHANGED=PASS`
- `POST_TEST_HEALTH=PASS`
- `TSK0310_PRODUCTION_INVARIANTS=PASS`

The final run's package delta between its own pre/post snapshots was empty.

## VER-0310 result matrix

### Functional — PASS

Rendered paths proved:

- discovery and global Help/Limits/Start-over navigation;
- supported-platform routing;
- Android native-safeguard path;
- iPhone native-safeguard path;
- DNS setup and verification;
- external-service state;
- Protection Map rendering/state preservation;
- troubleshooting and retries;
- removal and recovery;
- limitations/unsupported path;
- mobile 320 px and desktop 1280 px responsive rendering without horizontal overflow;
- desktop Protection Map renders three columns while the representative frame remains bounded to 512 px.

### Negative — PASS

Rendered negative coverage proved:

- an invalid state-machine transition is rejected and the current screen is preserved;
- unsupported platform routes to limitations without speculative setup/removal guidance;
- `action-needed`, `uncertain`, and `not-covered` verification outcomes route to the correct states;
- retry-after-change returns to verification;
- removal is available only after a configured route.

### Configuration — PASS

- Android rendered setup uses exact Private DNS hostname `dns.usesafeweb.com`.
- iPhone rendered setup uses exact DoH URL `https://dns.usesafeweb.com/dns-query`.
- Prototype explicitly does not silently alter Android DNS settings.
- Prototype explicitly does not fabricate/distribute an unverified iOS `.mobileconfig` profile.
- Unsupported paths do not invent speculative client workarounds.

### Security / privacy — PASS

Rendered checks proved:

- page resources were localhost-only;
- no external page requests occurred;
- local storage remained empty;
- session storage remained empty;
- cookies remained empty;
- no service worker was registered;
- no form/input/textarea/select data-entry controls were present in the internal prototype;
- all checked buttons had explicit `type="button"`;
- no console errors or page errors occurred;
- internal prototype retains `noindex,nofollow`;
- temporary HTTP serving was bound to `127.0.0.1:4173` only and was removed after verification.

No user login, personal data, participant data, raw DNS query data, or persistent browser-state evidence was used.

### Rollback / recovery — PASS

- rendered Android removal path explicitly returns to the platform's normal Automatic policy;
- prototype warns against silent plaintext fallback being represented as protected;
- after recovery/connectivity confirmation, Protection Map retains Internet state as `Removed` rather than falsely returning to verified protection;
- the temporary verification listener was removed;
- AdGuard configuration, Nginx configuration, server listening sockets, and failed-systemd-unit set were unchanged across the final verification run;
- AdGuardHome and Nginx remained active in the independent recovery health check and final run.

## ACC-0310 evaluation

All required representative prototype areas are present and were rendered/exercised: discovery, routing, native safeguard, DNS setup/verification, external service, Protection Map, troubleshooting, recovery/removal, and limitations. **ACC-0310 = PASS.**

Functional, negative, configuration, security/privacy, and rollback/recovery verification all passed in the accepted rendered environment. **VER-0310 = PASS.**

The evidence records artifact/version identifiers, exact environment, final verification output, date, verifier context, first-run deviation/root cause/correction, and final disposition. **EVD-0310 = SATISFIED.**

## Browser retention / cleanup obligation

Per current owner authorization, the Playwright-managed Chromium browser and required runtime dependencies remain on `adguardvm` for the current testing tranche. They are **not** being removed as part of TSK-0310 closure. Removal is a later bounded cleanup action after browser-based testing is no longer required and must include fresh AdGuard/Nginx health verification.

## Final disposition

`TSK-0310`: **PASS** for its current internal L4 acceptance contract.

`RSK-0002` remains OPEN. `TSK-0309` is not unlocked solely by this PASS because its other hard dependency `TSK-0187` remains required under the current validation-led lifecycle. No build, participant-processing, public-release, payment, market, or launch authority is inferred.