#!/usr/bin/env python3
"""Deterministic verifier for TSK-0049 L5 LG-07 technical/design approval component."""
from __future__ import annotations

import csv
import io
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WBS = ROOT / "Plans" / "Master" / "WBS" / "master-wbs.csv"
STATE = ROOT / "CURRENT_STATE.md"
ARTIFACT = ROOT / "TSK_0049_LG07_ARCHITECTURE_PRIVACY_SECURITY_OPERATIONS_APPROVAL_COMPONENT_2026-09-02.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def main() -> None:
    require(WBS.is_file(), f"missing WBS: {WBS}")
    require(STATE.is_file(), f"missing runtime: {STATE}")
    require(ARTIFACT.is_file(), f"missing artifact: {ARTIFACT}")

    rows = list(csv.DictReader(io.StringIO(read_text(WBS))))
    matches = [row for row in rows if row.get("Task_ID") == "TSK-0049"]
    require(len(matches) == 1, "expected exactly one TSK-0049 WBS row")
    row = matches[0]

    require(row.get("Lifecycle_Stage") == "L5", "TSK-0049 must remain L5")
    require(row.get("Priority") == "MEDIUM", "TSK-0049 priority drift")
    require(row.get("AI_Capability_A0_A4") == "A4", "TSK-0049 AI capability drift")
    require(row.get("Action_Authority") == "AUTO_ALLOWED", "TSK-0049 authority drift")
    deps = {item.strip() for item in (row.get("Dependencies") or "").split(";") if item.strip()}
    require(deps == {"TSK-0239", "TSK-0539"}, f"TSK-0049 dependency drift: {sorted(deps)}")
    require(row.get("Acceptance_ID") == "ACC-0049", "TSK-0049 acceptance id drift")
    require(row.get("Verification_ID") == "VER-0049", "TSK-0049 verification id drift")
    require(row.get("Evidence_ID") == "EVD-0049", "TSK-0049 evidence id drift")

    state = read_text(STATE)
    for dep in ("TSK-0239", "TSK-0539"):
        require(dep in state, f"runtime missing {dep}")
        marker = f"`{dep}"
        start = state.find(marker)
        require(start >= 0, f"runtime missing accepted-state marker for {dep}")
        window = state[start:start + 3500]
        require("**PASS**" in window or ": **PASS**" in window, f"{dep} is not current durable PASS in runtime")

    artifact = read_text(ARTIFACT)

    for token in (
        "TSK-0321",
        "TSK-0410",
        "TSK-0485",
        "TSK-0239",
        "TSK-0356",
        "TSK-0232",
        "TSK-0234",
        "TSK-0446",
        "TSK-0518",
        "TSK-0498",
        "TSK-0538",
        "TSK-0539",
        "TSK-0585",
        "TSK-0586",
        "CR-0009",
        "DEC-0056",
    ):
        require(token in artifact, f"artifact missing required evidence/authority token {token}")

    required_phrases = (
        "direct LG-07 technical/design component",
        "not final LG-07 PASS",
        "not proof of L6/runtime implementation",
        "OWNER_EXTERNAL_SATISFIED",
        "No legal evidence",
        "No legal evidence, legal compliance status, legal PASS",
        "Downstream implementation and retest obligations remain mandatory and blocking",
        "no unresolved High/Critical architecture or control-plan gap within this TSK-0049 technical/design component",
        "does not authorize spend",
    )
    artifact_lower = artifact.lower()
    for phrase in required_phrases:
        require(phrase.lower() in artifact_lower, f"artifact missing required boundary: {phrase}")

    forbidden_claims = (
        "LG-07 is PASS",
        "LG-07: PASS",
        "L6 implementation is complete",
        "production is ready",
        "legal compliance is confirmed",
        "legally compliant",
    )
    for phrase in forbidden_claims:
        require(phrase.lower() not in artifact_lower, f"artifact contains forbidden overclaim: {phrase}")

    print("PASS: TSK-0049 L5 LG-07 technical/design approval component is internally consistent with current canonical WBS/runtime boundaries.")


if __name__ == "__main__":
    main()
