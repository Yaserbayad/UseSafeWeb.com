from datetime import datetime, timezone
from pathlib import Path
import re

p=Path('CURRENT_STATE.md')
text=p.read_text(encoding='utf-8')
marker='## CR-0005 integrated-product-first human-validation sequencing — 2026-08-29'
if marker in text:
    print('RUNTIME_CR0005_ALREADY_RECONCILED=PASS')
    raise SystemExit(0)

now=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
text,n=re.subn(r'^\*\*Updated:\*\* .+$',f'**Updated:** {now}',text,count=1,flags=re.M)
if n!=1:
    raise SystemExit('Updated timestamp replacement failed')

replacements={
'**ACTIVE / OWNER-FROZEN / POST-FREEZE CR-0004 PUBLISHED, RECONCILED, READ-BACK VERIFIED.**':'**ACTIVE / OWNER-FROZEN / POST-FREEZE CR-0005 PUBLISHED, RECONCILED, READ-BACK VERIFIED.**',
'- Latest post-freeze change: `CR-0004` / `DEC-0051`, explicit Project Owner authority 2026-08-29.':'- Latest post-freeze change: `CR-0005` / `DEC-0052`, explicit Project Owner authority 2026-08-29: integrated product first; no parent/user/participant testing before LG-09/L8.',
'- CR-0004 planning publication commit: `aa875f6dbb4014edda9d80473963280a33306041`; durable evidence `CR_0004_PROVISIONAL_L4_BRAND_UX_DECOUPLING_EVIDENCE_2026-08-29.md`.':'- CR-0005 planning publication commit: `16e4007d8a4856f92cb690e29d6df90fa3356549`; durable evidence `CR_0005_INTEGRATED_PRODUCT_FIRST_VALIDATION_SEQUENCE_EVIDENCE_2026-08-29.md`, blob `c511be2de8ad55a50909514b7965b67bbe7539cc`.',
'- Manifest latest-change reconciliation commit: `50b2882` with repaired evidence record commit `e42f90d2be66405c41acecf2088e5e9e2e60f4f0`.':'- CR-0005 fresh-checkout read-back run/job: `33266767165` / `99138083913`; all declared checksums and the official master-plan validator passed.',
'- Current authoritative WBS blob: `6a25d63af125116a80f96ac0f1548b1ddb452a34`; relationship-index blob: `9ed219b4ccb6b05e68c6a264fc2b21b1008b02a4`; manifest blob: `acadf21483ee3fddd63ee57795126619f92a00f3`.':'- Current authoritative WBS blob: `f23b4f017d1baf73258fa30ecd71549bbfe1b815`; relationship-index blob remains `9ed219b4ccb6b05e68c6a264fc2b21b1008b02a4`; manifest blob: `1fc24e28e70c8005a75d37c1d21aecd4ea967ae5`.',
'- Deterministic validation after amendment/reconciliation: 641 tasks, 849 dependency edges, 5,178 relationship entities, 20,463 targets, 0 broken links, 0 generated missing task IDs; checksum inventory regenerated and verified.':'- Deterministic validation/read-back after CR-0005: 641 tasks, 849 dependency edges, 5,178 relationship entities, 20,463 targets, 0 broken links, 0 generated missing task IDs; all declared checksums verified from fresh GitHub checkout.',
'- CR-0004 changes only the provisional Brand/UX/prototype sequencing needed for internal L4 design: `TSK-0298` now depends on the accepted provisional L4 bridge `TSK-0139` instead of `TSK-0187`; `TSK-0309 -> TSK-0187` remains unchanged.':'- CR-0005 supersedes CR-0003/CR-0004 for human-validation sequencing: all 31 L3 tasks plus `TSK-0187`, `TSK-0326`, and `TSK-0336` are `NOT_APPLICABLE + PASS` exclusion records; they were not executed and supply no behavioral evidence. Historical dependency edges remain for traceability.',
'- `TSK-0187` remains mandatory representative-parent behavioral validation; `RSK-0002` remains OPEN; LG-03/LG-04/LG-05/LG-06 remain non-PASS as applicable; no legal/privacy/participant/L5-L6 build/publication/payment/market/launch authority is created.':'- `TSK-0187` no longer blocks pre-product progression; its dependency is satisfied only by verified exclusion semantics. LG-03/LG-04/LG-05 are inactive on the current path; LG-06/LG-07/LG-08/LG-09 remain mandatory technical/product/build/release gates. `RSK-0002` remains OPEN as an accepted product-assumption risk, not a pre-product human-testing blocker. No legal/privacy/participant/publication/payment/market/launch authority is created.'
}
for old,new in replacements.items():
    if text.count(old)!=1:
        raise SystemExit('Runtime replacement precondition failed: '+old[:80])
    text=text.replace(old,new,1)

block=f'''\n\n{marker}\n\n`DEC-0052 / CR-0005`: **CURRENT / VERIFIED**. The Project Owner's integrated-product-first sequencing is now canonical and has passed deterministic publication plus fresh GitHub read-back.\n\n- Pre-product parent/user/participant validation is excluded from active L4-L7 progression. The 31 L3 tasks plus `TSK-0187`, `TSK-0326`, and `TSK-0336` are `NOT_APPLICABLE + PASS` only as verified exclusions; no user/behavioral evidence is claimed.\n- First actual human/user validation is L8 after `LG-09 PASS`. Do not resurrect the retired pre-product validation branch as a blocker unless a later explicit owner decision supersedes DEC-0052.\n- Technical/product/accessibility/browser/device/network/security/privacy/performance/recovery/operational verification remains mandatory where applicable.\n- `TSK-0310` remains **PASS** on durable rendered-browser evidence `TSK_0310_RENDERED_BROWSER_ACCEPTANCE_EVIDENCE_2026-08-29.md`.\n- `TSK-0309 — Freeze the implementation-ready experience baseline from current internal and automated acceptance evidence`: **TODO / eligible**. Its hard dependencies are satisfied under current semantics: `TSK-0310=PASS`; `TSK-0187=NOT_APPLICABLE+PASS` exclusion. It is L4, A3/AUTO_ALLOWED, and no current human-validation gate blocks it.\n- `TSK-0327` remains planned downstream work; `TSK-0399` remains later L7 technical new-user-path acceptance.\n\n### Exact next authoritative step\n\nExecute `TSK-0309` against its rebaselined ACC/VER/EVD contract using the current accepted prototype and internal/automated target-environment evidence; correct/retest any material pre-product defects, persist durable evidence, then independently evaluate PASS and recompute eligibility. No parent/user/participant testing is required or to be scheduled before LG-09/L8.\n'''
text=text.rstrip()+block
p.write_text(text,encoding='utf-8')
print('RUNTIME_CR0005_EDIT=PASS')
