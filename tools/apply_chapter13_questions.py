"""Apply the approved 41-question Chapter 13 review set, without publishing."""
from pathlib import Path
import collections, hashlib, html, json, re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'reports/1.1/chapter13-structure'
C = '{http://cnx.rice.edu/cnxml}'
M = '{http://www.w3.org/1998/Math/MathML}'
def read(p): return p.read_text(encoding='utf-8')
def save(p, data): p.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
proposal = json.loads(read(OUT/'question-set-proposal.json'))
inventory = json.loads(read(OUT/'exercise-inventory.json'))
old = {int(q['number']): q for q in inventory}
modules = {q['section']: q['module'] for q in inventory}
modules['Chapter review'] = 'm42546'
byid = {q['draft_id']: q for q in proposal['proposed_questions']}
order = '''P02 P03 P05 P01 A1 P04
A2 P07 P06 A3 A6 A4 P08 G1 P11 G3 P14 G2 P12 P13 P15 P09 P10
P16 A5 P19 P21 P17 P18 P20
P24 P25 P23 P22 P26 P27 P28 P29 P30 A7 A8'''.split()
questions = [byid['C13-'+key] for key in order]
assert len(questions) == len(set(order)) == len(byid) == 41
byid['C13-P24']['prompt'] = byid['C13-P24']['prompt'].replace('for the preceding spacecraft problem', 'for a spacecraft moving at a substantial fraction of c')
# Keep the diagram question self-contained and identify it as an extension.
byid['C13-A6']['prompt'] = 'Extension: '+byid['C13-A6']['prompt']

def row(x): return '<m:mrow>'+x+'</m:mrow>'
def mi(x): return '<m:mi>'+x+'</m:mi>'
def mn(x): return '<m:mn>'+x+'</m:mn>'
def mo(x): return '<m:mo>'+html.escape(x)+'</m:mo>'
def power(x,n): return '<m:msup>'+x+mn(n)+'</m:msup>'
def frac(a,b): return '<m:mfrac>'+row(a)+row(b)+'</m:mfrac>'
def sqrt(x): return '<m:msqrt>'+row(x)+'</m:msqrt>'
def math(x): return '<m:math xmlns:m="'+M[1:-1]+'">'+row(x)+'</m:math>'
def parens(x): return row('<m:mo form="prefix" stretchy="false">(</m:mo>'+x+'<m:mo form="postfix" stretchy="false">)</m:mo>')
def sci(a,n,unit=''):
    return mn(a)+mo('×')+power(mn('10'),n)+('<m:mspace width="0.167em"/><m:mtext>'+unit+'</m:mtext>' if unit else '')
v,c,g,b,u = [mi(x) for x in ['v','c','γ','β','u']]
up = '<m:msup>'+u+'<m:mo>′</m:mo></m:msup>'
expressions = {
 'γ = 1/√(1 − v²/c²)':g+mo('=')+frac(mn('1'),sqrt(mn('1')+mo('−')+frac(power(v,'2'),power(c,'2')))),
 'γ = 1/√(1 − β²)':g+mo('=')+frac(mn('1'),sqrt(mn('1')+mo('−')+power(b,'2'))),
 'β = v/c':b+mo('=')+frac(v,c),
 'v/c = √(1 − 1/γ²)':frac(v,c)+mo('=')+sqrt(mn('1')+mo('−')+frac(mn('1'),power(g,'2'))),
 'γ = 1 + 5 × 10⁻¹⁵':g+mo('=')+mn('1')+mo('+')+sci('5','−15'),
 'γ − 1 ≈ β²/2':g+mo('−')+mn('1')+mo('≈')+frac(power(b,'2'),mn('2')),
 'c = 3.00 × 10⁸ m/s':c+mo('=')+sci('3.00','8','m/s'),
 '9.11 × 10⁻³¹ kg':sci('9.11','−31','kg'),
 'u = (v + u′)/(1 + vu′/c²)':u+mo('=')+frac(v+mo('+')+up,mn('1')+mo('+')+frac(v+up,power(c,'2'))),
 'u′ = −c':up+mo('=')+mo('−')+c,
 'u′ = c':up+mo('=')+c,
 '|v| < c':mo('|')+v+mo('|')+mo('<')+c,
 'p = γmv':mi('p')+mo('=')+g+mi('m')+v,
 'E² = (pc)² + (mc²)²':power(mi('E'),'2')+mo('=')+power(parens(mi('p')+c),'2')+mo('+')+power(parens(mi('m')+power(c,'2')),'2'),
 'c + v':c+mo('+')+v,
}
def markup(text):
    saved = []
    def stash(body):
        key = '@@MATH'+str(len(saved))+'@@';saved.append(math(body));return key
    for phrase,body in sorted(expressions.items(),key=lambda x:-len(x[0])):
        if phrase in text:text=text.replace(phrase,stash(body))
    # Relations to decimal values and speeds, followed by remaining bare speeds.
    text=re.sub(r'([γβv]) = (\d+(?:\.\d+)?)(c?)',lambda m:stash(mi(m[1])+mo('=')+mn(m[2])+(c if m[3] else '')),text)
    text=re.sub(r'(?<![\w.])(\d+(?:\.\d+)?)c\b',lambda m:stash(mn(m[1])+c),text)
    text=re.sub(r'(?<!\w)(γ|β|ct|mv|v|c|x)(?!\w)',lambda m:stash(''.join(mi(x) for x in m[1])),text)
    text=html.escape(text,quote=False)
    text=re.sub(r'(?<=\d) (?=(?:m/s|μs|h|m)(?:\b|[.,;)]))','\u00a0',text)
    for i,value in enumerate(saved):text=text.replace('@@MATH'+str(i)+'@@',value)
    assert '@@MATH' not in text
    return text

before={mid:read(ROOT/f'maintained/modules/{mid}/index.cnxml') for mid in set(modules.values())}
blocks={mid:[] for mid in before}
keepers={int(q['number']) for q in proposal['existing_dispositions'] if q['action']=='retain/revise'}
manifest=[]
for number,q in enumerate(questions,1):
    mid=modules[q['section']]
    kept=[n for n in q['current_numbers'] if n in keepers]
    assert len(kept)<=1
    eid=old[kept[0]]['id'] if kept else 'c13-mom-'+q['draft_id'].lower()
    problemid=eid+'-review-problem';paraid=eid+'-review-p1'
    body='<para id="'+paraid+'">'+markup(q['prompt'])+'</para>'
    blocks[mid].append(f'<exercise id="{eid}" type="conceptual-questions"><problem id="{problemid}">{body}</problem></exercise>')
    manifest.append({**q,'number':number,'proposed_number':number,'module':mid,'id':eid,'retained_prior_number':kept[0] if kept else None,'source_comparison':q['mom_export_locators']})

group_pattern=re.compile(r'<section\b[^>]*>(?:(?!<section\b).)*?</section>',re.S)
ledgerpath=ROOT/'maintained/editorial-changes.json';ledger=json.loads(read(ledgerpath))
for mid,src in before.items():
    inserted=False
    def replace(match):
        global inserted
        block=match[0]
        if '<title>Questions and Exercises</title>' not in block:return block
        if inserted:return ''
        inserted=True
        opening=block[:block.index('>')+1]
        return opening+'<title>Questions and Exercises</title>\n'+'\n'.join(blocks[mid])+'\n</section>'
    after=group_pattern.sub(replace,src);assert inserted
    a=ET.fromstring(src);z=ET.fromstring(after)
    ids=[e.get('id') for e in z.iter() if e.get('id')];assert len(ids)==len(set(ids))
    # Verify that every body paragraph/example and inline check stays untouched.
    def without_groups(root):
        for parent in root.iter():
            for child in list(parent):
                title=child.find(C+'title')
                if child.tag==C+'section' and title is not None and title.text=='Questions and Exercises':parent.remove(child)
        for e in root.iter():
            if e.text is not None and not e.text.strip():e.text=None
            if e.tail is not None and not e.tail.strip():e.tail=None
        return ET.tostring(root,encoding='unicode')
    assert without_groups(a)==without_groups(ET.fromstring(after)),mid
    assert len(list(z.iter(C+'exercise')))==len(blocks[mid])+sum(1 for e in a.iter(C+'exercise'))
    rid='EX-C13-APPROVED-QUESTION-SET-'+mid
    path=Path('proposals/author-corrections')/(rid+'.json');assert path.as_posix() not in ledger['changes']
    save(ROOT/path,dict(id=rid,status='applied-maintainer-approved',target_release='cp2e-ver1.1',module=mid,source_path=f'maintained/modules/{mid}/index.cnxml',source_sha256=hashlib.sha256(src.encode()).hexdigest(),after_sha256=hashlib.sha256(after.encode()).hexdigest(),before=src,after=after,reason='Apply user-approved 41-question Chapter 13 set, expanded MyOpenMath conceptual coverage, native MathML and textbook topic ordering. Preserve all section body content and inline checks.'))
    (ROOT/f'maintained/modules/{mid}/index.cnxml').write_text(after,encoding='utf-8');ledger['changes'].append(path.as_posix())
save(ledgerpath,ledger)
save(OUT/'applied-question-set.json',{'status':'applied; pending preview refresh and maintainer review','count':41,'questions':manifest,'inline_checks_preserved':5,'answers':'Internal editorial checks only; no new public solution key added.'})
# Retain the proposal as the historical review record, with an explicit applied crosswalk.
save(OUT/'applied-number-crosswalk.json',[{'number':q['number'],'draft_id':q['draft_id'],'id':q['id'],'module':q['module'],'current_numbers':q['current_numbers']} for q in manifest])
print('Applied 41 chapter-end questions across six modules; five inline checks preserved.')
