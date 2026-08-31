from datetime import datetime, timezone
from pathlib import Path
import subprocess

EXPECTED = {
    'CURRENT_STATE.md': '447f62e2a047d9637c6d0ee1797f4537bf753591',
    'Plans/Master/WBS/master-wbs.csv': 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
    'Plans/Master/Registers/DECISIONS_TRIGGERS.md': '380ff579dcffb7b8df73611e9159c672f9ed489e',
    'Plans/Master/Registers/GATES.md': '87cf9060954a82e1d5a092200d3c922f1986a5da',
    'TSK_0138_POST_CR0007_UNRESOLVED_PRODUCT_ASSUMPTIONS_AND_OWNER_DECISIONS_2026-08-31.md': 'a0992efa33c3a54511957c2e34f02a1fc97ad10a',
    'TSK_0138_POST_CR0007_ACCEPTANCE_EVIDENCE_2026-08-31.md': 'fac88076539a51292caa2279d9bcd3076e96b75e',
}
for path, sha in EXPECTED.items():
    actual = subprocess.check_output(['git', 'hash-object', path], text=True).strip()
    if actual != sha:
        raise SystemExit(f'prestate mismatch {path}: {actual} != {sha}')

p = Path('CURRENT_STATE.md')
s = p.read_text(encoding='utf-8')
start = '## TSK-0138 current accepted stable state — 2026-08-30 — POST-CR-0006\n'
end = '## Frozen technical identity\n'
if s.count(start) != 1:
    raise SystemExit(f'TSK0138 current-section start count={s.count(start)}')
if s.count(end) != 1:
    raise SystemExit(f'frozen technical identity marker count={s.count(end)}')
a = s.index(start)
b = s.index(end, a)
current = '''## TSK-0138 current accepted stable state — 2026-08-31 — POST-CR-0007

`TSK-0138 — Register unresolved product assumptions and owner decisions`: **PASS** under current `ACC-0138 / VER-0138 / EVD-0138` and `DEC-0052/CR-0005 + DEC-0053/CR-0006 + DEC-0054/CR-0007` authority.

- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, hard dependency `TSK-0141`, A3 / `AUTO_ALLOWED`; WBS planning snapshot is not runtime proof.
- Dependency `TSK-0141` remains current post-CR-0006 PASS; CR-0007 did not alter its product-scope acceptance.
- Current register: `TSK_0138_POST_CR0007_UNRESOLVED_PRODUCT_ASSUMPTIONS_AND_OWNER_DECISIONS_2026-08-31.md`, version `2.0.0-post-cr0007`, blob `a0992efa33c3a54511957c2e34f02a1fc97ad10a`, publication commit `439c6519df2ce3e63cb99dff66dda11ed8fa3208`.
- Durable independent acceptance evidence: `TSK_0138_POST_CR0007_ACCEPTANCE_EVIDENCE_2026-08-31.md`, blob `fac88076539a51292caa2279d9bcd3076e96b75e`, publication commit `1e39f9c4c92f3cfa4b0d95788bb680e83579b20f`.
- Fresh post-publication verification passed every current ACC-0138 control field for all 17 unresolved items and found no unresolved contradiction against DEC-0052/0053/0054.
- CR-0007 corrections are current: LG-06 is evidence-driven/AUTO_ALLOWED inside frozen scope; LG-12 readiness and LG-13 UK public-production GO are automatic only when all current prerequisites pass; routine technical scaling is AUTO only inside approved architecture/budget; no mandatory separate pilot/staging lifecycle exists.
- Real-parent behavioral unknowns remain unresolved until L8 live-production evidence after LG-09; legal/privacy/consent/security/platform prerequisites and retained human/nondelegable boundaries remain controlling where actually applicable.
- Historical UPA-009/010/017 remain resolved/superseded; UPA-016 and UPA-018 now carry current CR-0007 authority rather than stale owner-only semantics.
- This PASS does not infer TSK-0140, LG-06, architecture/build/release gates, production activation, payment, publication or launch PASS.

### Queue status after post-CR-0007 TSK-0138 re-acceptance

TSK-0138 may satisfy its outgoing hard-dependency edges, including TSK-0140. Successor eligibility must still be recomputed against current WBS dependencies, runtime evidence, gates, constraints and Action Authority.

'''
s = s[:a] + current + s[b:]
lines = s.splitlines()
if len(lines) < 3 or not lines[2].startswith('**Updated:** '):
    raise SystemExit('Updated header mismatch')
lines[2] = '**Updated:** ' + datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
s = '\n'.join(lines) + ('\n' if s.endswith('\n') else '')
for token in [
    '## TSK-0138 current accepted stable state — 2026-08-31 — POST-CR-0007',
    'a0992efa33c3a54511957c2e34f02a1fc97ad10a',
    'fac88076539a51292caa2279d9bcd3076e96b75e',
    'LG-06 is evidence-driven/AUTO_ALLOWED',
    'This PASS does not infer TSK-0140',
]:
    if token not in s:
        raise SystemExit('post-transform token missing: ' + token)
if start in s:
    raise SystemExit('stale post-CR0006 TSK0138 current heading remains')
p.write_text(s, encoding='utf-8')
print('TSK0138_POST_CR0007_RUNTIME_TRANSFORM=PASS')