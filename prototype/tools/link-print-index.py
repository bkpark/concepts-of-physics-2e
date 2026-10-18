"""Link the standalone index to adjacent accepted PDFs; retain an assembly manifest."""
from pathlib import Path
import json,re
from pypdf import PdfReader,PdfWriter
from pypdf.generic import DictionaryObject,NameObject,TextStringObject,ArrayObject,NumberObject,NullObject,BooleanObject
ROOT=Path(__file__).resolve().parents[2];qa=ROOT/'reports/1.1/index-print'
data=json.loads((qa/'entries.json').read_text(encoding='utf-8'))
writer=PdfWriter();writer.clone_document_from_reader(PdfReader(qa/'index-unlinked.pdf'))
manifest=[]
for i,page in enumerate(writer.pages):
    for ref in page.get('/Annots',[]):
        annot=ref.get_object();action=annot.get('/A')
        if not action or action.get('/S')!='/URI':continue
        uri=str(action.get('/URI',''));match=re.fullmatch(r'https://book-index.invalid/page/(\d+)',uri)
        if not match:continue
        bookpage=int(match[1]);target=data['targets'][str(bookpage)]
        annot[NameObject('/A')]=DictionaryObject({NameObject('/S'):NameObject('/GoToR'),NameObject('/F'):TextStringObject(target['file']),NameObject('/D'):ArrayObject([NumberObject(target['pageIndex']),NameObject('/Fit')]),NameObject('/NewWindow'):BooleanObject(True)})
        manifest.append(dict(indexPage=i,rect=list(map(float,annot['/Rect'])),bookPage=bookpage,**target))
writer.add_metadata({'/Title':'Index - Concepts of Physics 2e'})
outfile=ROOT/'output/pdf/v1.1-index.pdf'
with outfile.open('wb') as f:writer.write(f)
report=json.loads((qa/'layout.json').read_text())
assert len(manifest)==report['pageLinks']
reopened=PdfReader(outfile)
links=[r.get_object() for p in reopened.pages for r in p.get('/Annots',[])]
assert sum(a.get('/A',{}).get('/S')=='/GoToR' for a in links)==len(manifest)
(qa/'link-manifest.json').write_text(json.dumps(manifest,indent=2))
print('Verified',len(manifest),'page links;',len(links)-len(manifest),'internal links')
