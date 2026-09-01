import subprocess
from pathlib import Path

EXPECTED_RUNTIME='ff880a1c4853740d7fef48a5fc2fdee4575eb0fe'
EXPECTED={
'content/TSK-0323/DEVICE_SERVICE_INSTRUCTION_CATALOGUE.md':'f848372f7820ed9455fe80668e761bec741423ae',
'content/TSK-0323/CATALOGUE.json':'79753cc4916d38ed8d2f0ed6d01890e62df3fb04',
'TSK_0323_POST_CR0007_CURRENT_REVALIDATION_EVIDENCE_2026-09-01.md':'da2905815860f4586e24a53c1417008940103d92',
'.github/scripts/verify_tsk0323_post_cr0007_compatibility_20260901.py':'5a66a6b05f7358b27c2ffffd8ec365522f9a2450',
'.github/workflows/verify-tsk0323-post-cr0007-compatibility-20260901.yml':'5894969435f4f103db4767940602c572ffb0f9a2',
}

def blob(p): return subprocess.check_output(['git','rev-parse',f'HEAD:{p}'],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)
req(blob('CURRENT_STATE.md')==EXPECTED_RUNTIME,'TSK0323_RUNTIME_STALE')
for p,h in EXPECTED.items(): req(blob(p)==h,f'TSK0323_ACCEPTED_BLOB_STALE={p}')
path=Path('CURRENT_STATE.md')
text=path.read_text(encoding='utf-8')
heading='## TSK-0323 current accepted stable state — 2026-09-01 — POST-CR-0007'
req(heading not in text,'TSK0323_CURRENT_SECTION_ALREADY_EXISTS')
req('## TSK-0322 current accepted stable state — 2026-09-01 — POST-CR-0007' in text,'TSK0323_CURRENT_DEPENDENCY_MISSING')
section=f'''{heading}

- Runtime state: **PASS**.
- Current WBS contract: L4 / MEDIUM / A3 / `AUTO_ALLOWED`; sole dependency `TSK-0322`; `ACC-0323 / VER-0323 / EVD-0323`.
- Current catalogue: `content/TSK-0323/DEVICE_SERVICE_INSTRUCTION_CATALOGUE.md` version `1.0.1-post-cr0007`, blob `f848372f7820ed9455fe80668e761bec741423ae`.
- Current machine catalogue: `content/TSK-0323/CATALOGUE.json`, blob `79753cc4916d38ed8d2f0ed6d01890e62df3fb04`.
- Current acceptance evidence: `TSK_0323_POST_CR0007_CURRENT_REVALIDATION_EVIDENCE_2026-09-01.md`, blob `da2905815860f4586e24a53c1417008940103d92`.
- Deterministic verification: run/job `33483472503 / 99778062685` — SUCCESS; 12/12 instruction-record semantics unchanged, current dependency/scope/language-policy checks PASS.
- The current update only refreshes source/current-scope compatibility. Accountless core remains mandatory; optional account/dashboard continuity does not alter technical verification truth or physical DNS state.
- Historical 2026-08-29 TSK-0323 evidence remains provenance only and does not outrank this current post-CR-0007 acceptance.
- Non-inference fence: no public publication, production, payment, market activation, human-validation or launch authority is implied by this PASS.'''
path.write_text(text.rstrip()+'\n\n'+section.rstrip()+'\n',encoding='utf-8')
print('TSK0323_PASS_RUNTIME_PRECONDITIONS=PASS')
