from pathlib import Path

p = Path('Plans/Master/RELATIONSHIP_INDEX.yaml')
text = p.read_text(encoding='utf-8')
lines = text.splitlines()
indices = [i for i, line in enumerate(lines) if 'TSK-0328' in line]
if not indices:
    raise SystemExit('TSK-0328 absent from relationship graph')
seen = set()
for idx in indices:
    start = max(0, idx - 4)
    end = min(len(lines), idx + 5)
    for i in range(start, end):
        if i not in seen:
            print(f'{i+1}: {lines[i]}')
            seen.add(i)
print(f'TSK0328_GRAPH_MATCH_COUNT={len(indices)}')
print('TSK0328_GRAPH_INSPECTION=PASS')
