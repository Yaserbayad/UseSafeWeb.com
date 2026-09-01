import subprocess
from pathlib import Path

RUNTIME=Path('CURRENT_STATE.md')
EXPECTED_RUNTIME='ddbc60b780905094cf3714bf63d595b02ef8e7f2'
EXPECTED={
'Plans/Master/WBS/master-wbs.csv':'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
'prototype/TSK-0327/POST_CR0007_FINDINGS_DISPOSITION.md':'00abb274c7397e6fa8ffff3d6e1d407cc5cb9cc3',
'TSK_0327_POST_SAFEWEB_REVALIDATION_EVIDENCE_2026-09-01.md':'ee9a43d63a26e7c852c5b25f4ea21a77841014f3',
'.github/scripts/verify_tsk0327_after_safeweb_20260901.py':'95f87920e76c72e4988173aa976cbb1e6283c8fb',
'.github/workflows/verify-tsk0327-after-safeweb-20260901.yml':'fbbc30d98892dfad5e5315f7527c9626325e3c7a',
'prototype/TSK-0333/index.html':'934dc19d00cc9dd32e1ebc20c604373d153d4013',
'prototype/TSK-0333/model.mjs':'fc25e4b1facc303840311e8ce186612eb8799212',
'prototype/TSK-0333/app.mjs':'98659ba74a86d539b89664708bbcb830292486f8',
'TSK_0333_SAFEWEB_BRAND_REVALIDATION_EVIDENCE_2026-09-01.md':'f3ea3bf41c38050356a6e9e94aa251b07b35c5f3',
}

def blob(p): return subprocess.check_output(['git','rev-parse',f'HEAD:{p}'],text=True).strip()
def req(c,m):
    if not c: raise SystemExit(m)

req(blob('CURRENT_STATE.md')==EXPECTED_RUNTIME,'TSK0327_SAFEWEB_RUNTIME_STALE')
for p,h in EXPECTED.items(): req(blob(p)==h,f'TSK0327_SAFEWEB_INPUT_STALE={p}')
text=RUNTIME.read_text(encoding='utf-8')
heading='## TSK-0327 current accepted stable state — 2026-09-01 — POST-CR-0007'
start=text.find(heading); req(start>=0,'TSK0327_CURRENT_SECTION_MISSING')
end=text.find('\n## ',start+len(heading));
if end < 0: end=len(text)
new='''## TSK-0327 current accepted stable state — 2026-09-01 — POST-CR-0007

`TSK-0327 — Resolve critical usability, trust, and accessibility findings`: **PASS** under current `ACC-0327 / VER-0327 / EVD-0327`, `DEC-0053/CR-0006`, and `DEC-0054/CR-0007`.

- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, HIGH, hard dependency `TSK-0336`, A3 / `AUTO_ALLOWED`. `TSK-0336` remains `NOT_APPLICABLE + PASS` only as the verified pre-product human-validation exclusion; no behavioral evidence is inferred.
- Current findings disposition: `prototype/TSK-0327/POST_CR0007_FINDINGS_DISPOSITION.md`, version `2.1.0-post-cr0007`, blob `00abb274c7397e6fa8ffff3d6e1d407cc5cb9cc3`.
- Current TSK-0333 predecessor is the corrected SafeWeb-identity PASS at runtime commit `9fd087c7510999e4fafcca29c4a2de862386f768`, with source blobs index `934dc19d00cc9dd32e1ebc20c604373d153d4013`, model `fc25e4b1facc303840311e8ce186612eb8799212`, app `98659ba74a86d539b89664708bbcb830292486f8`, CSS `6f8af459a0b0b1c9ec132657dfcd7ebff43090b8`.
- Durable post-brand revalidation evidence: `TSK_0327_POST_SAFEWEB_REVALIDATION_EVIDENCE_2026-09-01.md`, blob `ee9a43d63a26e7c852c5b25f4ea21a77841014f3`.
- Deterministic post-brand run/job `33479274751 / 99765034038`: SUCCESS on self-hosted `adguardvm`; current blobs, WBS contract, corrected predecessor context, v2.1 findings disposition and SafeWeb retest evidence all PASS.
- Two real current-scope product defects were found and are closed with materially different evidence: (1) configured SafeWeb DNS removal was not reachable from the Protection Map; (2) visible brand rendered as `UseSafeWeb` despite owner-approved `SafeWeb` identity. The full integrated browser suite passed after each final correction. Two other failures were verifier-only diagnostics.
- No unresolved current critical/high functional, trust/evidence-state, accessibility/responsive, recovery/lifecycle, privacy-boundary or identity-conformance finding remains in the applicable internal/automated L4 review.
- `TSK-0321` retains its separate HUMAN_ONLY accessibility-review boundary; this PASS does not self-certify that task or claim human comprehension before L8.
- `RSK-0002` remains OPEN/non-blocking before L8. No downstream architecture, implementation, participant, gate, release, market, payment or launch PASS is inferred.

### Queue status after refreshed TSK-0327 acceptance

Recompute TSK-0322 from current product/identity authority. Its historical pre-CR-0006 content policy is not sufficient where it still excludes an account/dashboard product that is now in approved Version-1 scope.
'''
text=text[:start]+new.rstrip()+text[end:]
RUNTIME.write_text(text.rstrip()+'\n',encoding='utf-8')
print('TSK0327_SAFEWEB_PASS_RUNTIME_PRECONDITIONS=PASS')
