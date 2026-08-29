#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import re

PATH = Path("CURRENT_STATE.md")
MARKER = "## TSK-0323 accepted stable state — 2026-08-29"

text = PATH.read_text(encoding="utf-8")
if MARKER in text:
    print("RUNTIME_TSK0323_ALREADY_RECONCILED=PASS")
    raise SystemExit(0)

now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
updated, n = re.subn(r"(?m)^\*\*Updated:\*\* .*?$", f"**Updated:** {now}", text, count=1)
if n != 1:
    raise SystemExit("expected exactly one top-level Updated field")

section = r'''

## TSK-0323 accepted stable state — 2026-08-29

`TSK-0323 — Create versioned device and service instruction catalogue`: **PASS** under `ACC-0323 / VER-0323 / EVD-0323` and current `DEC-0052 / CR-0005` sequencing.

- Human-readable catalogue v1.0.0: `content/TSK-0323/DEVICE_SERVICE_INSTRUCTION_CATALOGUE.md`, blob `bbe9ed90b205f2ca852ebdaefedf054446dd7f91`, publication commit `412946c850640d95e3bc46e9b7bdec6c49a527f3`.
- Machine-readable catalogue v1.0.0: `content/TSK-0323/CATALOGUE.json`, blob `842e18c5666a82d53e2d348715dd6b9198daa44c`, publication commit `db04be14f428e81b7e78ed8a3ee89b0abc9a1d30`.
- Durable acceptance evidence: `TSK_0323_DEVICE_SERVICE_INSTRUCTION_CATALOGUE_EVIDENCE_2026-08-29.md`, blob `aa2f0eb00b3048d662dc2f0bb22fc3f77c9a4d45`, publication commit `cf206b1ce8d2865d3badd0595642801fd8ce37e5`.
- Successful deterministic verification: workflow `.github/workflows/verify-tsk0323.yml` at commit `83e36025f14fd235672a5e315ed823e3bb6bcfd2`; run `33268849558`; job `99143590468`; self-hosted `adguardvm` Linux x64.
- Verification results: all required metadata fields present for 12/12 records; exact source blobs pinned; WBS lifecycle/dependency/A3/AUTO_ALLOWED authority confirmed; predecessor `TSK-0322` runtime PASS confirmed; 12/12 scenario checks PASS; unsupported classes explicit; no named external service invented; accountless/privacy/i18n/claims fences PASS; repository clean.
- Initial verifier run `33268817512` / job `99143510591` failed only on a false-positive account-phrase guard; no catalogue/runtime mutation resulted. The guard was corrected and the materially different rerun passed. Closed harness defect; not a catalogue defect.
- Pre-product parent/user/participant evidence is not claimed and is non-applicable to this L4 acceptance under `DEC-0052 / CR-0005`; technical/source/scenario verification remains the basis of PASS.
- No named external service is currently hard-coded or supported by default; zero-service / S4 / S5 remains correct until a current provider-specific record satisfies the approved service contract.
- This PASS does not by itself authorize implementation, publication, production release, payment, real-user activity or launch.

### Queue status after TSK-0323 reconciliation

Do not infer the successor from task numbering. Recompute current eligible work from canonical WBS, dependencies, gates, runtime evidence and Action Authority after this state write/read-back. `TSK-0308` remains `HUMAN_ONLY` and cannot be self-executed merely because dependencies are satisfied.

### Exact next authoritative step

Reread this state from GitHub after the state commit, verify only `CURRENT_STATE.md` changed, then derive the highest-priority dependency-ready `AUTO_ALLOWED` task from current canonical authority and execute it if no gate/constraint blocks it.
'''

updated = updated.rstrip() + section + "\n"
PATH.write_text(updated, encoding="utf-8")
print("RUNTIME_TSK0323_EDIT=PASS")
