from pathlib import Path
import re,json,hashlib,xml.etree.ElementTree as E
assert not Path("proposals/maintainer-corrections/SUMMARY-PROSE-CONSISTENCY.json").exists(), "Already applied; see approved proposal. Do not rerun."
changes=[]
completed={'m52420','m42236','m52364','m52368','m42671','m42680','m52480','m67032','m67126','m67125','m67135','m75428'}
baseline=json.loads(Path('prototype/dist/course-full/build-manifest.json').read_text())['source_sha256']
inventory={x['module']:x for x in json.loads(Path('reports/1.1/summary-consistency/inventory.json').read_text(encoding='utf-8'))}
def edit(mid,pairs,custom=None):
 p=Path(f'maintained/modules/{mid}/index.cnxml');before=p.read_bytes();s=before.decode();m=re.search(r'<section\b[^>]*class="section-summary"[^>]*>.*?</section>',s,re.S);assert m,mid
 old=m[0];new=old
 if mid in completed:
  changes.append({'path':p.as_posix(),'before_sha256':baseline[mid],'after_sha256':hashlib.sha256(before).hexdigest(),'before_summary_text':inventory[mid]['summary'],'after':old})
  return
 for a,b in pairs:
  assert new.count(a)==1,(mid,a,new.count(a));new=new.replace(a,b)
 if custom:new=custom(new)
 E.fromstring(s[:m.start()]+new+s[m.end():]);after=(s[:m.start()]+new+s[m.end():]).encode()
 assert {e.get('id') for e in E.fromstring(before).iter() if e.get('id')}=={e.get('id') for e in E.fromstring(after).iter() if e.get('id')}
 p.write_bytes(after);changes.append({'path':p.as_posix(),'before_sha256':hashlib.sha256(before).hexdigest(),'after_sha256':hashlib.sha256(after).hexdigest(),'before':old,'after':new})
def item(s,id,fn):
 pat=r'(<item\b[^>]*id="'+id+r'"[^>]*>)(.*?)(</item>)'
 out,n=re.subn(pat,lambda m:m[1]+fn(m[2])+m[3],s,flags=re.S);assert n==1;return out

def magnet(s):
 s=item(s,'import-auto-id1166991832296',lambda x:x.replace('<m:mi>n</m:mi>','<m:mi>N</m:mi>').replace('"nI"','"NI"'))
 s=item(s,'import-auto-id1166991829458',lambda x:x.replace('<m:mo stretchy="false">=</m:mo><m:mrow><m:mn>4π','<m:mo stretchy="false">≈</m:mo><m:mrow><m:mn>4π').replace('=4π','approx 4π'))
 return item(s,'import-auto-id1166991832290',lambda x:'The Biot-Savart law gives the magnetic-field contribution from each segment of a steady current; adding these contributions gives the total field. Ampere’s law relates the accumulated component of the magnetic field along a closed path to the net current passing through a surface bounded by that path.')
edit('m52420',[],magnet)
edit('m42236',[
('An artifact of the second law of thermodynamics is the ability to heat an interior space using a heat pump. Heat pumps compress cold ambient air and, in so doing, heat it to room temperature without violation of conservation principles.','A heat pump uses work to transfer heat from a colder region to a warmer one. In the system described here, a refrigerant absorbs heat outdoors, is compressed to a higher temperature, and releases heat indoors.'),
('A refrigerator is a heat pump; it takes warm ambient air and expands it to chill it.','A refrigerator uses the same principle to remove heat from its cold interior and release heat to the warmer surroundings.')])
edit('m52364',[
('Temperature is the quantity measured by a thermometer.','Temperature describes a system’s thermal state and is measured by a thermometer in thermal equilibrium with it.'),
('Absolute zero is the temperature at which there is no molecular motion.','Absolute zero, 0 K, is the lower limit of the Kelvin temperature scale.'),
('Thermal equilibrium occurs when two bodies are in contact with each other and can freely exchange energy.','Bodies in thermal equilibrium have no net heat transfer between them.')])
edit('m52368',[
('Kilocalorie is defined to be the energy needed to change the temperature of 1.00&#160;kg of water between','UNEXPECTED')]) if False else None
# Text contains a literal nonbreaking space in the calorie definition.
def heat(s):
 s,n=re.subn(r'Kilocalorie is defined.*?</item>', 'A thermochemical calorie is defined as exactly 4.184 J; a kilocalorie is 1000 calories, or exactly 4184 J.</item>',s,count=1,flags=re.S);assert n==1
 return s.replace('The mechanical equivalent of this heat transfer is','The conversion between kilocalories and joules is')
edit('m52368',[],heat)
edit('m42671',[('Feynman diagrams are graphs of time versus position and are highly useful pictorial representations of particle processes.','Feynman diagrams represent contributions to quantum interaction calculations. Lines represent particles or their propagation, and vertices represent interactions; the lines are not measured trajectories.')])
edit('m42680',[('Unification of the strong force is expected at such high energies that it cannot be directly tested, but it may have observable consequences in the as-yet unobserved decay of the proton and topics to be discussed in the next chapter. Although unification of forces is generally anticipated, much remains to be done to prove its validity.','Further unification remains unconfirmed. Some grand unified theories predict proton decay, with lifetimes and decay modes that depend on the model. Searches have found no convincing evidence of proton decay and constrain these theories.')])
edit('m52480',[
('Ignition is the condition under which controlled fusion is self-sustaining; it has not yet been achieved. Break-even, in which the fusion energy output is as great as the external energy input, has nearly been achieved.','Ignition occurs when energy deposited by fusion products sustains the fuel’s heating against its losses. Break-even compares fusion output with a specified energy input. NIF has achieved ignition and output greater than the laser energy delivered to its target; this does not mean the facility produces net useful electrical energy.'),
('The first method uses magnetic fields and the second method uses the momentum of impinging laser beams for confinement.','Magnetic confinement uses magnetic fields. In laser-driven inertial confinement, expanding hot plasma compresses the fuel, whose inertia keeps it dense briefly before it expands.')])
edit('m67032',[
('All units can be expressed as combinations of four fundamental units.','SI uses seven base units: the meter, kilogram, second, ampere, kelvin, mole, and candela. Units for other quantities are derived from combinations of base units.'),
('The four fundamental units we will use in this text are','Four base units used frequently in this text are'),
('The four fundamental units are abbreviated as follows:','These four base units are abbreviated as follows:')])
edit('m67126',[('However, because of loss of energy owing to the second law of thermodynamics, complete reversibility does not work in practice.','Dissipative processes such as friction make real macroscopic processes irreversible; total energy is still conserved.')])
edit('m67125',[
('is the net heat transfer (the sum of all heat transfer into and out of the system)','is the net heat transferred into the system'),
('is the net work done (the sum of all work done on or by the system)','is the net work done by the system'),
('represents an independent quantity capable of being stored.','represents the change in the system’s stored internal energy.')])
edit('m67135',[('Image length is half the radius of curvature.','For a spherical mirror in the small-angle approximation, focal length is half the radius of curvature.')])
edit('m75428',[('A Faraday cage acts like a shield around an object, preventing electric charge from penetrating inside.','In electrostatic equilibrium, a closed conducting Faraday cage shields an empty cavity from external electric fields.')])
edit('m42356',[
('The voltage drop, or power dissipation, across each individual resistor in a series is different, and their combined total adds up to the power source input.','Series resistors carry the same current. Their voltage drops add to the source voltage, and their power dissipations add to the power supplied by the source. Equal resistors have equal voltage drops and equal power dissipations.'),
('The current flowing through each resistor in a parallel circuit is different, depending on the resistance.','The current through each parallel resistor depends on its resistance; equal resistors carry equal currents.')])
edit('m52443',[('They were predicted by Maxwell, who also showed that','They were predicted by Maxwell.')])
# Restrict the two inherited transition formulas to emission and use the prose convention hf = Ei - Ef.
for mid in ['m67807','m67808']:
 def transition(s):
  pat=r'(<item>Bohr correctly proposed.*?</item>)'
  m=re.search(pat,s,re.S);assert m
  x=m[0].replace('with energy for transitions between orbits given by','with the energy of a photon emitted in a downward transition given by')
  x=x.replace('<m:mi mathvariant="normal">Δ</m:mi><m:mi>E</m:mi><m:mo stretchy="false">=</m:mo>','',1).replace('ΔE= ital','ital',1)
  x,n=re.subn(r'where <m:math.*?</m:math> is the change in energy between the initial and final orbits and ', 'where ',x,count=1,flags=re.S);assert n==1
  x=x.replace('is the energy of an absorbed or emitted photon.','is the emitted photon’s energy, equal to the initial atomic energy minus the final atomic energy.')
  return s[:m.start()]+x+s[m.end():]
 edit(mid,[],transition)
edit('m76603',[('an electron’s neutrino','an electron neutrino'),('an electron’s antineutrino','an electron antineutrino')])
edit('m71593',[('The farther the force is applied from the pivot, the greater is the angular acceleration; angular acceleration is inversely proportional to mass.','For the same rotational inertia, a greater net torque produces a greater angular acceleration. For the same net torque, a greater rotational inertia produces a smaller angular acceleration.'),('The torque applied on an object is given by lever arm times the applied force:','The torque magnitude is the force magnitude times the perpendicular lever arm. For the tangential force considered here, the lever arm equals the radius:')])
proposal='proposals/maintainer-corrections/SUMMARY-PROSE-CONSISTENCY.json'
Path(proposal).write_text(json.dumps({'id':'SUMMARY-PROSE-CONSISTENCY','status':'approved','description':'Align section summaries with the maintained prose, preserving source IDs and summary equation anchors.','changes':changes},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
r=Path('maintained/editorial-changes.json');d=json.loads(r.read_text());d['changes'].append(proposal);r.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('Updated',len(changes),'modules; XML and IDs verified.')
