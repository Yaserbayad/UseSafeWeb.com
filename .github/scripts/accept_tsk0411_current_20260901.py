#!/usr/bin/env python3
from pathlib import Path
import csv
import os
import subprocess

ROOT = Path(__file__).resolve().parents[2]
WBS = ROOT / 'Plans/Master/WBS/master-wbs.csv'
STATE = ROOT / 'CURRENT_STATE.md'
ART = ROOT / 'TSK_0411_DNS_SERVICE_TOPOLOGY_CLIENT_CONFIGURATION_MODEL_2026-09-01.md'

SOURCE_COMMIT = os.environ.get('SOURCE_COMMIT', 'UNKNOWN')
RUN_ID = os.environ.get('GITHUB_RUN_ID', 'LOCAL')
RUN_ATTEMPT = os.environ.get('GITHUB_RUN_ATTEMPT', '1')


def git_hash(rel: str) -> str:
    return subprocess.check_output(['git', 'hash-object', rel], cwd=ROOT, text=True).strip()


with WBS.open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
row = next(r for r in rows if (r.get('Task_ID') or '').strip() == 'TSK-0411')

expected_fields = {
    'Lifecycle_Stage': 'L5',
    'Plan_Status': 'PLANNED',
    'Dependencies': 'TSK-0235',
    'AI_Capability_A0_A4': 'A3',
    'Action_Authority': 'AUTO_ALLOWED',
    'Risk_Reference': 'RSK-0004',
    'Interface_Reference': 'INT-0013',
    'Requirement_Reference': 'REQ-0042; REQ-0043; CON-0002; CON-0003',
    'Acceptance_ID': 'ACC-0411',
    'Verification_ID': 'VER-0411',
    'Evidence_ID': 'EVD-0411',
}
for field, expected in expected_fields.items():
    actual = (row.get(field) or '').strip()
    assert actual == expected, f'{field}: {actual!r} != {expected!r}'

expected_acc = (
    'Design meets DoH/privacy requirements, prevents open-resolver abuse as far as practical, defines '
    'verification/removal, covers Azure West Europe and later expansion triggers, and avoids unapproved US pilot traffic.'
)
assert (row.get('Acceptance_Criteria') or '').strip() == expected_acc

state = STATE.read_text(encoding='utf-8')
assert '## TSK-0235 current accepted stable state — 2026-09-01' in state
assert '## TSK-0052 / LG-06 current accepted stable state' in state
heading = '## TSK-0411 current accepted stable state — 2026-09-01'
assert heading not in state, 'TSK-0411 current state already exists; reconcile rather than duplicate'

expected_hashes = {
    'Plans/Master/WBS/master-wbs.csv': 'b27a0c5df2f5636d8ed71051e9e26a68959a2616',
    'TSK_0408_POST_CR0007_REVALIDATION_EVIDENCE_2026-09-01.md': 'a6b41ff7462dab630aad9e7640950b0d3467f040',
    'TSK_0235_SYSTEM_CONTEXT_CONTAINER_INTEGRATION_DIAGRAMS_2026-09-01.md': 'ecac82c1e020977a50af1d02345091415afba4ce',
    'infrastructure/adguard-server/tsk-0413-bundle-v1/README.md': '5a162a87dd2761ff5a0da587fa660549309a1404',
    'infrastructure/adguard-server/tsk-0413-bundle-v1/AdGuardHome.public-fragment.yaml': '867ef7162c739106fa42af151cda145f6d16888e',
    'infrastructure/adguard-server/tsk-0413-bundle-v1/endpoints.json': 'fe1d1b2d5cff13f85eda96a28f90a40921ef4506',
    'TSK_0411_DNS_SERVICE_TOPOLOGY_CLIENT_CONFIGURATION_MODEL_2026-09-01.md': '8bd206e3832bafc5b8033dddd3e7913a5e01f7b6',
}
for rel, expected in expected_hashes.items():
    actual = git_hash(rel)
    assert actual == expected, f'{rel}: {actual} != {expected}'

fragment = (ROOT / 'infrastructure/adguard-server/tsk-0413-bundle-v1/AdGuardHome.public-fragment.yaml').read_text(encoding='utf-8')
for required in (
    'address: 127.0.0.1:3000',
    '- 127.0.0.1',
    'port: 53',
    '- https://dns10.quad9.net/dns-query',
    'ratelimit: 20',
    'ratelimit_subnet_len_ipv4: 24',
    'ratelimit_subnet_len_ipv6: 56',
    'ratelimit_whitelist: []',
    'refuse_any: true',
    'enabled: false',
    'anonymize_client_ip: true',
    'file_enabled: false',
    'interval: 1d',
):
    assert required in fragment, required

art = ART.read_text(encoding='utf-8')
required_art = (
    '**UseSafeWeb DNS**',
    '`dns.usesafeweb.com`',
    '`https://dns.usesafeweb.com/dns-query`',
    'Azure West Europe / Netherlands',
    '`https://dns10.quad9.net/dns-query`',
    'ECS disabled',
    'persistent query logging off',
    'file query logging off',
    '24-hour retention',
    'client-IP anonymization on',
    '`127.0.0.1:53`',
    '`127.0.0.1:3000`',
    '| UDP 53 | **Not public**',
    '| TCP 53 | **Not public**',
    'DoH client IP is accepted only from the trusted same-host proxy boundary',
    'Do not claim HTTP `X-Forwarded-For`/trusted-proxy behavior applies to DoT',
    'DoT activation is **BLOCKED for that implementation**',
    '`ratelimit: 20`',
    '`refuse_any: true`',
    'No generic “paste this FQDN everywhere” workflow is authorized',
    'V1 — configuration identity',
    'V2 — service endpoint health',
    'V3 — upstream transport/configuration',
    'V4 — device-path technical verification',
    'endpoint reachability = **Reachable**, not Verified',
    'profile/hostname presence = **Configured**, not Verified',
    'parent confirmation = **Reported**, not Verified',
    'account/device ownership = **Owned/registered**, not Verified',
    'DNS/profile removal is distinct from account deletion',
    'No US DNS node is part of the initial path',
    'Expansion triggers',
    'INT-0013 — DNS capability to user experience contract',
    '`RSK-0004` remains **OPEN — unvalidated**',
    '| DoH requirements |',
    '| Prevent open-resolver abuse as far as practical |',
    '| Verification |',
    '| Removal |',
    '| Azure West Europe |',
    '| Avoid unapproved US initial traffic/node |',
    'https://github.com/AdguardTeam/AdGuardHome/wiki/Encryption',
    'https://github.com/AdguardTeam/AdGuardHome/wiki/Configuration',
    'https://docs.quad9.net/services/',
    'https://docs.quad9.net/FAQs/',
    'No implementation, live DNS activation, LG-07/LG-08, production deployment, market activation, launch, or real-user persistence PASS is inferred',
    'Responsible verifier/reviewer: ChatGPT Project Governor',
)
missing = [item for item in required_art if item not in art]
assert not missing, 'topology artifact missing: ' + '; '.join(missing)
assert art.count('| SATISFIED') >= 12, 'ACC/authority trace incomplete'
for forbidden in ('-----BEGIN PRIVATE KEY-----', '-----BEGIN CERTIFICATE-----', 'password=', 'admin_password'):
    assert forbidden not in art, f'prohibited material marker: {forbidden}'

subprocess.run(['python3', 'Plans/Master/Tools/validate_master_plan.py'], cwd=ROOT, check=True)
print('TSK0411_CURRENT_CONTRACT_TOPOLOGY=PASS')
print(f'TSK0411_ARTIFACT_BLOB={expected_hashes["TSK_0411_DNS_SERVICE_TOPOLOGY_CLIENT_CONFIGURATION_MODEL_2026-09-01.md"]}')

section = f'''{heading}

`TSK-0411 — Design DNS service topology and client configuration model`: **PASS** under current `ACC-0411 / VER-0411 / EVD-0411`, current `TSK-0235` dependency evidence, current `LG-06` PASS, `DEC-0016`, and `DEC-0055/CR-0008` proportional-evidence authority.

- Action authority: **A3 / AUTO_ALLOWED**.
- Artifact: `TSK_0411_DNS_SERVICE_TOPOLOGY_CLIENT_CONFIGURATION_MODEL_2026-09-01.md`, version `1.0.0`, blob `{expected_hashes['TSK_0411_DNS_SERVICE_TOPOLOGY_CLIENT_CONFIGURATION_MODEL_2026-09-01.md']}`, acceptance source commit `{SOURCE_COMMIT}`.
- Verification: ChatGPT Project Governor network-architecture review plus GitHub Actions run/attempt `{RUN_ID} / {RUN_ATTEMPT}`; exact WBS/ACC/VER/EVD, TSK-0235/LG-06 current state, frozen TSK-0408/TSK-0413 source blobs, topology/privacy/abuse/truth/removal/region clauses, master-plan validity and prohibited secret material were checked before this mutation.
- Topology boundary: one canonical `dns.usesafeweb.com` service; initial child-linked DNS remains on the owner-provided Azure West Europe/Netherlands DNS VM; public encrypted DNS is limited to DoH 443 and DoT 853 through the same-host edge; public UDP/TCP 53 and AdGuard admin 3000 remain closed; the web/application VM is outside the ordinary DNS data plane.
- TSK-0413 boundary: AdGuard Home v0.107.79/schema 34; exact Quad9 dns10 DoH upstream; ECS off; query/file logging off; client-IP anonymization on; 24-hour anonymized aggregate statistics only; official initial filter; empty allowlist; loopback DNS/admin; no browsing/query/activity history.
- Abuse disposition: the design retains `ratelimit=20`, /24 IPv4 and /56 IPv6 grouping, empty rate-limit whitelist and `refuse_any=true`, adds bounded encrypted-edge controls, and explicitly does not assume DoH forwarded-client-IP mechanics apply to DoT. DoT activation must fail closed until client-aware/equivalent edge controls and multi-client behavior are proven.
- Verification/removal truth: configuration presence, endpoint health, parent confirmation and ownership are separate from device-path technical verification; no technical `Verified` state is allowed without current deterministic device-path evidence. Removal is distinct from account/device-record/session lifecycle actions.
- `RSK-0004` remains OPEN/unvalidated; later live persistence evidence and expansion triggers can reopen the design. No US DNS node/market activation is inferred.
- **Non-inference:** no live DNS implementation/activation, LG-07/LG-08, production deployment, market activation, launch, or real-user persistence PASS is inferred.
'''
STATE.write_text(state.rstrip() + '\n\n' + section.strip() + '\n', encoding='utf-8')
print('TSK0411_STATE_CANDIDATE=PASS')
