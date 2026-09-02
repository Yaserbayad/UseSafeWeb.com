from __future__ import annotations

import csv,re,subprocess
from datetime import datetime,timezone
from pathlib import Path

EXPECTED={
"Plans/Master/WBS/master-wbs.csv":"b27a0c5df2f5636d8ed71051e9e26a68959a2616",
"Plans/Master/RELATIONSHIP_INDEX.yaml":"c108d2c162bcea2ee4cc01def46d0487a9501032",
"CURRENT_STATE.md":"2af7f02479cee28b43c1cffe5478d518b866eea8",
"TSK_0585_CURRENT_AUTH_VENDOR_COST_TERMS_EXIT_REVIEW_2026-09-02.md":"101fb63ed4367b514a36f5a07ee271be7cd7a5c3",
"TSK_0585_CURRENT_VENDOR_COST_TERMS_REVIEW_EVIDENCE_2026-09-02.md":"eb5128c1b0538b393770e9020095427571333659",
}
HEADING="## TSK-0585 current accepted stable state — 2026-09-02 — AUTH VENDOR COST/LICENCE/TERMS REVIEW"
def blob(p): return subprocess.check_output(["git","hash-object",p],text=True).strip()
def mask_updated(t): return re.sub(r"^\*\*Updated:\*\*.*$","**Updated:** <MASK>",t,count=1,flags=re.M)
path=Path("CURRENT_STATE.md"); old=path.read_text(encoding="utf-8")
if HEADING in old:
    sec=old.split(HEADING,1)[1]
    for v in ["**PASS**","101fb63ed4367b514a36f5a07ee271be7cd7a5c3","eb5128c1b0538b393770e9020095427571333659","33590152982","100122320757"]: assert v in sec,v
    print("TSK0585_STATE_RECONCILIATION=ALREADY_APPLIED"); raise SystemExit(0)
for p,h in EXPECTED.items():
    a=blob(p)
    if a!=h: raise AssertionError(f"hash drift {p}: {a} != {h}")
print("TSK0585_STATE_INPUT_HASHES=PASS")
with open("Plans/Master/WBS/master-wbs.csv",newline="",encoding="utf-8-sig") as f: rows=list(csv.DictReader(f))
r=next(x for x in rows if x.get("Task_ID")=="TSK-0585")
assert r["Lifecycle_Stage"]=="L4" and r["Priority"]=="MEDIUM" and r["AI_Capability_A0_A4"]=="A3" and r["Action_Authority"]=="AUTO_ALLOWED"
assert [x.strip() for x in (r["Dependencies"] or "").split(";") if x.strip()]==["TSK-0045","TSK-0353","TSK-0044"]
assert (r["Acceptance_ID"],r["Verification_ID"],r["Evidence_ID"])==("ACC-0585","VER-0585","EVD-0585")
print("TSK0585_STATE_WBS_CONTRACT=PASS")
ev=Path("TSK_0585_CURRENT_VENDOR_COST_TERMS_REVIEW_EVIDENCE_2026-09-02.md").read_text(encoding="utf-8")
for v in ["ACC-0585 = PASS","VER-0585 = PASS","EVD-0585 = SATISFIED","33590152982","100122320757","TSK0585_CURRENT_REVIEW=PASS"]: assert v in ev,v
print("TSK0585_STATE_EVIDENCE_BINDING=PASS")
now=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
base=re.sub(r"^\*\*Updated:\*\*.*$",f"**Updated:** {now}",old,count=1,flags=re.M)
assert mask_updated(base)==mask_updated(old)
append=f'''\n\n{HEADING}\n\n`TSK-0585 — Verify authentication free tier, AdGuard licence/API cost, vendor terms and exit triggers`: **PASS** under current `ACC-0585 / VER-0585 / EVD-0585` and current predecessors TSK-0045 / TSK-0353 / TSK-0044.\n\n- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / MEDIUM / A3 / `AUTO_ALLOWED`; dependencies exactly `TSK-0045; TSK-0353; TSK-0044`.\n- Current dated artifact `TSK_0585_CURRENT_AUTH_VENDOR_COST_TERMS_EXIT_REVIEW_2026-09-02.md`, blob `101fb63ed4367b514a36f5a07ee271be7cd7a5c3`, publication commit `fd8b89ef42509a092c17a0e140cc8236472cda1c`.\n- Durable evidence `TSK_0585_CURRENT_VENDOR_COST_TERMS_REVIEW_EVIDENCE_2026-09-02.md`, blob `eb5128c1b0538b393770e9020095427571333659`, publication commit `38a83bccfdc4eefd3e9008b0171e331f563e1825`.\n- Independent read-only live-source VER-0585: final wrapper blob `49251cf0cec47c59ff51e7c99210c684c1d92de1`, workflow blob `23d5e7033bf63c24c3c85a0cfc4a18cd65a2ca58`, run/job `33590152982 / 100122320757`, conclusion **SUCCESS**.\n- Current auth-cost fact: planned Google/social Firebase Authentication has a current no-cost Spark path; Identity Platform remains optional with explicit Spark/Blaze thresholds; current V1 has no SMS path. This is not a zero-total-service-cost claim.\n- Current processing-location fact: Firebase Authentication is currently documented by Firebase as US-only. Legal/transfer acceptability remains unresolved and is not inferred.\n- Current AdGuard fact: official AdGuard Home materials describe the self-hosted project as free/open-source GPL-3.0 with REST/OpenAPI integration; no separate AdGuard Home API subscription/per-call fee is evidenced by the reviewed official self-hosted project materials. Infrastructure and GPL/legal questions remain separate.\n- Firebase/AdGuard pricing, terms, location, licence/API, threshold, legal/privacy, provider and infrastructure-cost re-review/exit triggers are explicit in the accepted artifact.\n- **ACC-0585 = PASS. VER-0585 = PASS. EVD-0585 = SATISFIED.**\n- **Non-inference:** no vendor activation, paid-plan purchase, contract/legal approval, infrastructure purchase, software deployment, participant processing, market activation, lifecycle gate or successor PASS is inferred.\n\n### Queue status after current TSK-0585 acceptance\n\nRecompute the executable frontier from canonical WBS/graph, current runtime evidence, artifact-specific current-validity, gates and Action Authority. Preserve valid non-uniform historical PASS records unless current evidence materially invalidates them.\n'''
candidate=base+append
assert mask_updated(candidate)==mask_updated(old)+append
print("TSK0585_ALL_EXISTING_RUNTIME_BODY_PRESERVED=PASS")
path.write_text(candidate,encoding="utf-8")
written=path.read_text(encoding="utf-8")
for v in [HEADING,"101fb63ed4367b514a36f5a07ee271be7cd7a5c3","eb5128c1b0538b393770e9020095427571333659","33590152982 / 100122320757","ACC-0585 = PASS. VER-0585 = PASS. EVD-0585 = SATISFIED."]: assert v in written,v
print("TSK0585_STATE_CANDIDATE=PASS")
print("TSK0585_STATE_RECONCILIATION=PASS")
