from pathlib import Path
import json,re
from pypdf import PdfReader,PdfWriter
from pypdf.generic import DictionaryObject,NameObject,TextStringObject,ArrayObject,NumberObject,BooleanObject
ROOT=Path(__file__).resolve().parents[2];qa=ROOT/'reports/1.1/front-matter-print'
targets=json.loads((ROOT/'reports/1.1/index-print/entries.json').read_text(encoding='utf-8'))['targets']
for name,filename in [('index','v1.1-index.pdf'),('book-licensing','v1.1-licensing-attribution.pdf')]:
    r=json.loads((ROOT/f'reports/1.1/{name}-print/layout.json').read_text())
    for i in range(r['pages']):targets[str(r['startPage']+i)]=dict(file=filename,pageIndex=i)
writer=PdfWriter();writer.clone_document_from_reader(PdfReader(qa/'toc-preface-unlinked.pdf'));manifest=[]
for i,p in enumerate(writer.pages):
    for ref in p.get('/Annots',[]):
        a=ref.get_object();action=a.get('/A',{})
        m=re.fullmatch(r'https://book-front.invalid/body/(\d+)',str(action.get('/URI','')))
        if not m:continue
        bookpage=int(m[1]);target=targets[str(bookpage)]
        a[NameObject('/A')]=DictionaryObject({NameObject('/S'):NameObject('/GoToR'),NameObject('/F'):TextStringObject(target['file']),NameObject('/D'):ArrayObject([NumberObject(target['pageIndex']),NameObject('/Fit')]),NameObject('/NewWindow'):BooleanObject(True)})
        manifest.append(dict(frontMatterPage=i,rect=list(map(float,a['/Rect'])),bookPage=bookpage,**target))
writer.add_metadata({'/Title':'Contents and Preface - Introduction to Physics, Version 1.1'})
with (ROOT/'output/pdf/v1.1-toc-and-preface.pdf').open('wb') as f:writer.write(f)
(qa/'link-manifest.json').write_text(json.dumps(manifest,indent=2))
print('Linked',len(manifest),'body-page annotations')
