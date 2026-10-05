"""Add nine approved MyOpenMath-guided fluids questions and order the chapter."""
from pathlib import Path
import hashlib,json,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
def unit(value,p):
 n,u=value.split(' ',1)
 return '<m:math><m:mrow><m:mn>'+n+'</m:mn><m:mspace width="0.25em"/><m:msup><m:mtext>'+u+'</m:mtext><m:mn>'+str(p)+'</m:mn></m:msup></m:mrow></m:math>'
items=[
('m71613','cut-aluminum',['375','360'],'A uniform piece of aluminum is cut into two unequal pieces. How do their masses, volumes, and densities compare? Explain.'),
('m71613','water-density',['376'],'Water has a density of approximately '+unit('1 g/cm',3)+'. (a) What is the mass of '+unit('250 cm',3)+' of water? (b) Explain why expressing its density as '+unit('1000 kg/m',3)+' describes the same property.'),
('m71615','pressure-area',['377'],'The same uniform pressure acts on two surfaces, one with twice the area of the other. Compare the forces on them. Explain why equal pressure does not necessarily mean equal force.'),
('m71623','container-width',['378','377'],'Two open containers hold water to the same depth, but one is much wider. Both have flat, horizontal bottoms and are exposed to the same atmospheric pressure. Compare (a) the pressure at their bottoms and (b) the total force the water exerts on each bottom. Explain the distinction.'),
('m71624','submerged-volumes',['379','362'],'Two solid objects have equal volumes but different masses. Both are completely submerged in water without touching the container. Compare their buoyant forces. Must either buoyant force equal the object’s weight? Explain.'),
('m71624','boat-cargo',['379','362'],'Cargo is added to a floating boat, which settles lower but remains afloat. What happens to the buoyant force and the volume of water displaced? Explain.'),
('m71624','ice-density',['381'],'Ice floats in freshwater with 91.7% of its volume submerged. Taking water’s density as '+unit('1000 kg/m',3)+', determine the ice’s density. Explain how the balance between weight and buoyancy supports your calculation.'),
('m71626','narrow-pipe-energy',['380','363'],'Water flows steadily through a horizontal pipe that narrows. Neglect friction. Compare the water’s speed and pressure in the wide and narrow portions. Explain how the pressure difference is connected to the water’s gain in kinetic energy.'),
('m71626','friction-energy',['363'],'Friction in a flowing fluid converts some mechanical energy into thermal energy. Does this violate conservation of energy? Explain why the usual frictionless form of Bernoulli’s equation needs modification.')]
def nid(s):return 'ex-c7-'+s
orders={
'm71614':re.findall(r'<exercise id="([^"]+)"', (ROOT/'maintained/modules/m71614/index.cnxml').read_text(encoding='utf8')),
'm71613':[nid('cut-aluminum'),nid('water-density'),'fs-id1613737','fs-id1417224','fs-id1397150'],
'm71615':[nid('pressure-area'),'fs-id935474','fs-id1034685','fs-id3149806','fs-id2615691','fs-id2382902','fs-id1429595','fs-id2590796'],
'm71623':[nid('container-width'),'fs-id1381740','fs-id1870728','eip-29','fs-id3073220','fs-id3091727','fs-id3045581','fs-id3042305','fs-id1355852'],
'm71624':[nid('submerged-volumes'),'fs-id937576','fs-id2604080',nid('boat-cargo'),'fs-id2054662',nid('ice-density')],
'm71625':['fs-id1434712','fs-id1549295','fs-id1917833','fs-id3078884'],
'm71626':[nid('friction-energy'),nid('narrow-pipe-energy'),'fs-id1596349','fs-id2968273','fs-id1427122','fs-id1128778','fs-id1931767','fs-id2437386','fs-id3387506','fs-id2621156','fs-id3454946','fs-id2931718','eip-411','fs-id3415476']}
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
    if mid == 'm71626':
        fig = re.search(r'<figure id="import-auto-id3177713".*?</figure>', before, re.S)[0]
        hit = re.search(r'<exercise id="fs-id3387506".*?</exercise>', block, re.S)
        block = block[:hit.end()] + '\n' + fig + block[hit.end():]
    after = working[:group.start()] + block + working[group.end():]
    ET.fromstring(after)
    for old in re.findall(r'<exercise\b.*?</exercise>', before, re.S): assert old in after
    rid = 'EX-C7-ADD-ORDER-' + mid
    rp = Path('proposals/author-corrections')/(rid+'.json')
    assert rp.as_posix() not in ledger['changes']
    record = dict(id=rid, status='applied-maintainer-approved', target_release='cp2e-ver1.1', module=mid,
        source_path=path.relative_to(ROOT).as_posix(), source_sha256=sha(before), after_sha256=sha(after), before=before, after=after,
        additions=added, exercise_order=order, reason='Add approved nine MyOpenMath-guided questions and order all 50 by topic for maintainer review. Retain existing wording and inline Check Your Understanding.')
    (ROOT/rp).write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n', encoding='utf8')
    path.write_text(after, encoding='utf8')
    ledger['changes'].append(rp.as_posix())
ledgerpath.write_text(json.dumps(ledger, ensure_ascii=False, indent=2)+'\n', encoding='utf8')
assert len(provenance) == 9 and sum(map(len, orders.values())) == 50
report = dict(status='applied-pending-maintainer-review', chapter_exercises=50, added=9, retained=41,
    source_export_sha256=hashlib.sha256(ep.read_bytes()).hexdigest(), source_orders=orders, additions=provenance)
(ROOT/'reports/1.1/chapter7-structure/exercise-additions-and-order.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf8')
print('Added 9, retained 41, ordered 50 questions. Existing exercise content preserved.')
