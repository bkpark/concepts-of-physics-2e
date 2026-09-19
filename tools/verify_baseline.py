"""Verify the immutable Git baseline and the unmodified phase-one source tree."""
from pathlib import Path
import hashlib
import json
import subprocess
import tarfile

ROOT = Path(__file__).resolve().parents[1]
lock = json.loads((ROOT / 'metadata/recovery-lock.json').read_text(encoding='utf-8'))
failures = []
tree = subprocess.check_output(['git', 'ls-tree', '-r', '-z', lock['snapshots'][0]['commit']], cwd=ROOT)
git_blobs = {}
for entry in tree.split(b'\0'):
    if not entry:
        continue
    info, path = entry.split(b'\t', 1)
    mode, kind, oid = info.split()
    if kind != b'blob' or mode not in (b'100644', b'100755'):
        failures.append('Unexpected baseline entry type: ' + path.decode('utf-8'))
    git_blobs[path.decode('utf-8')] = oid.decode('ascii')
if set(git_blobs) != set(lock['baseline_files_sha256']):
    failures.append('Lock file inventory differs from original Git tree')
for snapshot in lock['snapshots']:
    actual = subprocess.check_output(['git', 'rev-parse', snapshot['tag'] + '^{commit}'], cwd=ROOT, text=True).strip()
    if actual != snapshot['commit']:
        failures.append('Tag moved: ' + snapshot['tag'])
for name, expected in lock['baseline_files_sha256'].items():
    path = ROOT / name
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        failures.append('Changed/missing baseline working file: ' + name)
    if path.is_file():
        data = path.read_bytes()
        git_hash = hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()
        if git_hash != git_blobs.get(name):
            failures.append('Working bytes differ from original Git blob: ' + name)
for item in lock['external_archives']:
    path = ROOT / item['relative_path']
    if not path.exists():
        print('External archive not present here (check portable backup): ' + item['relative_path'])
    elif hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
        failures.append('Archive checksum mismatch: ' + item['relative_path'])
    elif item.get('git_commit'):
        archive_tree = subprocess.check_output(['git', 'ls-tree', '-r', '-z', item['git_commit']], cwd=ROOT)
        expected_blobs = {}
        for entry in archive_tree.split(b'\0'):
            if entry:
                info, name = entry.split(b'\t', 1)
                expected_blobs[name.decode('utf-8')] = info.split()[2].decode('ascii')
        actual_blobs = {}
        with tarfile.open(path) as archive:
            for member in archive.getmembers():
                if member.isfile():
                    data = archive.extractfile(member).read()
                    actual_blobs[member.name] = hashlib.sha1(
                        b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()
        if actual_blobs != expected_blobs:
            failures.append('Archive bytes differ from original Git tree: ' + item['relative_path'])
        else:
            print('Verified archive contents against Git tree: ' + item['relative_path'])
if failures:
    raise SystemExit('\n'.join(failures))
print(f"Verified {len(lock['baseline_files_sha256'])} unchanged source files and both pinned Git tags.")
