#!/usr/bin/env bash
set -Eeuo pipefail

# UseSafeWeb TSK-0437 host security baseline for a fresh Ubuntu 24.04 LTS VM.
# Official references:
# - Ubuntu UFW: https://documentation.ubuntu.com/server/how-to/security/firewalls/
# - Ubuntu security updates: https://documentation.ubuntu.com/security/security-updates/
# - Ubuntu/OpenSSH sshd_config: https://manpages.ubuntu.com/manpages/noble/man5/sshd_config.5.html
#
# Design goals:
# - fail closed before changing SSH authentication unless the current login is
#   proven to have used a public key;
# - keep only SSH exposed before AdGuard is installed;
# - disable direct root/password/keyboard-interactive SSH authentication;
# - apply all currently available Ubuntu package updates and keep unattended
#   security updates enabled;
# - use UFW only when native nftables.service is not active;
# - remain idempotent and preserve the active SSH connection.

EXPECTED_UBUNTU_VERSION="${EXPECTED_UBUNTU_VERSION:-24.04}"
SSH_DROPIN="/etc/ssh/sshd_config.d/00-usesafeweb-hardening.conf"
STATE_DIR="/var/lib/usesafeweb/host-hardening"
MODE="${1:-}"

failures=0
warnings=0

pass() { printf 'PASS  %s\n' "$*"; }
warn() { printf 'WARN  %s\n' "$*"; warnings=$((warnings + 1)); }
fail() { printf 'FAIL  %s\n' "$*"; failures=$((failures + 1)); }
die() { fail "$*"; printf '\nOVERALL=FAIL failures=%d warnings=%d\n' "$failures" "$warnings"; exit 1; }

usage() {
  cat <<'USAGE'
Usage:
  bash harden-host.sh --apply
  sudo bash harden-host.sh --audit
  sudo bash harden-host.sh --rollback

Run --apply from the existing non-root SSH session. The script captures only the
current SSH username/source address and re-executes itself through sudo. Do not
start --apply with sudo, because the original SSH login context is required for
the public-key safety check.
USAGE
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "required command missing: $1"
}

validate_ip() {
  python3 - "$1" <<'PY'
import ipaddress, sys
try:
    ipaddress.ip_address(sys.argv[1])
except ValueError:
    raise SystemExit(1)
PY
}

validate_user() {
  [[ "$1" =~ ^[a-z_][a-z0-9_-]*[$]?$ ]]
}

is_loopback_host() {
  case "$1" in
    127.*|::1|\[::1\]|127.*%*|::1%*) return 0 ;;
    *) return 1 ;;
  esac
}

print_listener_inventory() {
  printf 'listener_inventory_begin\n'
  ss -H -lntu 2>/dev/null | awk '{print $1, $5}' | sort -u || true
  printf 'listener_inventory_end\n'
}

check_external_listeners() {
  local bad=0 proto addr host port
  while read -r proto addr; do
    [[ -n "${proto:-}" && -n "${addr:-}" ]] || continue

    # Extract host/port from IPv4 or [IPv6]:port forms.
    if [[ "$addr" =~ ^\[(.*)\]:([0-9]+)$ ]]; then
      host="${BASH_REMATCH[1]}"; port="${BASH_REMATCH[2]}"
    else
      host="${addr%:*}"; port="${addr##*:}"
    fi

    # Loopback listeners are not public exposure.
    if is_loopback_host "$host" || [[ "$host" == "127.0.0.53%lo" || "$host" == "127.0.0.54" ]]; then
      continue
    fi

    # SSH is the only intentionally exposed service at this pre-AdGuard stage.
    if [[ "$proto" == "tcp" && "$port" == "22" ]]; then
      continue
    fi

    # DHCP client traffic is required host plumbing, not a listening public service.
    if [[ "$proto" == "udp" && "$port" == "68" ]]; then
      continue
    fi

    printf 'UNEXPECTED_LISTENER %s %s\n' "$proto" "$addr"
    bad=1
  done < <(ss -H -lntu 2>/dev/null | awk '{print $1, $5}')
  return "$bad"
}

verify_effective_sshd() {
  local out
  out="$(sshd -T 2>/dev/null)" || return 1

  grep -qx 'permitrootlogin no' <<<"$out" || return 1
  grep -qx 'passwordauthentication no' <<<"$out" || return 1
  grep -qx 'kbdinteractiveauthentication no' <<<"$out" || return 1
  grep -qx 'pubkeyauthentication yes' <<<"$out" || return 1
  grep -qx 'permitemptypasswords no' <<<"$out" || return 1
  grep -qx 'x11forwarding no' <<<"$out" || return 1
  grep -qx 'maxauthtries 3' <<<"$out" || return 1
  grep -qx 'logingracetime 30' <<<"$out" || return 1
}

verify_unattended_upgrades() {
  dpkg-query -W -f='${Status}\n' unattended-upgrades 2>/dev/null | grep -qx 'install ok installed' || return 1
  systemctl is-enabled --quiet apt-daily.timer || return 1
  systemctl is-enabled --quiet apt-daily-upgrade.timer || return 1
  return 0
}

verify_ufw() {
  local status
  status="$(ufw status verbose 2>/dev/null || true)"
  grep -q '^Status: active' <<<"$status" || return 1
  grep -q '^Default: deny (incoming), allow (outgoing)' <<<"$status" || return 1
  verify_ufw_rules_only_ssh || return 1
  return 0
}

verify_no_pending_upgrades() {
  local sim
  sim="$(apt-get -s full-upgrade 2>/dev/null || true)"
  if grep -q '^Inst ' <<<"$sim"; then
    printf '%s\n' "$sim" | grep '^Inst ' | head -20
    return 1
  fi
  return 0
}

verify_public_key_login() {
  local admin_user="$1" source_ip="$2" pattern
  pattern="Accepted publickey for ${admin_user} from ${source_ip}"

  if journalctl -u ssh.service --since '-24 hours' --no-pager 2>/dev/null | grep -Fq "$pattern"; then
    return 0
  fi
  if [[ -r /var/log/auth.log ]] && grep -Fq "$pattern" /var/log/auth.log; then
    return 0
  fi
  return 1
}

restore_ssh_dropin() {
  if [[ -f "$STATE_DIR/original-ssh-dropin" ]]; then
    cp -a "$STATE_DIR/original-ssh-dropin" "$SSH_DROPIN"
  else
    rm -f "$SSH_DROPIN"
  fi
  sshd -t >/dev/null 2>&1 && systemctl reload ssh.service >/dev/null 2>&1 || true
}

verify_ufw_rules_only_ssh() {
  local line
  while IFS= read -r line; do
    [[ "$line" == *ALLOW* ]] || continue
    [[ "$line" == 22/tcp* ]] || { printf 'UNEXPECTED_UFW_ALLOW %s\n' "$line"; return 1; }
  done < <(ufw status 2>/dev/null)
  return 0
}

if [[ "$MODE" == "--apply" && EUID -ne 0 ]]; then
  require_cmd sudo
  require_cmd python3
  [[ -n "${SSH_CONNECTION:-}" ]] || die "--apply must be started from the active SSH user session"

  admin_user="$(id -un)"
  source_ip="${SSH_CONNECTION%% *}"
  validate_user "$admin_user" || die "unexpected SSH username format"
  validate_ip "$source_ip" || die "could not validate current SSH source address"
  script_path="$(readlink -f "$0")"

  printf 'Captured current SSH safety context for user=%s source=%s\n' "$admin_user" "$source_ip"
  exec sudo -- env \
    USW_ADMIN_USER="$admin_user" \
    USW_SSH_SOURCE_IP="$source_ip" \
    bash "$script_path" --apply-root
fi

if [[ "$MODE" == "--apply-root" && EUID -ne 0 ]]; then
  die "internal apply stage requires root"
fi

if [[ "$MODE" == "--audit" || "$MODE" == "--rollback" ]]; then
  (( EUID == 0 )) || die "$MODE requires sudo/root"
fi

if [[ "$MODE" != "--apply-root" && "$MODE" != "--audit" && "$MODE" != "--rollback" ]]; then
  usage
  exit 2
fi

for cmd in bash apt-get dpkg-query getent grep journalctl python3 ss sshd systemctl; do
  require_cmd "$cmd"
done

if [[ -r /etc/os-release ]]; then
  # shellcheck disable=SC1091
  source /etc/os-release
  [[ "${ID:-}" == "ubuntu" ]] || die "OS is '${ID:-unknown}', expected ubuntu"
  [[ "${VERSION_ID:-}" == "$EXPECTED_UBUNTU_VERSION" ]] || die "Ubuntu VERSION_ID is '${VERSION_ID:-unknown}', expected $EXPECTED_UBUNTU_VERSION"
  pass "Ubuntu $EXPECTED_UBUNTU_VERSION baseline confirmed"
else
  die "/etc/os-release is unreadable"
fi

if [[ "$MODE" == "--rollback" ]]; then
  require_cmd ufw
  if [[ -f "$STATE_DIR/original-ssh-dropin" ]]; then
    cp -a "$STATE_DIR/original-ssh-dropin" "$SSH_DROPIN"
  else
    rm -f "$SSH_DROPIN"
  fi
  sshd -t || die "rollback restored SSH configuration but sshd validation failed"
  systemctl reload ssh.service || die "rollback SSH reload failed"

  if [[ -f "$STATE_DIR/ufw-was-inactive" ]]; then
    ufw --force disable >/dev/null
  fi
  pass "UseSafeWeb SSH hardening rollback applied"
  printf '\nOVERALL=PASS failures=0 warnings=%d\n' "$warnings"
  exit 0
fi

if [[ "$MODE" == "--apply-root" ]]; then
  admin_user="${USW_ADMIN_USER:-}"
  source_ip="${USW_SSH_SOURCE_IP:-}"
  validate_user "$admin_user" || die "trusted SSH username context missing/invalid"
  validate_ip "$source_ip" || die "trusted SSH source context missing/invalid"
  id "$admin_user" >/dev/null 2>&1 || die "SSH admin user '$admin_user' does not exist"

  home_dir="$(getent passwd "$admin_user" | cut -d: -f6)"
  [[ -n "$home_dir" && -s "$home_dir/.ssh/authorized_keys" ]] || die "public-key file is missing/empty for '$admin_user'; refusing to disable password SSH"
  verify_public_key_login "$admin_user" "$source_ip" || die "current login could not be proven as public-key authenticated; refusing SSH authentication changes"
  pass "current remote session is proven public-key authenticated"

  if systemctl is-active --quiet nftables.service; then
    die "native nftables.service is active; refusing to layer UFW over another firewall manager"
  fi

  mkdir -p -m 0700 "$STATE_DIR"
  if [[ ! -f "$STATE_DIR/baseline-captured" ]]; then
    if [[ -e "$SSH_DROPIN" ]]; then
      cp -a "$SSH_DROPIN" "$STATE_DIR/original-ssh-dropin"
    fi
    if ! command -v ufw >/dev/null 2>&1 || ! ufw status 2>/dev/null | grep -q '^Status: active'; then
      touch "$STATE_DIR/ufw-was-inactive"
    fi
    touch "$STATE_DIR/baseline-captured"
  fi

  export DEBIAN_FRONTEND=noninteractive
  export NEEDRESTART_MODE=a
  apt-get update
  apt-get -y full-upgrade
  apt-get -y install ufw unattended-upgrades
  systemctl enable --now apt-daily.timer apt-daily-upgrade.timer >/dev/null
  pass "current package upgrades applied and unattended-upgrade timers enabled"

  cat > "$SSH_DROPIN" <<'SSHEOF'
# Managed by UseSafeWeb TSK-0437. Keep this file lexically early because
# OpenSSH uses the first obtained value for each keyword.
PermitRootLogin no
PasswordAuthentication no
KbdInteractiveAuthentication no
PubkeyAuthentication yes
PermitEmptyPasswords no
X11Forwarding no
MaxAuthTries 3
LoginGraceTime 30
SSHEOF
  chmod 0644 "$SSH_DROPIN"

  if ! sshd -t; then
    restore_ssh_dropin
    die "new SSH configuration failed syntax validation and was rolled back"
  fi
  if ! verify_effective_sshd; then
    restore_ssh_dropin
    die "effective sshd settings did not match policy; SSH drop-in was rolled back"
  fi
  if ! systemctl reload ssh.service; then
    restore_ssh_dropin
    die "SSH reload failed; SSH drop-in was rolled back"
  fi
  pass "SSH hardening validated and reloaded"

  if ! ufw default deny incoming >/dev/null \
    || ! ufw default allow outgoing >/dev/null \
    || ! ufw allow 22/tcp comment 'UseSafeWeb SSH' >/dev/null \
    || ! ufw logging off >/dev/null \
    || ! ufw --force enable >/dev/null; then
      [[ -f "$STATE_DIR/ufw-was-inactive" ]] && ufw --force disable >/dev/null 2>&1 || true
      restore_ssh_dropin
      die "UFW configuration failed; managed SSH/UFW changes were rolled back"
  fi
  pass "UFW enabled with default-deny inbound policy and SSH retained"
fi

# Common audit after apply or explicit --audit.
require_cmd ufw
printf '\nsecurity_audit_begin\n'

if verify_effective_sshd; then
  pass "effective SSH admin-access baseline matches policy"
else
  fail "effective SSH admin-access baseline does not match policy"
fi

if verify_ufw; then
  pass "UFW is active with deny-incoming/allow-outgoing defaults"
else
  fail "UFW baseline is not active as required"
fi

if verify_unattended_upgrades; then
  pass "unattended security update mechanism is installed and scheduled"
else
  fail "unattended security update mechanism is not fully enabled"
fi

if verify_no_pending_upgrades; then
  pass "no currently installable package upgrades remain"
else
  fail "installable package upgrades remain"
fi

print_listener_inventory
if check_external_listeners; then
  pass "no unexpected externally listening service detected at pre-AdGuard stage"
else
  fail "unexpected externally listening service detected"
fi

if [[ -e /var/run/reboot-required ]]; then
  warn "reboot is required before the patched host baseline can be considered fully active"
  printf 'REBOOT_REQUIRED=1\n'
fi

printf 'security_audit_end\n\n'

if (( failures > 0 )); then
  printf 'OVERALL=FAIL failures=%d warnings=%d\n' "$failures" "$warnings"
  exit 1
fi
if [[ -e /var/run/reboot-required ]]; then
  printf 'OVERALL=WAITING_REBOOT failures=0 warnings=%d\n' "$warnings"
  exit 2
fi
printf 'OVERALL=PASS failures=0 warnings=%d\n' "$warnings"
