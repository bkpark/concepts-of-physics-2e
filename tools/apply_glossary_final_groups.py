"""Apply the remaining maintainer-approved glossary decisions once."""
from pathlib import Path
import re,json,hashlib,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1]
# Reuse only pure helper definitions, never the previous one-time application.
helpers=(R/'tools/apply_glossary_quality_batch.py').read_text(encoding='utf-8').split('\ndefs={')[0]
exec(compile(helpers,'glossary_helpers','exec'))
def spans(s,exclude=()):
 return ''.join(f'<span id="{i}"/>' for i in re.findall(r'(?<![-\w])id="([^"]+)"',s) if i not in exclude)
groups=[5,17,27,29,33,34,36,39,42,46,47,49,51]
report=(R/'reports/1.1/glossary-wording-decisions.md').read_text(encoding='utf-8')
audit=json.loads((R/'reports/1.1/glossary-quality-review.json').read_text(encoding='utf-8'))['groups']
wanted={t for g in audit if int(g['id'][1:]) in groups for t in g['terms']}
removed={'statistical analysis','TV','laser printer','ink-jet printer','simple circuit'}
previously_removed={'hydrogen spectrum wavelengths'}
proposed=dict(re.findall(r'^(?:> |- )\*\*([^*]+):\*\* (.+)$',report,re.M))
for t in sorted(wanted-removed-previously_removed):
 assert t in proposed,t
 definition(t,proposed[t])

def para(mod,pid,text):
 """Keep all old anchors; reuse applicable term markup in replacement prose."""
 p=get(mod);m=re.search(r'(<para\b[^>]*id="'+re.escape(pid)+r'"[^>]*>)(.*?)(</para>)',texts[p],re.S);assert m,pid
 inner=m.group(2)
 for term in re.finditer(r'<term\b([^>]*)>([^<]+)</term>',inner):
  label=term.group(2)
  match=re.search(r'(?<![\w>])'+re.escape(label)+r'(?!\w)',text,re.I)
  if match:text=text[:match.start()]+'<term'+term.group(1)+'>'+match.group()+'</term>'+text[match.end():]
 used=set(re.findall(r'(?<![-\w])id="([^"]+)"',text))
 texts[p]=texts[p][:m.start(2)]+spans(inner,used)+text+texts[p][m.end(2):]
def transform_para(mod,pid,fn):
 p=get(mod);m=re.search(r'<para\b[^>]*id="'+re.escape(pid)+r'"[^>]*>.*?</para>',texts[p],re.S);assert m,pid
 old=m.group();new=fn(old);assert new!=old,pid;texts[p]=texts[p].replace(old,new)
def math(s):return '<m:math><m:mrow>'+s+'</m:mrow></m:math>'
def family(symbol):return math('<m:msub><m:mi>L</m:mi><m:mi mathvariant="italic">'+symbol+'</m:mi></m:msub>')

# G05: canonical field-magnitude definitions at their actual introductions.
for term,mod,pid,anchor,sentence in [
 ('electric field strength','m52385','canonical-electric-field-introduction','canonical-electric-field-strength','The electric field strength is the magnitude of the electric field, equal to the electric force per unit positive test charge.'),
 ('magnetic field strength','m52414',None,'canonical-magnetic-field-strength','The magnetic field strength is the magnitude B of the magnetic field, measured in teslas.')]:
 p=get(mod)
 sentence=sentence.replace(term,'<term id="'+anchor+'">'+term+'</term>',1)
 new='<para id="'+anchor+'-introduction">'+sentence+'</para>'
 if pid:after_para(mod,pid,new)
 else:
  m=re.search(r'<content\b[^>]*>',texts[p]);assert m;texts[p]=texts[p][:m.end()]+new+texts[p][m.end():]
 move(term,mod,anchor,proposed[term])

# G17: the example already specifies force perpendicular to radius.
para('m71593','import-auto-id1940935','The turning effect of a force is called torque. Its magnitude is the force multiplied by its lever arm: the perpendicular distance from the axis of rotation to the force’s line of action. A larger lever arm gives a larger torque for the same force. For example, a lighter child on a seesaw can balance a heavier child by sitting farther from the pivot. In the circular-motion example considered here, the force is tangent to the circle, so its lever arm equals the radius '+math('<m:mi>r</m:mi>')+' and the torque magnitude is '+math('<m:mi>τ</m:mi><m:mo>=</m:mo><m:mi>r</m:mi><m:mi>F</m:mi>')+'. Multiplying both sides of the preceding force equation by '+math('<m:mi>r</m:mi>')+' therefore gives the torque on the left-hand side.')

# G27: preserve decay examples and their MathML; qualify family conservation.
transform_para('m42674','import-auto-id1169738014897',lambda s:s.replace('The leptons fall into three families, implying three conservation laws for three quantum numbers.','Leptons occur in electron, muon, and tau families. For each family, assign +1 to its charged lepton and neutrino, −1 to their antiparticles, and zero to other particles. Adding these values gives the corresponding family number, '+family('e')+', '+family('μ')+', or '+family('τ')+'. The decay reactions considered here conserve each family number: the total before the reaction equals the total afterward.').replace(' is conserved. Thus,',' is conserved in these beta-decay reactions. Thus,').replace('electron’s neutrino','electron neutrino').replace('antielectron’s neutrino','electron antineutrino'))
para('m42674','import-auto-id1169737931662','which illustrates the muon family and its associated muon family number '+family('μ')+'. The muon neutrino in this decay balances the muon family number carried by the initial muon, so the total is the same before and after the decay.')
para('m42674','eip-328','These family numbers are useful for analyzing the decay reactions shown here. However, they are not universally conserved: neutrino oscillations change the flavor composition of a neutrino as it propagates.')
# Explicitly qualify earlier beta-decay discussion where it claims conservation.
p=get('m76603')
for m in list(re.finditer(r'<para\b[^>]*>.*?</para>',texts[p],re.S)):
 if 'family number' in m.group() and 'is conserved' in m.group():
  texts[p]=texts[p].replace(m.group(),m.group().replace('is conserved','is conserved in these beta-decay reactions'))

# G29: retain approved Standard Model / Higgs passages; repair speculative claims.
para('m42680','import-auto-id1169737756666','Electroweak theory and quantum chromodynamics are established parts of the Standard Model. Grand unified theories and superstring theories explore further unification that has not yet been experimentally established. Grand unified theories connect the strong and electroweak interactions at much higher energies; superstring theories pursue a broader framework that can also include gravity. Specific energy and length scales depend on the model.')
para('m42680','import-auto-id1169738052783','Grand unified theories propose a common framework for the strong and electroweak interactions at energies far beyond those reached by current accelerators. Their characteristic energy and length scales depend on the model. Superstring theory pursues a broader framework in which fundamental particles correspond to different vibrational states of strings and which incorporates supersymmetry. Such frameworks can also include gravity.')
transform_para('m42680','import-auto-id1169738072300',lambda s:s.replace('The search for a correct theory linking the forces, called the','The search for a theory linking the strong and electroweak interactions, called a'))
transform_para('m42680','import-auto-id1169737041485',lambda s:s.replace('forces would have been unified and may have left their fingerprint','proposed unification processes might have left their fingerprint'))
transform_para('m42680','fs-id1169736659526',lambda s:s.replace('If a GUT is proven, and the four forces are unified,','If a deeper theory successfully unifies all four forces,'))

# G33: definitions, reaction context and neutron balance, without safety aside.
para('m52479','import-auto-id2438390','Neutron capture can convert fertile material, such as uranium-238, into fissile material, such as plutonium-239. This production of new fissile material is called breeding. The following reaction sequence shows how uranium-238 can be converted into plutonium-239 in a reactor.')
para('m52479','import-auto-id1574891','Some plutonium-239 is produced when uranium-238 in reactor fuel captures neutrons. A breeder reactor is designed to produce more fissile material than it consumes.')
transform_para('m52479','import-auto-id2671079',lambda s:s.replace('The minimum amount necessary for self-sustained fission of a given nuclide is called its','For a specified composition, shape, density, and surroundings, the minimum mass needed for a self-sustaining chain reaction is called the'))
transform_para('m52479','import-auto-id3356531',lambda s:re.sub(r'To produce large power,.*?Control rods help prevent', 'A chain reaction is critical when, on average, each fission leads to one further fission. Its average rate then remains steady; this condition is called <term id="g33-criticality">criticality</term>. It is subcritical when the rate decreases and supercritical when the rate increases. <term id="g33-supercriticality">Supercriticality</term> means that each generation produces more fissions in the next. Whether a sample sustains a chain reaction depends on neutron production, absorption, and escape. Critical mass therefore depends on composition, shape, density, and surroundings, including neutron moderators and reflectors. Control rods help prevent',s,flags=re.S))
# Preserve any anchors removed from the criticality sentences.
p=get('m52479');old=ET.fromstring(before[p]);now=ET.fromstring(texts[p]);missing={e.get('id') for e in old.iter() if e.get('id')}-{e.get('id') for e in now.iter() if e.get('id')}
if missing:texts[p]=texts[p].replace('<para id="import-auto-id3356531">','<para id="import-auto-id3356531">'+''.join('<span id="'+i+'"/>' for i in sorted(missing)))

# G34: intrinsic spread, consistent wave-packet estimate and worked example.
para('m67804','import-auto-id1601236','A wave function describes a quantum state and is used to calculate probabilities for measurement outcomes. For position measurements, the squared magnitude of the wave function gives a probability density. The phrase “probability wave” refers to this wave-like probability amplitude. The Schrödinger equation describes how the wave function evolves.')
para('m67804','import-auto-id2608660','A quantum state generally does not assign one definite value to every measurable quantity. If we prepare many systems in the same state and measure position, the results have a distribution; measurements of momentum have another distribution. The spreads in position and momentum obey Heisenberg’s uncertainty principle. A state with a very narrow position distribution must have a broad momentum distribution. This restriction is a property of quantum states, not merely a consequence of imperfect instruments or a disturbance caused by measurement. As an illustrative estimate, consider a localized wave packet whose position spread is comparable to its typical wavelength:')
para('m67804','import-auto-id2686072','Such a localized wave packet contains a range of wavelengths and therefore a range of momenta. In this example, its momentum spread is of the same order as the momentum associated with the typical wavelength. Using the de Broglie relation gives the estimate')
para('m67804','import-auto-id1902868','For this family of wave packets, decreasing the position spread increases the momentum spread. Multiplying the two estimates cancels the typical wavelength, giving')
para('m67804','import-auto-id1434022','This illustrative estimate gives a product of spreads of order Planck’s constant. The precise lower bound depends on defining the spreads as standard deviations.')
para('m67804','import-auto-id1285511','With position and momentum spreads defined as standard deviations, quantum mechanics gives the precise lower bound')
para('m67804','import-auto-id1558492','This is the Heisenberg uncertainty principle. The product of the position and momentum spreads cannot be smaller than the bound shown above. Reducing one spread raises the minimum possible value of the other.')
para('m67804','eip-25','An electron localized within an atom has a spread of momenta. A more tightly localized state requires a larger momentum spread. Quantum mechanics therefore describes the electron with a quantum state and its measurement probabilities, rather than a definite planetary orbit.')
transform_para('m67804','import-auto-id966182',lambda s:s.replace('If the position of an electron in an atom is measured to an accuracy of','If an electron in an atom has a position spread of').replace('what is the electron’s uncertainty in velocity?','what is the minimum spread in its velocity?').replace('If the electron has this velocity, what is its kinetic energy in eV?','What kinetic-energy scale corresponds to that velocity spread, in eV?'))
transform_para('m67804','fs-id1516698',lambda s:s.replace('The uncertainty in position is the accuracy of the measurement, or','The uncertainty in position is the specified spread of the electron’s quantum state,'))
para('m67804','fs-id1782120','An atomic size is roughly 0.1 nm, so a position spread of 0.0100 nm describes an electron localized within a small part of an atom. The associated minimum velocity spread corresponds to a kinetic-energy scale of 95.5 eV. This is larger than many atomic transition energies, showing that such tight localization has substantial energetic consequences.')
para('m67804','import-auto-id2054300','Why don’t we notice this restriction in everyday life? Planck’s constant is very small on everyday scales. The minimum position and momentum spreads allowed for a macroscopic object can both be negligible for practical measurements. Classical mechanics then provides an excellent approximation, as expected from the correspondence principle.')
# The maintained section has no energy-time discussion; do not insert an orphan aside.

# G36: operational definitions at existing introduction points.
para('m52325','import-auto-id2712510','Inertia is an object’s resistance to a change in velocity. Mass measures inertia: a larger mass requires a larger net force to produce the same acceleration. Mass is a property of the object; its weight is the gravitational force acting on it. Newton’s first law is often called the law of inertia.')
para('m71407','import-auto-id1644233','Time allows us to describe the order of events and the intervals between them. We measure a time interval by comparing it with a repeating process, such as the oscillations used in a clock.')
after_para('m67539','import-auto-id1233935','<para id="canonical-energy-introduction"><term id="canonical-energy">Energy</term> is a quantity that we use to track physical changes and transfers between systems. Work transfers energy when a force acts through a displacement. Energy can take different forms, but the total energy of an isolated system remains constant.</para>')

# G39: replace relevant sentences, preserving other energy forms in the list.
transform_para('m67037','eip-740',lambda s:re.sub(r'<term id="import-auto-id2771762">Electrical energy</term>.*?Chemical fuel can also produce electrical energy, such as in batteries\.', '<term id="import-auto-id2771762">Electrical energy</term> is associated with electric charges and fields; it can be stored, as in a charged capacitor, or transferred through a circuit. <term id="import-auto-id2094176">Chemical energy</term> is associated with the arrangement and interactions of atoms and electrons. A chemical reaction releases energy when its products have less energy than its reactants; breaking a bond by itself requires energy. Chemical fuel can also produce electrical energy, such as in batteries.',s,flags=re.S))
transform_para('m67037','eip-740',lambda s:re.sub(r'Atoms and molecules inside all objects are in random motion\..*?because it is related to the temperature of the object\.', '<term id="import-auto-id2393416">Thermal energy</term> is associated with the disordered microscopic motion and interactions of matter. It is part of a system’s internal energy, which includes microscopic kinetic and potential energies.',s,flags=re.S))
para('m67125','import-auto-id1169737795608','Internal energy is energy associated with the system’s microscopic constituents and their interactions. It excludes the kinetic energy of the system’s overall motion and the potential energy associated with its position in an external field. Heat and work are ways of transferring energy. Because we cannot track every atom and molecule in a macroscopic system, we use averages and distributions to describe its microscopic energy.')

# G42: thermodynamic introduction, then compatible arrangements, not a disorder definition.
para('m67128','import-auto-id1169738239451','Entropy is a property of a system’s state that helps us describe the direction of spontaneous processes. For reversible heat transfer at a constant absolute temperature, the entropy change is the heat transferred into the system divided by that temperature. The total entropy of an isolated system cannot decrease: it remains constant for an ideal reversible process and increases for an irreversible process.')
para('m67128','import-auto-id1169738248900','The microscopic interpretation of entropy relates it to the number of arrangements compatible with a system’s macroscopic state. For example, when ice melts, its molecules gain access to many more arrangements in the liquid. The entropy increases, as the following example shows. The statistical interpretation is developed in the following section.')
content_replace('m67128','This is a significant increase in entropy accompanying an increase in disorder.','This is a significant increase in entropy accompanying the change from solid to liquid.')
content_replace('m67128','These three results—entropy, unavailability of energy, and disorder—are related in this example.','In this example, the increase in entropy accompanies a decrease in the energy available to do work.')
para('m42238','import-auto-id1169737762485','A macroscopic state can correspond to many microscopic arrangements. Entropy increases with the number of microscopic arrangements compatible with that state. Spontaneous changes overwhelmingly favor macroscopic states compatible with more microscopic arrangements. Counting those arrangements provides a statistical explanation of the second law of thermodynamics.')
para('m42238','import-auto-id1169737927504','For five fair coins, the macrostates with all heads or all tails each have one microstate. Together, they account for only 2 of the 32 equally likely outcomes. The macrostates with three heads and two tails, or two heads and three tails, together have 20 microstates. They are therefore much more likely. Starting with five heads and tossing the coins again is likely to produce a macrostate compatible with more microstates. The reverse remains possible, but is less likely.')
transform_para('m42238','import-auto-id1169737802488',lambda s:s.replace('The most orderly arrangements (most structured) are 100 heads or 100 tails. The least orderly (least structured) is that of 50 heads and 50 tails.','The macrostates with the fewest microstates are 100 heads or 100 tails. The macrostate with the most microstates is 50 heads and 50 tails.').replace('the most orderly arrangement','the all-heads arrangement').replace('the next most orderly arrangement','the arrangement').replace('the least orderly arrangement','the most probable macrostate').replace('an orderly macrostate like 100 heads','a macrostate like 100 heads').replace('a less orderly macrostate','a macrostate with more microstates').replace('the most orderly macrostate','the all-heads or all-tails macrostate').replace('Disorder is highly likely.','Macrostates with more microstates are more likely.'))
transform_para('m42238','import-auto-id1169737882693',lambda s:s.replace('The fantastic growth in the odds favoring disorder','The rapid growth in the odds favoring macrostates with more microstates'))
para('m42238','import-auto-id1169738209745','For a gas in equilibrium, a nearly uniform distribution of molecules throughout the available volume is compatible with far more microscopic arrangements than a state with all molecules confined to one small region. A substantial spontaneous concentration of the molecules is therefore overwhelmingly unlikely. This statistical imbalance explains why an isolated gas expands into available space.')
content_replace('m42238','Disorder is vastly more likely than order.','The expanded macrostate is compatible with vastly more microscopic arrangements.')
content_replace('m42238','The arguments that disorder and high entropy are the most probable states are quite convincing.','Macrostates with more compatible microstates have greater entropy and are more probable.')

# G46: fixed-direction language explicitly belongs to linear polarization.
para('m52456','import-auto-id1169737845771','Polarization describes how the direction of a transverse wave’s oscillation varies. For light, we describe it using the electric field. In linearly polarized light, the electric field oscillates along a fixed direction perpendicular to propagation. This fixed direction is the direction of polarization.')
transform_para('m52456','import-auto-id1169738249505',lambda s:re.sub(r'The Sun and many other light sources.*?all possible directions of polarization\.', 'The Sun and many other sources emit <term id="g46-unpolarized">unpolarized</term> light, which has no persistent preferred polarization direction. Its polarization fluctuates irregularly, so a polarizer transmits only part of its average intensity.',s,flags=re.S))
transform_para('m52456','import-auto-id1169738065983',lambda s:re.sub(r'Another interesting phenomenon.*?Each of the separated rays has a specific polarization\.', 'A <term id="g46-birefringent">birefringent</term> material has different refractive indices for different polarization modes. In suitable directions this can split an incident beam into two beams with different polarizations.',s,flags=re.S))

# G47: historical model scope without repeated modern-QM caveats.
para('m67250','import-auto-id1352686','A blackbody is an ideal absorber of all electromagnetic radiation incident on it. In thermal equilibrium it emits a spectrum determined by its temperature. This blackbody radiation is described by Planck’s law. Real objects can approximate this spectrum, but their emission also depends on their material and surface properties. The historical attempt to explain this spectrum using classical physics predicted too much radiation at short wavelengths. Resolving this problem helped launch quantum mechanics.')
transform_para('m67805','import-auto-id2403541',lambda s:re.sub(r'The planetary model of the atom pictures low-mass electrons orbiting a large-mass nucleus\.', 'The planetary model pictures electrons orbiting a small, massive nucleus. It was an important historical step, but classical orbiting electrons cannot explain stable atoms. Quantum mechanics describes electrons using quantum states rather than definite planetary trajectories.',s))
transform_para('m67807','eip-391',lambda s:s.replace('or the smallest orbital radius','the radius of the lowest-energy electron orbit in the Bohr model of hydrogen,'))
after_para('m67251','import-auto-id1560847','<para id="work-function-minimum-energy">The work function is the minimum energy required to remove an electron from a material’s surface into vacuum.</para>')
after_para('m67139','import-auto-id1827066','<para id="correspondence-classical-limit">Quantum mechanics reproduces classical predictions in the appropriate limit.</para>')

# G49: definitions only; preserve all dated milestones and status prose.
transform_para('m52480','import-auto-id2446715',lambda s:re.sub(r'<term[^>]*>Ignition</term>.*$', 'Ignition refers to conditions in which energy deposited by fusion products sustains the fuel’s heating against its losses. Fusion experiments compare fusion energy output with energy supplied at a specified stage of the experiment. Break-even means that those two quantities are equal; the comparison must state which input is counted. For example, energy delivered to a fusion target is different from the electrical energy used by the whole facility. Neither target-level gain nor ignition by itself establishes that a facility produces net useful electrical energy.</para>',s,flags=re.S))
transform_para('m52480','import-auto-id2603001',lambda s:re.sub(r'This technique is called(.*?)because the fuel’s inertia prevents it from escaping before significant fusion can take place\.',r'This technique is called\1because the fuel’s inertia keeps it dense for a very short time before it expands, allowing fusion reactions to occur during that interval.',s,flags=re.S))

# G51: remove five independent headwords; keep local explanations and anchors.
for t in sorted(removed):
 x=by[t];mod=Path(x['source']).parent.name;p=get(mod);m=re.search(r'<definition\b[^>]*id="'+x['id']+r'"[^>]*>.*?</definition>',texts[p],re.S);assert m,t
 texts[p]=texts[p].replace(m.group(),'');texts[p]=texts[p].replace('</content>','<para>'+spans(m.group())+'</para></content>')
 texts[p]=re.sub(r'<term\b([^>]*)>('+re.escape(t)+r')</term>',lambda m:'<span'+m.group(1)+'>'+m.group(2)+'</span>' if m.group(1).strip() else m.group(2),texts[p],flags=re.I)
 log.append({'term':t,'action':'removed standalone glossary; retained local prose'})
transform_para('m52401','import-auto-id1170614028838',lambda s:s.replace('has a single voltage source and a single resistor.','of the kind considered here contains one voltage source and one resistor.'))

if __name__=='__main__':
 # Restore anchors removed while replacing text fragments; no old URLs disappear.
 for p,s in list(texts.items()):
  old=ET.fromstring(before[p]);new=ET.fromstring(s)
  oldids={e.get('id') for e in old.iter() if e.get('id')};ids=[e.get('id') for e in new.iter() if e.get('id')]
  assert len(ids)==len(set(ids)),('duplicate ID',p)
  missing=oldids-set(ids)
  if missing:s=s.replace('</content>','<para>'+''.join('<span id="'+i+'"/>' for i in sorted(missing))+'</para></content>');texts[p]=s
  new=ET.fromstring(s)
  for tag in ['exercise','equation']:
   assert [e.get('id') for e in old.findall('.//c:content//c:'+tag,NS)]==[e.get('id') for e in new.findall('.//c:content//c:'+tag,NS)],(p,tag)
 changes=[dict(source=p,before_sha256=hashlib.sha256(before[p]).hexdigest(),after_sha256=hashlib.sha256(s.encode('utf-8')).hexdigest(),before=before[p].decode('utf-8'),after=s) for p,s in texts.items() if s.encode('utf-8')!=before[p]]
 q='proposals/maintainer-corrections/GLOSSARY-FINAL-APPROVED-GROUPS.json';assert not (R/q).exists(),'Already applied'
 (R/q).write_text(json.dumps(dict(status='approved',groups=groups,changes=changes),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 for c in changes:(R/c['source']).write_bytes(c['after'].encode('utf-8'))
 p=R/'maintained/editorial-changes.json';j=json.loads(p.read_text(encoding='utf-8'));j['changes'].append(q);p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 (R/'reports/1.1/glossary-final-applied.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 for name in ['next-release-1.1.md','exercise-revision-1.1.md']:
  with (R/'docs'/name).open('a',encoding='utf-8') as f:f.write('\nApplied all remaining approved glossary groups (G05, G17, G27, G29, G33, G34, G36, G39, G42, G46, G47, G49, G51), including five G51 removals. G49 experimental milestones unchanged. Preserved IDs and exercise numbering. Pending preview refresh. Next review: hard-coded chapter/section references before renumbering.\n')
 print(json.dumps({'groups':groups,'modules':len(changes),'definition_actions':len(log)}))
