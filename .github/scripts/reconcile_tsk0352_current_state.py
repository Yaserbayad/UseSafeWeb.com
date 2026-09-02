from __future__ import annotations

import csv,re,subprocess
from datetime import datetime,timezone
from pathlib import Path

EXPECTED={
"Plans/Master/WBS/master-wbs.csv":"b27a0c5df2f5636d8ed71051e9e26a68959a2616",
"Plans/Master/RELATIONSHIP_INDEX.yaml":"c108d2c162bcea2ee4cc01def46d0487a9501032",
"CURRENT_STATE.md":"761a608e37a959b237336d5f44aefefb4dc4fa3f",
"TSK_0352_POST_CR0008_ADGUARD_PERSISTENT_CLIENTID_API_LIFECYCLE_CONTRACT_2026-09-02.md":"e5cbbcac2f42810527717549482765b6b1ad72c1",
"TSK_0352_POST_CR0008_CURRENT_CONTRACT_EVIDENCE_2026-09-02.md":"4353991a443e162ce8ec3a9b1090c6ed9778a196",
}
HEADING="## TSK-0352 current accepted stable state — 2026-09-02 — PERSISTENT CLIENTID/API/LIFECYCLE CONTRACT"
def blob(p): return subprocess.check_output(["git","hash-object",p],text=True).strip()
def mask_updated(t): return re.sub(r"^\*\*Updated:\*\*.*$","**Updated:** <MASK>",t,count=1,flags=re.M)
path=Path("CURRENT_STATE.md"); old=path.read_text(encoding="utf-8")
if HEADING in old:
    sec=old.split(HEADING,1)[1]
    for v in ["**PASS**","e5cbbcac2f42810527717549482765b6b1ad72c1","4353991a443e162ce8ec3a9b1090c6ed9778a196","33590945044","100124642037"]: assert v in sec,v
    print("TSK0352_STATE_RECONCILIATION=ALREADY_APPLIED"); raise SystemExit(0)
for p,h in EXPECTED.items():
    a=blob(p)
    if a!=h: raise AssertionError(f"hash drift {p}: {a} != {h}")
print("TSK0352_STATE_INPUT_HASHES=PASS")
with open("Plans/Master/WBS/master-wbs.csv",newline="",encoding="utf-8-sig") as f: rows=list(csv.DictReader(f))
r=next(x for x in rows if x.get("Task_ID")=="TSK-0352")
assert r["Lifecycle_Stage"]=="L4" and r["Priority"]=="MEDIUM" and r["AI_Capability_A0_A4"]=="A3" and r["Action_Authority"]=="AUTO_ALLOWED"
assert [x.strip() for x in (r["Dependencies"] or "").split(";") if x.strip()]==["TSK-0041","TSK-0142"]
assert (r["Acceptance_ID"],r["Verification_ID"],r["Evidence_ID"])==("ACC-0352","VER-0352","EVD-0352")
print("TSK0352_STATE_WBS_CONTRACT=PASS")
ev=Path("TSK_0352_POST_CR0008_CURRENT_CONTRACT_EVIDENCE_2026-09-02.md").read_text(encoding="utf-8")
for v in ["ACC-0352 = PASS","VER-0352 = PASS","EVD-0352 = SATISFIED","33590945044","100124642037","TSK0352_CURRENT_CONTRACT=PASS"]: assert v in ev,v
print("TSK0352_STATE_EVIDENCE_BINDING=PASS")
now=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
base=re.sub(r"^\*\*Updated:\*\*.*$",f"**Updated:** {now}",old,count=1,flags=re.M)
assert mask_updated(base)==mask_updated(old)
append=f'''\n\n{HEADING}\n\n`TSK-0352 — Specify AdGuard API, persistent ClientID, privacy and lifecycle contract`: **PASS** under current `ACC-0352 / VER-0352 / EVD-0352`, current direct predecessors TSK-0041 / TSK-0142, and the frozen AdGuard Home v0.107.79 API boundary.\n\n- Current WBS `b27a0c5df2f5636d8ed71051e9e26a68959a2616`: L4 / MEDIUM / A3 / `AUTO_ALLOWED`; dependencies exactly `TSK-0041; TSK-0142`.\n- Current artifact `TSK_0352_POST_CR0008_ADGUARD_PERSISTENT_CLIENTID_API_LIFECYCLE_CONTRACT_2026-09-02.md`, version `1.0.0-post-CR0008`, blob `e5cbbcac2f42810527717549482765b6b1ad72c1`, publication commit `d5bf580f5d416539f9c176c2cec9aa65c69fa8aa`.\n- Durable evidence `TSK_0352_POST_CR0008_CURRENT_CONTRACT_EVIDENCE_2026-09-02.md`, blob `4353991a443e162ce8ec3a9b1090c6ed9778a196`, publication commit `bf9545aa79ccdc4b69e7a30b74ace3dc0f114b3a`.\n- Independent read-only VER-0352: base script blob `43a4013967c8066ba2c1f79d68a512c49cf9aef3`, final wrapper blob `11640b9b0c99c0a19440eda7987f3dcd32474539`, workflow blob `3c3832a66ed03d5cbe5ac8f163b1ae0a97abdfcd`, run/job `33590945044 / 100124642037`, conclusion **SUCCESS**.\n- Accepted API boundary: private server-side exact client search/add/update/delete only; no generic customer `/control` proxy and no browser/admin credential exposure.\n- Accepted ClientID boundary: server-generated 26-character lowercase base32 random identifier, collision-checked, identity-independent and never an authorization token or technical protection proof.\n- Accepted privacy boundary: persistent clients explicitly set `ignore_querylog=true` and `ignore_statistics=true` while the global no-history/no-statistics baseline remains independently required.\n- Accepted direct DoH route: `https://dns.usesafeweb.com/dns-query/{{client_id}}`; accountless route remains without persistent ClientID.\n- Lifecycle create/search/update/rotation/delete requires current parent/device authorization, exact read-back, datastore + AdGuard terminal agreement, no blind ambiguous mutation replay and state-based rollback/reconciliation.\n- Version/API/ClientID/privacy-field drift reopens the affected integration; v0.108+ behavior is not silently imported.\n- **ACC-0352 = PASS. VER-0352 = PASS. EVD-0352 = SATISFIED.**\n- **Non-inference:** this is L4 contract-definition PASS only; it does not deploy the adapter, call live AdGuard, create/update/delete a client, activate account/auth/datastore services, authorize real-user processing, pass a lifecycle gate, publish, launch or infer successor PASS.\n\n### Queue status after current TSK-0352 acceptance\n\nRecompute the executable frontier from canonical WBS/graph, current runtime evidence, artifact-specific current-validity, gates and Action Authority. Preserve valid non-uniform historical PASS records unless current evidence materially invalidates them.\n'''
candidate=base+append
assert mask_updated(candidate)==mask_updated(old)+append
print("TSK0352_ALL_EXISTING_RUNTIME_BODY_PRESERVED=PASS")
path.write_text(candidate,encoding="utf-8")
written=path.read_text(encoding="utf-8")
for v in [HEADING,"e5cbbcac2f42810527717549482765b6b1ad72c1","4353991a443e162ce8ec3a9b1090c6ed9778a196","33590945044 / 100124642037","ACC-0352 = PASS. VER-0352 = PASS. EVD-0352 = SATISFIED."]: assert v in written,v
print("TSK0352_STATE_CANDIDATE=PASS")
print("TSK0352_STATE_RECONCILIATION=PASS")
