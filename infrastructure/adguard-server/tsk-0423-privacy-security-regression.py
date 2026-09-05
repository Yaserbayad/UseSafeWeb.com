#!/usr/bin/env python3
import argparse, copy, json, sys
from pathlib import Path

APPROVED_UPSTREAM=['https://dns10.quad9.net/dns-query']
APPROVED_BOOTSTRAP=['9.9.9.10','149.112.112.10','2620:fe::10','2620:fe::fe:10']
APPROVED_FILTER='https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt'


def settings(doc):
    return doc.get('settings',doc)

def violations(doc):
    s=settings(doc); dns=s.get('dns') or {}; ecs=dns.get('edns_client_subnet') or {}
    q=s.get('querylog') or {}; st=s.get('statistics') or {}; fl=s.get('filtering') or {}
    http=s.get('http') or {}; active=[x.get('url') for x in (s.get('filters') or []) if x.get('enabled')]
    v=[]
    if q.get('enabled') is not False: v.append('query_logging')
    if q.get('file_enabled') is not False: v.append('file_logging')
    if st.get('enabled') is not False: v.append('identifiable_statistics')
    if dns.get('anonymize_client_ip') is not True: v.append('missing_anonymization')
    if bool(ecs.get('enabled')) or bool(ecs.get('use_custom')): v.append('ecs')
    if list(dns.get('upstream_dns') or []) != APPROVED_UPSTREAM or dns.get('upstream_dns_file') or (dns.get('fallback_dns') or []) or (dns.get('private_upstream') or []): v.append('wrong_upstream')
    if list(dns.get('bootstrap_dns') or []) != APPROVED_BOOTSTRAP: v.append('wrong_bootstrap')
    if http.get('address') != '127.0.0.1:3000': v.append('public_admin')
    if fl.get('protection_enabled') is not True or fl.get('filtering_enabled') is not True: v.append('filtering_disabled')
    if active != [APPROVED_FILTER] or (s.get('whitelist_filters') or []): v.append('unapproved_filters')
    if (s.get('user_rules') or []): v.append('unapproved_user_rules')
    if int(dns.get('ratelimit') or 0) != 20 or (dns.get('ratelimit_whitelist') or []): v.append('resolver_abuse_control')
    if dns.get('refuse_any') is not True: v.append('public_recursive_any')
    binds=list(dns.get('bind_hosts') or [])
    if binds != ['127.0.0.1']: v.append('public_plain_dns_bind')
    return sorted(set(v))

def load(path):
    p=Path(path)
    if p.suffix.lower() in ('.yaml','.yml'):
        import yaml
        return yaml.safe_load(p.read_text(encoding='utf-8')) or {}
    return json.loads(p.read_text(encoding='utf-8'))

def negative(base):
    s=settings(base)
    cases=[]
    def add(name,fn):
        d=copy.deepcopy(base); fn(settings(d)); cases.append((name,d))
    add('query_logging',lambda x:x['querylog'].__setitem__('enabled',True))
    add('file_logging',lambda x:x['querylog'].__setitem__('file_enabled',True))
    add('identifiable_statistics',lambda x:x['statistics'].__setitem__('enabled',True))
    add('missing_anonymization',lambda x:x['dns'].__setitem__('anonymize_client_ip',False))
    add('ecs',lambda x:x['dns']['edns_client_subnet'].__setitem__('enabled',True))
    add('wrong_upstream',lambda x:x['dns'].__setitem__('upstream_dns',['https://dns.google/dns-query']))
    add('wrong_bootstrap',lambda x:x['dns'].__setitem__('bootstrap_dns',['8.8.8.8']))
    add('public_admin',lambda x:x['http'].__setitem__('address','0.0.0.0:3000'))
    add('filtering_disabled',lambda x:x['filtering'].__setitem__('filtering_enabled',False))
    add('unapproved_filters',lambda x:x['filters'].append({'enabled':True,'name':'unsafe','url':'https://example.invalid/list.txt'}))
    add('unapproved_user_rules',lambda x:x.__setitem__('user_rules',['||example.invalid^']))
    add('resolver_abuse_control',lambda x:x['dns'].__setitem__('ratelimit',0))
    add('public_recursive_any',lambda x:x['dns'].__setitem__('refuse_any',False))
    add('public_plain_dns_bind',lambda x:x['dns'].__setitem__('bind_hosts',['0.0.0.0']))
    for name,d in cases:
        got=violations(d)
        if name not in got: raise SystemExit(f'negative fixture accepted: {name}; got={got}')
        print(f'NEGATIVE_{name.upper()}=REJECTED')
    print(f'TSK0423_NEGATIVE_MATRIX=PASS count={len(cases)}')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--config',required=True); ap.add_argument('--negative-matrix',action='store_true')
    a=ap.parse_args(); d=load(a.config); v=violations(d)
    if v: raise SystemExit('TSK0423_REGRESSION=FAIL '+','.join(v))
    print('TSK0423_REGRESSION=PASS')
    if a.negative_matrix: negative(d)
if __name__=='__main__': main()
