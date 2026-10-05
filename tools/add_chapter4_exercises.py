"""Apply approved Chapter 4 additions and topic order, preserving existing exercises."""
from pathlib import Path
import re,json,hashlib,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[1];sha=lambda s:hashlib.sha256(s.encode()).hexdigest()
proposalpath=ROOT/'reports/1.1/chapter4-structure/mom-addition-proposals.json';proposal=json.loads(proposalpath.read_text(encoding='utf8'))
items=[
('m71582','ex-momentum-energy-direction','C4-A1','A car travels around a circular track at constant speed. (a) Does its kinetic energy change? (b) Does its momentum change? (c) If the car doubles its speed, by what factors do its momentum magnitude and kinetic energy change? Explain.'),
('m71583','ex-stopping-versus-rebounding','C4-A2','A 0.20-kg ball approaches a wall at 5.0 m/s. In one collision it stops; in another it rebounds at 5.0 m/s along the same line. (a) Find the magnitude and direction of the ball’s momentum change in each case. (b) If the collisions last equally long, which produces the greater average net force on the ball, and by what factor?'),
('m71583','ex-equal-time-or-distance','C4-A3','Two carts of different masses start at rest on a level, frictionless track. Each is pushed with the same constant horizontal force. (a) If the forces act for the same time, do the carts gain the same momentum or the same kinetic energy? (b) In a separate trial, the carts again start at rest, but the forces act through the same distance. Do the carts gain the same momentum or the same kinetic energy? Explain.'),
('m67039','ex-astronaut-tool-recoil','C4-A4','An astronaut is initially at rest relative to a nearby spacecraft and is holding a tool. Neglect external forces during the following action. (a) In which direction should the astronaut throw the tool to move toward the spacecraft? (b) Explain why air is unnecessary for this method of propulsion. Use conservation of momentum in your explanation.'),
('m67042','ex-identifying-elastic-outcome','C4-A5','A cart moving at 4.0 m/s strikes an identical cart initially at rest on a level, frictionless track. Consider two proposed outcomes: A, the first cart stops and the second moves at 4.0 m/s; B, both carts move at 2.0 m/s in the original direction. (a) Which outcomes conserve momentum? (b) Which conserve kinetic energy? (c) Which could describe an elastic collision? Explain.'),
('m67043','ex-sticking-carts-energy','C4-A6','A 0.50-kg cart moving at 4.0 m/s collides with an identical cart initially at rest on a level, frictionless track. They stick together. (a) Find their common final velocity. (b) Calculate the total kinetic energy before and after the collision. (c) Where can the missing kinetic energy go? (d) Why can the carts not both come to rest?'),
('m67039','ex-hose-momentum-third-law','C4-HOSE','Revisit the garden-hose scenario in Chapter 2, <link document="m68330" target-id="fs-id2661705"/>. Explain the backward push on the hose in terms of momentum transferred to the water. How is this explanation connected to Newton’s third law?')]
orders={
'm71582':['ex-momentum-energy-direction','fs-id1522179','fs-id1522190','fs-id1522215','fs-id1522201'],
'm71583':['ex-equal-time-or-distance','ex-stopping-versus-rebounding','fs-id1247228','fs-id1126726'],
'm67039':['fs-id1749481','fs-id1640067','fs-id1183915','ex-hose-momentum-third-law','fs-id1251869','ex-astronaut-tool-recoil','fs-id1700412','fs-id1222066'],
'm67042':['fs-id3105556','eip-166','ex-identifying-elastic-outcome'],
'm67043':['fs-id1603604','ex-sticking-carts-energy','fs-id3106058']}
exportpath=ROOT.parent/'reference-inputs/phys-10-full-export-2026-09-27.imas';export=json.loads(exportpath.read_text(encoding='utf8'));exsha=hashlib.sha256(exportpath.read_bytes()).hexdigest();byid={x['id']:x for x in proposal['items']};lp=ROOT/'maintained/editorial-changes.json';ledger=json.loads(lp.read_text(encoding='utf8'));provenance=[]
for mid,order in orders.items():
 p=ROOT/f'maintained/modules/{mid}/index.cnxml';before=p.read_text(encoding='utf8');g=re.search(r'<section\b[^>]*class="conceptual-questions"[^>]*>.*?</section>',before,re.S);assert g;block=g[0];added=[]
 for mod,eid,pid,wording in items:
  if mod!=mid:continue
  sources=[]
  for ref in byid.get(pid,{}).get('sources',[]):
   q=export['questionset'][ref['export_question_set_id']];sources.append(dict(**ref,source_uniqueid=str(q['uniqueid']),author=q['author'],export_license_code=q['license'],upstream_attribution=q.get('otherattribution')))
  info=dict(id=eid,proposal_id=pid,module=mid,wording=wording,sources=sources,source_export_sha256=exsha if sources else None,adaptation='Approved fixed conceptual/short-calculation adaptation.' if sources else 'Maintainer-requested cross-chapter connection to garden-hose question.')
  added.append(info);provenance.append(info);block=block.replace('</section>',f'<exercise id="{eid}" type="conceptual-questions"><problem id="{eid}-problem"><para id="{eid}-p1">{wording}</para></problem></exercise>\n</section>')
 hits=list(re.finditer(r'<exercise\b[^>]*id="([^"]+)"[^>]*>.*?</exercise>',block,re.S));parts={h[1]:h[0] for h in hits};assert set(parts)==set(order),(mid,set(parts)^set(order));block=block[:hits[0].start()]+'\n'.join(parts[i] for i in order)+block[hits[-1].end():];after=before[:g.start()]+block+before[g.end():];E.fromstring(after)
 for old in re.findall(r'<exercise\b.*?</exercise>',before,re.S):assert old in after
 rid='EX-C4-ADD-ORDER-'+mid;rp=Path('proposals/author-corrections')/(rid+'.json');assert rp.as_posix() not in ledger['changes'];record=dict(id=rid,status='applied-maintainer-approved',target_release='cp2e-ver1.1',module=mid,source_path=p.relative_to(ROOT).as_posix(),source_sha256=sha(before),after_sha256=sha(after),before=before,after=after,additions=added,exercise_order=order,reason='Six approved MyOpenMath-guided additions plus garden-hose cross-reference; order full chapter by topic. Preserve 16 retained exercise texts and IDs. Previously approved removals remain removed.')
 (ROOT/rp).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8');p.write_text(after,encoding='utf8');ledger['changes'].append(rp.as_posix())
lp.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf8');(ROOT/'reports/1.1/chapter4-structure/exercise-additions-and-order.json').write_text(json.dumps(dict(chapter_exercises=23,source_orders=orders,additions=provenance,removed_public_version44_numbers=[7,8,18]),ensure_ascii=False,indent=2)+'\n',encoding='utf8');proposal['status']='applied-pending-final-preview-review';proposal['approved_separate_addition']['status']='applied'
for x in proposal['items']:x['status']='applied-pending-final-preview-review'
proposalpath.write_text(json.dumps(proposal,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print('Added 7, retained 16, ordered 23 questions.')
