import subprocess
from pathlib import Path
EXPECTED_RUNTIME='e1c183ee32301a98c4c1c7dd3a4aa59d2d9f074f'
EXPECTED={
'prototype/TSK-0324/UI_COMPONENT_RULES.md':'8747acdf6e0e98f91e8327b7225bd954956aaef1',
'prototype/TSK-0324/COMPONENT_CONTRACT.json':'55bc1d643b6b10ed1dbafce8c0ea3dc7c69f168d',
'TSK_0324_POST_CR0007_DUAL_MODE_UI_COMPONENT_ACCEPTANCE_EVIDENCE_2026-09-01.md':'dcaec6ee9abb946c93e2707e2ca3e135bb44aeb6',
'.github/scripts/verify_tsk0324_post_cr0007_dual_mode_20260901.py':'b7e9fd8db2ba1f889bc1183f5ff21d34e5fc7b37',
'.github/workflows/verify-tsk0324-post-cr0007-dual-mode-20260901.yml':'2433577b2ce7ec6ac7e2cad870ddc75343c04f77',
}
def blob(p): return subprocess.check_output(['git','rev-parse',f'HEAD:{p}'],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)
req(blob('CURRENT_STATE.md')==EXPECTED_RUNTIME,'TSK0324_RUNTIME_STALE')
for p,h in EXPECTED.items(): req(blob(p)==h,f'TSK0324_ACCEPTED_BLOB_STALE={p}')
path=Path('CURRENT_STATE.md'); text=path.read_text(encoding='utf-8')
heading='## TSK-0324 current accepted stable state — 2026-09-01 — POST-CR-0007'
req(heading not in text,'TSK0324_CURRENT_SECTION_ALREADY_EXISTS')
req('## TSK-0322 current accepted stable state — 2026-09-01 — POST-CR-0007' in text,'TSK0324_CURRENT_DEPENDENCY_MISSING')
section=f'''{heading}

- Runtime state: **PASS**.
- Current WBS contract: L4 / MEDIUM / A3 / `AUTO_ALLOWED`; sole dependency `TSK-0322`; `ACC-0324 / VER-0324 / EVD-0324`.
- Current normative UI component contract: `prototype/TSK-0324/UI_COMPONENT_RULES.md` version `1.1.0-post-cr0007`, blob `8747acdf6e0e98f91e8327b7225bd954956aaef1`.
- Current machine projection: `prototype/TSK-0324/COMPONENT_CONTRACT.json`, blob `55bc1d643b6b10ed1dbafce8c0ea3dc7c69f168d`.
- Current acceptance evidence: `TSK_0324_POST_CR0007_DUAL_MODE_UI_COMPONENT_ACCEPTANCE_EVIDENCE_2026-09-01.md`, blob `dcaec6ee9abb946c93e2707e2ca3e135bb44aeb6`.
- Deterministic verification: run/job `33484058318 / 99779915675` — SUCCESS; current WBS/dependency, preserved base accessibility contract, dual-mode component rules, contrast/source classification and TSK-0322 alignment all PASS.
- Shared TSK-0300 token/component sources remain unchanged; current change removes only the stale account/dashboard-navigation prohibition and adds bounded optional-account/session/dashboard/lifecycle accessibility rules.
- Historical 2026-08-29 TSK-0324 evidence remains provenance only and does not outrank this current post-CR-0007 acceptance.
- Non-inference fence: this PASS does not self-certify the HUMAN_ONLY TSK-0321 integrated accessibility review or authorize publication, production, participant processing, payment, market activation or launch.'''
path.write_text(text.rstrip()+'\n\n'+section.rstrip()+'\n',encoding='utf-8')
print('TSK0324_PASS_RUNTIME_PRECONDITIONS=PASS')
