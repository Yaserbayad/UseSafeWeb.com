from __future__ import annotations

import csv
import re
import subprocess
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "235cca98f7a3e1432b88e4581de5d0a80602195a",
    "TSK_0300_POST_CR0008_PROTECTION_COPY_CORRECTION_REVALIDATION_2026-09-02.md": "172e4b82c7c106c48291c6a6a75aca6848ca4d0c",
    "TSK_0299_POST_CR0008_DUAL_MODE_VERBAL_SYSTEM_2026-09-01.md": "ff30500b933b9ecc92325659d49ea4e671d296d2",
    "TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md": "bdc6bacc424669708f410466f3cfd5527f1c2b3c",
    "brand/system/TSK-0300/README.md": "a54a2b653720160261b034149cadff62bc399102",
    "brand/system/TSK-0300/tokens.css": "cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f",
    "brand/system/TSK-0300/components.css": "831e92a74b6dda04252d93242cb33bd491a02381",
    "brand/system/TSK-0300/templates/public.html": "309f6a1f38474f78cd8a241aad3028fd495f9b8e",
    "brand/system/TSK-0300/templates/product.html": "872920b6f7af6561a1015e1d8fea55dcf95f1249",
    "brand/system/TSK-0300/templates/help.html": "3193c0d1e11367204d6c46fd862fec5a91245b64",
    "brand/system/TSK-0300/templates/status.html": "8f9971edfc87b2da8174330b9b4be68338a96fb4",
    "brand/system/TSK-0300/templates/partner.html": "03bb1fd67b9a9824bc856d1f312977d7767619a8",
    "brand/system/TSK-0300/templates/social.html": "cabdd12851fce1dbd5a3c6326ec6dec63f843958",
    "brand/identity/TSK-0301/README.md": "b8ffd2ed234465a238558a7b94e56274de49696a",
    "brand/identity/TSK-0301/safeweb-wordmark-primary.svg": "f93958e3e4a16f9056693072c1b9b8b31fcda852",
    "brand/identity/TSK-0301/safeweb-wordmark-inverse.svg": "c38709e4239a2d36b340b4d9d630df85a17bb494",
    "brand/identity/TSK-0301/safeweb-wordmark-monochrome.svg": "ef9b6e0d52926f24c7e81bccb4489569067b852f",
    "brand/identity/TSK-0301/safeweb-monogram.svg": "49f20bae1d92bb04f125e988cb4cc3ea8a822b9e",
}

TEMPLATES = [
    "public.html", "product.html", "help.html", "status.html", "partner.html", "social.html"
]
CURRENT_LABELS = [
    "Protection verified",
    "Setup confirmed",
    "Action needed",
    "Not covered",
    "Protection status could not be verified",
    "Removed",
]
STALE_PRIMARY_LABELS = [
    ">Verified<",
    ">You confirmed this is set up<",
    ">Status uncertain<",
]


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def require_any(text: str, groups: list[tuple[str, ...]], label: str) -> None:
    low = text.lower()
    missing = [group for group in groups if not any(term.lower() in low for term in group)]
    if missing:
        raise AssertionError(f"{label} missing semantic groups: {missing}")


def task_sections(runtime: str, task_id: str) -> list[str]:
    return re.findall(
        rf"^(?:##|###) {re.escape(task_id)}\b.*?(?=^(?:##|###) |\Z)",
        runtime,
        re.M | re.S,
    )


for path, expected in EXPECTED.items():
    p = Path(path)
    assert p.exists(), f"missing {path}"
    actual = blob(path)
    assert actual == expected, f"hash drift {path}: {actual} != {expected}"
print("TSK0300_COPY_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0300")
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "HIGH"
assert row["AI_Capability_A0_A4"] == "A3"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert [x.strip() for x in (row.get("Dependencies") or "").split(";") if x.strip()] == ["TSK-0301"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0300", "VER-0300", "EVD-0300")
require_any(
    row.get("Acceptance_Criteria") or "",
    [
        ("public/product/help/status/partner/social",),
        ("one token source", "single token source"),
        ("implementation values",),
        ("accessibility states",),
    ],
    "ACC-0300",
)
print("TSK0300_COPY_WBS_CONTRACT=PASS")

runtime = Path("CURRENT_STATE.md").read_text(encoding="utf-8")
for tid in ["TSK-0301", "TSK-0299", "TSK-0320"]:
    sections = task_sections(runtime, tid)
    assert sections and any("**PASS**" in section for section in sections), f"no durable PASS {tid}"
print("TSK0300_COPY_PREDECESSOR_SUPPORT=PASS")

verbal = Path("TSK_0299_POST_CR0008_DUAL_MODE_VERBAL_SYSTEM_2026-09-01.md").read_text(encoding="utf-8")
state_model = Path("TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md").read_text(encoding="utf-8")
for label in CURRENT_LABELS:
    assert label in state_model, f"TSK-0320 missing {label}"
require_any(
    verbal,
    [
        ("accountless core",),
        ("optional parent account",),
        ("protection verified",),
        ("setup confirmed",),
        ("protection status could not be verified",),
        ("no browsing/query/activity history",),
    ],
    "current TSK-0299",
)
print("TSK0300_COPY_CURRENT_SEMANTIC_OWNERS=PASS")

readme = Path("brand/system/TSK-0300/README.md").read_text(encoding="utf-8")
status = Path("brand/system/TSK-0300/templates/status.html").read_text(encoding="utf-8")
section_match = re.search(r"## 4\. Canonical state copy used by reference contexts\n(.*?)(?=\n## 5\.)", readme, re.S)
assert section_match, "canonical state-copy section missing"
state_section = section_match.group(1)
for label in CURRENT_LABELS:
    assert label in state_section, f"README missing current label {label}"
assert "Protection has not yet been technically verified." in state_section
for stale in ["`Verified`", "`You confirmed this is set up`", "`Status uncertain`"]:
    assert stale not in state_section, f"README stale canonical label {stale}"
for label in CURRENT_LABELS:
    assert f">{label}<" in status, f"status template missing exact label {label}"
assert "Protection has not yet been technically verified." in status
for stale in STALE_PRIMARY_LABELS:
    assert stale not in status, f"status template stale primary label {stale}"
assert "data-state=\"protected/verified\"" in status
assert "data-state=\"configured/parent-confirmed\"" in status
assert "data-state=\"uncertain/error\"" in status
assert "Brand color is not a state signal" in status
assert "Non-color-only reference" in status
print("TSK0300_COPY_STATE_REFERENCE=PASS")

base = Path("brand/system/TSK-0300/templates")
actual_templates = sorted(p.name for p in base.glob("*.html"))
assert actual_templates == sorted(TEMPLATES), actual_templates
for name in TEMPLATES:
    text = (base / name).read_text(encoding="utf-8")
    assert 'href="../tokens.css"' in text, f"{name} missing tokens.css"
    assert 'href="../components.css"' in text, f"{name} missing components.css"
    assert "identity/TSK-0301/" in text, f"{name} missing TSK-0301 identity reference"
    assert "<script" not in text.lower(), f"script introduced in {name}"
    assert "http://" not in text.lower() and "https://" not in text.lower(), f"remote URL introduced in {name}"
print("TSK0300_COPY_SIX_CONTEXTS=PASS")

public = (base / "public.html").read_text(encoding="utf-8")
product = (base / "product.html").read_text(encoding="utf-8")
require_any(
    public,
    [
        ("Start setup",),
        ("Sign in / Manage devices",),
        ("Continue without account",),
        ("does not automatically import anonymous setup state",),
        ("does not prove that a device is currently protected",),
    ],
    "public dual-mode reference",
)
require_any(
    product,
    [
        ("Finish without account",),
        ("Sign in to manage devices",),
        ("does not automatically import anonymous journey state",),
        ("does not by itself mean SafeWeb has verified",),
    ],
    "product dual-mode reference",
)
print("TSK0300_COPY_DUAL_MODE_REFERENCE=PASS")

tracked = subprocess.check_output(["git", "ls-files"], text=True).splitlines()
font_ext = (".ttf", ".otf", ".woff", ".woff2", ".eot")
font_files = [p for p in tracked if p.lower().endswith(font_ext)]
assert not font_files, f"font binaries tracked: {font_files}"
print("TSK0300_COPY_NO_FONT_BINARIES=PASS")

candidate = Path("TSK_0300_POST_CR0008_PROTECTION_COPY_CORRECTION_REVALIDATION_2026-09-02.md").read_text(encoding="utf-8")
require_any(
    candidate,
    [
        ("two-file semantic patch",),
        ("does **not** alter or reopen", "does not alter or reopen"),
        ("complete login-free accountless core",),
        ("optional non-coercive",),
        ("no automatic j0/j1",),
        ("account/session/dashboard/device ownership never proves protection",),
        ("no implementation",),
    ],
    "candidate preservation/non-inference",
)
print("TSK0300_COPY_PRESERVATION_FENCE=PASS")

print("TSK0300_COPY_ACC=PASS")
print("TSK0300_COPY_VER=PASS")
print("TSK0300_COPY_EVD_READY=PASS")
print("TSK0300_PROTECTION_COPY_CORRECTION=PASS")
