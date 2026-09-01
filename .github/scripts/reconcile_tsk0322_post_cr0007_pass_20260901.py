import subprocess
from pathlib import Path

R=Path('CURRENT_STATE.md')
EXPECTED_RUNTIME='586a36d156ad05f1bc07298fda8328e9c54de027'
EXPECTED={
'Plans/Master/WBS/master-wbs.csv':'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
'content/TSK-0322/PRODUCT_VOICE_CLAIMS_TERMINOLOGY.md':'9344140b48ec99e0bd14639ac6640b581ee66d9f',
'content/TSK-0322/POLICY.json':'b4d8d144a8aac26114848542729bf2ac4aeee8d6',
'TSK_0322_POST_CR0007_DUAL_MODE_LANGUAGE_ACCEPTANCE_EVIDENCE_2026-09-01.md':'54f0dbd2fbbba93b0eb89b80ddc6ce82cb00f667',
'.github/scripts/verify_tsk0322_dual_mode_policy_20260901.py':'641387eb4d8685ccd4d25438adb58d158886f59f',
'.github/workflows/verify-tsk0322-dual-mode-policy-20260901.yml':'32fbb526422b619279ef9ac49bb51fc32b14a706',
}
def blob(p): return subprocess.check_output(['git','rev-parse',f'HEAD:{p}'],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)
req(blob('CURRENT_STATE.md')==EXPECTED_RUNTIME,'TSK0322_RUNTIME_STALE')
for p,h in EXPECTED.items(): req(blob(p)==h,f'TSK0322_INPUT_STALE={p}')
text=R.read_text(encoding='utf-8')
req('## TSK-0322 current accepted stable state — 2026-09-01 — POST-CR-0007' not in text,'TSK0322_ALREADY_CURRENT')
req('## TSK-0327 current accepted stable state — 2026-09-01 — POST-CR-0007' in text and 'version `2.1.0-post-cr0007`' in text,'TSK0322_CURRENT_DEP_MISSING')
section='''

## TSK-0322 current accepted stable state — 2026-09-01 — POST-CR-0007

`TSK-0322`: **PASS** under current `ACC-0322 / VER-0322 / EVD-0322`, `DEC-0053/CR-0006`, and `DEC-0054/CR-0007`.

- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, dependency `TSK-0327`, A4 / `AUTO_ALLOWED`; current TSK-0327 v2.1 is durable PASS.
- Historical pre-CR-0006 language policy is superseded where it said no account/dashboard product existed. Current dual-mode guide: `content/TSK-0322/PRODUCT_VOICE_CLAIMS_TERMINOLOGY.md`, version `2.0.0-post-cr0007`, blob `9344140b48ec99e0bd14639ac6640b581ee66d9f`.
- Current machine policy: `content/TSK-0322/POLICY.json`, schema `usesafeweb.product-language-policy.v2`, version `2.0.0-post-cr0007`, blob `b4d8d144a8aac26114848542729bf2ac4aeee8d6`.
- Durable evidence: `TSK_0322_POST_CR0007_DUAL_MODE_LANGUAGE_ACCEPTANCE_EVIDENCE_2026-09-01.md`, blob `54f0dbd2fbbba93b0eb89b80ddc6ce82cb00f667`.
- Deterministic run/job `33479775242 / 99766584019`: SUCCESS; WBS, current predecessor context, guide semantics, machine policy, identity and endpoint fences all PASS. Earlier run `33479719170 / 99766406951` was verifier-only phrase matching and changed no content/runtime.
- Visible brand remains exactly `SafeWeb`; `UseSafeWeb.com` remains domain/project identity and lowercase technical endpoints remain exact.
- Core setup/verification/help/recovery/removal remains usable without login. Optional parent account/session, minimum saved-device persistence, lightweight dashboard/device management and bounded lifecycle copy are permitted inside current Version-1 scope.
- Mandatory login for core, browsing/query/activity history, child accounts/profiles, broad/raw DNS administration, automatic J0/J1-to-account linkage, and technical `Verified` inferred from account/device/dashboard presence remain prohibited.
- Logout, account deletion, saved-record deletion, revoke/unlink, anonymous-state deletion and physical SafeWeb DNS removal remain distinct; unknown destructive results remain uncertain and must not imply success/automatic replay.
- No real-user comprehension, legal, implementation, publication, market or launch PASS is inferred.

### Queue status after current TSK-0322 acceptance

Revalidate TSK-0323 and TSK-0324 against this current language authority before allowing TSK-0321 dependency use.
'''
R.write_text(text.rstrip()+section.rstrip()+'\n',encoding='utf-8')
print('TSK0322_PASS_RUNTIME_PRECONDITIONS=PASS')
