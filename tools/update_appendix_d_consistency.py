"""Apply the approved Appendix D notation review, preserving existing source IDs."""
from pathlib import Path
import re, json, hashlib, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'maintained/modules/m42709/index.cnxml'
before=p.read_bytes();s=before.decode('utf-8'); records=[]
replacements={
 'zero as a subscript denotes an initial value':'subscript zero denotes an initial, reference, rest, or ground-state value, depending on context',
 'change in energy between the initial and final orbits of an electron in an atom':'change in energy; for an atomic transition, the difference between the final and initial energy levels',
 'difference in mass between initial and final products':'mass difference; for nuclear reaction energy, total initial rest mass minus total final rest mass',
 'uncertainty in momentum':'momentum spread (standard deviation) for measurements on identically prepared quantum states',
 'uncertainty in position':'position spread (standard deviation) for measurements on identically prepared quantum states',
 'uncertainty in time':'elapsed time interval',
 'proper time as measured by an observer at rest relative to the process':'proper time: the interval measured by a clock present at both events; for an inertial clock, the events occur at the same position in its rest frame',
 'antiblue (yellow) antiquark color':'antiblue antiquark color charge',
 'antigreen (magenta) antiquark color':'antigreen antiquark color charge',
 'antired (cyan) quark color':'antired antiquark color charge',
 'Avogadro’s number':'Avogadro constant (unit: mol⁻¹)',
 'latent heat':'heat transferred during a phase change',
 'calorie':'thermochemical calorie: 1 cal = 4.184 J exactly',
}
def row(symbol,definition):
 return '<row><entry><m:math>'+symbol+'</m:math></entry><entry>'+definition+'</entry></row>'
mi=lambda x:f'<m:mi>{x}</m:mi>'
unit=lambda x:f'<m:mtext>{x}</m:mtext>'
additions={
 'electron neutrino':row('<m:msub><m:mover accent="true"><m:mi>ν</m:mi><m:mo>¯</m:mo></m:mover><m:mtext>e</m:mtext></m:msub>','electron antineutrino'),
 'direct current':row(mi('D'),'absorbed dose (SI unit: gray, Gy)'),
 'emissivity of an object':row(mi('e'),'elementary charge, the positive magnitude of the proton’s charge; the electron has charge −e'),
 'antigreen (magenta) antiquark color':row(unit('Gy'),'gray, the SI unit of absorbed dose: 1 Gy = 1 J/kg = 100 rad')+row(mi('H'),'equivalent dose to an organ or tissue (SI unit: sievert, Sv)'),
 'force constant of a spring':row(mi('k'),'Coulomb constant'),
 'latent heat of vaporization':row('<m:msub><m:mi>L</m:mi><m:mn>0</m:mn></m:msub>','proper length: length measured in the rest frame of the object'),
 'number of neutrons':row(mi('N'),'number of radioactive nuclei remaining in a sample'),
 'latent heat':row(mi('Q'),'energy released in a nuclear reaction'),
 'radian':row(unit('rad'),'rad, an older unit of absorbed dose: 1 rad = 0.01 Gy = 0.01 J/kg'),
 'strangeness quantum number':row(unit('Sv'),'sievert, the SI unit of equivalent dose and effective dose: 1 Sv = 100 rem'),
 'watt':row(mi('W'),'number of microstates corresponding to a macrostate'),
}
seen=set()
def change(m):
 old=m.group(); entries=list(re.finditer(r'<entry\b[^>]*>[\s\S]*?</entry>',old))
 if len(entries)!=2:return old
 definition=entries[1].group()[7:-8]
 if definition=='uncertainty in energy':
  records.append({'before':old,'after':''});return ''
 new=old
 if definition in replacements:
  seen.add(definition);new=new.replace(entries[1].group(),'<entry>'+replacements[definition]+'</entry>')
 elif definition=='kilocalorie':
  text='food Calorie: 1 Cal = 1 kcal = 4184 J exactly' if '>Cal<' in old else 'kilocalorie: 1 kcal = 1000 cal = 4184 J exactly'
  new=new.replace(entries[1].group(),'<entry>'+text+'</entry>')
 elif definition.startswith('average (indicated'):
  new=new.replace(entries[1].group(),'<entry>an overbar denotes an average (for example, average velocity) or an antiparticle or anticolor, depending on context</entry>')
  new=re.sub(r'<m:mrow>\s*<m:mtext>any symbol</m:mtext>\s*<m:mi/>\s*</m:mrow>','<m:mi>x</m:mi>',new)
  new=new.replace('"any"`" symbol"','x')
 elif definition.startswith('a constant used in relativity'):
  new=new.replace('a constant used in relativity','Lorentz factor, which depends on relative speed')
 if definition in additions:new+=additions[definition]
 if new!=old:records.append({'before':old,'after':new})
 return new
s=re.sub(r'<row>[\s\S]*?</row>',change,s)
assert seen==set(replacements),set(replacements)-seen
r=ET.fromstring(s);r0=ET.fromstring(before)
assert {e.get('id') for e in r0.iter() if e.get('id')} <= {e.get('id') for e in r.iter() if e.get('id')}
assert 'uncertainty in energy' not in s and 'uncertainty in time' not in s
after=s.encode('utf-8');p.write_bytes(after)
proposal='proposals/maintainer-corrections/APPENDIX-D-NOTATION-CONSISTENCY.json'
(ROOT/proposal).write_text(json.dumps({'id':'APPENDIX-D-NOTATION-CONSISTENCY','status':'approved','description':'Approved notation definitions and missing meanings; remove orphaned energy/time uncertainty meanings and supply elapsed time.','changes':[{'path':str(p.relative_to(ROOT)).replace('\\','/'),'before_sha256':hashlib.sha256(before).hexdigest(),'after_sha256':hashlib.sha256(after).hexdigest(),'fragments':records}]},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=ROOT/'maintained/editorial-changes.json';d=json.loads(p.read_text(encoding='utf-8'));d['changes'].append(proposal);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=ROOT/'reports/1.1/appendix-d-consistency';out.mkdir(exist_ok=True)
counts={'before_rows':len(r0.findall('.//{*}row')),'after_rows':len(r.findall('.//{*}row')),'changed_fragments':len(records),'existing_ids_preserved':True}
(out/'validation.json').write_text(json.dumps(counts,indent=2)+'\n');print(counts)
