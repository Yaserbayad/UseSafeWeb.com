from datetime import datetime, timezone
from pathlib import Path
import subprocess

ROOT=Path('.')
RUNTIME=ROOT/'CURRENT_STATE.md'
EVIDENCE=ROOT/'TSK_0334_POST_CR0007_DEPENDENCY_COMPLETE_REVALIDATION_EVIDENCE_2026-08-31.md'
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'

def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)

req(blob(RUNTIME)=='d0fc4fd26949f718e96d8cccb5fc81709569bc71','TSK0334_RECONCILE_RUNTIME_CHANGED')
req(blob(EVIDENCE)=='c61ca9bde3184761ef793d2ae3f80cd4cffe021c','TSK0334_RECONCILE_EVIDENCE_CHANGED')
req(blob(WBS)=='f3c29b5db8b835ef2c896f61335656ea51d8ba1c','TSK0334_RECONCILE_WBS_CHANGED')
text=RUNTIME.read_text(encoding='utf-8')
heading='## TSK-0334 current accepted stable state — 2026-08-31 — POST-CR-0007'
req(heading in text,'TSK0334_CURRENT_SECTION_MISSING')
req('## TSK-0330 current accepted stable state — 2026-08-31 — POST-CR-0007' in text,'TSK0334_CURRENT_DEP_MISSING')
marker='- Corrective dependency-complete revalidation:'
req(marker not in text,'TSK0334_CORRECTION_ALREADY_PRESENT')
start=text.index(heading)
next_heading=text.find('\n## ',start+len(heading))
end=len(text) if next_heading<0 else next_heading
section=text[start:end]
insert='''- Corrective dependency-complete revalidation: `TSK_0334_POST_CR0007_DEPENDENCY_COMPLETE_REVALIDATION_EVIDENCE_2026-08-31.md`, blob `c61ca9bde3184761ef793d2ae3f80cd4cffe021c`; run/job `33420242950 / 99580565616`: SUCCESS after TSK-0330 became current-qualified. Exact artifacts/owner approval are unchanged; WBS contract, current predecessor proof, all eight ACC-0334 categories, owner authority, `git diff --check`, and clean-worktree checks PASS. This corrective evidence governs downstream dependency use of TSK-0334.\n'''
section=section.rstrip()+'\n'+insert
text=text[:start]+section+text[end:]
now=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
lines=text.splitlines()
for i,line in enumerate(lines):
    if line.startswith('**Updated:**'):
        lines[i]=f'**Updated:** {now}'
        break
else:
    raise SystemExit('CURRENT_STATE_UPDATED_FIELD_MISSING')
RUNTIME.write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')
print('TSK0334_DEPENDENCY_COMPLETE_RUNTIME_PRECONDITIONS=PASS')
