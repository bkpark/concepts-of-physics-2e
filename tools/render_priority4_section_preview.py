"""Full-section reading previews for selected Priority 4 overlays; no source edits."""
from pathlib import Path
import sys,json,hashlib,re,shutil,html,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[1]
selected=sys.argv[1:] or ['m42528']
packet=json.loads((ROOT/'proposals/1.1/priority4-followup-review.json').read_text(encoding='utf-8'))
sys.path.insert(0,str(ROOT/'prototype'));sys.argv=['build.py','course','--all']
ns={'__file__':str(ROOT/'prototype/build.py'),'__name__':'preview_renderer'}
s=(ROOT/'prototype/build.py').read_text(encoding='utf-8')
exec(compile(s.split('OUT.mkdir(parents=True,exist_ok=True);')[0],ns['__file__'],'exec'),ns)
out=ROOT/'prototype/dist/review-1.1/priority4-sections';out.mkdir(parents=True,exist_ok=True);ns['OUT']=out
def sig(e):return (e.tag,dict(e.attrib),re.sub(r'\s+',' ',e.text or '').strip(),[(sig(c),re.sub(r'\s+',' ',c.tail or '').strip()) for c in e])
changes=[];hashes={}
for mid in selected:
    patches=[p for i in packet['items'] for p in i['passages'] if p['module']==mid]
    assert patches,mid
    paths={p['source_path'] for p in patches};assert len(paths)==1
    path=ROOT/paths.pop();hashes[mid]=hashlib.sha256(path.read_bytes()).hexdigest()
    assert all(p['source_sha256']==hashes[mid] for p in patches)
    root=E.parse(path).getroot();ns['roots'][mid]=root
    for p in patches:
        if p.get('source_selector')=='glossary':node=root.find('{http://cnx.rice.edu/cnxml}glossary')
        elif p.get('source_selector')=='abstract':node=root.find('.//{http://cnx.rice.edu/mdml}abstract')
        else:node=next(e for e in root.iter() if e.get('id')==p['source_id'])
        assert sig(node)==sig(E.fromstring(p['before_xml'])),p['source_id']
        parent=next(e for e in root.iter() if node in list(e));pos=list(parent).index(node)
        if p.get('operation')=='remove':
            if node.tail:
                if pos:parent[pos-1].tail=(parent[pos-1].tail or '')+node.tail
                else:parent.text=(parent.text or '')+node.tail
            parent.remove(node)
        else:
            new=E.fromstring(p['proposed_xml']);new.tail=node.tail;parent.remove(node)
            if p.get('relocate_before'):
                destination=next(e for e in root.iter() if e.get('id')==p['relocate_before'])
                parent=next(e for e in root.iter() if destination in list(e))
                pos=list(parent).index(destination)
            parent.insert(pos,new)
        changes.append(dict(module=mid,source_id=p['source_id']))
    ids=[e.get('id') for e in root.iter() if e.get('id')];assert len(ids)==len(set(ids))
ns['parents']={m:{c:e for e in r.iter() for c in e} for m,r in ns['roots'].items()}
ns['objects']=ns['build_objects'](ns['sections'],ns['roots'],'course',ns['course'],ns['load']('maintained/numbering.json'),ns['anchor'])
for f in ['style.css','copy-math.js']:shutil.copyfile(ROOT/'prototype'/f,out/f)
slugs={ns['registry'][mid]['candidate_slug'] for mid in selected}
for mid in selected:
    slug=ns['registry'][mid]['candidate_slug'];folder=out/'sections'/slug;folder.mkdir(parents=True,exist_ok=True)
    body=ns['Renderer'](mid).module()
    def links(match):
        href=match[1]
        if href.startswith('#') or re.match(r'https?://',href):return match[0]
        dest=(folder/href.split('#')[0]).resolve()
        if '/sections/' in dest.as_posix() and dest.parent.name in slugs:return match[0]
        rel=dest.relative_to(out).as_posix() if dest.is_relative_to(out) else ''
        return 'href="/course-full/'+rel+('#'+href.split('#',1)[1] if '#' in href else '')+'"' if rel else match[0]
    body=re.sub(r'href="([^"]+)"',links,body)
    review_id='P4-07' if mid=='m42528' else ('P4-18' if mid=='m67132' else ('P4-19' if mid=='m76584' else 'P4-14'))
    notice='<aside class="prototype-notice">Priority 4 full-section reading preview. Includes the reviewed corrections; maintained source unchanged. Exercises are included for context. <a href="../../../priority4-review/#'+review_id+'">Comparison tables</a></aside>'
    page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(ns['registry'][mid]['title'])+' — reading preview</title><link rel="stylesheet" href="../../style.css"><script defer src="../../copy-math.js"></script></head><body>'+notice+'<main>'+body+'</main></body></html>'
    (folder/'index.html').write_text(page,encoding='utf-8')
    xmlfolder=out/'source'/mid;xmlfolder.mkdir(parents=True,exist_ok=True);E.ElementTree(ns['roots'][mid]).write(xmlfolder/'index.cnxml',encoding='utf-8',xml_declaration=True)
index='<html lang="en"><meta charset="utf-8"><title>Priority 4 section previews</title><h1>Priority 4 section previews</h1><ul>'+''.join('<li><a href="sections/'+ns['registry'][m]['candidate_slug']+'/index.html">'+html.escape(ns['registry'][m]['title'])+'</a></li>' for m in selected)+'</ul></html>'
(out/'index.html').write_text(index,encoding='utf-8')
(out/'math-sources.json').write_text(json.dumps(ns['math_sources'],ensure_ascii=False),encoding='utf-8')
report=ROOT/'reports/1.1/priority4-sections';report.mkdir(parents=True,exist_ok=True)
(report/'preview-manifest.json').write_text(json.dumps(dict(modules=selected,changes=changes,base_hashes=hashes,issues=ns['issues']),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Rendered',len(selected),'sections;',len(changes),'overlays;',len(ns['issues']),'renderer issues')
