#!/usr/bin/env python3
import csv,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
STATE=ROOT/'CURRENT_STATE.md'
ART=ROOT/'TSK_0050_LG07_APPROVED_BASELINE_PERSISTENCE_INDEX_2026-09-02.md'

def req(c,m):
    if not c: raise AssertionError(m)

def passed(state,tid):
    pats=[rf'^##+\s+{re.escape(tid)}(?:\s*/[^\n]*)?\s+current accepted stable state[^\n]*$',rf'^##+\s+{re.escape(tid)}(?:\s*/[^\n]*)?\s+accepted stable state[^\n]*$']
    starts=[]
    for p in pats: starts += [m.start() for m in re.finditer(p,state,re.M|re.I)]
    if starts:
        s=max(starts); e=state.find('\n## ',s+3); e=len(state) if e<0 else e
        sec=state[s:e]
        if '**PASS**' in sec or ': **PASS**' in sec or '`: **PASS**' in sec:return True
    return bool(re.search(rf'`{re.escape(tid)}[^`]*`[^\n]*\*\*PASS\*\*',state,re.I))

def main():
    with WBS.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
    r=next(x for x in rows if x['Task_ID']=='TSK-0050')
    req(r['Lifecycle_Stage']=='L5','lifecycle changed')
    req(r['Dependencies'].strip()=='TSK-0051','dependency changed')
    req(r['Action_Authority']=='AUTO_ALLOWED' and r['AI_Capability_A0_A4']=='A3','authority/capability changed')
    req(r['Acceptance_ID']=='ACC-0050' and r['Verification_ID']=='VER-0050' and r['Evidence_ID']=='EVD-0050','ACC/VER/EVD changed')
    acc=r['Acceptance_Criteria'].lower()
    for x in ['all approved artifacts are in version control','references are internally consistent','commit sha and current-state next action are verified','no secrets/participant data are included']:
        req(x in acc,f'missing ACC-0050 clause: {x}')
    state=STATE.read_text(encoding='utf-8-sig')
    req(passed(state,'TSK-0051'),'TSK-0051 not current PASS')
    req('`LG-07 — Architecture, Security, Privacy and Delivery Readiness`: **PASS**' in state,'LG-07 not current PASS')
    text=ART.read_text(encoding='utf-8'); low=text.lower()
    required=[
      'canonical normalized wbs blob','canonical lg-07 gate-register blob','tsk-0051 / lg-07 durable pass state commit','current_state.md remains the only volatile runtime authority',
      'final lg-07 readiness decision','dependency-ordered l6 implementation backlog','master verification and acceptance plan','release/checkpoint/rollback plan','vendor/api/version/price/change monitoring','pre-development infrastructure/operating-cost model','owner-approved resource/cost/tool envelope','security/privacy implementation/control matrix','privacy-safe observability design',
      'wbs remains the sole task/dependency/acceptance authority','gate register remains the sole gate-definition authority','recompute the full l6 eligible frontier','tsk-0454 is tsk-0050\'s direct wbs successor','no password, token, private key, production secret, raw dns query, browsing/activity history, participant record, or other participant data'
    ]
    for x in required:req(x in low,f'missing TSK-0050 persistence invariant: {x}')
    files={
      'TSK_0051_LG07_ARCHITECTURE_DELIVERY_READINESS_DECISION_2026-09-02.md':'f3febe09b804163e47b96a1784512b8b12620628',
      'Plans/Master/Tools/verify_tsk0051_lg07_readiness_20260902.py':'88185897babde6b76c8e49dbead65ac59bbd377b',
      'TSK_0049_LG07_ARCHITECTURE_PRIVACY_SECURITY_OPERATIONS_APPROVAL_COMPONENT_2026-09-02.md':'0e76b305c6ed282457e0da0b11b85eb1ccaf85c5',
      'TSK_0048_DEPENDENCY_ORDERED_VERTICAL_IMPLEMENTATION_BACKLOG_2026-09-02.md':'4463a818d15a9faa4e48363105bce92fe28e3450',
      'TSK_0516_MASTER_VERIFICATION_ACCEPTANCE_TEST_PLAN_2026-09-02.md':'68e1a104339d402550b178506f82a111b3155118',
      'TSK_0047_RELEASE_CHECKPOINT_ROLLBACK_PLAN_2026-09-02.md':'00e4c57b2db0efdd23e213ac2078a435f24f0171',
      'TSK_0237_VENDOR_VERSION_PRICE_TERMS_COMPATIBILITY_MONITORING_TRIGGERS_2026-09-02.md':'4eae7703238a603885da93cf816e61b43726efe1',
      'TSK_0586_PREDEVELOPMENT_INFRASTRUCTURE_OPERATING_COST_BASELINE_2026-09-02.md':'4e244c35ff7b954b88fc38868eab7c084dcbb27f',
      'TSK_0587_OWNER_DECISION_PACKET_2026-09-02.md':'88d3a57e79a69ed07210770a5bbb72e20d8c4dee',
      'TSK_0587_OWNER_APPROVAL_EVIDENCE_2026-09-02.md':'22c035bff361dcea8b915b940db088fcdb1f3931',
      'TSK_0239_SECURITY_PRIVACY_CONTROL_IMPLEMENTATION_VERIFICATION_MATRIX_2026-09-02.md':'674c21b4c169da4fb496617164ad68cfc6527fb4',
      'TSK_0539_PRIVACY_SAFE_LOGS_METRICS_TRACES_DASHBOARDS_ALERTS_2026-09-02.md':'291cd76d5f71fedb98188e6ecd5679c16ea44a98'
    }
    import subprocess
    for rel,expected in files.items():
        p=ROOT/rel
        req(p.is_file(),f'missing approved baseline file: {rel}')
        actual=subprocess.check_output(['git','hash-object',str(p)],cwd=ROOT,text=True).strip()
        req(actual==expected,f'baseline hash drift {rel}: {actual}')
    for forbidden in ['-----begin private key-----','ghp_','github_pat_','sk-proj-','authorization: bearer ','x-api-key:']:
        req(forbidden not in low,f'possible secret material in persistence index: {forbidden}')
    print(f'PASS: TSK-0050 baseline persistence index verifies {len(files)} immutable baseline artifacts, current LG-07 PASS, authority separation, next-action recompute, and no secret/participant-data payload.')
if __name__=='__main__':main()
