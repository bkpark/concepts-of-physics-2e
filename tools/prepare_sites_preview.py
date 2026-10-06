"""Prepare the complete static 1.1 reading preview for Sites or backup hosting.

Run after prototype/build.py course --all. The deployment checkout is generated,
not a second editable textbook. Existing Sites identity and Git state are retained.
"""
from pathlib import Path
import json,re,shutil,hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
source=ROOT/'prototype/dist/course-full'
target=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else ROOT.parent/'sites-preview-1.1'
target.mkdir(parents=True,exist_ok=True);out=target/'dist';out.mkdir(exist_ok=True)
manifest=json.loads((source/'build-manifest.json').read_text(encoding='utf-8'))
assert len(manifest['modules'])==141
for mid,digest in manifest['source_sha256'].items():
    assert hashlib.sha256((ROOT/f'maintained/modules/{mid}/index.cnxml').read_bytes()).hexdigest()==digest
files=[source/'index.html',source/'style.css',source/'copy-math.js',source/'search.js',source/'search-index.json']
for folder in ('sections','exercises','contents','media','search'):
    files.extend(p for p in (source/folder).rglob('*') if p.is_file())
expected=set()
for src in files:
    rel=src.relative_to(source);dest=out/rel;dest.parent.mkdir(parents=True,exist_ok=True);expected.add(dest)
    if src.suffix=='.html':
        s=src.read_text(encoding='utf-8')
        s=re.sub(r'<div class="prototype-notice">.*?</div>','<div class="prototype-notice">Version 1.1 preview — work (using Codex) in progress. <a href="https://intro.coaphys.xyz">Published version 1.0</a> · <a href="https://github.com/bkpark/concepts-of-physics-2e">Textbook source and revision history</a></div>',s,count=1,flags=re.S)
        s=s.replace(' — prototype',' — 1.1 preview').replace(' — sample',' — 1.1 preview')
        s=s.replace('<p>Historical source remains unchanged. Math source XML and issue logs are included beside the build. The other numbering profile uses exactly the same section paths and anchors.</p>','')
        s=re.sub(r'<p><a href="review.html">.*?</p>','',s,flags=re.S)
        s=s.replace('<p>Generated from the maintained sections. Section links and source-object identities remain canonical. Labels are provisional.</p>','')
        s=s.replace('<head>','<head><meta name="robots" content="noindex, nofollow"><meta name="book-release" content="cp2e-ver1.1-preview">',1)
        dest.write_text(s,encoding='utf-8',newline='\n')
    else:shutil.copyfile(src,dest)
# Only remove stale generated assets within this dedicated dist directory.
for stale in out.rglob('*'):
    if stale.is_file() and stale not in expected and stale.name not in ('robots.txt',):stale.unlink()
(out/'robots.txt').write_text('User-agent: *\nDisallow: /\n',encoding='utf-8')
hosting=target/'.openai/hosting.json';hosting.parent.mkdir(exist_ok=True)
config=json.loads(hosting.read_text(encoding='utf-8')) if hosting.exists() else {}
config['static']={'directory':'dist'}
hosting.write_text(json.dumps(config,indent=2)+'\n',encoding='utf-8')
(target/'README.md').write_text('# Introduction to Physics — 1.1 preview\n\nGenerated deployment copy of https://github.com/bkpark/concepts-of-physics-2e.\nDo not edit textbook content in this checkout. Rebuild the canonical project and run tools/prepare_sites_preview.py to update it.\n\nThis is a public work-in-progress preview, not the final 1.1 release.\n',encoding='utf-8')
receipt=dict(release='cp2e-ver1.1-preview',canonical_project=str(ROOT),source_sha256=manifest['source_sha256'],files=len(files),static_bytes=sum(p.stat().st_size for p in out.rglob('*') if p.is_file()),pending='Exercise revision, preface, final publication tasks and PDF release validation remain separate.')
(target/'build-provenance.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ('release','files','static_bytes')},indent=2))
print(target)
