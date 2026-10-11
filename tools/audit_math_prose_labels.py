"""Flag new prose-like MathML tokens for review; never strip text blindly."""
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
M='{http://www.w3.org/1998/Math/MathML}'
WORDS=re.compile(r'[A-Za-z]{4,}|[A-Za-z]{2,}\s+[A-Za-z]{2,}')
TOKENS={M+t for t in ('mtext','mo','mi','mn','ci','cn')}

def scan():
    records=[];count=0
    for path in sorted((ROOT/'maintained/modules').glob('*/index.cnxml')):
        root=ET.parse(path).getroot();parents={c:e for e in root.iter() for c in e}
        for index,math in enumerate(root.iter(M+'math'),1):
            count+=1
            tokens=[(e.tag.rsplit('}',1)[-1],e.text or '') for e in math.iter()
                    if e.tag in TOKENS and WORDS.search(e.text or '')]
            if not tokens:continue
            obj=math
            while not obj.get('id') and obj in parents:obj=parents[obj]
            records.append({'module':path.parent.name,'index':index,'object':obj.get('id'),'tokens':tokens})
    return count,records

def key(record):
    return json.dumps([record['module'],record['object'],record['tokens']],ensure_ascii=False,sort_keys=True)

if __name__=='__main__':
    total,records=scan()
    directory=ROOT/'reports/1.1/math-prose-labels'
    reviewed=json.loads((directory/'reviewed-retained.json').read_text(encoding='utf-8'))
    known={key(r) for r in reviewed}
    new=[r for r in records if key(r) not in known]
    result={'expressions_scanned':total,'retained_candidates':len(records),'unreviewed':new}
    (directory/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False))
    raise SystemExit(bool(new))
