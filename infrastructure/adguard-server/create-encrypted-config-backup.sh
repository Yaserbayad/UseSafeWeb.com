#!/usr/bin/env bash
set -Eeuo pipefail
umask 077

CONFIG='/opt/AdGuardHome/AdGuardHome.yaml'
APPROVED='infrastructure/adguard-server/approved-adguard-config-v1.json'
POLICY='infrastructure/adguard-server/BACKUP_SCOPE_POLICY.md'
AUTH_KEYS='/home/azureusr/.ssh/authorized_keys'
BACKUP_DIR='/var/backups/usesafeweb/adguard'
STAGE=''
SUCCESS=0

fail(){ printf 'FAIL  %s\n' "$*" >&2; exit 1; }
pass(){ printf 'PASS  %s\n' "$*"; }

cleanup(){
  rc=$?
  if [[ -n "$STAGE" ]]; then
    sudo rm -rf "$STAGE" >/dev/null 2>&1 || true
  fi
  exit "$rc"
}
trap cleanup EXIT

sudo -n true || fail 'non-interactive sudo unavailable'
for c in age tar sha256sum python3 ssh-keygen git systemctl; do command -v "$c" >/dev/null || fail "$c missing"; done
[[ "$(hostname -s)" == 'adguardvm' ]] || fail 'unexpected host'
systemctl is-active --quiet AdGuardHome.service || fail 'AdGuard Home service inactive'
[[ "$(git hash-object "$POLICY")" == 'e62b48a3e746b1be90881bbffab3b7680384cc16' ]] || fail 'backup policy blob mismatch'
[[ "$(git hash-object "$APPROVED")" == 'ea85830b5ef9de7f2772e5467570d52013228b0b' ]] || fail 'approved config artifact blob mismatch'

sudo test -f "$CONFIG" || fail 'AdGuard configuration missing'
sudo test -f "$AUTH_KEYS" || fail 'owner SSH recipient file missing'
[[ "$(sudo stat -c '%a %U:%G' "$CONFIG")" == '600 root:root' ]] || fail 'raw config permissions unexpected'
[[ "$(sudo stat -c '%a %U:%G' "$AUTH_KEYS")" == '600 azureusr:azureusr' ]] || fail 'authorized_keys permissions unexpected'

# Prove there is exactly one supported owner SSH recipient and record only its
# public fingerprint, never the public-key body/comment.
sudo python3 - "$AUTH_KEYS" <<'PY'
import sys
lines=[x.strip() for x in open(sys.argv[1],encoding='utf-8',errors='ignore') if x.strip() and not x.lstrip().startswith('#')]
assert len(lines)==1, len(lines)
parts=lines[0].split()
idx=next(i for i,p in enumerate(parts) if p.startswith(('ssh-','ecdsa-','sk-')))
assert parts[idx]=='ssh-rsa', parts[idx]
PY
read -r key_bits recipient_fingerprint < <(sudo ssh-keygen -lf "$AUTH_KEYS" | awk '{print $1,$2}')
[[ "$key_bits" =~ ^[0-9]+$ ]] && (( key_bits >= 2048 )) || fail 'owner SSH RSA key is below supported strength'
[[ -n "$recipient_fingerprint" ]] || fail 'owner SSH recipient fingerprint unavailable'

# Fail closed against any drift from the accepted privacy/filter/upstream
# projection immediately before capture.
sudo python3 - "$CONFIG" "$APPROVED" <<'PY'
import json,sys,yaml
config_path,approved_path=sys.argv[1:3]
with open(config_path,encoding='utf-8') as f: d=yaml.safe_load(f)
with open(approved_path,encoding='utf-8') as f: approved=json.load(f)['settings']
dns=d.get('dns') or {}; filtering=d.get('filtering') or {}; querylog=d.get('querylog') or {}
statistics=d.get('statistics') or {}; http=d.get('http') or {}; tls=d.get('tls') or {}; dhcp=d.get('dhcp') or {}
filters=d.get('filters') or []; edns=dns.get('edns_client_subnet') or {}
clients=(d.get('clients') or {}).get('persistent') or []
assert querylog.get('enabled') is False
assert querylog.get('file_enabled') is False
assert statistics.get('enabled') is False
assert dns.get('anonymize_client_ip') is True
assert clients == []
assert (d.get('user_rules') or []) == []
assert (d.get('whitelist_filters') or []) == []
assert not (tls.get('private_key') or tls.get('private_key_path'))
assert not (tls.get('certificate_chain') or tls.get('certificate_chain_path'))
live={
 'schema_version':d.get('schema_version'),
 'http':{'address':http.get('address')},
 'dns':{
  'bind_hosts':list(dns.get('bind_hosts') or []),'port':dns.get('port'),
  'upstream_dns':list(dns.get('upstream_dns') or []),'upstream_dns_file':str(dns.get('upstream_dns_file') or ''),
  'bootstrap_dns':list(dns.get('bootstrap_dns') or []),'fallback_dns':list(dns.get('fallback_dns') or []),
  'private_upstream':list(dns.get('private_upstream') or []),'upstream_mode':dns.get('upstream_mode'),
  'ratelimit':dns.get('ratelimit'),'ratelimit_subnet_len_ipv4':dns.get('ratelimit_subnet_len_ipv4'),
  'ratelimit_subnet_len_ipv6':dns.get('ratelimit_subnet_len_ipv6'),'ratelimit_whitelist':list(dns.get('ratelimit_whitelist') or []),
  'refuse_any':bool(dns.get('refuse_any')),
  'edns_client_subnet':{'enabled':bool(edns.get('enabled')),'use_custom':bool(edns.get('use_custom')),'custom_ip_configured':bool(edns.get('custom_ip'))},
  'anonymize_client_ip':bool(dns.get('anonymize_client_ip')),'cache_size':dns.get('cache_size'),
  'cache_ttl_min':dns.get('cache_ttl_min'),'cache_ttl_max':dns.get('cache_ttl_max'),'cache_optimistic':bool(dns.get('cache_optimistic')),
 },
 'filtering':{
  'protection_enabled':bool(filtering.get('protection_enabled')),'filtering_enabled':bool(filtering.get('filtering_enabled')),
  'blocking_mode':filtering.get('blocking_mode'),'interval':filtering.get('interval'),
  'safebrowsing_enabled':bool(filtering.get('safebrowsing_enabled')),'parental_enabled':bool(filtering.get('parental_enabled')),
  'safesearch_enabled':bool(filtering.get('safesearch_enabled')),
 },
 'filters':[{'name':x.get('name'),'url':x.get('url'),'enabled':bool(x.get('enabled'))} for x in filters],
 'whitelist_filters':[],'user_rules':[],
 'querylog':{'enabled':bool(querylog.get('enabled')),'file_enabled':bool(querylog.get('file_enabled')),'interval':querylog.get('interval')},
 'statistics':{'enabled':bool(statistics.get('enabled')),'interval':statistics.get('interval')},
 'tls':{'enabled':bool(tls.get('enabled')),'server_name':tls.get('server_name'),'force_https':bool(tls.get('force_https')),
        'port_https':tls.get('port_https'),'port_dns_over_tls':tls.get('port_dns_over_tls'),'port_dns_over_quic':tls.get('port_dns_over_quic')},
 'dhcp':{'enabled':bool(dhcp.get('enabled'))},
}
assert live == approved, 'live safe settings differ from accepted artifact'
PY
mapfile -t qfiles < <(sudo find /opt/AdGuardHome -type f -name 'querylog.json*' -size +0c -print 2>/dev/null || true)
((${#qfiles[@]} == 0)) || fail 'non-empty query-log file exists'
pass 'privacy and approved-settings preflight passed'

sudo install -d -m 700 -o root -g root "$BACKUP_DIR"
STAGE="$(sudo mktemp -d "$BACKUP_DIR/.stage.XXXXXX")"
[[ "$(sudo stat -c '%a %U:%G' "$STAGE")" == '700 root:root' ]] || fail 'staging directory permissions unexpected'

created_utc="$(date -u +'%Y-%m-%dT%H:%M:%SZ')"
stamp="$(date -u +'%Y%m%dT%H%M%SZ')"
version="$(/opt/AdGuardHome/AdGuardHome --version | awk '{print $NF}')"
source_commit="$(git rev-parse HEAD)"
config_copy="$STAGE/AdGuardHome.yaml"
inner_archive="$STAGE/configuration.tar"
manifest="$STAGE/manifest.json"
package="$STAGE/backup-package.tar"
final="$BACKUP_DIR/usesafeweb-adguard-config-${stamp}.tar.age"
sidecar="$final.meta.json"

sudo cp --preserve=mode,ownership,timestamps "$CONFIG" "$config_copy"
[[ "$(sudo stat -c '%a %U:%G' "$config_copy")" == '600 root:root' ]] || fail 'staged config permissions unexpected'
config_sha="$(sudo sha256sum "$config_copy" | awk '{print $1}')"

# The inner configuration archive exists so its checksum can be embedded in the
# manifest without any circular self-hash problem.
sudo tar --format=posix --owner=0 --group=0 -C "$STAGE" -cf "$inner_archive" AdGuardHome.yaml
inner_sha="$(sudo sha256sum "$inner_archive" | awk '{print $1}')"

sudo python3 - "$manifest" "$created_utc" "$version" "$source_commit" "$config_sha" "$inner_sha" "$recipient_fingerprint" <<'PY'
import json,sys
path,created,version,commit,config_sha,inner_sha,recipient_fp=sys.argv[1:]
data={
 'backup_format':'usesafeweb.adguard-encrypted-config.v1',
 'created_utc':created,
 'source_host':'adguardvm',
 'service_identity':'srv.UseSafeWeb.com',
 'adguard_home_version':version,
 'source_git_commit':commit,
 'backup_scope_policy_blob':'e62b48a3e746b1be90881bbffab3b7680384cc16',
 'approved_config_artifact_blob':'ea85830b5ef9de7f2772e5467570d52013228b0b',
 'configuration_file_sha256':config_sha,
 'configuration_archive_sha256':inner_sha,
 'encryption':'age SSH-RSA recipient',
 'owner_recipient_fingerprint':recipient_fp,
 'included_files':['AdGuardHome.yaml'],
 'excluded_classes':['plaintext admin credential','query/DNS history','persistent client/statistics data','participant/research data','diagnostic logs','generated caches','stale rollback copies','TLS private material (not configured)'],
}
with open(path,'w',encoding='utf-8') as f:
 json.dump(data,f,sort_keys=True,indent=2); f.write('\n')
PY
sudo chown root:root "$manifest"
sudo chmod 600 "$manifest"

# Final plaintext package contains only the checksummed configuration archive
# and non-secret manifest; no plaintext admin.env or query-log file is copied.
sudo tar --format=posix --owner=0 --group=0 -C "$STAGE" -cf "$package" configuration.tar manifest.json
sudo chmod 600 "$package"

# Encrypt directly to the sole owner SSH public-key recipient. The matching
# private key is not present or created by this task.
sudo age -R "$AUTH_KEYS" -o "$final.tmp" "$package"
sudo chown root:root "$final.tmp"
sudo chmod 600 "$final.tmp"
sudo mv "$final.tmp" "$final"
final_sha="$(sudo sha256sum "$final" | awk '{print $1}')"
final_size="$(sudo stat -c '%s' "$final")"

sudo python3 - "$sidecar" "$created_utc" "$final" "$final_sha" "$final_size" "$recipient_fingerprint" "$source_commit" <<'PY'
import json,os,sys
path,created,archive,sha,size,recipient_fp,commit=sys.argv[1:]
data={
 'backup_format':'usesafeweb.adguard-encrypted-config.v1',
 'created_utc':created,
 'encrypted_archive':os.path.basename(archive),
 'encrypted_archive_sha256':sha,
 'encrypted_archive_size_bytes':int(size),
 'owner_recipient_fingerprint':recipient_fp,
 'source_git_commit':commit,
 'location_class':'root-only same-VM encrypted staging/recovery artifact; not proof of node-loss resilience',
}
with open(path,'w',encoding='utf-8') as f:
 json.dump(data,f,sort_keys=True,indent=2); f.write('\n')
PY
sudo chown root:root "$sidecar"
sudo chmod 600 "$sidecar"

# Verify ciphertext/metadata before retention rotation.
sudo test -s "$final"
[[ "$(sudo stat -c '%a %U:%G' "$final")" == '600 root:root' ]] || fail 'encrypted archive permissions unexpected'
[[ "$(sudo stat -c '%a %U:%G' "$sidecar")" == '600 root:root' ]] || fail 'metadata permissions unexpected'
sudo head -c 21 "$final" | grep -a -q '^age-encryption.org/v1' || fail 'age ciphertext header not found'
recorded_sha="$(sudo python3 - "$sidecar" <<'PY'
import json,sys
print(json.load(open(sys.argv[1],encoding='utf-8'))['encrypted_archive_sha256'])
PY
)"
[[ "$recorded_sha" == "$final_sha" ]] || fail 'recorded encrypted checksum mismatch'
pass 'encrypted archive and metadata verified'

# Minimal event-based retention: keep at most the two newest verified encrypted
# generations and their metadata. Rotation occurs only after this one verifies.
mapfile -t backups < <(sudo find "$BACKUP_DIR" -maxdepth 1 -type f -name 'usesafeweb-adguard-config-*.tar.age' -printf '%T@ %p\n' | sort -nr | awk '{print $2}')
if ((${#backups[@]} > 2)); then
  for old in "${backups[@]:2}"; do
    sudo rm -f -- "$old" "$old.meta.json"
  done
fi
mapfile -t retained < <(sudo find "$BACKUP_DIR" -maxdepth 1 -type f -name 'usesafeweb-adguard-config-*.tar.age' -print)
((${#retained[@]} <= 2)) || fail 'backup retention rotation failed'

# Remove all plaintext staging before reporting success; trap repeats safely.
sudo rm -rf "$STAGE"
STAGE=''
plaintext_stage_count="$(sudo find "$BACKUP_DIR" -maxdepth 1 -type d -name '.stage.*' -print | wc -l)"
[[ "$plaintext_stage_count" == '0' ]] || fail 'plaintext staging directory remains'

printf 'backup_created_utc=%s\n' "$created_utc"
printf 'encrypted_archive_name=%s\n' "$(basename "$final")"
printf 'encrypted_archive_sha256=%s\n' "$final_sha"
printf 'encrypted_archive_size_bytes=%s\n' "$final_size"
printf 'owner_recipient_fingerprint=%s\n' "$recipient_fingerprint"
printf 'retained_encrypted_generation_count=%s\n' "${#retained[@]}"
printf 'plaintext_stage_count=0\n'
printf 'TSK_0430_BACKUP_CREATE=PASS\n'
SUCCESS=1
