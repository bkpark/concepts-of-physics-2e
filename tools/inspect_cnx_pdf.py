"""Extract historical PDF evidence without rewriting the PDF or textbook source.

Requires pypdf. Default input is the preserved sibling reference PDF.
Only front matter and the last 25 pages are read; not a full fidelity comparison.
"""
from pathlib import Path
import hashlib
import json
import re
import sys
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / 'references/introduction-to-physics-12.1.pdf'
reader = PdfReader(path)
pages = [{'pdf_page': i + 1, 'text': reader.pages[i].extract_text()}
         for i in sorted(set(range(7)) | set(range(len(reader.pages) - 25, len(reader.pages))))]
records = []
current = None
for page in pages:
    if page['pdf_page'] <= len(reader.pages) - 25:
        continue
    for line in page['text'].splitlines():
        if line.startswith('Module: '):
            current = {'pdf_pages': [], 'lines': []}
            records.append(current)
        if current is not None:
            if re.match(r'^(?:\d+ Index|Index \d+|This OpenStax book is available)', line):
                continue
            if line == 'ABOUT CONNEXIONS':
                current = None
                continue
            current['lines'].append(line)
            if page['pdf_page'] not in current['pdf_pages']:
                current['pdf_pages'].append(page['pdf_page'])

parsed = []
for r in records:
    raw = '\n'.join(r['lines'])
    own = re.search(r'^URL: (https?://legacy\.cnx\.org/content/(m\d+)/([^/\s]+)/?)', raw, re.M)
    if not own:
        raise ValueError('Attribution record lacks a module URL: ' + raw[:150])
    based = re.search(r'^Based on: (.*)', raw, re.M | re.S)
    parents = re.findall(r'https?://legacy\.cnx\.org/content/(m\d+)/([^/>\s]+)', based[1]) if based else []
    def field(name):
        m = re.search(r'^' + re.escape(name) + r': (.*?)(?=\n(?:Used here as|By|URL|Copyright|License|Based on):|\Z)', raw, re.M | re.S)
        return ' '.join(m[1].split()) if m else None
    parsed.append({'module_id': own[2], 'legacy_module_version': own[3], 'url': own[1],
        'module_title': field('Module'), 'used_here_as': field('Used here as'),
        'authors': field('By'), 'copyright': field('Copyright'), 'license': field('License'),
        'based_on_text': field('Based on'),
        'direct_ancestors': [{'module_id': m, 'legacy_version': v} for m, v in parents],
        'pdf_pages': r['pdf_pages'], 'status': 'extracted-from-pdf; full visual review pending'})

source = json.loads((ROOT / 'reports/sections.json').read_text(encoding='utf-8'))
source_ids = {s['module_id'] for s in source}
pdf_ids = {r['module_id'] for r in parsed}
assert len(pdf_ids) == len(parsed), 'Duplicate attribution records'
evidence = {'schema_version': 1, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
    'bytes': path.stat().st_size, 'pages': len(reader.pages),
    'pdf_metadata': {str(k): str(v) for k, v in reader.metadata.items()},
    'user_provenance': 'User identifies this as version 12.1 downloaded before CNX shutdown.',
    'printed_collection_url': 'https://legacy.cnx.org/content/col25183/1.12',
    'printed_structure_revision_date': '2019/10/14', 'printed_pdf_generation': '2019/11/01 14:46:23',
    'scope': 'Front matter and final 25 pages extracted; title and one attribution page visually inspected; no full text/math comparison.',
    'attribution_count': len(parsed), 'source_modules_missing_from_pdf_attributions': sorted(source_ids-pdf_ids),
    'pdf_attribution_modules_absent_from_source': sorted(pdf_ids-source_ids),
    'records_with_direct_ancestors': sum(bool(r['direct_ancestors']) for r in parsed),
    'pages_extracted': pages}
for name, data in [('cnx-12.1-pdf-evidence.json', evidence),
                   ('cnx-12.1-module-attributions.json', {'schema_version': 1, 'pdf_sha256': evidence['sha256'], 'modules': parsed})]:
    (ROOT / 'references' / name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')
print(json.dumps({k: v for k, v in evidence.items() if k not in ('pages_extracted', 'pdf_metadata')}, indent=2))
