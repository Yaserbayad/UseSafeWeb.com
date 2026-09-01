#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, re, sys

ROOT=Path(__file__).resolve().parent

def fail(msg):
    raise SystemExit(msg)

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

version=(ROOT/'VERSION').read_text(encoding='utf-8').strip()
if version != '1.0.0': fail('bundle version mismatch')
a=json.loads((ROOT/'bundle.json').read_text(encoding='utf-8'))
e=json.loads((ROOT/'endpoints.json').read_text(encoding='utf-8'))
if a.get('artifact_schema') != 'usesafeweb.adguard-recovery-bundle.v1': fail('artifact schema mismatch')
if a.get('bundle_version') != version: fail('bundle metadata version mismatch')
if a.get('task_id') != 'TSK-0413' or a.get('acceptance_id') != 'ACC-0413': fail('task binding mismatch')
compat=a['compatibility']
if compat != {
    'adguard_home_version':'v0.107.79',
    'config_schema_version':34,
    'official_tag_commit':'8e680e58c43cc7ae4fe38b3fbb4710024c687c3a',
    'policy':'Exact-version compatibility only. Any AdGuard Home version or schema change requires re-verification before this bundle is used.'
}: fail('compatibility contract mismatch')
identity=a['identity']
if identity != {
    'service_name':'UseSafeWeb DNS',
    'resolver_hostname':'dns.usesafeweb.com',
    'doh_url':'https://dns.usesafeweb.com/dns-query',
    'dot_hostname':'dns.usesafeweb.com'
}: fail('service identity mismatch')
if e['resolver_hostname'] != identity['resolver_hostname'] or e['doh_url'] != identity['doh_url']: fail('endpoint identity mismatch')
admin=a['admin_policy']
if admin['bind_address'] != '127.0.0.1:3000' or admin['public_exposure'] is not False or admin['authentication_required'] is not True: fail('admin policy mismatch')
if admin['credential_material'] != 'EXTERNAL_REQUIRED_NOT_VERSIONED' or admin['browser_receives_admin_credentials'] is not False: fail('admin secret policy mismatch')
settings=a['settings']; dns=settings['dns']
if settings['schema_version'] != 34: fail('schema mismatch')
if settings['http'] != {'address':'127.0.0.1:3000','doh':{'insecure_enabled':True}}: fail('http/admin binding mismatch')
if dns['bind_hosts'] != ['127.0.0.1'] or dns['port'] != 53: fail('dns bind mismatch')
if dns['upstream_dns'] != ['https://dns10.quad9.net/dns-query'] or dns['fallback_dns'] != [] or dns['private_upstream'] != []: fail('upstream mismatch')
if dns['edns_client_subnet'] != {'enabled':False,'use_custom':False,'custom_ip':''}: fail('ECS mismatch')
if dns['anonymize_client_ip'] is not True: fail('anonymization disabled')
if settings['querylog'] != {'enabled':False,'file_enabled':False,'interval':'1d'}: fail('querylog baseline mismatch')
if settings['statistics'] != {'enabled':True,'interval':'1d'}: fail('statistics baseline mismatch')
filters=settings['filters']
if filters != [{'name':'AdGuard DNS filter','url':'https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt','enabled':True}]: fail('filter baseline mismatch')
if settings['whitelist_filters'] != [] or settings['user_rules'] != []: fail('allowlist/rules baseline mismatch')
if settings['tls'] != {'enabled':False,'force_https':False,'port_dns_over_quic':853,'port_dns_over_tls':853,'port_https':443,'server_name':''}: fail('AdGuard TLS topology mismatch')
if settings['dhcp'] != {'enabled':False}: fail('DHCP mismatch')
if (ROOT/'allowlist.txt').read_bytes() != b'': fail('initial allowlist must be empty')

forbidden_exact_keys={'password','password_hash','hashed_password','private_key','certificate_chain','api_key','bearer_token','users','clients','client_id','client_identifier','raw_query_history','query_history'}
allowed_secret_policy_keys={'credential_material','adguard_admin_credential_source'}

def walk(v,path=''):
    if isinstance(v,dict):
        for k,x in v.items():
            lk=str(k).lower()
            if lk in forbidden_exact_keys and lk not in allowed_secret_policy_keys:
                fail('forbidden key in bundle: '+path+'/'+str(k))
            walk(x,path+'/'+str(k))
    elif isinstance(v,list):
        for i,x in enumerate(v): walk(x,path+'/'+str(i))
walk(a); walk(e)

combined='\n'.join(p.read_text(encoding='utf-8',errors='strict') for p in ROOT.iterdir() if p.is_file() and p.name != 'SHA256SUMS')
for pat in [r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',r'ADGUARD_ADMIN_PASSWORD\s*=',r'\bquerylog\.json\b']:
    if re.search(pat,combined,re.I): fail('forbidden secret/history content detected')

sum_path=ROOT/'SHA256SUMS'
if not sum_path.is_file(): fail('missing SHA256SUMS')
seen={}
for line in sum_path.read_text(encoding='utf-8').splitlines():
    if not line.strip(): continue
    h,name=line.split('  ',1)
    p=ROOT/name
    if not p.is_file(): fail('checksum target missing: '+name)
    if name == 'SHA256SUMS': fail('SHA256SUMS must not self-reference')
    if sha256(p) != h: fail('checksum mismatch: '+name)
    seen[name]=h
expected={p.name for p in ROOT.iterdir() if p.is_file() and p.name != 'SHA256SUMS'}
if set(seen) != expected: fail('checksum coverage mismatch')
print('TSK_0413_BUNDLE_VERIFY=PASS')
print('bundle_version='+version)
print('adguard_home_version=v0.107.79')
print('config_schema_version=34')
print('checksum_files='+str(len(seen)))
