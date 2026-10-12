"""Export alternate presentation labels without altering content or anchors."""
import json
import shutil

def write_toggle(out, prototype, course, legacy, objects):
    rows = {row['module']: row for row in legacy['sections']}
    sections = {label: rows[mid]['label'] for mid, label in course.items()}
    chapters = {label.split('.')[0]: rows[mid]['label'].split('.')[0]
                for mid, label in course.items() if '.' in label}
    labels = {}
    by_anchor = {}
    for (mid, ident), obj in objects.items():
        old = obj.get('label')
        if not old or mid not in rows or obj['kind'] == 'exercise':
            continue
        label_mid = obj.get('summary_original', mid+'#').split('#')[0]
        prefix = course[label_mid]
        row = rows[label_mid]
        alternate = row['label'] + ('.0' if row['kind'] == 'chapter-introduction' else '')
        if old.startswith(prefix + '.'):
            new = alternate + old[len(prefix):]
        elif '.E.' in old:
            chapter, suffix = old.split('.E.', 1)
            new = chapters[chapter] + '.E.' + suffix
        else:
            new = old
        kind = obj['kind'].title()
        key = kind + ' ' + old
        assert key not in labels or labels[key] == new, key
        labels[key] = new
        by_anchor[obj['anchor']] = dict(course=old, older=new, kind=obj['kind'])
    data = dict(sections=sections, chapters=chapters, labels=labels, objects=by_anchor,
                modules={mid:dict(course=course[mid],older=row['label']) for mid,row in rows.items()})
    (out/'numbering-data.js').write_text('window.PHYSICS_NUMBERING = '+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
    shutil.copyfile(prototype/'numbering-toggle.js',out/'numbering-toggle.js')
    # The same routes and HTML are retained in both modes. The course labels remain
    # the accessible no-JavaScript fallback and the canonical search index.
    for path in out.rglob('*.html'):
        if path.name in ('book.html','review.html') or 'review-items' in path.parts:
            continue
        html = path.read_text(encoding='utf-8')
        depth = len(path.relative_to(out).parts)-1
        prefix = '../'*depth
        scripts = f'<script src="{prefix}numbering-data.js"></script><script defer src="{prefix}numbering-toggle.js"></script>'
        html = html.replace('</head>',scripts+'</head>',1)
        path.write_text(html,encoding='utf-8')
