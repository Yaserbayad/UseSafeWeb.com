#!/usr/bin/env bash
set -Eeuo pipefail

# UseSafeWeb TSK-0451 post-VM server security baseline delta for Ubuntu 24.04 LTS.
# This script deliberately does not rewrite SSH or UFW. It first proves the
# previously accepted SSH/UFW baseline, then adds only the missing Fail2ban and
# unattended-upgrades controls required by ACC-0451 / VER-0451.
#
# Official references:
# - OpenSSH sshd_config (Ubuntu 24.04):
#   https://manpages.ubuntu.com/manpages/noble/man5/sshd_config.5.html
# - Fail2ban jail configuration (Ubuntu 24.04):
#   https://manpages.ubuntu.com/manpages/noble/man5/jail.conf.5.html
# - Fail2ban client (Ubuntu 24.04):
#   https://manpages.ubuntu.com/manpages/noble/man1/fail2ban-client.1.html
# - Ubuntu Server automatic updates:
#   https://ubuntu.com/server/docs/how-to/software/automatic-updates/

EXPECTED_UBUNTU_VERSION="${EXPECTED_UBUNTU_VERSION:-24.04}"
AUTO_UPGRADES_FILE="/etc/apt/apt.conf.d/20auto-upgrades"
FAIL2BAN_JAIL_FILE="/etc/fail2ban/jail.d/usesafeweb-sshd.local"
MODE="${1:-}"

pass() { printf 'PASS %s\n' "$*"; }
fail() { printf 'FAIL %s\n' "$*" >&2; exit 1; }

usage() {
  cat <<'USAGE'
Usage:
  sudo bash tsk-0451-post-vm-security-baseline.sh --apply
  sudo bash tsk-0451-post-vm-security-baseline.sh --audit

--apply verifies the existing SSH/UFW baseline before making any change, then
installs/configures Fail2ban and unattended upgrades and performs a full audit.
--audit is read-only and emits only sanitized PASS/FAIL status markers.
USAGE
}

require_root() {
  [[ "${EUID}" -eq 0 ]] || fail 'root privileges are required'
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || fail "required command missing: $1"
}

verify_os() {
  [[ -r /etc/os-release ]] || fail '/etc/os-release is missing'
  # shellcheck disable=SC1091
  . /etc/os-release
  [[ "${ID:-}" == "ubuntu" ]] || fail 'target OS is not Ubuntu'
  [[ "${VERSION_ID:-}" == "${EXPECTED_UBUNTU_VERSION}" ]] || fail "Ubuntu ${EXPECTED_UBUNTU_VERSION} is required"
  pass "OS=ubuntu-${EXPECTED_UBUNTU_VERSION}"
}

verify_sshd() {
  require_cmd sshd
  sshd -t
  local effective
  effective="$(sshd -T 2>/dev/null)"
  grep -qx 'permitrootlogin no' <<<"${effective}" || fail 'effective PermitRootLogin is not no'
  grep -qx 'passwordauthentication no' <<<"${effective}" || fail 'effective PasswordAuthentication is not no'
  pass 'COMMAND=sshd_-t STATUS=PASS'
  pass 'COMMAND=sshd_-T FIELDS=permitrootlogin,passwordauthentication STATUS=PASS'
}

verify_ufw() {
  require_cmd ufw
  local verbose numbered
  verbose="$(ufw status verbose 2>/dev/null)"
  grep -q '^Status: active$' <<<"${verbose}" || fail 'UFW is not active'
  grep -Eq '^Default: deny \(incoming\), allow \(outgoing\)' <<<"${verbose}" || fail 'UFW defaults are not deny-incoming/allow-outgoing'
  numbered="$(ufw status 2>/dev/null)"
  grep -Eq '^22/tcp[[:space:]]+ALLOW([[:space:]]|$)' <<<"${numbered}" || fail 'UFW does not allow SSH on 22/tcp'
  pass 'COMMAND=ufw_status_verbose STATUS=PASS default_deny_incoming=1 default_allow_outgoing=1 ssh_22_allowed=1'
}

verify_unattended_upgrades() {
  dpkg-query -W -f='${Status}\n' unattended-upgrades 2>/dev/null | grep -qx 'install ok installed' || fail 'unattended-upgrades package is not installed'
  systemctl is-enabled --quiet unattended-upgrades.service || fail 'unattended-upgrades.service is not enabled'
  systemctl is-enabled --quiet apt-daily.timer || fail 'apt-daily.timer is not enabled'
  systemctl is-enabled --quiet apt-daily-upgrade.timer || fail 'apt-daily-upgrade.timer is not enabled'
  [[ -f "${AUTO_UPGRADES_FILE}" ]] || fail '20auto-upgrades is missing'
  grep -Fxq 'APT::Periodic::Update-Package-Lists "1";' "${AUTO_UPGRADES_FILE}" || fail 'Update-Package-Lists is not enabled daily'
  grep -Fxq 'APT::Periodic::Unattended-Upgrade "1";' "${AUTO_UPGRADES_FILE}" || fail 'Unattended-Upgrade is not enabled daily'
  pass 'COMMAND=systemctl_is-enabled_unattended-upgrades.service STATUS=PASS'
  pass 'COMMAND=check_20auto-upgrades STATUS=PASS update_lists_daily=1 unattended_upgrade_daily=1'
}

verify_fail2ban() {
  require_cmd fail2ban-client
  dpkg-query -W -f='${Status}\n' fail2ban 2>/dev/null | grep -qx 'install ok installed' || fail 'fail2ban package is not installed'
  fail2ban-client -t >/dev/null 2>&1 || fail 'Fail2ban configuration test failed'
  systemctl is-enabled --quiet fail2ban.service || fail 'fail2ban.service is not enabled'
  systemctl is-active --quiet fail2ban.service || fail 'fail2ban.service is not active'
  local jail_status
  jail_status="$(fail2ban-client status sshd 2>/dev/null)" || fail 'Fail2ban sshd jail status failed'
  grep -q 'Status for the jail: sshd' <<<"${jail_status}" || fail 'Fail2ban sshd jail is not active'
  pass 'COMMAND=fail2ban-client_-t STATUS=PASS'
  pass 'COMMAND=fail2ban-client_status_sshd STATUS=PASS'
}

write_unattended_upgrades_policy() {
  local tmp
  tmp="$(mktemp)"
  cat >"${tmp}" <<'CFG'
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Unattended-Upgrade "1";
CFG
  install -o root -g root -m 0644 "${tmp}" "${AUTO_UPGRADES_FILE}"
  rm -f "${tmp}"
  systemctl enable unattended-upgrades.service >/dev/null
  systemctl enable apt-daily.timer apt-daily-upgrade.timer >/dev/null
}

write_fail2ban_policy() {
  local backup had_backup=0 tmp
  install -d -o root -g root -m 0755 /etc/fail2ban/jail.d
  backup="$(mktemp)"
  if [[ -f "${FAIL2BAN_JAIL_FILE}" ]]; then
    cp -a "${FAIL2BAN_JAIL_FILE}" "${backup}"
    had_backup=1
  fi
  tmp="$(mktemp)"
  cat >"${tmp}" <<'CFG'
[sshd]
enabled = true
backend = systemd
CFG
  install -o root -g root -m 0644 "${tmp}" "${FAIL2BAN_JAIL_FILE}"
  rm -f "${tmp}"

  if ! fail2ban-client -t >/dev/null 2>&1; then
    if [[ "${had_backup}" -eq 1 ]]; then
      install -o root -g root -m 0644 "${backup}" "${FAIL2BAN_JAIL_FILE}"
    else
      rm -f "${FAIL2BAN_JAIL_FILE}"
    fi
    rm -f "${backup}"
    fail 'new Fail2ban configuration did not validate; prior jail configuration restored'
  fi

  if ! systemctl enable --now fail2ban.service >/dev/null; then
    if [[ "${had_backup}" -eq 1 ]]; then
      install -o root -g root -m 0644 "${backup}" "${FAIL2BAN_JAIL_FILE}"
      systemctl restart fail2ban.service >/dev/null 2>&1 || true
    else
      rm -f "${FAIL2BAN_JAIL_FILE}"
      systemctl stop fail2ban.service >/dev/null 2>&1 || true
    fi
    rm -f "${backup}"
    fail 'Fail2ban could not be enabled; prior jail configuration restored'
  fi
  rm -f "${backup}"
}

apply_delta() {
  # Lockout guard: prove the already-accepted access/firewall state before any
  # package or configuration mutation. TSK-0451 itself does not rewrite SSH/UFW.
  verify_sshd
  verify_ufw

  export DEBIAN_FRONTEND=noninteractive
  apt-get update -y >/dev/null
  apt-get install -y fail2ban unattended-upgrades >/dev/null

  write_unattended_upgrades_policy
  write_fail2ban_policy
  pass 'TSK0451_DELTA_APPLIED=1'
}

full_audit() {
  verify_os
  verify_sshd
  verify_ufw
  verify_fail2ban
  verify_unattended_upgrades
  pass 'ACC_0451=PASS'
  pass 'VER_0451=PASS'
  pass 'EVD_0451_SANITIZED_STATUS=PASS'
}

main() {
  require_root
  case "${MODE}" in
    --apply)
      verify_os
      apply_delta
      full_audit
      ;;
    --audit)
      full_audit
      ;;
    -h|--help)
      usage
      ;;
    *)
      usage >&2
      exit 64
      ;;
  esac
}

main "$@"
