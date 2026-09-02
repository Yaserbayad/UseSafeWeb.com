from __future__ import annotations

import csv
import re
import subprocess
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "934a911d491e657f5cfe4991ad6217dc3d447509",
    "TSK_0044_POST_CR0008_DUAL_MODE_ADGUARD_API_COMPATIBILITY_CREDENTIAL_FAILURE_NFR_REVALIDATION_2026-09-02.md": "9e2df58093c592621eb1531dc1c34393a247dd80",
    "TSK_0044_ADGUARD_API_COMPATIBILITY_CREDENTIAL_FAILURE_NFR_2026-08-28.md": "07ab5539d11ff25d591adeada34e7f30854caa90",
    "TSK_0044_ADGUARD_API_COMPATIBILITY_CREDENTIAL_FAILURE_NFR_EVIDENCE_2026-08-28.md": "19355b7b9ea2bac219ccf79ef9cbfd588cc56ba4",
    "TSK_0484_POST_CR0008_SECURITY_ABUSE_NFR_REVALIDATION_2026-09-02.md": "285ee390499190137e8aac0fed976975fb79ed80",
    "TSK_0538_POST_CR0008_DUAL_MODE_RELIABILITY_OBSERVABILITY_NFR_REVALIDATION_2026-09-02.md": "44c9c299465e821e2ffd84a54b77e3e615d61925",
    "TSK_0146_VERSION_1_OPTIONAL_ACCOUNT_PRODUCT_BASELINE_2026-08-30.md": "9d3870d90add696fc352829fb4763c834b8d09af",
}


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def require_any(text: str, groups: list[tuple[str, ...]], label: str) -> None:
    low = text.lower()
    missing = [group for group in groups if not any(term.lower() in low for term in group)]
    if missing:
        raise AssertionError(f"{label} missing semantic groups: {missing}")


for path, expected in EXPECTED.items():
    if not Path(path).exists():
        raise AssertionError(f"missing {path}")
    actual = blob(path)
    if actual != expected:
        raise AssertionError(f"hash drift {path}: {actual} != {expected}")
print("TSK0044_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0044")
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "MEDIUM"
assert row["AI_Capability_A0_A4"] == "A3"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert [d.strip() for d in (row["Dependencies"] or "").split(";") if d.strip()] == ["TSK-0484", "TSK-0538", "TSK-0146"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0044", "VER-0044", "EVD-0044")
acc = row["Acceptance_Criteria"] or ""
require_any(acc, [
    ("private/restricted adguard administration", "restricted adguard administration"),
    ("secret storage/rotation", "secret storage", "rotation"),
    ("timeouts/retries", "timeouts", "retries"),
    ("partial-failure reconciliation", "failure reconciliation"),
    ("opaque setup/clientid identifiers", "clientid identifiers"),
    ("privacy booleans",),
    ("version/contract regression", "contract regression"),
    ("optional customer authentication/session", "authentication/session"),
    ("minimum persistence",),
    ("adguard, auth, datastore or verification", "adguard", "datastore"),
    ("no mandatory login for core value",),
], "ACC-0044")
print("TSK0044_CURRENT_WBS=PASS")

runtime = Path("CURRENT_STATE.md").read_text(encoding="utf-8")
for task_id in ["TSK-0484", "TSK-0538", "TSK-0146"]:
    pattern = rf"^(?:##|###) {task_id}\b.*?(?=^(?:##|###) |\Z)"
    sections = re.findall(pattern, runtime, re.M | re.S)
    assert sections and any("**PASS**" in section for section in sections), f"missing PASS {task_id}"
print("TSK0044_CURRENT_PREDECESSORS=PASS")

doc = Path("TSK_0044_POST_CR0008_DUAL_MODE_ADGUARD_API_COMPATIBILITY_CREDENTIAL_FAILURE_NFR_REVALIDATION_2026-09-02.md").read_text(encoding="utf-8")
low = doc.lower()
headings = [line for line in doc.splitlines() if line.startswith("## ")]
assert len(headings) >= 16, len(headings)
print("TSK0044_STRUCTURE=PASS")

require_any(doc, [
    ("adguard home v0.107.79",),
    ("v0.107.79/openapi/openapi.yaml",),
    ("/control",),
    ("basic-auth", "basic auth"),
    ("unexpected version/schema/field drift", "contract failure"),
], "version/control contract")
print("TSK0044_VERSION_CONTROL_CONTRACT=PASS")

require_any(doc, [
    ("no adguard admin credential",),
    ("no generic `/control` capability", "reject arbitrary `/control` proxying"),
    ("private server-side", "private adapter"),
    ("redact authentication", "sanitized"),
    ("apply authorization before", "authorization before"),
], "control isolation")
print("TSK0044_CONTROL_ISOLATION=PASS")

require_any(doc, [
    ("accountless setup must not create", "accountless setup creates no persistent"),
    ("persistent adguard client/clientid may exist", "persistent clientid creation"),
    ("tsk-0352 remains the downstream owner", "tsk-0352"),
    ("high-entropy opaque clientid", "opaque/high-entropy"),
    ("parent-to-device ownership authorization", "ownership authorization"),
    ("not proof that protection is active", "not treated as protection verification"),
    ("ignore_querylog",),
    ("ignore_statistics",),
    ("account deletion, device-record deletion and physical dns configuration removal", "account deletion, device deletion/revoke and physical dns removal"),
], "dual-mode client boundary")
print("TSK0044_DUAL_MODE_CLIENT_BOUNDARY=PASS")

require_any(doc, [
    ("query logging remains disabled",),
    ("query-log file persistence remains disabled",),
    ("statistics remain disabled",),
    ("client-ip anonymisation remains enabled", "anonymisation/privacy state"),
    ("no query-history/statistics source",),
], "privacy invariants")
print("TSK0044_PRIVACY_INVARIANTS=PASS")

require_any(doc, [
    ("connection timeout: 1 second",),
    ("ordinary read/health total timeout: 3 seconds",),
    ("bounded configuration/test total timeout: 5 seconds",),
    ("401/403: no blind retry",),
    ("mutation: no blind replay",),
    ("http/write acknowledgement alone never proves success",),
], "timeouts retries")
print("TSK0044_TIMEOUT_RETRY=PASS")

require_any(doc, [
    ("pre-read exact affected state",),
    ("execute one mutation",),
    ("read back the api state",),
    ("mixed/unknown state",),
    ("datastore and adguard state must be reconciled",),
], "idempotency reconciliation")
print("TSK0044_RECONCILIATION=PASS")

require_any(doc, [
    ("auth/provider/session failure must not make the complete accountless core unavailable",),
    ("expired/revoked/invalid sessions cannot mutate",),
    ("authentication success alone does not prove device ownership or protection state",),
    ("detailed authentication/session", "tsk-0353"),
], "auth failure")
print("TSK0044_AUTH_FAILURE=PASS")

require_any(doc, [
    ("datastore is unavailable or ambiguous",),
    ("accountless setup/protection remains available",),
    ("stale cached ownership is not accepted",),
    ("partial datastore + adguard mutations are reconciled",),
    ("no success is shown until both",),
], "datastore failure")
print("TSK0044_DATASTORE_FAILURE=PASS")

require_any(doc, [
    ("admin api unavailable; public dns healthy",),
    ("public verification unavailable or indeterminate",),
    ("adguard service unavailable/degraded",),
    ("auth or datastore unavailable",),
    ("accountless core independent",),
], "failure planes")
print("TSK0044_FAILURE_PLANES=PASS")

historical = Path("TSK_0044_ADGUARD_API_COMPATIBILITY_CREDENTIAL_FAILURE_NFR_2026-08-28.md").read_text(encoding="utf-8").lower()
assert "no mandatory usesafeweb customer account, customer authentication, persistent dashboard, adguard client record or customer datastore" in historical
require_any(doc, [
    ("superseded for current acceptance",),
    ("optional account/session/dashboard/minimum persistence",),
    ("categorical prohibition on any persistent adguard client",),
    ("accountless remains no-persistent-client and login-free",),
], "historical reconciliation")
print("TSK0044_HISTORICAL_CURRENT_RECONCILIATION=PASS")

assert "current upstream adguard documentation" in low
assert "persistent clients and clientids" in low
print("TSK0044_UPSTREAM_SOURCE_BOUNDARY=PASS")

section = re.search(r"## 14\. Deterministic downstream assertion catalogue\n(.*?)(?=\n## 15\.)", doc, re.S)
assert section, "assertion catalogue missing"
assert len(re.findall(r"^\d+\. ", section.group(1), re.M)) == 30
print("TSK0044_ASSERTION_CATALOGUE=PASS")

require_any(doc, [
    ("does not implement an adguard adapter", "no implementation"),
    ("create a persistent client", "persistent-client creation"),
    ("activate authentication", "authentication activation"),
    ("infer any successor pass", "successor pass"),
], "non-inference")
print("TSK0044_NON_INFERENCE=PASS")

print("TSK0044_CURRENT_ACC=PASS")
print("TSK0044_CURRENT_VER=PASS")
print("TSK0044_CURRENT_EVD_READY=PASS")
print("TSK0044_CURRENT_REVALIDATION=PASS")
