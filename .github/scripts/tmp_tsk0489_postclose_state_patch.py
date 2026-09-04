#!/usr/bin/env python3
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import re

path = Path('CURRENT_STATE.md')
text = path.read_text(encoding='utf-8')
marker = '## TSK-0243 current accepted stable state — 2026-09-04 — ISOLATED TARGET EVIDENCE PARTIAL'
assert text.count(marker) == 1
suffix_before = text[text.index(marker):]
suffix_hash = hashlib.sha256(suffix_before.encode('utf-8')).hexdigest()

old = '''## Queue status after corrected TSK-0489 reconciliation

`TSK-0489` is durable PASS once this exact evidence/checkpoint synchronization passes the repaired exact-head PR gate and is merged/read back on canonical `main`. Preserve the following TSK-0243 partial-evidence state unchanged and recompute the governed frontier only after the synchronization is confirmed.'''
new = '''## Queue status after corrected TSK-0489 reconciliation

`TSK-0489` is **durable PASS**. Final evidence/checkpoint PR #105 used exact source `04eb21a42554da266cfc7f7c376bd7518dfd918a`, passed governed run `33897001306`, retained artifact `9946155707` (`sha256:4c54f273b017c4b2d45f79bfb4b25702455e652af908e804babae9894b0ff546`), and merged as canonical `9bbc3984167d2c33c2eb6649acfb841a2fcc2f78`. On that exact canonical commit, TSK-0489 run `33897190748`, TSK-0491 run `33897190758`, and TSK-0453 run `33897190833` all succeeded.

Two dated read-only diagnostics on the same merge produced unrelated red noise: run `33897190792` failed only `git diff --check` on EVD-0489 Markdown trailing spaces, now normalized; run `33897190818` used a Sept-1 verifier hard-pinned to obsolete WBS blob `eb35f3b10356396c5117e3f47d0b0378953e2157` instead of current blob `142a0d45b381136567d78545f063333f1e74901f`. This post-close hygiene change preserves both workflow definitions in `.github/workflow-archive/tsk0489-postclose/` and retires their active `.github/workflows` entrypoints. Neither red reopens TSK-0489 or changes any planning/material-action authority.

No successor is preselected here. Preserve the following TSK-0243 partial-evidence TODO state unchanged. After this hygiene change passes exact-head governed promotion and canonical read-back, recompute the deterministic eligible frontier from current WBS/graph/checkpoint, strict evidence, gates, constraints, interfaces/risks, action authority and material-action fences.'''

assert text.count(old) == 1
text = text.replace(old, new, 1)
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
text, n = re.subn(r'\*\*Updated:\*\* [^\n]+', f'**Updated:** {stamp}', text, count=1)
assert n == 1
assert text.count(marker) == 1
suffix_after = text[text.index(marker):]
assert hashlib.sha256(suffix_after.encode('utf-8')).hexdigest() == suffix_hash
assert '`TSK-0243` remains `TODO`' in suffix_after
path.write_text(text, encoding='utf-8')
print('TSK0489_POSTCLOSE_STATE_PATCH=PASS')
print(f'TSK0489_PRESERVED_TSK0243_SUFFIX_SHA256={suffix_hash}')
