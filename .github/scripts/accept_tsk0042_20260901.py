#!/usr/bin/env python3
import csv, os, re, subprocess
from pathlib import Path

ART=Path('TSK_0042_USER_SUPPORT_EXCEPTION_RECOVERY_REMOVAL_REQUIREMENTS_2026-09-01.md')
STATE=Path('CURRENT_STATE.md')
WBS=Path('Plans/Master/WBS/master-wbs.csv')
L5=Path('Plans/Master/Layers/LAYER_5_AI_EXECUTION_EVIDENCE_STATE_CONTROL.md')
EVENTS=Path('TSK_0498_PRIVACY_SAFE_DECISION_LINKED_EVENT_CONTRACT_2026-09-01.md')

EXPECTED={
 'artifact':'95b2269059e991284e3268f7d2730747b24603a9',
 'state':'d8dea2f44f50bc989c4fd35414a85080a95df73e',
 'wbs':'b27a0c5df2f5636d8ed71051e9e26a68959a2616',
 'l5':'2097d83961affaa69850e41a5ffcd72a660d69cd',
 'events':'6b7a5095122c74ed9ec860b74408dab474576659',
}
PUB='e2802e3fff4e73ab2be890ad0f7e719bf36635bc'

def h(path):
    return subprocess.check_output(['git','hash-object',str(path)],text=True).strip()

def req(cond,msg):
    if not cond:
        raise AssertionError(msg)

for key,path in [('artifact',ART),('state',STATE),('wbs',WBS),('l5',L5),('events',EVENTS)]:
    actual=h(path)
    req(actual==EXPECTED[key],f'unexpected {key} blob: {actual}')
print('TSK0042_CURRENT_BLOBS=PASS')

with WBS.open(encoding='utf-8-sig',newline='') as f:
    rows=list(csv.DictReader(f))
r=next(x for x in rows if (x.get('Task_ID')or'').strip()=='TSK-0042')
req((r.get('Title')or'').strip()=='Specify user support, exception, recovery, and removal requirements','title mismatch')
req((r.get('Lifecycle_Stage')or'').strip()=='L4','lifecycle mismatch')
req((r.get('Priority')or'').strip()=='MEDIUM','priority mismatch')
req((r.get('AI_Capability_A0_A4')or'').strip()=='A3','capability mismatch')
req((r.get('Action_Authority')or'').strip()=='AUTO_ALLOWED','authority mismatch')
req({x.strip() for x in (r.get('Dependencies')or'').split(';') if x.strip()}=={'TSK-0041','TSK-0146'},'dependency mismatch')
req((r.get('Acceptance_ID')or'').strip()=='ACC-0042','acceptance id mismatch')
req((r.get('Verification_ID')or'').strip()=='VER-0042','verification id mismatch')
req((r.get('Evidence_ID')or'').strip()=='EVD-0042','evidence id mismatch')
req({x.strip() for x in (r.get('Requirement_Reference')or'').split(';') if x.strip()}=={'REQ-0001','REQ-0002','CON-0020','CON-0021'},'requirement/control refs mismatch')
req((r.get('Risk_Reference')or'').strip()=='RSK-0044','risk ref mismatch')
req({x.strip() for x in (r.get('Interface_Reference')or'').split(';') if x.strip()}=={'INT-0001','INT-0002'},'interface refs mismatch')
acc=(r.get('Acceptance_Criteria')or'').strip()
req(acc=='Requirements cover setup help, false-positive or unsupported-state incidents, remedies, escalation, data-minimized diagnostics, response expectations, deletion, removal, recovery, and support-burden metrics.',f'acceptance mismatch: {acc}')
print('TSK0042_WBS_CONTRACT=PASS')

state=STATE.read_text(encoding='utf-8')
for marker in [
 '## TSK-0041 current accepted stable state — 2026-09-01 — POST-CR-0008',
 '## TSK-0146 current accepted stable state — 2026-08-30 — POST-CR-0006',
 '## TSK-0320 current accepted stable state — 2026-09-01 — POST-CR-0008',
 '## TSK-0628 current accepted stable state — 2026-09-01 — POST-CR-0006/0007',
]:
    req(marker in state,f'missing current state marker: {marker}')
head='## TSK-0042 current accepted stable state — 2026-09-01 — POST-CR-0008'
req(head not in state,'TSK-0042 already current accepted')
print('TSK0042_DEPENDENCIES_RUNTIME=PASS')

art=ART.read_text(encoding='utf-8')
# Exact ACC clause coverage and incident model.
for marker in [
 '### SUP-01 — Setup help',
 '### SUP-04 — Unsupported / not-covered state',
 '### SUP-07 — False positive / required service blocked',
 '## 5. Diagnostic minimisation hierarchy',
 '### D0 — No-data self-service',
 '### D3 — Exceptional request-level diagnostics',
 '## 6. Response expectations',
 '## 7. Escalation contract',
 '## 8. Deletion, unlink, revoke, and physical removal are distinct',
 '## 9. Recovery requirements',
 '## 10. Support-burden measurement contract',
]: req(marker in art,f'missing ACC section: {marker}')
print('ACC_0042_CLAUSE_COVERAGE=PASS')

for state_name in ['`protected_verified`','`configured_parent_confirmed`','`action_needed`','`not_covered`','`uncertain_error`','`removed`']:
    req(state_name in art,f'missing truth state: {state_name}')
for marker in [
 'never creates `protected_verified`',
 'self-service first and no-routine-human-support by design',
 'exceptional bounded route',
 'does **not** invent a human service-level agreement',
 'narrowest safe explicit reversible exception',
 'no persistent per-parent/per-device personal DNS allowlist',
 'no unrestricted/raw AdGuard administration surface',
 'do not blind-retry materially equivalent failed operations',
 'fresh verification is required before restoring `protected_verified`',
]: req(marker.lower() in art.lower(),f'missing safety/support invariant: {marker}')
print('TSK0042_SUPPORT_TRUTH_AND_RECOVERY=PASS')

for marker in [
 'DNS questions/query history, browsing history, visited/top domains',
 'account ID/email/provider subject as an analytics join key',
 'secrets, tokens, cookies, credentials, authorization headers, private keys',
 'must not become a backdoor analytics or DNS-history store',
]: req(marker.lower() in art.lower(),f'missing diagnostic/privacy guard: {marker}')
print('TSK0042_DIAGNOSTIC_PRIVACY=PASS')

for marker in [
 '**Anonymous journey deletion**',
 '**Support-case data deletion**',
 '**Account deletion**',
 '**Saved device-record deletion**',
 '**Dashboard unlink/revoke**',
 '**Physical UseSafeWeb DNS removal/reset**',
 'One operation never silently implies another.',
]: req(marker in art,f'missing lifecycle separation: {marker}')
print('TSK0042_DELETION_REMOVAL_SEPARATION=PASS')

# Existing event contract is the only telemetry vocabulary allowed.
events=EVENTS.read_text(encoding='utf-8')
approved=[
 'journey_started','journey_step_entered','journey_step_outcome','journey_completed',
 'protection_state_evaluated','protection_verification_outcome','self_service_opened','self_service_outcome',
 'synthetic_service_probe_result','recovery_operation_outcome','channel_entry','cost_period_recorded'
]
for event in approved: req(f'`{event}`' in events,f'approved event missing from TSK-0498: {event}')
for used in ['self_service_opened','self_service_outcome','protection_state_evaluated','protection_verification_outcome','recovery_operation_outcome','channel_entry','cost_period_recorded']:
    req(f'`{used}`' in art,f'TSK-0042 metric source missing: {used}')
for marker in [
 'TSK-0042 introduces no analytics event or property.',
 'this event intentionally has **no `journey_session_id`**',
 'not currently computable',
 'source, formula/numerator, denominator, time window/release/cohort as applicable, owner, guardrail, action, and missing-data treatment',
]: req(marker.lower() in art.lower(),f'missing metric guard: {marker}')
# Ensure no accidental new event-like identifiers beyond controlled support labels and known events.
req('recovery_after_failed_verification' not in art,'invented recovery analytics event/field detected')
print('TSK0042_METRICS_EXISTING_SCHEMA_ONLY=PASS')

# Governance refs must exist in owning registers.
for path,markers in {
 'Plans/Master/Registers/REQUIREMENTS.md':['REQ-0001','REQ-0002'],
 'Plans/Master/Registers/CONSTRAINTS.md':['CON-0020','CON-0021'],
 'Plans/Master/Registers/RISKS.md':['RSK-0044'],
 'Plans/Master/Registers/INTERFACES.md':['INT-0001','INT-0002'],
}.items():
    txt=Path(path).read_text(encoding='utf-8')
    for marker in markers: req(marker in txt,f'{marker} missing from {path}')
for marker in ['fail-closed','Action Authority','scope change']:
    req(marker.lower() in art.lower(),f'governance behavior missing: {marker}')
print('TSK0042_GOVERNANCE_CONTROLS=PASS')

for pat in [r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',r'ghp_[A-Za-z0-9]{30,}',r'github_pat_[A-Za-z0-9_]{40,}',r'AKIA[0-9A-Z]{16}']:
    req(not re.search(pat,art),f'secret-like pattern detected: {pat}')
print('TSK0042_SECRET_GUARD=PASS')

for forbidden in [
 'LG-07 is PASS','implementation is PASS','production is PASS','launch is PASS','real-user supportability is proven',
 'human response within','guaranteed response within'
]:
    req(forbidden.lower() not in art.lower(),f'forbidden downstream/support claim: {forbidden}')
print('TSK0042_NO_DOWNSTREAM_INFERENCE=PASS')

v=subprocess.run(['python3','Plans/Master/Tools/validate_master_plan.py'],text=True,capture_output=True,check=True)
print(v.stdout,end='')
combined=v.stdout+v.stderr
for marker in ['VALIDATION PASS','tasks=641','dependency_edges=858','broken_links=0','generated_missing_task_ids=0']:
    req(marker in combined,f'validator marker missing: {marker}')
print('TSK0042_MASTER_VALIDATION=PASS')

sec=f'''{head}\n\n`TSK-0042 — Specify user support, exception, recovery, and removal requirements`: **PASS** under current `ACC-0042 / VER-0042 / EVD-0042`, current `TSK-0041` + `TSK-0146` dependency proof, and CR-0008 authority.\n\n- Action authority: **A3 / AUTO_ALLOWED**.\n- Artifact: `TSK_0042_USER_SUPPORT_EXCEPTION_RECOVERY_REMOVAL_REQUIREMENTS_2026-09-01.md`, version `1.0.0-post-CR-0008`, blob `{EXPECTED['artifact']}`, publication commit `{PUB}`.\n- Verification source commit: `{os.environ['SOURCE_COMMIT']}`; GitHub Actions run/attempt `{os.environ.get('GITHUB_RUN_ID','UNKNOWN')} / {os.environ.get('GITHUB_RUN_ATTEMPT','1')}`.\n- Acceptance proof: exact WBS/dependencies/ACC/VER/EVD/A3/AUTO_ALLOWED and REQ-0001/0002, CON-0020/0021, RSK-0044, INT-0001/0002; complete setup/false-positive/unsupported/remedy/escalation/diagnostic/response/deletion/removal/recovery/support-metric requirements; current six-state truth semantics; secret/privacy guards; TSK-0498 schema-only metric assertions; and full modular-plan validation all passed before runtime mutation.\n- Support is self-service first/no-routine-human-support for ordinary product paths, with exceptional human escalation only where a valid receiving authority/process exists; no staffing or response SLA is fabricated.\n- False positives require causal confirmation, narrow reversible correction and regression; this task creates no persistent personal DNS allowlist or unrestricted/raw AdGuard administration.\n- Anonymous journey deletion, support-case deletion, account deletion, saved-device deletion, dashboard unlink/revoke, and physical DNS removal remain distinct evidence-backed operations. Account/dashboard state cannot create technical DNS protection or removal evidence.\n- Support-burden metrics use only the current TSK-0498 event vocabulary. Operational `recovery_operation_outcome` remains intentionally non-user-correlated; unsupported metrics are explicitly not computable rather than expanding telemetry.\n- No browsing/query/activity history, child surveillance data, persistent analytics identity, secret, or backdoor DNS-history analytics is authorized.\n- Runtime acceptance does not alter WBS, graph, manifest, AdGuard, Quad9 dns10/ECS policy, or the CR-0008 owner-frozen planning baseline.\n- **Non-inference:** no support implementation/staffing outcome, human response capacity, LG-07, build, deployment, production activation, market activation, launch, legal-compliance completion, or real-user supportability becomes PASS from this L4 requirements task.'''
STATE.write_text(state.rstrip()+'\n\n'+sec+'\n',encoding='utf-8')
print('ACC_0042=PASS\nVER_0042=PASS\nEVD_0042=PASS\nTSK0042_STATE_CANDIDATE=PASS')
