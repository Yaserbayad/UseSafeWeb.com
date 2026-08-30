# TSK-0333 End-to-End Responsive Interactive Prototype Evidence — 2026-08-30

## Disposition

`TSK-0333 — Assemble end-to-end responsive interactive prototype`: **PASS subject to canonical runtime reconciliation/read-back** under `ACC-0333 / VER-0333 / EVD-0333`.

## Current WBS contract

WBS blob: `f23b4f017d1baf73258fa30ecd71549bbfe1b815`.

- lifecycle: L4;
- priority: MEDIUM;
- dependencies: `TSK-0335; TSK-0334; TSK-0146`;
- Action Authority: `AUTO_ALLOWED`;
- acceptance: prototype includes all critical normal/exception paths, representative iOS/Android content, responsive states, accessibility annotations, and analytics/test markers.

Corrected preflight run/job `33303487023 / 99235783837` proved all three direct predecessors current PASS and `TSK0333_ELIGIBILITY_DIRECT=PASS` before implementation.

## Dependency reconciliation relevant to acceptance

The initial TSK-0333 preflight correctly failed because the earlier conversational queue shorthand had omitted hard dependency `TSK-0146`. No TSK-0333 product mutation preceded resolution of that boundary.

`TSK-0146` was then independently reconstructed from current accepted owner/product/data/decision authority and reconciled to canonical PASS under `TSK_0146_ACCOUNTLESS_FIRST_BASELINE_ACCEPTANCE_EVIDENCE_2026-08-30.md`, blob `91f8cdacb825c2423f0f6d111ee9676d8645e081`; verification run/job `33303321786 / 99235333227`; runtime state blob after reconciliation `75d077675ed09d7d5e42f470416b486258bd0857`.

Current direct predecessors at TSK-0333 dispatch:
- `TSK-0335`: PASS;
- `TSK-0334`: PASS;
- `TSK-0146`: PASS.

## Accepted prototype artifact

Directory: `prototype/TSK-0333/`.

Exact artifact blobs verified by the final successful run:
- `index.html`: `70bc43e2fac6cae845b69f4e4c2c46fd1c23f15e`;
- `model.mjs`: `8752ec4d1f0b5450ca70cd379792cdee46336e5f`;
- `app.mjs`: `95427c081ae6b2dadc259ce93ac9be6ce13b730d`;
- `prototype.css`: `f92f2bdb507d23d37e009023f1bad3c1665af6a1`.

The implementation consumes rather than forks the accepted shared system:
- TSK-0300 tokens blob `cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f`;
- TSK-0300 components blob `831e92a74b6dda04252d93242cb33bd491a02381`;
- TSK-0308 responsive composition blob `de5571379ff240f36b5aecd50f555a07176dbd32`.

It also pins current owning sources including TSK-0330, TSK-0334, TSK-0335, TSK-0324, TSK-0328, TSK-0323, TSK-0320 and TSK-0309.

## Functional and truth-state coverage

The integrated prototype includes:

- accountless public-to-setup entry and routing;
- Android and iPhone phone/native safeguard branches;
- exact Android Private DNS hostname `dns.usesafeweb.com`;
- exact iPhone DoH endpoint `https://dns.usesafeweb.com/dns-query`;
- already-configured branches that still require qualifying verification before `Verified`;
- deterministic verification-result fixture for internal testing only;
- zero-service and future one-approved-service branches;
- Protection Map with Phone / Internet / Service evidence independently represented;
- all six authorized states: `Verified`, `You confirmed this is set up`, `Action needed`, `Not covered`, `Status uncertain`, `Removed`;
- strict parent-confirmation versus system-verification separation;
- action-needed and uncertainty troubleshooting with retry only after a changed condition;
- unsupported/not-covered behavior;
- false-positive interaction without arbitrary allowlist/bypass invention;
- removal, neutral connectivity recovery and reconfiguration;
- contextual Help and Limitations without protection-state mutation;
- transient-state-loss restart behavior without fabricated persistence;
- mixed-state completion without an overall safety score or seventh success state.

## Accessibility, responsive and test-marker coverage

Final successful verifier environment:
- self-hosted runner/machine: `adguardvm`;
- Node `v22.23.2`;
- npm `10.9.8`;
- Playwright `1.62.0`;
- Chromium executable `/home/azureusr/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome`.

Final verification:
- workflow head `6e67450548aafc4b4a43bb77fed19401541d7d2d`;
- run `33303835571` — SUCCESS;
- job `99236743408` — SUCCESS.

Terminal markers:
- `TSK0333_WBS_AUTHORITY=PASS`;
- `TSK0333_SOURCE_STRUCTURE=PASS`;
- `TSK0333_STATES=6/6_PASS`;
- `TSK0333_PRIVACY_TEST_MARKERS=PASS`;
- `TSK0333_NO_DESIGN_SYSTEM_FORK=PASS`;
- `TSK0333_MODEL_BRANCHES=PASS`;
- `FOCUS_SKIP_LINK=PASS`;
- `ANDROID_NORMAL_FALSE_POSITIVE_REMOVAL_RECONFIGURE=PASS`;
- `IPHONE_NORMAL=PASS`;
- `UNSUPPORTED_PATH=PASS`;
- `ACTION_NEEDED_CHANGED_CONDITION_RETRY=PASS`;
- `UNCERTAIN_PATH=PASS`;
- `VERIFY_NOT_COVERED_PATH=PASS`;
- `LOST_TRANSIENT_STATE=PASS`;
- `RTL_LTR_TECH_ISOLATION=PASS`;
- `VIEWPORT_320=PASS`;
- `VIEWPORT_768=PASS`;
- `VIEWPORT_1024=PASS`;
- `VIEWPORT_1440=PASS`;
- `TARGET_SIZE_FLOOR=PASS`;
- `REDUCED_MOTION=PASS`;
- `TEST_MARKERS_NO_TRANSPORT=PASS`;
- `NO_PERSISTENCE=PASS`;
- `BROWSER_CONSOLE=PASS`;
- `TSK0333_RENDERED_PROTOTYPE=PASS`;
- `PRODUCTION_INVARIANTS=PASS`;
- `REPOSITORY_CLEAN=PASS`.

The implementation provides deterministic `data-event-key` / `data-testid` instrumentation points but performs no analytics transport. Browser verification found no external requests, localStorage/sessionStorage/cookie/indexedDB persistence, or console/page errors. No user identity, browsing history or raw DNS history is collected by this prototype.

## Failure/correction history

Failures are retained as diagnostic evidence and are not counted as PASS:

1. run/job `33303698505 / 99236361432` stopped after source checks because Node was not on PATH. Product assertions beyond that point did not execute. Node 22 was then explicitly provisioned.
2. run/job `33303731128 / 99236453064` reached the browser and exposed a real accessibility defect: initial page render focused the screen `h1`, causing the first Tab key to skip the bypass link. This was a product defect, not a verifier defect.
3. guarded correction run/job `33303808881 / 99236669709` changed only `prototype/TSK-0333/app.mjs`, producing blob `95427c081ae6b2dadc259ce93ac9be6ce13b730d`. The corrected behavior leaves initial keyboard focus at document start so the first Tab reaches the skip link, while subsequent in-app screen changes focus the new `h1` and update the scoped polite announcer.
4. the full unchanged acceptance suite was rerun against the corrected blob in `33303835571 / 99236743408` and passed completely.

A transient first local curl attempt occurred before the test HTTP server bound; the bounded readiness retry succeeded and all browser assertions completed. It did not affect product or production state.

## Production-host invariants

The final verifier captured before/after checksums/state and proved:
- AdGuardHome active;
- Nginx active;
- `/opt/AdGuardHome/AdGuardHome.yaml` unchanged;
- `/etc/nginx` configuration set unchanged;
- listener set unchanged after temporary local test server cleanup;
- failed-systemd-unit set unchanged;
- local test port `41733` absent after cleanup.

## Acceptance conclusion

`ACC-0333` is fully satisfied by the exact artifact and successful final verification above. `VER-0333=PASS`; `EVD-0333=SATISFIED` by this durable record and pinned run/job.

This is internal L4 integrated-prototype acceptance only. It does not imply LG-06/L5/L6 PASS, public deployment/publication, payment, market activation, launch, or current human-comprehension evidence. `DEC-0052 / CR-0005` remains unchanged.