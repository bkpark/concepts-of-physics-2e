"""Render small author review packets and applied batches, without editing content."""
from pathlib import Path
import html,json,shutil,sys,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'prototype'))
from native_math import native_math
OUT=ROOT/'reports/1.1/backport-review';OUT.mkdir(parents=True,exist_ok=True)
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def render(xml):
    def visit(e):
        tag=e.tag.rsplit('}',1)[-1]
        if tag=='math':return native_math(e)[0]
        body=html.escape(e.text or '')+''.join(visit(c)+html.escape(c.tail or '') for c in e)
        if tag=='emphasis':return '<em>'+body+'</em>'
        if tag=='link':return body or '<span>[existing figure reference]</span>'
        return body
    return visit(ET.fromstring('<wrapper xmlns="http://cnx.rice.edu/cnxml" xmlns:m="http://www.w3.org/1998/Math/MathML">'+xml+'</wrapper>'))
style='<style>body{font:18px/1.65 Georgia;max-width:1100px;margin:auto;padding:24px;color:#20343c}a{color:#12647b;overflow-wrap:anywhere}section{margin:3em 0;border-top:1px solid #bbb;padding-top:1em}.columns{display:grid;grid-template-columns:1fr 1fr;gap:24px}.box{min-width:0;background:#f3f6f6;padding:16px;overflow:auto}img{max-width:100%;height:auto}.notice{background:#edf4f6;padding:18px}h1,h2{line-height:1.3}@media(max-width:700px){.columns{display:block}.box{margin:1em 0}}</style>'
page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>1.1 backport review</title>'+style+'<h1>1.1 backport: opening chapters</h1><p class="notice">BR01 is applied; BR02 remains pending. Thirteen other opening-chapter corrections have been applied and are listed afterward. The full-book backport is not complete. Published 1.0 is unchanged.</p><p><a href="#BR01">BR01: kilogram wording</a> · <a href="#BR02">BR02: exercise diagram</a> · <a href="#applied">Applied corrections</a></p>'
data=load('proposals/1.1/opening-review.json')
for item in data['items']:
    page+='<section id="'+item['id']+'"><h2>'+item['id']+' — '+html.escape(item['title'])+'</h2><p>'+html.escape(item['reason'])+'</p>'
    if item['id']=='BR01':
        page+='<ul>'+''.join('<li><del>'+html.escape(a)+'</del> → <ins>'+html.escape(b)+'</ins></li>' for a,b in item['substitutions'])+'</ul>'
        page+='<div class="columns"><div class="box"><h3>Before BR01</h3>'+render(item['before_xml'])+'</div><div class="box"><h3>Applied for 1.1</h3>'+render(item['after_xml'])+'</div></div>'
    else:
        for label,path,name in [('Local figure',item['local_image'],'path-local.jpg'),('Pinned CC BY upstream figure',item['upstream_image'],'path-upstream.jpg')]:
            shutil.copyfile(ROOT/path,OUT/name)
        page+='<div class="columns"><div class="box"><h3>Local: C ends at 11 m</h3><img src="path-local.jpg" alt="Local path diagram, C ends at 11 m; axis incorrectly labelled displacement."></div><div class="box"><h3>Pinned upstream: C ends at 10 m</h3><img src="path-upstream.jpg" alt="Upstream diagram correctly labels position but moves C endpoint to 10 m."></div></div><p>Local calculation: |10−2| + |8−10| + |11−8| = 13 m; displacement = 11−2 = +9 m. The pinned upstream solution still gives these values even though its new drawing ends at 10 m. That drawing would instead give 12 m and +8 m.</p><p>Suggested action: correct only the local axis label to “position x (m)”, keeping the original path and answer. Alternatively, leave this label for the planned exercise revision. The proposed label-only edit has not been made.</p>'
    page+='</section>'
page+='<section id="applied"><h2>Applied corrections</h2>'
sections=load('maintained/sections.json')['sections'];batch={'changes':load('proposals/1.1/upstream-batch-02.json')['changes']+load('proposals/1.1/upstream-batch-03.json')['changes']}
for change in batch['changes']:
    rec=load(change['record']);sec=next(x for x in sections if x['id']=='cnx:'+rec['module'])
    page+='<h3>'+change['id']+' — '+html.escape(sec['title'])+'</h3><p>'+html.escape(change['reason'])+'</p><ul>'+''.join('<li>'+html.escape(a)+' → '+html.escape(b)+'</li>' for a,b in change['substitutions'])+'</ul><p><a href="../../course-full/sections/'+sec['slug']+'/index.html#'+rec['module']+'--'+rec['source_object'].encode().hex()+'">Updated development section</a></p>'
page+='</section><p>Source: OpenStax College Physics 2e, CC BY 4.0, <a href="https://github.com/openstax/osbooks-college-physics-bundle/tree/'+data['upstream_commit']+'">pinned February 4, 2026 snapshot</a>. Individual image credit for the displayed path diagram: OpenStax textbook diagram; no separate third-party credit in its source caption.</p></html>'
(OUT/'index.html').write_text('\n'.join(x.rstrip() for x in page.splitlines())+'\n',encoding='utf-8',newline='\n')
shutil.copytree(OUT,ROOT/'prototype/dist/review-1.1/backport-review',dirs_exist_ok=True)
print('Review page: http://127.0.0.1:8765/review-1.1/backport-review/')
