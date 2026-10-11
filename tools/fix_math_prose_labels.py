"""Apply the individually reviewed global prose-label corrections (idempotent)."""
from pathlib import Path
import hashlib
import json
import re
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
M='{http://www.w3.org/1998/Math/MathML}'
# Source math ordinals identify reviewed occurrences without relying on wording
# elsewhere (e.g. identical prose in captions, units, or mathematical subscripts).
FIXES={
 'm42680': {42:(', (proposed proton decay)',None)},
 'm67034': {131:('on dry concrete','3 m on dry concrete'),133:('on wet concrete','0 m on wet concrete')},
 'm67037': {6:('(conservative\u00a0forces\u00a0only),',None)},
 'm67042': {3:('(two-object elastic collision)',None)},
 'm67124': {5:('(melting/freezing),',None),6:('(vaporization/condensation),',None)},
 'm67126': {11:('(isobaric process).',None)},
 'm67127': {24:('(cyclical process),',None),31:('(cyclical process),',None)},
 'm78798': {132:('(exactly)',None)},
}

def visible(xml):
    root=ET.fromstring('<wrap xmlns:m="'+M[1:-1]+'">'+xml+'</wrap>')
    for parent in root.iter():
        for child in list(parent):
            if child.tag==M+'annotation':parent.remove(child)
    return ''.join(''.join(root.itertext()).split())

if __name__=='__main__':
    ledger=ROOT/'maintained/editorial-changes.json'
    data=json.loads(ledger.read_text(encoding='utf-8'))
    changed=[]
    for mid,fixes in FIXES.items():
        ident='GLOBAL-MATH-PROSE-LABELS-'+mid
        recpath=ROOT/'proposals/author-corrections'/(ident+'.json')
        if recpath.exists():
            rel=recpath.relative_to(ROOT).as_posix()
            if rel not in data['changes']:data['changes'].append(rel)
            continue
        path=ROOT/'maintained/modules'/mid/'index.cnxml'
        before=path.read_bytes().decode('utf-8');index=0
        def change(match):
            global index
            index+=1
            old=match.group()
            if index not in fixes:return old
            label,mixed=fixes[index]
            new=re.sub(r'<m:annotation\b[^>]*>.*?</m:annotation>','',old,flags=re.S)
            if mixed:
                assert new.count(mixed)==1
                new=new.replace(mixed,mixed.split(' on ')[0])
                # The period is prose punctuation following this qualifier.
                new,n=re.subn(r'<m:mtext>\.</m:mtext>(\s*</m:mrow>\s*</m:mrow>\s*<m:mrow\s*/>)',r'\1',new)
                assert n==1
                label+='.'
            elif mid=='m78798':
                pattern=r'<m:mspace width="0.20em"\s*/><m:mo stretchy="false">\(</m:mo><m:mtext>exactly</m:mtext><m:mo stretchy="false">\)</m:mo>'
                new,n=re.subn(pattern,'',new);assert n==1
            else:
                pattern=r'<m:mtext>\s*'+re.escape(label)+r'</m:mtext>'
                new,n=re.subn(pattern,'',new);assert n==1,(mid,index,label)
            new=re.sub(r'<m:annotation\b[^>]*>.*?</m:annotation>','',new,flags=re.S)
            # Equation containers provide block layout; keep attached prose on
            # the same line and retain display-style fraction sizing.
            new=new.replace(' display="block"',' display="inline" displaystyle="true"')
            suffix=label if label.startswith(',') else ' '+label
            new+=suffix
            assert visible(old)==visible(new),(mid,index)
            changed.append({'module':mid,'math_index':index,'label':label})
            return new
        after=re.sub(r'<m:math\b.*?</m:math>',change,before,flags=re.S)
        ET.fromstring(after)
        assert after!=before
        rec={'id':ident,'status':'applied-maintainer-approved','target_release':'cp2e-ver1.1','module':mid,
             'source_path':path.relative_to(ROOT).as_posix(),
             'source_sha256':hashlib.sha256(before.encode()).hexdigest(),'after_sha256':hashlib.sha256(after.encode()).hexdigest(),
             'before':before,'after':after,'reason':'Global reviewed audit: move explanatory prose labels/qualifiers outside MathML, retaining mathematical content and wording.'}
        path.write_bytes(after.encode('utf-8'))
        recpath.write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        data['changes'].append(recpath.relative_to(ROOT).as_posix())
        ledger.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    ledger.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    out=ROOT/'reports/1.1/math-prose-labels/applied.json'
    applied=[{'module':mid,'math_index':i,'label':spec[0]} for mid,fixes in FIXES.items() for i,spec in fixes.items()
             if (ROOT/'proposals/author-corrections'/('GLOBAL-MATH-PROSE-LABELS-'+mid+'.json')).exists()]
    out.write_text(json.dumps(applied,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'labels_moved':len(changed),'modules':len({x['module'] for x in changed})}))
