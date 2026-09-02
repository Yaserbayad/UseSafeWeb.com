from __future__ import annotations

import csv
import re
import subprocess
from html.parser import HTMLParser
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "933bc16d90f66a7c8099666bd009cf50f78c5508",
    "prototype/TSK-0309/BASELINE.md": "6302bb2509d04c8269e4df112140d7c416e42eff",
    "TSK_0300_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md": "efaf7c80c1723208569b13ba4e725b2e7cad8d1a",
    "brand/system/TSK-0300/tokens.css": "cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f",
    "brand/system/TSK-0300/components.css": "831e92a74b6dda04252d93242cb33bd491a02381",
    "brand/identity/TSK-0301/safeweb-wordmark-primary.svg": "f93958e3e4a16f9056693072c1b9b8b31fcda852",
    "prototype/TSK-0308/SHARED_RESPONSIVE_DESIGN_SYSTEM_CANDIDATE.md": "cd5c217ca7882589617dc94701fe5b6ac0eaf8d4",
    "prototype/TSK-0308/candidate.css": "de5571379ff240f36b5aecd50f555a07176dbd32",
    "prototype/TSK-0308/reference.html": "fe86b9ec2b5d5e5e11cf4d135baca69f6b4a5862",
    "prototype/TSK-0308/DESIGN_SYSTEM_MAP.json": "cd83279cdf5381cd7dae3feb177439158c1f9197",
    "prototype/TSK-0308/REQUIREMENT_INTERFACE_TRACE.md": "5e34ce9c192c6af65ba493cb356adb964c3d30b6",
    "TSK_0308_SHARED_RESPONSIVE_DESIGN_SYSTEM_ACCEPTANCE_EVIDENCE_2026-08-29.md": "343961f30bc46a20762ad2b0108a4afe9593e5a3",
    "prototype/TSK-0308/DUAL_MODE_ADDENDUM.md": "195ace26e6e8586e8e19da85a21d430a4a89a55a",
    "prototype/TSK-0308/dual-mode-addendum.css": "67fe4f16a1aca56c7cd03ab28ec807a52e3e23e8",
    "prototype/TSK-0308/dual-mode-reference.html": "293945d9e2df823079e8dd73134168773a65a652",
    "TSK_0308_POST_CR0008_DUAL_MODE_SHARED_RESPONSIVE_DESIGN_SYSTEM_REVALIDATION_2026-09-02.md": "90dce398ae86238abf5cf141acac47d78bf085b8",
}


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def require_concepts(text: str, concepts: list[str], label: str) -> None:
    n = norm(text)
    missing = [c for c in concepts if norm(c) not in n]
    if missing:
        raise AssertionError(f"{label} missing: {missing}")


for path, expected in EXPECTED.items():
    if not Path(path).exists():
        raise AssertionError(f"missing {path}")
    actual = blob(path)
    if actual != expected:
        raise AssertionError(f"hash drift {path}: {actual} != {expected}")
print("TSK0308_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0308")
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "HIGH"
assert row["AI_Capability_A0_A4"] == "A3"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert [x.strip() for x in row["Dependencies"].split(";") if x.strip()] == ["TSK-0309", "TSK-0300"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0308", "VER-0308", "EVD-0308")
require_concepts(row["Acceptance_Criteria"], ["content", "error", "loading", "verification", "uncertain", "recovery", "tokens", "accessibility", "localization", "implementation"], "ACC-0308")
print("TSK0308_CURRENT_WBS=PASS")

runtime = Path("CURRENT_STATE.md").read_text(encoding="utf-8")

def task_pass(task_id: str) -> bool:
    pat = re.compile(rf"^(##|###) {re.escape(task_id)}\b.*?(?=^(?:##|###) |\Z)", re.M | re.S)
    sections = [m.group(0) for m in pat.finditer(runtime)]
    return any("**PASS" in s for s in sections)

for task_id in ["TSK-0309", "TSK-0300"]:
    assert task_pass(task_id), f"missing durable PASS for {task_id}"
print("TSK0308_CURRENT_PREDECESSORS=PASS")

historical = Path("prototype/TSK-0308/SHARED_RESPONSIVE_DESIGN_SYSTEM_CANDIDATE.md").read_text(encoding="utf-8")
historical_evd = Path("TSK_0308_SHARED_RESPONSIVE_DESIGN_SYSTEM_ACCEPTANCE_EVIDENCE_2026-08-29.md").read_text(encoding="utf-8")
addendum = Path("prototype/TSK-0308/DUAL_MODE_ADDENDUM.md").read_text(encoding="utf-8")
current = Path("TSK_0308_POST_CR0008_DUAL_MODE_SHARED_RESPONSIVE_DESIGN_SYSTEM_REVALIDATION_2026-09-02.md").read_text(encoding="utf-8")

# Historical provenance remains untouched and still proves the original required state system.
for i in range(1, 14):
    assert re.search(rf"^### DS-{i:02d}\b", historical, re.M), f"historical DS-{i:02d} missing"
require_concepts(historical_evd, ["13/13 component contracts", "6/6 required state classes", "6/6 protection states", "320/768/1024/1440", "visible focus", "reduced motion", "rtl/ltr"], "historical acceptance")
print("TSK0308_HISTORICAL_PROVENANCE=PASS")

# Current dual-mode predecessor requires optional account continuity plus complete accountless core.
baseline = Path("prototype/TSK-0309/BASELINE.md").read_text(encoding="utf-8")
require_concepts(baseline, ["complete core setup/protection/recovery journey remains usable without login", "optional parent google sign-in/account/session continuity", "lightweight dashboard/device-management", "account/device ownership never substitutes for technical dns/protection map verification", "account deletion does not claim dns removal"], "TSK-0309 dual mode")
print("TSK0308_DUAL_MODE_PREDECESSOR=PASS")

# The contradiction is explicit in provenance and explicitly superseded in the current addendum.
require_concepts(historical, ["no login, account, dashboard, profile", "no account/dashboard/pricing navigation", "does not create per-user indexable routes or persistent account navigation"], "historical scope contradiction")
require_concepts(addendum, ["superseded for current acceptance", "accountless core remains complete", "account use is optional and non-coercive", "identity is not protection evidence", "provider/datastore failure preserves accountless continuation", "lifecycle operations stay distinct"], "current scope reconciliation")
print("TSK0308_SCOPE_RECONCILIATION=PASS")

for i, name in [(14, "optionalaccountentry"), (15, "sessionstatus"), (16, "devicemanagementlist"), (17, "accountlifecycleactions")]:
    assert re.search(rf"^### DS-{i}\b", addendum, re.M), f"DS-{i} heading missing"
    assert name in re.sub(r"[^a-z0-9]", "", addendum.lower()), f"DS-{i} name missing"
print("TSK0308_DUAL_MODE_COMPONENTS=4/4_PASS")

# Shared token/primitive authority is unchanged; additive CSS may not define a local brand palette/font.
css = Path("prototype/TSK-0308/dual-mode-addendum.css").read_text(encoding="utf-8")
assert not re.search(r"#[0-9a-fA-F]{3,8}\b", css), "raw color found"
assert "font-family" not in css.lower(), "local font family found"
assert "var(--sw-" in css
for selector in [".sw-ds-account-entry", ".sw-ds-session-status", ".sw-ds-device-list", ".sw-ds-device-row", ".sw-ds-account-lifecycle"]:
    assert selector in css, selector
print("TSK0308_NO_TOKEN_OR_BRAND_FORK=PASS")

class RefParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]; self.images=[]; self.buttons=[]; self.text=[]; self.rtl=False
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=="link" and a.get("href"): self.links.append(a["href"])
        if tag=="img" and a.get("src"): self.images.append((a["src"],a.get("alt")))
        if tag=="button": self.buttons.append(a)
        if a.get("dir")=="rtl": self.rtl=True
    def handle_data(self, data):
        if data.strip(): self.text.append(data.strip())

html = Path("prototype/TSK-0308/dual-mode-reference.html").read_text(encoding="utf-8")
parser=RefParser(); parser.feed(html)
for href in ["../../brand/system/TSK-0300/tokens.css", "../../brand/system/TSK-0300/components.css", "candidate.css", "dual-mode-addendum.css"]:
    assert href in parser.links, href
assert ("../../brand/identity/TSK-0301/safeweb-wordmark-primary.svg", "SafeWeb") in parser.images
assert parser.rtl
text=" ".join(parser.text)
require_concepts(text, ["set up safeweb without an account", "sign in / manage devices", "sign-in is optional for core setup", "continue without signing in", "signed in describes account/session state only", "protection verification", "delete account", "reset anonymous web state", "remove safeweb dns", "deleting the account does not remove safeweb dns"], "reference semantics")
for prohibited in ["browse history", "child activity timeline", "query log viewer", "raw adguard admin", "fully protected"]:
    assert prohibited not in norm(text), prohibited
# Primary accountless action occurs before optional account entry in source order.
assert html.index(">Start setup<") < html.index(">Sign in / Manage devices<")
print("TSK0308_REFERENCE_STRUCTURE=PASS")

require_concepts(current, ["historical owner-approved tsk-0308 candidate", "bounded dual-mode addendum", "single token/primitive authority", "complete accountless core", "optional-account non-coercion", "identity/protection separation", "lifecycle truth", "no identity reselection/redesign"], "current revalidation")
print("TSK0308_CURRENT_REVALIDATION_ARTIFACT=PASS")

print("TSK0308_CURRENT_ACC_STRUCTURAL=PASS")
print("TSK0308_STATIC_VERIFICATION=PASS")
