#!/usr/bin/env python3
import csv, os, re, subprocess
from pathlib import Path

BASE=Path('TSK_0041_BASELINE_DNS_PROTECTION_ACTIVATION_REQUIREMENTS_2026-08-28.md')
AMEND=Path('TSK_0041_POST_CR0008_CURRENT_REQUALIFICATION_AMENDMENT_2026-09-01.md')
S=Path('CURRENT_STATE.md')
W=Path('Plans/Master/WBS/master-wbs.csv')
L5=Path('Plans/Master/Layers/LAYER_5_AI_EXECUTION_EVIDENCE_STATE_CONTROL.md')
T143=Path('TSK_0143_NATIVE_DEVICE_SAFEGUARD_ROUTING_REQUIREMENTS_2026-09-01.md')
T320=Path('TSK_0320_POST_CR0008_PROTECTION_STATE_MODEL_AND_COPY_RULES_2026-09-01.md')
T409=Path('TSK_0409_SUPPORTED_DEVICE_NETWORK_VERIFICATION_BYPASS_MATRIX_2026-09-01.md')
T408=Path('TSK_0408_USESAFEWEB_DNS_IDENTITY_PLATFORM_ENDPOINT_PROFILE_CONTRACT_2026-08-28.md')

EXPECTED={
 'base':'95a5292223f1d2c3c8f79d4c889ad91e917478b2',
 'amend':'ec453677ab5638a130c67ab54ead4c1c300ba90b',
 'wbs':'b27a0c5df2f5636d8ed71051e9e26a68959a2616',
 'l5':'2097d83961affaa69850e41a5ffcd72a660d69cd',
 't143':'7eca238090738f282db2b43c7f988a7ff716df19',
 't320':'bdc6bacc424669708f410466f3cfd5527f1c2b3c',
 't409':'3aa832777276115912e4f3990b30cb541c458f4f',
 't408':'52860ce167fc8a31962cd412772e428d280c8184',
}

def h(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def req(cond,msg):
    if not cond: raise AssertionError(msg)

for key,path in [('base',BASE),('amend',AMEND),('wbs',W),('l5',L5),('t143',T143),('t320',T320),('t409',T409),('t408',T408)]:
    req(h(path)==EXPECTED[key],f'unexpected {key} blob: {h(path)}')
print('TSK0041_CURRENT_BLOBS=PASS')

with W.open(encoding='utf-8-sig',newline='') as f:
    r=next(x for x in csv.DictReader(f) if (x.get('Task_ID')or'').strip()=='TSK-0041')
req((r.get('Title')or'').strip()=='Specify baseline DNS-protection activation requirements','title mismatch')
req((r.get('Lifecycle_Stage')or'').strip()=='L4','lifecycle mismatch')
req((r.get('Priority')or'').strip()=='MEDIUM','priority mismatch')
req((r.get('AI_Capability_A0_A4')or'').strip()=='A3','capability mismatch')
req((r.get('Action_Authority')or'').strip()=='AUTO_ALLOWED','authority mismatch')
req((r.get('Dependencies')or'').strip()=='TSK-0143','dependency mismatch')
req((r.get('Acceptance_ID')or'').strip()=='ACC-0041','acceptance id mismatch')
req((r.get('Verification_ID')or'').strip()=='VER-0041','verification id mismatch')
req((r.get('Evidence_ID')or'').strip()=='EVD-0041','evidence id mismatch')
acc=(r.get('Acceptance_Criteria')or'').strip()
req(acc=='Requirements cover endpoint format, DoH setup, filtering verification, fail-safe behavior, uninstall/removal, Private Relay/VPN conflicts, false positives, and no-history constraints.',f'acceptance mismatch: {acc}')
print('TSK0041_WBS_CONTRACT=PASS')

state=S.read_text(encoding='utf-8')
for marker in [
 '## TSK-0143 current accepted stable state — 2026-09-01 — POST-CR-0008',
 '## TSK-0320 current accepted stable state — 2026-09-01 — POST-CR-0008',
 '## TSK-0409 current accepted stable state — 2026-09-01 — POST-CR-0008',
 '## TSK-0052 / LG-06 current accepted stable state — 2026-09-01 — POST-CR-0007',
]: req(marker in state,f'missing runtime marker: {marker}')
head='## TSK-0041 current accepted stable state — 2026-09-01 — POST-CR-0008'
req(head not in state,'TSK-0041 already current accepted')
print('TSK0041_DEPENDENCY_GATE_RUNTIME=PASS')

base=BASE.read_text(encoding='utf-8'); amend=AMEND.read_text(encoding='utf-8'); t143=T143.read_text(encoding='utf-8'); t320=T320.read_text(encoding='utf-8'); t409=T409.read_text(encoding='utf-8')
for m in ['dns.usesafeweb.com','https://dns.usesafeweb.com/dns-query','filtering verification','Fail-safe behavior','Removal and uninstall requirements','False-positive requirements','No-history privacy constraints']:
    req(m.lower() in base.lower(),f'base clause missing: {m}')
for m in [
 'static OS minimums are replaced by the current versioned support catalogue/matrix rule',
 'Generic similarity to an older supported major version is not support evidence.',
 '`protected_verified`','`configured_parent_confirmed`','`action_needed`','`not_covered`','`uncertain_error`','`removed`',
 'Private Relay is a resolver/network-path conflict boundary for UseSafeWeb claims.',
 'Chrome Secure DNS','Firefox DoH','optional parent account/lightweight dashboard/device-management surface',
 'no persistent per-parent/per-device DNS allowlist or unrestricted/raw AdGuard administration',
 'DEC-0052 / CR-0005','DEC-0053 / CR-0006','DEC-0054 / CR-0007','DEC-0055 / CR-0008',
 'LG-06 is already current PASS','RSK-0002 remains OPEN and non-blocking before L8',
]: req(m in amend,f'amendment clause missing: {m}')
for m in ['supported_action_needed','guidance_stale_or_uncertain','parent confirmation must never masquerade as system verification','accountless users receive the complete core routing experience']:
    req(m in t143,f'TSK-0143 current routing marker missing: {m}')
for m in ['`protected/verified` requires its own current qualifying technical evidence','A **qualifying positive E1** is the only evidence class that can establish `protected/verified`','configured/parent-confirmed','uncertain/error','removed']:
    req(m in t320,f'TSK-0320 truth marker missing: {m}')
for m in ['Android Private DNS/DoT hostname','Apple DoH profile/Server-URL','Chrome Secure DNS','Firefox','Private Relay','VPN','captive portal','network change','No DNS questions/domains/URLs/browsing history/child activity/persistent identity linkage']:
    req(m.lower() in t409.lower(),f'TSK-0409 marker missing: {m}')
print('TSK0041_CURRENT_SEMANTICS=PASS')

for m in [
 'Endpoint format | PASS candidate','DoH setup | PASS candidate','Filtering verification | PASS candidate','Fail-safe behavior | PASS candidate',
 'Uninstall/removal | PASS candidate','Private Relay/VPN conflicts | PASS candidate','False positives | PASS candidate','No-history constraints | PASS candidate'
]: req(m in amend,f'ACC clause disposition missing: {m}')
print('ACC_0041_CLAUSES=PASS')

for m in [
 'configuration/profile/ClientID/account/dashboard/parent-confirmation/journey-completion evidence cannot substitute',
 'no unsupported combination is silently routed into an app/VPN/browser-specific fallback',
 'no hidden unencrypted/plain-DNS fallback may retain a UseSafeWeb protection state',
 'no pre-L8 human validation, LG-07, implementation/build/release/production/market/launch PASS is inferred'
]: req(m.lower() in amend.lower(),f'negative assertion missing: {m}')
for pat in [r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',r'ghp_[A-Za-z0-9]{30,}',r'github_pat_[A-Za-z0-9_]{40,}',r'AKIA[0-9A-Z]{16}']:
    req(not re.search(pat,amend),f'secret-like pattern in amendment: {pat}')
print('TSK0041_NEGATIVE_SECRET_GUARD=PASS')

v=subprocess.run(['python3','Plans/Master/Tools/validate_master_plan.py'],text=True,capture_output=True,check=True)
print(v.stdout,end=''); combined=v.stdout+v.stderr
for m in ['VALIDATION PASS','tasks=641','dependency_edges=858','broken_links=0','generated_missing_task_ids=0']:
    req(m in combined,f'validator marker missing: {m}')

sec=f'''{head}\n\n`TSK-0041 — Specify baseline DNS-protection activation requirements`: **PASS** under current `ACC-0041 / VER-0041 / EVD-0041`, current `TSK-0143` dependency proof, and CR-0008 authority after bounded current requalification.\n\n- Action authority: **A3 / AUTO_ALLOWED**.\n- Preserved base contract: `TSK_0041_BASELINE_DNS_PROTECTION_ACTIVATION_REQUIREMENTS_2026-08-28.md`, blob `{EXPECTED['base']}`.\n- Current amendment: `TSK_0041_POST_CR0008_CURRENT_REQUALIFICATION_AMENDMENT_2026-09-01.md`, version `2.0.0-post-CR-0008`, blob `{EXPECTED['amend']}`.\n- Current consumed authority: TSK-0143 blob `{EXPECTED['t143']}`; TSK-0320 blob `{EXPECTED['t320']}`; TSK-0409 blob `{EXPECTED['t409']}`; accepted TSK-0408 endpoint/mechanism blob `{EXPECTED['t408']}`.\n- Verification source commit: `{os.environ['SOURCE_COMMIT']}`; GitHub Actions run/attempt `{os.environ.get('GITHUB_RUN_ID','UNKNOWN')} / {os.environ.get('GITHUB_RUN_ATTEMPT','1')}`.\n- Requalification disposition: base endpoint/filtering/fail-safe/removal/false-positive/no-history requirements are preserved; static OS-minimum support claims, old Private-Relay DNS overclaim, historical accountless-only/CR-0003 lifecycle wording, and old TSK-0409/TSK-0320 pointers are superseded by the current amendment.\n- Current truth rule: configuration/profile/ClientID/account/dashboard/parent confirmation cannot create `protected_verified`; only fresh qualifying technical evidence for the effective DNS/filtering path can. Unknown/stale/conflicting browser/VPN/Private-Relay/app/network paths fail closed to `uncertain_error` or `not_covered` under current TSK-0409/TSK-0143 semantics.\n- Current Version-1 scope remains complete accountless core plus optional parent account/lightweight dashboard/device management, with no browsing/query/activity history, child surveillance profile, persistent personal DNS allowlist or unrestricted DNS administration created by this task.\n- Full modular validator passed before runtime mutation; WBS, graph, manifest, planning modules, AdGuard, Quad9 dns10/ECS policy and CR-0008 planning baseline are unchanged.\n- **Non-inference:** no LG-07, implementation/build, release, production activation, market activation, launch, legal-compliance completion or real-user validation becomes PASS from this requirements requalification.'''
S.write_text(state.rstrip()+'\n\n'+sec+'\n',encoding='utf-8')
print('ACC_0041=PASS\nVER_0041=PASS\nEVD_0041=PASS\nTSK0041_STATE_CANDIDATE=PASS')
