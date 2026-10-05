"""Guarded, reversible application of approved P3, heat-engine and P4 review packets.

Dry run by default. Does not regenerate review packets against changed source.
"""
from pathlib import Path
import json,re,hashlib,sys,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[1]
C='http://cnx.rice.edu/cnxml'
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(s):return hashlib.sha256(s.encode('utf-8')).hexdigest()
def parse(s):return E.fromstring('<wrap xmlns="'+C+'" xmlns:m="http://www.w3.org/1998/Math/MathML" xmlns:md="http://cnx.rice.edu/mdml" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0">'+s+'</wrap>')[0]
def sig(e):return(e.tag,dict(e.attrib),re.sub(r'\s+',' ',e.text or '').strip(),[(sig(c),re.sub(r'\s+',' ',c.tail or '').strip()) for c in e])
def span(s,ident=None,selector=None):
    if selector:
        pattern=r'<((?:\w+:)?'+selector+r')\b[^>]*>'
    else:pattern=r'<([\w:-]+)\b[^>]*\sid="'+re.escape(ident)+r'"[^>]*>'
    hits=list(re.finditer(pattern,s));assert len(hits)==1,(ident,selector,len(hits))
    m=hits[0]
    if m[0].endswith('/>'):return m.start(),m.end()
    depth=1
    for t in re.finditer(r'</?'+re.escape(m[1])+r'\b[^>]*>',s[m.end():]):
        if t[0].startswith('</'):depth-=1
        elif not t[0].endswith('/>'):depth+=1
        if depth==0:return m.start(),m.end()+t.end()
    raise ValueError(ident)
ledger=load('maintained/editorial-changes.json')
assert not any('P34-' in x for x in ledger['changes']),'Already applied; use ledger for rollback, not a second application.'
p3=load('proposals/1.1/priority3-conceptual-review.json')
he=load('proposals/1.1/heat-engine-preview-patches.json')
p4=load('proposals/1.1/priority4-followup-review.json')
groups=[(x,'proposals/1.1/priority3-conceptual-review.json') for x in p3['items']]
groups += [(dict(id='HE',title='Approved heat-engine contextual revision',passages=he['patches']),'proposals/1.1/heat-engine-preview-patches.json')]
groups += [(x,'proposals/1.1/priority4-followup-review.json') for x in p4['items']]
files={};originals={};records=[];assets={};attributions=[]
for group,packet in groups:
    starts={}
    for p in group['passages']:
        mid=p['module'];path=f'maintained/modules/{mid}/index.cnxml'
        s=files.get(path,(ROOT/path).read_text(encoding='utf-8'));originals.setdefault(path,s);starts.setdefault(path,s)
        a,b=span(s,p['source_id'],p.get('source_selector'));old=s[a:b]
        assert sig(parse(old))==sig(parse(p['before_xml'])),(group['id'],mid,p['source_id'],'before mismatch')
        new=p.get('proposed_xml') or ''
        if new:
            # Promote approved preview artwork to a maintained asset directory.
            for src in re.findall(r'src="([^"]+)"',new):
                if 'proposals/1.1/assets/' in src:
                    origin=(ROOT/path).parent.joinpath(src).resolve();assert origin.is_file(),origin
                    dest=ROOT/'maintained/assets'/origin.name
                    assets[dest]=origin
                    new=new.replace(src,'../../assets/'+origin.name)
        tail=''.join(p.get('proposed_following_xml',[]))
        if p.get('operation')=='replace-and-move' or p.get('relocate_before'):
            s=s[:a]+s[b:]
            if p.get('relocate_before'):pos=span(s,p['relocate_before'])[0]
            else:
                pos=span(s,p['insert_after_id'])[1]
                end=span(s,p['insert_before_id'])[0]
                assert not s[pos:end].strip(),(mid,'move adjacency')
            s=s[:pos]+new+tail+s[pos:]
        else:s=s[:a]+new+tail+s[b:]
        E.fromstring(s);files[path]=s
        if p.get('attribution'):attributions.append(dict(module=mid,**p['attribution']))
    for p in group.get('glossary_additions',[]):
        path=f"maintained/modules/{p['module']}/index.cnxml";s=files.get(path,(ROOT/path).read_text(encoding='utf-8'))
        originals.setdefault(path,s);starts.setdefault(path,s)
        a,b=span(s,selector='glossary');closing=s.rfind('</',a,b)
        s=s[:closing]+p['proposed_xml']+s[closing:];E.fromstring(s);files[path]=s
    for path,before in starts.items():
        after=files[path];mid=Path(path).parent.name
        ids=[e.get('id') for e in E.fromstring(after).iter() if e.get('id')]
        assert len(ids)==len(set(ids)),(mid,'duplicate IDs')
        rid='P34-'+group['id']+'-'+mid
        rp='proposals/author-corrections/'+rid+'.json'
        assert not (ROOT/rp).exists()
        records.append((rp,dict(id=rid,status='applied-author-directed',target_release='cp2e-ver1.1',module=mid,source_path=path,source_sha256=sha(before),after_sha256=sha(after),before=before,after=after,reason=group.get('title',group['id']),authorization='Maintainer approved the complete P3/P4 contextual review and explicitly requested coordinated application on 2026-09-27.',sources=group.get('sources',[]),review_packet=packet)))
# Validate against the reviewed full-section XML wherever available, allowing asset relocation only.
for path,s in files.items():
    mid=Path(path).parent.name
    candidates=[ROOT/f'prototype/dist/review-1.1/{batch}/source/{mid}/index.cnxml' for batch in ('priority4-sections','priority3-sections')]
    reference=next((p for p in candidates if p.exists()),None)
    if reference==candidates[1] and any(p['module']==mid for g in p4['items'] for p in g['passages']):
        reference=None  # P3 preview predates the subsequent guarded P4 patches.
    if reference:
        expected=reference.read_text(encoding='utf-8')
        expected=re.sub(r'src="[^"]*proposals/1.1/assets/([^"/]+)"',r'src="../../assets/\1"',expected)
        assert sig(E.fromstring(s))==sig(E.fromstring(expected)),(mid,'preview mismatch')
report=dict(date='2026-09-27',modules=len(files),records=len(records),patches=sum(len(g['passages']) for g,_ in groups),assets=[p.relative_to(ROOT).as_posix() for p in assets],before_sha256={p:sha(s) for p,s in originals.items()},after_sha256={p:sha(s) for p,s in files.items()},attributions=attributions)
print(json.dumps({k:report[k] for k in ('modules','records','patches','assets')},indent=2))
if '--apply' not in sys.argv:sys.exit()
for dest,src in assets.items():dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(src.read_bytes())
for path,s in files.items():(ROOT/path).write_text(s,encoding='utf-8',newline='\n')
for rp,r in records:
    (ROOT/rp).write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');ledger['changes'].append(rp)
(ROOT/'maintained/editorial-changes.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
asset_manifest=dict(assets=[dict(path=d.relative_to(ROOT).as_posix(),source=s.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(d.read_bytes()).hexdigest()) for d,s in assets.items()])
(ROOT/'maintained/added-assets.json').write_text(json.dumps(asset_manifest,indent=2)+'\n',encoding='utf-8')
out=ROOT/'reports/1.1/priority34-application';out.mkdir(parents=True,exist_ok=True)
(out/'manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Applied approved revisions; originals preserved, full-file reversible ledger records written.')
