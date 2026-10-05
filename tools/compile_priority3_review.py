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
 assert set(re.findall(r'\sid="([^"]+)"',old))<=set(re.findall(r'\sid="([^"]+)"',out)),id
 i['passages'].append(dict(module=mid,source_path=f'maintained/modules/{mid}/index.cnxml',source_id=id,source_sha256=hashlib.sha256(raw(mid).encode()).hexdigest(),before_xml=old,proposed_xml=out))
i=add('P3-01','Specific gravity and floating','The density ratio to water is not a universal float/sink test in every fluid. Preserve the general fraction-submerged derivation and scope the specific-gravity shortcut to its water reference.',[buoy])
edit(i,'m71624','import-auto-id2036384',[('the ratio of the density of an object to a fluid (usually water)','the ratio of the density of an object to the reference density of water')])
edit(i,'m71624','import-auto-id3105421',[
 ('If an object floats, its specific gravity is less than one. If it sinks, its specific gravity is greater than one.','In water at this reference density, an object with specific gravity less than one floats, while one with specific gravity greater than one sinks.'),
 ('Moreover, the fraction of a floating object that is submerged equals its specific gravity.','In this water, the fraction of a floating object that is submerged equals its specific gravity.'),
 ('If an object’s specific gravity is exactly 1, then it will remain suspended in the fluid, neither sinking nor floating.','If the object and the surrounding fluid have equal densities, the object can remain suspended, neither rising nor sinking.')])
i['status']='approved-pending-section-preview'
i['attention']='Approved; included in the whole-section reading preview'
i['authorization']='Maintainer confirmed prior approval of P3-01 and P3-03; earlier pending labels were a bookkeeping error.'
for passage in i['passages']:
 passage['status']='approved-pending-section-preview'

i=add('P3-02','Banked-curve normal force','Delete the incorrect final sentence. The flat-curve example remains complete, and the following paragraph independently introduces banked curves. Maintainer approved deletion without replacement.',[bank])
edit(i,'m67036','fs-id2397853',[(' If the surface of the road were banked, the normal force would be less as will be discussed below.','')])
i['status']='approved-pending-application'
i['authorization']='Maintainer approved deleting the final banked-curve sentence without replacement during P3-02 review.'
i['attention']='Approved deletion; awaiting coordinated application'
i=add('P3-03','Spring work: equilibrium and average force','Force balance in equilibrium follows from Newton’s second law. State that condition explicitly and identify the average force in the work calculation. The area-under-the-graph and elastic-energy result remain unchanged.',[spring])
edit(i,'m67045','import-auto-id2057112',[
 ('The applied force is exactly opposite to the restoring force (action-reaction),','When the forces are in equilibrium, the applied force balances the restoring force,'),
 ('Work done on the system is force multiplied by distance, which equals the area under the curve or','Work done on the system equals the area under the force-versus-deformation curve, or')])
p=i['passages'][-1];e=parse(p['proposed_xml']);maths=list(e.iter('{'+M+'}math'));last=maths[-1];sub=next(x for x in last.iter('{'+M+'}msub'))
parent=next(x for x in last.iter() if sub in list(x));idx=list(parent).index(sub);parent.remove(sub);bar=E.Element('{'+M+'}mover');bar.append(sub);E.SubElement(bar,'{'+M+'}mo').text='¯';parent.insert(idx,bar)
for node in last.iter():
 for child in list(node):
  if child.tag=='{'+M+'}annotation':node.remove(child)
p['proposed_xml']=E.tostring(e,encoding='unicode');i['math_change']='An overbar marks the average applied force in Method B; all other source mathematics is preserved.'
i['status']='approved-pending-section-preview'
i['attention']='Approved; included in the whole-section reading preview'
i['authorization']='Maintainer confirmed prior approval of P3-01 and P3-03; earlier pending labels were a bookkeeping error.'
for passage in i['passages']:
 passage['status']='approved-pending-section-preview'

i=add('P3-04','Pressure work and sign conventions','The existing note conflates internal/external pressure with opposite work-sign conventions. Replace the note with a consistent work-sign convention using the gas pressure acting on the piston, and scope the adjacent isothermal claim to an ideal gas. Piston acceleration does not invalidate the boundary-work calculation. Retain the parenthetical format and chemistry reference; no textbook structure changes are applied.',[work],'Read closely: replacement note and linked assumptions')
edit(i,'m67126','fs-id1169738204673',[( '<m:mi fontstyle="italic">P</m:mi>', '<m:mi>W</m:mi><m:mo>=</m:mo><m:mi fontstyle="italic">P</m:mi>'),('size 12{PΔV}', 'size 12{W=PΔV}')])
i['passages'][-1]['status']='approved-pending-application'
i['passages'][-1]['authorization']='Maintainer requested the numbered equation 8.9.1 explicitly read W = P ΔV so it stands alone when scanning.'
note_maths=re.findall(r'<m:math>.*?</m:math>',block('m67126','eip-122'),re.S)
assert len(note_maths)==4
# Compact token content avoids legacy indentation/newlines inside math identifiers.
note_maths[0]='<m:math><m:mi>P</m:mi></m:math>'
note_maths[3]='<m:math><m:mrow><m:mi mathvariant="normal">Δ</m:mi><m:mi>U</m:mi><m:mo>=</m:mo><m:mi>Q</m:mi><m:mo>+</m:mo><m:mi>W</m:mi></m:mrow></m:math>'

edit(i,'m67126','eip-122',new='(Note that the pressure involved in this work that we’ve called '+note_maths[0]+' is the pressure of the gas <emphasis effect="italics">inside</emphasis> the tank. There are some—especially chemists—who use work done <emphasis effect="italics">on</emphasis> the system, rather than work done <emphasis effect="italics">by</emphasis> the system, as the basis of the First Law of Thermodynamics. This definition reverses the sign convention for work, and results in a statement of the first law that becomes '+note_maths[3]+'. In this textbook, we will use the <emphasis effect="italics">physics</emphasis> convention of using work done by the system on the surrounding, not the other way around.)')
i['passages'][-1]['status']='approved-pending-application'
i['passages'][-1]['authorization']='Maintainer approved the parenthetical replacement retaining especially chemists and explaining work done on versus by the system, and requested exact restoration of the final sentence identifying the physics convention.'
edit(i,'m67126','import-auto-id1169738219750',[('a gas expanding under pressure','a gas expanding against an external pressure')])
edit(i,'m67126','eip-763',[('A gas expanding isothermally','An ideal gas expanding isothermally'),('its internal energy (as represented by the temperature)','its internal energy, which depends only on temperature,')])
i['math_change']='The note preserves P and ΔU=Q+W with compact native MathML tokens for correct inline typesetting and removes the external-pressure expressions. Equation 8.9.1 gains W = in both presentation MathML and its annotation; equation identifiers are retained.'
i['status']='approved-pending-application'
i['authorization']='Maintainer approved the revised parenthetical, requested exact restoration of the physics-convention sentence, and approved the rest of P3-04.'
i['attention']='Approved; awaiting coordinated application'
i=add('P3-05','Entropy formulas: Carnot cycle versus constant-temperature transfer','The heat-ratio relation belongs to a reversible cycle between two reservoirs. Q/T gives a finite entropy change for reversible transfer at constant temperature. The existing small-temperature-change approximation can stay.',[entcalc,ent],'Read the opening derivation and example strategy together')
edit(i,'m67128','import-auto-id1169737795745',[('for a Carnot cycle, and hence for any reversible processes,','for a Carnot cycle,')])
edit(i,'m67128','import-auto-id1169737770807',[('for any reversible process.','for a reversible Carnot cycle.'),('for a reversible process,','for reversible heat transfer at constant temperature,')])
# Keep the mathematics in the source; qualify the equation rather than redefining entropy itself.
old=block('m67128','import-auto-id1169738208667');end=old.index('However,')
opening=old[:old.index('>')+1]
new=opening+'The expression above applies to reversible heat transfer at constant temperature. '+old[end:]
edit(i,'m67128','import-auto-id1169738208667',new=new[len(opening):new.rfind('</para>')])
old=block('m67128','import-auto-id1169737790371');end=old.index('Remember that')
opening=old[:old.index('>')+1]
edit(i,'m67128','import-auto-id1169737790371',new='The hot reservoir’s internal energy decreases by 4000 J, while the cold reservoir’s internal energy increases by the same amount. These changes take each reservoir to a new state, even though its temperature remains nearly constant.')
i['passages'][-1]['proposed_following_xml']=['<para id="cp2e-entropy-example-reversible-path">To calculate the entropy changes, imagine bringing each reservoir separately to its final state by reversible heat transfer. The hot reservoir releases 4000 J to another body infinitesimally cooler than itself; the cold reservoir receives 4000 J from another body infinitesimally warmer than itself. We can then use <m:math><m:mi>ΔS</m:mi><m:mo>=</m:mo><m:mfrac><m:mi>Q</m:mi><m:mi>T</m:mi></m:mfrac></m:math> for each reservoir.</para>']
edit(i,'m67128','import-auto-id1169737968593',new='A hot reservoir at 600 K loses 4000 J through heat transfer to a cold reservoir at 250 K. The reservoirs are sufficiently large that their temperature changes are negligible. Calculate their total change in entropy. (See <link target-id="import-auto-id1169738087634"/>.)')
edit(i,'m67128','import-auto-id1169738234769',new='For the hot reservoir,')
edit(i,'m67128','import-auto-id1169737819358',new='For the cold reservoir,')
edit(i,'m67128','import-auto-id1169738110466',new='The cold reservoir gains more entropy than the hot reservoir loses, so the total entropy increases. The actual heat transfer conserves energy, but reduces the energy available to do work.')
example_figure=block('m67128','import-auto-id1169738087634')
caption=re.search(r'<caption>.*?</caption>',example_figure,re.S).group(0)
edit(i,'m67128','import-auto-id1169738087634',[(caption,'<caption>(a) Heat transfer from a hot reservoir to a cold one is irreversible and produces an overall increase in entropy. (b) Each reservoir can reach the same final state through a separate reversible heat transfer with an auxiliary body at an infinitesimally different temperature. These separate transfers give the same entropy changes for the two reservoirs as the actual irreversible transfer.</caption>'),('Part b of the figure shows two reversible heat transfers from the hot system to the cold system.','Part b shows separate reversible heat transfers: the hot reservoir releases heat to an auxiliary body and the cold reservoir receives heat from another auxiliary body.')])
edit(i,'m67128','import-auto-id1169738115905',[('The change in entropy is defined as:','For melting at constant temperature, the change in entropy is:')])
edit(i,'m67128','fs-id1169738076310',[('the ratio of heat transfer to temperature','for reversible heat transfer at constant temperature, the ratio of heat transfer to absolute temperature')])
edit(i,'m42238','import-auto-id1169737709995',[('which we have used extensively.','for reversible heat transfer at constant temperature, which we have used extensively.')])
i['status']='approved-pending-section-preview'
i['authorization']='Maintainer found the remainder of P3-05 acceptable after the Carnot-cycle wording correction; whole-section preview requested before final application.'
i['attention']='Approved wording; whole-section preview still requested'
i=add('P3-06','Entropy of the system versus system plus surroundings','First state only what the reservoir calculation establishes for one full cycle of a reversible Carnot engine, then complete the opening promise by accounting for the engine returning to its initial state. The later general statements remain for review. A system can lose entropy by releasing heat. The second-law statements must refer to an isolated system or to the combined system and surroundings. Coordinate the body, summary, and glossary; the numerical examples need no new results.',[ent],'Read closely: repeated scope correction across the section')
edit(i,'m67125','import-auto-id1169737860425',[(
 'The <term id="import-auto-id1169737753839">first law of thermodynamics</term> states',
 'A <emphasis effect="bold">closed system</emphasis> can exchange energy, but not matter, with its surroundings. An <emphasis effect="bold">isolated system</emphasis> exchanges neither energy nor matter with its surroundings. Here we consider closed systems, with energy transferred by heat and work. The <term id="import-auto-id1169737753839">first law of thermodynamics</term> states')])
i['passages'][-1]['status']='proposed-definition; awaiting review'
i['passages'][-1]['review_anchor']='P3-06-system-definitions'
after=block('m67125','import-auto-id1169737803043');after=after[:after.index('We use the following sign conventions:')].rstrip()+'</para>'
i['passages'][-1]['context_after_xml']=[block('m67125','fs-id1169737787594'),after]
edit(i,'m67128','import-auto-id1169738182621',new='This result means <emphasis effect="italics">the total change in entropy of the surrounding</emphasis> for one full cycle of a reversible Carnot engine is zero. The engine itself returns to its initial state after one full cycle, so its entropy is unchanged. Thus, the total entropy change of the engine and its surroundings is zero.')
i['passages'][-1]['authorization']='Maintainer supplied the reservoir-only conclusion and approved the following explanation that the engine returns to its initial state; do not generalize this calculation to all reversible processes.'
i['passages'][-1]['status']='approved-pending-application'
old=block('m67128','import-auto-id1169736590877');cut=old.index('Sometimes this is stated as follows:')
edit(i,'m67128','import-auto-id1169736590877',new='The entropy of the system and that of its surroundings may each change, but their changes sum to zero for a reversible process. '+old[cut:old.rfind('</para>')])
edit(i,'m67128','import-auto-id1169737821042',[('for any system undergoing','for the system and its surroundings together during')])
edit(i,'m67128','import-auto-id1169737871583',[('entropy is constant for a reversible process, and it increases for an irreversible process.','the combined entropy of the system and its surroundings is constant for a reversible process and increases for an irreversible process.')])
for id in ['import-auto-id1169737777969','import-auto-id1169737973964','fs-id1169737918010']:
 edit(i,'m67128',id,[('entropy of a system','entropy of an isolated system')])
edit(i,'m67128','import-auto-id1169737940509',[('Change of entropy is zero','The total entropy change of the system and its surroundings is zero')])
i['status']='approved-pending-section-preview'
i['authorization']='Maintainer approved the rest of P3-06, including the earlier closed/isolated definitions and matching glossary entries. Preview affected whole sections after review through P3-08 before final application.'
i['attention']='Approved; matching glossary entries included in whole-section preview'
# Whole-section read-through: replace the repeated law with macroscopic state examples.
edit(i,'m67125','import-auto-id1169737795608',[(' A second way to view the internal energy of a system is in terms of its macroscopic characteristics, which are very similar to atomic and molecular average values.','')])
edit(i,'m67125','import-auto-id1169737754060',new='A second way to view the internal energy of a system is in terms of its macroscopic characteristics, which are very similar to atomic and molecular average values. Internal energy is a property of the state of a system. For a fixed amount of an ideal gas, it depends only on temperature: raising the temperature increases the internal energy. For other materials, volume and physical state can also matter. For example, melting ice into water increases its internal energy even though its temperature remains constant during melting.')
edit(i,'m67125','import-auto-id1169738144580',new='The change in internal energy depends only on the initial and final states, whereas the amounts of heat transferred and work done depend on the process connecting those states.')
i['passages'].append(dict(module='m67125',source_path='maintained/modules/m67125/index.cnxml',source_id='fs-id1169738046146',source_sha256=hashlib.sha256(raw('m67125').encode()).hexdigest(),before_xml=block('m67125','fs-id1169738046146'),proposed_xml='',operation='remove',reason='Remove the duplicate first-law equation; no inbound references in maintained CNXML. The original first-law equation remains earlier in the section.'))
for passage in i['passages'][-4:]:
 passage['authorization']='Maintainer requested the suggested internal-energy/state-property replacement in context for preview review.'
 passage['status']='requested-preview; pending-context-review'
i['glossary_additions']=[dict(module='m67125', proposed_xml='<definition id="cp2e-'+key+'-definition"><term>'+term+'</term><meaning id="cp2e-'+key+'-meaning">'+meaning+'</meaning></definition>') for key,term,meaning in [('closed-system','closed system','a system that can exchange energy, but not matter, with its surroundings'),('isolated-system','isolated system','a system that exchanges neither energy nor matter with its surroundings')]]
i['followup_tasks']=[
 'Add matching closed system and isolated system glossary entries to The First Law of Thermodynamics and verify generated chapter-end glossary inclusion.',
 'After review through P3-08, prepare complete affected-section previews incorporating the coordinated proposals for maintainer read-through; additional corrections may follow.'
]
for passage in i['passages']:
 passage['status']='approved-pending-section-preview'

i=add('P3-07','Entropy is not an amount of lost energy','Entropy has units J/K; unavailable work has units J and depends on the surroundings. Keep the qualitative connection while removing identity claims. A broader rewrite of the disorder analogy is explicitly deferred; it is not needed to repair these statements.',[energy],'Short coordinated clarification; preserve the conceptual approach')
edit(i,'m67128','import-auto-id1169738036913',new='A heat engine converts part of the energy transferred to it as heat into mechanical work. It is not always possible, even in principle, to convert all of a system’s energy into work. Entropy helps determine how much energy is unavailable to do work. That unavailable energy is of interest in thermodynamics, because the field of thermodynamics arose from efforts to convert heat to work.')
i['passages'][-1]['status']='approved-pending-section-preview'
i['passages'][-1]['authorization']='Maintainer approved the revised opening connecting heat engines to mechanical work, followed by the limits on converting energy into work and the role of entropy; this supersedes the generic energy-transfer opening.'
edit(i,'m67128','import-auto-id1169737973962',[('Entropy is the loss of energy available to do work.','Entropy helps determine the energy available to do work.')])
edit(i,'m67128','import-auto-id1169738134574',[('are not only related but are in fact essentially equivalent.','are related in this example.')])
edit(i,'m67128','fs-id1169737805377',new='a thermodynamic state property associated with a system’s disorder and related to the energy available to do work')
edit(i,'m67128','import-auto-id1169738248900',[('Entropy is related not only to the unavailability of energy to do work—it is also a measure of disorder.','Entropy is related both to the unavailability of energy to do work and to the disorder of a system.')])
i['passages'][-1]['authorization']='Maintainer approved this replacement sentence during the whole-section read-through and requested the refreshed preview.'
i['passages'][-1]['status']='approved-pending-section-preview'
i['status']='approved-pending-section-preview'
i['authorization']='Maintainer approved P3-07 following the heat-engine opening and the glossary proposal retaining the disorder connection. Whole-section preview remains pending.'
i['attention']='Approved; whole-section preview pending'
from priority3_carnot_review import append_carnot_review
append_carnot_review(add,edit,block,source,ent,work)
i=add('P3-09','Simultaneity and light-travel time','Receiving two signals at once establishes simultaneous emission only after accounting for travel times. State that explicitly in the summary. Keep the previously approved train example and SR01 corrections.',[rel])
edit(i,'m42531','import-auto-id2906479',[('(such as by receiving light from the events)','(after accounting for the travel time of light from each event)')])
i['passages'][-1].update(proposed_xml='',operation='remove',authorization='Maintainer approved removing the redundant In summary paragraph after the train explanation and thought-experiment paragraph were revised.')
edit(i,'m42531','eip-745',[('Since both lamps are the same distance from her in her reference frame and the train is moving to the right, she perceives the flash from the right-hand bulb occurring before the left-hand bulb.  Since in her frame, the flashes are not emitted at the same time, they also do not arrive at the same time.','As observer B also notes, she receives the flash from the right-hand bulb before the flash from the left-hand bulb. Since the lamps are equally distant from her and light travels at the same speed in both directions in her frame, she concludes that the right-hand bulb emitted its flash first.')])
i['status']='approved-pending-section-preview'
i['authorization']='Maintainer approved P3-09 and the coordinated train-paragraph clarification: connect the arrival order already established in B’s description to A’s inference about emission times.'
for passage in i['passages']:
 passage['status']='approved-pending-section-preview'
train_paragraph=i['passages'][-1]
train_paragraph['proposed_xml']=train_paragraph['proposed_xml'].replace('light travels at the same speed in both directions in her frame,','light travels at the same speed in both directions in her frame (postulate 2),').replace(' Note, however, that both A and B agree on the order of the flashes arriving at A’s location.','')
edit(i,'m42531','import-auto-id2998902',new='This <emphasis effect="italics">thought experiment</emphasis> shows how the postulates of special relativity lead to a counterintuitive conclusion. We might expect two flashes emitted simultaneously for one observer to be emitted simultaneously for everyone. But the second postulate requires both observers to measure the same speed of light, despite their relative motion. Even after accounting for light-travel times, they disagree about whether the flashes were emitted simultaneously. Neither inertial reference frame is privileged (postulate 1), so we must give up the idea of absolute simultaneity.')
i['passages'][-1]['status']='approved-pending-section-preview'
i['passages'][-1]['authorization']='Maintainer requested a substantial rewrite emphasizing the counterintuitive conclusions required by the SR postulates, especially the second postulate.'
edit(i,'m42531','import-auto-id1964942',[('in both frames, and because time','in both frames (postulate 2), and because time')])
i['passages'][-1]['status']='approved-pending-section-preview'
edit(i,'m42531','import-auto-id3129650',[('In the case of the astronaut observe the reflecting light, the astronaut measures proper time.','The astronaut observing the reflected light measures proper time.')])
i['passages'][-1]['status']='approved-pending-section-preview'
edit(i,'m42531','import-auto-id1343207',new='During each constant-velocity leg of the journey, each twin measures the other’s clock as running slower. This symmetry does not extend to the whole round trip. The astronaut turns around and changes inertial frames, while the Earth-bound twin remains in approximately the same inertial frame. Changing frames also changes which event on Earth the astronaut assigns as simultaneous with her own: the outward and return frames assign different ages to the distant Earth-bound twin at the turnaround. Accounting for this change, special relativity predicts that the astronaut ages less when the twins reunite. The key is that the twins follow different paths through spacetime, so they need not experience the same elapsed time.')
edit(i,'m42531','import-auto-id2722570',[('Both special and general relativity had to be taken into account, since gravity and accelerations were involved as well as relative motion.','The predictions included both the effects of motion from special relativity and gravitational time dilation from general relativity: clocks at the aircraft’s higher altitude run faster than clocks on the ground because of the difference in gravitational potential.')])
edit(i,'m42531','import-auto-id2574148',new='The twin paradox asks why a twin traveling at a relativistic speed away and then back towards the Earth ages less than the Earth-bound twin. Although time dilation is reciprocal during each constant-velocity leg, the traveling twin changes inertial frames to return. Special relativity accounts for the different elapsed times along the twins’ paths.')
edit(i,'m42531','fs-id2692462',new='the apparent contradiction between reciprocal time dilation and the traveling twin aging less on a round trip; the traveling twin changes inertial frames, so the complete journeys are not symmetric')
for passage in i['passages'][-4:]:
 passage['status']='requested-preview; pending-context-review'
 passage['authorization']='Maintainer requested a coordinated twin-paradox rewrite preserving reciprocal time dilation and moving the gravitational explanation to Hafele–Keating. Summary and glossary aligned for review.'
i['sources'].append(source('Hafele and Keating: Around-the-World Atomic Clocks: Predicted Relativistic Time Gains','https://doi.org/10.1126/science.177.4044.166','Kinematic and gravitational contributions to the flying-clock comparison'))
edit(i,'m42531','import-auto-id2768850',[('The third side of these similar triangles','The third side of these triangles')])
i['passages'][-1]['status']='approved-pending-section-preview'
verified=[
 dict(topic='Floating fraction derivation',disposition='verified unchanged',reason='The preceding derivation correctly uses object density divided by the surrounding fluid density; only the specific-gravity shortcut needs repair.',sources=[buoy]),
 dict(topic='Ideal banked-curve derivation',disposition='verified unchanged',reason='The subsequent frictionless force balance is consistent; the isolated lead-in sentence is the defect.',sources=[bank]),
 dict(topic='Elastic potential energy and area under force graph',disposition='verified unchanged',reason='One-half k x squared and the triangular area agree; no numerical recalculation needed.',sources=[spring]),
 dict(topic='Entropy examples and state-function explanation',disposition='verified unchanged within this scope',reason='Constant-temperature reservoirs and melting support Q/T. The worked values are not changed. Preserve the reversible reference-path explanation and small-temperature-change approximation.',sources=[entcalc]),
 dict(topic='Entropy/disorder pedagogy',disposition='pending review after thermodynamics and P3-09 (SR)',reason='Maintainer requested review now within the current revision cycle, rather than automatic deferral. Examine disorder, macrostates, and the scope of a useful correction; present findings before deciding whether a broader revision should be deferred.',sources=[energy]),
 dict(topic='Conservative-force heuristic',disposition='verified unchanged in this audit',reason='Preserve the maintainer-approved scoped heuristic; no new contradiction identified. This is not reopened.'),
 dict(topic='Electrical safety and historical/technology leads',disposition='pending review after thermodynamics and P3-09 (SR)',reason='Maintainer requested these recorded leads be reviewed in the current revision cycle. Investigate before treating them as errors; any renewed deferral is for the maintainer to decide. Detailed leads remain in fact-check-followups.json.')]
i=add('P3-11','Use microstate comparisons without logarithm calculations','Retain Boltzmann’s expression as a reference while making the example and connected exercises accessible without logarithms.',[],'Maintainer requested this conceptual treatment; read the revised section in context.')
formula_note=next(p for group in items for p in group['passages'] if p['module']=='m42238' and p['source_id']=='import-auto-id1169737709995')
formula_note['proposed_xml']=formula_note['proposed_xml'].replace('</para>',' The formula is included here as a reference; no logarithm calculations are needed for this section. The key point is that more microstates correspond to greater entropy.</para>')
formula_note['authorization']='Maintainer approved retaining the expression as a reference without requiring logarithm calculations; coordinated with P3-11.'
edit(i,'m42238','import-auto-id1169737780734',[('What is the change in entropy?','Does the entropy increase or decrease?')])
edit(i,'m42238','import-auto-id1169737795101',new='Compare the numbers of microstates for the two macrostates in <link target-id="import-auto-id1169738223876"/>. The macrostate with more microstates has greater entropy.')
edit(i,'m42238','import-auto-id1169737895337',new='The 60-heads, 40-tails macrostate has <m:math><m:mn>1.4</m:mn><m:mo>×</m:mo><m:msup><m:mn>10</m:mn><m:mn>28</m:mn></m:msup></m:math> microstates. The 50-heads, 50-tails macrostate has <m:math><m:mn>1.0</m:mn><m:mo>×</m:mo><m:msup><m:mn>10</m:mn><m:mn>29</m:mn></m:msup></m:math> microstates, about seven times as many. The entropy therefore increases.')
for ident in ['eip-822','import-auto-id1169738155874','eip-827']:
 edit(i,'m42238',ident,[])
 i['passages'][-1].update(proposed_xml='',operation='remove')
edit(i,'m42238','import-auto-id1169737967292',new='It is not impossible for further tosses to produce the initial state of 60 heads and 40 tails, but it is less likely than 50 heads and 50 tails. The coin model illustrates why a macrostate with more microstates is more likely. For a macroscopic physical system, a substantial spontaneous decrease in total entropy is overwhelmingly unlikely.')
edit(i,'m42238','import-auto-id1169738164157',[('What is the change in entropy if','Does entropy increase or decrease if'),('(b) What if you get','(b) Does entropy increase or decrease if you get')])
edit(i,'m42238','import-auto-id1169738072210',[('What is the change in entropy if','Does entropy increase or decrease if')])
edit(i,'m42238','import-auto-id1169737861844',new='(a) Entropy decreases.')
edit(i,'m42238','fs-id1169738068841',[])
i['passages'][-1].update(proposed_xml='',operation='remove',status='approved-pending-section-preview',reason='Remove the seven-step numerical entropy checklist. Normalized text is identical in the maintained source, recovered CNX baseline, and pinned CC BY College Physics 2e snapshot. No inbound references were found in maintained CNXML.',authorization='Maintainer requested the same treatment as the thermodynamics checklist after checking upstream similarity and dependent exercises.')
i['passages'][-1]['sources']=[source('College Physics 2e, pinned CC BY snapshot: m42238','https://github.com/openstax/osbooks-college-physics-bundle/blob/f98d7a792138a6133fe7267d17e70aa04e9ccbed/modules/m42238/index.cnxml','Problem-Solving Strategies for Entropy; fs-id1169738068841')]
i['status']='approved-pending-section-preview'
i['authorization']='Maintainer approved retaining the formula without an expectation of logarithm calculations and requested a revised example and refreshed preview. Connected exercise parts are aligned by asking for the direction of change.'
codata=source('NIST: 2022 CODATA recommended constants','https://physics.nist.gov/cuu/Constants/Table/allascii.txt','Latest published adjustment verified 2026-09-23; vacuum constants and submicroscopic masses')
codata['checked']='2026-09-23'
i=add('P3-12','Update Useful Information to CODATA 2022','Update the two tables citing 2018 data to the latest published CODATA adjustment. Classroom-rounded values and SI-defining constants remain unchanged.',[codata],'Numerical reference update; high-precision values and uncertainties checked against NIST.')
common=[('http://www.physics.nist.gov/cuu','https://physics.nist.gov/cuu/Constants/'),('www.physics.nist.gov/cuu','physics.nist.gov/constants'),('(2018 values)','(2022 CODATA values)')]
edit(i,'m78798','import-auto-id1211982',common+[
 ('8.9875517923(13)','8.9875517862(14)'),
 ('8.8541878128(13)','8.8541878188(14)'),
 ('1.25663706212(19)','1.25663706127(20)')])
i['passages'][-1]['derivation']='Coulomb constant = 1/(4*pi*epsilon_0), using CODATA 2022 vacuum permittivity; relative standard uncertainty inherited from epsilon_0. All other numerical changes are directly tabulated by NIST.'
constants_patch=i['passages'][-1]
constants_patch['proposed_xml']=constants_patch['proposed_xml'].replace('Values in parentheses are the uncertainties in the last digits. Values in the approximate column are rounded. Absence of an uncertainty does not imply that a displayed value is exact.','Values marked “exact” are exact as written. The gas constant R and Stefan–Boltzmann constant σ are also exact, but their displayed values are rounded. Parentheses give uncertainties in the last digits. Values in the approximate column are rounded.')
exact_labels={'Speed of light in vacuum':'exact','Avogadro’s number':'exact','Boltzmann’s constant':'exact','Elementary charge':'exact','Planck’s constant':'exact','Gas constant':'rounded','Stefan-Boltzmann constant':'rounded'}
def label_constant_row(match):
 row=match[0]
 entries=list(re.finditer(r'<entry\b[^>]*>.*?</entry>',row,re.S))
 if len(entries)!=4:return row
 meaning=re.sub(r'<[^>]+>','',entries[1][0]).strip()
 if meaning not in exact_labels:return row
 value=entries[2]
 return row[:value.start()]+value[0].replace('</entry>',' ('+exact_labels[meaning]+')</entry>')+row[value.end():]
constants_patch['proposed_xml']=re.sub(r'<row\b[^>]*>.*?</row>',label_constant_row,constants_patch['proposed_xml'],flags=re.S)
constants_patch['authorization']='Maintainer approved explicit exact labels for c, N_A, k_B, e, h; rounded labels for the displayed R and sigma; and the explanatory table note.'
edit(i,'m78798','import-auto-id1125517',common+[
 ('9.1093837015(28)','9.1093837139(28)'),
 ('1.67262192369(51)','1.67262192595(52)'),
 ('1.67492749804(95)','1.67492750056(85)'),
 ('1.66053906660(50)','1.66053906892(52)'),
 ('Numbers without uncertainties are exact as defined.','Values in the approximate column are rounded.')])
i['status']='requested-update-pending-section-preview'
i['authorization']='Maintainer requested replacing the 2018 references with the most recent data.'
from priority3_boltzmann_review import append_boltzmann_review
append_boltzmann_review(items,add,edit,block,raw,ROOT)
notation_group=next(group for group in items if group['id']=='P3-10')
edit(notation_group,'m42531','import-auto-id1744942',[('<m:mi>τ</m:mi>','<m:msub><m:mi>t</m:mi><m:mn>0</m:mn></m:msub>')])
notation_group['passages'][-1]['status']='approved-pending-section-preview'
notation_group['passages'][-1]['authorization']='Maintainer approved changing the M02 pion calculation from Delta tau to Delta t_0 for consistency; numerical calculation unchanged. This approval does not approve pending P3-09.'
symbol_patch=next(p for group in items for p in group['passages'] if p['module']=='m42709' and p['source_id']=='import-auto-id1688908')
symbol_row=next(m[0] for m in re.finditer(r'<row\b[^>]*>.*?</row>',symbol_patch['proposed_xml'],re.S) if 'a constant used in relativity' in m[0])
symbol_formula=re.search(r'<m:math\b[^>]*>.*?</m:math>',symbol_row,re.S).group(0)
symbol_formula=symbol_formula.replace('display="block"','display="inline"')
symbol_new='<row><entry><m:math><m:mi>γ</m:mi></m:math></entry><entry>a constant used in relativity ('+symbol_formula+')</entry></row>'
symbol_patch['proposed_xml']=symbol_patch['proposed_xml'].replace(symbol_row,symbol_new)
symbol_patch['layout_followup']='Maintainer requested moving the gamma formula into its definition, leaving only gamma in the symbol column. Preserve the original inline division notation.'
delta_row=next(m[0] for m in re.finditer(r'<row\b[^>]*>.*?</row>',symbol_patch['proposed_xml'],re.S) if 'uncertainty in whatever quantity follows' in m[0])
symbol_patch['proposed_xml']=symbol_patch['proposed_xml'].replace(delta_row,'')
symbol_patch['notation_cleanup']='Maintainer approved removing the unused lowercase delta uncertainty entry; retain the Greek-alphabet table.'
assert symbol_patch['proposed_xml'].count('<entry>potential difference</entry>')==1
symbol_patch['proposed_xml']=symbol_patch['proposed_xml'].replace('<entry>potential difference</entry>','<entry>potential difference (voltage)</entry>')
symbol_patch['voltage_followup']='Maintainer requested voltage as a synonym for potential difference in the Delta V entry, not for electric potential.'
for unused_angle in ["Brewster's angle",'critical angle']:
 angle_row=next(m[0] for m in re.finditer(r'<row\b[^>]*>.*?</row>',symbol_patch['proposed_xml'],re.S) if '<entry>'+unused_angle+'</entry>' in m[0])
 symbol_patch['proposed_xml']=symbol_patch['proposed_xml'].replace(angle_row,'')
symbol_patch['angle_cleanup']='Maintainer approved removing the Brewster angle and critical angle entries; neither concept nor symbol occurs elsewhere in maintained text or equations.'
for unused_field in ['electron’s intrinsic magnetic field','orbital magnetic field']:
 field_row=next(m[0] for m in re.finditer(r'<row\b[^>]*>.*?</row>',symbol_patch['proposed_xml'],re.S) if '<entry>'+unused_field+'</entry>' in m[0])
 symbol_patch['proposed_xml']=symbol_patch['proposed_xml'].replace(field_row,'')
coulomb_row=next(m[0] for m in re.finditer(r'<row\b[^>]*>.*?</row>',symbol_patch['proposed_xml'],re.S) if '<entry>coulomb (a fundamental SI unit of charge)</entry>' in m[0])
coulomb_new=coulomb_row.replace('<m:mi>C</m:mi>','<m:mi mathvariant="normal">C</m:mi>').replace('size 12{C} {}','size 12{roman C} {}').replace('coulomb (a fundamental SI unit of charge)','coulomb (SI unit of charge)')
symbol_patch['proposed_xml']=symbol_patch['proposed_xml'].replace(coulomb_row,coulomb_new)
symbol_patch['field_and_unit_cleanup']='Maintainer approved removing unused B_int and B_orb and requested upright C for coulomb. Also remove the incorrect fundamental-unit designation; the coulomb is a derived SI unit.'
for unused_definition in ['total capacitance in parallel','total capacitance in series','center of gravity']:
 unused_row=next(m[0] for m in re.finditer(r'<row\b[^>]*>.*?</row>',symbol_patch['proposed_xml'],re.S) if '<entry>'+unused_definition+'</entry>' in m[0])
 symbol_patch['proposed_xml']=symbol_patch['proposed_xml'].replace(unused_row,'')
symbol_patch['capacitance_and_cg_cleanup']='Maintainer authorized removing C_p and C_s if series/parallel capacitance is absent, and CG if no matching text reference exists. Scan found only the glossary entries; the parallel-plate capacitor passage does not cover circuit combinations. CM retained.'
for optical_object in ['image','object']:
 old_definition='distance of an '+optical_object+' from the center of a lens'
 assert symbol_patch['proposed_xml'].count(old_definition)==1
 symbol_patch['proposed_xml']=symbol_patch['proposed_xml'].replace(old_definition,'distance of an '+optical_object+' from the center of a lens or the vertex of a mirror')
symbol_patch['image_distance_followup']='Maintainer requested including mirror usage if present. Both d_i and d_o are used in m67135 Image Formation by Mirrors; distinguish the lens center from the mirror vertex.'
hf_row=next(m[0] for m in re.finditer(r'<row\b[^>]*>.*?</row>',symbol_patch['proposed_xml'],re.S) if '<entry>photon energy</entry>' in m[0])
assert '<m:mtext>hf</m:mtext>' in hf_row
symbol_patch['proposed_xml']=symbol_patch['proposed_xml'].replace(hf_row,'')
symbol_patch['photon_energy_cleanup']='Maintainer requested removing the hf expression from the symbol glossary; retain the E entry for energy of a single photon and the physics treatment elsewhere.'
jpsi_row=next(m[0] for m in re.finditer(r'<row\b[^>]*>.*?</row>',symbol_patch['proposed_xml'],re.S) if 'Joules/psi meson' in m[0])
symbol_patch['proposed_xml']=symbol_patch['proposed_xml'].replace(jpsi_row,'')
symbol_patch['jpsi_cleanup']='Maintainer authorized removal if the associated discovery/November Revolution is not covered. Neither that discussion nor J/psi appears outside this erroneous glossary entry.'
energy_row=next(m[0] for m in re.finditer(r'<row\b[^>]*>.*?</row>',symbol_patch['proposed_xml'],re.S) if '<entry>mechanical energy</entry>' in m[0])
energy_new=re.sub(r'<m:math\b[^>]*>.*?</m:math>','<m:math><m:mtext>KE</m:mtext><m:mo>+</m:mo><m:mtext>PE</m:mtext></m:math>',energy_row,flags=re.S)
symbol_patch['proposed_xml']=symbol_patch['proposed_xml'].replace(energy_row,energy_new)
latent_row=next(m[0] for m in re.finditer(r'<row\b[^>]*>.*?</row>',symbol_patch['proposed_xml'],re.S) if 'latent heat coefficients' in m[0])
symbol_patch['proposed_xml']=symbol_patch['proposed_xml'].replace(latent_row,'')
for phase_change in ['fusion','sublimation','vaporization']:
 old_label='<entry>heat of '+phase_change+'</entry>'
 assert symbol_patch['proposed_xml'].count(old_label)==1
 symbol_patch['proposed_xml']=symbol_patch['proposed_xml'].replace(old_label,'<entry>latent heat of '+phase_change+'</entry>')
symbol_patch['energy_and_latent_heat_cleanup']='Maintainer requested saving the KE+PE alignment repair, removing the duplicate L_f and L_v row, and naming all three phase-change entries latent heats.'
for unit_definition in ['newton-meter (work-energy unit)','newtons times meters (SI unit of torque)']:
 unit_row=next(m[0] for m in re.finditer(r'<row\b[^>]*>.*?</row>',symbol_patch['proposed_xml'],re.S) if '<entry>'+unit_definition+'</entry>' in m[0])
 unit_new=re.sub(r'<m:math\b[^>]*>.*?</m:math>','<m:math><m:mtext>N</m:mtext><m:mo>⋅</m:mo><m:mtext>m</m:mtext></m:math>',unit_row,flags=re.S)
 symbol_patch['proposed_xml']=symbol_patch['proposed_xml'].replace(unit_row,unit_new)
symbol_patch['newton_meter_layout']='Maintainer requested the same leading-space repair for both N dot m entries; simplify MathML wrappers and retain upright unit symbols and both definitions.'
for unused_definition in ['other energy','atmospheric pressure']:
 unused_row=next(m[0] for m in re.finditer(r'<row\b[^>]*>.*?</row>',symbol_patch['proposed_xml'],re.S) if '<entry>'+unused_definition+'</entry>' in m[0])
 symbol_patch['proposed_xml']=symbol_patch['proposed_xml'].replace(unused_row,'')
electron_row=next(m[0] for m in re.finditer(r'<row\b[^>]*>.*?</row>',symbol_patch['proposed_xml'],re.S) if '<entry>electron charge</entry>' in m[0])
electron_new=re.sub(r'<m:math\b[^>]*>.*?</m:math>','<m:math><m:msub><m:mi>q</m:mi><m:mi mathvariant="normal">e</m:mi></m:msub></m:math>',electron_row,flags=re.S)
symbol_patch['proposed_xml']=symbol_patch['proposed_xml'].replace(electron_row,electron_new)
symbol_patch['pressure_and_charge_cleanup']='Maintainer approved deleting unused OE and the broader duplicate P_atm entry. Electron/proton charge symbols are used in m67805 charge-to-mass ratios (q_e also in m52381); retain them and repair the electron entry’s missing e subscript.'
resultant_row=next(m[0] for m in re.finditer(r'<row\b[^>]*>.*?</row>',symbol_patch['proposed_xml'],re.S) if '<entry>resultant or total displacement</entry>' in m[0])
resultant_new=re.sub(r'<m:math\b[^>]*>.*?</m:math>','<m:math><m:mi mathvariant="bold">R</m:mi></m:math>',resultant_row,flags=re.S)
symbol_patch['proposed_xml']=symbol_patch['proposed_xml'].replace(resultant_row,resultant_new)
symbol_patch['resultant_vector_cleanup']='Maintainer identified missing boldface in the resultant-displacement entry; use upright bold R, consistent with the existing vector convention.'
assert symbol_patch['proposed_xml'].count('<entry>perpendicular lever arm</entry>')==1
symbol_patch['proposed_xml']=symbol_patch['proposed_xml'].replace('<entry>perpendicular lever arm</entry>','<entry>lever arm: perpendicular distance from the pivot to the force’s line of action</entry>')
symbol_patch['lever_arm_cleanup']='Maintainer approved the explicit geometric definition for r_perp.'
schwarzschild_row=next(m[0] for m in re.finditer(r'<row\b[^>]*>.*?</row>',symbol_patch['proposed_xml'],re.S) if 'Schwarzschild radius' in m[0])
symbol_patch['proposed_xml']=symbol_patch['proposed_xml'].replace(schwarzschild_row,'')
symbol_patch['schwarzschild_cleanup']='Maintainer approved removing R_s: Schwarzschild radius appears only in the symbol glossary.'
removals=json.loads((ROOT/'proposals/1.1/symbol-glossary-removals.json').read_text(encoding='utf-8'))
glossary_rows=list(re.finditer(r'<row\b[^>]*>.*?</row>',symbol_patch['proposed_xml'],re.S))
assert len(glossary_rows)==332, 'Reconcile approved glossary snapshot before changing its row references.'
for removal in removals['entries']:
 row_xml=glossary_rows[removal['row']][0]
 cells=list(parse(row_xml))
 for parent in cells[1].iter():
  for child in list(parent):
   if child.tag=='{'+M+'}annotation':parent.remove(child)
 definition=' '.join(''.join(cells[1].itertext()).split())
 assert definition==removal['definition'], (removal,definition)
 assert symbol_patch['proposed_xml'].count(row_xml)==1
 symbol_patch['proposed_xml']=symbol_patch['proposed_xml'].replace(row_xml,'')
assert len(re.findall(r'<row\b',symbol_patch['proposed_xml']))==263
symbol_patch['approved_audit_removals']=removals
packet=dict(date='2026-09-22',status='Batch proposals ready for maintainer review; no canonical content changed.',scope='Six conceptual leads plus a completed Carnot/reversibility scan, grouped into ten review items. Related summary/glossary statements included. Not a full-book physics or numerical certification.',items=items,dispositions=verified)
(ROOT/'proposals/1.1/priority3-conceptual-review.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
# Reuse the textbook renderer so comparison MathML and cross-reference labels match the book.
sys.path.insert(0,str(ROOT/'prototype'));sys.argv=['build.py','course','--all'];ns={'__file__':str(ROOT/'prototype/build.py'),'__name__':'review_renderer'}
s= (ROOT/'prototype/build.py').read_text(encoding='utf-8');exec(compile(s.split('OUT.mkdir(parents=True,exist_ok=True);')[0],ns['__file__'],'exec'),ns)
def render(mid,xml):
 if not xml:return '<p><em>Removed duplicate equation.</em></p>'
 s=ns['Renderer'](mid).render(parse(xml));s=re.sub(r'\s+id="[^"]*"','',s)
 slug=ns['registry'][mid]['candidate_slug'];base='/course-full/sections/'+slug+'/index.html'
 s=re.sub(r'href="#([^"]+)"',lambda m:'href="'+base+'#'+m[1]+'"',s)
 s=s.replace('href="../','href="/course-full/sections/')
 return s
esc=html.escape
page=['<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Priority 3 conceptual review</title><style>body{max-width:1250px;margin:auto;padding:24px;font:18px/1.55 Georgia;color:#233c43}a{color:#075e76;overflow-wrap:anywhere}section{border-top:1px solid #abc;padding-top:16px;margin-top:32px}.compare{display:grid;grid-template-columns:1fr 1fr;gap:20px}.cell{min-width:0;background:#f2f6f7;padding:16px;overflow:auto}.note{background:#fff3d6;padding:14px}math{font-size:1.05em} @media(max-width:750px){.compare{grid-template-columns:1fr}}h3{font-size:1.05em}</style><h1>Priority 3: conceptual physics</h1><p>Proposed corrections only; none applied. Ten review groups cover the six leads, their connected summaries/glossaries, and the Carnot/reversibility review. The pressure-work note and entropy passages deserve the closest read.</p><div class="note" id="review-resume"><strong>P3-08 A–G approved. <a href="../priority3-sections/">Read all affected sections in context</a>.</strong> Whole-section flow review and P3-09 (SR) remain. After thermodynamics and P3-09 (SR), review these additional topics:<ul><li><strong>Entropy/disorder pedagogy:</strong> examine the disorder and macrostate treatment before deciding whether any broader revision should wait.</li><li><strong>Electrical safety and historical/technology claims:</strong> investigate the recorded leads and present findings; these are pending review, not automatically deferred.</li></ul>The affected whole-section preview/read-through remains planned. Any renewed deferral is for the maintainer to decide.</div><ul>']
for i in items:page.append('<li><a href="#'+i['id']+'">'+i['id']+' — '+esc(i['title'])+'</a></li>')
page.append('</ul>')
for i in items:
 page.append('<section id="'+i['id']+'"><h2>'+i['id']+' — '+esc(i['title'])+'</h2><p class="note">'+esc(i['attention'])+'</p><p>'+esc(i['reason'])+'</p>')
 seen_groups=set()
 for p in i['passages']:
  if p.get('review_label'):
   group=p['review_label'].split('.')[0]
   anchor=' id="'+i['id']+'-'+group+'"' if group not in seen_groups else ''
   seen_groups.add(group)
   page.append('<h3'+anchor+'>'+esc(p['review_label'])+'</h3><p>'+esc(p['review_reason'])+'</p>')
  mid=p['module'];slug=ns['registry'][mid]['candidate_slug'];link='/course-full/sections/'+slug+'/index.html#'+mid+'--'+p['source_id'].encode().hex()
  context=''.join(render(mid,x) for x in p.get('context_after_xml',[]))
  anchor=(' id="'+esc(p['review_anchor'])+'"') if p.get('review_anchor') else ''
  page.append('<p'+anchor+'><a href="'+link+'">'+esc(ns['registry'][mid]['title'])+' — current context</a></p><div class="compare"><div class="cell"><h3>Before</h3>'+render(mid,p['before_xml'])+context+'</div><div class="cell"><h3>Proposed for 1.1</h3>'+render(mid,p['proposed_xml'])+''.join(render(mid,x) for x in p.get('proposed_following_xml',[]))+context+'</div></div>')
 if i.get('dispositions'):
  page.append('<h3>Scan dispositions</h3>')
  for d in i['dispositions']:page.append('<p><strong>'+esc(d['topic'])+' — '+esc(d['disposition'])+'</strong>: '+esc(d['reason'])+'</p>')
 page.append('<p>Sources: '+ '; '.join('<a href="'+esc(s['url'])+'">'+esc(s['title'])+'</a> ('+esc(s['locator'])+')' for s in i['sources'])+'</p></section>')
page.append('<section><h2>Other dispositions</h2>')
for v in verified:page.append('<h3>'+esc(v['topic'])+' — '+esc(v['disposition'])+'</h3><p>'+esc(v['reason'])+'</p>')
page.append('</section></html>')
for out in [ROOT/'reports/1.1/priority3-review',ROOT/'prototype/dist/review-1.1/priority3-review']:
 out.mkdir(parents=True,exist_ok=True);(out/'index.html').write_text('\n'.join(page),encoding='utf-8',newline='\n')
print('Prepared',len(items),'review groups and',sum(len(i['passages']) for i in items),'passage comparisons. Maintained source unchanged.')
