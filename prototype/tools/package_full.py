"""Package the course HTML review build without claiming publication readiness."""
from pathlib import Path
import json,hashlib,zipfile
root=Path(__file__).resolve().parents[1];dist=root/'dist/course-full'
manifest=json.loads((dist/'build-manifest.json').read_text(encoding='utf-8'))
assert len(manifest['modules'])==141
(root/'dist/index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Introduction to Physics</title><link rel="stylesheet" href="course-full/style.css"><main><h1>Introduction to Physics</h1><p>Course numbering is the primary publication target. These are review builds.</p><p><a href="course-full/">Open the full course-numbered book</a></p><p><a href="course-full/review.html">Unresolved source findings</a></p><p><a href="cnx/">CNX six-section compatibility preview</a></p></main></html>',encoding='utf-8',newline='\n')
out=root/'output';out.mkdir(exist_ok=True)
with zipfile.ZipFile(out/'introduction-to-physics-course-full-review.zip','w',zipfile.ZIP_DEFLATED) as z:
    hashes={}
    for p in sorted(dist.rglob('*')):
        if p.is_file():
            name='site/'+p.relative_to(dist).as_posix();z.write(p,name);hashes[name]=hashlib.sha256(p.read_bytes()).hexdigest()
    z.write(root.parent/'docs/course-full-build.md','ASSESSMENT.md')
    z.write(root.parent/'reports/course-full-findings.json','findings.json')
    z.writestr('artifact-manifest.json',json.dumps({'publication_ready':False,'file_sha256':hashes},indent=2))
print(out/'introduction-to-physics-course-full-review.zip')
