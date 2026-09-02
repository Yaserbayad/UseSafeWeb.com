from __future__ import annotations

import csv
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "960f8449943552a6c7a8b747b0d9b072f8eaa507",
    "TSK_0308_POST_TSK0300_COPY_CORRECTION_REVALIDATION_2026-09-02.md": "76d652481a993469aaf175c08893e829ee01dad7",
    "TSK_0308_POST_TSK0300_COPY_CORRECTION_EVIDENCE_2026-09-02.md": "959c1f47d600fefbceb2f569ed5c7c606beae48f",
    "prototype/TSK-0308/DUAL_MODE_ADDENDUM.md": "86461ef4baac27cf4cfd906f7ed464781186e78d",
    "prototype/TSK-0308/dual-mode-reference.html": "7e522e23e43d04da3facf53747ad9b245e66ef62",
    "TSK_0300_POST_CR0008_PROTECTION_COPY_CORRECTION_EVIDENCE_2026-09-02.md": "a3e39896b67098ced321cb9e4b82c65c440806e4",
    "TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md": "bdc6bacc424669708f410466f3cfd5527f1c2b3c",
    ".github/workflows/verify-tsk0308-post-copy-correction.yml": "f35da0b77340e68b3247eb1a547c11ba02a6faa4",
}

HEADING = "## TSK-0308 current accepted stable state — 2026-09-02 — POST-TSK-0300 PROTECTION-COPY CORRECTION REVALIDATION"


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
        "76d652481a993469aaf175c08893e829ee01dad7",
        "959c1f47d600fefbceb2f569ed5c7c606beae48f",
        "33593810379 / 100133049388",
        "TSK0308_COPY_RENDERED_ACCEPTANCE=PASS",
        "ACC-0308 = PASS. VER-0308 = PASS. EVD-0308 = SATISFIED.",
    ]:
        assert value in section, value
    print("TSK0308_POST_COPY_STATE_RECONCILIATION=ALREADY_APPLIED")
    raise SystemExit(0)

for path, expected in EXPECTED.items():
    actual = blob(path)
    assert actual == expected, f"hash drift {path}: {actual} != {expected}"
print("TSK0308_POST_COPY_STATE_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0308")
deps = [x.strip() for x in (row.get("Dependencies") or "").split(";") if x.strip()]
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "HIGH"
assert row["AI_Capability_A0_A4"] == "A3"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert deps == ["TSK-0309", "TSK-0300"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0308", "VER-0308", "EVD-0308")
print("TSK0308_POST_COPY_STATE_WBS=PASS")

for tid in deps:
    ss = sections(old, tid)
    assert ss and any("**PASS" in s for s in ss), f"missing durable PASS {tid}"
s300 = "\n".join(sections(old, "TSK-0300"))
for value in [
    "a3e39896b67098ced321cb9e4b82c65c440806e4",
    "33592292946 / 100128578252",
    "ACC-0300 = PASS. VER-0300 = PASS. EVD-0300 = SATISFIED.",
]:
    assert value in s300, value
print("TSK0308_POST_COPY_STATE_PREDECESSORS=PASS")

evidence = Path("TSK_0308_POST_TSK0300_COPY_CORRECTION_EVIDENCE_2026-09-02.md").read_text(encoding="utf-8")
for value in [
    "ACC-0308 = PASS. VER-0308 = PASS. EVD-0308 = SATISFIED",
    "33593810379 / 100133049388",
    "TSK0308_COPY_VIEWPORT_320=PASS",
    "TSK0308_COPY_VIEWPORT_1440=PASS",
    "TSK0308_COPY_BROWSER_CURRENT_STATE_COPY=PASS",
    "TSK0308_COPY_RENDERED_ACCEPTANCE=PASS",
    "TSK0308_COPY_SOURCE_UNCHANGED=PASS",
]:
    assert value in evidence, value
print("TSK0308_POST_COPY_STATE_EVIDENCE=PASS")

now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
base = re.sub(r"^\*\*Updated:\*\*.*$", f"**Updated:** {now}", old, count=1, flags=re.M)
assert mask_updated(base) == mask_updated(old)

append = f"""

{HEADING}

`TSK-0308 — Create the shared responsive design system for public and product surfaces`: **PASS** under current `ACC-0308 / VER-0308 / EVD-0308`, current direct predecessors TSK-0309 and corrected TSK-0300, current TSK-0320 protection-state semantics, and preserved owner-approved responsive/design-system provenance.

- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / HIGH / A3 / `AUTO_ALLOWED`; hard dependencies exactly `TSK-0309; TSK-0300`.
- Correction artifact `TSK_0308_POST_TSK0300_COPY_CORRECTION_REVALIDATION_2026-09-02.md`, blob `76d652481a993469aaf175c08893e829ee01dad7`, publication commit `51d039c9d97f2ff48a048201ef9b23673021ebfa`.
- Durable correction evidence `TSK_0308_POST_TSK0300_COPY_CORRECTION_EVIDENCE_2026-09-02.md`, blob `959c1f47d600fefbceb2f569ed5c7c606beae48f`, publication commit `1f65c0d817f7b016103926f72f5e8fe10f8fb2d9`.
- Corrected active addendum blob `86461ef4baac27cf4cfd906f7ed464781186e78d`; corrected rendered reference blob `7e522e23e43d04da3facf53747ad9b245e66ef62`.
- Current visible protection-state examples now use `configured/parent-confirmed` / `Setup confirmed`, `protected/verified` / `Protection verified`, `uncertain/error` / `Protection status could not be verified`, and current `Not covered`; S2 explicitly says `Protection has not yet been technically verified.`
- The active reference no longer presents `You confirmed this is set up`, `Verified`, or `Status uncertain` as current primary state labels.
- Corrected TSK-0300 predecessor evidence blob `a3e39896b67098ced321cb9e4b82c65c440806e4` and independent run/job `33592292946 / 100128578252` are bound directly.
- Independent read-only VER-0308: script blob `3c364d588fd4d89407c2db8223cf4fe34f0b865f`, workflow blob `f35da0b77340e68b3247eb1a547c11ba02a6faa4`, run/job `33593810379 / 100133049388`, conclusion **SUCCESS**.
- Rendered current checks: 320/768/1024/1440 PASS; `TSK0308_COPY_BROWSER_CURRENT_STATE_COPY=PASS`; accountless-primary/optional-account-secondary/provider-fallback/identity-protection/lifecycle/RTL/focus/no-overflow/console checks PASS; `TSK0308_COPY_RENDERED_ACCEPTANCE=PASS`; `TSK0308_COPY_SOURCE_UNCHANGED=PASS`.
- Preserved unchanged: historical DS-01–DS-13 candidate/CSS/reference/map/trace/evidence, dual-mode additive CSS, shared TSK-0300 tokens/components, SafeWeb identity, DS-14–DS-17 architecture, responsive/accessibility/localization and lifecycle/privacy boundaries.
- **ACC-0308 = PASS. VER-0308 = PASS. EVD-0308 = SATISFIED.**
- **Non-inference:** no authentication/session/datastore implementation, legal/privacy completion, real-user processing, publication/payment/market/production/launch action, lifecycle-gate PASS or successor PASS is inferred.

### Queue status after corrected TSK-0308 reacceptance

Recompute the executable frontier from canonical WBS/graph, current runtime evidence, artifact-specific current-validity checks, gates and Action Authority. Preserve unrelated current/historical PASS only where current evidence remains valid.
"""

candidate = base.rstrip() + append
assert mask_updated(candidate) == mask_updated(old).rstrip() + append
state_path.write_text(candidate, encoding="utf-8")
written = state_path.read_text(encoding="utf-8")
for value in [
    HEADING,
    "76d652481a993469aaf175c08893e829ee01dad7",
    "959c1f47d600fefbceb2f569ed5c7c606beae48f",
    "33593810379 / 100133049388",
    "TSK0308_COPY_RENDERED_ACCEPTANCE=PASS",
    "ACC-0308 = PASS. VER-0308 = PASS. EVD-0308 = SATISFIED.",
]:
    assert value in written, value
print("TSK0308_POST_COPY_ALL_EXISTING_RUNTIME_BODY_PRESERVED=PASS")
print("TSK0308_POST_COPY_STATE_CANDIDATE=PASS")
print("TSK0308_POST_COPY_STATE_RECONCILIATION=PASS")
