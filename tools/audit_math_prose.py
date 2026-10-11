"""Read-only scan of presentation MathML for embedded English connectors."""
from pathlib import Path
import collections
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
M = '{http://www.w3.org/1998/Math/MathML}'
CONNECTORS = re.compile(r'\b(?:and|or|where|with|when|for|if|then|thus|since|because|so|but)\b', re.I)
PROSE = re.compile(r'\b(?:at|is|are|to|from|of|the|an)\b', re.I)
labels = {x['section_id'].split(':')[1]: x for x in json.loads((ROOT/'metadata/numbering-course-2026-07-07.proposed.json').read_text(encoding='utf-8'))['section_labels']}
rows = []
count = 0
modules = 0
for p in sorted((ROOT/'maintained/modules').glob('*/index.cnxml')):
    modules += 1
    root = ET.parse(p).getroot()
    parents = {child: parent for parent in root.iter() for child in parent}
    mid = p.parent.name
    label = labels.get(mid, {})
    for index, math in enumerate(root.iter(M+'math'), 1):
        count += 1
        # Ignore annotations: obsolete StarMath is not the displayed expression.
        tokens = [e.text or '' for e in math.iter() if e.tag in {M+'mtext', M+'mn', M+'mi', M+'mo'}]
        hits = [t for t in tokens if CONNECTORS.search(t) or PROSE.search(t)]
        # At is the chemical symbol for astatine, not an English preposition.
        hits = [t for t in hits if t.strip() != 'At']
        if not hits:
            continue
        chain = []
        cur = math
        while cur in parents:
            cur = parents[cur]
            chain.append(cur)
        location = next((e for e in chain if e.get('id')), None)
        display = math.get('display') == 'block' or any(e.tag.endswith('}equation') for e in chain)
        connectors = any(CONNECTORS.search(t) for t in hits)
        candidate = not display and (connectors or any('(the' in t for t in hits))
        category = 'inline-split-candidate' if candidate else 'display-connector-review' if display and connectors else 'descriptive-label-review'
        rows.append(dict(section=label.get('label', mid),title=label.get('title',mid),module=mid,math_index=index,location=location.get('id') if location is not None else None,display=display,category=category,tokens=hits,expression=''.join(tokens),mathml=ET.tostring(math,encoding='unicode')))
rows.sort(key=lambda r: (tuple(int(n) for n in r['section'].split('.')) if r['section'][0].isdigit() else (999,),r['math_index']))
out = ROOT/'reports/1.1/math-prose-audit'
out.mkdir(exist_ok=True)
summary = dict(modules=modules,expressions=count,flagged=len(rows),categories=dict(collections.Counter(r['category'] for r in rows)))
report = dict(summary=summary,scope='Presentation MathML across all maintained modules, including summaries, exercises, and appendices; annotations excluded. Whole-word heuristic scan, not a proof that all embedded prose has been found. Mathematical token order in snippets is flattened, not copy-ready notation.',changes='No source expressions changed by this audit.',expressions=rows)
(out/'inventory.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lines=['# Embedded prose in MathML — global scan','',f"Scanned {count} expressions across {modules} modules. Found {len(rows)} flags. No source changes applied.",'','Presentation text only; legacy annotations excluded. Snippets flatten fractions and scripts and are for identification, not copying. Individual letters and the chemical symbol At are not treated as prose. The scan cannot guarantee detection of words split across separate letter tokens.','']
for category,title in [('inline-split-candidate','Inline expressions likely worth splitting'),('display-connector-review','Displayed connectors requiring layout judgment'),('descriptive-label-review','Descriptive labels: not automatically errors')]:
    lines += ['## '+title,'']
    for r in rows:
        if r['category'] != category: continue
        lines += [f"- **{r['section']} — {r['title']}**; `{r['location']}`; `{r['module']}-math-{r['math_index']:04d}`",'  - Embedded text: '+', '.join('`'+t.strip()+'`' for t in r['tokens']), '  - Expression: `'+re.sub(r'\s+',' ',r['expression']).strip()+'`']
    lines += ['']
lines += ['## Editorial notes','','- The two isotope alternatives in Atomic Masses should preserve leading mass-number scripts when split around “or”.','- The 9.6 voltage/potential-energy identity pair occurs three times; any later layout decision should be applied consistently.','- Formula applicability labels (for example “at center of loop”), percentage labels, and conversion descriptions may legitimately remain in MathML.','- The reported 11.9 lens givens and 11.5 photon-energy parentheses were already corrected before this scan and are not counted.']
(out/'review.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps(summary))
