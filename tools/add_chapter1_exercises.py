"""Apply six approved MyOpenMath-guided additions in Chapter 1 topic order."""
from pathlib import Path
import json,re,hashlib,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[1]
items=[
 ('m71407','ex-thunder-distance','You hear thunder 3 seconds after seeing lightning. Taking the speed of sound as 340 m/s and neglecting the travel time of light, estimate the distance to the lightning.', 'fs-id4033346', 'Introduction to Physics - Time, Velocity, and Speed - Calculations - Q1 (updated to LibreTexts version)', 'Question Set 2: Kinematics Part 2'),
 ('m67033','ex-acceleration-units','Can both meters per second squared and miles per hour per second describe acceleration? Explain what each unit tells you.', None, 'Introduction to Physics - Acceleration - Units - Q1 (updated to LibreTexts version)', 'Question Set 2: Kinematics Part 2'),
 ('m67034','ex-velocity-time-graphs','Sketch velocity–time graphs for an object moving with constant positive velocity and for one starting from rest with constant positive acceleration. Explain the difference between their slopes.', 'eip-429', 'Physics 10 - Lecture 3, Section 4 - Motion Graph Examples [3 questions]', 'Lecture 3 - Acceleration and Motion Graphs'),
 ('m67034','ex-braking-distance-speed','A car brakes to a stop with constant acceleration. If its initial speed doubles but the magnitude of its braking acceleration stays the same, how does its braking distance change?', 'eip-371', 'Introduction to Physics - Constant Acceleration - Calculation - Q1 (updated to LibreTexts version)', 'Question Set 2: Kinematics Part 2'),
 ('m68876','ex-free-fall-while-rising','Neglecting air resistance, is a ball thrown upward in free fall while rising, at its highest point, and while descending? Explain.', None, 'Introduction to Physics - Falling Objects - Definition - Q1 (updated to LibreTexts version)', 'Question Set 2: Kinematics Part 2'),
 ('m67038','ex-ball-launched-from-cart','A cart moves at constant velocity along a level track and launches a ball vertically relative to the cart. Neglecting air resistance, does the ball land ahead of, behind, or back in the launcher? Explain.', 'fs-id1875651', 'Physics 10 - Lecture 4, Section 3 - Projectile Motion — Launcher-on-Cart Demo & Explanation [3 questions]', 'Lecture 4 - Free Fall, Projectiles, and Circular Motion'),
]
ledger_path=ROOT/'maintained/editorial-changes.json';ledger=json.loads(ledger_path.read_text(encoding='utf-8'))
export=json.loads((ROOT.parent/'reference-inputs/phys-10-full-export-2026-09-27.imas').read_text(encoding='utf-8'))
descriptions={q['description'] for q in export['questionset'].values()}
for mid in dict.fromkeys(x[0] for x in items):
 record_path=f'proposals/author-corrections/EX-C1-ADD-{mid}.json';assert record_path not in ledger['changes'],'Already applied'
 p=ROOT/f'maintained/modules/{mid}/index.cnxml';before=p.read_text(encoding='utf-8')
 group=re.search(r'<section\b[^>]*class="conceptual-questions"[^>]*>.*?</section>',before,re.S);assert group
 block=group[0];added=[]
 for _,ident,prompt,after_id,description,assessment in [x for x in items if x[0]==mid]:
  assert description in descriptions,description
  xml=f'<exercise id="{ident}" type="conceptual-questions"><problem id="{ident}-problem"><para id="{ident}-prompt">{prompt}</para></problem></exercise>'
  if after_id:
   target=re.search(r'<exercise\b[^>]*id="'+re.escape(after_id)+r'"[^>]*>.*?</exercise>',block,re.S);assert target;offset=target.end()
  else:offset=block.index('<exercise ')
  block=block[:offset]+'\n'+xml+'\n'+block[offset:]
  added.append(dict(id=ident,source_description=description,assessment=assessment,adaptation='New self-contained question guided by lecture topic' if description.startswith('Physics 10') else 'Fixed, self-contained adaptation of homework topic',task_kind='short-calculation' if ident=='ex-thunder-distance' else 'graph' if ident=='ex-velocity-time-graphs' else 'conceptual'))
 after=before[:group.start()]+block+before[group.end():];a=E.fromstring(before);b=E.fromstring(after);C='{http://cnx.rice.edu/cnxml}'
 def questions(r):
  result={}
  for e in r.iter(C+'exercise'):e.tail=None;result[e.get('id')]=E.tostring(e,encoding='unicode')
  return result
 old,new=questions(a),questions(b);assert all(new[k]==v for k,v in old.items());assert len(new)-len(old)==len(added)
 record=dict(id=f'EX-C1-ADD-{mid}',status='applied-maintainer-approved',target_release='cp2e-ver1.1',module=mid,source_path=p.relative_to(ROOT).as_posix(),source_sha256=hashlib.sha256(before.encode()).hexdigest(),after_sha256=hashlib.sha256(after.encode()).hexdigest(),before=before,after=after,additions=added,reason='Six approved additions placed in section/topic order before the 1.1 exercise-number freeze; existing questions and IDs preserved.')
 (ROOT/record_path).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');p.write_text(after,encoding='utf-8',newline='\n');ledger['changes'].append(record_path)
ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Six Chapter 1 exercises added; all existing exercise text preserved.')
