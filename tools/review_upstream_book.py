"""Inventory the maintained book against the pinned CC BY archive; never edit content.

Differences are candidates, not automatic corrections. A shared identifier establishes
correspondence, not permission to overwrite an adaptation or import third-party media.
"""
from pathlib import Path
import collections, difflib, hashlib, html, json, re, shutil, sys, tarfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'prototype'))
from native_math import native_math
C = '{http://cnx.rice.edu/cnxml}'
M = '{http://www.w3.org/1998/Math/MathML}'
OUT = ROOT/'reports/1.1/upstream-book'
OUT.mkdir(parents=True, exist_ok=True)
def load(p): return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(b): return hashlib.sha256(b).hexdigest()
def save(p, data): p.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')
def tag(e): return e.tag.rsplit('}',1)[-1]
def text(e):
    if e.tag == M+'math': return ' [MATH] '
    return (e.text or '')+''.join(text(c)+(c.tail or '') for c in e)
def norm(e): return ' '.join(text(e).split())
def ids(root): return {e.get('id'): e for e in root.iter() if e.get('id')}
def fragment(e):
    if e.tag == M+'math':
        try: return native_math(e)[0]
        except Exception: return '<code>'+html.escape(ET.tostring(e,encoding='unicode'))+'</code>'
    body = html.escape(e.text or '')+''.join(fragment(c)+html.escape(c.tail or '') for c in e)
    if tag(e) == 'emphasis': return '<em>'+body+'</em>'
    if tag(e) == 'link': return body or '<span class="muted">[reference]</span>'
    if tag(e) == 'image': return '<span class="muted">[image]</span>'
    return body
def math_records(root):
    parents={c:p for p in root.iter() for c in p}; counts=collections.Counter(); result={}
    for e in root.iter(M+'math'):
        a=e
        while a in parents and not a.get('id'): a=parents[a]
        owner=a.get('id','module'); counts[owner]+=1
        rendered=native_math(e)[0]
        tokens=[(tag(n),''.join(n.itertext()).strip()) for n in ET.fromstring(rendered).iter() if tag(n) in ('mi','mo','mn','mtext')]
        result[owner+'@'+str(counts[owner])]={'rendered':rendered,'tokens':tokens}
    return result

ref=load('metadata/upstream-cc-by-reference.json')
assert ref['license']=='CC-BY-4.0'
for evidence in ref['evidence']:
    assert sha((ROOT/evidence['local_path']).read_bytes())==evidence['sha256']
archive=ROOT/ref['archive']['local_path']
assert sha(archive.read_bytes())==ref['archive']['sha256']
allowed={e.get('document') for e in ET.parse(ROOT/'references/college-physics-2e-cc-by/collections/college-physics-2e.collection.xml').iter() if e.get('document')}
up={}; media={}
with tarfile.open(archive,'r|gz') as tar:
    for member in tar:
        match=re.search(r'/modules/(m\d+)/index.cnxml$',member.name)
        if match and match[1] in allowed:
            b=tar.extractfile(member).read(); root=ET.fromstring(b)
            up[match[1]]={'root':root,'ids':ids(root),'sha256':sha(b),'title':''.join(root.find(C+'title').itertext())}
        elif '/media/' in member.name and member.isfile():
            media[member.name.split('/media/',1)[1]]=sha(tar.extractfile(member).read())
assert set(up)==allowed
owners=collections.defaultdict(set)
for mid,u in up.items():
    for ident in u['ids']: owners[ident].add(mid)
prior={s:m for m in load('metadata/upstream-map.proposed.json')['mappings'] for s in m['local_sections']}
sections=load('maintained/sections.json')['sections']
mapping=[]; rows=[]; all_changes=[]
for sec in sections:
    mid=sec['id'].split(':')[1]; b=(ROOT/sec['source']).read_bytes(); root=ET.fromstring(b); local=ids(root)
    hits=collections.Counter(k for ident in local for k in owners[ident] if len(owners[ident])==1)
    mapped={u['module_id'] for u in prior[sec['id']]['upstream_sections']}
    # Two unique shared IDs cover small introductions; large sections require five.
    threshold=2 if len(local)<=10 else 5
    mapped.update(k for k,n in hits.items() if n>=threshold)
    if mid in up: mapped.add(mid)
    evidence=[]
    for k in sorted(mapped):
        evidence.append({'module_id':k,'title':up[k]['title'],'unique_shared_ids':hits[k],
                         'shared_ids':sorted(local.keys() & up[k]['ids'].keys()),'upstream_sha256':up[k]['sha256'],
                         'upstream_only_ids':sorted(up[k]['ids'].keys()-local.keys()),
                         'prior_candidate':any(u['module_id']==k for u in prior[sec['id']]['upstream_sections'])})
    mapping.append({'local_sections':[sec['id']],'upstream_sections':evidence,
                    'status':'correspondence-supported; applicability requires review' if mapped else 'no-supported-match',
                    'local_sha256':sha(b),'local_only_ids':sorted(i for i in local if not any(i in up[k]['ids'] for k in mapped)),
                    'intentional_differences':'Preserve until individually reviewed; unmatched upstream content is not an instruction to restore it.'})
    changes=[]; local_math=math_records(root)
    for k in sorted(mapped):
        u=up[k]; shared=local.keys() & u['ids'].keys()
        def add(kind,ident,before,after,**extra):
            key=sha((mid+'|'+k+'|'+kind+'|'+ident).encode())[:16]
            changes.append({'id':'UP-'+key,'kind':kind,'local_module':mid,'upstream_module':k,'source_id':ident,
                            'status':'unreviewed-difference','local':before,'upstream':after,**extra})
        for ident in sorted(shared):
            a=local[ident]; z=u['ids'][ident]
            # Avoid duplicate parent records; tables, lists and paragraphs compare at leaves.
            prose={'para','caption','title','meaning','item','entry','label'}
            if tag(a) in prose and not any(tag(c) in prose for c in a.iter() if c is not a):
                if norm(a)!=norm(z): add('prose',ident,norm(a),norm(z),local_html=fragment(a),upstream_html=fragment(z))
            if a.get('alt')!=z.get('alt'): add('accessibility',ident,a.get('alt'),z.get('alt'))
            if tag(a) in ('para','caption','meaning','entry'):
                al=[dict(e.attrib) for e in a.iter(C+'link')]; zl=[dict(e.attrib) for e in z.iter(C+'link')]
                if al!=zl: add('references',ident,al,zl)
        remote_math=math_records(u['root'])
        for key in sorted(local_math.keys() & remote_math.keys()):
            a=local_math[key]; z=remote_math[key]
            if a['rendered']!=z['rendered']:
                kind='math-token-change' if a['tokens']!=z['tokens'] else 'math-markup-change'
                add(kind,key,a['rendered'],z['rendered'])
        missing_local=sorted(key for key in local_math.keys()-remote_math.keys() if key.split('@')[0] in shared)
        missing_upstream=sorted(key for key in remote_math.keys()-local_math.keys() if key.split('@')[0] in shared)
        if missing_local or missing_upstream: add('math-structure',k,missing_local,missing_upstream)
        for ident in sorted(shared):
            a=local[ident]; z=u['ids'][ident]
            if tag(a)!='media': continue
            for ai,zi in zip(a.iter(C+'image'),z.iter(C+'image')):
                path=(ROOT/sec['source']).parent/ai.get('src',''); remote=Path(zi.get('src','')).name
                ah=sha(path.read_bytes()) if path.is_file() else None; zh=media.get(remote)
                if ah!=zh:add('media',ident,{'path':ai.get('src'),'sha256':ah},{'path':zi.get('src'),'sha256':zh},note='Different bytes do not prove a corrected figure. Check resolution, content, and individual credit before importing.')
    for change in changes:
        e=local.get(change['source_id'].split('@')[0]); parents={c:p for p in root.iter() for c in p}
        ancestors=[]
        while e is not None:
            ancestors.append(tag(e)+' '+e.get('class','')); e=parents.get(e)
        change['exercise_context']=any('exercise' in a or 'solution' in a or 'problem' in a for a in ancestors)
        change['credit_review_required']=change['kind']=='media' or bool(re.search(r'credit:|copyright|license|CC BY|noncommercial|share.?alike',str(change['upstream']),re.I))
    counts=dict(collections.Counter(x['kind'] for x in changes))
    row={'module':mid,'title':sec['title'],'slug':sec['slug'],'local_sha256':sha(b),'upstream_modules':sorted(mapped),'counts':counts,'changes':changes}
    save(OUT/(mid+'.json'),row); rows.append(row); all_changes.extend(changes)

manifest={'schema_version':1,'upstream_commit':ref['commit'],'license':'CC-BY-4.0','mappings':mapping,
          'policy':'Evidence-backed candidate correspondences; support one-to-many and many-to-one. No automatic content merge. Individual credits require review.'}
save(ROOT/'metadata/upstream-map.1.1.json',manifest)
summary={'upstream_commit':ref['commit'],'archive_sha256':ref['archive']['sha256'],'upstream_collection_modules':len(up),
         'local_sections':len(rows),'mapped_sections':sum(bool(r['upstream_modules']) for r in rows),
         'unmapped_sections':[r['module'] for r in rows if not r['upstream_modules']],
         'counts':dict(collections.Counter(c['kind'] for c in all_changes)),
         'exercise_context_differences':sum(c['exercise_context'] for c in all_changes),
         'status':'Inventory only; differences are not yet classified as applicable corrections.',
         'limitations':['Two-way comparison cannot distinguish every author adaptation from an upstream correction.',
                       'ID changes and additions/removals require structural review; shared-ID matching does not cover them completely.',
                       'Math markup changes have identical token lists but can still change layout or grouping; token changes can also be only formatting.',
                       'Individual image/source credit compatibility must be checked before incorporation.'],
         'sections':[{k:v for k,v in r.items() if k!='changes'} for r in rows]}
save(OUT/'summary.json',summary)
style='<style>body{font:18px/1.6 Georgia;max-width:1100px;margin:auto;padding:24px;color:#20343c}a{color:#12647b;overflow-wrap:anywhere}article{border-top:1px solid #aaa;margin:2em 0;padding-top:1em}.columns{display:grid;grid-template-columns:1fr 1fr;gap:20px}.box{min-width:0;overflow:auto;padding:12px;background:#f4f6f6}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:13px}.muted{color:#59666a}math{font-size:1.1em}table{border-collapse:collapse;width:100%}td,th{padding:8px;text-align:left;border-bottom:1px solid #ccc}@media(max-width:700px){.columns{display:block}}</style>'
def head(title):return '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title>'+style+'<h1>'+html.escape(title)+'</h1>'
source='<p>Comparison source: <a href="'+ref['repository']+'/tree/'+ref['commit']+'">OpenStax College Physics 2e, pinned February 4, 2026 CC BY 4.0 snapshot</a>. Introduction to Physics retains its existing attribution. No content is imported by this report.</p>'
index=head('1.1: whole-book upstream review')+'<p><b>Unreviewed differences, not a list of confirmed corrections.</b> SR01 and SR02 are already applied. Preserve author adaptations; defer broader rewriting. Exercise corrections remain in scope even though exercise redesign is deferred.</p>'+source+'<p><a href="applied.html">Applied corrections: first whole-book batch</a></p><p>'+str(summary['mapped_sections'])+' of '+str(len(rows))+' local sections have supported upstream correspondences. The remaining section is the local Preface. Math markup differences with identical token lists are listed separately from token changes; neither count is a count of mathematical errors.</p><table><tr><th>Section</th><th>Upstream</th><th>Differences by kind</th></tr>'
for row in rows:
    mid=row['module'];index+='<tr><td><a href="'+mid+'.html">'+html.escape(row['title'])+'</a></td><td>'+', '.join(row['upstream_modules'])+'</td><td>'+html.escape(str(row['counts']))+'</td></tr>'
    page=head(row['title'])+'<p><a href="index.html">Whole-book index</a> · <a href="'+mid+'.json">Machine-readable evidence</a> · <a href="https://intro.coaphys.xyz/sections/'+row['slug']+'/">Published 1.0 section</a></p>'+source
    page+='<p>Unreviewed differences. Neither column is automatically preferred. Math matches use owner ID and ordinal, which can shift after structural edits.</p>'
    for ch in row['changes']:
        if ch['kind']=='math-markup-change': page+='<details><summary>Math markup difference: '+html.escape(ch['source_id'])+' (same token list)</summary>'
        page+='<article id="'+ch['id']+'"><h2>'+ch['id']+' · '+ch['kind']+'</h2><p>Source '+html.escape(ch['source_id'])+' · upstream '+ch['upstream_module']+(' · exercise/solution' if ch['exercise_context'] else '')+'</p><div class="columns">'
        for side,label in [('local','Maintained text'),('upstream','Pinned upstream')]:
            if ch['kind']=='prose': body=ch[side+'_html']
            elif ch['kind'] in ('math-token-change','math-markup-change'):body=ch[side]
            else:body='<pre>'+html.escape(json.dumps(ch[side],ensure_ascii=False,indent=2))+'</pre>'
            page+='<div class="box"><h3>'+label+'</h3>'+body+'</div>'
        page+='</div></article>'
        if ch['kind']=='math-markup-change': page+='</details>'
    (OUT/(mid+'.html')).write_text(page+'</html>',encoding='utf-8',newline='\n')
(OUT/'index.html').write_text(index+'</table><p><a href="summary.json">Summary and coverage limits</a></p></html>',encoding='utf-8',newline='\n')
batch=load('proposals/1.1/upstream-batch-01.json')
page=head('Applied upstream corrections: batch 1')+'<p><a href="index.html">Whole-book review index</a></p>'+source+'<p>Applied for 1.1 under the author’s instruction to backport applicable CC BY upstream corrections. Only the listed wording changes were made; local MathML, media, links, IDs, and numbering are preserved.</p>'
for entry in batch['changes']:
    record=load(entry['record']); sec=next(s for s in sections if s['id']=='cnx:'+record['module'])
    page+='<article id="'+entry['id']+'"><h2>'+html.escape(sec['title'])+'</h2><p>'+html.escape(entry['reason'])+'</p><ul>'
    for a,b in entry['substitutions']:page+='<li><del>'+html.escape(a)+'</del> → <ins>'+html.escape(b)+'</ins></li>'
    page+='</ul><p><a href="../../course-full/sections/'+sec['slug']+'/index.html#'+record['module']+'--'+record['source_object'].encode().hex()+'">Updated development text in context</a></p></article>'
(OUT/'applied.html').write_text(page+'</html>',encoding='utf-8',newline='\n')
shutil.copytree(OUT,ROOT/'prototype/dist/review-1.1/upstream-book',dirs_exist_ok=True)
print(json.dumps({k:v for k,v in summary.items() if k!='sections'}))
