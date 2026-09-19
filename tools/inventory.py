"""Read-only CNXML audit; writes derived evidence only under reports/.

Run with Python 3.12+: python tools/inventory.py
No network, external entities, content rewriting, or third-party dependencies.
"""
from pathlib import Path
from collections import Counter, defaultdict
import hashlib
import json
import posixpath
import re
import subprocess
import unicodedata
import urllib.parse
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'reports'
NS = {'c': 'http://cnx.rice.edu/cnxml', 'col': 'http://cnx.rice.edu/collxml',
      'md': 'http://cnx.rice.edu/mdml', 'm': 'http://www.w3.org/1998/Math/MathML'}
BASE = 'e2b8ec04bd22d78da0e97826b9705a3f0cc6eba5'

def local(tag):
    return tag.rsplit('}', 1)[-1]

def txt(el):
    return '' if el is None else ''.join(el.itertext()).strip()

def slug(title):
    value = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', value).strip('-')

def dump(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def main():
    OUT.mkdir(exist_ok=True)
    collection = ET.parse(ROOT / 'collections/introduction-to-physics.collection.xml').getroot()
    occurrences = []
    groups = []
    def walk(node, parents):
        for e in node:
            if local(e.tag) == 'module':
                occurrences.append({'module_id': e.get('document'), 'parents': parents})
            elif local(e.tag) == 'subcollection':
                title = txt(e.find('md:title', NS))
                groups.append({'title': title, 'parents': parents})
                walk(e.find('col:content', NS), parents + [title])
    walk(collection.find('col:content', NS), [])
    selected = {o['module_id'] for o in occurrences}
    roots, errors, modules = {}, [], {}
    for f in sorted((ROOT / 'modules').glob('*/index.cnxml')):
        try:
            r = ET.parse(f).getroot()
        except ET.ParseError as ex:
            errors.append({'file': f.relative_to(ROOT).as_posix(), 'error': str(ex)})
            continue
        mid = f.parent.name
        roots[mid] = r
        modules[mid] = {'module_id': mid, 'title': txt(r.find('c:title', NS)),
                        'uuid': txt(r.find('c:metadata/md:uuid', NS)),
                        'source': f.relative_to(ROOT).as_posix(),
                        'metadata': [{'element': local(e.tag), 'attributes': e.attrib, 'text': txt(e)}
                                     for e in r.find('c:metadata', NS)],
                        'sha256': hashlib.sha256(f.read_bytes()).hexdigest()}
    counts, math_tags, attrs, metadata_tags = Counter(), Counter(), defaultdict(Counter), Counter()
    refs, assets, duplicates, missing_ids, math_arity, media_no_alt = [], [], [], [], [], []
    content_math = []
    ids = {mid: Counter(e.get('id') for e in r.iter() if e.get('id')) for mid, r in roots.items()}
    for mid in sorted(selected & roots.keys()):
        r = roots[mid]
        for ordinal, math in enumerate(r.findall('.//m:math', NS), 1):
            if any(local(e.tag) in ('apply', 'ci', 'cn', 'csymbol') for e in math.iter()):
                content_math.append({'module': mid, 'math_ordinal_for_audit_only': ordinal,
                                     'has_apply': math.find('.//m:apply', NS) is not None})
        for ident, count in ids[mid].items():
            if count > 1:
                duplicates.append({'module': mid, 'id': ident, 'count': count})
        for e in r.iter():
            name = local(e.tag)
            if e.tag.startswith('{' + NS['m'] + '}'):
                math_tags[name] += 1
                arity = {'msub': 2, 'msup': 2, 'mfrac': 2, 'mroot': 2, 'mover': 2,
                         'munder': 2, 'msubsup': 3, 'munderover': 3}.get(name)
                if arity and len(e) != arity:
                    math_arity.append({'module': mid, 'element': name, 'expected': arity,
                                       'actual': len(e), 'xml': ET.tostring(e, encoding='unicode')})
            elif e.tag.startswith('{' + NS['c'] + '}'):
                counts[name] += 1
            elif e.tag.startswith('{' + NS['md'] + '}'):
                metadata_tags[name] += 1
            for k, v in e.attrib.items():
                if k in ('class', 'type', 'number', 'number-style', 'display', 'effect'):
                    attrs[name + '@' + k][v] += 1
            if name in ('figure', 'subfigure', 'example', 'equation', 'exercise', 'note', 'table') and not e.get('id'):
                missing_ids.append({'module': mid, 'element': name})
            if name == 'media' and not e.get('alt', '').strip():
                media_no_alt.append({'module': mid, 'id': e.get('id')})
            if any(k in e.attrib for k in ('target-id', 'document', 'url')) and name != 'license':
                doc = e.get('document', mid)
                target = e.get('target-id')
                url = e.get('url')
                if url:
                    status = 'url-not-checked'
                elif doc not in roots:
                    status = 'module-absent'
                elif target and target not in ids[doc]:
                    status = 'target-absent'
                elif doc not in selected:
                    status = 'module-outside-book'
                else:
                    status = 'resolved'
                refs.append({'module': mid, 'element': name, 'attributes': e.attrib,
                             'label': txt(e), 'status': status})
            if 'src' in e.attrib:
                src = e.get('src')
                parts = urllib.parse.urlsplit(src)
                if parts.scheme or parts.netloc:
                    status, path = 'external', None
                else:
                    lexical_path = posixpath.normpath(posixpath.join(
                        posixpath.dirname(modules[mid]['source']), urllib.parse.unquote(parts.path)))
                    p = ROOT / lexical_path
                    p = p.resolve()
                    path = p.relative_to(ROOT).as_posix() if p.is_relative_to(ROOT) else str(p)
                    status = 'present' if p.is_file() else 'missing'
                    if status == 'present' and lexical_path not in tracked_paths:
                        status = 'case-mismatch'
                assets.append({'module': mid, 'element': name, 'attributes': e.attrib,
                               'path': path, 'status': status})
    slug_groups = defaultdict(list)
    title_groups = defaultdict(list)
    for o in occurrences:
        m = modules.get(o['module_id'], {})
        o.update({k: m.get(k) for k in ('title', 'uuid', 'source')})
        o['candidate_slug'] = slug(o['title'] or o['module_id'])
        slug_groups[o['candidate_slug']].append(o['module_id'])
        title_groups[o['title']].append(o['module_id'])
    media = sorted((ROOT / 'media').rglob('*'))
    media = [f for f in media if f.is_file()]
    referenced = {a['path'] for a in assets if a['path']}
    summary = {
        'baseline_commit': BASE,
        'collection_metadata': [{'element': local(e.tag), 'text': txt(e), 'attributes': e.attrib}
                                for e in collection.find('col:metadata', NS)],
        'module_files': len(modules), 'module_occurrences': len(occurrences), 'unique_book_modules': len(selected),
        'missing_book_modules': sorted(selected - roots.keys()), 'unused_modules': sorted(roots.keys() - selected),
        'xml_parse_errors': errors, 'groups': groups,
        'duplicate_titles': {k: v for k, v in title_groups.items() if len(v) > 1},
        'slug_collisions': {k: v for k, v in slug_groups.items() if len(v) > 1},
        'cnxml_elements': dict(counts), 'mathml_elements': dict(math_tags),
        'classification_attributes': {k: dict(v) for k, v in attrs.items()},
        'metadata_elements': dict(metadata_tags), 'duplicate_ids': duplicates,
        'objects_without_ids': missing_ids, 'media_without_alt': media_no_alt,
        'fixed_arity_mathml_findings': len(math_arity),
        'math_with_content_elements': len(content_math),
        'modules_with_content_math': len({x['module'] for x in content_math}),
        'references_by_status': dict(Counter(x['status'] for x in refs)),
        'asset_references_by_status': dict(Counter(x['status'] for x in assets)),
        'media_files': len(media), 'media_bytes': sum(f.stat().st_size for f in media),
        'media_extensions': dict(Counter(f.suffix.lower() for f in media)),
        'unreferenced_media': [f.relative_to(ROOT).as_posix() for f in media if f.relative_to(ROOT).as_posix() not in referenced],
    }
    dump('inventory.json', summary)
    dump('sections.json', occurrences)
    dump('modules.json', modules)
    dump('references.json', refs)
    dump('assets.json', assets)
    dump('mathml-findings.json', math_arity)
    dump('content-mathml.json', content_math)
    print(json.dumps({k: summary[k] for k in ('module_files', 'module_occurrences', 'unique_book_modules',
        'missing_book_modules', 'xml_parse_errors', 'duplicate_titles', 'slug_collisions', 'media_files',
        'fixed_arity_mathml_findings', 'references_by_status', 'asset_references_by_status')}, indent=2))

if __name__ == '__main__':
    tracked_paths = set(subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', BASE], cwd=ROOT, text=True).splitlines())
    main()
