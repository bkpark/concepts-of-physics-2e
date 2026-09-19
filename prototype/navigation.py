"""Website navigation from collection hierarchy; section identities never use labels."""
from html import escape


class Navigation:
    def __init__(self, sections, labels, views):
        self.labels = labels
        self.chapters = {}
        self.groups = {}
        for section in sections:
            parents = tuple(section['parents'])
            if parents:
                self.chapters.setdefault(parents, []).append(section)
            else:
                self.groups.setdefault('Preface' if section['title'] == 'Preface' else 'Appendices', []).append(section)
        self.views = {v['chapter_label']: v for v in views}
        self.by_module = {s['module_id']: key for key, members in self.chapters.items() for s in members}

    def link(self, section, prefix='', numbered=True, current=None):
        label = self.labels.get(section['module_id'], '') if numbered else ''
        title = (label + ': ' if label else '') + section['title']
        active = ' aria-current="page"' if current == section['module_id'] else ''
        return '<a' + active + ' href="' + prefix + 'sections/' + section['candidate_slug'] + '/index.html">' + escape(title) + '</a>'

    def chapter_title(self, key):
        label = self.labels.get(self.chapters[key][0]['module_id'], '').split('.')[0]
        return ('Chapter ' + label + ': ' if label else '') + key[-1]

    def contents(self, key, prefix='', current=None):
        members = self.chapters[key]
        items = ['<li>' + self.link(s, prefix, current=current) + '</li>' for s in members]
        label = self.labels.get(members[0]['module_id'], '').split('.')[0]
        view = self.views.get(label)
        if view:
            items.append('<li class="chapter-exercises"><a href="' + prefix + 'exercises/' + view['slug'] + '/index.html">Chapter exercises</a></li>')
        return '<ul class="section-links">' + ''.join(items) + '</ul>'

    def section_navigation(self, mid):
        key = self.by_module.get(mid)
        if key is None:
            return ''
        first = self.chapters[key][0]
        if first['module_id'] != mid:
            return '<p class="chapter-return"><a href="../../sections/' + first['candidate_slug'] + '/index.html">Chapter contents: ' + escape(self.chapter_title(key)) + '</a></p>'
        return '<aside class="chapter-contents" aria-label="Chapter contents"><h2>' + escape(self.chapter_title(key)) + '</h2>' + self.contents(key, '../../', mid) + '</aside>'

    def overview(self, full=False, prefix=''):
        result = ''
        for section in self.groups.get('Preface', []):
            result += '<p>' + self.link(section, prefix, numbered=False) + '</p>'
        units = {}
        for key in self.chapters:
            units.setdefault(key[0] if len(key) > 1 else 'Getting started', []).append(key)
        for unit, keys in units.items():
            result += '<section class="contents-unit"><h2>' + escape(unit) + '</h2><ul class="chapter-links">'
            for key in keys:
                first = self.chapters[key][0]
                result += '<li><a class="chapter-link" href="' + prefix + 'sections/' + first['candidate_slug'] + '/index.html">' + escape(self.chapter_title(key)) + '</a>'
                if full:
                    result += self.contents(key, prefix)
                result += '</li>'
            result += '</ul></section>'
        result += '<section class="contents-unit"><h2>Appendices</h2><ul class="section-links">'
        result += ''.join('<li>' + self.link(s, prefix) + '</li>' for s in self.groups.get('Appendices', []))
        return result + '</ul></section>'
