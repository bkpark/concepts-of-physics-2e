"""Stable chapter entry pages; original section pages and anchors remain valid."""
import html
import json
import posixpath
import re
from urllib.parse import urlsplit, urlunsplit


def preferred_url(url, page_path, routes):
    parts = urlsplit(url)
    if parts.scheme or parts.netloc or not parts.path:
        return url
    target = posixpath.normpath(posixpath.join(posixpath.dirname(page_path), parts.path)).lstrip('/')
    if target.endswith('/index.html'):
        target = target[:-10]
    target = target.rstrip('/')
    if target not in routes:
        return url
    path = posixpath.relpath(routes[target], posixpath.dirname(page_path) or '.') + '/'
    return urlunsplit(('', '', path, parts.query, parts.fragment))


def apply_chapter_permalinks(out, registry, entries):
    routes = {}
    for entry in entries:
        mid, path = entry['module_id'], entry['path']
        if mid not in registry:
            raise ValueError('Unknown chapter introduction: ' + mid)
        if not re.fullmatch(r'chapters/[a-z][a-z0-9-]*/', path):
            raise ValueError('Invalid chapter permalink: ' + path)
        original = 'sections/' + registry[mid]['candidate_slug']
        if original in routes or path in routes.values():
            raise ValueError('Duplicate chapter permalink')
        routes[original] = path
        source = out / original / 'index.html'
        dest = out / path / 'index.html'
        dest.parent.mkdir(parents=True, exist_ok=True)
        # Both routes have the same directory depth, retaining all asset URLs.
        canonical = '../../' + original + '/index.html'
        content = source.read_text(encoding='utf-8').replace(
            '<head>', '<head><link rel="canonical" href="' + canonical + '">', 1)
        dest.write_text(content, encoding='utf-8')
    link = re.compile(r'(<a\b[^>]*\bhref=")([^"]*)(")')
    for page in out.rglob('*.html'):
        relative = page.relative_to(out).as_posix()
        source = page.read_text(encoding='utf-8')
        def replace(match):
            url = preferred_url(html.unescape(match[2]), relative, routes)
            return match[1] + html.escape(url, quote=True) + match[3]
        revised = link.sub(replace, source)
        if revised != source:
            page.write_text(revised, encoding='utf-8')
    search = out / 'search-index.json'
    records = json.loads(search.read_text(encoding='utf-8'))
    for record in records:
        record['url'] = preferred_url(record['url'], 'index.html', routes)
    search.write_text(json.dumps(records, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    return routes
