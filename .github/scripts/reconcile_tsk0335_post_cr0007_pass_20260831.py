import subprocess
from pathlib import Path

ROOT=Path('.')
RUNTIME=ROOT/'CURRENT_STATE.md'
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
BASE=ROOT/'design/TSK-0335/PROTECTION_MAP_COVERAGE_LIMIT_INTERACTIONS_CANDIDATE.md'
AMEND=ROOT/'design/TSK-0335/POST_CR0007_DUAL_MODE_PROTECTION_MAP_AMENDMENT_CANDIDATE.md'
PREP=ROOT/'TSK_0335_POST_CR0007_CURRENT_SCOPE_PREPARATION_EVIDENCE_2026-08-31.md'
APPROVAL=ROOT/'TSK_0335_POST_CR0007_OWNER_APPROVAL_EVIDENCE_2026-08-31.md'
FINAL=ROOT/'TSK_0335_POST_CR0007_DETERMINISTIC_ACCEPTANCE_EVIDENCE_2026-08-31.md'

EXPECTED={
 RUNTIME:'8f053c4c12a90c0c6e0646b824846bfbd6682935',
 WBS:'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
 BASE:'7c65a697a98961d0df278658e59262ce39874ff5',
 AMEND:'80db66d9261e6ccf85e0253530819ad262b39497',
 PREP:'03e7a35b7943586d635975fdc9a53bfd0e99ee44',
 APPROVAL:'f1b6dcaf10ee276593563e1adf732d305e5d5789',
 FINAL:'a907e91a046e07a16b761b0687d4397dc48a7acd',
}

def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)

for p,e in EXPECTED.items():
    req(p.exists(),f'TSK0335_RECON_MISSING={p.as_posix()}')
    req(blob(p)==e,f'TSK0335_RECON_BLOB_CHANGED={p.as_posix()}')

text=RUNTIME.read_text(encoding='utf-8')
waiting='## TSK-0335 current waiting state — 2026-08-31 — POST-CR-0007'
accepted='## TSK-0335 current accepted stable state — 2026-08-31 — POST-CR-0007'
req(waiting in text,'TSK0335_RECON_WAITING_SECTION_MISSING')
req(accepted not in text,'TSK0335_RECON_CURRENT_PASS_ALREADY_PRESENT')
req('APPROVE TSK-0335 POST-CR-0007 DUAL-MODE PROTECTION MAP AMENDMENT' in text,'TSK0335_RECON_RESOLUTION_COMMAND_MISSING')

start=text.index(waiting)
next_heading=text.find('\n## ',start+len(waiting))
end=next_heading if next_heading>=0 else len(text)
section=f'''## TSK-0335 current accepted stable state — 2026-08-31 — POST-CR-0007

`TSK-0335 — Design Protection Map and coverage-limit interactions`: **PASS** under current `ACC-0335 / VER-0335 / EVD-0335`, `DEC-0053/CR-0006`, `DEC-0054/CR-0007`, and explicit Project Owner approval at `2026-08-31T19:30:51Z`.

- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, MEDIUM, dependency `TSK-0330`, A1 / `HUMAN_ONLY`; dependency TSK-0330 is current-qualified PASS.
- Historical owner-approved Protection Map base remains `design/TSK-0335/PROTECTION_MAP_COVERAGE_LIMIT_INTERACTIONS_CANDIDATE.md`, blob `7c65a697a98961d0df278658e59262ce39874ff5`.
- Current dual-mode amendment: `design/TSK-0335/POST_CR0007_DUAL_MODE_PROTECTION_MAP_AMENDMENT_CANDIDATE.md`, blob `80db66d9261e6ccf85e0253530819ad262b39497`.
- Preparation evidence: `TSK_0335_POST_CR0007_CURRENT_SCOPE_PREPARATION_EVIDENCE_2026-08-31.md`, blob `03e7a35b7943586d635975fdc9a53bfd0e99ee44`; preparation run/job `33430327495 / 99613846431`: SUCCESS.
- Owner approval evidence: `TSK_0335_POST_CR0007_OWNER_APPROVAL_EVIDENCE_2026-08-31.md`, blob `f1b6dcaf10ee276593563e1adf732d305e5d5789`; exact owner command: `APPROVE TSK-0335 POST-CR-0007 DUAL-MODE PROTECTION MAP AMENDMENT`.
- Deterministic final acceptance evidence: `TSK_0335_POST_CR0007_DETERMINISTIC_ACCEPTANCE_EVIDENCE_2026-08-31.md`, blob `a907e91a046e07a16b761b0687d4397dc48a7acd`.
- Final owner-bound verifier run/job `33431191778 / 99616661300`: SUCCESS; exact blobs, WBS/graph, WAITING precondition, owner approval binding, preparation proof, current acceptance, source alignment, privacy/validation fences and repository cleanliness all PASS.
- Accepted current interaction model preserves the six-state evidence map, strict technical `Verified` versus parent-confirmed separation, immediate material-gap disclosure, independent Phone/Internet/Service truth, deterministic state checks, no overall safety score, and future L8 comprehension hooks without claiming L4 human evidence.
- The same truth model is valid in the complete accountless core and optional signed-in dashboard/device-detail context. Account/session/dashboard/device-record presence never creates technical `Verified`; stored/earlier results are not automatically current; provider/session/account failure does not rewrite physical protection truth.
- No automatic J0/J1 promotion is authorized. Logout, unlink/revoke, dashboard-record deletion, account deletion, J0/J1 deletion and physical UseSafeWeb removal remain distinct; physical `Removed` requires owning physical-removal evidence.
- No browsing/query/activity history, child profiles, raw DNS logs, unrestricted DNS administration, broad per-domain controls or safety certification is introduced. Full core Protection Map/help/recovery remains usable without login.
- No TSK-0333, LG-06, L5 architecture/security/privacy/vendor, implementation, production behavior, real-user validation, publication or launch PASS is inferred.
- `RSK-0002` remains OPEN/non-blocking before L8.

### Queue status after post-CR-0007 TSK-0335 acceptance

Recompute eligibility from current WBS dependencies, relationship graph, runtime evidence, gates/constraints, changed-scope validity and Action Authority. TSK-0333 may use TSK-0335 as a dependency only after this PASS mutation is committed and read back; no successor inherits PASS automatically.
'''
new=text[:start]+section+(text[end:] if next_heading>=0 else '\n')
# update runtime timestamp only; preserve all unrelated content
import re
new=re.sub(r'\*\*Updated:\*\* [^\n]+', '**Updated:** 2026-08-31T19:33:18Z', new, count=1)
RUNTIME.write_text(new.rstrip()+'\n',encoding='utf-8')
print('TSK0335_PASS_RUNTIME_PRECONDITIONS=PASS')
