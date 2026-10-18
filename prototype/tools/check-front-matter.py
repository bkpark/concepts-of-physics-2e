from pathlib import Path
import json,unicodedata
from lxml import html
from pypdf import PdfReader
import pdfplumber
ROOT=Path(__file__).resolve().parents[2];qa=ROOT/'reports/1.1/front-matter-print'
data=json.loads((qa/'source.json').read_text(encoding='utf-8'));layout=json.loads((qa/'layout.json').read_text(encoding='utf-8'))
manifest=json.loads((qa/'link-manifest.json').read_text());targets={m['bookPage']:m for m in manifest}
norm=lambda s:''.join(c for c in unicodedata.normalize('NFKD',s).casefold() if c.isalnum())
readers={};cache={};mismatches=[]
for ch in data['chapters']:
    for sec in ch['sections']:
        t=targets[sec['page']];fn=t['file']
        if fn not in readers:readers[fn]=PdfReader(ROOT/'output/pdf'/fn)
        if sec['page'] not in cache:cache[sec['page']]=norm(readers[fn].pages[t['pageIndex']].extract_text())
        if norm(sec['title']) not in cache[sec['page']]:mismatches.append(sec)
reader=PdfReader(ROOT/'output/pdf/v1.1-toc-and-preface.pdf')
doc=html.fromstring((ROOT/'prototype/dist/course-full/toc-preface-print.html').read_text(encoding='utf-8'))
sheets=doc.xpath('//*[contains(concat(" ",@class," ")," sheet ")]')
assert len(reader.pages)==len(sheets)==layout['pages']
margin=[];missing=[];remote=0;internal=0;urls=0
with pdfplumber.open(ROOT/'output/pdf/v1.1-toc-and-preface.pdf') as pdf:
    for i,p in enumerate(pdf.pages):
        assert(p.width,p.height)==(612,792)
        lo,hi=(72,565.2) if i%2==0 else (46.8,540)
        margin += [dict(page=i,word=w) for w in p.extract_words() if w['x0']<lo-1 or w['x1']>hi+1 or w['top']<18 or w['bottom']>774]
        text=norm(reader.pages[i].extract_text())
        for e in sheets[i].xpath('.//h1 | .//h2 | .//h3 | .//*[@class="para"] | .//footer/p | .//a[contains(@class,"toc-row")]'):
            if norm(e.text_content()) not in text:missing.append(dict(page=i,text=e.text_content()))
        for ref in reader.pages[i].get('/Annots',[]):
            a=ref.get_object();action=a.get('/A',{})
            if action.get('/S')=='/GoToR':
                fn=str(action['/F']);idx=int(action['/D'][0])
                if fn not in readers:readers[fn]=PdfReader(ROOT/'output/pdf'/fn)
                assert 0<=idx<len(readers[fn].pages)
                remote+=1
            elif '/Dest' in a:
                destination=reader.named_destinations[str(a['/Dest'])]
                target_page=reader.get_destination_page_number(destination)
                assert layout['tocPages']<=target_page<layout['pages']
                internal+=1
            elif action.get('/S')=='/URI':urls+=1
            else:raise AssertionError(str(a))
assert remote==layout['bodyLinks']
assert not margin and not missing and not mismatches,(margin,missing,mismatches)
report=dict(pages=len(reader.pages),tocRoman='iii-viii',prefaceRoman='ix-x',bodyPageLinks=remote,prefaceLinks=internal,externalLinks=urls,sectionTitlePageMismatches=mismatches,marginIssues=margin,missingContent=missing)
(qa/'pdf-check.json').write_text(json.dumps(report,indent=2));print(json.dumps(report))
