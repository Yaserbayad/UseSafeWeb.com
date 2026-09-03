from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "CURRENT_STATE.md"
EVIDENCE = ROOT / "TSK_0499_PRODUCT_EVENTS_METRICS_SOURCE_IMPLEMENTATION_2026-09-03.md"
MARKER = "## TSK-0499 current accepted stable state — 2026-09-03 — SOURCE IMPLEMENTATION PARTIAL"

if EVIDENCE.exists():
    raise SystemExit("EVD-0499 source-partial artifact already exists")

state_before = STATE.read_text(encoding="utf-8")
if MARKER in state_before:
    raise SystemExit("TSK-0499 source-partial runtime marker already exists")

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

`TSK-0499 — Implement approved product events and metric validation`: **TODO**. The privacy-safe, default-disabled source implementation is durably integrated and independently source-verified, but `VER-0499` still requires authorized target-environment functional, negative, configuration, security/privacy, and rollback evidence before PASS.

- Canonical source implementation: PR `#82`; starting canonical base `278a27b267ecfdcdd9510d2a348391f49cb4c96c`; accepted feature head `cdf9b218d0633b553e26eda2966cc600b58d41d5`; squash merge `9221aeed32c131597e8356a9d7d0660eb893b1c5`; merge tree `3d0f6b7657e05d72f4a37776c991a20a47ce2c84`.
- Canonical source blobs: `website/src/lib/product-events.ts` `909aeb5ca8b6c1cc8e142abea0fda3002015c48d`; `website/src/app/api/product-events/route.ts` `ac810d8969fd99cea87662600e0a9a01f93813a5`; `website/tests/contract/tsk0499.test.mjs` `1cdbb60005a0b9c05d19231bce2c5df7918e7843`; `website/package.json` `831ee3edf37fc8b4c28b814cfea22b317f54f72f`; acceptance workflow `4b7ba5bf31180911b71f1a66f6c49d48fb8af8ff`.
- TDD evidence: initial RED `33739090936 / 100596537910`; initial GREEN `33739331776 / 100597297103`; review-driven retention RED `33739604943 / 100598167709`; accepted feature-head GREEN `33739736623 / 100598582675`.
- Clean-main TSK-0499 acceptance on exact merge `9221aeed...`: run/job `33740074174 / 100599668788`; focused contract 7/7; complete website contract suite 87/87; repository/Master-Plan validators PASS; lint has zero errors and one inherited non-error warning; typecheck/build PASS; both npm audits report 0 vulnerabilities; marker `TSK0499_PRODUCT_EVENTS_METRICS_ACCEPTANCE=PASS`.
- Clean-main inherited regressions are terminal-success: TSK-0369 `33740074186 / 100599668981`; TSK-0360 `33740074191 / 100599668975`; TSK-0375 including real-browser intake `33740074159 / 100599669083`; TSK-0629 including real-browser acceptance `33740074167 / 100599669034`; TSK-0243 including real-browser DNS verification `33740074196 / 100599668995`; TSK-0376 `33740074152 / 100599668559`; TSK-0359 including real-browser localization/accountless acceptance `33740074143 / 100599668763`.
- Event/data boundary: schema `1.0.1` accepts exactly the twelve TSK-0498 event names with exact-key fail-closed validation; browsing/domain/DNS-query/URL/child-activity, identity/account/device linkage, free text, secrets/tokens/cookies/headers and arbitrary fields are rejected. Aggregate projection removes event ID, raw timestamp, journey-session ID and cost source reference.
- Protection/metric boundary: the six authoritative protection states remain distinct; parent/config confirmation cannot become positive technical verification; rate metrics require explicit source/formula/numerator/denominator/window/release-or-cohort/owner/guardrail/decision action and return null instead of fabricating a percentage when the denominator is missing or zero.
- Retention/transport boundary: accountless raw/session state hard-expires non-sliding within 24 hours; synthetic/recovery raw data uses 30 days; measurement/cost raw retention uses a conservative fixed 390-day ceiling; client timestamps cannot extend receipt-time TTL; deleting the last raw event cannot reset a session TTL. The HTTP route is bounded, `no-store`, exposes no public GET/list endpoint, contains no third-party analytics transport or payload logging, and POST remains disabled unless `USESAFEWEB_PRODUCT_EVENTS_ENABLED=1`.
- Remaining `VER-0499` evidence: authorized target deployment/enablement plus target functional/negative/configuration/security/privacy/rollback checks, including rate/abuse/capacity/concurrency behavior, process/restart/topology behavior, target deletion/expiry, direct confirmation that forbidden persistent logs/data are absent, and catalogue/data-quality semantics under target use.
- Preserved fences: no telemetry/analytics activation, deployment, production/runtime enablement, participant processing, optional-account event expansion, third-party analytics integration, market activation, launch, lifecycle-gate PASS, downstream task PASS, or target acceptance is inferred.

### Queue effect

Successors requiring `TSK-0499` remain dependency-blocked while this task is `TODO`. After this evidence/runtime publication is merged and independently read back, recompute the current WBS/graph/runtime frontier; unrelated eligible `AUTO_ALLOWED` work may continue without crossing the preserved material-action fences.
"""

STATE.write_text(state_after.rstrip() + section + "\n", encoding="utf-8")

EVIDENCE.write_text(
    f"""# TSK-0499 — Product events and metric validation source implementation evidence

**Evidence ID:** EVD-0499 source-implementation partial
**Date:** 2026-09-03
**Task runtime disposition:** TODO — source implementation verified; target-environment verification incomplete
**Acceptance authority:** ACC-0499 / VER-0499 / EVD-0499

## Decision

The privacy-safe, default-disabled TSK-0499 source implementation is accepted as durable partial evidence only. It is not task PASS. `VER-0499` requires target-environment functional, negative, configuration, security/privacy and rollback evidence that source/CI checks cannot supply.

## Canonical implementation

- Starting canonical base: `278a27b267ecfdcdd9510d2a348391f49cb4c96c`
- PR: #82
- Accepted feature head: `cdf9b218d0633b553e26eda2966cc600b58d41d5`
- Canonical squash merge: `9221aeed32c131597e8356a9d7d0660eb893b1c5`
- Canonical merge tree: `3d0f6b7657e05d72f4a37776c991a20a47ce2c84`
- `website/src/lib/product-events.ts`: `909aeb5ca8b6c1cc8e142abea0fda3002015c48d`
- `website/src/app/api/product-events/route.ts`: `ac810d8969fd99cea87662600e0a9a01f93813a5`
- `website/tests/contract/tsk0499.test.mjs`: `1cdbb60005a0b9c05d19231bce2c5df7918e7843`
- `website/package.json`: `831ee3edf37fc8b4c28b814cfea22b317f54f72f`
- `.github/workflows/accept-tsk0499-product-events-metrics-20260903.yml`: `4b7ba5bf31180911b71f1a66f6c49d48fb8af8ff`

## TDD and review evidence

- Initial RED: `33739090936 / 100596537910`; repository and Master-Plan validators passed, then the six focused tests failed because the production module and route did not yet exist.
- Initial GREEN: `33739331776 / 100597297103` after the minimum implementation and exact-key test fixture correction.
- Review RED: `33739604943 / 100598167709`; retention-hardening tests exposed client-controlled future timestamp extension and an overlong fixed measurement duration, while source review independently confirmed session-expiry reset risk after deleting the last raw event.
- Accepted feature-head GREEN: `33739736623 / 100598582675` on exact head `cdf9b218d0633b553e26eda2966cc600b58d41d5`.
- Clean-main GREEN: `33740074174 / 100599668788` on exact canonical merge `9221aeed32c131597e8356a9d7d0660eb893b1c5`.

Clean-main TSK-0499 evidence: focused 7/7; full website contracts 87/87; repository structure and Master-Plan validators PASS; 641 tasks, 858 dependency edges, 4,587 relationship entities, 18,152 relationship targets, 0 broken links and 0 generated missing task IDs; lint zero errors with one inherited non-error warning; typecheck PASS; production build PASS; both dependency audits 0 vulnerabilities; final marker `TSK0499_PRODUCT_EVENTS_METRICS_ACCEPTANCE=PASS`.

## Inherited clean-main regressions

All are terminal-success on canonical merge `9221aeed...`:

- TSK-0369 support capture: `33740074186 / 100599668981`
- TSK-0360 gated profile delivery: `33740074191 / 100599668975`
- TSK-0375 intake routing, including real-browser acceptance: `33740074159 / 100599669083`
- TSK-0629 automated checks, including real-browser acceptance: `33740074167 / 100599669034`
- TSK-0243 DNS verification, including real-browser acceptance: `33740074196 / 100599668995`
- TSK-0376 accountless state machine: `33740074152 / 100599668559`
- TSK-0359 localization/accountless, including real-browser acceptance: `33740074143 / 100599668763`

## Accepted event, privacy and metric boundary

- Schema `1.0.1` accepts exactly the twelve current TSK-0498 event names and rejects unknown event names or fields before capture.
- Browsing/domain/DNS query/URL/child-activity data, identity/account/device linkage, free text, arbitrary payloads, secrets, tokens, cookies and headers are rejected.
- Aggregate projection excludes `event_id`, `occurred_at`, `journey_session_id` and `source_reference`, preventing the raw accountless session key from becoming a product-analytics join key.
- The six authoritative protection states remain distinct; parent/configuration confirmation is not accepted as positive technical verification.
- Metric definitions require explicit source events, formula, numerator, denominator, time window, release/cohort, owner, guardrail and decision action. Missing or zero denominators produce null rather than an invented percentage.
- Raw accountless/session retention is non-sliding and capped at 24 hours; synthetic/recovery raw retention is 30 days; measurement/cost raw retention uses a conservative fixed 390-day ceiling. Client timestamps cannot extend the receipt-time TTL, and deleting the last raw event does not reset an originating accountless session expiry.
- The route is bounded UTF-8 JSON with `Cache-Control: no-store`, no public GET/list endpoint, no third-party analytics transport and no payload logging. New capture remains disabled unless `USESAFEWEB_PRODUCT_EVENTS_ENABLED=1`.

## Remaining acceptance / non-inference

`ACC-0499` is not promoted to PASS because `VER-0499` requires target-environment execution. Remaining evidence includes authorized target deployment/enablement and target functional, negative, configuration, security/privacy and rollback verification, including rate/abuse/capacity/concurrency behavior, restart/process-topology behavior, target deletion/expiry, direct confirmation that forbidden persistent logs/data are absent, and catalogue/data-quality semantics under target use.

No telemetry/analytics activation, deployment, production/runtime enablement, participant processing, optional-account event expansion, third-party analytics integration, market activation, launch, lifecycle-gate PASS, downstream task PASS or target acceptance is created or inferred by this evidence.

**Generated for guarded publication:** {updated_at}
""",
    encoding="utf-8",
)
