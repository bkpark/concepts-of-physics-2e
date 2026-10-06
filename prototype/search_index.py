"""Index only rendered reading pages, never reports or private source material."""
from html.parser import HTMLParser
import json
import re


class Passages(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.parts = {}
        self.title = []
        self.label = []

    def handle_starttag(self, tag, attrs):
        if tag in ('div', 'p', 'li', 'td', 'th', 'h1', 'h2', 'h3', 'h4', 'br'):
            self.handle_data(' ')
        attrs = dict(attrs)
        classes = attrs.get('class', '').split()
        skip = tag in ('nav', 'footer', 'script', 'style', 'annotation', 'annotation-xml') or any(c in classes for c in ('chapter-contents', 'chapter-return', 'relocated-anchor', 'moved-anchor', 'chapter-review-link'))
        frame = (tag, attrs.get('id'), skip, classes)
        self.stack.append(frame)
        if tag in ('br', 'img', 'meta', 'link', 'hr', 'input', 'source', 'wbr'):
            self.stack.pop()

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag in ('div', 'p', 'li', 'td', 'th', 'h1', 'h2', 'h3', 'h4'):
            self.handle_data(' ')
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        if not any(f[0] == 'main' for f in self.stack) or any(f[2] for f in self.stack):
            return
        if any(f[0] == 'h1' for f in self.stack):
            self.title.append(data)
        if any('eyebrow' in f[3] for f in self.stack):
            self.label.append(data)
        # Inline terms can have their own IDs; retain surrounding sentence context.
        ident = next((f[1] for f in reversed(self.stack) if f[1] and f[0] in ('div', 'section', 'article', 'li', 'figure', 'table', 'p')), None)
        if ident:
            self.parts.setdefault(ident, []).append(data)


def build_search_index(out):
    records = []
    for folder in ('sections', 'exercises'):
        for path in sorted((out/folder).glob('*/index.html')):
            parser = Passages()
            parser.feed(path.read_text(encoding='utf-8'))
            title = ''.join(parser.title).strip()
            label = ''.join(parser.label).strip()
            title = (label + ': ' if label else '') + title
            for ident, parts in parser.parts.items():
                content = re.sub(r'\s+', ' ', ''.join(parts)).strip()
                if content:
                    records.append({'title': title, 'url': path.relative_to(out).as_posix()+'#'+ident, 'text': content})
    (out/'search-index.json').write_text(json.dumps(records, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    return len(records)


SEARCH_BODY = '''<h1>Search the textbook</h1>
<form id="book-search" role="search">
<label for="search-query">Word or phrase</label>
<div class="search-controls"><input id="search-query" name="q" type="search" maxlength="200" autocomplete="off" placeholder="e.g., momentum" aria-describedby="search-help"><button type="submit">Search</button></div>
</form>
<p id="search-help">Search sections, glossary entries, and exercises. Use quotation marks for an exact phrase.</p>
<p id="search-status" role="status" aria-live="polite">Enter a word or phrase to begin.</p>
<ol id="search-results"></ol><button id="search-more" type="button" hidden>Show more results</button>
<noscript><p>Search needs JavaScript enabled in your browser. You can also browse the <a href="../contents/index.html">full contents</a>.</p></noscript>
<script defer src="../search.js"></script>'''
