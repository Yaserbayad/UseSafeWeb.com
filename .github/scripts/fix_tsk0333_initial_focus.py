#!/usr/bin/env python3
from pathlib import Path
p=Path('prototype/TSK-0333/app.mjs')
s=p.read_text(encoding='utf-8')
old="""  const heading = app.querySelector('h1');
  if (heading) {
    heading.tabIndex = -1;
    heading.focus({ preventScroll: true });
    if (announce) announcer.textContent = heading.textContent;
  }
"""
new="""  const heading = app.querySelector('h1');
  if (heading && announce) {
    heading.tabIndex = -1;
    heading.focus({ preventScroll: true });
    announcer.textContent = heading.textContent;
  }
"""
assert old in s, 'expected render focus block missing'
s=s.replace(old,new,1)
assert s.count('heading.focus({ preventScroll: true });') == 1
p.write_text(s,encoding='utf-8')
print('TSK0333_INITIAL_FOCUS_FIX=PASS')
