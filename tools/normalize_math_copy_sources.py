"""Conservative, reversible MathML normalization for equation copying.

Default is an audit; --apply records full-file before/after editorial patches.
Only MathML fragments are serialized, so surrounding CNXML is untouched.
"""
from pathlib import Path
import collections, copy, hashlib, html, json, re, sys
import xml.etree.ElementTree as E

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'prototype'))
from native_math import native_math
M='{http://www.w3.org/1998/Math/MathML}'
E.register_namespace('m',M)
OUT=ROOT/'reports/1.1/math-source-normalization'
OUT.mkdir(parents=True,exist_ok=True)
tag=lambda e:e.tag.rsplit('}',1)[-1]
text=lambda e:''.join(e.itertext()).strip()
def node(t,value=None,children=()):
    e=E.Element(M+t);e.text=value;e.extend(children);return e
def space():return E.Element(M+'mspace',{'width':'0.167em'})
def unwrap(e):
    while tag(e)=='mrow' and not e.attrib and len(e)==1:e=e[0]
    return e
def token(e):
    e=unwrap(e)
    return e if tag(e) in ('mi','mn','mtext') and not len(e) and not e.attrib else None
UNITS=set('m s kg g km cm mm nm pm fm h hr min ms ns ps yr y N J W V A C K Pa Hz T H F S Bq Gy Sv Ci rad rem mol eV keV MeV GeV TeV kW kWh kPa MPa L mL dB u'.split())|{'μm','μs','μC','Ω','kΩ','MΩ','μA','mA','mW','kJ','MJ','nC','pC','mT','μT'}
NUMBER=r'(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d*)?|\.\d+'
def unit_parts(s):
    """Only whitelist units and literal slash/dot products, not arbitrary prose."""
    parts=re.split(r'([/·⋅])',s.strip())
    if not parts or any(p.strip() not in UNITS for p in parts if p and p not in '/·⋅'):return None
    result=[]
    for p in parts:
        if not p:continue
        part=node('mo',p) if p in '/·⋅' else node('mtext',p.strip())
        if p=='/':part.set('lspace','0');part.set('rspace','0')
        result.append(part)
    return result if result and tag(result[-1])=='mtext' else None
def quantity(s):
    match=re.fullmatch('('+NUMBER+r')\s+(.+)',s.strip())
    if not match:return None
    units=unit_parts(match[2])
    return [node('mn',match[1]),space(),*units] if units else None
ELEMENTS=set('H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr X'.split())|{'n','p','e','α','β','γ'}
def nuclear_base(e):
    """Find the first element in a following group; never skip an operator."""
    e=unwrap(e)
    if tag(e)=='mrow' and len(e):return nuclear_base(e[0])
    base=e[0] if tag(e) in ('msub','msup','msubsup') else e
    leaf=token(base)
    return e if leaf is not None and text(leaf) in ELEMENTS else None
def left_scripts(e):
    e=unwrap(e);t=tag(e)
    if t in ('msup','msubsup') and not text(e[0]):
        return (node('none') if t=='msup' else copy.deepcopy(e[1]),copy.deepcopy(e[-1]))
    if t=='mmultiscripts' and len(e)==4 and not text(e[0]) and tag(e[1])=='mprescripts':
        return copy.deepcopy(e[2]),copy.deepcopy(e[3])
    return None
def visible(e):
    if tag(e) in ('annotation','annotation-xml'):return ''
    return (e.text or '')+''.join(visible(c)+(c.tail or '') for c in e)

def normalize(tree,mid,ordinal):
    reasons=collections.Counter()
    # Three verified nonnuclear detached subscripts, not a heuristic.
    expected={('m67034',151):'v',('m68876',39):'y',('m71411',22):'W'}.get((mid,ordinal))
    if expected:
        parents={c:p for p in tree.iter() for c in p};ordered=list(tree.iter())
        detached=[e for e in tree.iter(M+'mmultiscripts') if not text(e[0])]
        if detached:
            assert len(detached)==1
            e=detached[0];prior=[n for n in ordered[:ordered.index(e)] if tag(n) in ('mi','mtext') and n.text==expected][-1]
            parent=parents[prior];i=list(parent).index(prior)
            parent[i]=node('msub',children=[copy.deepcopy(prior),copy.deepcopy(e[2])]);parents[e].remove(e)
            reasons['attach-verified-subscript']+=1
    def walk(e):
        if tag(e) in ('annotation','annotation-xml'):return
        # Fix unit exponent attachment before splitting the base text.
        if tag(e)=='msup' and len(e)==2:
            base=token(e[0])
            if base is not None:
                raw=text(base);parts=quantity(raw) or unit_parts(raw)
                # A lone unit already has the right base; only compound text needs repair.
                if parts and len(parts)>1:
                    exponent=copy.deepcopy(e[1]);last=parts.pop()
                    tail=e.tail;e.clear();e.tag=M+'mrow';e.tail=tail
                    e.extend(parts+[node('msup',children=[last,exponent])]);reasons['attach-unit-exponent']+=1
        for c in list(e):walk(c)
        # Bind explicit left nuclear scripts to the immediately following element.
        if tag(e) in ('mrow','math','mtd'):
            i=0
            while i+1<len(e):
                scripts=left_scripts(e[i]);target=nuclear_base(e[i+1]) if scripts else None
                if scripts and target is not None:
                    base=copy.deepcopy(target[0]) if tag(target) in ('msub','msup','msubsup') else copy.deepcopy(target)
                    right=[]
                    if tag(target)=='msub':right=[copy.deepcopy(target[1]),node('none')]
                    elif tag(target)=='msup':right=[node('none'),copy.deepcopy(target[1])]
                    elif tag(target)=='msubsup':right=[copy.deepcopy(target[1]),copy.deepcopy(target[2])]
                    replacement=node('mmultiscripts',children=[base,*right,node('mprescripts'),*scripts])
                    parent=next(p for p in e.iter() if target in list(p));parent[list(parent).index(target)]=replacement
                    e.remove(e[i]);reasons['bind-nuclear-prescripts']+=1
                else:i+=1
        # Tokenize only explicit number+known-unit strings.
        for i,c in enumerate(list(e)):
            if tag(c) in ('mtext','mn') and not c.attrib and not len(c):
                parts=quantity(c.text or '')
                if parts:
                    e[i]=node('mrow',children=parts);e[i].tail=c.tail;reasons['split-quantity-token']+=1
        # Merge only decimal fragments, never arbitrary adjacent integers.
        if tag(e) in ('mrow','math','mtd'):
            i=0
            while i+1<len(e):
                a,b=token(e[i]),token(e[i+1])
                if a is not None and b is not None and re.fullmatch(r'\d+',a.text or ''):
                    if re.fullmatch(r'\.\d+',b.text or ''):
                        e[i]=node('mn',a.text+b.text);e.remove(e[i+1]);reasons['join-decimal']+=1;continue
                    if b.text=='.' and i+2<len(e):
                        c=token(e[i+2])
                        if c is not None and re.fullmatch(r'\d+',c.text or ''):
                            merged=node('mn',a.text+'.'+c.text);del e[i:i+3];e.insert(i,merged);reasons['join-decimal']+=1;continue
                i+=1
    walk(tree)
    return reasons

def main():
    items=[];changes=[];counts=collections.Counter()
    pattern=re.compile(r'<m:math\b.*?</m:math>',re.S)
    for path in sorted((ROOT/'maintained/modules').glob('*/index.cnxml')):
        before=path.read_text(encoding='utf-8');mid=path.parent.name;edits=[]
        for ordinal,match in enumerate(pattern.finditer(before),1):
            raw=match.group(); parse_raw=raw if 'xmlns:m=' in raw.split('>',1)[0] else raw.replace('<m:math','<m:math xmlns:m="'+M[1:-1]+'"',1); tree=E.fromstring(parse_raw)
            oldtree=copy.deepcopy(tree);reasons=normalize(tree,mid,ordinal)
            if not reasons:continue
            assert collections.Counter(re.sub(r'\s','',visible(oldtree)))==collections.Counter(re.sub(r'\s','',visible(tree))),(mid,ordinal,'content changed')
            assert [E.tostring(n) for n in oldtree.iter(M+'annotation')]==[E.tostring(n) for n in tree.iter(M+'annotation')]
            rendered_before=native_math(oldtree)[0];rendered_after=native_math(tree)[0]
            E.register_namespace('m',M[1:-1])
            result=E.tostring(tree,encoding='unicode')
            edits.append((match.start(),match.end(),result));counts.update(reasons)
            items.append(dict(module=mid,key=f'{mid}-math-{ordinal:04d}',reasons=dict(reasons),before=raw,after=result,rendered_before=rendered_before,rendered_after=rendered_after))
        after=before
        for a,b,result in reversed(edits):after=after[:a]+result+after[b:]
        if edits:
            assert [n.get('id') for n in E.fromstring(before).iter() if n.get('id')]==[n.get('id') for n in E.fromstring(after).iter() if n.get('id')]
            changes.append((path,before,after))
    report=dict(status='applied' if '--apply' in sys.argv else 'audit-only',modules=len(changes),expressions=len(items),operations=dict(counts),items=items)
    if '--apply' in sys.argv:
        ledger_path=ROOT/'maintained/editorial-changes.json';ledger=json.loads(ledger_path.read_text(encoding='utf-8'))
        for path,before,after in changes:
            mid=path.parent.name;pid='MATH-COPY-NORMALIZE-'+mid;rel='proposals/author-corrections/'+pid+'.json'
            assert rel not in ledger['changes'],'Do not overwrite an existing patch'
            patch=dict(id=pid,status='applied-maintainer-approved',target_release='cp2e-ver1.1',module=mid,source_path=path.relative_to(ROOT).as_posix(),source_sha256=hashlib.sha256(before.encode()).hexdigest(),after_sha256=hashlib.sha256(after.encode()).hexdigest(),before=before,after=after,reason='Authorized structural MathML cleanup for copying: attach verified subscripts and nuclear prescripts, preserve unit exponent scope, tokenize explicit quantities, and merge unambiguous decimal fragments. Preserve source IDs, annotation text, mathematical characters and all non-MathML content.')
            (ROOT/rel).write_text(json.dumps(patch,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
            path.write_text(after,encoding='utf-8',newline='\n');ledger['changes'].append(rel)
        ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    (OUT/'changes.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    body='<h1>MathML normalization: before and after</h1><p>'+html.escape(str({k:v for k,v in report.items() if k!='items'}))+'</p>'
    for item in items:
        body+='<section id="'+item['key']+'"><h2>'+item['key']+'</h2><p>'+html.escape(str(item['reasons']))+'</p><div class="pair"><div><h3>Before</h3>'+item['rendered_before']+'</div><div><h3>After</h3>'+item['rendered_after']+'</div></div></section>'
    (OUT/'index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><title>MathML normalization review</title><style>body{font:16px system-ui;margin:2rem;color:#172b35}section{border-top:1px solid #bcc;padding:1rem 0}.pair{display:grid;grid-template-columns:1fr 1fr;gap:2rem}.pair>div{overflow:auto;padding:1rem}math{font-size:22px}h2{font-size:17px}</style>'+body+'</html>',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in report.items() if k!='items'},indent=2))

if __name__ == "__main__":
    main()
