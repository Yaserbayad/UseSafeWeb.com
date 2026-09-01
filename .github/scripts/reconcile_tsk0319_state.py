from __future__ import annotations

import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

EXPECTED = {
    "CURRENT_STATE.md": "c9d4735e18752284cc61c4b6a4ad771c752f9685",
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "TSK_0319_POST_CR0008_AUTOMATED_VERIFICATION_TROUBLESHOOTING_RECOVERY_HELP_2026-09-01.md": "dec2b556745c635656fa0f18945c63c47120f6ff",
    "TSK_0319_POST_CR0008_INDEPENDENT_VERIFICATION_EVIDENCE_2026-09-01.md": "8a797f8257247bc3c557af10fe1d16b37c831077",
}


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


state_path = Path("CURRENT_STATE.md")
state = state_path.read_text(encoding="utf-8")
if re.search(r"^## TSK-0319 .*current accepted stable state", state, re.MULTILINE):
    print("TSK0319_STATE_ALREADY_APPLIED=PASS")
    raise SystemExit(0)

for path, expected in EXPECTED.items():
    actual = blob(path)
    if actual != expected:
        raise SystemExit(f"hash mismatch {path}: {actual} != {expected}")

for heading in (
    "## TSK-0315 current accepted stable state",
    "## TSK-0320 current accepted stable state",
    "## TSK-0628 current accepted stable state",
    "## TSK-0485 current accepted stable state",
):
    if heading not in state:
        raise SystemExit(f"required current PASS heading missing: {heading}")

evidence = Path("TSK_0319_POST_CR0008_INDEPENDENT_VERIFICATION_EVIDENCE_2026-09-01.md").read_text(encoding="utf-8")
if "**Result:** PASS" not in evidence or "33567214382 / 1" not in evidence:
    raise SystemExit("independent evidence contract mismatch")

lines = state.splitlines()
updated = [i for i, line in enumerate(lines) if line.startswith("**Updated:**")]
if len(updated) != 1:
    raise SystemExit("unexpected Updated field count")
lines[updated[0]] = "**Updated:** " + datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
section = r'''

## TSK-0319 current accepted stable state — 2026-09-01 — POST-CR-0008 REQUALIFICATION

`TSK-0319 — Design automated verification, issue-specific troubleshooting, safe reset/reinstall/remove, and point-of-need help`: **PASS** under current `ACC-0319 / VER-0319 / EVD-0319`, `DEC-0053/CR-0006`, `DEC-0054/CR-0007`, and `DEC-0055/CR-0008`.

- WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / HIGH / A3 / `AUTO_ALLOWED` / `PLANNED`; hard dependencies `TSK-0315; TSK-0320`, both strict current PASS.
- Current artifact `TSK_0319_POST_CR0008_AUTOMATED_VERIFICATION_TROUBLESHOOTING_RECOVERY_HELP_2026-09-01.md`, blob `dec2b556745c635656fa0f18945c63c47120f6ff`, commit `e323852452a4dd7a9163d98b00aca6509202fcb2`.
- Independent evidence `TSK_0319_POST_CR0008_INDEPENDENT_VERIFICATION_EVIDENCE_2026-09-01.md`, blob `8a797f8257247bc3c557af10fe1d16b37c831077`, commit `050374e470e58d7fbd30bfd85bf60eef32197da4`; run/job `33567214382 / 100053030433`: **SUCCESS**.
- Verifier proved current WBS/ACC/VER/EVD, predecessor PASS, graph `TSK-0319 -> TSK-0315/TSK-0320`, and downstream `TSK-0628 -> TSK-0319/TSK-0331`.
- ACC-0319 is satisfied for accountless and optional-account/provider/session/dashboard/device-lifecycle failure, verification, troubleshooting, recovery/removal and point-of-need-help paths, with privacy-safe checks, changed-evidence retries, and no blind replay of ambiguous consequential actions.
- The pre-CR-0006 accountless-only artifact remains historical for unchanged facts only.
- This repairs the missing direct-predecessor proof beneath current `TSK-0628`; `TSK-0331` is already current PASS. No new substantive TSK-0628/LG-06 acceptance is invented.
- **Non-inference:** L4 design PASS only; no implementation, provider integration, production diagnostics, legal/privacy compliance, real-user supportability, build, release, or launch PASS is inferred.

### Queue status after post-CR-0008 TSK-0319 requalification

Recompute HIGH L4/AUTO_ALLOWED eligibility from canonical WBS/graph, strict current PASS evidence, CR-0006 semantic validity, gates, and governing priority rules; never by task number.
'''
state_path.write_text("\n".join(lines).rstrip() + section + "\n", encoding="utf-8")
result = state_path.read_text(encoding="utf-8")
if "## TSK-0485 current accepted stable state" not in result:
    raise SystemExit("TSK-0485 preservation check failed")
if "## TSK-0319 current accepted stable state — 2026-09-01 — POST-CR-0008 REQUALIFICATION" not in result:
    raise SystemExit("TSK-0319 append verification failed")
print("TSK0319_STATE_RECONCILIATION=PASS")
