#!/usr/bin/env bash
set -Eeuo pipefail
umask 077

usage(){
  cat >&2 <<'EOF'
Usage:
  verify-owner-encrypted-backup.sh <ssh-target> <ssh-private-key> [age-private-key]

Example:
  verify-owner-encrypted-backup.sh azureusr@srv.UseSafeWeb.com ~/.ssh/id_rsa

The age private key defaults to the SSH private-key path. The private key stays
on the owner's workstation and is never copied to the DNS server or GitHub.
EOF
  exit 2
}

[[ $# -ge 2 && $# -le 3 ]] || usage
TARGET="$1"
SSH_ID="$2"
AGE_ID="${3:-$2}"
EXPECTED_ARCHIVE='usesafeweb-adguard-config-20260827T235612Z.tar.age'
EXPECTED_SHA256='bd5cad421a44efb27a669a0119f6247f456e1e8e97a0f23bb628933e6208ccde'
EXPECTED_SIZE='21121'
EXPECTED_CREATED='2026-08-27T23:56:12Z'
EXPECTED_RECIPIENT_FP='SHA256:682Jbw3baP6jxs57+1c5lchlkrNMELcvDk8bauEl51U'
REMOTE_DIR='/var/backups/usesafeweb/adguard'
TMP=''

fail(){ printf 'FAIL  %s\n' "$*" >&2; exit 1; }
pass(){ printf 'PASS  %s\n' "$*"; }
cleanup(){
  rc=$?
  [[ -n "$TMP" ]] && rm -rf "$TMP" >/dev/null 2>&1 || true
  exit "$rc"
}
trap cleanup EXIT

for c in ssh age tar sha256sum python3 stat; do command -v "$c" >/dev/null || fail "$c missing on owner workstation"; done
[[ -f "$SSH_ID" ]] || fail 'SSH private-key path does not exist'
[[ -f "$AGE_ID" ]] || fail 'age SSH private-key path does not exist'

TMP="$(mktemp -d)"
chmod 700 "$TMP"
ARCHIVE="$TMP/$EXPECTED_ARCHIVE"
META="$TMP/$EXPECTED_ARCHIVE.meta.json"
PACKAGE="$TMP/backup-package.tar"
CONFIG_ARCHIVE="$TMP/configuration.tar"
MANIFEST="$TMP/manifest.json"
RAW_CONFIG="$TMP/AdGuardHome.yaml"

# Fetch only the known ciphertext and non-secret metadata. The owner private key
# stays local; remote sudo reads the root-only backup but never receives a key.
ssh -i "$SSH_ID" -o IdentitiesOnly=yes "$TARGET" \
  "sudo cat '$REMOTE_DIR/$EXPECTED_ARCHIVE'" > "$ARCHIVE"
ssh -i "$SSH_ID" -o IdentitiesOnly=yes "$TARGET" \
  "sudo cat '$REMOTE_DIR/$EXPECTED_ARCHIVE.meta.json'" > "$META"

[[ "$(stat -c '%s' "$ARCHIVE")" == "$EXPECTED_SIZE" ]] || fail 'downloaded ciphertext size mismatch'
actual_sha="$(sha256sum "$ARCHIVE" | awk '{print $1}')"
[[ "$actual_sha" == "$EXPECTED_SHA256" ]] || fail 'downloaded ciphertext checksum mismatch'
pass 'ciphertext checksum verified locally'

python3 - "$META" "$EXPECTED_ARCHIVE" "$EXPECTED_SHA256" "$EXPECTED_SIZE" "$EXPECTED_CREATED" "$EXPECTED_RECIPIENT_FP" <<'PY'
import json,sys
path,name,sha,size,created,fp=sys.argv[1:]
d=json.load(open(path,encoding='utf-8'))
assert d['backup_format']=='usesafeweb.adguard-encrypted-config.v1'
assert d['encrypted_archive']==name
assert d['encrypted_archive_sha256']==sha
assert d['encrypted_archive_size_bytes']==int(size)
assert d['created_utc']==created
assert d['owner_recipient_fingerprint']==fp
print('owner_local_sidecar_verification=PASS')
PY

# This is the acceptance-critical human-owned operation. age reads the owner's
# SSH private key file locally. If the key is passphrase protected, age may ask
# for that passphrase locally; it is never sent to the server or GitHub.
age -d -i "$AGE_ID" -o "$PACKAGE" "$ARCHIVE"
pass 'owner private key decrypted encrypted backup locally'

python3 - "$PACKAGE" <<'PY'
import subprocess,sys
names=subprocess.check_output(['tar','-tf',sys.argv[1]],text=True).splitlines()
assert sorted(names)==['configuration.tar','manifest.json'], names
print('decrypted_package_member_scope=PASS')
PY
tar -xf "$PACKAGE" -C "$TMP" configuration.tar manifest.json

python3 - "$MANIFEST" "$EXPECTED_CREATED" "$EXPECTED_RECIPIENT_FP" <<'PY'
import json,sys
path,created,fp=sys.argv[1:]
d=json.load(open(path,encoding='utf-8'))
assert d['backup_format']=='usesafeweb.adguard-encrypted-config.v1'
assert d['created_utc']==created
assert d['source_host']=='adguardvm'
assert d['service_identity']=='srv.UseSafeWeb.com'
assert d['adguard_home_version']=='v0.107.79'
assert d['owner_recipient_fingerprint']==fp
assert d['included_files']==['AdGuardHome.yaml']
assert 'plaintext admin credential' in d['excluded_classes']
assert 'query/DNS history' in d['excluded_classes']
print('decrypted_manifest_identity_and_scope=PASS')
PY

inner_expected="$(python3 - "$MANIFEST" <<'PY'
import json,sys
print(json.load(open(sys.argv[1],encoding='utf-8'))['configuration_archive_sha256'])
PY
)"
inner_actual="$(sha256sum "$CONFIG_ARCHIVE" | awk '{print $1}')"
[[ "$inner_actual" == "$inner_expected" ]] || fail 'decrypted configuration archive checksum mismatch'

tar -tf "$CONFIG_ARCHIVE" | grep -qx 'AdGuardHome.yaml'
[[ "$(tar -tf "$CONFIG_ARCHIVE" | wc -l | tr -d ' ')" == '1' ]] || fail 'configuration archive contains unexpected files'
tar -xf "$CONFIG_ARCHIVE" -C "$TMP" AdGuardHome.yaml

config_expected="$(python3 - "$MANIFEST" <<'PY'
import json,sys
print(json.load(open(sys.argv[1],encoding='utf-8'))['configuration_file_sha256'])
PY
)"
config_actual="$(sha256sum "$RAW_CONFIG" | awk '{print $1}')"
[[ "$config_actual" == "$config_expected" ]] || fail 'decrypted raw configuration checksum mismatch'

# Validate structure and privacy controls without printing configuration content.
python3 - "$RAW_CONFIG" <<'PY'
import sys,yaml
with open(sys.argv[1],encoding='utf-8') as f: d=yaml.safe_load(f)
q=d.get('querylog') or {}; s=d.get('statistics') or {}; dns=d.get('dns') or {}; tls=d.get('tls') or {}
assert d.get('schema_version')==34
assert q.get('enabled') is False
assert q.get('file_enabled') is False
assert s.get('enabled') is False
assert dns.get('anonymize_client_ip') is True
assert ((d.get('clients') or {}).get('persistent') or [])==[]
assert (d.get('user_rules') or [])==[]
assert not (tls.get('private_key') or tls.get('private_key_path'))
assert not (tls.get('certificate_chain') or tls.get('certificate_chain_path'))
print('decrypted_configuration_privacy_invariants=PASS')
PY

printf 'encrypted_archive_sha256=%s\n' "$actual_sha"
printf 'owner_recipient_fingerprint=%s\n' "$EXPECTED_RECIPIENT_FP"
printf 'decrypted_configuration_sha256=%s\n' "$config_actual"
printf 'TSK_0430_OWNER_DECRYPTION=PASS\n'
