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
# current Version-1 optional-account reconciliation controls
by={r['Task_ID']:r for r in rows}
required={'TSK-0146','TSK-0312','TSK-0142','TSK-0329','TSK-0331','TSK-0332','TSK-0356','TSK-0377','TSK-0394','TSK-0523'}
for tid in required:
    if tid not in by: err('missing V1 account task '+tid)
    elif by[tid]['Plan_Status']=='DEFERRED': err('V1 account task still deferred '+tid)
for tid in ['TSK-0187','TSK-0326','TSK-0336']:
    if by[tid]['Plan_Status']!='NOT_APPLICABLE' or by[tid]['Execution_State']!='PASS': err('CR-0005 exclusion changed '+tid)
if 'optional parent account' not in by['TSK-0146']['Acceptance_Criteria'].lower(): err('V1 account baseline missing')
if 'without login' not in by['TSK-0146']['Acceptance_Criteria'].lower(): err('accountless core guarantee missing')
if 'optional' not in by['TSK-0052']['Acceptance_Criteria'].lower(): err('LG-06 optional account contract missing')
if 'accountless' not in by['TSK-0052']['Acceptance_Criteria'].lower(): err('LG-06 accountless core contract missing')
if 'optional-account boundary' not in by['TSK-0398']['Title'].lower(): err('L7 optional account boundary verification missing')
for tid in ['TSK-0146','TSK-0052','TSK-0398','TSK-0524']:
    a=by[tid]['Acceptance_Criteria'].lower()
    if 'browsing/activity history' not in a and 'browsing/query/activity history' not in a: err('V1 privacy exclusion missing '+tid)
old_note='deferred_exception exc-0001: account/persistence capability is not in the current accountless baseline'
for r in rows:
    if old_note in r['Notes'].lower(): err('stale EXC-0001 task note '+r['Task_ID'])
# CR-0011 reconciliation invariants
recurring_ids={r['Task_ID'] for r in rows if r['Plan_Status']=='PLANNED_RECURRING'}
recurring_hard=[]
for r in rows:
    for d in [x.strip() for x in re.split(r'[;,]',r['Dependencies']) if x.strip()]:
        if d in recurring_ids:
            recurring_hard.append((r['Task_ID'],d))
stats['recurring_hard_predecessors']=len(recurring_hard)
for child,parent in recurring_hard:
    err(f'recurring hard predecessor {child}->{parent}')

decisions_text=(ROOT/'Registers'/'DECISIONS_TRIGGERS.md').read_text(encoding='utf-8')
gates_text=(ROOT/'Registers'/'GATES.md').read_text(encoding='utf-8')
layer5_text=(ROOT/'Layers'/'LAYER_5_AI_EXECUTION_EVIDENCE_STATE_CONTROL.md').read_text(encoding='utf-8')
root_plan_text=(ROOT/'MASTER_PLAN.md').read_text(encoding='utf-8')
manifest_text=MAN.read_text(encoding='utf-8')
if re.search(r'\b100(?:-|\s+)(?:active(?:-|\s+)?)?users?\b', decisions_text+'\n'+gates_text, re.I):
    err('unsupported current 100-user scale trigger present')
if '500-active-user threshold' not in decisions_text or 'internal scale/formalisation review trigger only' not in decisions_text:
    err('500-user formalisation-only control missing')
if 'LG-16' not in decisions_text or 'DEC-0030' not in decisions_text:
    err('independent geographic-expansion control missing')
if 'TSK-0438' not in by or 'DNS/registrar control and renewal state' not in by['TSK-0438']['Title'] or 'renewal' not in by['TSK-0438']['Acceptance_Criteria'].lower():
    err('direct domain-control verification control missing')
if 'TSK-0012' not in by or 'ClickUp' not in by['TSK-0012']['Title']:
    err('current ClickUp derived-view control missing')
if 'TSK-0013' not in by or 'Monday' not in by['TSK-0013']['Title']:
    err('current Monday derived-view control missing')
if 'derived_modules_never_authoritative: true' not in manifest_text:
    err('manifest derived-view authority fence missing')
if 'Derived hierarchy roll-up invariant' not in layer5_text:
    err('derived hierarchy roll-up invariant missing')
if 'Recurring/event dependency invariant' not in layer5_text:
    err('recurring/event dependency invariant missing')
if 'CR-0011 / DEC-0058' not in root_plan_text:
    err('root CR-0011 authority marker missing')
stats['cr0011_invariants']='PASS' if not recurring_hard else 'FAIL'

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
