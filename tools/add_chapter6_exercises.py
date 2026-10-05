"""Add eight approved MyOpenMath-guided rotation questions and order the chapter."""
from pathlib import Path
import hashlib,json,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
items=[
('m71593','maintaining-rotation',['364','369'],'A rigid wheel rotates about a fixed axis at constant angular velocity with negligible friction. (a) Does it need a net torque to keep rotating? (b) What would a constant nonzero net torque do? Explain.'),
('m71593','rotation-axis',['365'],'A uniform rod can rotate about an axis through its midpoint or about a parallel axis through one end. Both axes are perpendicular to the rod. For the same net torque, about which axis is it harder to angularly accelerate the rod? Explain why the same object can have different rotational inertias.'),
('m71593','angular-acceleration',['366','369'],'Equal net torques are applied to a thin hoop and a uniform solid disk with the same mass and radius. Each rotates about a fixed axis through its center, perpendicular to its plane. Which has the greater angular acceleration? Explain in terms of rotational inertia.'),
('m67046','energy-ranking',['368'],'A thin hoop, a thin spherical shell, a uniform solid disk, and a uniform solid sphere have equal masses and radii. All spin at the same angular speed about axes through their centers; the axes of the hoop and disk are perpendicular to their planes. Rank their rotational kinetic energies from greatest to least. You may use <link document="m71593" target-id="fs-id1838666"/>. Explain your ranking.'),
('m67046','energy-scaling',['367'],'An object’s angular speed doubles while its rotational inertia stays unchanged. By what factor does its rotational kinetic energy change? How does this compare with doubling the speed of an object of fixed mass moving without rotating? Explain.'),
('m71594','comet-torque',['370','356'],'A comet experiences the Sun’s gravitational force, directed toward the Sun. Neglect other forces and treat the Sun as fixed. Can the comet’s angular momentum about the Sun remain constant even though its velocity changes? Explain by considering the torque about the Sun.'),
('m71594','flipping-wheel',['488'],'A person sits initially at rest on a stool that can turn freely about a vertical axis. They hold a spinning bicycle wheel with its axle vertical, so the wheel lies in a horizontal plane. Viewed from above, the wheel spins clockwise. The person turns the wheel upside down and holds its axle vertical again, so that its spin is now counterclockwise as viewed from above. Neglect external torque about the stool’s axis. Which way do the person and stool turn, as viewed from above? Explain using conservation of angular momentum.'),
('m71595','precession-vector',['372','370'],'A spinning gyroscope precesses steadily about a vertical axis while its spin speed remains constant. Is its angular momentum constant? Explain what changes and what causes that change.')]
def nid(s):return 'ex-c6-'+s
orders={
'm71592':['fs-id1361145','fs-id1867019','fs-id3046867','fs-id3046066'],
'm71593':['fs-id1222304',nid('maintaining-rotation'),nid('rotation-axis'),'fs-id2655227','fs-id2450048',nid('angular-acceleration'),'fs-id2680047'],
'm67046':[nid('energy-scaling'),nid('energy-ranking'),'fs-id3026004','fs-id1401566','fs-id1428194','fs-id2640555'],
'm71594':['fs-id1860696',nid('comet-torque'),'fs-id2410017','fs-id2052739','fs-id3180885','fs-id3093611',nid('flipping-wheel'),'fs-id2640407','fs-id1994709','fs-id1080849','fs-id2446255','fs-id2595479','fs-id1985120','fs-id3450198'],
'm71595':['fs-id1972542','eip-746',nid('precession-vector'),'eip-idm1290875088']}
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
        raise AssertionError(mid)
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
    rid = 'EX-C6-ADD-ORDER-' + mid
    rp = Path('proposals/author-corrections')/(rid+'.json')
    assert rp.as_posix() not in ledger['changes']
    record = dict(id=rid, status='applied-maintainer-approved', target_release='cp2e-ver1.1', module=mid,
        source_path=path.relative_to(ROOT).as_posix(), source_sha256=sha(before), after_sha256=sha(after), before=before, after=after,
        additions=added, exercise_order=order, reason='Add approved eight MyOpenMath-guided questions and order all 35 by topic for maintainer review. Retain existing wording and inline Check Your Understanding.')
    (ROOT/rp).write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n', encoding='utf8')
    path.write_text(after, encoding='utf8')
    ledger['changes'].append(rp.as_posix())
ledgerpath.write_text(json.dumps(ledger, ensure_ascii=False, indent=2)+'\n', encoding='utf8')
assert len(provenance) == 8 and sum(map(len, orders.values())) == 35
report = dict(status='applied-pending-maintainer-review', chapter_exercises=35, added=8, retained=27,
    source_export_sha256=hashlib.sha256(ep.read_bytes()).hexdigest(), source_orders=orders, additions=provenance)
(ROOT/'reports/1.1/chapter6-structure/exercise-additions-and-order.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf8')
print('Added 8, retained 27, ordered 35 questions. Existing exercise content preserved.')
