from __future__ import annotations
import csv, io, re, subprocess
from pathlib import Path

ROOT=Path('.')
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
RUNTIME=ROOT/'CURRENT_STATE.md'
CR6='40a5e4612e08b25ac63dd9e63b142eec1179b877'
CR7='c730c8c147e8cb4559ee03c8fe5b8a91429bc2c6'
CHANGE_FIELDS=('Title','Dependencies','Acceptance_Criteria','Plan_Status','Execution_State','AI_Capability_A0_A4','Action_Authority','Notes')

with WBS.open(newline='',encoding='utf-8-sig') as f:
    reader=csv.DictReader(f); fieldnames=reader.fieldnames or []; rows_list=list(reader)
rows={r['Task_ID']:r for r in rows_list}
order={r['Task_ID']:i for i,r in enumerate(rows_list)}
runtime=RUNTIME.read_text(encoding='utf-8')

def csv_at(rev):
    raw=subprocess.check_output(['git','show',f'{rev}:Plans/Master/WBS/master-wbs.csv'])
    return {r['Task_ID']:r for r in csv.DictReader(io.StringIO(raw.decode('utf-8-sig')))}
pre6=csv_at(CR6+'^'); post6=csv_at(CR6); pre7=csv_at(CR7+'^'); post7=csv_at(CR7)

def deps(tid): return [x.strip() for x in (rows[tid].get('Dependencies') or '').split(';') if x.strip()]
def current_pass(tid): return bool(re.search(rf'^##+\s+{re.escape(tid)}(?:\s+/[^\n]+?)?\s+current accepted stable state\b',runtime,re.M))
def historical_pass(tid):
    return bool(re.search(rf'^##+\s+{re.escape(tid)}(?:\s+[^\n]*)?accepted stable state\b',runtime,re.M)) or bool(re.search(rf'^##+\s+{re.escape(tid)}\b[^\n]*\n\n`?{re.escape(tid)}[^\n]*\*\*PASS',runtime,re.M))
def exclusion_pass(tid):
    r=rows[tid]; return r.get('Plan_Status')=='NOT_APPLICABLE' and r.get('Execution_State')=='PASS'
def changed(a,b,tid):
    if tid not in a or tid not in b: return 'ROW_ADDED_OR_REMOVED'
    c=[k for k in CHANGE_FIELDS if a[tid].get(k)!=b[tid].get(k)]
    return ';'.join(c) or 'NONE'
def unchanged_cr67(tid): return changed(pre6,post6,tid)=='NONE' and changed(pre7,post7,tid)=='NONE'
def historical_unchanged_pass(tid): return historical_pass(tid) and not current_pass(tid) and unchanged_cr67(tid)
def legal_hold(tid): return 'OWNER_LEGAL_HOLD_2026-08-27' in ' | '.join(str(v or '') for v in rows[tid].values())
def dep_status(tid):
    if current_pass(tid): return 'CURRENT_PASS'
    if exclusion_pass(tid): return 'EXCLUSION_PASS'
    if historical_unchanged_pass(tid): return 'HISTORICAL_UNCHANGED_PASS'
    if legal_hold(tid): return 'LEGAL_HOLD_CONDITIONAL'
    return 'UNSATISFIED'

def task_runtime_done(tid): return current_pass(tid) or exclusion_pass(tid) or historical_unchanged_pass(tid)

stage_candidates=[]
for k in fieldnames:
    vals=[(r.get(k) or '').strip() for r in rows_list]
    n=sum(bool(re.fullmatch(r'L(?:[0-9]|1[0-3])',v)) for v in vals)
    if n: stage_candidates.append((k,n,sorted({v for v in vals if re.fullmatch(r'L(?:[0-9]|1[0-3])',v)})))
print('FIELDNAMES='+'|'.join(fieldnames))
print('STAGE_FIELD_CANDIDATES='+repr(stage_candidates))
assert len(stage_candidates)==1, stage_candidates
stage_field=stage_candidates[0][0]
print('STAGE_FIELD='+stage_field)

assert '## TSK-0052 / LG-06 current accepted stable state — 2026-09-01 — POST-CR-0007' in runtime
assert current_pass('TSK-0052')

print('DIRECT_SUCCESSORS_OF_TSK0052_BEGIN')
for r in rows_list:
    tid=r['Task_ID']
    if 'TSK-0052' in deps(tid):
        print('|'.join([
            tid,r.get(stage_field) or '',r.get('Priority') or '',r.get('Plan_Status') or '',r.get('Execution_State') or '',
            r.get('AI_Capability_A0_A4') or '',r.get('Action_Authority') or '',r.get('Title') or '',
            ';'.join(f'{d}:{dep_status(d)}' for d in deps(tid)) or 'NONE',
            changed(pre6,post6,tid),changed(pre7,post7,tid)
        ]))
print('DIRECT_SUCCESSORS_OF_TSK0052_END')

l5=[r for r in rows_list if (r.get(stage_field) or '').strip()=='L5']
print(f'L5_TASK_COUNT={len(l5)}')

priority_rank={'CRITICAL':0,'HIGH':1,'MEDIUM':2,'LOW':3}
def key(r): return (priority_rank.get((r.get('Priority') or '').upper(),9),order[r['Task_ID']])

strict=[]; conditional=[]; unsatisfied=[]
for r in l5:
    tid=r['Task_ID']
    if task_runtime_done(tid): continue
    statuses=[(d,dep_status(d)) for d in deps(tid)]
    hard_bad=[x for x in statuses if x[1]=='UNSATISFIED']
    legal=[x for x in statuses if x[1]=='LEGAL_HOLD_CONDITIONAL']
    if not hard_bad and not legal: strict.append(r)
    elif not hard_bad and legal: conditional.append(r)
    else: unsatisfied.append(r)

def emit(label,items):
    print(label+'_BEGIN')
    for r in sorted(items,key=key):
        tid=r['Task_ID']; statuses=[(d,dep_status(d)) for d in deps(tid)]
        print('|'.join([
            tid,r.get('Priority') or '',r.get('Plan_Status') or '',r.get('Execution_State') or '',
            r.get('AI_Capability_A0_A4') or '',r.get('Action_Authority') or '',r.get('Title') or '',
            ';'.join(f'{d}:{s}' for d,s in statuses) or 'NONE',
            changed(pre6,post6,tid),changed(pre7,post7,tid),
            (r.get('Acceptance_ID') or ''),(r.get('Verification_ID') or ''),(r.get('Evidence_ID') or '')
        ]))
    print(label+'_END')
emit('STRICT_CANDIDATES',strict)
emit('CONDITIONAL_LEGAL_CANDIDATES',conditional)
emit('UNSATISFIED_L5',unsatisfied)

print('STRICT_CANDIDATE_DETAILS_BEGIN')
for r in sorted(strict,key=key):
    tid=r['Task_ID']
    for k in ('Task_ID','Title',stage_field,'Priority','Plan_Status','Execution_State','Dependencies','Acceptance_ID','Verification_ID','Evidence_ID','Acceptance_Criteria','AI_Capability_A0_A4','Action_Authority','Source_Reference','Notes'):
        print(f'{tid}:{k}={r.get(k,"")}')
print('STRICT_CANDIDATE_DETAILS_END')

print(f'STRICT_COUNT={len(strict)}')
print(f'CONDITIONAL_LEGAL_COUNT={len(conditional)}')
print(f'UNSATISFIED_COUNT={len(unsatisfied)}')
