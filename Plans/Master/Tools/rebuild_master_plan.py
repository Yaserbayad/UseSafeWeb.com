#!/usr/bin/env python3
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
MAN=ROOT/'MANIFEST.yaml'
OUT=ROOT/'Generated'/'MASTER_PLAN_FULL.md'

def assembly_order(text):
    lines=text.splitlines(); out=[]; inside=False
    for line in lines:
        if line.startswith('deterministic_assembly_order:'):
            inside=True; continue
        if inside:
            if line.startswith('- '): out.append(line[2:].strip().strip("'\"")); continue
            if line and not line.startswith(' '): break
    return out

def rebase_links(text, source_rel):
    src=(ROOT/source_rel).parent
    outdir=OUT.parent
    pat=re.compile(r'(!?\[[^\]]*\])\(([^)]+)\)')
    def sub(m):
        label,target=m.group(1),m.group(2)
        if target.startswith(('http://','https://','mailto:','#')): return m.group(0)
        path,sep,anchor=target.partition('#')
        if not path: return m.group(0)
        resolved=(src/path).resolve()
        try: rel=resolved.relative_to(ROOT.resolve())
        except ValueError: return m.group(0)
        new=Path('..')/rel
        s=new.as_posix()+(('#'+anchor) if sep else '')
        return f'{label}({s})'
    return pat.sub(sub,text)

order=assembly_order(MAN.read_text(encoding='utf-8'))
parts=['# UseSafeWeb.com - Complete Reconstructed Master Plan','', '> **DERIVED / NON-AUTHORITATIVE / DO NOT EDIT independently.**', '>', '> Authoritative information resides in the modular source files under `Plans/Master/`. Conflicts resolve in favor of those authoritative modules according to `MASTER_PLAN.md` and `MANIFEST.yaml`. This file is rebuilt deterministically from the manifest order and exists only for whole-plan reading/audit.', '']
for rel in order:
    p=ROOT/rel
    parts += ['', '---', '', f'<!-- BEGIN MODULE: {rel} -->', '']
    if p.suffix.lower()=='.csv':
        parts += [f'## {rel}', '', '```csv', p.read_text(encoding='utf-8-sig').rstrip('\n'), '```']
    else:
        parts.append(rebase_links(p.read_text(encoding='utf-8').rstrip('\n'), rel))
    parts += ['', f'<!-- END MODULE: {rel} -->']
OUT.parent.mkdir(exist_ok=True)
OUT.write_text('\n'.join(parts).rstrip()+'\n',encoding='utf-8')
print(OUT)
