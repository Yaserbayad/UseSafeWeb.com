#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
TARGET="$ROOT/infrastructure/adguard-server/deploy_or_recover.sh"
DESIGN="$ROOT/infrastructure/adguard-server/TSK-0445-DEPLOYMENT-RECOVERY-SCRIPT-DESIGN.md"
CONTRACT="$ROOT/infrastructure/adguard-server/TSK-0446-RECOVERY-SCOPE-CONTRACT.md"
BUNDLE="$ROOT/infrastructure/adguard-server/tsk-0413-bundle-v1/bundle.json"

fail() { printf 'FAIL  %s\n' "$*" >&2; exit 1; }
pass() { printf 'PASS  %s\n' "$*"; }
require_literal() { grep -Fq -- "$1" "$TARGET" || fail "missing required contract literal: $1"; }
require_regex() { grep -Eq -- "$1" "$TARGET" || fail "missing required contract pattern: $1"; }
forbid_regex() { ! grep -Eq -- "$1" "$TARGET" || fail "forbidden pattern present: $1"; }

[[ -r "$DESIGN" && -r "$CONTRACT" && -r "$BUNDLE" ]] || fail 'authoritative design/contract/bundle input missing'
[[ -f "$TARGET" ]] || fail 'deploy_or_recover.sh is not implemented'
[[ -x "$TARGET" ]] || fail 'deploy_or_recover.sh is not executable'

bash -n "$TARGET" || fail 'bash syntax invalid'
head -n 1 "$TARGET" | grep -Fxq '#!/usr/bin/env bash' || fail 'unexpected shebang'
require_literal 'set -Eeuo pipefail'
require_literal 'umask 077'
for mode in --check --apply --verify --remove; do require_literal "$mode"; done
require_literal '--config'
require_literal '/etc/usesafeweb/recovery.env'
require_literal '/etc/usesafeweb/secrets'
require_literal '/run/lock/usesafeweb-adguard-recovery.lock'
require_literal 'flock'
require_literal 'v0.107.79'
require_literal 'c48f4a43000665484c5ec28177de11a004759b620dae8f77b2aabefc9ef3687f'
require_literal 'tsk-0413-bundle-v1'
require_literal 'verify_bundle.py'
require_literal 'SHA256SUMS'
require_literal 'dns.usesafeweb.com'
require_literal 'https://dns.usesafeweb.com/dns-query'
require_literal 'https://dns10.quad9.net/dns-query'
require_literal '127.0.0.1:3000'
require_literal '9.9.9.10'
require_literal '149.112.112.10'
require_literal '2620:fe::10'
require_literal '2620:fe::fe:10'
require_literal 'filter_1.txt'
require_literal '/srv/usesafeweb-backups'
require_literal 'nginx'
require_literal 'certbot'
require_regex 'query(log|_logging)'
require_regex 'statistics'
require_literal '1d'
require_regex 'anonym'
require_regex 'ECS|edns_client_subnet'
require_regex 'rollback|compensat'
require_regex 'retry'
require_regex 'uncertain'
require_regex 'verify'
require_regex 'mktemp'
require_regex 'sha256'
require_regex 'root'
require_regex 'symlink|readlink|realpath'
require_regex '0600|600'
require_regex '443'
require_regex '853'
forbid_regex '(^|[[:space:]])eval([[:space:]]|$)'
forbid_regex 'bash[[:space:]]+-c[[:space:]].*\$'
forbid_regex 'curl[^\n|]*\|[[:space:]]*(sh|bash)'
! grep -Fq 'clean-recovery-drill-runtime.sh' "$TARGET" || fail 'stale recovery helper must not be composed'
! grep -Fq 'create-encrypted-config-backup.sh' "$TARGET" || fail 'stale backup helper must not be composed'
forbid_regex 'set[[:space:]]+-x'
pass 'TSK-0455 static deployment/recovery contract'
printf 'TSK0455_STATIC_CONTRACT=PASS\n'
