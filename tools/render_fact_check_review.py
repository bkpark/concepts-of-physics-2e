"""Render read-only factual-review proposals and reproduce the screening inventory.

Run from any directory. This tool never writes to maintained/ or historical source.
Serialized XML in the proposal file is for review, not a patch to apply wholesale.
"""
from pathlib import Path
import collections, hashlib, html, json, re, shutil, sys
import xml.etree.ElementTree as E

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'prototype'))
from native_math import native_math

OUT = ROOT / 'reports/1.1/fact-check-review'
OUT.mkdir(parents=True, exist_ok=True)
def load(path): return json.loads((ROOT / path).read_text(encoding='utf-8'))
def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
def esc(text): return html.escape(str(text), quote=True)
sections = {s['id'].split(':')[1]: s for s in load('maintained/sections.json')['sections']}
packet = load('proposals/1.1/fact-check.json')
items = packet['items']
patterns = {
    'history': r'\b(1[5-9]\d\d|20[0-2]\d|Nobel|discovered|discovery|first .*?observ|century|died)\b',
    'health-environment': r'\b(cancer|radiation dose|safe|risk|CFC|ozone|global warming|greenhouse|climate|MRI|X-ray|health|medical|DNA|hearing loss|ultrasound)\b',
    'definitions-current': r'\b(defined|definition|exactly|currently|today|at present|recently)\b',
}
def plain(e):
    if e.tag.rsplit('}', 1)[-1] in ('annotation', 'annotation-xml'): return ''
    return (e.text or '') + ''.join(plain(c) + (c.tail or '') for c in e)

inventory = []
coverage = []
for mid, sec in sections.items():
    path = ROOT / sec['source']
    tree = E.parse(path)
    parents = {c: e for e in tree.iter() for c in e}
    eligible = 0
    found = 0
    for el in tree.iter():
        tag = el.tag.rsplit('}', 1)[-1]
        if tag not in ('para', 'caption'): continue
        ancestors = []; parent = el
        while parent in parents:
            parent = parents[parent]; ancestors.append(parent)
        if any(a.tag.rsplit('}', 1)[-1] in ('exercise', 'solution') for a in ancestors): continue
        eligible += 1
        text = re.sub(r'\s+', ' ', plain(el)).strip()
        cats = [c for c, pattern in patterns.items() if re.search(pattern, text, re.I)]
        if not cats: continue
        found += 1
        anchor = el.get('id') or next((a.get('id') for a in ancestors if a.get('id')), None)
        linked = [i['id'] for i in items if i['module'] == mid and i['anchor'] == anchor]
        inventory.append(dict(module=mid, source_id=el.get('id'), anchor=anchor, tag=tag, categories=cats,
                              text=text, review_items=linked,
                              status='see-review-item' if linked else 'screening-candidate-not-independently-certified'))
    coverage.append(dict(module=mid, title=sec['title'], source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                         paragraphs_and_captions_screened=eligible, candidate_blocks=found,
                         review_items=[i['id'] for i in items if i['module'] == mid]))

limits = [
    'All 141 canonical sections were searched. Keyword screening is not independent verification of every claim.',
    'This packet follows up selected high-risk historical, medical/environmental, SI-definition and dated-current assertions. Unlisted passages are not certified correct.',
    'Exercises/solutions, a full numerical-table audit, figure-content inspection and recalculation of every example are outside this focused pass. Some worked-example prose appears among candidates.',
    'Confirmed factual problems, source discrepancies and passages needing coordinated changes are distinguished in the item notes. Additional screening leads are recorded separately, not silently treated as cleared.',
    'All proposals are unapplied. Full XML snippets are review snapshots; later edits must preserve canonical byte structure and use the editorial ledger.',
    'External sources establish facts. No new external prose or images have been imported into the textbook; the CC BY baseline and license restrictions remain in force.',
]
summary = dict(date=packet['date'], sections=len(coverage), candidate_blocks=len(inventory),
               category_counts=dict(collections.Counter(c for i in inventory for c in i['categories'])),
               review_items=len(items), proposed_corrections=sum(bool(i['proposed_xml']) and i['category'] != 'author-discussion' for i in items),
               author_discussion=sum(i['category']=='author-discussion' for i in items), limitations=limits,
               section_coverage=coverage)
save(OUT / 'screening-inventory.json', inventory)
save(OUT / 'summary.json', summary)

def link(mid, anchor=None):
    return '../../course-full/sections/' + sections[mid]['slug'] + '/index.html' + ('#' + mid + '--' + anchor.encode().hex() if anchor else '')

def render(xml, mid):
    def visit(e):
        tag = e.tag.rsplit('}', 1)[-1]
        if tag == 'math': return native_math(e)[0]
        if tag in ('annotation','annotation-xml','image','media'): return ''
        body = esc(e.text or '') + ''.join(visit(c) + esc(c.tail or '') for c in e)
        if tag == 'link':
            target = e.get('document', mid)
            if target in sections:
                return '<a href="' + esc(link(target, e.get('target-id'))) + '">' + (body or '[existing textbook reference]') + '</a>'
            return body or '[external reference]'
        if tag in ('para','caption'): return '<p>' + body + '</p>'
        if tag in ('emphasis','term'): return '<em>' + body + '</em>'
        return body
    return visit(E.fromstring(xml))

stale=[]
for i in items:
    if hashlib.sha256((ROOT/i['source_path']).read_bytes()).hexdigest()!=i['source_sha256']: stale.append(i['id'])
css='''body{font:18px/1.6 Georgia,serif;max-width:1240px;margin:auto;padding:24px;color:#24383c}h1,h2,h3{line-height:1.25}a{color:#075b72;overflow-wrap:anywhere}section{border-top:1px solid #bbc;padding:1.5em 0;scroll-margin-top:12px}.cols{display:grid;grid-template-columns:1fr 1fr;gap:20px}.box{background:#f3f6f7;padding:18px;min-width:0;overflow:auto}.notice{background:#eaf2f4;padding:18px}.hold{background:#fff4db;padding:18px}li{margin:.4em 0}math{font-family:"STIX Two Math",math}summary{cursor:pointer}.badge{font:14px sans-serif;color:#576}details{margin:1em 0}.edits{font-size:.9em}del{background:#ffe5e5}ins{background:#e0f2dc;text-decoration:none}@media(max-width:720px){body{padding:16px}.cols{display:block}.box{margin:12px 0}}'''
page=['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>1.1 focused fact-check review</title><style>'+css+'</style></head><body>',
      '<h1>Introduction to Physics: focused fact-check for 1.1</h1>',
      '<p class="notice">'+str(summary['proposed_corrections'])+' proposed corrections and '+str(summary['author_discussion'])+' passages for discussion. <strong>None is applied.</strong> Published 1.0 and the maintained draft are unchanged. Review date: '+packet['date']+'.</p>',
      '<p>Small edits preserve surrounding wording and equations. Discussion items identify connected problems that should be decided together. These are independent factual checks, not another upstream prose backport.</p>',
      '<p><a href="#corrections">Proposed corrections</a> · <a href="#discussion">Passages needing discussion</a> · <a href="#limits">Coverage and limits</a> · <a href="review.md">Readable Markdown copy</a></p>']
if stale:page.append('<p class="hold">Canonical source has changed since this snapshot: '+', '.join(stale)+'. Reconcile before applying.</p>')
md=['# Focused fact-check for 1.1','', 'Review snapshot '+packet['date']+'. No proposals applied.','']
for category,label in [('corrections','Proposed corrections'),('discussion','Passages needing discussion')]:
    group=[i for i in items if (i['category']=='author-discussion') == (category=='discussion')]
    page.append('<h2 id="'+category+'">'+label+'</h2><ul>'+''.join('<li><a href="#'+i['id']+'">'+i['id']+' — '+esc(i['title'])+'</a></li>' for i in group)+'</ul>')
    for i in group:
        page.append('<section id="'+i['id']+'"><h2>'+i['id']+' — '+esc(i['title'])+'</h2><p class="badge">'+esc(i['section_title'])+' · '+esc(i['status'])+'</p><p>'+esc(i['reason'])+'</p><p><a href="'+esc(link(i['module'],i['anchor']))+'">View current textbook context</a></p>')
        if i['edits']:
            page.append('<details class="edits"><summary>Exact proposed substitutions</summary><ul>'+''.join('<li><del>'+esc(e['before'])+'</del> → <ins>'+esc(e['after'] or '[delete]')+'</ins></li>' for e in i['edits'])+'</ul></details>')
        page.append('<div class="cols"><div class="box"><h3>Current 1.1 draft</h3>'+render(i['before_xml'],i['module'])+'</div><div class="box"><h3>'+('Proposed — not applied' if i['proposed_xml'] else 'Decision needed')+'</h3>'+ (render(i['proposed_xml'],i['module']) if i['proposed_xml'] else '<p>'+esc(i['reason'])+'</p>')+'</div></div>')
        page.append('<ul>'+''.join('<li><a href="'+esc(s['url'])+'">'+esc(s['title'])+'</a></li>' for s in i['sources'])+'</ul></section>')
        md+=['## '+i['id']+' — '+i['title'],'',i['section_title']+' · '+i['status'],'',i['reason'],'','**Current:** '+re.sub(r'\s+',' ',plain(E.fromstring(i['before_xml']))),'']
        if i['proposed_xml']:md+=['**Proposed:** '+re.sub(r'\s+',' ',plain(E.fromstring(i['proposed_xml']))),'']
        md += ['- ['+s['title']+']('+s['url']+')' for s in i['sources']]+['']
leads=load('proposals/1.1/fact-check-followups.json')
page.append('<section id="limits"><h2>Coverage and limits</h2><ul>'+''.join('<li>'+esc(l)+'</li>' for l in limits)+'</ul><p>The screening inventory contains '+str(len(inventory))+' candidate blocks from 141 sections; category counts overlap. Most candidates are ordinary teaching statements, not suspected errors.</p><h3>Additional leads, not independently resolved</h3><ul>'+''.join('<li><strong>'+esc(x['topic'])+':</strong> '+esc(x['note'])+'</li>' for x in leads)+'</ul></section></body></html>')
md+=['## Coverage and limits','']+['- '+l for l in limits]+['','## Additional leads, not independently resolved','']+['- **'+x['topic']+':** '+x['note'] for x in leads]
(OUT/'index.html').write_text('\n'.join(page)+'\n',encoding='utf-8',newline='\n')
(OUT/'review.md').write_text('\n'.join(md)+'\n',encoding='utf-8',newline='\n')
dest=ROOT/'prototype/dist/review-1.1/fact-check-review';dest.mkdir(parents=True,exist_ok=True)
for name in ('index.html','review.md'):shutil.copyfile(OUT/name,dest/name)
print(json.dumps({k:v for k,v in summary.items() if k not in ('section_coverage','limitations')}))
print('http://127.0.0.1:8765/review-1.1/fact-check-review/')
