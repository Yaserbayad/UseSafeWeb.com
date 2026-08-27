#!/usr/bin/env bash
set -Eeuo pipefail

BASE_URL='http://127.0.0.1:3000'
ADMIN_USER='usesafeweb-admin'
SECRET_DIR='/var/lib/usesafeweb/adguard'
SECRET_FILE="${SECRET_DIR}/admin.env"
CONFIG_FILE='/opt/AdGuardHome/AdGuardHome.yaml'
CONFIG_BACKUP="${SECRET_DIR}/AdGuardHome.pre-loopback.yaml"
BINARY='/opt/AdGuardHome/AdGuardHome'

fail() { printf 'FAIL  %s\n' "$*" >&2; exit 1; }
pass() { printf 'PASS  %s\n' "$*"; }

[[ -x "$BINARY" ]] || fail 'AdGuard Home binary missing'
sudo -n true || fail 'non-interactive sudo unavailable'
for c in curl openssl python3 ss ufw systemctl; do command -v "$c" >/dev/null || fail "$c missing"; done

sudo install -d -m 0700 -o root -g root "$SECRET_DIR"

if sudo test -s "$SECRET_FILE"; then
  pass 'root-restricted AdGuard admin credential file already exists'
else
  password="$(openssl rand -hex 24)"
  [[ ${#password} -eq 48 ]] || fail 'password generation failed'
  tmp="$(mktemp)"
  trap 'rm -f "$tmp"' EXIT
  umask 077
  printf 'ADGUARD_ADMIN_USER=%s\nADGUARD_ADMIN_PASSWORD=%s\n' "$ADMIN_USER" "$password" > "$tmp"
  sudo install -m 0600 -o root -g root "$tmp" "$SECRET_FILE"
  rm -f "$tmp"
  trap - EXIT
  unset password
  pass 'root-restricted AdGuard admin credential file created'
fi

read_secret() {
  local key="$1"
  sudo awk -F= -v k="$key" '$1==k {sub(/^[^=]*=/,""); print; exit}' "$SECRET_FILE"
}

username="$(read_secret ADGUARD_ADMIN_USER)"
password="$(read_secret ADGUARD_ADMIN_PASSWORD)"
[[ "$username" == "$ADMIN_USER" ]] || fail 'unexpected stored admin username'
[[ -n "$password" ]] || fail 'stored admin password is empty'

auth_code="$(curl --silent --show-error --output /dev/null --write-out '%{http_code}' \
  --max-time 5 --user "$username:$password" "$BASE_URL/control/status" || true)"

if [[ "$auth_code" != '200' ]]; then
  setup_code="$(curl --silent --show-error --output /dev/null --write-out '%{http_code}' --max-time 5 "$BASE_URL/control/install/get_addresses" || true)"
  [[ "$setup_code" == '200' ]] || fail "setup endpoint unavailable before initialization (HTTP ${setup_code})"

  # First-run handler cannot move the active wildcard web listener to the same
  # port on loopback because it validates the new bind while the old listener
  # still owns that port. Initialize using the existing web bind, then harden
  # http.address to loopback in a separate rollbackable restart below.
  payload="$(python3 - "$username" "$password" <<'PY'
import json, sys
print(json.dumps({
  'web': {'ip': '0.0.0.0', 'port': 3000},
  'dns': {'ip': '127.0.0.1', 'port': 53},
  'username': sys.argv[1],
  'password': sys.argv[2],
  'language': 'en',
}, separators=(',', ':')))
PY
)"

  configure_code="$(curl --silent --show-error --output /tmp/usesafeweb-adguard-install-response \
    --write-out '%{http_code}' --max-time 15 \
    --header 'Content-Type: application/json' \
    --data-binary "$payload" \
    "$BASE_URL/control/install/configure" || true)"
  unset payload

  if [[ "$configure_code" != '200' ]]; then
    # Error body is not printed because it could unexpectedly echo input.
    rm -f /tmp/usesafeweb-adguard-install-response
    fail "AdGuard initial configuration failed (HTTP ${configure_code})"
  fi
  rm -f /tmp/usesafeweb-adguard-install-response
  pass 'AdGuard initial authenticated configuration applied'

  for _ in $(seq 1 20); do
    auth_code="$(curl --silent --show-error --output /dev/null --write-out '%{http_code}' \
      --max-time 3 --user "$username:$password" "$BASE_URL/control/status" || true)"
    [[ "$auth_code" == '200' ]] && break
    sleep 0.5
  done
fi

[[ "$auth_code" == '200' ]] || fail "authenticated local control/status failed (HTTP ${auth_code})"
pass 'authenticated local admin API access works'

# Harden the generated web/admin bind to loopback. Preserve the exact original
# generated configuration for one rollback point; never copy it to GitHub.
[[ -f "$CONFIG_FILE" ]] || fail 'generated AdGuardHome.yaml missing after initialization'
if ! sudo test -f "$CONFIG_BACKUP"; then
  sudo install -m 0600 -o root -g root "$CONFIG_FILE" "$CONFIG_BACKUP"
fi

current_http_addr="$(sudo python3 - "$CONFIG_FILE" <<'PY'
from pathlib import Path
import sys
lines=Path(sys.argv[1]).read_text(encoding='utf-8').splitlines()
in_http=False
for line in lines:
    if line and not line[0].isspace():
        in_http = line.rstrip() == 'http:'
        continue
    if in_http and line.startswith('  address:'):
        print(line.split(':',1)[1].strip())
        raise SystemExit
raise SystemExit(2)
PY
)" || fail 'could not read http.address from AdGuardHome.yaml'

echo "current_http_address=${current_http_addr}"
if [[ "$current_http_addr" != '127.0.0.1:3000' ]]; then
  sudo python3 - "$CONFIG_FILE" <<'PY'
from pathlib import Path
import os, sys, tempfile
p=Path(sys.argv[1])
lines=p.read_text(encoding='utf-8').splitlines(keepends=True)
in_http=False
changed=0
out=[]
for line in lines:
    if line and not line[0].isspace():
        in_http = line.rstrip('\r\n') == 'http:'
    if in_http and line.startswith('  address:'):
        if changed:
            raise SystemExit('multiple http.address entries')
        ending='\r\n' if line.endswith('\r\n') else '\n'
        line='  address: 127.0.0.1:3000'+ending
        changed=1
    out.append(line)
if changed != 1:
    raise SystemExit('http.address entry not found exactly once')
fd,tmp=tempfile.mkstemp(prefix=p.name+'.',dir=str(p.parent))
os.close(fd)
Path(tmp).write_text(''.join(out),encoding='utf-8')
os.chmod(tmp,0o600)
os.chown(tmp,0,0)
os.replace(tmp,p)
PY

  if ! sudo systemctl restart AdGuardHome.service; then
    sudo install -m 0600 -o root -g root "$CONFIG_BACKUP" "$CONFIG_FILE"
    sudo systemctl restart AdGuardHome.service || true
    fail 'AdGuard restart failed after loopback admin bind; configuration rolled back'
  fi
fi

for _ in $(seq 1 20); do
  auth_code="$(curl --silent --show-error --output /dev/null --write-out '%{http_code}' \
    --max-time 3 --user "$username:$password" "$BASE_URL/control/status" || true)"
  [[ "$auth_code" == '200' ]] && break
  sleep 0.5
done
[[ "$auth_code" == '200' ]] || {
  sudo install -m 0600 -o root -g root "$CONFIG_BACKUP" "$CONFIG_FILE"
  sudo systemctl restart AdGuardHome.service || true
  fail 'authenticated API failed after loopback hardening; configuration rolled back'
}
pass 'authenticated local admin API works after loopback hardening'

unauth_code="$(curl --silent --show-error --output /dev/null --write-out '%{http_code}' --max-time 5 "$BASE_URL/control/status" || true)"
echo "unauthenticated_status_http=${unauth_code}"
[[ "$unauth_code" == '401' || "$unauth_code" == '403' ]] || fail 'unauthenticated control API access was not denied'
pass 'unauthenticated control API access is denied'

admin_listeners="$(sudo ss -H -lntp | awk '/AdGuardHome/ && $4 ~ /:3000$/ {print $4}')"
printf 'admin_listener_inventory_begin\n%s\nadmin_listener_inventory_end\n' "$admin_listeners"
[[ -n "$admin_listeners" ]] || fail 'admin listener missing'
while IFS= read -r addr; do
  [[ "$addr" == '127.0.0.1:3000' || "$addr" == '[::1]:3000' ]] || fail "admin listener is not loopback-only: $addr"
done <<<"$admin_listeners"
pass 'admin listener is loopback-only'

adguard_dns_listeners="$(sudo ss -H -lntup | awk '/AdGuardHome/ && $5 ~ /:53$/ {print $1, $5}')"
printf 'adguard_dns_listener_inventory_begin\n%s\nadguard_dns_listener_inventory_end\n' "$adguard_dns_listeners"
[[ -n "$adguard_dns_listeners" ]] || fail 'AdGuard DNS listener missing after initialization'
while read -r proto addr; do
  [[ "$addr" == '127.0.0.1:53' || "$addr" == '[::1]:53' ]] || fail "AdGuard DNS listener is not loopback-only: $proto $addr"
done <<<"$adguard_dns_listeners"
pass 'initial DNS listener is loopback-only'

ufw_verbose="$(sudo ufw status verbose)"
grep -q '^Status: active' <<<"$ufw_verbose" || fail 'UFW inactive'
grep -q '^Default: deny (incoming), allow (outgoing)' <<<"$ufw_verbose" || fail 'unexpected UFW defaults'
while IFS= read -r line; do
  [[ "$line" == *ALLOW* ]] || continue
  [[ "$line" == 22/tcp* ]] || fail "unexpected inbound UFW allow rule: $line"
done <<<"$(sudo ufw status)"
pass 'host firewall still exposes only SSH'

stat_line="$(sudo stat -c '%a %U:%G' "$SECRET_FILE")"
echo "credential_file_mode_owner=${stat_line}"
[[ "$stat_line" == '600 root:root' ]] || fail 'credential file permissions/owner are not 600 root:root'
pass 'admin credential storage is root-restricted'

unset password
printf 'TSK_0201_MUTATION=PASS\n'
