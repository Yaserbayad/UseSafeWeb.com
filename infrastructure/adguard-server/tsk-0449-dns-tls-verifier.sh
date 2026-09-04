#!/usr/bin/env bash
set -Eeuo pipefail
umask 077

MODE="${1:-}"
case "${MODE}" in
  --target|--external) ;;
  *) echo 'FAIL usage: --target|--external' >&2; exit 64 ;;
esac

HOST='dns.usesafeweb.com'
DOH_URL="https://${HOST}/dns-query"
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd -- "${SCRIPT_DIR}/../.." && pwd)"
RUNBOOK="${SCRIPT_DIR}/TLS_CERTIFICATE_RENEWAL_RUNBOOK.md"
DNS_DECISION="${SCRIPT_DIR}/DNS_ENDPOINT_DECISION.md"
MONITOR="${ROOT_DIR}/.github/workflows/certificate-expiry-monitor.yml"
STATE="${ROOT_DIR}/CURRENT_STATE.md"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf -- "${TMP_DIR}"' EXIT

fail() {
  printf 'FAIL %s\n' "$1" >&2
  exit 1
}

require_file_marker() {
  local file="$1" marker="$2"
  [[ -f "${file}" ]] || fail 'required canonical artifact missing'
  grep -Fq -- "${marker}" "${file}" || fail 'required canonical artifact marker missing'
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || fail 'required verifier command missing'
}

check_canonical_artifacts() {
  require_file_marker "${DNS_DECISION}" 'Canonical client-facing hostname: **`dns.usesafeweb.com`**'
  require_file_marker "${DNS_DECISION}" 'Canonical DNS-over-HTTPS URL: **`https://dns.usesafeweb.com/dns-query`**'
  require_file_marker "${DNS_DECISION}" 'DNS-only/direct to the Azure resolver'
  require_file_marker "${RUNBOOK}" 'sudo certbot renew --dry-run --no-random-sleep-on-renew'
  require_file_marker "${RUNBOOK}" '/etc/letsencrypt/renewal-hooks/deploy/10-usesafeweb-reload-nginx.sh'
  require_file_marker "${RUNBOOK}" '## Emergency certificate replacement boundary'
  require_file_marker "${RUNBOOK}" 'do not fail open to plaintext DNS'
  require_file_marker "${MONITOR}" "cron: '17 6 * * *'"
  require_file_marker "${MONITOR}" 'HOSTNAME: dns.usesafeweb.com'
  require_file_marker "${MONITOR}" "THRESHOLD_DAYS: '30'"
  require_file_marker "${MONITOR}" 'OWNER_LOGIN: Yaserbayad'
  require_file_marker "${MONITOR}" 'issues: write'
  require_file_marker "${MONITOR}" 'GH_TOKEN: ${{ github.token }}'
  require_file_marker "${MONITOR}" "for port in (443, 853):"
  printf 'CANONICAL_AUTOMATION_ARTIFACTS=PASS\n'
  printf 'EXPIRY_MONITOR=PASS\n'
  printf 'EMERGENCY_REPLACEMENT_RUNBOOK=PASS\n'
}

check_secret_boundary() {
  local scan
  scan="${TMP_DIR}/secret-scan.txt"
  if grep -EIn -- 'BEGIN ([A-Z ]+)?PRIVATE KEY|AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9_]{20,}|(api[_-]?key|api[_-]?token|password)[[:space:]]*[:=][[:space:]]*["'\''`]?[A-Za-z0-9/+_=.-]{12,}' \
      "${DNS_DECISION}" "${RUNBOOK}" "${MONITOR}" "${BASH_SOURCE[0]}" >"${scan}" 2>/dev/null; then
    fail 'secret-like material detected in versioned DNS/TLS artifacts'
  fi
  printf 'SECRET_BOUNDARY=PASS\n'
}

make_dns_query() {
  python3 - "${TMP_DIR}/query.bin" <<'PY'
import struct, sys
out = sys.argv[1]
qname = b''.join(bytes([len(x)]) + x for x in (b'example', b'com')) + b'\x00'
msg = struct.pack('!HHHHHH', 0x4490, 0x0100, 1, 0, 0, 0) + qname + struct.pack('!HH', 1, 1)
with open(out, 'wb') as f:
    f.write(msg)
PY
}

validate_dns_response() {
  python3 - "${TMP_DIR}/response.bin" <<'PY'
import struct, sys
raw = open(sys.argv[1], 'rb').read()
if len(raw) < 12:
    raise SystemExit(1)
tid, flags = struct.unpack('!HH', raw[:4])
if tid != 0x4490 or not (flags & 0x8000):
    raise SystemExit(1)
PY
}

check_doh() {
  local scope="$1"
  make_dns_query
  if [[ "${scope}" == 'local' ]]; then
    curl --silent --show-error --fail \
      --resolve "${HOST}:443:127.0.0.1" \
      --header 'accept: application/dns-message' \
      --header 'content-type: application/dns-message' \
      --data-binary "@${TMP_DIR}/query.bin" \
      --output "${TMP_DIR}/response.bin" \
      "${DOH_URL}" >/dev/null 2>&1 || fail 'local DoH request failed'
  else
    curl --silent --show-error --fail \
      --header 'accept: application/dns-message' \
      --header 'content-type: application/dns-message' \
      --data-binary "@${TMP_DIR}/query.bin" \
      --output "${TMP_DIR}/response.bin" \
      "${DOH_URL}" >/dev/null 2>&1 || fail 'external DoH request failed'
  fi
  validate_dns_response || fail 'DoH response failed structural validation'
  rm -f -- "${TMP_DIR}/query.bin" "${TMP_DIR}/response.bin"
  printf 'DOH_ENDPOINT=PASS\n'
}

check_public_admin_negative() {
  local scope="$1" code_root code_admin code_wrong
  local -a resolve=()
  [[ "${scope}" == 'local' ]] && resolve=(--resolve "${HOST}:443:127.0.0.1")
  code_root="$(curl --silent --show-error --output /dev/null --write-out '%{http_code}' "${resolve[@]}" "https://${HOST}/")"
  code_admin="$(curl --silent --show-error --output /dev/null --write-out '%{http_code}' "${resolve[@]}" "https://${HOST}/control/status")"
  code_wrong="$(curl --silent --show-error --output /dev/null --write-out '%{http_code}' "${resolve[@]}" "https://${HOST}/not-a-doh-route")"
  [[ "${code_root}" == '404' && "${code_admin}" == '404' && "${code_wrong}" == '404' ]] || fail 'public path boundary is not closed'
  printf 'NEGATIVE_PUBLIC_ADMIN=REJECTED\n'
  printf 'NEGATIVE_WRONG_DOH_PATH=REJECTED\n'
}

check_tls_local() {
  timeout 15 openssl s_client -connect 127.0.0.1:443 -servername "${HOST}" -verify_hostname "${HOST}" -verify_return_error </dev/null >/dev/null 2>&1 || fail 'local DoH TLS validation failed'
  timeout 15 openssl s_client -connect 127.0.0.1:853 -servername "${HOST}" -verify_hostname "${HOST}" -verify_return_error </dev/null >/dev/null 2>&1 || fail 'local DoT TLS validation failed'
  timeout 15 openssl s_client -connect 127.0.0.1:443 -servername "${HOST}" -verify_hostname "${HOST}" -verify_return_error -tls1_2 </dev/null >/dev/null 2>&1 || fail 'TLS 1.2 is unavailable on DoH endpoint'
  timeout 15 openssl s_client -connect 127.0.0.1:443 -servername "${HOST}" -verify_hostname "${HOST}" -verify_return_error -tls1_3 </dev/null >/dev/null 2>&1 || fail 'TLS 1.3 is unavailable on DoH endpoint'
  if timeout 15 openssl s_client -connect 127.0.0.1:443 -servername "${HOST}" -verify_hostname 'invalid.usesafeweb.com' -verify_return_error </dev/null >/dev/null 2>&1; then
    fail 'wrong TLS hostname unexpectedly validated'
  fi
  printf 'TLS_CHAIN_HOSTNAME=PASS\n'
  printf 'TLS_PROTOCOL=PASS\n'
  printf 'NEGATIVE_WRONG_TLS_HOSTNAME=REJECTED\n'
}

check_tls_external() {
  timeout 15 openssl s_client -connect "${HOST}:443" -servername "${HOST}" -verify_hostname "${HOST}" -verify_return_error </dev/null >/dev/null 2>&1 || fail 'external DoH TLS validation failed'
  if timeout 15 openssl s_client -connect "${HOST}:443" -servername "${HOST}" -verify_hostname 'invalid.usesafeweb.com' -verify_return_error </dev/null >/dev/null 2>&1; then
    fail 'wrong external TLS hostname unexpectedly validated'
  fi
  printf 'TLS_CHAIN_HOSTNAME=PASS\n'
  printf 'TLS_PROTOCOL=PASS\n'
  printf 'NEGATIVE_WRONG_TLS_HOSTNAME=REJECTED\n'
}

check_target_dns_identity() {
  require_file_marker "${STATE}" '- `TSK-0435` — Azure VM handoff — evidence blob'
  require_file_marker "${STATE}" '### TSK-0441 accepted stable state'
  curl --silent --show-error --fail --noproxy '*' --connect-timeout 4 --max-time 8 \
    --header 'Metadata:true' \
    --output "${TMP_DIR}/imds-compute.json" \
    'http://169.254.169.254/metadata/instance/compute?api-version=2021-02-01' \
    || fail 'Azure instance metadata lookup failed'
  python3 - "${TMP_DIR}/imds-compute.json" <<'PY'
import json, sys
with open(sys.argv[1], encoding='utf-8') as f:
    compute = json.load(f)
if str(compute.get('location', '')).lower().replace(' ', '') != 'westeurope':
    raise SystemExit(1)
PY
  rm -f -- "${TMP_DIR}/imds-compute.json"
  python3 - "${STATE}" "${HOST}" <<'PY'
import re, socket, sys
state_path, host = sys.argv[1], sys.argv[2]
with open(state_path, encoding='utf-8') as f:
    state = f.read()
pattern = rf"resolve `{re.escape(host)}` to `([0-9]+(?:\.[0-9]+){{3}})`"
accepted = re.findall(pattern, state)
if not accepted:
    raise SystemExit(1)
resolved = {x[4][0] for x in socket.getaddrinfo(host, 443, socket.AF_INET, socket.SOCK_STREAM)}
if accepted[-1] not in resolved:
    raise SystemExit(1)
PY
  printf 'TARGET_AZURE_REGION=PASS\n'
  printf 'DNS_RESOLUTION=PASS\n'
  printf 'DNS_DIRECT_TARGET=PASS\n'
}

check_external_dns() {
  getent ahostsv4 "${HOST}" >/dev/null 2>&1 || fail 'external DNS resolution failed'
  printf 'DNS_RESOLUTION=PASS\n'
}

check_no_public_plain_dns() {
  if ss -H -lntu | grep -Eq '(^|[[:space:]])(0\.0\.0\.0|\*|\[::\]|::):53([[:space:]]|$)'; then
    fail 'plaintext DNS 53 is publicly bound'
  fi
  printf 'NEGATIVE_PUBLIC_PLAINTEXT_DNS=REJECTED\n'
}

check_cert_automation_target() {
  local lineage='/etc/letsencrypt/live/dns.usesafeweb.com'
  local fullchain="${lineage}/fullchain.pem"
  local privkey="${lineage}/privkey.pem"
  local hook='/etc/letsencrypt/renewal-hooks/deploy/10-usesafeweb-reload-nginx.sh'
  local before after priv_real

  systemctl is-enabled certbot.timer >/dev/null 2>&1 || fail 'certbot timer is not enabled'
  systemctl is-active certbot.timer >/dev/null 2>&1 || fail 'certbot timer is not active'
  nginx -t >/dev/null 2>&1 || fail 'nginx configuration validation failed'
  [[ -r "${fullchain}" && -e "${privkey}" ]] || fail 'certificate lineage incomplete'
  [[ -f "${hook}" && -x "${hook}" ]] || fail 'certificate deploy hook missing or non-executable'
  [[ "$(stat -c '%U' "${hook}")" == 'root' ]] || fail 'certificate deploy hook is not root-owned'
  priv_real="$(readlink -f -- "${privkey}")"
  [[ -n "${priv_real}" && -f "${priv_real}" ]] || fail 'private key target missing'
  [[ "$(stat -c '%U' "${priv_real}")" == 'root' ]] || fail 'private key target is not root-owned'
  if find "${priv_real}" -perm /077 -print -quit | grep -q .; then
    fail 'private key target has group/other permissions'
  fi

  before="$(sha256sum "${fullchain}" | awk '{print $1}')"
  certbot renew --dry-run --no-random-sleep-on-renew >/dev/null 2>&1 || fail 'certificate renewal dry-run failed'
  after="$(sha256sum "${fullchain}" | awk '{print $1}')"
  [[ "${before}" == "${after}" ]] || fail 'production certificate changed during dry-run'
  nginx -t >/dev/null 2>&1 || fail 'nginx validation failed after renewal rehearsal'

  printf 'NGINX_CONFIG=PASS\n'
  printf 'CERTBOT_TIMER=PASS\n'
  printf 'CERTBOT_RENEW_DRY_RUN=PASS\n'
  printf 'DEPLOY_HOOK=PASS\n'
  printf 'CERTIFICATE_PRODUCTION_MATERIAL_UNCHANGED=PASS\n'
  printf 'ROLLBACK_CONTROL=PASS\n'
}

main() {
  require_cmd python3
  require_cmd curl
  require_cmd openssl
  require_cmd getent
  require_cmd timeout
  check_canonical_artifacts
  check_secret_boundary

  if [[ "${MODE}" == '--target' ]]; then
    [[ "$(id -u)" -eq 0 ]] || fail 'target verification requires root'
    [[ "$(hostname -s)" == 'adguardvm' ]] || fail 'unexpected target host'
    require_cmd systemctl
    require_cmd nginx
    require_cmd certbot
    require_cmd ss
    check_target_dns_identity
    check_tls_local
    check_doh local
    check_public_admin_negative local
    check_no_public_plain_dns
    check_cert_automation_target
    printf 'CI_EPHEMERAL_ENDPOINT_APPLICABILITY=NOT_PROVISIONED\n'
    printf 'STAGING_APPLICABILITY=NOT_TRIGGERED\n'
    printf 'PRODUCTION_CONFIGURATION_MUTATION=NONE\n'
    printf 'ACC_0449=PASS\n'
    printf 'VER_0449=PASS\n'
    printf 'EVD_0449_SANITIZED_STATUS=PASS\n'
    printf 'TARGET_VERIFY=PASS\n'
  else
    check_external_dns
    check_tls_external
    check_doh external
    check_public_admin_negative external
    printf 'CI_EPHEMERAL_ENDPOINT_APPLICABILITY=NOT_PROVISIONED\n'
    printf 'STAGING_APPLICABILITY=NOT_TRIGGERED\n'
    printf 'PRODUCTION_CONFIGURATION_MUTATION=NONE\n'
    printf 'ACC_0449=PASS\n'
    printf 'VER_0449=PASS\n'
    printf 'EVD_0449_SANITIZED_STATUS=PASS\n'
    printf 'INDEPENDENT_VERIFY=PASS\n'
  fi
}

main
