#!/usr/bin/env bash
set -Eeuo pipefail
umask 077

MODE="${1:-}"
case "${MODE}" in
  --ephemeral|--target) ;;
  *) printf 'FAIL usage: --ephemeral|--target\n' >&2; exit 64 ;;
esac

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd -- "${SCRIPT_DIR}/../.." && pwd)"
STATE="${ROOT_DIR}/CURRENT_STATE.md"
TSK0422="${SCRIPT_DIR}/tsk-0422-adguard-config-pipeline.sh"
TSK0451="${SCRIPT_DIR}/tsk-0451-post-vm-security-baseline.sh"
TSK0449_EVIDENCE="${ROOT_DIR}/TSK_0449_DNS_DOH_TLS_AUTOMATION_EVIDENCE_2026-09-04.md"
ACTIVE_DIR=''
ACTIVE_PID=''
ACTIVE_PORT=''

fail() { printf 'FAIL %s\n' "$*" >&2; exit 1; }
pass() { printf '%s=PASS\n' "$1"; }
require_cmd() { command -v "$1" >/dev/null 2>&1 || fail "required command missing: $1"; }

cleanup_active() {
  local rc=$?
  if [[ -n "${ACTIVE_PID}" ]] && kill -0 "${ACTIVE_PID}" >/dev/null 2>&1; then
    kill "${ACTIVE_PID}" >/dev/null 2>&1 || true
    wait "${ACTIVE_PID}" >/dev/null 2>&1 || true
  fi
  if [[ -n "${ACTIVE_DIR}" && -d "${ACTIVE_DIR}" ]]; then
    rm -rf -- "${ACTIVE_DIR}" >/dev/null 2>&1 || true
  fi
  ACTIVE_PID=''
  ACTIVE_PORT=''
  ACTIVE_DIR=''
  return "${rc}"
}
trap cleanup_active EXIT

validate_manifest() {
  python3 - "$1" <<'PY'
import json, sys
with open(sys.argv[1], encoding='utf-8') as f:
    d = json.load(f)
assert d == {
    'data_class': 'synthetic',
    'network_bind': '127.0.0.1',
    'participant_data': False,
    'persistent': False,
    'schema': 'usesafeweb.ephemeral-test-environment.v1',
    'secrets': False,
    'task': 'TSK-0450',
}
PY
}

write_manifest() {
  python3 - "$1" <<'PY'
import json, sys
obj = {
    'data_class': 'synthetic',
    'network_bind': '127.0.0.1',
    'participant_data': False,
    'persistent': False,
    'schema': 'usesafeweb.ephemeral-test-environment.v1',
    'secrets': False,
    'task': 'TSK-0450',
}
with open(sys.argv[1], 'w', encoding='utf-8') as f:
    json.dump(obj, f, sort_keys=True, separators=(',', ':'))
    f.write('\n')
PY
}

start_ephemeral() {
  local base="${RUNNER_TEMP:-/tmp}"
  [[ -d "${base}" ]] || fail 'ephemeral base directory is unavailable'
  ACTIVE_DIR="$(mktemp -d "${base%/}/usesafeweb-tsk0450.XXXXXX")"
  write_manifest "${ACTIVE_DIR}/manifest.json"
  validate_manifest "${ACTIVE_DIR}/manifest.json" || fail 'ephemeral environment manifest failed policy validation'
  printf '%s\n' '{"fixture":"synthetic","task":"TSK-0450"}' > "${ACTIVE_DIR}/fixture.json"

  python3 - "${ACTIVE_DIR}/port" "${ACTIVE_DIR}/fixture.json" <<'PY' &
import http.server, sys
port_file, fixture_file = sys.argv[1:]
with open(fixture_file, encoding='utf-8') as f:
    fixture = f.read().strip().encode('utf-8')
class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            body = b'{"environment":"ephemeral","status":"ok"}'
            code = 200
        elif self.path == '/fixture':
            body = fixture
            code = 200
        else:
            body = b'not found'
            code = 404
        self.send_response(code)
        self.send_header('Content-Type', 'application/json' if code == 200 else 'text/plain')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *_):
        pass
server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), Handler)
with open(port_file, 'w', encoding='ascii') as f:
    f.write(str(server.server_address[1]))
server.serve_forever()
PY
  ACTIVE_PID=$!

  local i
  for i in $(seq 1 100); do
    [[ -s "${ACTIVE_DIR}/port" ]] && break
    kill -0 "${ACTIVE_PID}" >/dev/null 2>&1 || fail 'ephemeral service exited before readiness'
    sleep 0.05
  done
  [[ -s "${ACTIVE_DIR}/port" ]] || fail 'ephemeral service did not publish readiness port'
  ACTIVE_PORT="$(cat "${ACTIVE_DIR}/port")"
  [[ "${ACTIVE_PORT}" =~ ^[0-9]+$ ]] || fail 'ephemeral service published invalid port'

  local health fixture code
  health="$(curl --silent --show-error --fail --max-time 5 "http://127.0.0.1:${ACTIVE_PORT}/health")" || fail 'ephemeral health check failed'
  fixture="$(curl --silent --show-error --fail --max-time 5 "http://127.0.0.1:${ACTIVE_PORT}/fixture")" || fail 'ephemeral fixture check failed'
  code="$(curl --silent --show-error --output /dev/null --write-out '%{http_code}' --max-time 5 "http://127.0.0.1:${ACTIVE_PORT}/not-present")" || true
  [[ "${health}" == '{"environment":"ephemeral","status":"ok"}' ]] || fail 'ephemeral health payload mismatch'
  [[ "${fixture}" == '{"fixture":"synthetic","task":"TSK-0450"}' ]] || fail 'ephemeral synthetic fixture mismatch'
  [[ "${code}" == '404' ]] || fail 'ephemeral negative route was not rejected'
  pass EPHEMERAL_FUNCTIONAL
  pass SYNTHETIC_DATA_ONLY
  pass LOOPBACK_ISOLATION
  printf 'NEGATIVE_UNKNOWN_ROUTE=REJECTED\n'
}

teardown_ephemeral() {
  local old_dir="${ACTIVE_DIR}" old_pid="${ACTIVE_PID}"
  [[ -n "${old_dir}" && -d "${old_dir}" ]] || fail 'no active ephemeral directory to tear down'
  [[ -n "${old_pid}" ]] || fail 'no active ephemeral process to tear down'
  kill "${old_pid}" >/dev/null 2>&1 || true
  wait "${old_pid}" >/dev/null 2>&1 || true
  ACTIVE_PID=''
  ACTIVE_PORT=''
  rm -rf -- "${old_dir}"
  ACTIVE_DIR=''
  [[ ! -e "${old_dir}" ]] || fail 'ephemeral directory survived teardown'
  if kill -0 "${old_pid}" >/dev/null 2>&1; then
    fail 'ephemeral process survived teardown'
  fi
  pass EPHEMERAL_TEARDOWN
  pass ROLLBACK_TEARDOWN
}

negative_manifest_tests() {
  local base="${RUNNER_TEMP:-/tmp}" d
  d="$(mktemp -d "${base%/}/usesafeweb-tsk0450-negative.XXXXXX")"
  trap 'rm -rf -- "'"${d}"'"; cleanup_active' EXIT
  write_manifest "${d}/base.json"
  python3 - "${d}" <<'PY'
import json, os, sys
root = sys.argv[1]
base = json.load(open(os.path.join(root, 'base.json'), encoding='utf-8'))
for name, key, value in (
    ('non-synthetic', 'data_class', 'participant'),
    ('persistent', 'persistent', True),
    ('nonlocal-bind', 'network_bind', '0.0.0.0'),
):
    obj = dict(base)
    obj[key] = value
    with open(os.path.join(root, name + '.json'), 'w', encoding='utf-8') as f:
        json.dump(obj, f, sort_keys=True, separators=(',', ':'))
PY
  if validate_manifest "${d}/non-synthetic.json" >/dev/null 2>&1; then fail 'non-synthetic fixture was accepted'; fi
  if validate_manifest "${d}/persistent.json" >/dev/null 2>&1; then fail 'persistent fixture was accepted'; fi
  if validate_manifest "${d}/nonlocal-bind.json" >/dev/null 2>&1; then fail 'nonlocal-bind fixture was accepted'; fi
  rm -rf -- "${d}"
  trap cleanup_active EXIT
  printf 'NEGATIVE_NON_SYNTHETIC=REJECTED\n'
  printf 'NEGATIVE_PERSISTENT=REJECTED\n'
  printf 'NEGATIVE_NONLOCAL_BIND=REJECTED\n'
  pass EPHEMERAL_NEGATIVE_TESTS
}

run_ephemeral() {
  require_cmd python3
  require_cmd curl
  require_cmd sha256sum
  [[ "${GITHUB_ACTIONS:-}" == 'true' ]] || fail 'ephemeral verification must run in GitHub Actions'
  negative_manifest_tests

  start_ephemeral
  local first_hash first_dir
  first_hash="$(sha256sum "${ACTIVE_DIR}/manifest.json" | awk '{print $1}')"
  first_dir="${ACTIVE_DIR}"
  teardown_ephemeral

  start_ephemeral
  local second_hash second_dir
  second_hash="$(sha256sum "${ACTIVE_DIR}/manifest.json" | awk '{print $1}')"
  second_dir="${ACTIVE_DIR}"
  [[ "${first_hash}" == "${second_hash}" ]] || fail 'rebuilt environment manifest is not deterministic'
  [[ "${first_dir}" != "${second_dir}" ]] || fail 'rebuild reused the prior disposable directory'
  teardown_ephemeral

  pass EPHEMERAL_REBUILD
  pass EPHEMERAL_CONFIGURATION
  pass EPHEMERAL_SECURITY_PRIVACY
  printf 'PERSISTENT_STAGING_PROVISIONED=NO\n'
  printf 'AZURE_CONTROL_PLANE_ACTION=NONE\n'
  printf 'PARTICIPANT_DATA_USED=NO\n'
  printf 'CI_EPHEMERAL_PHASE=PASS\n'
}

run_target() {
  require_cmd curl
  require_cmd python3
  require_cmd sha256sum
  [[ "${EUID}" -eq 0 ]] || fail 'target verification requires root'
  [[ "$(hostname -s)" == 'adguardvm' ]] || fail 'unexpected target host'
  [[ -f "${STATE}" ]] || fail 'CURRENT_STATE.md missing'
  [[ -f "${TSK0422}" && -f "${TSK0451}" && -f "${TSK0449_EVIDENCE}" ]] || fail 'required canonical predecessor artifact missing'
  grep -Fq -- '- `TSK-0435` — Azure VM handoff — evidence blob' "${STATE}" || fail 'owner VM handoff evidence missing'
  grep -Fq '## TSK-0449 current accepted stable state — 2026-09-04' "${STATE}" || fail 'TSK-0449 durable PASS missing'
  grep -Fq 'persistent staging was not triggered' "${TSK0449_EVIDENCE}" || fail 'persistent staging trigger boundary is not proven closed'

  . /etc/os-release
  [[ "${ID:-}" == 'ubuntu' && "${VERSION_ID:-}" == '24.04' ]] || fail 'owner-provided VM is not Ubuntu 24.04 LTS'

  local imds
  imds="$(mktemp)"
  curl --silent --show-error --fail --noproxy '*' --connect-timeout 4 --max-time 8 \
    --header 'Metadata:true' \
    --output "${imds}" \
    'http://169.254.169.254/metadata/instance/compute?api-version=2021-02-01' \
    || fail 'Azure instance metadata lookup failed'
  python3 - "${imds}" <<'PY'
import json, sys
with open(sys.argv[1], encoding='utf-8') as f:
    compute = json.load(f)
location = str(compute.get('location', '')).lower().replace(' ', '')
if location != 'westeurope':
    raise SystemExit(1)
if str(compute.get('osType', '')).lower() not in ('linux', ''):
    raise SystemExit(1)
PY
  rm -f -- "${imds}"
  pass OWNER_VM_REGION_POLICY

  local access_out data_out before_cfg after_cfg
  access_out="$(mktemp)"
  data_out="$(mktemp)"
  before_cfg="$(sha256sum /opt/AdGuardHome/AdGuardHome.yaml | awk '{print $1}')"

  bash "${TSK0451}" --audit > "${access_out}"
  grep -Fq 'ACC_0451=PASS' "${access_out}" || fail 'owner VM access/security baseline failed'
  grep -Fq 'VER_0451=PASS' "${access_out}" || fail 'owner VM access verification failed'
  pass OWNER_VM_ACCESS_POLICY

  bash "${TSK0422}" --verify > "${data_out}"
  grep -Fq 'PERSISTED_CONFIG_MATCH=PASS' "${data_out}" || fail 'persisted privacy/config policy mismatch'
  grep -Fq 'RUNTIME_APPROVED_CONFIG=PASS' "${data_out}" || fail 'runtime privacy/config policy mismatch'
  grep -Fq 'SYNTHETIC_LOOPBACK_DNS=PASS' "${data_out}" || fail 'synthetic target functional check failed'
  grep -Fq 'ACC_0422=PASS' "${data_out}" || fail 'approved AdGuard policy verification failed'
  grep -Fq 'VER_0422=PASS' "${data_out}" || fail 'AdGuard policy target verification failed'
  pass OWNER_VM_DATA_POLICY

  after_cfg="$(sha256sum /opt/AdGuardHome/AdGuardHome.yaml | awk '{print $1}')"
  [[ "${before_cfg}" == "${after_cfg}" ]] || fail 'read-only target verification changed AdGuard configuration'
  rm -f -- "${access_out}" "${data_out}"

  pass OWNER_PROVIDED_PILOT_VM_ACCEPTANCE
  pass TARGET_CONFIGURATION_UNCHANGED
  pass TARGET_SECURITY_PRIVACY
  printf 'PILOT_LIFECYCLE_SEPARATE_ENVIRONMENT=NOT_REQUIRED_UNDER_DEC_0054\n'
  printf 'STAGING_TRIGGER=NOT_OPENED\n'
  printf 'PERSISTENT_STAGING_PROVISIONED=NO\n'
  printf 'AZURE_CONTROL_PLANE_ACTION=NONE\n'
  printf 'TARGET_MUTATION=NONE\n'
  printf 'TARGET_PHASE=PASS\n'
}

case "${MODE}" in
  --ephemeral) run_ephemeral ;;
  --target) run_target ;;
esac
