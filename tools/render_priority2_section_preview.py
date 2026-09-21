"""Render full priority-2 reading previews from maintained source plus recorded XML overlays."""
from pathlib import Path
import sys,json,copy,hashlib,re,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'prototype'))
sys.argv=['build.py','course','--all']
source=(ROOT/'prototype/build.py').read_text(encoding='utf-8')
ns={'__file__':str(ROOT/'prototype/build.py'),'__name__':'preview_renderer'}
exec(compile(source.split('OUT.mkdir(parents=True,exist_ok=True);')[0],str(ROOT/'prototype/build.py'),'exec'),ns)
packet=json.loads((ROOT/'proposals/1.1/priority2-preview-patches.json').read_text(encoding='utf-8'))
selected=['m68327','m42649'];out=ROOT/'prototype/dist/review-1.1/priority2-sections';out.mkdir(parents=True,exist_ok=True)
ns['OUT']=out
C='{http://cnx.rice.edu/cnxml}'
changes=[]
def sig(e):return (e.tag,dict(e.attrib),re.sub(r'\s+',' ',e.text or '').strip(),[(sig(c),re.sub(r'\s+',' ',c.tail or '').strip()) for c in e])
def parse(s):return E.fromstring('<wrap xmlns="http://cnx.rice.edu/cnxml" xmlns:m="http://www.w3.org/1998/Math/MathML">'+s+'</wrap>')[0]
for p in packet['patches']:
 mid=p['module'];r=ns['roots'][mid];nodes={e.get('id'):e for e in r.iter() if e.get('id')};parents={c:e for e in r.iter() for c in e}
 node=nodes[p['source_id']];before=parse(p['before_xml']);new=parse(p['proposed_xml'])
 assert sig(node)==sig(before),(p['item'],p['source_id'])
 new.tail=node.tail;parent=parents[node];pos=list(parent).index(node);parent.remove(node);parent.insert(pos,new)
 changes.append(dict(item=p['item'],module=mid,anchor=p['source_id']))
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
 notice='<aside class="prototype-notice">Reading preview: All Priority 2 edits are applied to the maintained source. Includes exercises for context. The connected activity and geographic claims have approved replacements. <a href="../../index.html">Both section previews</a> · <a href="../../../priority2-numerical-audit/">Comparison tables</a></aside>'
 html='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+ns['registry'][mid]['title']+' — reading preview</title><link rel="stylesheet" href="../../style.css"><script defer src="../../copy-math.js"></script></head><body>'+notice+'<main>'+body+'</main></body></html>'
 (folder/'index.html').write_text(html,encoding='utf-8',newline='\n')
 xmlfolder=out/'source'/mid;xmlfolder.mkdir(parents=True,exist_ok=True);E.ElementTree(ns['roots'][mid]).write(xmlfolder/'index.cnxml',encoding='utf-8',xml_declaration=True)
(out/'index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><title>Radiation section previews</title><link rel="stylesheet" href="style.css"><main><h1>Radiation section reading previews</h1><p>Read the finalized P2-01–P2-06 changes in context, rebuilt from maintained source. The approved qualitative replacements for the terrestrial and internal-background passages are included. Source notes are attached to the revised tables.</p><ul>'+''.join('<li><a href="sections/'+ns['registry'][m]['candidate_slug']+'/index.html">'+ns['registry'][m]['title']+'</a></li>' for m in selected)+'</ul></main></html>',encoding='utf-8')
(out/'math-sources.json').write_text(json.dumps(ns['math_sources'],ensure_ascii=False),encoding='utf-8')
report={'modules':selected,'overlays':changes,'source_layer':'maintained-after-priority2','applied_items':['P2-01','P2-02','P2-03','P2-04','P2-05','P2-06'],'issues':ns['issues'],'open_checks':packet['open_checks'],'source_sha256':{m:hashlib.sha256((ROOT/ns['registry'][m]['source']).read_bytes()).hexdigest() for m in selected}}
reportdir=ROOT/'reports/1.1/priority2-sections';reportdir.mkdir(parents=True,exist_ok=True);(reportdir/'preview-manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print('Rendered two complete sections;',len(changes),'overlays;',len(ns['issues']),'renderer issues')
