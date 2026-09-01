import subprocess
from pathlib import Path

EXPECTED = {
    'brand/identity/TSK-0301/README.md': 'b8ffd2ed234465a238558a7b94e56274de49696a',
    'brand/guidelines/TSK-0297/README.md': '89e915678e85f7f301e8fa4b05c335cd803dd9d4',
    'prototype/TSK-0333/index.html': '9395f0e105d20683b5beafa01b02d7b300e79a8d',
    'prototype/TSK-0333/model.mjs': '9b7c239024d8ae24371b687aa39de6fa6b2b62b6',
    'prototype/TSK-0333/app.mjs': '476ea932d95592fabf586f7ba381be0d346117fe',
}
TARGETS = [Path('prototype/TSK-0333/index.html'), Path('prototype/TSK-0333/model.mjs'), Path('prototype/TSK-0333/app.mjs')]

def blob(path):
    return subprocess.check_output(['git','rev-parse',f'HEAD:{path}'], text=True).strip()

def req(cond, msg):
    if not cond:
        raise SystemExit(msg)

for path, expected in EXPECTED.items():
    req(blob(path) == expected, f'TSK0333_BRAND_INPUT_STALE={path}')
identity = Path('brand/identity/TSK-0301/README.md').read_text(encoding='utf-8')
req('visible product/brand name is exactly **SafeWeb**' in identity, 'TSK0333_IDENTITY_AUTHORITY_MISSING')
req('do not render `UseSafeWeb`' in identity, 'TSK0333_IDENTITY_PROHIBITION_MISSING')

changed = 0
for path in TARGETS:
    text = path.read_text(encoding='utf-8')
    count = text.count('UseSafeWeb')
    req(count > 0, f'TSK0333_EXPECTED_VISIBLE_NAME_NOT_FOUND={path}')
    text = text.replace('UseSafeWeb', 'SafeWeb')
    req('UseSafeWeb' not in text, f'TSK0333_VISIBLE_NAME_REMAINS={path}')
    path.write_text(text, encoding='utf-8')
    changed += count

combined = '\n'.join(p.read_text(encoding='utf-8') for p in TARGETS)
req('dns.usesafeweb.com' in combined, 'TSK0333_ANDROID_ENDPOINT_CHANGED')
req('https://dns.usesafeweb.com/dns-query' in combined, 'TSK0333_IPHONE_ENDPOINT_CHANGED')
req('SafeWeb' in combined, 'TSK0333_SAFEWEB_NAME_MISSING')
print(f'TSK0333_BRAND_REPLACEMENTS={changed}')
print('TSK0333_SAFEWEB_BRAND_FIX=PASS')
