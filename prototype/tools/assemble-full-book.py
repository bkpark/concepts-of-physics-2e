"""Assemble approved proofs and restore links across their boundaries."""
from pathlib import Path
import json, re, hashlib
from urllib.parse import urlparse, unquote
from pypdf import PdfReader, PdfWriter
from pypdf.generic import DictionaryObject, ArrayObject, NameObject, FloatObject, NumberObject, NullObject
ROOT=Path(__file__).resolve().parents[2]
QA=ROOT/'reports/1.1/full-book'
load=lambda p:json.loads(p.read_text(encoding='utf-8'))
plan=load(QA/'components.json'); dom=load(QA/'dom-links.json')
front=load(ROOT/'reports/1.1/front-matter-print/source.json')
anchors={}; local={}
for d in dom:
    local[d['key']]={}
    for a in d['ids']:
        anchors.setdefault(a['id'],a); local[d['key']].setdefault(a['id'],a)
chapters={re.sub(r'[^a-z0-9]+','-',c['title'].lower()).strip('-'):c['page'] for c in front['chapters']}
def resolve(href,key):
    u=urlparse(href); fragment=unquote(u.fragment)
    internal=not u.netloc or u.netloc in ('book-index.invalid','book-front.invalid') or (u.netloc in ('intro-1-1.coaphys.xyz','intro.coaphys.xyz') and u.path.startswith(('/sections/','/exercises/','/chapters/')))
    if not internal:return False
    if u.netloc in ('book-index.invalid','book-front.invalid'):
        return dict(page=int(u.path.rstrip('/').split('/')[-1])+11,y=792)
    if fragment:
        a=local[key].get(fragment) or anchors.get(fragment) or plan['modules'].get(fragment)
        if a:return a
        return None
    bits=u.path.strip('/').split('/')
    if len(bits)>1 and bits[0]=='sections':return plan['modules'].get(plan['slugs'].get(bits[1]))
    if len(bits)>1 and bits[0]=='chapters' and bits[1] in chapters:return dict(page=chapters[bits[1]]+11,y=792)
    return None
resolved=[]; unresolved=[]
for d in dom:
    for link in d['links']:
        target=resolve(link['href'],d['key'])
        if target is None:unresolved.append(dict(key=d['key'],**link))
        elif target is not False:resolved.append(dict(key=d['key'],target=target,**link))
(QA/'unresolved-links.json').write_text(json.dumps(unresolved,indent=2),encoding='utf-8')
if unresolved:raise SystemExit(f'{len(unresolved)} unresolved links; inspect report')
writer=PdfWriter(); readers=[]; external=0
for part in plan['parts']:
    if 'pdf' not in part:writer.add_blank_page(612,792);continue
    path=ROOT/part['pdf'];assert hashlib.sha256(path.read_bytes()).hexdigest()==part['sha256']
    reader=PdfReader(path);readers.append(reader)
    for n in part.get('select',range(len(reader.pages))):
        page=writer.add_page(reader.pages[n]);keep=ArrayObject()
        for ref in page.get('/Annots',[]):
            a=ref.get_object();action=a.get('/A',{});uri=action.get('/URI')
            if uri and resolve(str(uri),part['key']) is False:keep.append(ref);external+=1
        page[NameObject('/Annots')]=keep
assert len(writer.pages)==plan['pages']
count=0
for link in resolved:
    t=link['target'];assert 0<=t['page']<len(writer.pages)
    for rect in link['rects']:
        assert all(-1<=v<=793 for v in rect),rect
        dest=ArrayObject([writer.pages[t['page']].indirect_reference,NameObject('/XYZ'),NullObject(),FloatObject(min(792,max(0,t['y']+8))),NullObject()])
        annotation=DictionaryObject({NameObject('/Type'):NameObject('/Annot'),NameObject('/Subtype'):NameObject('/Link'),NameObject('/Rect'):ArrayObject([FloatObject(v) for v in rect]),NameObject('/Border'):ArrayObject([NumberObject(0)]*3),NameObject('/Dest'):dest})
        writer.pages[link['page']]['/Annots'].append(writer._add_object(annotation));count+=1
bookmarks=[]
def bookmark(title,page,parent=None):
    bookmarks.append(dict(title=title,page=page))
    return writer.add_outline_item(title,page,parent=parent,is_open=False)
for title,p in [('Cover',0),('Title page',2),('Copyright',3),('Contents',4)]:bookmark(title,p)
pref=bookmark('Preface',10)
for title,p in [('About Version 1.1',10),('Original About This Book',11),('Preface to Concepts of Physics',11),('About OpenStax College',11)]:bookmark(title,p,pref)
unit=None
for c in front['chapters']:
    if c['unit']:unit=bookmark(c['unit'],c['page']+11)
    chap=bookmark(f"Chapter {c['number']}: {c['title']}",c['page']+11,unit)
    for s in c['sections']:bookmark((s['label']+' '+s['title']).strip(),s['page']+11,chap)
appendices=bookmark('Appendices',618)
for p in plan['parts']:
    if p['key'].startswith('appendix-'):bookmark('Appendix '+p['key'][-1].upper(),p['offset'],appendices)
bookmark('Index',644);lic=bookmark('Licensing and Attribution',652);bookmark('Sources and Adaptation History',653,lic)
writer.set_page_label(0,0,prefix='Cover');writer.set_page_label(1,1,prefix='Cover verso')
writer.set_page_label(2,11,style='/r',start=1);writer.set_page_label(12,653,style='/D',start=1)
writer.add_metadata({'/Title':'Introduction to Physics, Version 1.1','/Author':'Andrew Park','/Subject':'Complete textbook review proof','/Creator':'Introduction to Physics PDF assembly'})
writer.page_mode='/UseOutlines'
output=ROOT/'output/pdf/v1.1-complete-book.pdf'
writer.compress_identical_objects(remove_identicals=True,remove_orphans=True)
with output.open('wb') as f:writer.write(f)
report=dict(pages=len(writer.pages),internalLinkAnnotations=count,internalSourceLinks=len(resolved),externalLinkAnnotations=external,bookmarks=len(bookmarks),unresolved=0,output=str(output),bytes=output.stat().st_size,bookmarkTargets=bookmarks,prefaceLinks=[x for x in resolved if x['key']=='front' and x['href'] in ['#m42528','#m68327','#m67804','#m42238','#m42680']])
(QA/'assembly-check.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in ('bookmarkTargets','prefaceLinks')}))
