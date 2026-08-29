#!/usr/bin/env python3
from pathlib import Path
import csv, hashlib, io, re, subprocess

ROOT = Path('Plans/Master')
PLANS = Path('Plans')
WBS = ROOT / 'WBS/master-wbs.csv'

DECISION = 'DEC-0052'
CHANGE = 'CR-0005'
STAMP = '2026-08-29'
OWNER_BASIS = 'Explicit Project Owner instruction 2026-08-29: no parent/user/participant validation or testing before a fully working integrated product; first real-user testing occurs only after integrated product readiness.'


def read(path):
    return Path(path).read_text(encoding='utf-8')


def write(path, text):
    Path(path).write_text(text, encoding='utf-8')


def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected exactly one occurrence, found {n}')
    return text.replace(old, new, 1)


def table_row_update(path, key, updates):
    p = Path(path)
    lines = p.read_text(encoding='utf-8').splitlines()
    hits = 0
    out = []
    for line in lines:
        if line.startswith(f'| {key} |'):
            hits += 1
            parts = [x.strip() for x in line.split('|')]
            for index, value in updates.items():
                parts[index] = value
            line = '| ' + ' | '.join(parts[1:-1]) + ' |'
        out.append(line)
    if hits != 1:
        raise SystemExit(f'{path}:{key}: expected one row, found {hits}')
    p.write_text('\n'.join(out) + '\n', encoding='utf-8')


def append_unique(path, marker, block):
    p = Path(path)
    text = p.read_text(encoding='utf-8')
    if marker in text:
        raise SystemExit(f'{path}: marker already present: {marker}')
    p.write_text(text.rstrip() + '\n' + block.rstrip() + '\n', encoding='utf-8')


with WBS.open(encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)
if not fieldnames:
    raise SystemExit('WBS has no header')
by = {r['Task_ID']: r for r in rows}
if len(by) != len(rows):
    raise SystemExit('WBS duplicate Task_ID')

excluded = {r['Task_ID'] for r in rows if r['Lifecycle_Stage'] == 'L3'} | {'TSK-0187','TSK-0326','TSK-0336'}
if len({r['Task_ID'] for r in rows if r['Lifecycle_Stage'] == 'L3'}) != 31:
    raise SystemExit('Expected 31 L3 tasks before CR-0005')
if len(excluded) != 34:
    raise SystemExit(f'Expected 34 excluded tasks, got {len(excluded)}')

exclusion_note = (
    'DEC-0052/CR-0005: pre-product parent/user/participant validation is excluded from the active path. '
    'Plan_Status=NOT_APPLICABLE + Execution_State=PASS verifies this exclusion only; the task was not executed and no behavioral/user evidence is inferred. '
    'Actual human/user validation begins only after LG-09 PASS in L8 Controlled Integrated-Product Pilot.'
)
for tid in excluded:
    r = by[tid]
    r['Plan_Status'] = 'NOT_APPLICABLE'
    r['Execution_State'] = 'PASS'
    r['Critical_Path'] = 'NO'
    r['Trigger'] = 'Not applicable to the active pre-product path under DEC-0052/CR-0005; human/user testing begins only after LG-09 PASS in L8.'
    r['Preconditions'] = 'Owner exclusion decision DEC-0052 is current; no task execution or participant evidence is required for this excluded pre-product work.'
    r['Next_Action'] = 'No execution. Preserve as excluded historical pre-product validation work; use the L8 controlled integrated-product pilot for actual human/user validation.'
    ev = (r.get('Evidence_Reference') or '').strip()
    tag = 'DEC-0052; CR-0005; owner instruction 2026-08-29'
    r['Evidence_Reference'] = (ev + '; ' + tag).strip('; ') if tag not in ev else ev
    notes = (r.get('Notes') or '').strip()
    r['Notes'] = (notes + (' ' if notes else '') + exclusion_note).strip()

by['TSK-0024']['Acceptance_Criteria'] = (
    'Before LG-07, reject implementation outside the owner-authorised integrated-product-first sequence. Under DEC-0052/CR-0005, '
    'real parent/user/participant testing is not required before LG-09; L6 build still requires LG-06 and LG-07 PASS. The active baseline is accountless-first: '
    'no mandatory UseSafeWeb account, auth vendor, persistent parent identity/dashboard, or customer-facing AdGuard control plane. Optional persistence/account/dashboard '
    'may activate only through EXC-0001 with validated need and owner approval; surveillance/activity history, child accounts, broad DNS administration, GROW automation, '
    'native app, school portal, paid-acquisition system, and complex safety paywalls remain excluded unless separately authorised.'
)
by['TSK-0024']['Notes'] += ' CR-0005/DEC-0052 supersedes the earlier pre-build behavioral-validation ordering; technical/product/security/privacy gates remain mandatory.'

by['TSK-0052']['Acceptance_Criteria'] = (
    'LG-06 passes only if the accountless minimum product/non-goals, requirements, setup/Protection-Map journey, brand/design system, content, accessibility/i18n, '
    'self-service behavior and traceability are frozen and internally/automatically accepted to the current L4 contract; optional persistence/account/dashboard remains EXC-0001 '
    'and critical conflicts are resolved. Under DEC-0052 no real-user/participant evidence is required before this gate and none may be inferred; human validation begins after LG-09 in L8.'
)
by['TSK-0052']['Notes'] += ' CR-0005/DEC-0052 makes LG-05/L3 human evidence non-required for the active product-first LG-06 decision.'

by['TSK-0139']['Title'] = 'Translate integrated-product-first owner authorization into authorised product outcomes'
by['TSK-0139']['Acceptance_Criteria'] = (
    'Mandate identifies the current job assumption, target user, required outcome, current owner/product/technical/synthetic evidence basis, unresolved risks/constraints/stop conditions, '
    'and authorised L4 definition/design scope under DEC-0052. Human validation is intentionally scheduled only after LG-09 in L8; the mandate must not claim pre-product behavioral validation, '
    'public-launch authorization, or bypass applicable product, architecture, security, privacy, build, or release gates.'
)
by['TSK-0139']['Notes'] = 'CR-0005/DEC-0052 rebaselines this task as the owner-authorized integrated-product-first L4 entry. Pre-product human/user testing is not required and no behavioral validation is inferred.'

by['TSK-0141']['Acceptance_Criteria'] = (
    'Every included capability maps to a current need assumption, mandatory operation/safety requirement, or explicit owner-approved architectural/product decision. The first-product scope remains '
    'accountless-first and minimum; mandatory authentication, persistent parent dashboard and customer-facing AdGuard control plane remain deferred under EXC-0001, while surveillance/activity history, '
    'child accounts and other advanced capabilities remain excluded unless separately reauthorised. No capability may be described as behaviorally/user validated before the L8 controlled integrated-product pilot.'
)
by['TSK-0141']['Notes'] += ' CR-0005/DEC-0052 authorizes product-first progression through L4-L7 without pre-product human testing; no behavioral evidence is invented.'

by['TSK-0298']['Acceptance_Criteria'] = (
    'Brief is traceable to current accepted owner/customer/product evidence and non-surveillance/claims constraints; it is approved before identity finalization. '
    'Under DEC-0052, post-integration human validation is scheduled for L8 and no pre-product behavioral validation is required or implied.'
)
by['TSK-0298']['Notes'] = 'CR-0005/DEC-0052 supersedes CR-0004 sequencing: this accepted internal Brand/UX/prototype work may support product build; actual human/user validation begins in L8 after LG-09.'

by['TSK-0299']['Acceptance_Criteria'] = (
    'Verbal system follows plain-language, child-aware, non-alarmist, non-technical design rules for parent-facing use, conforms to current approved claims/non-surveillance constraints, '
    'and is reusable across surfaces/locales. Under DEC-0052, human comprehension validation occurs only after integrated-product readiness in L8; no pre-product human validation or deferred legal completion is implied.'
)
by['TSK-0299']['Notes'] = 'CR-0005/DEC-0052: internal verbal-system conformance supports build; actual human/user comprehension validation is reserved for L8 after LG-09.'

by['TSK-0309']['Title'] = 'Freeze the implementation-ready experience baseline from current internal and automated acceptance evidence'
by['TSK-0309']['Purpose'] = 'Correct and verify the representative prototype using current internal, automated, browser/device, accessibility, truth-state, recovery/removal and claims evidence, then freeze the implementation-ready experience baseline without requiring pre-product human testing.'
by['TSK-0309']['Acceptance_Criteria'] = (
    'Material internally or automatically observed functional, truth-state, responsive, accessibility, recovery/removal, claims, and interaction defects have root cause/disposition; '
    'all critical/high pre-product defects are corrected and retested; speculative features are excluded. No real-user comprehension claim is required or inferred before L8.'
)
by['TSK-0309']['Notes'] = 'CR-0005/DEC-0052: TSK-0187 remains an excluded dependency record (NOT_APPLICABLE+PASS), not behavioral evidence. TSK-0309 is accepted from internal/automated target-environment evidence before build.'

by['TSK-0327']['Acceptance_Criteria'] = (
    'All critical/high findings from current internal/automated functional, trust-state, accessibility, responsive and recovery review are fixed or formally accepted by the owner with rationale; '
    'retest evidence confirms critical paths, truthful Protection Map state semantics and accessibility. No human comprehension claim is required or inferred before L8.'
)
by['TSK-0327']['Verification_Method'] = 'Review the approved brief, claims, accessibility, source currency, current automated/internal findings, and representative technical task checks; retain reproducible retest evidence.'
by['TSK-0327']['Notes'] += ' CR-0005/DEC-0052: pre-product human usability/comprehension testing is excluded; use internal/automated evidence until L8.'

by['TSK-0335']['Acceptance_Criteria'] = (
    'Prototype never labels parent confirmation as verification, exposes material gaps at the right time, supports deterministic internal/automated truth-state checks, and preserves the interaction points needed for later L8 human comprehension validation.'
)
by['TSK-0335']['Notes'] += ' CR-0005/DEC-0052 reserves actual human comprehension testing for L8 after LG-09.'

by['TSK-0399']['Title'] = 'Prove the accountless new-user path can discover, start, configure, verify, understand, recover/remove, and finish without login, card, or persistent identity'
by['TSK-0399']['Notes'] = 'CR-0005/DEC-0052: this L7 task is target-device/network technical acceptance using simulated/automated new-user paths; it does not require or imply real-parent testing before LG-09.'

buf = io.StringIO(newline='')
writer = csv.DictWriter(buf, fieldnames=fieldnames, lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
writer.writeheader(); writer.writerows(rows)
WBS.write_text(buf.getvalue(), encoding='utf-8')

ver_path = ROOT/'Registers/VERIFICATION_EVIDENCE_ACCEPTANCE.md'
ver_lines = ver_path.read_text(encoding='utf-8').splitlines()
affected_for_ver = excluded | {'TSK-0024','TSK-0052','TSK-0139','TSK-0141','TSK-0298','TSK-0299','TSK-0309','TSK-0327','TSK-0335','TSK-0399'}

def md(v):
    return (v or '').replace('\\','\\\\').replace('|','\\|').replace('\n',' ').strip()
repl = {}
for tid in affected_for_ver:
    r = by[tid]
    repl[tid] = f"| {tid} | {md(r['Verification_ID'])} | {md(r['Verification_Method'])} | {md(r['Evidence_ID'])} | {md(r['Evidence_Required'])} | {md(r['Acceptance_ID'])} | {md(r['Acceptance_Criteria'])} | {md(r['Execution_State'])} |"
seen=set(); out=[]
for line in ver_lines:
    m=re.match(r'^\| (TSK-\d{4}) \|', line)
    if m and m.group(1) in repl:
        tid=m.group(1); line=repl[tid]; seen.add(tid)
    out.append(line)
missing=affected_for_ver-seen
if missing:
    raise SystemExit('Verification register missing rows: '+','.join(sorted(missing)))
ver_path.write_text('\n'.join(out)+'\n', encoding='utf-8')

dec_path=ROOT/'Registers/DECISIONS_TRIGGERS.md'
table_row_update(dec_path, 'DEC-0009', {4:'ACTIVE product-shape decision under DEC-0052 — accountless-first public/setup product with native safeguards first, real AdGuard baseline, one relevant service, truthful Protection Map and quiet completion; pre-product Experiment-1 is no longer an active sequencing prerequisite and human validation starts in L8.'})
table_row_update(dec_path, 'DEC-0019', {4:'Historical MODIFY outcome retained; downstream pre-build validation sequencing is superseded by DEC-0052.'})
table_row_update(dec_path, 'DEC-0020', {4:'SUPERSEDED for active pre-product sequencing by DEC-0052; retained as historical Experiment-1 protocol only.'})
table_row_update(dec_path, 'DEC-0024', {
    4:'SUPERSEDED FOR SEQUENCING by DEC-0052 — integrated product build no longer waits for pre-product behavioral validation; L6 still requires LG-06 and LG-07 PASS.',
    5:'Owner override 2026-08-29.',
    6:'Current L4/L5 product, architecture, security, privacy, delivery and acceptance evidence plus LG-06/LG-07; no real-user evidence is required before build. Human validation begins only after LG-09 in L8.'
})
table_row_update(dec_path, 'DEC-0050', {4:'SUPERSEDED by DEC-0052 for active sequencing; retained as historical deferral/change-control record.'})
table_row_update(dec_path, 'DEC-0051', {4:'SUPERSEDED by DEC-0052 for active sequencing; retained as historical provisional-decoupling record.'})
append_unique(dec_path, '| DEC-0052 |', f"""
| DEC-0052 | New | Integrated-product-first human validation sequencing | ACTIVE OWNER DECISION — no parent/user/participant validation, usability/comprehension study, recruitment, or other real-user testing is required or permitted as a pre-product gate; build and integrated technical/product verification proceed first, and actual human/user validation begins only after LG-09 PASS in L8. Pre-product human-validation tasks are excluded as NOT_APPLICABLE+PASS (exclusion verified, not implemented), not fabricated evidence. | Explicit Project Owner instruction 2026-08-29; supersedes DEC-0050/DEC-0051 sequencing and earlier pre-build behavioral assumptions. | WBS/gate/lifecycle re-sequencing; exact excluded-task disposition; no fabricated participant evidence; L4-L7 technical/product/accessibility/security/privacy/recovery/operational acceptance remains mandatory; LG-09 PASS precedes first L8 participant activation. | Project Owner | All L3 tasks; TSK-0187; TSK-0326; TSK-0336; TSK-0309; TSK-0327; TSK-0399; LG-03..LG-10 | {OWNER_BASIS}; {CHANGE} |
""")

cr_path=ROOT/'Registers/EXCEPTIONS_CHANGE_CONTROLS.md'
append_unique(cr_path, '| CR-0005 |', f"""
| CR-0005 | Project Owner | 2026-08-29 | Replace pre-product human/participant behavioral-validation sequencing with an integrated-product-first sequence: complete product definition, architecture, build and integrated technical/product verification before any parent/user/participant testing; actual human/user validation begins in L8 only after LG-09 PASS. | WBS planning/execution dispositions for all 31 L3 tasks plus TSK-0187/TSK-0326/TSK-0336; active acceptance semantics for TSK-0024/0052/0139/0141/0298/0299/0309/0327/0335/0399; LG-03..LG-10 sequencing; CON-0025; RSK-0002/RSK-0022; Layers 1/4/5; lifecycle/current-state interface; manifest/generated/checksums. Dependency edges are preserved because exclusion-PASS satisfies the historical predecessor record without fabricating execution. | Owner product strategy: no parent/user/participant validation before a fully working product; avoid blocking design/build on incomplete prototype studies while preserving rigorous automated/device/network/accessibility/security/privacy/recovery/operational verification. | Project Owner DEC-0052; actual safety/legal/security/platform reality remains higher authority. | Set affected pre-product human-validation tasks to NOT_APPLICABLE+PASS as verified exclusions; rebaseline LG-03/LG-04/LG-05 as inactive historical pre-product gates; allow LG-06 -> LG-07 -> LG-08 -> LG-09 progression without real-human evidence; preserve L8 as first real-user validation stage and LG-10/LG-11 as evidence/production-decision gates. No claim of behavioral validation is created. | Explicit owner reversal may reopen pre-product validation; restore affected task/gate semantics from the pre-CR-0005 Git history and re-run deterministic validation. | Rebuild generated plan; regenerate declared SHA-256s; run master validator; assert 641 tasks, 849 dependency edges, exactly 31 L3 plus TSK-0187/0326/0336 as NOT_APPLICABLE+PASS, no active pre-L8 human-validation blocker, and L8 pilot gates retained. GitHub commit/tree/blob read-back and CURRENT_STATE reconciliation required before further progression. | Pending canonical publication/read-back in the amendment execution; durable evidence and runtime state must record final commit/blobs. | ACTIVE — supersedes CR-0003/CR-0004 only for human-validation sequencing; legal hold/accountless/security/privacy/build/release/publication/launch authorities remain independently controlled. |
""")

gates=ROOT/'Registers/GATES.md'
table_row_update(gates, 'LG-03', {
    4:'Inactive historical pre-product participant-readiness gate under DEC-0052/CR-0005; retained only if the owner explicitly reopens a pre-product human study.',
    5:'Only if explicitly reopened: current applicable legal/privacy/participant, data-flow, notice, technical, recovery and incident evidence for that study.',
    6:'NOT_APPLICABLE ACTIVE PATH; if reopened: PASS; REWORK; DEFER; STOP',
    10:'No active pre-product unlock. Current product-first progression enters L4 under DEC-0052; real-user pilot readiness is governed by LG-09 after integrated product verification.'
})
table_row_update(gates, 'LG-04', {
    4:'Inactive historical pre-product experiment gate under DEC-0052/CR-0005; only applies if the owner explicitly reopens the retired pre-product study.',
    5:'Only if reopened: protocol, cohort, scripts, retention/deletion, incident/stop routes, technical acceptance and owner authorization.',
    6:'NOT_APPLICABLE ACTIVE PATH; if reopened: PASS; REWORK; DEFER; STOP',
    10:'No active-path unlock; L8 participant activation is controlled by LG-09 after the integrated product is fully verified.'
})
table_row_update(gates, 'LG-05', {
    4:'Inactive historical pre-product behavioral-validation gate under DEC-0052/CR-0005.',
    5:'No pre-product human evidence is required on the active path. Historical criteria remain relevant only if the owner explicitly reopens that study.',
    6:'NOT_APPLICABLE ACTIVE PATH; if reopened: PASS/PROCEED; REPEAT; MODIFY; PIVOT; DEFER; PAUSE; STOP',
    10:'No active-path predecessor to LG-06. DEC-0052 authorizes product-first L4-L7 progression while preserving actual human/user validation for L8 after LG-09.'
})
table_row_update(gates, 'LG-06', {
    5:'Product/non-goals; traceability; internally/automatically accepted prototype and critical journeys; brand/design system; self-service; content sources; accessibility/i18n; accountless/privacy model; unresolved risks. Under DEC-0052 no real-user/participant evidence is required before this gate and none may be inferred.',
    4:'Applicable L4 dependencies and current owner product authority satisfied under DEC-0052; LG-05 is not an active-path prerequisite.',
    10:'Unlocks final architecture/delivery readiness only on actual LG-06 PASS; pre-product human validation is not a prerequisite.'
})
table_row_update(gates, 'LG-09', {
    5:'Functional/device/network; deterministic UX/truth-state flows; accessibility/RTL; security/privacy; performance/capacity; self-service; clean-server recovery; operations; defects/residual risks; pilot protocol/readiness. No real-user/participant evidence is required for LG-09 because LG-09 must pass before the first L8 human/user validation.',
    10:'Unlocks L8 as the first active parent/user/participant validation stage; no participant is activated before LG-09 PASS.'
})

constraints=ROOT/'Registers/CONSTRAINTS.md'
table_row_update(constraints, 'CON-0025', {
    2:'Under DEC-0052/CR-0005, parent/user/participant behavioral validation is intentionally postponed until after the fully integrated product has passed LG-09. No real-user testing may block L4-L7 progression. This does not waive or reduce product correctness, accessibility, technical, security/privacy, reliability, recovery or operational verification and does not create behavioral-validation evidence.',
    3:'Project Owner may explicitly reverse/reopen pre-product human validation. Until then the 31 L3 tasks plus TSK-0187/TSK-0326/TSK-0336 are NOT_APPLICABLE+PASS exclusions, and actual human/user validation starts in L8.',
    4:'TSK-0099; TSK-0164; TSK-0165; TSK-0166; TSK-0167; TSK-0168; TSK-0169; TSK-0170; TSK-0171; TSK-0172; TSK-0173; TSK-0174; TSK-0175; TSK-0176; TSK-0177; TSK-0178; TSK-0179; TSK-0180; TSK-0181; TSK-0182; TSK-0183; TSK-0184; TSK-0185; TSK-0186; TSK-0187; TSK-0309; TSK-0326; TSK-0336; TSK-0399'
})
risks=ROOT/'Registers/RISKS.md'
table_row_update(risks, 'RSK-0002', {
    3:'Human behavioral/usability/comprehension evidence is intentionally deferred until the L8 controlled integrated-product pilot, so pre-product design/build may rely on wrong assumptions about completion, value, comprehension, support burden, persistence or duplication.',
    8:'DEC-0052/CR-0005 requires rigorous internal/automated/browser/device/accessibility/security/privacy/recovery verification through L7, prohibits synthetic evidence from being labelled user validation, and requires LG-09 PASS before the first L8 human validation.',
    9:'Use the L8 pilot to observe real behavior; correct/rework product, claims, support and scope before the L9 production decision if evidence contradicts assumptions.',
    10:'LG-09 PASS enables L8; any L8 contrary evidence; or any pre-L8 claim that user/behavioral validation occurred.',
    12:'TSK-0139; TSK-0309; TSK-0399; LG-06; LG-09; LG-10; LG-11',
    13:'Open — explicitly accepted integrated-product-first validation risk under DEC-0052/CR-0005; not a pre-product blocker'
})
table_row_update(risks, 'RSK-0022', {
    8:'Use automated/browser/device acceptance, friction-budget review, accessibility checks, explicit routing/recovery states and self-service content before LG-09; perform real-user observation only in the L8 controlled integrated-product pilot.',
    9:'Simplify/limit supported paths, improve content/recovery, offer bounded help in the approved pilot/production context, pause failing route or pivot.',
    10:'Internal/automated critical-path or accessibility failure before LG-09; high abandonment/intervention or repeated route/error/support pattern in L8 or later.'
})

lifecycle=ROOT/'Registers/LIFECYCLE_OBLIGATIONS.md'
table_row_update(lifecycle, 'L2', {3:'Maintain mandatory technical/privacy/security/readiness controls that are independently required; the retired pre-product participant experiment is not an active progression prerequisite under DEC-0052.'})
table_row_update(lifecycle, 'L3', {3:'Historical pre-product concierge behavioral-validation stage retained for traceability but NOT_APPLICABLE to the active path under DEC-0052/CR-0005; its 31 tasks are exclusion-PASS, not executed.'})
table_row_update(lifecycle, 'L4', {3:'Define and freeze the owner-approved minimum compelling product, service journey, brand, UX and content system from current owner/product/technical/synthetic/internal evidence; human validation is intentionally deferred until L8.'})
table_row_update(lifecycle, 'L6', {3:'Implement the smallest approved integrated product, website, DNS service, automation and supporting systems after LG-06/LG-07; pre-product human validation is not a prerequisite under DEC-0052.'})
table_row_update(lifecycle, 'L8', {3:'First active real-user validation stage: operate the fully integrated LG-09-approved product with a bounded cohort and collect value, comprehension, persistence, reliability, supportability and funding evidence.'})
life_text=read(lifecycle)
needle='Legend: R = Required; C = Conditional with exact activation trigger below; N = Not Applicable with rationale below. A deliberate postponement uses EXC/DEFERRED_EXCEPTION, not N.'
addition=needle+'\n\n**DEC-0052 / CR-0005 active-path override:** L3 is retired from the current pre-product sequence. Its 31 task rows are `NOT_APPLICABLE + PASS` exclusion records, not executed work. The matrix retains the original L3 R/C/N package obligations only as historical/reopen semantics; actual human/user validation starts in L8 after LG-09 PASS.'
life_text=replace_once(life_text, needle, addition, 'lifecycle legend override')
write(lifecycle, life_text)

layer1=ROOT/'Layers/LAYER_1_PROGRAM_ARCHITECTURE_STRATEGIC_BASELINE.md'
t=read(layer1)
t=replace_once(t, '- Validate the riskiest behavior before expensive build; L3 concierge validation and L8 integrated-product pilot remain separate.', '- Under DEC-0052/CR-0005, build and verify the integrated product before any real parent/user/participant testing. Pre-product risk is reduced with owner/product evidence plus automated, browser/device, accessibility, security/privacy, recovery and operational verification; the first real-user validation occurs only in L8 after LG-09 PASS.', 'layer1 lean doctrine')
t=replace_once(t, '| Experience before code | Customer evidence -> product definition -> service/journey design -> prototype -> usability/comprehension -> brand/design system -> validated UI -> implementation. |', '| Experience before code | Owner/product evidence -> product definition -> service/journey design -> prototype -> internal/automated accessibility and truth-state acceptance -> brand/design system -> implementation -> integrated L7 verification -> real-user validation in L8. |', 'layer1 experience principle')
t=replace_once(t, '| Initial behavioral validation | England |', '| First controlled human validation | L8 after LG-09 PASS; England remains the initial planned location unless a later owner decision changes it. |', 'layer1 validation geography')
t=replace_once(t, '| L2 | Validation Readiness & Mandatory Controls | Make the bounded behavioral experiment legally, technically, operationally, and evidentially safe to run. | LG-03 |', '| L2 | Validation Readiness & Mandatory Controls | Maintain independently required technical/privacy/security/readiness controls; the retired pre-product participant experiment is not an active progression prerequisite under DEC-0052. | LG-03 (inactive active-path gate) |', 'layer1 L2')
t=replace_once(t, '| L3 | Concierge Behavioral Validation | Test whether qualified parents complete real safeguards and value the orchestration before expensive software build. | LG-05 |', '| L3 | Concierge Behavioral Validation | Historical pre-product human-validation stage retained for traceability but NOT_APPLICABLE to the active product-first path under DEC-0052/CR-0005. | LG-05 (inactive active-path gate) |', 'layer1 L3')
t=replace_once(t, '| L4 | Product Definition, Requirements & Experience Design | Translate validated behavior into a frozen minimum compelling product, service journey, brand, UX, and content system; under DEC-0050/CR-0003, only provisional internal definition/design may proceed from technical/synthetic evidence while missing real-participant evidence remains explicit. | LG-06 |', '| L4 | Product Definition, Requirements & Experience Design | Define and freeze the owner-approved minimum compelling product, service journey, brand, UX and content system from current owner/product/technical/synthetic/internal evidence; human validation is intentionally deferred until L8 under DEC-0052. | LG-06 |', 'layer1 L4')
t=replace_once(t, '| L6 | Build & Integration | Implement the smallest validated integrated product, website, DNS service, automation, and supporting systems. | LG-08 |', '| L6 | Build & Integration | Implement the smallest approved integrated product, website, DNS service, automation and supporting systems after LG-06/LG-07; pre-product human validation is not a prerequisite under DEC-0052. | LG-08 |', 'layer1 L6')
t=replace_once(t, '| L8 | Controlled Integrated-Product Pilot | Operate the real integrated product with a bounded cohort and collect minimum evidence on value, persistence, reliability, supportability, and funding. | LG-10 |', '| L8 | Controlled Integrated-Product Pilot | First active real-user validation stage: operate the fully integrated LG-09-approved product with a bounded cohort and collect value, comprehension, persistence, reliability, supportability and funding evidence. | LG-10 |', 'layer1 L8')
write(layer1,t)

layer4=ROOT/'Layers/LAYER_4_INTEGRATED_PROGRAM_CRITICAL_PATH.md'
t=read(layer4)
t=replace_once(t, '| 2 | L2 - Validation Readiness & Mandatory Controls | Make the bounded behavioral experiment legally, technically, operationally, and evidentially safe to run. | LG-03 |', '| 2 | L2 - Validation Readiness & Mandatory Controls | Maintain independently required technical/privacy/security/readiness controls; pre-product participant validation is not an active progression prerequisite under DEC-0052. | LG-03 (inactive active-path gate) |', 'layer4 L2')
t=replace_once(t, '| 3 | L3 - Concierge Behavioral Validation | Test whether qualified parents complete real safeguards and value the orchestration before expensive software build. | LG-05 |', '| 3 | L3 - Concierge Behavioral Validation | Historical pre-product participant-validation stage; NOT_APPLICABLE to the active integrated-product-first path under DEC-0052/CR-0005. | LG-05 (inactive active-path gate) |', 'layer4 L3')
t=replace_once(t, '| 4 | L4 - Product Definition, Requirements & Experience Design | Translate validated behavior into a frozen minimum compelling product, service journey, brand, UX, and content system; DEC-0050 temporarily permits provisional internal definition/design from technical/synthetic evidence while L3 remains deferred. | LG-06 |', '| 4 | L4 - Product Definition, Requirements & Experience Design | Define and freeze the owner-approved product, service journey, brand, UX and content baseline from current owner/product/technical/synthetic/internal evidence; real-user validation is intentionally deferred until L8. | LG-06 |', 'layer4 L4')
t=replace_once(t, '| 6 | L6 - Build & Integration | Implement the smallest validated integrated product, website, DNS service, automation, and supporting systems. | LG-08 |', '| 6 | L6 - Build & Integration | Implement the smallest approved integrated product, website, DNS service, automation and supporting systems after LG-06/LG-07 without a pre-product human-testing prerequisite. | LG-08 |', 'layer4 L6')
t=replace_once(t, '| 8 | L8 - Controlled Integrated-Product Pilot | Operate the real integrated product with a bounded cohort and collect minimum evidence on value, persistence, reliability, supportability, and funding. | LG-10 |', '| 8 | L8 - Controlled Integrated-Product Pilot | First active parent/user/participant validation stage: operate the fully integrated LG-09-approved product with a bounded cohort and collect value, comprehension, persistence, reliability, supportability and funding evidence. | LG-10 |', 'layer4 L8')
old_dep='- LG-04 authorizes concierge recruitment only after LG-03 and the synthetic operating rehearsal. L3 tests behavior before integrated software build.\n- Positive LG-05 evidence normally unlocks product/brand/service/UX definition. Through 2027-08-27, DEC-0050/CR-0003 instead permits bounded provisional internal L4 definition/design from current technical/synthetic evidence while LG-05 remains DEFER; missing real-participant evidence is explicit RSK-0002, cannot be fabricated, and any real-evidence-dependent L4 task remains deferred. The override does not authorize LG-06 PASS, L5/L6 progression, integrated build, or launch.'
new_dep='- DEC-0052/CR-0005 retires LG-03/LG-04/LG-05 and the 31-task L3 Experiment-1 branch from the active pre-product path. Those tasks/gates remain traceable historical/exclusion records and do not provide behavioral evidence.\n- L4 product/brand/service/UX definition may proceed from current owner/product/technical/synthetic/internal evidence. LG-06 and LG-07 still require exact applicable product, accessibility, architecture, security/privacy and delivery evidence; their PASS may unlock L6 build without real-user evidence. L7 then independently proves the integrated product and LG-09 must PASS before the first L8 human/user validation.'
t=replace_once(t, old_dep, new_dep, 'layer4 dependency strategy')
t=replace_once(t, 'Behavioral validation (currently DEFER under DEC-0050) -> provisional accountless minimum product/non-goals from technical/synthetic evidence -> service blueprint/friction budget/truth state -> brand/prototype work that does not require real-user evidence -> deferred usability/comprehension evidence where real users are required -> LG-06 decision -> architecture -> accountless public/setup build plus real DNS -> integrated acceptance/self-service/recovery -> controlled pilot -> product correction and primary-channel selection -> production readiness -> staged launch -> persistence/support/root-cause improvement -> Year-1 decision. No arrow after the provisional L4 segment implies that missing behavioral evidence was satisfied.', 'Owner-authorized product definition from current evidence -> service blueprint/friction budget/truth state -> brand/prototype -> internal/automated accessibility, browser/device and truth-state acceptance -> LG-06 decision -> architecture/security/privacy/delivery readiness -> LG-07 -> accountless public/setup build plus real DNS -> LG-08 -> integrated L7 acceptance/self-service/recovery -> LG-09 -> first real-user controlled pilot in L8 -> product correction and production decision -> production readiness -> staged launch -> persistence/support/root-cause improvement -> Year-1 decision. Pre-L8 work must never be labelled user/behaviorally validated.', 'layer4 customer path')
t=replace_once(t, 'LG-03 Azure/AdGuard/DNS/TLS/privacy acceptance -> DNS endpoint/platform mechanism contract -> accountless app and DNS integration architecture -> versioned DNS recovery bundle -> production-grade Ubuntu 24.04 Bash recovery script -> security/idempotency/failure-injection/clean-server acceptance -> integrated release -> controlled pilot -> production deployment/runbooks -> Year-1 maintenance and recovery rehearsals.', 'Current technical/privacy/security readiness -> DNS endpoint/platform mechanism contract -> accountless app and DNS integration architecture -> versioned DNS recovery bundle -> production-grade Ubuntu 24.04 recovery path -> security/idempotency/failure-injection/clean-server acceptance -> LG-06/LG-07 -> integrated build -> L7 integrated release verification -> LG-09 -> first L8 real-user pilot -> production deployment/runbooks -> Year-1 maintenance and recovery rehearsals.', 'layer4 tech path')
t=replace_once(t, 'OWNER LEGAL HOLD (2026-08-27 to 2027-08-27 unless reactivated earlier): UK representative/Article-27, ICO, DPIA/LIA/legal-notice/terms/tax-regulatory work is DEFERRED/WAITING while eligible technical privacy/security/infrastructure readiness continues. Real-participant Experiment 1 authorization still requires LG-03 PASS, so unresolved mandatory legal evidence remains a gate blocker rather than being treated as complete. DEC-0050/CR-0003 separately defers the complete real-participant L3 branch to the same date and permits only provisional internal L4 definition/design; it does not satisfy any legal condition or participant gate. After reactivation/resolution: Experiment 1 authorization -> behavioral evidence -> reconciliation of provisional L4 assumptions -> architecture/privacy/security readiness -> integrated acceptance -> later pilot/production gates.', 'OWNER LEGAL HOLD (2026-08-27 to 2027-08-27 unless reactivated earlier) remains independently controlling for applicable legal/regulatory/compliance acts; DEC-0052 does not waive or satisfy legal evidence. The retired pre-product L3 experiment no longer gates L4-L7. Applicable legal/privacy/vendor/participant-readiness evidence for the first actual human/user pilot must be current before LG-09 can authorize L8 participant activation; public launch remains governed by later production gates.', 'layer4 legal path')
write(layer4,t)

layer5=ROOT/'Layers/LAYER_5_AI_EXECUTION_EVIDENCE_STATE_CONTROL.md'
t=read(layer5)
insert='''\n### 5.3.4 Owner-approved integrated-product-first human-validation sequencing (DEC-0052 / CR-0005)\n\n- Effective **2026-08-29** until explicitly superseded by a later Project Owner decision, no parent/user/participant recruitment, usability/comprehension study, behavioral validation, or other real-human testing is required or permitted as a prerequisite to L4, L5, L6 or L7 progression. The first active real-user validation stage is **L8 Controlled Integrated-Product Pilot**, and it may begin only after **LG-09 PASS**.\n- This decision supersedes DEC-0050/CR-0003 and DEC-0051/CR-0004 **for sequencing**. Their historical records remain traceable. LG-03, LG-04 and LG-05 are inactive/not-applicable to the current product-first path unless the owner explicitly reopens a pre-product study.\n- The 31 L3 task rows plus `TSK-0187`, `TSK-0326`, and `TSK-0336` are `Plan_Status=NOT_APPLICABLE` + `Execution_State=PASS`. Under Section 5.4.1 this means **the exclusion/disposition is verified; the task was not implemented or executed**. It is never behavioral/user evidence and may not support a claim of validation.\n- Historical dependency edges to those excluded tasks may remain for traceability; their exclusion-PASS satisfies the dependency record for active-path sequencing only. It does not provide the excluded task's behavioral observations or measurements. Any downstream acceptance criterion that formerly required those observations is rebaselined by CR-0005 before the downstream task may PASS.\n- L4-L7 may use exact current owner/product decisions, source-backed requirements, technical/synthetic evidence, internal review, deterministic state/claim checks, automated browser/device/network tests, accessibility checks, security/privacy tests, performance/capacity evidence, recovery/rollback evidence and operational verification. Those controls remain mandatory where applicable and may not be weakened merely because human testing is deferred.\n- No pre-L8 artifact may state or imply `user-tested`, `behaviorally validated`, `representative-parent validated`, or equivalent unless real current evidence actually exists from an independently authorized later stage. The owner sequencing decision is not evidence of user behavior.\n- `LG-06` and `LG-07` remain mandatory before L6 build; `LG-08` remains mandatory before L7 integrated verification; `LG-09` remains mandatory before any L8 participant activation. Applicable legal, privacy, security, safeguarding, platform, data, vendor, cost, and action-authority requirements remain independently controlling.\n- Do not resurrect the retired pre-product validation branch as a blocker during ordinary governed execution unless a later explicit owner decision supersedes DEC-0052. Contradictory real evidence obtained in L8 or later reopens materially affected product/UX/claims tasks under the ordinary evidence-precedence rule.\n'''
anchor='\n### 5.4 Evidence and PASS rules\n'
if '### 5.3.4 Owner-approved integrated-product-first human-validation sequencing' in t:
    raise SystemExit('Layer5 CR-0005 section already exists')
if anchor not in t:
    raise SystemExit('Layer5 anchor missing')
t=t.replace(anchor, insert+anchor,1)
write(layer5,t)

iface=ROOT/'Governance/CURRENT_STATE_INTERFACE.md'
t=read(iface)
t=replace_once(t, '| Validation readiness LG-03 | IN PROGRESS / publication handoff | Legal/regulatory/compliance work is OWNER-DEFERRED until 2027-08-27 or earlier explicit reactivation; technical Azure/AdGuard/endpoint/privacy/security readiness may continue after canonical publication/read-back. The legal hold is not PASS and does not by itself authorize real participants. |', '| Validation readiness LG-03 | NOT_APPLICABLE TO ACTIVE PRE-PRODUCT PATH | DEC-0052/CR-0005 retires LG-03/LG-04/LG-05 and the pre-product participant experiment from active progression. Applicable technical/privacy/security controls remain independently required; first participant activation is after LG-09 in L8. |', 'iface LG03')
t=replace_once(t, '| Experiment 1 protocol | Designed | Execution/recruitment unauthorized until LG-03 and LG-04 PASS. |', '| Experiment 1 protocol | HISTORICAL / NOT ACTIVE PRE-PRODUCT | Retained for traceability only; pre-product recruitment/testing is excluded under DEC-0052. |', 'iface experiment')
t=replace_once(t, '| L4 product/brand/experience definition | PROVISIONAL / OWNER-AUTHORIZED under DEC-0050 | Through 2027-08-27, internal definition/design may proceed from current technical/synthetic evidence with RSK-0002 explicit; LG-05 remains DEFER and no behavioral validation is inferred. |', '| L4 product/brand/experience definition | ACTIVE / OWNER-AUTHORIZED under DEC-0052 | Product definition/design may proceed from current owner/product/technical/synthetic/internal evidence; no pre-product human validation is required or inferred. |', 'iface L4')
t=replace_once(t, '| Integrated product build | WAITING | Still requires actual downstream gate authority; DEC-0050 does not itself satisfy LG-06/LG-07 or authorize L6 build. |', '| Integrated product build | GATED BY LG-06 / LG-07 | Pre-product human validation is not a prerequisite under DEC-0052. L6 begins only after the product/experience and architecture/security/privacy/delivery gates PASS. |', 'iface build')
t=replace_once(t, '| Integrated pilot | WAITING | Requires LG-09. |', '| Integrated pilot / first real-user validation | WAITING | Requires LG-09; this is the first active parent/user/participant testing stage under DEC-0052. |', 'iface pilot')
sec_old='''### 8.2B Owner L3 behavioral-validation deferral / provisional L4 authorization\n\nEffective 2026-08-28, DEC-0050/CR-0003 defers the complete real-participant Experiment-1/L3 branch through 2027-08-27 unless reactivated earlier. LG-03/LG-04/LG-05 remain DEFER/non-PASS. Bounded internal L4 product/brand/experience definition and design may proceed from accepted technical/synthetic evidence only; missing real-participant behavioral evidence remains explicit RSK-0002, real-evidence-dependent tasks remain deferred, and no integrated build/public launch follows merely from this sequencing exception.\n'''
sec_new='''### 8.2B Owner integrated-product-first human-validation sequencing\n\nEffective 2026-08-29, DEC-0052/CR-0005 supersedes the earlier pre-product behavioral-validation sequencing. No parent/user/participant study, recruitment, usability/comprehension test or other real-human validation is required or permitted as a blocker before the integrated product is built and has passed L7/LG-09 acceptance. The 31 L3 tasks plus TSK-0187/TSK-0326/TSK-0336 are `NOT_APPLICABLE + PASS` exclusion records only; none is treated as executed or as behavioral evidence. Product, architecture, build and integrated verification continue through LG-06/LG-07/LG-08/LG-09 with full applicable automated/device/network/accessibility/security/privacy/recovery/operational proof. L8 is the first real-user validation stage.\n'''
t=replace_once(t, sec_old, sec_new, 'iface sequencing section')
old5='5. Recompute eligibility from the verified canonical modular system and current checkpoint; resume eligible non-legal LG-03 technical/privacy/security/operational readiness work while OWNER_LEGAL_HOLD_2026-08-27 tasks remain DEFERRED/WAITING until 2027-08-27 or earlier explicit owner reactivation. The hold itself does not satisfy LG-03 real-participant legal evidence.'
new5='5. Recompute eligibility under DEC-0052/CR-0005: continue eligible L4 product/brand/UX definition, then LG-06 -> L5/LG-07 -> L6/LG-08 -> L7/LG-09. Do not require or schedule real-human validation before LG-09; applicable legal/privacy/security controls remain independently governed and L8 participant activation requires current pilot authority.'
t=replace_once(t, old5, new5, 'iface sequence item5')
write(iface,t)

manifest=ROOT/'MANIFEST.yaml'
t=read(manifest)
status_old='  status: 2.0-owner-frozen / OWNER_FREEZE_2026-08-27 / OWNER_TECHNICAL_COMMERCIAL_AMENDMENT_APPLIED / OWNER_LEGAL_HOLD_ACTIVE_TO_2027-08-27 / OWNER_AZURE_HANDOFF_BOUNDARY_APPLIED_2026-08-27 / POST_FREEZE_CR_0001_DEPENDENCY_REPAIR_2026-08-27 / OWNER_LEGAL_SEQUENCING_OVERRIDE_ACTIVE_TO_2027-08-27 / OWNER_L3_BEHAVIORAL_VALIDATION_DEFERRED_TO_2027-08-27 / PROVISIONAL_L4_AUTHORIZED / OWNER_PROVISIONAL_L4_BRAND_UX_DECOUPLING_2026-08-29 / deterministic validation PASS / canonical activation established; post-freeze CR requires verified GitHub publication-readback before reliance'
status_new='  status: 2.0-owner-frozen / OWNER_FREEZE_2026-08-27 / OWNER_TECHNICAL_COMMERCIAL_AMENDMENT_APPLIED / OWNER_LEGAL_HOLD_ACTIVE_TO_2027-08-27 / OWNER_AZURE_HANDOFF_BOUNDARY_APPLIED_2026-08-27 / POST_FREEZE_CR_0001_DEPENDENCY_REPAIR_2026-08-27 / OWNER_LEGAL_SEQUENCING_OVERRIDE_ACTIVE_TO_2027-08-27 / CR_0003_CR_0004_HISTORICAL_SEQUENCING_SUPERSEDED / OWNER_INTEGRATED_PRODUCT_FIRST_HUMAN_VALIDATION_SEQUENCE_2026-08-29 / PRE_PRODUCT_HUMAN_VALIDATION_EXCLUDED / deterministic validation pending CR-0005 execution readback'
t=replace_once(t,status_old,status_new,'manifest status')
new_block='''post_freeze_change_control:\n  latest_change: CR-0005\n  date: '2026-08-29'\n  status: owner-authorized integrated-product-first human-validation sequencing; pre-product parent/user/participant testing excluded from active L4-L7 progression; first real-user validation occurs in L8 only after LG-09 PASS; canonical reliance requires deterministic validation plus GitHub publication/read-back\n  authority: explicit current Project Owner instruction 2026-08-29; DEC-0052; actual applicable safety/legal/security/privacy/platform reality remains higher authority\n  affected_tasks:\n  - all 31 L3 tasks (NOT_APPLICABLE + PASS exclusion records; not executed)\n  - TSK-0187 (excluded pre-product representative-parent validation)\n  - TSK-0326 (excluded pre-product experiment-evidence synthesis)\n  - TSK-0336 (excluded pre-product human usability/comprehension testing)\n  - TSK-0309 / TSK-0327 / TSK-0399 (rebaselined to internal/automated technical/product acceptance before L8)\n  affected_gates:\n  - LG-03 / LG-04 / LG-05 (inactive/not-applicable to current pre-product path)\n  - LG-06 / LG-07 / LG-08 / LG-09 (remain mandatory technical/product/build/release gates; no real-human evidence required before LG-09)\n  - LG-10 (retained as post-L8 human/pilot evidence checkpoint)\n  semantic_delta: no pre-product human/user validation may block product completion; exclusion-PASS is not behavioral evidence; rigorous internal/automated/browser/device/accessibility/security/privacy/recovery/operational verification remains mandatory; first actual human/user testing starts in L8 after LG-09\n  change_record: Registers/EXCEPTIONS_CHANGE_CONTROLS.md#post-freeze-material-change-records\n'''
pat=r'post_freeze_change_control:\n.*?\ngenerated_assembly_contract:'
m=re.search(pat,t,flags=re.S)
if not m:
    raise SystemExit('manifest post_freeze_change_control block not found')
t=t[:m.start()]+new_block+'\ngenerated_assembly_contract:'+t[m.end():]
write(manifest,t)

subprocess.run(['python3', str(ROOT/'Tools/rebuild_master_plan.py')], check=True)
sum_path=PLANS/'SHA256SUMS.txt'
new_sum=[]
for line in sum_path.read_text(encoding='utf-8').splitlines():
    if not line.strip(): continue
    _old, rel=line.split('  ',1)
    p=PLANS/rel
    if not p.is_file():
        raise SystemExit(f'checksum target missing: {rel}')
    new_sum.append(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {rel}")
sum_path.write_text('\n'.join(new_sum)+'\n', encoding='utf-8')

with WBS.open(encoding='utf-8', newline='') as f:
    final=list(csv.DictReader(f))
fb={r['Task_ID']:r for r in final}
assert len(final)==641, len(final)
l3=[r for r in final if r['Lifecycle_Stage']=='L3']
assert len(l3)==31
for r in l3:
    assert r['Plan_Status']=='NOT_APPLICABLE' and r['Execution_State']=='PASS'
for tid in ('TSK-0187','TSK-0326','TSK-0336'):
    assert fb[tid]['Plan_Status']=='NOT_APPLICABLE' and fb[tid]['Execution_State']=='PASS'
assert fb['TSK-0309']['Plan_Status']!='NOT_APPLICABLE'
assert fb['TSK-0327']['Plan_Status']!='NOT_APPLICABLE'
assert fb['TSK-0399']['Plan_Status']!='NOT_APPLICABLE'
assert 'real-user comprehension claim is required' not in fb['TSK-0309']['Acceptance_Criteria'].lower()
assert 'real parent' not in fb['TSK-0399']['Title'].lower()
edges=0
for r in final:
    edges += len([x for x in re.split(r'[;,]', r['Dependencies']) if x.strip()])
assert edges==849, edges
assert 'DEC-0052 / CR-0005' in read(layer5)
assert 'first real-user validation' in read(gates).lower()
assert 'NOT_APPLICABLE TO ACTIVE PRE-PRODUCT PATH' in read(iface)
assert 'latest_change: CR-0005' in read(manifest)
assert '| DEC-0052 |' in read(dec_path)
assert '| CR-0005 |' in read(cr_path)
print('CR0005_PREVALIDATION_EXCLUDED_TASKS=34')
print('CR0005_L3_EXCLUDED_TASKS=31')
print('CR0005_TASK_COUNT=641')
print('CR0005_DEPENDENCY_EDGES=849')
print('CR0005_TRANSFORM_ASSERTIONS=PASS')

subprocess.run(['python3', str(ROOT/'Tools/validate_master_plan.py')], check=True)
print('CR0005_AMENDMENT_VALIDATION=PASS')
