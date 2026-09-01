import csv,re,subprocess,io
from pathlib import Path
ROOT=Path('.')
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
RUNTIME=ROOT/'CURRENT_STATE.md'
with WBS.open(newline='',encoding='utf-8-sig') as f: rows={r.get('Task_ID'):r for r in csv.DictReader(f)}
runtime=RUNTIME.read_text(encoding='utf-8')

def current_pass_marker(tid):
    return f'## {tid} current accepted stable state' in runtime

def historical_pass_marker(tid):
    return f'## {tid} accepted stable state' in runtime

def disposition_pass(tid):
    r=rows[tid]
    return r.get('Plan_Status')=='NOT_APPLICABLE' and r.get('Execution_State')=='PASS'

def show_task(tid):
    r=rows.get(tid); print(f'--- {tid} ---')
    if not r: print('WBS=MISSING'); return
    for k in ('Task_ID','Title','Layer','Priority','Plan_Status','Execution_State','Dependencies','Acceptance_ID','Verification_ID','Evidence_ID','Acceptance_Criteria','AI_Capability_A0_A4','Action_Authority','Gate_Reference','Risk_ID','Requirement_IDs','Interface_IDs','Source_Reference','Notes'):
        print(f'{k}={r.get(k,"")}')
    print('RUNTIME_CURRENT_PASS='+str(current_pass_marker(tid)))
    print('RUNTIME_HISTORICAL_PASS='+str(historical_pass_marker(tid)))
    print('WBS_NOT_APPLICABLE_PASS='+str(disposition_pass(tid)))
    for d in [x.strip() for x in (r.get('Dependencies') or '').split(';') if x.strip()]:
        print(f'DEP_{d}_CURRENT_OR_EXCLUSION_PASS='+str(current_pass_marker(d) or disposition_pass(d)))

def csv_at(rev):
    raw=subprocess.check_output(['git','show',f'{rev}:Plans/Master/WBS/master-wbs.csv'])
    return {r['Task_ID']:r for r in csv.DictReader(io.StringIO(raw.decode('utf-8-sig')))}

chain=['TSK-0145','TSK-0043','TSK-0310','TSK-0187','TSK-0309','TSK-0319','TSK-0331','TSK-0628','TSK-0321','TSK-0052']
for tid in chain: show_task(tid)

pre=csv_at('40a5e4612e08b25ac63dd9e63b142eec1179b877^')
post=csv_at('40a5e4612e08b25ac63dd9e63b142eec1179b877')
print('CR0006_CHAIN_CONTRACT_DELTAS_BEGIN')
for tid in chain:
    changed=[]
    for k in ('Title','Dependencies','Acceptance_Criteria','Plan_Status','Execution_State','AI_Capability_A0_A4','Action_Authority','Notes'):
        if pre[tid].get(k)!=post[tid].get(k): changed.append(k)
    print(f'{tid}|'+(';'.join(changed) if changed else 'NONE'))
print('CR0006_CHAIN_CONTRACT_DELTAS_END')

print('ELIGIBILITY_SNAPSHOT_BEGIN')
for tid in chain:
    r=rows[tid]
    deps=[x.strip() for x in (r.get('Dependencies') or '').split(';') if x.strip()]
    deps_ok=all(current_pass_marker(d) or disposition_pass(d) for d in deps)
    print('|'.join([tid,r.get('Priority') or '',r.get('AI_Capability_A0_A4') or '',r.get('Action_Authority') or '',str(current_pass_marker(tid)),str(disposition_pass(tid)),str(deps_ok)]))
print('ELIGIBILITY_SNAPSHOT_END')
