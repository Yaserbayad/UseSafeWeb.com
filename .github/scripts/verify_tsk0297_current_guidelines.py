from __future__ import annotations

import csv
import json
import re
import subprocess
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "f12f87cec9993f811d25d5f2f34b9996c4497c67",
    "brand/guidelines/TSK-0297/README.md": "e79121fd95932a6f4b2550f5f05b84c6e9c7aeac",
    "brand/guidelines/TSK-0297/ASSET_MANIFEST.json": "c31eb9674eee9cf330b1af4764088f51e9c398fe",
    "TSK_0297_POST_CR0008_CURRENT_BRAND_GUIDELINES_REVALIDATION_2026-09-02.md": "7e472d3373fa226584dcea358ed3215f40aa2e7b",
    "TSK_0297_BRAND_GUIDELINES_EVIDENCE_2026-08-29.md": "02b28f3f040d44e495ace63bf074535e4a4bd03d",
    "TSK_0298_EVIDENCE_GROUNDED_BRAND_STRATEGY_2026-08-29.md": "73d8587ef9bb37d92b44f102d5a33545b416c44b",
    "brand/identity/TSK-0301/README.md": "b8ffd2ed234465a238558a7b94e56274de49696a",
    "brand/system/TSK-0300/README.md": "a54a2b653720160261b034149cadff62bc399102",
    "TSK_0300_POST_CR0008_PROTECTION_COPY_CORRECTION_EVIDENCE_2026-09-02.md": "a3e39896b67098ced321cb9e4b82c65c440806e4",
    "TSK_0299_POST_CR0008_DUAL_MODE_VERBAL_SYSTEM_2026-09-01.md": "ff30500b933b9ecc92325659d49ea4e671d296d2",
    "TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md": "bdc6bacc424669708f410466f3cfd5527f1c2b3c",
}

CURRENT_LABELS = [
    "Protection verified",
    "Setup confirmed",
    "Action needed",
    "Not covered",
    "Protection status could not be verified",
    "Removed",
]
FORBIDDEN_FONT_EXT = (".ttf", ".otf", ".woff", ".woff2", ".eot")


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def require_groups(text: str, groups: list[tuple[str, ...]], label: str) -> None:
    n = norm(text)
    missing = [group for group in groups if not any(norm(term) in n for term in group)]
    if missing:
        raise AssertionError(f"{label} missing semantic groups: {missing}")


def task_sections(runtime: str, task_id: str) -> list[str]:
    pat = re.compile(rf"^(?:##|###) {re.escape(task_id)}\b.*?(?=^(?:##|###) |\Z)", re.M | re.S)
    return [m.group(0) for m in pat.finditer(runtime)]


for path, expected in EXPECTED.items():
    p = Path(path)
    assert p.exists(), f"missing {path}"
    actual = blob(path)
    assert actual == expected, f"hash drift {path}: {actual} != {expected}"
print("TSK0297_CURRENT_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0297")
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "MEDIUM"
assert row["AI_Capability_A0_A4"] == "A3"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert [x.strip() for x in (row.get("Dependencies") or "").split(";") if x.strip()] == ["TSK-0300"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0297", "VER-0297", "EVD-0297")
require_groups(
    row.get("Acceptance_Criteria") or "",
    [
        ("human or ai",),
        ("without guessing",),
        ("deprecated assets", "deprecated"),
        ("traceable",),
        ("no font files", "font files"),
    ],
    "ACC-0297",
)
print("TSK0297_CURRENT_WBS=PASS")

runtime = Path("CURRENT_STATE.md").read_text(encoding="utf-8")
s300 = task_sections(runtime, "TSK-0300")
assert s300 and any("**PASS" in section for section in s300)
joined300 = "\n".join(s300)
for value in [
    "a3e39896b67098ced321cb9e4b82c65c440806e4",
    "33592292946 / 100128578252",
    "ACC-0300 = PASS. VER-0300 = PASS. EVD-0300 = SATISFIED.",
]:
    assert value in joined300, value
print("TSK0297_CURRENT_TSK0300_PREDECESSOR=PASS")

readme = Path("brand/guidelines/TSK-0297/README.md").read_text(encoding="utf-8")
manifest = json.loads(Path("brand/guidelines/TSK-0297/ASSET_MANIFEST.json").read_text(encoding="utf-8"))
assert manifest["schema"] == "usesafeweb.brand-assets.v1"
assert manifest["guideline_version"] == "2.0.0"
assert manifest["status"] == "provisional_internal_l4"
assert "**Version:** 2.0.0" in readme
assert "Version `2.0.0` is MAJOR" in readme
assert manifest["supersedes"]["guideline_version"] == "1.0.0"
assert manifest["supersedes"]["readme_blob"] == "89e915678e85f7f301e8fa4b05c335cd803dd9d4"
assert manifest["supersedes"]["manifest_blob"] == "11e26ee46ebb60762c085513e50f8e40ec1f4854"
print("TSK0297_CURRENT_PACKAGE_VERSION=PASS")

# Recompute every currently selectable authority/asset/source/template blob from current main.
selectable_groups = ["authority_sources", "identity_assets", "implementation_sources", "surface_templates"]
selectable = []
for group in selectable_groups:
    for record in manifest[group]:
        if record.get("status") == "DEPRECATED":
            continue
        path = record.get("path")
        expected = record.get("blob")
        assert path and expected, f"selectable {group} record lacks path/blob: {record}"
        assert not re.match(r"https?://", path), f"remote selectable source: {path}"
        assert Path(path).exists(), f"manifest path missing: {path}"
        actual = blob(path)
        assert actual == expected, f"manifest blob drift {path}: {actual} != {expected}"
        selectable.append((group, path, expected))
assert len(selectable) == 18, len(selectable)
print("TSK0297_CURRENT_MANIFEST_ACTIVE_BLOBS=PASS")

# Current authority bindings must be active; old ones may appear only in explicit supersession provenance.
auth_by_role = {r["role"]: r for r in manifest["authority_sources"]}
assert auth_by_role["shared_brand_system"]["blob"] == "a54a2b653720160261b034149cadff62bc399102"
assert auth_by_role["shared_brand_system_current_evidence"]["blob"] == "a3e39896b67098ced321cb9e4b82c65c440806e4"
assert auth_by_role["verbal_claims"]["path"] == "TSK_0299_POST_CR0008_DUAL_MODE_VERBAL_SYSTEM_2026-09-01.md"
assert auth_by_role["verbal_claims"]["blob"] == "ff30500b933b9ecc92325659d49ea4e671d296d2"
assert auth_by_role["protection_state_semantics"]["path"] == "TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md"
assert auth_by_role["protection_state_semantics"]["blob"] == "bdc6bacc424669708f410466f3cfd5527f1c2b3c"
assert "cannot override current" in auth_by_role["brand_strategy_compatible_scope"]["binding_scope"].lower()
active_paths = {r["path"] for r in manifest["authority_sources"]}
assert "TSK_0299_PROVISIONAL_VERBAL_SYSTEM_2026-08-29.md" not in active_paths
assert "TSK_0320_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-08-28.md" not in active_paths
sup = manifest["superseded_authority_bindings"]
assert any(r.get("blob") == "4baa67f565c14c3034fca47bb5fad0b9ff71b091" and r.get("replacement_blob") == "a54a2b653720160261b034149cadff62bc399102" for r in sup)
assert any(r.get("blob") == "a4ff2314ff02c407249e8b5d4d6b9600b89403b3" and r.get("replacement_blob") == "ff30500b933b9ecc92325659d49ea4e671d296d2" for r in sup)
assert any(r.get("blob") == "1146f7622f434590dde1253d11f14fb6a87e19de" and r.get("replacement_blob") == "bdc6bacc424669708f410466f3cfd5527f1c2b3c" for r in sup)
print("TSK0297_CURRENT_AUTHORITY_SUPERSESSION=PASS")

surface = {r["id"]: r for r in manifest["surface_templates"]}
assert surface["surface.public"]["blob"] == "309f6a1f38474f78cd8a241aad3028fd495f9b8e"
assert surface["surface.product"]["blob"] == "872920b6f7af6561a1015e1d8fea55dcf95f1249"
assert surface["surface.status"]["blob"] == "8f9971edfc87b2da8174330b9b4be68338a96fb4"
assert surface["surface.help"]["blob"] == "3193c0d1e11367204d6c46fd862fec5a91245b64"
assert surface["surface.partner"]["blob"] == "03bb1fd67b9a9824bc856d1f312977d7767619a8"
assert surface["surface.social"]["blob"] == "cabdd12851fce1dbd5a3c6326ec6dec63f843958"
print("TSK0297_CURRENT_SURFACE_BINDINGS=PASS")

# State/copy must match current semantic owners and the package itself.
state_model = Path("TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md").read_text(encoding="utf-8")
verbal = Path("TSK_0299_POST_CR0008_DUAL_MODE_VERBAL_SYSTEM_2026-09-01.md").read_text(encoding="utf-8")
for label in CURRENT_LABELS:
    assert label in state_model, label
    assert label in readme, f"README missing {label}"
    assert label in manifest["current_semantic_rules"]["protection_state_primary_copy"], f"manifest missing {label}"
assert "Protection has not yet been technically verified." in state_model
assert "Protection has not yet been technically verified." in readme
assert manifest["current_semantic_rules"]["setup_confirmed_supporting_copy"] == "Protection has not yet been technically verified."
for stale in ["`Verified`", "`You confirmed this is set up`", "`Status uncertain`"]:
    assert stale not in readme, f"stale active README label {stale}"
require_groups(
    verbal,
    [
        ("accountless core stays first-class",),
        ("optional account is continuity, not stronger protection",),
        ("lifecycle operations say exactly what they change",),
        ("no browsing/query/activity history",),
    ],
    "current TSK-0299",
)
print("TSK0297_CURRENT_PROTECTION_COPY=PASS")

rules = manifest["current_semantic_rules"]
assert rules["accountless_core_required"] is True
assert rules["optional_account_continuity"] is True
assert rules["account_or_device_ownership_is_protection_evidence"] is False
assert rules["automatic_anonymous_to_account_linkage"] is False
assert rules["browsing_query_activity_history_allowed"] is False
assert rules["child_accounts_allowed"] is False
assert rules["unrestricted_customer_dns_admin_allowed"] is False
require_groups(
    readme,
    [
        ("complete core setup", "complete core"),
        ("remains usable without login",),
        ("optional parent sign-in/session continuity",),
        ("never technical protection evidence",),
        ("not automatically imported", "not automatically"),
        ("lifecycle operations must name exactly what they change",),
    ],
    "dual-mode guideline",
)
print("TSK0297_CURRENT_DUAL_MODE_BOUNDARY=PASS")

# Identity/system sources remain unchanged and deterministic.
identity = {r["id"]: r for r in manifest["identity_assets"]}
assert identity["safeweb.wordmark.primary"]["blob"] == "f93958e3e4a16f9056693072c1b9b8b31fcda852"
assert identity["safeweb.wordmark.inverse"]["blob"] == "c38709e4239a2d36b340b4d9d630df85a17bb494"
assert identity["safeweb.wordmark.monochrome"]["blob"] == "ef9b6e0d52926f24c7e81bccb4489569067b852f"
assert identity["safeweb.monogram.sw"]["blob"] == "49f20bae1d92bb04f125e988cb4cc3ea8a822b9e"
impl = {r["id"]: r for r in manifest["implementation_sources"]}
assert impl["brand.tokens"]["blob"] == "cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f"
assert impl["brand.components"]["blob"] == "831e92a74b6dda04252d93242cb33bd491a02381"
require_groups(
    readme,
    [
        ("public header, light background",),
        ("safeweb-wordmark-primary.svg",),
        ("small dark status/icon context",),
        ("safeweb-wordmark-monochrome.svg", "monochrome off-white"),
        ("arabic rtl",),
        ("optional account/dashboard surface",),
        ("lifecycle asset/copy",),
    ],
    "representative deterministic decisions",
)
print("TSK0297_CURRENT_DETERMINISTIC_SELECTION=PASS")

# Deprecation contract must be complete; any actual deprecated record must be reconstructable.
dep_policy = manifest["deprecation_policy"]
assert dep_policy["statuses"] == ["ACTIVE", "DEPRECATED"]
assert dep_policy["retain_deprecated_records"] is True
assert dep_policy["allow_new_use_of_deprecated"] is False
assert dep_policy["silent_delete"] is False
required = set(dep_policy["required_when_deprecated"])
assert required == {"replacement", "reason", "deprecated_at", "authorizing_commit_or_evidence"}
for group in ["identity_assets", "implementation_sources", "surface_templates"]:
    for record in manifest[group]:
        if record.get("status") == "DEPRECATED":
            missing = [key for key in required if key not in record]
            assert not missing, f"deprecated {record.get('id')} missing {missing}"
print("TSK0297_CURRENT_DEPRECATION_TRACE=PASS")

# No font binary is packaged/exposed by TSK-0297 and no selectable manifest source is a font binary.
package_files = subprocess.check_output(["git", "ls-files", "brand/guidelines/TSK-0297"], text=True).splitlines()
assert package_files == [
    "brand/guidelines/TSK-0297/ASSET_MANIFEST.json",
    "brand/guidelines/TSK-0297/README.md",
], package_files
assert not any(path.lower().endswith(FORBIDDEN_FONT_EXT) for path in package_files)
assert manifest["font_policy"]["deliver_font_binaries"] is False
assert tuple(manifest["font_policy"]["forbidden_extensions"]) == FORBIDDEN_FONT_EXT
assert not any(path.lower().endswith(FORBIDDEN_FONT_EXT) for _, path, _ in selectable)
assert not any(re.match(r"https?://", path) for _, path, _ in selectable)
print("TSK0297_CURRENT_NO_FONT_DELIVERY=PASS")
print("TSK0297_CURRENT_LOCAL_SOURCE_LIBRARY=PASS")

artifact = Path("TSK_0297_POST_CR0008_CURRENT_BRAND_GUIDELINES_REVALIDATION_2026-09-02.md").read_text(encoding="utf-8")
require_groups(
    artifact,
    [
        ("source-currency/no-guessing boundary",),
        ("version 2.0.0",),
        ("superseded provenance",),
        ("current tsk-0299",),
        ("current tsk-0320",),
        ("no approved identity master",),
        ("no build/legal/privacy/user-validation",),
    ],
    "revalidation artifact",
)
print("TSK0297_CURRENT_PRESERVATION_NONINFERENCE=PASS")

print("TSK0297_CURRENT_ACC=PASS")
print("TSK0297_CURRENT_VER=PASS")
print("TSK0297_CURRENT_EVD_READY=PASS")
print("TSK0297_CURRENT_GUIDELINES=PASS")
