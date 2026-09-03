from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "CURRENT_STATE.md"
EVIDENCE = ROOT / "TSK_0369_MINIMAL_SUPPORT_CAPTURE_SOURCE_IMPLEMENTATION_2026-09-03.md"
MARKER = "## TSK-0369 current accepted stable state — 2026-09-03 — SOURCE IMPLEMENTATION PARTIAL"

if EVIDENCE.exists():
    raise SystemExit("EVD-0369 source-partial artifact already exists")

state_before = STATE.read_text(encoding="utf-8")
if MARKER in state_before:
    raise SystemExit("TSK-0369 source-partial runtime marker already exists")

updated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
state_after, count = re.subn(
    r"(?m)^\*\*Updated:\*\* [^\n]+$",
    f"**Updated:** {updated_at}",
    state_before,
    count=1,
)
if count != 1:
    raise SystemExit("CURRENT_STATE Updated field not found exactly once")

section = f"""

{MARKER}

`TSK-0369 — Implement minimal support, feedback, false-positive, and abandonment capture`: **TODO**. Source implementation is durably integrated and independently source-verified, but `VER-0369` still requires target-environment functional, negative, configuration, security/privacy, and rollback evidence before PASS.

- Canonical source implementation: PR `#80`; accepted feature head `ec644b20672094b126e2a4233277975fe23806c0`; squash merge `f353e557438ec31f4967fd1bda961e1d95a8f4bb`; merge tree `f2c18ea9cf1d96f519e04cff4332f9d1db0494e5`.
- Canonical source blobs: `website/src/lib/support-capture.ts` `b8ca3edd73a8c517e46cc9acf132acd9859e759c`; `website/src/app/api/support-capture/route.ts` `185655fbccf85f0d2e5e5048143c3cfb483735b2`; `website/tests/contract/tsk0369.test.mjs` `4a37c7c16dce3f440869efd8ba99f348ee546688`; `website/package.json` `32dd6e912f4fddce22565a09982dac9b74b15053`; acceptance workflow `81709a917f0f667c719b94f4edcbdf2963a2d0d7`.
- TDD evidence: initial RED `33736223901 / 100587287332`; review-driven activation-fence RED `33736767793 / 100589069932`; accepted feature-head GREEN `33736797686 / 100589165631`; clean-main GREEN `33737232323 / 100590559641`.
- Clean-main acceptance on exact merge `f353e557...`: focused TSK-0369 contract 6/6; complete website contract suite 80/80; repository/Master-Plan validators PASS; lint has zero errors and one inherited non-error warning; typecheck/build PASS; both npm audits report 0 vulnerabilities.
- Clean-main inherited regressions are terminal-success: TSK-0360 `33737232387 / 100590559469`; TSK-0243 including real-browser acceptance `33737232369 / 100590560009`; TSK-0375 `33737232393 / 100590559433`; TSK-0359 including real-browser locale/accountless acceptance `33737232419 / 100590559664`; TSK-0629 `33737232430 / 100590559791`; TSK-0376 `33737232454 / 100590559762`.
- Source boundary: capture is fail-closed/default-off unless `USESAFEWEB_SUPPORT_CAPTURE_ENABLED=1`; no activation is recorded here. DELETE remains available to honor issued deletion receipts if capture is disabled. There is no public GET/list endpoint.
- Data boundary: exact categorical fields only; only false-positive reports may include one bounded normalized hostname; free text, identity, browsing/query/history fields and arbitrary keys fail closed; metric projection excludes the hostname; transient in-memory records hard-expire within 24 hours and can be deleted by opaque receipt.
- Remaining `VER-0369` evidence: authorized target deployment/enablement plus target functional/negative/configuration/security/privacy/rollback checks, including runtime expiry/deletion, restart/process-topology behavior, concurrency/capacity/abuse behavior and confirmation that forbidden persistence/logging is absent. Source/CI evidence cannot substitute for those observations.
- Preserved fences: no deployment, production/runtime enablement, participant processing, analytics activation, market activation, launch, lifecycle-gate PASS, downstream task PASS, or target acceptance is inferred.

### Queue effect

Successors requiring `TSK-0369` remain dependency-blocked while this task is `TODO`. After this evidence/runtime publication is merged and independently read back, recompute the current WBS/graph/runtime frontier; unrelated eligible `AUTO_ALLOWED` work may continue without crossing the preserved material-action fences.
"""

STATE.write_text(state_after.rstrip() + section + "\n", encoding="utf-8")

EVIDENCE.write_text(
    f"""# TSK-0369 — Minimal support capture source implementation evidence

**Evidence ID:** EVD-0369 source-implementation partial  
**Date:** 2026-09-03  
**Task runtime disposition:** TODO — source implementation verified; target-environment verification incomplete  
**Acceptance authority:** ACC-0369 / VER-0369 / EVD-0369

## Decision

The default-disabled TSK-0369 source implementation is accepted as durable partial evidence only. It is not task PASS. `VER-0369` requires target-environment functional, negative, configuration, security/privacy and rollback evidence that is not supplied by source/CI checks.

## Canonical implementation

- PR: #80
- Accepted feature head: `ec644b20672094b126e2a4233277975fe23806c0`
- Canonical squash merge: `f353e557438ec31f4967fd1bda961e1d95a8f4bb`
- Canonical merge tree: `f2c18ea9cf1d96f519e04cff4332f9d1db0494e5`
- `website/src/lib/support-capture.ts`: `b8ca3edd73a8c517e46cc9acf132acd9859e759c`
- `website/src/app/api/support-capture/route.ts`: `185655fbccf85f0d2e5e5048143c3cfb483735b2`
- `website/tests/contract/tsk0369.test.mjs`: `4a37c7c16dce3f440869efd8ba99f348ee546688`
- `website/package.json`: `32dd6e912f4fddce22565a09982dac9b74b15053`
- `.github/workflows/accept-tsk0369-minimal-support-capture-20260903.yml`: `81709a917f0f667c719b94f4edcbdf2963a2d0d7`

## TDD and review evidence

- Initial RED: run/job `33736223901 / 100587287332`; repository and Master-Plan validators passed, then the six focused tests failed because the implementation did not yet exist.
- Review RED: run/job `33736767793 / 100589069932`; the added default-off activation-fence expectation failed before the route correction.
- Accepted feature-head GREEN: run/job `33736797686 / 100589165631` on exact head `ec644b20672094b126e2a4233277975fe23806c0`.
- Clean-main GREEN: run/job `33737232323 / 100590559641` on exact canonical merge `f353e557438ec31f4967fd1bda961e1d95a8f4bb`.

Clean-main TSK-0369 evidence: focused 6/6; full website contracts 80/80; repository structure and Master-Plan validators PASS; 641 tasks, 858 dependency edges, 4,587 relationship entities, 18,152 relationship targets, 0 broken links and 0 generated missing task IDs; lint zero errors with one inherited non-error warning; typecheck PASS; production build PASS; both dependency audits 0 vulnerabilities; final marker `TSK0369_MINIMAL_SUPPORT_CAPTURE_ACCEPTANCE=PASS`.

## Inherited clean-main regressions

All are terminal-success on canonical merge `f353e557...`:

- TSK-0360 delivery: `33737232387 / 100590559469`
- TSK-0243 DNS verification, including real-browser acceptance: `33737232369 / 100590560009`
- TSK-0375 intake routing: `33737232393 / 100590559433`
- TSK-0359 localization/accountless browser acceptance: `33737232419 / 100590559664`
- TSK-0629 automated checks: `33737232430 / 100590559791`
- TSK-0376 accountless state machine: `33737232454 / 100590559762`

## Accepted source/data boundary

- New capture is disabled unless `USESAFEWEB_SUPPORT_CAPTURE_ENABLED=1`; this evidence does not enable it.
- POST uses bounded UTF-8 JSON and no-store responses; DELETE remains available while collection is disabled so prior deletion receipts are not stranded; there is no public GET/list route.
- Accepted input is categorical and exact-key only. Free text, identity, browsing/query/history fields and arbitrary fields are rejected.
- A false-positive report may include one normalized bounded hostname only; non-false-positive reports cannot include it. The aggregate metric projection removes the hostname.
- Records use a bounded in-memory store, opaque UUIDv4 deletion receipts and a non-sliding hard expiry of at most 24 hours; source contains no filesystem/local-storage/SQL persistence path.

## Remaining acceptance / non-inference

`ACC-0369` is not promoted to PASS because `VER-0369` requires target-environment execution. Remaining evidence includes authorized target deployment/enablement and target functional, negative, configuration, security/privacy and rollback verification, including runtime expiry/deletion, restart/process-topology behavior, concurrency/capacity/abuse behavior and direct inspection that forbidden persistence/logging is absent.

No deployment, runtime/production enablement, participant processing, analytics activation, market activation, launch, lifecycle-gate PASS, downstream task PASS or target acceptance is created or inferred by this evidence.

**Generated for guarded publication:** {updated_at}
""",
    encoding="utf-8",
)
