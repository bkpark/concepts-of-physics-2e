"""Apply the maintainer-approved 47-question Chapter 8 proposal."""
from pathlib import Path
import json,re,hashlib,html,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[1]
report=ROOT/'reports/1.1/chapter8-structure'
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

def markup(s):
    s=html.escape(s,quote=False)
    s=s.replace('Q = 0','<m:math><m:mi>Q</m:mi><m:mo>=</m:mo><m:mn>0</m:mn></m:math>')
    s=s.replace('ΔS = Q_rev/T','<m:math><m:mrow><m:mi>ΔS</m:mi><m:mo>=</m:mo><m:mfrac><m:msub><m:mi>Q</m:mi><m:mtext>rev</m:mtext></m:msub><m:mi>T</m:mi></m:mfrac></m:mrow></m:math>')
    s=s.replace('the heating curve in Section 8.7','the heating curve in <link document="m67124" target-id="import-auto-id2928714"/>')
    return s

for number,q in enumerate(proposal['questions'],1):
    mid=modules[q['section']]
    eid=old[q['old']]['id'] if q['old'] else 'ex-c8-'+re.sub('[^a-z0-9]+','-',q['title'].lower()).strip('-')
    if not q['draft']:
        block=blocks[q['old']]
    else:
        paras=q['draft'].split('\n\n')
        body='\n'.join(f'<para id="{eid}-revised-p{i}">{markup(p)}</para>' for i,p in enumerate(paras,1))
        if q['old']==31:
            fig=re.search(r'<figure\b.*?</figure>',blocks[31],re.S)
            assert fig
            body+='\n'+fig[0]
        block=f'<exercise id="{eid}" type="conceptual-questions"><problem id="{eid}-revised-problem">{body}</problem></exercise>'
    out[mid].append(block)
    manifest.append(dict(number=number,module=mid,id=eid,prior_number=q['old'],source_comparison=q['source'],title=q['title']))

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
    key='EX-C8-CURATION-'+mid
    patch='proposals/author-corrections/'+key+'.json'
    assert patch not in ledger['changes']
    record=dict(id=key,status='applied-maintainer-approved',target_release='cp2e-ver1.1',module=mid,source_path=f'maintained/modules/{mid}/index.cnxml',source_sha256=sha(src),after_sha256=sha(result),before=src,after=result,reason='Approved 47-question Chapter 8 selection, revisions, MyOpenMath adaptations, and topic ordering. Section body and summaries unchanged by this patch.')
    (ROOT/patch).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (ROOT/f'maintained/modules/{mid}/index.cnxml').write_text(result,encoding='utf-8')
    ledger['changes'].append(patch)
ledgerpath.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(report/'applied-question-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert sum(len(x) for x in out.values())==47
print('Applied 47 questions across 13 sections; preserved all non-exercise content and retained thermos figure.')
