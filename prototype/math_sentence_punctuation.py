"""Separate terminal prose punctuation from presentation MathML for publication.

Operate after the native adapter, before copy-format generation. Source XML stays
available unchanged. Only the outer expression's trailing edge is eligible:
fractions, scripts, radicals, fences, and nonfinal table cells are never entered.
"""
import re
import xml.etree.ElementTree as ET

M = '{http://www.w3.org/1998/Math/MathML}'
ROWS = {'math', 'mrow', 'mstyle', 'mpadded', 'mtd'}
TOKENS = {'mo', 'mi', 'mn', 'mtext'}


def local(e):
    return e.tag.rsplit('}', 1)[-1]


def meaningful(e):
    return bool(''.join(e.itertext()).strip()) or local(e) not in ROWS | {'mspace'}


def separate(xml):
    """Return (MathML, punctuation, decision), preserving mathematical marks."""
    root = ET.fromstring(xml)
    node = root
    parents = {child: parent for parent in root.iter() for child in parent}
    tables = []
    while True:
        tag = local(node)
        if tag in ROWS:
            children = [c for c in node if meaningful(c)]
            if not children:
                return xml, '', 'empty-edge'
            node = children[-1]
        elif tag == 'mtable':
            rows = list(node)
            if not rows or any(local(r) != 'mtr' for r in rows):
                return xml, '', 'table-structure'
            tables.append(node)
            node = rows[-1]
        elif tag == 'mtr':
            if not len(node) or any(local(c) != 'mtd' for c in node):
                return xml, '', 'table-structure'
            node = node[-1]
        else:
            break
    text = (node.text or '').rstrip()
    if local(node) not in TOKENS or not text or text[-1] not in '.,;:?':
        return xml, '', 'no-sentence-punctuation'
    if (text.endswith('...') and not text.endswith('....')) or text.endswith('…'):
        return xml, '', 'ellipsis'
    # A lone comma after an ellipsis is also mathematical list punctuation.
    leaves = [e for e in root.iter() if local(e) in TOKENS and (e.text or '').strip()]
    if text == '.' and len(leaves) > 1 and (leaves[-2].text or '').rstrip().endswith('.') and not ''.join(root.itertext()).rstrip().endswith('....'):
        return xml, '', 'ellipsis'
    if text == ',' and len(leaves) > 1 and (leaves[-2].text or '').rstrip().endswith(('…', '...')):
        return xml, '', 'ellipsis'
    # Do not interpret a punctuation-only mathematical expression as prose.
    if len(leaves) == 1 and text in '.,;:?':
        return xml, '', 'punctuation-only'
    if text == '?' and len(leaves) > 1 and (leaves[-2].text or '').strip() in {'=', '≈', '→'}:
        return xml, '', 'unknown-placeholder'
    punctuation = text[-1]
    remaining = text[:-1].rstrip()
    parent = parents.get(node)
    position = list(parent).index(node) if parent is not None else 0
    if remaining:
        node.text = remaining
    else:
        parents[node].remove(node)
    # With a multiline derivation, adjacent prose must share the last row's
    # baseline, rather than the table's default vertical centre.
    for table in tables:
        table.set('align', 'baseline -1')
    if tables:
        # Reserve a tiny slot at the actual end of the last line. The HTML
        # punctuation is positioned there, not after the table's widest line.
        parent.insert(position + bool(remaining), ET.Element(M+'mspace', {
            'width':'0.3em', 'data-sentence-punctuation-anchor':'true'}))
    if root.get('display') == 'block':
        root.set('display', 'inline')
        root.set('displaystyle', 'true')
    result = ET.tostring(root, encoding='unicode')
    result = re.sub(r'(<\/?)[\w]+:', r'\1', result)
    result = re.sub(r'xmlns:[\w]+=', 'xmlns=', result)
    return result, punctuation, 'sentence-punctuation'
