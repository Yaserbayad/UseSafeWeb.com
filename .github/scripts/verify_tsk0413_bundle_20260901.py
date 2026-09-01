#!/usr/bin/env python3
from pathlib import Path
import csv, hashlib, json, subprocess, urllib.request

ROOT=Path('.')
BUNDLE=ROOT/'infrastructure/adguard-server/tsk-0413-bundle-v1'

def require(cond,msg):
    if not cond:
        raise SystemExit(msg)

def github_json(url):
    req=urllib.request.Request(url,headers={'Accept':'application/vnd.github+json','User-Agent':'UseSafeWeb-TSK-0413-verifier'})
    with urllib.request.urlopen(req,timeout=20) as r:
        return json.load(r)

with (ROOT/'Plans/Master/WBS/master-wbs.csv').open(encoding='utf-8-sig',newline='') as f:
    rows=list(csv.DictReader(f))
by={r['Task_ID']:r for r in rows}
r=by['TSK-0413']
require(r['Dependencies'].strip()=='TSK-0408','TSK-0413 dependency drift')
require(r['AI_Capability_A0_A4']=='A4' and r['Action_Authority']=='AUTO_ALLOWED','TSK-0413 authority drift')
require(r['Acceptance_ID']=='ACC-0413' and r['Verification_ID']=='VER-0413' and r['Evidence_ID']=='EVD-0413','TSK-0413 acceptance identity drift')
acc=r['Acceptance_Criteria'].lower()
for term in ['upstream','ecs','log','statistics','anonymization','filter','admin','no browsing history','secrets','checksums','version compatibility']:
    require(term in acc,'TSK-0413 acceptance missing '+term)

state=(ROOT/'CURRENT_STATE.md').read_text(encoding='utf-8')
require('## TSK-0408 current accepted stable state — 2026-09-01' in state,'current TSK-0408 PASS marker missing')
require('## TSK-0413 owner-approved privacy-first AdGuard baseline — 2026-09-01' in state,'owner baseline runtime marker missing')
require('This reconciliation does **not** mark `TSK-0413`' in state,'TSK-0413 must remain non-PASS before verifier')

dec=(ROOT/'Plans/Master/Registers/DECISIONS_TRIGGERS.md').read_text(encoding='utf-8')
for text in [
    'persistent raw query history and file query logging are off',
    '24-hour maximum and deleted',
    'minimum anonymized aggregate operational statistics may be enabled with 24-hour retention',
    'client IP anonymisation is on',
    'ECS is off',
    'browsing/activity-history metrics are prohibited',
]:
    require(text in dec,'DEC-0016 owner baseline missing: '+text)

subprocess.run(['python3',str(BUNDLE/'verify_bundle.py')],check=True)
new=json.loads((BUNDLE/'bundle.json').read_text(encoding='utf-8'))
old_path=ROOT/'infrastructure/adguard-server/approved-adguard-config-v1.json'
old=json.loads(old_path.read_text(encoding='utf-8'))
old_blob=subprocess.check_output(['git','hash-object',str(old_path)],text=True).strip()
require(old_blob=='e9975c4e75c2a68131f049da942468d8d1952d8d','prior approved config blob drift')
require(new['sources']['prior_safe_config_blob']==old_blob,'bundle prior-source binding mismatch')
require(old['target']['adguard_home_version']=='v0.107.79','prior target version drift')
require(new['compatibility']['adguard_home_version']==old['target']['adguard_home_version'],'bundle version must preserve prior supported target')

ns=new['settings']; os=old['settings']
for k in ['bind_hosts','bootstrap_dns','cache_optimistic','cache_size','cache_ttl_max','cache_ttl_min','fallback_dns','port','private_upstream','ratelimit','ratelimit_subnet_len_ipv4','ratelimit_subnet_len_ipv6','ratelimit_whitelist','refuse_any','upstream_dns','upstream_dns_file','upstream_mode','anonymize_client_ip']:
    require(ns['dns'][k]==os['dns'][k],'unexpected DNS baseline change: '+k)
require(ns['dns']['edns_client_subnet']['enabled'] is False and ns['dns']['edns_client_subnet']['use_custom'] is False,'ECS must remain disabled')
require(ns['http']==os['http'],'HTTP/admin loopback baseline changed')
require(ns['tls']==os['tls'],'inert AdGuard TLS topology changed')
require(ns['dhcp']==os['dhcp'],'DHCP baseline changed')
for k in ['blocking_mode','filtering_enabled','parental_enabled','protection_enabled','safebrowsing_enabled','safesearch_enabled']:
    require(ns['filtering'][k]==os['filtering'][k],'unexpected filtering baseline change: '+k)
require(ns['querylog']=={'enabled':False,'file_enabled':False,'interval':'1d'},'owner query-log baseline not encoded')
require(os['querylog']['enabled'] is False and os['querylog']['file_enabled'] is False,'prior query logging baseline unexpected')
require(ns['statistics']=={'enabled':True,'interval':'1d'},'owner 24h aggregate stats baseline not encoded')
require(os['statistics']=={'enabled':False,'interval':'1d'},'prior stats source unexpected')
require(ns['filters']==[{'name':'AdGuard DNS filter','url':'https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt','enabled':True}],'initial filter must be official-only')
require(any(x.get('name')=='AdAway Default Blocklist' and x.get('enabled') is False for x in os['filters']),'expected dormant historical filter source missing')
require(ns['whitelist_filters']==[] and ns['user_rules']==[],'initial exceptions must be empty')
require((BUNDLE/'allowlist.txt').read_bytes()==b'','versioned allowlist must start empty')
require(new['admin_policy']['bind_address']=='127.0.0.1:3000' and new['admin_policy']['public_exposure'] is False and new['admin_policy']['authentication_required'] is True,'private authenticated admin policy mismatch')
require(new['admin_policy']['browser_receives_admin_credentials'] is False,'browser admin credential exposure prohibited')
require(new['diagnostic_policy']['exceptional_query_diagnostics_maximum']=='24h','diagnostic maximum mismatch')
require(new['diagnostic_policy']['browsing_query_activity_history_prohibited'] is True,'history prohibition missing')

latest=github_json('https://api.github.com/repos/AdguardTeam/AdGuardHome/releases/latest')
require(latest.get('tag_name')=='v0.107.79','pinned AdGuard version is no longer latest official release')
ref=github_json('https://api.github.com/repos/AdguardTeam/AdGuardHome/git/ref/tags/v0.107.79')
obj=ref['object']
if obj['type']=='tag':
    tag=github_json(obj['url'])
    commit=tag['object']['sha']
else:
    commit=obj['sha']
require(commit=='05ba17b282da1c4393d6a4ba4db0cf519194a362','official v0.107.79 tag commit mismatch')
require(new['compatibility']['official_tag_commit']==commit,'bundle official tag binding mismatch')

subprocess.run(['python3','Plans/Master/Tools/validate_master_plan.py'],check=True)
subprocess.run(['git','diff','--check'],check=True)
require(subprocess.check_output(['git','status','--porcelain'],text=True).strip()=='','verification checkout is dirty')
print('TSK_0413_REPOSITORY_VERIFICATION=PASS')
print('prior_config_blob='+old_blob)
print('official_adguard_release=v0.107.79')
print('official_tag_commit=05ba17b282da1c4393d6a4ba4db0cf519194a362')
print('bundle_sha256='+hashlib.sha256((BUNDLE/'bundle.json').read_bytes()).hexdigest())
