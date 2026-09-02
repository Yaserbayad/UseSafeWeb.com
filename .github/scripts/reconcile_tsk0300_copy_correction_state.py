from __future__ import annotations

import csv
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "235cca98f7a3e1432b88e4581de5d0a80602195a",
    "TSK_0300_POST_CR0008_PROTECTION_COPY_CORRECTION_REVALIDATION_2026-09-02.md": "172e4b82c7c106c48291c6a6a75aca6848ca4d0c",
    "TSK_0300_POST_CR0008_PROTECTION_COPY_CORRECTION_EVIDENCE_2026-09-02.md": "a3e39896b67098ced321cb9e4b82c65c440806e4",
    "brand/system/TSK-0300/README.md": "a54a2b653720160261b034149cadff62bc399102",
    "brand/system/TSK-0300/templates/status.html": "8f9971edfc87b2da8174330b9b4be68338a96fb4",
}
HEADING = "## TSK-0300 current accepted stable state — 2026-09-02 — PROTECTION-STATE COPY CORRECTION REVALIDATION"


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def mask_updated(text: str) -> str:
    return re.sub(r"^\*\*Updated:\*\*.*$", "**Updated:** <MASK>", text, count=1, flags=re.M)


path = Path("CURRENT_STATE.md")
old = path.read_text(encoding="utf-8")
if HEADING in old:
    section = old.split(HEADING, 1)[1]
    for value in [
        "**PASS**",
        "172e4b82c7c106c48291c6a6a75aca6848ca4d0c",
        "a3e39896b67098ced321cb9e4b82c65c440806e4",
        "33592292946 / 100128578252",
        "a54a2b653720160261b034149cadff62bc399102",
        "8f9971edfc87b2da8174330b9b4be68338a96fb4",
    ]:
        assert value in section, value
    print("TSK0300_COPY_STATE_RECONCILIATION=ALREADY_APPLIED")
    raise SystemExit(0)

for file_path, expected in EXPECTED.items():
    actual = blob(file_path)
    if actual != expected:
        raise AssertionError(f"hash drift {file_path}: {actual} != {expected}")
print("TSK0300_COPY_STATE_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0300")
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "HIGH"
assert row["AI_Capability_A0_A4"] == "A3"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert [x.strip() for x in (row.get("Dependencies") or "").split(";") if x.strip()] == ["TSK-0301"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0300", "VER-0300", "EVD-0300")
print("TSK0300_COPY_STATE_WBS=PASS")

evidence = Path("TSK_0300_POST_CR0008_PROTECTION_COPY_CORRECTION_EVIDENCE_2026-09-02.md").read_text(encoding="utf-8")
for value in [
    "ACC-0300 = PASS. VER-0300 = PASS. EVD-0300 = SATISFIED",
    "33592292946 / 100128578252",
    "TSK0300_PROTECTION_COPY_CORRECTION=PASS",
    "a54a2b653720160261b034149cadff62bc399102",
    "8f9971edfc87b2da8174330b9b4be68338a96fb4",
]:
    assert value in evidence, value
print("TSK0300_COPY_STATE_EVIDENCE_BINDING=PASS")

now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
base = re.sub(r"^\*\*Updated:\*\*.*$", f"**Updated:** {now}", old, count=1, flags=re.M)
assert mask_updated(base) == mask_updated(old)
append = f"""

{HEADING}

`TSK-0300 — Translate the approved identity into shared tokens, components, templates, and asset conventions`: **PASS** under current `ACC-0300 / VER-0300 / EVD-0300`, current predecessor TSK-0301, current TSK-0299/TSK-0320 semantic authority, and the preserved owner-approved SafeWeb identity.

- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / HIGH / A3 / `AUTO_ALLOWED`; dependency exactly `TSK-0301`.
- Correction artifact `TSK_0300_POST_CR0008_PROTECTION_COPY_CORRECTION_REVALIDATION_2026-09-02.md`, blob `172e4b82c7c106c48291c6a6a75aca6848ca4d0c`, publication commit `e9b04150de7c053d919493fba9eb296eed9b4430`.
- Durable correction evidence `TSK_0300_POST_CR0008_PROTECTION_COPY_CORRECTION_EVIDENCE_2026-09-02.md`, blob `a3e39896b67098ced321cb9e4b82c65c440806e4`, publication commit `7fd4e0a1fac43e7cd9bc9bb0dc2a029648d7330d`.
- Independent read-only VER-0300 correction: verifier blob `154f84b453694861f58df1a5dcf19ea372644fb5`, workflow blob `85278743149c6017f7ea0d4ad899c4094d0f3249`, run/job `33592292946 / 100128578252`, conclusion **SUCCESS**.
- Genuine contradiction resolved: the shared-system README and status reference no longer present historical `Verified` / `You confirmed this is set up` / `Status uncertain` labels as the current TSK-0320 canonical state copy.
- Corrected README blob `a54a2b653720160261b034149cadff62bc399102`; corrected status-reference blob `8f9971edfc87b2da8174330b9b4be68338a96fb4`.
- Current canonical primary copy is `Protection verified`, `Setup confirmed`, `Action needed`, `Not covered`, `Protection status could not be verified`, `Removed`; S2 retains `Protection has not yet been technically verified.`
- Preserved unchanged: tokens `cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f`, components `831e92a74b6dda04252d93242cb33bd491a02381`, current public/product dual-mode references, help/partner/social references, and all owner-approved TSK-0301 identity masters.
- Accountless core remains complete; optional account continuity remains non-coercive; J0/J1 are not automatically linked; account/session/dashboard/device ownership is not technical protection evidence.
- **ACC-0300 = PASS. VER-0300 = PASS. EVD-0300 = SATISFIED.**
- **Non-inference:** this correction does not deploy/build, change identity, activate auth/persistence, authorize real-user/publication/payment/market/production/launch work, pass a lifecycle gate, or infer successor PASS. Direct successor TSK-0310 must refresh current TSK-0300 predecessor/materiality proof before its earlier current PASS is relied upon for further progression.

### Queue status after corrected TSK-0300 reacceptance

Refresh direct successor evidence where the corrected predecessor is material, including TSK-0310, before recomputing the executable frontier. Preserve all unrelated current PASS states unless current evidence independently contradicts them.
"""
candidate = base.rstrip() + append
assert mask_updated(candidate) == mask_updated(old).rstrip() + append
path.write_text(candidate, encoding="utf-8")
written = path.read_text(encoding="utf-8")
for value in [
    HEADING,
    "172e4b82c7c106c48291c6a6a75aca6848ca4d0c",
    "a3e39896b67098ced321cb9e4b82c65c440806e4",
    "33592292946 / 100128578252",
    "ACC-0300 = PASS. VER-0300 = PASS. EVD-0300 = SATISFIED.",
]:
    assert value in written, value
print("TSK0300_COPY_ALL_EXISTING_RUNTIME_BODY_PRESERVED=PASS")
print("TSK0300_COPY_STATE_CANDIDATE=PASS")
print("TSK0300_COPY_STATE_RECONCILIATION=PASS")
