from datetime import datetime, timezone
from pathlib import Path

p = Path("CURRENT_STATE.md")
text = p.read_text()
marker = "## TSK-0310 rendered-browser acceptance — 2026-08-29"
if marker in text:
    print("RUNTIME_ALREADY_RECONCILED=PASS")
    raise SystemExit(0)

lines = text.splitlines()
stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
for i, line in enumerate(lines):
    if line.startswith("**Updated:** "):
        lines[i] = f"**Updated:** {stamp}"
        break
else:
    raise RuntimeError("CURRENT_STATE.md missing Updated marker")

appendix = """

## TSK-0310 rendered-browser acceptance — 2026-08-29

`TSK-0310 — Build the representative mobile-first public-to-setup prototype before production implementation`: **PASS**.

Durable acceptance evidence: `TSK_0310_RENDERED_BROWSER_ACCEPTANCE_EVIDENCE_2026-08-29.md`, blob `02b34756862a62091908e60d32b490059a84a67c`. Accepted core prototype blobs: `index.html` `5d80dfdefb52042bc34468723354fefd325285e4`, `model.mjs` `01343273fd09c3c12d26f0c0eb1ae9a2fce10c91`, `app.mjs` `a4a0aff8848f8541e2581e333efbf48767c9f0ff`, `prototype.css` `439ef05dd04da7fccf01cb4b85e317a828389edf`.

Final rendered verification ran on owner-authorized `adguardvm` with Playwright `1.62.0` and Chromium/Chrome for Testing `151.0.7922.34`: run `33263045598`, job `99128162008`. `BROWSER_ACCEPTANCE_CHECKS=218`, `BROWSER_ACCEPTANCE=PASS`, `RENDERED_ACCEPTANCE=PASS`. Functional, negative, configuration, security/privacy, and rollback/recovery verification all passed. AdGuard and Nginx configurations, listening sockets, and failed-systemd-unit state were unchanged; the temporary localhost test listener was removed. npm audit reported 0 vulnerabilities.

The initial rendered attempt (`33262868889` / `99127705834`) exposed a test-harness fixture-isolation defect rather than a prototype defect. The root cause was corrected and guarded before the final full rerun; independent post-failure production-health run `33262985208` / `99128001397` also passed all service/config/listener invariants.

Per current owner authority, the Playwright-managed browser and required runtime dependencies remain installed on `adguardvm` through the current testing tranche and must be removed with fresh service/config/listener verification when browser testing is no longer required.

`ACC-0310=PASS`; `VER-0310=PASS`; `EVD-0310=SATISFIED`.

`RSK-0002` remains OPEN. This PASS is internal L4 prototype evidence only and does not imply representative-parent validation, legal/privacy completion, production build authority, participant processing, public publication, payment, market activation, or launch readiness.

### Eligibility recomputation

`TSK-0309 — Correct the prototype from usability/comprehension evidence and freeze the implementation-ready experience baseline` now has `TSK-0310` satisfied but remains **WAITING / non-eligible** because its other hard dependency `TSK-0187` is not PASS.

`TSK-0187 — Validate the proposed accountless critical journey before production coding` remains the material L4 validation gate. Its ACC requires representative parents to complete the prototype, understand protection limits, and recover/remove without hidden facilitation, with findings and contrary evidence recorded. That evidence cannot be fabricated from automated browser execution.

### Exact next authoritative step

Resolve `TSK-0187` by running the approved representative-parent validation when qualified participants and the required research/communication inputs are available; until then do not advance `TSK-0309` or infer behavioral validation. Browser capability may remain on `adguardvm` for the current testing tranche under the owner authorization above.
"""

p.write_text("\n".join(lines) + appendix)
print("RUNTIME_TSK0310_PASS_EDIT=PASS")
