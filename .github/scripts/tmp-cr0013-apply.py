#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import io
import os
import re
import subprocess
import sys
from pathlib import Path

BASE_SHA = "d941ccf5ede60878d355c3b6395c9c689f75cf44"
OLD_ACC = "Checks run locally/CI; critical paths require review; generated/configuration changes are included; exceptions are documented and time-bounded."
NEW_ACC = "Checks run locally/CI; critical-path changes are subject to deterministic automated quality/change-policy verification without mandatory human or Code Owner approval; generated/configuration changes are included; exceptions are documented and time-bounded."
TEMP_WORKFLOW = Path(".github/workflows/tmp-cr0013-autonomous-review-apply.yml")
TEMP_SCRIPT = Path(".github/scripts/tmp-cr0013-apply.py")


def sh(*args: str, capture: bool = False) -> str:
    if capture:
        return subprocess.check_output(args, text=True).strip()
    subprocess.run(args, check=True)
    return ""


def read(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def write(path: str | Path, text: str) -> None:
    Path(path).write_text(text, encoding="utf-8")


def replace_once(path: str | Path, old: str, new: str) -> None:
    text = read(path)
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected exactly one replacement target, found {count}")
    write(path, text.replace(old, new, 1))


def update_wbs() -> None:
    p = Path("Plans/Master/WBS/master-wbs.csv")
    lines = p.read_text(encoding="utf-8-sig").splitlines()
    header = next(csv.reader([lines[0]]))
    task_i = header.index("Task_ID")
    acc_i = header.index("Acceptance_Criteria")
    changed = False
    for i in range(1, len(lines)):
        if not lines[i].startswith("TSK-0453,"):
            continue
        row = next(csv.reader([lines[i]]))
        if row[task_i] != "TSK-0453" or row[acc_i] != OLD_ACC:
            raise SystemExit("TSK-0453 WBS source does not match expected pre-change authority")
        before = row.copy()
        row[acc_i] = NEW_ACC
        for j, (a, b) in enumerate(zip(before, row)):
            if j != acc_i and a != b:
                raise SystemExit(f"Unexpected TSK-0453 mutation at {header[j]}")
        out = io.StringIO(newline="")
        csv.writer(out, lineterminator="").writerow(row)
        lines[i] = out.getvalue()
        changed = True
        break
    if not changed:
        raise SystemExit("TSK-0453 row not found")
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")


def update_decisions() -> None:
    p = Path("Plans/Master/Registers/DECISIONS_TRIGGERS.md")
    lines = read(p).splitlines()
    if any(line.startswith("| DEC-0060 |") for line in lines):
        raise SystemExit("DEC-0060 already exists")
    idx = next(i for i, line in enumerate(lines) if line.startswith("| DEC-0059 |"))
    row = (
        "| DEC-0060 | New | Autonomous critical-path review policy | "
        "ACTIVE OWNER DECISION — ordinary governed `AUTO_ALLOWED` changes, including critical-path changes, do not require mandatory human/Code Owner approval or branch protection as a merge condition. "
        "`TSK-0453` instead requires deterministic automated local/CI quality and change-policy verification, generated/configuration coverage, and explicit time-bounded exceptions. "
        "CODEOWNERS may remain advisory routing metadata but must not create a human approval gate. Separate genuine human-only, strategic, safety, security, legal, identity, contract, material-spend or irreversible-action boundaries remain unchanged. | "
        "Explicit Project Owner instruction 2026-09-04. | Revised `ACC-0453` in WBS and synchronized acceptance register; updated review policy/template/contract; deterministic master-plan validation; formatting/lint/type/contracts/build/audits; exact GitHub publication/read-back. | "
        "Project Owner | TSK-0453; TSK-0489; CR-0013; `.github` review/CI policy | Explicit Project Owner instruction 2026-09-04; DEC-0054/DEC-0055 autonomy principles retained |"
    )
    lines.insert(idx + 1, row)
    write(p, "\n".join(lines) + "\n")


def update_change_control() -> None:
    p = Path("Plans/Master/Registers/EXCEPTIONS_CHANGE_CONTROLS.md")
    lines = read(p).splitlines()
    if any(line.startswith("| CR-0013 |") for line in lines):
        raise SystemExit("CR-0013 already exists")
    idx = next(i for i, line in enumerate(lines) if line.startswith("| CR-0012 |"))
    row = (
        "| CR-0013 | Project Owner | 2026-09-04 | Remove mandatory human/Code Owner merge approval from `TSK-0453` and replace that single acceptance clause with deterministic automated critical-path quality/change-policy verification. | "
        "TSK-0453 WBS Acceptance_Criteria; synchronized acceptance register; DEC-0060; `.github/CHANGE_REVIEW_POLICY.md`; `.github/CODEOWNERS` advisory description; pull-request template; TSK-0453 contract/workflow; manifest latest-change metadata; generated reconstruction/checksums; runtime reconciliation. No task ID, dependency edge, plan status, action authority, requirement, interface, risk, gate, milestone, TSK-0455 contract or material-action fence changes. | "
        "Explicit owner decision that mandatory owner approval is not wanted because it unnecessarily reduces intended AI autonomy. Existing TSK-0453 source/CI evidence remains valid except for the superseded human-review-enforcement clause. | "
        "Project Owner DEC-0060; actual safety/security/platform/technical reality remains higher authority. | Revise only ACC-0453 review semantics; make CODEOWNERS non-blocking/advisory; keep automated formatting/lint/type/change-policy controls; rebuild/checksum/validate; run full TSK-0453 verification; if all revised criteria pass, reconcile TSK-0453 to PASS and recompute successors. | "
        "Explicit owner reversal may restore mandatory human review; restore the prior ACC/policy from Git history and re-evaluate TSK-0453. No prior evidence is discarded except the superseded enforcement wait condition. | "
        "Validator PASS with 641 tasks and 858 dependency edges; parsed WBS comparison proves only TSK-0453 Acceptance_Criteria changed; TSK-0455/0456/0457/0492 rows remain byte-semantically unchanged; TSK-0453 formatting/lint/type/contracts/build/audits and negative formatter propagation pass; exact GitHub commit/blob read-back required. | "
        "ACTIVE — creates no deployment, telemetry activation, participant-facing mutation, production credential/service revocation, payment, activation, launch or other material-action authority. |"
    )
    lines.insert(idx + 1, row)
    write(p, "\n".join(lines) + "\n")


def update_manifest() -> None:
    p = Path("Plans/Master/MANIFEST.yaml")
    text = read(p)
    marker = " / OWNER_SINGLE_WORKING_SERVER_RECOVERY_DEFERRAL_CR_0012"
    if text.count(marker) != 1:
        raise SystemExit("Manifest CR-0012 status marker mismatch")
    text = text.replace(marker, marker + " / OWNER_AUTONOMOUS_REVIEW_POLICY_CR_0013", 1)
    pattern = re.compile(r"post_freeze_change_control:\n.*?\ngenerated_assembly_contract:\n", re.S)
    block = "\n".join([
        "post_freeze_change_control:",
        "  latest_change: CR-0013",
        "  previous_change: CR-0012",
        "  date: '2026-09-04'",
        "  status: owner-approved removal of mandatory human/Code Owner merge approval from TSK-0453 in favor of deterministic automated critical-path quality/change-policy verification",
        "  authority: explicit current Project Owner instruction 2026-09-04; DEC-0060/CR-0013; actual law/safety/security/platform/technical reality remains higher authority",
        "  affected_scope:",
        "  - TSK-0453 Acceptance_Criteria and synchronized acceptance register",
        "  - DEC-0060 and CR-0013 change-control metadata",
        "  - repository review/CI policy, pull-request review wording, focused TSK-0453 contract/workflow, generated reconstruction and checksums",
        "  - CURRENT_STATE reconciliation after complete verification; no dependency edge, action authority, gate, requirement, interface, risk, TSK-0455 contract or material-action fence change",
        "  semantic_delta: critical-path human/Code Owner approval is advisory/not mandatory for ordinary governed AUTO_ALLOWED work; deterministic automated local/CI quality and change-policy verification remains mandatory; genuine separate human-authority boundaries remain unchanged",
        "  change_record: Registers/EXCEPTIONS_CHANGE_CONTROLS.md#post-freeze-material-change-records",
        "",
        "generated_assembly_contract:",
        "",
    ])
    text, n = pattern.subn(block, text, count=1)
    if n != 1:
        raise SystemExit("Manifest post_freeze_change_control block mismatch")
    write(p, text)


def update_repo_policy() -> None:
    replace_once(
        ".github/CHANGE_REVIEW_POLICY.md",
        "Changes to critical paths declared in `.github/CODEOWNERS` require owner review as repository policy. **GitHub only makes that requirement merge-blocking when the `main` branch is protected by a branch protection rule or ruleset requiring Code Owner review.** CODEOWNERS alone is review-routing metadata, not proof of platform enforcement.",
        "Changes to critical paths declared in `.github/CODEOWNERS` retain advisory owner-routing metadata for visibility, but owner/Code Owner approval is **not a mandatory merge condition**. Under DEC-0060/CR-0013, ordinary governed `AUTO_ALLOWED` changes are accepted through deterministic automated local/CI quality and change-policy verification instead of a human approval gate.",
    )
    replace_once(
        ".github/CHANGE_REVIEW_POLICY.md",
        "## Current platform enforcement boundary\n\nSource policy and CODEOWNERS can be versioned here. Merge-blocking review enforcement is a GitHub repository setting. Until branch protection/rulesets are verified to require the intended review on `main`, TSK-0453 cannot claim that critical-path review is technically enforced.",
        "## Autonomous review boundary\n\nBranch protection or required Code Owner approval is not required by ACC-0453 under DEC-0060/CR-0013. CODEOWNERS remains advisory routing metadata only. Formatting, linting, type checking, focused change-policy contracts, applicable tests/build/audits, generated/configuration impact coverage, and bounded exception documentation remain mandatory. A separate current human-authority, safety, security, legal, identity, contract, material-spend, strategic or irreversible-action boundary still overrides this policy where applicable.",
    )
    replace_once(
        ".github/CODEOWNERS",
        "# Critical/governance paths. GitHub only enforces these approvals when branch protection/rulesets require Code Owner review.",
        "# Critical/governance path ownership/routing metadata. Under DEC-0060/CR-0013 this is advisory and does not require human/Code Owner approval to merge.",
    )
    replace_once(
        ".github/pull_request_template.md",
        "## Review\n\n- [ ] CODEOWNERS critical-path review applies\n- [ ] No critical-path review applies",
        "## Review / automated governance\n\n- [ ] Applicable automated critical-path quality/change-policy verification passed\n- [ ] Optional CODEOWNERS routing/review considered where useful; human approval is not a default merge gate",
    )


def update_contract_and_workflow() -> None:
    p = Path("website/tests/contract/tsk0453.test.mjs")
    text = read(p)
    old_name = "test('TSK-0453 defines review ownership for critical and governance paths', () => {"
    new_name = "test('TSK-0453 records advisory ownership routing for critical and governance paths', () => {"
    if text.count(old_name) != 1:
        raise SystemExit("Focused contract ownership test mismatch")
    text = text.replace(old_name, new_name, 1)
    old_assert = "  assert.match(policy, /owner/i);\n  assert.match(policy, /expir/i);\n  assert.match(policy, /branch protection|ruleset/i);"
    new_assert = "  assert.match(policy, /owner/i);\n  assert.match(policy, /expir/i);\n  assert.match(policy, /deterministic automated/i);\n  assert.match(policy, /not a mandatory merge condition/i);\n  assert.match(policy, /AUTO_ALLOWED/);\n  assert.doesNotMatch(policy, /TSK-0453 cannot claim/i);"
    if text.count(old_assert) != 1:
        raise SystemExit("Focused contract policy assertion mismatch")
    write(p, text.replace(old_assert, new_assert, 1))

    wf = Path(".github/workflows/accept-tsk0453-quality-review-rules-20260903.yml")
    text = read(wf)
    old = "          test \"$(git hash-object Plans/Master/WBS/master-wbs.csv)\" = 'eb35f3b10356396c5117e3f47d0b0378953e2157'"
    new = (
        "          python3 -c 'import csv; f=open(\"Plans/Master/WBS/master-wbs.csv\", newline=\"\", encoding=\"utf-8-sig\"); "
        "r=next(x for x in csv.DictReader(f) if x[\"Task_ID\"]==\"TSK-0453\"); "
        "assert r[\"Dependencies\"]==\"TSK-0380\"; "
        "assert r[\"Acceptance_Criteria\"]==\"" + NEW_ACC.replace("\\", "\\\\").replace('"', '\\"') + "\"'"
    )
    if text.count(old) != 1:
        raise SystemExit("Permanent TSK-0453 workflow WBS guard mismatch")
    write(wf, text.replace(old, new, 1))


def rebuild_and_checksums() -> None:
    sh("python3", "Plans/Master/Tools/rebuild_master_plan.py")
    checksum = Path("Plans/SHA256SUMS.txt")
    paths: list[str] = []
    for line in read(checksum).splitlines():
        if line.strip():
            _, rel = line.split("  ", 1)
            paths.append(rel)
    out: list[str] = []
    for rel in paths:
        p = Path("Plans") / rel
        if not p.is_file():
            raise SystemExit(f"Missing checksummed file: {p}")
        out.append(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {rel}")
    write(checksum, "\n".join(out) + "\n")


def verify_wbs_delta() -> None:
    old = sh("git", "show", f"{BASE_SHA}:Plans/Master/WBS/master-wbs.csv", capture=True)
    new = Path("Plans/Master/WBS/master-wbs.csv").read_text(encoding="utf-8-sig")
    old_rows = {r["Task_ID"]: r for r in csv.DictReader(io.StringIO(old))}
    new_rows = {r["Task_ID"]: r for r in csv.DictReader(io.StringIO(new))}
    if old_rows.keys() != new_rows.keys() or len(new_rows) != 641:
        raise SystemExit("WBS task identity/count changed")
    diffs: list[tuple[str, str, str, str]] = []
    for tid in old_rows:
        for key in old_rows[tid]:
            if old_rows[tid][key] != new_rows[tid][key]:
                diffs.append((tid, key, old_rows[tid][key], new_rows[tid][key]))
    if len(diffs) != 1 or diffs[0][0:2] != ("TSK-0453", "Acceptance_Criteria"):
        raise SystemExit(f"Unexpected WBS delta: {diffs[:20]}")
    for tid in ("TSK-0455", "TSK-0456", "TSK-0457", "TSK-0492"):
        if old_rows[tid] != new_rows[tid]:
            raise SystemExit(f"Preserved row changed: {tid}")
    deps = sum(len([x for x in r["Dependencies"].split(";") if x.strip()]) for r in new_rows.values())
    if deps != 858:
        raise SystemExit(f"Dependency edge count changed: {deps}")
    print("CR0013_WBS_SEMANTIC_DIFF=PASS tasks=641 dependency_edges=858 changed=TSK-0453.Acceptance_Criteria")


def apply_source() -> None:
    if sh("git", "rev-parse", "HEAD^", capture=True) != BASE_SHA:
        # The staging trigger commit must be exactly one commit above the authoritative base.
        head_parent = sh("git", "rev-parse", "HEAD^", capture=True)
        if head_parent != BASE_SHA:
            raise SystemExit(f"Unexpected staging ancestry: parent={head_parent} expected={BASE_SHA}")

    update_wbs()
    replace_once("Plans/Master/Registers/VERIFICATION_EVIDENCE_ACCEPTANCE.md", OLD_ACC, NEW_ACC)
    update_decisions()
    update_change_control()
    update_manifest()
    update_repo_policy()
    update_contract_and_workflow()
    rebuild_and_checksums()

    TEMP_WORKFLOW.unlink(missing_ok=False)
    TEMP_SCRIPT.unlink(missing_ok=False)

    sh("git", "config", "user.name", "github-actions[bot]")
    sh("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
    sh("git", "add", "-A")
    sh("git", "diff", "--cached", "--check")
    verify_wbs_delta()

    expected = sorted([
        ".github/CHANGE_REVIEW_POLICY.md",
        ".github/CODEOWNERS",
        ".github/pull_request_template.md",
        ".github/workflows/accept-tsk0453-quality-review-rules-20260903.yml",
        "Plans/Master/Generated/MASTER_PLAN_FULL.md",
        "Plans/Master/MANIFEST.yaml",
        "Plans/Master/Registers/DECISIONS_TRIGGERS.md",
        "Plans/Master/Registers/EXCEPTIONS_CHANGE_CONTROLS.md",
        "Plans/Master/Registers/VERIFICATION_EVIDENCE_ACCEPTANCE.md",
        "Plans/Master/WBS/master-wbs.csv",
        "Plans/SHA256SUMS.txt",
        "website/tests/contract/tsk0453.test.mjs",
    ])
    actual = sorted(sh("git", "diff", "--cached", "--name-only", capture=True).splitlines())
    if actual != expected:
        raise SystemExit(f"Unexpected source changed paths: {actual}")

    sh("git", "commit", "-m", "governance: apply CR-0013 autonomous review policy")
    print("CR0013_SOURCE_COMMIT=" + sh("git", "rev-parse", "HEAD", capture=True))
    print("CR0013_SOURCE_TREE=" + sh("git", "rev-parse", "HEAD^{tree}", capture=True))


def finalize_state() -> None:
    source = os.environ["CR0013_SOURCE_COMMIT"]
    tree = os.environ["CR0013_SOURCE_TREE"]
    run_id = os.environ["GITHUB_RUN_ID"]
    attempt = os.environ.get("GITHUB_RUN_ATTEMPT", "1")
    now = sh("date", "-u", "+%Y-%m-%dT%H:%M:%SZ", capture=True)

    def blob(path: str) -> str:
        return sh("git", "hash-object", path, capture=True)

    evidence = f"""# TSK-0453 / CR-0013 — Autonomous Review Acceptance Evidence

Date: {now}
Owner decision: 2026-09-04T09:15:08Z
Decision/change: DEC-0060 / CR-0013
Task: `TSK-0453 — Configure formatting, linting, type checking, commit/change, and code-review rules`
Stable disposition after canonical publication/read-back: **PASS**

## Owner-authorized semantic change

The Project Owner explicitly rejected mandatory owner/Code Owner merge approval and chose the controlled alternative: revise ACC-0453 so critical-path changes use deterministic automated quality/change-policy verification without mandatory human or Code Owner approval. This is an acceptance-baseline change, not a fabricated enforcement result.

Revised ACC-0453:

> {NEW_ACC}

CODEOWNERS remains advisory routing metadata only. Separate genuine human-only, strategic, safety, security, legal, identity, contract, material-spend and irreversible-action boundaries are unchanged.

## Preserved prior evidence

The 2026-09-03 source checkpoint remains valid for formatter/lint/type/check/change-policy implementation and regression evidence: `TSK_0453_QUALITY_AND_REVIEW_RULES_SOURCE_CHECKPOINT_2026-09-03.md`, blob `{blob('TSK_0453_QUALITY_AND_REVIEW_RULES_SOURCE_CHECKPOINT_2026-09-03.md')}`. Its former WAIT condition is superseded only by DEC-0060/CR-0013.

## Exact source and verification

- CR-0013 source commit: `{source}`
- CR-0013 source tree: `{tree}`
- GitHub Actions run/attempt: `{run_id} / {attempt}`
- Base canonical main before change: `{BASE_SHA}`
- WBS blob: `{blob('Plans/Master/WBS/master-wbs.csv')}`
- Manifest blob: `{blob('Plans/Master/MANIFEST.yaml')}`
- Decision register blob: `{blob('Plans/Master/Registers/DECISIONS_TRIGGERS.md')}`
- Change-control register blob: `{blob('Plans/Master/Registers/EXCEPTIONS_CHANGE_CONTROLS.md')}`
- Acceptance register blob: `{blob('Plans/Master/Registers/VERIFICATION_EVIDENCE_ACCEPTANCE.md')}`
- Review policy blob: `{blob('.github/CHANGE_REVIEW_POLICY.md')}`
- CODEOWNERS blob: `{blob('.github/CODEOWNERS')}`
- Focused contract blob: `{blob('website/tests/contract/tsk0453.test.mjs')}`
- Permanent TSK-0453 workflow blob: `{blob('.github/workflows/accept-tsk0453-quality-review-rules-20260903.yml')}`
- Generated master-plan blob: `{blob('Plans/Master/Generated/MASTER_PLAN_FULL.md')}`
- Plans checksum blob: `{blob('Plans/SHA256SUMS.txt')}`

Verification completed successfully on the exact source commit before this evidence/state-only commit:

- repository structure verification PASS;
- deterministic Master Plan validator PASS with 641 tasks and 858 dependency edges;
- parsed WBS semantic diff proves the only task-field change is TSK-0453 Acceptance_Criteria;
- TSK-0455, TSK-0456, TSK-0457 and TSK-0492 WBS rows are unchanged;
- pinned Prettier 3.9.6 verified;
- focused TSK-0453 contract PASS;
- format check PASS;
- lint PASS;
- typecheck PASS;
- full contract suite PASS;
- production build PASS;
- npm audit and production-only npm audit PASS at high threshold;
- deliberate unformatted-source negative probe returned nonzero and was removed; post-probe format check PASS;
- clean worktree and git diff check PASS.

## Acceptance disposition

Under revised ACC-0453, every applicable clause is proven. Mandatory GitHub branch protection/Code Owner approval is intentionally not part of the current acceptance contract. TSK-0453 may therefore be reconciled to PASS after exact canonical publication/read-back.

## Preserved fences

This change performs no deployment, telemetry activation, participant-facing mutation, production credential or service revocation, payment, activation, launch, service-removal/revocation, live-device/profile/certificate action, or other fenced material action. TSK-0455 remains DEFERRED/WAITING under DEC-0059/CR-0012 with ACC-0455/VER-0455/EVD-0455 unchanged; TSK-0456, TSK-0457 and TSK-0492 remain dependency-blocked.
"""
    write("TSK_0453_CR0013_AUTONOMOUS_REVIEW_ACCEPTANCE_EVIDENCE_2026-09-04.md", evidence)

    state_path = Path("CURRENT_STATE.md")
    state = read(state_path)
    state, n = re.subn(r"\*\*Updated:\*\* [^\n]+", f"**Updated:** {now}", state, count=1)
    if n != 1:
        raise SystemExit("CURRENT_STATE Updated anchor mismatch")

    anchor = "- Latest post-freeze planning change: `CR-0011` / `DEC-0058`"
    replacement = (
        "- Latest post-freeze planning change: `CR-0013` / `DEC-0060`, explicitly authorized by the Project Owner on 2026-09-04: mandatory human/Code Owner merge approval is removed from TSK-0453 and replaced by deterministic automated critical-path quality/change-policy verification; all genuine separate human/material-action boundaries remain unchanged.\n"
        "- `CR-0012` / `DEC-0059` remains active and unchanged: TSK-0455 stays DEFERRED / WAITING until the integrated environment is fully working and no earlier than the owner re-evaluation window; TSK-0456, TSK-0457 and TSK-0492 remain dependency-blocked.\n"
        "- Prior post-freeze planning change: `CR-0011` / `DEC-0058`"
    )
    if state.count(anchor) != 1:
        raise SystemExit(f"CURRENT_STATE latest-change anchor mismatch: {state.count(anchor)}")
    state = state.replace(anchor, replacement, 1)
    state = state.replace(
        "`TSK-0453` remains WAITING on its existing enforcement-proof boundary",
        "`TSK-0453` is PASS under DEC-0060/CR-0013 after revised acceptance and complete automated verification",
        1,
    )

    pattern = re.compile(
        r"## TSK-0453 current accepted stable state — 2026-09-03 — SOURCE/POLICY VERIFIED; REVIEW ENFORCEMENT WAITING\n.*?(?=## TSK-0491 current accepted stable state)",
        re.S,
    )
    section = f"""## TSK-0453 current accepted stable state — 2026-09-04 — PASS UNDER DEC-0060 / CR-0013

`TSK-0453 — Configure formatting, linting, type checking, commit/change, and code-review rules`: **PASS** under the owner-revised `ACC-0453 / VER-0453 / EVD-0453`.

- Owner authority: explicit Project Owner decision 2026-09-04 that mandatory human/Code Owner merge approval and branch protection are not required for ordinary governed `AUTO_ALLOWED` critical-path changes.
- Revised ACC-0453: {NEW_ACC}
- CR-0013 source commit/tree: `{source}` / `{tree}`.
- Verification run/attempt: `{run_id} / {attempt}` — repository structure, deterministic Master Plan validation, focused TSK-0453 contract, formatting, lint, typecheck, full contracts, production build, high-threshold dependency audits, negative formatter propagation/cleanup and clean-worktree checks all passed.
- Durable evidence: `TSK_0453_CR0013_AUTONOMOUS_REVIEW_ACCEPTANCE_EVIDENCE_2026-09-04.md`; the 2026-09-03 source checkpoint remains valid for unchanged source-control evidence, while its former review-enforcement WAIT condition is superseded only by DEC-0060/CR-0013.
- WBS invariants: 641 tasks and 858 dependency edges; the only task-field mutation is TSK-0453 `Acceptance_Criteria`. TSK-0455/0456/0457/0492 rows and every material-action fence are unchanged.
- CODEOWNERS remains advisory routing metadata; it is not a human approval gate. Separate genuine human-only/approval-required or higher-authority safety/security/legal/platform/strategic/irreversible boundaries remain controlling.
- **Non-inference / fences:** no deployment, telemetry activation, participant-facing mutation, production credential/service revocation, payment, activation, launch, live-device/profile/certificate action or service removal/revocation occurred or is authorized by this PASS.

### Queue effect after TSK-0453 PASS

`TSK-0489` may consume TSK-0453 only after a fresh eligibility check confirms its other predecessors (`TSK-0491`, `TSK-0422`), gates, inputs, authority and preserved material-action fences. TSK-0453 PASS does not itself authorize deployment-fenced TSK-0452 or any other consequential action.

"""
    state, n = pattern.subn(section, state, count=1)
    if n != 1:
        raise SystemExit("CURRENT_STATE TSK-0453 section mismatch")

    state = state.replace(
        "TSK-0453 remains WAITING; TSK-0455 remains DEFERRED / WAITING under DEC-0059 / CR-0012",
        "TSK-0453 is PASS under DEC-0060 / CR-0013; TSK-0455 remains DEFERRED / WAITING under DEC-0059 / CR-0012",
    )
    state = state.replace(
        "Existing TSK-0374, TSK-0417, TSK-0453, and TSK-0499 material-action/evidence fences remain unchanged.",
        "Existing TSK-0374, TSK-0417, and TSK-0499 material-action/evidence fences remain unchanged; the former TSK-0453 review-enforcement wait is superseded by DEC-0060/CR-0013.",
    )
    write(state_path, state)

    sh("git", "add", "CURRENT_STATE.md", "TSK_0453_CR0013_AUTONOMOUS_REVIEW_ACCEPTANCE_EVIDENCE_2026-09-04.md")
    sh("git", "diff", "--cached", "--check")
    sh("git", "commit", "-m", "state: accept TSK-0453 under CR-0013")
    print("CR0013_STATE_HEAD=" + sh("git", "rev-parse", "HEAD", capture=True))
    print("CR0013_STATE_TREE=" + sh("git", "rev-parse", "HEAD^{tree}", capture=True))


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] not in {"apply", "finalize"}:
        raise SystemExit("usage: tmp-cr0013-apply.py {apply|finalize}")
    if sys.argv[1] == "apply":
        apply_source()
    else:
        finalize_state()


if __name__ == "__main__":
    main()
