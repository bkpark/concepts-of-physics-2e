"""Validate screen proof structure and render 200% comparisons."""
from pathlib import Path
import json,hashlib,subprocess
from pypdf import PdfReader
from PIL import Image
import numpy as np
ROOT=Path(__file__).resolve().parents[2];QA=ROOT/'reports/1.1/screen-pdf'
data=json.loads((QA/'optimization.json').read_text(encoding='utf-8'))
a=PdfReader(data['source']);b=PdfReader(data['output'])
assert len(a.pages)==len(b.pages)==654
assert a.page_labels==b.page_labels
def signature(reader):
    ids={p.indirect_reference.idnum:i for i,p in enumerate(reader.pages)}
    result=[]
    for n,p in enumerate(reader.pages):
        for ref in p.get('/Annots',[]):
            obj=ref.get_object()
            dest=obj.get('/Dest');action=obj.get('/A',{})
            result.append([n,list(obj['/Rect']),[ids[dest[0].idnum],str(dest[1]),str(dest[2:])] if dest else [str(action)]])
    return result
assert signature(a)==signature(b)
def outlines(reader,items):
    result=[]
    for item in items:
        if isinstance(item,list):result.append(outlines(reader,item))
        else:result.append([item.title,reader.get_destination_page_number(item)])
    return result
assert outlines(a,a.outline)==outlines(b,b.outline)
for x,y in zip(a.pages,b.pages):
    assert x.mediabox==y.mediabox
    xc=x.get_contents();yc=y.get_contents()
    assert (xc.get_data() if xc is not None else b'')==(yc.get_data() if yc is not None else b'')
assert hashlib.sha256(Path(data['source']).read_bytes()).hexdigest()==data['sourceSHA256']
jpegs=[r for r in data['images'] if r['method']=='jpeg']
worst=sorted(jpegs,key=lambda x:x['psnr'])[:4]
biggest=sorted(jpegs,key=lambda x:x['before']-x['after'],reverse=True)[:4]
details=sorted([r for r in jpegs if r.get('profile')=='fine-detail'],key=lambda x:x['psnr'])[:2]
pages=sorted(set([r['pages'][0] for r in worst+biggest+details]+[13,458,497,602]))
pop='C:/Users/a/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe'
samples=[]
for n in pages:
    for label,path in [('original',data['source']),('screen',data['output'])]:
        subprocess.run([pop,'-f',str(n),'-l',str(n),'-r','192','-singlefile','-png',path,str(QA/f'{label}-{n}')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    x=np.array(Image.open(QA/f'original-{n}.png')).astype(np.int16)
    y=np.array(Image.open(QA/f'screen-{n}.png')).astype(np.int16)
    d=np.abs(x-y)
    samples.append(dict(pdfPage=n,meanAbsolutePixelError=float(np.mean(d)),p99=float(np.percentile(d,99)),maximumPixelError=int(np.max(d))))
    print('Rendered 200% comparison page',n,flush=True)
report=dict(pages=654,contentStreamsIdentical=True,pageLabelsIdentical=True,allLinkAnnotationsIdentical=True,bookmarkHierarchyIdentical=True,originalHashUnchanged=True,renderDPI=192,samples=samples)
(QA/'validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report))
