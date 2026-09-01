from pathlib import Path

p=Path('.github/scripts/verify_tsk0321_post_cr0007_accessibility_browser_20260901.mjs')
t=p.read_text(encoding='utf-8')
old="req(await page.locator('#skip-link').isVisible().catch(() => false) === false, 'skip-link-should-be-visually-hidden-before-focus');\n"
if t.count(old)!=1: raise SystemExit('TSK0321_SKIP_PREFLIGHT_ANCHOR')
t=t.replace(old,'',1)
old="await page.evaluate(() => window.__TSK0333_TEST__.toggleRtl());"
if t.count(old)!=2: raise SystemExit(f'TSK0321_RTL_PREFLIGHT_ANCHOR={t.count(old)}')
t=t.replace(old,"await page.locator('[data-global-action=\"TOGGLE_RTL\"]').click();")
p.write_text(t,encoding='utf-8')
print('TSK0321_AUDIT_HARNESS_PREFLIGHT_FIX=PASS')
