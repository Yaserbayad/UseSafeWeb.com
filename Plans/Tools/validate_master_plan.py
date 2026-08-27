#!/usr/bin/env python3
from pathlib import Path
import csv, hashlib, re, sys
ROOT=Path(__file__).resolve().parents[1]
PLANS=ROOT.parent
WBS=ROOT/'WBS'/'master-wbs.csv'
MAN=ROOT/'MANIFEST.yaml'
REL=ROOT/'RELATIONSHIP_INDEX.yaml'
GEN=ROOT/'Generated'/'MASTER_PLAN_FULL.md'
SUM=PLANS/'SHA256SUMS.txt'
errors=[]; stats={}

def err(x): errors.append(x)
def order():
    out=[]; inside=False
    for line in MAN.read_text(encoding='utf-8').splitlines():
        if line.startswith('deterministic_assembly_order:'): inside=True; continue
        if inside:
            if line.startswith('- '): out.append(line[2:].strip().strip("'\"")); continue
            if line and not line.startswith(' '): break
    return out

ordr=order(); stats['assembly_modules']=len(ordr)
if len(ordr)!=len(set(ordr)): err('duplicate manifest assembly path')
for p in ordr:
    if not (ROOT/p).is_file(): err('missing assembly module '+p)

with WBS.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
ids=[r['Task_ID'] for r in rows]; idset=set(ids); stats['tasks']=len(rows)
if len(ids)!=len(idset): err('duplicate task id')
if any(not x for x in ids): err('blank task id')
# dependencies + cycles
adj={i:[] for i in idset}; edges=0
for r in rows:
    for d in [x.strip() for x in re.split(r'[;,]',r['Dependencies']) if x.strip()]:
        edges+=1
        if d not in idset: err(f'unknown dependency {r["Task_ID"]}->{d}')
        else: adj[d].append(r['Task_ID'])
stats['dependency_edges']=edges
state={}; cycle=False
def dfs(n):
    global cycle
    state[n]=1
    for q in adj[n]:
        if state.get(q)==1: cycle=True
        elif state.get(q,0)==0: dfs(q)
    state[n]=2
for i in ids:
    if state.get(i,0)==0: dfs(i)
if cycle: err('dependency cycle')
# authority matrix
valid={('A1','HUMAN_ONLY'),('A2','HUMAN_APPROVAL_REQUIRED'),('A3','AUTO_ALLOWED'),('A4','AUTO_ALLOWED')}
for r in rows:
    if (r['AI_Capability_A0_A4'],r['Action_Authority']) not in valid: err('authority mismatch '+r['Task_ID'])
# specific accountless reconciliation controls
corrected={'TSK-0024','TSK-0042','TSK-0044','TSK-0048','TSK-0049','TSK-0051','TSK-0052','TSK-0053','TSK-0055','TSK-0056','TSK-0141','TSK-0233','TSK-0235','TSK-0240','TSK-0246','TSK-0251','TSK-0252','TSK-0265','TSK-0288','TSK-0313','TSK-0336','TSK-0337','TSK-0340','TSK-0355','TSK-0485','TSK-0497','TSK-0499','TSK-0507','TSK-0516','TSK-0524','TSK-0534','TSK-0553','TSK-0586'}
by={r['Task_ID']:r for r in rows}
for tid in corrected:
    if tid not in by: err('missing corrected task '+tid)
# forbid stale active mandatory-identity phrases in corrected tasks
for tid in corrected:
    a=by[tid]['Acceptance_Criteria'].lower()
    bad=['firebase uid','google sign-in','google authentication','authenticated parent dashboard','parent/device ownership store','parent-device idor','production-like firebase/google auth']
    for b in bad:
        if b in a: err(f'stale account architecture remains {tid}: {b}')
# publication tree semantics
for tid in ['TSK-0009','TSK-0011','TSK-0017']:
    if 'Plans/' not in by[tid]['Acceptance_Criteria'] and 'Plans/' not in by[tid]['Title']: err('publication not modular '+tid)
# relationship locator parser
ents=set(); targets=[]; sources=[]
for line in REL.read_text(encoding='utf-8').splitlines():
    m=re.match(r'^  ([A-Za-z0-9_.:-]+):$',line)
    if m and m.group(1) not in {'relationships'}: ents.add(m.group(1))
    m=re.match(r'^    - target: (.+)$',line)
    if m: targets.append(m.group(1).strip())
    m=re.match(r'^    source: (.+)$',line)
    if m: sources.append(m.group(1).strip())
stats['relationship_entities']=len(ents); stats['relationship_targets']=len(targets)
for x in targets:
    if x not in ents: err('unknown relationship target '+x)
for s in set(sources):
    if not (ROOT/s).exists(): err('missing relationship source '+s)
# markdown links including generated
linkre=re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')
broken=[]
for md in ROOT.rglob('*.md'):
    text=md.read_text(encoding='utf-8')
    for target in linkre.findall(text):
        if target.startswith(('http://','https://','mailto:','#')): continue
        path=target.split('#',1)[0]
        if not path: continue
        if not (md.parent/path).resolve().exists(): broken.append((md.relative_to(ROOT).as_posix(),target))
stats['broken_links']=len(broken)
for x in broken[:20]: err('broken link '+repr(x))
# generated assembly markers/order + every task id
text=GEN.read_text(encoding='utf-8')
mods=re.findall(r'<!-- BEGIN MODULE: (.+?) -->',text)
if mods!=ordr: err('generated assembly order mismatch')
missing=[tid for tid in ids if tid not in text]
stats['generated_missing_task_ids']=len(missing)
if missing: err('generated missing task ids '+','.join(missing[:10]))
# checksums if present
if SUM.exists():
    for line in SUM.read_text(encoding='utf-8').splitlines():
        if not line.strip(): continue
        h,rel=line.split('  ',1); p=PLANS/rel
        if not p.is_file(): err('checksum file missing '+rel); continue
        got=hashlib.sha256(p.read_bytes()).hexdigest()
        if got!=h: err('checksum mismatch '+rel)
print('VALIDATION', 'PASS' if not errors else 'FAIL')
for k,v in stats.items(): print(f'{k}={v}')
if errors:
    for e in errors: print('ERROR',e)
    sys.exit(1)
