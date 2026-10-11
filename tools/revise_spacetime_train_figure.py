import hashlib
import json
import re
import shutil
from pathlib import Path
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="670" viewBox="0 0 640 670" role="img" aria-labelledby="title desc">
<title id="title">Train and light flashes in the station frame</title>
<desc id="desc">The ct axis is centered horizontally. Observer B at the station has a vertical world line. Observer A on the train moves right along a sloping world line. Light is emitted at the same station time from lamps equally far left and right of the origin. The right flash reaches A at event 1; both flashes reach B together at event 2; the left flash reaches A at event 3.</desc>
<rect width="640" height="670" fill="white"/>
<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#253544"/></marker></defs>
<g font-family="Arial, sans-serif" font-size="22" fill="#253544">
<text x="320" y="28" text-anchor="middle" font-weight="bold">Station frame</text>
<g stroke="#e0e5e9" stroke-width="1"><path d="M140 70V430 M500 70V430 M140 250H500"/></g>
<g stroke="#253544" stroke-width="2" marker-end="url(#arrow)"><path d="M50 430H590"/><path d="M320 445V50"/></g>
<path d="M320 430V70" stroke="#2464a0" stroke-width="5"/>
<path d="M320 430L464 70" stroke="#a04291" stroke-width="4" stroke-dasharray="12 5"/>
<path d="M140 430L500 70 M500 430L140 70" stroke="#bc5b00" stroke-width="4" fill="none"/>
<text x="600" y="437" font-style="italic">x</text><text x="281" y="62" font-style="italic">ct</text>
<text x="306" y="458">0</text>
<circle cx="140" cy="430" r="6" fill="#bc5b00"/><circle cx="500" cy="430" r="6" fill="#bc5b00"/>
<text x="140" y="463" text-anchor="middle">Left lamp flashes</text><text x="500" y="463" text-anchor="middle">Right lamp flashes</text>
<text x="320" y="495" text-anchor="middle">Emitted simultaneously in the station frame</text>
<g fill="#253544" stroke="white" stroke-width="2"><circle cx="371.429" cy="301.429" r="15"/><circle cx="320" cy="250" r="15"/><circle cx="440" cy="130" r="15"/></g>
<g fill="white" text-anchor="middle" font-size="20" font-weight="bold"><text x="371.429" y="308.429">1</text><text x="320" y="257">2</text><text x="440" y="137">3</text></g>
<path d="M57 530H92" stroke="#2464a0" stroke-width="5"/><text x="106" y="537">B: station</text>
<path d="M295 530H330" stroke="#a04291" stroke-width="4" stroke-dasharray="12 5"/><text x="344" y="537">A: train moving right</text>
<path d="M57 565H92" stroke="#bc5b00" stroke-width="4"/><text x="106" y="572">Light (45°; equal axis scales)</text>
<text x="57" y="608">1  Right flash reaches A</text>
<text x="57" y="634">2  Both flashes reach B together</text>
<text x="57" y="660">3  Left flash reaches A</text>
</g></svg>'''
asset = root / 'proposals/1.1/assets/spacetime-train-flashes.svg'
asset.write_text(svg, encoding='utf-8')
ET.fromstring(svg)
shutil.copyfile(asset, root / 'maintained/assets/spacetime-train-flashes.svg')
source = root / 'maintained/modules/m42531/index.cnxml'
before = source.read_text(encoding='utf-8')
block = '''<section id="spacetime-diagrams"><title>Reading a Space-Time Diagram</title>
<para id="spacetime-diagrams-intro">We can represent the train-and-flashes experiment on a space-time diagram. In <link target-id="spacetime-world-lines"/>, position <m:math><m:mi>x</m:mi></m:math> increases to the right and time increases upward. The vertical axis is labeled <m:math><m:mi>c</m:mi><m:mi>t</m:mi></m:math>: multiplying time by the speed of light gives a distance, so both axes can use the same scale. Each point represents an event, and all coordinates in this diagram belong to the station frame. The flashes are emitted when the train observer A passes the station observer B at the origin.</para>
<figure id="spacetime-world-lines"><media id="spacetime-world-lines-media" alt="Station-frame space-time diagram centered on the vertical ct axis. B has a vertical world line at x equals zero, while A on the train moves right along a sloping world line. The left and right lamps emit flashes at equally spaced points on the horizontal x axis, at the same station time. Inward-moving light follows two 45-degree lines. The right flash meets A first at event 1. Both light lines cross B at event 2. The left flash catches A later at event 3."><image mime-type="image/svg+xml" src="../../assets/spacetime-train-flashes.svg" width="640"/></media><caption>The train-and-flashes experiment drawn in the station frame. The two emission events lie on the same horizontal line and are equally distant from B. Both flashes reach B together (event 2), but the right flash reaches A (event 1) before the left flash does (event 3). The lamps move with the train; the points on the horizontal axis mark their positions only at emission. Light paths continue through arrival events to show the separate receptions by A and B. (Original diagram for this textbook.)</caption></figure>
<para id="spacetime-diagrams-reading">An object’s path on this graph is called its <emphasis effect="italics">world line</emphasis>. B stays at one position, so his world line is vertical. A moves steadily to the right, so her world line slopes to the right as time passes. Light travels at speed <m:math><m:mi>c</m:mi></m:math>, so its world lines make 45° angles with the horizontal when the axis scales are equal. Intersections mark events at which light reaches an observer. Reading upward, we see the right flash reach A, both flashes reach B together, and finally the left flash reach A. A horizontal line joins events that are simultaneous in the station frame.</para>
<para id="spacetime-diagrams-train-interpretation">The diagram shows the different arrival times using station-frame coordinates. To understand the emission times assigned by A, return to her description of the experiment: she and the lamps are at rest relative to one another, and she is midway between the lamps. Light travels equal distances to her at the same speed in both directions, so the two travel times in her frame are equal. Because the right flash arrives first, she concludes that the right lamp emitted its flash first. Unequal arrival times alone would not establish unequal emission times; the equal distances and equal light speeds in A’s frame are essential to her conclusion.</para>
</section>'''
after, count = re.subn(r'<section id="spacetime-diagrams">.*?</section>', lambda _: block, before, flags=re.S)
assert count == 1
ET.fromstring(after)
source.write_text(after,encoding='utf-8')
def save(path,obj): path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
record_id='C13-SPACETIME-TRAIN-FLASHES'
record_path=f'proposals/author-corrections/{record_id}.json'
save(root/record_path,dict(id=record_id,status='applied-maintainer-approved',target_release='cp2e-ver1.1',module='m42531',source_path='maintained/modules/m42531/index.cnxml',source_sha256=hashlib.sha256(before.encode()).hexdigest(),after_sha256=hashlib.sha256(after.encode()).hexdigest(),before=before,after=after,reason='Replace generic world lines with the station-frame train-and-flashes example, centered ct axis, three arrival events, and an explanation of the train-frame emission-time inference.'))
p=root/'maintained/editorial-changes.json';d=json.loads(p.read_text(encoding='utf-8'));d['changes'].append(record_path);save(p,d)
p=root/'maintained/added-assets.json';d=json.loads(p.read_text(encoding='utf-8'));d['assets'].append(dict(path='maintained/assets/spacetime-train-flashes.svg',source='proposals/1.1/assets/spacetime-train-flashes.svg',sha256=hashlib.sha256(asset.read_bytes()).hexdigest()));save(p,d)
with (root/'docs/exercise-revision-1.1.md').open('a',encoding='utf-8') as f:
    f.write('\n\n### 2026-10-10: Train-and-flashes space-time diagram\n\nRevised Figure 13.3.3 to illustrate the preceding simultaneity scenario. All coordinates are in the station frame, with symmetric lamp positions at emission, a centered ct axis, station and train world lines, two inward light paths, and numbered reception events. Text explains the train observer’s emission-time inference from equal source distances and equal light speeds without transformed axes. Geometry uses x_A=0.4ct and emissions x=±180 at ct=0; reception times are 180/1.4, 180, and 180/0.6. Original artwork; no reused OpenStax image.\n')
print('Revised figure and text; XML and SVG parse successfully.')
