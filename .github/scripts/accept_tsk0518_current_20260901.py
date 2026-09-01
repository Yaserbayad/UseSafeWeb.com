#!/usr/bin/env python3
from pathlib import Path
import subprocess
from datetime import datetime, timezone

ROOT = Path('.')
STATE = ROOT / 'CURRENT_STATE.md'
PLAN = ROOT / 'TSK_0518_INDEPENDENT_RECOVERY_ACCEPTANCE_PLAN_2026-09-01.md'
EVID = ROOT / 'TSK_0518_INDEPENDENT_RECOVERY_ACCEPTANCE_EVIDENCE_2026-09-01.md'
MARKER = ROOT / 'TSK_0518_INDEPENDENT_RECOVERY_ACCEPTANCE_AUTOVERIFY_2026-09-01.md'
VERIFIER = ROOT / '.github/scripts/verify_tsk0518_independent_recovery_acceptance_20260901.py'

state = STATE.read_text(encoding='utf-8')
marker = '## TSK-0518 current accepted stable state — 2026-09-01'
assert marker not in state, 'TSK-0518 already has current PASS state'
assert '## TSK-0052 / LG-06 current accepted stable state — 2026-09-01 — POST-CR-0007' in state
assert '## TSK-0446 current accepted stable state — 2026-09-01' in state

expected_hashes = {
    PLAN: '9915f59e356c0d06a0c54ce0c9d4bb63f7e0b553',
    EVID: '80387be3669c23ba6f7d7a0a128da9fe48cb972b',
    MARKER: 'c1c37dd4c080a91e917b313db0ec0c79793333dc',
    VERIFIER: 'bd900f345beffcb812d145e0f4379615b127c0f1',
}
for path, expected in expected_hashes.items():
    actual = subprocess.check_output(['git', 'hash-object', str(path)], text=True).strip()
    assert actual == expected, f'{path} drift: {actual}'

ev = EVID.read_text(encoding='utf-8')
for text in [
    '**TSK-0518: PASS** at the independent-acceptance-plan definition boundary.',
    'Final run/job: `33505275372 / 99847736387` — **SUCCESS**.',
    'Marker commit/read-back: `23893e7b998e334d4d3db63ecaee951d28a15d5d`',
    'all 20 current recovery requirements are mapped to independent evidence classes and severity/blocking rules',
    'no target execution outcome is inferred',
]:
    assert text in ev, text

mk = MARKER.read_text(encoding='utf-8')
for text in [
    'Source commit: `930d719b928030ea2902e56652554499fb1e4a4e`',
    'GitHub Actions run: `33505275372`',
    'Result: **PASS**',
    'maps exactly RA-01 through RA-20',
    'does not prove a clean-server recovery, target RTO, production deployment, downstream task PASS, or LG-07 PASS',
]:
    assert text in mk, text

now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
lines = state.splitlines()
for i, line in enumerate(lines):
    if line.startswith('**Updated:**'):
        lines[i] = f'**Updated:** {now}'
        break
else:
    raise AssertionError('CURRENT_STATE Updated field missing')
state = '\n'.join(lines).rstrip()
state += '''\n\n## TSK-0518 current accepted stable state — 2026-09-01\n\n`TSK-0518 — Define an independent acceptance plan for the AdGuard deployment/recovery script`: **PASS** at the current L5 independent-acceptance-plan definition boundary under `ACC-0518 / VER-0518 / EVD-0518`, current `TSK-0446` dependency evidence, owner-approved `DEC-0016 / TSK-0413`, and current `LG-06` PASS.\n\n- Action authority: **A3 / AUTO_ALLOWED**.\n- Acceptance plan: `TSK_0518_INDEPENDENT_RECOVERY_ACCEPTANCE_PLAN_2026-09-01.md`, version `1.0.0`, blob `9915f59e356c0d06a0c54ce0c9d4bb63f7e0b553`.\n- Original plan/source commit: `6e72ae53b36acddda4e1b3b548bc8db8eefcedf2`.\n- Corrected verifier/source head: `930d719b928030ea2902e56652554499fb1e4a4e`; verifier blob `bd900f345beffcb812d145e0f4379615b127c0f1`.\n- Independent verification: GitHub Actions run/job `33505275372 / 99847736387` — **SUCCESS**.\n- Automated verification marker: `TSK_0518_INDEPENDENT_RECOVERY_ACCEPTANCE_AUTOVERIFY_2026-09-01.md`, blob `c1c37dd4c080a91e917b313db0ec0c79793333dc`, marker commit `23893e7b998e334d4d3db63ecaee951d28a15d5d`.\n- Durable EVD-0518: `TSK_0518_INDEPENDENT_RECOVERY_ACCEPTANCE_EVIDENCE_2026-09-01.md`, blob `80387be3669c23ba6f7d7a0a128da9fe48cb972b`.\n- The plan separates the Cloud/Platform producer from QA acceptance, treats producer/local/artifact-only evidence as supporting only, requires direct independent target evidence where behavior is target-dependent, and forbids hidden inference as evidence.\n- Exactly `RA-01` through `RA-20` map the current recovery surface to independent evidence classes and default severity/blocking rules. Missing/wrong-target/producer-only evidence is `EB`; `S1` and `S2` findings block recovery acceptance.\n- The plan preserves current TSK-0413 privacy authority: persistent query/file logging off; identifiable per-client statistics/history excluded; client-IP anonymization on; ECS off; Quad9 dns10 only; minimum anonymized aggregate operational statistics at 24h/`1d`. Older blanket “statistics off” wording cannot override the current baseline.\n- The approximately-30-minute recovery target requires later direct timed target evidence using the TSK-0446 clock boundary; no tolerance or target PASS is inferred here.\n- **Non-inference:** no recovery implementation, clean-server restore, measured RTO, backup/restore, rollback, idempotency/failure-injection, live DNS/TLS, production/public/user activation, downstream task, `LG-07`, or later gate PASS is claimed.\n\n### Queue effect after TSK-0518 current PASS\n\nRecompute the exact current frontier from WBS/graph/gates/runtime and current authorities. `TSK-0445` is dependency-satisfied but remains **A1 / HUMAN_ONLY**; do not perform or self-certify it. Continue any higher-valid autonomous L5 work whose current dependencies, gates and authority are independently satisfied; otherwise stop at the exact human boundary.\n'''
STATE.write_text(state.rstrip() + '\n', encoding='utf-8')
