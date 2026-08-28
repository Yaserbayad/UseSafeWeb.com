#!/usr/bin/env python3
import csv
import datetime
import json
import re
import subprocess
from pathlib import Path

STATE = Path("CURRENT_STATE.md")
EVIDENCE = Path("TSK_0207_PRIVACY_PERSISTENCE_EVIDENCE_2026-08-28.md")
QUEUE = Path("TSK_0207_QUEUE_RECOMPUTE_EVIDENCE_2026-08-28.md")
EXPECTED_STATE = "3987dabdeced6ea70e811bc9b7a59dcd0ed46758"
EXPECTED_EVIDENCE = "1c16db063e2e84d300b547075721d33c2e020e32"


def blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


if blob(STATE) != EXPECTED_STATE:
    raise SystemExit(f"CURRENT_STATE stale: expected {EXPECTED_STATE}, got {blob(STATE)}")
if blob(EVIDENCE) != EXPECTED_EVIDENCE:
    raise SystemExit(f"TSK-0207 evidence mismatch: expected {EXPECTED_EVIDENCE}, got {blob(EVIDENCE)}")

state = STATE.read_text(encoding="utf-8")
pass_block = state.split("### PASS", 1)[1].split("### TSK-0204 corrected stable state", 1)[0]
if "`TSK-0207`" in pass_block:
    raise SystemExit("TSK-0207 already runtime PASS; manual reconciliation required")

now = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
state = re.sub(r"\*\*Updated:\*\* [^\n]+", f"**Updated:** {now}  ", state, count=1)

anchor = "- `TSK-0206` — client-IP anonymisation enabled while query logging/statistics remain disabled — evidence: `TSK_0206_CLIENT_IP_ANONYMIZATION_EVIDENCE_2026-08-27.md`, blob `5905136433d930c2325a877e10a45e8540ac6a80`.\n"
addition = "- `TSK-0207` — synthetic production persistence audit proves no persistent raw query/domain history, file query log, identifiable client/statistics history, or unapproved backup copy in controlled project locations; only the documented approved encrypted configuration recovery artifact remains — evidence: `TSK_0207_PRIVACY_PERSISTENCE_EVIDENCE_2026-08-28.md`, blob `1c16db063e2e84d300b547075721d33c2e020e32`, publication commit `53728ea6cc13e9510859217b4567294a30a60bab`.\n"
if anchor not in state:
    raise SystemExit("TSK-0206 PASS anchor not found")
state = state.replace(anchor, anchor + addition, 1)

section = """### TSK-0207 accepted stable state

`TSK-0207` — verify no persistent identifiable query history or client statistics: **PASS**.

ACC-0207 requires that after a controlled test there be no persistent raw query/domain history, file query log, identifiable client history, or unapproved backup copy, and that any residual operational data be documented/anonymised. VER-0207/EVD-0207 require the approved procedure against the exact artifact/environment with reproducible output and reviewer disposition.

Fresh production evidence `TSK_0207_PRIVACY_PERSISTENCE_EVIDENCE_2026-08-28.md`, blob `1c16db063e2e84d300b547075721d33c2e020e32`, publication commit `53728ea6cc13e9510859217b4567294a30a60bab`, executed on the accepted production host `adguardvm`, AdGuard Home v0.107.79, against runtime-state blob `3987dabdeced6ea70e811bc9b7a59dcd0ed46758`, approved-config blob `e9975c4e75c2a68131f049da942468d8d1952d8d`, and backup-policy blob `e62b48a3e746b1be90881bbffab3b7680384cc16`.

The assertion-based synthetic test proved persisted/API query logging disabled; persisted file query logging disabled; a randomized reserved `.invalid` request absent from query-log output with query-log item count zero; no non-empty `querylog.json*`; persisted/API statistics disabled; top-client count and stored statistics query count zero; persistent client count zero; client-IP anonymisation enabled; one approved root-only age-encrypted configuration backup pair with matching metadata/hash; zero unexpected backup-directory classes; zero plaintext staging; and zero stale/raw/unapproved backup-named artifacts in the controlled service/config/secret/temp locations.

The retained same-VM encrypted backup remains the documented approved configuration recovery artifact already proven under TSK-0430 to exclude prohibited query/client history. It is not a participant-history dataset and is not evidence of node-loss resilience.

REQ-0018 and RSK-0001 remain respected: this was a synthetic rehearsal only and no real England participant was activated or processed. The separately deferred UK representative/ICO work remains unresolved. **ACC-0207 is fully satisfied. TSK-0207: PASS.**

"""
marker = "### External/provider and legal boundaries\n"
if marker not in state:
    raise SystemExit("external-boundary marker not found")
state = state.replace(marker, section + marker, 1)

state = state.replace(
    "- TSK-0442 TLS target-device acceptance, TSK-0443 certificate renewal/expiry controls, TSK-0514 external-network/removal verification, TSK-0511 per-supported-device verification, and TSK-0512 filtering/exception/rollback verification are satisfied. None of these technical PASS states by themselves authorize participant activation.",
    "- TSK-0442 TLS target-device acceptance, TSK-0443 certificate renewal/expiry controls, TSK-0514 external-network/removal verification, TSK-0511 per-supported-device verification, TSK-0512 filtering/exception/rollback verification, and TSK-0207 privacy-persistence verification are satisfied. None of these PASS states by themselves authorize participant activation.",
)
state = state.replace(
    "- Plain DNS 53 remains non-public. TSK-0442 TLS, TSK-0443 certificate renewal/expiry controls, TSK-0514 external-network/removal verification, TSK-0511 supported-device verification and TSK-0512 filtering regression are PASS, but broader participant/public readiness remains gated by validation, privacy/legal and activation evidence.",
    "- Plain DNS 53 remains non-public. TSK-0442 TLS, TSK-0443 certificate renewal/expiry controls, TSK-0514 external-network/removal verification, TSK-0511 supported-device verification, TSK-0512 filtering regression and TSK-0207 privacy-persistence verification are PASS, but broader participant/public readiness remains gated by validation, privacy/legal and activation evidence.",
)

rows = list(csv.DictReader(open("Plans/Master/WBS/master-wbs.csv", newline="", encoding="utf-8-sig")))
pass_block = state.split("### PASS", 1)[1].split("### TSK-0204 corrected stable state", 1)[0]
runtime_pass = set(re.findall(r"`(TSK-\d+)`\s+—", pass_block))
runtime_pass.add("TSK-0011")
runtime_wait = set(re.findall(r"### WAITING — (TSK-\d+)", state))
planning_pass = {r["Task_ID"].strip() for r in rows if (r.get("Execution_State") or "").strip() == "PASS"}
satisfied = runtime_pass | planning_pass
rank = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
ready = []
for i, row in enumerate(rows):
    tid = (row.get("Task_ID") or "").strip()
    if not tid or tid in runtime_pass or tid in runtime_wait:
        continue
    if (row.get("Lifecycle_Stage") or "").strip() != "L2":
        continue
    if (row.get("Action_Authority") or "").strip() != "AUTO_ALLOWED":
        continue
    if (row.get("Plan_Status") or "").strip() not in {"PLANNED", "ACTIVE"}:
        continue
    deps = [x.strip() for x in (row.get("Dependencies") or "").split(";") if x.strip()]
    if all(dep in satisfied for dep in deps):
        ready.append((i, row, deps))
ready.sort(key=lambda item: (rank.get((item[1].get("Priority") or "").strip(), 9), item[0], item[1]["Task_ID"]))

qlines = [
    "# Queue Recompute Evidence after TSK-0207 PASS", "", "**Date:** 2026-08-28", "",
    f"- Pre-mutation CURRENT_STATE blob: `{EXPECTED_STATE}`",
    f"- TSK-0207 evidence blob: `{EXPECTED_EVIDENCE}`",
    f"- Runtime PASS count after local reconciliation (including TSK-0011 sentinel): `{len(runtime_pass)}`",
    f"- Runtime WAIT: `{','.join(sorted(runtime_wait)) or 'none'}`",
    f"- L2 AUTO_ALLOWED dependency-ready count: `{len(ready)}`", "", "## Dependency-ready tasks", "",
]
if not ready:
    qlines.append("None.")
else:
    for _, row, _ in ready[:40]:
        qlines.extend([
            f"### {row.get('Task_ID','')} — {row.get('Title','')}", "",
            f"- Priority: `{row.get('Priority','')}`",
            f"- Critical path: `{row.get('Critical_Path','')}`",
            f"- Plan status: `{row.get('Plan_Status','')}`",
            f"- WBS execution snapshot: `{row.get('Execution_State','')}`",
            f"- Dependencies: `{row.get('Dependencies','')}`",
            f"- Action authority: `{row.get('Action_Authority','')}`",
            f"- Acceptance: `{row.get('Acceptance_ID','')}` — {row.get('Acceptance_Criteria','')}",
            f"- Verification: `{row.get('Verification_ID','')}`",
            f"- Required tools/access: {row.get('Required_Tools_or_Access','')}",
            f"- Requirement refs: `{row.get('Requirement_Reference','')}`",
            f"- Interface refs: `{row.get('Interface_Reference','')}`",
            f"- Risk refs: `{row.get('Risk_Reference','')}`",
            f"- Trigger: {row.get('Trigger','')}",
            f"- Preconditions: {row.get('Preconditions','')}", "",
        ])
qlines.extend(["## Selection note", "", "Dependency readiness alone does not authorize execution; every candidate still requires current gate/trigger/constraint/interface/platform/authority preflight and direct acceptance evidence.", ""])
QUEUE.write_text("\n".join(qlines), encoding="utf-8")

tail = "## Queue status after current reconciliation\n\n"
tail += f"TSK-0207 is runtime PASS with fresh synthetic production privacy-persistence evidence. The deterministic WBS dependency-readiness recomputation found **{len(ready)}** L2 `AUTO_ALLOWED` candidate(s).\n\n"
if ready:
    first = ready[0][1]
    tail += f"Highest dependency-ready candidate: `{first.get('Task_ID','')}` — {first.get('Title','')}. Dependency readiness alone does not authorize execution; full current preflight is required.\n\n"
else:
    tail += "No ordinary L2 `AUTO_ALLOWED` candidate is dependency-ready.\n\n"
tail += "Current explicit WAITING boundary:\n\n- `TSK-0431` — identify/provide the owner-managed Azure-native backup/restore path required by REQ-0052.\n\n"
tail += "## Exact next authoritative step\n\n"
if ready:
    first = ready[0][1]
    tail += f"Preflight `{first.get('Task_ID','')}` — {first.get('Title','')} against its exact acceptance, gates, trigger, requirements, constraints, interfaces, risk and available executor. Continue only if safe and authorized. "
else:
    tail += "No ordinary L2 work may progress until a dependency/gate condition changes. "
tail += "Separately, TSK-0431 remains WAITING on the owner-managed Azure-native backup/restore path. Do not bypass participant-activation, legal, Azure control-plane, provider, recovery, privacy or validation gates.\n"
state = state.split("## Queue status after current reconciliation\n", 1)[0] + tail
STATE.write_text(state, encoding="utf-8")

print(f"READY_COUNT={len(ready)}")
for _, row, _ in ready[:10]:
    print("READY=" + json.dumps({key: row.get(key, "") for key in ["Task_ID","Title","Priority","Critical_Path","Dependencies","Action_Authority","Acceptance_ID","Acceptance_Criteria","Verification_ID","Required_Tools_or_Access","Requirement_Reference","Interface_Reference","Risk_Reference","Trigger","Preconditions"]}, sort_keys=True, ensure_ascii=False))
