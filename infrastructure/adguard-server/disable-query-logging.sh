#!/usr/bin/env bash
set -Eeuo pipefail

BASE='http://127.0.0.1:3000/control'
SECRET='/var/lib/usesafeweb/adguard/admin.env'

fail(){ printf 'FAIL  %s\n' "$*" >&2; exit 1; }
pass(){ printf 'PASS  %s\n' "$*"; }

sudo -n true || fail 'non-interactive sudo unavailable'
for c in curl python3 find; do command -v "$c" >/dev/null || fail "$c missing"; done
[[ "$(sudo stat -c '%a %U:%G' "$SECRET")" == '600 root:root' ]] || fail 'admin credential file is not root restricted'

username="$(sudo awk -F= '$1=="ADGUARD_ADMIN_USER" {sub(/^[^=]*=/,""); print; exit}' "$SECRET")"
password="$(sudo awk -F= '$1=="ADGUARD_ADMIN_PASSWORD" {sub(/^[^=]*=/,""); print; exit}' "$SECRET")"
[[ -n "$username" && -n "$password" ]] || fail 'admin credential unavailable'

curl_auth(){ curl --silent --show-error --fail --max-time 10 --user "$username:$password" "$@"; }

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
pass 'persistent query logging disabled and prior query log cleared'

curl_auth "$BASE/querylog/config" -o /tmp/usw-qlog-config-after.json
python3 - <<'PY'
import json
p='/tmp/usw-qlog-config-after.json'
d=json.load(open(p,encoding='utf-8'))
assert d.get('enabled') is False, d
print('querylog_enabled=false')
print('querylog_interval_ms='+str(d.get('interval')))
print('querylog_anonymize_client_ip='+str(d.get('anonymize_client_ip')).lower())
PY

# Synthetic DNS query directly to the loopback AdGuard listener; no user data.
python3 - <<'PY'
import random, socket, struct
name='usesafeweb-log-test.invalid'
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
p='/tmp/usw-qlog-after-test.json'
d=json.load(open(p,encoding='utf-8'))
items=d.get('data') or []
for item in items:
    text=json.dumps(item,sort_keys=True)
    if 'usesafeweb-log-test.invalid' in text:
        raise SystemExit('synthetic query appeared in query log while disabled')
print('synthetic_query_retained=false')
print('querylog_items_after_clear_and_test='+str(len(items)))
PY

# The official querylog implementation uses querylog.json. Disabled logging +
# clear must leave no non-empty querylog.json* file behind.
mapfile -t files < <(sudo find /opt/AdGuardHome -type f -name 'querylog.json*' -size +0c -print 2>/dev/null || true)
if ((${#files[@]})); then
  printf 'unexpected_nonempty_querylog_file=%s\n' "${files[@]}"
  fail 'non-empty persistent querylog.json file remains'
fi
pass 'no non-empty persistent querylog.json file remains'

unset password
rm -f /tmp/usw-qlog-config-before.json /tmp/usw-qlog-config-target.json /tmp/usw-qlog-config-after.json /tmp/usw-qlog-after-test.json
printf 'TSK_0204_MUTATION=PASS\n'
