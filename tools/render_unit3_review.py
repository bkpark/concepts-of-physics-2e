"""Render the Unit 3 review packet from immutable correction records and held proposals."""
from pathlib import Path
import json,html,shutil,sys,base64,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'prototype'))
from native_math import native_math
OUT=ROOT/'reports/1.1/unit3-review';OUT.mkdir(parents=True,exist_ok=True)
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def esc(s):return html.escape(str(s),quote=True)
sections={x['id'].split(':')[1]:x for x in load('maintained/sections.json')['sections']}
summary=load('reports/1.1/unit3-review/summary.json');batch=load('proposals/1.1/upstream-batch-05.json');holds=load('proposals/1.1/unit3-holds.json')
def render(xml,mid):
 def visit(e):
  tag=e.tag.rsplit('}',1)[-1]
  if tag=='math':return native_math(e)[0]
  if tag=='annotation':return ''
  if tag=='image':return ''
  if tag=='media':return '<p><strong>Alternative text:</strong> '+esc(e.get('alt',''))+'</p>'
  body=esc(e.text or '')+''.join(visit(c)+esc(c.tail or '') for c in e)
  if tag=='link':
   target=e.get('document',mid);targetid=e.get('target-id');sec=sections.get(target)
   if sec:
    url='../../course-full/sections/'+sec['slug']+'/index.html'+('#'+target+'--'+targetid.encode().hex() if targetid else '')
    return '<a href="'+url+'">'+(body or '[existing reference]')+'</a>'
   return body or '[upstream reference]'
  if tag in ('para','meaning','caption'):return '<p>'+body+'</p>'
  if tag=='emphasis':return '<em>'+body+'</em>'
  if tag in ('title','label'):return '<strong>'+body+'</strong>'
  mapping={'table':'table','row':'tr','entry':'td','thead':'thead','tbody':'tbody','list':'ul','item':'li'}
  if tag in mapping:return '<'+mapping[tag]+'>'+body+'</'+mapping[tag]+'>'
  return body
 return visit(E.fromstring('<wrapper xmlns="http://cnx.rice.edu/cnxml" xmlns:m="http://www.w3.org/1998/Math/MathML">'+xml+'</wrapper>'))
def link(mid,ident):return '../../course-full/sections/'+sections[mid]['slug']+'/index.html#'+mid+'--'+ident.encode().hex()
style='body{font:18px/1.6 Georgia;max-width:1200px;margin:auto;padding:24px;color:#24383c}a{color:#075b72;overflow-wrap:anywhere}h1,h2,h3{line-height:1.25}section{border-top:1px solid #bbc;padding:1.5em 0;scroll-margin-top:12px}.cols{display:grid;grid-template-columns:1fr 1fr;gap:20px}.cols.wide{display:block}.cols.wide .box{margin-bottom:16px}.box{background:#f3f6f7;padding:18px;min-width:0;overflow:auto}img{max-width:100%;height:auto}math{font-family:"STIX Two Math",math;font-size:1.1em}.notice{padding:20px;background:#eaf2f4}.held{background:#fff4db;padding:18px}li{margin:.35em 0}table{border-collapse:collapse}td{border:1px solid #ccd;padding:6px}summary{cursor:pointer}@media(max-width:720px){.cols{display:block}.box{margin-bottom:1em}body{padding:16px}}'
page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>1.1 Unit 3 backport review</title><style>'+style+'</style><h1>1.1 backport review: Unit 3</h1>'
page+='<p>Thermal physics, electricity, magnetism, and light — 49 sections.</p><p class="notice">'+str(len(batch['changes']))+' scoped correction records applied to the maintained development draft. The six original review items below show their current resolution status. Existing section identities, numbering, organization and exercise placement are preserved. Published 1.0 is unchanged.</p>'
page+='<p><a href="../../course-full/">Development textbook</a> · <a href="#held">Items needing review</a> · <a href="#applied">Applied corrections</a> · <a href="#retained">Preserved differences and limits</a></p>'
page+='<h2 id="held">Author review and resolutions</h2><ul>'+''.join('<li><a href="#'+h['id']+'">'+h['id']+' — '+esc(h['title'])+'</a></li>' for h in holds)+'</ul>'
for h in holds:
 page+='<section id="'+h['id']+'"><h2>'+h['id']+' — '+esc(h['title'])+'</h2><p><strong>'+esc(h['status'])+'</strong></p><p>'+esc(h['reason'])+'</p><p class="held">'+esc(h['recommendation'])+'</p><p><a href="'+link(h['module'],h['source_id'])+'">View current passage in textbook</a></p><div class="cols">'
 for side,label in [('before','Before'),('after','Applied for 1.1')] if h.get('after') else [('before','Current paragraph — unchanged'),('upstream','Pinned upstream — paragraph not applied')]:
  body=render(h[side],h['module']) if h.get(side) else 'No corresponding upstream block.'
  if h['id']=='U3-H05':
   r=next(load(x) for x in h.get('records',[]) if load(x).get('encoding')=='base64');name='generator-'+side+'.jpg';(OUT/name).write_bytes(base64.b64decode(r['before' if side=='before' else 'after']));body='<img src="'+name+'" alt="'+esc(label+' generator-current diagram')+'">'+body
  page+='<div class="box"><h3>'+label+'</h3>'+body+'</div>'
 page+='</div><p>'+ ' · '.join('<a href="#'+load(r)['id']+'">Applied change '+load(r)['id']+'</a>' for r in h.get('records',[]))+'</p></section>'
page+='<h2 id="applied">Applied corrections</h2><ul>'+''.join('<li><a href="#'+x['id']+'">'+x['id']+' — '+esc(sections[x['module']]['title'])+'</a>: '+esc(x['reason'])+'</li>' for x in batch['changes'])+'</ul>'
for x in batch['changes']:
 r=load(x['record']);page+='<section id="'+x['id']+'"><h2>'+x['id']+' — '+esc(sections[x['module']]['title'])+'</h2><p>'+esc(x['reason'])+'</p><p><a href="'+link(x['module'],x['source_id'])+'">View in development textbook</a></p><div class="cols">'
 for side,label in [('before','Before'),('after','Applied for 1.1')]:
  if r.get('encoding')=='base64':
   name=x['id']+'-'+side+'.jpg';(OUT/name).write_bytes(base64.b64decode(r[side]));body='<img src="'+name+'" alt="'+esc(label+' — '+x['reason'])+'">'
  else:body=render(r[side],x['module'])
  page+='<div class="box"><h3>'+label+'</h3>'+body+'</div>'
 page+='</div></section>'
page+='<section id="retained"><h2>Preserved differences and limits</h2><p>Not every upstream change is an improvement or applicable to this adaptation. In particular, U notation, perpendicular-component formulas, omitted trigonometry and author-approved reference repairs remain. Several inconsistent upstream numbers or definitions were explicitly rejected.</p><details><summary>Section-by-section decisions (49 sections)</summary>'+''.join('<h3>'+esc(sections[mid]['title'])+'</h3><p>'+esc(reason)+'</p>' for mid,reason in summary['module_rationales'].items())+'</details><h3>Limits of this pass</h3><ul>'+''.join('<li>'+esc(x)+'</li>' for x in summary['limitations'])+'</ul></section>'
page+='<p>Update source: OpenStax College Physics 2e, CC BY 4.0, <a href="https://github.com/openstax/osbooks-college-physics-bundle/tree/f98d7a792138a6133fe7267d17e70aa04e9ccbed">pinned February 4, 2026 snapshot</a>. Diagram imports use exact pinned bytes. Original figure credits remain in the textbook. Local consistency repairs and adapted wording are distinguished in the editorial records.</p></html>'
page=page.replace('</html>', '<script>function fit(){document.querySelectorAll(".cols").forEach(c=>{if([...c.querySelectorAll("math")].some(m=>m.getBoundingClientRect().width>c.clientWidth/2-50))c.classList.add("wide");});}document.fonts.ready.then(fit);addEventListener("resize",fit);</script></html>')
(OUT/'index.html').write_text('\n'.join(line.rstrip() for line in page.splitlines())+'\n',encoding='utf-8',newline='\n')
dest=ROOT/'prototype/dist/review-1.1/unit3-review';dest.mkdir(parents=True,exist_ok=True)
for p in OUT.iterdir():
 if p.suffix in ('.html','.jpg'):shutil.copyfile(p,dest/p.name)
print('http://127.0.0.1:8765/review-1.1/unit3-review/')
