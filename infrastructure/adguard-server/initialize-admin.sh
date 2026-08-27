#!/usr/bin/env bash
set -Eeuo pipefail

BASE_URL='http://127.0.0.1:3000'
ADMIN_USER='usesafeweb-admin'
SECRET_DIR='/var/lib/usesafeweb/adguard'
SECRET_FILE="${SECRET_DIR}/admin.env"
BINARY='/opt/AdGuardHome/AdGuardHome'

fail() { printf 'FAIL  %s\n' "$*" >&2; exit 1; }
pass() { printf 'PASS  %s\n' "$*"; }

[[ -x "$BINARY" ]] || fail 'AdGuard Home binary missing'
sudo -n true || fail 'non-interactive sudo unavailable'
command -v curl >/dev/null || fail 'curl missing'
command -v openssl >/dev/null || fail 'openssl missing'
command -v python3 >/dev/null || fail 'python3 missing'
command -v ss >/dev/null || fail 'ss missing'
command -v ufw >/dev/null || fail 'ufw missing'

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

# Read credentials through a root shell without printing them.
read_secret() {
  local key="$1"
  sudo awk -F= -v k="$key" '$1==k {sub(/^[^=]*=/,""); print; exit}' "$SECRET_FILE"
}

username="$(read_secret ADGUARD_ADMIN_USER)"
password="$(read_secret ADGUARD_ADMIN_PASSWORD)"
[[ "$username" == "$ADMIN_USER" ]] || fail 'unexpected stored admin username'
[[ -n "$password" ]] || fail 'stored admin password is empty'

# If authenticated status already succeeds, treat initialization as idempotent
# and continue to the stable-state checks below.
auth_code="$(curl --silent --show-error --output /dev/null --write-out '%{http_code}' \
  --max-time 5 --user "$username:$password" "$BASE_URL/control/status" || true)"

if [[ "$auth_code" != '200' ]]; then
  setup_code="$(curl --silent --show-error --output /dev/null --write-out '%{http_code}' --max-time 5 "$BASE_URL/control/install/get_addresses" || true)"
  [[ "$setup_code" == '200' ]] || fail "setup endpoint unavailable before initialization (HTTP ${setup_code})"

  payload="$(python3 - "$username" "$password" <<'PY'
import json, sys
print(json.dumps({
  'web': {'ip': '127.0.0.1', 'port': 3000},
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
    rm -f /tmp/usesafeweb-adguard-install-response
    fail "AdGuard initial configuration failed (HTTP ${configure_code})"
  fi
  rm -f /tmp/usesafeweb-adguard-install-response
  pass 'AdGuard initial authenticated configuration applied'

  # Allow the service to rebind after first-time configuration.
  for _ in $(seq 1 20); do
    auth_code="$(curl --silent --show-error --output /dev/null --write-out '%{http_code}' \
      --max-time 3 --user "$username:$password" "$BASE_URL/control/status" || true)"
    [[ "$auth_code" == '200' ]] && break
    sleep 0.5
  done
fi

[[ "$auth_code" == '200' ]] || fail "authenticated local control/status failed (HTTP ${auth_code})"
pass 'authenticated local admin API access works'

unauth_code="$(curl --silent --show-error --output /dev/null --write-out '%{http_code}' --max-time 5 "$BASE_URL/control/status" || true)"
echo "unauthenticated_status_http=${unauth_code}"
[[ "$unauth_code" == '401' || "$unauth_code" == '403' ]] || fail 'unauthenticated control API access was not denied'
pass 'unauthenticated control API access is denied'

# Admin must be loopback-only after initialization.
admin_listeners="$(sudo ss -H -lntp | awk '/AdGuardHome/ && $4 ~ /:3000$/ {print $4}')"
printf 'admin_listener_inventory_begin\n%s\nadmin_listener_inventory_end\n' "$admin_listeners"
[[ -n "$admin_listeners" ]] || fail 'admin listener missing'
while IFS= read -r addr; do
  [[ "$addr" == '127.0.0.1:3000' || "$addr" == '[::1]:3000' ]] || fail "admin listener is not loopback-only: $addr"
done <<<"$admin_listeners"
pass 'admin listener is loopback-only'

# DNS may bind only to loopback at this stage; public resolver activation is later.
dns_listeners="$(sudo ss -H -lntu | awk '$5 ~ /:53$/ {print $1, $5}')"
printf 'dns53_listener_inventory_begin\n%s\ndns53_listener_inventory_end\n' "$dns_listeners"
if sudo ss -H -lntup | awk '/AdGuardHome/ && $5 ~ /:53$/ {print $5}' | grep -Evq '^(127\.0\.0\.1:53|\[::1\]:53)$'; then
  fail 'AdGuard DNS listener is exposed beyond loopback during admin initialization'
fi

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
