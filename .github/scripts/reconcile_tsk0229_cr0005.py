#!/usr/bin/env python3
from datetime import datetime, timezone
from pathlib import Path
import re

p = Path('CURRENT_STATE.md')
text = p.read_text(encoding='utf-8')
marker = '### TSK-0229 accepted stable state'
if marker not in text:
    raise SystemExit('missing TSK-0229 runtime section')

segment_start = text.index(marker)
segment = text[segment_start:segment_start + 2400]
if 'TSK_0229_CURRENT_REVALIDATION_EVIDENCE_2026-08-29.md' in segment:
    print('TSK0229_RUNTIME_ALREADY_CURRENT=PASS')
    raise SystemExit(0)

new = '''### TSK-0229 accepted stable state — current under DEC-0052 / CR-0005

`TSK-0229 — Define and approve the accountless journey data model, expiry, deletion, and no-linkage rules`: **PASS** under current `ACC-0229 / VER-0229 / EVD-0229` and `DEC-0052 / CR-0005` sequencing.

The accepted `accountless-journey-data-v1` contract remains `TSK_0229_ACCOUNTLESS_JOURNEY_DATA_MODEL_EXPIRY_DELETION_NO_LINKAGE_2026-08-28.md`, blob `3fa48b11b6c7704ecc3748bcd865f77aa54f5605`. Current revalidation evidence is `TSK_0229_CURRENT_REVALIDATION_EVIDENCE_2026-08-29.md`, blob `7c6bd3b888196f2a487c7b7fe14d11e72bec424b`; successful verifier run `33269282897`, job `99144732470`, self-hosted `adguardvm`.

ACC-0229 remains satisfied: J0 session-only state is preferred; optional J1 is minimal/transient; persistent parent/child/device identity, browsing/DNS history, cross-session linkage and raw diagnostics are prohibited; the J1 hard TTL is non-sliding and no more than 24 hours; early deletion is synchronous where possible or no more than 15 minutes; diagnostic/logging/backup boundaries and fourteen implementation-testable invariants remain explicit. The 24-hour/15-minute values are conservative internal product defaults, not legal thresholds.

Current GDPR Article 5/25 and EDPB data-protection-by-design/default review found no contradiction with the minimisation/default-deletion direction. No final legal-compliance conclusion is inferred. `RSK-0002` remains nonblocking for this L4 PASS. Pre-product parent/user/participant validation is non-applicable under CR-0005 and is neither required nor claimed here.
'''
pattern = r'### TSK-0229 accepted stable state\n.*?(?=\n### TSK-0408 accepted stable state)'
text, n = re.subn(pattern, new.rstrip(), text, count=1, flags=re.S)
if n != 1:
    raise SystemExit(f'expected one TSK-0229 section replacement, got {n}')

now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
text, n = re.subn(r'(?m)^\*\*Updated:\*\* .*$', f'**Updated:** {now}', text, count=1)
if n != 1:
    raise SystemExit('expected one top-level Updated field')

p.write_text(text.rstrip() + '\n', encoding='utf-8')
print('TSK0229_RUNTIME_CR0005_EDIT=PASS')
