from datetime import datetime, timezone
from pathlib import Path

p = Path("CURRENT_STATE.md")
text = p.read_text()
marker = "## TSK-0297 brand-guidelines acceptance — 2026-08-29"
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

## TSK-0297 brand-guidelines acceptance — 2026-08-29

`TSK-0297 — Publish concise brand guidelines, source/editable asset library, versioning, ownership, and usage rules`: **PASS**.

Durable evidence: `TSK_0297_BRAND_GUIDELINES_EVIDENCE_2026-08-29.md`, blob `02b28f3f040d44e495ace63bf074535e4a4bd03d`. Accepted artifacts are `brand/guidelines/TSK-0297/README.md` blob `89e915678e85f7f301e8fa4b05c335cd803dd9d4` and `brand/guidelines/TSK-0297/ASSET_MANIFEST.json` blob `11e26ee46ebb60762c085513e50f8e40ec1f4854`, guideline version `1.0.0`.

ACC-0297 is proven: asset selection/generation is deterministic without inventing upstream rules; deprecation is retained and traceable; no font binaries are exposed as deliverables. VER-0297 passed against current TSK-0298/0299/0300/0301/0320 sources, claims, accessibility, source currency, surface mappings and three representative tasks. Manifest assertions returned `MANIFEST_STRUCTURE=PASS` and `MANIFEST_REFERENCE_COUNT=PASS`.

`RSK-0002` remains OPEN. This PASS is provisional internal L4 brand-governance evidence only and does not imply real-parent/native-speaker validation, legal/privacy completion, L5/L6 build authority, participant processing, public release, payment, market activation or launch readiness. All CR-0004 fences remain unchanged.

### Eligibility recomputation

The WBS direct successor newly dependency-satisfied by TSK-0297 is `TSK-0303 — Verify brand tokens/assets across critical public/product/help/status/partner/mobile/RTL contexts`, but TSK-0303 is lifecycle **L7**, not current executable L4 work. It therefore remains outside the current execution tranche until its lifecycle gate is current.

`TSK-0310` remains **WAITING / non-PASS** under its prior reconciliation because target-browser verification is still unavailable. No additional dependency-satisfied current L4 task was unlocked by TSK-0297.

### Exact next authoritative step

Current executable L4 work is exhausted. Resolve the TSK-0310 deterministic WAITING condition by providing or approving an isolated browser-capable verification environment; do not install a browser on the operational AdGuard runner or incur hosted-runner cost without owner authority. Once that environment exists, rerun VER-0310 rendered functional/negative/configuration/security-privacy/removal-reset checks and independently evaluate PASS.
"""

p.write_text("\n".join(lines) + appendix)
print("RUNTIME_TSK0297_EDIT=PASS")
