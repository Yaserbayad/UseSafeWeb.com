import subprocess
from pathlib import Path

RUNTIME=Path('CURRENT_STATE.md')
EXPECTED_RUNTIME='bb41c616de872a1d8f402295f5b647786b3a3ddc'
EXPECTED={
'Plans/Master/WBS/master-wbs.csv':'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
'brand/identity/TSK-0301/README.md':'b8ffd2ed234465a238558a7b94e56274de49696a',
'prototype/TSK-0333/index.html':'934dc19d00cc9dd32e1ebc20c604373d153d4013',
'prototype/TSK-0333/model.mjs':'fc25e4b1facc303840311e8ce186612eb8799212',
'prototype/TSK-0333/app.mjs':'98659ba74a86d539b89664708bbcb830292486f8',
'prototype/TSK-0333/prototype.css':'6f8af459a0b0b1c9ec132657dfcd7ebff43090b8',
'TSK_0333_SAFEWEB_BRAND_REVALIDATION_EVIDENCE_2026-09-01.md':'f3ea3bf41c38050356a6e9e94aa251b07b35c5f3',
'.github/scripts/verify_tsk0333_safeweb_brand_revalidation_20260901.py':'118336623a93089c8622cbd47e9057da1eb0e845',
'.github/workflows/verify-tsk0333-safeweb-brand-revalidation-20260901.yml':'6d65b6886096a71ed84dc83b8ef5b7ed9d4da796',
}

def blob(p): return subprocess.check_output(['git','rev-parse',f'HEAD:{p}'],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)

req(blob('CURRENT_STATE.md')==EXPECTED_RUNTIME,'TSK0333_SAFEWEB_RUNTIME_STALE')
for p,h in EXPECTED.items(): req(blob(p)==h,f'TSK0333_SAFEWEB_INPUT_STALE={p}')
text=RUNTIME.read_text(encoding='utf-8')
old='## TSK-0333 current accepted stable state — 2026-08-31 — POST-CR-0007'
start=text.find(old); req(start>=0,'TSK0333_OLD_CURRENT_SECTION_MISSING')
end=text.find('\n## ',start+len(old)); req(end>=0,'TSK0333_OLD_CURRENT_SECTION_UNBOUNDED')
new='''## TSK-0333 current accepted stable state — 2026-09-01 — POST-CR-0007\n\n`TSK-0333`: **PASS** under current `ACC-0333 / VER-0333 / EVD-0333`, `DEC-0053/CR-0006`, and `DEC-0054/CR-0007` authority.\n\n- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, MEDIUM, hard dependencies `TSK-0335; TSK-0334; TSK-0146; TSK-0331`, A3 / `AUTO_ALLOWED`; all four direct dependencies remain current durable PASS.\n- Corrected current integrated prototype blobs: `index.html` `934dc19d00cc9dd32e1ebc20c604373d153d4013`; `model.mjs` `fc25e4b1facc303840311e8ce186612eb8799212`; `app.mjs` `98659ba74a86d539b89664708bbcb830292486f8`; `prototype.css` unchanged `6f8af459a0b0b1c9ec132657dfcd7ebff43090b8`.\n- The 2026-08-31 integrated prototype behavior/evidence remains valid for unchanged functionality, but its three pre-correction source blobs are superseded. Current identity authority TSK-0301/TSK-0297 requires visible brand `SafeWeb`; capitalized `UseSafeWeb` is prohibited as a wordmark.\n- Bounded identity correction run/job `33478938540 / 99764031711` changed only 23 capitalized visible-name occurrences across index/model/controller; lowercase `dns.usesafeweb.com` and `https://dns.usesafeweb.com/dns-query` remained unchanged and CSS was untouched. Fix commit `e5ce4b6b9e71b9b06226e1a0b74cdd6a688d107b`.\n- Durable correction evidence: `TSK_0333_SAFEWEB_BRAND_REVALIDATION_EVIDENCE_2026-09-01.md`, blob `f3ea3bf41c38050356a6e9e94aa251b07b35c5f3`.\n- Full identity + regression run/job `33479022852 / 99764278062`: SUCCESS on self-hosted `adguardvm`; exact identity authority, pure substitution, endpoint fence, WBS contract and the full integrated Chromium suite all PASS.\n- Full current paths remain covered: accountless setup/verification, Android/iPhone, Protection Map, false positive/help/removal/recovery, optional Google sign-in/account/session/dashboard/device management, destructive lifecycle uncertainty, replacement, provider/session errors, logout/account delete, responsive/mobile/RTL/accessibility and privacy/no-transport boundaries.\n- Core value remains usable without login; browsing/query/activity history, child accounts/profiles and broad/raw DNS administration remain absent. Account/device/dashboard state never establishes technical `Verified`.\n- One earlier real product defect (configured DNS removal unreachable from the Protection Map) and the later visible-brand defect are both closed with materially different passing browser evidence. Verifier-only failures remain diagnostics, not product failures.\n- `RSK-0002` remains OPEN/non-blocking before L8. No architecture, implementation, participant, gate, release, market, payment or launch PASS is inferred.\n\n### Queue status after SafeWeb brand revalidation\n\nDownstream evidence that pins the superseded TSK-0333 source blobs must be revalidated before dependency use. TSK-0327 is therefore revalidated next; TSK-0322/0323/0324/0321 remain downstream of that evidence chain.\n'''
text=text[:start]+new.rstrip()+text[end:]
RUNTIME.write_text(text.rstrip()+'\n',encoding='utf-8')
print('TSK0333_SAFEWEB_RUNTIME_PRECONDITIONS=PASS')
