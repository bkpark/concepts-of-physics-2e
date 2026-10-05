"""Apply the maintainer-approved 55-question Chapter 9 proposal."""
from pathlib import Path
import json,re,hashlib,html,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[1]
report=ROOT/'reports/1.1/chapter9-structure'
proposal=json.loads((report/'question-set-proposal.json').read_text(encoding='utf-8'))
inventory=json.loads((report/'current-question-inventory.json').read_text(encoding='utf-8'))
old={q['number']:q for q in inventory}
modules={q['section']:q['module'] for q in inventory}
before={m:(ROOT/f'maintained/modules/{m}/index.cnxml').read_text(encoding='utf-8') for m in modules.values()}
groups=re.compile(r'<section\b[^>]*>(?:(?!<section\b).)*?</section>',re.S)
isgroup=lambda s:'<title>Questions and Exercises</title>' in s
exercise=re.compile(r'<exercise\b[^>]*id="([^"]+)"[^>]*>.*?</exercise>',re.S)
blocks={n:next(m[0] for m in exercise.finditer(before[q['module']]) if m[1]==q['id']) for n,q in old.items()}
out={m:[] for m in before}
manifest=[]

def math(body):return '<m:math><m:mrow>'+body+'</m:mrow></m:math>'
def mi(x):return '<m:mi>'+x+'</m:mi>'
def mn(x):return '<m:mn>'+x+'</m:mn>'
def mo(x):return '<m:mo>'+html.escape(x)+'</m:mo>'
def unit(x):return '<m:mtext>'+x+'</m:mtext>'
def power(x,n):return '<m:msup>'+x+mn(n)+'</m:msup>'
gap='<m:mspace width="0.167em"/>'
def scientific(a,n,u=''):
    return mn(a)+mo('×')+power(mn('10'),n)+(gap+unit(u) if u else '')

def markup(s):
    # Explicit expressions from the approved prose draft; numbers/units in prose
    # use nonbreaking spaces, while mathematical relations use native MathML.
    replacements={
        'e = 1.60 × 10⁻¹⁹ C':mi('e')+mo('=')+scientific('1.60','−19','C'),
        'k = 8.99 × 10⁹ N·m²/C²':mi('k')+mo('=')+scientific('8.99','9')+gap+'<m:mfrac><m:mrow>'+unit('N')+mo('·')+power(unit('m'),'2')+'</m:mrow>'+power(unit('C'),'2')+'</m:mfrac>',
        '2.0 × 10¹⁰':scientific('2.0','10'),
        '6.0 × 10⁻⁴ N':scientific('6.0','−4','N'),
        'P = V²/R':mi('P')+mo('=')+'<m:mfrac>'+power(mi('V'),'2')+mi('R')+'</m:mfrac>',
        'P = I²R':mi('P')+mo('=')+power(mi('I'),'2')+mi('R'),
        '1 W = 1 J/s':mn('1')+gap+unit('W')+mo('=')+mn('1')+gap+unit('J/s'),
        '1 kW·h = 3.60 × 10⁶ J':mn('1')+gap+unit('kW')+mo('·')+unit('h')+mo('=')+scientific('3.60','6','J'),
        '0 < x < L':mn('0')+mo('<')+mi('x')+mo('<')+mi('L'),
        'x < 0':mi('x')+mo('<')+mn('0'), 'x > L':mi('x')+mo('>')+mi('L'),
        'x = 0':mi('x')+mo('=')+mn('0'), 'x = L':mi('x')+mo('=')+mi('L'),
        '−4q':mo('−')+mn('4')+mi('q'), '−3q':mo('−')+mn('3')+mi('q'),
        '+2q':mo('+')+mn('2')+mi('q'), '+q':mo('+')+mi('q'), '−q':mo('−')+mi('q'),
        'q and L':None,
    }
    # Placeholder replacement avoids treating tags as prose or reprocessing math.
    saved=[]
    for phrase,body in replacements.items():
        if body is None:continue
        if phrase in s:
            key='@@MATH'+str(len(saved))+'@@';saved.append(math(body));s=s.replace(phrase,key)
    s=html.escape(s,quote=False)
    s=s.replace('q and L',math(mi('q'))+' and '+math(mi('L')))
    s=re.sub(r'(?<=\d) (?=(?:mA·h|N/C|m/s|kΩ|μC|μs|nC|cm|Ω|A|C|V|s|h|minute)(?:\b|[.,;) ]))','\u00a0',s)
    for i,value in enumerate(saved):s=s.replace('@@MATH'+str(i)+'@@',value)
    return s

for number,q in enumerate(proposal['questions'],1):
    mid=modules[q['section']]
    eid=old[q['old']]['id'] if q['old'] else 'ex-c9-'+re.sub('[^a-z0-9]+','-',q['title'].lower()).strip('-')
    if q['old'] and q['prompt']==old[q['old']]['text']:
        block=blocks[q['old']]
    else:
        paras=q['prompt'].split('\n\n')
        body='\n'.join(f'<para id="{eid}-revised-p{i}">{markup(p)}</para>' for i,p in enumerate(paras,1))
        block=f'<exercise id="{eid}" type="conceptual-questions"><problem id="{eid}-revised-problem">{body}</problem></exercise>'
    out[mid].append(block)
    manifest.append(dict(number=number,module=mid,id=eid,prior_number=q['old'],source_comparison=q['sources'],title=q['title']))

ledgerpath=ROOT/'maintained/editorial-changes.json'
ledger=json.loads(ledgerpath.read_text(encoding='utf-8'))
sha=lambda s:hashlib.sha256(s.encode()).hexdigest()
for mid,src in before.items():
    inserted=False
    def replace(m):
        global inserted
        if not isgroup(m[0]):return m[0]
        if inserted:return ''
        inserted=True
        opening=re.match(r'<section\b[^>]*>',m[0])[0]
        return opening+'<title>Questions and Exercises</title>\n'+'\n'.join(out[mid])+'\n</section>'
    result=groups.sub(replace,src)
    assert inserted
    # Outside chapter-end exercise sections, source must be byte-for-byte unchanged.
    clean=lambda s:groups.sub(lambda m:'' if isgroup(m[0]) else m[0],s).replace('\r\n','\n').strip()
    # Removing a second group leaves its surrounding whitespace intact.
    assert re.sub(r'\s+',' ',clean(src))==re.sub(r'\s+',' ',clean(result)),mid
    E.fromstring(result)
    key='EX-C9-CURATION-'+mid
    patch='proposals/author-corrections/'+key+'.json'
    assert patch not in ledger['changes']
    record=dict(id=key,status='applied-maintainer-approved',target_release='cp2e-ver1.1',module=mid,source_path=f'maintained/modules/{mid}/index.cnxml',source_sha256=sha(src),after_sha256=sha(result),before=src,after=result,reason='Approved 55-question Chapter 9 selection, revisions, MyOpenMath adaptations, and topic ordering. Answers remain in internal reports only. Section body and summaries unchanged by this patch.')
    (ROOT/patch).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (ROOT/f'maintained/modules/{mid}/index.cnxml').write_text(result,encoding='utf-8')
    ledger['changes'].append(patch)
ledgerpath.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(report/'applied-question-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert sum(len(x) for x in out.values())==55
print('Applied 55 questions across 11 sections; preserved all non-exercise content.')
