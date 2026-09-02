#!/usr/bin/env python3
import csv
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WBS = ROOT / 'Plans/Master/WBS/master-wbs.csv'
STATE = ROOT / 'CURRENT_STATE.md'
ART = ROOT / 'TSK_0048_DEPENDENCY_ORDERED_VERTICAL_IMPLEMENTATION_BACKLOG_2026-09-02.md'
GEN = ROOT / 'Plans/Master/Tools/generate_tsk0048_vertical_backlog_20260902.py'


def current_pass(state: str, tid: str) -> bool:
    pats=[rf'^##+\s+{re.escape(tid)}\s+current accepted stable state[^\n]*$',rf'^##+\s+{re.escape(tid)}\s+accepted stable state[^\n]*$']
    starts=[]
    for pat in pats: starts += [m.start() for m in re.finditer(pat,state,re.M|re.I)]
    if not starts: return False
    s=max(starts); e=state.find('\n## ',s+3); e=len(state) if e<0 else e
    sec=state[s:e]
    return '**PASS**' in sec or ': **PASS**' in sec or '`: **PASS**' in sec


def req(cond, msg):
    if not cond:
        raise AssertionError(msg)


def main():
    req(ART.exists(), 'backlog artifact missing')
    with WBS.open(encoding='utf-8-sig', newline='') as f:
        rows=list(csv.DictReader(f))
    state=STATE.read_text(encoding='utf-8-sig')
    l6=[r for r in rows if r.get('Lifecycle_Stage')=='L6' and not current_pass(state,r['Task_ID'])]
    expected={r['Task_ID'] for r in l6}
    text=ART.read_text(encoding='utf-8')

    present=re.findall(r'\|\s*\d+\s*\|\s*`(TSK-\d{4})`\s*—',text)
    req(len(present)==len(expected), f'expected {len(expected)} L6 rows, found {len(present)}')
    req(set(present)==expected, f'L6 coverage mismatch missing={sorted(expected-set(present))} extra={sorted(set(present)-expected)}')
    req(len(present)==len(set(present)), 'duplicate task row in backlog')

    order={tid:i for i,tid in enumerate(present)}
    by={r['Task_ID']:r for r in l6}
    for tid,r in by.items():
        deps=[x.strip() for x in (r.get('Dependencies') or '').split(';') if x.strip()]
        for d in deps:
            if d in order:
                req(order[d] < order[tid], f'dependency order violation: {d} must precede {tid}')
        row_match=re.search(rf'^\|\s*\d+\s*\|\s*`{re.escape(tid)}`\s*—.*$',text,re.M)
        req(row_match, f'missing row for {tid}')
        line=row_match.group(0)
        for value,name in [
            (r.get('Primary_Owner'),'owner'),(r.get('Acceptance_ID'),'acceptance id'),(r.get('Verification_ID'),'verification id'),
            (r.get('Action_Authority'),'authority'),(r.get('Plan_Status'),'plan status'),(r.get('Risk_Reference'),'risk reference')]:
            if value:
                req(value in line, f'{tid} missing {name} {value}')
        req('| S |' in line or '| M |' in line, f'{tid} missing derived size')
        req((r.get('Relative_Timing') or 'L6 / dependency-led') in line, f'{tid} missing release target')

    slices=[int(x) for x in re.findall(r'^## Slice (\d+) —',text,re.M)]
    req(slices and slices==list(range(1,len(slices)+1)), 'slice numbering invalid')
    req(all(len(re.findall(r'^\|\s*\d+\s*\|\s*`TSK-',sec,re.M))<=4 for sec in re.split(r'^## Slice \d+ —',text,flags=re.M)[1:]), 'slice exceeds four canonical tasks')

    required_phrases=[
        'accountless core','mandatory login','Google sign-in','parent/device ownership','dashboard/device management',
        'browsing/query/activity history','child accounts','unrestricted customer DNS administration','CR-0009/DEC-0056',
        'Protection Map','AdGuard/DNS','security/privacy negative tests','observability/support/operations','No L6 task is marked PASS',
        'L6 build begins only after LG-07 is actually PASS'
    ]
    lower=text.lower()
    for phrase in required_phrases:
        req(phrase.lower() in lower, f'missing required scope/guardrail phrase: {phrase}')

    # Re-generate from the same canonical inputs and require byte-for-byte determinism.
    before=ART.read_bytes()
    subprocess.run(['python3',str(GEN)],cwd=ROOT,check=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    after=ART.read_bytes()
    req(after==before,'artifact is not byte-for-byte reproducible from current WBS/runtime')

    print(f'PASS: TSK-0048 backlog covers {len(expected)} current non-PASS L6 tasks exactly once in {len(slices)} dependency-ordered slices.')

if __name__=='__main__':
    main()
