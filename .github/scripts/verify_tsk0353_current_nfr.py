from __future__ import annotations

import csv
import re
import subprocess
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "0a0fc742d3e0d54dbb07c29275b4d5e1358c4fd4",
    "TSK_0353_POST_CR0008_AUTHORIZATION_SESSION_ACCOUNT_LIFECYCLE_NFRS_2026-09-02.md": "3cb7c248b6d121e1c8d9db47accdf639998edc93",
    "TSK_0230_PRIVACY_DATA_MINIMISATION_RETENTION_DELETION_NFRS_2026-09-01.md": "eda85b062a3a7ba29544de35a8a813c9790092f2",
    "TSK_0484_POST_CR0008_SECURITY_ABUSE_NFR_REVALIDATION_2026-09-02.md": "285ee390499190137e8aac0fed976975fb79ed80",
    "TSK_0044_POST_CR0008_DUAL_MODE_ADGUARD_API_COMPATIBILITY_CREDENTIAL_FAILURE_NFR_REVALIDATION_2026-09-02.md": "9e2df58093c592621eb1531dc1c34393a247dd80",
}


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def require_groups(text: str, groups: list[tuple[str, ...]], label: str) -> None:
    low = text.lower()
    missing = [group for group in groups if not any(term.lower() in low for term in group)]
    if missing:
        raise AssertionError(f"{label} missing semantic groups: {missing}")


def task_sections(runtime: str, task_id: str) -> list[str]:
    return re.findall(rf"^(?:##|###) {re.escape(task_id)}\b.*?(?=^(?:##|###) |\Z)", runtime, re.M | re.S)


def markdown_rows(section: str, header_prefix: str) -> list[str]:
    out = []
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        if line.startswith(header_prefix) or re.match(r"^\|\s*-+", line):
            continue
        out.append(line)
    return out


for path, expected in EXPECTED.items():
    if not Path(path).exists():
        raise AssertionError(f"missing {path}")
    actual = blob(path)
    if actual != expected:
        raise AssertionError(f"hash drift {path}: {actual} != {expected}")
print("TSK0353_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0353")
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "MEDIUM"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert row["AI_Capability_A0_A4"] in {"A3", "A4"}
assert [d.strip() for d in (row["Dependencies"] or "").split(";") if d.strip()] == ["TSK-0230", "TSK-0484"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0353", "VER-0353", "EVD-0353")
acc = row["Acceptance_Criteria"] or ""
require_groups(acc, [
    ("firebase/google token verification", "firebase", "google token"),
    ("httponly",), ("secure",), ("samesite",),
    ("csrf",), ("revocation",), ("account takeover",),
    ("parent-to-device ownership", "ownership"), ("idor",),
    ("rate limits", "rate limit"), ("logout/deletion", "logout", "deletion"),
    ("provider outage",), ("privacy-safe security audit events", "security audit events"),
], "ACC-0353")
assert (row.get("Verification_Method") or "").strip(), "missing Verification_Method"
assert (row.get("Evidence_Required") or "").strip(), "missing Evidence_Required"
print("TSK0353_CURRENT_WBS=PASS")
print("TSK0353_WBS_AI_CAPABILITY=" + row["AI_Capability_A0_A4"])
print("TSK0353_WBS_VER_METHOD=" + re.sub(r"\s+", " ", row["Verification_Method"]).strip())
print("TSK0353_WBS_EVIDENCE_REQUIRED=" + re.sub(r"\s+", " ", row["Evidence_Required"]).strip())

runtime = Path("CURRENT_STATE.md").read_text(encoding="utf-8")
for tid in ["TSK-0230", "TSK-0484"]:
    sections = task_sections(runtime, tid)
    assert sections and any("**PASS**" in s for s in sections), f"missing current/historical durable PASS {tid}"
print("TSK0353_CURRENT_PREDECESSORS=PASS")

doc = Path("TSK_0353_POST_CR0008_AUTHORIZATION_SESSION_ACCOUNT_LIFECYCLE_NFRS_2026-09-02.md").read_text(encoding="utf-8")
low = doc.lower()
assert len([line for line in doc.splitlines() if line.startswith("## ")]) >= 17
print("TSK0353_STRUCTURE=PASS")

require_groups(doc, [
    ("firebase, **verify id tokens**", "firebase", "verify id tokens"),
    ("manage session cookies",), ("manage user sessions",),
    ("google identity services",), ("owasp session management",),
    ("idor prevention", "authorization guidance"),
], "source review")
print("TSK0353_SOURCE_REVIEW=PASS")

require_groups(doc, [
    ("dedicated https session-exchange endpoint",),
    ("firebase admin sdk",),
    ("wrong-project", "aud"), ("wrong-issuer", "iss"),
    ("non-expired", "exp"), ("non-empty `sub`", "uid"),
    ("auth_time <= 5 minutes", "<=5-minute"),
    ("checkrevoked=true", "revocation-aware"),
    ("disabled/deleted/revoked",),
    ("localstorage/sessionstorage",),
], "Firebase token contract")
print("TSK0353_FIREBASE_TOKEN_VERIFICATION=PASS")

require_groups(doc, [
    ("g_csrf_token",), ("signature",), ("`aud`",), ("`iss`",), ("`exp`",),
    ("`sub` is the unique provider identity key",),
    ("email is **not** an ownership/authorization key", "email alone cannot"),
    ("no automatic account merge/link",),
], "Google token contract")
print("TSK0353_GOOGLE_TOKEN_VERIFICATION=PASS")

require_groups(doc, [
    ("accountless j0/j1 state is never silently", "never silently converted/promoted/copied"),
    ("no child identity/profile",),
    ("no browsing/dns query/domain/url history",),
    ("raw provider token",),
], "data minimisation")
print("TSK0353_DATA_MINIMISATION=PASS")

require_groups(doc, [
    ("`secure` — mandatory",), ("`httponly` — mandatory",),
    ("samesite=lax",), ("path=/", "`path=/`"),
    ("no `domain` attribute",), ("__host-",),
    ("never `samesite=none`",),
    ("maximum 7 days",), ("no sliding extension",),
    ("session fixation",), ("persistence is `none`", "non-persistent mode"),
], "session cookie")
print("TSK0353_SESSION_COOKIE=PASS")

require_groups(doc, [
    ("safe http methods",), ("unsafe request",),
    ("server-validated csrf token",), ("origin",), ("referer",),
    ("samesite does not replace",), ("zero authorized effect",),
], "CSRF")
print("TSK0353_CSRF=PASS")

require_groups(doc, [
    ("derive current `parent_id` from the verified server session",),
    ("request-supplied account/device/clientid/reference",),
    ("deny by default",), ("re-check authorization",),
    ("never authorize via obscurity",),
    ("parent a", "parent b"),
    ("zero unauthorized data/effect",),
], "ownership/IDOR")
print("TSK0353_OWNERSHIP_IDOR=PASS")

require_groups(doc, [
    ("high-risk operations require **recent authentication <=5 minutes**",),
    ("email/display name is never sufficient",),
    ("suspected token theft",),
    ("no local password",), ("sms",), ("mfa is not claimed",),
], "account takeover")
print("TSK0353_ACCOUNT_TAKEOVER=PASS")

require_groups(doc, [
    ("current-browser logout",), ("clears the host session cookie",),
    ("sign out all sessions", "global/security revocation"),
    ("revoke refresh tokens", "refresh-token revocation"),
    ("pending/uncertain",),
], "logout/revocation")
print("TSK0353_LOGOUT_REVOCATION=PASS")

require_groups(doc, [
    ("account deletion is a high-risk",), ("opaque operation id",),
    ("account to `deleting`",), ("invalidate/revoke active account sessions",),
    ("owned device records",), ("pending_reconciliation",),
    ("never claim physical dns/profile removal",),
    ("never resurrect",),
], "account deletion")
print("TSK0353_ACCOUNT_DELETION=PASS")

require_groups(doc, [
    ("provider unavailable",), ("no new account session",),
    ("accountless setup/verify/protection map/recovery/removal",),
    ("ownership datastore unavailable",),
    ("stale cache is not authority",),
    ("ambiguous partial writes reconcile",),
], "outage")
print("TSK0353_PROVIDER_DATASTORE_OUTAGE=PASS")

rate = re.search(r"## 12\. Rate-limit and abuse-control NFRs\n(.*?)(?=\n## 13\.)", doc, re.S)
assert rate, "rate section missing"
rate_rows = markdown_rows(rate.group(1), "| Surface |")
assert len(rate_rows) == 5, len(rate_rows)
require_groups(rate.group(1), [
    ("10 attempts / 5 min",), ("5 attempts / 5 min",),
    ("20 / 5 min",), ("30 / 5 min",), ("5 attempts / hour",),
    ("short-ttl keyed hash", "memory/short-ttl keyed hash"),
], "rate limits")
print("TSK0353_RATE_LIMITS=PASS")

audit = re.search(r"## 13\. Privacy-safe authentication/security audit events\n(.*?)(?=\n## 14\.)", doc, re.S)
assert audit, "audit-event section missing"
require_groups(audit.group(1), [
    ("auth_session_created",), ("auth_session_rejected",),
    ("auth_session_revoked",), ("authz_denied",),
    ("account_deletion_terminal",), ("provider_dependency_state",),
    ("raw firebase/google id token",), ("email/name/photo",),
    ("dns query/qname/domain/url",),
    ("retention fail-closed rule",),
    ("undefined retention means durable collection is blocked",),
], "security events")
print("TSK0353_SECURITY_AUDIT_EVENTS=PASS")

require_groups(doc, [
    ("never produce or strengthen technical `protected_verified`",),
    ("valid google/firebase identity",), ("device ownership",),
    ("stored clientid/profile/configuration",),
], "protection separation")
print("TSK0353_PROTECTION_SEPARATION=PASS")

assertions = re.search(r"## 15\. Deterministic acceptance test catalogue\n(.*?)(?=\n## 16\.)", doc, re.S)
assert assertions, "acceptance catalogue missing"
assert len(re.findall(r"^\d+\. ", assertions.group(1), re.M)) == 30
print("TSK0353_ASSERTION_CATALOGUE=PASS")

require_groups(doc, [
    ("does not activate firebase/google", "no implementation/provider activation"),
    ("does not", "legal-compliance conclusion"),
    ("participant processing",), ("successor pass",),
], "non-inference")
print("TSK0353_NON_INFERENCE=PASS")

# Interface compatibility: TSK-0353 must not steal concrete AdGuard ClientID contract ownership.
require_groups(doc, [
    ("tsk-0352",), ("clientid remains",),
    ("never an authorization token",),
], "TSK-0044/0352 boundary")
print("TSK0353_ADGUARD_INTERFACE_BOUNDARY=PASS")

print("TSK0353_CURRENT_ACC=PASS")
print("TSK0353_CURRENT_VER=PASS")
print("TSK0353_CURRENT_EVD_READY=PASS")
print("TSK0353_CURRENT_NFR=PASS")
