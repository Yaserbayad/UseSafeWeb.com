from __future__ import annotations

import hashlib
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

EXPECTED={
  'CURRENT_STATE.md':'1d25f08512fe2398bbfbdb89783a87a2b7da3dd2',
  'Plans/Master/WBS/master-wbs.csv':'b27a0c5df2f5636d8ed71051e9e26a68959a2616',
  'Plans/Master/RELATIONSHIP_INDEX.yaml':'c108d2c162bcea2ee4cc01def46d0487a9501032',
  'TSK_0299_POST_CR0008_DUAL_MODE_VERBAL_SYSTEM_2026-09-01.md':'ff30500b933b9ecc92325659d49ea4e671d296d2',
  'TSK_0299_POST_CR0008_OWNER_IDENTITY_BINDING_CORRECTION_2026-09-01.md':'6b4ac6020391a2f6e291f83c50f27a7583215f3b',
  'TSK_0299_POST_CR0008_CORRECTED_ACCEPTANCE_EVIDENCE_2026-09-01.md':'9d48add06fee14aef76f82a876a61cc88ce59440',
  'TSK_0301_OWNER_IDENTITY_APPROVAL_2026-08-29.md':'66f4b545c03571649a8baa4c0fe3d1df564b5949',
}
OLD='## TSK-0299 current accepted stable state — 2026-09-01 — POST-CR-0008 REQUALIFICATION'
NEW='## TSK-0299 current accepted stable state — 2026-09-01 — POST-CR-0008 CORRECTED OWNER-IDENTITY BINDING'
PROTECTED=(
  '## TSK-0485 current accepted stable state',
  '## TSK-0318 current accepted stable state',
  '## TSK-0319 current accepted stable state',
)

def blob(path):
    return subprocess.check_output(['git','hash-object',path],text=True).strip()

def section(text,prefix):
    m=re.search(r'^'+re.escape(prefix)+r'.*$',text,re.MULTILINE)
    if not m: raise SystemExit(f'missing section {prefix}')
    n=re.search(r'^## ',text[m.end():],re.MULTILINE)
    end=m.end()+n.start() if n else len(text)
    return text[m.start():end]

def sh(text,prefix):
    return hashlib.sha256(section(text,prefix).encode()).hexdigest()

p=Path('CURRENT_STATE.md')
state=p.read_text(encoding='utf-8')
if NEW in state:
    if state.count(NEW)==1 and 'TSK_0299_POST_CR0008_CORRECTED_ACCEPTANCE_EVIDENCE_2026-09-01.md' in section(state,NEW):
        print('TSK0299_CORRECTED_STATE_ALREADY_APPLIED=PASS')
        raise SystemExit(0)
    raise SystemExit('ambiguous corrected TSK-0299 state')
if state.count(OLD)!=1:
    raise SystemExit('expected exactly one stale first-pass TSK-0299 state section')
for path,expected in EXPECTED.items():
    actual=blob(path)
    if actual!=expected: raise SystemExit(f'hash mismatch {path}: {actual} != {expected}')
for h in PROTECTED:
    if h not in state: raise SystemExit(f'protected heading missing: {h}')
before={h:sh(state,h) for h in PROTECTED}

evidence=Path('TSK_0299_POST_CR0008_CORRECTED_ACCEPTANCE_EVIDENCE_2026-09-01.md').read_text(encoding='utf-8')
for s in ['CORRECTED PASS','33572423991 / 100069047010','TSK0299_CORRECTED_ACCEPTANCE=PASS','visible brand name as **`SafeWeb`**']:
    if s not in evidence: raise SystemExit(f'corrected evidence mismatch: {s}')

replacement=r'''## TSK-0299 current accepted stable state — 2026-09-01 — POST-CR-0008 CORRECTED OWNER-IDENTITY BINDING

`TSK-0299 — Define tone, voice, terminology, trust language, protection-state language, and communication examples`: **PASS** under current `ACC-0299 / VER-0299 / EVD-0299`, Project Owner identity authority, `DEC-0052/CR-0005`, `DEC-0053/CR-0006`, `DEC-0054/CR-0007`, and `DEC-0055/CR-0008`.

- WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / HIGH / A3 / `AUTO_ALLOWED` / `PLANNED`; hard dependency `TSK-0298`, current accepted PASS.
- Base complete verbal system `TSK_0299_POST_CR0008_DUAL_MODE_VERBAL_SYSTEM_2026-09-01.md`, blob `ff30500b933b9ecc92325659d49ea4e671d296d2`, publication commit `284a566c9ff282e35bc2500f1060a0869262bb37`.
- Binding owner-identity correction `TSK_0299_POST_CR0008_OWNER_IDENTITY_BINDING_CORRECTION_2026-09-01.md`, blob `6b4ac6020391a2f6e291f83c50f27a7583215f3b`, publication commit `af5331eedb61f2acd4a180da7a638d6d08caf45a`.
- Current owner authority `TSK_0301_OWNER_IDENTITY_APPROVAL_2026-08-29.md`, blob `66f4b545c03571649a8baa4c0fe3d1df564b5949`: visible brand is exactly `SafeWeb`; `UseSafeWeb.com` is project/domain/repository identity; the `Use` prefix is not reusable as visible brand copy/logo text.
- Corrected durable acceptance evidence `TSK_0299_POST_CR0008_CORRECTED_ACCEPTANCE_EVIDENCE_2026-09-01.md`, blob `9d48add06fee14aef76f82a876a61cc88ce59440`, publication commit `86ed9762e3c44885529939d001ed8b2dbec4e29a`.
- Corrected independent read-only verification `.github/workflows/verify-tsk0299-owner-identity-correction-v2.yml`, blob `8f039c55ed6c61f790cae958f3b40a9b0d0321f4`; run/job `33572423991 / 100069047010`: **SUCCESS** with `contents: read`.
- Current visible product/brand copy uses `SafeWeb`; generic parent-facing DNS feature/CTA copy uses `SafeWeb DNS`; exact `UseSafeWeb.com`/hostnames/URLs remain literal only where they are actual technical identifiers.
- Current TSK-0320 S1–S6 evidence and transition semantics remain unchanged; this correction changes only the higher-authority visible brand token in parent-facing examples, never evidence strength or protection truth.
- The complete accountless core remains first-class. Optional sign-in/session/dashboard/device management is bounded continuity, never mandatory for core value or a stronger-protection signal. No J0/J1 auto-link/import/promotion/TTL extension is authorized.
- No browsing/query/activity history, child account/profile or broad DNS administration is introduced. Dashboard/device ownership remains non-verifying context.
- Start over, logout, unlink/revoke, device-record deletion, account deletion and physical SafeWeb DNS removal remain distinct operations; ambiguous consequential results require reconciliation before retry.
- English/Turkish/Arabic+RTL semantics preserve evidence strength, actor, optionality, scope and destructive-operation object meaning; language availability does not activate a market.
- `RSK-0002` remains OPEN; representative-parent comprehension validation remains L8-only. No deferred legal/privacy completion is inferred.
- TSK-0301 remains independently dependent on both `TSK-0302` and current TSK-0299; the owner-approved identity itself is preserved and not reselected here.
- The first-pass TSK-0299 state commit `dcbe2c272afa690d4feb088ff2b94d411da56a38` and evidence remain diagnostic/historical for compatible facts only; they are superseded by this corrected current binding.
- **Non-inference:** L4 verbal-system design PASS only; no implementation/build, provider acceptance, legal/privacy completion, publication, payment, participant/market activation, LG-06, production behavior or launch PASS is inferred.

### Queue status after corrected post-CR-0008 TSK-0299 acceptance

Recompute current eligibility from canonical WBS/graph, current semantic PASS validity and gates. Verify TSK-0302/TSK-0301 current dependency validity and compare any open brand-chain requalification against reopened TSK-0316 under governing selection rules. Preserve current TSK-0485 and synchronized TSK-0318/TSK-0319 sections unchanged.
'''

m=re.search(r'^'+re.escape(OLD)+r'.*$',state,re.MULTILINE)
n=re.search(r'^## ',state[m.end():],re.MULTILINE)
end=m.end()+n.start() if n else len(state)
result=state[:m.start()]+replacement+state[end:]
lines=result.splitlines()
idx=[i for i,x in enumerate(lines) if x.startswith('**Updated:**')]
if len(idx)!=1: raise SystemExit('unexpected Updated count')
lines[idx[0]]='**Updated:** '+datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
result='\n'.join(lines).rstrip()+'\n'
if OLD in result or result.count(NEW)!=1: raise SystemExit('replacement failed')
for h,b in before.items():
    if sh(result,h)!=b: raise SystemExit(f'protected section changed: {h}')
p.write_text(result,encoding='utf-8')
check=p.read_text(encoding='utf-8')
for h,b in before.items():
    if sh(check,h)!=b: raise SystemExit(f'post-write protected section changed: {h}')
print('TSK0485_SECTION_PRESERVED=PASS')
print('TSK0318_SECTION_PRESERVED=PASS')
print('TSK0319_SECTION_PRESERVED=PASS')
print('TSK0299_CORRECTED_STATE_RECONCILIATION=PASS')
