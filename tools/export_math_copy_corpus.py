"""Export every built source expression for the MathJax renderer regression test."""
from pathlib import Path
import json
import sys
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'prototype'))
from native_math import native_math
from math_copy import copy_formats
sources=json.loads((ROOT/'prototype/dist/course-full/math-source.json').read_text(encoding='utf-8'))
rows=[]
for source in sources:
    rendered=native_math(ET.fromstring(source['xml']))[0]
    rows.append(dict(key=source['key'],mathml=rendered,**copy_formats(rendered)))
(ROOT/'output').mkdir(exist_ok=True)
(ROOT/'output/math-copy-corpus.json').write_text(json.dumps(rows,ensure_ascii=False),encoding='utf-8')
print('Exported',len(rows),'expressions for renderer testing.')
