"""Recovery-stage check: maintained corpus differs only by the four approved repairs."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'proposals/fidelity-repairs/manifest.json').read_text(encoding='utf-8'))
expected={}
for r in manifest['repairs']:
    p=r['source_path'];original=(ROOT/p).read_bytes()
    assert hashlib.sha256(original).hexdigest()==r['source_file_sha256']
    before=expected.get(p,original);old=r['before'].encode();assert before.count(old)==1
    expected[p]=before.replace(old,r['after'].encode(),1)
count=0
for folder in ('modules','media','collections'):
    original_files={p.relative_to(ROOT) for p in (ROOT/folder).rglob('*') if p.is_file()}
    maintained_files={p.relative_to(ROOT/'maintained') for p in (ROOT/'maintained'/folder).rglob('*') if p.is_file()}
    assert original_files==maintained_files,folder
    for rel in original_files:
        assert (ROOT/'maintained'/rel).read_bytes()==expected.get(rel.as_posix(),(ROOT/rel).read_bytes()),rel
        count+=1
print(f'Verified {count} maintained content files: only the four approved repairs differ from baseline.')
