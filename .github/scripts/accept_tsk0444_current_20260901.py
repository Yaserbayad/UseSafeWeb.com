#!/usr/bin/env python3
from pathlib import Path
import csv
import os
import subprocess

ROOT = Path(__file__).resolve().parents[2]
WBS = ROOT / 'Plans/Master/WBS/master-wbs.csv'
STATE = ROOT / 'CURRENT_STATE.md'
ART = ROOT / 'TSK_0444_PRODUCTION_CI_EPHEMERAL_ENVIRONMENT_MODEL_2026-09-01.md'

SOURCE_COMMIT = os.environ.get('SOURCE_COMMIT', 'UNKNOWN')
RUN_ID = os.environ.get('GITHUB_RUN_ID', 'LOCAL')
RUN_ATTEMPT = os.environ.get('GITHUB_RUN_ATTEMPT', '1')


def git_hash(rel: str) -> str:
    return subprocess.check_output(['git', 'hash-object', rel], cwd=ROOT, text=True).strip()


with WBS.open(encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
row = next(r for r in rows if (r.get('Task_ID') or '').strip() == 'TSK-0444')

expected_fields = {
    'Lifecycle_Stage': 'L5',
    'Plan_Status': 'PLANNED',
    'Dependencies': 'TSK-0355; TSK-0411',
    'AI_Capability_A0_A4': 'A3',
    'Action_Authority': 'AUTO_ALLOWED',
    'Risk_Reference': 'RSK-0048',
    'Interface_Reference': 'INT-0014',
    'Requirement_Reference': 'REQ-0049; REQ-0050; CON-0004; CON-0005',
    'Acceptance_ID': 'ACC-0444',
    'Verification_ID': 'VER-0444',
    'Evidence_ID': 'EVD-0444',
}
for field, expected in expected_fields.items():
    actual = (row.get(field) or '').strip()
    assert actual == expected, f'{field}: {actual!r} != {expected!r}'

expected_acc = (
    'Architecture records pilot/production and CI/ephemeral preview/test environments with '
    'purpose/data/access/region/endpoint/deployment/cleanup/cost/rollback; persistent staging is absent '
    'unless evidence later justifies it; owner-provided VM boundary is explicit.'
)
assert (row.get('Acceptance_Criteria') or '').strip() == expected_acc

state = STATE.read_text(encoding='utf-8')
for heading in (
    '## TSK-0355 current accepted stable state — 2026-09-01',
    '## TSK-0411 current accepted stable state — 2026-09-01',
    '## TSK-0052 / LG-06 current accepted stable state',
    '## TSK-0446 current accepted stable state',
):
    assert heading in state, heading
heading = '## TSK-0444 current accepted stable state — 2026-09-01'
assert heading not in state, 'TSK-0444 current state already exists; reconcile rather than duplicate'

expected_hashes = {
    'Plans/Master/WBS/master-wbs.csv': 'b27a0c5df2f5636d8ed71051e9e26a68959a2616',
    'TSK_0355_MINIMUM_TYPESCRIPT_NEXTJS_APPLICATION_ARCHITECTURE_ADRS_2026-09-01.md': 'e9efc3b498040cc7e3cdd42a912359e41250d068',
    'TSK_0411_DNS_SERVICE_TOPOLOGY_CLIENT_CONFIGURATION_MODEL_2026-09-01.md': '8bd206e3832bafc5b8033dddd3e7913a5e01f7b6',
    'infrastructure/adguard-server/tsk-0413-bundle-v1/README.md': '5a162a87dd2761ff5a0da587fa660549309a1404',
    'infrastructure/adguard-server/tsk-0413-bundle-v1/AdGuardHome.public-fragment.yaml': '867ef7162c739106fa42af151cda145f6d16888e',
    'infrastructure/adguard-server/tsk-0413-bundle-v1/endpoints.json': 'fe1d1b2d5cff13f85eda96a28f90a40921ef4506',
    'TSK_0444_PRODUCTION_CI_EPHEMERAL_ENVIRONMENT_MODEL_2026-09-01.md': '75de2ff96ecbaf7bb098016822203fe08285695e',
}
for rel, expected in expected_hashes.items():
    actual = git_hash(rel)
    assert actual == expected, f'{rel}: {actual} != {expected}'

art = ART.read_text(encoding='utf-8')
required = (
    'one live production environment',
    'one dedicated AdGuard/DNS VM',
    'one separate web/application VM',
    'Do not maintain a persistent staging environment by default',
    'initial bounded/ramped live-production validation mode after LG-09 PASS',
    '| PROD-DNS |', '| PROD-WEB |', '| PROD-RAMP |', '| CI-SOURCE |', '| CI-TARGET |', '| EPH-APP |', '| EPH-DNS |', '| STAGE-COND |',
    'persistent query logging and file query logging remain OFF',
    'anonymized aggregate operational statistics with 24-hour retention',
    'client-IP anonymization remains ON',
    '`127.0.0.1:3000`',
    'public UDP/TCP 53 remains closed',
    'Azure **West Europe / Netherlands**',
    '`dns.usesafeweb.com`',
    '`https://dns.usesafeweb.com/dns-query`',
    'project automation starts only after the owner hands off the fresh Ubuntu 24.04 LTS VM',
    'approximately 30-minute recovery objective',
    'the web/application VM is owner-provided and separate from the DNS VM',
    'GitHub-hosted runner location is not treated as a controlled UseSafeWeb processing region or production evidence',
    'no production AdGuard admin credential',
    'source-only hosted runner cannot substitute for target observation',
    'synthetic accounts/devices/journey state only',
    'persistent staging is **ABSENT**',
    '12. teardown occurs when the evidence is captured or the risk-specific exit condition is met',
    'Azure control-plane provisioning/configuration is owner-managed',
    '## 11. INT-0014',
    '| DNS service name | Public | `UseSafeWeb DNS`.',
    '| DNS resolver hostname | Public | `dns.usesafeweb.com`.',
    '| DNS DoH URL | Public | `https://dns.usesafeweb.com/dns-query`.',
    '| AdGuard control origin/transport | Server only |',
    '| AdGuard admin credential | Secret/server only |',
    '| Optional Firebase client configuration | Intentionally public subset only |',
    '| Ownership datastore connection/credential | Secret/server only |',
    'A release may be promoted only when it deploys without an unapproved service/data flow and rollback is available',
    'only two standing production VMs',
    'CI/ephemeral environments have **zero standing infrastructure by default**',
    '`RSK-0048` remains **OPEN — critical control**',
    '| Pilot/production model |',
    '| Persistent staging absent |',
    '| Evidence-based staging trigger |',
    '| Owner-provided VM boundary |',
    '| INT-0014 |',
    '| TSK-0413 privacy baseline |',
    'No Azure control-plane provisioning, website/DNS deployment, LG-07/LG-08/LG-09, live-production activation, market launch, payment or real-user validation PASS is inferred',
    'Responsible reviewer: ChatGPT Project Governor',
)
missing = [item for item in required if item not in art]
assert not missing, 'environment model missing: ' + '; '.join(missing)
assert art.count('| SATISFIED') >= 17, 'ACC/authority trace incomplete'
for forbidden in ('-----BEGIN PRIVATE KEY-----', '-----BEGIN CERTIFICATE-----', 'password=', 'admin_password', 'private_key='):
    assert forbidden not in art, f'prohibited material marker: {forbidden}'

subprocess.run(['python3', 'Plans/Master/Tools/validate_master_plan.py'], cwd=ROOT, check=True)
print('TSK0444_CURRENT_CONTRACT_ENV_MODEL=PASS')
print(f'TSK0444_ARTIFACT_BLOB={expected_hashes["TSK_0444_PRODUCTION_CI_EPHEMERAL_ENVIRONMENT_MODEL_2026-09-01.md"]}')

section = f'''{heading}

`TSK-0444 — Record the production + CI/ephemeral environment model and conditional staging rule`: **PASS** under current `ACC-0444 / VER-0444 / EVD-0444`, current `TSK-0355` and `TSK-0411` dependency evidence, current `LG-06` PASS, and `DEC-0055/CR-0008` proportional-evidence authority.

- Action authority: **A3 / AUTO_ALLOWED**.
- Artifact: `TSK_0444_PRODUCTION_CI_EPHEMERAL_ENVIRONMENT_MODEL_2026-09-01.md`, version `1.0.0`, blob `{expected_hashes['TSK_0444_PRODUCTION_CI_EPHEMERAL_ENVIRONMENT_MODEL_2026-09-01.md']}`, acceptance source commit `{SOURCE_COMMIT}`.
- Verification: ChatGPT Project Governor cloud/runtime architecture review plus GitHub Actions run/attempt `{RUN_ID} / {RUN_ATTEMPT}`; exact WBS/ACC/VER/EVD, TSK-0355/TSK-0411/LG-06 current state, owner VM/recovery authority, frozen source blobs, full environment dimensions, INT-0014 bindings, master-plan validity and secret/history exclusions were checked before this mutation.
- Current lifecycle reconciliation: there is one live production environment. The inherited ACC word `pilot` is represented only as bounded/ramped `PROD-RAMP` live-production validation after LG-09 under DEC-0054; it does not create a pilot VM, second resolver identity, persistent staging environment or extra gate.
- Production boundary: two owner-provided Ubuntu 24.04 LTS hosts after manual Azure handoff—one lean West-Europe/Netherlands DNS node and one separate web/application VM. Azure control-plane provisioning/configuration remains owner-managed. Public production deployment is not inferred.
- CI/ephemeral boundary: source CI, target verification, disposable application preview and isolated DNS tests use synthetic/minimum data and no standing duplicate infrastructure by default; GitHub-hosted CI location is not production-region evidence and source-only CI cannot replace target observation when acceptance requires it.
- Conditional staging: persistent staging is absent. A staging-like environment requires a specific unprovable risk, bounded purpose/evidence/exit, synthetic/minimum data, separate non-production identity, TSK-0413 preservation, cost/authority review and deterministic teardown.
- TSK-0413 boundary: DNS production/test/recovery preserves exact Quad9 dns10, ECS off, persistent query/file logging off, client-IP anonymization on, 24-hour anonymized aggregate statistics only, loopback DNS/admin, no browser admin credentials and no browsing/query/activity history.
- `RSK-0048` remains OPEN/critical; architecture does not fabricate timed clean-server success. Rollback/recovery keeps unsafe partial service disabled/uncertain and retains the approximately 30-minute DNS recovery objective.
- **Non-inference:** no Azure control-plane provisioning, website/DNS deployment, LG-07/LG-08/LG-09, live-production activation, market launch, payment or real-user validation PASS is inferred.
'''
STATE.write_text(state.rstrip() + '\n\n' + section.strip() + '\n', encoding='utf-8')
print('TSK0444_STATE_CANDIDATE=PASS')
