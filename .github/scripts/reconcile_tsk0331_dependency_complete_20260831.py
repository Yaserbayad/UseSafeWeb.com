import subprocess
from pathlib import Path

ROOT=Path('.')
RUNTIME=ROOT/'CURRENT_STATE.md'
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
EVIDENCE=ROOT/'TSK_0331_POST_CR0007_DEPENDENCY_COMPLETE_REVALIDATION_EVIDENCE_2026-08-31.md'

EXPECTED_RUNTIME='e43fd43c4cb6d3ac3ae405c10cb04e83d8e30206'
EXPECTED_WBS='f3c29b5db8b835ef2c896f61335656ea51d8ba1c'
EXPECTED_EVIDENCE='3c128d430d2d31998f2e637a292a46ed740464e6'


def blob(path):
    return subprocess.check_output(['git','hash-object',str(path)],text=True).strip()

def req(cond,msg):
    if not cond:
        raise SystemExit(msg)

req(blob(RUNTIME)==EXPECTED_RUNTIME,'TSK0331_CORRECTIVE_RUNTIME_CHANGED')
req(blob(WBS)==EXPECTED_WBS,'TSK0331_CORRECTIVE_WBS_CHANGED')
req(blob(EVIDENCE)==EXPECTED_EVIDENCE,'TSK0331_CORRECTIVE_EVIDENCE_CHANGED')
text=RUNTIME.read_text(encoding='utf-8')
section='## TSK-0331 current accepted stable state — 2026-08-31 — POST-CR-0007'
queue='### Queue status after post-CR-0007 TSK-0331 acceptance'
req(section in text,'TSK0331_CURRENT_SECTION_MISSING')
req(queue in text,'TSK0331_QUEUE_MARKER_MISSING')
req('Corrective dependency-complete revalidation: `TSK_0331_POST_CR0007_DEPENDENCY_COMPLETE_REVALIDATION_EVIDENCE_2026-08-31.md`' not in text,'TSK0331_CORRECTIVE_ALREADY_PRESENT')
insert=(
    '- Corrective dependency-complete revalidation: `TSK_0331_POST_CR0007_DEPENDENCY_COMPLETE_REVALIDATION_EVIDENCE_2026-08-31.md`, '
    'blob `3c128d430d2d31998f2e637a292a46ed740464e6`; final run/job `33429887875 / 99612416336`: SUCCESS after correcting a verifier-only Markdown marker assertion. '
    'Exact product/browser evidence is unchanged; current WBS contract, TSK-0332 + dependency-complete TSK-0334 predecessor proof, ACC artifact semantics, prior target-browser proof, `git diff --check`, and clean-worktree checks PASS. '
    'This corrective evidence governs downstream dependency use of TSK-0331.\n\n'
)
pos=text.index(queue)
text=text[:pos]+insert+text[pos:]
lines=text.splitlines()
for i,line in enumerate(lines):
    if line.startswith('**Updated:**'):
        lines[i]='**Updated:** 2026-08-31T19:19:09Z'
        break
RUNTIME.write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')
print('TSK0331_DEPENDENCY_COMPLETE_RUNTIME_PRECONDITIONS=PASS')
