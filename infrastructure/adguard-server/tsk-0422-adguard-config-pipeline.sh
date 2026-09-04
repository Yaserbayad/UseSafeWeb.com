#!/usr/bin/env bash
set -Eeuo pipefail

MODE="${1:---verify}"
case "${MODE}" in
  --verify|--apply|--negative-self-test) ;;
  *) echo "Usage: $0 [--verify|--apply|--negative-self-test]" >&2; exit 64 ;;
esac

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
APPROVED="${SCRIPT_DIR}/approved-adguard-config-v1.json"
CONFIG="/opt/AdGuardHome/AdGuardHome.yaml"
SECRET="/var/lib/usesafeweb/adguard/admin.env"
BASE="http://127.0.0.1:3000/control"
TSK0243_REWRITE_ENV="${USESAFEWEB_TSK0243_REWRITE_ENV:-/etc/usesafeweb/verifier-rewrite.env}"
TSK0243_VERIFIER_RULE=""
TMP="$(mktemp -d /tmp/usesafeweb-tsk0422.XXXXXX)"
BACKUP=""
REPLACED=0
SUCCESS=0

fail(){ printf 'FAIL %s\n' "$*" >&2; exit 1; }
pass(){ printf 'PASS %s\n' "$*"; }

cleanup(){
  rc=$?
  if [[ "${REPLACED}" == "1" && "${SUCCESS}" != "1" && -n "${BACKUP}" && -f "${BACKUP}" ]]; then
    systemctl stop AdGuardHome.service >/dev/null 2>&1 || true
    cp --preserve=mode,ownership,timestamps "${BACKUP}" "${CONFIG}" >/dev/null 2>&1 || true
    systemctl start AdGuardHome.service >/dev/null 2>&1 || true
  fi
  [[ -z "${BACKUP}" ]] || rm -f "${BACKUP}" >/dev/null 2>&1 || true
  rm -rf "${TMP}" >/dev/null 2>&1 || true
  exit "${rc}"
}
trap cleanup EXIT

[[ -f "${APPROVED}" ]] || fail "approved artifact missing"
python3 -c 'import yaml' >/dev/null 2>&1 || fail "python3 PyYAML unavailable"

validate_approved(){
  python3 - "${APPROVED}" <<'PY'
import json, sys
p=sys.argv[1]
d=json.load(open(p,encoding='utf-8'))
assert d.get('artifact_schema') == 'usesafeweb.adguard-approved-config.v1'
assert d.get('artifact_version') == '1.1.0'
s=d['settings']; dns=s['dns']; q=s['querylog']; st=s['statistics']; fl=s['filtering']
assert dns.get('upstream_dns') == ['https://dns10.quad9.net/dns-query']
assert dns.get('fallback_dns') == []
assert dns.get('private_upstream') == []
assert dns.get('upstream_dns_file') == ''
assert (dns.get('edns_client_subnet') or {}).get('enabled') is False
assert (dns.get('edns_client_subnet') or {}).get('use_custom') is False
assert dns.get('anonymize_client_ip') is True
assert q.get('enabled') is False and q.get('file_enabled') is False
assert st.get('enabled') is False
assert fl.get('protection_enabled') is True and fl.get('filtering_enabled') is True
assert s.get('dhcp',{}).get('enabled') is False
active=[x.get('url') for x in s.get('filters',[]) if x.get('enabled')]
assert active == ['https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt']
assert s.get('user_rules') == []
assert s.get('whitelist_filters') == []
print('APPROVED_ARTIFACT_INVARIANTS=PASS')
PY
}

negative_self_test(){
  python3 - "${APPROVED}" <<'PY'
import copy, json, sys
base=json.load(open(sys.argv[1],encoding='utf-8'))

def valid(d):
    s=d['settings']; dns=s['dns']; q=s['querylog']; st=s['statistics']; fl=s['filtering']
    active=[x.get('url') for x in s.get('filters',[]) if x.get('enabled')]
    return (
      dns.get('upstream_dns') == ['https://dns10.quad9.net/dns-query'] and
      (dns.get('fallback_dns') or []) == [] and (dns.get('private_upstream') or []) == [] and not dns.get('upstream_dns_file') and
      bool((dns.get('edns_client_subnet') or {}).get('enabled')) is False and
      bool((dns.get('edns_client_subnet') or {}).get('use_custom')) is False and
      dns.get('anonymize_client_ip') is True and
      q.get('enabled') is False and q.get('file_enabled') is False and
      st.get('enabled') is False and
      fl.get('protection_enabled') is True and fl.get('filtering_enabled') is True and
      active == ['https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt'] and
      d['settings'].get('user_rules') == [] and d['settings'].get('whitelist_filters') == []
    )

def semantic(s):
    dns=s.get('dns') or {}; ecs=dns.get('edns_client_subnet') or {}; fl=s.get('filtering') or {}; http=s.get('http') or {}; doh=http.get('doh') or {}
    return {
      'upstream_dns': list(dns.get('upstream_dns') or []),
      'fallback_dns': list(dns.get('fallback_dns') or []),
      'private_upstream': list(dns.get('private_upstream') or []),
      'upstream_dns_file': dns.get('upstream_dns_file') or '',
      'ecs_enabled': bool(ecs.get('enabled')),
      'ecs_use_custom': bool(ecs.get('use_custom')),
      'safesearch_enabled': bool(fl.get('safesearch_enabled')),
      'doh_insecure_enabled': bool(doh.get('insecure_enabled')),
    }

assert valid(base)
mut=[]
x=copy.deepcopy(base); x['settings']['querylog']['enabled']=True; mut.append(('query_logging',x))
x=copy.deepcopy(base); x['settings']['dns']['edns_client_subnet']['enabled']=True; mut.append(('ecs',x))
x=copy.deepcopy(base); x['settings']['dns']['upstream_dns']=['https://dns.google/dns-query']; mut.append(('wrong_upstream',x))
x=copy.deepcopy(base); x['settings']['filters'].append({'enabled':True,'name':'unapproved','url':'https://example.invalid/list.txt'}); mut.append(('unapproved_filter_processor',x))
for name,case in mut:
    if valid(case): raise SystemExit(f'negative fixture accepted: {name}')
    print(f'NEGATIVE_{name.upper()}=REJECTED')
print('NEGATIVE_SELF_TEST=PASS')

runtime=copy.deepcopy(base['settings'])
runtime['dns']['edns_client_subnet']['custom_ip']=''
runtime['dns']['edns_client_subnet'].pop('custom_ip_configured',None)
runtime['dns'].pop('private_upstream',None)
runtime['filtering'].pop('safesearch_enabled',None)
runtime['http']['doh']['routes']=['/dns-query']
assert semantic(runtime) == semantic(base['settings'])
print('NORMALIZATION_SELF_TEST=PASS')
PY
}

validate_approved
if [[ "${MODE}" == "--negative-self-test" ]]; then
  negative_self_test
  SUCCESS=1
  exit 0
fi

[[ "${EUID}" == "0" ]] || fail "run as root"
[[ "$(hostname -s)" == "adguardvm" ]] || fail "wrong target host"
if [[ "${USESAFEWEB_TSK0243_REQUIRED:-0}" == "1" && ! -f "${TSK0243_REWRITE_ENV}" ]]; then
  fail "required TSK-0243 rewrite input is missing"
fi
if [[ -e "${TSK0243_REWRITE_ENV}" ]]; then
  [[ -f "${TSK0243_REWRITE_ENV}" ]] || fail "TSK-0243 rewrite input is not a regular file"
  [[ "$(stat -c '%a %U:%G' "${TSK0243_REWRITE_ENV}")" == "600 root:root" ]] || fail "TSK-0243 rewrite input permissions invalid"
  verifier_ipv4="$(awk -F= '$1=="TSK0243_VERIFIER_IPV4" {sub(/^[^=]*=/,""); print; exit}' "${TSK0243_REWRITE_ENV}")"
  TSK0243_VERIFIER_RULE="$(python3 - "${verifier_ipv4}" <<'PY'
import ipaddress,sys
address=ipaddress.ip_address(sys.argv[1])
assert address.version == 4
assert not any((address.is_unspecified,address.is_loopback,address.is_link_local,address.is_multicast))
print(r'/^[0-9a-f]{32}\.verify\.usesafeweb\.com$/$dnsrewrite=NOERROR;A;'+str(address))
PY
)" || fail "TSK-0243 verifier address invalid"
  export TSK0243_VERIFIER_RULE
fi
[[ -f "${CONFIG}" ]] || fail "AdGuardHome.yaml missing"
[[ -f "${SECRET}" ]] || fail "admin credential file missing"
[[ "$(stat -c '%a %U:%G' "${SECRET}")" == "600 root:root" ]] || fail "admin credential file permissions invalid"
systemctl is-active --quiet AdGuardHome.service || fail "AdGuard Home service inactive"

username="$(awk -F= '$1=="ADGUARD_ADMIN_USER" {sub(/^[^=]*=/,""); print; exit}' "${SECRET}")"
password="$(awk -F= '$1=="ADGUARD_ADMIN_PASSWORD" {sub(/^[^=]*=/,""); print; exit}' "${SECRET}")"
[[ -n "${username}" && -n "${password}" ]] || fail "admin credential unavailable"
curl_auth(){ curl --silent --show-error --fail --max-time 10 --user "${username}:${password}" "$@"; }
wait_api(){
  for _ in $(seq 1 100); do
    if curl_auth -o /dev/null "${BASE}/status" 2>/dev/null; then return 0; fi
    sleep 0.1
  done
  return 1
}

projection_and_candidate(){
  python3 - "${APPROVED}" "${CONFIG}" "${TMP}/candidate.yaml" "${TMP}/before.json" "${TMP}/desired.json" "${TMP}/changes.txt" <<'PY'
import copy, hashlib, json, os, sys, yaml
approved_path, live_path, candidate_path, before_path, desired_path, changes_path=sys.argv[1:]
a=json.load(open(approved_path,encoding='utf-8'))['settings']
expected_user_rules=[os.environ['TSK0243_VERIFIER_RULE']] if os.environ.get('TSK0243_VERIFIER_RULE') else []
a=copy.deepcopy(a); a['user_rules']=expected_user_rules
with open(live_path,encoding='utf-8') as f: live=yaml.safe_load(f) or {}
DIRECT={
 'dhcp': ('enabled',),
 'dns': ('anonymize_client_ip','bind_hosts','bootstrap_dns','cache_optimistic','cache_size','cache_ttl_max','cache_ttl_min','fallback_dns','port','ratelimit','ratelimit_subnet_len_ipv4','ratelimit_subnet_len_ipv6','ratelimit_whitelist','refuse_any','upstream_dns','upstream_dns_file','upstream_mode'),
 'filtering': ('blocking_mode','filtering_enabled','parental_enabled','protection_enabled','safebrowsing_enabled'),
 'http': ('address',),
 'querylog': ('enabled','file_enabled','interval'),
 'statistics': ('enabled','interval'),
 'tls': ('enabled','force_https','port_dns_over_quic','port_dns_over_tls','port_https','server_name'),
}
TOP=('user_rules','whitelist_filters')
def projection(obj):
    out={}
    for section,keys in DIRECT.items():
        src=obj.get(section) or {}; out[section]={k:copy.deepcopy(src.get(k)) for k in keys}
    dns=obj.get('dns') or {}; ecs=dns.get('edns_client_subnet') or {}
    out['dns']['private_upstream']=list(dns.get('private_upstream') or [])
    out['dns']['edns_client_subnet']={'enabled':bool(ecs.get('enabled')),'use_custom':bool(ecs.get('use_custom'))}
    fl=obj.get('filtering') or {}; out['filtering']['safesearch_enabled']=bool(fl.get('safesearch_enabled'))
    http=obj.get('http') or {}; doh=http.get('doh') or {}; out['http']['doh']={'insecure_enabled':bool(doh.get('insecure_enabled'))}
    for k in TOP: out[k]=copy.deepcopy(obj.get(k))
    out['filters']=[{k:x.get(k) for k in ('enabled','name','url')} for x in (obj.get('filters') or [])]
    return out
def patch(base):
    out=copy.deepcopy(base)
    for section,keys in DIRECT.items():
        if not isinstance(out.get(section),dict): out[section]={}
        for k in keys: out[section][k]=copy.deepcopy(a[section][k])
    if not isinstance(out['dns'].get('edns_client_subnet'),dict): out['dns']['edns_client_subnet']={}
    out['dns']['edns_client_subnet']['enabled']=bool((a['dns'].get('edns_client_subnet') or {}).get('enabled'))
    out['dns']['edns_client_subnet']['use_custom']=bool((a['dns'].get('edns_client_subnet') or {}).get('use_custom'))
    out['dns']['private_upstream']=copy.deepcopy(a['dns'].get('private_upstream') or [])
    out['filtering']['safesearch_enabled']=bool(a['filtering'].get('safesearch_enabled'))
    if not isinstance(out['http'].get('doh'),dict): out['http']['doh']={}
    out['http']['doh']['insecure_enabled']=bool((a['http'].get('doh') or {}).get('insecure_enabled'))
    for k in TOP: out[k]=copy.deepcopy(a[k])
    desired_filters=[{k:x.get(k) for k in ('enabled','name','url')} for x in (a.get('filters') or [])]
    by_url={x.get('url'):copy.deepcopy(x) for x in (base.get('filters') or [])}
    rebuilt=[]
    for want in desired_filters:
        cur=by_url.get(want.get('url'))
        if cur is None: raise SystemExit('cannot safely synthesize missing filter runtime identity: '+str(want.get('url')))
        cur['enabled']=want.get('enabled'); cur['name']=want.get('name'); cur['url']=want.get('url'); rebuilt.append(cur)
    out['filters']=rebuilt
    return out
def strip_controlled(obj):
    out=copy.deepcopy(obj)
    for section,keys in DIRECT.items():
        if isinstance(out.get(section),dict):
            for k in keys: out[section].pop(k,None)
    dns=out.get('dns') or {}; dns.pop('private_upstream',None)
    ecs=dns.get('edns_client_subnet')
    if isinstance(ecs,dict): ecs.pop('enabled',None); ecs.pop('use_custom',None)
    fl=out.get('filtering') or {}; fl.pop('safesearch_enabled',None)
    http=out.get('http') or {}; doh=http.get('doh')
    if isinstance(doh,dict): doh.pop('insecure_enabled',None)
    for k in TOP: out.pop(k,None)
    out.pop('filters',None)
    return out
before=projection(live); desired=projection(a); candidate=patch(live)
assert projection(candidate)==desired
assert strip_controlled(candidate)==strip_controlled(live)
changes=[]
def walk(prefix,x,y):
    if isinstance(x,dict) and isinstance(y,dict):
        for k in sorted(set(x)|set(y)): walk(prefix+[str(k)],x.get(k),y.get(k))
    elif x!=y: changes.append('.'.join(prefix))
walk([],before,desired)
with open(candidate_path,'w',encoding='utf-8') as f: yaml.safe_dump(candidate,f,sort_keys=False,default_flow_style=False)
json.dump(before,open(before_path,'w',encoding='utf-8'),sort_keys=True,separators=(',',':'))
json.dump(desired,open(desired_path,'w',encoding='utf-8'),sort_keys=True,separators=(',',':'))
open(changes_path,'w',encoding='utf-8').write('\n'.join(changes)+'\n' if changes else '')
print('SANITIZED_CHANGE_COUNT='+str(len(changes)))
print('LIVE_PROJECTION_SHA256='+hashlib.sha256(open(before_path,'rb').read()).hexdigest())
print('APPROVED_PROJECTION_SHA256='+hashlib.sha256(open(desired_path,'rb').read()).hexdigest())
if changes: print('SANITIZED_CHANGED_PATHS='+','.join(changes))
else: print('SANITIZED_CHANGED_PATHS=none')
PY
}

verify_persisted(){
  python3 - "${APPROVED}" "${CONFIG}" <<'PY'
import json, os, sys, yaml
a=json.load(open(sys.argv[1],encoding='utf-8'))['settings']
expected_user_rules=[os.environ['TSK0243_VERIFIER_RULE']] if os.environ.get('TSK0243_VERIFIER_RULE') else []
a=dict(a); a['user_rules']=expected_user_rules
with open(sys.argv[2],encoding='utf-8') as f: live=yaml.safe_load(f) or {}
checks=[]
def eq(path,x,y):
    if x!=y: raise SystemExit(f'drift:{path}')
    checks.append(path)
direct={
 'dhcp': ('enabled',),
 'dns': ('anonymize_client_ip','bind_hosts','bootstrap_dns','cache_optimistic','cache_size','cache_ttl_max','cache_ttl_min','fallback_dns','port','ratelimit','ratelimit_subnet_len_ipv4','ratelimit_subnet_len_ipv6','ratelimit_whitelist','refuse_any','upstream_dns','upstream_dns_file','upstream_mode'),
 'filtering': ('blocking_mode','filtering_enabled','parental_enabled','protection_enabled','safebrowsing_enabled'),
 'http': ('address',),
 'querylog': ('enabled','file_enabled','interval'),
 'statistics': ('enabled','interval'),
 'tls': ('enabled','force_https','port_dns_over_quic','port_dns_over_tls','port_https','server_name'),
}
for section,keys in direct.items():
    for k in keys: eq(f'{section}.{k}',(live.get(section) or {}).get(k),a[section][k])
dns=live.get('dns') or {}; adns=a.get('dns') or {}; ecs=dns.get('edns_client_subnet') or {}; aecs=adns.get('edns_client_subnet') or {}
eq('dns.private_upstream',list(dns.get('private_upstream') or []),list(adns.get('private_upstream') or []))
eq('dns.edns_client_subnet.enabled',bool(ecs.get('enabled')),bool(aecs.get('enabled')))
eq('dns.edns_client_subnet.use_custom',bool(ecs.get('use_custom')),bool(aecs.get('use_custom')))
eq('filtering.safesearch_enabled',bool((live.get('filtering') or {}).get('safesearch_enabled')),bool((a.get('filtering') or {}).get('safesearch_enabled')))
eq('http.doh.insecure_enabled',bool(((live.get('http') or {}).get('doh') or {}).get('insecure_enabled')),bool(((a.get('http') or {}).get('doh') or {}).get('insecure_enabled')))
norm=lambda xs:[{k:x.get(k) for k in ('enabled','name','url')} for x in (xs or [])]
eq('filters',norm(live.get('filters')),norm(a.get('filters')))
for k in ('user_rules','whitelist_filters'): eq(k,live.get(k),a[k])
print('PERSISTED_APPROVED_FIELDS='+str(len(checks)))
print('PERSISTED_CONFIG_MATCH=PASS')
PY
}

runtime_verify(){
  curl_auth "${BASE}/status" -o "${TMP}/status.json"
  curl_auth "${BASE}/dns_info" -o "${TMP}/dns.json"
  curl_auth "${BASE}/querylog/config" -o "${TMP}/querylog.json"
  curl_auth "${BASE}/stats/config" -o "${TMP}/stats.json"
  curl_auth "${BASE}/filtering/status" -o "${TMP}/filtering.json"
  python3 - "${TMP}/status.json" "${TMP}/dns.json" "${TMP}/querylog.json" "${TMP}/stats.json" "${TMP}/filtering.json" <<'PY'
import json,os,sys
status,dns,q,st,fl=[json.load(open(p,encoding='utf-8')) for p in sys.argv[1:]]
assert status.get('protection_enabled') is True
assert dns.get('upstream_dns') == ['https://dns10.quad9.net/dns-query'], dns.get('upstream_dns')
assert dns.get('fallback_dns') in ([],None)
assert q.get('enabled') is False
assert st.get('enabled') is False
active=[x.get('url') for x in fl.get('filters',[]) if x.get('enabled')]
assert active == ['https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt'], active
expected_user_rules=[os.environ['TSK0243_VERIFIER_RULE']] if os.environ.get('TSK0243_VERIFIER_RULE') else []
assert (fl.get('user_rules') or []) == expected_user_rules
print('RUNTIME_APPROVED_CONFIG=PASS')
PY

  python3 - <<'PY'
import random,socket,struct
name='example.com'
q=b''.join(bytes([len(x)])+x.encode() for x in name.split('.'))+b'\x00'
pkt=struct.pack('!HHHHHH',random.randrange(0,65536),0x0100,1,0,0,0)+q+struct.pack('!HH',1,1)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM); s.settimeout(5); s.sendto(pkt,('127.0.0.1',53))
data,_=s.recvfrom(4096)
if len(data)<12: raise SystemExit('short DNS response')
flags=struct.unpack('!H',data[2:4])[0]; rcode=flags & 0xF
if rcode not in (0,3): raise SystemExit(f'unexpected DNS rcode={rcode}')
print('SYNTHETIC_LOOPBACK_DNS=PASS')
PY
}

projection_and_candidate
negative_self_test

if [[ "${MODE}" == "--apply" ]]; then
  if [[ -s "${TMP}/changes.txt" ]]; then
    BACKUP="$(mktemp /var/lib/usesafeweb/adguard/AdGuardHome.yaml.tsk0422.XXXXXX)"
    cp --preserve=mode,ownership,timestamps "${CONFIG}" "${BACKUP}"
    chmod 600 "${BACKUP}"
    [[ "$(stat -c '%a %U:%G' "${BACKUP}")" == "600 root:root" ]] || fail "rollback copy not root restricted"

    old_mode="$(stat -c '%a' "${CONFIG}")"; old_uid="$(stat -c '%u' "${CONFIG}")"; old_gid="$(stat -c '%g' "${CONFIG}")"
    install -o "${old_uid}" -g "${old_gid}" -m "${old_mode}" "${TMP}/candidate.yaml" "${CONFIG}.tsk0422.new"
    systemctl stop AdGuardHome.service
    mv "${CONFIG}.tsk0422.new" "${CONFIG}"
    REPLACED=1
    systemctl start AdGuardHome.service
    wait_api || fail "control API failed after apply"
    pass "approved configuration applied with rollback protection"
  else
    pass "target already matches approved configuration; apply is idempotent no-op"
  fi
fi

verify_persisted
runtime_verify

[[ "$(stat -c '%a %U:%G' "${SECRET}")" == "600 root:root" ]] || fail "credential permissions drifted"
pass "secrets remain outside versioned approved artifact and sanitized evidence"
pass "rollback guard staged candidate plus root-only backup restore-on-failure is active"

unset password username
SUCCESS=1
printf 'ACC_0422=PASS\nVER_0422=PASS\nEVD_0422_SANITIZED_STATUS=PASS\n'
