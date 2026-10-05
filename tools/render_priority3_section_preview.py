"""Render full priority-3 reading previews from maintained source plus recorded XML overlays."""
from pathlib import Path
import sys,json,copy,hashlib,re,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'prototype'))
sys.argv=['build.py','course','--all']
source=(ROOT/'prototype/build.py').read_text(encoding='utf-8')
ns={'__file__':str(ROOT/'prototype/build.py'),'__name__':'preview_renderer'}
exec(compile(source.split('OUT.mkdir(parents=True,exist_ok=True);')[0],str(ROOT/'prototype/build.py'),'exec'),ns)
packet=json.loads((ROOT/'proposals/1.1/priority3-conceptual-review.json').read_text(encoding='utf-8'))
he=json.loads((ROOT/'proposals/1.1/heat-engine-preview-patches.json').read_text(encoding='utf-8'))
packet['items'].append(dict(id='HE01–HE08',status='approved-pending-section-preview',passages=he['patches']))
patches=[dict(p,item=i['id']) for i in packet['items'] for p in i['passages']]
additions=[dict(p,item=i['id']) for i in packet['items'] for p in i.get('glossary_additions',[])]
selected=[s['module_id'] for s in ns['sections'] if s['module_id'] in {p['module'] for p in patches}];out=ROOT/'prototype/dist/review-1.1/priority3-sections';out.mkdir(parents=True,exist_ok=True)
ns['OUT']=out
C='{http://cnx.rice.edu/cnxml}'
changes=[]
def sig(e):return (e.tag,dict(e.attrib),re.sub(r'\s+',' ',e.text or '').strip(),[(sig(c),re.sub(r'\s+',' ',c.tail or '').strip()) for c in e])
def parse(s):return E.fromstring('<wrap xmlns="http://cnx.rice.edu/cnxml" xmlns:m="http://www.w3.org/1998/Math/MathML" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0">'+s+'</wrap>')[0]
source_hashes={m:hashlib.sha256((ROOT/ns['registry'][m]['source']).read_bytes()).hexdigest() for m in selected}
for p in patches:
 mid=p['module'];r=ns['roots'][mid];nodes={e.get('id'):e for e in r.iter() if e.get('id')};parents={c:e for e in r.iter() for c in e}
 node=nodes[p['source_id']];before=parse(p['before_xml'])
 assert sig(node)==sig(before),(p['item'],p['source_id'])
 if p.get('operation')=='remove':
  parents[node].remove(node)
  changes.append(dict(item=p['item'],module=mid,anchor=p['source_id'],operation='remove'))
  continue
 new=parse(p['proposed_xml'])
 new.tail=node.tail;parent=parents[node];pos=list(parent).index(node);parent.remove(node)
 if p.get('operation')=='replace-and-move':
  preceding=nodes[p['insert_after_id']];following=nodes[p['insert_before_id']];parent=parents[preceding]
  assert parents[following] is parent
  pos=list(parent).index(preceding)+1
  assert list(parent).index(following)==pos
 parent.insert(pos,new)
 for offset,xml in enumerate(p.get('proposed_following_xml',[]),1):parent.insert(pos+offset,parse(xml))
 changes.append(dict(item=p['item'],module=mid,anchor=p['source_id']))
for p in additions:
 r=ns['roots'][p['module']];glossary=r.find(C+'glossary');assert glossary is not None
 entry=parse(p['proposed_xml']);assert not any(e.get('id')==entry.get('id') for e in r.iter())
 glossary.append(entry);changes.append(dict(item=p['item'],module=p['module'],anchor=entry.get('id'),operation='add-glossary-entry'))
for mid in selected:
 ids=[e.get('id') for e in ns['roots'][mid].iter() if e.get('id')];assert len(ids)==len(set(ids)),mid
ns['parents']={mid:{c:e for e in r.iter() for c in e} for mid,r in ns['roots'].items()}
ns['objects']=ns['build_objects'](ns['sections'],ns['roots'],'course',ns['course'],ns['load']('maintained/numbering.json'),ns['anchor'])
import shutil
for file in ['style.css','copy-math.js']:shutil.copyfile(ROOT/'prototype'/file,out/file)
slugs={ns['registry'][m]['candidate_slug'] for m in selected}
for mid in selected:
 slug=ns['registry'][mid]['candidate_slug'];folder=out/'sections'/slug;folder.mkdir(parents=True,exist_ok=True)
 body=ns['Renderer'](mid).module()
 def links(match):
  href=match[1]
  if href.startswith('#') or re.match(r'https?://',href):return match[0]
  dest=(folder/href.split('#')[0]).resolve()
  if '/sections/' in dest.as_posix() and dest.parent.name in slugs:return match[0]
  # Book navigation and references outside these two previews use the existing full draft.
  rel=dest.relative_to(out).as_posix() if dest.is_relative_to(out) else ''
  return 'href="/course-full/'+rel+('#'+href.split('#',1)[1] if '#' in href else '')+'"' if rel else match[0]
 body=re.sub(r'href="([^"]+)"',links,body)
 relevant=[i for i in packet['items'] if any(p['module']==mid for p in i['passages'])]
 pending=[i['id'] for i in relevant if not i['status'].startswith('approved')]
 notice='<aside class="prototype-notice">Priority 3 reading preview: proposed changes overlaid for context; maintained source unchanged. Includes exercises for context. <a href="../../index.html">All section previews</a> · <a href="../../../priority3-review/">Comparison tables</a>'
 if pending:notice+=' <strong>Review still pending: '+', '.join(pending)+'.</strong>'
 notice+='</aside>'
 for p in patches:
  if p['module']==mid and p.get('attribution'):
   a=p['attribution']
   body+='<footer><p>Carnot’s Principle statement and adapted following sentence: '+', '.join(a['authors'])+', <a href="'+a['source_url']+'">'+a['title']+', '+a['section']+'</a>, '+a['publisher']+' ('+str(a['copyright_year'])+'), <a href="'+a['license_url']+'">'+a['license']+'</a>. '+a['changes']+'</p></footer>'
 html='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+ns['registry'][mid]['title']+' — reading preview</title><link rel="stylesheet" href="../../style.css"><script defer src="../../copy-math.js"></script></head><body>'+notice+'<main>'+body+'</main></body></html>'
 (folder/'index.html').write_text(html,encoding='utf-8',newline='\n')
 xmlfolder=out/'source'/mid;xmlfolder.mkdir(parents=True,exist_ok=True);E.ElementTree(ns['roots'][mid]).write(xmlfolder/'index.cnxml',encoding='utf-8',xml_declaration=True)
import html
index=['<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Priority 3 section previews</title><link rel="stylesheet" href="style.css"><main><h1>Priority 3: full-section reading previews</h1><p>Complete sections with the coordinated Priority 3 proposals overlaid on the maintained 1.1 draft. P3-08 A–G is approved. Read for continuity, paragraph boundaries, and surviving repetition before final application. Maintained source is unchanged.</p><p>Exercises remain inline in these reading previews for context. Links outside these sections lead to the existing full draft. <a href="../priority3-review/">Before/proposed comparisons</a></p><ul>']
for m in selected:
 items=[i for i in packet['items'] if any(p['module']==m for p in i['passages'])]
 pending=[i['id'] for i in items if not i['status'].startswith('approved')]
 index.append('<li><a href="sections/'+ns['registry'][m]['candidate_slug']+'/index.html">'+html.escape(ns['registry'][m]['title'])+'</a> — '+', '.join(i['id'] for i in items)+(' <strong>(pending review: '+', '.join(pending)+')</strong>' if pending else '')+'</li>')
index.append('</ul></main></html>');(out/'index.html').write_text('\n'.join(index),encoding='utf-8',newline='\n')
(out/'math-sources.json').write_text(json.dumps(ns['math_sources'],ensure_ascii=False),encoding='utf-8')
assert source_hashes=={m:hashlib.sha256((ROOT/ns['registry'][m]['source']).read_bytes()).hexdigest() for m in selected}
report={'modules':selected,'overlays':changes,'source_layer':'maintained with preview-only Priority 3 overlays','issues':ns['issues'],'source_sha256':source_hashes}
reportdir=ROOT/'reports/1.1/priority3-sections';reportdir.mkdir(parents=True,exist_ok=True);(reportdir/'preview-manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print('Rendered',len(selected),'complete sections;',len(changes),'overlays;',len(ns['issues']),'renderer issues')

