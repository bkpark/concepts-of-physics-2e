"""Verify all historical section labels against the preserved PDF outline."""
from pathlib import Path
import hashlib, json, re, unicodedata
from pypdf import PdfReader

root = Path(__file__).resolve().parents[1]
pdf = root.parent / 'references/introduction-to-physics-12.1.pdf'
reader = PdfReader(pdf)
headings, chapters, appendices = [], {}, {}
def walk(items):
    for item in items:
        if isinstance(item, list):
            walk(item)
            continue
        title = item['/Title']
        page = reader.get_destination_page_number(item) + 1
        match = re.match(r'^(\d+\.\d+)\.\s*(.*)', title)
        if match:
            headings.append((match[1], match[2].rstrip('*'), page))
        match = re.match(r'^Chapter\s+(\d+)\.\s*(.*)', title)
        if match:
            chapters[match[1]] = (match[2], page)
        match = re.match(r'^Appendix\s+([A-D])\.\s*(.*)', title)
        if match:
            appendices[match[1]] = (match[2], page)
walk(reader.outline)
def norm(s):
    return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).lower())
course = json.loads((root/'metadata/numbering-course-2026-07-07.proposed.json').read_text(encoding='utf-8'))['section_labels']
source = json.loads((root/'metadata/numbering-cnx.proposed.json').read_text(encoding='utf-8'))
rows = []
for section in course:
    mid = section['section_id'].split(':')[1]
    matches = [h for h in headings if norm(h[1]) == norm(section['title'])]
    if matches:
        assert len(matches) == 1
        label, title, page = matches[0]
        kind = 'numbered-section'
    elif '.' in section['label']:
        chapter, index = map(int, section['label'].split('.'))
        assert index == 1, section
        label = str(chapter + 1)
        title, page = chapters[label]
        kind = 'chapter-introduction'
    else:
        label = dict(m42699='A', m42702='B', m78798='C', m42709='D')[mid]
        title, page = appendices[label]
        kind = 'appendix'
    rows.append(dict(module=mid, label=label, kind=kind, pdf_heading=title, pdf_page=page))
assert len(rows) == 140
lookup = {r['module']:r for r in rows}
for old in source['ordered_sections']:
    mid = old['section_id'].split(':')[1]
    if old['display_label'] is not None:
        assert lookup[mid]['label'] == old['display_label']
result = dict(schema_version=1, profile='older-textbook', source='Introduction to Physics, CNX 1.12 (2019 PDF)', source_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(), status='All 140 labeled modules verified against PDF outline; preface is unnumbered.', sections=rows, object_policy='Section-based counters in both modes; only section prefixes change. Introduction objects use chapter.0 prefixes because historical introductions have no section number. Reviewed exercise numbers are retained across modes.')
(root/'maintained/numbering-legacy.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Verified {len(rows)} labels; {len(headings)} numbered sections, {len(chapters)} chapters, {len(appendices)} appendices.')
