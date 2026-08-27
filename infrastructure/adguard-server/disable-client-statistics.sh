#!/usr/bin/env bash
set -Eeuo pipefail

BASE='http://127.0.0.1:3000/control'
SECRET='/var/lib/usesafeweb/adguard/admin.env'

fail(){ printf 'FAIL  %s\n' "$*" >&2; exit 1; }
pass(){ printf 'PASS  %s\n' "$*"; }

sudo -n true || fail 'non-interactive sudo unavailable'
for c in curl python3; do command -v "$c" >/dev/null || fail "$c missing"; done
[[ "$(sudo stat -c '%a %U:%G' "$SECRET")" == '600 root:root' ]] || fail 'admin credential file is not root restricted'
username="$(sudo awk -F= '$1=="ADGUARD_ADMIN_USER" {sub(/^[^=]*=/,""); print; exit}' "$SECRET")"
password="$(sudo awk -F= '$1=="ADGUARD_ADMIN_PASSWORD" {sub(/^[^=]*=/,""); print; exit}' "$SECRET")"
[[ -n "$username" && -n "$password" ]] || fail 'admin credential unavailable'
curl_auth(){ curl --silent --show-error --fail --max-time 10 --user "$username:$password" "$@"; }

curl_auth "$BASE/stats/config" -o /tmp/usw-stats-before.json
python3 - <<'PY'
import json
p='/tmp/usw-stats-before.json'
d=json.load(open(p,encoding='utf-8'))
for k in ('enabled','interval','ignored'):
    if k not in d: raise SystemExit(f'missing stats config key: {k}')
d['enabled']=False
open('/tmp/usw-stats-target.json','w',encoding='utf-8').write(json.dumps(d,separators=(',',':')))
PY

curl_auth --request PUT --header 'Content-Type: application/json' \
  --data-binary @/tmp/usw-stats-target.json "$BASE/stats/config/update" -o /dev/null
curl_auth --request POST "$BASE/stats_reset" -o /dev/null
pass 'AdGuard statistics disabled and existing statistics reset'

curl_auth "$BASE/stats/config" -o /tmp/usw-stats-after.json
python3 - <<'PY'
import json
d=json.load(open('/tmp/usw-stats-after.json',encoding='utf-8'))
assert d.get('enabled') is False, d
print('stats_enabled=false')
print('stats_interval_ms='+str(d.get('interval')))
PY

# Send a synthetic query after disabling statistics.  If the statistics engine
# is truly disabled, it must not create an identifiable top-client record.
python3 - <<'PY'
import random, socket, struct
name='usesafeweb-stats-test.invalid'
q=b''.join(bytes([len(x)])+x.encode() for x in name.split('.'))+b'\x00'
pkt=struct.pack('!HHHHHH',random.randrange(0,65536),0x0100,1,0,0,0)+q+struct.pack('!HH',1,1)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM); s.settimeout(3); s.sendto(pkt,('127.0.0.1',53))
try: s.recvfrom(4096)
except socket.timeout: pass
PY
sleep 1

curl_auth "$BASE/stats" -o /tmp/usw-stats-data.json
python3 - <<'PY'
import json
d=json.load(open('/tmp/usw-stats-data.json',encoding='utf-8'))
top=d.get('top_clients') or []
assert top == [], top
assert int(d.get('num_dns_queries') or 0) == 0, d.get('num_dns_queries')
print('top_clients_count=0')
print('stats_num_dns_queries=0')
PY

# Verify the persisted YAML reflects disabled statistics without printing any
# unrelated configuration or credentials.
sudo python3 - /opt/AdGuardHome/AdGuardHome.yaml <<'PY'
from pathlib import Path
import sys
lines=Path(sys.argv[1]).read_text(encoding='utf-8').splitlines()
in_stats=False
enabled=None
for line in lines:
    if line and not line[0].isspace():
        in_stats = line.rstrip() == 'statistics:'
        continue
    if in_stats and line.startswith('  enabled:'):
        enabled=line.split(':',1)[1].strip().lower()
        break
if enabled != 'false':
    raise SystemExit(f'persisted statistics.enabled is {enabled!r}, expected false')
print('persisted_statistics_enabled=false')
PY

unset password
rm -f /tmp/usw-stats-before.json /tmp/usw-stats-target.json /tmp/usw-stats-after.json /tmp/usw-stats-data.json
printf 'TSK_0205_MUTATION=PASS\n'
