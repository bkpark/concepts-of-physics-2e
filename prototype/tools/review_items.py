"""Build an author-facing review page from source context and archived PDF pages."""
from pathlib import Path
import runpy,sys,json,re,subprocess,hashlib
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'prototype'));sys.argv=['build.py','course','--all']
b=runpy.run_path(str(ROOT/'prototype/build.py'))
esc=b['esc'];local=b['local'];roots=b['roots'];parents=b['parents'];registry=b['registry'];anchor=b['anchor']
out=ROOT/'prototype/dist/course-full';target=out/'review-items';target.mkdir(exist_ok=True)
assets=out/'review-assets';assets.mkdir(exist_ok=True)
pdf=ROOT.parent/'references/introduction-to-physics-12.1.pdf'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()=='9f1fd756b7892eca543f1b57c4fae433fa9509361e3beb51d3c306eb3deb6120'
evidence=[(466,'Equation 13.17, near the bottom of printed page 460.','A mixed Content/Presentation MathML operator is not supported by the adapter. This is not yet a claim that the equation is wrong.'),(496,'Second Check Your Understanding solution, printed page 490.','The subscript has three children instead of two. The archived PDF also displays this notation awkwardly.'),(610,'Exercise 15.179, solution (b), printed page 604.','Several subscripts have only one child. This occurs in an exercise solution; broader exercise revision is deferred.')]
for n,(page,_,_) in enumerate(evidence,1):
 subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-scale-to','1600','-png',str(pdf),str(assets/f'math-{n}')],check=True)
items=[];maths=[i for i in json.loads((ROOT/'reports/course-full-findings.json').read_text(encoding='utf-8'))['findings'] if i['kind']=='unresolved-math'];refs=[i for i in json.loads((ROOT/'reports/course-full-findings.json').read_text(encoding='utf-8'))['findings'] if i['kind'] in ('reference-outside-book','source-reference-unresolved')] # Freeze review IDs across repairs.
assert len(maths)==3 and len(refs)==25
seen={}
for kind,findings in [('M',maths),('X',refs)]:
 for number,item in enumerate(findings,1):
  code=kind+str(number).zfill(2);mid=item['module'];r=roots[mid];ps=parents[mid]
  applied=None;wording_proposal=None
  change_path=ROOT/'proposals/author-corrections'/f'{code}.json'
  if change_path.exists() and (kind=='X' or json.loads(change_path.read_text(encoding='utf-8'))['status']=='applied-author-directed'):
   change=json.loads(change_path.read_text(encoding='utf-8'))
   if change.get('proposal_ref'):change=json.loads((ROOT/change['proposal_ref']).read_text(encoding='utf-8'))
   if change['status']=='applied-author-directed':
    applied=change
    if applied.get('change_kind')!='replace-prose':item={**item,'document':applied['target_document'],'target':applied['target_id']}
   else:
    assert change['status']=='preview-awaiting-author-confirmation'
    wording_proposal=change
  if applied and applied.get('change_kind')=='replace-prose':
   e=next(e for e in r.iter() if e.get('id')==applied['source_object'])
  elif kind=='M':e=list(r.iter('{http://www.w3.org/1998/Math/MathML}math'))[int(item['key'].rsplit('-',1)[1])-1]
  else:
   key=(mid,item['document'],item.get('target'));matches=[e for e in r.iter('{http://cnx.rice.edu/cnxml}link') if e.get('document',mid)==item['document'] and e.get('target-id')==item.get('target') and not e.get('url')]
   occurrence=seen.get(key,0);e=matches[occurrence];seen[key]=occurrence+1
  ancestors=[];p=e
  while p in ps:p=ps[p];ancestors.append(p)
  exercise=e if local(e)=='exercise' else next((p for p in ancestors if local(p)=='exercise'),None)
  context=next((p for p in ancestors if local(p) in ('para','equation','problem','solution')),ps[e])
  if applied and applied.get('change_kind')=='replace-prose':context=e
  source=e
  while not source.get('id') and source in ps:source=ps[source]
  source_url='../sections/'+registry[mid]['candidate_slug']+'/index.html#'+anchor(mid,source.get('id'))
  renderer=b['Renderer'](mid,projection=True)
  before=list(r.iter());renderer.math_index=sum(local(x)=='math' for x in before[:before.index(context)])
  html=renderer.render(context).replace('../../sections/','../sections/').replace('../../media/','../media/')
  html=re.sub(r' id="[^"]*"','',html)
  status='Exercise context — editorial cleanup deferred.' if exercise is not None else 'Main section content.'
  body=f'<section class="review-card" id="{code}"><h2>{code} · {esc(b["course"].get(mid,""))} {esc(registry[mid]["title"])}</h2><p class="status">{status}</p><p><a href="{source_url}">Open this location in the textbook</a></p>'
  if kind=='M':
   page,location,explanation=evidence[number-1]
   body+='<p>'+esc(explanation)+'</p><h3>Current build context</h3><div class="context">'+html+'</div>'
   proposal_path=ROOT/'proposals/author-corrections'/f'{code}.json'
   if proposal_path.exists():
    proposal=json.loads(proposal_path.read_text(encoding='utf-8'))
    if proposal['status']=='applied-author-directed':
     body+='<p class="status"><strong>Applied:</strong> '+esc(proposal['reason'])+'</p>'
    elif proposal['status']=='deferred-by-author':
     body+='<p class="status"><strong>Deferred by author.</strong> Source unchanged. Only this expression has a review placeholder; it does not prevent the surrounding content from rendering.</p>'
    else:
     assert hashlib.sha256((ROOT/proposal['source_path']).read_bytes()).hexdigest()==proposal['source_sha256']
     math,_=b['native_math'](b['ET'].fromstring(proposal['after']))
     body+='<div id="'+code+'-proposal"><h3>Proposed rendering from your AsciiMath</h3><p>'+esc(proposal['preview_note'])+'</p><div class="context proposal-math">'+math+'</div></div>'
   body+=f'<details><summary>View original CNX PDF: {esc(location)} (PDF page {page})</summary><p>This is the unchanged archived rendering, not a proposed correction.</p><a href="../review-assets/math-{number}.png"><img src="../review-assets/math-{number}.png" alt="Archived CNX PDF page {page}; {esc(location)}"></a></details>'
  else:
   destination=item['document']+('#'+item['target'] if item.get('target') else '')
   if applied:
    body+='<p><strong>Applied:</strong> '+esc(applied['reason'])+'</p><div class="context">'+html+'</div>'
   else:body+='<p>Missing destination: <code>'+esc(destination)+'</code>. '+('The referenced module is outside the recovered book.' if item['kind']=='reference-outside-book' else 'The target ID is absent from this module.')+'</p><div class="context">'+html+'</div>'
  if wording_proposal:
   assert hashlib.sha256((ROOT/wording_proposal['source_path']).read_bytes()).hexdigest()==wording_proposal['source_sha256']
   body+='<div id="'+code+'-proposal"><h3>Proposed wording — not applied</h3><div class="context">'+esc(wording_proposal['replacement_text'])+'</div><p>'+esc(wording_proposal['reason'])+'</p></div>'
  xml=b['ET'].tostring(e,encoding='unicode')
  body+='<details><summary>Technical source details</summary><p>'+esc(mid+' / '+str(source.get('id')))+'</p><pre>'+esc(xml)+'</pre></details></section>'
  items.append({'id':code,'kind':kind,'module':mid,'source_id':source.get('id'),'exercise_context':exercise is not None,'source_url':source_url,'body':body,'status':'applied' if applied else ('deferred' if code=='M03' else 'pending')})
header='<h1>Expressions and cross-references for review</h1><p>Three expressions and the original 25 reference occurrences. '+str(sum(i['kind']=='X' and i['status']=='applied' for i in items))+' references corrected; '+str(sum(i['kind'] in ('reference-outside-book','source-reference-unresolved') for i in b['issues']))+' remain unresolved. Some references repeat the same destination; each occurrence is shown separately. M01 and M02 have proposed corrections below; M03’s question part and solution have been removed as requested. M01 and M02 remain unapplied proposals. Corrected references are marked Applied below.</p><p><strong>Exercise cleanup is deferred.</strong> Exercise-related findings are labeled for context, not presented as requests for a broader revision. The initial publication target remains recovered CNX content with course numbering.</p><p>Reply using item IDs such as M01 or X07. There is no need to inspect the XML unless useful.</p>'
for prefix,title in [('M','Expressions'),('X','References')]:header+='<p>'+title+': '+ ' · '.join('<a href="#'+i['id']+'">'+i['id']+'</a>' for i in items if i['kind']==prefix)+'</p>'
style='<style>.review-card{border-top:3px solid #38636d;margin-top:3rem;padding-top:1rem;scroll-margin-top:1rem}.context{padding:1rem;background:#f3f6f7}.proposal-math{font-size:1.2em;overflow-x:auto}.status{font-family:sans-serif;color:#52666d}summary{cursor:pointer;font-weight:bold;padding:1rem 0}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:12px}img{max-width:100%;height:auto}code{overflow-wrap:anywhere}</style>'
page=b['page']('Introduction to Physics: review items',header+''.join(i['body'] for i in items),'../').replace('</head>',style+'</head>')
(target/'index.html').write_text(page,encoding='utf-8',newline='\n')
manifest=[{k:v for k,v in i.items() if k!='body'} for i in items]
(ROOT/'reports/author-review-items.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
for name in ['index.html','review.html']:
 p=out/name;s=p.read_text(encoding='utf-8');s=s.replace('<main>','<main><p><a href="review-items/index.html">Open the illustrated 28-item author review</a></p>',1);p.write_text(s,encoding='utf-8',newline='\n')
print('Created 28-item review:',target/'index.html')
