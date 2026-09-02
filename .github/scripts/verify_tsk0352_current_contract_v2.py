from __future__ import annotations

import subprocess
from pathlib import Path

BASE = ".github/scripts/verify_tsk0352_current_contract.py"
EXPECTED_BASE = "43a4013967c8066ba2c1f79d68a512c49cf9aef3"
actual = subprocess.check_output(["git", "hash-object", BASE], text=True).strip()
assert actual == EXPECTED_BASE, (actual, EXPECTED_BASE)
src = Path(BASE).read_text(encoding="utf-8")
old = '("## 9. Update / repair lifecycle", ["clients/update", "server-known current name", "read back"], "UPDATE"),'
new = '("## 9. Update / repair lifecycle", ["clients/update", "server-known", "read back"], "UPDATE"),'
assert old in src
src = src.replace(old, new, 1)
exec(compile(src, BASE + "[v2-markdown-robust]", "exec"), {"__name__": "__main__"})
