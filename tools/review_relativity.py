"""Read-only 1.1 comparison against the pinned CC BY snapshot; never edits content."""
from pathlib import Path
import collections, difflib, hashlib, html, json, shutil, subprocess, sys, tarfile
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'prototype'))
from native_math import native_math
C='{http://cnx.rice.edu/cnxml}';M='{http://www.w3.org/1998/Math/MathML}'
OUT=ROOT/'reports/1.1/special-relativity';OUT.mkdir(parents=True,exist_ok=True)
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(b):return hashlib.sha256(b).hexdigest()
def local(e):return e.tag.rsplit('}',1)[-1]
def text(e,mask=False):
    if mask and e.tag==M+'math':return ' [MATH] '
    return (e.text or '')+''.join(text(c,mask)+(c.tail or '') for c in e)
def norm(e,mask=False):return ' '.join(text(e,mask).split())
def maths(root):
    parents={c:p for p in root.iter() for c in p};counts=collections.Counter();out={}
    for e in root.iter(M+'math'):
        a=e
        while a in parents and not a.get('id'):a=parents[a]
        ident=a.get('id','module');counts[ident]+=1
        rendered,_=native_math(e);tree=ET.fromstring(rendered)
        tokens=[(local(x),''.join(x.itertext()).strip()) for x in tree.iter() if local(x) in ('mi','mn','mo','mtext')]
        out[ident+'@'+str(counts[ident])]={'rendered':rendered,'tokens':tokens}
    return out
def live(mid,slug,ident=None):
    return 'https://intro.coaphys.xyz/sections/'+slug+'/index.html'+('#'+mid+'--'+ident.encode().hex() if ident else '')
ref=load('metadata/upstream-cc-by-reference.json');proposal=load('proposals/1.1/special-relativity.json')
sections={x['id'].split(':')[1]:x for x in load('maintained/sections.json')['sections']}
assert ref['license']=='CC-BY-4.0' and ref['commit']==proposal['upstream_commit']
archive=ROOT/ref['archive']['local_path'];assert sha(archive.read_bytes())==ref['archive']['sha256']
prefix='osbooks-college-physics-bundle-'+ref['commit']+'/'
rows=[]
with tarfile.open(archive) as tar:
    for info in ref['relativity_modules']:
        mid=info['module_id'];source=ROOT/sections[mid]['source']
        a_bytes=subprocess.check_output(['git','show','cp2e-ver1.0:'+sections[mid]['source']],cwd=ROOT)
        b_bytes=tar.extractfile(prefix+'modules/'+mid+'/index.cnxml').read();assert sha(b_bytes)==info['sha256']
        a=ET.fromstring(a_bytes);b=ET.fromstring(b_bytes)
        aa={e.get('id'):e for e in a.iter() if e.get('id')};bb={e.get('id'):e for e in b.iter() if e.get('id')}
        if mid == proposal['items'][0]['module']:
            for change in proposal['items'][0]['changes']:
                ident = change['source_id']
                assert norm(ET.fromstring(change['before_xml'])) == norm(aa[ident])
                if change['action'] == 'remove-paragraph-retain-anchor':
                    assert ident not in bb and change['after_xml'] is None
                else:
                    expected = ET.fromstring(ET.tostring(bb[ident], encoding='unicode').strip())
                    actual = ET.fromstring(change.get('upstream_xml',change['after_xml']))
                    assert ET.tostring(actual) == ET.tostring(expected), ident
                    if 'upstream_xml' in change:
                        assert change['after_xml'] == change['upstream_xml'].replace('bulb and arrive','bulb arrive').replace('</ns0:emphasis>. Note','</ns0:emphasis> Note')
        changes=[]
        for ident,e in aa.items():
            if ident in bb and local(e) in ('para','caption','title','problem','solution','meaning') and norm(e,True)!=norm(bb[ident],True):
                changes.append({'id':ident,'tag':local(e),'local':norm(e,True),'upstream':norm(bb[ident],True),'url':live(mid,sections[mid]['slug'],ident)})
        am=maths(a);bm=maths(b);common=am.keys()&bm.keys()
        math_changes=[{'key':k,'local':am[k]['rendered'],'upstream':bm[k]['rendered']} for k in sorted(common) if am[k]['tokens']!=bm[k]['tokens']]
        images=[]
        for img in a.iter(C+'image'):
            src=img.get('src');name=Path(src).name;upname=prefix+'media/'+name
            try:uphash=sha(tar.extractfile(upname).read())
            except KeyError:uphash=None
            images.append({'src':src,'local_sha256':sha((source.parent/src).read_bytes()),'upstream_sha256':uphash})
        links=[]
        for ident,e in aa.items():
            if ident not in bb:continue
            x=[dict(x.attrib) for x in e.iter(C+'link')];y=[dict(x.attrib) for x in bb[ident].iter(C+'link')]
            if x!=y and local(e) in ('para','caption','meaning'):links.append({'id':ident,'local':x,'upstream':y})
        diff=''.join(difflib.unified_diff(a_bytes.decode().splitlines(True),b_bytes.decode().splitlines(True),fromfile=sections[mid]['source'],tofile='CC-BY-upstream/'+mid+'/index.cnxml'))
        (OUT/(mid+'.diff')).write_text(diff,encoding='utf-8',newline='\n')
        rows.append({'module':mid,'title':info['title'],'local_sha256':sha(a_bytes),'upstream_sha256':sha(b_bytes),'url':live(mid,sections[mid]['slug']),
          'prose_changes_math_masked':changes,'local_only_ids':sorted(aa.keys()-bb.keys()),'upstream_only_ids':sorted(bb.keys()-aa.keys()),
          'math':{'local':len(am),'upstream':len(bm),'matched_by_owner_and_ordinal':len(common),'token_differences':math_changes,'local_unmatched':sorted(am.keys()-bm.keys()),'upstream_unmatched':sorted(bm.keys()-am.keys()),'rendered_equal':sum(am[k]['rendered']==bm[k]['rendered'] for k in common)},'images':images,'link_changes':links})
report={'target_release':'cp2e-ver1.1','status':'1.0 baseline comparison; SR01 applied for 1.1; SR02 awaiting review','upstream_commit':ref['commit'],'upstream_license':ref['license'],'scope':'All seven sections inventoried. Math token comparison is a triage aid, not proof of mathematical equivalence; nested structural changes can shift matching. Exercises inventoried but pedagogical revision deferred.','sections':rows}
(OUT/'comparison.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
esc=html.escape
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>1.1 review: Special Relativity</title><style>
body{font:18px/1.65 Georgia,serif;color:#20343c;max-width:1040px;margin:auto;padding:24px}h1,h2,h3{line-height:1.25}a{color:#12647b;overflow-wrap:anywhere}nav,.notice,aside{background:#edf4f6;padding:18px}section{margin:3rem 0;border-top:2px solid #d6e0e4;padding-top:1rem}.columns{display:grid;grid-template-columns:1fr 1fr;gap:24px}.box{border:1px solid #ccd8dc;padding:18px;min-width:0}summary{cursor:pointer;font-weight:bold}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:13px}img{max-width:100%}table{width:100%;border-collapse:collapse}td,th{text-align:left;border-bottom:1px solid #ccd8dc;padding:8px}math{max-width:100%}.math{overflow-x:auto;padding:12px}li{margin:.5rem 0}.muted{font-size:.9em;color:#50656e}@media(max-width:700px){.columns{display:block}.box{margin:1rem 0}body{padding:16px}table{font-size:14px}}
</style><h1>Special Relativity: review for 1.1</h1><p class="notice"><b>SR01 applied to the maintained 1.1 source; SR02 awaiting review.</b> The live textbook, published PDF, and frozen 1.0 release are unchanged. The inventory compares the frozen 1.0 baseline against upstream. Comparison source: OpenStax College Physics 2e, CC BY 4.0, February 4, 2026.</p><nav><a href="#SR01">SR01 · Simultaneity</a> · <a href="#SR02">SR02 · Earth is not a star</a> · <a href="#followup">Further review</a> · <a href="#inventory">Seven-section inventory</a></nav>'''
item=proposal['items'][0];mid=item['module'];assert sha((ROOT/sections[mid]['source']).read_bytes())==item.get('after_sha256',item['source_sha256'])
page+='<section id="SR01"><h2>SR01 — Upstream-only simultaneity update</h2><p>This version incorporates the pinned upstream update with only two approved typo fixes: two paragraph replacements and removal of the intervening paragraph, whose explanation upstream folded into the first replacement. The introduction, thought-experiment paragraph, summary, figure caption, and image description remain unchanged.</p><p>The broader rewrite is withdrawn. The columns below show only the affected paragraphs, in their original order.</p><p><a href="'+live(mid,sections[mid]['slug'],'fs-id3155062')+'">Read the current textbook passage in context</a></p>'

def review_markup(xml):
    if xml is None:return '<p class="muted">[Paragraph removed in upstream; explanation folded into the preceding paragraph. Its existing link anchor is retained in the maintained source.]</p>'
    def render(e):
        if e.tag==M+'math':return native_math(e)[0]
        if e.tag==C+'link':return '<a href="'+live('m42531',sections['m42531']['slug'],e.get('target-id'))+'">Figure 13.3.2</a>'
        body=esc(e.text or '')+''.join(render(c)+esc(c.tail or '') for c in e)
        if e.tag==C+'para':return '<p>'+body+'</p>'
        if e.tag==C+'emphasis':return '<em>'+body+'</em>'
        return body
    return render(ET.fromstring(xml))
page+='<div class="columns"><div class="box"><h3>Current 1.0 wording</h3>'+''.join(review_markup(x['before_xml']) for x in item['changes'])+'</div><div class="box"><h3>Applied for 1.1: upstream plus two typo fixes</h3>'+''.join(review_markup(x['after_xml']) for x in item['changes'])+'</div></div>'
page+='<p class="notice"><b>Applied:</b> removed “and” from “and arrive” and the extra period after “Simultaneity is not absolute.” All other upstream wording is retained; broader prose revision is deferred.</p><p>The existing figure artwork, caption, and image description are unchanged. <a href="../../course-full/sections/simultaneity-and-time-dilation/index.html">Read the updated development section</a>.</p></section>'

item=proposal['items'][1];page+='<section id="SR02"><h2>SR02 — Earth is not a star</h2><p>In the Alpha Centauri example’s strategy paragraph, change <q>'+esc(item['before'])+'</q> to <q>'+esc(item['after'])+'</q>. This is the upstream’s small wording correction; values, equations and reasoning stay the same.</p><p><a href="'+live(item['module'],sections[item['module']]['slug'],item['source_id'])+'">Read this sentence in context</a></p></section>'
page+='''<section id="followup"><h2>Further review and differences to preserve</h2><ul>
<li><b>Special relativity and acceleration:</b> both sources contain the overstatement that special relativity applies only to unaccelerated motion. The twin-paradox explanation also suggests general relativity is needed. This is a separate conceptual issue, not a correction supplied by the pinned upstream. Flag for author-led wording review; no replacement is proposed or applied here. Background verification: <a href="https://www.einstein-online.info/en/spotlight/twinsroad/">Einstein Online’s special-relativistic explanation</a> (reference link only; no wording or artwork imported).</li>
<li><b>Preserve approved adaptation:</b> keep the Refraction link, the Impulse and Momentum chapter reference, the Nuclear and Particle Physics reference, the author-approved twin-paradox closing sentence, and M02’s proper-time notation. Do not restore upstream links to omitted sections.</li>
<li><b>MathML:</b> velocity-addition expressions include upstream changes that split combined text tokens into symbols/operators. These are potential selection/accessibility improvements, not established changes in the mathematical result. The Doppler glossary equation was moved out of an equation wrapper upstream, shifting matching ordinals; retain its canonical local anchor.</li>
<li><b>Figures:</b> 22 of 23 local image references are byte-identical upstream. The remaining Einstein portrait is the same photograph at lower resolution upstream; retain the larger local image. No artwork replacement is proposed.</li>
<li><b>Exercises:</b> the upstream adds AP test-preparation material and a rock-length problem. These are candidates for the later conceptual-exercise pilot, not automatic additions. Some existing answers are arranged differently. MyOpenMath exports are not needed yet.</li>
<li><b>Coverage limit:</b> all seven modules have machine-readable text, ID, MathML, image and link comparisons. This first report is not a complete line-by-line physics proof or exercise-quality review. Structural math changes and exercise solutions still need focused review.</li></ul></section><section id="inventory"><h2>Seven-section inventory</h2><p>Detailed differences below preserve the audit trail. [MATH] masks each expression when comparing surrounding prose; use the rendered math differences and full XML diff for equations. Parent/child entries can overlap, so counts are not numbers of independent corrections.</p><table><tr><th>Section</th><th>Prose records</th><th>Math local/upstream</th><th>Images identical</th></tr>'''
for row in rows:
    page+='<tr><td><a href="#'+row['module']+'">'+esc(row['title'])+'</a></td><td>'+str(len(row['prose_changes_math_masked']))+'</td><td>'+str(row['math']['local'])+'/'+str(row['math']['upstream'])+'</td><td>'+str(sum(i['local_sha256']==i['upstream_sha256'] for i in row['images']))+'/'+str(len(row['images']))+'</td></tr>'
page+='</table></section>'
for row in rows:
    page+='<section id="'+row['module']+'"><h2>'+esc(row['title'])+'</h2><p><a href="'+row['url']+'">Current textbook</a> · <a href="'+row['module']+'.diff">Full source XML diff</a></p><details><summary>Prose differences ('+str(len(row['prose_changes_math_masked']))+')</summary>'
    for x in row['prose_changes_math_masked']:
        page+='<h3>'+esc(x['id'])+'</h3><div class="columns"><div class="box"><b>Current</b><p>'+esc(x['local'])+'</p></div><div class="box"><b>Pinned upstream</b><p>'+esc(x['upstream'])+'</p></div></div>'
    page+='</details><details><summary>Math token differences ('+str(len(row['math']['token_differences']))+')</summary><p>Owner/ordinal matching can shift when an equation wrapper is removed. Token equality alone does not prove equal fraction, root or script structure.</p>'
    for x in row['math']['token_differences']:
        page+='<h3>'+esc(x['key'])+'</h3><div class="columns"><div class="box math">'+x['local']+'</div><div class="box math">'+x['upstream']+'</div></div>'
    page+='</details><details><summary>IDs, links and media audit</summary><pre>'+esc(json.dumps({k:row[k] for k in ('local_only_ids','upstream_only_ids','images','link_changes')},ensure_ascii=False,indent=2))+'</pre></details></section>'
page+='<footer><p>Comparison excerpts: OpenStax College Physics 2e, Rice University, CC BY 4.0, pinned commit <a href="'+ref['repository']+'/tree/'+ref['commit']+'">'+ref['commit']+'</a>. Current textbook: Introduction to Physics, CC BY 4.0; original credits retained in the published text. SR01 uses wording from the pinned upstream with two approved typo fixes; SR02 is also an upstream correction. No additional prose rewrite is proposed.</p><p><a href="comparison.json">Machine-readable comparison</a></p></footer></html>'
(OUT/'index.html').write_text(page,encoding='utf-8',newline='\n')
shutil.copyfile(ROOT/'maintained/media/Figure_29_02_02a.jpg',OUT/'train-flashes.jpg')
preview=ROOT/'prototype/dist/review-1.1/special-relativity';shutil.copytree(OUT,preview,dirs_exist_ok=True)
print(json.dumps({'sections':len(rows),'local_math':sum(x['math']['local'] for x in rows),'upstream_math':sum(x['math']['upstream'] for x in rows),'local_images':sum(len(x['images']) for x in rows),'preview':str(preview)}))
