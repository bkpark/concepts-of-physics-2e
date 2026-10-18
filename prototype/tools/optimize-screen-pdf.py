"""Conservative screen PDF: retain all pixel dimensions and document objects.

Try lossless PNG prediction and high-quality JPEG with no chroma subsampling.
Accept JPEG only against decoded source pixels within strict error thresholds.
Keep originals when compression offers no benefit or image semantics are unusual.
"""
from pathlib import Path
from io import BytesIO
import json, hashlib, math, struct
import numpy as np
from PIL import Image
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, NumberObject, DictionaryObject
from pypdf.generic._image_xobject import _xobj_to_image

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'output/pdf/v1.1-complete-book.pdf'
OUTPUT=ROOT/'output/pdf/v1.1-complete-book-screen.pdf'
QA=ROOT/'reports/1.1/screen-pdf';QA.mkdir(parents=True,exist_ok=True)
before_hash=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
writer=PdfWriter(clone_from=SOURCE)
pages={}
def visit(resources,page,seen):
    for ref in resources.get('/XObject',{}).values():
        obj=ref.get_object();num=obj.indirect_reference.idnum
        if num in seen:continue
        seen.add(num)
        if obj.get('/Subtype')=='/Image':pages.setdefault(num,[]).append(page)
        elif '/Resources' in obj:visit(obj['/Resources'],page,seen)
for n,page in enumerate(writer.pages):visit(page['/Resources'],n+1,set())
records=[]
# Reviewed photographic images from the retained-image contact sheet. Mixed
# diagrams, scientific plots and images with important lettering stay strict.
photographs={121,331,357,461,496,596,683,852,876,931,1109,1131,1139,
1318,1444,1494,1670,1693,1718,1839,1847,2076,2167,2205,2284,2310,
2354,2609,2626,2748,2761,2777,2792,2798,2846,2857,2949,2965,2973,
2981,3560,3568,3605,3643,3669,3671,3713,3715,3781,3930,3974,4083,
4092,4331,4338,4353,4467,4507,4511,4513,4814,4919,5076,5086,5179,
5208,5441,5545,5558}
for obj in list(writer._objects):
    if not isinstance(obj,DictionaryObject) or obj.get('/Subtype')!='/Image':continue
    n=obj.indirect_reference.idnum
    if not pages.get(n):continue # Masks are retained unchanged.
    old=len(obj._data)
    record=dict(object=n,pages=pages[n],before=old,width=int(obj['/Width']),height=int(obj['/Height']))
    records.append(record)
    if any(k in obj for k in ['/SMask','/Mask','/Decode']) or obj.get('/ImageMask') or obj.get('/BitsPerComponent')!=8:
        record.update(after=old,method='original-special');continue
    ext,data,im=_xobj_to_image(obj)
    if im.mode not in ('RGB','L'):
        record.update(after=old,method='original-color');continue
    original=np.array(im).astype(np.int16)
    channels=3 if im.mode=='RGB' else 1
    # A lossless PNG IDAT stream can be used directly with PDF PNG prediction.
    buf=BytesIO();im.save(buf,format='PNG',optimize=True)
    png=buf.getvalue();pos=8;idat=b''
    while pos<len(png):
        size=struct.unpack('>I',png[pos:pos+4])[0];typ=png[pos+4:pos+8]
        if typ==b'IDAT':idat+=png[pos+8:pos+8+size]
        pos+=size+12
    candidates=[(old,'original',None,{})]
    candidates.append((len(idat),'lossless',idat,{}))
    photographic=n in photographs
    record['profile']='photograph' if photographic else 'fine-detail'
    for quality in ((92,95,97,99) if photographic else (90,93,95,97)):
        buf=BytesIO();im.save(buf,format='JPEG',quality=quality,subsampling=0,optimize=True)
        jpg=buf.getvalue()
        if len(jpg)>=min(c[0] for c in candidates):break
        decoded=np.array(Image.open(BytesIO(jpg))).astype(np.int16)
        delta=np.abs(original-decoded)
        mse=float(np.mean(delta.astype(np.float32)**2));psnr=99 if mse==0 else 10*math.log10(255**2/mse)
        mae=float(np.mean(delta));p99=float(np.percentile(delta,99))
        if psnr>=(40 if photographic else 43) and mae<=(1.6 if photographic else 0.85) and p99<=(10 if photographic else 6):
            candidates.append((len(jpg),'jpeg',jpg,dict(quality=quality,psnr=round(psnr,3),meanAbsoluteError=round(mae,4),p99=p99)))
            break
    size,method,payload,metrics=min(candidates,key=lambda c:c[0])
    if size>old*.98:method='original';size=old
    record.update(after=size,method=method,**metrics)
    if method!='original':
        obj._data=payload
        if hasattr(obj,'decoded_self'):obj.decoded_self=None
        for k in ['/DecodeParms','/ColorTransform']:
            obj.pop(NameObject(k),None)
        obj[NameObject('/Filter')]=NameObject('/DCTDecode' if method=='jpeg' else '/FlateDecode')
        if method=='lossless':
            obj[NameObject('/DecodeParms')]=DictionaryObject({NameObject('/Predictor'):NumberObject(15),NameObject('/Colors'):NumberObject(channels),NameObject('/BitsPerComponent'):NumberObject(8),NameObject('/Columns'):NumberObject(im.width)})
    if len(records)%50==0:print('Processed',len(records),'images',flush=True)
writer.compress_identical_objects(remove_duplicates=True,remove_unreferenced=True)
with OUTPUT.open('wb') as f:writer.write(f)
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==before_hash
report=dict(source=str(SOURCE),output=str(OUTPUT),sourceSHA256=before_hash,outputSHA256=hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),sourceBytes=SOURCE.stat().st_size,outputBytes=OUTPUT.stat().st_size,pixelDimensionsUnchanged=True,images=records)
(QA/'optimization.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='images'}))
