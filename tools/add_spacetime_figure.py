import hashlib
import json
import shutil
from pathlib import Path
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
source = root / 'maintained/modules/m42531/index.cnxml'
before = source.read_text(encoding='utf-8')
def math(s):
    return '<m:math>' + s + '</m:math>'
x = math('<m:mi>x</m:mi>')
ct = math('<m:mi>c</m:mi><m:mi>t</m:mi>')
c = math('<m:mi>c</m:mi>')
addition = f'''<section id="spacetime-diagrams"><title>Reading a Space-Time Diagram</title>
<para id="spacetime-diagrams-intro">A space-time diagram places events on a graph according to where and when they occur. In <link target-id="spacetime-world-lines"/>, position {x} increases to the right and time increases upward. The vertical axis is labeled {ct}: multiplying time by the speed of light gives a distance, so both axes can use the same scale. Each point represents an event in one chosen reference frame.</para>
<figure id="spacetime-world-lines"><media id="spacetime-world-lines-media" alt="Space-time diagram with position x to the right and ct upward on equal scales. From the origin, a blue vertical line represents an object at rest, a dashed purple line represents an object moving right at 0.4c, and an orange line at 45 degrees represents light moving right. A horizontal dotted line connects events with the same time coordinate."><image mime-type="image/svg+xml" src="../../assets/spacetime-world-lines.svg" width="540"/></media><caption>World lines in a single reference frame. A stationary object stays at one position as time passes; a moving object changes position. Light travels one unit of distance for each unit increase in {ct}, giving its world line a 45° angle when the axis scales are equal. Points on a horizontal line represent simultaneous events in this frame. (Original diagram for this textbook.)</caption></figure>
<para id="spacetime-diagrams-reading">An object’s path on this graph is called its <emphasis effect="italics">world line</emphasis>. Constant velocity gives a straight world line. For motion to the right, a slower object has a steeper world line, closer to vertical; the diagram has time on the vertical axis, unlike the usual position-versus-time graph. The horizontal dotted line marks a shared time coordinate, not the motion of an object. Another inertial frame generally assigns different time coordinates to events at different positions, so events simultaneous in this frame need not be simultaneous in that frame.</para>
</section>
'''
marker = '<section id="fs-id1936300"><title>Time Dilation</title>'
assert before.count(marker) == 1 and 'id="spacetime-diagrams"' not in before
after = before.replace(marker, addition + marker).replace('>Extension: A spacetime diagram', '>A spacetime diagram')
# Part (c) is a list label, not the speed of light.
after = after.replace('and (<m:math xmlns:m="http://www.w3.org/1998/Math/MathML"><m:mrow><m:mi>c</m:mi></m:mrow></m:math>) a light pulse', 'and (c) a light pulse')
ET.fromstring(after)
source.write_text(after, encoding='utf-8')
asset = root / 'proposals/1.1/assets/spacetime-world-lines.svg'
shutil.copyfile(asset, root / 'maintained/assets/spacetime-world-lines.svg')
record_id = 'C13-SPACETIME-FIGURE'
record = dict(id=record_id, status='applied-maintainer-approved', target_release='cp2e-ver1.1', module='m42531', source_path=str(source.relative_to(root)).replace('\\','/'), source_sha256=hashlib.sha256(before.encode()).hexdigest(), after_sha256=hashlib.sha256(after.encode()).hexdigest(), before=before, after=after, reason='Introduce a simple space-time diagram in the textbook before time dilation, supporting Exercise 11; remove Extension label and correct part (c) typography.')
def save(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
record_path = f'proposals/author-corrections/{record_id}.json'
save(root / record_path, record)
ledger_path = root / 'maintained/editorial-changes.json'
ledger = json.loads(ledger_path.read_text(encoding='utf-8'))
ledger['changes'].append(record_path)
save(ledger_path, ledger)
assets_path = root / 'maintained/added-assets.json'
assets = json.loads(assets_path.read_text(encoding='utf-8'))
assets['assets'].append(dict(path='maintained/assets/spacetime-world-lines.svg',source='proposals/1.1/assets/spacetime-world-lines.svg',sha256=hashlib.sha256(asset.read_bytes()).hexdigest()))
save(assets_path, assets)
manifest = root / 'reports/1.1/chapter13-structure/applied-question-set.json'
data = json.loads(manifest.read_text(encoding='utf-8'))
def update(obj):
    if isinstance(obj, dict):
        if obj.get('number') == 11:
            obj['prompt'] = obj['prompt'].removeprefix('Extension: ')
            obj['rationale'] = 'Supported by the new Reading a Space-Time Diagram subsection and original figure; no Lorentz-transformation calculation required.'
            obj['review_flag'] = 'Now supported in the textbook discussion.'
        for value in obj.values(): update(value)
    elif isinstance(obj, list):
        for value in obj: update(value)
update(data)
save(manifest, data)
with (root / 'docs/exercise-revision-1.1.md').open('a',encoding='utf-8') as f:
    f.write('\n\n### 2026-10-10: Space-time diagram for Chapter 13\n\nAdded an original SVG figure and introductory subsection after simultaneity in m42531. The graph uses equal x and ct scales, rest, 0.4c motion, light, and a horizontal simultaneity line. OpenStax University Physics Volume 3 section 5.5 was consulted (https://openstax.org/books/university-physics-volume-3/pages/5-5-the-lorentz-transformation); its light-cone and transformed-axis figures exceed the scope of this introductory exercise, so no OpenStax artwork was reused. Removed Extension from Exercise 11 and restored plain-text part (c).\n')
print('Added figure, source explanation, exercise update, and editorial records.')
