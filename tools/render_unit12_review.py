"""Build the internal Unit 1/2 review page from journaled corrections."""
from pathlib import Path
import json,html,shutil,sys,xml.etree.ElementTree as ET,base64
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'prototype'))
from native_math import native_math
OUT=ROOT/'reports/1.1/unit12-review';OUT.mkdir(parents=True,exist_ok=True)
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def render(xml):
    def visit(e):
        tag=e.tag.rsplit('}',1)[-1]
        if tag=='math':return native_math(e)[0]
        if tag=='image':return ''
        if tag=='media':return '<p><strong>Image description:</strong> '+html.escape(e.get('alt',''))+'</p>'
        body=html.escape(e.text or '')+''.join(visit(c)+html.escape(c.tail or '') for c in e)
        if tag=='link':return body or '<span>[existing reference]</span>'
        if tag in ('para','meaning','caption'):return '<p>'+body+'</p>'
        if tag=='emphasis':return '<em>'+body+'</em>'
        return body
    return visit(ET.fromstring('<wrapper xmlns="http://cnx.rice.edu/cnxml" xmlns:m="http://www.w3.org/1998/Math/MathML">'+xml+'</wrapper>'))
summary=load('reports/1.1/unit12-review/summary.json');batch=load('proposals/1.1/upstream-batch-04.json');sections={x['id'].split(':')[1]:x for x in load('maintained/sections.json')['sections']}
style='body{font:18px/1.6 Georgia;max-width:1200px;margin:auto;padding:24px;color:#24383c}a{color:#075b72;overflow-wrap:anywhere}h1,h2,h3{line-height:1.25}section{border-top:1px solid #bbc;padding:1.5em 0}.cols{display:grid;grid-template-columns:1fr 1fr;gap:20px}.box{background:#f3f6f7;padding:18px;min-width:0;overflow:auto}img{max-width:100%;height:auto}math{font-family:"STIX Two Math",math;font-size:1.1em}.notice{padding:20px;background:#eaf2f4}li{margin:.35em 0}@media(max-width:720px){.cols{display:block}.box{margin-bottom:1em}body{padding:16px}}'
page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>1.1 Units 1–2 backport review</title><style>'+style+'</style><h1>1.1 backport review: Units 1–2</h1>'
page+='<p class="notice">Reviewed '+str(summary['section_count'])+' sections, including the remaining Kinematics differences, all of Dynamics, and all five Unit 2 chapters. Applied '+str(len(batch['changes']))+' scoped correction records. The plasma expansion is deferred to broader revision by your decision; no chapter or section restructuring was performed. This is a development draft. The full-book backport and release PDF checks remain unfinished.</p><p><a href="../../course-full/">Current 1.1 development textbook</a> · <a href="#plasma">Deferred coverage expansion</a> · <a href="#retained">Retained differences and limitations</a></p>'
page+='<ul>'+''.join('<li><a href="#'+x['id']+'">'+x['id']+' — '+html.escape(sections[x['module']]['title'])+'</a>: '+html.escape(x['reason'])+'</li>' for x in batch['changes'])+'</ul>'
for x in batch['changes']:
    r=load(x['record']);sec=sections[x['module']];anchor=x['module']+'--'+x.get('review_source_id',x['source_id']).encode().hex()
    if x.get('review_followup'):
        followup=load(x['review_followup'])
        original=load('proposals/author-corrections/U12-35.json')
        # Show the original paragraph against the final applied wording, while
        # preserving the ordered correction records for exact reconstruction.
        r=dict(r)
        for side in ('before','after'):
            paragraph=original['before'] if side=='before' else followup['after']
            r[side]=(r[side]+paragraph) if x['id']=='U12-33' else paragraph
    page+='<section id="'+x['id']+'"><h2>'+x['id']+' — '+html.escape(sec['title'])+'</h2><p>'+html.escape(x['reason'])+'</p><p><a href="../../course-full/sections/'+sec['slug']+'/index.html#'+anchor+'">View in development textbook</a></p><div class="cols">'
    for side,label in [('before','Before'),('after','Applied for 1.1')]:
        if r.get('encoding')=='base64':
            name=x['id']+'-'+side+'.jpg';(OUT/name).write_bytes(base64.b64decode(r[side]));body='<img src="'+name+'" alt="'+html.escape(label+' — '+x['reason'],quote=True)+'">'
        else:body=render(r[side])
        page+='<div class="box"><h3>'+label+'</h3>'+body+'</div>'
    page+='</div></section>'
page+='<section id="plasma"><h2>Deferred: plasma in “What Is a Fluid?”</h2><p>Upstream expands the three-phase overview to include plasma, coordinating three paragraphs, the figure caption and a fourth panel. This adds coverage; it is not needed to repair the existing solids/liquids/gases explanation. Author decision (September 19, 2026): defer this expansion to the broader content revision. No part of it has been imported.</p><div class="cols">'
for name,path,label in [('phases-local.jpg','maintained/media/Figure_12_01_01a.jpg','Current three-phase figure'),('phases-upstream.jpg','tmp/unit12-media/Figure_12_01_01a.jpg','Pinned upstream four-phase figure (reference only)')]:
    shutil.copyfile(ROOT/path,OUT/name);page+='<div class="box"><h3>'+label+'</h3><img src="'+name+'" alt="'+label+'"></div>'
page+='</div></section><section id="retained"><h2>What was retained</h2><p>All source identities, section URLs, exercise organization and numbering profiles are preserved. The structured dispositions record why each remaining shared-object difference was retained or held.</p><ul><li>Preserved vector notation, explicit Δt and Δh, total kinetic energy terminology, and the conceptual treatment without restored trigonometric derivations.</li><li>Retained correct rocket arithmetic, the rate-of-change definition of acceleration, the author’s gyroscope/precession explanation, and the roller-coaster scenario.</li><li>Did not restore AP preparation, removed examples, the omitted energy table, or expanded historical anecdotes. Changed wrapper IDs and relocated content were checked separately.</li><li>The bridge/catenary caption remains a possible broader clarification: a hanging chain and a uniformly loaded bridge deck have different load distributions. Upstream’s deletion alone does not fully explain this.</li></ul>'
page+='<details><summary>Section-by-section retention notes</summary>'+''.join('<h3>'+html.escape(sections[mid]['title'])+'</h3><p>'+html.escape(reason)+'</p>' for mid,reason in summary['module_rationales'].items())+'</details><h3>Limits of this comparison</h3><ul>'+''.join('<li>'+html.escape(x)+'</li>' for x in summary['limitations'])+'</ul></section>'
page+='<p>Source for backports: OpenStax College Physics 2e, CC BY 4.0, <a href="https://github.com/openstax/osbooks-college-physics-bundle/tree/f98d7a792138a6133fe7267d17e70aa04e9ccbed">pinned February 4, 2026 snapshot</a>. Original image credits remain in the book. The new waveform and gauge-pressure assets are OpenStax diagrams without separate third-party credits in their source captions.</p></html>'
(OUT/'index.html').write_text(page+'\n',encoding='utf-8',newline='\n')
# The initial comparison and ledger contain internal source evidence, not public site assets.
dest=ROOT/'prototype/dist/review-1.1/unit12-review';dest.mkdir(parents=True,exist_ok=True)
for p in OUT.iterdir():
    if p.suffix in ('.html','.jpg'):shutil.copyfile(p,dest/p.name)
print('http://127.0.0.1:8765/review-1.1/unit12-review/')
