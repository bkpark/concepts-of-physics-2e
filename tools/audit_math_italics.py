"""Conservative typography repair and review inventory; no mathematical substitutions."""
from pathlib import Path
import xml.etree.ElementTree as E
import re,json,hashlib,collections
ROOT=Path(__file__).resolve().parents[1]
M='{http://www.w3.org/1998/Math/MathML}'
E.register_namespace('m',M[1:-1])
labels=json.loads((ROOT/'prototype/dist/course-full/object-labels.json').read_text(encoding='utf-8'))
sections={x['section_id'].split(':')[1]:x['label'] for x in json.loads((ROOT/'metadata/numbering-course-2026-07-07.proposed.json').read_text(encoding='utf-8'))['section_labels']}
report=ROOT/'reports/1.1/math-italic-audit';report.mkdir(exist_ok=True)
ledgerpath=ROOT/'maintained/editorial-changes.json';ledger=json.loads(ledgerpath.read_text(encoding='utf-8'))
products=set('IR hf mg IV PV at mv ma mgΔh mgh gh mr qV mc V/R Pt pc γmu nI mL Ad mM Ah mu xn PA gt kx hc rF qQ kQ V/I rg Fd PAd LC hv Mgh nh mvr vr mad ad MR Qt kq qE nqAv rB Rt ZM Nm fd md ρv Iω πr λt fλ γmc ρgh ρg nλ rα Iα πd qr Nμ Mℓ mR πR ρπ mλ rω ρV'.split())
abbrevs={'COP','Eff','EER','PE','KE'}
scripts={M+x for x in ['msub','msup','msubsup','mover','munder','munderover']}
fixed=[];flagged=[];changed=[];scanned=0
def italic(e):return e.get('fontstyle')=='italic' or e.get('mathvariant')=='italic'
def norm(s):return re.sub(r'\s+','',s)
def content(e):
    return ''.join(t.text or '' for t in e.iter() if len(t)==0 and t.tag!=M+'annotation')
def tokenized(s):
    out=[]
    for c in s:
        if c.isspace():continue
        if c in '=+−/.,|()′':e=E.Element(M+'mo');e.text=c
        elif c.isdigit():e=E.Element(M+'mn');e.text=c
        else:
            e=E.Element(M+'mi');e.text=c
            if c=='Δ':e.set('mathvariant','normal')
        out.append(e)
    return out
for path in sorted((ROOT/'maintained/modules').glob('*/index.cnxml')):
    mid=path.parent.name;before=path.read_text(encoding='utf-8');local=[];serial=0
    def repair(match):
        global scanned,serial
        serial+=1;scanned+=1
        raw=match[0]
        e=E.fromstring('<root xmlns:m="'+M[1:-1]+'">'+raw+'</root>')[0]
        parents={ch:p for p in e.iter() for ch in p}
        # Match the nearest source object ID preceding this expression for review navigation.
        ids=re.findall(r'\bid="([^"]+)"',before[:match.start()]);ident=ids[-1] if ids else ''
        obj=labels.get(mid+'#'+ident,{})
        context=dict(module=mid,section=sections.get(mid,''),source_id=ident,object_label=obj.get('label'),math_index=serial,expression=norm(content(e)))
        actions=[]
        def inherited(t):
            p=t
            while p is not None:
                if italic(p):return True
                p=parents.get(p)
            return False
        def scriptbase(t):
            p=parents.get(t);child=t
            while p is not None and p.tag in (M+'mrow',M+'mstyle',M+'semantics'):
                # A last factor followed by an exponent on the whole group may be ambiguous.
                child=p;p=parents.get(p)
            return p is not None and p.tag in scripts and list(p)[0] is child
        for t in list(e.iter()):
            if len(t) or t.tag not in {M+'mi',M+'mtext',M+'mn',M+'mo'}:continue
            s=(t.text or '').strip();compact=norm(s);it=inherited(t)
            candidate=it and t.tag!=M+'mi' or t.tag==M+'mi' and len(compact)>1 or t.tag==M+'mtext' and compact in {'Δ','−Δ'}
            if not candidate:continue
            if compact in abbrevs:
                t.tag=M+'mtext';t.attrib.pop('fontstyle',None);t.set('mathvariant','normal');actions.append('upright descriptive label');continue
            if compact=='soda' and t.tag==M+'mi':
                t.tag=M+'mtext';t.set('mathvariant','normal');actions.append('upright descriptive subscript');continue
            if it and compact in {'0°C','20°C'}:
                t.attrib.pop('fontstyle',None);t.set('mathvariant','normal');actions.append('upright temperature unit');continue
            core=compact.strip('=+−/.,|()′')
            recognized=(core in products or (len(core)==1 and core.isalpha()) or re.fullmatch(r'Δ[A-Za-zα-ωΑ-Ω]',core))
            if recognized and scriptbase(t) and len(core)>1:
                flagged.append(dict(**context,fragment=s,reason='Compound script base: review whether exponent/subscript applies to last factor or whole product.'))
                continue
            if recognized:
                t.tag=M+'mrow';t.attrib.pop('fontstyle',None);t.attrib.pop('mathvariant',None);t.text=None
                t.extend(tokenized(compact));actions.append('separate variables/operators');continue
            # Real operators/numbers under italic wrappers are explicitly upright.
            if it and t.tag in {M+'mo',M+'mn'} and (compact.isdigit() or compact in '=+−/.,|()'):
                t.attrib.pop('fontstyle',None);t.set('mathvariant','normal');actions.append('upright number/operator');continue
            if it or (t.tag==M+'mi' and len(compact)>1):
                flagged.append(dict(**context,fragment=s,reason='Unclassified italic fragment or multi-character identifier; inspect in context.'))
        if not actions:return raw
        # Explicit per-token variants override inherited italic styles, while existing structure remains intact.
        assert norm(content(e))==norm(content(E.fromstring('<root xmlns:m="'+M[1:-1]+'">'+raw+'</root>')[0])),context
        result=E.tostring(e,encoding='unicode')
        local.append(dict(**context,actions=sorted(set(actions)),before=raw,after=result))
        return result
    after=re.sub(r'<m:math\b[^>]*>.*?</m:math>',repair,before,flags=re.S)
    if after==before:continue
    E.fromstring(after)
    # Everything outside MathML is unchanged.
    strip=lambda s:re.sub(r'<m:math\b[^>]*>.*?</m:math>','MATH',s,flags=re.S)
    assert strip(before)==strip(after)
    key='MATH-ITALIC-TYPOGRAPHY-'+mid;rel='proposals/author-corrections/'+key+'.json';assert rel not in ledger['changes']
    record=dict(id=key,status='applied-maintainer-approved',target_release='cp2e-ver1.1',module=mid,source_path=path.relative_to(ROOT).as_posix(),source_sha256=hashlib.sha256(before.encode()).hexdigest(),after_sha256=hashlib.sha256(after.encode()).hexdigest(),before=before,after=after,reason='Approved textbook-wide scan: repair clear italic text/variable and descriptive label typography only; compound script bases deferred for review.')
    (ROOT/rel).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');path.write_text(after,encoding='utf-8');ledger['changes'].append(rel)
    changed.append(mid);fixed.extend(local)
ledgerpath.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
data=dict(scanned_math=scanned,changed_modules=changed,fixed_expressions=fixed,review_candidates=flagged)
(report/'audit.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lines=['# Math italic typography audit','',f'Scanned {scanned} MathML expressions. Repaired {len(fixed)} expressions in {len(changed)} modules. Flagged {len(flagged)} fragments for contextual review. No preview refresh.','', 'Repairs separate clear variable products/operators and make descriptive labels, numbers, and temperature units upright. All non-MathML source and normalized mathematical text are preserved. Script grouping is not changed.','', '## Cases needing review','', '| Section | Object / source ID | Fragment | Reason |','|---|---|---|---|']
for x in flagged:lines.append('| '+x['section']+' | '+str(x['object_label'] or x['source_id'])+' | '+x['fragment'].replace('|','&#124;').replace('\n',' ')+' | '+x['reason']+' |')
(report/'review.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps(dict(scanned=scanned,fixed=len(fixed),modules=len(changed),flagged=len(flagged))))
