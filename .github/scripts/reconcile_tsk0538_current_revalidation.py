from __future__ import annotations

import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

PRE_RUNTIME = 'db1f55f6d78e2408bab515fa6bcddd0c6cb5ac20'
EXPECTED = {
    'Plans/Master/WBS/master-wbs.csv': 'b27a0c5df2f5636d8ed71051e9e26a68959a2616',
    'Plans/Master/RELATIONSHIP_INDEX.yaml': 'c108d2c162bcea2ee4cc01def46d0487a9501032',
    'TSK_0538_POST_CR0008_DUAL_MODE_RELIABILITY_OBSERVABILITY_NFR_REVALIDATION_2026-09-02.md': '44c9c299465e821e2ffd84a54b77e3e615d61925',
    'TSK_0538_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md': '3ba04601ea5574fcd1fb1f58f95922ae94b74ac2',
    'TSK_0484_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md': 'a7461f68f99ccda5c947a4ee77453817db9db1e5',
}
NEW = '## TSK-0538 current accepted stable state — 2026-09-02 — POST-CR-0008 DUAL-MODE RELIABILITY NFR REVALIDATION'


def blob(path: str) -> str:
    return subprocess.check_output(['git', 'hash-object', path], text=True).strip()


for path, expected in EXPECTED.items():
    p = Path(path)
    if not p.exists():
        raise SystemExit('missing guarded input: ' + path)
    actual = blob(path)
    if actual != expected:
        raise SystemExit(f'hash mismatch {path}: {actual} != {expected}')

state_path = Path('CURRENT_STATE.md')
state = state_path.read_text(encoding='utf-8')
if NEW in state:
    section = state[state.index(NEW):]
    required = [
        '**PASS**',
        'TSK_0538_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md',
        '33579914315 / 100091795138',
        '`AUTO_ALLOWED`',
        '12 current critical journeys',
        '14 provisional internal SLI/SLOs',
    ]
    if all(token in section for token in required):
        print('TSK0538_CURRENT_STATE_ALREADY_APPLIED=PASS')
        raise SystemExit(0)
    raise SystemExit('ambiguous existing current TSK-0538 section')

if blob('CURRENT_STATE.md') != PRE_RUNTIME:
    raise SystemExit('pre-runtime blob mismatch; refuse stale write')
if not state.endswith('\n'):
    raise SystemExit('CURRENT_STATE.md must end with newline')

evidence = Path('TSK_0538_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md').read_text(encoding='utf-8')
for token in [
    'TSK-0538 current dual-mode reliability/observability/recovery/service-level NFR revalidation: PASS.',
    'ACC-0538 = PASS. VER-0538 = PASS. EVD-0538 = SATISFIED.',
    '33579914315 / 100091795138',
    'TSK0538_12_CRITICAL_JOURNEYS=PASS',
    'TSK0538_14_PROVISIONAL_SLI_SLO_CONTRACTS=PASS',
    'TSK0538_CURRENT_ACC=PASS',
]:
    if token not in evidence:
        raise SystemExit('missing evidence token: ' + token)

append = r'''## TSK-0538 current accepted stable state — 2026-09-02 — POST-CR-0008 DUAL-MODE RELIABILITY NFR REVALIDATION

`TSK-0538 — Define reliability, observability, recovery, and service-level NFRs`: **PASS** under current `ACC-0538 / VER-0538 / EVD-0538`, current direct predecessor TSK-0484, current dual-mode Version-1 scope and refreshed reliability/observability source review.

- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / MEDIUM / A3 / `AUTO_ALLOWED`; dependency exactly `TSK-0484`.
- Current artifact `TSK_0538_POST_CR0008_DUAL_MODE_RELIABILITY_OBSERVABILITY_NFR_REVALIDATION_2026-09-02.md`, version `2.0.0-post-CR0008`, blob `44c9c299465e821e2ffd84a54b77e3e615d61925`, publication commit `7559ded680625af640f6d7797bd296afc97a9b31`.
- Current durable evidence `TSK_0538_POST_CR0008_CURRENT_REVALIDATION_EVIDENCE_2026-09-02.md`, blob `3ba04601ea5574fcd1fb1f58f95922ae94b74ac2`, publication commit `56ec474ce63d85d1575ae75b7e0140e9d429eed3`.
- Independent structural verifier script blob `b71a66bfac3584d52cc7b3f16c5096962c1a3d2c`; read-only workflow blob `a92aed2c2ccef8b2d9f706995dfedc5d454254df`; run/job `33579914315 / 100091795138`: **SUCCESS**.
- Historical TSK-0538 evidence remains valid for the unchanged lean single-node DNS/accountless baseline, but its future web/app critical-journey model was accountless-only and did not cover the now-active optional session/dashboard/device/provider/datastore boundary.
- Current TSK-0484 makes authentication/session/ownership/provider/datastore/reconciliation/accountless-fallback failure boundaries active; TSK-0538 therefore required current revalidation rather than date-only preservation.
- Current acceptance defines 12 critical journeys, 13 bounded on-call questions, privacy-safe bounded metrics/logs/optional traces, and 14 provisional internal SLI/SLO rows. Account-only and accountless-core failure are measured separately.
- Historical DNS recovery objective `<=30 minutes` remains. Provisional accountless web/app RTO is `<=30 minutes` without inferring HA spend. Third-party provider recovery time is not fabricated; fail-closed account authority plus accountless fallback and fresh restoration evidence are required.
- Persistent account/device recovery permits zero security-authority regression: restore cannot cross ownership, resurrect deleted/revoked authority or present ambiguous mutation as success. Consequential unknown outcomes reconcile before replay.
- Backup/restore remains privacy-minimal and excludes DNS/query/domain/browsing history, J0/J1, raw product events, bearer/session material and ordinary provider/service-account secrets.
- PAGE/TICKET alerting remains symptom-centered and requires affected journey, symptom, first diagnostic check, owner and runbook. High-cardinality identity/token/ClientID/raw URL/DNS data remains prohibited from metric labels.
- OpenTelemetry is only a vendor-neutral instrumentation vocabulary if/when cross-component instrumentation is justified; no collector/backend/APM vendor, HA topology or paid monitoring deployment is selected or authorized here.
- TSK-0352 and TSK-0353 retain their own implementation/security ownership and are not inferred PASS.
- **Non-inference:** L4 reliability/observability/recovery/service-level NFR definition PASS only; no telemetry implementation, backend/collector, HA, auth/provider/datastore implementation, production SLO attainment, target-environment incident/recovery evidence, public SLA, later task/gate, participant, publication, payment, market activation or launch PASS is inferred.

### Queue status after current TSK-0538 revalidation

Recompute the executable frontier from canonical WBS/graph, current runtime evidence, artifact-specific change/reopen semantics, gates and Action Authority. Preserve valid non-uniform historical PASS records where current evidence still proves unchanged acceptance.
'''

stamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
base, count = re.subn(r'^\*\*Updated:\*\* .+$', '**Updated:** ' + stamp, state, count=1, flags=re.MULTILINE)
if count != 1:
    raise SystemExit('Updated header replacement failed')
result = base + '\n' + append
if not result.startswith(base):
    raise SystemExit('existing runtime prefix not preserved')
if result.count(NEW) != 1:
    raise SystemExit('new section count invalid')
state_path.write_text(result, encoding='utf-8')
check = state_path.read_text(encoding='utf-8')
if check != result or not check.startswith(base):
    raise SystemExit('runtime reread preservation failure')

for token in [
    '## TSK-0299 current accepted stable state',
    '## TSK-0485 current accepted stable state',
    '## TSK-0318 current accepted stable state',
    '## TSK-0319 current accepted stable state',
    '## TSK-0301 current accepted stable state',
    '## TSK-0316 current accepted stable state',
    '## TSK-0300 current accepted stable state',
    '## TSK-0317 current accepted stable state',
    '## TSK-0310 current accepted stable state',
    '## TSK-0484 current accepted stable state',
]:
    if token not in base:
        raise SystemExit('protected anchor missing: ' + token)

print('TSK0538_EXISTING_RUNTIME_PREFIX_PRESERVED=PASS')
print('TSK0538_PROTECTED_PASS_ANCHORS_PRESERVED=PASS')
print('TSK0538_CURRENT_STATE_RECONCILIATION=PASS')
