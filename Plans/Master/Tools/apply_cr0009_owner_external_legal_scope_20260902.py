#!/usr/bin/env python3
from pathlib import Path
import hashlib
import subprocess

REPO = Path(__file__).resolve().parents[3]
MASTER = REPO / 'Plans/Master'
DECISIONS = MASTER / 'Registers/DECISIONS_TRIGGERS.md'
CHANGES = MASTER / 'Registers/EXCEPTIONS_CHANGE_CONTROLS.md'
L5 = MASTER / 'Layers/LAYER_5_AI_EXECUTION_EVIDENCE_STATE_CONTROL.md'
MANIFEST = MASTER / 'MANIFEST.yaml'
WBS = MASTER / 'WBS/master-wbs.csv'
GRAPH = MASTER / 'RELATIONSHIP_INDEX.yaml'
SHA = REPO / 'Plans/SHA256SUMS.txt'
EVIDENCE = REPO / 'CR_0009_OWNER_EXTERNAL_LEGAL_SCOPE_EVIDENCE_2026-09-02.md'


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

wbs_before = digest(WBS)
graph_before = digest(GRAPH)

# 1) Record the latest owner decision without rewriting task definitions or dependency edges.
dec = DECISIONS.read_text(encoding='utf-8')
assert '| DEC-0055 |' in dec
assert '| DEC-0056 |' not in dec
new_dec = (
    '| DEC-0056 | New | Owner-external legal/compliance scope and dependency satisfaction | '
    'ACTIVE OWNER DECISION — all legal, regulatory and compliance analysis, determinations, filings, registrations, representative appointments, regulated-fee determinations/payments, legal approvals, attestations and signatures are outside AI project scope. For governed execution they are treated as OWNER_EXTERNAL_SATISFIED for dependency and gate sequencing, so they do not block technical/product/security/privacy-engineering/delivery work. No legal/compliance fact, conclusion, filing, payment, approval, signature or attestation is claimed or fabricated by the AI. Mixed tasks retain every non-legal acceptance requirement. | '
    'Explicit Project Owner instruction 2026-09-02; supersedes DEC-0036 and DEC-0049/CR-0002 legal-hold timing and preparatory-only restrictions for active sequencing. | '
    'Actual law, safety, security, platform and technical reality remain higher authority. A known prohibition cannot be bypassed, and an external act that inherently requires a person/professional remains external rather than AI-executed. Legal-scope exclusions may never be cited as legal evidence. | '
    'Project Owner | All legal/regulatory/compliance WBS work and legal subcriteria in mixed tasks/gates; Layer 5 execution semantics; LG-07 onward | Explicit Project Owner instruction 2026-09-02; CR-0009 |'
)
DECISIONS.write_text(dec.rstrip() + '\n' + new_dec + '\n', encoding='utf-8')

# 2) Material change record.
chg = CHANGES.read_text(encoding='utf-8')
assert '| CR-0008 |' in chg
assert '| CR-0009 |' not in chg
marker = '\n\nMaterial change records use `CR-xxxx`;'
assert marker in chg
cr = (
    '| CR-0009 | 2026-09-02 | Layer-5 legal-scope dependency/gate semantics; decision register; manifest latest-change metadata; generated reconstruction/checksums; runtime reconciliation. No WBS task scope/title/acceptance/dependency/plan-status or relationship-edge change. | '
    'Explicit current Project Owner instruction that all legal work is outside AI scope, is to be considered done from the AI/project-execution perspective, and must no longer block progression. | '
    'Add DEC-0056 and a deterministic OWNER_EXTERNAL_SATISFIED rule. Supersede DEC-0036 and DEC-0049/CR-0002 timing/preparatory-only restrictions for sequencing. Pure legal/compliance work is never selected by AI; its dependency/gate role is treated as externally satisfied. In mixed work, only the legal/compliance clause is external; all technical, privacy-engineering, security, product, delivery and operational acceptance remains mandatory. | '
    'Removes legal-work waiting from the governed critical path without fabricating legal compliance. Existing task runtime/planning states are not rewritten as legal PASS. Prior technical/security/privacy/product PASS is preserved only where unchanged evidence still proves unchanged acceptance. | '
    'Update decision register, Layer 5 and manifest; create bounded CR-0009 evidence; rebuild generated plan; regenerate declared checksums; run deterministic validator and semantic assertions; publish/read back; reconcile CURRENT_STATE; recompute L5 frontier. | '
    'Explicit owner reversal may restore legal work to AI sequencing; remove DEC-0056/5.3.8, restore DEC-0049 semantics from prior Git history, rebuild/checksum/validate, and re-evaluate work materially reliant on external satisfaction. | '
    'Validator PASS; WBS and relationship-index SHA-256 unchanged; DEC-0056/5.3.8/manifest CR-0009 present; generated/checksums valid; no legal/compliance PASS claim introduced. | '
    'Pending publication/read-back at record creation; final planning commit and runtime reconciliation are recorded in CURRENT_STATE. |'
)
CHANGES.write_text(chg.replace(marker, '\n' + cr + marker, 1), encoding='utf-8')

# 3) Execution semantics. This supersedes the temporary legal-hold exception without deleting history.
l5 = L5.read_text(encoding='utf-8')
assert '### 5.3.7 Owner proportional-evidence and authority-normalization rule (DEC-0055 / CR-0008)' in l5
assert '### 5.3.8 Owner-external legal/compliance scope (DEC-0056 / CR-0009)' not in l5
insert = '''### 5.3.8 Owner-external legal/compliance scope (DEC-0056 / CR-0009)\n\n- Effective **2026-09-02** until explicitly superseded, legal/regulatory/compliance work is outside AI project scope. This rule supersedes the timing and preparatory-only restrictions in Section 5.3.1 / DEC-0049 / CR-0002 for active sequencing; their history remains traceable.\n- A **legal-scope item** is a task or acceptance clause whose primary required outcome is a legal/regulatory/compliance determination, legal assessment/opinion, filing/registration, representative appointment, regulated-fee determination/payment, legal approval, attestation, signature, or equivalent externally accountable legal act. A legacy `OWNER_LEGAL_HOLD_2026-08-27` marker is sufficient to classify that task as legal-scope.\n- Legal-scope items are **OWNER_EXTERNAL_SATISFIED** for governed dependency and gate evaluation. They are not selected or executed by AI and do not block otherwise eligible technical/product/security/privacy-engineering/delivery/operations work. Existing WBS/graph rows remain unchanged for traceability; this semantic treatment is not a task `PASS` and is not legal evidence.\n- For a mixed task or gate, exclude only the legal/regulatory/compliance clause. Every non-legal acceptance boundary remains mandatory, including data minimisation, privacy engineering, security, auth/authz/CSRF/IDOR, deletion/recovery mechanics, vendor technical behavior, architecture, testing, observability, rollback, cost and operational readiness.\n- AI outputs and runtime evidence must never state or imply that a legal obligation was verified, satisfied, waived, exempted, registered, paid, approved, signed or attested merely because DEC-0056 allows sequencing past it. Where material, label the legal portion `owner-external / not verified by AI`.\n- Actual law, safety, security, platform and technical reality remain higher authority. If a known real-world prohibition makes an action impermissible, do not perform it. If a consequential external legal act inherently requires a person/professional, leave that act external; do not fabricate it.\n- No existing technical/product/security/privacy-engineering `PASS` is invalidated solely by this scope change. No new task or gate becomes `PASS` solely because legal work moved outside AI scope; each gate still requires all remaining non-legal acceptance evidence.\n- Reopening legal work for AI sequencing requires a later explicit Project Owner instruction and ordinary change-control/read-back.\n\n'''
L5.write_text(l5.replace('### 5.4 Evidence and PASS rules', insert + '### 5.4 Evidence and PASS rules', 1), encoding='utf-8')

# 4) Manifest latest-change routing metadata.
man = MANIFEST.read_text(encoding='utf-8')
start = man.index('post_freeze_change_control:\n')
end = man.index('\ngenerated_assembly_contract:', start)
new_block = '''post_freeze_change_control:\n  latest_change: CR-0009\n  date: '2026-09-02'\n  status: owner-external legal/compliance scope amendment; legal work is nonblocking for governed sequencing while remaining outside AI evidence claims\n  authority: explicit current Project Owner instruction 2026-09-02; DEC-0056/CR-0009; actual law/safety/security/platform/technical reality remains higher authority\n  affected_scope:\n  - Layer-5 legal-scope dependency and gate-evaluation semantics\n  - all legal/regulatory/compliance work becomes OWNER_EXTERNAL_SATISFIED for project sequencing and is not AI-executed\n  - mixed tasks retain every non-legal acceptance requirement\n  - DEC-0036 and DEC-0049/CR-0002 timing/preparatory-only legal-hold restrictions are superseded for active sequencing\n  - no WBS task definition, acceptance, dependency, plan status, relationship edge or task runtime PASS is created by this change\n  affected_gates:\n  - legal/regulatory/compliance clauses are owner-external and nonblocking from LG-07 onward\n  - all remaining technical, product, security, privacy-engineering, delivery, test, recovery, cost and operations evidence remains mandatory\n  semantic_delta: external legal satisfaction is a sequencing rule only and must never be presented as legal/compliance evidence or a verified legal fact\n  change_record: Registers/EXCEPTIONS_CHANGE_CONTROLS.md#post-freeze-material-change-records\n'''
MANIFEST.write_text(man[:start] + new_block + man[end:], encoding='utf-8')

# 5) Bounded durable evidence for the owner change.
EVIDENCE.write_text(f'''# CR-0009 — Owner-external legal/compliance scope\n\n**Date:** 2026-09-02  \n**Authority:** explicit current Project Owner instruction  \n**Decision:** DEC-0056 / CR-0009\n\n## Exact execution meaning\n\n- Legal/regulatory/compliance work is outside AI project scope and no longer blocks governed sequencing.\n- Pure legal-scope tasks are treated as `OWNER_EXTERNAL_SATISFIED` for dependency/gate evaluation and are not selected by AI.\n- Mixed tasks retain every non-legal acceptance criterion.\n- This is not legal advice, legal verification, compliance evidence, registration/payment/approval evidence, a signature, an attestation, an exemption or a waiver.\n- Actual law, safety, security, platform and technical reality remain higher authority.\n\n## Structural preservation\n\n- WBS SHA-256 before amendment: `{wbs_before}`\n- Relationship-index SHA-256 before amendment: `{graph_before}`\n- CR-0009 intentionally changes neither file.\n\n## Required verification\n\nDeterministic master-plan validation, generated-plan rebuild, declared checksum refresh, Git diff hygiene and exact GitHub publication/read-back are required before CR-0009 is relied on for later work.\n''', encoding='utf-8')

# 6) Rebuild derived reading view and declared checksums.
subprocess.run(['python3', str(MASTER / 'Tools/rebuild_master_plan.py')], check=True, cwd=REPO)
updated = []
for line in SHA.read_text(encoding='utf-8').splitlines():
    if not line.strip():
        updated.append(line)
        continue
    _old, rel = line.split(None, 1)
    p = REPO / 'Plans' / rel.strip()
    assert p.is_file(), p
    updated.append(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {rel.strip()}')
SHA.write_text('\n'.join(updated).rstrip() + '\n', encoding='utf-8')

assert digest(WBS) == wbs_before, 'CR-0009 must not alter WBS'
assert digest(GRAPH) == graph_before, 'CR-0009 must not alter relationship graph'
print('CR0009_WBS_SHA256=' + wbs_before)
print('CR0009_GRAPH_SHA256=' + graph_before)
print('CR0009_APPLIED=1')
