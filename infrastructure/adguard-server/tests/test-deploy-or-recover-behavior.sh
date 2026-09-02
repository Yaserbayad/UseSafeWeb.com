#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
TARGET="$ROOT/infrastructure/adguard-server/deploy_or_recover.sh"
BUNDLE_ALLOWLIST="$ROOT/infrastructure/adguard-server/tsk-0413-bundle-v1/allowlist.txt"
TEST_ROOT='/etc/usesafeweb'
SECRETS="${TEST_ROOT}/secrets"
CONFIG="${TEST_ROOT}/recovery.env"
LOCK='/run/lock/usesafeweb-adguard-recovery.lock'

test_fail() { printf 'FAIL  %s\n' "$*" >&2; exit 1; }
pass() { printf 'PASS  %s\n' "$*"; }
expect_exit() {
  local expected="$1"; shift
  set +e
  "$@" >/tmp/tsk0455-test.out 2>/tmp/tsk0455-test.err
  local rc=$?
  set -e
  [[ "$rc" == "$expected" ]] || { cat /tmp/tsk0455-test.err >&2; test_fail "expected exit $expected, got $rc: $*"; }
}
write_valid_config() {
  cat >"$CONFIG" <<EOF
TARGET_ROLE=dns-resolver
EXPECTED_HOSTNAME=dns.usesafeweb.com
ADMIN_SSH_CIDR=192.0.2.10/32
ADMIN_USERNAME=usesafeweb-admin
ADMIN_PASSWORD_HASH_FILE=${SECRETS}/admin.bcrypt
BACKUP_PASSPHRASE_FILE=${SECRETS}/backup.pass
ACME_EMAIL_FILE=${SECRETS}/acme.email
BUNDLE_VERSION=1.0.0
BACKUP_DIR=/srv/usesafeweb-backups
PROFILE_DEST=/var/www/usesafeweb/UseSafeWeb-iPhone-DoH.mobileconfig
ENABLE_UFW=true
ALLOW_REMOVE=false
EOF
  chown root:root "$CONFIG"; chmod 0600 "$CONFIG"
}
cleanup() {
  cp -a /tmp/tsk0455-allowlist.original "$BUNDLE_ALLOWLIST" 2>/dev/null || true
  rm -rf "$TEST_ROOT" /tmp/tsk0455-test.out /tmp/tsk0455-test.err /tmp/tsk0455-allowlist.original /tmp/tsk0455-ufw-calls
}
trap cleanup EXIT

[[ "$(id -u)" == 0 ]] || test_fail 'behavior test must run as root on ephemeral CI'
[[ -x "$TARGET" ]] || test_fail 'target missing'

# Sourcing is required for deterministic unit tests and must never execute main.
# shellcheck disable=SC1090
source "$TARGET"

a=0
flaky() { a=$((a + 1)); (( a >= 3 )); }
sleep() { :; }
retry_transient 3 flaky || test_fail 'bounded retry did not reconcile third-attempt success'
unset -f sleep
[[ "$a" == 3 ]] || test_fail 'bounded retry attempted an unexpected number of times'
pass 'bounded transient retry'

install -d -m 0700 -o root -g root "$SECRETS" /run/lock
printf '%s\n' '$2b$12$012345678901234567890u12345678901234567890123456789012' >"${SECRETS}/admin.bcrypt"
printf '%s\n' 'synthetic-test-passphrase-not-a-real-secret' >"${SECRETS}/backup.pass"
printf '%s\n' 'ops@example.invalid' >"${SECRETS}/acme.email"
chown root:root "${SECRETS}/"*; chmod 0600 "${SECRETS}/"*
write_valid_config

"$TARGET" --check --config "$CONFIG" | grep -Fxq 'TSK0455_CHECK=PASS' || test_fail 'valid read-only preflight did not pass'
pass 'valid read-only preflight'

expect_exit 10 "$TARGET" --unknown
expect_exit 10 "$TARGET" --check --config '/etc/usesafeweb/../unsafe.env'

cp "$CONFIG" "${TEST_ROOT}/bad.env"; printf '%s\n' 'UNKNOWN_KEY=value' >>"${TEST_ROOT}/bad.env"; chmod 0600 "${TEST_ROOT}/bad.env"; expect_exit 10 "$TARGET" --check --config "${TEST_ROOT}/bad.env"
cp "$CONFIG" "${TEST_ROOT}/dup.env"; printf '%s\n' 'TARGET_ROLE=dns-resolver' >>"${TEST_ROOT}/dup.env"; chmod 0600 "${TEST_ROOT}/dup.env"; expect_exit 10 "$TARGET" --check --config "${TEST_ROOT}/dup.env"
cp "$CONFIG" "${TEST_ROOT}/malformed.env"; printf '%s\n' 'MALFORMED LINE' >>"${TEST_ROOT}/malformed.env"; chmod 0600 "${TEST_ROOT}/malformed.env"; expect_exit 10 "$TARGET" --check --config "${TEST_ROOT}/malformed.env"
pass 'malformed/unknown/duplicate config rejection'

chmod 0644 "${SECRETS}/admin.bcrypt"; expect_exit 10 "$TARGET" --check --config "$CONFIG"; chmod 0600 "${SECRETS}/admin.bcrypt"
ln -s "${SECRETS}/backup.pass" "${SECRETS}/symlink.pass"
sed "s#BACKUP_PASSPHRASE_FILE=.*#BACKUP_PASSPHRASE_FILE=${SECRETS}/symlink.pass#" "$CONFIG" >"${TEST_ROOT}/symlink.env"; chmod 0600 "${TEST_ROOT}/symlink.env"; expect_exit 10 "$TARGET" --check --config "${TEST_ROOT}/symlink.env"
pass 'unsafe secret metadata rejection'

cp -a "$BUNDLE_ALLOWLIST" /tmp/tsk0455-allowlist.original
printf 'tamper\n' >>"$BUNDLE_ALLOWLIST"
expect_exit 40 "$TARGET" --check --config "$CONFIG"
cp -a /tmp/tsk0455-allowlist.original "$BUNDLE_ALLOWLIST"
pass 'bundle checksum tamper rejection'

: >"$LOCK"; chmod 0600 "$LOCK"
flock -n "$LOCK" -c 'sleep 4' &
locker=$!
sleep 0.2
expect_exit 50 "$TARGET" --check --config "$CONFIG"
wait "$locker"
pass 'concurrent invocation rejection'

expect_exit 10 "$TARGET" --remove --config "$CONFIG"
pass 'guarded remove refusal'

# A verified compliant host must exit --apply before any mutator executes.
set +e
noop_out="$(
  (
    set -e
    verify_state() { return 0; }
    snapshot_for_rollback() { printf 'unexpected mutation\n' >&2; exit 97; }
    apply_state
  ) 2>&1
)"
noop_rc=$?
set -e
[[ "$noop_rc" == 0 ]] || test_fail "verified-compliant apply did not no-op; rc=${noop_rc}; output=${noop_out}"
grep -Fxq 'TSK0455_APPLY_NOOP=PASS' <<<"$noop_out" || test_fail 'verified-compliant apply did not emit stable no-op evidence'
pass 'verified second apply is mutation-free no-op'

# Firewall reconciliation must not append rules or rewrite defaults when exact state is already present.
UFW_SCENARIO='exact'
: >/tmp/tsk0455-ufw-calls
ufw() {
  printf '%s\n' "$*" >>/tmp/tsk0455-ufw-calls
  case "$*" in
    'status')
      cat <<'EOF'
Status: active
To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    192.0.2.10/32
80/tcp                     ALLOW IN    Anywhere
443/tcp                    ALLOW IN    Anywhere
853/tcp                    ALLOW IN    Anywhere
80/tcp (v6)                ALLOW IN    Anywhere (v6)
443/tcp (v6)               ALLOW IN    Anywhere (v6)
853/tcp (v6)               ALLOW IN    Anywhere (v6)
EOF
      ;;
    'status verbose')
      cat <<'EOF'
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip
EOF
      ;;
    'show added')
      cat <<'EOF'
Added user rules (see 'ufw status' for running firewall):
ufw allow from 192.0.2.10/32 to any port 22 proto tcp comment 'UseSafeWeb admin SSH'
ufw allow 80/tcp comment 'UseSafeWeb ACME HTTP-01'
ufw allow 443/tcp comment 'UseSafeWeb DoH'
ufw allow 853/tcp comment 'UseSafeWeb DoT'
EOF
      ;;
    *) return 0 ;;
  esac
}
configure_firewall
if grep -Evq '^(status|status verbose|show added)$' /tmp/tsk0455-ufw-calls; then
  cat /tmp/tsk0455-ufw-calls >&2
  test_fail 'exact firewall state caused a mutating UFW command'
fi
pass 'exact firewall state is a no-op'

# A broad or otherwise non-project UFW allow must fail closed, not be accepted because its port number is familiar.
UFW_SCENARIO='overbroad'
ufw() {
  case "$*" in
    'status')
      cat <<'EOF'
Status: active
To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    Anywhere
80/tcp                     ALLOW IN    Anywhere
443/tcp                    ALLOW IN    Anywhere
853/tcp                    ALLOW IN    Anywhere
EOF
      ;;
    'status verbose') printf '%s\n' 'Status: active' 'Default: deny (incoming), allow (outgoing), disabled (routed)' ;;
    'show added')
      cat <<'EOF'
Added user rules (see 'ufw status' for running firewall):
ufw allow 22/tcp
ufw allow 80/tcp comment 'UseSafeWeb ACME HTTP-01'
ufw allow 443/tcp comment 'UseSafeWeb DoH'
ufw allow 853/tcp comment 'UseSafeWeb DoT'
EOF
      ;;
    *) return 0 ;;
  esac
}
set +e
( configure_firewall ) >/tmp/tsk0455-test.out 2>/tmp/tsk0455-test.err
over_rc=$?
set -e
[[ "$over_rc" == 50 ]] || { cat /tmp/tsk0455-test.err >&2; test_fail "over-broad SSH firewall rule was not refused with uncertain exit 50; rc=${over_rc}"; }
pass 'over-broad firewall rule fails closed'
unset -f ufw

# Static evidence for idempotent no-op, failed-verification rollback and ambiguous-effect reconciliation.
grep -Fq 'cmp -s' "$TARGET" || test_fail 'no-op comparison missing'
grep -Fq 'trap on_error ERR' "$TARGET" || test_fail 'failed-verification rollback trap missing'
grep -Fq 'rollback' "$TARGET" || test_fail 'rollback implementation missing'
grep -Fq 'certificate issuance outcome uncertain; reconcile before retry' "$TARGET" || test_fail 'ambiguous cert effect reconciliation missing'
grep -Fq 'different or unrecognized AdGuard Home installation exists; refusing overwrite' "$TARGET" || test_fail 'unsupported installed-version guard missing'
pass 'idempotency/rollback/ambiguous-effect guards'

printf 'TSK0455_BEHAVIOR_CONTRACT=PASS\n'
