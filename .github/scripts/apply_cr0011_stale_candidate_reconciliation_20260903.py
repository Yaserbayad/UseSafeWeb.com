#!/usr/bin/env python3
from pathlib import Path
import csv
import hashlib
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
MASTER = ROOT / "Plans" / "Master"
WBS = MASTER / "WBS" / "master-wbs.csv"
REL = MASTER / "RELATIONSHIP_INDEX.yaml"
DECISIONS = MASTER / "Registers" / "DECISIONS_TRIGGERS.md"
CHANGES = MASTER / "Registers" / "EXCEPTIONS_CHANGE_CONTROLS.md"
LAYER5 = MASTER / "Layers" / "LAYER_5_AI_EXECUTION_EVIDENCE_STATE_CONTROL.md"
MANIFEST = MASTER / "MANIFEST.yaml"
MASTER_PLAN = MASTER / "MASTER_PLAN.md"
VALIDATOR = MASTER / "Tools" / "validate_master_plan.py"
SUMS = ROOT / "Plans" / "SHA256SUMS.txt"
EVIDENCE = ROOT / "CR_0011_STALE_CANDIDATE_RECONCILIATION_EVIDENCE_2026-09-03.md"
EXPECTED_BASE = "383fae79fada94279de699aadc885b8778564c04"


def fail(message):
    raise SystemExit("CR0011_FAIL: " + message)


def run(*args):
    return subprocess.run(args, cwd=ROOT, text=True, check=True, capture_output=True).stdout


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def base_bytes(path):
    rel = path.relative_to(ROOT).as_posix()
    return subprocess.run(["git", "show", f"{EXPECTED_BASE}:{rel}"], cwd=ROOT, check=True, capture_output=True).stdout


def insert_after_prefix(path, prefix, row):
    text = path.read_text(encoding="utf-8")
    if row.split(" | ", 2)[0] in text:
        return
    lines = text.splitlines()
    matches = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    if len(matches) != 1:
        fail(f"expected exactly one {prefix!r} row in {path}, found {len(matches)}")
    lines.insert(matches[0] + 1, row)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# The bootstrap commit must be based on the exact recovered canonical main head.
bootstrap_parent = run("git", "rev-parse", "HEAD^").strip()
if bootstrap_parent != EXPECTED_BASE:
    fail(f"bootstrap parent {bootstrap_parent} != expected canonical base {EXPECTED_BASE}")

base_wbs = base_bytes(WBS)
base_rel = base_bytes(REL)
base_wbs_sha256 = sha256_bytes(base_wbs)
base_rel_sha256 = sha256_bytes(base_rel)
if WBS.read_bytes() != base_wbs or REL.read_bytes() != base_rel:
    fail("bootstrap changed WBS or relationship index before CR-0011 application")

# DEC-0058 records the owner's current instruction without importing stale candidate structure.
decision_row = (
    "| DEC-0058 | New | Stale corrected-plan intent reconciliation onto current CR-0010 authority | "
    "ACTIVE OWNER DECISION — use the previously audited stale candidate only as change-intent input. Preserve the current CR-0010 modular authority and all post-CR-0010 owner decisions, task IDs, the 641-task WBS, 858 dependency edges, runtime PASS/evidence and material-action fences. Apply only still-valid corrections; already-satisfied items are preserved/no-op and superseded legacy gate/status/count semantics are not reintroduced. | "
    "Explicit Project Owner authorization 2026-09-03. | CR-0011 audit must prove exact WBS/relationship invariance, validator PASS, zero recurring hard predecessors, derived hierarchy-status semantics, preserved 500-user/geography/domain/tracker controls, and exact canonical read-back. | Project Owner | CR-0011; Layer 5; validator; current planning authority | Explicit Project Owner authorization 2026-09-03; owner-supplied stale corrected candidate |"
)
insert_after_prefix(DECISIONS, "| DEC-0057 |", decision_row)

# CR-0011 is a controlled reconciliation/hardening change, not a plan replacement.
change_row = (
    "| CR-0011 | Project Owner | 2026-09-03 | Reconcile the intended corrections from the stale audited candidate onto the current CR-0010 modular authority without importing its obsolete 502-task/849-edge/G-00..G-17 structure. | "
    "Decision register; Layer-5 hierarchy/status and recurring-dependency semantics; deterministic validator; root/manifest latest-change metadata; generated reconstruction/checksums; bounded evidence. WBS rows, 858 dependency edges, relationship index, gates, milestones, requirements, constraints, risks, interfaces, product scope, action authority and runtime task/gate state are unchanged. | "
    "The owner explicitly authorized current-state rebase/reconciliation instead of verbatim stale-candidate publication. Current canonical evidence already implements most candidate corrections; later DEC-0052..DEC-0057 semantics supersede its legacy gate/status model. | "
    "Project Owner DEC-0058; actual safety/legal/security/platform/technical reality remains higher authority. | Add only the missing general invariants, harden validation, document preserved/no-op/superseded dispositions, rebuild generated view/checksums, run full audit, publish exact audited tree, read back, then synchronize CURRENT_STATE without changing runtime PASS/fences. | "
    "Rollback requires a later owner-authorized CR removing DEC-0058/CR-0011 and the Layer-5/validator hardening from this commit; never restore the stale candidate or force-reset history. | Validator must PASS with 641 tasks, 858 dependency edges, zero cycles/orphans/broken links/generated-missing IDs, zero recurring hard predecessors, unchanged WBS and relationship bytes, current 500-user formalisation-only and independent geography controls, TSK-0438 domain-control coverage, derived tracker authority, and all preserved runtime fences. | ACTIVE — publication/read-back and CURRENT_STATE reconciliation must record final commit/blobs; CR-0011 creates no task/gate/milestone PASS and no deployment/participant/telemetry/launch authority. |"
)
insert_after_prefix(CHANGES, "| CR-0010 |", change_row)

# Add the two still-useful candidate invariants to current Layer-5 authority.
layer_text = LAYER5.read_text(encoding="utf-8")
if "## 5.3.9 CR-0011 reconciliation invariants" not in layer_text:
    layer_text = layer_text.rstrip() + """

## 5.3.9 CR-0011 reconciliation invariants

The owner-supplied pre-canonical corrected Master Plan is **change-intent input only**, never a replacement authority. Reconciliation is always against the current manifest-routed modular system and current runtime evidence. Legacy candidate counts, gates, dates, status labels and sequencing are not imported when later canonical decisions supersede them.

### Derived hierarchy roll-up invariant

- WBS task runtime state remains the task-level execution authority; hierarchy/parent completion is a derived reporting view and must never become a second mutable state store.
- A parent/group may be reported complete only when every mandatory current child is `PASS` or is explicitly `NOT_APPLICABLE + PASS` as a verified exclusion. A mandatory child that is `TODO`, `WAITING`, or `BLOCKED` prevents a completed roll-up. Deferred/trigger work must be dispositioned under its governing trigger rather than silently counted complete.
- `NOT_APPLICABLE + PASS` proves exclusion only, never implementation, execution, behavioral evidence, deployment, or satisfaction of a missing direct-predecessor proof requirement.
- No hierarchy roll-up can substitute for direct task acceptance evidence or make a hard predecessor satisfied when the predecessor's own current semantics require direct proof.

### Recurring/event dependency invariant

- A `PLANNED_RECURRING` or event/trigger cadence item must not be used as an ordinary hard `FINISH_TO_START` predecessor because such work has no single terminal completion under its recurring semantics.
- Express recurrence, monitoring and trigger relationships through recurrence/trigger/operating-input fields. If a successor genuinely requires one bounded occurrence to complete, model that occurrence as an independently verifiable bounded task with its own acceptance/evidence and dependency semantics.
- The deterministic validator must reject any current WBS hard dependency whose predecessor is `PLANNED_RECURRING`.

CR-0011 changes no existing task, dependency edge, gate, milestone, runtime PASS, evidence binding or material-action fence; it only makes these invariants explicit and machine-checkable.
"""
    LAYER5.write_text(layer_text, encoding="utf-8")

# Update root authority description without changing product/task semantics.
root_text = MASTER_PLAN.read_text(encoding="utf-8")
old = "through `CR-0010 / DEC-0057`, routed by `MANIFEST.yaml`."
new = "through `CR-0011 / DEC-0058`, routed by `MANIFEST.yaml`."
if old not in root_text and new not in root_text:
    fail("MASTER_PLAN authority-state marker not found")
root_text = root_text.replace(old, new, 1)
needle = "Historical candidate/publication wording is not current authority."
replacement = needle + " The owner-supplied stale corrected-plan candidate reviewed on 2026-09-03 is likewise change-intent input only; CR-0011 records its audited disposition against current canonical authority rather than replacing the modular plan."
if needle in root_text and "CR-0011 records its audited disposition" not in root_text:
    root_text = root_text.replace(needle, replacement, 1)
MASTER_PLAN.write_text(root_text, encoding="utf-8")

# Make CR-0011 the manifest's latest controlled change while preserving CR-0010 as its base.
manifest_text = MANIFEST.read_text(encoding="utf-8")
new_block = """post_freeze_change_control:
  latest_change: CR-0011
  previous_change: CR-0010
  date: '2026-09-03'
  status: owner-approved stale-candidate correction-intent reconciliation and governance-invariant hardening; current CR-0010 task/dependency/runtime semantics preserved
  authority: explicit current Project Owner authorization 2026-09-03 to rebase the intended corrections onto current CR-0010 rather than publish the stale candidate verbatim; DEC-0058/CR-0011; actual law/safety/security/platform/technical reality remains higher authority
  affected_scope:
  - decision/change-control/root/manifest metadata, Layer-5 hierarchy-status and recurring-dependency clarification, deterministic validator, generated reconstruction and checksums
  - no WBS task row, dependency edge, relationship index, gate, milestone, requirement, constraint, risk, interface, product scope, action authority, runtime PASS/evidence or material-action fence changes
  - stale candidate numeric structure, G-00..G-17 sequencing, exact critical-path count and superseded statuses/dates are not adopted
  semantic_delta: parent hierarchy completion is explicitly derived-only; recurring/event cadence work cannot be an ordinary hard predecessor; current canonical equivalents of other candidate corrections are preserved/no-op and superseded items remain superseded
  change_record: Registers/EXCEPTIONS_CHANGE_CONTROLS.md#post-freeze-material-change-records
"""
pattern = r"post_freeze_change_control:\n.*?\ngenerated_assembly_contract:"
if not re.search(pattern, manifest_text, flags=re.S):
    fail("manifest post_freeze_change_control block not found")
manifest_text = re.sub(pattern, new_block + "\ngenerated_assembly_contract:", manifest_text, count=1, flags=re.S)
status_old = " / OWNER_STRUCTURAL_NORMALIZATION_CR_0010"
status_new = status_old + " / OWNER_STALE_CANDIDATE_RECONCILIATION_CR_0011"
if status_new not in manifest_text:
    if status_old not in manifest_text:
        fail("manifest source-plan status marker for CR-0010 not found")
    manifest_text = manifest_text.replace(status_old, status_new, 1)
MANIFEST.write_text(manifest_text, encoding="utf-8")

# Harden the permanent validator with the candidate corrections that remain generally valid.
validator_text = VALIDATOR.read_text(encoding="utf-8")
if "# CR-0011 reconciliation invariants" not in validator_text:
    marker = "# publication tree semantics\n"
    if marker not in validator_text:
        fail("validator injection marker not found")
    extra = r'''# CR-0011 reconciliation invariants
recurring_ids={r['Task_ID'] for r in rows if r['Plan_Status']=='PLANNED_RECURRING'}
recurring_hard=[]
for r in rows:
    for d in [x.strip() for x in re.split(r'[;,]',r['Dependencies']) if x.strip()]:
        if d in recurring_ids:
            recurring_hard.append((r['Task_ID'],d))
stats['recurring_hard_predecessors']=len(recurring_hard)
for child,parent in recurring_hard:
    err(f'recurring hard predecessor {child}->{parent}')

decisions_text=(ROOT/'Registers'/'DECISIONS_TRIGGERS.md').read_text(encoding='utf-8')
gates_text=(ROOT/'Registers'/'GATES.md').read_text(encoding='utf-8')
layer5_text=(ROOT/'Layers'/'LAYER_5_AI_EXECUTION_EVIDENCE_STATE_CONTROL.md').read_text(encoding='utf-8')
root_plan_text=(ROOT/'MASTER_PLAN.md').read_text(encoding='utf-8')
manifest_text=MAN.read_text(encoding='utf-8')
if re.search(r'\b100(?:-|\s+)(?:active(?:-|\s+)?)?users?\b', decisions_text+'\n'+gates_text, re.I):
    err('unsupported current 100-user scale trigger present')
if '500-active-user threshold' not in decisions_text or 'internal scale/formalisation review trigger only' not in decisions_text:
    err('500-user formalisation-only control missing')
if 'LG-16' not in decisions_text or 'Official geographic/market expansion' not in decisions_text:
    err('independent geographic-expansion control missing')
if 'TSK-0438' not in by or 'DNS/registrar control and renewal state' not in by['TSK-0438']['Title'] or 'renewal' not in by['TSK-0438']['Acceptance_Criteria'].lower():
    err('direct domain-control verification control missing')
if 'TSK-0012' not in by or 'ClickUp' not in by['TSK-0012']['Title']:
    err('current ClickUp derived-view control missing')
if 'TSK-0013' not in by or 'Monday' not in by['TSK-0013']['Title']:
    err('current Monday derived-view control missing')
if 'derived_modules_never_authoritative: true' not in manifest_text:
    err('manifest derived-view authority fence missing')
if 'Derived hierarchy roll-up invariant' not in layer5_text:
    err('derived hierarchy roll-up invariant missing')
if 'Recurring/event dependency invariant' not in layer5_text:
    err('recurring/event dependency invariant missing')
if 'CR-0011 / DEC-0058' not in root_plan_text:
    err('root CR-0011 authority marker missing')
stats['cr0011_invariants']='PASS' if not recurring_hard else 'FAIL'

'''
    validator_text = validator_text.replace(marker, extra + marker, 1)
    VALIDATOR.write_text(validator_text, encoding="utf-8")

# Rebuild the derived full-plan view from authoritative modules.
run(sys.executable, str(MASTER / "Tools" / "rebuild_master_plan.py"))

# Regenerate the complete declared Master-tree checksums deterministically.
lines = []
for path in sorted(p for p in MASTER.rglob("*") if p.is_file()):
    digest = sha256_bytes(path.read_bytes())
    rel = path.relative_to(ROOT / "Plans").as_posix()
    lines.append(f"{digest}  {rel}")
SUMS.write_text("\n".join(lines) + "\n", encoding="utf-8")

# Full canonical validation, including the new CR-0011 invariants.
validation = run(sys.executable, str(VALIDATOR))
required_validation = [
    "VALIDATION PASS",
    "tasks=641",
    "dependency_edges=858",
    "broken_links=0",
    "generated_missing_task_ids=0",
    "recurring_hard_predecessors=0",
    "cr0011_invariants=PASS",
]
for token in required_validation:
    if token not in validation:
        fail(f"validator output missing {token!r}:\n{validation}")

# Prove the change did not mutate the current task/dependency or relationship authorities.
after_wbs = WBS.read_bytes()
after_rel = REL.read_bytes()
if after_wbs != base_wbs:
    fail("CR-0011 changed WBS bytes")
if after_rel != base_rel:
    fail("CR-0011 changed relationship-index bytes")

# Independent bounded semantic audit over the current WBS.
with WBS.open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
by = {r["Task_ID"]: r for r in rows}
recurring = {r["Task_ID"] for r in rows if r["Plan_Status"] == "PLANNED_RECURRING"}
recurring_edges = []
for r in rows:
    deps = [x.strip() for x in re.split(r"[;,]", r["Dependencies"]) if x.strip()]
    recurring_edges.extend((r["Task_ID"], d) for d in deps if d in recurring)
if recurring_edges:
    fail("independent audit found recurring hard predecessors: " + repr(recurring_edges))

current_decisions = DECISIONS.read_text(encoding="utf-8")
current_gates = (MASTER / "Registers" / "GATES.md").read_text(encoding="utf-8")
if re.search(r"\b100(?:-|\s+)(?:active(?:-|\s+)?)?users?\b", current_decisions + "\n" + current_gates, re.I):
    fail("independent audit found unsupported current 100-user trigger")
for token in ["DEC-0018", "internal scale/formalisation review trigger only", "DEC-0030", "LG-16", "DEC-0058"]:
    if token not in current_decisions:
        fail(f"independent decision audit missing {token}")
if "TSK-0438" not in by or "renewal" not in by["TSK-0438"]["Acceptance_Criteria"].lower():
    fail("independent domain-control audit failed")
if "ClickUp" not in by["TSK-0012"]["Title"] or "Monday" not in by["TSK-0013"]["Title"]:
    fail("independent derived-tracker audit failed")

wbs_blob = run("git", "hash-object", str(WBS)).strip()
rel_blob = run("git", "hash-object", str(REL)).strip()

# Durable audit evidence. Publication/read-back identity is intentionally completed by runtime reconciliation.
evidence = f"""# CR-0011 — stale corrected-candidate reconciliation evidence

**Date:** 2026-09-03  
**Owner authority:** explicit Project Owner authorization to rebase intended corrections onto current CR-0010 authority instead of publishing the stale candidate verbatim.  
**Recovered canonical base:** `{EXPECTED_BASE}`  
**Stale candidate repository snapshot stated by the supplied candidate:** `87ac767fec2ab44a71f21a6bed0e32f5f05373d2`  
**Preflight comparison:** current base was independently verified as 2,361 commits ahead and 0 behind that stale snapshot before CR-0011 construction.

## Decision

CR-0011 is a bounded reconciliation/invariant-hardening change. The stale candidate is evidence of correction intent only. It does not replace the manifest-routed modular Master Plan, and its 502-task / 849-edge / G-00..G-17 structure is not adopted.

## Candidate correction disposition

| Candidate intent | CR-0011 disposition |
| --- | --- |
| Zero duplicate/orphan/cyclic dependencies | **PRESERVED / already canonical.** Existing deterministic validator remains authoritative and PASS. |
| Recurring tasks must not be hard predecessors | **HARDENED.** Layer 5 now states the invariant and the canonical validator rejects any such edge. Independent audit found **0** recurring hard predecessors. |
| Avoid status/Blocked misuse | **PRESERVED.** Current Layer-5 stable runtime semantics and WBS/runtime separation remain controlling; no blanket status rewrite is introduced. |
| Reduce critical-path inflation / exact old G-02 count | **SUPERSEDED.** Current L0-L13 / LG sequencing and post-candidate owner decisions govern; stale exact count is not imported. |
| Remove unsupported 100-user trigger | **VERIFIED CURRENT INVARIANT.** No current 100-user trigger exists in decision/gate authority. |
| Keep 500 users as organisational/commercial formalisation trigger only | **PRESERVED.** DEC-0018/DEC-0032 remain current; 500 is not treated as a legal threshold. |
| Decouple geographic expansion from 500 users | **PRESERVED.** Current named-market expansion remains independently gated by LG-16/DEC-0030/EXC-0007 semantics. |
| Move legacy G-02/G-03 rehearsal sequencing | **SUPERSEDED.** DEC-0052 and DEC-0054 now govern integrated-product-first and production-only sequencing; old G-02/G-03 logic is not transplanted. |
| Deterministic parent/child roll-up | **HARDENED.** Parent/group completion is explicitly a derived reporting view; task runtime state remains single authority and NOT_APPLICABLE+PASS remains exclusion-only. |
| Deterministic next-task selection | **PRESERVED / already canonical.** Existing Layer-5 selection algorithm remains controlling. |
| Candidate remains noncanonical until controlled publication | **RECONCILED.** DEC-0058/CR-0011 records this controlled current-authority publication path. |
| Remove fabricated exact dates | **PRESERVED.** CR-0011 introduces no fabricated schedule dates. |
| Evidence taxonomy / no unsupported PASS | **PRESERVED.** Current proportional-evidence, direct-proof and read-back rules remain unchanged. |
| Direct DNS/registrar control verification | **PRESERVED.** TSK-0438 remains the current explicit control. |
| Monday/ClickUp are derived views only | **PRESERVED.** TSK-0012/TSK-0013 plus manifest/root authority fences remain current; stale tracker assets cannot override GitHub. |

## Structural/evidence invariance

- WBS SHA-256 before/after: `{base_wbs_sha256}` — **unchanged**.
- WBS Git blob: `{wbs_blob}`.
- Relationship-index SHA-256 before/after: `{base_rel_sha256}` — **unchanged**.
- Relationship-index Git blob: `{rel_blob}`.
- WBS tasks: **641**.
- Hard dependency edges: **858**.
- Recurring hard predecessors: **0**.
- No task ID, task row, dependency edge, gate, milestone, requirement, constraint, risk, interface, product scope, action authority or runtime execution state was changed by CR-0011.

## Full deterministic validation

```text
{validation.strip()}
```

## Preserved current runtime evidence and fences

CR-0011 creates no task/gate/milestone PASS. Existing valid PASS/evidence remains untouched, including TSK-0491 PASS. TSK-0453 remains WAITING on mandatory GitHub review-enforcement proof. TSK-0417 remains non-PASS at its real-target material-action boundary. TSK-0374 and TSK-0499 remain TODO/source-partial where target evidence is incomplete. PR #86 remains draft and unmerged.

No deployment, live-device/profile/certificate action, service removal/revocation, participant processing, telemetry activation, production/public activation, market activation, launch, service-revocation interface/authority, TSK-0374 PASS, TSK-0417 PASS or TSK-0499 PASS is inferred or authorized by this planning reconciliation.

## Publication requirement

This audit proves the candidate tree only. CR-0011 becomes canonically active only after the exact audited branch head is published to `main`, the changed planning files/generated view/checksums are read back and verified, and `CURRENT_STATE.md` is minimally synchronized with the final commit/blob evidence while preserving the runtime state above.
"""
EVIDENCE.write_text(evidence, encoding="utf-8")

# Final sanity checks before the workflow creates the audited commit.
changed = set(run("git", "diff", "--name-only", EXPECTED_BASE).splitlines())
for prohibited in ["Plans/Master/WBS/master-wbs.csv", "Plans/Master/RELATIONSHIP_INDEX.yaml", "Plans/Master/Registers/GATES.md"]:
    if prohibited in changed:
        fail(f"prohibited authority changed: {prohibited}")
run("git", "diff", "--check", EXPECTED_BASE)

# Temporary applicator machinery must not exist in the final CR-0011 tree.
for temp in [
    ROOT / ".github" / "scripts" / "apply_cr0011_stale_candidate_reconciliation_20260903.py",
    ROOT / ".github" / "workflows" / "apply-cr0011-stale-candidate-reconciliation-20260903.yml",
]:
    if temp.exists():
        temp.unlink()

print("CR0011_AUDIT_PASS")
print(f"base={EXPECTED_BASE}")
print(f"wbs_sha256={base_wbs_sha256}")
print(f"relationship_sha256={base_rel_sha256}")
print("tasks=641")
print("dependency_edges=858")
print("recurring_hard_predecessors=0")
