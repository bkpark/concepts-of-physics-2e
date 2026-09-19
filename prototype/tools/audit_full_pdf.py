from pathlib import Path
import pdfplumber,json,hashlib
from pypdf import PdfReader
p=Path('output/pdf/introduction-to-physics-course.pdf');out=Path('prototype/qa/course-full-pdf.json')
rows=[];fonts=set();mathchars=0
with pdfplumber.open(p) as pdf:
 for n,page in enumerate(pdf.pages,1):
  chars=page.chars; body=[c for c in chars if c['top']<745]
  outside=[c for c in body if c['x0']<35 or c['x1']>577 or c['top']<35 or c['bottom']>774]
  text=page.extract_text() or ''
  fonts.update(c['fontname'] for c in chars);mathchars+=sum('CambriaMath' in c['fontname'] for c in chars)
  rows.append({'page':n,'chars':len(body),'outside':len(outside),'outside_sample': ''.join(c['text'] for c in outside)[:100],'bottom':max((c['bottom'] for c in body),default=0),'start':text[:150],'images':len(page.images)})
  page.close()
  if n%100==0:print(n,flush=True)
reader=PdfReader(p);names=reader.named_destinations;page_ids={page.indirect_reference.idnum for page in reader.pages};bad_links=[];internal=external=0
for n,page in enumerate(reader.pages,1):
 for ref in page.get('/Annots',[]):
  annot=ref.get_object();action=annot.get('/A',{});dest=annot.get('/Dest',action.get('/D'))
  if dest is not None:
   internal+=1
   if isinstance(dest,str):
    if dest not in names:bad_links.append([n,str(dest)])
   elif dest[0].idnum not in page_ids:bad_links.append([n,str(dest)])
  elif action.get('/S')=='/URI':external+=1
report={'internal_links':internal,'external_links':external,'broken_pdf_links':bad_links,'tagged':bool(reader.trailer['/Root'].get('/StructTreeRoot')),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'pages':len(rows),'math_chars':mathchars,'fonts':sorted(fonts),'page_audit':rows}
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'pages':len(rows),'outside_pages':[r['page'] for r in rows if r['outside']],'sparse':[r['page'] for r in rows if r['chars']<100]},ensure_ascii=True))

assert not bad_links,bad_links
assert not any(r['outside'] for r in rows),'Text beyond page margins'
assert mathchars>50000,'Missing mathematical text layer'
