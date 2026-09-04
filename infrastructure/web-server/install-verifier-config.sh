#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="${USESAFEWEB_TLS_ENV_FILE:-/etc/usesafeweb/verifier-tls.env}"
DESTINATION="/etc/nginx/conf.d/usesafeweb-verifier.conf"
TEMPORARY="$(mktemp /etc/nginx/conf.d/.usesafeweb-verifier.XXXXXX)"
BACKUP=""
INSTALLED=0
SUCCESS=0

fail(){ printf 'VERIFIER_CONFIG_INSTALL=FAIL %s\n' "$*" >&2; exit 1; }
cleanup(){
  rc=$?
  rm -f -- "${TEMPORARY}"
  if [[ "${SUCCESS}" != 1 && -n "${BACKUP}" && -f "${BACKUP}" ]]; then
    install -o root -g root -m 0644 "${BACKUP}" "${DESTINATION}" >/dev/null 2>&1 || true
    nginx -t >/dev/null 2>&1 && systemctl reload nginx.service >/dev/null 2>&1 || true
  elif [[ "${SUCCESS}" != 1 && "${INSTALLED}" == 1 ]]; then
    rm -f -- "${DESTINATION}"
    nginx -t >/dev/null 2>&1 && systemctl reload nginx.service >/dev/null 2>&1 || true
  fi
  [[ -z "${BACKUP}" ]] || rm -f -- "${BACKUP}"
  exit "${rc}"
}
trap cleanup EXIT

[[ "${EUID}" == 0 ]] || fail 'root is required'
[[ -f "${ENV_FILE}" ]] || fail 'TLS environment file is missing'
[[ "$(stat -c '%a %U:%G' "${ENV_FILE}")" == '600 root:root' ]] || fail 'TLS environment file permissions must be 0600 root:root'
set -a
# shellcheck disable=SC1090
source "${ENV_FILE}"
set +a
: "${USESAFEWEB_VERIFIER_CERTIFICATE:?certificate path is required}"
: "${USESAFEWEB_VERIFIER_PRIVATE_KEY:?private-key path is required}"

python3 "${SCRIPT_DIR}/render-verifier-config.py" \
  --certificate "${USESAFEWEB_VERIFIER_CERTIFICATE}" \
  --private-key "${USESAFEWEB_VERIFIER_PRIVATE_KEY}" \
  --output "${TEMPORARY}"
if [[ -f "${DESTINATION}" ]]; then
  BACKUP="$(mktemp /tmp/usesafeweb-verifier-nginx.XXXXXX)"
  cp --preserve=mode,ownership,timestamps "${DESTINATION}" "${BACKUP}"
fi
install -o root -g root -m 0644 "${TEMPORARY}" "${DESTINATION}"
INSTALLED=1
nginx -t || fail 'nginx configuration validation failed'
systemctl reload nginx.service || fail 'nginx reload failed'
SUCCESS=1
printf 'VERIFIER_TLS_INPUT=PASS\nVERIFIER_NGINX_TEST=PASS\nVERIFIER_CONFIG_INSTALL=PASS\n'
