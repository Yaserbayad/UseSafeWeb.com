from __future__ import annotations
import datetime as dt
import re
import subprocess
from pathlib import Path

ROOT=Path.cwd()
RUNTIME=ROOT/'CURRENT_STATE.md'
REVIEW=ROOT/'TSK_0052_LG06_CURRENT_DUAL_MODE_FREEZE_REVIEW_2026-09-01.md'
MARKER=ROOT/'TSK_0052_LG06_CURRENT_EVIDENCE_AUTOVERIFY_2026-09-01.md'
EVIDENCE=ROOT/'TSK_0052_LG06_CURRENT_ACCEPTANCE_EVIDENCE_2026-09-01.md'

def read(p: Path)->str: return p.read_text(encoding='utf-8')
def blob(path: str)->str: return subprocess.check_output(['git','hash-object',path],text=True).strip()
def path_commit(path: str)->str: return subprocess.check_output(['git','log','-1','--format=%H','--',path],text=True).strip()

# Re-evaluate the complete repository-current gate review immediately before state mutation.
subprocess.run(['python3','.github/scripts/verify_tsk0052_lg06_current_review_20260901.py'],check=True)

assert blob('Plans/Master/WBS/master-wbs.csv')=='b57104a71ab814d0f67e7fb8b0fd388d1f6aacfa'
assert blob(str(REVIEW.relative_to(ROOT)))=='352f302164d1074547b46de9acdffba406903ac8'
assert blob(str(MARKER.relative_to(ROOT)))=='8eb3eb14b7f62775f0ee0fbc6312f161a5a94333'
assert blob('TSK_LG06_PREDECESSOR_CURRENT_REQUALIFICATION_EVIDENCE_2026-09-01.md')=='e17f0128045091a500c9ad89a9334c51732109ff'

marker=read(MARKER)
for phrase in ['**Review verification:** PASS','`cce13bab9494356c4271e46335b2fa7a128e8383`','`33493887308`','every applicable current ACC-0052 L4 evidence category is mapped','does not itself create gate PASS or unlock L5']:
    assert phrase in marker, phrase

state=read(RUNTIME)
pass_heading='## TSK-0052 / LG-06 current accepted stable state — 2026-09-01 — POST-CR-0007'
assert pass_heading not in state
assert '`TSK-0052 / LG-06` remains **non-PASS**' in state
for heading in [
    '## TSK-0043 current accepted stable state — 2026-09-01 — POST-CR-0006/0007',
    '## TSK-0321 current accepted stable state — 2026-09-01 — POST-CR-0007',
    '## TSK-0309 current accepted stable state — 2026-09-01 — POST-CR-0006/0007',
    '## TSK-0628 current accepted stable state — 2026-09-01 — POST-CR-0006/0007',
]: assert heading in state, heading
assert not EVIDENCE.exists()

now=dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
review_blob=blob(str(REVIEW.relative_to(ROOT)))
marker_blob=blob(str(MARKER.relative_to(ROOT)))
marker_commit=path_commit(str(MARKER.relative_to(ROOT)))
predecessor_blob=blob('TSK_LG06_PREDECESSOR_CURRENT_REQUALIFICATION_EVIDENCE_2026-09-01.md')

evidence=f'''# TSK-0052 / LG-06 current acceptance evidence — 2026-09-01

**Disposition:** **PASS**  
**Task / gate:** `TSK-0052 / LG-06 — Product, Brand and Experience Freeze`  
**Acceptance / verification / evidence:** `ACC-0052 / VER-0052 / EVD-0052`  
**Authority:** `A4 / AUTO_ALLOWED`; `DEC-0052 / CR-0005`; `DEC-0053 / CR-0006`; `DEC-0054 / CR-0007`.  
**Current WBS blob:** `b57104a71ab814d0f67e7fb8b0fd388d1f6aacfa`.  
**Current review:** `TSK_0052_LG06_CURRENT_DUAL_MODE_FREEZE_REVIEW_2026-09-01.md`, blob `{review_blob}`.  
**Independent review marker:** blob `{marker_blob}` at commit `{marker_commit}`; GitHub Actions run `33493887308` / job `99811476611` — SUCCESS.  
**Current predecessor evidence:** blob `{predecessor_blob}`.  
**Acceptance time:** {now}.

## Acceptance result

PASS. Every applicable current ACC-0052 L4 category is evidenced: dual-mode Version-1 product/non-goals; all 91 requirements and traceability; zero unresolved critical L4 requirement conflicts; accountless setup/Protection Map/recovery; optional Google sign-in/account/session; minimum ownership persistence and lightweight dashboard/device management; account/device lifecycle/deletion/recovery; privacy/security/truth boundaries; one SafeWeb identity/design system; source-controlled content; accessibility/responsive/i18n; and dual-mode self-service.

The four direct hard dependencies `TSK-0043`, `TSK-0321`, `TSK-0309`, and `TSK-0628` are current durable PASS. The current integrated prototype/source and final accessibility evidence are pinned by the verified review. Historical pre-CR-0006 LG-06 readiness is not used as current proof.

## Residual risks and contrary evidence

No current evidence contradicts the L4 freeze. `RSK-0002`, `RSK-0005`, `RSK-0015`, `RSK-0017`, and `RSK-0022` remain OPEN with their existing owners/triggers/mitigations. DEC-0054 permits project-defined material residual-risk acceptance inside frozen scope where no higher-authority prohibition or required human act applies. This acceptance does not close or hide those risks.

Deferred legal/compliance facts under DEC-0049 remain unresolved facts, not PASS, waiver or exemption. No pre-L8 real-user evidence is required or inferred under DEC-0052. All actually applicable legal/privacy/consent/security/platform prerequisites remain controlling at their later gates and before live users.

## Work unlocked

LG-06 PASS unlocks **L5 / LG-07 architecture, security, privacy and delivery-readiness work only**, subject to ordinary WBS dependencies, current inputs, Action Authority and evidence. It does not make LG-07 PASS and does not approve Google/Firebase vendor use, persistence architecture, build, deployment, participant processing, production activation, payment, publication, market activation or launch.
'''
EVIDENCE.write_text(evidence.rstrip()+'\n',encoding='utf-8')

appendix=f'''

{pass_heading}

`TSK-0052 / LG-06 — Product, Brand and Experience Freeze`: **PASS** under current `ACC-0052 / VER-0052 / EVD-0052`, `DEC-0052/CR-0005`, `DEC-0053/CR-0006`, and `DEC-0054/CR-0007` authority.

- Action authority: **A4 / AUTO_ALLOWED** inside frozen scope; owner-approved authority reconciliation is already canonical.
- Direct hard dependencies `TSK-0043`, `TSK-0321`, `TSK-0309`, and `TSK-0628` are current durable PASS.
- Current gate review: `TSK_0052_LG06_CURRENT_DUAL_MODE_FREEZE_REVIEW_2026-09-01.md`, blob `{review_blob}`.
- Independent verification: run/job `33493887308 / 99811476611` — SUCCESS; durable marker `TSK_0052_LG06_CURRENT_EVIDENCE_AUTOVERIFY_2026-09-01.md`, blob `{marker_blob}`.
- Durable acceptance evidence: `TSK_0052_LG06_CURRENT_ACCEPTANCE_EVIDENCE_2026-09-01.md`.
- Every current L4 gate category is evidenced: dual-mode product/non-goals, current requirements/traceability, zero unresolved critical conflicts, accountless critical journey/Protection Map/recovery, optional account/session/dashboard/device lifecycle, privacy/security/truth boundaries, brand/design system, content, accessibility/i18n and self-service.
- `RSK-0002`, `RSK-0005`, `RSK-0015`, `RSK-0017`, and `RSK-0022` remain OPEN and explicitly carried forward. Deferred legal/compliance facts remain unresolved and no real-user evidence is inferred.
- **Unlock:** L5 / LG-07 architecture-security-privacy-delivery readiness work may now be derived from current authority. No LG-07, build, implementation, production, payment, publication, market or launch PASS is inherited.

### Queue status after LG-06 PASS

Recompute the exact eligible L5 work from current WBS dependencies, relationship graph, gate preconditions, runtime PASS evidence, constraints/interfaces, executor availability and Action Authority. Do not select the next task from task numbering or historical plans.
'''
state=re.sub(r'\*\*Updated:\*\*\s*[^\n]+',f'**Updated:** {now}',state,count=1)
RUNTIME.write_text(state.rstrip()+appendix.rstrip()+'\n',encoding='utf-8')

new=read(RUNTIME)
assert new.count(pass_heading)==1
assert 'LG-06 PASS unlocks **L5 / LG-07 architecture, security, privacy and delivery-readiness work only**' in read(EVIDENCE)
assert 'No LG-07, build, implementation, production, payment, publication, market or launch PASS is inherited.' in new
print('TSK0052_LG06_STABLE_PASS_READY')
