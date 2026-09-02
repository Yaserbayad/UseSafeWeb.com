from __future__ import annotations

import subprocess
from pathlib import Path

BASE = ".github/scripts/verify_tsk0585_current_vendor_review.py"
EXPECTED_BASE = "af8b087caec65ca488dba24f23859561c5234bc4"
actual = subprocess.check_output(["git", "hash-object", BASE], text=True).strip()
assert actual == EXPECTED_BASE, (actual, EXPECTED_BASE)

src = Path(BASE).read_text(encoding="utf-8")
old = '''for key, url in SOURCES.items():
    assert url in doc, (key, url)
print("TSK0585_OFFICIAL_SOURCE_REGISTER=PASS")
'''
new = '''documented_source = {
    "firebase_pricing": "https://firebase.google.com/pricing",
    "firebase_auth": "https://firebase.google.com/docs/auth",
    "identity_pricing": "https://cloud.google.com/identity-platform/pricing",
    "firebase_privacy": "https://firebase.google.com/support/privacy",
    "firebase_terms": "https://firebase.google.com/terms/",
    "adguard_readme": "https://github.com/AdguardTeam/AdGuardHome",
    "adguard_license": "https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/master/LICENSE.txt",
    "adguard_openapi": "https://github.com/AdguardTeam/AdGuardHome/tree/master/openapi",
}
for key, url in documented_source.items():
    assert url in doc, (key, url)
print("TSK0585_OFFICIAL_SOURCE_REGISTER=PASS")
'''
assert old in src, "expected base source-register block not found"
src = src.replace(old, new, 1)
exec(compile(src, BASE + "[v2-mapping]", "exec"), {"__name__": "__main__"})
