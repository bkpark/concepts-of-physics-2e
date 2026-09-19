"""Six-module fidelity experiment; canonical XML is never written.
Run: python prototype/build.py [cnx|course]
"""
from pathlib import Path
import collections, copy, hashlib, html, json, re, shutil, sys
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'prototype'
PROFILE=sys.argv[1] if len(sys.argv)>1 else 'cnx'
assert PROFILE in ('cnx','course')
OUT=P/'dist'/PROFILE
IDS=['m67034','m67530','m71410','m67122','m67807','m42709']
NS={'c':'http://cnx.rice.edu/cnxml','m':'http://www.w3.org/1998/Math/MathML','md':'http://cnx.rice.edu/mdml'}
esc=lambda s:html.escape(str(s),quote=True)
local=lambda e:e.tag.rsplit('}',1)[-1]
text=lambda e:''.join(e.itertext()).strip() if e is not None else ''
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def dump(path,data):path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
sections=load('reports/sections.json')
registry={s['module_id']:s for s in sections}
identities=load('metadata/sections.proposed.json')['sections']
for identity in identities:
    registry[identity['id'].split(':')[1]]['candidate_slug']=identity['slug']
attributions={a['module_id']:a for a in load('references/cnx-12.1-module-attributions.json')['modules']}
roots={s['module_id']:ET.parse(ROOT/s['source']).getroot() for s in sections}
parents={mid:{child:parent for parent in r.iter() for child in parent} for mid,r in roots.items()}
course={x['section_id'].split(':')[1]:x['label'] for x in load('metadata/numbering-course-2026-07-07.proposed.json')['section_labels']}
# Body headings inspected in historical PDF. Only these six labels are asserted.
cnx={'m67034':'2.5','m67530':'3.3','m71410':'3.8','m67122':'9.2','m67807':'13.6','m42709':'D'}
issues=[]; adaptations=[]; math_sources=[]; objects={}; counts=collections.Counter()
def anchor(mid,ident):return mid+'--'+ident.encode('utf-8').hex()
# Candidate counters, deliberately marked provisional; this tests identity separation.
chapter=0; previous=None; counter=collections.Counter()
for s in sections:
    mid=s['module_id']; group=s['parents'][-1] if s['parents'] else mid
    if group!=previous:
        chapter+=bool(s['parents']); counter=collections.Counter(); previous=group
    local_counter=collections.Counter()
    for e in roots[mid].iter():
        if not e.get('id'):continue
        kind=local(e); label=None
        if kind in ('figure','example','equation','table','exercise'):
            empty=e.find('c:label',NS)
            if e.get('class')!='unnumbered' and not(empty is not None and not text(empty)):
                counter[kind]+=1; local_counter[kind]+=1
                label=(f'{chapter}.{counter[kind]}' if PROFILE=='cnx' else f'{course.get(mid,"?")}.{local_counter[kind]}')
        objects[(mid,e.get('id'))]={'kind':kind,'label':label,'anchor':anchor(mid,e.get('id'))}

from mathml import math_node, UnsupportedMath

class Renderer:
    def __init__(self,mid,book=False):self.mid=mid;self.book=book;self.math_index=0
    def content(self,e):return esc(e.text or '')+''.join(self.render(x)+esc(x.tail or '') for x in e)
    def render(self,e,depth=2):
        tag=local(e); mid=self.mid; ident=e.get('id'); aid=f' id="{anchor(mid,ident)}"' if ident else ''
        obj=objects.get((mid,ident),{}); label=obj.get('label')
        if e.tag.startswith('{'+NS['m']+'}'):
            if tag!='math':raise ValueError('Top level MathML child outside math: '+tag)
            self.math_index+=1; key=f'{mid}-math-{self.math_index:04d}'
            if not self.book:
                parent=e
                while not parent.get('id') and parent in parents[mid]:parent=parents[mid][parent]
                snapshot=copy.deepcopy(e);snapshot.tail=None
                math_sources.append({'key':key,'module':mid,'xml':ET.tostring(snapshot,encoding='unicode'),'source_object':parent.get('id')})
            try:result=math_node(e)
            except UnsupportedMath as ex:
                if not self.book:issues.append({'kind':'unresolved-math','module':mid,'key':key,'detail':str(ex)})
                return f'<span class="math-issue" data-math-key="{key}">[Expression needs review: {key}]</span>'
            if not self.book and any(local(x) in ('apply','ci','cn','csymbol') for x in e.iter()):
                adaptations.append({'kind':'content-mathml','key':key,'policy':'Presentation adapter; bold vectors, symbolic juxtaposition, grouped composite powers; visual review required'})
            if not self.book and any(local(x)=='mtr' and any(local(y)!='mtd' for y in x) for x in e.iter()):
                adaptations.append({'kind':'math-table-cell-wrapper','key':key})
            return f'<span data-math-key="{key}">{result}</span>'
        if tag in ('metadata','label','colspec'):return ''
        if tag=='title':return f'<h3{aid}>{self.content(e)}</h3>'
        if tag=='link':
            doc=e.get('document',mid); target=e.get('target-id'); url=e.get('url'); obj=objects.get((doc,target),{})
            body=self.content(e) or (f'{obj.get("kind","reference").title()} {obj.get("label") or "(unnumbered)"}')
            if url:return f'<a href="{esc(url)}">{body}</a>'
            if doc not in IDS or (target and not obj):
                if not self.book:issues.append({'kind':'reference-outside-prototype' if doc not in IDS else 'source-reference-unresolved','module':mid,'document':doc,'target':target})
                reason='outside preview' if doc not in IDS else 'source target unresolved'
                return f'<span class="unavailable" title="{esc(reason)}">{body} [{reason}]</span>'
            frag=anchor(doc,target) if target else doc
            href='#'+frag if self.book or doc==mid else '../'+registry[doc]['candidate_slug']+'/index.html#'+frag
            return f'<a href="{href}">{body}</a>'
        if tag=='image':
            src=(ROOT/registry[mid]['source']).parent/e.get('src'); dest=OUT/'media'/src.name;dest.parent.mkdir(parents=True,exist_ok=True)
            if not dest.exists():shutil.copyfile(src,dest)
            url=('media/' if self.book else '../../media/')+src.name
            return f'<img src="{esc(url)}" alt="{esc(e.get("alt", ""))}" style="max-width:{esc(e.get("width","600"))}px">'
        if tag=='media':
            # Alt belongs to CNXML media, not image. Set only on the derived copy.
            clone=copy.deepcopy(e)
            for img in clone.findall('c:image',NS):img.set('alt',e.get('alt',''))
            return f'<div class="media"{aid}>'+self.content(clone)+'</div>'
        if tag=='figure':
            cap=e.find('c:caption',NS); body=esc(e.text or '')+''.join(self.render(x)+esc(x.tail or '') for x in e if local(x)!='caption')
            caption=self.content(cap) if cap is not None else ''
            return f'<figure{aid}>{body}<figcaption><b>Figure {esc(label or "(unnumbered)")}. </b>{caption}</figcaption></figure>'
        if tag=='equation':return f'<div class="equation"{aid}><div>{self.content(e)}</div><span class="eq-label">{("("+esc(label)+")") if label else ""}</span></div>'
        if tag in ('example','exercise','note'):
            heading=(tag.title()+' '+str(label)) if label else (tag.title() if tag!='note' else '')
            return f'<div class="{tag}"{aid}>'+ (f'<div class="object-title">{esc(heading)}</div>' if heading else '')+self.content(e)+'</div>'
        if tag=='solution':return f'<div class="solution"{aid}><b>Solution</b>{self.content(e)}</div>'
        if tag=='list':
            ordered=e.get('list-type')=='enumerated';htag='ol' if ordered else 'ul'
            style={'lower-alpha':'a','upper-alpha':'A','lower-roman':'i','upper-roman':'I','arabic':'1'}.get(e.get('number-style'))
            extra=f' type="{style}"' if ordered and style else ''
            return f'<{htag}{aid}{extra}>{self.content(e)}</{htag}>'
        if tag=='emphasis':return f'<{"em" if e.get("effect")=="italics" else "strong"}{aid}>{self.content(e)}</'+('em' if e.get('effect')=='italics' else 'strong')+'>'
        if tag=='entry':
            attr=''
            if e.get('morerows'):attr+=' rowspan="'+str(int(e.get('morerows'))+1)+'"'
            return f'<td{aid}{attr}>{self.content(e)}</td>'
        if tag=='table':
            caption=e.find('c:title',NS)
            if caption is None:caption=e.find('c:caption',NS)
            heading=f'<caption>Table {esc(label or "(unnumbered)")}. {self.content(caption)}</caption>' if caption is not None else ''
            body=esc(e.text or '')+''.join(self.render(x)+esc(x.tail or '') for x in e if local(x) not in ('title','caption'))
            summary=f' aria-label="{esc(e.get("summary"))}"' if e.get('summary') else ''
            return f'<div class="table-wrap"{aid}><table{summary}>{heading}{body}</table></div>'
        if tag=='footnote':return f'<span class="footnote"{aid}> [Note: {self.content(e)}]</span>'
        if tag=='newline':return '<br>'
        tags={'para':'div','content':'div','section':'section','item':'li','term':'dfn','definition':'div','meaning':'div','glossary':'section','problem':'div','tgroup':'tbody','thead':'thead','tbody':'tbody','row':'tr','sub':'sub','sup':'sup','span':'span','div':'div','caption':'caption'}
        if tag=='tgroup':return self.content(e)
        if tag not in tags:raise ValueError('Unsupported CNXML element '+tag)
        htag=tags[tag]; cls=f' class="{tag}"'
        return f'<{htag}{aid}{cls}>{self.content(e)}</{htag}>'
    def module(self):
        mid=self.mid;r=roots[mid];label=(cnx if PROFILE=='cnx' else course)[mid]
        abstract=r.find('c:metadata/md:abstract',NS)
        learning=f'<aside class="objectives"><h2>Learning objectives</h2>{self.content(abstract)}</aside>' if abstract is not None and text(abstract) else ''
        a=attributions[mid]
        credit='<footer class="attribution"><p>Historical attribution: '+esc(a['authors'])+'. Copyright: '+esc(a['copyright'])+'. <a href="'+esc(a['license'])+'">CC BY 4.0</a>. <a href="'+esc(a['url'])+'">Original module '+esc(mid)+' version '+esc(a['legacy_module_version'])+'</a>.</p>'
        if a.get('based_on_text'):credit+='<p>Based on: '+esc(a['based_on_text'])+'</p>'
        credit+='<p>Derived rendering: CNXML adapted to HTML; object numbering is provisional and malformed expressions are flagged. Text and source files remain unchanged. Attribution transcribed from the historical PDF.</p></footer>'
        return f'<article id="{mid}"><header><p class="eyebrow">{esc(PROFILE.upper())} · {esc(label)}</p><h1>{esc(text(r.find("c:title",NS)))}</h1></header>{learning}'+''.join(self.render(x) for x in r if local(x) in ('content','glossary'))+credit+'</article>'

def page(title,body,prefix=''):
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(title)+'</title><link rel="stylesheet" href="'+prefix+'style.css"><script>window.MathJax={loader:{load:[]},options:{enableMenu:false},svg:{fontCache:"local"},startup:{pageReady:()=>MathJax.startup.defaultPageReady().then(()=>window.mathReady=true)}};</script><script defer src="'+prefix+'vendor/mml-svg.js"></script></head><body><nav><a href="'+prefix+'index.html">Introduction to Physics · Fidelity prototype</a></nav><div class="prototype-notice">Six-module preview. Section labels follow the selected reference; object numbers are experimental. Highlighted expressions need review.</div><main>'+body+'</main></body></html>'

OUT.mkdir(parents=True,exist_ok=True);shutil.copytree(P/'vendor',OUT/'vendor',dirs_exist_ok=True);shutil.copyfile(P/'style.css',OUT/'style.css')
book=[]
for mid in IDS:
    source_dir=OUT/'source'/mid;source_dir.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(ROOT/registry[mid]['source'],source_dir/'index.cnxml')
    target=OUT/'sections'/registry[mid]['candidate_slug'];target.mkdir(parents=True,exist_ok=True)
    body=Renderer(mid).module();(target/'index.html').write_text(page(registry[mid]['title'],body,'../../'),encoding='utf-8',newline='\n')
    book.append(Renderer(mid,True).module())
intro='<header><p class="eyebrow">Recovery / rendering experiment</p><h1>Introduction to Physics</h1><p>Six complete modules from the preserved CNX import.</p></header><ol>'+''.join('<li><a href="sections/'+registry[m]['candidate_slug']+'/index.html">'+esc(registry[m]['title'])+'</a></li>' for m in IDS)+'</ol>'
intro+='<p>Historical source remains unchanged. Math source XML and issue logs are included beside the build. The other numbering profile uses exactly the same section paths and anchors.</p>'
intro+='<p><a href="review.html">Review flagged expressions and references</a> · <a href="book.html">Complete printable sample</a></p>'
(OUT/'index.html').write_text(page('Introduction to Physics — prototype',intro),encoding='utf-8',newline='\n')
(OUT/'book.html').write_text(page('Introduction to Physics — sample', '<div class="cover"><h1>Introduction to Physics</h1><h2>Fidelity prototype</h2><p>Six selected modules · '+PROFILE+' profile</p><p>Provisional object numbering. Not a student edition.</p><p>Adaptation by Andrew Park; underlying content by Bobby Bailey, Andrew Park, OpenStax and James Rittenbach. Historical collection: CC BY 4.0. Original figure credits are retained.</p></div>'+''.join(book)),encoding='utf-8',newline='\n')
dump(OUT/'math-source.json',math_sources);dump(OUT/'issues.json',issues);dump(OUT/'adaptations.json',adaptations)
review='<h1>Fidelity review</h1><p>These findings require review; no source repairs have been applied.</p>'
for item in issues:
    review+='<section><h2>'+esc(item.get('key',item['module']))+'</h2><p>'+esc(item.get('detail',str(item)))+'</p>'
    if item.get('key'):
        source=next(x for x in math_sources if x['key']==item['key'])
        review+='<p>Source object: '+esc(source['source_object'])+'</p><pre style="white-space:pre-wrap;overflow-wrap:anywhere;font-size:12px">'+esc(source['xml'])+'</pre>'
    review+='</section>'
(OUT/'review.html').write_text(page('Fidelity review',review),encoding='utf-8',newline='\n')
dump(OUT/'identity-registry.json',{m:{'slug':registry[m]['candidate_slug'],'anchors':[o['anchor'] for (d,i),o in objects.items() if d==m]} for m in IDS})
dump(OUT/'build-manifest.json',{'profile':PROFILE,'modules':IDS,'math_expressions':len(math_sources),'issues':len(issues),'source_sha256':{m:hashlib.sha256((ROOT/registry[m]['source']).read_bytes()).hexdigest() for m in IDS},'object_numbering_status':'experimental; not verified against historical labels','section_labels':{m:(cnx if PROFILE=='cnx' else course)[m] for m in IDS}})
print(json.dumps({'profile':PROFILE,'math':len(math_sources),'issues':dict(collections.Counter(x['kind'] for x in issues)),'adaptations':len(adaptations)}))
