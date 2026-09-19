"""One-time, non-overwriting creation of the maintained CNXML source layer."""
from pathlib import Path
import hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'maintained'
if OUT.exists():raise SystemExit('maintained/ already exists; edit it through Git, never re-bootstrap it.')
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf-8'))
lock=load('metadata/recovery-lock.json')
repairs=load('proposals/fidelity-repairs/manifest.json')['repairs']
sha=lambda b:hashlib.sha256(b).hexdigest()
for path,digest in lock['baseline_files_sha256'].items():
    assert sha((ROOT/path).read_bytes())==digest,path
for directory in ('modules','media','collections'):shutil.copytree(ROOT/directory,OUT/directory)
applied=[]
for repair in repairs:
    historical=(ROOT/repair['source_path']).read_bytes()
    assert sha(historical)==repair['source_file_sha256']
    path=OUT/repair['source_path'];before=path.read_bytes()
    old=repair['before'].encode();new=repair['after'].encode()
    assert before.count(old)==1,repair['id']
    after=before.replace(old,new,1);path.write_bytes(after)
    applied.append({'id':repair['id'],'module':repair['module'],'source_object':repair['source_object'],
      'classification':repair['classification'],'reason':repair['reason'],
      'decision':'approved by author in conversation: Corrections as made look good.',
      'maintained_path':str(path.relative_to(ROOT)).replace('\\','/'),
      'before_sha256':sha(before),'after_sha256':sha(after)})
sections=load('metadata/sections.proposed.json')
sections['status']='maintained; frozen identities, not yet published'
for section in sections['sections']:section['source']='maintained/'+section['source']
(OUT/'sections.json').write_text(json.dumps(sections,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
ledger={'schema_version':1,'book_title':'Introduction to Physics',
 'baseline_commit':lock['snapshots'][0]['commit'],
 'policy':'Edit maintained/ only. Historical modules/, media/, collections/ remain immutable. This initialization ledger records the approved starting changes; later edits belong in Git history.',
 'approved_repairs':applied,'upstream_errata':[{'repair_id':'R3','url':'https://openstax.org/errata/30172','status':'submitted by author; reported in conversation; OpenStax disposition not verified'}]}
(OUT/'initialization.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print('Created maintained source, media, collection, identities; applied R1-R4 only.')
