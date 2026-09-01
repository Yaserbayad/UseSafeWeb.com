#!/usr/bin/env python3
import csv, os, re, subprocess
from pathlib import Path
A=Path('TSK_0143_NATIVE_DEVICE_SAFEGUARD_ROUTING_REQUIREMENTS_2026-09-01.md'); S=Path('CURRENT_STATE.md'); W=Path('Plans/Master/WBS/master-wbs.csv')
AB='7eca238090738f282db2b43c7f988a7ff716df19'; WB='b27a0c5df2f5636d8ed71051e9e26a68959a2616'; LB='2097d83961affaa69850e41a5ffcd72a660d69cd'; PUB='3e10db0f6549a24349fafeef24fb30db8dd282cc'
def h(p): return subprocess.check_output(['git','hash-object',p],text=True).strip()
assert h(str(A))==AB and h(str(W))==WB and h('Plans/Master/Layers/LAYER_5_AI_EXECUTION_EVIDENCE_STATE_CONTROL.md')==LB
with W.open(encoding='utf-8-sig',newline='') as f:r=next(x for x in csv.DictReader(f) if (x.get('Task_ID')or'').strip()=='TSK-0143')
assert (r.get('Title')or'').strip()=='Specify native-device safeguard routing requirements'
assert (r.get('Lifecycle_Stage')or'').strip()=='L4' and (r.get('Priority')or'').strip()=='MEDIUM'
assert (r.get('AI_Capability_A0_A4')or'').strip()=='A3' and (r.get('Action_Authority')or'').strip()=='AUTO_ALLOWED'
assert (r.get('Dependencies')or'').strip()=='TSK-0146'
assert (r.get('Acceptance_ID')or'').strip()=='ACC-0143' and (r.get('Verification_ID')or'').strip()=='VER-0143' and (r.get('Evidence_ID')or'').strip()=='EVD-0143'
assert (r.get('Risk_Reference')or'').strip()=='RSK-0002' and (r.get('Interface_Reference')or'').strip()=='INT-0003; INT-0004'
assert {x.strip() for x in (r.get('Requirement_Reference')or'').split(';')}=={'REQ-0007','REQ-0008','CON-0001','CON-0002'}
assert (r.get('Acceptance_Criteria')or'').strip()=='Requirements cover supported platform states, already-configured handling, parent confirmation, unsupported paths, stale guidance, and verification limitations.'
s=S.read_text(); assert '## TSK-0146 current accepted stable state — 2026-08-30 — POST-CR-0006' in s
head='## TSK-0143 current accepted stable state — 2026-09-01 — POST-CR-0008'; assert head not in s
a=A.read_text()
for m in ['supported_action_needed','supported_already_configured','supported_parent_confirmation_required','supported_verified','unsupported','guidance_stale_or_uncertain','not_applicable','removed_or_disabled','never create `protected_verified` by itself','No stale route may silently inherit support','accountless users receive the complete core routing experience','synthetic/internal evidence is never relabelled human validation','INT-0004','RSK-0002','PASS candidate pending deterministic reviewer verification']: assert m in a,m
for m in ['Technical verification','Configuration evidence','Parent confirmation','`configured_parent_confirmed`','`uncertain_error`','`not_covered`']: assert m in a,m
for p in [r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',r'ghp_[A-Za-z0-9]{30,}',r'github_pat_[A-Za-z0-9_]{40,}',r'AKIA[0-9A-Z]{16}']: assert not re.search(p,a)
for path,marks in {'Plans/Master/Registers/REQUIREMENTS.md':['REQ-0007','REQ-0008'],'Plans/Master/Registers/CONSTRAINTS.md':['CON-0001','CON-0002'],'Plans/Master/Registers/RISKS.md':['RSK-0002'],'Plans/Master/Registers/INTERFACES.md':['INT-0003','INT-0004']}.items():
 t=Path(path).read_text(); [(_ for _ in ()).throw(AssertionError(m)) if m not in t else None for m in marks]
v=subprocess.run(['python3','Plans/Master/Tools/validate_master_plan.py'],text=True,capture_output=True,check=True); print(v.stdout,end=''); c=v.stdout+v.stderr
for m in ['VALIDATION PASS','tasks=641','dependency_edges=858','broken_links=0','generated_missing_task_ids=0']: assert m in c,m
sec=f'''{head}\n\n`TSK-0143 — Specify native-device safeguard routing requirements`: **PASS** under current `ACC-0143 / VER-0143 / EVD-0143`, current `TSK-0146` dependency proof and CR-0008 authority.\n\n- Action authority: **A3 / AUTO_ALLOWED**.\n- Artifact: `TSK_0143_NATIVE_DEVICE_SAFEGUARD_ROUTING_REQUIREMENTS_2026-09-01.md`, version `1.0.0`, blob `{AB}`, publication commit `{PUB}`.\n- Verification source commit: `{os.environ['SOURCE_COMMIT']}`; GitHub Actions run/attempt `{os.environ.get('GITHUB_RUN_ID','UNKNOWN')} / {os.environ.get('GITHUB_RUN_ATTEMPT','1')}`.\n- Acceptance proof: exact WBS/dependency/ACC/VER/EVD/authority; REQ-0007/0008; CON-0001/0002; RSK-0002; INT-0003/0004; supported/already-configured/parent-confirmed/unsupported/stale/verification-limited routing semantics; truth-state negative assertions; secret guard; and full modular validator passed before runtime mutation.\n- Parent/configuration confirmation never becomes technical `protected_verified`; unsupported/stale paths fail closed to truthful lower states. Accountless core remains complete without login.\n- No internal/synthetic review is represented as human behavioral/user validation.\n- Runtime acceptance does not alter WBS, graph, manifest, AdGuard or the CR-0008 owner-frozen planning baseline.\n- **Non-inference:** no implementation, device/runtime verification, LG-07, production activation, launch or real-user outcome becomes PASS from this requirements task.'''
S.write_text(s.rstrip()+'\n\n'+sec+'\n')
print('ACC_0143=PASS\nVER_0143=PASS\nEVD_0143=PASS\nTSK0143_STATE_CANDIDATE=PASS')