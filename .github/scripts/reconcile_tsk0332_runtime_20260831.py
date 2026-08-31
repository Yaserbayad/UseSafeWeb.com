from pathlib import Path
import subprocess
from datetime import datetime, timezone

ROOT=Path('.')
RUNTIME=ROOT/'CURRENT_STATE.md'
EXPECTED={
 'CURRENT_STATE.md':'3565211485530631e56a4db63163710d2218dfe0',
 'Plans/Master/WBS/master-wbs.csv':'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
 'Plans/Master/RELATIONSHIP_INDEX.yaml':'c108d2c162bcea2ee4cc01def46d0487a9501032',
 'prototype/TSK-0332/DASHBOARD_DEVICE_MANAGEMENT_PROTOTYPE.md':'7b19f726fefd4675f55fcad2ffb5fbf4e1c4aa2d',
 'prototype/TSK-0332/DASHBOARD_STATE_MODEL.json':'9d591509ae42138e70a02413233d16edcc61737a',
 'prototype/TSK-0332/index.html':'fb6b2a7469932ea63235a8950814bafd4ea53fc6',
 'prototype/TSK-0332/prototype.css':'8c8de09298fa8359952032d022c882b75c43844c',
 'prototype/TSK-0332/app.mjs':'eff3a0db7c9f0464ed750ca2f571524db1a5eb8b',
 'TSK_0332_POST_CR0007_DASHBOARD_DEVICE_MANAGEMENT_ACCEPTANCE_EVIDENCE_2026-08-31.md':'c6ed33e9e8dbeec13c800f97e68befb15a6b5d88',
 'TSK_0332_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md':'6053498411657cc1eb501ab19568607ba971893f',
 '.github/scripts/verify_tsk0332_post_cr0007_structured_20260831.py':'efcfd6f10f18ef3d9c981c3a27b10c944e225de8',
 '.github/scripts/verify_tsk0332_browser_20260831.mjs':'e5dbf04a77c835ec0721d159d30d00decb480b87',
 '.github/workflows/verify-tsk0332-post-cr0007-structured-20260831.yml':'237d43386374d09ed9a6c9ce76bca7352ad323b5',
}

def blob(path):
    return subprocess.check_output(['git','hash-object',path], text=True).strip()

for path, expected in EXPECTED.items():
    actual=blob(path)
    if actual != expected:
        raise SystemExit(f'TSK0332_STALE_INPUT={path}:{actual}:{expected}')

text=RUNTIME.read_text(encoding='utf-8')
heading='## TSK-0332 current accepted stable state — 2026-08-31 — POST-CR-0007'
if heading in text:
    raise SystemExit('TSK0332_RUNTIME_ALREADY_RECONCILED')
for dep in ('TSK-0329','TSK-0142'):
    if f'## {dep} current accepted stable state' not in text:
        raise SystemExit(f'TSK0332_DEPENDENCY_PASS_MISSING={dep}')
if 'LG-06 remains non-PASS' not in text:
    raise SystemExit('TSK0332_LG06_FENCE_MISSING')

now=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
lines=text.splitlines()
for i,line in enumerate(lines):
    if line.startswith('**Updated:**'):
        lines[i]=f'**Updated:** {now}'
        break
text='\n'.join(lines).rstrip()+'\n\n'
section=f'''{heading}\n\n`TSK-0332`: **PASS** under current `ACC-0332 / VER-0332 / EVD-0332`, `DEC-0053/CR-0006` and `DEC-0054/CR-0007` authority.\n\n- Current WBS blob `f3c29b5db8b835ef2c896f61335656ea51d8ba1c`: L4, MEDIUM, hard dependencies `TSK-0329; TSK-0142`, A4 / `AUTO_ALLOWED`; WBS planning state is not runtime proof.\n- Both hard dependencies are current durable PASS.\n- Accepted normative prototype: `prototype/TSK-0332/DASHBOARD_DEVICE_MANAGEMENT_PROTOTYPE.md`, version `1.0.0-post-cr0007`, blob `7b19f726fefd4675f55fcad2ffb5fbf4e1c4aa2d`.\n- Structured dashboard model: `prototype/TSK-0332/DASHBOARD_STATE_MODEL.json`, blob `9d591509ae42138e70a02413233d16edcc61737a`.\n- Runnable prototype blobs: `index.html` `fb6b2a7469932ea63235a8950814bafd4ea53fc6`; `prototype.css` `8c8de09298fa8359952032d022c882b75c43844c`; `app.mjs` `eff3a0db7c9f0464ed750ca2f571524db1a5eb8b`.\n- Analytical evidence: `TSK_0332_POST_CR0007_DASHBOARD_DEVICE_MANAGEMENT_ACCEPTANCE_EVIDENCE_2026-08-31.md`, blob `c6ed33e9e8dbeec13c800f97e68befb15a6b5d88`.\n- Deterministic evidence: `TSK_0332_DETERMINISTIC_VERIFICATION_EVIDENCE_2026-08-31.md`, blob `6053498411657cc1eb501ab19568607ba971893f`.\n- Structural verifier blob `efcfd6f10f18ef3d9c981c3a27b10c944e225de8`; browser verifier blob `e5dbf04a77c835ec0721d159d30d00decb480b87`; workflow blob `237d43386374d09ed9a6c9ce76bca7352ad323b5`.\n- Final run/job `33415101545 / 99563744494`: **SUCCESS** on self-hosted `adguardvm`; Node `v22.23.2`, npm `10.9.8`, Playwright `1.62.0`, Chromium `151.0.7922.34`.\n- Final structural markers: WBS contract PASS; dependency runtime PASS; graph contract PASS; structured model PASS; normative prototype PASS; static UI contract PASS; PASS fence PASS; structured verification PASS.\n- Final browser markers: 320px PASS; responsive 320/768/1024/1440 PASS; keyboard/skip-link PASS; Arabic RTL PASS; state semantics PASS; zero console/page errors PASS.\n- Test-first RED run `33414226440 / 99560920271` proved the verifier rejected missing implementation. Diagnostic failures were retained: one semantic verifier false negative, two runner-environment failures, and one real skip-link focus defect. No failing run mutated runtime PASS.\n- Accepted experience provides polished mobile-first empty/device states, add/setup/status/Protection Map, bounded device controls and contextual help using parent-facing language.\n- Complete core value remains usable without login. Record/account/session/dashboard presence never establishes technical `Verified`; S1 system verification remains distinct from S2 parent confirmation and stale/conflicting evidence downgrades truthfully.\n- Physical UseSafeWeb removal, dashboard-record deletion, unlinking, account deletion and J0/J1 deletion remain distinct lifecycles.\n- Browsing/query/activity history, top sites, child profiles, raw/unrestricted administration, broad per-domain controls, customer query logs and safety scores remain excluded.\n- This PASS does **not** infer TSK-0331, TSK-0333, provider/vendor/security/privacy architecture, persistent schema/storage, production deletion/deployment, behavioral validation, LG-06 or any later gate PASS.\n- `RSK-0002` remains OPEN/non-blocking before L8. `LG-06` remains non-PASS.\n\n### Queue status after post-CR-0007 TSK-0332 acceptance\n\nRecompute eligibility from current WBS dependencies, relationship graph, runtime evidence, gates/constraints and Action Authority. No successor or gate inherits PASS from TSK-0332.\n'''
RUNTIME.write_text(text+section,encoding='utf-8')
print('TSK0332_RUNTIME_PRECONDITIONS=PASS')
