from __future__ import annotations
import csv
import re
import subprocess
from pathlib import Path

ROOT = Path.cwd()

def read(path: str) -> str:
    return (ROOT / path).read_text(encoding='utf-8')

def blob(path: str) -> str:
    return subprocess.check_output(['git','hash-object',path], text=True).strip()

def row_with_prefix(path: str, prefix: str) -> str:
    matches=[line for line in read(path).splitlines() if line.startswith(prefix)]
    assert len(matches)==1, (path,prefix,len(matches))
    return matches[0]

# Canonical task and gate authority.
wbs='Plans/Master/WBS/master-wbs.csv'
assert blob(wbs)=='b57104a71ab814d0f67e7fb8b0fd388d1f6aacfa', blob(wbs)
with open(wbs, newline='', encoding='utf-8-sig') as f:
    rows=list(csv.DictReader(f))
rows52=[r for r in rows if r.get('Task_ID')=='TSK-0052']
assert len(rows52)==1
r=rows52[0]
assert r.get('AI_Capability')=='A4', r.get('AI_Capability')
assert r.get('Action_Authority')=='AUTO_ALLOWED', r.get('Action_Authority')
deps={x.strip() for x in (r.get('Dependencies') or '').split(';') if x.strip()}
assert deps=={'TSK-0043','TSK-0321','TSK-0309','TSK-0628'}, deps
acc=r.get('Acceptance_Criteria') or ''
for phrase in ['dual-mode baseline','accountless core','optional parent account','Google sign-in/session','lightweight dashboard/device management','account/device deletion/recovery','accessibility/i18n','self-service','traceability','no real-user evidence']:
    assert phrase in acc, phrase

gates='Plans/Master/Registers/GATES.md'
assert blob(gates)=='87cf9060954a82e1d5a092200d3c922f1986a5da', blob(gates)
lg06=row_with_prefix(gates,'| LG-06 |')
for phrase in ['Product, Brand and Experience Freeze','dual-mode Version-1','account/session/dashboard/device lifecycle','accountless-core availability','brand/design system','self-service','content','accessibility/i18n','privacy/security boundaries','unresolved risks','AUTO_ALLOWED inside frozen scope','Automatically unlocks L5 only']:
    assert phrase in lg06, phrase

decisions='Plans/Master/Registers/DECISIONS_TRIGGERS.md'
assert blob(decisions)=='380ff579dcffb7b8df73611e9159c672f9ed489e', blob(decisions)
d53=row_with_prefix(decisions,'| DEC-0053 |')
d54=row_with_prefix(decisions,'| DEC-0054 |')
for phrase in ['optional parent account','complete core safety setup/protection journey remains usable without login','Mandatory login','browsing/activity history','child accounts','unrestricted DNS administration']:
    assert phrase in d53, phrase
for phrase in ['AI may accept project-defined material residual risk','LG-07 is evidence-driven AUTO','higher actual legal/safety/security/platform/technical reality always controls']:
    assert phrase in d54, phrase

# Runtime must show current direct predecessors and supporting changed-scope evidence.
state=read('CURRENT_STATE.md')
for heading in [
    '## TSK-0140 current accepted stable state — 2026-08-31 — POST-CR-0007',
    '## TSK-0141 current accepted stable state — 2026-08-30 — POST-CR-0006',
    '## TSK-0146 current accepted stable state — 2026-08-30 — POST-CR-0006',
    '## TSK-0229 current accepted stable state — 2026-08-30 — POST-CR-0006',
    '## TSK-0312 current accepted stable state — 2026-08-31',
    '## TSK-0142 current accepted stable state — 2026-08-31',
    '## TSK-0329 current accepted stable state — 2026-08-31 — POST-CR-0007',
    '## TSK-0332 current accepted stable state — 2026-08-31 — POST-CR-0007',
    '## TSK-0331 current accepted stable state — 2026-08-31 — POST-CR-0007',
    '## TSK-0333 current accepted stable state — 2026-09-01 — POST-CR-0007',
    '## TSK-0324 current accepted stable state — 2026-09-01 — POST-CR-0007',
    '## TSK-0321 current accepted stable state — 2026-09-01 — POST-CR-0007',
    '## TSK-0145 current accepted stable state — 2026-09-01 — POST-CR-0006/0007',
    '## TSK-0043 current accepted stable state — 2026-09-01 — POST-CR-0006/0007',
    '## TSK-0309 current accepted stable state — 2026-09-01 — POST-CR-0006/0007',
    '## TSK-0628 current accepted stable state — 2026-09-01 — POST-CR-0006/0007',
]:
    assert heading in state, heading
assert '`TSK-0052 / LG-06` remains **non-PASS**' in state
assert '## TSK-0052 / LG-06 current accepted stable state' not in state

# Current exact product/browser sources and current final accessibility evidence.
expected={
    'prototype/TSK-0333/index.html':'934dc19d00cc9dd32e1ebc20c604373d153d4013',
    'prototype/TSK-0333/model.mjs':'fc25e4b1facc303840311e8ce186612eb8799212',
    'prototype/TSK-0333/app.mjs':'98659ba74a86d539b89664708bbcb830292486f8',
    'prototype/TSK-0333/prototype.css':'385dc5269de79b7baca9aa597b9ecf4cca8a95f2',
    'TSK_0321_POST_CR0007_FINAL_ACCESSIBILITY_EVIDENCE_2026-09-01.md':'433800f2fd4a54c1fba2c42826579675df20bd75',
    'TSK_LG06_PREDECESSOR_CURRENT_REQUALIFICATION_EVIDENCE_2026-09-01.md':'e17f0128045091a500c9ad89a9334c51732109ff',
}
for p,sha in expected.items():
    assert blob(p)==sha,(p,blob(p),sha)

# Still-valid unchanged L4 brand/content/localization authorities are pinned and bridged by current dual-mode consumers.
unchanged={
    'brand/identity/TSK-0301/README.md':'b8ffd2ed234465a238558a7b94e56274de49696a',
    'brand/system/TSK-0300/tokens.css':'cd7d9a7cd5109e1ff0baa76532495dfd7a27a70f',
    'brand/system/TSK-0300/components.css':'831e92a74b6dda04252d93242cb33bd491a02381',
    'brand/guidelines/TSK-0297/README.md':'89e915678e85f7f301e8fa4b05c335cd803dd9d4',
    'TSK_0307_SOURCE_BACKED_INSTRUCTION_CONTENT_CATALOGUE_2026-08-28.md':'d717c9b3f66197abe1f3e73361633f222b817e7c',
    'TSK_0311_LOCALIZATION_CONTENT_ARCHITECTURE_2026-08-29.md':'ef746d64c7878eb7d0f1b8fdf2356721728041c4',
    'TSK_0559_FIRST_PHONE_CONTENT_QUALITY_SOURCE_UPDATE_PRUNING_STANDARD_2026-08-28.md':'b2039d48e2356c0ea37fafe4fadc59d065cca6c8',
    'prototype/TSK-0324/UI_COMPONENT_RULES.md':'8747acdf6e0e98f91e8327b7225bd954956aaef1',
}
for p,sha in unchanged.items():
    assert blob(p)==sha,(p,blob(p),sha)
index=read('prototype/TSK-0333/index.html')
assert '../../brand/system/TSK-0300/tokens.css' in index
assert '../../brand/system/TSK-0300/components.css' in index
assert 'SafeWeb' in index and '>UseSafeWeb<' not in index

# Current review must explicitly close every LG-06 category without erasing later risks/obligations.
review=read('TSK_0052_LG06_CURRENT_DUAL_MODE_FREEZE_REVIEW_2026-09-01.md')
for phrase in [
    'CANDIDATE PASS — independent verification and stable-state reconciliation required before PASS',
    'Frozen Version-1 product/non-goals',
    'Requirements and traceability',
    'Critical conflicts',
    'Accountless core setup / Protection Map / recovery',
    'Optional sign-in/account/session',
    'Minimum ownership persistence + dashboard/device management',
    'Account/device deletion, revoke, replacement and recovery',
    'Privacy/security/truth boundaries',
    'Brand / identity / design system',
    'Content / source currency / support content',
    'Accessibility / responsive / i18n',
    'Self-service / no routine human support',
    'Pre-L8 human-evidence rule',
    '`RSK-0002`', '`RSK-0005`', '`RSK-0015`', '`RSK-0017`', '`RSK-0022`',
    'Deferred legal/compliance facts under DEC-0049 remain unresolved facts, not PASS or waiver',
    'unlock **L5 architecture/security/privacy/delivery readiness work only**',
]:
    assert phrase in review, phrase
assert review.count('**Satisfied**')>=12
assert 'prior 2026-08-30 LG-06 readiness conclusion is superseded' in review

# Risk register must preserve the named downstream/open risks rather than silently close them.
risks=read('Plans/Master/Registers/RISKS.md')
for prefix in ['| RSK-0002 |','| RSK-0005 |','| RSK-0015 |','| RSK-0017 |','| RSK-0022 |']:
    assert prefix in risks, prefix
assert 'not a pre-product blocker' in row_with_prefix('Plans/Master/Registers/RISKS.md','| RSK-0002 |')
assert 'Open — expanded by dashboard amendment' in row_with_prefix('Plans/Master/Registers/RISKS.md','| RSK-0015 |')
assert 'Open — unvalidated software experience' in row_with_prefix('Plans/Master/Registers/RISKS.md','| RSK-0022 |')

print('TSK0052_DIRECT_PREDECESSORS_CURRENT PASS')
print('LG06_PRODUCT_SCOPE_NON_GOALS PASS')
print('LG06_REQUIREMENTS_TRACEABILITY_CONFLICTS PASS')
print('LG06_DUAL_MODE_JOURNEYS PASS')
print('LG06_BRAND_CONTENT_ACCESSIBILITY_I18N PASS')
print('LG06_SELF_SERVICE_PRIVACY_TRUTH PASS')
print('LG06_RESIDUAL_RISK_AND_LEGAL_FENCES PASS')
print('TSK0052_LG06_CURRENT_EVIDENCE_REVIEW PASS')
