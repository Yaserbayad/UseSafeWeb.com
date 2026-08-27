#!/usr/bin/env bash
set -Eeuo pipefail

BASE='http://127.0.0.1:3000/control'
SECRET='/var/lib/usesafeweb/adguard/admin.env'
CONFIG='/opt/AdGuardHome/AdGuardHome.yaml'
BACKUP=''
config_changed=0
success=0

fail(){ printf 'FAIL  %s\n' "$*" >&2; exit 1; }
pass(){ printf 'PASS  %s\n' "$*"; }

rollback(){
  rc=$?
  if [[ "$config_changed" == '1' && "$success" != '1' && -n "$BACKUP" ]] && sudo test -f "$BACKUP"; then
    sudo systemctl stop AdGuardHome.service >/dev/null 2>&1 || true
    sudo cp --preserve=mode,ownership,timestamps "$BACKUP" "$CONFIG" >/dev/null 2>&1 || true
    sudo systemctl start AdGuardHome.service >/dev/null 2>&1 || true
  fi
  if [[ -n "$BACKUP" ]]; then sudo rm -f "$BACKUP" >/dev/null 2>&1 || true; fi
  rm -f /tmp/usw-qlog-config-before.json /tmp/usw-qlog-config-target.json \
    /tmp/usw-qlog-config-after.json /tmp/usw-qlog-after-test.json
  exit "$rc"
}
trap rollback EXIT

sudo -n true || fail 'non-interactive sudo unavailable'
for c in curl python3 find systemctl; do command -v "$c" >/dev/null || fail "$c missing"; done
[[ "$(sudo stat -c '%a %U:%G' "$SECRET")" == '600 root:root' ]] || fail 'admin credential file is not root restricted'
systemctl is-active --quiet AdGuardHome.service || fail 'AdGuard Home service is not active'

username="$(sudo awk -F= '$1=="ADGUARD_ADMIN_USER" {sub(/^[^=]*=/,""); print; exit}' "$SECRET")"
password="$(sudo awk -F= '$1=="ADGUARD_ADMIN_PASSWORD" {sub(/^[^=]*=/,""); print; exit}' "$SECRET")"
[[ -n "$username" && -n "$password" ]] || fail 'admin credential unavailable'

curl_auth(){ curl --silent --show-error --fail --max-time 10 --user "$username:$password" "$@"; }
wait_control_api(){
  for _ in $(seq 1 100); do
    code="$(curl --silent --show-error --max-time 2 --user "$username:$password" -o /dev/null -w '%{http_code}' "$BASE/status" 2>/dev/null || true)"
    [[ "$code" == '200' ]] && return 0
    sleep 0.1
  done
  return 1
}

# Keep the supported runtime query-log API globally disabled and clear prior history.
curl_auth "$BASE/querylog/config" -o /tmp/usw-qlog-config-before.json
python3 - <<'PY'
import json
p='/tmp/usw-qlog-config-before.json'
d=json.load(open(p,encoding='utf-8'))
required=('enabled','interval','anonymize_client_ip','ignored')
for k in required:
    if k not in d: raise SystemExit(f'missing querylog config key: {k}')
d['enabled']=False
open('/tmp/usw-qlog-config-target.json','w',encoding='utf-8').write(json.dumps(d,separators=(',',':')))
PY
curl_auth --request PUT --header 'Content-Type: application/json' \
  --data-binary @/tmp/usw-qlog-config-target.json "$BASE/querylog/config/update" -o /dev/null
curl_auth --request POST "$BASE/querylog_clear" -o /dev/null
pass 'global query logging disabled and prior query log cleared'

# file_enabled is a separate persisted setting and is not exposed by the current
# /querylog/config API.  Edit only that scalar while AdGuard Home is stopped.
file_enabled="$(sudo python3 - "$CONFIG" <<'PY'
import sys, yaml
with open(sys.argv[1],encoding='utf-8') as f: d=yaml.safe_load(f)
q=d.get('querylog') or {}
print(str(bool(q.get('file_enabled'))).lower())
PY
)"

if [[ "$file_enabled" == 'true' ]]; then
  BACKUP="$(sudo mktemp /var/lib/usesafeweb/adguard/AdGuardHome.yaml.tsk0204.XXXXXX)"
  sudo cp --preserve=mode,ownership,timestamps "$CONFIG" "$BACKUP"
  sudo chmod 600 "$BACKUP"
  [[ "$(sudo stat -c '%a %U:%G' "$BACKUP")" == '600 root:root' ]] || fail 'rollback copy is not root restricted'

  sudo systemctl stop AdGuardHome.service
  config_changed=1
  sudo python3 - "$CONFIG" <<'PY'
import os, re, sys
path=sys.argv[1]
st=os.stat(path)
with open(path,encoding='utf-8') as f: lines=f.readlines()
in_querylog=False
replaced=0
for i,line in enumerate(lines):
    if line and not line[0].isspace() and line.strip().endswith(':'):
        in_querylog=(line.strip()=='querylog:')
        continue
    if in_querylog and re.match(r'^\s+file_enabled\s*:',line):
        indent=line[:len(line)-len(line.lstrip())]
        newline='\n' if line.endswith('\n') else ''
        lines[i]=f'{indent}file_enabled: false{newline}'
        replaced += 1
if replaced != 1:
    raise SystemExit(f'expected exactly one querylog.file_enabled field, found {replaced}')
tmp=path+'.tsk0204.tmp'
with open(tmp,'w',encoding='utf-8') as f:
    f.writelines(lines)
    f.flush(); os.fsync(f.fileno())
os.chmod(tmp,st.st_mode)
os.chown(tmp,st.st_uid,st.st_gid)
os.replace(tmp,path)
PY
  sudo systemctl start AdGuardHome.service
  systemctl is-active --quiet AdGuardHome.service || fail 'AdGuard Home did not restart after file logging correction'
  wait_control_api || fail 'AdGuard control API did not become ready after restart'
  pass 'querylog.file_enabled changed to false with rollback protection'
else
  pass 'querylog.file_enabled already false; no direct config edit required'
fi

# Verify both persisted scalars and all privacy/resolver/filter invariants before
# allowing the rollback copy to be discarded.
sudo python3 - "$CONFIG" <<'PY'
import sys, yaml
with open(sys.argv[1],encoding='utf-8') as f: d=yaml.safe_load(f)
q=d.get('querylog') or {}; dns=d.get('dns') or {}; stats=d.get('statistics') or {}; filtering=d.get('filtering') or {}
filters=d.get('filters') or []
assert q.get('enabled') is False, q.get('enabled')
assert q.get('file_enabled') is False, q.get('file_enabled')
assert dns.get('anonymize_client_ip') is True, dns.get('anonymize_client_ip')
assert stats.get('enabled') is False, stats.get('enabled')
assert list(dns.get('upstream_dns') or []) == ['https://dns10.quad9.net/dns-query']
assert bool((dns.get('edns_client_subnet') or {}).get('enabled')) is False
assert filtering.get('protection_enabled') is True
assert filtering.get('filtering_enabled') is True
active=[x.get('url') for x in filters if x.get('enabled')]
assert active == ['https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt'], active
assert (d.get('user_rules') or []) == []
print('persisted_querylog_enabled=false')
print('persisted_querylog_file_enabled=false')
print('privacy_upstream_filter_invariants_preserved=true')
PY

curl_auth "$BASE/querylog/config" -o /tmp/usw-qlog-config-after.json
python3 - <<'PY'
import json
d=json.load(open('/tmp/usw-qlog-config-after.json',encoding='utf-8'))
assert d.get('enabled') is False, d
print('api_querylog_enabled=false')
print('api_querylog_anonymize_client_ip='+str(d.get('anonymize_client_ip')).lower())
PY

# Synthetic DNS query directly to loopback; no participant data.
python3 - <<'PY'
import random, socket, struct
name='usesafeweb-log-correction.invalid'
q=b''.join(bytes([len(x)])+x.encode() for x in name.split('.'))+b'\x00'
pkt=struct.pack('!HHHHHH',random.randrange(0,65536),0x0100,1,0,0,0)+q+struct.pack('!HH',1,1)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM); s.settimeout(3); s.sendto(pkt,('127.0.0.1',53))
try: s.recvfrom(4096)
except socket.timeout: pass
PY
sleep 1

curl_auth "$BASE/querylog?limit=20" -o /tmp/usw-qlog-after-test.json
python3 - <<'PY'
import json
d=json.load(open('/tmp/usw-qlog-after-test.json',encoding='utf-8'))
items=d.get('data') or []
assert not any('usesafeweb-log-correction.invalid' in json.dumps(x,sort_keys=True) for x in items)
print('synthetic_query_retained=false')
print('querylog_items_after_correction='+str(len(items)))
PY

mapfile -t files < <(sudo find /opt/AdGuardHome -type f -name 'querylog.json*' -size +0c -print 2>/dev/null || true)
((${#files[@]} == 0)) || fail 'non-empty persistent querylog.json file remains'
pass 'no non-empty persistent querylog.json file remains'

unset password
success=1
printf 'TSK_0204_MUTATION=PASS\n'
