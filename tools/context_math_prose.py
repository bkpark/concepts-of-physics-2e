"""Add reader-facing locations and nearby prose to the MathML prose audit."""
from pathlib import Path
import copy
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'reports/1.1/math-prose-audit'
audit = json.loads((OUT/'inventory.json').read_text(encoding='utf-8'))
labels = json.loads((ROOT/'prototype/dist/course-full/object-labels.json').read_text(encoding='utf-8'))
registry = json.loads((ROOT/'prototype/dist/course-full/identity-registry.json').read_text(encoding='utf-8'))
relocations = json.loads((ROOT/'prototype/dist/course-full/chapter-end-relocations.json').read_text(encoding='utf-8'))
C = '{http://cnx.rice.edu/cnxml}'
M = '{http://www.w3.org/1998/Math/MathML}'

def readable(element):
    if element is None:
        return ''
    element = copy.deepcopy(element)
    for parent in element.iter():
        for child in list(parent):
            if child.tag == M+'annotation':
                parent.remove(child)
    return re.sub(r'\s+', ' ', ''.join(element.itertext())).strip()

cache = {}
lines = ['# MathML prose audit — reading context', '',
         'All 28 flagged expressions, in textbook order. Links target stable source anchors in the preview. Surrounding prose is quoted from the maintained source; math in excerpts is flattened, so superscripts and fractions may look compressed. No corrections are applied by this report.', '']
for number, row in enumerate(audit['expressions'], 1):
    mid = row['module']
    if mid not in cache:
        root = ET.parse(ROOT/f'maintained/modules/{mid}/index.cnxml').getroot()
        cache[mid] = (root, {c: p for p in root.iter() for c in p})
    root, parents = cache[mid]
    math = list(root.iter(M+'math'))[row['math_index']-1]
    chain = []
    cur = math
    while cur in parents:
        cur = parents[cur]
        chain.append(cur)
    block = next((e for e in chain if e.tag in {C+'para', C+'equation', C+'item', C+'entry', C+'caption', C+'meaning'}), chain[0])
    headings = []
    for e in reversed(chain):
        title = e.find(C+'title')
        if title is not None and e.tag != C+'document':
            obj = labels.get(mid+'#'+str(e.get('id')), {})
            prefix = (obj['kind'].capitalize()+' '+str(obj['label'])+': ') if obj.get('label') and obj.get('kind') in {'example','table','figure'} else ''
            headings.append(prefix+readable(title))
    obj = labels.get(mid+'#'+str(row['location']), {})
    anchor = mid+'--'+row['location'].encode().hex() if row['location'] else ''
    slug = registry[mid]['slug']
    path = 'sections/'+slug+'/'
    for relocation in relocations:
        if relocation['module']==mid and anchor in relocation['anchors']:
            path = 'exercises/'+relocation['review_slug']+'/'
            break
    url = 'https://intro-1-1.coaphys.xyz/'+path+('#'+anchor if anchor else '')
    equation = 'Equation '+str(obj['label']) if obj.get('kind')=='equation' and obj.get('label') else ''
    siblings = list(parents[block]) if block in parents else []
    index = siblings.index(block) if siblings else 0
    preceding = ''
    following = ''
    if block.tag == C+'equation':
        for e in reversed(siblings[:index]):
            if e.tag == C+'para':
                preceding = readable(e)
                break
        for e in siblings[index+1:]:
            if e.tag == C+'para':
                following = readable(e)
                break
    context = readable(block)
    row['reading_context'] = dict(url=url,headings=headings,equation=equation,paragraph=context,preceding_paragraph=preceding,following_paragraph=following)
    lines += [f"## {number}. {row['section']} — {row['title']}" + (f' — {equation}' if equation else ''), '',
              '[Open this location]('+url+')', '',
              '**Within:** '+(' → '.join(headings) if headings else 'section body'), '',
              '**Flagged expression:** `'+re.sub(r'\s+',' ',row['expression']).strip()+'`', '']
    if preceding:
        lines += ['**Lead-in:**', '', '> '+preceding, '']
    if block.tag != C+'equation':
        lines += ['**Surrounding passage:**', '', '> '+context, '']
    if following:
        lines += ['**Following paragraph:**', '', '> '+following, '']
    lines += ['Source locator: `'+mid+'#'+str(row['location'])+'`; '+row['category']+'.', '']
(OUT/'inventory.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(OUT/'context-review.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('Added context, headings, and direct links for all '+str(len(audit['expressions']))+' expressions.')
