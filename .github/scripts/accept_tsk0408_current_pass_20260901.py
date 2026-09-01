from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import re

runtime_path = Path('CURRENT_STATE.md')
evidence_path = Path('TSK_0408_CURRENT_ACCEPTANCE_EVIDENCE_2026-09-01.md')
marker = '## TSK-0408 current accepted stable state — 2026-09-01 — POST-CR-0007'

runtime = runtime_path.read_text(encoding='utf-8')
evidence = evidence_path.read_text(encoding='utf-8')

assert '**Disposition:** **PASS**' in evidence
assert 'ACC-0408 / VER-0408 / EVD-0408' in evidence
assert '33497169433' in evidence and '99821919358' in evidence
assert 'a6b41ff7462dab630aad9e7640950b0d3467f040' in evidence

if marker in runtime:
    print('TSK_0408_RUNTIME_ALREADY_ACCEPTED=1')
else:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    runtime = re.sub(r'^\*\*Updated:\*\* .*$', f'**Updated:** {now}', runtime, count=1, flags=re.M)
    section = f'''\n\n{marker}\n\n`TSK-0408 — Define one coherent UseSafeWeb DNS identity and approved platform-specific endpoint/profile mechanisms`: **PASS** under current `ACC-0408 / VER-0408 / EVD-0408`, `DEC-0053/CR-0006` and `DEC-0054/CR-0007`.\n\n- Action authority: **A3 / AUTO_ALLOWED**.\n- Current revalidation: `TSK_0408_POST_CR0007_REVALIDATION_EVIDENCE_2026-09-01.md`, blob `a6b41ff7462dab630aad9e7640950b0d3467f040`.\n- Independent verification: GitHub Actions run/job `33497169433 / 99821919358` — SUCCESS at verification head `3293a3fcae7e1258eab947bfb4218186b275d75a`.\n- Durable acceptance evidence: `TSK_0408_CURRENT_ACCEPTANCE_EVIDENCE_2026-09-01.md`, blob `0bbf1d934ecd4a7693baf7de56362391e46dcf55`.\n- Current accepted identity remains `UseSafeWeb DNS` / `dns.usesafeweb.com`; Android native Private DNS uses DoT hostname semantics and Apple DoH uses the HTTPS profile Server URL.\n- CR-0007 supersedes the historical mandatory pilot/staging/future-production environment model. Current separation is one production identity plus explicitly non-production local/dev/CI/ephemeral/preview/mock/synthetic/dry-run evidence; no non-production evidence is relabeled as production.\n- Verification/removal/fallback remain truthful and privacy-safe; no browsing/query history, invented FQDN/path/profile/account route, browser-visible `/control` proxy or administrator secret is introduced.\n- **Unlock:** `TSK-0413` may now consume TSK-0408 as its current direct hard-dependency evidence. No TSK-0413 or LG-07 PASS is inherited.\n\n### Queue status after TSK-0408 current PASS\n\nRecompute the L5 frontier from current WBS dependencies, gate/authority, runtime evidence and executor availability. `TSK-0413` remains non-PASS until its complete secret-safe versioned recovery-consumable bundle is constructed and independently verified.\n'''
    runtime = runtime.rstrip() + section
    runtime_path.write_text(runtime, encoding='utf-8')
    print('TSK_0408_RUNTIME_APPENDED=1')
