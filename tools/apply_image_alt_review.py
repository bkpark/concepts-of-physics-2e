"""Apply the reviewed v1.1 alt-only corrections once, preserving XML formatting."""
from pathlib import Path
import hashlib
import html
import json
import re
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
report = root / 'reports/1.1/image-alt-audit'
proposal = 'proposals/maintainer-corrections/IMAGE-ALT-REVIEW.json'
assert not (root / proposal).exists(), 'Already applied.'
inventory = json.loads((report / 'inventory.json').read_text(encoding='utf-8'))
corrections = json.loads((report / 'corrections.json').read_text(encoding='utf-8'))
mapping = json.loads((report / 'flagged-source-map.json').read_text(encoding='utf-8'))
changes = []
pending = {}
for item in mapping:
    key = str(item['index'])
    if key in corrections:
        pending.setdefault(item['module'], []).append(item)
for module, items in pending.items():
    path = root / f'maintained/modules/{module}/index.cnxml'
    before = path.read_bytes()
    source = before.decode('utf-8')
    edits = []
    for item in items:
        pattern = r'<media\b[^>]*\bid="' + re.escape(item['id']) + r'"[^>]*>'
        matches = list(re.finditer(pattern, source))
        assert len(matches) == 1, item
        match = matches[0]
        tag = match[0]
        alt = re.search(r'\balt="([^"]*)"', tag)
        assert alt, item
        old = html.unescape(alt[1])
        assert old == inventory['images'][item['index']]['alt'], (item, old)
        new = corrections[str(item['index'])]
        updated = tag[:alt.start(1)] + html.escape(new, quote=True) + tag[alt.end(1):]
        source = source[:match.start()] + updated + source[match.end():]
        edits.append({'id': item['id'], 'inventory_index': item['index'], 'before': old, 'after': new})
    after = source.encode('utf-8')
    def neutralize(data):
        return re.sub(rb'(<media\b[^>]*\balt=")[^"]*', rb'\1', data)
    assert neutralize(before) == neutralize(after), 'Unexpected non-alt change'
    assert [e.get('id') for e in ET.fromstring(before).iter()] == [e.get('id') for e in ET.fromstring(after).iter()]
    snapshot = report / 'source-before' / module / 'index.cnxml'
    snapshot.parent.mkdir(parents=True, exist_ok=True)
    snapshot.write_bytes(before)
    path.write_bytes(after)
    changes.append({'path': path.relative_to(root).as_posix(), 'before_sha256': hashlib.sha256(before).hexdigest(), 'after_sha256': hashlib.sha256(after).hexdigest(), 'edits': edits})
(root / proposal).write_text(json.dumps({'id': 'IMAGE-ALT-REVIEW', 'status': 'approved', 'description': 'Correct reviewed image descriptions; only media alt attributes change.', 'changes': changes}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
ledger = root / 'maintained/editorial-changes.json'
data = json.loads(ledger.read_text(encoding='utf-8'))
data['changes'].append(proposal)
ledger.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Updated {sum(len(c["edits"]) for c in changes)} media descriptions in {len(changes)} modules; XML, IDs, and alt-only changes verified.')
