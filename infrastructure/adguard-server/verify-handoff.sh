#!/usr/bin/env bash
set -euo pipefail

# UseSafeWeb TSK-0435 read-only Azure VM handoff verifier.
# Azure IMDS usage follows Microsoft Learn:
# https://learn.microsoft.com/en-us/azure/virtual-machines/instance-metadata-service

EXPECTED_HOSTNAME="${1:-srv.UseSafeWeb.com}"
EXPECTED_REGION="${EXPECTED_REGION:-westeurope}"
EXPECTED_UBUNTU_VERSION="${EXPECTED_UBUNTU_VERSION:-24.04}"
IMDS_API_VERSION="${IMDS_API_VERSION:-2025-04-07}"
REQUIRE_SSH="${REQUIRE_SSH:-1}"

failures=0
warnings=0

pass() { printf 'PASS  %s\n' "$*"; }
warn() { printf 'WARN  %s\n' "$*"; warnings=$((warnings + 1)); }
fail() { printf 'FAIL  %s\n' "$*"; failures=$((failures + 1)); }

need_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    fail "required command missing: $1"
    return 1
  fi
}

printf 'UseSafeWeb TSK-0435 handoff verification\n'
printf 'checked_at_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
printf 'expected_hostname=%s\n' "$EXPECTED_HOSTNAME"
printf 'expected_region=%s\n' "$EXPECTED_REGION"
printf 'expected_ubuntu_version=%s\n' "$EXPECTED_UBUNTU_VERSION"
printf '\n'

for cmd in curl python3 getent hostname; do
  need_cmd "$cmd" || true
done
if (( failures > 0 )); then
  printf '\nOVERALL=FAIL failures=%d warnings=%d\n' "$failures" "$warnings"
  exit 1
fi

# Local OS baseline.
if [[ -r /etc/os-release ]]; then
  # shellcheck disable=SC1091
  source /etc/os-release
  if [[ "${ID:-}" == "ubuntu" ]]; then
    pass "OS ID is Ubuntu"
  else
    fail "OS ID is '${ID:-unknown}', expected ubuntu"
  fi
  if [[ "${VERSION_ID:-}" == "$EXPECTED_UBUNTU_VERSION" ]]; then
    pass "Ubuntu VERSION_ID is $EXPECTED_UBUNTU_VERSION"
  else
    fail "Ubuntu VERSION_ID is '${VERSION_ID:-unknown}', expected $EXPECTED_UBUNTU_VERSION"
  fi
else
  fail "/etc/os-release is not readable"
fi

local_hostname="$(hostname -f 2>/dev/null || hostname 2>/dev/null || true)"
printf 'local_hostname=%s\n' "${local_hostname:-unknown}"

# Running this script in an SSH session is the strongest proof available here
# that the host is reachable through the intended remote deployment path.
if [[ -n "${SSH_CONNECTION:-}" ]]; then
  pass "verification is executing through an SSH session"
else
  if [[ "$REQUIRE_SSH" == "1" ]]; then
    fail "SSH_CONNECTION is absent; approved remote deployment-path reachability is not proven"
  else
    warn "SSH_CONNECTION is absent; inventory-only mode cannot prove deployment-path reachability"
  fi
fi

imds_url="http://169.254.169.254/metadata/instance?api-version=${IMDS_API_VERSION}"
imds_json=""
if imds_json="$(curl -fsS -H 'Metadata:true' --noproxy '*' --connect-timeout 2 --max-time 6 "$imds_url" 2>/dev/null)"; then
  pass "Azure Instance Metadata Service is reachable"
else
  fail "Azure Instance Metadata Service request failed"
fi

metadata_lines=""
if [[ -n "$imds_json" ]]; then
  if metadata_lines="$(python3 -c '
import json, sys
obj = json.load(sys.stdin)
compute = obj.get("compute") or {}
network = obj.get("network") or {}
public_ips = []
for iface in network.get("interface") or []:
    ipv4 = iface.get("ipv4") or {}
    for item in ipv4.get("ipAddress") or []:
        pub = (item.get("publicIpAddress") or "").strip()
        if pub:
            public_ips.append(pub)
print("location=" + str(compute.get("location") or ""))
print("vm_name=" + str(compute.get("name") or ""))
print("vm_size=" + str(compute.get("vmSize") or ""))
print("zone=" + str(compute.get("zone") or ""))
print("os_type=" + str(compute.get("osType") or ""))
print("public_ips=" + ",".join(dict.fromkeys(public_ips)))
' <<<"$imds_json")"; then
    pass "Azure metadata JSON parsed"
  else
    fail "Azure metadata JSON could not be parsed"
  fi
fi

location=""
os_type=""
public_ips=""
if [[ -n "$metadata_lines" ]]; then
  while IFS='=' read -r key value; do
    case "$key" in
      location) location="$value" ;;
      os_type) os_type="$value" ;;
      public_ips) public_ips="$value" ;;
    esac
    printf 'azure_%s=%s\n' "$key" "$value"
  done <<< "$metadata_lines"

  if [[ "${location,,}" == "${EXPECTED_REGION,,}" ]]; then
    pass "Azure region is $EXPECTED_REGION"
  else
    fail "Azure region is '${location:-unknown}', expected $EXPECTED_REGION"
  fi

  if [[ "${os_type,,}" == "linux" ]]; then
    pass "Azure metadata reports Linux"
  else
    fail "Azure metadata osType is '${os_type:-unknown}', expected Linux"
  fi
fi

mapfile -t resolved_ips < <(getent ahostsv4 "$EXPECTED_HOSTNAME" 2>/dev/null | awk '$2 == "STREAM" {print $1}' | sort -u)
if (( ${#resolved_ips[@]} > 0 )); then
  printf 'dns_ipv4=%s\n' "$(IFS=,; echo "${resolved_ips[*]}")"
  pass "$EXPECTED_HOSTNAME resolves through the host resolver"
else
  fail "$EXPECTED_HOSTNAME has no IPv4 result through the host resolver"
fi

if [[ -n "$public_ips" && ${#resolved_ips[@]} -gt 0 ]]; then
  matched=0
  IFS=',' read -r -a imds_public <<< "$public_ips"
  for dns_ip in "${resolved_ips[@]}"; do
    for azure_ip in "${imds_public[@]}"; do
      if [[ -n "$azure_ip" && "$dns_ip" == "$azure_ip" ]]; then
        matched=1
      fi
    done
  done
  if (( matched == 1 )); then
    pass "DNS A record matches an Azure IMDS public IPv4 address"
  else
    fail "DNS A record does not match Azure IMDS public IPv4 address(es)"
  fi
elif [[ -z "$public_ips" ]]; then
  warn "Azure IMDS exposes no public IPv4 address; DNS-to-public-IP correlation is not applicable"
fi

printf '\nlistener_inventory_begin\n'
if command -v ss >/dev/null 2>&1; then
  # Deliberately omit process names/PIDs. This is evidence of network exposure,
  # not a process-forensics dump.
  ss -H -lntu 2>/dev/null | awk '{print $1, $5}' | sort -u || true
else
  warn "ss command is unavailable; listener inventory was not collected"
fi
printf 'listener_inventory_end\n'

printf '\n'
if (( failures == 0 )); then
  printf 'OVERALL=PASS failures=0 warnings=%d\n' "$warnings"
  exit 0
fi
printf 'OVERALL=FAIL failures=%d warnings=%d\n' "$failures" "$warnings"
exit 1
