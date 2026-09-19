"""Check maintained corpus against initialization and the ordered approved editorial ledger."""
from pathlib import Path
import base64,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'proposals/fidelity-repairs/manifest.json').read_text(encoding='utf-8'))
expected={}
for r in manifest['repairs']:
    p=r['source_path'];original=(ROOT/p).read_bytes()
    assert hashlib.sha256(original).hexdigest()==r['source_file_sha256']
    before=expected.get(p,original);old=r['before'].encode();assert before.count(old)==1
    expected[p]=before.replace(old,r['after'].encode(),1)
applied=0
ledger=ROOT/'maintained/editorial-changes.json'
if ledger.exists():
    for path in json.loads(ledger.read_text(encoding='utf-8'))['changes']:
        change=json.loads((ROOT/path).read_text(encoding='utf-8'))
        assert change['status']=='applied-author-directed'
        rel=Path(change['source_path']).relative_to('maintained').as_posix()
        current=expected.get(rel,(ROOT/rel).read_bytes())
        assert hashlib.sha256(current).hexdigest()==change['source_sha256']
        if change.get('encoding')=='base64':
            old=base64.b64decode(change['before'],validate=True)
            new=base64.b64decode(change['after'],validate=True)
            assert current==old
            expected[rel]=new
        else:
            old=change['before'].encode('utf-8');assert current.count(old)==1
            expected[rel]=current.replace(old,change['after'].encode('utf-8'),1)
        assert hashlib.sha256(expected[rel]).hexdigest()==change['after_sha256']
        applied+=1
count=0
for folder in ('modules','media','collections'):
    original_files={p.relative_to(ROOT) for p in (ROOT/folder).rglob('*') if p.is_file()}
    maintained_files={p.relative_to(ROOT/'maintained') for p in (ROOT/'maintained'/folder).rglob('*') if p.is_file()}
    assert original_files==maintained_files,folder
    for rel in original_files:
        assert (ROOT/'maintained'/rel).read_bytes()==expected.get(rel.as_posix(),(ROOT/rel).read_bytes()),rel
        count+=1
print(f'Verified {count} maintained content files: four initialization repairs plus {applied} approved editorial change(s).')
