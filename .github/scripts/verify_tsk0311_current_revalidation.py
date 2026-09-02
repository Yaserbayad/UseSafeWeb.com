from __future__ import annotations

import csv
import re
import subprocess
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "974c7e5ebdbf64e382d2d4075490567f11be6fff",
    "TSK_0318_POST_CR0008_DUAL_MODE_PUBLIC_PRODUCT_SETUP_IA_2026-09-01.md": "975e2e7a8e85e9408e0bbbc2be226f3fdd012db3",
    "TSK_0311_LOCALIZATION_CONTENT_ARCHITECTURE_2026-08-29.md": "ef746d64c7878eb7d0f1b8fdf2356721728041c4",
    "TSK_0311_LOCALIZATION_CONTENT_ARCHITECTURE_EVIDENCE_2026-08-29.md": "b9e7770faa0fa94a35d98d8141dec367583233f7",
    "TSK_0307_POST_CR0008_CURRENT_SOURCE_BACKED_INSTRUCTION_CATALOGUE_REVALIDATION_2026-09-02.md": "73a7028e247833bfe7e98487d9e079a51d36d424",
    "TSK_0307_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md": "afba74ba076bcc6832199955682462631abea0f0",
    "TSK_0311_POST_CR0008_DUAL_MODE_LOCALIZATION_CONTENT_ARCHITECTURE_REVALIDATION_2026-09-02.md": "4f702a61bfccad385be83c1a37a753cdeb1d8b43",
}


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def tracked(path: str) -> str:
    return subprocess.check_output(["git", "show", f"HEAD:{path}"], text=True)


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def require(text: str, concepts: list[str], label: str) -> None:
    n = normalized(text)
    missing = [c for c in concepts if normalized(c) not in n]
    if missing:
        raise AssertionError(f"{label} missing {missing}")


for path, expected in EXPECTED.items():
    assert Path(path).exists(), path
    actual = blob(path)
    assert actual == expected, f"hash drift {path}: {actual} != {expected}"
print("TSK0311_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0311")
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "HIGH"
assert row["AI_Capability_A0_A4"] == "A3"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert [d.strip() for d in (row["Dependencies"] or "").split(";") if d.strip()] == ["TSK-0318"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0311", "VER-0311", "EVD-0311")
require(row["Acceptance_Criteria"], ["English baseline", "externalized content", "no hard-coded UI copy", "Turkish/Arabic", "locale fallback", "content versioning", "testable"], "ACC-0311")
print("TSK0311_CURRENT_WBS=PASS")

runtime = tracked("CURRENT_STATE.md")
sections = list(re.finditer(r"^(##|###) TSK-0318\b.*?(?=^(?:##|###) |\Z)", runtime, re.M | re.S))
assert any("**PASS" in m.group(0) for m in sections), "TSK-0318 durable PASS missing"
print("TSK0311_CURRENT_PREDECESSOR=PASS")

ia = tracked("TSK_0318_POST_CR0008_DUAL_MODE_PUBLIC_PRODUCT_SETUP_IA_2026-09-01.md")
historical = tracked("TSK_0311_LOCALIZATION_CONTENT_ARCHITECTURE_2026-08-29.md")
historical_evd = tracked("TSK_0311_LOCALIZATION_CONTENT_ARCHITECTURE_EVIDENCE_2026-08-29.md")
current = tracked("TSK_0311_POST_CR0008_DUAL_MODE_LOCALIZATION_CONTENT_ARCHITECTURE_REVALIDATION_2026-09-02.md")
current_instructions = tracked("TSK_0307_POST_CR0008_CURRENT_SOURCE_BACKED_INSTRUCTION_CATALOGUE_REVALIDATION_2026-09-02.md")

# Historical architecture remains valid provenance for the unchanged localization mechanics.
for heading in [
    "## 2. Locale baseline", "## 3. Externalized file model", "## 4. Key taxonomy",
    "## 5. Source-backed instruction binding", "## 6. Locale manifest", "## 7. Fallback contract",
    "## 8. Plural, number and date/time rules", "## 9. RTL and accessibility rules",
    "## 10. Content ownership", "## 11. Content versioning", "## 12. Testable acceptance assertions",
]:
    assert heading in historical, heading
require(historical_evd, ["English baseline externalized", "Turkish/Arabic not blocked", "fallback deterministic and testable", "content versioning testable", "plural/date/number rules", "instruction variants bound", "accessibility/localization", "privacy boundary"], "historical evidence")
print("TSK0311_HISTORICAL_PROVENANCE=PASS")

# The current predecessor really introduces the optional account/session/dashboard/device lifecycle surfaces.
require(ia, [
    "Sign in / Manage devices", "optional parent-account and lightweight dashboard",
    "/account/sign-in", "/account/auth-result", "dashboard", "Add device", "reverify",
    "reinstall", "replace", "revoke/unlink", "delete record", "account deletion",
    "session", "continue without account", "destructive operations are distinct",
], "current TSK-0318 dual-mode surfaces")
print("TSK0311_DUAL_MODE_IA_INPUT=PASS")

# The historical scope was explicitly accountless and therefore incomplete for the current IA.
require(historical, ["provisional accountless first-phone product", "accountless setup"], "historical accountless scope")
require(current, ["stale only where", "optional parent-account/session/dashboard/device-lifecycle surfaces", "preserves the historical architecture", "extends the key/file/ownership/test model"], "current scope reconciliation")
print("TSK0311_SCOPE_RECONCILIATION=PASS")

# Current locale manifest contract: three locales, direction/status/fallback/marketActivation/version/owner fields.
locale_table = current.split("## 3. Preserved locale baseline and manifest contract", 1)[1].split("## 4. Current externalized file model", 1)[0]
for locale in ["`en-GB`", "`tr-TR`", "`ar`"]:
    assert locale in locale_table
require(locale_table, ["LTR", "RTL", "baseline", "provisional", "marketActivation=false", "contentVersion", "lastVerified", "owner"], "locale manifest")
print("TSK0311_LOCALE_MANIFEST=PASS")

# File-model namespace coverage includes the old core plus all current account/session/dashboard/device lifecycle namespaces.
file_model = current.split("## 4. Current externalized file model",1)[1].split("## 5. Preserved semantic key model",1)[0]
for namespace in [
    "common.json", "navigation.json", "setup.json", "verification.json", "protection-map.json",
    "troubleshooting.json", "removal-recovery.json", "accessibility.json", "account.json",
    "session.json", "dashboard.json", "device-management.json", "account-lifecycle.json",
]:
    assert namespace in file_model, namespace
require(file_model, ["no user-facing production sentence", "auth/session message", "dashboard/device-management label", "destructive lifecycle consequence"], "externalized current file model")
print("TSK0311_EXTERNALIZED_NAMESPACES=13/13_PASS")

# Parse representative current key tables and ensure the current IA categories are actually represented.
key_section = current.split("## 6. Current dual-mode key inventory",1)[1].split("## 7. Current truth and separation rules",1)[0]
required_keys = [
    "navigation.sign_in_manage_devices", "account.entry.continue_without_account",
    "setup.complete.finish_without_account", "account.sign_in.provider_action",
    "account.auth_result.continue_without_account", "session.expired.reauthenticate",
    "session.provider_unavailable.continue_without_account", "dashboard.add_device",
    "device.status.ownership", "device.status.configuration", "device.status.verification",
    "device.action.reverify", "device.action.reinstall", "device.action.replace",
    "device.action.revoke", "device.action.delete_record", "device.action.remove_dns",
    "account.delete.dns_not_removed", "anonymous.reset.account_not_deleted",
    "removal.account_not_deleted", "removal.device_record_not_deleted",
]
for key in required_keys:
    assert f"`{key}`" in key_section, key
print(f"TSK0311_DUAL_MODE_KEY_COVERAGE={len(required_keys)}/{len(required_keys)}_PASS")

# Core semantic safety/truth requirements are explicitly localized, not inferred from generic fallback.
truth = current.split("## 7. Current truth and separation rules",1)[1].split("## 8. Source-backed instruction binding remains single-authority",1)[0]
require(truth, [
    "Optional account is optional", "Accountless fallback remains explicit",
    "Session/account/device ownership is not protection evidence", "Destructive operations are not synonyms",
    "No automatic J0/J1 linkage", "No surveillance expansion", "SafeWeb visible identity is stable",
], "dual-mode truth")
print("TSK0311_DUAL_MODE_TRUTH=PASS")

# Current source-backed instruction authority remains single-owner and current.
require(current_instructions, ["nine instruction classes", "SafeWeb", "dns.usesafeweb.com", "2026-09-02"], "current TSK-0307")
instruction_binding = current.split("## 8. Source-backed instruction binding remains single-authority",1)[1].split("## 9. Deterministic fallback contract",1)[0]
require(instruction_binding, ["nine TSK-0307 instruction IDs", "cannot silently retain an older instruction string", "not added to the TSK-0307 instruction catalogue unless it is genuinely platform/source-owned"], "instruction binding")
print("TSK0311_CURRENT_INSTRUCTION_BINDING=PASS")

# Fallback, locale formatting, RTL/accessibility, ownership and versioning remain testable and include new critical account copy.
fallback = current.split("## 9. Deterministic fallback contract",1)[1].split("## 10. Plural/number/date/time rules",1)[0]
require(fallback, ["exact requested locale", "en-GB", "missing-key failure", "destructive-operation consequence", "machine translation"], "fallback")
formatting = current.split("## 10. Plural/number/date/time rules",1)[1].split("## 11. RTL and accessibility",1)[0]
require(formatting, ["CLDR/Unicode", "device counts", "session expiry", "ISO-8601 UTC", "never localized", "bidi isolation"], "formatting")
accessibility = current.split("## 11. RTL and accessibility",1)[1].split("## 12. Current content ownership",1)[0]
require(accessibility, ["RTL", "logical DOM/focus order", "auth/session errors", "device-list rows", "destructive controls", "text expansion/reflow", "text, not color/icon alone"], "RTL/accessibility")
ownership = current.split("## 12. Current content ownership",1)[1].split("## 13. Schema/content versioning",1)[0]
for content_class in ["Optional account entry/auth/session", "Dashboard/device management", "Account/device destructive lifecycle"]:
    assert content_class in ownership, content_class
versioning = current.split("## 13. Schema/content versioning",1)[1].split("## 14. Current testable acceptance assertions",1)[0]
require(versioning, ["localization schema version", "per-locale content bundle semantic version", "minor-compatible schema/content expansion", "without removing the still-valid accountless keys"], "versioning")
print("TSK0311_FALLBACK_FORMATTING_A11Y_OWNERSHIP_VERSIONING=PASS")

# Current test assertions must cover the complete dual-mode addition, not only historical core assertions.
tests = current.split("## 14. Current testable acceptance assertions",1)[1].split("## 15. Acceptance reconciliation",1)[0]
numbered = re.findall(r"^\d+\. ", tests, re.M)
assert len(numbered) == 18, len(numbered)
require(tests, [
    "Every user-facing key referenced by current TSK-0318", "no current UI component hard-codes",
    "auth/provider failure", "ownership labels cannot reuse or alias the protection `Verified` key",
    "distinct keys and consequence/result copy", "account deletion copy explicitly does not claim DNS removal",
    "SafeWeb visible brand and exact technical endpoints",
], "current test assertions")
print("TSK0311_TEST_ASSERTIONS=18/18_PASS")

# ACC and non-inference are explicit.
acceptance = current.split("## 15. Acceptance reconciliation",1)[1].split("## 16. Non-inference",1)[0]
require(acceptance, ["English semantic baseline remains externalized", "full current dual-mode IA", "Turkish/Arabic remain structurally unblocked", "fallback remains deterministic", "Content/schema versioning remains independently testable"], "acceptance reconciliation")
non_inference = current.split("## 16. Non-inference",1)[1]
require(non_inference, ["does not implement production locale files", "native-speaker or representative-parent validation", "activate a market", "authentication/session/dashboard/device ownership", "legal/privacy review", "publish", "LG-06", "launch"], "non-inference")
print("TSK0311_NON_INFERENCE=PASS")
print("TSK0311_CURRENT_ACC=PASS")
print("TSK0311_CURRENT_VER=PASS")
print("TSK0311_CURRENT_EVD_READY=PASS")
print("TSK0311_CURRENT_REVALIDATION=PASS")
