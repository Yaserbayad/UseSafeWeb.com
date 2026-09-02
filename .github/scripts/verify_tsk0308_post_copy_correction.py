from __future__ import annotations

import csv
import re
import subprocess
from html.parser import HTMLParser
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "960f8449943552a6c7a8b747b0d9b072f8eaa507",
    "prototype/TSK-0309/BASELINE.md": "6302bb2509d04c8269e4df112140d7c416e42eff",
    "TSK_0300_POST_CR0008_PROTECTION_COPY_CORRECTION_EVIDENCE_2026-09-02.md": "a3e39896b67098ced321cb9e4b82c65c440806e4",
    "TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md": "bdc6bacc424669708f410466f3cfd5527f1c2b3c",
    "brand/system/TSK-0300/tokens.css": "cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f",
    "brand/system/TSK-0300/components.css": "831e92a74b6dda04252d93242cb33bd491a02381",
    "brand/identity/TSK-0301/safeweb-wordmark-primary.svg": "f93958e3e4a16f9056693072c1b9b8b31fcda852",
    "prototype/TSK-0308/SHARED_RESPONSIVE_DESIGN_SYSTEM_CANDIDATE.md": "cd5c217ca7882589617dc94701fe5b6ac0eaf8d4",
    "prototype/TSK-0308/candidate.css": "de5571379ff240f36b5aecd50f555a07176dbd32",
    "prototype/TSK-0308/reference.html": "fe86b9ec2b5d5e5e11cf4d135baca69f6b4a5862",
    "prototype/TSK-0308/DESIGN_SYSTEM_MAP.json": "cd83279cdf5381cd7dae3feb177439158c1f9197",
    "prototype/TSK-0308/REQUIREMENT_INTERFACE_TRACE.md": "5e34ce9c192c6af65ba493cb356adb964c3d30b6",
    "TSK_0308_SHARED_RESPONSIVE_DESIGN_SYSTEM_ACCEPTANCE_EVIDENCE_2026-08-29.md": "343961f30bc46a20762ad2b0108a4afe9593e5a3",
    "TSK_0308_POST_CR0008_DUAL_MODE_SHARED_RESPONSIVE_DESIGN_SYSTEM_REVALIDATION_2026-09-02.md": "90dce398ae86238abf5cf141acac47d78bf085b8",
    "TSK_0308_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md": "f280154e45fccbcaab51a2fdca2dd3c33edbb99a",
    "prototype/TSK-0308/DUAL_MODE_ADDENDUM.md": "86461ef4baac27cf4cfd906f7ed464781186e78d",
    "prototype/TSK-0308/dual-mode-addendum.css": "67fe4f16a1aca56c7cd03ab28ec807a52e3e23e8",
    "prototype/TSK-0308/dual-mode-reference.html": "7e522e23e43d04da3facf53747ad9b245e66ef62",
    "TSK_0308_POST_TSK0300_COPY_CORRECTION_REVALIDATION_2026-09-02.md": "76d652481a993469aaf175c08893e829ee01dad7",
}


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def require_groups(text: str, groups: list[tuple[str, ...]], label: str) -> None:
    n = norm(text)
    missing = [group for group in groups if not any(norm(term) in n for term in group)]
    if missing:
        raise AssertionError(f"{label} missing semantic groups: {missing}")


def sections(runtime: str, task_id: str) -> list[str]:
    pat = re.compile(rf"^(?:##|###) {re.escape(task_id)}\b.*?(?=^(?:##|###) |\Z)", re.M | re.S)
    return [m.group(0) for m in pat.finditer(runtime)]


for path, expected in EXPECTED.items():
    p = Path(path)
    assert p.exists(), f"missing {path}"
    actual = blob(path)
    assert actual == expected, f"hash drift {path}: {actual} != {expected}"
print("TSK0308_COPY_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0308")
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "HIGH"
assert row["AI_Capability_A0_A4"] == "A3"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert [x.strip() for x in (row.get("Dependencies") or "").split(";") if x.strip()] == ["TSK-0309", "TSK-0300"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0308", "VER-0308", "EVD-0308")
require_groups(
    row.get("Acceptance_Criteria") or "",
    [
        ("content",), ("error",), ("loading",), ("verification",), ("uncertain",),
        ("recovery",), ("tokens",), ("accessibility",), ("localization",), ("implementation",),
    ],
    "ACC-0308",
)
print("TSK0308_COPY_WBS=PASS")

runtime = Path("CURRENT_STATE.md").read_text(encoding="utf-8")
for tid in ["TSK-0309", "TSK-0300"]:
    ss = sections(runtime, tid)
    assert ss and any("**PASS" in s for s in ss), f"missing durable PASS {tid}"
s300 = "\n".join(sections(runtime, "TSK-0300"))
for value in [
    "a3e39896b67098ced321cb9e4b82c65c440806e4",
    "33592292946 / 100128578252",
    "ACC-0300 = PASS. VER-0300 = PASS. EVD-0300 = SATISFIED.",
]:
    assert value in s300, value
print("TSK0308_COPY_CURRENT_PREDECESSORS=PASS")
print("TSK0308_COPY_TSK0300_CORRECTED_BINDING=PASS")

baseline = Path("prototype/TSK-0309/BASELINE.md").read_text(encoding="utf-8")
require_groups(
    baseline,
    [
        ("complete core setup/protection/recovery journey remains usable without login",),
        ("optional parent google sign-in/account/session continuity",),
        ("lightweight dashboard/device-management",),
        ("account/device ownership never substitutes for technical dns/protection map verification",),
        ("account deletion does not claim dns removal",),
    ],
    "TSK-0309 dual mode",
)
print("TSK0308_COPY_TSK0309=PASS")

state_model = Path("TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md").read_text(encoding="utf-8")
for label in [
    "Protection verified",
    "Setup confirmed",
    "Action needed",
    "Not covered",
    "Protection status could not be verified",
    "Removed",
]:
    assert label in state_model, label
assert "Protection has not yet been technically verified." in state_model
print("TSK0308_COPY_TSK0320=PASS")

historical = Path("prototype/TSK-0308/SHARED_RESPONSIVE_DESIGN_SYSTEM_CANDIDATE.md").read_text(encoding="utf-8")
historical_evd = Path("TSK_0308_SHARED_RESPONSIVE_DESIGN_SYSTEM_ACCEPTANCE_EVIDENCE_2026-08-29.md").read_text(encoding="utf-8")
for i in range(1, 14):
    assert re.search(rf"^### DS-{i:02d}\b", historical, re.M), f"historical DS-{i:02d} missing"
require_groups(
    historical_evd,
    [
        ("13/13 component contracts",), ("6/6 required state classes",), ("6/6 protection states",),
        ("320/768/1024/1440",), ("visible focus",), ("reduced motion",), ("rtl/ltr",),
    ],
    "historical acceptance",
)
print("TSK0308_COPY_HISTORICAL_PROVENANCE=PASS")

old_current = Path("TSK_0308_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md").read_text(encoding="utf-8")
for value in [
    "33585488537", "100108650200", "TSK0308_RENDERED_CURRENT_ACCEPTANCE=PASS", "TSK0308_SOURCE_UNCHANGED=PASS"
]:
    assert value in old_current, value
print("TSK0308_COPY_PRIOR_CURRENT_MECHANICS=PASS")

addendum = Path("prototype/TSK-0308/DUAL_MODE_ADDENDUM.md").read_text(encoding="utf-8")
require_groups(
    addendum,
    [
        ("accountless core remains complete",),
        ("account use is optional and non-coercive",),
        ("protected/verified",),
        ("protection verified",),
        ("visible protection copy follows current tsk-0320/tsk-0300 semantics",),
        ("provider/datastore failure preserves accountless continuation",),
        ("lifecycle operations stay distinct",),
        ("current tsk-0320 protection-state semantics",),
    ],
    "corrected addendum",
)
for i, name in [(14, "OptionalAccountEntry"), (15, "SessionStatus"), (16, "DeviceManagementList"), (17, "AccountLifecycleActions")]:
    assert re.search(rf"^### DS-{i}\b", addendum, re.M), f"DS-{i} missing"
    assert name in addendum, name
print("TSK0308_COPY_ADDENDUM=PASS")

css = Path("prototype/TSK-0308/dual-mode-addendum.css").read_text(encoding="utf-8")
assert not re.search(r"#[0-9a-fA-F]{3,8}\b", css), "raw color found"
assert "font-family" not in css.lower(), "local font family found"
assert "var(--sw-" in css
for selector in [".sw-ds-account-entry", ".sw-ds-session-status", ".sw-ds-device-list", ".sw-ds-device-row", ".sw-ds-account-lifecycle"]:
    assert selector in css, selector
print("TSK0308_COPY_NO_TOKEN_BRAND_FORK=PASS")

class RefParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.images = []
        self.text = []
        self.rtl = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "link" and a.get("href"):
            self.links.append(a["href"])
        if tag == "img" and a.get("src"):
            self.images.append((a["src"], a.get("alt")))
        if a.get("dir") == "rtl":
            self.rtl = True
    def handle_data(self, data):
        if data.strip():
            self.text.append(data.strip())

html = Path("prototype/TSK-0308/dual-mode-reference.html").read_text(encoding="utf-8")
parser = RefParser(); parser.feed(html)
for href in [
    "../../brand/system/TSK-0300/tokens.css",
    "../../brand/system/TSK-0300/components.css",
    "candidate.css",
    "dual-mode-addendum.css",
]:
    assert href in parser.links, href
assert ("../../brand/identity/TSK-0301/safeweb-wordmark-primary.svg", "SafeWeb") in parser.images
assert parser.rtl
text = " ".join(parser.text)
for label in ["Setup confirmed", "Protection verified", "Protection status could not be verified", "Not covered"]:
    assert label in text, label
assert "Protection has not yet been technically verified." in text
for stale in ["You confirmed this is set up", ">Verified<", "Status uncertain"]:
    assert stale not in html, f"stale active copy: {stale}"
for state in ["configured/parent-confirmed", "protected/verified", "uncertain/error"]:
    assert f'data-evidence-state="{state}"' in html, state
assert "Protection verification: Protection status could not be verified" in text
require_groups(
    text,
    [
        ("set up safeweb without an account",),
        ("sign in / manage devices",),
        ("sign-in is optional for core setup",),
        ("continue without signing in",),
        ("signed in describes account/session state only",),
        ("delete account",),
        ("reset anonymous web state",),
        ("remove safeweb dns",),
        ("deleting the account does not remove safeweb dns",),
    ],
    "corrected reference semantics",
)
assert html.index(">Start setup<") < html.index(">Sign in / Manage devices<")
print("TSK0308_COPY_ACTIVE_STATE_REFERENCE=PASS")
print("TSK0308_COPY_REFERENCE_STRUCTURE=PASS")

artifact = Path("TSK_0308_POST_TSK0300_COPY_CORRECTION_REVALIDATION_2026-09-02.md").read_text(encoding="utf-8")
require_groups(
    artifact,
    [
        ("two-file correction", "exact two-file correction"),
        ("historical immutable provenance files are left unchanged",),
        ("current tsk-0300",),
        ("current tsk-0320",),
        ("no implementation/auth/datastore",),
    ],
    "correction artifact",
)
print("TSK0308_COPY_PRESERVATION_FENCE=PASS")

print("TSK0308_COPY_ACC_STRUCTURAL=PASS")
print("TSK0308_COPY_EVD_READY=PASS")
print("TSK0308_POST_COPY_CORRECTION_STATIC=PASS")
