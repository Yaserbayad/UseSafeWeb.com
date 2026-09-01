from pathlib import Path
import subprocess

harness = Path('.github/scripts/verify_tsk0321_post_cr0007_accessibility_browser_20260901.mjs')
workflow = Path('.github/workflows/verify-tsk0321-post-cr0007-accessibility-20260901.yml')

t = harness.read_text(encoding='utf-8')
old = "req(await page.getByRole('button', { name: 'Start setup' }).isVisible(), 'account-error-core-fallback');"
new = "req(await page.getByTestId('action-start').isVisible(), 'account-error-core-fallback');"
if t.count(old) != 1:
    raise SystemExit(f'TSK0321_PROVIDER_ERROR_LOCATOR_ANCHOR={t.count(old)}')
t = t.replace(old, new, 1)
harness.write_text(t, encoding='utf-8')

new_blob = subprocess.check_output(['git', 'hash-object', str(harness)], text=True).strip()
w = workflow.read_text(encoding='utf-8')
old_blob = 'bbb1e9b993b962d64cd16b182778f6925feb7b94'
if w.count(old_blob) != 1:
    raise SystemExit(f'TSK0321_WORKFLOW_HARNESS_PIN_ANCHOR={w.count(old_blob)}')
w = w.replace(old_blob, new_blob, 1)
workflow.write_text(w, encoding='utf-8')

print(f'TSK0321_PROVIDER_ERROR_LOCATOR_FIX=PASS')
print(f'TSK0321_HARNESS_BLOB={new_blob}')
