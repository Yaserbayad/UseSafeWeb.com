from __future__ import annotations

import csv
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "c50c9c119f4cd1b1ed0258292a4cda34639cf20e",
    "TSK_0497_POST_CR0008_DUAL_MODE_PRODUCT_EVENT_KPI_CATALOGUE_REVALIDATION_2026-09-02.md": "8c3b26ad0771b09a7e223ffc47f5e81b0ca217c7",
    "TSK_0497_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md": "94f05dfd9b1eb88f65d3a4173373da231f3d371f",
}

HEADING = "## TSK-0497 current accepted stable state — 2026-09-02 — POST-CR-0008 DUAL-MODE PRODUCT EVENT/KPI REVALIDATION"


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def mask_updated(text: str) -> str:
    return re.sub(r"^\*\*Updated:\*\*.*$", "**Updated:** <MASK>", text, count=1, flags=re.M)


runtime_path = Path("CURRENT_STATE.md")
old = runtime_path.read_text(encoding="utf-8")

# Idempotent read-back path for a completed prior attempt.
if HEADING in old:
    section = old.split(HEADING, 1)[1]
    required = [
        "**PASS**",
        "8c3b26ad0771b09a7e223ffc47f5e81b0ca217c7",
        "94f05dfd9b1eb88f65d3a4173373da231f3d371f",
        "33583778318",
        "100103488785",
    ]
    for value in required:
        assert value in section, value
    print("TSK0497_STATE_RECONCILIATION=ALREADY_APPLIED")
    raise SystemExit(0)

for path, expected in EXPECTED.items():
    actual = blob(path)
    if actual != expected:
        raise AssertionError(f"hash drift {path}: {actual} != {expected}")
print("TSK0497_STATE_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0497")
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "MEDIUM"
assert row["AI_Capability_A0_A4"] == "A3"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert [d.strip() for d in (row["Dependencies"] or "").split(";") if d.strip()] == ["TSK-0230"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0497", "VER-0497", "EVD-0497")
print("TSK0497_STATE_WBS_CONTRACT=PASS")

evidence = Path("TSK_0497_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md").read_text(encoding="utf-8")
for value in [
    "ACC-0497 = PASS",
    "VER-0497 = PASS",
    "EVD-0497 = SATISFIED",
    "33583778318",
    "100103488785",
    "TSK0497_CURRENT_REVALIDATION=PASS",
]:
    assert value in evidence, value
print("TSK0497_STATE_EVIDENCE_BINDING=PASS")

# Preserve all existing runtime bytes except the top-level Updated timestamp.
now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
base = re.sub(r"^\*\*Updated:\*\*.*$", f"**Updated:** {now}", old, count=1, flags=re.M)
assert mask_updated(base) == mask_updated(old)

append = f"""

{HEADING}

`TSK-0497 — Define minimal product event and KPI catalogue`: **PASS** under current `ACC-0497 / VER-0497 / EVD-0497`, current direct predecessor TSK-0230, current dual-mode Version-1 scope and the current TSK-0498 event-schema authority.

- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / MEDIUM / A3 / `AUTO_ALLOWED`; dependency exactly `TSK-0230`.
- Current artifact `TSK_0497_POST_CR0008_DUAL_MODE_PRODUCT_EVENT_KPI_CATALOGUE_REVALIDATION_2026-09-02.md`, version `2.0.0-post-CR0008`, blob `8c3b26ad0771b09a7e223ffc47f5e81b0ca217c7`, publication commit `26f8720d7a209aa70bdfb73c8ceee456570db97a`.
- Durable acceptance evidence `TSK_0497_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md`, blob `94f05dfd9b1eb88f65d3a4173373da231f3d371f`, publication commit `b67d99a29671fdb8eb5b3ab409140c3d0d83bc50`.
- Independent read-only VER-0497: workflow blob `b0ea2fc03440862496f748a1bf5701272d26b77a`; verifier script blob `c1b85b059b74b8a1d1d3b660ab75ff6c4d325cab`; run/job `33583778318 / 100103488785`; conclusion **SUCCESS**.
- Current event/KPI rule: TSK-0498 remains the single current event-schema authority; unknown events/fields fail closed. Accountless analytics remains non-identifying and short-lived at the raw-linkage boundary. Optional account/session/dashboard/device-management scope does not make account identity an analytics identity; unapproved optional-account KPI sources remain dormant until an owning approved source/event contract exists.
- Prohibited measurement remains explicit: DNS/domain/URL/browsing/search and child-activity history, raw analytics IP, session replay, attention/addictive-engagement metrics, cross-session/cross-device identity graphs, marketing/advertising profiles, raw tokens/secrets and unnecessary account/device identifiers remain outside product analytics.
- Historical TSK-0497 evidence remains preserved for compatible aggregate-by-design facts only; its pre-CR-0006 assumption that EXC-0001 remained inactive is superseded for current acceptance.
- **ACC-0497 = PASS. VER-0497 = PASS. EVD-0497 = SATISFIED.**
- **Non-inference:** this is L4 measurement/KPI contract PASS only. It does not activate telemetry, approve a datastore/vendor/new optional-account event, create a lawful basis, authorize real-user processing, prove KPI values, implement analytics/authentication, pass a lifecycle gate, publish, activate a market, launch or infer successor PASS.

### Queue status after current TSK-0497 revalidation

Recompute the executable frontier from canonical WBS/graph, current runtime evidence, artifact-specific current-validity, gates and Action Authority. Preserve valid non-uniform historical PASS records unless current evidence materially invalidates them.
"""

candidate = base + append
assert mask_updated(candidate) == mask_updated(old) + append
print("TSK0497_ALL_EXISTING_RUNTIME_BODY_PRESERVED=PASS")

runtime_path.write_text(candidate, encoding="utf-8")

written = runtime_path.read_text(encoding="utf-8")
assert HEADING in written
for value in [
    "8c3b26ad0771b09a7e223ffc47f5e81b0ca217c7",
    "94f05dfd9b1eb88f65d3a4173373da231f3d371f",
    "33583778318 / 100103488785",
    "ACC-0497 = PASS. VER-0497 = PASS. EVD-0497 = SATISFIED.",
]:
    assert value in written, value
print("TSK0497_STATE_CANDIDATE=PASS")
print("TSK0497_STATE_RECONCILIATION=PASS")
