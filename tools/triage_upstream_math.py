"""Recognize redundant MathML rows in comparison reports; do not alter textbook XML.

Only empty rows inside math/rows, attribute-free singleton rows, and equivalent
decimal spellings of em spacing are normalized.
Fractions, roots, scripts, attributes, tokens, accents and table cells stay distinct.
This proves a narrow representation equivalence, not correctness of an equation.
"""
from pathlib import Path
import hashlib,json,re,xml.etree.ElementTree as ET
from decimal import Decimal
ROOT=Path(__file__).resolve().parents[1]
def signature(e):
    name=e.tag.rsplit('}',1)[-1]
    attributes=dict(e.attrib)
    if name=='mspace' and re.fullmatch(r'\d*\.\d+em',attributes.get('width','')):
        attributes['width']=str(Decimal(attributes['width'][:-2]).normalize())+'em'
    attrs=tuple(sorted(attributes.items()))
    text=e.text or ''
    if name not in ('mi','mo','mn','mtext'):text=text.strip()
    children=[]
    for child in e:
        value=signature(child);tail=(child.tail or '').strip()
        if value==('mrow',(),' ',()) and not tail and name in ('mrow','math'):continue
        if value==('mrow',(),'',()) and not tail and name in ('mrow','math'):continue
        children.append((value,tail))
    if name=='mrow' and not attrs and not text and len(children)==1 and not children[0][1]:return children[0][0]
    return name,attrs,text,tuple(children)

if __name__=='__main__':
    decisions=[];total=0
    for path in sorted((ROOT/'reports/1.1/upstream-book').glob('m*.json')):
        row=json.loads(path.read_text(encoding='utf-8'))
        for change in row['changes']:
            if change['kind'] not in ('math-markup-change','math-token-change'):continue
            total+=1
            if signature(ET.fromstring(change['local']))!=signature(ET.fromstring(change['upstream'])):continue
            decisions.append({'id':change['id'],'module':row['module'],'source_id':change['source_id'],
                'status':'retain-local-representation','reason':'Rendered trees differ only by redundant attribute-free rows under the documented conservative normalization; preserve local MathML.',
                'local_render_sha256':hashlib.sha256(change['local'].encode()).hexdigest(),
                'upstream_render_sha256':hashlib.sha256(change['upstream'].encode()).hexdigest()})
    result={'method':'conservative-row-equivalence-v1','scope':'Representation triage only; not a complete physics or layout audit.',
            'compared':total,'equivalent':len(decisions),'remaining':total-len(decisions),'decisions':decisions}
    (ROOT/'reports/1.1/math-representation-decisions.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in result.items() if k!='decisions'}))
