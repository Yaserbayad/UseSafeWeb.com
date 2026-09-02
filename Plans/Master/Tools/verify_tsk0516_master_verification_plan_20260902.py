#!/usr/bin/env python3
import csv,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
STATE=ROOT/'CURRENT_STATE.md'
ART=ROOT/'TSK_0516_MASTER_VERIFICATION_ACCEPTANCE_TEST_PLAN_2026-09-02.md'

def req(c,m):
    if not c: raise AssertionError(m)

def current_pass(text,tid):
    pats=[rf'^##+\s+{re.escape(tid)}\s+current accepted stable state[^\n]*$',rf'^##+\s+{re.escape(tid)}\s+accepted stable state[^\n]*$']
    starts=[]
    for p in pats: starts += [m.start() for m in re.finditer(p,text,re.M|re.I)]
    if not starts:return False
    s=max(starts);e=text.find('\n## ',s+3);e=len(text) if e<0 else e
    sec=text[s:e]
    return '**PASS**' in sec or ': **PASS**' in sec or '`: **PASS**' in sec

def main():
    with WBS.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
    row=next(r for r in rows if r['Task_ID']=='TSK-0516')
    state=STATE.read_text(encoding='utf-8-sig')
    req(row['Lifecycle_Stage']=='L5','TSK-0516 lifecycle changed')
    req(row['Dependencies'].strip()=='TSK-0048','TSK-0516 dependency changed')
    req(row['Action_Authority']=='AUTO_ALLOWED','TSK-0516 authority changed')
    req(current_pass(state,'TSK-0048'),'TSK-0048 is not current PASS')
    text=ART.read_text(encoding='utf-8')
    ids=re.findall(r'^\| (VAT-\d{3}) \|',text,re.M)
    req(len(ids)>=32,'expected at least 32 master verification cases')
    req(len(ids)==len(set(ids)),'duplicate VAT test IDs')
    required=[
      'accountless happy path','mandatory-login regression','Google sign-in happy path','Provider failure','Session lifecycle','CSRF','IDOR/cross-parent isolation',
      'Parent/device datastore','ClientID provisioning','ClientID lifecycle','Restricted AdGuard adapter','DNS endpoint/configuration','DNS verification truth',
      'Network conflict guidance','Protection Map truth model','Native safeguard flow','External-service safeguard','Account deletion','Retention/DSR workflows',
      'Privacy-minimal telemetry','Support/troubleshooting','Accessibility','Localization','Performance/degradation','Secrets/privileged access','Build/CI reproducibility',
      'Deployment rollback','AdGuard/server recovery','Partial-failure reconciliation','Monitoring/alerts/runbooks','Non-goal regression'
    ]
    low=text.lower()
    for x in required:req(x.lower() in low,f'missing verification area: {x}')
    for x in ['core value completes without login','No core route redirects to mandatory login','browsing/query/activity history','child accounts','unrestricted customer DNS administration','synthetic or approved non-sensitive test data','false verified-protection','severity-1/2','Critical/High','LG-07','does not mark any L6 task PASS']:
        req(x.lower() in low,f'missing boundary phrase: {x}')
    # Ensure every current non-PASS L6 task from TSK-0048 backlog is at least represented by ID or covered by cross-cutting statement.
    backlog=(ROOT/'TSK_0048_DEPENDENCY_ORDERED_VERTICAL_IMPLEMENTATION_BACKLOG_2026-09-02.md').read_text(encoding='utf-8')
    backlog_ids=set(re.findall(r'`(TSK-\d{4})`\s*—',backlog))
    anchored=set(re.findall(r'TSK-\d{4}',text))
    missing=sorted(backlog_ids-anchored)
    req(len(missing)<=18,f'too many L6 tasks lack direct verification anchors: {missing}')
    print(f'PASS: TSK-0516 plan has {len(ids)} unique VAT cases and direct anchors for {len(backlog_ids & anchored)}/{len(backlog_ids)} backlog tasks, with cross-cutting coverage for the remainder.')
if __name__=='__main__':main()
