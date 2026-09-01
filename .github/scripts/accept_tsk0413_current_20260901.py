#!/usr/bin/env python3
from pathlib import Path
import hashlib, subprocess
from datetime import datetime, timezone

ROOT=Path('.')
STATE=ROOT/'CURRENT_STATE.md'
EVID=ROOT/'TSK_0413_BUNDLE_VERIFICATION_EVIDENCE_2026-09-01.md'
BUNDLE=ROOT/'infrastructure/adguard-server/tsk-0413-bundle-v1/bundle.json'

state=STATE.read_text(encoding='utf-8')
marker='## TSK-0413 current accepted stable state — 2026-09-01'
assert marker not in state, 'TSK-0413 already has current PASS state'
assert '## TSK-0408 current accepted stable state — 2026-09-01' in state
assert '## TSK-0413 owner-approved privacy-first AdGuard baseline — 2026-09-01' in state
assert subprocess.check_output(['git','hash-object',str(EVID)],text=True).strip()=='632badd4a8f926cb314aaa8941f029ae4dfc7058'
assert subprocess.check_output(['git','hash-object',str(BUNDLE)],text=True).strip()=='f0735e6a508f16de7a9c4510cc2893b972c1786c'
assert hashlib.sha256(BUNDLE.read_bytes()).hexdigest()=='e51130d22ba22a940fe5be10e423537474bb7ccc6a2a6b3b25596bbe96081bb0'

ev=EVID.read_text(encoding='utf-8')
for text in ['Run/job: `33500597612 / 99832778403`','Result: **SUCCESS**','All current `ACC-0413` clauses are evidenced']:
    assert text in ev

now=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
lines=state.splitlines()
for i,line in enumerate(lines):
    if line.startswith('**Updated:**'):
        lines[i]=f'**Updated:** {now}'
        break
else:
    raise AssertionError('CURRENT_STATE Updated field missing')
state='\n'.join(lines).rstrip()
state += '''\n\n## TSK-0413 current accepted stable state — 2026-09-01\n\n`TSK-0413 — Create the secret-safe versioned AdGuard configuration, filter, allowlist, endpoint, and verification bundle consumed by recovery automation`: **PASS** under current `ACC-0413 / VER-0413 / EVD-0413`, the owner-approved privacy-first `DEC-0016` baseline, current `TSK-0408` dependency evidence and `DEC-0054/CR-0007`.\n\n- Action authority: **A4 / AUTO_ALLOWED**.\n- Bundle: `infrastructure/adguard-server/tsk-0413-bundle-v1/`, version `1.0.0`.\n- Verified candidate head: `8d329051ba900a92ae9d5897022bd2d090ad1c2d`.\n- `bundle.json` Git blob: `f0735e6a508f16de7a9c4510cc2893b972c1786c`; SHA-256 `e51130d22ba22a940fe5be10e423537474bb7ccc6a2a6b3b25596bbe96081bb0`.\n- Independent verification: GitHub Actions run/job `33500597612 / 99832778403` — **SUCCESS**.\n- Durable verification evidence: `TSK_0413_BUNDLE_VERIFICATION_EVIDENCE_2026-09-01.md`, blob `632badd4a8f926cb314aaa8941f029ae4dfc7058`.\n- Compatibility pin: AdGuard Home `v0.107.79`, configuration schema `34`, official tag commit `05ba17b282da1c4393d6a4ba4db0cf519194a362`.\n- Approved desired state encoded: Quad9 dns10 only; ECS off; persistent query/file logging off; exceptional diagnostics capped at 24h/delete; anonymized aggregate statistics at 24h; client-IP anonymization on; official AdGuard DNS filter only initially; empty versioned allowlist; private authenticated admin path; no browsing/query/activity history or versioned secrets.\n- The bundle is secret-safe desired state consumed by recovery automation; it is not a raw server backup. Administrator authentication material and TLS/proxy secrets remain external and must be injected by the governed recovery mechanism.\n- **Non-inference:** no live deployment of the newly approved statistics/filter state, rebuild/restore success, production activation, `TSK-0412`, `TSK-0446` or `LG-07` PASS is claimed.\n\n### Queue effect after TSK-0413 current PASS\n\nRecompute the exact L5 frontier from current WBS dependencies, relationship graph, gate/authority, runtime evidence, constraints/interfaces and executor availability. Direct successors may consume TSK-0413 only where their own current dependencies and acceptance are independently satisfied.\n'''
STATE.write_text(state.rstrip()+'\n',encoding='utf-8')
