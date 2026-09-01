from __future__ import annotations

import hashlib
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

EXPECTED = {
    "CURRENT_STATE.md": "d427e03dfe343187c17fe4383cd3893084a599d3",
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "TSK_0298_EVIDENCE_GROUNDED_BRAND_STRATEGY_2026-08-29.md": "73d8587ef9bb37d92b44f102d5a33545b416c44b",
    "TSK_0299_POST_CR0008_DUAL_MODE_VERBAL_SYSTEM_2026-09-01.md": "ff30500b933b9ecc92325659d49ea4e671d296d2",
    "TSK_0299_POST_CR0008_ACCEPTANCE_EVIDENCE_2026-09-01.md": "63190056e7e20a8adb3968a4b503788b8ed02cec",
}

HEADING = "## TSK-0299 current accepted stable state — 2026-09-01 — POST-CR-0008 REQUALIFICATION"
PROTECTED = (
    "## TSK-0485 current accepted stable state",
    "## TSK-0318 current accepted stable state",
    "## TSK-0319 current accepted stable state",
)


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def extract_section(text: str, heading_prefix: str) -> str:
    match = re.search(r"^" + re.escape(heading_prefix) + r".*$", text, re.MULTILINE)
    if not match:
        raise SystemExit(f"protected/current heading missing: {heading_prefix}")
    start = match.start()
    nxt = re.search(r"^## ", text[match.end():], re.MULTILINE)
    end = match.end() + nxt.start() if nxt else len(text)
    return text[start:end]


def section_sha(text: str, heading_prefix: str) -> str:
    return hashlib.sha256(extract_section(text, heading_prefix).encode("utf-8")).hexdigest()


state_path = Path("CURRENT_STATE.md")
state = state_path.read_text(encoding="utf-8")

# Exact idempotent already-applied outcome is safe; a partial/ambiguous duplicate is not.
if HEADING in state:
    if state.count(HEADING) == 1 and "TSK_0299_POST_CR0008_ACCEPTANCE_EVIDENCE_2026-09-01.md" in extract_section(state, HEADING):
        print("TSK0299_STATE_ALREADY_APPLIED=PASS")
        raise SystemExit(0)
    raise SystemExit("ambiguous existing TSK-0299 current-state section")

for path, expected in EXPECTED.items():
    actual = blob(path)
    if actual != expected:
        raise SystemExit(f"hash mismatch {path}: {actual} != {expected}")

for heading in (
    "## TSK-0298 accepted stable state",
    "## TSK-0320 current accepted stable state",
    *PROTECTED,
):
    if heading not in state:
        raise SystemExit(f"required current PASS heading missing: {heading}")

artifact = Path("TSK_0299_POST_CR0008_DUAL_MODE_VERBAL_SYSTEM_2026-09-01.md").read_text(encoding="utf-8")
evidence = Path("TSK_0299_POST_CR0008_ACCEPTANCE_EVIDENCE_2026-09-01.md").read_text(encoding="utf-8")
if "**TSK-0299 remains non-PASS until independent verification" not in artifact:
    raise SystemExit("candidate pre-state contract mismatch")
if "**Disposition:** PASS — subject to durable `CURRENT_STATE.md` synchronization" not in evidence:
    raise SystemExit("acceptance evidence disposition mismatch")
if "33571984135" not in evidence or "100067714979" not in evidence or "TSK0299_ACCEPTANCE=PASS" not in evidence:
    raise SystemExit("independent verification evidence mismatch")

protected_before = {h: section_sha(state, h) for h in PROTECTED}

lines = state.splitlines()
updated = [i for i, line in enumerate(lines) if line.startswith("**Updated:**")]
if len(updated) != 1:
    raise SystemExit("unexpected Updated field count")
lines[updated[0]] = "**Updated:** " + datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

section = r'''

## TSK-0299 current accepted stable state — 2026-09-01 — POST-CR-0008 REQUALIFICATION

`TSK-0299 — Define tone, voice, terminology, trust language, protection-state language, and communication examples`: **PASS** under current `ACC-0299 / VER-0299 / EVD-0299`, `DEC-0052/CR-0005`, `DEC-0053/CR-0006`, `DEC-0054/CR-0007`, and `DEC-0055/CR-0008`.

- WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / HIGH / A3 / `AUTO_ALLOWED` / `PLANNED`; hard dependency `TSK-0298`, current accepted PASS.
- Current artifact `TSK_0299_POST_CR0008_DUAL_MODE_VERBAL_SYSTEM_2026-09-01.md`, version `2.0.0-post-cr0008`, blob `ff30500b933b9ecc92325659d49ea4e671d296d2`, publication commit `284a566c9ff282e35bc2500f1060a0869262bb37`.
- Durable acceptance evidence `TSK_0299_POST_CR0008_ACCEPTANCE_EVIDENCE_2026-09-01.md`, blob `63190056e7e20a8adb3968a4b503788b8ed02cec`, publication commit `c2d057159c02c63716b29fbdee50abc8ca8073b0`.
- Independent read-only verification workflow `.github/workflows/verify-tsk0299-post-cr0008.yml`, blob `fb3d23d300c6154d95f23ae4d8275ddb22f969b8`; run/job `33571984135 / 100067714979`: **SUCCESS** on GitHub-hosted Ubuntu 24.04 with `contents: read`.
- ACC-0299 is satisfied for current plain-language, child-aware, calm/non-alarmist, non-technical-by-default parent-facing voice; current approved claims/non-surveillance controls; and reusable public/product/account/dashboard/help/status/localized semantics.
- CR-0006 repair is explicit: the complete accountless core stays first-class while optional sign-in/session/dashboard/device management is described as bounded continuity, never a core-value gate or stronger-protection signal.
- Current TSK-0320 S1–S6 copy is preserved exactly: account ownership, dashboard/device registration, configuration presence or parent confirmation never substitute for qualifying technical verification.
- Anonymous J0/J1 state is not automatically linked, promoted, imported or extended by sign-in. No browsing/query/activity history, child account/profile or broad DNS administration is introduced.
- Start-over, logout, unlink/revoke, device-record deletion, account deletion and physical UseSafeWeb DNS removal have distinct consequence language; ambiguous consequential results require reconciliation rather than blind replay.
- English/Turkish/Arabic plus RTL semantics preserve evidence strength, actor, optionality, scope, uncertainty and destructive-operation object meaning; language availability does not activate a market.
- `RSK-0002` remains OPEN. Under DEC-0052/CR-0005, representative-parent comprehension validation begins only in the authorized L8 integrated-product stage; no pre-L8 human-validation or deferred legal/privacy completion is claimed.
- TSK-0301 remains independently dependent on both `TSK-0302` and current TSK-0299. No successor/gate becomes PASS from this state update.
- **Non-inference:** L4 verbal-system design PASS only; no implementation/build, provider acceptance, legal/privacy completion, public publication, participant activation, payment, named-market activation, LG-06, production behavior or launch PASS is inferred.

### Queue status after post-CR-0008 TSK-0299 requalification

Recompute the current executable frontier from canonical WBS/graph, strict current PASS and CR-0006/CR-0008 artifact validity. In particular, independently resolve current TSK-0302 validity before treating TSK-0301 as dependency-complete, and compare that chain against reopened TSK-0316 under the governing priority rules. Preserve TSK-0485 and synchronized TSK-0318/TSK-0319 accepted states unchanged.
'''

result = "\n".join(lines).rstrip() + section + "\n"
for h, before in protected_before.items():
    after = section_sha(result, h)
    if after != before:
        raise SystemExit(f"protected section changed: {h}: {before} != {after}")

if result.count(HEADING) != 1:
    raise SystemExit("TSK-0299 append verification failed")
state_path.write_text(result, encoding="utf-8")

for h, before in protected_before.items():
    after = section_sha(state_path.read_text(encoding="utf-8"), h)
    if after != before:
        raise SystemExit(f"post-write protected section changed: {h}")

print("TSK0485_SECTION_PRESERVED=PASS")
print("TSK0318_SECTION_PRESERVED=PASS")
print("TSK0319_SECTION_PRESERVED=PASS")
print("TSK0299_STATE_RECONCILIATION=PASS")
