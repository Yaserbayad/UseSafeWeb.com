from datetime import datetime, timezone
from pathlib import Path
import subprocess

EXPECTED = {
    'CURRENT_STATE.md': 'cbbeee8c5435f34cbc0a16f520150a896775a5ab',
    'Plans/Master/WBS/master-wbs.csv': 'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
    'Plans/Master/Registers/DECISIONS_TRIGGERS.md': '380ff579dcffb7b8df73611e9159c672f9ed489e',
    'Plans/Master/Registers/GATES.md': '87cf9060954a82e1d5a092200d3c922f1986a5da',
    'TSK_0138_POST_CR0007_ACCEPTANCE_EVIDENCE_2026-08-31.md': 'fac88076539a51292caa2279d9bcd3076e96b75e',
    'TSK_0140_POST_CR0007_PRODUCT_BRIEF_2026-08-31.md': '8ed698b3e34540aefac617e5f6754e20d9dfbdc3',
    'TSK_0140_POST_CR0007_ACCEPTANCE_EVIDENCE_2026-08-31.md': 'a3388e6c5bed3e8908028ba0513bb8370f8dee62',
    'TSK_0140_POST_CR0007_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md': 'd2cc63426736ff9ae77bfe8fa32f812c1b55a5e2',
}
for path, sha in EXPECTED.items():
    actual = subprocess.check_output(['git', 'hash-object', path], text=True).strip()
    if actual != sha:
        raise SystemExit(f'prestate mismatch {path}: {actual} != {sha}')

p = Path('CURRENT_STATE.md')
s = p.read_text(encoding='utf-8')

old_bullet = '- **No task or gate became PASS solely because CR-0007 changed authority.** Re-evaluate any changed acceptance against current evidence. In particular, the post-CR-0006 `TSK-0140` candidate (`955ebc6a4592439c3d2edbedde3671fd910fac7c`) had preparation evidence but was previously waiting for a ceremonial owner review; CR-0007 removes that ceremonial requirement, yet `TSK-0140` remains non-PASS until its revised objective ACC is independently re-evaluated and durably evidenced.'
new_bullet = '- **No task or gate became PASS solely because CR-0007 changed authority.** Re-evaluate any changed acceptance against current evidence. `TSK-0140` has now been separately rebuilt, independently re-evaluated and durably evidenced PASS under its current objective ACC; that fresh PASS is recorded below and does not infer any successor or gate PASS.'
if s.count(old_bullet) != 1:
    raise SystemExit(f'TSK0140 CR0007 top-bullet count={s.count(old_bullet)}')
s = s.replace(old_bullet, new_bullet, 1)

old_heading = '### TSK-0140 accepted stable state\n'
historical_heading = '### Historical TSK-0140 accepted stable state — PRE-CR-0006/0007 — SUPERSEDED\n\n> Historical only. CR-0006 changed the Version-1 product scope and CR-0007 changed the objective action/gate authority and post-LG-09 lifecycle. Use the post-CR-0007 TSK-0140 current section below for runtime truth.\n\n'
if s.count(old_heading) != 1:
    raise SystemExit(f'historical TSK0140 heading count={s.count(old_heading)}')
s = s.replace(old_heading, historical_heading, 1)

marker = '## Frozen technical identity\n'
if s.count(marker) != 1:
    raise SystemExit(f'frozen technical identity marker count={s.count(marker)}')
current = '''## TSK-0140 current accepted stable state — 2026-08-31 — POST-CR-0007

`TSK-0140 — Issue the post-validation product brief`: **PASS** under current `ACC-0140 / VER-0140 / EVD-0140`, `DEC-0053/CR-0006` and `DEC-0054/CR-0007` authority.

- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, hard dependency `TSK-0138`, A4 / `AUTO_ALLOWED`; the WBS planning snapshot is not runtime proof.
- Hard dependency `TSK-0138` is current post-CR-0007 PASS under its independently re-accepted artifact/evidence.
- Current product brief: `TSK_0140_POST_CR0007_PRODUCT_BRIEF_2026-08-31.md`, version `3.0.0-post-cr0007`, blob `8ed698b3e34540aefac617e5f6754e20d9dfbdc3`, publication commit `0e6f7d5aa26238a227778c55883ebc3f606f4b42`.
- Analytical acceptance evidence: `TSK_0140_POST_CR0007_ACCEPTANCE_EVIDENCE_2026-08-31.md`, blob `a3388e6c5bed3e8908028ba0513bb8370f8dee62`, publication commit `dfc43bf086cbe07d873654ec1ad16b41d9d93a88`.
- Supplemental deterministic evidence: `TSK_0140_POST_CR0007_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md`, blob `d2cc63426736ff9ae77bfe8fa32f812c1b55a5e2`, publication commit `ee74dfb40813abfe2f9ac08e685bd2f1361ffd5a`.
- Successful independent verification run/job `33391565765 / 99486171756` on self-hosted `adguardvm`: WBS contract PASS; current TSK-0138 dependency PASS; CR-0006 dual-mode reconciliation PASS; CR-0007 authority/lifecycle reconciliation PASS; ACC semantics PASS; stale owner-review absence PASS; independent verification PASS; `git diff --check` and clean-status checks passed.
- Initial diagnostic run `33391353069 / 99485483541` failed only because its verifier omitted Markdown backticks in a runtime-fence substring assertion; it produced no product/evidence/runtime mutation and is not acceptance proof. A fresh corrected run, not the pinned rerun, supplied the successful evidence above.
- Current brief preserves the complete accountless core plus optional parent account/session/minimum ownership persistence/lightweight dashboard/device management; mandatory login, browsing/query/activity history, child accounts and unrestricted/raw DNS administration remain excluded.
- The accepted brief preserves accountless/persistent-state separation, AdGuard/encrypted-DNS technical truth, downstream security/privacy/provider obligations, free-core commercial limits, and the current LG-06 -> LG-07 -> LG-08 -> LG-09 -> bounded live-production lifecycle.
- No behavioral/user evidence is inferred before L8; no provider, architecture, implementation, release, legal/privacy/consent, payment, production, publication or launch completion is inferred.
- `LG-06` remains non-PASS until every current applicable L4 acceptance requirement is independently evidenced. Material frozen-scope changes and other retained human/nondelegable acts remain separately controlled.

### Queue status after post-CR-0007 TSK-0140 acceptance

TSK-0140 may now satisfy its outgoing hard-dependency edges, including `TSK-0312`. Recompute the L4 queue from current WBS/graph/runtime evidence, gate/constraint state and Action Authority before choosing the next task.

'''
s = s.replace(marker, current + marker, 1)

lines = s.splitlines()
if len(lines) < 3 or not lines[2].startswith('**Updated:** '):
    raise SystemExit('Updated header mismatch')
lines[2] = '**Updated:** ' + datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
s = '\n'.join(lines) + ('\n' if s.endswith('\n') else '')

required = [
    '## TSK-0140 current accepted stable state — 2026-08-31 — POST-CR-0007',
    '`TSK-0140 — Issue the post-validation product brief`: **PASS**',
    '33391565765 / 99486171756',
    'd2cc63426736ff9ae77bfe8fa32f812c1b55a5e2',
    '### Historical TSK-0140 accepted stable state — PRE-CR-0006/0007 — SUPERSEDED',
    'TSK-0140 has now been separately rebuilt, independently re-evaluated and durably evidenced PASS',
    'LG-06` remains non-PASS',
]
for token in required:
    if token not in s:
        raise SystemExit('post-transform token missing: ' + token)
if old_bullet in s or old_heading in s:
    raise SystemExit('stale TSK0140 current-state token remains')

p.write_text(s, encoding='utf-8')
print('TSK0140_POST_CR0007_RUNTIME_TRANSFORM=PASS')