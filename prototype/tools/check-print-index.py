from pathlib import Path
import json,re,unicodedata
from lxml import html
import pdfplumber
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[2];qa=ROOT/'reports/1.1/index-print'
layout=json.loads((qa/'layout.json').read_text());data=json.loads((qa/'entries.json').read_text(encoding='utf-8'))
doc=html.fromstring((ROOT/'prototype/dist/course-full/index-print.html').read_text(encoding='utf-8'))
sheets=doc.xpath('//*[@class="sheet"]');reader=PdfReader(ROOT/'output/pdf/v1.1-index.pdf')
normalize=lambda s:''.join(c for c in unicodedata.normalize('NFKD',s).casefold() if c.isalnum())
errors=[];missing=[];remote=0;internal=0;destinations=reader.named_destinations;targets={}
assert len(reader.pages)==layout['pages']==len(sheets)
with pdfplumber.open(ROOT/'output/pdf/v1.1-index.pdf') as pdf:
    for i,page in enumerate(pdf.pages):
        assert(page.width,page.height)==(612,792)
        lo,hi=(72,565.2) if (layout['startPage']+i)%2 else (46.8,540)
        for word in page.extract_words():
            if word['x0']<lo-1 or word['x1']>hi+1 or word['top']<18 or word['bottom']>774:errors.append(dict(page=i,word=word))
        text=normalize(reader.pages[i].extract_text())
        for row in sheets[i].xpath('.//*[@class="entry"]'):
            if normalize(row.text_content()) not in text:missing.append(row.text_content())
        for ref in reader.pages[i].get('/Annots',[]):
            a=ref.get_object();action=a.get('/A',{})
            if action.get('/S')=='/GoToR':
                filename=str(action['/F']);p=int(action['/D'][0])
                if filename not in targets:targets[filename]=len(PdfReader(ROOT/'output/pdf'/filename).pages)
                assert 0<=p<targets[filename],(filename,p)
                remote+=1
            elif '/Dest' in a:
                assert str(a['/Dest']) in destinations,a['/Dest']
                internal+=1
            else:raise AssertionError(str(a))
assert remote==layout['pageLinks']
assert not errors and not missing,(errors,missing)
audit=json.loads((qa/'source-audit.json').read_text(encoding='utf-8'))
assert not audit['missingGlossary'] and not audit['unverifiedPdfText']
report=dict(pages=len(reader.pages),startPage=layout['startPage'],endPage=layout['startPage']+len(reader.pages)-1,entries=layout['entries'],glossaryTerms=audit['glossaryTerms'],verifiedPageLinks=remote,verifiedInternalLinkRectangles=internal,marginIssues=errors,missingEntries=missing)
(qa/'pdf-check.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report))
