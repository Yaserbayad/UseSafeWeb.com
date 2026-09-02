from __future__ import annotations

import csv
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "974c7e5ebdbf64e382d2d4075490567f11be6fff",
    "TSK_0311_POST_CR0008_DUAL_MODE_LOCALIZATION_CONTENT_ARCHITECTURE_REVALIDATION_2026-09-02.md": "4f702a61bfccad385be83c1a37a753cdeb1d8b43",
    "TSK_0311_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md": "563c63df5b34034a30d8587f1cff5fe76457c623",
    "TSK_0318_POST_CR0008_DUAL_MODE_PUBLIC_PRODUCT_SETUP_IA_2026-09-01.md": "975e2e7a8e85e9408e0bbbc2be226f3fdd012db3",
    "TSK_0307_POST_CR0008_CURRENT_SOURCE_BACKED_INSTRUCTION_CATALOGUE_REVALIDATION_2026-09-02.md": "73a7028e247833bfe7e98487d9e079a51d36d424",
}

HEADING = "## TSK-0311 current accepted stable state — 2026-09-02 — POST-CR-0008 DUAL-MODE LOCALIZATION/CONTENT ARCHITECTURE REVALIDATION"


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
        "4f702a61bfccad385be83c1a37a753cdeb1d8b43",
        "563c63df5b34034a30d8587f1cff5fe76457c623",
        "33587275544",
        "100113936593",
    ]:
        assert value in section, value
    print("TSK0311_STATE_RECONCILIATION=ALREADY_APPLIED")
    raise SystemExit(0)

for path, expected in EXPECTED.items():
    actual = blob(path)
    if actual != expected:
        raise AssertionError(f"hash drift {path}: {actual} != {expected}")
print("TSK0311_STATE_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0311")
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "HIGH"
assert row["AI_Capability_A0_A4"] == "A3"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert [d.strip() for d in (row["Dependencies"] or "").split(";") if d.strip()] == ["TSK-0318"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0311", "VER-0311", "EVD-0311")
print("TSK0311_STATE_WBS_CONTRACT=PASS")

evidence = Path("TSK_0311_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md").read_text(encoding="utf-8")
for value in [
    "ACC-0311 = PASS",
    "VER-0311 = PASS",
    "EVD-0311 = SATISFIED",
    "33587275544",
    "100113936593",
    "TSK0311_TEST_ASSERTIONS=18/18_PASS",
]:
    assert value in evidence, value
print("TSK0311_STATE_EVIDENCE_BINDING=PASS")

now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
base = re.sub(r"^\*\*Updated:\*\*.*$", f"**Updated:** {now}", old, count=1, flags=re.M)
assert mask_updated(base) == mask_updated(old)

append = f"""

{HEADING}

`TSK-0311 — Define translation keys/files, locale metadata, plural/date rules, content ownership, localized instruction variants, and fallback behavior`: **PASS** under current `ACC-0311 / VER-0311 / EVD-0311`, current direct predecessor TSK-0318, current dual-mode Version-1 IA and current source-backed TSK-0307 instruction authority.

- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / HIGH / A3 / `AUTO_ALLOWED`; dependency exactly `TSK-0318`.
- Current revalidation artifact `TSK_0311_POST_CR0008_DUAL_MODE_LOCALIZATION_CONTENT_ARCHITECTURE_REVALIDATION_2026-09-02.md`, version `2.0.0-post-CR0008`, blob `4f702a61bfccad385be83c1a37a753cdeb1d8b43`, publication commit `f47c8cddca8906cd4b78640de8f76065c4bc92fa`.
- Durable acceptance evidence `TSK_0311_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md`, blob `563c63df5b34034a30d8587f1cff5fe76457c623`, publication commit `77d3ef29ea5eab4a7491ad2f48ef2677e0ae58fb`.
- Historical TSK-0311 architecture/evidence remain immutable provenance for the still-valid en-GB/tr-TR/ar locale model, externalized semantic keys, deterministic fallback, source-backed instruction binding, CLDR/Unicode-equivalent plural/number/date behavior, RTL/bidi isolation, accessibility, ownership, privacy and schema/content versioning. Its old accountless-only surface inventory is superseded for current acceptance.
- Current architecture adds `account`, `session`, `dashboard`, `device-management` and `account-lifecycle` namespaces to the preserved core namespaces and defines current keys for optional account entry/fallback, auth/session results, dashboard/device state, reverify/reinstall/replace/revoke/delete, account deletion, anonymous-state reset and DNS-removal consequence separation.
- Current truth rules preserve optional-account non-coercion, accountless fallback, identity/ownership versus technical-verification separation, distinct destructive operations, no J0/J1 automatic linkage, no surveillance expansion and exact SafeWeb/technical-endpoint handling.
- Current TSK-0307 remains the single source-backed owner for platform setup/verification/removal/recovery instructions; localization binds current instruction IDs and cannot silently retain stale copied platform text.
- Independent read-only VER-0311: verifier script blob `7908f574aeffbe7b19c51670a2dee5b49cee08ce`; workflow blob `b5e1dc4d6e34cca83f289e3bca0a0095488abaec`; run/job `33587275544 / 100113936593`; conclusion **SUCCESS**. Verification proved 13/13 namespaces, 21/21 representative dual-mode keys and 18/18 current implementation test assertions.
- **ACC-0311 = PASS. VER-0311 = PASS. EVD-0311 = SATISFIED.**
- **Non-inference:** L4 localization/content architecture PASS only; no production locale files, Turkish/Arabic linguistic certification, native-speaker/representative-parent validation, market activation, auth/session/dashboard/device implementation, legal/privacy completion, publication, participant processing, payment, LG-06, launch or successor PASS is inferred.

### Queue status after current TSK-0311 revalidation

Recompute the executable frontier from canonical WBS/graph, current runtime evidence, artifact-specific current-validity, gates and Action Authority. Preserve valid non-uniform historical PASS records unless current evidence materially invalidates them.
"""

candidate = base + append
assert mask_updated(candidate) == mask_updated(old) + append
print("TSK0311_ALL_EXISTING_RUNTIME_BODY_PRESERVED=PASS")

runtime_path.write_text(candidate, encoding="utf-8")
written = runtime_path.read_text(encoding="utf-8")
assert HEADING in written
for value in [
    "4f702a61bfccad385be83c1a37a753cdeb1d8b43",
    "563c63df5b34034a30d8587f1cff5fe76457c623",
    "33587275544 / 100113936593",
    "ACC-0311 = PASS. VER-0311 = PASS. EVD-0311 = SATISFIED.",
]:
    assert value in written, value
print("TSK0311_STATE_CANDIDATE=PASS")
print("TSK0311_STATE_RECONCILIATION=PASS")
