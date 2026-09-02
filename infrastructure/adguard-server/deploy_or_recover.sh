#!/usr/bin/env bash
set -Eeuo pipefail
umask 077
PATH='/usr/sbin:/usr/bin:/sbin:/bin'
export PATH

readonly ADGUARD_VERSION='v0.107.79'
readonly ADGUARD_SHA256='c48f4a43000665484c5ec28177de11a004759b620dae8f77b2aabefc9ef3687f'
readonly ADGUARD_ASSET='AdGuardHome_linux_amd64.tar.gz'
readonly ADGUARD_BASE_URL="https://github.com/AdguardTeam/AdGuardHome/releases/download/${ADGUARD_VERSION}"
readonly EXPECTED_SCHEMA='34'
readonly BUNDLE_VERSION='1.0.0'
readonly SERVICE_HOSTNAME='dns.usesafeweb.com'
readonly DOH_URL='https://dns.usesafeweb.com/dns-query'
readonly UPSTREAM_DOH='https://dns10.quad9.net/dns-query'
readonly ADMIN_BIND='127.0.0.1:3000'
readonly DEFAULT_CONFIG='/etc/usesafeweb/recovery.env'
readonly SECRET_ROOT='/etc/usesafeweb/secrets'
readonly LOCK_FILE='/run/lock/usesafeweb-adguard-recovery.lock'
readonly INSTALL_DIR='/opt/AdGuardHome'
readonly ADGUARD_BINARY="${INSTALL_DIR}/AdGuardHome"
readonly ADGUARD_CONFIG="${INSTALL_DIR}/AdGuardHome.yaml"
readonly RUNTIME_ROOT='/usr/local/lib/usesafeweb-adguard'
readonly INSTALLED_ENTRY='/usr/local/sbin/usesafeweb-deploy-or-recover'
readonly BACKUP_DIR_FIXED='/srv/usesafeweb-backups'
readonly PROFILE_DEST_FIXED='/var/www/usesafeweb/UseSafeWeb-iPhone-DoH.mobileconfig'
readonly ACME_ROOT='/var/www/usesafeweb-acme'
readonly NGINX_HTTP='/etc/nginx/sites-available/usesafeweb-dns'
readonly NGINX_HTTP_LINK='/etc/nginx/sites-enabled/usesafeweb-dns'
readonly NGINX_STREAM_DIR='/etc/nginx/streams-enabled'
readonly NGINX_STREAM="${NGINX_STREAM_DIR}/usesafeweb-dot.conf"
readonly MONITOR_SERVICE='/etc/systemd/system/usesafeweb-dns-verify.service'
readonly MONITOR_TIMER='/etc/systemd/system/usesafeweb-dns-verify.timer'
readonly EXIT_INPUT=10 EXIT_PRIV=20 EXIT_DEP=30 EXIT_VERIFY=40 EXIT_UNCERTAIN=50

MODE=''
CONFIG_PATH="$DEFAULT_CONFIG"
ROLLBACK_DIR=''
APPLY_ACTIVE=0
INSTALLED_BY_RUN=0
CHANGED_NGINX_MAIN=0

declare -A CFG=()

log() { printf '%s %s\n' "$(date -u +'%Y-%m-%dT%H:%M:%SZ')" "$*"; }
fail() { local code="$1"; shift; printf 'ERROR %s\n' "$*" >&2; exit "$code"; }
usage() {
  cat <<'EOF'
Usage:
  deploy_or_recover.sh --check  [--config /etc/usesafeweb/recovery.env]
  deploy_or_recover.sh --apply  [--config /etc/usesafeweb/recovery.env]
  deploy_or_recover.sh --verify [--config /etc/usesafeweb/recovery.env]
  deploy_or_recover.sh --remove [--config /etc/usesafeweb/recovery.env]
EOF
}

retry_transient() {
  local attempts="$1"; shift
  local n=1
  until "$@"; do
    (( n >= attempts )) && return 1
    sleep $((n * 2))
    n=$((n + 1))
  done
}

parse_args() {
  while (($#)); do
    case "$1" in
      --check|--apply|--verify|--remove)
        [[ -z "$MODE" ]] || fail "$EXIT_INPUT" 'multiple modes are not allowed'
        MODE="$1"; shift ;;
      --config)
        (($# >= 2)) || fail "$EXIT_INPUT" '--config requires a path'
        CONFIG_PATH="$2"; shift 2 ;;
      -h|--help) usage; exit 0 ;;
      *) fail "$EXIT_INPUT" "unknown option: $1" ;;
    esac
  done
  [[ -n "$MODE" ]] || fail "$EXIT_INPUT" 'one mode is required'
  [[ "$CONFIG_PATH" == /* ]] || fail "$EXIT_INPUT" 'config path must be absolute'
  [[ "$CONFIG_PATH" != *'..'* ]] || fail "$EXIT_INPUT" 'unsafe config path'
}

is_allowed_key() {
  case "$1" in
    TARGET_ROLE|EXPECTED_HOSTNAME|ADMIN_SSH_CIDR|ADMIN_USERNAME|ADMIN_PASSWORD_HASH_FILE|BACKUP_PASSPHRASE_FILE|ACME_EMAIL_FILE|BUNDLE_VERSION|BACKUP_DIR|PROFILE_DEST|ENABLE_UFW|ALLOW_REMOVE) return 0 ;;
    *) return 1 ;;
  esac
}

parse_config() {
  [[ -f "$CONFIG_PATH" && ! -L "$CONFIG_PATH" ]] || fail "$EXIT_INPUT" 'config file missing or symlinked'
  local owner mode line key value
  owner="$(stat -c '%u' "$CONFIG_PATH")"
  mode="$(stat -c '%a' "$CONFIG_PATH")"
  [[ "$owner" == '0' ]] || fail "$EXIT_INPUT" 'config must be root-owned'
  (( (8#$mode & 8#022) == 0 )) || fail "$EXIT_INPUT" 'config must not be group/world writable'
  while IFS= read -r line || [[ -n "$line" ]]; do
    [[ -z "$line" || "$line" == \#* ]] && continue
    [[ "$line" =~ ^([A-Z][A-Z0-9_]*)=([A-Za-z0-9._:/@+,-]+)$ ]] || fail "$EXIT_INPUT" 'malformed config line'
    key="${BASH_REMATCH[1]}"; value="${BASH_REMATCH[2]}"
    is_allowed_key "$key" || fail "$EXIT_INPUT" "unknown config key: $key"
    [[ -z "${CFG[$key]+x}" ]] || fail "$EXIT_INPUT" "duplicate config key: $key"
    CFG[$key]="$value"
  done < "$CONFIG_PATH"

  : "${CFG[TARGET_ROLE]:=dns-resolver}"
  : "${CFG[EXPECTED_HOSTNAME]:=$SERVICE_HOSTNAME}"
  : "${CFG[ADMIN_USERNAME]:=usesafeweb-admin}"
  : "${CFG[BUNDLE_VERSION]:=$BUNDLE_VERSION}"
  : "${CFG[BACKUP_DIR]:=$BACKUP_DIR_FIXED}"
  : "${CFG[PROFILE_DEST]:=$PROFILE_DEST_FIXED}"
  : "${CFG[ENABLE_UFW]:=true}"
  : "${CFG[ALLOW_REMOVE]:=false}"

  [[ "${CFG[TARGET_ROLE]}" == 'dns-resolver' ]] || fail "$EXIT_INPUT" 'TARGET_ROLE must be dns-resolver'
  [[ "${CFG[EXPECTED_HOSTNAME]}" == "$SERVICE_HOSTNAME" ]] || fail "$EXIT_INPUT" 'hostname conflicts with canonical authority'
  [[ "${CFG[BUNDLE_VERSION]}" == "$BUNDLE_VERSION" ]] || fail "$EXIT_INPUT" 'bundle selector conflicts with canonical authority'
  [[ "${CFG[BACKUP_DIR]}" == "$BACKUP_DIR_FIXED" ]] || fail "$EXIT_INPUT" 'backup path conflicts with canonical authority'
  [[ "${CFG[PROFILE_DEST]}" == "$PROFILE_DEST_FIXED" ]] || fail "$EXIT_INPUT" 'profile destination conflicts with canonical authority'
  [[ "${CFG[ENABLE_UFW]}" == 'true' ]] || fail "$EXIT_INPUT" 'ENABLE_UFW must remain true'
  [[ "${CFG[ALLOW_REMOVE]}" == 'true' || "${CFG[ALLOW_REMOVE]}" == 'false' ]] || fail "$EXIT_INPUT" 'ALLOW_REMOVE must be true or false'
  [[ "${CFG[ADMIN_USERNAME]}" =~ ^[A-Za-z0-9._-]{1,64}$ ]] || fail "$EXIT_INPUT" 'invalid admin username'
  [[ -n "${CFG[ADMIN_SSH_CIDR]:-}" ]] || fail "$EXIT_INPUT" 'ADMIN_SSH_CIDR is required'
  [[ "${CFG[ADMIN_SSH_CIDR]}" =~ ^([0-9]{1,3}\.){3}[0-9]{1,3}/([0-9]|[12][0-9]|3[0-2])$ || "${CFG[ADMIN_SSH_CIDR]}" =~ ^[0-9A-Fa-f:]+/[0-9]{1,3}$ ]] || fail "$EXIT_INPUT" 'invalid ADMIN_SSH_CIDR'
  for k in ADMIN_PASSWORD_HASH_FILE BACKUP_PASSPHRASE_FILE ACME_EMAIL_FILE; do
    [[ -n "${CFG[$k]:-}" ]] || fail "$EXIT_INPUT" "$k is required"
    validate_secret_file "${CFG[$k]}" "$k"
  done
}

validate_secret_file() {
  local p="$1" label="$2" owner mode resolved
  [[ "$p" == "${SECRET_ROOT}/"* ]] || fail "$EXIT_INPUT" "$label must be below $SECRET_ROOT"
  [[ "$p" == /* && "$p" != *'..'* ]] || fail "$EXIT_INPUT" "$label has unsafe path"
  [[ -f "$p" && ! -L "$p" ]] || fail "$EXIT_INPUT" "$label missing or symlinked"
  resolved="$(realpath -e "$p")" || fail "$EXIT_INPUT" "$label cannot be resolved"
  [[ "$resolved" == "${SECRET_ROOT}/"* ]] || fail "$EXIT_INPUT" "$label escapes secret root"
  owner="$(stat -c '%u' "$p")"; mode="$(stat -c '%a' "$p")"
  [[ "$owner" == '0' ]] || fail "$EXIT_INPUT" "$label must be root-owned"
  (( (8#$mode & 8#077) == 0 )) || fail "$EXIT_INPUT" "$label must be mode 0600 or stricter"
  [[ -s "$p" ]] || fail "$EXIT_INPUT" "$label is empty"
}

require_platform() {
  [[ "$(id -u)" == '0' ]] || fail "$EXIT_PRIV" 'run as root'
  [[ -r /etc/os-release ]] || fail "$EXIT_INPUT" '/etc/os-release missing'
  # shellcheck disable=SC1091
  source /etc/os-release
  [[ "${ID:-}" == 'ubuntu' && "${VERSION_ID:-}" == '24.04' ]] || fail "$EXIT_INPUT" 'unsupported host: expected Ubuntu 24.04 LTS'
  [[ "$(uname -m)" == 'x86_64' ]] || fail "$EXIT_INPUT" 'unsupported architecture: expected x86_64'
  command -v flock >/dev/null || fail "$EXIT_DEP" 'flock missing'
  command -v python3 >/dev/null || fail "$EXIT_DEP" 'python3 missing'
}

resolve_source_assets() {
  local script_dir candidate
  script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  candidate="${script_dir}/tsk-0413-bundle-v1"
  if [[ -d "$candidate" ]]; then
    BUNDLE_DIR="$candidate"
    PROFILE_SOURCE="${script_dir}/client-profiles/UseSafeWeb-iPhone-DoH.mobileconfig"
  else
    BUNDLE_DIR="${RUNTIME_ROOT}/tsk-0413-bundle-v1"
    PROFILE_SOURCE="${RUNTIME_ROOT}/UseSafeWeb-iPhone-DoH.mobileconfig"
  fi
  [[ -d "$BUNDLE_DIR" && -f "$BUNDLE_DIR/verify_bundle.py" && -f "$BUNDLE_DIR/SHA256SUMS" ]] || fail "$EXIT_DEP" 'versioned recovery bundle missing'
  [[ -f "$PROFILE_SOURCE" ]] || fail "$EXIT_DEP" 'approved end-user profile artifact missing'
  python3 "$BUNDLE_DIR/verify_bundle.py" >/tmp/usesafeweb-bundle-verify.$$ || fail "$EXIT_VERIFY" 'bundle verification failed'
  grep -Fxq 'TSK_0413_BUNDLE_VERIFY=PASS' /tmp/usesafeweb-bundle-verify.$$ || fail "$EXIT_VERIFY" 'bundle verifier did not emit PASS'
  rm -f /tmp/usesafeweb-bundle-verify.$$
}

install_dependencies() {
  export DEBIAN_FRONTEND=noninteractive
  retry_transient 3 apt-get update -qq || fail "$EXIT_DEP" 'apt metadata refresh failed'
  retry_transient 3 apt-get install -y -qq ca-certificates curl tar python3 python3-yaml nginx libnginx-mod-stream certbot ufw openssl dnsutils util-linux || fail "$EXIT_DEP" 'dependency installation failed'
}

version_matches() { [[ "$1" == *"${ADGUARD_VERSION}"* ]]; }

install_adguard() {
  if [[ -x "$ADGUARD_BINARY" ]]; then
    local installed
    installed="$($ADGUARD_BINARY --version 2>/dev/null || true)"
    version_matches "$installed" || fail "$EXIT_UNCERTAIN" 'different or unrecognized AdGuard Home installation exists; refusing overwrite'
    log "AdGuard Home already at ${ADGUARD_VERSION}; no install change"
    return
  fi
  [[ ! -e "$INSTALL_DIR" ]] || fail "$EXIT_UNCERTAIN" 'unrecognized AdGuard installation directory exists'
  local tmp actual upstream_sha member extracted
  tmp="$(mktemp -d)"
  retry_transient 3 curl --fail --show-error --silent --location --proto '=https' --tlsv1.2 "${ADGUARD_BASE_URL}/${ADGUARD_ASSET}" -o "${tmp}/${ADGUARD_ASSET}" || fail "$EXIT_DEP" 'AdGuard release download failed'
  actual="$(sha256sum "${tmp}/${ADGUARD_ASSET}" | awk '{print $1}')"
  [[ "$actual" == "$ADGUARD_SHA256" ]] || fail "$EXIT_DEP" 'AdGuard release checksum mismatch'
  retry_transient 3 curl --fail --show-error --silent --location --proto '=https' --tlsv1.2 "${ADGUARD_BASE_URL}/checksums.txt" -o "${tmp}/checksums.txt" || fail "$EXIT_DEP" 'official checksums download failed'
  upstream_sha="$(awk -v a="$ADGUARD_ASSET" '{n=$2; sub(/^\.\//,"",n); if(n==a){print $1; exit}}' "${tmp}/checksums.txt")"
  [[ "$upstream_sha" == "$ADGUARD_SHA256" ]] || fail "$EXIT_DEP" 'official checksums do not match pinned digest'
  while IFS= read -r member; do
    [[ "$member" != /* ]] || fail "$EXIT_DEP" 'unsafe absolute archive member'
    member="${member#./}"
    [[ "$member" == AdGuardHome/* && "$member" != *'../'* && "$member" != *'/..' ]] || fail "$EXIT_DEP" 'unsafe archive member'
  done < <(tar -tzf "${tmp}/${ADGUARD_ASSET}")
  tar -xzf "${tmp}/${ADGUARD_ASSET}" -C "$tmp"
  extracted="$("${tmp}/AdGuardHome/AdGuardHome" --version 2>/dev/null || true)"
  version_matches "$extracted" || fail "$EXIT_DEP" 'extracted AdGuard version mismatch'
  install -d -m 0755 -o root -g root "$INSTALL_DIR"
  install -m 0755 -o root -g root "${tmp}/AdGuardHome/AdGuardHome" "$ADGUARD_BINARY"
  (cd "$INSTALL_DIR" && "$ADGUARD_BINARY" -s install) || { rm -rf "$tmp"; fail "$EXIT_DEP" 'AdGuard service install failed'; }
  systemctl stop AdGuardHome.service || true
  INSTALLED_BY_RUN=1
  rm -rf "$tmp"
}

install_authority_assets() {
  install -d -m 0755 -o root -g root "$RUNTIME_ROOT"
  rm -rf "${RUNTIME_ROOT}/tsk-0413-bundle-v1.new"
  install -d -m 0755 -o root -g root "${RUNTIME_ROOT}/tsk-0413-bundle-v1.new"
  cp -a "${BUNDLE_DIR}/." "${RUNTIME_ROOT}/tsk-0413-bundle-v1.new/"
  python3 "${RUNTIME_ROOT}/tsk-0413-bundle-v1.new/verify_bundle.py" >/dev/null || fail "$EXIT_VERIFY" 'copied bundle failed verification'
  rm -rf "${RUNTIME_ROOT}/tsk-0413-bundle-v1"
  mv "${RUNTIME_ROOT}/tsk-0413-bundle-v1.new" "${RUNTIME_ROOT}/tsk-0413-bundle-v1"
  install -m 0644 -o root -g root "$PROFILE_SOURCE" "${RUNTIME_ROOT}/UseSafeWeb-iPhone-DoH.mobileconfig"
  install -m 0755 -o root -g root "${BASH_SOURCE[0]}" "$INSTALLED_ENTRY"
}

render_adguard_config() {
  local hash_file tmp
  hash_file="${CFG[ADMIN_PASSWORD_HASH_FILE]}"
  grep -Eq '^\$2[aby]\$[0-9]{2}\$[./A-Za-z0-9]{53}$' "$hash_file" || fail "$EXIT_INPUT" 'admin password hash must be one bcrypt hash'
  tmp="$(mktemp)"
  BUNDLE_JSON="${BUNDLE_DIR}/bundle.json" ADMIN_USERNAME="${CFG[ADMIN_USERNAME]}" HASH_FILE="$hash_file" OUT="$tmp" python3 - <<'PY'
import json, os, pathlib, yaml
bundle=json.loads(pathlib.Path(os.environ['BUNDLE_JSON']).read_text())
cfg=dict(bundle['settings'])
cfg['users']=[{'name':os.environ['ADMIN_USERNAME'],'password':pathlib.Path(os.environ['HASH_FILE']).read_text().strip()}]
pathlib.Path(os.environ['OUT']).write_text(yaml.safe_dump(cfg,sort_keys=False),encoding='utf-8')
PY
  chmod 0600 "$tmp"
  if [[ -f "$ADGUARD_CONFIG" ]] && cmp -s "$tmp" "$ADGUARD_CONFIG"; then rm -f "$tmp"; log 'AdGuard configuration already exact'; return; fi
  install -m 0600 -o root -g root "$tmp" "$ADGUARD_CONFIG"
  rm -f "$tmp"
}

write_atomic() {
  local path="$1" mode="$2" tmp
  tmp="$(mktemp)"; cat >"$tmp"; chmod "$mode" "$tmp"; chown root:root "$tmp"; install -m "$mode" -o root -g root "$tmp" "$path"; rm -f "$tmp"
}

ensure_nginx_stream_include() {
  grep -Fq 'include /etc/nginx/streams-enabled/*.conf;' /etc/nginx/nginx.conf && return
  grep -Eq '^[[:space:]]*http[[:space:]]*\{' /etc/nginx/nginx.conf || fail "$EXIT_UNCERTAIN" 'unrecognized nginx.conf; cannot add stream include safely'
  cp -a /etc/nginx/nginx.conf "${ROLLBACK_DIR}/nginx.conf.before"
  CHANGED_NGINX_MAIN=1
  awk 'BEGIN{done=0} !done && $0 ~ /^[[:space:]]*http[[:space:]]*\{/ {print "include /etc/nginx/streams-enabled/*.conf;"; done=1} {print}' /etc/nginx/nginx.conf >"${ROLLBACK_DIR}/nginx.conf.new"
  install -m 0644 -o root -g root "${ROLLBACK_DIR}/nginx.conf.new" /etc/nginx/nginx.conf
}

configure_http01_site() {
  install -d -m 0755 -o root -g root "$ACME_ROOT" /etc/nginx/sites-available /etc/nginx/sites-enabled
  write_atomic "$NGINX_HTTP" 0644 <<EOF
server {
    listen 80;
    listen [::]:80;
    server_name ${SERVICE_HOSTNAME};
    location ^~ /.well-known/acme-challenge/ { root ${ACME_ROOT}; }
    location / { return 404; }
}
EOF
  ln -sfn "$NGINX_HTTP" "$NGINX_HTTP_LINK"
  nginx -t || fail "$EXIT_VERIFY" 'nginx HTTP-01 staging config invalid'
  systemctl enable --now nginx
  systemctl reload nginx
}

ensure_certificate() {
  local cert="/etc/letsencrypt/live/${SERVICE_HOSTNAME}/fullchain.pem" key="/etc/letsencrypt/live/${SERVICE_HOSTNAME}/privkey.pem" email
  if [[ -r "$cert" && -r "$key" ]]; then
    openssl x509 -in "$cert" -noout -checkend 86400 >/dev/null || fail "$EXIT_VERIFY" 'existing certificate expires within 24 hours'
    return
  fi
  email="$(tr -d '\r\n' < "${CFG[ACME_EMAIL_FILE]}")"
  [[ "$email" =~ ^[^[:space:]@]+@[^[:space:]@]+\.[^[:space:]@]+$ ]] || fail "$EXIT_INPUT" 'invalid ACME contact email'
  if ! certbot certonly --webroot -w "$ACME_ROOT" -d "$SERVICE_HOSTNAME" --email "$email" --agree-tos --non-interactive --keep-until-expiring; then
    if [[ -r "$cert" && -r "$key" ]] && openssl x509 -in "$cert" -noout -checkend 86400 >/dev/null; then
      log 'certbot returned failure but reconciled certificate is valid; continuing after observation'
    else
      fail "$EXIT_UNCERTAIN" 'certificate issuance outcome uncertain; reconcile before retry'
    fi
  fi
  [[ -r "$cert" && -r "$key" ]] || fail "$EXIT_VERIFY" 'certificate material absent after issuance'
}

configure_nginx_tls() {
  local cert="/etc/letsencrypt/live/${SERVICE_HOSTNAME}/fullchain.pem" key="/etc/letsencrypt/live/${SERVICE_HOSTNAME}/privkey.pem"
  install -d -m 0755 -o root -g root "$NGINX_STREAM_DIR"
  ensure_nginx_stream_include
  write_atomic "$NGINX_HTTP" 0644 <<EOF
server {
    listen 80;
    listen [::]:80;
    server_name ${SERVICE_HOSTNAME};
    location ^~ /.well-known/acme-challenge/ { root ${ACME_ROOT}; }
    location / { return 404; }
}
server {
    listen 443 ssl;
    listen [::]:443 ssl;
    server_name ${SERVICE_HOSTNAME};
    ssl_certificate ${cert};
    ssl_certificate_key ${key};
    ssl_protocols TLSv1.2 TLSv1.3;
    add_header Strict-Transport-Security "max-age=63072000" always;
    location = /dns-query {
        proxy_pass http://${ADMIN_BIND}/dns-query;
        proxy_http_version 1.1;
        proxy_set_header Host ${SERVICE_HOSTNAME};
        proxy_set_header X-Forwarded-Proto https;
    }
    location / { return 404; }
}
EOF
  write_atomic "$NGINX_STREAM" 0644 <<EOF
server {
    listen 853 ssl;
    listen [::]:853 ssl;
    proxy_pass 127.0.0.1:53;
    ssl_certificate ${cert};
    ssl_certificate_key ${key};
    ssl_protocols TLSv1.2 TLSv1.3;
}
EOF
  nginx -t || fail "$EXIT_VERIFY" 'nginx TLS/DoT configuration invalid'
  systemctl enable --now nginx
  systemctl reload nginx
}

check_existing_firewall_conflicts() {
  local line
  ufw status 2>/dev/null | while IFS= read -r line; do
    [[ "$line" == *ALLOW* ]] || continue
    if [[ "$line" == *'22/tcp'* || "$line" == *'80/tcp'* || "$line" == *'443/tcp'* || "$line" == *'853/tcp'* ]]; then continue; fi
    printf 'unexpected UFW allow rule: %s\n' "$line" >&2
    exit 51
  done || fail "$EXIT_UNCERTAIN" 'unexpected pre-existing firewall allow rule; refusing destructive reset'
}

configure_firewall() {
  check_existing_firewall_conflicts
  ufw default deny incoming >/dev/null
  ufw default allow outgoing >/dev/null
  ufw allow from "${CFG[ADMIN_SSH_CIDR]}" to any port 22 proto tcp comment 'UseSafeWeb admin SSH' >/dev/null
  ufw allow 80/tcp comment 'UseSafeWeb ACME HTTP-01' >/dev/null
  ufw allow 443/tcp comment 'UseSafeWeb DoH' >/dev/null
  ufw allow 853/tcp comment 'UseSafeWeb DoT' >/dev/null
  ufw --force enable >/dev/null
}

install_profile() {
  install -d -m 0755 -o root -g root "$(dirname "$PROFILE_DEST_FIXED")"
  install -m 0644 -o root -g root "$PROFILE_SOURCE" "$PROFILE_DEST_FIXED"
}

create_encrypted_backup() {
  local stamp plain enc sum tmp
  install -d -m 0700 -o root -g root "$BACKUP_DIR_FIXED"
  stamp="$(date -u +'%Y%m%dT%H%M%SZ')"
  tmp="$(mktemp -d)"; plain="${tmp}/usesafeweb-config.tar"; enc="${BACKUP_DIR_FIXED}/usesafeweb-config-${stamp}.tar.enc"
  tar -cf "$plain" -C / opt/AdGuardHome/AdGuardHome.yaml etc/nginx/sites-available/usesafeweb-dns etc/nginx/streams-enabled/usesafeweb-dot.conf usr/local/lib/usesafeweb-adguard/tsk-0413-bundle-v1 usr/local/lib/usesafeweb-adguard/UseSafeWeb-iPhone-DoH.mobileconfig 2>/dev/null || fail "$EXIT_VERIFY" 'privacy-safe backup staging failed'
  openssl enc -aes-256-cbc -pbkdf2 -salt -in "$plain" -out "$enc" -pass "file:${CFG[BACKUP_PASSPHRASE_FILE]}" || fail "$EXIT_VERIFY" 'backup encryption failed'
  chmod 0600 "$enc"
  sum="$(sha256sum "$enc" | awk '{print $1}')"; printf '%s  %s\n' "$sum" "$(basename "$enc")" >"${enc}.sha256"; chmod 0600 "${enc}.sha256"
  rm -rf "$tmp"
  log "Encrypted configuration backup created: ${enc}; sha256=${sum}"
}

install_monitor() {
  write_atomic "$MONITOR_SERVICE" 0644 <<EOF
[Unit]
Description=UseSafeWeb privacy-safe DNS configuration verification
After=network-online.target nginx.service AdGuardHome.service
[Service]
Type=oneshot
ExecStart=${INSTALLED_ENTRY} --verify --config ${CONFIG_PATH}
PrivateTmp=true
NoNewPrivileges=true
EOF
  write_atomic "$MONITOR_TIMER" 0644 <<'EOF'
[Unit]
Description=Run UseSafeWeb DNS verification periodically
[Timer]
OnBootSec=5min
OnUnitActiveSec=5min
RandomizedDelaySec=30s
Persistent=true
[Install]
WantedBy=timers.target
EOF
  systemctl daemon-reload
  systemctl enable --now usesafeweb-dns-verify.timer
}

assert_adguard_config() {
  CFG_PATH="$ADGUARD_CONFIG" python3 - <<'PY'
import os,yaml
c=yaml.safe_load(open(os.environ['CFG_PATH'],encoding='utf-8'))
assert c['schema_version']==34
assert c['http']=={'address':'127.0.0.1:3000','doh':{'insecure_enabled':True}}
d=c['dns']; assert d['bind_hosts']==['127.0.0.1'] and d['port']==53
assert d['upstream_dns']==['https://dns10.quad9.net/dns-query'] and d['fallback_dns']==[] and d['private_upstream']==[]
assert d['bootstrap_dns']==['9.9.9.10','149.112.112.10','2620:fe::10','2620:fe::fe:10']
assert d['edns_client_subnet']=={'enabled':False,'use_custom':False,'custom_ip':''}
assert d['anonymize_client_ip'] is True and d['ratelimit']==20 and d['refuse_any'] is True
assert c['querylog']=={'enabled':False,'file_enabled':False,'interval':'1d'}
assert c['statistics']=={'enabled':True,'interval':'1d'}
assert c['filtering']['protection_enabled'] is True and c['filtering']['filtering_enabled'] is True
assert c['filters']==[{'name':'AdGuard DNS filter','url':'https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt','enabled':True}]
assert c['whitelist_filters']==[] and c['user_rules']==[]
assert c['tls']['enabled'] is False and c['dhcp']['enabled'] is False
assert len(c.get('users',[]))==1 and c['users'][0]['name']
PY
}

verify_state() {
  local ver http_code
  [[ -x "$ADGUARD_BINARY" ]] || fail "$EXIT_VERIFY" 'AdGuard binary missing'
  ver="$($ADGUARD_BINARY --version 2>/dev/null || true)"; version_matches "$ver" || fail "$EXIT_VERIFY" 'AdGuard version mismatch'
  [[ -f "$ADGUARD_CONFIG" && ! -L "$ADGUARD_CONFIG" ]] || fail "$EXIT_VERIFY" 'AdGuard config missing or symlinked'
  assert_adguard_config || fail "$EXIT_VERIFY" 'AdGuard config does not match current authority'
  systemctl is-enabled --quiet AdGuardHome.service && systemctl is-active --quiet AdGuardHome.service || fail "$EXIT_VERIFY" 'AdGuard service not enabled/active'
  systemctl is-enabled --quiet nginx && systemctl is-active --quiet nginx || fail "$EXIT_VERIFY" 'nginx not enabled/active'
  nginx -t >/dev/null 2>&1 || fail "$EXIT_VERIFY" 'nginx config test failed'
  ss -H -lntup | grep -Eq '127\.0\.0\.1:53([[:space:]]|$)' || fail "$EXIT_VERIFY" 'loopback DNS listener missing'
  ! ss -H -lntup | awk '$5 ~ /:53$/ && $5 !~ /127\.0\.0\.1:53$/ && $5 !~ /\[::1\]:53$/ {bad=1} END{exit bad?0:1}' || fail "$EXIT_VERIFY" 'DNS port 53 exposed beyond loopback'
  ss -H -lntp | grep -Eq '127\.0\.0\.1:3000([[:space:]]|$)' || fail "$EXIT_VERIFY" 'loopback admin/DoH listener missing'
  ss -H -lntp | grep -Eq ':443([[:space:]]|$)' || fail "$EXIT_VERIFY" 'DoH TLS listener missing'
  ss -H -lntp | grep -Eq ':853([[:space:]]|$)' || fail "$EXIT_VERIFY" 'DoT TLS listener missing'
  http_code="$(curl --silent --show-error --output /dev/null --write-out '%{http_code}' --resolve "${SERVICE_HOSTNAME}:443:127.0.0.1" "$DOH_URL" || true)"
  [[ "$http_code" =~ ^(200|400|405)$ ]] || fail "$EXIT_VERIFY" "DoH path did not reach expected endpoint; status=${http_code}"
  [[ "$(curl --silent --show-error --output /dev/null --write-out '%{http_code}' --resolve "${SERVICE_HOSTNAME}:443:127.0.0.1" "https://${SERVICE_HOSTNAME}/" || true)" == '404' ]] || fail "$EXIT_VERIFY" 'unexpected public root exposure'
  timeout 10 openssl s_client -connect 127.0.0.1:853 -servername "$SERVICE_HOSTNAME" </dev/null 2>/dev/null | grep -q 'BEGIN CERTIFICATE' || fail "$EXIT_VERIFY" 'DoT TLS handshake failed'
  [[ -f "$PROFILE_DEST_FIXED" ]] || fail "$EXIT_VERIFY" 'approved profile artifact missing'
  [[ -d "$BACKUP_DIR_FIXED" && "$(stat -c '%a' "$BACKUP_DIR_FIXED")" == '700' ]] || fail "$EXIT_VERIFY" 'backup directory is not root-only 0700'
  if [[ "${CFG[ENABLE_UFW]}" == 'true' ]]; then ufw status | grep -q '^Status: active' || fail "$EXIT_VERIFY" 'UFW is not active'; fi
  log 'Verification PASS: exact version/config/privacy/listener/TLS/profile/firewall baseline observed'
  printf 'TSK0455_VERIFY=PASS\n'
}

snapshot_for_rollback() {
  ROLLBACK_DIR="$(mktemp -d)"
  mkdir -p "${ROLLBACK_DIR}/files"
  for p in "$ADGUARD_CONFIG" "$NGINX_HTTP" "$NGINX_STREAM" "$PROFILE_DEST_FIXED" "$MONITOR_SERVICE" "$MONITOR_TIMER"; do
    if [[ -e "$p" || -L "$p" ]]; then mkdir -p "${ROLLBACK_DIR}/files$(dirname "$p")"; cp -a "$p" "${ROLLBACK_DIR}/files${p}"; fi
  done
}

rollback() {
  set +e
  log 'Attempting bounded rollback after failed verification/mutation'
  systemctl stop usesafeweb-dns-verify.timer 2>/dev/null
  for p in "$ADGUARD_CONFIG" "$NGINX_HTTP" "$NGINX_STREAM" "$PROFILE_DEST_FIXED" "$MONITOR_SERVICE" "$MONITOR_TIMER"; do
    if [[ -e "${ROLLBACK_DIR}/files${p}" || -L "${ROLLBACK_DIR}/files${p}" ]]; then
      mkdir -p "$(dirname "$p")"; rm -f "$p"; cp -a "${ROLLBACK_DIR}/files${p}" "$p"
    elif [[ "$p" != "$ADGUARD_CONFIG" ]]; then rm -f "$p"; fi
  done
  if (( CHANGED_NGINX_MAIN )) && [[ -f "${ROLLBACK_DIR}/nginx.conf.before" ]]; then cp -a "${ROLLBACK_DIR}/nginx.conf.before" /etc/nginx/nginx.conf; fi
  if (( INSTALLED_BY_RUN )); then (cd "$INSTALL_DIR" && "$ADGUARD_BINARY" -s uninstall) >/dev/null 2>&1; rm -rf "$INSTALL_DIR"; fi
  systemctl daemon-reload 2>/dev/null; nginx -t >/dev/null 2>&1 && systemctl reload nginx 2>/dev/null
  set -e
}

on_error() {
  local rc="$?"
  if (( APPLY_ACTIVE )) && [[ -n "$ROLLBACK_DIR" ]]; then rollback; fi
  printf 'ERROR apply/verification failed; safe result may be uncertain, exit=%s\n' "$rc" >&2
  exit "$rc"
}

apply_state() {
  APPLY_ACTIVE=1; snapshot_for_rollback; trap on_error ERR
  install_dependencies
  install_authority_assets
  install_adguard
  render_adguard_config
  systemctl enable AdGuardHome.service
  systemctl restart AdGuardHome.service
  configure_http01_site
  configure_firewall
  ensure_certificate
  configure_nginx_tls
  install_profile
  create_encrypted_backup
  install_monitor
  verify_state
  APPLY_ACTIVE=0; trap - ERR
  rm -rf "$ROLLBACK_DIR"; ROLLBACK_DIR=''
  log 'Apply completed and verified'
}

remove_state() {
  [[ "${CFG[ALLOW_REMOVE]}" == 'true' ]] || fail "$EXIT_INPUT" 'remove guard denied; set ALLOW_REMOVE=true in root-managed config'
  [[ -x "$ADGUARD_BINARY" ]] || fail "$EXIT_UNCERTAIN" 'AdGuard installation absent; refusing ambiguous removal'
  version_matches "$($ADGUARD_BINARY --version 2>/dev/null || true)" || fail "$EXIT_UNCERTAIN" 'unrecognized AdGuard installation; refusing removal'
  systemctl disable --now usesafeweb-dns-verify.timer 2>/dev/null || true
  rm -f "$MONITOR_TIMER" "$MONITOR_SERVICE" "$NGINX_HTTP_LINK" "$NGINX_HTTP" "$NGINX_STREAM" "$PROFILE_DEST_FIXED"
  systemctl daemon-reload
  nginx -t >/dev/null 2>&1 && systemctl reload nginx || true
  ufw delete allow from "${CFG[ADMIN_SSH_CIDR]}" to any port 22 proto tcp >/dev/null 2>&1 || true
  ufw delete allow 80/tcp >/dev/null 2>&1 || true
  ufw delete allow 443/tcp >/dev/null 2>&1 || true
  ufw delete allow 853/tcp >/dev/null 2>&1 || true
  (cd "$INSTALL_DIR" && "$ADGUARD_BINARY" -s uninstall) || fail "$EXIT_UNCERTAIN" 'AdGuard service uninstall outcome uncertain'
  rm -rf "$INSTALL_DIR" "$RUNTIME_ROOT"; rm -f "$INSTALLED_ENTRY"
  log "Remove completed; protected backups in ${BACKUP_DIR_FIXED} and Certbot/ACME state were intentionally preserved"
  printf 'TSK0455_REMOVE=PASS\n'
}

main() {
  parse_args "$@"
  require_platform
  parse_config
  resolve_source_assets
  install -d -m 0755 -o root -g root "$(dirname "$LOCK_FILE")"
  exec 9>"$LOCK_FILE"
  flock -n 9 || fail "$EXIT_UNCERTAIN" 'concurrent invocation refused by flock'
  case "$MODE" in
    --check) log "Preflight PASS: Ubuntu 24.04/x86_64, config, secret metadata, bundle checksums/version, canonical hostname ${SERVICE_HOSTNAME}, upstream ${UPSTREAM_DOH}, bootstrap 9.9.9.10 149.112.112.10 2620:fe::10 2620:fe::fe:10, ECS/edns_client_subnet disabled, anonymized statistics 1d, querylog disabled, public TLS ports 443/853"; printf 'TSK0455_CHECK=PASS\n' ;;
    --apply) apply_state ;;
    --verify) verify_state ;;
    --remove) remove_state ;;
    *) fail "$EXIT_INPUT" 'internal mode error' ;;
  esac
}

if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
  main "$@"
fi
