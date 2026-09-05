#!/usr/bin/env bash
set -Eeuo pipefail

NODE_VERSION='v22.23.2'
ARCHIVE='node-v22.23.2-linux-x64.tar.xz'
EXPECTED_SHA256='d60acfe00a2932254bb0ad20e01b0d74397a0875595de719654b214f4b03f307'
RUNTIME_ROOT='/opt/usesafeweb-runtime'
DESTINATION="${RUNTIME_ROOT}/node-v22.23.2"
DOWNLOAD_URL="https://nodejs.org/dist/v22.23.2/${ARCHIVE}"

fail(){ printf 'USESAFEWEB_NODE_RUNTIME=FAIL reason=%s\n' "$1" >&2; exit 1; }
verify_runtime(){
  [[ -x "${DESTINATION}/bin/node" ]] || return 1
  [[ -f "${DESTINATION}/lib/node_modules/npm/bin/npm-cli.js" ]] || return 1
  [[ "$("${DESTINATION}/bin/node" --version)" == "${NODE_VERSION}" ]] || return 1
  [[ "$("${DESTINATION}/bin/node" "${DESTINATION}/lib/node_modules/npm/bin/npm-cli.js" --version)" == '10.9.8' ]] || return 1
}

[[ "${EUID}" == 0 ]] || fail root_required
[[ "$(uname -m)" == 'x86_64' ]] || fail architecture
. /etc/os-release
[[ "${ID:-}" == 'ubuntu' && "${VERSION_ID:-}" == '24.04' ]] || fail operating_system
command -v curl >/dev/null 2>&1 || fail curl_missing
command -v sha256sum >/dev/null 2>&1 || fail sha256sum_missing
command -v tar >/dev/null 2>&1 || fail tar_missing

if [[ -e "${DESTINATION}" ]]; then
  verify_runtime || fail existing_runtime_invalid
  printf 'USESAFEWEB_NODE_RUNTIME=PASS version=%s already_installed=1\n' "${NODE_VERSION}"
  exit 0
fi

install -d -o root -g root -m 0755 "${RUNTIME_ROOT}"
temporary="$(mktemp -d "${RUNTIME_ROOT}/.node-runtime.XXXXXX")"
staged="${DESTINATION}.new.$$"
cleanup(){ rm -rf -- "${temporary}" "${staged}"; }
trap cleanup EXIT

curl --fail --silent --show-error --location --proto '=https' --tlsv1.2 \
  --output "${temporary}/${ARCHIVE}" "${DOWNLOAD_URL}"
printf '%s  %s\n' "${EXPECTED_SHA256}" "${temporary}/${ARCHIVE}" | sha256sum --check --status \
  || fail archive_checksum

tar -xJf "${temporary}/${ARCHIVE}" -C "${temporary}"
source_dir="${temporary}/node-v22.23.2-linux-x64"
[[ -x "${source_dir}/bin/node" ]] || fail archive_layout
[[ -f "${source_dir}/lib/node_modules/npm/bin/npm-cli.js" ]] || fail archive_layout
[[ "$("${source_dir}/bin/node" --version)" == "${NODE_VERSION}" ]] || fail node_version
[[ "$("${source_dir}/bin/node" "${source_dir}/lib/node_modules/npm/bin/npm-cli.js" --version)" == '10.9.8' ]] || fail npm_version

mv -- "${source_dir}" "${staged}"
chown -R root:root "${staged}"
chmod -R a+rX,go-w "${staged}"
mv -- "${staged}" "${DESTINATION}"
verify_runtime || fail installed_runtime_invalid

trap - EXIT
rm -rf -- "${temporary}"
printf 'USESAFEWEB_NODE_RUNTIME=PASS version=%s sha256=%s\n' "${NODE_VERSION}" "${EXPECTED_SHA256}"
