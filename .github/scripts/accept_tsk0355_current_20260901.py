#!/usr/bin/env python3
from pathlib import Path
import csv
import os
import subprocess

ROOT = Path(__file__).resolve().parents[2]
WBS = ROOT / 'Plans/Master/WBS/master-wbs.csv'
STATE = ROOT / 'CURRENT_STATE.md'
ART = ROOT / 'TSK_0355_MINIMUM_TYPESCRIPT_NEXTJS_APPLICATION_ARCHITECTURE_ADRS_2026-09-01.md'

SOURCE_COMMIT = os.environ.get('SOURCE_COMMIT', 'UNKNOWN')
RUN_ID = os.environ.get('GITHUB_RUN_ID', 'LOCAL')
RUN_ATTEMPT = os.environ.get('GITHUB_RUN_ATTEMPT', '1')


def git_hash(rel: str) -> str:
    return subprocess.check_output(['git', 'hash-object', rel], cwd=ROOT, text=True).strip()


with WBS.open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
row = next(r for r in rows if (r.get('Task_ID') or '').strip() == 'TSK-0355')

expected_fields = {
    'Lifecycle_Stage': 'L5',
    'Plan_Status': 'PLANNED',
    'Dependencies': 'TSK-0235',
    'AI_Capability_A0_A4': 'A3',
    'Action_Authority': 'AUTO_ALLOWED',
    'Risk_Reference': 'RSK-0045',
    'Interface_Reference': 'INT-0011; INT-0012',
    'Requirement_Reference': 'REQ-0036; REQ-0037; REQ-0039; CON-0010; CON-0011',
    'Acceptance_ID': 'ACC-0355',
    'Verification_ID': 'VER-0355',
    'Evidence_ID': 'EVD-0355',
}
for field, expected in expected_fields.items():
    actual = (row.get(field) or '').strip()
    assert actual == expected, f'{field}: {actual!r} != {expected!r}'

expected_acc = (
    'ADRs fix framework/deployment/runtime boundaries, anonymous ephemeral state, minimum persistent '
    'account/device ownership store required by Version 1, authentication/session pattern, server-only '
    'AdGuard adapter, observability, backups/deletion/recovery, and explicit non-goals. Persistent data is '
    'limited to the approved account/device purpose; no browsing/activity history is introduced.'
)
assert (row.get('Acceptance_Criteria') or '').strip() == expected_acc

state = STATE.read_text(encoding='utf-8')
assert '## TSK-0235 current accepted stable state — 2026-09-01' in state
assert '## TSK-0052 / LG-06 current accepted stable state' in state
heading = '## TSK-0355 current accepted stable state — 2026-09-01'
assert heading not in state, 'TSK-0355 current state already exists; reconcile rather than duplicate'

expected_hashes = {
    'Plans/Master/WBS/master-wbs.csv': 'b27a0c5df2f5636d8ed71051e9e26a68959a2616',
    'TSK_0354_VERSION_1_APPLICATION_ARCHITECTURE_2026-09-01.md': '4196c83e95a013c10b5c0a9a13005b97bbe08a59',
    'TSK_0235_SYSTEM_CONTEXT_CONTAINER_INTEGRATION_DIAGRAMS_2026-09-01.md': 'ecac82c1e020977a50af1d02345091415afba4ce',
    'infrastructure/adguard-server/tsk-0413-bundle-v1/README.md': '5a162a87dd2761ff5a0da587fa660549309a1404',
    'infrastructure/adguard-server/tsk-0413-bundle-v1/AdGuardHome.public-fragment.yaml': '867ef7162c739106fa42af151cda145f6d16888e',
    'TSK_0355_MINIMUM_TYPESCRIPT_NEXTJS_APPLICATION_ARCHITECTURE_ADRS_2026-09-01.md': 'e9efc3b498040cc7e3cdd42a912359e41250d068',
}
for rel, expected in expected_hashes.items():
    actual = git_hash(rel)
    assert actual == expected, f'{rel}: {actual} != {expected}'

assert not (ROOT / 'website/package.json').exists(), 'website/package.json now exists; re-evaluate version claims'

art = ART.read_text(encoding='utf-8')
required = (
    'one TypeScript + Next.js App Router full-stack application under `/website`',
    'Next.js **16.3.4 current-reference baseline**',
    "Node.js must be a maintained supported release satisfying Next.js's documented `>=20.9` minimum",
    "`output: 'standalone'`",
    'Reverse proxy terminates/controls the public HTTP boundary',
    'Server Components are the default',
    'State-changing integration endpoints are bounded Route Handlers',
    'J0 — browser/session-only accountless state',
    'J1 — optional anonymous transient server state',
    'A — optional persistent account/device domain',
    'server-managed application session',
    '`HttpOnly`, `Secure` server-managed session cookie',
    'server-side parent-to-device authorization',
    'typed, allowlisted adapter',
    'AdGuard Home `v0.107.79`, configuration schema `34`',
    'https://dns10.quad9.net/dns-query',
    'ECS disabled',
    'persistent query/file logging disabled',
    'client-IP anonymization enabled',
    '`127.0.0.1:3000`',
    'no generic browser-visible proxy to AdGuard `/control/*` endpoints',
    'Observability without surveillance',
    'Backup, deletion, and recovery boundaries',
    'Explicit non-goals',
    '`RSK-0045` remains **OPEN',
    'INT-0011', 'INT-0012', 'REQ-0036', 'REQ-0037', 'REQ-0039', 'CON-0010', 'CON-0011',
    'no browsing/activity history',
    'No implementation, build, deployment, LG-07/LG-08, production activation, launch, payment, or real-user validation PASS is inferred',
    'https://nextjs.org/docs/app/guides/self-hosting',
    'https://nextjs.org/docs/app/getting-started/installation',
    'https://nextjs.org/docs/app/guides/environment-variables',
    'https://nextjs.org/docs/app/getting-started/server-and-client-components',
    'https://nextjs.org/docs/app/getting-started/route-handlers',
    'https://nextjs.org/docs/app/api-reference/config/next-config-js/output',
    'https://firebase.google.com/docs/auth/admin/manage-cookies',
    'Responsible architecture review: ChatGPT Project Governor',
)
missing = [item for item in required if item not in art]
assert not missing, 'ADR missing: ' + '; '.join(missing)
assert art.count('| SATISFIED') >= 17, 'authority/acceptance trace incomplete'
for forbidden in ('-----BEGIN PRIVATE KEY-----', '-----BEGIN CERTIFICATE-----', 'password=', 'sessionCookie='):
    assert forbidden not in art, f'prohibited material marker: {forbidden}'

subprocess.run(['python3', 'Plans/Master/Tools/validate_master_plan.py'], cwd=ROOT, check=True)
print('TSK0355_CURRENT_CONTRACT_ADR=PASS')
print(f'TSK0355_ARTIFACT_BLOB={expected_hashes["TSK_0355_MINIMUM_TYPESCRIPT_NEXTJS_APPLICATION_ARCHITECTURE_ADRS_2026-09-01.md"]}')

section = f'''{heading}

`TSK-0355 — Validate and record the minimum owner-selected TypeScript + Next.js application architecture`: **PASS** under current `ACC-0355 / VER-0355 / EVD-0355`, current `TSK-0235` dependency evidence, current `LG-06` PASS, and `DEC-0055/CR-0008` proportional-evidence authority.

- Action authority: **A3 / AUTO_ALLOWED**.
- Artifact: `TSK_0355_MINIMUM_TYPESCRIPT_NEXTJS_APPLICATION_ARCHITECTURE_ADRS_2026-09-01.md`, version `1.0.0`, blob `{expected_hashes['TSK_0355_MINIMUM_TYPESCRIPT_NEXTJS_APPLICATION_ARCHITECTURE_ADRS_2026-09-01.md']}`, acceptance source commit `{SOURCE_COMMIT}`.
- Verification: ChatGPT Project Governor architecture review plus GitHub Actions run/attempt `{RUN_ID} / {RUN_ATTEMPT}`; exact WBS/ACC/VER/EVD, TSK-0235/LG-06 current state, frozen source blobs, official-source ADR clauses, master-plan validity, no-package version truth, and prohibited secret material were checked before this mutation.
- Framework/runtime boundary: one `/website` TypeScript + Next.js App Router application, current-reference Next.js 16.3.4 architecture, Node.js runtime with exact supported version pinned at implementation, self-hosted behind a reverse proxy, and a standalone direct-host release/rollback boundary. No installed dependency version is fabricated while `/website/package.json` is absent.
- Data/auth boundary: J0 browser state plus only optional anonymous bounded J1; separate server-only minimum parent/device persistent domain; optional Google/Firebase identity terminates in a server-validated secure session; core value remains usable without login.
- TSK-0413 boundary: server-only typed AdGuard adapter; AdGuard Home v0.107.79/schema 34; exact Quad9 dns10 DoH; ECS off; persistent query/file logging off; client-IP anonymization on; 24-hour anonymized aggregate statistics only; loopback-only authenticated administration; no browser admin credentials and no browsing/query/activity history.
- `RSK-0045` remains OPEN as a scope/privacy control. Datastore product/schema, final Firebase vendor/version/terms, CMS/component-library product, exact private cross-VM AdGuard control transport, secret-provider implementation and an actual L6 release remain downstream and are not invented.
- **Non-inference:** no website implementation/build, LG-07/LG-08, production deployment/activation, launch, payment, or real-user validation PASS is inferred.
'''
STATE.write_text(state.rstrip() + '\n\n' + section.strip() + '\n', encoding='utf-8')
print('TSK0355_STATE_CANDIDATE=PASS')
