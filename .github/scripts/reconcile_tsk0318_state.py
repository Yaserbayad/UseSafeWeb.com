from __future__ import annotations

import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

EXPECTED = {
    "CURRENT_STATE.md": "c4594837623b2462fea250fb360aed8fcabc90f3",
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "TSK_0318_POST_CR0008_DUAL_MODE_PUBLIC_PRODUCT_SETUP_IA_2026-09-01.md": "975e2e7a8e85e9408e0bbbc2be226f3fdd012db3",
    "TSK_0318_POST_CR0008_ACCEPTANCE_EVIDENCE_2026-09-01.md": "dccefe56070dc7e44d07fadee5307531e1140dba",
}

HEADING = "## TSK-0318 current accepted stable state — 2026-09-01 — POST-CR-0008 REQUALIFICATION"


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def extract_section(text: str, heading: str) -> str:
    start = text.find(heading)
    if start < 0:
        raise SystemExit(f"required section missing: {heading}")
    match = re.search(r"\n## ", text[start + len(heading):])
    if match:
        end = start + len(heading) + match.start()
        return text[start:end].rstrip()
    return text[start:].rstrip()


state_path = Path("CURRENT_STATE.md")
state = state_path.read_text(encoding="utf-8")

# Idempotent completion path: verify the expected accepted section and preservation anchors.
if HEADING in state:
    for required in (
        "`TSK-0318 — Design the public website IA and product/setup IA as distinct but connected systems`: **PASS**",
        "`975e2e7a8e85e9408e0bbbc2be226f3fdd012db3`",
        "`dccefe56070dc7e44d07fadee5307531e1140dba`",
        "`33571019275 / 100064770925`: **SUCCESS**",
        "## TSK-0485 current accepted stable state",
        "## TSK-0319 current accepted stable state — 2026-09-01 — POST-CR-0008 REQUALIFICATION",
    ):
        if required not in state:
            raise SystemExit(f"already-applied state contract mismatch: {required}")
    print("TSK0318_STATE_ALREADY_APPLIED=PASS")
    raise SystemExit(0)

for path, expected in EXPECTED.items():
    actual = blob(path)
    if actual != expected:
        raise SystemExit(f"hash mismatch {path}: {actual} != {expected}")

for heading in (
    "## TSK-0315 current accepted stable state",
    "## TSK-0229 current accepted stable state",
    "## TSK-0331 current accepted stable state",
    "## TSK-0485 current accepted stable state",
    "## TSK-0319 current accepted stable state — 2026-09-01 — POST-CR-0008 REQUALIFICATION",
):
    if heading not in state:
        raise SystemExit(f"required current PASS heading missing: {heading}")

# Capture protected accepted-state sections before mutation and prove they are unchanged after it.
protected_headings = (
    "## TSK-0485 current accepted stable state",
    "## TSK-0319 current accepted stable state — 2026-09-01 — POST-CR-0008 REQUALIFICATION",
)
protected = {h: extract_section(state, h) for h in protected_headings}

evidence = Path("TSK_0318_POST_CR0008_ACCEPTANCE_EVIDENCE_2026-09-01.md").read_text(encoding="utf-8")
for required in (
    "ACC-0318 / VER-0318 / EVD-0318",
    "33571019275",
    "100064770925",
    "TSK0318_ACCEPTANCE=PASS",
    "975e2e7a8e85e9408e0bbbc2be226f3fdd012db3",
    "TSK-0628`: **current PASS**",
    "TSK-0229`: **current PASS**",
):
    if required not in evidence:
        raise SystemExit(f"acceptance evidence contract mismatch: {required}")

lines = state.splitlines()
updated = [i for i, line in enumerate(lines) if line.startswith("**Updated:**")]
if len(updated) != 1:
    raise SystemExit("unexpected Updated field count")
lines[updated[0]] = "**Updated:** " + datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

section = r'''

## TSK-0318 current accepted stable state — 2026-09-01 — POST-CR-0008 REQUALIFICATION

`TSK-0318 — Design the public website IA and product/setup IA as distinct but connected systems`: **PASS** under current `ACC-0318 / VER-0318 / EVD-0318`, `DEC-0053/CR-0006`, `DEC-0054/CR-0007`, and `DEC-0055/CR-0008`.

- WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / HIGH / A3 / `AUTO_ALLOWED` / `PLANNED`; hard dependency `TSK-0315`, strict current PASS under its post-CR-0007 dual-mode service blueprint.
- Current artifact `TSK_0318_POST_CR0008_DUAL_MODE_PUBLIC_PRODUCT_SETUP_IA_2026-09-01.md`, version `2.0.0-post-cr0008`, blob `975e2e7a8e85e9408e0bbbc2be226f3fdd012db3`, publication commit `31cbd3af8175dd8c82d9e58828b6cf0ee4a1f168`.
- Durable acceptance evidence `TSK_0318_POST_CR0008_ACCEPTANCE_EVIDENCE_2026-09-01.md`, blob `dccefe56070dc7e44d07fadee5307531e1140dba`, publication commit `c69b81415a8f39f3b876e276129f9498c0af0573`.
- Independent read-only verification run/job `33571019275 / 100064770925`: **SUCCESS** on GitHub-hosted Ubuntu 24.04 with `contents: read`. WBS contract, current predecessor, graph references, dual-mode scope, 38 complete page/screen IA rows, SEO/privacy/accessibility, lifecycle-operation separation, scope negatives and successor-impact assertions all PASS.
- Current IA has 9 public surfaces, 14 accountless operational setup surfaces and 15 optional parent-account/dashboard/device-lifecycle surfaces. Each has one purpose, entry, exit/next action, content owner, explicit index intent, privacy requirement and accessibility requirement.
- The complete core path remains usable without login. Optional sign-in/session/dashboard/device management is represented without coercion; auth cancellation/failure/provider outage preserves an accountless-capable continuation.
- J0/J1 anonymous state remains separate from persistent account/device state. No automatic anonymous-to-account linkage/promotion, browsing/query/activity history, child account/profile, raw AdGuard administration/query-log surface, payment gate before core value, or overall safety-score/all-clear route is authorized.
- Logout, revoke/unlink, dashboard-device-record deletion, account deletion, anonymous-state reset/deletion and physical DNS removal are distinct IA operations and cannot claim one another completed.
- Historical TSK-0318 evidence remains preserved for compatible facts only; its explicit pre-CR-0006 Login/Dashboard/Account exclusions and no-account/session-navigation clause are superseded for current acceptance.
- TSK-0229 and TSK-0628 remain current PASS. TSK-0299 and TSK-0316 remain separately reopened current-scope requalification candidates; this PASS does not silently reclassify them.
- TSK-0310 retains its accepted accountless public-to-setup core evidence for its own current ACC; this TSK-0318 PASS does not claim the historical prototype implements the optional account/dashboard branch. TSK-0311 retains its own localization/externalization acceptance boundary.
- **Non-inference:** L4 IA design PASS only; no LG-06/gate, architecture, authentication-provider, persistent-schema, implementation, legal/privacy completion, participant, payment, production, publication, market or launch PASS is inferred.

### Queue status after post-CR-0008 TSK-0318 requalification

Recompute the current executable frontier from canonical WBS/graph, strict current PASS evidence, CR-0006/CR-0008 artifact validity, gates, dependency-chain impact, customer value, priority and WBS order. Preserve current TSK-0485 and TSK-0319 accepted states unchanged.
'''

state_path.write_text("\n".join(lines).rstrip() + section + "\n", encoding="utf-8")
result = state_path.read_text(encoding="utf-8")
if HEADING not in result:
    raise SystemExit("TSK-0318 append verification failed")
for heading, before in protected.items():
    after = extract_section(result, heading)
    if after != before:
        raise SystemExit(f"protected accepted-state section changed: {heading}")
print("TSK0485_SECTION_PRESERVED=PASS")
print("TSK0319_SECTION_PRESERVED=PASS")
print("TSK0318_STATE_RECONCILIATION=PASS")
