from pathlib import Path
import subprocess
from datetime import datetime, timezone

ROOT=Path('.')
R=ROOT/'CURRENT_STATE.md'
EXPECTED={
 'CURRENT_STATE.md':'f735ab7b68cd0231dc3515739992242d67f5193e',
 'Plans/Master/WBS/master-wbs.csv':'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
 'design/TSK-0334/SUPPORT_FALSE_POSITIVE_REMOVAL_RECONFIGURATION_FLOWS_CANDIDATE.md':'44fab92b51ae8ed8b6f5f325ba1558bcd297eb5f',
 'design/TSK-0334/POST_CR0007_ACCOUNT_SUPPORT_LIFECYCLE_AMENDMENT_CANDIDATE.md':'de423bdb8aeb2b0a0f25a85850be380cfab7e67d',
 'TSK_0334_POST_CR0007_CURRENT_SCOPE_PREPARATION_EVIDENCE_2026-08-31.md':'652845396bc62a1df859b2a9f1944576268066b6',
 '.github/scripts/verify_tsk0334_post_cr0007_candidate_20260831.py':'0cb80a09ee765e266932a91e7b45b092bc7e7d13',
 '.github/workflows/verify-tsk0334-post-cr0007-candidate-20260831.yml':'e1bdede89dc906e5adf60488155a9582228bb85e',
}
def blob(p): return subprocess.check_output(['git','hash-object',p],text=True).strip()
for p,e in EXPECTED.items():
    a=blob(p)
    if a!=e: raise SystemExit(f'TSK0334_STALE_INPUT={p}:{a}:{e}')
text=R.read_text(encoding='utf-8')
heading='## TSK-0334 current state — 2026-08-31 — POST-CR-0007'
if heading in text: raise SystemExit('TSK0334_CURRENT_STATE_ALREADY_PRESENT')
if '## TSK-0332 current accepted stable state' not in text: raise SystemExit('TSK0332_CURRENT_PASS_MISSING')
now=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
lines=text.splitlines()
for i,l in enumerate(lines):
    if l.startswith('**Updated:**'):
        lines[i]=f'**Updated:** {now}'; break
text='\n'.join(lines).rstrip()+'\n\n'
section=f'''{heading}\n\n`TSK-0334 — Design support, false-positive, removal, and reconfiguration flows`: **WAITING / HUMAN_APPROVAL_REQUIRED**, not PASS.\n\n- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, MEDIUM, dependency `TSK-0330`, A1 / `HUMAN_ONLY`.\n- Historical owner-approved base candidate remains evidence for still-valid technical support categories only: `design/TSK-0334/SUPPORT_FALSE_POSITIVE_REMOVAL_RECONFIGURATION_FLOWS_CANDIDATE.md`, blob `44fab92b51ae8ed8b6f5f325ba1558bcd297eb5f`.\n- Its account-system/persistent-device exclusions are stale under DEC-0053/CR-0006 and cannot alone satisfy current scope.\n- Prepared current amendment: `design/TSK-0334/POST_CR0007_ACCOUNT_SUPPORT_LIFECYCLE_AMENDMENT_CANDIDATE.md`, version `1.0.0-post-cr0007`, blob `de423bdb8aeb2b0a0f25a85850be380cfab7e67d`.\n- Preparation evidence: `TSK_0334_POST_CR0007_CURRENT_SCOPE_PREPARATION_EVIDENCE_2026-08-31.md`, blob `652845396bc62a1df859b2a9f1944576268066b6`.\n- Deterministic preparation run/job `33415828154 / 99566111401`: **SUCCESS** on `adguardvm`; WBS human boundary PASS; eight-category coverage PASS; current-scope semantics PASS; HUMAN_ONLY PASS fence PASS; preparation verification PASS; repository diff/clean checks PASS.\n- Current candidate preserves SUP-01..SUP-05 and adds SUP-06 account/session/provider access, SUP-07 saved-device/ownership/unlink, and SUP-08 account/device deletion/lifecycle-result support.\n- Account/session/provider failures remain account-only; ownership mismatch fails closed; uncertain destructive outcomes require authoritative resolution; no destructive action auto-replays after re-authentication.\n- Logout, account deletion, dashboard-record deletion, unlinking, J0/J1 deletion and physical UseSafeWeb removal remain distinct.\n- No password/token/child identity/browsing-query-activity history/raw DNS logs or unrestricted administration is introduced.\n- **Required human decision:** approve or reject the exact base candidate + current amendment. No approval is inferred from prior instructions or from preparation success.\n- Exact approval phrase accepted for this bounded decision: `APPROVE TSK-0334 POST-CR-0007 CURRENT-SCOPE SUPPORT AMENDMENT`.\n- TSK-0331 remains not eligible because its hard dependencies are `TSK-0332; TSK-0334`; TSK-0332 is current PASS, TSK-0334 is WAITING.\n- No TSK-0331, TSK-0333, LG-06, implementation, provider/vendor/security/privacy architecture, production operation or behavioral-validation PASS is inferred. `RSK-0002` remains OPEN/non-blocking before L8.\n\n### Queue status at TSK-0334 human boundary\n\nStop governed progression on this active dependency chain until the Project Owner explicitly approves or rejects the exact current candidate. Recompute eligibility after that decision is persisted and read back.\n'''
R.write_text(text+section,encoding='utf-8')
print('TSK0334_WAITING_PRECONDITIONS=PASS')
