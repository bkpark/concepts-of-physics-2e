"""Apply approved six MyOpenMath-guided additions and Chapter 2 topic ordering."""
from pathlib import Path
import json, re, hashlib, xml.etree.ElementTree as E
ROOT = Path(__file__).resolve().parents[1]
C = '{http://cnx.rice.edu/cnxml}'
suffix = ' (updated to LibreTexts version)'
items = [
 ('m78923', 'ex-identifying-forces', [
  'Which of the following describe a force: Earth, the pull of a stretched spring, a ball moving upward, the push of a bat on a ball, and a car’s acceleration? For each force, identify the object exerting it and the object experiencing it.'
 ], 'Force Concept - Categorization - Q1'),
 ('m67044', 'ex-spring-proportionality', [
  'A spring stretches 2 cm when pulled with a force of 3 N. How far would it stretch under a force of 6 N, assuming it obeys Hooke’s law? Explain your reasoning.'
 ], 'Spring Force - Calculation - Q1'),
 ('m67044', 'ex-spring-equilibrium-release', [
  'An object hangs at rest from a spring. How does the spring force compare with the object’s weight? If you pull the object farther downward and release it, which force has changed, and in which direction does the object initially accelerate?'
 ], 'Spring Force - Calculation - Q2'),
 ('m71409', 'ex-tommy-box-friction', [
  'A box of mass 40 kg rests on a horizontal wooden floor. Tommy tries to push it horizontally.',
  '(a) Tommy pushes with a force of 20 N, but the box does not move. What is the net force on the box? What are the magnitude and direction of the friction force?',
  '(b) After getting the box moving, Tommy pushes with a force of 80 N, and it slides at a constant speed. What is the magnitude of the friction force?',
  '(c) Tommy stops pushing while the box is still sliding on the wooden floor. What are the magnitude and direction of its acceleration?',
  '(d) Still sliding without Tommy’s push, the box reaches a horizontal marble floor and slows down at 0.5 m/s². What is the magnitude of the kinetic friction force there?',
  '(e) Explain why a smaller friction force in (a) than in (b) does not contradict the usual relationship between maximum static friction and kinetic friction.'
 ], "Newton's Second Law - Force Calculation - Q3"),
 ('m71409', 'ex-friction-walking-forward', [
  'As you start walking forward, your shoe pushes backward on the ground without slipping. In which direction does friction act on your shoe? Is this static or kinetic friction? Explain how friction helps you speed up.'
 ], 'Friction - Description - Q1'),
 ('m71410', 'ex-earth-apple-forces', [
  'Earth pulls downward on a falling apple. How does the apple’s gravitational pull on Earth compare in magnitude and direction? Why are their accelerations so different?'
 ], 'Universal Gravitation - Description - Q2'),
]
orders = {
 'm78923':['ex-identifying-forces','fs-id1654920','fs-id1445672'],
 'm67530':['fs-id2928601','fs-id3026744','fs-id1930138','fs-id3010660','fs-id3210019','fs-id1475076','fs-id3180550','fs-id2672485','fs-id1449832','fs-id2423185'],
 'm68330':['fs-id2846557','fs-id2661705','fs-id1595226','fs-id2423524','fs-id2355576','fs-id1572333'],
 'm67044':['ex-spring-proportionality','ex-spring-equilibrium-release','fs-id2008703','eip-540'],
 'm71409':['ex-friction-walking-forward','ex-tommy-box-friction','fs-id1320466','fs-id1425681','fs-id1272970'],
 'm71410':['fs-id1890173','fs-id959677','ex-earth-apple-forces','fs-id3122954'],
 'm67036':['fs-id3055510','fs-id3340905','fs-id3035023','fs-id3047120','fs-id3286004'],
}
export_path=ROOT.parent/'reference-inputs/phys-10-full-export-2026-09-27.imas'
export=json.loads(export_path.read_text(encoding='utf-8'))
sources={q['description']:q for q in export['questionset'].values()}
ledger_path=ROOT/'maintained/editorial-changes.json'
ledger=json.loads(ledger_path.read_text(encoding='utf-8'))
def exercise_content(xml):
 out={}
 for e in E.fromstring(xml).iter(C+'exercise'):
  e.tail=None;out[e.get('id')]=E.tostring(e,encoding='unicode')
 return out
for mid,order in orders.items():
 ident='EX-C2-ADD-ORDER-'+mid
 record_path='proposals/author-corrections/'+ident+'.json'
 assert record_path not in ledger['changes'], 'Already applied'
 p=ROOT/f'maintained/modules/{mid}/index.cnxml';before=p.read_text(encoding='utf-8')
 group=re.search(r'<section\b[^>]*class="conceptual-questions"[^>]*>.*?</section>',before,re.S);assert group,mid
 block=group[0];added=[]
 for module,eid,paragraphs,source_title in items:
  if module!=mid:continue
  description='Introduction to Physics - '+source_title+suffix
  source=sources[description]
  xml=f'<exercise id="{eid}" type="conceptual-questions"><problem id="{eid}-problem">'+''.join(f'<para id="{eid}-p{i}">{text}</para>' for i,text in enumerate(paragraphs,1))+'</problem></exercise>'
  block=block.replace('</section>',xml+'\n</section>')
  added.append(dict(id=eid,source_description=description,assessment="Question Set 3: Newton’s Laws",source_uniqueid=str(source['uniqueid']),source_export_sha256=hashlib.sha256(export_path.read_bytes()).hexdigest(),author=source['author'],export_license_code=source['license'],upstream_attribution=source.get('otherattribution'),adaptation='Fixed-number multipart adaptation with explicit static-versus-kinetic explanation' if 'tommy' in eid else 'Approved fixed conceptual/short-calculation adaptation'))
 hits=list(re.finditer(r'<exercise\b[^>]*id="([^"]+)"[^>]*>.*?</exercise>',block,re.S));parts={h[1]:h[0] for h in hits}
 assert set(parts)==set(order),(mid,set(parts)^set(order))
 block=block[:hits[0].start()]+'\n'.join(parts[eid] for eid in order)+block[hits[-1].end():]
 after=before[:group.start()]+block+before[group.end():]
 old,new=exercise_content(before),exercise_content(after)
 assert all(new[k]==v for k,v in old.items()),mid
 assert len(new)-len(old)==len(added)
 record=dict(id=ident,status='applied-maintainer-approved',target_release='cp2e-ver1.1',module=mid,source_path=p.relative_to(ROOT).as_posix(),source_sha256=hashlib.sha256(before.encode()).hexdigest(),after_sha256=hashlib.sha256(after.encode()).hexdigest(),before=before,after=after,additions=added,exercise_order=order,reason='Six approved MyOpenMath-guided additions and chapter-wide ordering by section topic progression. Existing wording and identities preserved. Cross-section display placement is in exercise-placement.json.')
 (ROOT/record_path).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 p.write_text(after,encoding='utf-8');ledger['changes'].append(record_path)
ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
placement_path=ROOT/'maintained/exercise-placement.json'
placement=json.loads(placement_path.read_text(encoding='utf-8'))
assert not any(p['exercise_id']=='fs-id1572333' for p in placement['placements'])
placement['placements'].append(dict(module='m68330',exercise_id='fs-id1572333',after_module='m67530',after_exercise_id='fs-id3180550',status='maintainer-approved',reason='Approved deferred relocation now applied with overall reorder: aircraft-seat sensation belongs with acceleration/net force in Section 2.4, not Third Law. Original module identity retained.'))
placement_path.write_text(json.dumps(placement,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report=ROOT/'reports/1.1/chapter2-structure/exercise-additions-and-order.json'
report.write_text(json.dumps(dict(additions=6,chapter_exercises=41,source_orders=orders,display_placements=placement['placements'],notes=['Two existing First Law and two Normal Force/Tension questions retain their order.','Within-section order follows basic definitions, force identification, applications, and extensions.','No new circular-motion exercises.','Public version 23 numbers are superseded on next publication.']),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Added six questions; preserved existing exercise content and identities; applied topic order and aircraft relocation.')
