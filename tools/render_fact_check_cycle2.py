"""Render the second factual-review cycle. Read-only with respect to canonical content."""
from pathlib import Path
import json,html,re,shutil,sys,hashlib,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'prototype'))
from native_math import native_math
P=ROOT/'proposals/1.1/fact-check-cycle2.json';packet=json.loads(P.read_text(encoding='utf-8'));out=ROOT/'reports/1.1/fact-check-cycle2';out.mkdir(parents=True,exist_ok=True)
esc=lambda s:html.escape(str(s),quote=True)
def plain(e):
 if e.tag.split('}')[-1] in ('annotation','annotation-xml'):return ''
 return (e.text or '')+''.join(plain(c)+(c.tail or '') for c in e)
def context(i,anchor=None):return '../../course-full/sections/'+i['slug']+'/index.html#'+i['module']+'--'+(anchor or i['anchor']).encode().hex()
def render(s,i):
 def visit(e):
  tag=e.tag.split('}')[-1]
  if tag=='math':return native_math(e)[0]
  content=esc(e.text or '')+''.join(visit(c)+esc(c.tail or '') for c in e)
  if tag=='link':return '<a href="'+esc(e.get('url') or context(i,e.get('target-id',i['anchor'])))+'">'+(content or '[existing textbook reference]')+'</a>'
  t={'para':'p','item':'p','caption':'p','term':'strong','emphasis':'em','table':'table','row':'tr','entry':'td','title':'h4','footnote':'small'}.get(tag)
  return '<'+t+'>'+content+'</'+t+'>' if t else content
 return visit(E.fromstring(s))
css='body{font:18px/1.6 Georgia,serif;max-width:1240px;margin:auto;padding:24px;color:#24383c}a{color:#075b72;overflow-wrap:anywhere}h1,h2,h3{line-height:1.25}section{border-top:1px solid #bbc;padding:1.5em 0;scroll-margin-top:15px}.cols{display:grid;grid-template-columns:1fr 1fr;gap:20px}.box{background:#f3f6f7;padding:18px;min-width:0;overflow:auto}.notice{background:#eaf2f4;padding:18px}.hold{background:#fff4db;padding:18px}table{border-collapse:collapse;font-size:.85em}td{border:1px solid #bbc;padding:6px}math{font-family:"STIX Two Math",math}.status{font:14px sans-serif}summary{cursor:pointer}del{background:#ffe5e5}ins{background:#e0f2dc;text-decoration:none}@media(max-width:720px){body{padding:16px}.cols{display:block}.box{margin:12px 0}}'
page=['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>1.1 factual review — cycle 2</title><style>'+css+'</style></head><body><h1>Introduction to Physics: factual review, cycle 2</h1><p class="notice">Priority 1: radiation/medical explanations and electrical safety. 11 proposed corrections and two coordinated decisions. <strong>No changes in this packet are applied.</strong> The current textbook already includes the approved first cycle.</p><p><a href="../fact-check-review/">First-cycle review</a> · <a href="../../course-full/">1.1 preview</a> · <a href="review.md">Readable Markdown</a></p><ul>']
page+=['<li><a href="#'+i['id']+'">'+i['id']+' — '+esc(i['title'])+'</a></li>' for i in packet['items']];page+=['</ul>']
md=['# Factual review cycle 2 — 1.1','',packet['scope'],'','No cycle-2 edits applied.','']
for i in packet['items']:
 assert hashlib.sha256((ROOT/i['source_path']).read_bytes()).hexdigest()==i['source_sha256']
 before=i['before_xml']
 for e in i['edits']:
  assert e['before'] in before
  before=before.replace(e['before'],e['after'])
 if i['proposed_xml']:assert before==i['proposed_xml']
 page+=['<section id="'+i['id']+'"><h2>'+i['id']+' — '+esc(i['title'])+'</h2><p class="status">'+esc(i['status'])+' · '+esc(i['section_title'])+'</p><p>'+esc(i['reason'])+'</p><p><a href="'+context(i)+'">View current textbook context</a></p>']
 md+=['## '+i['id']+' — '+i['title'],'',i['reason'],'']
 for passage in [i]+i.get('related_passages',[]):
  if passage is not i:page+=['<h3>'+esc(passage['title'])+'</h3><p><a href="'+context(i,passage['anchor'])+'">View related passage</a></p>']
  after=render(passage['proposed_xml'],i) if passage.get('proposed_xml') else '<p class="hold">Coordinated author decision needed; no replacement drafted.</p>'
  page+=['<div class="cols"><div class="box"><h3>Current 1.1 preview</h3>'+render(passage['before_xml'],i)+'</div><div class="box"><h3>Proposed — not applied</h3>'+after+'</div></div>']
  md+=['**Current:** '+re.sub(r'\s+',' ',plain(E.fromstring(passage['before_xml']))).strip(),'']
  if passage.get('proposed_xml'):md+=['**Proposed:** '+re.sub(r'\s+',' ',plain(E.fromstring(passage['proposed_xml']))).strip(),'']
 if i.get('revision_note'):page+=['<p class="notice">'+esc(i['revision_note'])+'</p>'];md+=[i['revision_note'],'']
 page+=['<details><summary>Exact proposed substitutions</summary><ul>'+''.join('<li><del>'+esc(e['before'])+'</del> → <ins>'+esc(e['after'])+'</ins></li>' for e in i['edits'])+'</ul></details>']
 page+=['<ul>'+''.join('<li><a href="'+esc(s['url'])+'">'+esc(s['title'])+'</a></li>' for s in i['sources'])+'</ul></section>'];md+=['- ['+s['title']+']('+s['url']+')' for s in i['sources']]+['']
page+=['<section id="scope"><h2>Coverage and remaining dependencies</h2><p>These are targeted checks of named leads and directly connected claims, not certification of every paragraph, table, exercise, or medical statement.</p><ul>']
for d in packet['dispositions']:page+=['<li><strong>'+esc(d['topic'])+' — '+esc(d['status'])+':</strong> '+esc(d['note'])+'</li>'];md+=['- **'+d['topic']+' — '+d['status']+':** '+d['note']]
page+=['</ul></section></body></html>']
for name,lines in [('index.html',page),('review.md',md)]:
 (out/name).write_text('\n'.join(line.rstrip() for line in '\n'.join(lines).splitlines())+'\n',encoding='utf-8',newline='\n')
dest=ROOT/'prototype/dist/review-1.1/fact-check-cycle2';dest.mkdir(parents=True,exist_ok=True)
for name in ['index.html','review.md']:shutil.copyfile(out/name,dest/name)
print('Rendered 13 items: http://127.0.0.1:8765/review-1.1/fact-check-cycle2/')
