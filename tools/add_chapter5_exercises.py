"""Add the twenty approved MyOpenMath-guided Chapter 5 questions and topic order."""
from pathlib import Path
import hashlib
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
items = [
('m71584', 'units', ['321'], 'Which of the following can express a period, and which can express a frequency: seconds, hertz, beats per minute, and minutes per cycle? Explain how the units distinguish the two quantities.'),
('m71584', 'timing-cycle', ['322'], 'A mass oscillates vertically on a spring. One student times its motion from its highest point until it next reaches its highest point. Another times its motion from the equilibrium position until it next reaches the equilibrium position. Do both measurements give one period? Explain, including how the direction of motion matters.'),
('m71584', 'counting-cycles', ['434'], 'A pendulum completes 12 full oscillations in 24 s. (a) What is its period? (b) What is its frequency? (c) Why might timing several oscillations give a more reliable measurement of the period than timing just one?'),
('m71584', 'heartbeat', ['330'], 'A health practitioner counts 18 heartbeats in 15 s. Assuming a steady rhythm, find (a) the heart rate in beats per minute, (b) the frequency in hertz, and (c) the time between successive beats.'),
('m71585', 'amplitude-travel', ['323'], 'A mass on a spring moves between positions 4 cm above and 4 cm below equilibrium. (a) What is its amplitude? (b) Starting at its highest point, how far does it travel during one complete cycle? (c) What is its displacement over that cycle?'),
('m71585', 'speed-cycle', ['324'], 'An object undergoes simple harmonic motion. (a) Where in its motion is its speed greatest? (b) Where is its speed zero? (c) Is its acceleration zero when its speed is zero? Explain in terms of the restoring force.'),
('m71585', 'oscillator-energy', ['324'], 'A cart oscillates on a horizontal spring with negligible friction. Describe how its kinetic energy and the spring’s potential energy change as it moves (a) from a turning point to equilibrium and (b) from equilibrium to the opposite turning point. What happens to their sum?'),
('m71586', 'natural-driving', ['333'], 'A mass on a spring oscillates at 2 Hz when displaced and released. It is then driven by a repeating force whose frequency can be adjusted. (a) Distinguish the natural frequency from the driving frequency. (b) With weak damping, near what driving frequency would you expect the largest oscillations? Explain.'),
('m71587', 'ribbon-wave', ['334'], 'A ribbon is tied to one point on a stretched horizontal rope. A transverse wave travels along the rope. Does the ribbon travel along the rope with the wave? Describe its motion and explain the distinction between wave speed and the speed of the ribbon.'),
('m71587', 'space-time', ['335', '336'], 'A snapshot shows a repeating wave on a rope, while a second graph shows the displacement of one point on the rope versus time. (a) Which would you use to measure wavelength? (b) Which would you use to measure period? Explain what repeats in each case.'),
('m71587', 'one-period-distance', ['339'], 'During one period, how far does a crest of a periodic traveling wave move? Use your answer to explain the relationship between wave speed, wavelength, and period.'),
('m71588', 'pulse-sum', ['486'], 'Two pulses travel toward one another on a rope. At one instant, one pulse alone would displace a particular point 3 cm upward, and the other alone would displace it 2 cm downward. (a) What is the displacement of that point when the pulses overlap? (b) After the pulses pass through one another, do they continue traveling? Explain using the superposition principle.'),
('m71588', 'standing-motion', ['485', '341'], 'A student says, “Nothing moves in a standing wave; that is why it is called standing.” Is this correct? Explain what remains in place and describe the motion of the string at a node and at an antinode.'),
('m71588', 'standing-patterns', ['343'], 'A string fixed at both ends forms three standing-wave patterns: one loop, two equal loops, and three equal loops. Each loop lies between neighboring nodes. For the same string length and tension, (a) rank the wavelengths from longest to shortest and (b) rank the frequencies from lowest to highest. Explain.'),
('m71588', 'harmonics', ['346'], 'A guitar string has a fundamental frequency of 150 Hz. (a) What are the frequencies of its second and third harmonics? (b) How many loops would appear in the standing-wave pattern for each of these harmonics?'),
('m71588', 'tighten-string', ['340'], 'A guitarist tightens a string without changing its vibrating length. The speed of waves on the string increases. For its fundamental standing wave, what happens to (a) the wavelength and (b) the frequency? Explain why the fixed length matters.'),
('m71590', 'air-sound', ['344'], 'A loudspeaker produces sound in air. (a) What are compressions and rarefactions? (b) Do the air molecules near the speaker travel all the way to a listener’s ear? Explain how the disturbance reaches the listener.'),
('m71589', 'audible-ultrasound', ['347'], 'Using 20 Hz to 20,000 Hz as the approximate human audible range, classify sounds with frequencies of 10 Hz, 1,000 Hz, and 40,000 Hz as infrasound, audible sound, or ultrasound. If all three travel through the same air, which has the shortest wavelength? Explain.'),
('m71589', 'lightning-distance', ['349'], 'You see a flash of lightning and hear the thunder 3.0 s later. Taking the speed of sound as 340 m/s, estimate how far away the lightning struck. Explain why the light’s travel time can be neglected in this estimate.'),
('m67819', 'mach-number', ['350'], 'An aircraft travels at 680 m/s where the local speed of sound is 340 m/s. (a) What is its Mach number? (b) Is it subsonic or supersonic? (c) Does a given Mach number always correspond to the same speed in meters per second? Explain.'),
]
def nid(name): return 'ex-c5-' + name
orders = {
'm71584': ['eip-452', nid('units'), 'eip-668', nid('timing-cycle'), nid('counting-cycles'), nid('heartbeat')],
'm71585': ['fs-id2017072', nid('amplitude-travel'), nid('speed-cycle'), 'fs-id1561901', 'fs-id2032223', 'fs-id1888472', 'fs-id3306170', 'fs-id3449442', nid('oscillator-energy')],
'm71586': [nid('natural-driving'), 'fs-id2424262', 'eip-846'],
'm71587': ['fs-id1931421', nid('ribbon-wave'), nid('space-time'), 'fs-id2639388', nid('one-period-distance'), 'eip-890'],
'm71588': [nid('pulse-sum'), 'fs-id2032212', 'eip-idm1116685344', nid('standing-motion'), 'eip-idm357263456', nid('standing-patterns'), nid('harmonics'), nid('tighten-string'), 'eip-idm358254704'],
'm71590': [nid('air-sound')],
'm71589': ['fs-id1375143', nid('lightning-distance'), 'fs-id3008692', nid('audible-ultrasound'), 'eip-idm305945248'],
'm67819': ['fs-id1562301', nid('mach-number'), 'fs-id3415376', 'fs-id1272247'],
}
ep = ROOT.parent / 'reference-inputs/phys-10-full-export-2026-09-27.imas'
export = json.loads(ep.read_text(encoding='utf8'))
crosswalk = json.loads((ROOT/'reports/1.1/exercise-crosswalk/crosswalk.json').read_text(encoding='utf8'))
refs = {q['export_question_set_id']: q for q in crosswalk['questions']}
ledgerpath = ROOT/'maintained/editorial-changes.json'
ledger = json.loads(ledgerpath.read_text(encoding='utf8'))
sha = lambda text: hashlib.sha256(text.encode()).hexdigest()
provenance = []
for mid, order in orders.items():
    path = ROOT/f'maintained/modules/{mid}/index.cnxml'
    before = path.read_text(encoding='utf8')
    working = before
    group = re.search(r'<section\b[^>]*class="conceptual-questions"[^>]*>.*?</section>', working, re.S)
    if group is None:
        assert mid == 'm71590'
        working = working.replace('</content>', '<section id="c5-sound-questions" class="conceptual-questions"><title>Questions and Exercises</title></section>\n</content>')
        group = re.search(r'<section\b[^>]*class="conceptual-questions"[^>]*>.*?</section>', working, re.S)
    block = group[0]
    added = []
    for mod, name, sourceids, wording in items:
        if mod != mid: continue
        eid = nid(name)
        assert eid not in before
        sources = []
        for key in sourceids:
            q = export['questionset'][key]
            sources.append(dict(export_question_set_id=key, source_uniqueid=str(q['uniqueid']), description=q['description'],
                assessments=[export['items'][a]['data']['name'] for a in refs[key]['assessment_ids']],
                author=q['author'], export_license_code=q['license'], upstream_attribution=q.get('otherattribution')))
        info = dict(id=eid, module=mid, wording=wording, sources=sources,
            adaptation='Fixed conceptual or short-calculation question; source controls and answer keys are not published.')
        added.append(info)
        provenance.append(info)
        block = block.replace('</section>', f'<exercise id="{eid}" type="conceptual-questions"><problem id="{eid}-problem"><para id="{eid}-p1">{wording}</para></problem></exercise>\n</section>')
    hits = list(re.finditer(r'<exercise\b[^>]*id="([^"]+)"[^>]*>.*?</exercise>', block, re.S))
    parts = {hit[1]: hit[0] for hit in hits}
    assert set(parts) == set(order), (mid, set(parts)^set(order))
    block = block[:hits[0].start()] + '\n'.join(parts[e] for e in order) + block[hits[-1].end():]
    after = working[:group.start()] + block + working[group.end():]
    ET.fromstring(after)
    for old in re.findall(r'<exercise\b.*?</exercise>', before, re.S): assert old in after
    rid = 'EX-C5-ADD-ORDER-' + mid
    rp = Path('proposals/author-corrections')/(rid+'.json')
    assert rp.as_posix() not in ledger['changes']
    record = dict(id=rid, status='applied-maintainer-approved', target_release='cp2e-ver1.1', module=mid,
        source_path=path.relative_to(ROOT).as_posix(), source_sha256=sha(before), after_sha256=sha(after), before=before, after=after,
        additions=added, exercise_order=order, reason='Add approved twenty MyOpenMath-guided questions and order all 43 by topic for maintainer review. Retain existing wording and inline Check Your Understanding.')
    (ROOT/rp).write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n', encoding='utf8')
    path.write_text(after, encoding='utf8')
    ledger['changes'].append(rp.as_posix())
ledgerpath.write_text(json.dumps(ledger, ensure_ascii=False, indent=2)+'\n', encoding='utf8')
assert len(provenance) == 20 and sum(map(len, orders.values())) == 43
report = dict(status='applied-pending-maintainer-review', chapter_exercises=43, added=20, retained=23,
    source_export_sha256=hashlib.sha256(ep.read_bytes()).hexdigest(), source_orders=orders, additions=provenance)
(ROOT/'reports/1.1/chapter5-structure/exercise-additions-and-order.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf8')
print('Added 20, retained 23, ordered 43 questions. Existing exercise content preserved.')
