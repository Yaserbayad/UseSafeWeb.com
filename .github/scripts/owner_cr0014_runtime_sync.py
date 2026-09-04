from datetime import datetime, timezone
from pathlib import Path

path = Path("CURRENT_STATE.md")
text = path.read_text(encoding="utf-8")

section_heading = "## Release-1 limited-test scope deferral — 2026-09-04 — OWNER DECISION ACTIVE"
assert section_heading not in text
assert "CR-0014` / `DEC-0061" not in text

old_status = "**ACTIVE / OWNER-FROZEN / POST-FREEZE CR-0011 PUBLISHED, RECONCILED, READ-BACK VERIFIED.**"
new_status = "**ACTIVE / OWNER-FROZEN / POST-FREEZE CR-0014 PUBLISHED; RUNTIME RECONCILIATION RECORDED.**"
assert text.count(old_status) == 1
text = text.replace(old_status, new_status, 1)

old_latest = "- Latest post-freeze planning change: `CR-0013` / `DEC-0060`, explicitly authorized by the Project Owner on 2026-09-04: mandatory human/Code Owner merge approval is removed from TSK-0453 and replaced by deterministic automated critical-path quality/change-policy verification; all genuine separate human/material-action boundaries remain unchanged."
assert text.count(old_latest) == 1
new_latest = (
    "- Latest post-freeze planning change: `CR-0014` / `DEC-0061`, explicitly authorized by the Project Owner on 2026-09-04: exactly `TSK-0631`, `TSK-0633`, `TSK-0634`, `TSK-0635`, `TSK-0637` and `TSK-0640` are deferred until after the controlled Release-1 test with approximately 10-20 people; they remain non-PASS and retain their dependency and ACC/VER/EVD contracts. No other task is deferred by this decision.\n"
    "- `CR-0013` / `DEC-0060` remains active and unchanged: ordinary governed AUTO_ALLOWED critical-path changes use deterministic automated quality/change-policy verification rather than mandatory human/Code Owner approval; all genuine separate human/material-action boundaries remain unchanged."
)
text = text.replace(old_latest, new_latest, 1)

lines = text.splitlines()
assert lines[2].startswith("**Updated:** ")
lines[2] = "**Updated:** " + datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
text = "\n".join(lines) + "\n"

section = """## Release-1 limited-test scope deferral — 2026-09-04 — OWNER DECISION ACTIVE

Release 1 is a controlled test with approximately 10-20 people.

Under `DEC-0061 / CR-0014`, the following tasks are **WAITING / DEFERRED** until after Release 1:
- `TSK-0631` — AI-assisted support.
- `TSK-0633` — rehearse exceptional support situations.
- `TSK-0634` — periodic focused parent research.
- `TSK-0635` — formal feedback collection/classification.
- `TSK-0637` — support quality/workload/root-cause review.
- `TSK-0640` — 14/30/90-day persistence measurement.

These tasks are not PASS, waived or deleted. Their dependencies and current acceptance, verification and evidence contracts remain intact.

No other task is deferred by this decision. `TSK-0630`, `TSK-0632`, `TSK-0636`, `TSK-0638`, `TSK-0639` and `TSK-0641` remain undeferred. `TSK-0641` remains dependency-blocked while `TSK-0633` is deferred because its hard predecessor is not PASS.

Reactivation condition: after Release-1 controlled testing is complete, or earlier only by explicit Project Owner instruction.

Planning publication: PR `#111`; canonical merge `2ac022bd71326fda69d1db0ff61b953ad31eaed9`; validated WBS blob `1806751a53087d39e27360a885dab7c05abb49d7`; decisions blob `b53ed6c9ad468225772e37b33e951fb74de1153c`; change-control blob `224e9d9a8f5349be92081d768afa84bb116b7393`. Pre-publication validation passed with 641 tasks and 858 dependency edges; exactly the six named WBS rows changed, and only `Plan_Status`, `Trigger`, `Relative_Timing` and `Notes` changed. All four exact-head PR acceptance workflows passed. The canonical merge triggered 8 push workflows and all 8 reached terminal SUCCESS.

Publication also repaired stale whole-WBS snapshot pins in the existing `TSK-0629` and `TSK-0359` acceptance workflows. Those repairs removed only obsolete global WBS hash assertions, set checkout credentials non-persistent, and preserved the actual repository/master-plan validators, package/version pins, build, contract, audit and browser acceptance checks; all repaired exact-head checks passed. No product/runtime source changed.

**Non-inference / fences:** this decision creates no PASS, deployment, participant processing, telemetry activation, service mutation/removal/revocation, payment, production/public activation, geographic/market activation, launch, live-device/profile/certificate action or other material-action authority.
"""

path.write_text(text.rstrip() + "\n\n" + section, encoding="utf-8")
