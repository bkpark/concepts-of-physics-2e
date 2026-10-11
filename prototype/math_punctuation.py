"""Keep prose punctuation attached to math without changing MathML payloads."""
import html
import re

MATH = '{http://www.w3.org/1998/Math/MathML}math'
# Closing punctuation only: never consume an opening bracket or a prose word.
TRAILING = re.compile(r'''^[\t\r\n \u00a0]*([.,;:!?\u2026\u2019\u201d\u00bb)\]}"']+)''')
INLINE = {'emphasis', 'span', 'link', 'term', 'foreign'}
OPENING = re.compile(r'([([{]+)[\t\r\n \u00a0]*$')


def ends_in_math(element):
    if element.tag == MATH:
        return element.get('display') != 'block'
    return (element.tag.rsplit('}', 1)[-1] in INLINE and len(element) > 0
            and not (element[-1].tail or '').strip()
            and ends_in_math(element[-1]))


def math_only(element):
    if element.tag == MATH:
        return element.get('display') != 'block'
    return (element.tag.rsplit('}', 1)[-1] in INLINE
            and not (element.text or '').strip()
            and len(element) == 1
            and not (element[0].tail or '').strip()
            and math_only(element[0]))


def render_content(element, render):
    """Group opening brackets from prose with the following inline expression."""
    children = list(element)
    prefix = element.text or ''
    leading = ''
    if children and math_only(children[0]):
        match = OPENING.search(prefix)
        if match:
            leading, prefix = match[1], prefix[:match.start()]
    output = [html.escape(prefix, quote=True)]
    for index, child in enumerate(children):
        tail = child.tail or ''
        next_leading = ''
        if index + 1 < len(children) and math_only(children[index + 1]):
            match = OPENING.search(tail)
            if match:
                next_leading, tail = match[1], tail[:match.start()]
        output.append(render_child(child, render, leading=leading, tail_override=tail))
        leading = next_leading
    return ''.join(output)


def render_child(element, render, leading='', tail_override=None):
    """Render a child and its tail, keeping adjacent closing punctuation together."""
    body = render(element)
    tail = (element.tail or '') if tail_override is None else tail_override
    match = TRAILING.match(tail) if ends_in_math(element) else None
    if leading and math_only(element):
        punctuation = html.escape(match[1], quote=True) if match else ''
        body = '<span class="math-with-punctuation">' + html.escape(leading, quote=True) + body + punctuation + '</span>'
        if match:
            tail = tail[match.end():]
        return body + html.escape(tail, quote=True)
    if match:
        punctuation = html.escape(match[1], quote=True)
        if math_only(element):
            body = '<span class="math-with-punctuation">' + body + punctuation + '</span>'
        else:
            # A long emphasized phrase may end in math. Group only its final
            # equation, placing punctuation just inside the inline styling.
            start = body.rfind('<span data-math-key=')
            end = body.find('</span>', start) + len('</span>')
            if start < 0 or end <= start:
                return body + html.escape(tail, quote=True)
            body = (body[:start] + '<span class="math-with-punctuation">'
                    + body[start:end] + punctuation + '</span>' + body[end:])
        tail = tail[match.end():]
    return body + html.escape(tail, quote=True)
