#!/usr/bin/env python3
import csv,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
STATE=ROOT/'CURRENT_STATE.md'
ART=ROOT/'TSK_0047_RELEASE_CHECKPOINT_ROLLBACK_PLAN_2026-09-02.md'

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
    row=next(r for r in rows if r['Task_ID']=='TSK-0047')
    state=STATE.read_text(encoding='utf-8-sig')
    req(row['Lifecycle_Stage']=='L5','lifecycle changed')
    req(row['Dependencies'].strip()=='TSK-0516','dependency changed')
    req(row['Action_Authority']=='AUTO_ALLOWED','authority changed')
    req(current_pass(state,'TSK-0516'),'TSK-0516 not current PASS')
    text=ART.read_text(encoding='utf-8'); low=text.lower()
    required=[
      'versioning and change classes','branch and change flow','environment and promotion checkpoints','configuration and data migration rules','test gates','rollback triggers','rollback procedure','evidence retention','release-class authority',
      'cr-0007 / dec-0054','production is the only active lifecycle environment','ci / ephemeral','not mandatory','lg-07 is a prerequisite','accountless core remains usable without login','cross-parent','secrets','deletion/revocation/recovery','dns/adguard','protection map truth','privacy-minimal','severity-1/2','critical/high','fail closed','cr-0009','does not mark lg-07 pass'
    ]
    for x in required:req(x in low,f'missing required release-plan boundary: {x}')
    req('persistent staging or separate pilot lifecycle is **not mandatory**' in low,'CR-0007 no-staging/no-pilot rule not explicit')
    req('no browsing/query/activity history' in low,'non-goal privacy rule missing')
    print('PASS: TSK-0047 release/checkpoint/rollback plan satisfies current WBS and CR-0007/CR-0009 boundaries.')
if __name__=='__main__':main()
