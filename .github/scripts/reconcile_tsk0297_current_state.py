from __future__ import annotations

import csv
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "f12f87cec9993f811d25d5f2f34b9996c4497c67",
    "brand/guidelines/TSK-0297/README.md": "e79121fd95932a6f4b2550f5f05b84c6e9c7aeac",
    "brand/guidelines/TSK-0297/ASSET_MANIFEST.json": "c31eb9674eee9cf330b1af4764088f51e9c398fe",
    "TSK_0297_POST_CR0008_CURRENT_BRAND_GUIDELINES_REVALIDATION_2026-09-02.md": "7e472d3373fa226584dcea358ed3215f40aa2e7b",
    "TSK_0297_POST_CR0008_CURRENT_BRAND_GUIDELINES_EVIDENCE_2026-09-02.md": "0415b7c6719712de33822e991dd0882096c0a030",
    "TSK_0300_POST_CR0008_PROTECTION_COPY_CORRECTION_EVIDENCE_2026-09-02.md": "a3e39896b67098ced321cb9e4b82c65c440806e4",
    ".github/workflows/verify-tsk0297-current-guidelines.yml": "cd5bfb7b6bbb96b18a2ccdfc677787df056f11e2",
}
HEADING = "## TSK-0297 current accepted stable state — 2026-09-02 — POST-CR-0008 CURRENT BRAND-GUIDELINES REVALIDATION"


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def mask_updated(text: str) -> str:
    return re.sub(r"^\*\*Updated:\*\*.*$", "**Updated:** <MASK>", text, count=1, flags=re.M)


def sections(runtime: str, task_id: str) -> list[str]:
    pat = re.compile(rf"^(?:##|###) {re.escape(task_id)}\b.*?(?=^(?:##|###) |\Z)", re.M | re.S)
    return [m.group(0) for m in pat.finditer(runtime)]


state_path = Path("CURRENT_STATE.md")
old = state_path.read_text(encoding="utf-8")
if HEADING in old:
    section = old.split(HEADING, 1)[1]
    for value in [
        "**PASS**",
        "e79121fd95932a6f4b2550f5f05b84c6e9c7aeac",
        "c31eb9674eee9cf330b1af4764088f51e9c398fe",
        "0415b7c6719712de33822e991dd0882096c0a030",
        "33594493974 / 100135082837",
        "ACC-0297 = PASS. VER-0297 = PASS. EVD-0297 = SATISFIED.",
    ]:
        assert value in section, value
    print("TSK0297_CURRENT_STATE_RECONCILIATION=ALREADY_APPLIED")
    raise SystemExit(0)

for path, expected in EXPECTED.items():
    actual = blob(path)
    assert actual == expected, f"hash drift {path}: {actual} != {expected}"
print("TSK0297_CURRENT_STATE_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0297")
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "MEDIUM"
assert row["AI_Capability_A0_A4"] == "A3"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert [x.strip() for x in (row.get("Dependencies") or "").split(";") if x.strip()] == ["TSK-0300"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0297", "VER-0297", "EVD-0297")
print("TSK0297_CURRENT_STATE_WBS=PASS")

s300 = sections(old, "TSK-0300")
assert s300 and any("**PASS" in section for section in s300)
joined300 = "\n".join(s300)
for value in [
    "a3e39896b67098ced321cb9e4b82c65c440806e4",
    "33592292946 / 100128578252",
    "ACC-0300 = PASS. VER-0300 = PASS. EVD-0300 = SATISFIED.",
]:
    assert value in joined300, value
print("TSK0297_CURRENT_STATE_PREDECESSOR=PASS")

evidence = Path("TSK_0297_POST_CR0008_CURRENT_BRAND_GUIDELINES_EVIDENCE_2026-09-02.md").read_text(encoding="utf-8")
for value in [
    "ACC-0297 = PASS. VER-0297 = PASS. EVD-0297 = SATISFIED",
    "33594493974 / 100135082837",
    "TSK0297_CURRENT_MANIFEST_ACTIVE_BLOBS=PASS",
    "TSK0297_CURRENT_AUTHORITY_SUPERSESSION=PASS",
    "TSK0297_CURRENT_DETERMINISTIC_SELECTION=PASS",
    "TSK0297_CURRENT_DEPRECATION_TRACE=PASS",
    "TSK0297_CURRENT_NO_FONT_DELIVERY=PASS",
    "TSK0297_CURRENT_SOURCE_UNCHANGED=PASS",
]:
    assert value in evidence, value
print("TSK0297_CURRENT_STATE_EVIDENCE=PASS")

now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
base = re.sub(r"^\*\*Updated:\*\*.*$", f"**Updated:** {now}", old, count=1, flags=re.M)
assert mask_updated(base) == mask_updated(old)
append = f"""

{HEADING}

`TSK-0297 — Publish concise brand guidelines, source/editable asset library, versioning, ownership, and usage rules`: **PASS** under current `ACC-0297 / VER-0297 / EVD-0297`, corrected current predecessor TSK-0300, current TSK-0299/TSK-0320 semantic authority and preserved owner-approved SafeWeb identity/system sources.

- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / MEDIUM / A3 / `AUTO_ALLOWED`; hard dependency exactly `TSK-0300`.
- Current guideline `brand/guidelines/TSK-0297/README.md`, version `2.0.0`, blob `e79121fd95932a6f4b2550f5f05b84c6e9c7aeac`, update commit `113f9de234f14f85b8d14a29e929e32bc565989d`.
- Current manifest `brand/guidelines/TSK-0297/ASSET_MANIFEST.json`, blob `c31eb9674eee9cf330b1af4764088f51e9c398fe`, update commit `280f68a13e3d965887ae59edba66718c3d4c1c7f`.
- Current revalidation artifact `TSK_0297_POST_CR0008_CURRENT_BRAND_GUIDELINES_REVALIDATION_2026-09-02.md`, blob `7e472d3373fa226584dcea358ed3215f40aa2e7b`, publication commit `2729255c22ddf8860ec6af43e59025eca47676e4`.
- Durable evidence `TSK_0297_POST_CR0008_CURRENT_BRAND_GUIDELINES_EVIDENCE_2026-09-02.md`, blob `0415b7c6719712de33822e991dd0882096c0a030`, publication commit `32ed3d27242dd46f2ea1323969f5231a286dd17a`.
- Corrected TSK-0300 predecessor evidence blob `a3e39896b67098ced321cb9e4b82c65c440806e4` and independent run/job `33592292946 / 100128578252` are bound directly.
- Independent read-only VER-0297: verifier blob `ccdb8e65177777500cc2bbe80a68ebff0b3a6a49`, workflow blob `cd5bfb7b6bbb96b18a2ccdfc677787df056f11e2`, run/job `33594493974 / 100135082837`, conclusion **SUCCESS**.
- All 18 currently selectable manifest authority/identity/implementation/template paths were recomputed from current `main` and matched exactly; current public/product/status sources are bound to their dual-mode/copy-corrected blobs.
- Current state copy is `Protection verified`, `Setup confirmed`, `Action needed`, `Not covered`, `Protection status could not be verified`, `Removed`, with the S2 limitation `Protection has not yet been technically verified.`
- v1 package/source bindings are retained only as superseded provenance; actual asset deprecation remains traceable through the explicit `ACTIVE` / `DEPRECATED` contract and required replacement/reason/date/authorizing evidence.
- Identity masters, shared TSK-0300 tokens/components, help/partner/social sources, palette and typography stack remain unchanged. No font binary is packaged or selectable.
- Accountless core remains complete; optional account continuity is non-coercive; account/session/device ownership is not protection evidence; no automatic anonymous-to-account linkage or browsing/query/activity history is introduced.
- **ACC-0297 = PASS. VER-0297 = PASS. EVD-0297 = SATISFIED.**
- **Non-inference:** no identity redesign, implementation/build, legal/privacy completion, real-user/native-speaker validation, publication/payment/market/production/launch action, lifecycle-gate PASS or successor PASS is inferred.

### Queue status after current TSK-0297 reacceptance

Recompute the next eligible frontier from canonical WBS/graph, lifecycle/gates, current runtime evidence, current artifact validity and Action Authority. Preserve valid non-uniform historical PASS records unless current evidence actually invalidates them.
"""
candidate = base.rstrip() + append
assert mask_updated(candidate) == mask_updated(old).rstrip() + append
state_path.write_text(candidate, encoding="utf-8")
written = state_path.read_text(encoding="utf-8")
for value in [
    HEADING,
    "e79121fd95932a6f4b2550f5f05b84c6e9c7aeac",
    "c31eb9674eee9cf330b1af4764088f51e9c398fe",
    "0415b7c6719712de33822e991dd0882096c0a030",
    "33594493974 / 100135082837",
    "ACC-0297 = PASS. VER-0297 = PASS. EVD-0297 = SATISFIED.",
]:
    assert value in written, value
print("TSK0297_CURRENT_ALL_EXISTING_RUNTIME_BODY_PRESERVED=PASS")
print("TSK0297_CURRENT_STATE_CANDIDATE=PASS")
print("TSK0297_CURRENT_STATE_RECONCILIATION=PASS")
