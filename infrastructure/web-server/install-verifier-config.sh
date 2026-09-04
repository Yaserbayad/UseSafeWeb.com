#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="${USESAFEWEB_TLS_ENV_FILE:-/etc/usesafeweb/verifier-tls.env}"
DESTINATION="/etc/nginx/conf.d/usesafeweb-verifier.conf"
DEFAULT_SITE="/etc/nginx/sites-enabled/default"
TEMPORARY="$(mktemp /etc/nginx/conf.d/.usesafeweb-verifier.XXXXXX)"
BACKUP=""
INSTALLED=0
DEFAULT_SITE_DISABLED=0
SUCCESS=0

fail(){ printf 'VERIFIER_CONFIG_INSTALL=FAIL %s\n' "$*" >&2; exit 1; }
cleanup(){
  rc=$?
  rm -f -- "${TEMPORARY}"
  if [[ "${SUCCESS}" != 1 && -n "${BACKUP}" && -f "${BACKUP}" ]]; then
    install -o root -g root -m 0644 "${BACKUP}" "${DESTINATION}" >/dev/null 2>&1 || true
  elif [[ "${SUCCESS}" != 1 && "${INSTALLED}" == 1 ]]; then
    rm -f -- "${DESTINATION}"
  fi
  if [[ "${SUCCESS}" != 1 && "${DEFAULT_SITE_DISABLED}" == 1 ]]; then
    ln -s ../sites-available/default "${DEFAULT_SITE}" >/dev/null 2>&1 || true
  fi
  if [[ "${SUCCESS}" != 1 ]]; then
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
: "${USESAFEWEB_PUBLIC_APPLICATION_HOST:?public application host is required}"
: "${USESAFEWEB_PUBLIC_CERTIFICATE:?public certificate path is required}"
: "${USESAFEWEB_PUBLIC_PRIVATE_KEY:?public private-key path is required}"
: "${USESAFEWEB_TLS_TRUST_BUNDLE:?TLS trust bundle is required}"

python3 "${SCRIPT_DIR}/render-verifier-config.py" \
  --certificate "${USESAFEWEB_VERIFIER_CERTIFICATE}" \
  --private-key "${USESAFEWEB_VERIFIER_PRIVATE_KEY}" \
  --public-host "${USESAFEWEB_PUBLIC_APPLICATION_HOST}" \
  --public-certificate "${USESAFEWEB_PUBLIC_CERTIFICATE}" \
  --public-private-key "${USESAFEWEB_PUBLIC_PRIVATE_KEY}" \
  --trust-bundle "${USESAFEWEB_TLS_TRUST_BUNDLE}" \
  --output "${TEMPORARY}"
if [[ -e "${DEFAULT_SITE}" || -L "${DEFAULT_SITE}" ]]; then
  [[ -L "${DEFAULT_SITE}" ]] || fail 'stock default site is not a managed symlink'
  [[ "$(readlink -f "${DEFAULT_SITE}")" == '/etc/nginx/sites-available/default' ]] || fail 'unexpected default site owner'
  unlink "${DEFAULT_SITE}"
  DEFAULT_SITE_DISABLED=1
fi
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
