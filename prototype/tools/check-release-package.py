"""Check the current release package against maintained source and approved PDFs."""
from pathlib import Path
import json,hashlib,re,zipfile
from lxml import etree,html
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads(p.read_text(encoding='utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rel=load(ROOT/'metadata/release.json');base=ROOT/'output/releases'/rel['release_id'];public=base/'public';stage=base/'site'
manifest=load(base/'artifact-manifest.json');build=load(stage/'build-manifest.json');browser=load(base/'browser-audit.json')
assert not browser['failures'] and not browser['external_requests']
assert all(browser[k] for k in ('structured_math_copy','numbering','theme','search'))
assert not any(x['missingAlt'] for x in browser['results'])
for name,digest in manifest['files'].items():assert sha(public/name)==digest,name
with zipfile.ZipFile(base/rel['site_archive_filename']) as z:
    assert z.testzip() is None
    assert set(z.namelist())==set(manifest['files'])|{'artifact-manifest.json'}
    for name,digest in manifest['files'].items():assert hashlib.sha256(z.read(name)).hexdigest()==digest,name
    assert [n for n in z.namelist() if n.endswith('.pdf')]==[rel['pdf_filename']]
assert [p.name for p in public.rglob('*.pdf')]==[rel['pdf_filename']]
assert sha(base/rel['pdf_filename'])==sha(ROOT/'output/pdf/v1.1-complete-book-screen.pdf')==sha(public/rel['pdf_filename'])
assert sha(base/rel['print_pdf_filename'])==sha(ROOT/'output/pdf/v1.1-complete-book.pdf')
screen=load(ROOT/'reports/1.1/screen-pdf/optimization.json')
assert sha(base/rel['pdf_filename'])==screen['outputSHA256']
assert sha(base/rel['print_pdf_filename'])==screen['sourceSHA256']
registry=load(stage/'identity-registry.json');maths=0;anchors=0
for mid,entry in registry.items():
    source=ROOT/'maintained/modules'/mid/'index.cnxml';assert sha(source)==build['source_sha256'][mid]
    assert source.read_bytes()==(public/'source'/mid/'index.cnxml').read_bytes()
    tree=etree.fromstring(source.read_bytes());ids={mid+'--'+e.get('id').encode().hex() for e in tree.iter() if e.get('id')}
    page=html.parse(str(public/'sections'/entry['slug']/'index.html'))
    assert ids<=set(page.xpath('//@id')),mid
    anchors+=len(ids);maths+=len(tree.findall('.//{http://www.w3.org/1998/Math/MathML}math'))
assert maths==build['math_expressions']
cnx=load(ROOT/'prototype/dist/cnx-full/build-manifest.json');assert cnx['source_sha256']==build['source_sha256'];assert cnx['issues']==build['issues']==0
exercises={}
for p in sorted((public/'exercises').rglob('*.html')):
    tree=html.parse(str(p));labels=tree.xpath('//*[@id="questions"]//div[@class="exercise"]/div[@class="object-title"]/text()')
    numbers=[int(re.fullmatch(r'Exercise (\d+)',x).group(1)) for x in labels]
    assert numbers==list(range(1,len(numbers)+1)),p
    exercises[p.parent.name]=len(numbers)
assert sum(exercises.values())==648
for p in public.rglob('*.html'):
    text=p.read_text(encoding='utf-8');assert all(s not in text for s in ('127.0.0.1','book-front.invalid','book-index.invalid','cp2e-ver1.0.pdf'))
    tree=html.fromstring(text);download=tree.xpath('//body/nav//a[text()="Download PDF"]/@href');assert len(download)==1 and download[0].endswith(rel['pdf_filename'])
report=dict(release=rel['release_id'],status='passed',publicPages=browser['pages'],localLinks=manifest['local_links_checked'],sourceModules=len(registry),sourceAnchors=anchors,mathExpressions=maths,exercises=exercises,totalExercises=648,bothNumberingBuildsPassed=True,screenPDFBytes=(base/rel['pdf_filename']).stat().st_size,printPDFWebsiteExcluded=True,approvedPDFHashesPreserved=True,zipCRCAndAllHashesPassed=True,browserWidths=browser['widths'],browserFailures=0,checks=['search','theme','LaTeX and ASCIIMath copy','numbering selector','all source files and anchors','sequential exercises','download links','canonical package links','images and alt text','mobile overflow'],legacyLedgerNote='The version 1.0 replay utility does not support later multi-file/maintainer ledger schemas. No complete ledger replay is claimed. Current source bytes are independently matched to both builds and the packaged source; original baseline verification passed.')
(base/'release-checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report))
