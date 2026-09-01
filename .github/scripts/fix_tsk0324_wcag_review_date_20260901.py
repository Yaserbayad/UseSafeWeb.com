import subprocess
from pathlib import Path
P=Path('prototype/TSK-0324/UI_COMPONENT_RULES.md')
EXPECTED='edacbd570543df2c823ff869d344c7c2147d9883'
def blob(p): return subprocess.check_output(['git','rev-parse',f'HEAD:{p}'],text=True).strip()
if blob(str(P)) != EXPECTED: raise SystemExit('TSK0324_MD_STALE')
t=P.read_text(encoding='utf-8')
old='Current WCAG 2.2 AA source baseline reviewed 2026-08-29:'
if t.count(old)!=1: raise SystemExit('TSK0324_WCAG_DATE_ANCHOR')
t=t.replace(old,'Current WCAG 2.2 AA source baseline reviewed 2026-09-01:',1)
P.write_text(t,encoding='utf-8')
print('TSK0324_WCAG_DATE_NORMALIZED=PASS')
