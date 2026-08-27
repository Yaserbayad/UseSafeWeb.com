#!/usr/bin/env bash
set -Eeuo pipefail

VERSION="v0.107.79"
EXPECTED_SHA256="c48f4a43000665484c5ec28177de11a004759b620dae8f77b2aabefc9ef3687f"
ASSET="AdGuardHome_linux_amd64.tar.gz"
BASE_URL="https://github.com/AdguardTeam/AdGuardHome/releases/download/${VERSION}"
INSTALL_DIR="/opt/AdGuardHome"
BINARY="${INSTALL_DIR}/AdGuardHome"

fail() { printf 'FAIL  %s\n' "$*" >&2; exit 1; }
pass() { printf 'PASS  %s\n' "$*"; }

[[ "$(uname -m)" == "x86_64" ]] || fail "unsupported architecture: $(uname -m)"
[[ -r /etc/os-release ]] || fail "/etc/os-release unavailable"
# shellcheck disable=SC1091
source /etc/os-release
[[ "${ID:-}" == "ubuntu" && "${VERSION_ID:-}" == "24.04" ]] || fail "expected Ubuntu 24.04"
command -v curl >/dev/null || fail "curl missing"
command -v tar >/dev/null || fail "tar missing"
command -v sha256sum >/dev/null || fail "sha256sum missing"
command -v systemctl >/dev/null || fail "systemctl missing"
command -v ufw >/dev/null || fail "ufw missing"
sudo -n true || fail "non-interactive sudo unavailable"

# Never overwrite an unrecognized installation.
if [[ -x "$BINARY" ]]; then
  installed="$($BINARY --version 2>/dev/null || true)"
  if grep -Fq "${VERSION#v}" <<<"$installed"; then
    echo "installed_version=${installed}"
    pass "requested AdGuard Home version is already installed"
  else
    fail "different/unrecognized AdGuard Home installation already exists: ${installed:-unknown}"
  fi
else
  tmp="$(mktemp -d)"
  trap 'rm -rf "$tmp"' EXIT

  curl --fail --show-error --silent --location --proto '=https' --tlsv1.2 \
    "${BASE_URL}/${ASSET}" -o "${tmp}/${ASSET}"
  actual="$(sha256sum "${tmp}/${ASSET}" | awk '{print $1}')"
  [[ "$actual" == "$EXPECTED_SHA256" ]] || fail "release asset SHA-256 mismatch"
  echo "release_asset_sha256=${actual}"
  pass "release asset matches GitHub release digest"

  curl --fail --show-error --silent --location --proto '=https' --tlsv1.2 \
    "${BASE_URL}/checksums.txt" -o "${tmp}/checksums.txt"
  upstream_sha="$(awk -v a="$ASSET" '$2==a {print $1}' "${tmp}/checksums.txt")"
  [[ -n "$upstream_sha" && "$upstream_sha" == "$EXPECTED_SHA256" ]] \
    || fail "official checksums.txt does not match pinned GitHub asset digest"
  pass "official checksums.txt agrees with pinned digest"

  # Reject absolute/path-traversal archive members before extraction.
  while IFS= read -r member; do
    [[ "$member" == AdGuardHome/* ]] || fail "unexpected archive member: $member"
    [[ "$member" != /* && "$member" != *"../"* && "$member" != *"/.."* ]] \
      || fail "unsafe archive member: $member"
  done < <(tar -tzf "${tmp}/${ASSET}")

  tar -xzf "${tmp}/${ASSET}" -C "$tmp"
  [[ -x "${tmp}/AdGuardHome/AdGuardHome" ]] || fail "release binary missing after extraction"
  extracted_version="$("${tmp}/AdGuardHome/AdGuardHome" --version 2>/dev/null || true)"
  grep -Fq "${VERSION#v}" <<<"$extracted_version" || fail "extracted binary version mismatch: $extracted_version"
  echo "extracted_version=${extracted_version}"

  sudo install -d -m 0755 -o root -g root "$INSTALL_DIR"
  sudo install -m 0755 -o root -g root "${tmp}/AdGuardHome/AdGuardHome" "$BINARY"
  for f in LICENSE.txt README.md CHANGELOG.md; do
    if [[ -f "${tmp}/AdGuardHome/${f}" ]]; then
      sudo install -m 0644 -o root -g root "${tmp}/AdGuardHome/${f}" "${INSTALL_DIR}/${f}"
    fi
  done

  # Use AdGuard Home's supported built-in service installer. UFW remains
  # default-deny and no public DNS/admin port is opened by this task.
  if ! (cd "$INSTALL_DIR" && sudo "$BINARY" -s install); then
    (cd "$INSTALL_DIR" && sudo "$BINARY" -s uninstall) >/dev/null 2>&1 || true
    sudo rm -rf "$INSTALL_DIR"
    fail "AdGuard Home service installation failed and fresh install was rolled back"
  fi
fi

unit="$(systemctl list-unit-files 'AdGuardHome.service' --no-legend 2>/dev/null | awk 'NR==1 {print $1}' || true)"
[[ "$unit" == "AdGuardHome.service" ]] || fail "AdGuardHome.service not installed"
sudo systemctl is-enabled --quiet AdGuardHome.service || fail "AdGuardHome.service is not enabled"
sudo systemctl is-active --quiet AdGuardHome.service || fail "AdGuardHome.service is not active"
pass "AdGuardHome.service is enabled and active"

version_out="$($BINARY --version 2>/dev/null || true)"
grep -Fq "${VERSION#v}" <<<"$version_out" || fail "installed version mismatch: $version_out"
echo "installed_version=${version_out}"

# Keep administration and resolver service unexposed until later tasks.
ufw_status="$(sudo ufw status verbose)"
grep -q '^Status: active' <<<"$ufw_status" || fail "UFW is not active"
# At this stage only SSH may be allowed inbound.
while IFS= read -r line; do
  [[ "$line" == *ALLOW* ]] || continue
  [[ "$line" == 22/tcp* ]] || fail "unexpected UFW allow rule after install: $line"
done <<<"$(sudo ufw status)"
pass "no public AdGuard/admin firewall port was opened"

printf 'adguard_listener_inventory_begin\n'
sudo ss -H -lntup | awk '/AdGuardHome/ {print}' | sort -u || true
printf 'adguard_listener_inventory_end\n'

# Fresh install should expose the setup/admin listener locally on the host but
# it remains blocked by UFW from inbound networks until later authorized tasks.
if ! sudo ss -H -lntp | grep -q 'AdGuardHome'; then
  fail "AdGuard Home has no TCP listener after service start"
fi

printf 'TSK_0203_MUTATION=PASS\n'
