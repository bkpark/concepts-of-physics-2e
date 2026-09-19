"""One-time, reviewable phase-one metadata seed. Refuses to overwrite manifests.

Run after inventory.py. Reads the pinned upstream collection and extracted PDF TOC.
These are proposals/evidence, not a publishing configuration.
"""
from pathlib import Path
from collections import Counter
import base64
import hashlib
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from inventory import BASE, NS, ROOT

META = ROOT / 'metadata'

def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))

def write(name, value):
    path = META / name
    with path.open('x', encoding='utf-8', newline='\n') as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write('\n')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def normalized(title):
    return re.sub('[^a-z0-9]', '', title.lower())

def main():
    META.mkdir(exist_ok=True)
    names = ['recovery-lock.json', 'sections.proposed.json', 'upstream-map.proposed.json',
             'numbering-course-2026-07-07.proposed.json', 'numbering-cnx.proposed.json']
    if any((META / n).exists() for n in names):
        raise SystemExit('Seed manifests already exist; edit them through reviewed changes, never reseed silently.')
    sections = read('reports/sections.json')
    files = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', BASE], cwd=ROOT, text=True).splitlines()
    archives = ['recovered-all-refs.bundle', 'introduction-cnx-import-e2b8ec0.tar', 'introduction-branch-tip-4a86614.tar']
    pdf = ROOT.parent / 'references/course-numbering-2026-07-07.pdf'
    upstream = ROOT / 'references/college-physics-2e.collection.xml'
    upstream_commit = 'fd1b25dfd5d8c6580c6e2b2b34a19e29cc69ada9'
    write('recovery-lock.json', {
        'schema_version': 1, 'book_title': 'Introduction to Physics',
        'recovered_repository': 'https://github.com/cnx-user-books/cnxbook-concepts-of-physics',
        'selected_branch': 'introduction-to-physics', 'collection_id': 'col25183',
        'collection_uuid': '58fbacb7-693d-4d0a-80dc-21e7c33abd8f',
        'legacy_identifier_user_supplied': 'WPust2k9@12.1',
        'uuid_first_six_bytes_base64url': base64.urlsafe_b64encode(bytes.fromhex('58fbacb7693d')).decode(),
        'version_12_1_status': 'user-supplied; not independently attested by recovered metadata; archive endpoint timed out',
        'snapshots': [
            {'tag': 'recovered/cnx-import-2022-06-23', 'commit': BASE, 'role': 'earliest available import of this book'},
            {'tag': 'recovered/introduction-branch-2022-09-29', 'commit': '4a8661442d4612738ff388f7f1be7c5deabd1b68',
             'role': 'branch tip; contains later MathML and attribution changes'}],
        'baseline_files_sha256': {n: sha(ROOT / n) for n in files},
        'external_archives': [{'relative_path': '../' + n, 'sha256': sha(ROOT.parent / n)} for n in archives],
        'course_numbering_reference': {
            'url': 'https://coaphys.xyz/wordpress/wp-content/uploads/2026/07/Introduction-to-Physics-Park-PHYS-10-2026-07-07.pdf',
            'local_relative_path': '../references/course-numbering-2026-07-07.pdf', 'sha256': sha(pdf), 'pages': 744,
            'role': 'User-designated course numbering authority, not replacement textbook prose'},
        'upstream_reference': {'repository': 'https://github.com/openstax/osbooks-college-physics-bundle',
            'commit': upstream_commit, 'file': 'collections/college-physics-2e.collection.xml',
            'local_path': 'references/college-physics-2e.collection.xml', 'sha256': sha(upstream),
            'license_declared': 'CC-BY-NC-SA-4.0', 'scope': 'collection only; no upstream module snapshot yet'}
    })
    write('sections.proposed.json', {'schema_version': 1, 'status': 'draft-unpublished',
        'url_policy': '/sections/{frozen-slug}/',
        'sections': [{'id': 'cnx:' + s['module_id'], 'slug': s['candidate_slug'], 'aliases': [],
                      'title': s['title'], 'source': s['source'],
                      'provenance': {'cnx_module_id': s['module_id'], 'cnx_uuid': s['uuid'], 'recovery_commit': BASE}}
                     for s in sections]})
    up = ET.parse(upstream).getroot()
    upstream_ids = {e.get('document') for e in up.findall('.//col:module', NS)}
    write('upstream-map.proposed.json', {'schema_version': 1,
        'reference_commit': upstream_commit,
        'policy': 'Candidates are not confirmed derivations or permission to merge. Empty targets mean unresolved, not no counterpart.',
        'mappings': [{'local_sections': ['cnx:' + s['module_id']],
            'upstream_sections': ([{'work': 'college-physics-2e', 'module_id': s['module_id'],
                                   'source_path': 'modules/' + s['module_id'] + '/index.cnxml'}]
                                  if s['module_id'] in upstream_ids else []),
            'status': 'candidate' if s['module_id'] in upstream_ids else 'unresolved',
            'evidence': ['Same module ID occurs in pinned upstream collection'] if s['module_id'] in upstream_ids else [],
            'local_selectors': [], 'upstream_selectors': [], 'intentional_differences': [],
            'reviewed_by': None, 'reviewed_at': None} for s in sections]})
    toc = read('references/course-toc-2026-07-07.json')
    entries, exercise_pages, appendix = [], [], []
    for page in toc:
        for line in page['text'].splitlines():
            m = re.match(r'^(\d+)\.(\d+|E):\s*(.+)$', line)
            if m:
                row = {'label': m[1] + '.' + m[2], 'title': m[3], 'pdf_toc_page': page['pdf_page']}
                (exercise_pages if m[2] == 'E' else entries).append(row)
            a = re.match(r'^Chapter (1[5-8]):\s*(.+)$', line)
            if a:
                appendix.append({'label': a[1], 'title': a[2], 'pdf_toc_page': page['pdf_page']})
    body = [s for s in sections if s['parents']]
    if len(body) != len(entries):
        raise SystemExit(f'PDF/source counts differ: {len(entries)} vs {len(body)}; manual alignment required')
    rows = []
    for s, e in zip(body, entries):
        rows.append({**e, 'section_id': 'cnx:' + s['module_id'], 'source_title': s['title'],
                     'status': 'title-match' if normalized(e['title']) == normalized(s['title']) else 'candidate-needs-title-review',
                     'evidence': 'PDF TOC order aligned with recovered collection; punctuation/case ignored for title match'})
    for s, e in zip(sections[-4:], appendix):
        rows.append({**e, 'section_id': 'cnx:' + s['module_id'], 'source_title': s['title'],
                     'status': 'title-match' if normalized(e['title']) == normalized(s['title']) else 'candidate-needs-title-review'})
    write('numbering-course-2026-07-07.proposed.json', {'schema_version': 1,
        'profile': 'course-2026-07-07', 'status': 'draft-needs-review', 'reference_sha256': sha(pdf),
        'section_labels': rows, 'front_matter': [{'section_id': 'cnx:m67030', 'label': None, 'status': 'placement-needs-review'}],
        'exercise_pages': exercise_pages,
        'exercise_page_policy': 'Proposed generated views of existing exercises; object-level PDF alignment still required',
        'object_numbering': {'status': 'unverified', 'overrides': []}})
    write('numbering-cnx.proposed.json', {'schema_version': 1, 'profile': 'cnx-recovered',
        'status': 'hierarchy-only; historical display labels not yet verified',
        'collection': 'collections/introduction-to-physics.collection.xml',
        'ordered_sections': [{'section_id': 'cnx:' + s['module_id'], 'groups': s['parents'], 'display_label': None} for s in sections],
        'object_numbering': {'status': 'unverified', 'overrides': []}})
    print('Wrote five draft/evidence manifests.')
    print('Upstream same-ID candidates:', len(upstream_ids & {s['module_id'] for s in sections}))
    print('Course section mapping statuses:', dict(Counter(x['status'] for x in rows)))
    print('Title differences:', json.dumps([x for x in rows if x['status'] != 'title-match'], ensure_ascii=True))

if __name__ == '__main__':
    main()
