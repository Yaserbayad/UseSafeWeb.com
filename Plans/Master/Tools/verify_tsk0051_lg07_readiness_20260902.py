#!/usr/bin/env python3
import csv,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
STATE=ROOT/'CURRENT_STATE.md'
GATES=ROOT/'Plans/Master/Registers/GATES.md'
ART=ROOT/'TSK_0051_LG07_ARCHITECTURE_DELIVERY_READINESS_DECISION_2026-09-02.md'
BACKLOG=ROOT/'TSK_0048_DEPENDENCY_ORDERED_VERTICAL_IMPLEMENTATION_BACKLOG_2026-09-02.md'

def req(c,m):
    if not c: raise AssertionError(m)

def semantic_text(text):
    text=text.lower().replace('`','').replace('*','').replace('_',' ')
    text=re.sub(r'\s+',' ',text)
    return text

def passed(state,tid):
    pats=[rf'^##+\s+{re.escape(tid)}(?:\s*/[^\n]*)?\s+current accepted stable state[^\n]*$',rf'^##+\s+{re.escape(tid)}(?:\s*/[^\n]*)?\s+accepted stable state[^\n]*$']
    starts=[]
    for p in pats: starts += [m.start() for m in re.finditer(p,state,re.M|re.I)]
    if starts:
        s=max(starts); e=state.find('\n## ',s+3); e=len(state) if e<0 else e
        sec=state[s:e]
        if '**PASS**' in sec or ': **PASS**' in sec or '`: **PASS**' in sec: return True
    return bool(re.search(rf'`{re.escape(tid)}[^`]*`[^\n]*\*\*PASS\*\*',state,re.I))

def main():
    with WBS.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
    by={r['Task_ID']:r for r in rows}
    r=by['TSK-0051']
    req(r['Lifecycle_Stage']=='L5','TSK-0051 lifecycle changed')
    req(r['Dependencies'].strip()=='TSK-0587; TSK-0052; TSK-0049','TSK-0051 dependencies changed')
    req(r['Action_Authority']=='AUTO_ALLOWED' and r['AI_Capability_A0_A4']=='A4','TSK-0051 authority changed')
    req(r['Acceptance_ID']=='ACC-0051' and r['Verification_ID']=='VER-0051' and r['Evidence_ID']=='EVD-0051','TSK-0051 ACC/VER/EVD changed')
    acc=semantic_text(r['Acceptance_Criteria'])
    for x in ['lg-06 has passed','architecture/privacy/security/operations','implementation','test','release','resource evidence','accountless core','optional version-1 account/session/dashboard boundary','no critical blocker']:
        req(x in acc,f'missing current ACC-0051 clause: {x}')

    gates=GATES.read_text(encoding='utf-8-sig').lower()
    lg07=next((line for line in gates.splitlines() if line.startswith('| lg-07 |')),None)
    req(lg07 is not None,'LG-07 gate row missing')
    gate=semantic_text(lg07)
    for x in ['architecture and implementation plan','account/session/data/vendor/privacy/security model','auth/authz/csrf/idor/deletion/recovery','typed adguard integration','measurement','test/recovery','budget','delivery plan','residual risks','project governance / auto allowed','unlocks l6 build only on evidence-complete pass']:
        req(x in gate,f'missing LG-07 gate clause: {x}')

    state=STATE.read_text(encoding='utf-8-sig')
    required_pass=['TSK-0587','TSK-0052','TSK-0049','TSK-0048','TSK-0516','TSK-0047','TSK-0237','TSK-0586','TSK-0539','TSK-0585','TSK-0239','TSK-0485','TSK-0410','TSK-0321','TSK-0232','TSK-0234','TSK-0446','TSK-0518','TSK-0498','TSK-0538']
    missing=[t for t in required_pass if not passed(state,t)]
    req(not missing,'required LG-07 evidence tasks not current PASS: '+','.join(missing))
    req('OWNER_EXTERNAL_SATISFIED' in state and 'TSK-0240' in state,'CR-0009 / TSK-0240 owner-external boundary missing')

    residual=[]
    for row in rows:
        if row.get('Lifecycle_Stage')!='L5' or passed(state,row['Task_ID']): continue
        residual.append(row['Task_ID'])
    req(set(residual)=={'TSK-0050','TSK-0051','TSK-0240'},f'unexpected residual L5 frontier: {residual}')

    art=semantic_text(ART.read_text(encoding='utf-8'))
    for x in [
        'decision candidate: pass',
        'architecture and implementation plan',
        'cp-lg07-01',
        'planned initial integrated implementation checkpoint',
        'accountless core remains complete without login',
        'optional parent-account boundary is implemented',
        'csrf/idor/cross-parent isolation',
        'query/statistics-history suppression',
        'mandatory login, browsing/query/activity history, child accounts and unrestricted customer dns administration remain excluded',
        'approved incremental new development spend without another owner decision: 0',
        'contingency: 0',
        'no unresolved high/critical architecture/control-plan gap',
        'tsk-0050 must then persist the approved baseline/readiness decision',
        'does not claim completed l6 implementation'
    ]:
        req(x in art,f'missing LG-07 decision semantic invariant: {x}')

    backlog=semantic_text(BACKLOG.read_text(encoding='utf-8'))
    for x in [
        'current non-pass l6 tasks represented: 76',
        'dependency-ordered execution slices: 55',
        'preserve the complete accountless core',
        'optional version-1 scope may include google sign-in/server session',
        'slice 30',
        'implement firebase google sign-in and privacy-minimal server session lifecycle',
        'slice 38',
        'implement dashboard shell, empty state and parent-owned device cards',
        'coverage checkpoints required before lg-07'
    ]:
        req(x in backlog,f'backlog/checkpoint semantic evidence missing: {x}')
    req('no unresolved high/critical architecture/control-plan gap within this component' in semantic_text(state),'TSK-0049 no-critical-design-gap evidence missing')
    print('PASS: TSK-0051/LG-07 authoritative contracts, 20 current evidence anchors, residual L5 frontier, integrated checkpoint, risk/cost/legal fences and L6 non-inference verified semantically.')
if __name__=='__main__': main()
