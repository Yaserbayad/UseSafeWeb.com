#!/usr/bin/env python3
import csv,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
WBS=ROOT/'Plans/Master/WBS/master-wbs.csv'
STATE=ROOT/'CURRENT_STATE.md'
ART=ROOT/'TSK_0237_VENDOR_VERSION_PRICE_TERMS_COMPATIBILITY_MONITORING_TRIGGERS_2026-09-02.md'

def req(c,m):
    if not c: raise AssertionError(m)

def current_pass(text,tid):
    pats=[rf'^##+\s+{re.escape(tid)}\s+current accepted stable state[^\n]*$',rf'^##+\s+{re.escape(tid)}\s+accepted stable state[^\n]*$']
    starts=[]
    for p in pats: starts += [m.start() for m in re.finditer(p,text,re.M|re.I)]
    if not starts:return False
    s=max(starts);e=text.find('\n## ',s+3);e=len(text) if e<0 else e
    sec=text[s:e]
    return '**PASS**' in sec or ': **PASS**' in sec or '`: **PASS**' in sec

def main():
    with WBS.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
    row=next(r for r in rows if r['Task_ID']=='TSK-0237')
    state=STATE.read_text(encoding='utf-8-sig')
    req(row['Lifecycle_Stage']=='L5','lifecycle changed')
    req(row['Dependencies'].strip()=='TSK-0586; TSK-0539; TSK-0585','dependencies changed')
    req(row['Action_Authority']=='AUTO_ALLOWED' and row['AI_Capability_A0_A4']=='A4','authority/capability changed')
    for d in ['TSK-0586','TSK-0539','TSK-0585']: req(current_pass(state,d),f'{d} not current PASS')
    text=ART.read_text(encoding='utf-8'); low=text.lower()
    req(text.count('| F-')>=6,'missing Firebase trigger classes')
    req(text.count('| G-')>=2,'missing Google OAuth trigger classes')
    req(text.count('| A-')>=7,'missing AdGuard trigger classes')
    required=[
      'owner','cadence','signal / threshold','verification','safe response','migration / retest path','gate/state reopening rule',
      'auth quota','price/free-tier','session semantics','firebase auth api/provider','gis/oauth browser/flow','scope expansion','terms page','subprocessor register',
      'adguard stable release','openapi breaking/deprecation','privacy/security default','security advisory','adguard license','platform compatibility',
      'before every release candidate / production activation','weekly','daily or event-driven','monthly','>=70%',
      'https://firebase.google.com/pricing','https://firebase.google.com/docs/auth/limits','https://firebase.google.com/docs/auth/admin/manage-cookies','https://firebase.google.com/terms','https://cloud.google.com/terms/subprocessors',
      'https://developers.google.com/identity/gsi/web/reference/release-notes','https://github.com/adguardteam/adguardhome/blob/master/openapi/openapi.yaml','https://github.com/adguardteam/adguardhome/blob/master/openapi/changelog.md','https://github.com/adguardteam/adguardhome/security',
      'accountless core','no automatic plan upgrade/spend','do not auto-upgrade production','typed allowlisted adapter','owner_external','no ai legal conclusion','no legal pass inference'
    ]
    for x in required:req(x in low,f'missing TSK-0237 acceptance element: {x}')
    trigger_lines=[l for l in text.splitlines() if re.match(r'^\| [FGA]-[A-Z]+-\d+',l)]
    req(len(trigger_lines)>=15,'insufficient trigger rows')
    for l in trigger_lines:
        req(l.count('|')>=8,f'incomplete trigger row: {l[:60]}')
    print(f'PASS: TSK-0237 operating design contains {len(trigger_lines)} vendor monitoring triggers with owners/cadence/signals/thresholds, verification, safe response, retest and reopening rules.')
if __name__=='__main__':main()
