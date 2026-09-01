import csv
from pathlib import Path

with Path('Plans/Master/WBS/master-wbs.csv').open(encoding='utf-8-sig', newline='') as f:
    rows = {r['Task_ID']: r for r in csv.DictReader(f) if r['Task_ID'] in {'TSK-0323','TSK-0324','TSK-0321'}}

for tid in ('TSK-0323','TSK-0324','TSK-0321'):
    r = rows[tid]
    print(f"{tid}_TITLE={r.get('Task_Name') or r.get('Task') or r.get('Title')}")
    print(f"{tid}_LIFECYCLE={r['Lifecycle_Stage']}")
    print(f"{tid}_PRIORITY={r.get('Priority','')}")
    print(f"{tid}_DEPS={r['Dependencies']}")
    print(f"{tid}_ACC_ID={r['Acceptance_ID']}")
    print(f"{tid}_VER_ID={r['Verification_ID']}")
    print(f"{tid}_EVD_ID={r['Evidence_ID']}")
    print(f"{tid}_AI={r['AI_Capability_A0_A4']}")
    print(f"{tid}_AUTH={r['Action_Authority']}")
    print(f"{tid}_ACC={r['Acceptance_Criteria']}")
