#!/usr/bin/env python3
from pathlib import Path
import csv, io, re, runpy

runpy.run_path('.github/scripts/cr0006_reconcile_v2.py', run_name='__main__')

wbs=Path('Plans/Master/WBS/master-wbs.csv')
ver=Path('Plans/Master/Registers/VERIFICATION_EVIDENCE_ACCEPTANCE.md')
rel=Path('Plans/Master/RELATIONSHIP_INDEX.yaml')

lines=wbs.read_text(encoding='utf-8-sig').splitlines()
header=next(csv.reader([lines[0]])); idx={n:i for i,n in enumerate(header)}
patch={
    'TSK-0333': {
        'Dependencies':'TSK-0335; TSK-0334; TSK-0146; TSK-0331'
    },
    'TSK-0052': {
        'Acceptance_Criteria':'LG-06 passes only if the Version-1 product/non-goals are frozen as a dual-mode baseline: the complete accountless core setup/protection journey remains usable without login, and optional parent account, Google sign-in/session, minimum parent/device ownership persistence, lightweight dashboard/device management, account/device deletion/recovery and associated privacy/security/truth states are included. Requirements, setup/Protection-Map journey, brand/design system, content, accessibility/i18n, self-service and traceability must be internally/automatically accepted to the current L4 contract; mandatory login, browsing/activity history, child accounts and broad DNS administration remain excluded; critical conflicts are resolved. Under DEC-0052 no real-user evidence is required before this gate and none may be inferred.'
    },
    'TSK-0524': {
        'Acceptance_Criteria':'Automated end-to-end tests cover public start -> accountless setup/routing -> native safeguard guidance -> DNS setup/verification -> relevant external-service step -> Protection Map -> recovery/reinstall/remove/clear-state, plus the optional Version-1 sign-in/session/dashboard/device-management/account-deletion paths and critical failures. Tests fail on incorrect state/evidence/privacy, cross-account leakage or any hidden mandatory-login dependency for core value. No browsing/query/activity history is collected or persisted.'
    }
}
rows={}; out=[lines[0]]
for line in lines[1:]:
    row=next(csv.reader([line])); tid=row[idx['Task_ID']]
    if tid in patch:
        for k,v in patch[tid].items(): row[idx[k]]=v
        s=io.StringIO(newline=''); csv.writer(s,lineterminator='').writerow(row); line=s.getvalue()
    rows[tid]={k:row[i] for k,i in idx.items()}
    out.append(line)
wbs.write_text('\n'.join(out)+'\n',encoding='utf-8')

# Keep acceptance audit synchronized for the two changed acceptance rows.
def esc(s): return str(s).replace('|','\\|')
vout=[]; seen=set()
for line in ver.read_text(encoding='utf-8').splitlines():
    m=re.match(r'^\| (TSK-\d{4}) \|',line)
    if m and m.group(1) in {'TSK-0052','TSK-0524','TSK-0333'}:
        tid=m.group(1); r=rows[tid]
        line='| '+' | '.join(map(esc,[tid,r['Verification_ID'],r['Verification_Method'],r['Evidence_ID'],r['Evidence_Required'],r['Acceptance_ID'],r['Acceptance_Criteria'],r['Execution_State']]))+' |'
        seen.add(tid)
    vout.append(line)
assert seen=={'TSK-0052','TSK-0524','TSK-0333'},seen
ver.write_text('\n'.join(vout)+'\n',encoding='utf-8')

# Remove only the candidate-added TSK-0333 -> TSK-0324 relationship edge.
text=rel.read_text(encoding='utf-8')
start=text.index('  TSK-0333:\n')
m=re.search(r'^  [A-Z][A-Z0-9-]*:\n',text[start+1:],re.M); end=(start+1+m.start()) if m else len(text)
block=text[start:end]
needle='    - target: TSK-0324\n      type: depends_on\n'
assert block.count(needle)==1,block
block=block.replace(needle,'',1)
text=text[:start]+block+text[end:]
rel.write_text(text,encoding='utf-8')

print('CR0006_V3_PATCH=PASS')
