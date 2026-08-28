#!/usr/bin/env python3
import csv, datetime, json, re, subprocess
from pathlib import Path

STATE=Path('CURRENT_STATE.md')
EVID=Path('TSK_0428_AZURE_REGION_DATA_PATH_EVIDENCE_2026-08-28.md')
QUEUE=Path('TSK_0428_QUEUE_RECOMPUTE_EVIDENCE_2026-08-28.md')
EXPECTED_STATE='b286cf2b0cb75c644895661bab624a9af456a251'
EXPECTED_EVID='bbcd27772f8a9cad8248c48e9290b52baf71056f'

def blob(p):
    return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()

if blob(STATE)!=EXPECTED_STATE:
    raise SystemExit(f'CURRENT_STATE stale: {blob(STATE)}')
if blob(EVID)!=EXPECTED_EVID:
    raise SystemExit(f'evidence mismatch: {blob(EVID)}')

state=STATE.read_text(encoding='utf-8')
pass_block=state.split('### PASS',1)[1].split('### TSK-0204 corrected stable state',1)[0]
if '`TSK-0428`' in pass_block:
    raise SystemExit('TSK-0428 already PASS')
now=datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
state=re.sub(r'\*\*Updated:\*\* [^\n]+',f'**Updated:** {now}  ',state,count=1)
anchor='- `TSK-0429` — privacy-minimal AdGuard backup scope documented and independently verified against current DPIA/retention/live state — policy: `infrastructure/adguard-server/BACKUP_SCOPE_POLICY.md`, blob `e62b48a3e746b1be90881bbffab3b7680384cc16`; evidence: `TSK_0429_PRIVACY_MINIMAL_BACKUP_SCOPE_EVIDENCE_2026-08-27.md`, blob `b77c6d7a2e17adc5e653151b55137467a8c5b62f`.\n'
addition='- `TSK-0428` — Azure region, recipients, and active DNS data path verified on production: Azure `westeurope`, Quad9 dns10 recursive/bootstrap path, loopback-only DoH/DoT backends, and no US DNS node/CDN/analytics/payment/email/application processor in the child-linked DNS query path — evidence: `TSK_0428_AZURE_REGION_DATA_PATH_EVIDENCE_2026-08-28.md`, blob `bbcd27772f8a9cad8248c48e9290b52baf71056f`.\n'
if anchor not in state: raise SystemExit('TSK-0429 anchor missing')
state=state.replace(anchor,addition+anchor,1)
section='''### TSK-0428 accepted stable state

`TSK-0428` — verify Azure region, recipients, and data path: **PASS**.

Fresh production evidence `TSK_0428_AZURE_REGION_DATA_PATH_EVIDENCE_2026-08-28.md`, blob `bbcd27772f8a9cad8248c48e9290b52baf71056f`, proves Azure IMDS location `westeurope` on VM `adguardvm` / VM ID `bc7f566f-7231-41fb-9fdd-49cf190fd5e1`; live AdGuard upstream exactly `https://dns10.quad9.net/dns-query` with Quad9 dns10 bootstrap addresses, no fallback/private upstream and ECS disabled; effective Nginx DoH/DoT proxy targets only same-host loopback backends; expected DNS listener topology; and no CDN, analytics, payment, email, US DNS node, or other application processor in the active child-linked DNS query path.

The first verifier run `33167781526` was rejected as a test false negative because it omitted the legitimate loopback DoT proxy from its expectation. No product mutation occurred. Corrected run `33167847368` passed fully and published the evidence. Microsoft IMDS and current Quad9 documentation were also checked on 2026-08-28 as source corroboration.

**ACC-0428 is fully satisfied. TSK-0428: PASS.** Azure control-plane configuration remains owner-managed and this PASS does not authorize participant activation or web/application deployment.

'''
marker='### External/provider and legal boundaries\n'
if marker not in state: raise SystemExit('boundary marker missing')
state=state.replace(marker,section+marker,1)

rows=list(csv.DictReader(open('Plans/Master/WBS/master-wbs.csv',newline='',encoding='utf-8-sig')))
pass_block=state.split('### PASS',1)[1].split('### TSK-0204 corrected stable state',1)[0]
runtime_pass=set(re.findall(r'`(TSK-\d+)`\s+—',pass_block)); runtime_pass.add('TSK-0011')
runtime_wait=set(re.findall(r'### WAITING — (TSK-\d+)',state))
planning_pass={r['Task_ID'].strip() for r in rows if (r.get('Execution_State') or '').strip()=='PASS'}
satisfied=runtime_pass|planning_pass
rank={'CRITICAL':0,'HIGH':1,'MEDIUM':2,'LOW':3}
ready=[]
for i,r in enumerate(rows):
    tid=(r.get('Task_ID') or '').strip()
    if not tid or tid in runtime_pass or tid in runtime_wait: continue
    if (r.get('Lifecycle_Stage') or '').strip()!='L2': continue
    if (r.get('Action_Authority') or '').strip()!='AUTO_ALLOWED': continue
    if (r.get('Plan_Status') or '').strip() not in {'PLANNED','ACTIVE'}: continue
    deps=[x.strip() for x in (r.get('Dependencies') or '').split(';') if x.strip()]
    if all(d in satisfied for d in deps): ready.append((i,r,deps))
ready.sort(key=lambda x:(rank.get((x[1].get('Priority') or '').strip(),9),x[0],x[1]['Task_ID']))
ql=['# Queue Recompute Evidence after TSK-0428 PASS','', '**Date:** 2026-08-28','',f'- Pre-mutation CURRENT_STATE blob: `{EXPECTED_STATE}`',f'- TSK-0428 evidence blob: `{EXPECTED_EVID}`',f'- Runtime PASS count after local reconciliation (including TSK-0011 sentinel): `{len(runtime_pass)}`',f'- Runtime WAIT: `{",".join(sorted(runtime_wait)) or "none"}`',f'- L2 AUTO_ALLOWED dependency-ready count: `{len(ready)}`','','## Dependency-ready tasks','']
if not ready: ql.append('None.')
else:
    for _,r,_ in ready[:40]:
        ql += [f"### {r.get('Task_ID','')} — {r.get('Title','')}",'',f"- Priority: `{r.get('Priority','')}`",f"- Critical path: `{r.get('Critical_Path','')}`",f"- Plan status: `{r.get('Plan_Status','')}`",f"- WBS execution snapshot: `{r.get('Execution_State','')}`",f"- Dependencies: `{r.get('Dependencies','')}`",f"- Action authority: `{r.get('Action_Authority','')}`",f"- Acceptance: `{r.get('Acceptance_ID','')}` — {r.get('Acceptance_Criteria','')}",f"- Verification: `{r.get('Verification_ID','')}`",f"- Required tools/access: {r.get('Required_Tools_or_Access','')}",f"- Requirement refs: `{r.get('Requirement_Reference','')}`",f"- Interface refs: `{r.get('Interface_Reference','')}`",f"- Risk refs: `{r.get('Risk_Reference','')}`",f"- Trigger: {r.get('Trigger','')}",f"- Preconditions: {r.get('Preconditions','')}",'']
ql += ['## Selection note','','Dependency readiness alone does not authorize execution; every candidate still requires current gate/trigger/constraint/interface/platform/authority preflight and direct acceptance evidence.','']
QUEUE.write_text('\n'.join(ql),encoding='utf-8')

tail='## Queue status after current reconciliation\n\n'
tail+=f'TSK-0428 is runtime PASS with fresh target evidence. The deterministic WBS dependency-readiness recomputation found **{len(ready)}** L2 `AUTO_ALLOWED` candidate(s).\n\n'
if ready:
    first=ready[0][1]; tail+=f"Highest dependency-ready candidate: `{first.get('Task_ID','')}` — {first.get('Title','')}. Full current preflight remains required.\n\n"
else: tail+='No ordinary L2 `AUTO_ALLOWED` candidate is dependency-ready.\n\n'
tail+='Current explicit WAITING boundary:\n\n- `TSK-0431` — identify/provide the owner-managed Azure-native backup/restore path required by REQ-0052.\n\n## Exact next authoritative step\n\n'
if ready:
    first=ready[0][1]; tail+=f"Preflight `{first.get('Task_ID','')}` — {first.get('Title','')} against its exact acceptance, gates, trigger, requirements, constraints, interfaces, risk and available executor. Continue only if safe and authorized. "
else: tail+='No ordinary L2 work may progress until a dependency/gate condition changes. '
tail+='Separately, TSK-0431 remains WAITING on the owner-managed Azure-native backup/restore path. Do not bypass participant-activation, legal, Azure control-plane, provider, recovery, privacy or validation gates.\n'
state=state.split('## Queue status after current reconciliation\n',1)[0]+tail
STATE.write_text(state,encoding='utf-8')
print('READY_COUNT='+str(len(ready)))
for _,r,_ in ready[:10]: print('READY='+json.dumps({k:r.get(k,'') for k in ['Task_ID','Title','Priority','Critical_Path','Dependencies','Action_Authority','Acceptance_ID','Acceptance_Criteria','Verification_ID','Required_Tools_or_Access','Requirement_Reference','Interface_Reference','Risk_Reference','Trigger','Preconditions']},sort_keys=True,ensure_ascii=False))
