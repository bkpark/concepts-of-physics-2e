"""Reproducible whole-book audit of published MathML sentence punctuation."""
from pathlib import Path
import collections
import json
import sys
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'prototype'))
from native_math import native_math
from math_sentence_punctuation import separate, M

records=[];retained=[];total=0
for path in sorted((ROOT/'maintained/modules').glob('*/index.cnxml')):
    root=ET.parse(path).getroot()
    parents={c:e for e in root.iter() for c in e}
    for index,math in enumerate(root.iter(M+'math'),1):
        total+=1
        xml,_=native_math(math)
        new,punctuation,decision=separate(xml)
        obj=math
        while not obj.get('id') and obj in parents:obj=parents[obj]
        text=''.join(ET.fromstring(xml).itertext())
        rec={'module':path.parent.name,'index':index,'object':obj.get('id'),
             'text':text,'decision':decision}
        if punctuation:
            # No content is lost: only the terminal mark and surrounding
            # insignificant whitespace may move out of the expression.
            normalized=lambda s:''.join(s.split())
            assert normalized(text)==normalized(''.join(ET.fromstring(new).itertext())+punctuation),rec
            rec['punctuation']=punctuation
            records.append(rec)
        elif text.rstrip().endswith(('.',',',';',':','?')):
            retained.append(rec)
out=ROOT/'reports/1.1/math-sentence-punctuation'
out.mkdir(parents=True,exist_ok=True)
summary={'expressions_audited':total,'separated':len(records),'modules_changed':len({r['module'] for r in records}),
         'retained_candidates':len(retained)}
(out/'audit.json').write_text(json.dumps({'summary':summary,'moved':records,'retained':retained},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary))
for rec in retained:print(json.dumps(rec,ensure_ascii=False))
