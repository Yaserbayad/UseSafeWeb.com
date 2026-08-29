# TSK-0310 AdGuard VM Browser-Capability Evidence — 2026-08-29

## Disposition

`TSK-0310` remains **WAITING / non-PASS**. The operational `adguardvm` runner cannot currently provide the required isolated rendered-browser verification environment without installing additional browser/container capability, which is outside the current approved operational-server fence.

## Authority / context

- Project Owner explicitly approved use of `adguardvm` if it was safe for the pending work and reported that the prior test VM had been deleted.
- The current runtime fence prohibits installing a browser on the operational AdGuard runner merely to satisfy `TSK-0310` verification.
- A read-only capability probe was therefore executed; no browser, container runtime, isolation package, configuration, service, or AdGuard setting was installed or changed.

## Direct execution evidence

- Workflow commit: `45a933b6cd9a594534e390a31b7380a58026b890`
- GitHub Actions run: `33262314091`
- Job: `99126249865`
- Runner name / machine: `adguardvm`
- Runner user: `azureusr`
- Token permissions: repository contents read-only

Observed capability results:

- Chromium: NO
- chromium-browser: NO
- Google Chrome: NO
- Firefox: NO
- Docker: NO
- Podman: NO
- Bubblewrap (`bwrap`): NO
- Firejail: NO
- `unshare` binary: YES, but unprivileged user namespace test: NO
- Docker daemon access: NO
- Cached browser container image: NO
- Podman access: NO
- CPU count: 2
- Memory available at probe: 3,083,748 kB
- Root filesystem available at probe: 25,074,172 kB
- Probe terminal marker: `TSK0310_CAPABILITY_PROBE=PASS`

## Verification conclusion

`adguardvm` is suitable for repository/runtime reconciliation but **not** for the pending `TSK-0310` rendered-browser acceptance work under the current safety/governance fence. Using it for that work would require installing or introducing new browser/container capability on the operational DNS VM.

The deterministic resolution remains: provide or approve a separate isolated browser-capable verification environment, then run the current `VER-0310` rendered functional, negative, configuration, security/privacy, and removal/reset checks. Historical evidence from the deleted test VM remains historical evidence only and is not evidence of current executor availability.
