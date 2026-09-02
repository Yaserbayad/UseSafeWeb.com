from __future__ import annotations

import csv
import re
import subprocess
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "b0e320a862eaf83b3fea11e565b42621608578eb",
    "TSK_0046_POST_CR0008_DUAL_MODE_PERFORMANCE_CAPACITY_NFR_REVALIDATION_2026-09-02.md": "8e72d542b68de6f7f5c8c375b63b6229c6d15529",
    "TSK_0046_PERFORMANCE_CAPACITY_NFR_2026-08-28.md": "2c48f975d557b1bb4ba6c58c2a8ad3580b2c7b06",
    "TSK_0046_PERFORMANCE_CAPACITY_NFR_EVIDENCE_2026-08-28.md": "09d111530c5e9c86feb2cafb54f62fb046a44b6f",
    "TSK_0538_POST_CR0008_DUAL_MODE_RELIABILITY_OBSERVABILITY_NFR_REVALIDATION_2026-09-02.md": "44c9c299465e821e2ffd84a54b77e3e615d61925",
    "TSK_0538_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md": "3ba04601ea5574fcd1fb1f58f95922ae94b74ac2",
}


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def require_all(text: str, concepts: list[str], label: str) -> None:
    missing = [c for c in concepts if c not in text]
    if missing:
        raise AssertionError(f"{label} missing concepts: {missing}")


for path, expected in EXPECTED.items():
    if not Path(path).exists():
        raise AssertionError(f"missing {path}")
    actual = blob(path)
    if actual != expected:
        raise AssertionError(f"hash drift {path}: {actual} != {expected}")
print("TSK0046_V3_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0046")
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "MEDIUM"
assert row["AI_Capability_A0_A4"] == "A3"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert [d.strip() for d in row["Dependencies"].split(";") if d.strip()] == ["TSK-0538"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0046", "VER-0046", "EVD-0046")
acc = row["Acceptance_Criteria"].lower()
for group in [
    ["expected", "load"],
    ["safety", "margin"],
    ["dns", "latency", "availability"],
    ["web", "performance"],
    ["degradation", "behavior"],
    ["capacity", "review", "trigger"],
]:
    require_all(acc, group, "ACC-0046")
print("TSK0046_V3_WBS=PASS")

runtime = Path("CURRENT_STATE.md").read_text(encoding="utf-8")
task_sections: dict[str, list[str]] = {}
for match in re.finditer(r"^(##|###) (TSK-\d{4})\b.*?(?=^(?:##|###) |\Z)", runtime, re.M | re.S):
    task_sections.setdefault(match.group(2), []).append(match.group(0))
assert any("**PASS" in section and "current accepted" in section.splitlines()[0].lower() for section in task_sections.get("TSK-0538", []))
print("TSK0046_V3_PREDECESSOR=PASS")

doc = Path("TSK_0046_POST_CR0008_DUAL_MODE_PERFORMANCE_CAPACITY_NFR_REVALIDATION_2026-09-02.md").read_text(encoding="utf-8")
low = doc.lower()


def section(number: int, next_number: int | None) -> str:
    end = rf"(?=\n## {next_number}\.)" if next_number is not None else r"\Z"
    match = re.search(rf"## {number}\.[^\n]*\n(.*?){end}", doc, re.S)
    if not match:
        raise AssertionError(f"missing section {number}")
    return match.group(1).lower()

s4 = section(4, 5)
require_all(s4, ["lg-09", "0 real-user devices", "unfrozen", "n_dns_active_peak", "q_dns_expected", "r_accountless_peak", "r_session_peak", "r_dashboard_peak", "r_mutation_peak", "c_account_peak"], "load scope")
print("TSK0046_V3_LOAD_SCOPE=PASS")

s5 = section(5, 6)
require_all(s5, ["2×", "expected", "correctness", "security", "privacy", "rate-limit"], "safety margin")
s6 = section(6, 7)
require_all(s6, ["doh", "dot", "tls", "synthetic", "p50/p95/p99", "rate-limit", "correctness"], "dns method")
assert "allow" in s6 and "block" in s6
print("TSK0046_V3_MARGIN_DNS=PASS")

s7 = section(7, 8)
require_all(s7, ["accountless core journey", "optional-account journey", "cross-parent", "provider/datastore", "ambiguous consequential mutations", "p50/p95/p99", "technical protection verification"], "dual-mode web performance")
require_all(low, [">=99.9%", "p95 `<=1.0s`", "p99 `<=2.0s`", "authorization isolation", "accountless fallback"], "TSK-0538 targets")
print("TSK0046_V3_DUAL_MODE_PERFORMANCE=PASS")

s8 = section(8, 9)
require_all(s8, ["web.dev/articles/vitals", "web.dev/articles/defining-core-web-vitals-thresholds", "web.dev/articles/vitals-spa-faq", "lcp `<=2.5s`", "inp `<=200ms`", "cls `<=0.1`", "75th percentile", "soft-navigation", "synthetic/lab results do not prove field p75"], "web performance")
print("TSK0046_V3_WEB_PERF=PASS")

s9 = section(9, 10)
s10 = section(10, 11)
assert len(re.findall(r"^\d+\.", s9, re.M)) >= 12
require_all(s9, ["cpu", "memory", "p95/p99", "provider/datastore", "2× margin", "accountless"], "capacity triggers")
require_all(s10, ["encrypted-dns correctness", "account-only authority fails closed", "dns/query/activity-history", "/control", "supported/ramped load"], "degradation")
print("TSK0046_V3_TRIGGERS_DEGRADATION=PASS")

historical = Path("TSK_0046_PERFORMANCE_CAPACITY_NFR_2026-08-28.md").read_text(encoding="utf-8").lower()
assert "cr-0003" in historical and "pilot" in historical
assert "cr-0003 remains active" not in low
require_all(low, ["no separate mandatory pilot/staging lifecycle is reintroduced", "live-production", "optional parent", "complete accountless core"], "historical reconciliation")
print("TSK0046_V3_RECONCILIATION=PASS")

s15 = section(15, None)
require_all(s15, ["live-production activation", "real-user cohort/load", "production stress testing", "infrastructure resize/ha/new paid monitoring", "web/app/account/auth implementation", "legal/privacy completion", "successor pass"], "non-inference")
print("TSK0046_V3_NON_INFERENCE=PASS")

print("TSK0046_CURRENT_ACC=PASS")
print("TSK0046_CURRENT_VER=PASS")
print("TSK0046_CURRENT_EVD_READY=PASS")
print("TSK0046_CURRENT_REVALIDATION=PASS")
