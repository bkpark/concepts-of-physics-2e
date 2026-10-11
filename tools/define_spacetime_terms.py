import hashlib, json, re
from pathlib import Path
import xml.etree.ElementTree as ET
root=Path(__file__).resolve().parents[1]
p=root/'maintained/modules/m42531/index.cnxml'
before=p.read_text(encoding='utf-8')
after=before.replace(' (Original diagram for this textbook.)','').replace('world lines','worldlines').replace('world line','worldline')
after=after.replace('on a space-time diagram. In <link target-id="spacetime-world-lines"/>','on a <term id="term-space-time-diagram">space-time diagram</term>, a graph of events according to their positions and times in a chosen reference frame. In <link target-id="spacetime-world-lines"/>')
after=after.replace('<emphasis effect="italics">worldline</emphasis>','<term id="term-worldline">worldline</term>')
definitions='''<definition id="definition-space-time-diagram"><term>space-time diagram</term><meaning id="meaning-space-time-diagram">a graph representing events by their positions and times in a chosen reference frame; here, position is horizontal and time multiplied by the speed of light is vertical</meaning></definition>
<definition id="definition-worldline"><term>worldline</term><meaning id="meaning-worldline">the path through space-time traced by an object, consisting of the events specifying its position at each time</meaning></definition>
'''
assert 'id="definition-worldline"' not in before
after=after.replace('</glossary>',definitions+'</glossary>')
after=after.replace('A spacetime diagram has position','On a space-time diagram with position').replace('on the vertical axis, with the same length scale on both axes. A worldline records an object’s position at each time. Starting at the origin, sketch worldlines','on the vertical axis and the same length scale on both axes, sketch worldlines starting at the origin')
ET.fromstring(after);p.write_text(after,encoding='utf-8')
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
rid='C13-SPACETIME-GLOSSARY-EXERCISE';rp=f'proposals/author-corrections/{rid}.json'
save(root/rp,dict(id=rid,status='applied-maintainer-approved',target_release='cp2e-ver1.1',module='m42531',source_path='maintained/modules/m42531/index.cnxml',source_sha256=hashlib.sha256(before.encode()).hexdigest(),after_sha256=hashlib.sha256(after.encode()).hexdigest(),before=before,after=after,reason='Define space-time diagram and worldline in text and glossary, remove unnecessary original-art credit, and coordinate Exercise 11 wording with the new introduction.'))
p=root/'maintained/editorial-changes.json';d=json.loads(p.read_text(encoding='utf-8'));d['changes'].append(rp);save(p,d)
p=root/'reports/1.1/chapter13-structure/applied-question-set.json';d=json.loads(p.read_text(encoding='utf-8'))
def update(o):
    if isinstance(o,dict):
        if o.get('number')==11:
            o['title']='Reading a simple space-time diagram'
            o['prompt']='On a space-time diagram with position x on the horizontal axis and ct on the vertical axis and the same length scale on both axes, sketch worldlines starting at the origin for (a) an object at rest, (b) an object moving steadily to the right at 0.500c, and (c) a light pulse moving right in vacuum. Which line is vertical? Which makes a 45° angle with the horizontal axis? What feature of the diagram represents two events simultaneous in this frame?'
            o['rationale']='Applies the space-time diagram and worldline definitions introduced with the train-and-flashes figure; no Extension label or Lorentz transformation required.'
        for v in o.values():update(v)
    elif isinstance(o,list):
        for v in o:update(v)
update(d);save(p,d)
with (root/'docs/exercise-revision-1.1.md').open('a',encoding='utf-8') as f:f.write('\n\n### 2026-10-10: Space-time glossary and Exercise 11\n\nDefined space-time diagram and worldline in the running text and chapter glossary. Standardized worldline to one word in the section and Exercise 11. Removed the original-art caption note. Exercise 11 now applies the introduced terminology rather than reintroducing it; it retains the sketching and simultaneity questions without an Extension label.\n')
print('Glossary, caption, Exercise 11, and records updated.')
