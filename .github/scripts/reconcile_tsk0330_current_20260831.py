from datetime import datetime, timezone
from pathlib import Path
import subprocess

ROOT=Path('.')
RUNTIME=ROOT/'CURRENT_STATE.md'
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
CANDIDATE=ROOT/'design/TSK-0330/PHONE_INTERNET_SERVICES_SETUP_FLOWS_CANDIDATE.md'
OLD_ACCEPT=ROOT/'TSK_0330_PHONE_INTERNET_SERVICES_FLOW_ACCEPTANCE_EVIDENCE_2026-08-29.md'
CURRENT=ROOT/'TSK_0330_POST_CR0007_CURRENT_REVALIDATION_EVIDENCE_2026-08-31.md'
EXPECTED={
 RUNTIME:'7ec16c5099c0a450bcac35da218a70692f51d9af',
 WBS:'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
 CANDIDATE:'07fa10b3fa9b91ddd02f19f5d1c68b15184677a7',
 OLD_ACCEPT:'794e12b56e902270f6d4ef052abaa2d1fba1963b',
 CURRENT:'784c5552bd02f81092d59c6c2fb05a5610208734',
}

def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)
for p,e in EXPECTED.items():
    req(p.exists(),f'TSK0330_RECONCILE_MISSING={p.as_posix()}')
    req(blob(p)==e,f'TSK0330_RECONCILE_BLOB_CHANGED={p.as_posix()}')
text=RUNTIME.read_text(encoding='utf-8')
req('## TSK-0146 current accepted stable state' in text,'TSK0330_DEP_CURRENT_PASS_MISSING')
req('## TSK-0330 accepted stable state — 2026-08-29' in text,'TSK0330_HISTORICAL_RECORD_MISSING')
heading='## TSK-0330 current accepted stable state — 2026-08-31 — POST-CR-0007'
req(heading not in text,'TSK0330_CURRENT_ALREADY_PRESENT')
section='''\n## TSK-0330 current accepted stable state — 2026-08-31 — POST-CR-0007

`TSK-0330 — Design Phone → Internet → Services setup flows`: **PASS** under current `ACC-0330 / VER-0330 / EVD-0330`, the existing Project Owner approval, `DEC-0053/CR-0006`, and `DEC-0054/CR-0007` authority.

- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, MEDIUM, dependency `TSK-0146`, A1 / `HUMAN_ONLY`; TSK-0146 is current durable PASS.
- Existing explicit Project Owner approval `2026-08-29T23:06:35Z`: `APPROVE TSK-0330 PHONE INTERNET SERVICES FLOWS` remains bound to the unchanged exact candidate.
- Accepted candidate: `design/TSK-0330/PHONE_INTERNET_SERVICES_SETUP_FLOWS_CANDIDATE.md`, blob `07fa10b3fa9b91ddd02f19f5d1c68b15184677a7`.
- Original owner-bound acceptance evidence: `TSK_0330_PHONE_INTERNET_SERVICES_FLOW_ACCEPTANCE_EVIDENCE_2026-08-29.md`, blob `794e12b56e902270f6d4ef052abaa2d1fba1963b`; original final run/job `33280241901 / 99174073706`: SUCCESS.
- Current revalidation evidence: `TSK_0330_POST_CR0007_CURRENT_REVALIDATION_EVIDENCE_2026-08-31.md`, blob `784c5552bd02f81092d59c6c2fb05a5610208734`.
- Current revalidation run/job `33420018806 / 99579828681`: SUCCESS; exact input blobs, current WBS/ACC, current TSK-0146 dependency, dual-mode scope compatibility, unchanged candidate coverage, and existing human authority all PASS; `git diff --check` and clean-worktree checks passed.
- Current acceptance remains the accountless core Phone → Internet → Services setup contract. Its accountless-first/no-account-introduction boundary is compatible with Version 1's optional account/dashboard because core setup remains fully usable without login.
- Android/iPhone exact DNS routes, parent-confirmation/system-verification separation, unsupported/conflict/troubleshooting/removal behavior, independent Protection Map layers, zero-service validity, and truthful completion remain accepted.
- No TSK-0334/TSK-0335/TSK-0331/TSK-0333/LG-06 PASS is inferred by this revalidation. Downstream tasks require current dependency-aware verification.
- `RSK-0002` remains OPEN/non-blocking before L8.

### Queue status after current TSK-0330 revalidation

Re-evaluate direct successors against this current predecessor proof before treating their earlier post-CR-0007 PASS/evidence as dependency-complete.
'''
text=text.rstrip()+section
now=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
lines=text.splitlines()
for i,line in enumerate(lines):
    if line.startswith('**Updated:**'):
        lines[i]=f'**Updated:** {now}'
        break
RUNTIME.write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')
print('TSK0330_RUNTIME_PRECONDITIONS=PASS')
