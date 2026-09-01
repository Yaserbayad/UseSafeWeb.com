from pathlib import Path
import os

src = Path('.github/scripts/verify_tsk0333_post_cr0007_browser_20260831.mjs')
out = Path(os.environ['RUNNER_TEMP']) / 'tsk0333-safeweb-browser.mjs'
text = src.read_text(encoding='utf-8')
count = text.count('UseSafeWeb')
if count != 1:
    raise SystemExit(f'TSK0333_SAFEWEB_VERIFIER_REPLACEMENT_COUNT={count}')
text = text.replace('UseSafeWeb', 'SafeWeb')
out.write_text(text, encoding='utf-8')
print(f'TSK0333_SAFEWEB_VERIFIER_REPLACEMENTS={count}')
print(f'TSK0333_SAFEWEB_VERIFIER_PATH={out}')
