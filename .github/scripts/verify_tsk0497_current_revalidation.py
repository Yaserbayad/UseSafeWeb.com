from __future__ import annotations

import csv
import re
import subprocess
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "c50c9c119f4cd1b1ed0258292a4cda34639cf20e",
    "TSK_0497_POST_CR0008_DUAL_MODE_PRODUCT_EVENT_KPI_CATALOGUE_REVALIDATION_2026-09-02.md": "8c3b26ad0771b09a7e223ffc47f5e81b0ca217c7",
    "TSK_0497_MINIMAL_PRODUCT_EVENT_KPI_CATALOGUE_2026-08-28.md": "61bcd78bbe7ac2446c9c79e5e2e0765cb4f66b8c",
    "TSK_0497_MINIMAL_PRODUCT_EVENT_KPI_CATALOGUE_EVIDENCE_2026-08-28.md": "b26a4cb123929518b7875023530f37256612ac98",
    "TSK_0230_PRIVACY_DATA_MINIMISATION_RETENTION_DELETION_NFRS_2026-09-01.md": "eda85b062a3a7ba29544de35a8a813c9790092f2",
    "TSK_0498_PRIVACY_SAFE_DECISION_LINKED_EVENT_CONTRACT_2026-09-01.md": "6b7a5095122c74ed9ec860b74408dab474576659",
}


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def require(text: str, concepts: list[str], label: str) -> None:
    missing = [concept for concept in concepts if concept not in text]
    if missing:
        raise AssertionError(f"{label} missing concepts: {missing}")


for path, expected in EXPECTED.items():
    if not Path(path).exists():
        raise AssertionError(f"missing {path}")
    actual = blob(path)
    if actual != expected:
        raise AssertionError(f"hash drift {path}: {actual} != {expected}")
print("TSK0497_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0497")
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "MEDIUM"
assert row["AI_Capability_A0_A4"] == "A3"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert [d.strip() for d in (row["Dependencies"] or "").split(";") if d.strip()] == ["TSK-0230"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0497", "VER-0497", "EVD-0497")
acc = (row["Acceptance_Criteria"] or "").lower()
require(acc, ["approved purpose", "accountless events", "optional-account events", "dns/domain browsing history", "child activity", "raw token", "retention", "access", "deletion"], "ACC-0497")
print("TSK0497_CURRENT_WBS=PASS")

runtime = Path("CURRENT_STATE.md").read_text(encoding="utf-8")
for task_id in ["TSK-0230", "TSK-0498"]:
    match = re.search(rf"^## {task_id} current accepted stable state.*?(?=^## |\Z)", runtime, re.M | re.S)
    assert match and "**PASS**" in match.group(0), f"missing current PASS {task_id}"
print("TSK0497_CURRENT_PRIVACY_EVENT_AUTHORITIES=PASS")

doc = Path("TSK_0497_POST_CR0008_DUAL_MODE_PRODUCT_EVENT_KPI_CATALOGUE_REVALIDATION_2026-09-02.md").read_text(encoding="utf-8")
low = doc.lower()
headings = [line for line in doc.splitlines() if line.startswith("## ")]
assert len(headings) >= 13
print("TSK0497_STRUCTURE=PASS")

# Single schema authority and exact current event set.
require(low, ["single event-schema authority", "tsk-0498 remains the current authoritative l5 event contract", "unknown event names or fields are rejected"], "schema authority")
expected_events = [
    "journey_started",
    "journey_step_entered",
    "journey_step_outcome",
    "journey_completed",
    "protection_state_evaluated",
    "protection_verification_outcome",
    "self_service_opened",
    "self_service_outcome",
    "synthetic_service_probe_result",
    "recovery_operation_outcome",
    "channel_entry",
    "cost_period_recorded",
]
for event in expected_events:
    assert f"`{event}`" in doc, event
print("TSK0497_TSK0498_SCHEMA_ALIGNMENT=PASS")

# Accountless privacy/retention semantics.
require(low, ["no stable analytics user id", "maximum 24 hours", "sign-in cannot extend or link accountless event history", "maximum 13 months", "synthetic reliability", "30 days", "cost analytics", "dns qname", "unknown/high-cardinality fields fail closed"], "accountless privacy")
print("TSK0497_ACCOUNTLESS_PRIVACY_RETENTION=PASS")

# Optional account boundary: product analytics stays non-identifying, operational identifiers remain outside analytics.
require(low, ["account identity is not thereby analytics identity", "zero account/device identifiers", "operational/security event", "no implicit new event approval", "dormant / no current data source", "account/session/device operational logs cannot be repurposed as product analytics"], "optional-account boundary")
require(low, ["email", "provider subject", "adguard clientid", "session/token id"], "optional-account prohibited identifiers")
print("TSK0497_OPTIONAL_ACCOUNT_BOUNDARY=PASS")

# Global prohibited measurement classes.
require(low, ["dns query/qname", "browsing/search history", "child activity", "raw ip as analytics data", "session replay", "daily-active-user", "cross-session/cross-device identity graph", "marketing/advertising profile"], "prohibited classes")
print("TSK0497_PROHIBITED_MEASUREMENT=PASS")

# Approved event table must expose ACC metadata for all 12 current events.
event_section = re.search(r"## 6\. Current approved event catalogue metadata\n(.*?)(?=\n## 7\.)", doc, re.S)
assert event_section, "event catalogue section missing"
event_rows = [line for line in event_section.group(1).splitlines() if line.startswith("| `")]
assert len(event_rows) == 12, len(event_rows)
header = next(line for line in event_section.group(1).splitlines() if line.startswith("| Event |"))
require(header.lower(), ["approved purpose", "prohibited", "collection point", "denominator", "retention", "access"], "event table header")
print("TSK0497_APPROVED_EVENT_METADATA=PASS")

# Dormant optional-account KPIs are defined but not activated.
optional_kpi = re.search(r"## 7\. Optional-account KPI definitions.*?\n(.*?)(?=\n## 8\.)", doc, re.S)
assert optional_kpi
optional_rows = [line for line in optional_kpi.group(1).splitlines() if line.startswith("| Optional") or line.startswith("| Owned") or line.startswith("| Account-")]
assert len(optional_rows) >= 4, len(optional_rows)
assert optional_kpi.group(1).lower().count("dormant") >= 4
print("TSK0497_OPTIONAL_KPI_DORMANCY=PASS")

# Current product KPI table includes source/formula/window/owner/guardrail/action and sufficient decision coverage.
kpi_section = re.search(r"## 8\. Current accountless/product KPI catalogue\n(.*?)(?=\n## 9\.)", doc, re.S)
assert kpi_section
kpi_rows = [line for line in kpi_section.group(1).splitlines() if line.startswith("| Accountless") or line.startswith("| Critical") or line.startswith("| Protection") or line.startswith("| Technical") or line.startswith("| Self-service") or line.startswith("| Synthetic") or line.startswith("| Recovery") or line.startswith("| Qualified") or line.startswith("| Aggregate")]
assert len(kpi_rows) >= 10, len(kpi_rows)
kpi_header = next(line for line in kpi_section.group(1).splitlines() if line.startswith("| KPI |"))
require(kpi_header.lower(), ["source", "formula", "window", "owner", "guardrail", "decision action"], "KPI header")
print("TSK0497_KPI_CATALOGUE=PASS")

# Data quality/access/deletion and no backdoor operational analytics.
require(low, ["event absence is not automatically a negative outcome", "unknown schema versions/fields/events are rejected", "synthetic/test data cannot enter a real-user cohort", "account/operational logs are not a backdoor analytics store", "kpi percentages are not emitted when the required denominator is unavailable", "least privilege", "blocked from processing until exact purpose"], "quality/access/deletion")
print("TSK0497_QUALITY_ACCESS_DELETION=PASS")

# Historical contradiction is explicitly reconciled rather than silently preserved.
historical = Path("TSK_0497_MINIMAL_PRODUCT_EVENT_KPI_CATALOGUE_2026-08-28.md").read_text(encoding="utf-8").lower()
require(historical, ["account/login/password-reset/dashboard event while exc-0001 remains inactive", "login`, `logout`, `signup`"], "historical account exclusion")
assert "exc-0001 remains inactive" not in low
require(low, ["cr-0006 activated optional parent account", "historical tsk-0497 event names", "not independently collection-approved"], "current reconciliation")
print("TSK0497_HISTORICAL_CURRENT_RECONCILIATION=PASS")

# Non-inference.
require(low, ["does not activate telemetry", "approve a datastore", "approve a new optional-account event name", "create a legal basis", "authorize real-user processing", "prove kpi values", "gate or infer any successor pass"], "non-inference")
print("TSK0497_NON_INFERENCE=PASS")

print("TSK0497_CURRENT_ACC=PASS")
print("TSK0497_CURRENT_VER=PASS")
print("TSK0497_CURRENT_EVD_READY=PASS")
print("TSK0497_CURRENT_REVALIDATION=PASS")
