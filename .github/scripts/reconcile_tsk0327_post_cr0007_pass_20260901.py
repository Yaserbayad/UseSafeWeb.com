import subprocess
from pathlib import Path

RUNTIME=Path('CURRENT_STATE.md')
EXPECTED_RUNTIME='cef662d8f7ac79fd0d4e9bcfb8f9a8e6064a66a8'
EXPECTED={
'Plans/Master/WBS/master-wbs.csv':'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
'prototype/TSK-0327/POST_CR0007_FINDINGS_DISPOSITION.md':'1836484278e741a041dea172ddc63edf9053ef6a',
'TSK_0327_POST_CR0007_CURRENT_FINDINGS_ACCEPTANCE_EVIDENCE_2026-09-01.md':'1f6c1a006a96866d2dcfb6a317081d7379802087',
'.github/scripts/verify_tsk0327_post_cr0007_20260901.py':'52f25981c9c88894962b9b4dc2739c095aaebe38',
'.github/workflows/verify-tsk0327-post-cr0007-20260901.yml':'164d50e1cad4cf6bf4c6eea5e4b2393cc236e5dc',
}

def git_blob(path):
    return subprocess.check_output(['git','rev-parse',f'HEAD:{path}'],text=True).strip()

def req(c,m):
    if not c: raise SystemExit(m)

req(git_blob('CURRENT_STATE.md')==EXPECTED_RUNTIME,'TSK0327_RUNTIME_STALE')
for p,h in EXPECTED.items(): req(git_blob(p)==h,f'TSK0327_INPUT_STALE={p}')
text=RUNTIME.read_text(encoding='utf-8')
req('## TSK-0327 current accepted stable state — 2026-09-01 — POST-CR-0007' not in text,'TSK0327_ALREADY_CURRENT')
req('## TSK-0333 current accepted stable state — 2026-08-31 — POST-CR-0007' in text,'TSK0327_TSK0333_CURRENT_MISSING')
section='''

## TSK-0327 current accepted stable state — 2026-09-01 — POST-CR-0007

`TSK-0327 — Resolve critical usability, trust, and accessibility findings`: **PASS** under current `ACC-0327 / VER-0327 / EVD-0327`, `DEC-0053/CR-0006`, and `DEC-0054/CR-0007`.

- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, HIGH, hard dependency `TSK-0336`, A3 / `AUTO_ALLOWED`. `TSK-0336` remains `NOT_APPLICABLE + PASS` solely as the verified pre-product human-validation exclusion; no behavioral evidence is inferred.
- Historical 2026-08-29 findings PASS is retained only for unchanged accountless facts. CR-0006 expanded the current surface with optional account/session, saved-device/dashboard and lifecycle states, so the broad historical zero-findings conclusion was independently re-evaluated.
- Current findings disposition: `prototype/TSK-0327/POST_CR0007_FINDINGS_DISPOSITION.md`, version `2.0.0-post-cr0007`, blob `1836484278e741a041dea172ddc63edf9053ef6a`.
- Durable current evidence: `TSK_0327_POST_CR0007_CURRENT_FINDINGS_ACCEPTANCE_EVIDENCE_2026-09-01.md`, blob `1f6c1a006a96866d2dcfb6a317081d7379802087`.
- Deterministic verification run/job `33478481395 / 99762657735`: SUCCESS on self-hosted `adguardvm`; WBS/graph, current predecessor context, exact dual-mode TSK-0333 source/evidence blobs, current findings disposition, current browser retest evidence and PASS fences all passed.
- Current retest basis is the accepted TSK-0333 integrated browser campaign `33432762152 / 99621849637`, including accountless Android/iPhone, unsupported states, optional account creation, saved device, returning dashboard, device replacement, provider/session errors, logout/account deletion, record deletion, DNS removal/recovery, destructive-result uncertainty, keyboard, RTL/responsive, privacy/no-transport and no-console-error checks.
- One real current-scope defect discovered in that campaign—configured SafeWeb DNS removal not reachable from the Protection Map—was fixed and passed the materially different removal/recovery rerun. Two later failures were verifier-only and did not weaken product acceptance.
- No unresolved current critical/high finding remains in the applicable internal/automated L4 review. `TSK-0321` retains its separate HUMAN_ONLY accessibility-review boundary; this PASS does not self-certify it or claim human comprehension before L8.
- `RSK-0002` remains OPEN/non-blocking before L8. No implementation, architecture/security/privacy, participant, release, market, payment or launch PASS is inferred.

### Queue status after current TSK-0327 acceptance

Recompute successors from current WBS/graph/runtime. In particular, TSK-0322 must be evaluated against current CR-0006 dual-mode product scope rather than relying on its pre-CR-0006 language-policy PASS.
'''
RUNTIME.write_text(text.rstrip()+section.rstrip()+'\n',encoding='utf-8')
print('TSK0327_PASS_RUNTIME_PRECONDITIONS=PASS')
