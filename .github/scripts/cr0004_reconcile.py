#!/usr/bin/env python3
from pathlib import Path
import csv, io, hashlib, re, subprocess

ROOT = Path('.').resolve()
WBS = ROOT/'Plans/Master/WBS/master-wbs.csv'
VER = ROOT/'Plans/Master/Registers/VERIFICATION_EVIDENCE_ACCEPTANCE.md'
DEC = ROOT/'Plans/Master/Registers/DECISIONS_TRIGGERS.md'
CR = ROOT/'Plans/Master/Registers/EXCEPTIONS_CHANGE_CONTROLS.md'
L5 = ROOT/'Plans/Master/Layers/LAYER_5_AI_EXECUTION_EVIDENCE_STATE_CONTROL.md'
MAN = ROOT/'Plans/Master/MANIFEST.yaml'
REL = ROOT/'Plans/Master/RELATIONSHIP_INDEX.yaml'
SUMS = ROOT/'Plans/SHA256SUMS.txt'
EVIDENCE = ROOT/'CR_0004_PROVISIONAL_L4_BRAND_UX_DECOUPLING_EVIDENCE_2026-08-29.md'

ACC298_OLD = 'Brief is traceable to validated customer/product evidence and non-surveillance/claims constraints; it is approved before identity finalization.'
ACC298_NEW = 'Brief is traceable to current accepted customer/product evidence and non-surveillance/claims constraints; missing representative-parent behavioral validation is explicit under RSK-0002; it is approved before identity finalization and does not imply behavioral validation.'
ACC299_OLD = 'Verbal system is clear to normal parents, child-aware, non-alarmist, non-technical, legally/claims reviewed, and reusable across surfaces/locales.'
ACC299_NEW = 'Verbal system follows plain-language, child-aware, non-alarmist, non-technical design rules for parent-facing use, conforms to current approved claims/non-surveillance constraints, and is reusable across surfaces/locales; representative-parent comprehension and legal completion remain unproven and are not implied.'

def run(*args, capture=False):
    return subprocess.run(args, cwd=ROOT, check=True, text=True, capture_output=capture)

def blob(path):
    return run('git','hash-object',str(path),capture=True).stdout.strip()

def insert_after_table_row(text, marker, new_row):
    pos = text.index(marker)
    line_end = text.index('\n', pos) + 1
    return text[:line_end] + new_row + text[line_end:]

# Exact durable planning prestate; workflow-only commits are allowed but no Plans/runtime drift is.
assert blob('CURRENT_STATE.md') == '46185aaff2bf30a8fc33a1aabbabb3845258226e'
assert blob('Plans/Master/MANIFEST.yaml') == '00feca027babfd99dcd1992e3e0abd6ef2d3380b'
assert blob('Plans/Master/WBS/master-wbs.csv') == 'dce5b829c4d447eac180ae1e896e0019292cf971'
assert blob('Plans/Master/RELATIONSHIP_INDEX.yaml') == '42f08784321d216fe77b1baa0ad54aa6f96aa4f7'

# Patch only physical rows TSK-0298 and TSK-0299; preserve all unrelated CSV rows byte-for-byte.
raw = WBS.read_text(encoding='utf-8-sig')
lines = raw.splitlines()
header = next(csv.reader([lines[0]]))
idx = {name:i for i,name in enumerate(header)}
changed = set()
for n, line in enumerate(lines):
    if not (line.startswith('TSK-0298,') or line.startswith('TSK-0299,')):
        continue
    row = next(csv.reader([line]))
    tid = row[idx['Task_ID']]
    if tid == 'TSK-0298':
        assert row[idx['Dependencies']] == 'TSK-0187'
        assert row[idx['Acceptance_Criteria']] == ACC298_OLD
        row[idx['Dependencies']] = 'TSK-0139'
        row[idx['Acceptance_Criteria']] = ACC298_NEW
        row[idx['Notes']] = (row[idx['Notes']] + ' CR-0004/DEC-0051: provisional internal Brand/UX/prototype work now enters through TSK-0139; representative-parent validation remains mandatory at TSK-0187/TSK-0309 and no behavioral validation is implied.').strip()
    else:
        assert row[idx['Acceptance_Criteria']] == ACC299_OLD
        row[idx['Acceptance_Criteria']] = ACC299_NEW
        row[idx['Notes']] = (row[idx['Notes']] + ' CR-0004/DEC-0051: this is provisional internal verbal-system design conformance only; representative-parent comprehension and deferred legal completion are not claimed.').strip()
    out = io.StringIO(newline='')
    csv.writer(out, lineterminator='').writerow(row)
    lines[n] = out.getvalue()
    changed.add(tid)
assert changed == {'TSK-0298','TSK-0299'}
WBS.write_text('\n'.join(lines)+'\n', encoding='utf-8')

# Synchronize acceptance register.
text = VER.read_text(encoding='utf-8')
assert text.count(ACC298_OLD) == 1
assert text.count(ACC299_OLD) == 1
VER.write_text(text.replace(ACC298_OLD, ACC298_NEW).replace(ACC299_OLD, ACC299_NEW), encoding='utf-8')

# Replace only TSK-0298's dependency edge in relationship locator.
text = REL.read_text(encoding='utf-8')
start = text.index('  TSK-0298:\n')
end = text.index('  TSK-0299:\n', start)
block = text[start:end]
old_edge = '    - target: TSK-0187\n      type: depends_on\n'
new_edge = '    - target: TSK-0139\n      type: depends_on\n'
assert block.count(old_edge) == 1
REL.write_text(text[:start] + block.replace(old_edge, new_edge, 1) + text[end:], encoding='utf-8')

# Persist explicit owner decision DEC-0051.
text = DEC.read_text(encoding='utf-8')
assert '| DEC-0051 |' not in text
DEC_ROW = '| DEC-0051 |  | Provisional L4 Brand/UX/prototype dependency decoupling | ACTIVE OWNER OVERRIDE — remaining internal non-public L4 Brand/UX/prototype definition/design may proceed from the explicit provisional L4 entry bridge without treating representative-parent validation as a predecessor. TSK-0298 depends on TSK-0139 instead of TSK-0187. TSK-0187 remains required behavioral validation and TSK-0309 retains TSK-0187 before usability/comprehension correction or implementation-ready experience freeze. | Explicit Project Owner instruction 2026-08-29; active with DEC-0050 until behavioral reactivation/expiry or later supersession. | Internal artifacts must use current accepted evidence, explicitly carry RSK-0002, and never claim representative-parent comprehension, behavioral validation, deferred legal completion, LG-05/LG-06 PASS, integrated-build authority, publication/payment/launch authority, or other fenced outcome. | Project Owner | TSK-0139; TSK-0187; TSK-0298; TSK-0299; TSK-0300; TSK-0301; TSK-0302; TSK-0309; TSK-0310; LG-05; LG-06; RSK-0002 | Owner instruction 2026-08-29; CR-0004 |\n'
DEC.write_text(insert_after_table_row(text, '| DEC-0050 |', DEC_ROW), encoding='utf-8')

# Persist material change record CR-0004.
text = CR.read_text(encoding='utf-8')
assert '| CR-0004 |' not in text
CR_ROW = '| CR-0004 | 2026-08-29 | WBS dependency/acceptance semantics for provisional internal L4 Brand/UX/prototype work; relationship index; decision register; Layer-5 execution semantics; manifest/change metadata; generated reconstruction/checksums. TSK-0187, TSK-0309, RSK-0002 and all legal/privacy/participant/build/publication/payment/launch gate semantics remain controlling. | Explicit Project Owner approval 2026-08-29 to decouple remaining provisional internal L4 Brand/UX/prototype design from deferred representative-parent behavioral validation while preserving future behavioral validation and all downstream fences. | Replace only the TSK-0298 hard dependency TSK-0187 with the existing provisional L4 entry bridge TSK-0139; rephrase ACC-0298 and ACC-0299 so provisional internal acceptance cannot be mistaken for representative-parent validation or legal completion; keep TSK-0309 -> TSK-0187 unchanged. | Preserves 641 tasks and 849 dependency edges with no cycle. No existing PASS is invalidated because prior evidence semantics are not weakened. The Brand chain may progress provisionally through TSK-0298, TSK-0299 and TSK-0302, then stops at the existing TSK-0301 HUMAN_ONLY identity approval unless separately approved. Prototype creation may later reach TSK-0310, but TSK-0309 and LG-06 remain blocked on real behavioral/usability/comprehension evidence as applicable. | Update the two WBS acceptance rows, one WBS dependency cell, matching acceptance register entries, one relationship edge, DEC-0051, Layer-5 rule and manifest status; rebuild Generated/MASTER_PLAN_FULL.md; regenerate Plans/SHA256SUMS.txt; run full deterministic validation and direct fence assertions; publish/read back; reconcile CURRENT_STATE before relying on new eligibility. | Restore TSK-0298 -> TSK-0187 and prior ACC-0298/ACC-0299 wording; remove DEC-0051/CR-0004/Layer-5/manifest delta; rebuild/checksum/validate; re-evaluate any downstream PASS created solely under CR-0004. | Validator must PASS with 641 tasks, 849 dependency edges, zero cycles/broken links, generated reconstruction complete and checksums valid. Direct audit must prove TSK-0187 unchanged, TSK-0309 still depends on TSK-0187, RSK-0002 remains OPEN, and LG-03/LG-04/LG-05/LG-06 plus L5/L6/participant/legal/publication/payment/launch fences are not satisfied by this change. | Pending bounded GitHub publication/read-back at record creation; runtime evidence must record final commit/blobs before newly eligible work relies on CR-0004. |\n'
CR.write_text(insert_after_table_row(text, '| CR-0003 |', CR_ROW), encoding='utf-8')

# Add narrow execution semantics; do not alter the gate register or risk state.
text = L5.read_text(encoding='utf-8')
assert '### 5.3.3 Owner-approved provisional L4 Brand/UX/prototype decoupling' not in text
INSERTION = '''### 5.3.3 Owner-approved provisional L4 Brand/UX/prototype decoupling (DEC-0051 / CR-0004)\n\n- Under the same expiry/reactivation boundary as DEC-0050, internal non-public L4 Brand/UX/prototype definition/design whose own acceptance can be satisfied without representative-parent evidence may enter through the explicit provisional L4 bridge `TSK-0139`; `TSK-0298` therefore depends on `TSK-0139` rather than `TSK-0187`.\n- `ACC-0298` and `ACC-0299` use provisional design-conformance semantics only. Plain-language or parent-facing design intent is not observed representative-parent comprehension, and current claims constraints are not deferred legal completion. Every artifact must carry active `RSK-0002` and the missing real-participant evidence limitation.\n- `TSK-0187` remains the mandatory representative-parent behavioral-validation work. `TSK-0309` intentionally retains `TSK-0187` as a hard dependency before correcting from real usability/comprehension evidence or freezing an implementation-ready experience baseline. No synthetic, AI, owner-preference or internal-review evidence may satisfy that behavioral edge.\n- Existing HUMAN_ONLY boundaries remain unchanged. In particular, `TSK-0301` still requires explicit Project Owner approval of one visual identity system when its dependencies are satisfied.\n- This change does not satisfy or bypass `LG-03`, `LG-04`, `LG-05`, `LG-06`, legal/privacy/participant conditions, L5/L6 build gates, public release/publication, payment, market activation or launch authority. It creates no participant-processing authority and no legal/compliance evidence.\n- At behavioral-validation reactivation/expiry, execute current required validation when otherwise authorized and re-evaluate every downstream PASS materially based on provisional assumptions; contradictory real evidence reopens affected work.\n\n'''
marker = '### 5.4 Evidence and PASS rules\n'
assert text.count(marker) == 1
L5.write_text(text.replace(marker, INSERTION + marker, 1), encoding='utf-8')

# Manifest marker: preserve all existing hold/deferral/fence markers.
text = MAN.read_text(encoding='utf-8')
old_status = 'PROVISIONAL_L4_AUTHORIZED / deterministic validation PASS'
new_status = 'PROVISIONAL_L4_AUTHORIZED / OWNER_PROVISIONAL_L4_BRAND_UX_DECOUPLING_2026-08-29 / deterministic validation PASS'
assert text.count(old_status) == 1
MAN.write_text(text.replace(old_status, new_status, 1), encoding='utf-8')

# Rebuild derived full plan.
run('python3','Plans/Master/Tools/rebuild_master_plan.py')

# Recalculate exactly the existing checksum inventory.
out=[]
for line in SUMS.read_text(encoding='utf-8').splitlines():
    if not line.strip():
        continue
    _, relpath = line.split('  ',1)
    p = ROOT/'Plans'/relpath
    out.append(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {relpath}')
SUMS.write_text('\n'.join(out)+'\n', encoding='utf-8')

# Full deterministic validator.
res = run('python3','Plans/Master/Tools/validate_master_plan.py',capture=True)
validation = res.stdout.strip()
print(validation)
for expected in ['VALIDATION PASS','tasks=641','dependency_edges=849','broken_links=0','generated_missing_task_ids=0']:
    assert expected in validation.splitlines(), expected

# Direct semantic/fence assertions.
with WBS.open(encoding='utf-8-sig', newline='') as f:
    rows={r['Task_ID']:r for r in csv.DictReader(f)}
assert rows['TSK-0298']['Dependencies'] == 'TSK-0139'
assert rows['TSK-0187']['Dependencies'] == 'TSK-0146'
assert 'Representative parents can complete the prototype' in rows['TSK-0187']['Acceptance_Criteria']
deps={x.strip() for x in re.split(r'[;,]',rows['TSK-0309']['Dependencies']) if x.strip()}
assert deps == {'TSK-0310','TSK-0187'}, deps
assert rows['TSK-0301']['Action_Authority'] == 'HUMAN_ONLY'
assert rows['TSK-0301']['AI_Capability_A0_A4'] == 'A1'
risk=(ROOT/'Plans/Master/Registers/RISKS.md').read_text(encoding='utf-8')
assert '| RSK-0002 |' in risk and 'Open — explicitly accepted provisional validation risk' in risk
gates=(ROOT/'Plans/Master/Registers/GATES.md').read_text(encoding='utf-8')
assert 'DEC-0050 does not itself satisfy this gate' in gates
assert 'LG-03' in gates and 'LG-04' in gates and 'LG-05' in gates and 'LG-06' in gates
l5=L5.read_text(encoding='utf-8')
for phrase in ['does not satisfy or bypass `LG-03`, `LG-04`, `LG-05`, `LG-06`','`TSK-0309` intentionally retains `TSK-0187`','`TSK-0301` still requires explicit Project Owner approval']:
    assert phrase in l5
# Runtime is deliberately untouched until plan publication/read-back succeeds.
assert blob('CURRENT_STATE.md') == '46185aaff2bf30a8fc33a1aabbabb3845258226e'

# Durable external-to-Plan change evidence with post-change blob identities.
changed_paths = [
    'Plans/Master/WBS/master-wbs.csv',
    'Plans/Master/RELATIONSHIP_INDEX.yaml',
    'Plans/Master/Registers/VERIFICATION_EVIDENCE_ACCEPTANCE.md',
    'Plans/Master/Registers/DECISIONS_TRIGGERS.md',
    'Plans/Master/Registers/EXCEPTIONS_CHANGE_CONTROLS.md',
    'Plans/Master/Layers/LAYER_5_AI_EXECUTION_EVIDENCE_STATE_CONTROL.md',
    'Plans/Master/MANIFEST.yaml',
    'Plans/Master/Generated/MASTER_PLAN_FULL.md',
    'Plans/SHA256SUMS.txt',
]
blob_lines='\n'.join(f'- `{p}` -> `{blob(p)}`' for p in changed_paths)
EVIDENCE.write_text(f'''# CR-0004 — Provisional L4 Brand/UX/prototype dependency decoupling evidence\n\n**Date:** 2026-08-29  \n**Owner authority:** explicit approval to decouple remaining provisional internal L4 Brand/UX/prototype design from deferred representative-parent behavioral validation while preserving TSK-0187/RSK-0002 and all legal, privacy, participant, build, publication, payment and launch fences.\n\n## Impact-analysis outcome\n\n- `TSK-0298 -> TSK-0187` was the inappropriate early behavioral coupling for provisional internal Brand work.\n- It is replaced by `TSK-0298 -> TSK-0139`, the existing explicit provisional L4 owner-authorization bridge.\n- `TSK-0309 -> TSK-0187` is intentionally unchanged because TSK-0309 requires real usability/comprehension evidence before implementation-ready experience freeze.\n- `ACC-0298` and `ACC-0299` now state provisional design-conformance semantics and cannot be read as representative-parent validation or deferred legal completion.\n- `TSK-0187` itself is unchanged and remains representative-parent behavioral validation.\n- `RSK-0002` remains OPEN/critical and unchanged.\n- `TSK-0301` remains A1/HUMAN_ONLY and still requires explicit owner approval of the identity system.\n- LG-03/LG-04/LG-05/LG-06 and all L5/L6, participant, legal, publication, payment, market and launch fences remain unsatisfied/unmodified by CR-0004.\n- No existing PASS is invalidated by this amendment; no prior acceptance proof is weakened or replaced.\n\n## Structural verification\n\n```text\n{validation}\n```\n\n## Post-change planning blob identities before commit\n\n{blob_lines}\n\n## Publication/read-back rule\n\nPlanning evidence is not adopted for execution until this mutation is committed to `main`, exact changed paths/blobs are fetched back, and `CURRENT_STATE.md` is reconciled in a separate confirmed mutation.\n''', encoding='utf-8')

print('CR0004_SEMANTIC_AUDIT=PASS')
