from __future__ import annotations

import csv
import re
import subprocess
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "6cc78a81d3b503902c915a2b02d88b81f75b8342",
    "TSK_0307_SOURCE_BACKED_INSTRUCTION_CONTENT_CATALOGUE_2026-08-28.md": "d717c9b3f66197abe1f3e73361633f222b817e7c",
    "TSK_0307_SOURCE_BACKED_INSTRUCTION_CONTENT_CATALOGUE_EVIDENCE_2026-08-28.md": "7bc98f1b18f3a20c9a6be75138a4704b2002bf2f",
    "TSK_0317_POST_CR0008_CURRENT_PLATFORM_PATH_REVALIDATION_2026-09-02.md": "37173d2f9cb970a7b5e6a83af90c8f868f9fbfa8",
    "TSK_0307_POST_CR0008_CURRENT_SOURCE_BACKED_INSTRUCTION_CATALOGUE_REVALIDATION_2026-09-02.md": "73a7028e247833bfe7e98487d9e079a51d36d424",
}

IDS = [
    "INS-AND-SETUP-01", "INS-AND-VERIFY-01", "INS-AND-REMOVE-01",
    "INS-IOS-SETUP-01", "INS-IOS-VERIFY-01", "INS-IOS-REMOVE-01",
    "INS-COMMON-UNCERTAIN-01", "INS-COMMON-NOTCOVERED-01", "INS-COMMON-RECOVERY-01",
]


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def tracked_text(path: str) -> str:
    return subprocess.check_output(["git", "show", f"HEAD:{path}"], text=True)


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def require(text: str, concepts: list[str], label: str) -> None:
    n = norm(text)
    missing = [c for c in concepts if norm(c) not in n]
    if missing:
        raise AssertionError(f"{label} missing {missing}")


for path, expected in EXPECTED.items():
    assert Path(path).exists(), path
    actual = blob(path)
    assert actual == expected, f"hash drift {path}: {actual} != {expected}"
print("TSK0307_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0307")
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "HIGH"
assert row["AI_Capability_A0_A4"] == "A3"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert [d.strip() for d in row["Dependencies"].split(";") if d.strip()] == ["TSK-0317"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0307", "VER-0307", "EVD-0307")
require(row["Acceptance_Criteria"], ["official source", "platform/version/region", "owner", "last verification", "review trigger", "localized variants", "known limits", "test reference"], "ACC-0307")
print("TSK0307_CURRENT_WBS=PASS")

runtime = tracked_text("CURRENT_STATE.md")
pat = re.compile(r"^(##|###) TSK-0317\b.*?(?=^(?:##|###) |\Z)", re.M | re.S)
assert any("**PASS" in m.group(0) for m in pat.finditer(runtime)), "TSK-0317 durable PASS missing"
print("TSK0307_CURRENT_PREDECESSOR=PASS")

current = tracked_text("TSK_0307_POST_CR0008_CURRENT_SOURCE_BACKED_INSTRUCTION_CATALOGUE_REVALIDATION_2026-09-02.md")
predecessor = tracked_text("TSK_0317_POST_CR0008_CURRENT_PLATFORM_PATH_REVALIDATION_2026-09-02.md")
historical = tracked_text("TSK_0307_SOURCE_BACKED_INSTRUCTION_CONTENT_CATALOGUE_2026-08-28.md")
historical_evd = tracked_text("TSK_0307_SOURCE_BACKED_INSTRUCTION_CONTENT_CATALOGUE_EVIDENCE_2026-08-28.md")

require(historical_evd, ["nine current instruction classes", "official/current source", "platform/version", "region/locale", "owner", "last verification", "review trigger", "localized variants", "known limits", "test reference"], "historical provenance")
print("TSK0307_HISTORICAL_PROVENANCE=PASS")

require(predecessor, ["dns.usesafeweb.com", "https://dns.usesafeweb.com/dns-query", "accountless core remains complete", "optional account is orthogonal continuity", "profile installation and removal remain explicit user/OS actions", "do not instruct the user to weaken security"], "current predecessor")
assert "`SafeWeb`" in predecessor and "`SafeWeb DNS`" in predecessor
print("TSK0307_PREDECESSOR_ALIGNMENT=PASS")

lines = current.splitlines()
header_idx = next(i for i,l in enumerate(lines) if l.startswith("| ID | Purpose | Platform/version |"))
rows_md=[]
for line in lines[header_idx+2:]:
    if not line.startswith("|"):
        break
    cells=[c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells)==10:
        rows_md.append(cells)
assert len(rows_md)==9, len(rows_md)
seen=[]
for cells in rows_md:
    ident=cells[0].strip("`"); seen.append(ident)
    assert ident in IDS
    assert all(cells[i] for i in range(10)), ident
    assert cells[6] == "2026-09-02", (ident,cells[6])
    for idx in [4,5,7,8,9]: assert len(cells[idx]) >= 4, (ident,idx)
assert seen == IDS, seen
print("TSK0307_REGISTRY_FIELDS=9/9_PASS")

source_review = current.split("## 2. Current official-source review — 2026-09-02",1)[1].split("## 3. Current project sources",1)[0]
source_urls = re.findall(r"https://[^\s)`]+", source_review)
assert len(source_urls) == 6, source_urls
assert any("support.google.com/android/answer/9654714" in u for u in source_urls)
assert any("developer.android.com/reference/android/app/admin/DevicePolicyManager" in u for u in source_urls)
assert any("developer.android.com/reference/android/net/LinkProperties" in u for u in source_urls)
assert any("support.apple.com/guide/deployment/dns-settings" in u for u in source_urls)
assert any("support.apple.com/guide/iphone/install-or-remove-configuration-profiles" in u for u in source_urls)
assert any("support.apple.com/guide/personal-safety" in u for u in source_urls)
assert all(any(host in u for host in ["support.google.com", "developer.android.com", "support.apple.com"]) for u in source_urls)
print("TSK0307_OFFICIAL_SOURCE_SET=PASS")

require(current, ["Private DNS provider hostname", "DNS questions/answers", "hostname serving DNS-over-TLS", "Private DNS is active", "HTTPS or TLS", "VPN & Device Management", "explicit user permission"], "current source semantics")
print("TSK0307_CURRENT_SOURCE_SEMANTICS=PASS")

assert "dns.usesafeweb.com" in current
assert "https://dns.usesafeweb.com/dns-query" in current
for forbidden in ["Get UseSafeWeb profile", "Turn on UseSafeWeb"]:
    assert current.count(forbidden) == 1, forbidden
variants=current.split("## 6. Current instruction variants",1)[1].split("## 7. Acceptance reconciliation",1)[0]
assert "UseSafeWeb" not in variants
require(variants, ["SafeWeb DNS", "Return to SafeWeb", "Verified", "Status uncertain", "Remove SafeWeb DNS"], "current visible copy")
print("TSK0307_SAFEWEB_NAMING=PASS")

sections = [
    "### Android setup", "### Android verification", "### Android removal/recovery",
    "### iPhone setup", "### iPhone verification", "### iPhone removal/recovery",
    "### Common uncertainty", "### Common not covered", "### Common recovery",
]
for heading in sections:
    assert heading in current, heading
variant_segments = re.split(r"^### ", variants, flags=re.M)[1:]
assert len(variant_segments) == 9, len(variant_segments)
for segment in variant_segments:
    require(segment, ["en-GB", "tr-TR", "ar"], segment.splitlines()[0])
print("TSK0307_LOCALIZED_VARIANTS=9/9_PASS")

require(current, [
    "accountless setup/verification/help/removal remains complete",
    "never substitutes for technical verification",
    "no browsing/query/activity history",
    "do not repeatedly replay a failed consequential platform action",
    "do not weaken that control merely to make SafeWeb green",
    "profile removal ends its DNS configuration claim only",
    "no silent plaintext fallback",
], "truth and recovery")
print("TSK0307_TRUTH_SAFETY_RECOVERY=PASS")

assert "UseSafeWeb" in historical
assert "historical parent-facing copy uses the superseded visible name" in norm(current)
assert "Parent-facing product name is **SafeWeb** / **SafeWeb DNS**" in current
assert "technical identifiers continue to use the `usesafeweb.com` domain" in current
print("TSK0307_HISTORICAL_CURRENT_RECONCILIATION=PASS")

non_inference = current.split("## 8. Non-inference",1)[1]
require(non_inference, ["does not distribute a production Apple profile", "implement account/session/dashboard behavior", "prove native-speaker/representative-parent comprehension", "legal/privacy completion", "public publication", "participant processing", "payment", "market activation", "LG-06", "launch"], "non-inference")
print("TSK0307_NON_INFERENCE=PASS")
print("TSK0307_CURRENT_ACC=PASS")
print("TSK0307_CURRENT_VER=PASS")
print("TSK0307_CURRENT_EVD_READY=PASS")
print("TSK0307_CURRENT_REVALIDATION=PASS")
