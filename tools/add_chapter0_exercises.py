"""Apply the five maintainer-approved Chapter 0 additions, without rewriting XML."""
from pathlib import Path
import json, re, hashlib, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
items=[
 ('m52310','physics-in-other-fields','Give an example of physics used in each of two fields, such as biology, medicine, architecture, or geology. Identify the physical phenomenon involved in each example.', 'Realm of Physics - Relationship to Other Sciences - Q1/Q2', 'conceptual'),
 ('m67032','recognizing-units','Classify the following units as SI or U.S. customary: meter, second, kilogram, centimeter, square meter, meter per second, foot, and pound. Among the SI units listed, identify the base units, the unit formed by adding a prefix to the meter, and the units formed by combining base units.', 'Physical Quantities and Units - SI Units - Q1/Q2', 'conceptual'),
 ('m67032','why-conversion-works','Explain why multiplying a distance expressed in kilometers by <m:math><m:mfrac><m:mrow><m:mn>1000</m:mn><m:mtext> m</m:mtext></m:mrow><m:mrow><m:mn>1</m:mn><m:mtext> km</m:mtext></m:mrow></m:mfrac></m:math> changes its numerical value without changing the distance. What happens to the units?', 'Physics 10 - Lecture 1, Section 4 - Unit Conversion Examples [3 questions]', 'conceptual'),
 ('m67032','posted-speed-conversion','A road has a posted speed limit of 65 miles per hour. Express this speed in (a) kilometers per hour and (b) meters per second. Use 1 mile = 1.609 kilometers and 1 hour = 3600 seconds. Round your answers to the nearest whole number.', 'Physical Quantities and Units - SI Unit Conversions - Q1', 'short-calculation'),
 ('m67032','plate-motion-over-time','A tectonic plate moves at an average speed of 4 centimeters per year. If it maintains this speed, how far does it travel in one million years? Express your answer in kilometers. Explain why a small annual motion can matter over long periods of time.', 'Physical Quantities and Units - SI Unit Conversions - Q3', 'short-calculation'),
]
ledger_path=ROOT/'maintained/editorial-changes.json'
ledger=json.loads(ledger_path.read_text(encoding='utf-8'))
for mid in dict.fromkeys(x[0] for x in items):
 record_path=f'proposals/author-corrections/EX-C0-{mid}.json'
 assert record_path not in ledger['changes'],'Already applied'
 p=ROOT/f'maintained/modules/{mid}/index.cnxml';before=p.read_text(encoding='utf-8')
 match=re.search(r'<section\b[^>]*class="conceptual-questions"[^>]*>.*?</section>',before,re.S)
 assert match
 group=[x for x in items if x[0]==mid]
 additions='\n'.join('<exercise id="ex-'+key+'" type="conceptual-questions"><problem id="problem-'+key+'"><para id="prompt-'+key+'">'+prompt+'</para></problem></exercise>' for _,key,prompt,_,_ in group)
 block=match[0].replace('<title>Conceptual Questions</title>','<title>Questions and Exercises</title>')
 block=block[:-len('</section>')]+additions+'\n</section>'
 after=before[:match.start()]+block+before[match.end():]
 ET.fromstring(after)
 record=dict(id=f'EX-C0-{mid}',status='applied-maintainer-approved',target_release='cp2e-ver1.1',module=mid,source_path=p.relative_to(ROOT).as_posix(),source_sha256=hashlib.sha256(before.encode()).hexdigest(),after_sha256=hashlib.sha256(after.encode()).hexdigest(),before=before,after=after,reason='Five additions approved in chat; unified Questions and Exercises heading. Existing XML category retained for compatible collection/numbering; task kind is recorded separately.',additions=[dict(id='ex-'+key,source_description=src,task_kind=kind,assessment='Lecture 1 - What is Physics? Models, Units, and Learning Physics in Age of AI' if 'Lecture' in src else 'Question Set 1: Intro, Units, and Kinematics Part 1') for _,key,_,src,kind in group])
 (ROOT/record_path).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 p.write_text(after,encoding='utf-8',newline='\n');ledger['changes'].append(record_path)
ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Added five exercises; preserved existing questions and historical source.')
