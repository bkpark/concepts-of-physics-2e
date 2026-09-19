"""Validate source coverage, page identities, links and known-issue accounting."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import collections, hashlib,json,xml.etree.ElementTree as ET
P=Path(__file__).resolve().parent;ROOT=P.parent
class Page(HTMLParser):
    def __init__(self):super().__init__();self.ids=[];self.math=[];self.links=[];self.images=[];self.text=[]
    def handle_data(self,data):self.text.append(data)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if 'data-math-key' in a:self.math.append(a['data-math-key'])
        if tag=='a' and 'href' in a:self.links.append(a['href'])
        if tag=='img':self.images.append(a)
stats={}
vendor=json.loads((P/'vendor/manifest.json').read_text(encoding='utf-8'))['mathjax']
assert hashlib.sha256((P/'vendor/mml-svg.js').read_bytes()).hexdigest()==vendor['sha256']
for profile in ('course-full',):
    out=P/'dist'/profile
    registry=json.loads((out/'identity-registry.json').read_text(encoding='utf-8'))
    pages={}
    for f in out.rglob('*.html'):
        p=Page();p.feed(f.read_text(encoding='utf-8'));assert len(p.ids)==len(set(p.ids)),f'Duplicate IDs: {f}';pages[f.resolve()]=p
    for f,p in pages.items():
        for href in p.links:
            u=urlsplit(href)
            if u.scheme or u.netloc:continue
            target=(f.parent/unquote(u.path)).resolve() if u.path else f
            if target.suffix.lower() in ('.png','.jpg','.svg','.pdf'):
                assert target.is_file(),f'Missing linked asset: {target}'
                continue
            assert target in pages,f'Broken page link: {f} -> {href}'
            if u.fragment:assert u.fragment in pages[target].ids,f'Broken anchor: {href}'
    count=collections.Counter()
    for mid,entry in registry.items():
        data=(ROOT/'maintained/modules'/mid/'index.cnxml').read_bytes()
        assert data==(out/'source'/mid/'index.cnxml').read_bytes()
        source=ET.fromstring(data);p=pages[(out/'sections'/entry['slug']/'index.html').resolve()]
        ids=[mid+'--'+e.get('id').encode().hex() for e in source.iter() if e.get('id')]
        assert set(ids)<=set(p.ids),(mid,'Missing source anchors')
        math=list(source.iter('{http://www.w3.org/1998/Math/MathML}math'))
        assert len(math)==len(p.math)==len(set(p.math))
        imgs=list(source.iter('{http://cnx.rice.edu/cnxml}image'));assert len(imgs)==len(p.images)
        visible=' '.join(' '.join(p.text).split())
        def prose(e,inside_math=False):
            inside_math=inside_math or e.tag.startswith('{http://www.w3.org/1998/Math/MathML}')
            if not inside_math and e.text and len(e.text.strip())>20:
                fragment=' '.join(e.text.split());assert fragment in visible,(mid,'Missing prose',fragment[:100])
                count['prose_fragments_checked']+=1
            for child in e:
                prose(child,inside_math)
                if not inside_math and child.tail and len(child.tail.strip())>20:
                    fragment=' '.join(child.tail.split());assert fragment in visible,(mid,'Missing prose tail',fragment[:100])
                    count['prose_fragments_checked']+=1
        for child in source:
            if child.tag.rsplit('}',1)[-1] in ('title','content','glossary'):prose(child)
        abstract=source.find('{http://cnx.rice.edu/cnxml}metadata/{http://cnx.rice.edu/mdml}abstract')
        if abstract is not None:prose(abstract)
        count['math']+=len(math);count['images']+=len(imgs);count['source_ids']+=len(ids)
    stats[profile]=dict(count)
audit=json.loads((P/'qa/course-full-browser-audit.json').read_text(encoding='utf-8'))
assert len(audit['pages'])==156 and not audit['external_requests']
for p in audit['pages']:
    for key in ('errors','mathErrors','brokenImages','overflow','duplicateIds'):assert not p[key],(p['module'],key,p[key])
    assert p['renderedMath']+len(p['unresolved'])==p['mathWrappers']
views=json.loads((P/'dist/course-full/exercise-views.json').read_text(encoding='utf-8'))
projected=[b['module']+'#'+ident for v in views for b in v['blocks'] for ident in b['exercise_ids']]
assert len(projected)==len(set(projected))==944
labels=json.loads((P/'dist/course-full/object-labels.json').read_text(encoding='utf-8'))
assert labels['m67123#import-auto-id2589627']['label']=='8.E.1'
assert (P/'dist/course-full/identity-registry.json').read_bytes()==(P/'dist/cnx-full/identity-registry.json').read_bytes()
issues=json.loads((P/'dist/course-full/issues.json').read_text(encoding='utf-8'))
result={'coverage':stats,'browser_pages':len(audit['pages']),'issues':dict(collections.Counter(i['kind'] for i in issues)),'publication_ready':False}
(P/'qa/course-full-validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(result,indent=2))
