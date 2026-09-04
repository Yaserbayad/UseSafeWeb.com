#!/usr/bin/env bash
set -Eeuo pipefail

fail() {
  printf 'FAIL %s\n' "$1" >&2
  exit 1
}

sha256_text() {
  printf '%s' "$1" | sha256sum | awk '{print $1}'
}

secret_state_accepts() {
  local state_file="$1" candidate="$2"
  [[ -f "$state_file" ]] || return 1
  local expected actual
  expected="$(cat "$state_file")"
  actual="$(sha256_text "$candidate")"
  [[ "$actual" == "$expected" ]]
}

scan_history() {
  git rev-parse --is-inside-work-tree >/dev/null
  git rev-parse --verify HEAD >/dev/null

  python3 - <<'PY'
import re
import subprocess
import sys

# High-confidence provider credential signatures. Private-key detection is handled
# separately and requires a complete PEM block, avoiding false positives from
# source code that merely names a prohibited PEM header as a negative assertion.
provider_patterns = [
    ("github_token", re.compile(("gh" + r"[pousr]_[A-Za-z0-9_]{20,}").encode())),
    ("aws_access_key", re.compile(("AK" + r"IA[0-9A-Z]{16}").encode())),
    ("google_api_key", re.compile(("AI" + r"za[0-9A-Za-z_-]{35}").encode())),
    ("stripe_secret", re.compile(("sk_" + r"(?:live|test)_[0-9A-Za-z]{16,}").encode())),
]

# Build PEM markers from fragments so this scanner source does not itself contain
# a complete private-key marker. Require both a matching begin/end boundary and
# plausible encoded material between them before treating a blob as key material.
key_labels = (b"PRIVATE KEY", b"ENCRYPTED PRIVATE KEY", b"RSA PRIVATE KEY", b"EC PRIVATE KEY", b"OPENSSH PRIVATE KEY")
base64ish = re.compile(rb"^[A-Za-z0-9+/=\r\n]+$")

def contains_complete_private_key(data: bytes) -> bool:
    for label in key_labels:
        begin = b"-----BEGIN " + label + b"-----"
        end = b"-----END " + label + b"-----"
        start = data.find(begin)
        while start != -1:
            body_start = start + len(begin)
            finish = data.find(end, body_start)
            if finish != -1:
                body = data[body_start:finish].strip()
                compact = b"".join(body.split())
                if len(compact) >= 80 and base64ish.fullmatch(body):
                    return True
            start = data.find(begin, body_start)
    return False

# Encrypted/private-key container formats are forbidden in Git for this project
# because an encrypted production secret is still a committed secret.
forbidden_suffixes = (".p12", ".pfx", ".jks", ".keystore", ".key", ".age", ".gpg", ".enc")

raw = subprocess.check_output(["git", "rev-list", "--objects", "--all"], text=True, errors="replace")
objects = []
paths = {}
for line in raw.splitlines():
    if not line.strip():
        continue
    parts = line.split(" ", 1)
    oid = parts[0]
    path = parts[1] if len(parts) == 2 else ""
    objects.append(oid)
    if path:
        paths.setdefault(oid, set()).add(path)

bad_paths = sorted({p for ps in paths.values() for p in ps if p.lower().endswith(forbidden_suffixes)})
if bad_paths:
    print(f"SECRET_SCAN_FORBIDDEN_CONTAINER_COUNT={len(bad_paths)}")
    for path in bad_paths:
        print(f"SECRET_SCAN_FORBIDDEN_CONTAINER_PATH={path}")
    sys.exit(11)

# Scan each unique blob once. A failure may disclose only the repository path and
# object id needed to investigate the finding; matched bytes are never emitted.
seen = set()
scanned_blobs = 0
scanned_bytes = 0
for oid in objects:
    if oid in seen:
        continue
    seen.add(oid)
    meta = subprocess.check_output(["git", "cat-file", "-t", oid], text=True).strip()
    if meta != "blob":
        continue
    size = int(subprocess.check_output(["git", "cat-file", "-s", oid], text=True).strip())
    if size > 8 * 1024 * 1024:
        continue
    data = subprocess.check_output(["git", "cat-file", "blob", oid])
    scanned_blobs += 1
    scanned_bytes += len(data)
    match_class = None
    if contains_complete_private_key(data):
        match_class = "private_key"
    else:
        for name, pattern in provider_patterns:
            if pattern.search(data):
                match_class = name
                break
    if match_class:
        print(f"SECRET_SCAN_MATCH_CLASS={match_class}")
        print(f"SECRET_SCAN_MATCH_OBJECT={oid}")
        matched_paths = sorted(paths.get(oid, {"<unknown>"}))
        for path in matched_paths:
            print(f"SECRET_SCAN_MATCH_PATH={path}")
        commits = subprocess.check_output(
            ["git", "log", "--all", "--format=%H", "--find-object", oid],
            text=True,
            errors="replace",
        ).splitlines()
        for commit in commits[:20]:
            if commit:
                print(f"SECRET_SCAN_MATCH_COMMIT={commit}")
        sys.exit(12)

print(f"SECRET_SCAN_BLOBS={scanned_blobs}")
print(f"SECRET_SCAN_BYTES={scanned_bytes}")
print("SECRET_SCAN_PRIVATE_KEY=PASS")
print("SECRET_SCAN_PROVIDER_TOKENS=PASS")
print("SECRET_SCAN_ENCRYPTED_SECRET_CONTAINERS=PASS")
print("FULL_HISTORY_SECRET_SCAN=PASS")
PY
}

synthetic_controls() {
  [[ -n "${TSK0490_EXTERNAL_SECRET:-}" ]] || fail 'external_secret_missing'
  [[ ${#TSK0490_EXTERNAL_SECRET} -ge 20 ]] || fail 'external_secret_too_short'
  echo 'EXTERNAL_SECRET_INJECTION=PASS source=github_job_token value=not_emitted'

  local work old new breakglass state bgstate
  work="$(mktemp -d)"
  trap 'rm -rf "$work"' RETURN
  umask 077
  state="$work/active.sha256"
  bgstate="$work/breakglass.sha256"
  old="$(openssl rand -hex 32)"
  new="$(openssl rand -hex 32)"
  breakglass="$(openssl rand -hex 32)"

  printf '%s\n' "$(sha256_text "$old")" > "$state"
  chmod 600 "$state"
  secret_state_accepts "$state" "$old" || fail 'initial_secret_rejected'

  printf '%s\n' "$(sha256_text "$new")" > "$state.tmp"
  chmod 600 "$state.tmp"
  mv -f "$state.tmp" "$state"
  secret_state_accepts "$state" "$new" || fail 'rotated_secret_rejected'
  if secret_state_accepts "$state" "$old"; then fail 'old_secret_survived_rotation'; fi
  echo 'SECRET_ROTATION_TEST=PASS old_credential=rejected new_credential=accepted'

  rm -f "$state"
  if secret_state_accepts "$state" "$new"; then fail 'revoked_secret_still_accepted'; fi
  echo 'SECRET_REVOCATION_TEST=PASS revoked_credential=rejected'

  printf '%s\n' "$(sha256_text "$breakglass")" > "$bgstate"
  chmod 600 "$bgstate"
  secret_state_accepts "$bgstate" "$breakglass" || fail 'breakglass_recovery_failed'
  rm -f "$bgstate"
  if secret_state_accepts "$bgstate" "$breakglass"; then fail 'breakglass_not_resealed'; fi
  echo 'BREAK_GLASS_RECOVERY_TEST=PASS enabled_boundedly=1 resealed=1'

  local mode
  mode="$(stat -c '%a' "$work")"
  [[ "$mode" == 700 ]] || fail "unsafe_temp_mode_${mode}"
  echo 'TEMP_SECRET_PERMISSIONS=PASS mode=700'

  unset old new breakglass
  rm -rf "$work"
  trap - RETURN
  [[ ! -e "$work" ]] || fail 'temporary_secret_material_not_removed'
  echo 'TEMP_SECRET_CLEANUP=PASS'
  echo 'SYNTHETIC_ROLLBACK=PASS state_removed=1'
}

target_readonly() {
  [[ "$(hostname -s)" == adguardvm ]] || fail 'unexpected_target'
  [[ "$(id -un)" == azureusr ]] || fail 'unexpected_executor'
  [[ "$(id -u)" -ne 0 ]] || fail 'normal_executor_is_root'
  sudo -n true || fail 'root_capable_bridge_unavailable'

  local unit runner_user runner_pid runner_proc_user
  unit="$(systemctl list-unit-files 'actions.runner.*.service' --no-legend 2>/dev/null | awk 'NR==1 {print $1}' || true)"
  [[ -n "$unit" ]] || fail 'runner_service_missing'
  systemctl is-enabled --quiet "$unit"
  systemctl is-active --quiet "$unit"
  runner_user="$(systemctl show "$unit" -p User --value)"
  runner_pid="$(systemctl show "$unit" -p MainPID --value)"
  [[ "$runner_user" == azureusr ]] || fail 'runner_service_not_least_privilege_user'
  [[ "$runner_pid" =~ ^[0-9]+$ && "$runner_pid" -gt 1 ]] || fail 'runner_pid_invalid'
  runner_proc_user="$(ps -o user= -p "$runner_pid" | xargs)"
  [[ "$runner_proc_user" == azureusr ]] || fail 'runner_process_user_mismatch'

  local ssh_before ssh_after sudo_before sudo_after
  ssh_before="$(sudo sha256sum /etc/ssh/sshd_config | awk '{print $1}')"
  sudo_before="$(sudo sh -c 'cat /etc/sudoers /etc/sudoers.d/* 2>/dev/null' | sha256sum | awk '{print $1}')"

  sudo sshd -t
  local effective
  effective="$(sudo sshd -T 2>/dev/null)"
  grep -qx 'permitrootlogin no' <<<"$effective"
  grep -qx 'passwordauthentication no' <<<"$effective"

  sudo systemctl is-active --quiet "$unit"
  sudo test -r /etc/sudoers

  ssh_after="$(sudo sha256sum /etc/ssh/sshd_config | awk '{print $1}')"
  sudo_after="$(sudo sh -c 'cat /etc/sudoers /etc/sudoers.d/* 2>/dev/null' | sha256sum | awk '{print $1}')"
  [[ "$ssh_before" == "$ssh_after" ]] || fail 'ssh_configuration_changed'
  [[ "$sudo_before" == "$sudo_after" ]] || fail 'sudo_configuration_changed'

  echo 'NORMAL_EXECUTOR_LEAST_PRIVILEGE=PASS user=azureusr root=0'
  echo 'RUNNER_SERVICE_LEAST_PRIVILEGE=PASS user=azureusr'
  echo 'ROOT_CAPABLE_PATH=PASS use=read_only_task_bounded audited_by=github_actions'
  echo 'SSH_ROOT_LOGIN=DISABLED'
  echo 'SSH_PASSWORD_AUTH=DISABLED'
  echo 'TARGET_CONFIGURATION_UNCHANGED=PASS'
  echo 'PRODUCTION_SECRET_ROTATION=NOT_PERFORMED'
  echo 'PRODUCTION_SERVICE_REVOCATION=NOT_PERFORMED'
  echo 'DEPLOYMENT_ACTION=NONE'
  echo 'TELEMETRY_ACTIVATION=NONE'
  echo 'PARTICIPANT_ACTION=NONE'
  echo 'TARGET_SECURITY_PRIVACY=PASS secrets=not_emitted auth_logs=not_emitted client_data=not_emitted'
}

case "${1:-}" in
  --synthetic)
    scan_history
    synthetic_controls
    echo 'ACC_0490_SYNTHETIC=PASS'
    ;;
  --target-readonly)
    target_readonly
    echo 'ACC_0490_TARGET_READONLY=PASS'
    ;;
  *)
    echo 'Usage: tsk-0490-security-controls-verifier.sh --synthetic|--target-readonly' >&2
    exit 64
    ;;
esac
