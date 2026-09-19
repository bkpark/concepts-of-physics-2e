"""Fail release rendering when the recorded local renderer/fonts have changed."""
from pathlib import Path
import json,hashlib,subprocess,os
root=Path(__file__).resolve().parents[1]
lock=json.loads((root/'metadata/render-environment.lock.json').read_text(encoding='utf-8'))
for f in lock['files']:
 p=Path(f['path']);assert p.is_file(),f'Missing locked dependency: {p}'
 assert hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256'],f'Changed locked dependency: {p}'
assert subprocess.check_output(['node','--version'],text=True).strip()==lock['node_version']
assert subprocess.check_output(['node','-p',"require('playwright/package.json').version"],text=True).strip()==lock['playwright_version']
print('Locked renderer and font files verified.')
