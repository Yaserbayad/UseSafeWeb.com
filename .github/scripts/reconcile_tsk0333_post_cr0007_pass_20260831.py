import re, subprocess
from pathlib import Path

ROOT=Path('.')
RUNTIME=ROOT/'CURRENT_STATE.md'
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
GRAPH=ROOT/'Plans/Master/RELATIONSHIP_INDEX.yaml'
INDEX=ROOT/'prototype/TSK-0333/index.html'
MODEL=ROOT/'prototype/TSK-0333/model.mjs'
APP=ROOT/'prototype/TSK-0333/app.mjs'
CSS=ROOT/'prototype/TSK-0333/prototype.css'
ANALYTICAL=ROOT/'TSK_0333_POST_CR0007_INTEGRATED_PROTOTYPE_ACCEPTANCE_EVIDENCE_2026-08-31.md'
DETERMINISTIC=ROOT/'TSK_0333_POST_CR0007_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md'
STRUCT=ROOT/'.github/scripts/verify_tsk0333_post_cr0007_structured_20260831.py'
BROWSER=ROOT/'.github/scripts/verify_tsk0333_post_cr0007_browser_20260831.mjs'
STRUCT_WF=ROOT/'.github/workflows/verify-tsk0333-post-cr0007-structured-20260831.yml'
BROWSER_WF=ROOT/'.github/workflows/verify-tsk0333-post-cr0007-browser-20260831.yml'

EXPECTED={
 RUNTIME:'15948b153c5c0c07b93fc894ac9f4ca6c537cce0',
 WBS:'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
 GRAPH:'c108d2c162bcea2ee4cc01def46d0487a9501032',
 INDEX:'9395f0e105d20683b5beafa01b02d7b300e79a8d',
 MODEL:'9b7c239024d8ae24371b687aa39de6fa6b2b62b6',
 APP:'476ea932d95592fabf586f7ba381be0d346117fe',
 CSS:'6f8af459a0b0b1c9ec132657dfcd7ebff43090b8',
 ANALYTICAL:'4de73da09d637a142fc9968873ffdd755fdb07f3',
 DETERMINISTIC:'d1427b8bdd64772aab82683220af9becaf07f2ac',
 STRUCT:'497d709c40632a9bbd7e1f9513c27699e1f2d0f6',
 BROWSER:'966cb53e01e58155350fc9a904cf71bd1a30c748',
 STRUCT_WF:'812ab1dbdead44f7cae4d5c9c1c9e7b653766b27',
 BROWSER_WF:'532b1f6c67516e2e449720f791d91af4ee8fe2bc',
}

def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)
for p,e in EXPECTED.items():
    req(p.exists(),f'TSK0333_RECON_MISSING={p.as_posix()}')
    req(blob(p)==e,f'TSK0333_RECON_BLOB_CHANGED={p.as_posix()}')

text=RUNTIME.read_text(encoding='utf-8')
req('## TSK-0333 current accepted stable state — 2026-08-31 — POST-CR-0007' not in text,'TSK0333_RECON_PASS_ALREADY_PRESENT')
for dep in ('TSK-0335','TSK-0334','TSK-0146','TSK-0331'):
    req(f'## {dep} current accepted stable state' in text,f'TSK0333_RECON_CURRENT_DEP_MISSING={dep}')
req('33432762152 / 99621849637' in DETERMINISTIC.read_text(encoding='utf-8'),'TSK0333_RECON_FINAL_RUN_NOT_BOUND')
req('TSK0333_POST_CR0007_BROWSER_VERIFICATION=PASS' in DETERMINISTIC.read_text(encoding='utf-8'),'TSK0333_RECON_FINAL_MARKER_NOT_BOUND')

insert='''## TSK-0333 current accepted stable state — 2026-08-31 — POST-CR-0007

`TSK-0333`: **PASS** under current `ACC-0333 / VER-0333 / EVD-0333`, `DEC-0053/CR-0006`, and `DEC-0054/CR-0007` authority.

- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, MEDIUM, hard dependencies `TSK-0335; TSK-0334; TSK-0146; TSK-0331`, A3 / `AUTO_ALLOWED`; all four direct dependencies are current durable PASS.
- Current integrated prototype blobs: `index.html` `9395f0e105d20683b5beafa01b02d7b300e79a8d`; `model.mjs` `9b7c239024d8ae24371b687aa39de6fa6b2b62b6`; `app.mjs` `476ea932d95592fabf586f7ba381be0d346117fe`; `prototype.css` `6f8af459a0b0b1c9ec132657dfcd7ebff43090b8`.
- Analytical acceptance evidence: `TSK_0333_POST_CR0007_INTEGRATED_PROTOTYPE_ACCEPTANCE_EVIDENCE_2026-08-31.md`, blob `4de73da09d637a142fc9968873ffdd755fdb07f3`.
- Deterministic verification evidence: `TSK_0333_POST_CR0007_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md`, blob `d1427b8bdd64772aab82683220af9becaf07f2ac`.
- Current structured verifier/workflow blobs: `497d709c40632a9bbd7e1f9513c27699e1f2d0f6` / `812ab1dbdead44f7cae4d5c9c1c9e7b653766b27`.
- Current browser verifier/workflow blobs: `966cb53e01e58155350fc9a904cf71bd1a30c748` / `532b1f6c67516e2e449720f791d91af4ee8fe2bc`.
- RED run/job `33431633072 / 99618110708` proved the current verifier rejected the historical accountless-only prototype after authority/dependency checks passed.
- Structured current-scope run/job `33432040521 / 99619466660`: SUCCESS. The final browser workflow reran the structured verifier and all structural markers passed at the accepted head.
- Browser run/job `33432339619 / 99620437461` found one substantive product defect: configured Protection Map lacked the physical DNS removal action. Product code was corrected; the assertion was not weakened.
- Browser run/jobs `33432524365 / 99621051328` and `33432645054 / 99621453921` exposed verifier-only selector/literal false negatives after progressively more product scenarios had already passed. Only verifier assertions changed for those diagnostics.
- Final decisive browser run/job `33432762152 / 99621849637`: **SUCCESS** on self-hosted `adguardvm` with Node `v22.23.2`, npm `10.9.8`, Playwright `1.62.0`, Chrome for Testing / Chromium `151.0.7922.34` in temporary verification-only paths.
- Final browser evidence passed keyboard/skip-link; accountless Android/iPhone setup; false-positive truth; physical removal/recovery/reconfigure; unsupported state; first-session account creation; explicit saved-device creation; returning dashboard; device replacement; fail-closed unknown destructive result plus record deletion; provider error; session expiry/reauth/logout/account-delete boundaries; RTL/responsive 320/768/1024/1440; privacy/no-transport; zero console/page errors.
- Accepted current product rule: the complete core start/configure/verify/Protection Map/support/removal/recovery path remains usable without login. Optional Google account/session/dashboard/device continuity never creates technical `Verified`, never auto-imports/promotes J0/J1, and keeps account/data lifecycle separate from physical protection removal.
- No browsing/query/activity history, child profile, raw DNS logs/history, broad DNS administration, broad per-domain controls or safety score/certification is introduced. The prototype created no browser persistence or external runtime transport during target-browser verification.
- Historical 2026-08-30 TSK-0333 PASS remains historical evidence only; this current section governs downstream dependency use under the post-CR-0007 scope.
- No LG-06, L5 architecture/security/privacy/vendor, implementation, production behavior, real-user validation, publication or launch PASS is inferred.
- `RSK-0002` remains OPEN/non-blocking before L8.

### Queue status after current TSK-0333 acceptance

Recompute eligibility from current WBS dependencies, graph, gates/constraints, runtime evidence and Action Authority. No successor or gate inherits PASS automatically.

'''
# Insert before current TSK-0330 section if present, otherwise append.
anchor='## TSK-0330 current accepted stable state — 2026-08-31 — POST-CR-0007'
pos=text.find(anchor)
if pos>=0:
    new=text[:pos]+insert+text[pos:]
else:
    new=text.rstrip()+'\n\n'+insert
new=re.sub(r'\*\*Updated:\*\* [^\n]+','**Updated:** 2026-08-31T19:52:00Z',new,count=1)
RUNTIME.write_text(new.rstrip()+'\n',encoding='utf-8')
print('TSK0333_PASS_RUNTIME_PRECONDITIONS=PASS')
