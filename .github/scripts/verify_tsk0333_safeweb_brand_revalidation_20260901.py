import csv
import subprocess
from pathlib import Path

FIX_COMMIT='e5ce4b6b9e71b9b06226e1a0b74cdd6a688d107b'
EXPECTED={
'brand/identity/TSK-0301/README.md':'b8ffd2ed234465a238558a7b94e56274de49696a',
'brand/guidelines/TSK-0297/README.md':'89e915678e85f7f301e8fa4b05c335cd803dd9d4',
'Plans/Master/WBS/master-wbs.csv':'f3c29b5db8b835ef2c896f61335656ea51d8ba1c',
'Plans/Master/RELATIONSHIP_INDEX.yaml':'c108d2c162bcea2ee4cc01def46d0487a9501032',
'prototype/TSK-0333/index.html':'934dc19d00cc9dd32e1ebc20c604373d153d4013',
'prototype/TSK-0333/model.mjs':'fc25e4b1facc303840311e8ce186612eb8799212',
'prototype/TSK-0333/app.mjs':'98659ba74a86d539b89664708bbcb830292486f8',
'prototype/TSK-0333/prototype.css':'6f8af459a0b0b1c9ec132657dfcd7ebff43090b8',
}
OLD={
'prototype/TSK-0333/index.html':'9395f0e105d20683b5beafa01b02d7b300e79a8d',
'prototype/TSK-0333/model.mjs':'9b7c239024d8ae24371b687aa39de6fa6b2b62b6',
'prototype/TSK-0333/app.mjs':'476ea932d95592fabf586f7ba381be0d346117fe',
}

def req(c,m):
    if not c: raise SystemExit(m)
def head_blob(p):
    return subprocess.check_output(['git','rev-parse',f'HEAD:{p}'],text=True).strip()
def show(spec):
    return subprocess.check_output(['git','show',spec],text=True)

for p,h in EXPECTED.items(): req(head_blob(p)==h,f'TSK0333_BRAND_BLOB_MISMATCH={p}')
print('TSK0333_BRAND_CURRENT_BLOBS=PASS')

identity=Path('brand/identity/TSK-0301/README.md').read_text(encoding='utf-8')
guidelines=Path('brand/guidelines/TSK-0297/README.md').read_text(encoding='utf-8')
req('visible product/brand name is exactly **SafeWeb**' in identity,'TSK0333_BRAND_IDENTITY_MISSING')
req('do not render `UseSafeWeb`' in identity,'TSK0333_BRAND_PROHIBITION_MISSING')
req('visible brand is exactly `SafeWeb`' in guidelines,'TSK0333_BRAND_GUIDELINE_MISSING')
print('TSK0333_BRAND_AUTHORITY=PASS')

for p,old_blob in OLD.items():
    req(subprocess.check_output(['git','rev-parse',f'{FIX_COMMIT}^:{p}'],text=True).strip()==old_blob,f'TSK0333_BRAND_PARENT_BLOB_MISMATCH={p}')
    before=show(f'{FIX_COMMIT}^:{p}')
    after=Path(p).read_text(encoding='utf-8')
    req(before.count('UseSafeWeb')>0,f'TSK0333_BRAND_OLD_NAME_ABSENT={p}')
    req(before.replace('UseSafeWeb','SafeWeb')==after,f'TSK0333_BRAND_NOT_PURE_REPLACEMENT={p}')
    req('UseSafeWeb' not in after,f'TSK0333_BRAND_OLD_NAME_REMAINS={p}')
print('TSK0333_BRAND_PURE_SUBSTITUTION=PASS')

combined='\n'.join(Path(p).read_text(encoding='utf-8') for p in OLD)
req('dns.usesafeweb.com' in combined,'TSK0333_BRAND_ANDROID_ENDPOINT_MISSING')
req('https://dns.usesafeweb.com/dns-query' in combined,'TSK0333_BRAND_IPHONE_ENDPOINT_MISSING')
req('SafeWeb' in combined,'TSK0333_BRAND_SAFEWEB_MISSING')
print('TSK0333_BRAND_ENDPOINT_FENCE=PASS')

with Path('Plans/Master/WBS/master-wbs.csv').open(encoding='utf-8-sig',newline='') as f:
    row=next(r for r in csv.DictReader(f) if r['Task_ID']=='TSK-0333')
req(row['Action_Authority']=='AUTO_ALLOWED' and row['AI_Capability_A0_A4']=='A3','TSK0333_BRAND_AUTH_CHANGED')
req(row['Dependencies']=='TSK-0335; TSK-0334; TSK-0146; TSK-0331','TSK0333_BRAND_DEP_CHANGED')
print('TSK0333_BRAND_WBS_CONTRACT=PASS')
print('TSK0333_SAFEWEB_BRAND_REVALIDATION=PASS')
