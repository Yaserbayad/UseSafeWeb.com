#!/usr/bin/env python3
import csv, hashlib, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request
from datetime import datetime, timezone

API='https://api.clickup.com/api/v2'
EXPECTED_SHA='234d42e86968cb2b466aba9ffc7c56355d9fbd37cc7d96085caf2baef7b40cd1'
PRIORITY={'Critical':1,'High':2,'Medium':3,'Low':4}
STATUS={
 'Planned':'planned','Ready':'ready','In Progress':'in progress','Blocked':'blocked','Completed':'completed',
 'Completed — evidence incomplete':'comple eviden incomplete','Deferred':'deferred','Recurring':'recurring','Not Applicable':'not applicable'
}
DEP_SPLIT=re.compile(r'[;,|\n]+')
ISO_DATE=re.compile(r'^\d{4}-\d{2}-\d{2}$')


def sha256(path):
 h=hashlib.sha256()
 with open(path,'rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
 return h.hexdigest()


def deps(raw): return [x.strip() for x in DEP_SPLIT.split(raw or '') if x.strip()]

def date_ms(v):
 v=(v or '').strip()
 if not ISO_DATE.fullmatch(v): return None
 return int(datetime.strptime(v,'%Y-%m-%d').replace(tzinfo=timezone.utc).timestamp()*1000)


def stable_name(r): return f"{r['WBS_ID'].strip()} — {r['Task_Name'].strip()}"

def description(r):
 meta={k:(v or '') for k,v in r.items() if (v or '').strip()}
 return (f"# {r['WBS_ID'].strip()} — {r['Task_Name'].strip()}\n\n"
         f"**UseSafeWeb Master WBS**  \nSource SHA-256: `{EXPECTED_SHA}`  \n"
         f"WBS ID: `{r['WBS_ID'].strip()}`  \nSource Status: `{r['Status'].strip()}`\n\n"
         f"## Authoritative WBS metadata\n```json\n{json.dumps(meta,ensure_ascii=False,indent=2)}\n```\n")


def load_validate(path):
 if sha256(path)!=EXPECTED_SHA: raise ValueError('source SHA-256 mismatch')
 with open(path,newline='',encoding='utf-8-sig') as f: rows=list(csv.DictReader(f))
 if len(rows)!=743: raise ValueError(f'expected 743 rows, got {len(rows)}')
 ids=[r['WBS_ID'].strip() for r in rows]
 if len(ids)!=len(set(ids)): raise ValueError('duplicate WBS_ID')
 by={r['WBS_ID'].strip():r for r in rows}
 roots=[]; edges=0
 for r in rows:
  wid=r['WBS_ID'].strip(); p=r['Parent_WBS_ID'].strip(); lvl=int(r['Level'])
  if p:
   if p not in by: raise ValueError(f'{wid}: missing parent {p}')
   if int(by[p]['Level'])!=lvl-1: raise ValueError(f'{wid}: level mismatch vs parent {p}')
  else:
   roots.append(wid)
   if lvl!=0: raise ValueError(f'{wid}: root level must be 0')
  if r['Status'].strip() not in STATUS: raise ValueError(f'{wid}: unsupported status {r["Status"]!r}')
  if r['Priority'].strip() not in PRIORITY: raise ValueError(f'{wid}: unsupported priority {r["Priority"]!r}')
  for d in deps(r['Dependency_IDs']):
   edges+=1
   if d not in by: raise ValueError(f'{wid}: missing dependency {d}')
   if d==wid: raise ValueError(f'{wid}: self dependency')
 if roots!=['USW']: raise ValueError(f'expected single root USW, got {roots}')
 for wid in ids:
  seen=set(); cur=wid
  while by[cur]['Parent_WBS_ID'].strip():
   if cur in seen: raise ValueError(f'parent cycle at {wid}')
   seen.add(cur); cur=by[cur]['Parent_WBS_ID'].strip()
 if edges!=975: raise ValueError(f'expected 975 dependency edges, got {edges}')
 return sorted(rows,key=lambda r:(int(r['Level']),r['WBS_ID']))


class CU:
 def __init__(self,token):
  self.token=token; self.calls=0; self.last=0.0
 def request(self,method,path,body=None,tries=8):
  url=API+path
  data=None if body is None else json.dumps(body,ensure_ascii=False).encode()
  for attempt in range(tries):
   wait=max(0,0.72-(time.monotonic()-self.last))
   if wait: time.sleep(wait)
   req=urllib.request.Request(url,data=data,method=method,headers={'Authorization':self.token,'Content-Type':'application/json'})
   try:
    self.last=time.monotonic(); self.calls+=1
    with urllib.request.urlopen(req,timeout=45) as resp:
     raw=resp.read(); return json.loads(raw) if raw else {}
   except urllib.error.HTTPError as e:
    msg=e.read().decode('utf-8','replace')
    if e.code==429 or 500<=e.code<600:
     ra=e.headers.get('Retry-After')
     time.sleep(float(ra) if ra and ra.replace('.','',1).isdigit() else min(30,2**attempt)); continue
    raise RuntimeError(f'{method} {path} -> HTTP {e.code}: {msg[:1000]}') from e
   except (urllib.error.URLError,TimeoutError) as e:
    if attempt==tries-1: raise
    time.sleep(min(30,2**attempt))
  raise RuntimeError(f'{method} {path}: retries exhausted')

 def get_list(self,lid): return self.request('GET',f'/list/{lid}')
 def tasks(self,lid):
  out=[]
  for page in range(100):
   q=urllib.parse.urlencode({'page':page,'subtasks':'true','include_closed':'true','include_markdown_description':'true'})
   data=self.request('GET',f'/list/{lid}/task?{q}')
   batch=data.get('tasks') or []; out.extend(batch)
   if len(batch)<100: break
  return out
 def create(self,lid,body): return self.request('POST',f'/list/{lid}/task',body)
 def add_dep(self,tid,depends_on): return self.request('POST',f'/task/{tid}/dependency',{'depends_on':depends_on})


def get_parent_id(t):
 p=t.get('parent')
 if isinstance(p,dict): return str(p.get('id') or '')
 return str(p or '')

def priority_num(t):
 p=t.get('priority')
 if isinstance(p,dict):
  v=p.get('priority')
  try:return int(v)
  except:return None
 try:return int(p)
 except:return None

def dep_targets(t):
 tid=str(t.get('id') or ''); out=set()
 for d in t.get('dependencies') or []:
  target=str(d.get('depends_on') or ''); src=str(d.get('task_id') or '')
  if target and (not src or src==tid): out.add(target)
 return out

def task_text(t): return str(t.get('markdown_description') or t.get('description') or t.get('text_content') or '')

def main():
 csv_path=os.environ.get('WBS_CSV','deployment/clickup/UseSafeWeb_Master_Plan_WBS.csv')
 report_path=os.environ.get('DEPLOYMENT_REPORT','deployment/clickup/DEPLOYMENT_REPORT.json')
 token=os.environ.get('CLICKUP_TOKEN','').strip(); lid=os.environ.get('CLICKUP_LIST_ID','').strip(); sid=os.environ.get('CLICKUP_SPACE_ID','').strip()
 if not token or not lid or not sid: raise SystemExit('CLICKUP_TOKEN, CLICKUP_LIST_ID, CLICKUP_SPACE_ID are required')
 rows=load_validate(csv_path); client=CU(token)
 report={'result':'FAIL','source_sha256':EXPECTED_SHA,'source_rows':743,'expected_parent_links':742,'expected_dependency_edges':975,
         'space_id':sid,'list_id':lid,'status_aliases':{'Completed — evidence incomplete':'comple eviden incomplete'},'created':0,'reused':0,'dependencies_created':0,'errors':[]}
 try:
  lst=client.get_list(lid)
  if str((lst.get('space') or {}).get('id') or '')!=sid: raise RuntimeError('target List is not in expected UseSafeWeb Space')
  live_status={str(s.get('status') or '').casefold() for s in (lst.get('statuses') or [])}
  missing=sorted({v for v in STATUS.values() if v.casefold() not in live_status})
  if missing: raise RuntimeError(f'missing target statuses: {missing}')
  existing=client.tasks(lid); expected_names={stable_name(r) for r in rows}
  unexpected=[t for t in existing if (t.get('name') or '') not in expected_names]
  if unexpected: raise RuntimeError(f'target list has {len(unexpected)} unexpected task(s); refusing to mix/overwrite')
  name_map={t.get('name'):t for t in existing}; idmap={}
  for r in rows:
   wid=r['WBS_ID'].strip(); name=stable_name(r)
   if name in name_map:
    tid=str(name_map[name]['id']); report['reused']+=1
   else:
    body={'name':name,'markdown_content':description(r),'status':STATUS[r['Status'].strip()],'priority':PRIORITY[r['Priority'].strip()]}
    s=date_ms(r['Start_Period']); d=date_ms(r['Due_Period'])
    if s is not None: body['start_date']=s
    if d is not None: body['due_date']=d
    p=r['Parent_WBS_ID'].strip()
    if p: body['parent']=idmap[p]
    obj=client.create(lid,body); tid=str(obj['id']); report['created']+=1
   idmap[wid]=tid
  current={t.get('name'):t for t in client.tasks(lid)}
  for r in rows:
   wid=r['WBS_ID'].strip(); tid=idmap[wid]; have=dep_targets(current.get(stable_name(r),{}))
   for d in deps(r['Dependency_IDs']):
    target=idmap[d]
    if target not in have:
     client.add_dep(tid,target); report['dependencies_created']+=1
  final=client.tasks(lid)
  if len(final)!=743: raise RuntimeError(f'read-back task count {len(final)} != 743')
  fmap={t.get('name'):t for t in final}; parents=0; dep_edges=0
  for r in rows:
   wid=r['WBS_ID'].strip(); name=stable_name(r); t=fmap.get(name)
   if not t: raise RuntimeError(f'{wid}: missing after read-back')
   if str(t.get('id'))!=idmap[wid]: raise RuntimeError(f'{wid}: task id changed')
   p=r['Parent_WBS_ID'].strip(); expected_parent=idmap[p] if p else ''
   if get_parent_id(t)!=expected_parent: raise RuntimeError(f'{wid}: parent mismatch')
   if p: parents+=1
   got_status=str((t.get('status') or {}).get('status') or '').casefold()
   if got_status!=STATUS[r['Status'].strip()].casefold(): raise RuntimeError(f'{wid}: status mismatch {got_status!r}')
   if priority_num(t)!=PRIORITY[r['Priority'].strip()]: raise RuntimeError(f'{wid}: priority mismatch')
   text=task_text(t)
   if EXPECTED_SHA not in text or wid not in text: raise RuntimeError(f'{wid}: description/source marker mismatch')
   expected={idmap[d] for d in deps(r['Dependency_IDs'])}; got=dep_targets(t); dep_edges+=len(expected)
   if not expected.issubset(got): raise RuntimeError(f'{wid}: dependency mismatch missing={sorted(expected-got)}')
  if parents!=742 or dep_edges!=975: raise RuntimeError(f'aggregate mismatch parents={parents} dependencies={dep_edges}')
  report.update({'result':'PASS','verified_tasks':743,'verified_parent_links':parents,'verified_dependency_edges':dep_edges,'wbs_to_clickup_id':idmap})
 except Exception as e:
  report['errors'].append(str(e)); raise
 finally:
  report['api_requests']=client.calls
  os.makedirs(os.path.dirname(report_path) or '.',exist_ok=True)
  with open(report_path,'w',encoding='utf-8') as f: json.dump(report,f,ensure_ascii=False,indent=2,sort_keys=True)
 if report['result']!='PASS': raise SystemExit(1)
 print(json.dumps({k:report[k] for k in ['result','verified_tasks','verified_parent_links','verified_dependency_edges','created','reused','dependencies_created','api_requests']},indent=2))

if __name__=='__main__': main()
