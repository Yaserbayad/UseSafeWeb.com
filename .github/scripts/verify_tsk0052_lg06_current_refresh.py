from __future__ import annotations

import csv
import re
import subprocess
from collections import defaultdict, deque
from datetime import date
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "Plans/Master/Registers/GATES.md": "87cf9060954a82e1d5a092200d3c922f1986a5da",
    "Plans/Master/Registers/RISKS.md": "0ebb7ab97ec4d418e61eaae0fce6a35e3a9e36ec",
    "CURRENT_STATE.md": "b8baccb4c7f89e4b0029dd9b1cc686cf3eff09f2",
    "TSK_0052_LG06_CURRENT_DUAL_MODE_FREEZE_REVIEW_2026-09-01.md": "352f302164d1074547b46de9acdffba406903ac8",
    "TSK_0052_LG06_CURRENT_DUAL_MODE_FREEZE_EVIDENCE_2026-09-01.md": "2a1d408062441ac56bf7859b9d6aede10b49936b",
    "TSK_0052_LG06_POST_CR0008_CURRENT_FREEZE_REVALIDATION_2026-09-02.md": "0647adbbc03a2f2750c9ab869b5788775ea77f9e",
    "TSK_0300_POST_CR0008_PROTECTION_COPY_CORRECTION_EVIDENCE_2026-09-02.md": "a3e39896b67098ced321cb9e4b82c65c440806e4",
    "TSK_0310_POST_TSK0300_COPY_CORRECTION_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md": "34d119334e07a5d6ffe63fb893bb741d3aa0c775",
    "TSK_0308_POST_TSK0300_COPY_CORRECTION_EVIDENCE_2026-09-02.md": "959c1f47d600fefbceb2f569ed5c7c606beae48f",
    "TSK_0297_POST_CR0008_CURRENT_BRAND_GUIDELINES_EVIDENCE_2026-09-02.md": "0415b7c6719712de33822e991dd0882096c0a030",
    "TSK_0317_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md": "cd001f3ce391634e38ef0c89934cb34f4f347401",
    "TSK_0299_POST_CR0008_DUAL_MODE_VERBAL_SYSTEM_2026-09-01.md": "ff30500b933b9ecc92325659d49ea4e671d296d2",
    "TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md": "bdc6bacc424669708f410466f3cfd5527f1c2b3c",
    ".github/workflows/audit-post-tsk0045-frontier.yml": "bc999d531f4e44e396ba184616d855acb6658f6c",
}

MATRIX = {
    "product_non_goals": ["TSK-0140", "TSK-0141", "TSK-0146"],
    "requirements_traceability": ["TSK-0145"],
    "critical_conflicts": ["TSK-0043"],
    "accountless_core": ["TSK-0309", "TSK-0333", "TSK-0335", "TSK-0321", "TSK-0310", "TSK-0320"],
    "optional_account_session": ["TSK-0312", "TSK-0329", "TSK-0333", "TSK-0309"],
    "ownership_dashboard": ["TSK-0142", "TSK-0332", "TSK-0333", "TSK-0309"],
    "deletion_recovery": ["TSK-0331", "TSK-0333", "TSK-0309"],
    "privacy_security_truth": ["TSK-0229", "TSK-0312", "TSK-0331", "TSK-0335", "TSK-0333", "TSK-0309", "TSK-0300", "TSK-0320"],
    "brand_design": ["TSK-0301", "TSK-0300", "TSK-0308", "TSK-0297", "TSK-0324", "TSK-0333"],
    "content_source_support": ["TSK-0307", "TSK-0559", "TSK-0334", "TSK-0628", "TSK-0299"],
    "accessibility_i18n": ["TSK-0321", "TSK-0324", "TSK-0311", "TSK-0329", "TSK-0309", "TSK-0308"],
    "self_service": ["TSK-0628"],
}

CURRENT_LABELS = [
    "Protection verified",
    "Setup confirmed",
    "Action needed",
    "Not covered",
    "Protection status could not be verified",
    "Removed",
]


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def require_groups(text: str, groups: list[tuple[str, ...]], label: str) -> None:
    n = norm(text)
    missing = [group for group in groups if not any(norm(term) in n for term in group)]
    if missing:
        raise AssertionError(f"{label} missing semantic groups: {missing}")


for path, expected in EXPECTED.items():
    p = Path(path)
    assert p.exists(), f"missing {path}"
    actual = blob(path)
    assert actual == expected, f"hash drift {path}: {actual} != {expected}"
print("LG06_REFRESH_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
by = {r["Task_ID"]: r for r in rows if r.get("Task_ID")}
order = {r["Task_ID"]: i for i, r in enumerate(rows) if r.get("Task_ID")}
row = by["TSK-0052"]
assert row["Lifecycle_Stage"] == "L5"
assert row["AI_Capability_A0_A4"] == "A4"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert [x.strip() for x in (row.get("Dependencies") or "").split(";") if x.strip()] == ["TSK-0043", "TSK-0321", "TSK-0309", "TSK-0628"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0052", "VER-0052", "EVD-0052")
require_groups(
    row.get("Acceptance_Criteria") or "",
    [
        ("every applicable l4 acceptance requirement",),
        ("product and non-goals",),
        ("requirements are testable/traceable",),
        ("dual-mode accountless plus optional-account prototype",),
        ("account/session/dashboard/device lifecycle",),
        ("brand and design system",),
        ("responsive",),
        ("accessibility",),
        ("localization",),
        ("self-service",),
        ("no unresolved critical product/requirements conflict",),
        ("no pre-product representative-human evidence",),
    ],
    "ACC-0052",
)
print("LG06_REFRESH_WBS_CONTRACT=PASS")

gates = Path("Plans/Master/Registers/GATES.md").read_text(encoding="utf-8")
lg06_lines = [line for line in gates.splitlines() if "LG-06" in line and "Product, Brand and Experience Freeze" in line]
assert len(lg06_lines) == 1, lg06_lines
lg06 = lg06_lines[0]
require_groups(
    lg06,
    [
        ("L4",),
        ("all applicable acceptance requirements", "all applicable"),
        ("AUTO_ALLOWED",),
        ("Unlocks L5", "L5"),
        ("RSK-0002 remains OPEN", "RSK-0002"),
    ],
    "LG-06 gate row",
)
print("LG06_REFRESH_GATE_REGISTER=PASS")

# Robust runtime parser: preserve current PASS, valid non-uniform historical PASS and static WBS PASS,
# while recursively invalidating historical records whose direct predecessors have newer current proof.
state = Path("CURRENT_STATE.md").read_text(encoding="utf-8")
sec = defaultdict(list)
for idx, m in enumerate(re.finditer(r"^(##|###) (TSK-\d{4})\b.*?(?=^(?:##|###) |\Z)", state, re.M | re.S)):
    text = m.group(0)
    head = text.splitlines()[0]
    dm = re.search(r"20\d{2}-\d{2}-\d{2}", head)
    sec[m.group(2)].append({
        "pass": "**PASS" in text,
        "current": "current accepted" in head.lower(),
        "date": date.fromisoformat(dm.group(0)) if dm else None,
        "order": idx,
        "head": head,
    })
current = {t for t, ss in sec.items() if any(s["pass"] and s["current"] for s in ss)}
hist = {t for t, ss in sec.items() if any(s["pass"] for s in ss)}
static = {t for t, r in by.items() if (r.get("Execution_State") or "").strip() == "PASS"}
deps = {}
children = defaultdict(set)
for t, r in by.items():
    ds = [x.strip() for x in (r.get("Dependencies") or "").split(";") if x.strip()]
    deps[t] = ds
    for d in ds:
        children[d].add(t)

def latest(t: str, cur: bool = False):
    ds = [s["date"] for s in sec.get(t, []) if s["pass"] and s["date"] and (not cur or s["current"])]
    return max(ds) if ds else None

def newer(t: str):
    if t in current or t not in hist:
        return []
    td = latest(t)
    return [(d, latest(d, True)) for d in deps.get(t, []) if latest(d, True) and (td is None or latest(d, True) > td)]

stale = {t for t in hist if newer(t)}
effective = set(current) | {t for t in hist if t not in stale} | {t for t in static if t not in hist and t not in current}
changed = True
while changed:
    changed = False
    for t in list(effective):
        if t in current:
            continue
        if any(d not in effective for d in deps.get(t, [])):
            effective.remove(t)
            stale.add(t)
            changed = True
print(f"LG06_REFRESH_CURRENT_PASS_COUNT={len(current)}")
print(f"LG06_REFRESH_STALE_COUNT={len(stale)}")
print("LG06_REFRESH_EFFECTIVE_PARSER=PASS")

# Direct predecessors must be current/effective at gate time.
for tid in ["TSK-0043", "TSK-0321", "TSK-0309", "TSK-0628"]:
    assert tid in effective, f"LG-06 direct predecessor not effective: {tid}"
print("LG06_REFRESH_DIRECT_PREDECESSORS=PASS")

# Every matrix category used by the refreshed review must consist of effective task evidence.
for category, tids in MATRIX.items():
    missing = [tid for tid in tids if tid not in effective]
    assert not missing, f"{category} non-effective: {missing}"
    print(f"LG06_MATRIX_{category.upper()}=PASS")
print("LG06_REFRESH_MATRIX_EFFECTIVE=PASS")

# Independently recompute the dependency-ready L4 AUTO_ALLOWED frontier.
ready = []
l4_total = 0
l4_effective = 0
l4_blocked = []
for t, r in by.items():
    if (r.get("Lifecycle_Stage") or "").strip() != "L4" or (r.get("Action_Authority") or "").strip() != "AUTO_ALLOWED":
        continue
    l4_total += 1
    if t in effective:
        l4_effective += 1
        continue
    missing = [d for d in deps[t] if d not in effective]
    if not missing:
        ready.append(t)
    else:
        l4_blocked.append((t, missing))
assert not ready, f"dependency-ready L4 work remains: {ready}"
assert l4_total == l4_effective + len(l4_blocked)
assert l4_total == 89, l4_total
assert l4_effective == 86, l4_effective
assert len(l4_blocked) == 3, l4_blocked
print("LG06_REFRESH_L4_TOTAL=89")
print("LG06_REFRESH_L4_EFFECTIVE=86")
print("LG06_REFRESH_L4_DEPENDENCY_BLOCKED=3")
print("LG06_REFRESH_L4_READY=0")
print("LG06_REFRESH_L4_EXHAUSTION=PASS")

# Cross-check the external read-only audit evidence embedded in the refreshed review.
review = Path("TSK_0052_LG06_POST_CR0008_CURRENT_FREEZE_REVALIDATION_2026-09-02.md").read_text(encoding="utf-8")
for value in [
    "33594970281 / 100136470954",
    "CURRENT_PASS_COUNT=81",
    "STALE_COUNT=93",
    "L4_AUTO_TOTAL=89",
    "L4_AUTO_EFFECTIVE=86",
    "L4_AUTO_BLOCKED_OR_WAITING=3",
    "READY_COUNT=0",
]:
    assert value in review, value
print("LG06_REFRESH_EXTERNAL_L4_AUDIT_BINDING=PASS")

# Directly bind the corrected material consumers and semantic owners.
material = {
    "TSK0300": ("TSK_0300_POST_CR0008_PROTECTION_COPY_CORRECTION_EVIDENCE_2026-09-02.md", ["33592292946 / 100128578252", "ACC-0300 = PASS. VER-0300 = PASS. EVD-0300 = SATISFIED"]),
    "TSK0310": ("TSK_0310_POST_TSK0300_COPY_CORRECTION_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md", ["33592936750 / 100130472136", "BROWSER_ACCEPTANCE_CHECKS=221", "ACC-0310 = PASS. VER-0310 = PASS. EVD-0310 = SATISFIED"]),
    "TSK0308": ("TSK_0308_POST_TSK0300_COPY_CORRECTION_EVIDENCE_2026-09-02.md", ["33593810379 / 100133049388", "TSK0308_COPY_RENDERED_ACCEPTANCE=PASS", "ACC-0308 = PASS. VER-0308 = PASS. EVD-0308 = SATISFIED"]),
    "TSK0297": ("TSK_0297_POST_CR0008_CURRENT_BRAND_GUIDELINES_EVIDENCE_2026-09-02.md", ["33594493974 / 100135082837", "TSK0297_CURRENT_MANIFEST_ACTIVE_BLOBS=PASS", "ACC-0297 = PASS. VER-0297 = PASS. EVD-0297 = SATISFIED"]),
}
for name, (path, markers) in material.items():
    text = Path(path).read_text(encoding="utf-8")
    for marker in markers:
        assert marker in text, f"{name} missing {marker}"
    print(f"LG06_REFRESH_{name}_BINDING=PASS")

state_model = Path("TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md").read_text(encoding="utf-8")
verbal = Path("TSK_0299_POST_CR0008_DUAL_MODE_VERBAL_SYSTEM_2026-09-01.md").read_text(encoding="utf-8")
for label in CURRENT_LABELS:
    assert label in state_model, label
    assert label in review, f"review missing {label}"
assert "Protection has not yet been technically verified." in state_model
assert "Protection has not yet been technically verified." in review
require_groups(
    verbal,
    [
        ("accountless core stays first-class",),
        ("optional account is continuity, not stronger protection",),
        ("lifecycle operations say exactly what they change",),
    ],
    "TSK-0299 current verbal system",
)
for stale_label in ["`Verified`", "`You confirmed this is set up`", "`Status uncertain`"]:
    # Historical labels may be named only in explicit supersession explanation, never asserted as current contract.
    assert review.count(stale_label) <= 1, stale_label
print("LG06_REFRESH_CURRENT_STATE_COPY=PASS")
print("LG06_REFRESH_CURRENT_VERBAL_AUTHORITY=PASS")

# Open risks remain open and are not converted by the gate.
risks = Path("Plans/Master/Registers/RISKS.md").read_text(encoding="utf-8")
for rid in ["RSK-0002", "RSK-0005", "RSK-0015", "RSK-0017", "RSK-0022"]:
    lines = [line for line in risks.splitlines() if line.startswith(f"| {rid} ")]
    assert len(lines) == 1, rid
    assert "Open" in lines[0], f"{rid} not open"
require_groups(
    review,
    [
        ("rsk-0002 remains open/non-blocking",),
        ("rsk-0005 remains an open",),
        ("rsk-0015 remains an open",),
        ("rsk-0017 remains an open",),
        ("rsk-0022 remains an open",),
        ("unlock internal l5 architecture/security/privacy/delivery-readiness work only",),
        ("does not waive legal/privacy/consent/security/vendor requirements",),
        ("pass lg-07/lg-08/lg-09",),
    ],
    "gate risk/non-inference fence",
)
print("LG06_REFRESH_OPEN_RISKS=PASS")
print("LG06_REFRESH_NONINFERENCE=PASS")

# The old gate review/evidence remain provenance, not the current source of corrected copy/brand proof.
old_review = Path("TSK_0052_LG06_CURRENT_DUAL_MODE_FREEZE_REVIEW_2026-09-01.md").read_text(encoding="utf-8")
old_evidence = Path("TSK_0052_LG06_CURRENT_DUAL_MODE_FREEZE_EVIDENCE_2026-09-01.md").read_text(encoding="utf-8")
assert "LG-06" in old_review and "TSK-0300" in old_review and "TSK-0297" in old_review
assert "LG06_DUAL_MODE_REVIEW=PASS" in old_evidence
require_groups(
    review,
    [
        ("prior lg-06 pass cannot be used as current proof without refreshing",),
        ("candidate pass",),
        ("every applicable acc-0052 category",),
        ("all four tsk-0052 hard predecessors remain current/effective",),
    ],
    "gate refresh disposition",
)
print("LG06_REFRESH_PROVENANCE=PASS")

print("LG06_REFRESH_ACC0052=PASS")
print("LG06_REFRESH_VER0052=PASS")
print("LG06_REFRESH_EVD_READY=PASS")
print("LG06_CURRENT_FREEZE_REVALIDATION=PASS")
