from __future__ import annotations

import csv
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "933bc16d90f66a7c8099666bd009cf50f78c5508",
    "TSK_0308_POST_CR0008_DUAL_MODE_SHARED_RESPONSIVE_DESIGN_SYSTEM_REVALIDATION_2026-09-02.md": "90dce398ae86238abf5cf141acac47d78bf085b8",
    "TSK_0308_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md": "f280154e45fccbcaab51a2fdca2dd3c33edbb99a",
    "prototype/TSK-0308/DUAL_MODE_ADDENDUM.md": "195ace26e6e8586e8e19da85a21d430a4a89a55a",
    "prototype/TSK-0308/dual-mode-addendum.css": "67fe4f16a1aca56c7cd03ab28ec807a52e3e23e8",
    "prototype/TSK-0308/dual-mode-reference.html": "293945d9e2df823079e8dd73134168773a65a652",
    "prototype/TSK-0309/BASELINE.md": "6302bb2509d04c8269e4df112140d7c416e42eff",
    "brand/system/TSK-0300/tokens.css": "cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f",
    "brand/system/TSK-0300/components.css": "831e92a74b6dda04252d93242cb33bd491a02381",
    "brand/identity/TSK-0301/safeweb-wordmark-primary.svg": "f93958e3e4a16f9056693072c1b9b8b31fcda852",
}

HEADING = "## TSK-0308 current accepted stable state — 2026-09-02 — POST-CR-0008 DUAL-MODE SHARED RESPONSIVE DESIGN-SYSTEM REVALIDATION"


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def mask_updated(text: str) -> str:
    return re.sub(r"^\*\*Updated:\*\*.*$", "**Updated:** <MASK>", text, count=1, flags=re.M)


runtime_path = Path("CURRENT_STATE.md")
old = runtime_path.read_text(encoding="utf-8")

if HEADING in old:
    section = old.split(HEADING, 1)[1]
    for value in [
        "**PASS**",
        "90dce398ae86238abf5cf141acac47d78bf085b8",
        "f280154e45fccbcaab51a2fdca2dd3c33edbb99a",
        "33585488537",
        "100108650200",
    ]:
        assert value in section, value
    print("TSK0308_STATE_RECONCILIATION=ALREADY_APPLIED")
    raise SystemExit(0)

for path, expected in EXPECTED.items():
    actual = blob(path)
    if actual != expected:
        raise AssertionError(f"hash drift {path}: {actual} != {expected}")
print("TSK0308_STATE_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0308")
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "HIGH"
assert row["AI_Capability_A0_A4"] == "A3"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert [d.strip() for d in row["Dependencies"].split(";") if d.strip()] == ["TSK-0309", "TSK-0300"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0308", "VER-0308", "EVD-0308")
print("TSK0308_STATE_WBS_CONTRACT=PASS")

evidence = Path("TSK_0308_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md").read_text(encoding="utf-8")
for value in [
    "ACC-0308 = PASS",
    "VER-0308 = PASS",
    "EVD-0308 = SATISFIED",
    "33585488537",
    "100108650200",
    "TSK0308_RENDERED_CURRENT_ACCEPTANCE=PASS",
    "TSK0308_SOURCE_UNCHANGED=PASS",
]:
    assert value in evidence, value
print("TSK0308_STATE_EVIDENCE_BINDING=PASS")

now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
base = re.sub(r"^\*\*Updated:\*\*.*$", f"**Updated:** {now}", old, count=1, flags=re.M)
assert mask_updated(base) == mask_updated(old)

append = f"""

{HEADING}

`TSK-0308 — Create the shared responsive design system for public and product surfaces`: **PASS** under current `ACC-0308 / VER-0308 / EVD-0308`, current direct predecessors TSK-0309 / TSK-0300, current CR-0006/CR-0008 dual-mode scope and fresh structural/rendered-browser verification.

- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / HIGH / A3 / `AUTO_ALLOWED`; dependencies exactly `TSK-0309; TSK-0300`.
- Current revalidation artifact `TSK_0308_POST_CR0008_DUAL_MODE_SHARED_RESPONSIVE_DESIGN_SYSTEM_REVALIDATION_2026-09-02.md`, version `2.0.0-post-CR0008`, blob `90dce398ae86238abf5cf141acac47d78bf085b8`, publication commit `0f840f3616af0030d65181965a4bf683a981586f`.
- Durable acceptance evidence `TSK_0308_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md`, blob `f280154e45fccbcaab51a2fdca2dd3c33edbb99a`, publication commit `e4030b0fb1fa223870118be8c4f4603bc6d82258`.
- Historical owner-approved TSK-0308 package remains immutable provenance for compatible DS-01 through DS-13, state, responsive, accessibility and localization facts. Its blanket pre-CR-0006 Login/Account/Dashboard/Profile exclusions are superseded only for current scope.
- Current additive authority: `prototype/TSK-0308/DUAL_MODE_ADDENDUM.md` blob `195ace26e6e8586e8e19da85a21d430a4a89a55a`; `dual-mode-addendum.css` blob `67fe4f16a1aca56c7cd03ab28ec807a52e3e23e8`; `dual-mode-reference.html` blob `293945d9e2df823079e8dd73134168773a65a652`.
- Current design-system rule: DS-01 through DS-13 remain preserved; DS-14 `OptionalAccountEntry`, DS-15 `SessionStatus`, DS-16 `DeviceManagementList` and DS-17 `AccountLifecycleActions` add the bounded optional-account/session/dashboard/device-lifecycle composition required by current TSK-0309 while preserving the complete login-free core.
- TSK-0300 remains the sole shared token/primitive authority. SafeWeb identity remains unchanged. Account/session/device ownership never substitutes for technical protection verification; provider/session failure preserves an accountless continuation where the core path is available; account/device/anonymous-state/DNS-removal operations remain distinct.
- Independent read-only VER-0308: script blob `c614eb171c13a7c845257a10cb0597eb7d851b37`; accepted workflow blob `b26d5f8f502b1f6e3e671b179c23734fe6d07ccc`; run/job `33585488537 / 100108650200`; conclusion **SUCCESS**.
- Fresh rendered verification: 320 / 768 / 1024 / 1440 PASS; no horizontal overflow; accountless primary; optional-account secondary; provider fallback; identity/protection separation; lifecycle separation; RTL; visible focus; clean console; source unchanged.
- **ACC-0308 = PASS. VER-0308 = PASS. EVD-0308 = SATISFIED.**
- **Non-inference:** L4 design-system PASS only; no authentication/session/datastore/device-ownership implementation, real-user processing, legal/privacy completion, public publication, payment/market activation, LG-06, launch or successor PASS is inferred.

### Queue status after current TSK-0308 revalidation

Recompute the executable frontier from canonical WBS/graph, current runtime evidence, artifact-specific current-validity, gates and Action Authority. Preserve valid non-uniform historical PASS records unless current evidence materially invalidates them.
"""

candidate = base + append
assert mask_updated(candidate) == mask_updated(old) + append
print("TSK0308_ALL_EXISTING_RUNTIME_BODY_PRESERVED=PASS")

runtime_path.write_text(candidate, encoding="utf-8")
written = runtime_path.read_text(encoding="utf-8")
assert HEADING in written
for value in [
    "90dce398ae86238abf5cf141acac47d78bf085b8",
    "f280154e45fccbcaab51a2fdca2dd3c33edbb99a",
    "33585488537 / 100108650200",
    "ACC-0308 = PASS. VER-0308 = PASS. EVD-0308 = SATISFIED.",
]:
    assert value in written, value
print("TSK0308_STATE_CANDIDATE=PASS")
print("TSK0308_STATE_RECONCILIATION=PASS")
