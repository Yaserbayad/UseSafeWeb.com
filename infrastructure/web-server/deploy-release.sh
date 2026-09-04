#!/usr/bin/env bash
set -Eeuo pipefail

SOURCE_ROOT="${1:-}"
RELEASE_SHA="${2:-}"
INSTALL_ROOT="${USESAFEWEB_INSTALL_ROOT:-/opt/usesafeweb-web}"
INSTALL_ROOT="${INSTALL_ROOT%/}"
SERVICE="usesafeweb-web.service"
ENV_FILE="/etc/usesafeweb/website.env"

fail(){ printf 'USESAFEWEB_DEPLOY=FAIL reason=%s\n' "$1" >&2; exit 1; }
set_release_binding(){
  local value="$1" temporary
  [[ "${value}" =~ ^[0-9a-f]{40}$ ]] || return 1
  temporary="$(mktemp "${ENV_FILE}.XXXXXX")" || return 1
  if ! awk -v sha="${value}" '
    BEGIN { found=0 }
    /^USESAFEWEB_RELEASE_SHA=/ {
      if (found != 0) exit 42
      print "USESAFEWEB_RELEASE_SHA=" sha
      found=1
      next
    }
    { print }
    END { if (found != 1) exit 43 }
  ' "${ENV_FILE}" >"${temporary}"; then
    rm -f -- "${temporary}"
    return 1
  fi
  chown root:root "${temporary}" || { rm -f -- "${temporary}"; return 1; }
  chmod 0600 "${temporary}" || { rm -f -- "${temporary}"; return 1; }
  mv -f -- "${temporary}" "${ENV_FILE}"
}

[[ -d "${SOURCE_ROOT}/website" ]] || fail source_root
[[ "${RELEASE_SHA}" =~ ^[0-9a-f]{40}$ ]] || fail release_sha
[[ "$(git -C "${SOURCE_ROOT}" rev-parse HEAD)" == "${RELEASE_SHA}" ]] || fail source_binding
[[ "$(node --version)" == 'v22.23.2' ]] || fail node_version
[[ "$(npm --version)" == '10.9.8' ]] || fail npm_version
[[ -f "${ENV_FILE}" ]] || fail environment_file
[[ "$(stat -c '%a %U:%G' "${ENV_FILE}")" == '600 root:root' ]] || fail environment_permissions
env_release="$(awk -F= '$1=="USESAFEWEB_RELEASE_SHA" {sub(/^[^=]*=/,""); print; exit}' "${ENV_FILE}")"
[[ "${env_release}" == "${RELEASE_SHA}" ]] || fail environment_release_binding

release="${INSTALL_ROOT}/releases/${RELEASE_SHA}"
current="${INSTALL_ROOT}/current"
previous=""
previous_release_sha=""
if [[ -e "${current}" && ! -L "${current}" ]]; then
  fail current_not_managed_symlink
fi
if [[ -L "${current}" ]]; then
  previous="$(readlink -f "${current}")"
  previous_release_sha="${previous##*/}"
  [[ "${previous_release_sha}" =~ ^[0-9a-f]{40}$ ]] || fail previous_release_identity
  [[ "${previous}" == "${INSTALL_ROOT}/releases/${previous_release_sha}" ]] || fail previous_release_path
  [[ -d "${previous}" ]] || fail previous_release_missing
fi
rollback(){
  rc=$?
  trap - EXIT
  if (( rc != 0 )); then
    rm -rf -- "${release}.new" >/dev/null 2>&1 || true
    if [[ -n "${previous}" && -d "${previous}" ]]; then
      ln -sfn "${previous}" "${current}"
      if set_release_binding "${previous_release_sha}"; then
        if systemctl restart "${SERVICE}" >/dev/null 2>&1; then
          printf 'USESAFEWEB_DEPLOY_ROLLBACK=RESTORED\n' >&2
        else
          printf 'USESAFEWEB_DEPLOY_ROLLBACK=SERVICE_RESTART_FAILED\n' >&2
        fi
      else
        printf 'USESAFEWEB_DEPLOY_ROLLBACK=IDENTITY_RESTORE_FAILED\n' >&2
      fi
    else
      rm -f "${current}"
      printf 'USESAFEWEB_DEPLOY_ROLLBACK=FIRST_DEPLOY_CLEANED\n' >&2
    fi
  fi
  exit "${rc}"
}
trap rollback EXIT

cd "${SOURCE_ROOT}/website"
npm ci --ignore-scripts --no-fund --no-audit
NEXT_TELEMETRY_DISABLED=1 npm run validate

rm -rf "${release}.new"
install -d -o usesafeweb-web -g usesafeweb-web -m 0750 "${release}.new"
standalone='.next/standalone/website'
[[ -f "${standalone}/server.js" ]] || standalone='.next/standalone'
[[ -f "${standalone}/server.js" ]] || fail standalone_output
cp -a "${standalone}/." "${release}.new/"
install -d -o usesafeweb-web -g usesafeweb-web -m 0750 "${release}.new/.next/static"
cp -a .next/static/. "${release}.new/.next/static/"
if [[ -d public ]]; then cp -a public "${release}.new/public"; fi
install -o usesafeweb-web -g usesafeweb-web -m 0550 \
  "${SOURCE_ROOT}/infrastructure/web-server/validate-runtime.mjs" "${release}.new/validate-runtime.mjs"
chown -R usesafeweb-web:usesafeweb-web "${release}.new"
mv "${release}.new" "${release}"
ln -sfn "${release}" "${current}"
systemctl daemon-reload
systemctl restart "${SERVICE}"

for _ in $(seq 1 30); do
  if curl --silent --show-error --fail --max-time 2 http://127.0.0.1:3100/api/health/ready >/dev/null; then
    trap - EXIT
    printf 'USESAFEWEB_DEPLOY=PASS release=%s\n' "${RELEASE_SHA}"
    exit 0
  fi
  sleep 1
done
fail readiness
