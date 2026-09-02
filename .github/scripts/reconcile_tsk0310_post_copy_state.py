from __future__ import annotations

import csv
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

EXPECTED = {
    "Plans/Master/WBS/master-wbs.csv": "b27a0c5df2f5636d8ed71051e9e26a68959a2616",
    "Plans/Master/RELATIONSHIP_INDEX.yaml": "c108d2c162bcea2ee4cc01def46d0487a9501032",
    "CURRENT_STATE.md": "1e68911d10eb648ac57a9e0f80b552f89dd9f823",
    "TSK_0310_POST_TSK0300_COPY_CORRECTION_CURRENT_REVALIDATION_2026-09-02.md": "24c8e3cdf059fc62a3df1fe8119b959246c216f6",
    "TSK_0310_POST_TSK0300_COPY_CORRECTION_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md": "34d119334e07a5d6ffe63fb893bb741d3aa0c775",
    "TSK_0300_POST_CR0008_PROTECTION_COPY_CORRECTION_EVIDENCE_2026-09-02.md": "a3e39896b67098ced321cb9e4b82c65c440806e4",
    "TSK_0317_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md": "cd001f3ce391634e38ef0c89934cb34f4f347401",
    "TSK_0318_POST_CR0008_DUAL_MODE_PUBLIC_PRODUCT_SETUP_IA_2026-09-01.md": "975e2e7a8e85e9408e0bbbc2be226f3fdd012db3",
    "TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md": "bdc6bacc424669708f410466f3cfd5527f1c2b3c",
    "prototype/TSK-0310/model.mjs": "cb35f7dbc46ba5d19da18fb09429b59e097e0492",
    "prototype/TSK-0310/app.mjs": "a235993d5abcaac550b6c01978792092012afb00",
    "prototype/TSK-0310/browser-acceptance.mjs": "5f68400a8bfb063853304e937f744e1ee71032e7",
    ".github/workflows/verify-tsk0310-post-copy-refresh.yml": "41e96e2df5c94cf8c7a2a75e6c69ab13f59400c7",
}

HEADING = "## TSK-0310 current accepted stable state — 2026-09-02 — POST-TSK-0300 PROTECTION-COPY CORRECTION REVALIDATION"


def blob(path: str) -> str:
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def mask_updated(text: str) -> str:
    return re.sub(r"^\*\*Updated:\*\*.*$", "**Updated:** <MASK>", text, count=1, flags=re.M)


def sections(runtime: str, tid: str) -> list[str]:
    return [m.group(0) for m in re.finditer(rf"^(?:##|###) {re.escape(tid)}\b.*?(?=^(?:##|###) |\Z)", runtime, re.M | re.S)]


state_path = Path("CURRENT_STATE.md")
old = state_path.read_text(encoding="utf-8")

if HEADING in old:
    section = old.split(HEADING, 1)[1]
    for value in [
        "**PASS**",
        "24c8e3cdf059fc62a3df1fe8119b959246c216f6",
        "34d119334e07a5d6ffe63fb893bb741d3aa0c775",
        "33592936750 / 100130472136",
        "BROWSER_ACCEPTANCE_CHECKS=221",
        "ACC-0310 = PASS. VER-0310 = PASS. EVD-0310 = SATISFIED.",
    ]:
        assert value in section, value
    print("TSK0310_POST_COPY_STATE_RECONCILIATION=ALREADY_APPLIED")
    raise SystemExit(0)

for path, expected in EXPECTED.items():
    actual = blob(path)
    assert actual == expected, f"hash drift {path}: {actual} != {expected}"
print("TSK0310_POST_COPY_STATE_INPUT_HASHES=PASS")

with open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
row = next(r for r in rows if r.get("Task_ID") == "TSK-0310")
deps = [x.strip() for x in (row.get("Dependencies") or "").split(";") if x.strip()]
assert row["Lifecycle_Stage"] == "L4"
assert row["Priority"] == "HIGH"
assert row["AI_Capability_A0_A4"] == "A3"
assert row["Action_Authority"] == "AUTO_ALLOWED"
assert deps == ["TSK-0318", "TSK-0317", "TSK-0320", "TSK-0300"]
assert (row["Acceptance_ID"], row["Verification_ID"], row["Evidence_ID"]) == ("ACC-0310", "VER-0310", "EVD-0310")
print("TSK0310_POST_COPY_STATE_WBS=PASS")

for tid in deps:
    ss = sections(old, tid)
    assert ss and any("**PASS" in s for s in ss), f"missing durable PASS {tid}"
corrected_300 = "\n".join(sections(old, "TSK-0300"))
for value in [
    "172e4b82c7c106c48291c6a6a75aca6848ca4d0c",
    "a3e39896b67098ced321cb9e4b82c65c440806e4",
    "33592292946 / 100128578252",
    "ACC-0300 = PASS. VER-0300 = PASS. EVD-0300 = SATISFIED.",
]:
    assert value in corrected_300, value
print("TSK0310_POST_COPY_STATE_PREDECESSORS=PASS")

evidence = Path("TSK_0310_POST_TSK0300_COPY_CORRECTION_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md").read_text(encoding="utf-8")
for value in [
    "ACC-0310 = PASS. VER-0310 = PASS. EVD-0310 = SATISFIED",
    "33592936750 / 100130472136",
    "BROWSER_ACCEPTANCE_CHECKS=221",
    "BROWSER_ACCEPTANCE=PASS",
    "TSK0310_REFRESH_RENDERED_ACCEPTANCE=PASS",
    "TSK0310_REFRESH_SOURCE_UNCHANGED=PASS",
    "a3e39896b67098ced321cb9e4b82c65c440806e4",
    "33576615158 / 100081874297",
]:
    assert value in evidence, value
print("TSK0310_POST_COPY_STATE_EVIDENCE=PASS")

now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
base = re.sub(r"^\*\*Updated:\*\*.*$", f"**Updated:** {now}", old, count=1, flags=re.M)
assert mask_updated(base) == mask_updated(old)

append = f"""

{HEADING}

`TSK-0310 — Build the representative mobile-first public-to-setup prototype before production implementation`: **PASS** under current `ACC-0310 / VER-0310 / EVD-0310`, all four current direct predecessors, corrected TSK-0300 protection-state semantics, refreshed TSK-0317 proof, current TSK-0318 scope and current TSK-0320 state/copy authority.

- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / HIGH / A3 / `AUTO_ALLOWED`; hard dependencies exactly `TSK-0318; TSK-0317; TSK-0320; TSK-0300`.
- Current revalidation artifact `TSK_0310_POST_TSK0300_COPY_CORRECTION_CURRENT_REVALIDATION_2026-09-02.md`, blob `24c8e3cdf059fc62a3df1fe8119b959246c216f6`, publication commit `4c7da17cc9077b17eef025081e55012cad0bff20`.
- Durable evidence `TSK_0310_POST_TSK0300_COPY_CORRECTION_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md`, blob `34d119334e07a5d6ffe63fb893bb741d3aa0c775`, publication commit `684d7b1b6f435b4f5865f61fb6d52f7b9e1e87e3`.
- Corrected TSK-0300 predecessor is current PASS at runtime commit `93fea25db8c1b6fd70a8fd45e0ff531cf33ea2e1`; evidence blob `a3e39896b67098ced321cb9e4b82c65c440806e4` and independent run/job `33592292946 / 100128578252` are bound directly.
- Refreshed TSK-0317 predecessor evidence blob `cd001f3ce391634e38ef0c89934cb34f4f347401`; final run/job `33576615158 / 100081874297` SUCCESS.
- Corrected prototype source: model `cb35f7dbc46ba5d19da18fb09429b59e097e0492`, app `a235993d5abcaac550b6c01978792092012afb00`, browser verifier `5f68400a8bfb063853304e937f744e1ee71032e7`; unchanged index/CSS/shared tokens/components/SafeWeb identity remain preserved.
- Current six-state primary semantics are represented by `protected/verified`, `configured/parent-confirmed`, `action-needed`, `not-covered`, `uncertain/error`, `removed`, with current TSK-0320 copy including `Protection verified`, `Setup confirmed`, and `Protection status could not be verified`.
- Independent read-only VER-0310 workflow blob `41e96e2df5c94cf8c7a2a75e6c69ab13f59400c7`; final run/job `33592936750 / 100130472136`: **SUCCESS**.
- Fresh rendered result: `BROWSER_ACCEPTANCE_CHECKS=221`; `BROWSER_ACCEPTANCE=PASS`; `TSK0310_REFRESH_RENDERED_ACCEPTANCE=PASS`; source-unchanged proof PASS.
- The first refreshed run `33592798757 / 100130059983` is retained as diagnostic verifier-format failure only: it stopped before browser execution because it searched for `667/667` instead of the exact TSK-0321 markers `A11Y_CHECKS=667`, `A11Y_FAILURES=0`, `A11Y_ACCEPTANCE_FAILURES=0`; no product assertion failed and no product/runtime mutation occurred.
- Preserved boundary: TSK-0310 remains the representative accountless public-to-setup core prototype. Current TSK-0318 owns the separate optional-account/dashboard IA branch; no login/dashboard implementation is inferred here.
- **ACC-0310 = PASS. VER-0310 = PASS. EVD-0310 = SATISFIED.**
- **Non-inference:** no authentication/provider implementation, persistence schema, integrated production build, legal/privacy completion, behavioral/user validation, participant/publication/payment/market/production/launch action, lifecycle-gate PASS or successor PASS is inferred.

### Queue status after refreshed TSK-0310 reacceptance

Recompute current eligibility from canonical WBS/graph, current runtime evidence, gates and Action Authority. Preserve valid non-uniform historical PASS records unless current evidence actually invalidates them; do not infer a successor solely from TSK-0310 completion.
"""

candidate = base.rstrip() + append
assert mask_updated(candidate) == mask_updated(old).rstrip() + append
state_path.write_text(candidate, encoding="utf-8")
written = state_path.read_text(encoding="utf-8")
for value in [
    HEADING,
    "24c8e3cdf059fc62a3df1fe8119b959246c216f6",
    "34d119334e07a5d6ffe63fb893bb741d3aa0c775",
    "33592936750 / 100130472136",
    "BROWSER_ACCEPTANCE_CHECKS=221",
    "ACC-0310 = PASS. VER-0310 = PASS. EVD-0310 = SATISFIED.",
]:
    assert value in written, value
print("TSK0310_POST_COPY_ALL_EXISTING_RUNTIME_BODY_PRESERVED=PASS")
print("TSK0310_POST_COPY_STATE_CANDIDATE=PASS")
print("TSK0310_POST_COPY_STATE_RECONCILIATION=PASS")
