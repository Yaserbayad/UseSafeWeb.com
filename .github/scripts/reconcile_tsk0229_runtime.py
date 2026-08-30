from datetime import datetime, timezone
from pathlib import Path
import subprocess

EXPECTED = {
    'CURRENT_STATE.md': '515638ae5efaa8dfec4e9a8362f28f7efb45cd6e',
    'Plans/Master/WBS/master-wbs.csv': '3bb1598a6233a2bbefa52c746a7621867c6c6e89',
    'TSK_0229_ACCOUNTLESS_JOURNEY_DATA_MODEL_EXPIRY_DELETION_NO_LINKAGE_2026-08-28.md': '3fa48b11b6c7704ecc3748bcd865f77aa54f5605',
    'TSK_0229_POST_CR0006_ACCOUNTLESS_NO_LINKAGE_AMENDMENT_2026-08-30.md': '2955c2762e726f95ec67c33b9abbc5e4b25cb84a',
    'TSK_0229_POST_CR0006_REVALIDATION_EVIDENCE_2026-08-30.md': '37fd97419bb0a5c9c072691dec7bf24cc511aba8',
}
for path, sha in EXPECTED.items():
    actual = subprocess.check_output(['git', 'hash-object', path], text=True).strip()
    if actual != sha:
        raise SystemExit(f'prestate mismatch {path}: {actual} != {sha}')

p = Path('CURRENT_STATE.md')
s = p.read_text(encoding='utf-8')

old = "- Prior PASS/evidence remains valid only for unchanged facts. `TSK-0146` is current **PASS** under the revised DEC-0053/CR-0006 dual-mode Version-1 contract and evidence recorded below; revised account-inclusive `TSK-0313`, `TSK-0315`, `TSK-0328`, `TSK-0333`, `TSK-0321`, `TSK-0309`, and `TSK-0628` remain non-PASS until their current acceptance contracts are satisfied. Activated HUMAN_ONLY account UX decisions (`TSK-0329`, `TSK-0332`, `TSK-0331`) remain human-authority work when dependency-eligible."
new = "- Prior PASS/evidence remains valid only for unchanged facts. `TSK-0146` and `TSK-0229` are current **PASS** under the revised DEC-0053/CR-0006 dual-mode Version-1 contract and evidence recorded below; revised account-inclusive `TSK-0313`, `TSK-0315`, `TSK-0328`, `TSK-0333`, `TSK-0321`, `TSK-0309`, and `TSK-0628` remain non-PASS until their current acceptance contracts are satisfied. Activated HUMAN_ONLY account UX decisions (`TSK-0329`, `TSK-0332`, `TSK-0331`) remain human-authority work when dependency-eligible."
if s.count(old) != 1:
    raise SystemExit('top CR0006 state bullet mismatch')
s = s.replace(old, new, 1)

old = "- After this TSK-0146 PASS is persisted/read back, exact next work must be recomputed from current WBS dependencies, gates, Action Authority and runtime evidence; do not infer the successor from task numbering or the old LG-06 readiness package."
new = "- `TSK-0146` and post-CR-0006 `TSK-0229` are now the current accepted product/privacy baselines recorded below. Exact next work must be recomputed from current WBS dependencies, gates, Action Authority and runtime evidence; do not infer the successor from task numbering or the old LG-06 readiness package."
if s.count(old) != 1:
    raise SystemExit('CR0006 queue boundary mismatch')
s = s.replace(old, new, 1)

old = "### TSK-0229 accepted stable state — current under DEC-0052 / CR-0005\n\n`TSK-0229 — Define and approve the accountless journey data model, expiry, deletion, and no-linkage rules`: **PASS** under current `ACC-0229 / VER-0229 / EVD-0229` and `DEC-0052 / CR-0005` sequencing."
new = "### Historical TSK-0229 accepted stable state — DEC-0052 / CR-0005 — SUPERSEDED BY CR-0006 REVALIDATION\n\n> Historical only. DEC-0053/CR-0006 activated the optional Version-1 account and triggered the base contract's material-change rule. The word `current` in this historical section refers to its 2026-08-29 context; use the post-CR-0006 TSK-0229 section below for current runtime state.\n\n`TSK-0229 — Define and approve the accountless journey data model, expiry, deletion, and no-linkage rules`: **PASS** under the then-current `ACC-0229 / VER-0229 / EVD-0229` and `DEC-0052 / CR-0005` sequencing."
if s.count(old) != 1:
    raise SystemExit('historical TSK0229 heading mismatch')
s = s.replace(old, new, 1)

marker = '## Frozen technical identity\n'
if s.count(marker) != 1:
    raise SystemExit('frozen technical identity marker mismatch')
current = '''## TSK-0229 current accepted stable state — 2026-08-30 — POST-CR-0006

`TSK-0229 — Define and approve the accountless journey data model, expiry, deletion, and no-linkage rules`: **PASS** under current `ACC-0229 / VER-0229 / EVD-0229` and `DEC-0053 / CR-0006` authority.

- Current WBS blob `3bb1598a6233a2bbefa52c746a7621867c6c6e89`: L4, HIGH, dependency `TSK-0146`, A3 / `AUTO_ALLOWED`; WBS planning snapshot was `WAITING` before this execution and is not runtime proof.
- Dependency `TSK-0146` is current PASS under the post-CR-0006 Version-1 baseline.
- Base accountless contract remains `TSK_0229_ACCOUNTLESS_JOURNEY_DATA_MODEL_EXPIRY_DELETION_NO_LINKAGE_2026-08-28.md`, `accountless-journey-data-v1`, blob `3fa48b11b6c7704ecc3748bcd865f77aa54f5605`.
- Post-CR-0006 separation amendment: `TSK_0229_POST_CR0006_ACCOUNTLESS_NO_LINKAGE_AMENDMENT_2026-08-30.md`, version `1.0.0`, blob `2955c2762e726f95ec67c33b9abbc5e4b25cb84a`, publication commit `a75d88622a818a64761d4292110dcc229cd5d4af`.
- Durable current evidence: `TSK_0229_POST_CR0006_REVALIDATION_EVIDENCE_2026-08-30.md`, blob `37fd97419bb0a5c9c072691dec7bf24cc511aba8`.
- Corrected deterministic verification run/job `33307917535 / 99247643413`: SUCCESS on self-hosted `adguardvm`; eligibility, base contract, CR-0006 separation, ACC-0229, privacy boundaries and downstream scope fence all PASS.
- Earlier run/job `33307832517 / 99247423588` is retained as diagnostic evidence only: it failed because the verifier expected `Anonymous journey state` instead of the actual TSK-0146 phrase `Accountless journey state`; no authority/artifact/runtime change resulted. The corrected assertion passed.
- Current data rule: J0/J1 remain anonymous, short-lived and separate from the optional persistent parent-account domain. No automatic J1-to-account join/conversion/promotion is authorized; any future explicit transfer requires a separately approved downstream dual-mode data-flow contract.
- The base J1 allowlist, non-sliding maximum 24-hour TTL, early deletion, no browsing/query/activity history, no persistent child/family profile, diagnostic separation, token/logging restrictions and backup exclusion remain in force. The TTL/cleanup bounds are internal product defaults, not legal thresholds.
- Account sign-in/activity cannot extend J1 expiry. Account/device deletion, anonymous-state deletion and DNS configuration removal remain distinct operations whose completion must be represented truthfully.
- TSK-0229 does not define or approve the persistent account schema, provider identifiers, storage, retention, backup, access or account/device ownership enforcement. Those remain downstream authoritative work.
- Current official EUR-Lex/EDPB review found no contradiction to the minimisation/storage-limitation/privacy-by-default direction; no final legal-compliance conclusion is inferred.
- `RSK-0001` remains OPEN for later England participant legal/data readiness; `RSK-0002` remains OPEN/non-blocking before L8 under DEC-0052/CR-0005. No human/user validation, LG-06, architecture, implementation, participant, release or launch PASS is inferred.

### Queue status after post-CR-0006 TSK-0229 acceptance

TSK-0229 may now satisfy its hard-dependency edges, including the TSK-0315 dependency, but every successor must be independently recomputed against its other WBS hard dependencies, current runtime state, gates, inputs and Action Authority.

'''
s = s.replace(marker, current + marker, 1)

lines = s.splitlines()
if len(lines) < 3 or not lines[2].startswith('**Updated:** '):
    raise SystemExit('Updated header mismatch')
lines[2] = '**Updated:** ' + datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
s = '\n'.join(lines) + ('\n' if s.endswith('\n') else '')
p.write_text(s, encoding='utf-8')

for token in [
    '`TSK-0146` and `TSK-0229` are current **PASS**',
    '## TSK-0229 current accepted stable state — 2026-08-30 — POST-CR-0006',
    '### Historical TSK-0229 accepted stable state — DEC-0052 / CR-0005 — SUPERSEDED BY CR-0006 REVALIDATION',
    '37fd97419bb0a5c9c072691dec7bf24cc511aba8',
    '33307917535 / 99247643413',
]:
    if token not in s:
        raise SystemExit('post-transform token missing: ' + token)
print('TSK0229_RUNTIME_TRANSFORM=PASS')
