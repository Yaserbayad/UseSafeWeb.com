from __future__ import annotations

import csv
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "934a911d491e657f5cfe4991ad6217dc3d447509",
    "TSK_0044_POST_CR0008_DUAL_MODE_ADGUARD_API_COMPATIBILITY_CREDENTIAL_FAILURE_NFR_REVALIDATION_2026-09-02.md": "9e2df58093c592621eb1531dc1c34393a247dd80",
    "TSK_0044_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md": "e2180b768d63a54ce65d2959ef9b7a19e02082bd",
}

HEADING = "## TSK-0044 current accepted stable state — 2026-09-02 — POST-CR-0008 DUAL-MODE ADGUARD API/CREDENTIAL/FAILURE NFR REVALIDATION"


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def mask_updated(text: str) -> str:
    return re.sub(r"^\*\*Updated:\*\*.*$", "**Updated:** <MASK>", text, count=1, flags=re.M)


runtime_path = Path("CURRENT_STATE.md")
old = runtime_path.read_text(encoding="utf-8")

if HEADING in old:
    section = old.split(HEADING, 1)[1]
    required = [
        "**PASS**",
        "9e2df58093c592621eb1531dc1c34393a247dd80",
        "e2180b768d63a54ce65d2959ef9b7a19e02082bd",
        "33588675744",
        "100118011663",
    ]
    for value in required:
        assert value in section, value
    print("TSK0044_STATE_RECONCILIATION=ALREADY_APPLIED")
    raise SystemExit(0)

for path, expected in EXPECTED.items():
    actual = blob(path)
    if actual != expected:
        raise AssertionError(f"hash drift {path}: {actual} != {expected}")
print("TSK0044_STATE_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0044")
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "MEDIUM"
assert row["AI_Capability_A0_A4"] == "A3"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert [d.strip() for d in (row["Dependencies"] or "").split(";") if d.strip()] == ["TSK-0484", "TSK-0538", "TSK-0146"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0044", "VER-0044", "EVD-0044")
print("TSK0044_STATE_WBS_CONTRACT=PASS")

evidence = Path("TSK_0044_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md").read_text(encoding="utf-8")
for value in [
    "ACC-0044 = PASS",
    "VER-0044 = PASS",
    "EVD-0044 = SATISFIED",
    "33588675744",
    "100118011663",
    "TSK0044_CURRENT_REVALIDATION=PASS",
]:
    assert value in evidence, value
print("TSK0044_STATE_EVIDENCE_BINDING=PASS")

now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
base = re.sub(r"^\*\*Updated:\*\*.*$", f"**Updated:** {now}", old, count=1, flags=re.M)
assert mask_updated(base) == mask_updated(old)

append = f"""

{HEADING}

`TSK-0044 — Define AdGuard API compatibility, credential-isolation and failure NFRs`: **PASS** under current `ACC-0044 / VER-0044 / EVD-0044`, current direct predecessors TSK-0484 / TSK-0538 / TSK-0146, current dual-mode Version-1 scope and the frozen AdGuard Home v0.107.79 backend boundary.

- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / MEDIUM / A3 / `AUTO_ALLOWED`; dependencies exactly `TSK-0484; TSK-0538; TSK-0146`.
- Current artifact `TSK_0044_POST_CR0008_DUAL_MODE_ADGUARD_API_COMPATIBILITY_CREDENTIAL_FAILURE_NFR_REVALIDATION_2026-09-02.md`, version `2.0.0-post-CR0008`, blob `9e2df58093c592621eb1531dc1c34393a247dd80`, publication commit `2c14ee2539f3e85cd3fe7e2ed7d7c7a7b73dce9e`.
- Durable acceptance evidence `TSK_0044_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md`, blob `e2180b768d63a54ce65d2959ef9b7a19e02082bd`, publication commit `725fd2f841503a39044c24cda62d04a4b8dcbe5b`.
- Independent read-only VER-0044: workflow blob `00e367e8dc5456b5052f1f8f6a6daa1fb4cc113b`; verifier script blob `0c92fdebb55da98e8f94be649f5bec88f85233e2`; run/job `33588675744 / 100118011663`; conclusion **SUCCESS**.
- The accepted private-control rule remains: browsers/customer surfaces receive no AdGuard admin credential or generic `/control` proxy; version/schema drift fails closed; secrets remain server-side; HTTP/write acknowledgement never proves mutation success.
- Accountless setup remains login-free and creates no persistent AdGuard client/account ownership state. Optional account/device management may use a persistent opaque/high-entropy ClientID only under a separately accepted downstream TSK-0352 API/lifecycle contract with server-side ownership authorization, query/statistics exclusion and distinct deletion/revoke/removal truth.
- Auth/provider or datastore failure cannot make the independent accountless core unavailable. Invalid sessions cannot mutate device/AdGuard state; ambiguous datastore + AdGuard mutations reconcile before retry; account/device ownership never substitutes for technical Protection Map verification.
- Historical TSK-0044 evidence remains preserved for compatible v0.107.79 control-plane, credential, privacy, timeout/retry, idempotency and version-regression facts. Its pre-CR-0006 whole-product accountless-only assumption is superseded.
- **ACC-0044 = PASS. VER-0044 = PASS. EVD-0044 = SATISFIED.**
- **Non-inference:** this is L4 NFR-definition PASS only. It does not implement the AdGuard adapter, approve/execute TSK-0352, create a persistent client, activate authentication/datastore, rotate credentials, change AdGuard configuration/version, authorize real-user processing, publish, launch, pass a lifecycle gate or infer successor PASS.

### Queue status after current TSK-0044 revalidation

Recompute the executable frontier from canonical WBS/graph, current runtime evidence, artifact-specific current-validity, gates and Action Authority. Preserve valid non-uniform historical PASS records unless current evidence materially invalidates them.
"""

candidate = base + append
assert mask_updated(candidate) == mask_updated(old) + append
print("TSK0044_ALL_EXISTING_RUNTIME_BODY_PRESERVED=PASS")

runtime_path.write_text(candidate, encoding="utf-8")
written = runtime_path.read_text(encoding="utf-8")
assert HEADING in written
for value in [
    "9e2df58093c592621eb1531dc1c34393a247dd80",
    "e2180b768d63a54ce65d2959ef9b7a19e02082bd",
    "33588675744 / 100118011663",
    "ACC-0044 = PASS. VER-0044 = PASS. EVD-0044 = SATISFIED.",
]:
    assert value in written, value
print("TSK0044_STATE_CANDIDATE=PASS")
print("TSK0044_STATE_RECONCILIATION=PASS")
