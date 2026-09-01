import csv,re,subprocess,io
from pathlib import Path
ROOT=Path('.')
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
RUNTIME=ROOT/'CURRENT_STATE.md'
with WBS.open(newline='',encoding='utf-8-sig') as f: rows={r.get('Task_ID'):r for r in csv.DictReader(f)}
runtime=RUNTIME.read_text(encoding='utf-8')

def deps(tid):
    return [x.strip() for x in (rows[tid].get('Dependencies') or '').split(';') if x.strip()]

def current_pass(tid): return f'## {tid} current accepted stable state' in runtime
def historical_pass(tid): return f'## {tid} accepted stable state' in runtime
def exclusion_pass(tid):
    r=rows[tid]
    return r.get('Plan_Status')=='NOT_APPLICABLE' and r.get('Execution_State')=='PASS'

def csv_at(rev):
    raw=subprocess.check_output(['git','show',f'{rev}:Plans/Master/WBS/master-wbs.csv'])
    return {r['Task_ID']:r for r in csv.DictReader(io.StringIO(raw.decode('utf-8-sig')))}
pre6=csv_at('40a5e4612e08b25ac63dd9e63b142eec1179b877^')
post6=csv_at('40a5e4612e08b25ac63dd9e63b142eec1179b877')
pre7=csv_at('c730c8c147e8cb4559ee03c8fe5b8a91429bc2c6^')
post7=csv_at('c730c8c147e8cb4559ee03c8fe5b8a91429bc2c6')
fields=('Title','Dependencies','Acceptance_Criteria','Plan_Status','Execution_State','AI_Capability_A0_A4','Action_Authority','Notes')
def changed(a,b,tid): return ';'.join(k for k in fields if a[tid].get(k)!=b[tid].get(k)) or 'NONE'

# Full hard-dependency closure for LG-06 task.
seen=set()
def walk(tid):
    if tid in seen or tid not in rows: return
    seen.add(tid)
    for d in deps(tid): walk(d)
walk('TSK-0052')

# Stable topological order (predecessors first).
ordered=[]; done=set()
def topo(tid):
    if tid in done:return
    for d in deps(tid):
        if d in seen: topo(d)
    done.add(tid); ordered.append(tid)
topo('TSK-0052')

print(f'CLOSURE_COUNT={len(ordered)}')
print('CLOSURE_SUMMARY_BEGIN')
for tid in ordered:
    r=rows[tid]
    print('|'.join([
        tid,r.get('Priority') or '',r.get('Plan_Status') or '',r.get('Execution_State') or '',
        r.get('AI_Capability_A0_A4') or '',r.get('Action_Authority') or '',
        str(current_pass(tid)),str(historical_pass(tid)),str(exclusion_pass(tid)),
        changed(pre6,post6,tid),changed(pre7,post7,tid),';'.join(deps(tid)) or 'NONE'
    ]))
print('CLOSURE_SUMMARY_END')

print('UNSATISFIED_BY_STRICT_MARKERS_BEGIN')
for tid in ordered:
    if current_pass(tid) or exclusion_pass(tid): continue
    r=rows[tid]
    dep_ok=all(current_pass(d) or exclusion_pass(d) for d in deps(tid))
    print('|'.join([tid,r.get('Priority') or '',r.get('AI_Capability_A0_A4') or '',r.get('Action_Authority') or '',str(historical_pass(tid)),changed(pre6,post6,tid),changed(pre7,post7,tid),str(dep_ok)]))
print('UNSATISFIED_BY_STRICT_MARKERS_END')

# Candidate unchanged historical PASS nodes whose own WBS contract was untouched by CR-0006/7.
print('UNCHANGED_HISTORICAL_CANDIDATES_BEGIN')
for tid in ordered:
    if historical_pass(tid) and not current_pass(tid) and not exclusion_pass(tid) and changed(pre6,post6,tid)=='NONE' and changed(pre7,post7,tid)=='NONE':
        print('|'.join([tid,rows[tid].get('Title') or '',rows[tid].get('Action_Authority') or '', ';'.join(deps(tid)) or 'NONE']))
print('UNCHANGED_HISTORICAL_CANDIDATES_END')

# Print details only for nodes directly on stale frontiers.
frontier={'TSK-0145','TSK-0043','TSK-0310','TSK-0309','TSK-0319','TSK-0628','TSK-0052'}
print('FRONTIER_DETAILS_BEGIN')
for tid in ordered:
    if tid not in frontier: continue
    r=rows[tid]
    for k in ('Task_ID','Title','Priority','Plan_Status','Execution_State','Dependencies','Acceptance_ID','Verification_ID','Evidence_ID','Acceptance_Criteria','AI_Capability_A0_A4','Action_Authority','Source_Reference','Notes'):
        print(f'{tid}:{k}={r.get(k,"")}')
print('FRONTIER_DETAILS_END')
