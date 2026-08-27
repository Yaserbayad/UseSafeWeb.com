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

curl_auth "$BASE/querylog/config" -o /tmp/usw-qcfg-before.json
python3 - <<'PY'
import json
d=json.load(open('/tmp/usw-qcfg-before.json',encoding='utf-8'))
for k in ('enabled','interval','anonymize_client_ip','ignored'):
    if k not in d: raise SystemExit(f'missing querylog config key: {k}')
if d.get('enabled') is not False:
    raise SystemExit('query logging is not disabled before anonymisation change')
d['anonymize_client_ip']=True
open('/tmp/usw-qcfg-target.json','w',encoding='utf-8').write(json.dumps(d,separators=(',',':')))
PY

curl_auth --request PUT --header 'Content-Type: application/json' \
  --data-binary @/tmp/usw-qcfg-target.json "$BASE/querylog/config/update" -o /dev/null
pass 'client IP anonymisation enabled in query-log privacy configuration'

curl_auth "$BASE/querylog/config" -o /tmp/usw-qcfg-after.json
curl_auth "$BASE/stats/config" -o /tmp/usw-stats-config.json
python3 - <<'PY'
import json
q=json.load(open('/tmp/usw-qcfg-after.json',encoding='utf-8'))
s=json.load(open('/tmp/usw-stats-config.json',encoding='utf-8'))
assert q.get('enabled') is False, q
assert q.get('anonymize_client_ip') is True, q
assert s.get('enabled') is False, s
print('querylog_enabled=false')
print('anonymize_client_ip=true')
print('statistics_enabled=false')
PY

sudo python3 - /opt/AdGuardHome/AdGuardHome.yaml <<'PY'
from pathlib import Path
import sys
lines=Path(sys.argv[1]).read_text(encoding='utf-8').splitlines()
inside=False; enabled=None; anon=None
for line in lines:
    if line and not line[0].isspace():
        inside=line.rstrip()=='querylog:'
        continue
    if inside and line.startswith('  enabled:'):
        enabled=line.split(':',1)[1].strip().lower()
    if inside and line.startswith('  anonymize_client_ip:'):
        anon=line.split(':',1)[1].strip().lower()
    if inside and enabled is not None and anon is not None:
        break
assert enabled=='false', enabled
assert anon=='true', anon
print('persisted_querylog_enabled=false')
print('persisted_anonymize_client_ip=true')
PY

unset password
rm -f /tmp/usw-qcfg-before.json /tmp/usw-qcfg-target.json /tmp/usw-qcfg-after.json /tmp/usw-stats-config.json
printf 'TSK_0206_MUTATION=PASS\n'
