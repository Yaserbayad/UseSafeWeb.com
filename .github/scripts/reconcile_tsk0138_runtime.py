from datetime import datetime, timezone
from pathlib import Path
import subprocess

EXPECTED={
 'CURRENT_STATE.md':'14fe2b734eb58c63aa2ce38aa3b99739c66f8ef5',
 'Plans/Master/WBS/master-wbs.csv':'3bb1598a6233a2bbefa52c746a7621867c6c6e89',
 'TSK_0138_UNRESOLVED_PRODUCT_ASSUMPTIONS_AND_OWNER_DECISIONS_2026-08-28.md':'d782f26d5d48b0902b044d8bbab48569bdee0ea2',
 'TSK_0138_POST_CR0006_UNRESOLVED_PRODUCT_ASSUMPTIONS_AND_OWNER_DECISIONS_2026-08-30.md':'a628d84afda666b99e05e494a921fb01e73ac930',
 'TSK_0138_POST_CR0006_UNRESOLVED_ASSUMPTIONS_DECISIONS_EVIDENCE_2026-08-30.md':'645e3df77bae21690b8272e7dc786da39023cb7f',
}
for path,sha in EXPECTED.items():
    actual=subprocess.check_output(['git','hash-object',path],text=True).strip()
    if actual!=sha: raise SystemExit(f'prestate mismatch {path}: {actual} != {sha}')

p=Path('CURRENT_STATE.md'); s=p.read_text(encoding='utf-8')
old='### TSK-0138 accepted stable state\n'
new='### Historical TSK-0138 accepted stable state — PRE-CR-0005/0006 — SUPERSEDED\n\n> Historical only. DEC-0052/CR-0005 and DEC-0053/CR-0006 superseded the account-deferral and pre-build-human-validation assumptions in this acceptance. Use the post-CR-0006 TSK-0138 section below for current runtime state.\n\n'
if s.count(old)!=1: raise SystemExit('historical TSK0138 heading mismatch')
s=s.replace(old,new,1)
marker='## Frozen technical identity\n'
if s.count(marker)!=1: raise SystemExit('frozen technical identity marker mismatch')
current='''## TSK-0138 current accepted stable state — 2026-08-30 — POST-CR-0006

`TSK-0138 — Register unresolved product assumptions and owner decisions`: **PASS** under current `ACC-0138 / VER-0138 / EVD-0138` and `DEC-0052/CR-0005 + DEC-0053/CR-0006` authority.

- Current WBS blob `3bb1598a6233a2bbefa52c746a7621867c6c6e89`: L4, dependency `TSK-0141`, A3 / `AUTO_ALLOWED`; WBS planning snapshot is not runtime proof.
- Dependency `TSK-0141` is current post-CR-0006 PASS.
- Current register: `TSK_0138_POST_CR0006_UNRESOLVED_PRODUCT_ASSUMPTIONS_AND_OWNER_DECISIONS_2026-08-30.md`, blob `a628d84afda666b99e05e494a921fb01e73ac930`.
- Durable evidence: `TSK_0138_POST_CR0006_UNRESOLVED_ASSUMPTIONS_DECISIONS_EVIDENCE_2026-08-30.md`, blob `645e3df77bae21690b8272e7dc786da39023cb7f`.
- Deterministic verifier run/job `33322945034 / 99288000661`: SUCCESS on self-hosted `adguardvm`; dependency, stale historical assumptions, DEC-0052/0053 rebaseline, all open-item control fields and owner boundaries passed.
- Historical UPA-009/010/017 are resolved/superseded: bounded optional V1 accounts/dashboard are required while the accountless core remains required, and integrated build no longer waits for pre-product human validation.
- Seventeen current unresolved items remain controlled. Real-parent behavioral unknowns are deferred to L8 after LG-09, not fabricated or used as L4-L7 blockers.
- LG-06 remains non-PASS/HUMAN_ONLY; legal/participant/public/payment/launch/advanced-scope fences remain active.

### Queue status after post-CR-0006 TSK-0138 acceptance

TSK-0138 may now satisfy its hard-dependency edges, including TSK-0140. Successor eligibility must still be recomputed against current WBS dependencies, runtime evidence, gates and Action Authority.

'''
s=s.replace(marker,current+marker,1)
lines=s.splitlines()
if len(lines)<3 or not lines[2].startswith('**Updated:** '): raise SystemExit('Updated header mismatch')
lines[2]='**Updated:** '+datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
s='\n'.join(lines)+('\n' if s.endswith('\n') else '')
p.write_text(s,encoding='utf-8')
for token in ['## TSK-0138 current accepted stable state — 2026-08-30 — POST-CR-0006','645e3df77bae21690b8272e7dc786da39023cb7f','33322945034 / 99288000661','### Historical TSK-0138 accepted stable state — PRE-CR-0005/0006 — SUPERSEDED']:
    if token not in s: raise SystemExit('post-transform token missing: '+token)
print('TSK0138_RUNTIME_TRANSFORM=PASS')
