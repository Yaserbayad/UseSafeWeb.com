from __future__ import annotations

import csv
import re
import subprocess
import time
import urllib.request
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "761a608e37a959b237336d5f44aefefb4dc4fa3f",
    "TSK_0352_POST_CR0008_ADGUARD_PERSISTENT_CLIENTID_API_LIFECYCLE_CONTRACT_2026-09-02.md": "e5cbbcac2f42810527717549482765b6b1ad72c1",
}

OPENAPI_URL = "https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/v0.107.79/openapi/openapi.yaml"
LOCALE_URL = "https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/v0.107.79/client/src/__locales/en.json"
CLIENTS_DOC_URL = "https://raw.githubusercontent.com/wiki/AdguardTeam/AdGuardHome/Clients.md"


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def fetch(url: str) -> str:
    last = None
    for attempt in range(3):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "TSK-0352-verifier/1.0"})
            with urllib.request.urlopen(request, timeout=30) as response:
                if response.status != 200:
                    raise RuntimeError(f"HTTP {response.status}")
                return response.read().decode("utf-8", errors="replace")
        except Exception as exc:
            last = exc
            if attempt < 2:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"failed to fetch {url}: {last}")


def require_groups(text: str, groups: list[tuple[str, ...]], label: str) -> None:
    low = text.lower()
    missing = [group for group in groups if not any(term.lower() in low for term in group)]
    if missing:
        raise AssertionError(f"{label} missing semantic groups: {missing}")


def sections(runtime: str, task_id: str) -> list[str]:
    return re.findall(rf"^(?:##|###) {re.escape(task_id)}\b.*?(?=^(?:##|###) |\Z)", runtime, re.M | re.S)


for path, expected in EXPECTED.items():
    if not Path(path).exists():
        raise AssertionError(f"missing {path}")
    actual = blob(path)
    if actual != expected:
        raise AssertionError(f"hash drift {path}: {actual} != {expected}")
print("TSK0352_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0352")
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "MEDIUM"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert row["AI_Capability_A0_A4"] in {"A3", "A4"}
assert [d.strip() for d in (row["Dependencies"] or "").split(";") if d.strip()] == ["TSK-0041", "TSK-0142"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0352", "VER-0352", "EVD-0352")
acc = row["Acceptance_Criteria"] or ""
require_groups(acc, [
    ("allowlisted server-side client add/search/update/delete",),
    ("high-entropy clientid generation",),
    ("direct doh endpoint",),
    ("ignore_querylog",),
    ("ignore_statistics",),
    ("idempotency",),
    ("authorization",),
    ("rollback/reconciliation",),
    ("version compatibility",),
    ("prohibition of arbitrary /control proxying",),
    ("browser admin credentials",),
], "ACC-0352")
assert (row.get("Verification_Method") or "").strip()
assert (row.get("Evidence_Required") or "").strip()
print("TSK0352_CURRENT_WBS=PASS")
print("TSK0352_WBS_AI_CAPABILITY=" + row["AI_Capability_A0_A4"])
print("TSK0352_WBS_VER_METHOD=" + re.sub(r"\s+", " ", row["Verification_Method"]).strip())
print("TSK0352_WBS_EVIDENCE_REQUIRED=" + re.sub(r"\s+", " ", row["Evidence_Required"]).strip())

runtime = Path("CURRENT_STATE.md").read_text(encoding="utf-8")
for tid in ["TSK-0041", "TSK-0142"]:
    ss = sections(runtime, tid)
    assert ss and any("**PASS**" in s for s in ss), f"missing durable PASS {tid}"
print("TSK0352_CURRENT_PREDECESSORS=PASS")

doc = Path("TSK_0352_POST_CR0008_ADGUARD_PERSISTENT_CLIENTID_API_LIFECYCLE_CONTRACT_2026-09-02.md").read_text(encoding="utf-8")
assert len([line for line in doc.splitlines() if line.startswith("## ")]) >= 19
print("TSK0352_STRUCTURE=PASS")

# Immutable version-pinned upstream API/UI + official clients documentation.
openapi = fetch(OPENAPI_URL)
locale = fetch(LOCALE_URL)
clients_doc = fetch(CLIENTS_DOC_URL)
print("TSK0352_UPSTREAM_FETCH=PASS")

require_groups(openapi, [
    ("'version': '0.107'",), ("'url': '/control'",), ("'basicAuth': []",),
    ("'/clients/add':",), ("'/clients/search':",), ("'/clients/update':",), ("'/clients/delete':",),
    ("'operationId': 'clientsAdd'",), ("'operationId': 'clientsSearch'",),
    ("'operationId': 'clientsUpdate'",), ("'operationId': 'clientsDelete'",),
], "OpenAPI operations")
print("TSK0352_VERSION_PINNED_API=PASS")

require_groups(openapi, [
    ("'description': 'IP, CIDR, MAC, or ClientID.'",),
    ("'ignore_querylog':",), ("'ignore_statistics':",),
    ("'description': 'Client search request'",),
    ("'description': 'Client IP address, CIDR, MAC address, or ClientID'",),
    ("'description': 'Client update request'",),
    ("'description': 'Client delete request'",),
], "OpenAPI client schema")
print("TSK0352_VERSION_PINNED_CLIENT_SCHEMA=PASS")

assert "ClientID must contain only numbers, lowercase letters, and hyphens" in locale
print("TSK0352_VERSION_PINNED_CLIENTID_SYNTAX=PASS")

require_groups(clients_doc, [
    ("persistent clients",), ("clientid",),
    ("dns-over-https",), ("/dns-query/",),
], "Clients documentation")
print("TSK0352_OFFICIAL_DOH_CLIENTID_ROUTE=PASS")

require_groups(doc, [
    ("post /control/clients/search",), ("post /control/clients/add",),
    ("post /control/clients/update",), ("post /control/clients/delete",),
    ("never expose generic adguard `/control` proxying",),
], "API allowlist")
print("TSK0352_API_ALLOWLIST=PASS")

require_groups(doc, [
    ("26 lowercase rfc-4648 base32",), ("approximately 130 bits",),
    ("cryptographically secure random source",), ("collision check",),
    ("does **not** make clientid an authorization secret", "does not make clientid an authorization secret"),
], "ClientID generation")
print("TSK0352_CLIENTID_GENERATION=PASS")

require_groups(doc, [
    ("ignore_querylog = true",), ("ignore_statistics = true",),
    ("explicitly",), ("global no-query-log/no-statistics",),
    ("no customer-specific unrestricted filtering",),
], "privacy settings")
print("TSK0352_PRIVACY_SETTINGS=PASS")

require_groups(doc, [
    ("https://dns.usesafeweb.com/dns-query/{client_id}",),
    ("accountless path remains `https://dns.usesafeweb.com/dns-query`",),
    ("not an account authorization credential", "never an authorization"),
    ("does not itself prove", "protection map"),
], "direct DoH")
print("TSK0352_DIRECT_DOH_ENDPOINT=PASS")

for heading, concepts, marker in [
    ("## 7. Create lifecycle", ["creating", "clients/add", "clients/search", "read-back"], "CREATE"),
    ("## 8. Read/search lifecycle", ["one exact expected match", "zero matches", "conflict", "drift"], "SEARCH"),
    ("## 9. Update / repair lifecycle", ["clients/update", "server-known current name", "read back"], "UPDATE"),
    ("## 10. ClientID rotation / replacement", ["rotating", "old id", "new id", "physical device/profile"], "ROTATE"),
    ("## 11. Unlink / revoke / delete lifecycle", ["clients/delete", "server-read", "search", "absent"], "DELETE"),
]:
    start = doc.find(heading)
    assert start >= 0, heading
    next_start = doc.find("\n## ", start + len(heading))
    section = doc[start: next_start if next_start >= 0 else len(doc)].lower()
    for concept in concepts:
        assert concept.lower() in section, (heading, concept)
    print(f"TSK0352_{marker}_LIFECYCLE=PASS")

require_groups(doc, [
    ("parent a cannot",), ("parent b",),
    ("clientid possession cannot become ownership",),
    ("authorization is rechecked",),
    ("basic-auth credential remains restricted",),
], "authorization IDOR")
print("TSK0352_AUTHORIZATION_IDOR=PASS")

require_groups(doc, [
    ("no upstream idempotency key is assumed",),
    ("at most one consequential mutation",),
    ("search/read actual adguard state before retry",),
    ("http 200 alone is not terminal evidence",),
    ("datastore and adguard terminal truth must agree",),
], "idempotency reconciliation")
print("TSK0352_IDEMPOTENCY_RECONCILIATION=PASS")

require_groups(doc, [
    ("rollback is state-based",),
    ("delete an orphan only when",),
    ("search both old/new ids",),
    ("recovery does not resurrect",),
], "rollback")
print("TSK0352_ROLLBACK_RECOVERY=PASS")

require_groups(doc, [
    ("verify `/control` private basic-auth boundary",),
    ("verify clientid syntax/routing behavior",),
    ("rerun crud/rotation/idempotency/authorization/privacy/rollback tests",),
    ("fail closed",),
    ("no future adguard endpoint",),
], "version gate")
print("TSK0352_VERSION_DRIFT_GATE=PASS")

catalog = re.search(r"## 18\. Deterministic implementation acceptance catalogue\n(.*?)(?=\n## 19\.)", doc, re.S)
assert catalog, "assertion catalogue missing"
assert len(re.findall(r"^\d+\. ", catalog.group(1), re.M)) == 30
print("TSK0352_ASSERTION_CATALOGUE=PASS")

require_groups(doc, [
    ("does not",), ("implement or deploy",),
    ("create/update/delete any live adguard client",),
    ("make login mandatory",), ("successor",),
], "non-inference")
print("TSK0352_NON_INFERENCE=PASS")

print("TSK0352_CURRENT_ACC=PASS")
print("TSK0352_CURRENT_VER=PASS")
print("TSK0352_CURRENT_EVD_READY=PASS")
print("TSK0352_CURRENT_CONTRACT=PASS")
