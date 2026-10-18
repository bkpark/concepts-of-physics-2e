"""Build a traceable subject index from the accepted explicit-page print files."""
from pathlib import Path
from collections import defaultdict
import json,re,unicodedata
from lxml import html
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[2]
DIST=ROOT/'prototype/dist/course-full'
QA=ROOT/'reports/1.1/index-print'
QA.mkdir(parents=True,exist_ok=True)
words='zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen'.split()
clean=lambda s:' '.join(s.split()).strip()
def key(s):
    return clean(s).replace('\u2019',"'").replace('\u2013','-').replace('\u2011','-').casefold()
def pdfkey(s):
    return ''.join(c for c in unicodedata.normalize('NFKD',s).casefold() if c.isalnum())
entries={}; targets={}; sources=[]; pdftexts={}
def add(term,page,kind,node_id=None):
    term=clean(term)
    if not term:return
    k=key(term)
    e=entries.setdefault(k,dict(term=term,refs=[],evidence=[]))
    # Prefer normal prose capitalization to a heading's title case.
    if kind=='term' and term[:1].islower():e['term']=term
    if page not in e['refs']:e['refs'].append(page)
    e['evidence'].append(dict(page=page,text=term,kind=kind,id=node_id))

for i,w in enumerate(words):
    name=f'chapter-{i}'
    report=json.loads((ROOT/f'reports/1.1/{name}-print/layout.json').read_text())
    pdf=f'v1.1-chapter-{i}.pdf' if i else 'v1.1-chapter-0-revised.pdf'
    sources.append((name,f'chapter-{w}-print.html',pdf,report))
for letter in 'abcd':
    name=f'appendix-{letter}'
    report=json.loads((ROOT/f'reports/1.1/{name}-print/layout.json').read_text())
    sources.append((name,f'{name}-print.html',f'v1.1-{name}.pdf',report))
for name,filename,pdf,report in sources:
    doc=html.fromstring((DIST/filename).read_text(encoding='utf-8'))
    sheets=doc.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," sheet ")]')
    reader=PdfReader(ROOT/'output/pdf'/pdf)
    assert len(sheets)==report['pages']==len(reader.pages),(name,len(sheets),report['pages'])
    for offset,sheet in enumerate(sheets):
        page=report.get('startPage',1)+offset
        folio=sheet.xpath('.//*[@class="folio"]/text()')
        assert folio and int(folio[0])==page,(name,page,folio)
        targets[page]=dict(file=pdf,pageIndex=offset)
        pdftexts[page]=pdfkey(reader.pages[offset].extract_text())
        for node in sheet.xpath('.//dfn'):
            add(node.text_content(),page,'term',node.get('id'))
        if name.startswith('chapter'):
            for node in sheet.xpath('.//h1'):
                h=html.fromstring(html.tostring(node))
                for small in h.xpath('./small'):small.drop_tree()
                title=clean(h.text_content())
                if title in ['Sources and adaptations','Chapter Review','Chapter review'] or re.search(r'Questions|Exercises|Summary|Glossary',title):continue
                if title.startswith('Introduction to '):title=title[len('Introduction to '):]
                add(title,page,'heading',node.get('id'))
        else:
            for node in sheet.xpath('.//caption | .//h1'):
                title=clean(node.text_content()).split('[Note:')[0].strip()
                title=re.sub(r'^Table [A-D]\.\d+\.\s*','',title).replace(' (continued)','')
                if title:add(title,page,'reference',node.get('id'))
    print(name,'checked',len(sheets),'pages',flush=True)

# Consolidate only straightforward plural variants already present as singular entries.
for k in list(entries):
    singular=k[:-1] if k.endswith('s') and not k.endswith('ss') else None
    if singular and singular in entries:
        a=entries[singular];b=entries.pop(k)
        a['refs']=sorted(set(a['refs']+b['refs']));a['evidence']+=b['evidence']

editorial=json.loads((ROOT/'prototype/tools/print-index-editorial.json').read_text(encoding='utf-8'))
for old,new in editorial['rename'].items():
    if key(old)==key(new):continue
    assert key(old) in entries,old
    b=entries.pop(key(old));a=entries.setdefault(key(new),dict(term=new,refs=[],evidence=[]))
    a['refs']=sorted(set(a['refs']+b['refs']));a['evidence']+=b['evidence']
for term,target in editorial['see'].items():
    assert key(target) in entries,target
    assert key(term) not in entries,term
    entries[key(term)]=dict(term=term,refs=[],evidence=[],see=entries[key(target)]['term'])

book=html.fromstring((DIST/'book.html').read_text(encoding='utf-8'))
glossary={key(x.text_content()):clean(x.text_content()) for x in book.xpath('//section[@class="glossary"]//dfn')}
covered={key(v['text']) for e in entries.values() for v in e['evidence']}
missing={k:v for k,v in glossary.items() if k not in covered}

unverified=[]
for e in entries.values():
    e['refs'].sort()
    for ev in e['evidence']:
        # Reference-table captions may have notes removed above; verify the indexed title itself.
        if pdfkey(ev['text']) not in pdftexts[ev['page']]:unverified.append(ev)
result=dict(startPage=max(targets)+1,entries=sorted(entries.values(),key=lambda e:re.sub(r'[^a-z0-9]','',key(e['term']))),targets=targets)
(QA/'entries.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
(QA/'source-audit.json').write_text(json.dumps(dict(sourcePages=len(targets),entries=len(entries),glossaryTerms=len(glossary),missingGlossary=missing,unverifiedPdfText=unverified),ensure_ascii=False,indent=2),encoding='utf-8')
print('entries',len(entries),'missing glossary',len(missing),'unverified',len(unverified))
