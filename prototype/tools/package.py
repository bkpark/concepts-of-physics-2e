"""Package the already-built review samples; does not modify historical source."""
from pathlib import Path
import hashlib, json, zipfile

root=Path(__file__).resolve().parents[1]
dist=root/'dist'
(dist/'index.html').write_text('''<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Introduction to Physics - fidelity preview</title>
<link rel="stylesheet" href="cnx/style.css"></head><body><main>
<p class="eyebrow">Recovery / six-module preview</p><h1>Introduction to Physics</h1>
<p>Compare the same source under two numbering profiles:</p>
<ul><li><a href="cnx/">CNX numbering preview</a></li>
<li><a href="course/">Course numbering preview</a></li></ul>
<p>Section labels follow the reference PDFs. Object numbers are provisional.
Three malformed expressions are flagged for review. This is not a student edition.</p>
<p>Both profiles use identical section paths and anchors. The profile prefixes
are for this local comparison only.</p></main></body></html>''',encoding='utf-8',newline='\n')
out=root/'output';out.mkdir(exist_ok=True)
pdfs=sorted(out.glob('introduction-to-physics-prototype-*.pdf'))
assert len(pdfs)==2,'Render both PDFs before packaging'
manifest={'pdf_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in pdfs},
          'purpose':'six-module review prototype; not a student edition'}
(out/'artifact-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
with zipfile.ZipFile(out/'introduction-to-physics-fidelity-preview.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(dist.rglob('*')):
        if p.is_file():z.write(p,'site/'+p.relative_to(dist).as_posix())
    for p in pdfs:z.write(p,p.name)
    z.write(out/'artifact-manifest.json','artifact-manifest.json')
    z.write(root/'README.md','BUILD-README.md')
    z.write(root.parent/'docs/fidelity-prototype-report.md','ASSESSMENT.md')
print(out/'introduction-to-physics-fidelity-preview.zip')
