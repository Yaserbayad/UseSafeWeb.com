#!/usr/bin/env python3
from pathlib import Path
import csv
import hashlib
import re
import subprocess

REPO = Path(__file__).resolve().parents[3]
MASTER = REPO / 'Plans/Master'
WBS = MASTER / 'WBS/master-wbs.csv'
L5 = MASTER / 'Layers/LAYER_5_AI_EXECUTION_EVIDENCE_STATE_CONTROL.md'
DECISIONS = MASTER / 'Registers/DECISIONS_TRIGGERS.md'
CHANGES = MASTER / 'Registers/EXCEPTIONS_CHANGE_CONTROLS.md'
MANIFEST = MASTER / 'MANIFEST.yaml'
AUTONOMY = MASTER / 'Governance/AUTONOMY_POLICY.yaml'
AUDIT = REPO / 'CR_0008_ACTION_AUTHORITY_AUDIT_2026-09-01.md'
SHA = REPO / 'Plans/SHA256SUMS.txt'

# Retain only rows whose current task semantics still contain a genuinely nondelegable
# owner/controller/legal/strategic/material-commitment act. Historical/excluded rows are
# preserved as historical authority records rather than rewritten retroactively.
KEEP_HUMAN = {
    'TSK-0027', # legacy readiness decision includes recruitment authorization
    'TSK-0056', # current AC still requires owner cohort/stop-condition signature
    'TSK-0065', # strategic proceed/modify/repeat/pivot/stop decision
    'TSK-0081', # mixed quarterly strategic alternatives include pause/stop
    'TSK-0084', # organizational/entity/contracts/transfers
    'TSK-0085', # named-market expansion authority
    'TSK-0092', # Year-2 strategic direction
    'TSK-0161', # material product-scope reversal decision
    'TSK-0210', # regulated fee/payment act
    'TSK-0217', # accountable controller LIA/DPIA residual-risk approval
    'TSK-0250', # accountable controller final DPIA/LIA/notices approval
    'TSK-0259', # accountable controller production DPIA/LIA approval
    'TSK-0261', # safeguarding/parental-authority/protection-claims policy approval
    'TSK-0292', # strategic pause/pivot/transfer/closure
    'TSK-0568', # current AC explicitly requires owner/legal approval
    'TSK-0587', # development resource/cost envelope can authorize material commitment
    'TSK-0588', # supporter-payment experiment activation decision
    'TSK-0591', # supporter-payment release activation
    'TSK-0599', # launch/Year-1 operating budget approval
    'TSK-0618', # funding/partnership negotiation/commitment decision
}

# A4 is reserved here for converted rows that are objective gates/state publication,
# routine deploy/configure/release/recovery/deletion, or bounded production operations.
# Other converted rows become A3: AI executes the work and reports verified durable evidence.
A4 = {
    'TSK-0009','TSK-0010','TSK-0049','TSK-0051','TSK-0053','TSK-0055',
    'TSK-0067','TSK-0069','TSK-0070','TSK-0071','TSK-0072',
    'TSK-0154','TSK-0155','TSK-0156','TSK-0191','TSK-0254','TSK-0255',
    'TSK-0267','TSK-0268','TSK-0272','TSK-0342','TSK-0392','TSK-0425',
    'TSK-0464','TSK-0468','TSK-0469','TSK-0471','TSK-0474','TSK-0481',
    'TSK-0553','TSK-0554','TSK-0560','TSK-0590','TSK-0600','TSK-0601','TSK-0605',
}

with WBS.open(encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames or []
    rows = list(reader)
for required in ('Task_ID','Action_Authority','AI_Capability_A0_A4'):
    assert required in fields, f'missing WBS field {required}'

before = [dict(r) for r in rows]
human_before = [r for r in rows if (r.get('Action_Authority') or '').strip() in {'HUMAN_ONLY','HUMAN_APPROVAL_REQUIRED'}]
assert len(rows) == 641, len(rows)
assert len(human_before) == 101, len(human_before)

converted = []
retained = []
for r in rows:
    tid = (r.get('Task_ID') or '').strip()
    auth = (r.get('Action_Authority') or '').strip()
    if auth not in {'HUMAN_ONLY','HUMAN_APPROVAL_REQUIRED'}:
        continue
    status = (r.get('Plan_Status') or r.get('Planning_Status') or r.get('Disposition') or '').strip().upper()
    if status in {'COMPLETED_RECORD','NOT_APPLICABLE'} or tid in KEEP_HUMAN:
        retained.append(tid)
        continue
    r['Action_Authority'] = 'AUTO_ALLOWED'
    r['AI_Capability_A0_A4'] = 'A4' if tid in A4 else 'A3'
    converted.append(tid)

# Prove the WBS delta is exactly authority/capability metadata and nothing else.
allowed = {'Action_Authority','AI_Capability_A0_A4'}
for old, new in zip(before, rows):
    assert old.get('Task_ID') == new.get('Task_ID')
    for key in fields:
        if key not in allowed:
            assert old.get(key) == new.get(key), f'unapproved WBS change {old.get("Task_ID")} {key}'
assert len(converted) + len(retained) == 101
assert KEEP_HUMAN.issubset(set(retained)), KEEP_HUMAN - set(retained)

with WBS.open('w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
    writer.writeheader(); writer.writerows(rows)

# Decision register: new owner decision, without rewriting DEC-0054.
dec = DECISIONS.read_text(encoding='utf-8')
assert 'DEC-0054' in dec and 'DEC-0055' not in dec
new_dec = "| DEC-0055 | New | Proportional evidence and delegated action-authority normalization | ACTIVE OWNER DECISION — preserve SERIAL LIGHT, every current acceptance criterion, evidence integrity, security/privacy controls and canonical read-back, while minimizing non-value governance overhead. Use the minimum durable evidence that actually proves each task; separate evidence documents, independent verifiers, marker files, dedicated workflows and derived audits are required only when they materially improve proof, risk control, ambiguity resolution or recovery. Research, analysis, architecture, design, drafting, coding, testing, objective evidence gates and ordinary reversible technical/production work inside frozen scope are AUTO_ALLOWED unless the task contains a genuinely nondelegable human act. Existing artifacts are not reorganized solely for cleanliness. | Explicit Project Owner approval 2026-09-01; effective after CR-0008 canonical publication/read-back. | No acceptance criterion, task scope, dependency or PASS is weakened or inferred. Human boundaries remain for actual legal signatures/attestations, accountable controller approvals where retained, contracts, regulated fees, banking/merchant identity, identity/KYC/consent acts requiring a person, named-market activation, organizational/entity formalization, material/unbudgeted commitments, strategic modify/pivot/pause/stop/transfer/resume and irreversible acts that actually require human authority. | Project Owner | Layer 5 evidence/action authority; all WBS HUMAN_ONLY/HUMAN_APPROVAL_REQUIRED rows; CR-0008 | Explicit Project Owner instruction 2026-09-01; CR-0008 |"
dec = dec.rstrip() + '\n' + new_dec + '\n'
DECISIONS.write_text(dec, encoding='utf-8')

# Change-control record.
chg = CHANGES.read_text(encoding='utf-8')
assert 'CR-0007' in chg and 'CR-0008' not in chg
marker = "\n\nMaterial change records use `CR-xxxx`;"
assert marker in chg
cr = "| CR-0008 | 2026-09-01 | Layer-5 evidence/action-authority semantics; all WBS HUMAN_ONLY/HUMAN_APPROVAL_REQUIRED task metadata; decision register; autonomy projection; manifest status; generated reconstruction/checksums. No task scope/title/acceptance/dependency/gate/plan-status changes. | Explicit Project Owner approval 2026-09-01 to optimize governed execution for correctness and efficiency under DEC-0054/CR-0007 while preserving SERIAL LIGHT, acceptance, evidence integrity, security/privacy and read-back. | Add DEC-0055 proportional-evidence semantics; audit all 101 human-gated rows; preserve only genuine human/accountable boundaries and historical/excluded records; convert delegable work to AUTO_ALLOWED with A3/A4 capability as appropriate. | Reduces ceremonial proof and unnecessary approval waits without weakening any acceptance criterion. Authority change creates no PASS. Existing evidence remains valid only where it still proves unchanged acceptance. | Apply exact WBS authority/capability-only delta; update Layer 5/decision/autonomy projection/manifest; rebuild generated plan/checksums; validate; publish/read back; sync CURRENT_STATE; recompute current L5 frontier. | Revert DEC-0055/CR-0008, Layer-5 delta and WBS authority/capability cells to the immediately prior canonical tree; rebuild/checksum/validate; re-evaluate only work whose execution materially relied on CR-0008. | Deterministic validator PASS; parsed WBS remains 641 rows; every non-authority/capability WBS field byte-semantically unchanged by parsed comparison; all 101 prior human-gated rows explicitly dispositioned as converted or retained; retained human rows match the bounded CR-0008 list; generated/checksums valid; no authority-change-as-PASS inference. | Pending publication/read-back at record creation; final commit/blobs/counts are recorded in CURRENT_STATE and the bounded CR-0008 audit. |"
chg = chg.replace(marker, '\n' + cr + marker, 1)
CHANGES.write_text(chg, encoding='utf-8')

# Layer 5: explicit proportional-evidence and normalized human-boundary rule.
l5 = L5.read_text(encoding='utf-8')
assert '### 5.3.6 Owner autonomy and production-only lifecycle authority (DEC-0054 / CR-0007)' in l5
assert '### 5.3.7 Owner proportional-evidence and authority-normalization rule (DEC-0055 / CR-0008)' not in l5
insert = '''### 5.3.7 Owner proportional-evidence and authority-normalization rule (DEC-0055 / CR-0008)

- Preserve SERIAL LIGHT, every current acceptance criterion, evidence integrity, security/privacy controls, deterministic state semantics and canonical write/read-back verification. Efficiency may reduce ceremony, never proof required by the actual acceptance boundary.
- Use the **minimum durable evidence that actually proves the task**. Prefer an authoritative artifact/source or observed test/result plus its exact version/commit/blob/environment reference and the stable runtime-state update when needed.
- A separate evidence document, independent verifier, marker/autoverify file, dedicated workflow, or derived audit is **not a default requirement**. Create one only when it materially improves independent proof, risk control, ambiguity resolution, reproducibility/recovery, non-idempotent-effect reconciliation, or a security/privacy/production/high-impact acceptance boundary.
- Independent verification remains mandatory whenever the acceptance/risk actually requires independence; proportional evidence must never become producer self-certification for security, privacy, recovery, production behavior, consequential effects, or other material high-risk claims.
- Inside frozen scope, research, analysis, architecture, design, drafting, coding, testing, objective evidence gates, routine reversible deployment/release/rollback/recovery, reporting and ordinary production operations are `AUTO_ALLOWED` when dependencies/gates/preconditions/access are satisfied. `A3` is sufficient for bounded execution plus verified durable evidence; use `A4` where autonomous verification/recovery/state progression is part of the task.
- Preserve human authority only where the **task itself** still contains a genuinely nondelegable act: actual legal signature/attestation, retained accountable-controller approval, contract/partnership commitment, regulated fee, banking/merchant identity, identity/KYC/consent act requiring a person, named official-market activation, organizational/entity formalization, material/unbudgeted commitment, strategic modify/pivot/pause/stop/transfer/resume, or an irreversible act that actually requires human authority. A human-looking historical label alone is not a boundary.
- Historical/excluded rows are not retroactively rewritten solely to make counts look cleaner. No authority reclassification creates task/gate `PASS`, supplies missing evidence, changes scope/acceptance/dependencies, or waives legal/safety/security/platform reality.
- Do not reorganize existing repository artifacts solely for cleanliness. Repository layout work requires separate product/governance value beyond aesthetics.

'''
l5 = l5.replace('### 5.4 Evidence and PASS rules', insert + '### 5.4 Evidence and PASS rules', 1)
L5.write_text(l5, encoding='utf-8')

# Manifest: record latest authoritative amendment without changing routing ownership.
man = MANIFEST.read_text(encoding='utf-8')
assert 'OWNER_AUTONOMY_PRODUCTION_ONLY_CR_0007' in man
if 'OWNER_PROPORTIONAL_EVIDENCE_AUTHORITY_NORMALIZATION_CR_0008' not in man:
    man = man.replace('OWNER_AUTONOMY_PRODUCTION_ONLY_CR_0007', 'OWNER_AUTONOMY_PRODUCTION_ONLY_CR_0007 / OWNER_PROPORTIONAL_EVIDENCE_AUTHORITY_NORMALIZATION_CR_0008', 1)
MANIFEST.write_text(man, encoding='utf-8')

# Rebuild derived autonomy projection from authoritative WBS/Layer 5.
counts_cap = {}
counts_auth = {}
for r in rows:
    c = (r.get('AI_Capability_A0_A4') or '').strip(); a = (r.get('Action_Authority') or '').strip()
    counts_cap[c] = counts_cap.get(c,0)+1
    counts_auth[a] = counts_auth.get(a,0)+1
auto = AUTONOMY.read_text(encoding='utf-8')
for cap in ('A0','A1','A2','A3','A4'):
    auto = re.sub(rf'(?m)^  {cap}: \d+$', f'  {cap}: {counts_cap.get(cap,0)}', auto)
for auth in ('AUTO_ALLOWED','HUMAN_APPROVAL_REQUIRED','HUMAN_ONLY'):
    auto = re.sub(rf'(?m)^  {auth}: \d+$', f'  {auth}: {counts_auth.get(auth,0)}', auto)
auto = re.sub(r'(?m)^human_boundary:.*$', 'human_boundary: DEC-0055/CR-0008 preserves only genuinely nondelegable legal/controller/contract/identity/consent/named-market/organizational/material-commitment/strategic/irreversible human acts; otherwise DEC-0054 autonomy applies with proportional evidence and unchanged acceptance.', auto)
AUTONOMY.write_text(auto, encoding='utf-8')

# Update the one bounded audit artifact with actual disposition evidence.
audit = AUDIT.read_text(encoding='utf-8')
assert '## Final CR-0008 disposition' not in audit
audit += '\n## Final CR-0008 disposition\n\n'
audit += f'- Converted to `AUTO_ALLOWED`: **{len(converted)}** rows.\n'
audit += f'- Retained human-gated: **{len(retained)}** rows.\n'
audit += '- Converted task IDs: ' + ', '.join(f'`{x}`' for x in converted) + '\n'
audit += '- Retained task IDs: ' + ', '.join(f'`{x}`' for x in retained) + '\n'
audit += '- WBS scope/title/acceptance/dependencies/gates/plan status: **unchanged by parsed field comparison**.\n'
audit += '- Authority mutation itself creates **no PASS** and supplies **no missing acceptance evidence**.\n'
AUDIT.write_text(audit, encoding='utf-8')

# Rebuild generated reading view.
subprocess.run(['python3', str(MASTER/'Tools/rebuild_master_plan.py')], check=True, cwd=REPO)

# Refresh every checksum already declared in Plans/SHA256SUMS.txt, preserving list/order.
updated = []
for line in SHA.read_text(encoding='utf-8').splitlines():
    if not line.strip():
        updated.append(line); continue
    old, rel = line.split(None, 1)
    p = REPO/'Plans'/rel.strip()
    assert p.is_file(), p
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    updated.append(f'{h}  {rel.strip()}')
SHA.write_text('\n'.join(updated).rstrip()+'\n', encoding='utf-8')

print(f'CR0008_CONVERTED={len(converted)}')
print(f'CR0008_RETAINED={len(retained)}')
print('CR0008_CONVERTED_IDS=' + ','.join(converted))
print('CR0008_RETAINED_IDS=' + ','.join(retained))
print('CR0008_AUTH_COUNTS=' + repr(counts_auth))
print('CR0008_CAP_COUNTS=' + repr(counts_cap))
