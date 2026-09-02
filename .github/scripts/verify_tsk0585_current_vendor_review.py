from __future__ import annotations

import csv
import html
import re
import subprocess
import time
import urllib.request
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "2af7f02479cee28b43c1cffe5478d518b866eea8",
    "TSK_0585_CURRENT_AUTH_VENDOR_COST_TERMS_EXIT_REVIEW_2026-09-02.md": "101fb63ed4367b514a36f5a07ee271be7cd7a5c3",
    "TSK_0045_POST_CR0008_DUAL_MODE_MAINTAINABILITY_DEPLOYMENT_COST_NFR_REVALIDATION_2026-09-02.md": "0df1b4747afea4521e4e98b0728c83750ed2b547",
    "TSK_0353_POST_CR0008_AUTHORIZATION_SESSION_ACCOUNT_LIFECYCLE_NFRS_2026-09-02.md": "3cb7c248b6d121e1c8d9db47accdf639998edc93",
    "TSK_0044_POST_CR0008_DUAL_MODE_ADGUARD_API_COMPATIBILITY_CREDENTIAL_FAILURE_NFR_REVALIDATION_2026-09-02.md": "9e2df58093c592621eb1531dc1c34393a247dd80",
}

SOURCES = {
    "firebase_pricing": "https://firebase.google.com/pricing",
    "firebase_auth": "https://firebase.google.com/docs/auth",
    "identity_pricing": "https://cloud.google.com/identity-platform/pricing",
    "firebase_privacy": "https://firebase.google.com/support/privacy",
    "firebase_terms": "https://firebase.google.com/terms/",
    "adguard_readme": "https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/master/README.md",
    "adguard_license": "https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/master/LICENSE.txt",
    "adguard_openapi": "https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/master/openapi/README.md",
}


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def norm(raw: str) -> str:
    raw = re.sub(r"(?is)<script.*?</script>|<style.*?</style>", " ", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", html.unescape(raw)).strip().lower()


def require_groups(text: str, groups: list[tuple[str, ...]], label: str) -> None:
    low = text.lower()
    missing = [group for group in groups if not any(term.lower() in low for term in group)]
    if missing:
        raise AssertionError(f"{label} missing semantic groups: {missing}")


def fetch_text(url: str) -> str:
    last = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 TSK-0585-verifier/1.0"})
            with urllib.request.urlopen(req, timeout=30) as response:
                if response.status != 200:
                    raise RuntimeError(f"HTTP {response.status}")
                return response.read().decode("utf-8", errors="replace")
        except Exception as exc:
            last = exc
            if attempt < 2:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"source fetch failed {url}: {last}")


for path, expected in EXPECTED.items():
    if not Path(path).exists():
        raise AssertionError(f"missing {path}")
    actual = blob(path)
    if actual != expected:
        raise AssertionError(f"hash drift {path}: {actual} != {expected}")
print("TSK0585_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0585")
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "MEDIUM"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert row["AI_Capability_A0_A4"] in {"A3", "A4"}
assert [d.strip() for d in (row["Dependencies"] or "").split(";") if d.strip()] == ["TSK-0045", "TSK-0353", "TSK-0044"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0585", "VER-0585", "EVD-0585")
acc = row["Acceptance_Criteria"] or ""
require_groups(acc, [
    ("dated official-source evidence",),
    ("initial auth cost assumptions",),
    ("identity platform thresholds",),
    ("no sms path",),
    ("adguard home gpl/api status", "gpl/api"),
    ("no separate adguard api subscription evidenced",),
    ("infrastructure cost remains separate",),
    ("legal review/migration triggers",),
    ("processing-location",),
], "ACC-0585")
assert (row.get("Verification_Method") or "").strip(), "missing Verification_Method"
assert (row.get("Evidence_Required") or "").strip(), "missing Evidence_Required"
print("TSK0585_CURRENT_WBS=PASS")
print("TSK0585_WBS_AI_CAPABILITY=" + row["AI_Capability_A0_A4"])
print("TSK0585_WBS_VER_METHOD=" + re.sub(r"\s+", " ", row["Verification_Method"]).strip())
print("TSK0585_WBS_EVIDENCE_REQUIRED=" + re.sub(r"\s+", " ", row["Evidence_Required"]).strip())

runtime = Path("CURRENT_STATE.md").read_text(encoding="utf-8")
for task_id in ["TSK-0045", "TSK-0353", "TSK-0044"]:
    sections = re.findall(rf"^(?:##|###) {task_id}\b.*?(?=^(?:##|###) |\Z)", runtime, re.M | re.S)
    assert sections and any("**PASS**" in s for s in sections), f"missing durable PASS {task_id}"
print("TSK0585_CURRENT_PREDECESSORS=PASS")

doc = Path("TSK_0585_CURRENT_AUTH_VENDOR_COST_TERMS_EXIT_REVIEW_2026-09-02.md").read_text(encoding="utf-8")
low = doc.lower()
assert len([line for line in doc.splitlines() if line.startswith("## ")]) >= 14
print("TSK0585_STRUCTURE=PASS")

for key, url in SOURCES.items():
    assert url in doc, (key, url)
print("TSK0585_OFFICIAL_SOURCE_REGISTER=PASS")

# Live source retrieval. Assertions use broad semantic groups, not sentence-exact copy.
live = {key: norm(fetch_text(url)) for key, url in SOURCES.items()}
print("TSK0585_LIVE_SOURCE_FETCH=PASS")

require_groups(live["firebase_pricing"], [
    ("spark plan",), ("no payment method",), ("other authentication services",),
    ("billed per sms", "phone auth"),
], "Firebase pricing live")
print("TSK0585_LIVE_FIREBASE_BASE_PRICING=PASS")

require_groups(live["firebase_auth"], [
    ("optional upgrade",), ("3,000 daily active users", "3,000 daus"),
    ("50,000 monthly active users", "50,000 users"),
    ("saml",), ("openid connect",),
], "Firebase Authentication live")
print("TSK0585_LIVE_IDENTITY_PLATFORM_LIMITS=PASS")

require_groups(live["identity_pricing"], [
    ("0 count to 50,000", "50,000"), ("0.0055",), ("0.0046",),
    ("0.0032",), ("0.0025",), ("0.015",), ("saml",), ("openid connect",),
], "Identity Platform pricing live")
print("TSK0585_LIVE_IDENTITY_PLATFORM_PRICING=PASS")

require_groups(live["firebase_privacy"], [
    ("firebase authentication",), ("us data centers",),
    ("exclusively in the united states",),
], "Firebase privacy live")
print("TSK0585_LIVE_AUTH_PROCESSING_LOCATION=PASS")

require_groups(live["firebase_terms"], [
    ("may 1, 2026",), ("firebase authentication",),
    ("google cloud platform terms of service",),
], "Firebase terms live")
print("TSK0585_LIVE_FIREBASE_TERMS=PASS")

require_groups(live["adguard_readme"], [
    ("free and open source",), ("rest api",),
], "AdGuard README live")
require_groups(live["adguard_license"], [("gnu general public license",), ("version 3",)], "AdGuard license live")
require_groups(live["adguard_openapi"], [("openapi",), ("api specification",), ("basic access authentication", "authorization: basic")], "AdGuard OpenAPI live")
print("TSK0585_LIVE_ADGUARD_LICENSE_API=PASS")

# Artifact semantics / no overclaiming.
require_groups(doc, [
    ("initial authentication-service fee assumption = $0",),
    ("identity platform is optional",), ("3,000 dau",), ("50,000 mau",),
    ("0.0055",), ("0.0046",), ("0.0032",), ("0.0025",), ("0.015",),
    ("zero sms/phone messages",),
], "auth cost disposition")
print("TSK0585_AUTH_COST_THRESHOLDS=PASS")

require_groups(doc, [
    ("processing location for firebase authentication is currently confirmed as united states-only",),
    ("legal/transfer acceptability remains unresolved", "legally acceptable"),
    ("no location or transfer fact", "not inferred"),
], "processing location disposition")
print("TSK0585_PROCESSING_LOCATION_NO_GUESS=PASS")

require_groups(doc, [
    ("adguard home software licence fee: $0 evidenced",),
    ("separate adguard home api subscription fee: none evidenced",),
    ("infrastructure", "separate"),
    ("gpl-3.0",),
    ("does not mean gpl has no obligations",),
], "AdGuard cost/license disposition")
assert "adguard home api subscription fee: $0 guaranteed" not in low
assert "adguard home api will always be free" not in low
print("TSK0585_ADGUARD_COST_LICENSE_BOUNDARY=PASS")

triggers = re.search(r"## 7\. Firebase terms / vendor boundary(.*?)(?=\n## 8\.)", doc, re.S)
assert triggers and len(re.findall(r"^\d+\. ", triggers.group(1), re.M)) >= 10
adg_triggers = re.search(r"## 9\. AdGuard exit / re-review triggers(.*?)(?=\n## 10\.)", doc, re.S)
assert adg_triggers and len(re.findall(r"^\d+\. ", adg_triggers.group(1), re.M)) >= 8
print("TSK0585_EXIT_TRIGGERS=PASS")

require_groups(doc, [
    ("infrastructure cost is separate",),
    ("vm compute",), ("storage/backups",), ("database/storage",),
    ("$0 end-to-end service cost",),
], "infrastructure separation")
print("TSK0585_INFRASTRUCTURE_COST_SEPARATION=PASS")

require_groups(doc, [
    ("does not determine",), ("lawful basis",), ("transfer mechanism",),
    ("gpl obligations",), ("vendor-contract acceptance",),
    ("unresolved rather than guessed",),
], "unresolved legal boundary")
print("TSK0585_LEGAL_UNRESOLVED_NO_GUESS=PASS")

matrix = re.search(r"## 11\. Current factual disposition matrix(.*?)(?=\n## 12\.)", doc, re.S)
assert matrix and len([line for line in matrix.group(1).splitlines() if line.startswith("|") and not re.match(r"^\|\s*-", line)]) >= 13
print("TSK0585_FACT_MATRIX=PASS")

require_groups(doc, [
    ("does not activate",), ("purchase",), ("legal",),
    ("no vendor activation",), ("successor pass",),
], "non-inference")
print("TSK0585_NON_INFERENCE=PASS")

print("TSK0585_CURRENT_ACC=PASS")
print("TSK0585_CURRENT_VER=PASS")
print("TSK0585_CURRENT_EVD_READY=PASS")
print("TSK0585_CURRENT_REVIEW=PASS")
