"""Compile source-preserving conceptual-physics proposals; never edit maintained content."""
from pathlib import Path
import json,re,hashlib,xml.etree.ElementTree as E,html,sys
ROOT=Path(__file__).resolve().parents[1]
C='http://cnx.rice.edu/cnxml';M='http://www.w3.org/1998/Math/MathML'
E.register_namespace('',C);E.register_namespace('m',M)
def source(title,url,locator):return dict(title=title,url=url,locator=locator,checked='2026-09-21')
buoy=source('MIT 8.01: Chapter 27, Static Fluids','https://www.ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/mit8_01scs22_chapter27.pdf','Archimedes principle and floating equilibrium')
bank=source('UNSW PHYS1131: Tutorial 3 solutions','https://newt.phys.unsw.edu.au/~jw/1131/tuts/PHYS1131t3.pdf','Banked-curve force balance: vertical component of normal force equals weight in the frictionless case')
spring=source('Richard Fitzpatrick, UT Austin: Stretching a spring','https://farside.ph.utexas.edu/teaching/301/lectures/node66.html','Slow stretching; external work integral')
work=source('MIT Unified Engineering: Changing the State of a System with Heat and Work','https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node12.html','Quasi-static pressure work and work-sign conventions')
ent=source('MIT: Irreversibility, Entropy Changes, and Lost Work','https://web.mit.edu/16.unified/www/SPRING/propulsion/notes/node47.html','System versus surroundings entropy; reversible heat transfer')
entcalc=source('MIT: Calculation of Entropy Change in Some Basic Processes','https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node41.html','Reversible reference paths and temperature-dependent entropy changes')
energy=source('MIT: Entropy and Unavailable Energy','https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node49.html','Lost work depends on entropy generation and surroundings temperature')
rel=source('Max Planck Institute / Einstein Online: The definition of now','https://www.einstein-online.info/en/spotlight/now/','Equidistant light-signal test; clock synchronization')
files={};items=[]
def raw(mid):
 if mid not in files:files[mid]=(ROOT/f'maintained/modules/{mid}/index.cnxml').read_text(encoding='utf-8')
 return files[mid]
def block(mid,id):
 s=raw(mid);m=re.search(r'<([\w:-]+)\b[^>]*\sid="'+re.escape(id)+r'"[^>]*>',s);assert m,id
 depth=1
 for t in re.finditer(r'</?'+re.escape(m[1])+r'\b[^>]*>',s[m.end():]):
  if t[0].startswith('</'):depth-=1
  elif not t[0].endswith('/>'):depth+=1
  if not depth:return s[m.start():m.end()+t.end()]
 raise ValueError(id)
def parse(s):return E.fromstring('<wrap xmlns="'+C+'" xmlns:m="'+M+'" xmlns:fo="http://www.w3.org/1999/XSL/Format">'+s+'</wrap>')[0]
def add(id,title,reason,sources,attention='Minimal correction; review in context'):
 i=dict(id=id,title=title,status='proposed-correction; not applied',attention=attention,reason=reason,sources=sources,passages=[]);items.append(i);return i
def edit(i,mid,id,replacements=None,new=None):
 old=block(mid,id);out=old
 if new is not None:
  e=parse(old);opening=old[:old.index('>')+1];closing='</'+old[1:].split()[0].split('>')[0]+'>';out=opening+new+closing
 else:
  for a,b in replacements:
   assert out.count(a)==1,(i['id'],id,a,out.count(a));out=out.replace(a,b,1)
 parse(out)
 assert set(re.findall(r'\bid="([^"]+)"',old))<=set(re.findall(r'\bid="([^"]+)"',out)),id
 i['passages'].append(dict(module=mid,source_path=f'maintained/modules/{mid}/index.cnxml',source_id=id,source_sha256=hashlib.sha256(raw(mid).encode()).hexdigest(),before_xml=old,proposed_xml=out))
i=add('P3-01','Specific gravity and floating','The density ratio to water is not a universal float/sink test in every fluid. Preserve the general fraction-submerged derivation and scope the specific-gravity shortcut to its water reference.',[buoy])
edit(i,'m71624','import-auto-id2036384',[('the ratio of the density of an object to a fluid (usually water)','the ratio of the density of an object to the reference density of water')])
edit(i,'m71624','import-auto-id3105421',[
 ('If an object floats, its specific gravity is less than one. If it sinks, its specific gravity is greater than one.','In water at this reference density, an object with specific gravity less than one floats, while one with specific gravity greater than one sinks.'),
 ('Moreover, the fraction of a floating object that is submerged equals its specific gravity.','In this water, the fraction of a floating object that is submerged equals its specific gravity.'),
 ('If an object’s specific gravity is exactly 1, then it will remain suspended in the fluid, neither sinking nor floating.','If the object and the surrounding fluid have equal densities, the object can remain suspended, neither rising nor sinking.')])
i=add('P3-02','Banked-curve normal force','The sentence says banking reduces the normal force. For the ideal banked case developed next, N cos(theta) = mg, so N is larger than mg. Replace the claim with the role of its horizontal component.',[bank])
edit(i,'m67036','fs-id2397853',[('If the surface of the road were banked, the normal force would be less as will be discussed below.','If the surface of the road were banked, the normal force would have a horizontal component toward the center of the curve, as will be discussed below.')])
i=add('P3-03','Spring work: slow deformation and average force','Action–reaction is valid for forces between the hand and spring; it is not a general argument that two forces on one object balance. State slow deformation and identify the average force in the work calculation. The area-under-the-graph and elastic-energy result remain unchanged.',[spring])
edit(i,'m67045','import-auto-id2057112',[
 ('The applied force is exactly opposite to the restoring force (action-reaction),','For slow deformation, the applied force balances the restoring force,'),
 ('Work done on the system is force multiplied by distance, which equals the area under the curve or','Work done on the system equals the area under the force-versus-deformation curve, or')])
p=i['passages'][-1];e=parse(p['proposed_xml']);maths=list(e.iter('{'+M+'}math'));last=maths[-1];sub=next(x for x in last.iter('{'+M+'}msub'))
parent=next(x for x in last.iter() if sub in list(x));idx=list(parent).index(sub);parent.remove(sub);bar=E.Element('{'+M+'}mover');bar.append(sub);E.SubElement(bar,'{'+M+'}mo').text='¯';parent.insert(idx,bar)
for node in last.iter():
 for child in list(node):
  if child.tag=='{'+M+'}annotation':node.remove(child)
p['proposed_xml']=E.tostring(e,encoding='unicode');i['math_change']='An overbar marks the average applied force in Method B; all other source mathematics is preserved.'
i=add('P3-04','Pressure work and sign conventions','The existing note conflates internal/external pressure with opposite work-sign conventions. Replace the note, state slow mechanical balance for the derivation, and scope the adjacent isothermal claim to an ideal gas. This is the largest coordinated proposal; no textbook structure changes are applied.',[work],'Read closely: replacement note and linked assumptions')
edit(i,'m67126','import-auto-id1169737795645',[('A process by which a gas does work on a piston at constant pressure','For a piston moving slowly with negligible friction, the gas pressure nearly balances the external pressure. A process by which the gas does work on the piston at constant pressure')])
edit(i,'m67126','eip-122',new='Here the gas expands slowly enough that its pressure nearly equals the external pressure. For expansion against a constant external pressure, the work done by the gas is <m:math><m:mi>W</m:mi><m:mo>=</m:mo><m:msub><m:mi>P</m:mi><m:mtext>ext</m:mtext></m:msub><m:mi>ΔV</m:mi></m:math>. Some texts instead define work as work done on the gas, giving <m:math><m:msub><m:mi>W</m:mi><m:mtext>on</m:mtext></m:msub><m:mo>=</m:mo><m:mo>−</m:mo><m:msub><m:mi>P</m:mi><m:mtext>ext</m:mtext></m:msub><m:mi>ΔV</m:mi></m:math> and <m:math><m:mi>ΔU</m:mi><m:mo>=</m:mo><m:mi>Q</m:mi><m:mo>+</m:mo><m:msub><m:mi>W</m:mi><m:mtext>on</m:mtext></m:msub></m:math>. These conventions describe the same energy transfer. In this textbook, work is positive when done by the system on its surroundings.')
edit(i,'m67126','import-auto-id1169738219750',[('a gas expanding under pressure','a gas expanding against an external pressure')])
edit(i,'m67126','eip-763',[('A gas expanding isothermally','An ideal gas expanding isothermally'),('its internal energy (as represented by the temperature)','its internal energy, which depends only on temperature,')])
i['math_change']='The note distinguishes W (by the gas) from W_on. Existing numbered equations are retained.'
i=add('P3-05','Entropy formulas: Carnot cycle versus constant-temperature transfer','The heat-ratio relation belongs to a reversible cycle between two reservoirs. Q/T gives a finite entropy change for reversible transfer at constant temperature. The existing small-temperature-change approximation can stay.',[entcalc,ent],'Read the opening derivation and example strategy together')
edit(i,'m67128','import-auto-id1169737795745',[('for a Carnot cycle, and hence for any reversible processes,','for a Carnot cycle,')])
edit(i,'m67128','import-auto-id1169737770807',[('for any reversible process.','for a reversible cycle between these two reservoirs.'),('for a reversible process,','for reversible heat transfer at constant temperature,')])
# Keep the mathematics in the source; qualify the equation rather than redefining entropy itself.
old=block('m67128','import-auto-id1169738208667');end=old.index('However,')
opening=old[:old.index('>')+1]
new=opening+'The expression above applies to reversible heat transfer at constant temperature. '+old[end:]
edit(i,'m67128','import-auto-id1169738208667',new=new[len(opening):new.rfind('</para>')])
old=block('m67128','import-auto-id1169737790371');end=old.index('Remember that')
opening=old[:old.index('>')+1]
edit(i,'m67128','import-auto-id1169737790371',new='How can we calculate the change in entropy for irreversible heat transfer? '+old[end:old.rfind('</para>')])
edit(i,'m67128','import-auto-id1169738115905',[('The change in entropy is defined as:','For melting at constant temperature, the change in entropy is:')])
edit(i,'m67128','fs-id1169738076310',[('the ratio of heat transfer to temperature','for reversible heat transfer at constant temperature, the ratio of heat transfer to absolute temperature')])
edit(i,'m42238','import-auto-id1169737709995',[('which we have used extensively.','for reversible heat transfer at constant temperature, which we have used extensively.')])
i=add('P3-06','Entropy of the system versus system plus surroundings','A system can lose entropy by releasing heat. The second-law statements must refer to an isolated system or to the combined system and surroundings. Coordinate the body, summary, and glossary; the numerical examples need no new results.',[ent],'Read closely: repeated scope correction across the section')
edit(i,'m67128','import-auto-id1169738182621',[('the total change in entropy for a system in any reversible process','the total change in entropy of the system and its surroundings in any reversible process')])
old=block('m67128','import-auto-id1169736590877');cut=old.index('Sometimes this is stated as follows:')
edit(i,'m67128','import-auto-id1169736590877',new='The entropy of the system and that of its surroundings may each change, but their changes sum to zero for a reversible process. '+old[cut:old.rfind('</para>')])
edit(i,'m67128','import-auto-id1169737821042',[('for any system undergoing','for the system and its surroundings together during')])
edit(i,'m67128','import-auto-id1169737871583',[('entropy is constant for a reversible process, and it increases for an irreversible process.','the combined entropy of the system and its surroundings is constant for a reversible process and increases for an irreversible process.')])
for id in ['import-auto-id1169737777969','import-auto-id1169737973964','fs-id1169737918010']:
 edit(i,'m67128',id,[('entropy of a system','entropy of an isolated system')])
edit(i,'m67128','import-auto-id1169737940509',[('Change of entropy is zero','The total entropy change of the system and its surroundings is zero')])
i=add('P3-07','Entropy is not an amount of lost energy','Entropy has units J/K; unavailable work has units J and depends on the surroundings. Keep the qualitative connection while removing identity claims. A broader rewrite of the disorder analogy is explicitly deferred; it is not needed to repair these statements.',[energy],'Short coordinated clarification; preserve the conceptual approach')
edit(i,'m67128','import-auto-id1169738036913',new='Recall that the simple definition of energy is the ability to do work. Entropy helps determine how much energy is unavailable to do work. Although all forms of energy are interconvertible, and all can be used to do work, it is not always possible, even in principle, to convert the entire available energy into work. That unavailable energy is of interest in thermodynamics, because the field of thermodynamics arose from efforts to convert heat to work.')
edit(i,'m67128','import-auto-id1169737973962',[('Entropy is the loss of energy available to do work.','Entropy helps determine the energy available to do work.')])
edit(i,'m67128','import-auto-id1169738134574',[('are not only related but are in fact essentially equivalent.','are related in this example.')])
edit(i,'m67128','fs-id1169737805377',new='a thermodynamic state property related to the dispersal of energy and the energy available to do work')
i=add('P3-08','Simultaneity and light-travel time','Receiving two signals at once establishes simultaneous emission only after accounting for travel times. State that explicitly in the summary. Keep the previously approved train example and SR01 corrections.',[rel])
edit(i,'m42531','import-auto-id2906479',[('(such as by receiving light from the events)','(after accounting for the travel time of light from each event)')])
verified=[
 dict(topic='Floating fraction derivation',disposition='verified unchanged',reason='The preceding derivation correctly uses object density divided by the surrounding fluid density; only the specific-gravity shortcut needs repair.',sources=[buoy]),
 dict(topic='Ideal banked-curve derivation',disposition='verified unchanged',reason='The subsequent frictionless force balance is consistent; the isolated lead-in sentence is the defect.',sources=[bank]),
 dict(topic='Elastic potential energy and area under force graph',disposition='verified unchanged',reason='One-half k x squared and the triangular area agree; no numerical recalculation needed.',sources=[spring]),
 dict(topic='Entropy examples and state-function explanation',disposition='verified unchanged within this scope',reason='Constant-temperature reservoirs and melting support Q/T. The worked values are not changed. Preserve the reversible reference-path explanation and small-temperature-change approximation.',sources=[entcalc]),
 dict(topic='Entropy/disorder pedagogy',disposition='explicitly deferred',reason='A broader statistical-mechanics explanation would be a substantive rewrite. P3-07 repairs energy/entropy identity claims; fuller treatment of disorder and macrostates remains for broader revision.',sources=[energy]),
 dict(topic='Conservative-force heuristic',disposition='verified unchanged in this audit',reason='Preserve the maintainer-approved scoped heuristic; no new contradiction identified. This is not reopened.'),
 dict(topic='Electrical safety and historical/technology leads',disposition='explicitly deferred to next audit batch',reason='Recorded separately in fact-check-followups.json; no claim of verification in Priority 3.')]
packet=dict(date='2026-09-21',status='Batch proposals ready for maintainer review; no canonical content changed.',scope='Six conceptual leads, grouped into eight review items. Related summary/glossary statements included. Not a full-book physics or numerical certification.',items=items,dispositions=verified)
(ROOT/'proposals/1.1/priority3-conceptual-review.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
# Reuse the textbook renderer so comparison MathML and cross-reference labels match the book.
sys.path.insert(0,str(ROOT/'prototype'));sys.argv=['build.py','course','--all'];ns={'__file__':str(ROOT/'prototype/build.py'),'__name__':'review_renderer'}
s= (ROOT/'prototype/build.py').read_text(encoding='utf-8');exec(compile(s.split('OUT.mkdir(parents=True,exist_ok=True);')[0],ns['__file__'],'exec'),ns)
def render(mid,xml):
 s=ns['Renderer'](mid).render(parse(xml));s=re.sub(r'\s+id="[^"]*"','',s)
 slug=ns['registry'][mid]['candidate_slug'];base='/course-full/sections/'+slug+'/index.html'
 s=re.sub(r'href="#([^"]+)"',lambda m:'href="'+base+'#'+m[1]+'"',s)
 s=s.replace('href="../','href="/course-full/sections/')
 return s
esc=html.escape
page=['<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Priority 3 conceptual review</title><style>body{max-width:1250px;margin:auto;padding:24px;font:18px/1.55 Georgia;color:#233c43}a{color:#075e76;overflow-wrap:anywhere}section{border-top:1px solid #abc;padding-top:16px;margin-top:32px}.compare{display:grid;grid-template-columns:1fr 1fr;gap:20px}.cell{min-width:0;background:#f2f6f7;padding:16px;overflow:auto}.note{background:#fff3d6;padding:14px}math{font-size:1.05em} @media(max-width:750px){.compare{grid-template-columns:1fr}}h3{font-size:1.05em}</style><h1>Priority 3: conceptual physics</h1><p>Proposed corrections only; none applied. Eight review groups cover the six leads and their connected summaries/glossaries. The pressure-work note and entropy passages deserve the closest read.</p><ul>']
for i in items:page.append('<li><a href="#'+i['id']+'">'+i['id']+' — '+esc(i['title'])+'</a></li>')
page.append('</ul>')
for i in items:
 page.append('<section id="'+i['id']+'"><h2>'+i['id']+' — '+esc(i['title'])+'</h2><p class="note">'+esc(i['attention'])+'</p><p>'+esc(i['reason'])+'</p>')
 for p in i['passages']:
  mid=p['module'];slug=ns['registry'][mid]['candidate_slug'];link='/course-full/sections/'+slug+'/index.html#'+mid+'--'+p['source_id'].encode().hex()
  page.append('<p><a href="'+link+'">'+esc(ns['registry'][mid]['title'])+' — current context</a></p><div class="compare"><div class="cell"><h3>Before</h3>'+render(mid,p['before_xml'])+'</div><div class="cell"><h3>Proposed for 1.1</h3>'+render(mid,p['proposed_xml'])+'</div></div>')
 page.append('<p>Sources: '+ '; '.join('<a href="'+esc(s['url'])+'">'+esc(s['title'])+'</a> ('+esc(s['locator'])+')' for s in i['sources'])+'</p></section>')
page.append('<section><h2>Other dispositions</h2>')
for v in verified:page.append('<h3>'+esc(v['topic'])+' — '+esc(v['disposition'])+'</h3><p>'+esc(v['reason'])+'</p>')
page.append('</section></html>')
for out in [ROOT/'reports/1.1/priority3-review',ROOT/'prototype/dist/review-1.1/priority3-review']:
 out.mkdir(parents=True,exist_ok=True);(out/'index.html').write_text('\n'.join(page),encoding='utf-8',newline='\n')
print('Prepared',len(items),'review groups and',sum(len(i['passages']) for i in items),'passage comparisons. Maintained source unchanged.')
