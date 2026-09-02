from __future__ import annotations

import csv
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "6cc78a81d3b503902c915a2b02d88b81f75b8342",
    "TSK_0307_POST_CR0008_CURRENT_SOURCE_BACKED_INSTRUCTION_CATALOGUE_REVALIDATION_2026-09-02.md": "73a7028e247833bfe7e98487d9e079a51d36d424",
    "TSK_0307_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md": "afba74ba076bcc6832199955682462631abea0f0",
    "TSK_0317_POST_CR0008_CURRENT_PLATFORM_PATH_REVALIDATION_2026-09-02.md": "37173d2f9cb970a7b5e6a83af90c8f868f9fbfa8",
}

HEADING = "## TSK-0307 current accepted stable state — 2026-09-02 — POST-CR-0008 CURRENT SOURCE-BACKED INSTRUCTION CATALOGUE REVALIDATION"


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
        "73a7028e247833bfe7e98487d9e079a51d36d424",
        "afba74ba076bcc6832199955682462631abea0f0",
        "33586673039",
        "100112160467",
    ]:
        assert value in section, value
    print("TSK0307_STATE_RECONCILIATION=ALREADY_APPLIED")
    raise SystemExit(0)

for path, expected in EXPECTED.items():
    actual = blob(path)
    if actual != expected:
        raise AssertionError(f"hash drift {path}: {actual} != {expected}")
print("TSK0307_STATE_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0307")
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "HIGH"
assert row["AI_Capability_A0_A4"] == "A3"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert [d.strip() for d in row["Dependencies"].split(";") if d.strip()] == ["TSK-0317"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0307", "VER-0307", "EVD-0307")
print("TSK0307_STATE_WBS_CONTRACT=PASS")

evidence = Path("TSK_0307_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md").read_text(encoding="utf-8")
for value in [
    "ACC-0307 = PASS",
    "VER-0307 = PASS",
    "EVD-0307 = SATISFIED",
    "33586673039",
    "100112160467",
    "TSK0307_OFFICIAL_SOURCE_REACHABILITY=6/6_PASS",
]:
    assert value in evidence, value
print("TSK0307_STATE_EVIDENCE_BINDING=PASS")

now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
base = re.sub(r"^\*\*Updated:\*\*.*$", f"**Updated:** {now}", old, count=1, flags=re.M)
assert mask_updated(base) == mask_updated(old)

append = f"""

{HEADING}

`TSK-0307 — Create the source-backed instruction/content catalogue with applicability and review triggers`: **PASS** under current `ACC-0307 / VER-0307 / EVD-0307`, current direct predecessor TSK-0317, current SafeWeb identity and refreshed first-party Android/Apple platform-source review.

- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / HIGH / A3 / `AUTO_ALLOWED`; dependency exactly `TSK-0317`.
- Current artifact `TSK_0307_POST_CR0008_CURRENT_SOURCE_BACKED_INSTRUCTION_CATALOGUE_REVALIDATION_2026-09-02.md`, version `2.0.0-post-CR0008`, blob `73a7028e247833bfe7e98487d9e079a51d36d424`, publication commit `330e9d13b9d479212ca6c49df3431f19f7107ba5`.
- Durable acceptance evidence `TSK_0307_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md`, blob `afba74ba076bcc6832199955682462631abea0f0`, publication commit `0a20669591b953e8a66e12dd9a37549bf2ff6374`.
- Historical nine-class TSK-0307 catalogue/evidence remain provenance for compatible applicability, metadata, limits, localization and recovery facts. Stale generic parent-facing `UseSafeWeb` wording is superseded by current `SafeWeb` / `SafeWeb DNS` visible copy; literal technical `usesafeweb.com` endpoints remain unchanged.
- Current catalogue retains exactly nine instruction classes and every ACC metadata field: official source, platform/version/region, owner, last verification, review trigger, localized variants, known limits and test reference; current review date is 2026-09-02.
- Current source review remains first-party and current: Android Help Private DNS, Android DevicePolicyManager, Android LinkProperties, Apple DNS Settings, Apple iPhone configuration-profile install/remove guidance and Apple Personal Safety profile-removal guidance.
- Independent read-only VER-0307: verifier script blob `34fb3b8532375ba7b6e080f44256f6f0ab9a0ddf`; workflow blob `00077c7dac9a5001001a077ea4e7482f76dea4c6`; run/job `33586673039 / 100112160467`; conclusion **SUCCESS**. Structural current acceptance PASS and live first-party source reachability `6/6 PASS`.
- Current truth boundary: accountless setup/verification/help/removal remains complete; account/session/device ownership does not substitute for technical verification; managed/security controls are not weakened just to make SafeWeb green; no browsing/query/activity-history requirement, speculative unsupported client path or silent plaintext fallback is introduced.
- **ACC-0307 = PASS. VER-0307 = PASS. EVD-0307 = SATISFIED.**
- **Non-inference:** internal L4 instruction/content definition only; no production Apple profile distribution, account/session/dashboard implementation, representative-parent/native-speaker proof, legal/privacy completion, publication, participant processing, payment/market activation, LG-06, launch or successor PASS is inferred.

### Queue status after current TSK-0307 revalidation

Recompute the executable frontier from canonical WBS/graph, current runtime evidence, artifact-specific current-validity, gates and Action Authority. Preserve valid non-uniform historical PASS records unless current evidence materially invalidates them.
"""

candidate = base + append
assert mask_updated(candidate) == mask_updated(old) + append
print("TSK0307_ALL_EXISTING_RUNTIME_BODY_PRESERVED=PASS")

runtime_path.write_text(candidate, encoding="utf-8")
written = runtime_path.read_text(encoding="utf-8")
assert HEADING in written
for value in [
    "73a7028e247833bfe7e98487d9e079a51d36d424",
    "afba74ba076bcc6832199955682462631abea0f0",
    "33586673039 / 100112160467",
    "ACC-0307 = PASS. VER-0307 = PASS. EVD-0307 = SATISFIED.",
]:
    assert value in written, value
print("TSK0307_STATE_CANDIDATE=PASS")
print("TSK0307_STATE_RECONCILIATION=PASS")
