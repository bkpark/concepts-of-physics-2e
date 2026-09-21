"""Render two complete sections with cycle-2 proposals overlaid in memory only."""
from pathlib import Path
import sys,json,copy,hashlib,re,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'prototype'))
sys.argv=['build.py','course','--all']
source=(ROOT/'prototype/build.py').read_text(encoding='utf-8')
ns={'__file__':str(ROOT/'prototype/build.py'),'__name__':'preview_renderer'}
exec(compile(source.split('OUT.mkdir(parents=True,exist_ok=True);')[0],str(ROOT/'prototype/build.py'),'exec'),ns)
packet=json.loads((ROOT/'proposals/1.1/fact-check-cycle2.json').read_text(encoding='utf-8'))
selected=['m76584','m68327'];out=ROOT/'prototype/dist/review-1.1/radiation-sections';out.mkdir(parents=True,exist_ok=True)
ns['OUT']=out
C='{http://cnx.rice.edu/cnxml}'
changes=[]
for item in packet['items']:
 if item['module'] not in selected:continue
 if item['status']=='applied-author-directed':continue
 for p in [item]+item.get('related_passages',[]):
  mid=p.get('module',item['module'])
  if mid not in selected or not p.get('proposed_xml'):continue
  assert hashlib.sha256((ROOT/p.get('source_path',item['source_path'])).read_bytes()).hexdigest()==p.get('source_sha256',item['source_sha256'])
  r=ns['roots'][mid];nodes={e.get('id'):e for e in r.iter() if e.get('id')};parents={c:e for e in r.iter() for c in e}
  if p.get('attribute_edit'):
   a=p['attribute_edit'];node=nodes[a['source_id']];assert node.get(a['attribute'])==a['before'];node.set(a['attribute'],a['after'])
  else:
   ident=p.get('source_id') or p['anchor'];node=nodes[ident]
   if p.get('source_selector')=='caption':node=node.find(C+'caption')
   new=E.fromstring(p['proposed_xml']);before=E.fromstring(p['before_xml'])
   # Compare XML content, ignoring serialization whitespace and namespace prefixes.
   def sig(e):return (e.tag,dict(e.attrib),re.sub(r'\s+',' ',e.text or '').strip(),[(sig(c),re.sub(r'\s+',' ',c.tail or '').strip()) for c in e])
   assert sig(node)==sig(before),(item['id'],ident,'source differs')
   new.tail=node.tail;parent=parents[node];pos=list(parent).index(node);parent.remove(node);parent.insert(pos,new)
  changes.append({'item':item['id'],'module':mid,'anchor':p.get('anchor',item['anchor'])})
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
 notice='<aside class="prototype-notice">Reading preview: all approved cycle-2 changes, including F2-H01/F2-H02 and glossary alignment, are now applied to the maintained source. Includes existing exercises and glossary for context; unchanged material may still need audit. <a href="../../index.html">Both section previews</a> · <a href="../../../fact-check-cycle2/">Comparison tables</a></aside>'
 html='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+ns['registry'][mid]['title']+' — reading preview</title><link rel="stylesheet" href="../../style.css"><script defer src="../../copy-math.js"></script></head><body>'+notice+'<main>'+body+'</main></body></html>'
 (folder/'index.html').write_text(html,encoding='utf-8',newline='\n')
 xmlfolder=out/'source'/mid;xmlfolder.mkdir(parents=True,exist_ok=True);E.ElementTree(ns['roots'][mid]).write(xmlfolder/'index.cnxml',encoding='utf-8',xml_declaration=True)
(out/'index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><title>Radiation section previews</title><link rel="stylesheet" href="style.css"><main><h1>Radiation section reading previews</h1><p>Approved cycle-2 changes applied to the maintained source; these pages are rebuilt from that source.</p><ul>'+''.join('<li><a href="sections/'+ns['registry'][m]['candidate_slug']+'/index.html">'+ns['registry'][m]['title']+'</a></li>' for m in selected)+'</ul></main></html>',encoding='utf-8')
(out/'math-sources.json').write_text(json.dumps(ns['math_sources'],ensure_ascii=False),encoding='utf-8')
report={'modules':selected,'overlays':changes,'source_layer':'maintained-after-cycle2','applied_items':[i['id'] for i in packet['items'] if i['module'] in selected and i['status']=='applied-author-directed'],'issues':ns['issues'],'source_sha256':{m:hashlib.sha256((ROOT/ns['registry'][m]['source']).read_bytes()).hexdigest() for m in selected}}
reportdir=ROOT/'reports/1.1/radiation-sections';reportdir.mkdir(parents=True,exist_ok=True);(reportdir/'preview-manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print('Rendered two complete sections;',len(changes),'overlays;',len(ns['issues']),'renderer issues')
