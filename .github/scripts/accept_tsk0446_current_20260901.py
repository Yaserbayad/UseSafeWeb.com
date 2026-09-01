#!/usr/bin/env python3
from pathlib import Path
import subprocess
from datetime import datetime, timezone

ROOT = Path('.')
STATE = ROOT / 'CURRENT_STATE.md'
EVID = ROOT / 'TSK_0446_RECOVERY_SCOPE_CONTRACT_EVIDENCE_2026-09-01.md'
MARKER = ROOT / 'TSK_0446_RECOVERY_SCOPE_CONTRACT_AUTOVERIFY_2026-09-01.md'
CONTRACT = ROOT / 'infrastructure/adguard-server/TSK-0446-RECOVERY-SCOPE-CONTRACT.md'

state = STATE.read_text(encoding='utf-8')
marker = '## TSK-0446 current accepted stable state — 2026-09-01'
assert marker not in state, 'TSK-0446 already has current PASS state'
assert '## TSK-0413 current accepted stable state — 2026-09-01' in state
assert '## TSK-0052 / LG-06 — Product, Brand and Experience Freeze' in state

expected_hashes = {
    EVID: '714a5ccf4e7d0dc104ff55c1d87381571ab786f9',
    MARKER: 'f5fe287aac8a40054cc9175b95b85b8f9a63768d',
    CONTRACT: '18d998e2406e801c7ac08f4daa2e3b763ea9b523',
}
for path, expected in expected_hashes.items():
    actual = subprocess.check_output(['git', 'hash-object', str(path)], text=True).strip()
    assert actual == expected, f'{path} drift: {actual}'

ev = EVID.read_text(encoding='utf-8')
for text in [
    '**TSK-0446: PASS** at its defined L5 recovery-contract boundary.',
    'Final workflow run/job: `33504115232 / 99843993787` — **SUCCESS**.',
    'Marker commit/read-back: `e77d287488caba1d279a920e69d0e7a6d404c444` — PASS.',
    'actual clean-server timed restoration remains explicitly downstream evidence rather than an inferred result',
]:
    assert text in ev, text

mk = MARKER.read_text(encoding='utf-8')
for text in [
    'Source commit: `6214ac817ed3279561495f73212bd7e2e9acfc6b`',
    'GitHub Actions run: `33504115232`',
    'Result: **PASS**',
    'not target-environment restoration, production activation, or LG-07 PASS',
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
state += '''\n\n## TSK-0446 current accepted stable state — 2026-09-01\n\n`TSK-0446 — Freeze end-to-end recovery scope, supported clean-server assumptions, RTO target, required inputs, outputs, tests, and exclusions`: **PASS** at the current L5 recovery-contract boundary under `ACC-0446 / VER-0446 / EVD-0446`, current `TSK-0413` dependency evidence, owner-approved `DEC-0016`, and current `LG-06` PASS.\n\n- Action authority: **A3 / AUTO_ALLOWED**.\n- Contract: `infrastructure/adguard-server/TSK-0446-RECOVERY-SCOPE-CONTRACT.md`, version `1.0.0`, blob `18d998e2406e801c7ac08f4daa2e3b763ea9b523`.\n- Original contract commit: `18f90a9ef9a27ca2e3ce1917e1d2b35e8b91478c`.\n- Corrected verifier/source head: `6214ac817ed3279561495f73212bd7e2e9acfc6b`; verifier blob `42968bfe96ef9d8a7d7f86a4d6767a2df4f754a3`.\n- Independent verification: GitHub Actions run/job `33504115232 / 99843993787` — **SUCCESS**.\n- Automated verification marker: `TSK_0446_RECOVERY_SCOPE_CONTRACT_AUTOVERIFY_2026-09-01.md`, blob `f5fe287aac8a40054cc9175b95b85b8f9a63768d`, marker commit `e77d287488caba1d279a920e69d0e7a6d404c444`.\n- Durable EVD-0446: `TSK_0446_RECOVERY_SCOPE_CONTRACT_EVIDENCE_2026-09-01.md`, blob `714a5ccf4e7d0dc104ff55c1d87381571ab786f9`.\n- The contract incorporates the approved TSK-0413 privacy-first desired state: Quad9 dns10 only; ECS off; persistent query/file logging off; exceptional diagnostics not enabled by default and capped at 24h/delete if separately authorised; minimum anonymized aggregate operational statistics at 24h; client-IP anonymization on; initial official AdGuard DNS filter only; empty versioned allowlist; private authenticated administration; no browsing/query/activity history.\n- The older backup-policy `statistics=false` live preflight is historical and cannot override current `DEC-0016 / TSK-0413`; a protected raw backup is an input, not desired-state authority.\n- The approximately-30-minute RTO now has a frozen measurement boundary: the clock starts immediately before recovery execution after owner-handoff prerequisites and stops only after all applicable acceptance checks plus external encrypted-DNS health pass; elapsed UTC timing and deviations are mandatory downstream evidence.\n- **Non-inference:** no actual clean-server timed rebuild/restore, measured ~30-minute RTO attainment, Azure control-plane provisioning, production/public/user activation, `TSK-0445`, `TSK-0447`, `TSK-0518`, `LG-07`, or later task/gate PASS is claimed.\n\n### Queue effect after TSK-0446 current PASS\n\nRecompute the exact current frontier from WBS/graph/gates/runtime and current authorities. `TSK-0445` may consume this PASS only as a predecessor and remains HUMAN_ONLY unless newer owner authority changes that fact; other eligible autonomous work must be ranked independently rather than inferred from adjacency.\n'''
STATE.write_text(state.rstrip() + '\n', encoding='utf-8')
