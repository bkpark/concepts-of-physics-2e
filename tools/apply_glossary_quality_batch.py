"""One-time approved glossary corrections. Run only against pre-batch source."""
from pathlib import Path
import json, re, hashlib, html, xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1]
NS={'c':'http://cnx.rice.edu/cnxml'}
inv=json.loads((R/'reports/1.1/glossary-current-inventory.json').read_text(encoding='utf-8'))
by={x['term']:x for x in inv}
before={}; texts={}; log=[]
def get(mod):
 p=f'maintained/modules/{mod}/index.cnxml'
 if p not in texts:
  before[p]=(R/p).read_bytes(); texts[p]=before[p].decode('utf-8')
 return p
def rep(mod,old,new,count=1):
 p=get(mod); assert texts[p].count(old)==count,(mod,old[:100],texts[p].count(old))
 texts[p]=texts[p].replace(old,new)
def spans(s,exclude=()):
 return ''.join(f'<span id="{i}"/>' for i in re.findall(r'\bid="([^"]+)"',s) if i not in exclude)
def definition(term,wording):
 x=by[term];mod=Path(x['source']).parent.name;p=get(mod)
 m=re.search(r'<definition\b[^>]*id="'+re.escape(x['id'])+r'"[^>]*>.*?</definition>',texts[p],re.S);assert m,term
 old=m.group(); mm=re.search(r'(<meaning\b[^>]*>)(.*?)(</meaning>)',old,re.S);assert mm
 new=old[:mm.start(2)]+spans(mm.group(2))+wording+old[mm.end(2):]
 texts[p]=texts[p].replace(old,new);log.append({'term':term,'source':p,'definition':wording})
def content_replace(mod,old,new):
 p=get(mod);end=texts[p].index('</content>');a,b=texts[p][:end],texts[p][end:]
 assert old in a,(mod,old[:100]);texts[p]=a.replace(old,new)+b
def after_para(mod,pid,new):
 p=get(mod);m=re.search(r'<para\b[^>]*id="'+pid+r'"[^>]*>.*?</para>',texts[p],re.S);assert m,pid
 texts[p]=texts[p][:m.end()]+new+texts[p][m.end():]
def replace_para(mod,pid,new):
 p=get(mod);m=re.search(r'(<para\b[^>]*id="'+pid+r'"[^>]*>)(.*?)(</para>)',texts[p],re.S);assert m,pid
 texts[p]=texts[p][:m.start(2)]+spans(m.group(2))+new+texts[p][m.end(2):]
def canonical(term,mod):
 p=get(mod);root=ET.fromstring(texts[p]);
 for t in root.findall('.//c:content//c:term',NS):
  if ''.join(t.itertext()).casefold() in [term.casefold(),term.casefold()+'s'] and t.get('id'):return t.get('id')
 raise AssertionError(('no canonical anchor',term,mod))
def alias(term,destmod,target):
 x=by[term];mod=Path(x['source']).parent.name;p=get(mod)
 m=re.search(r'<definition\b[^>]*id="'+x['id']+r'"[^>]*>.*?</definition>',texts[p],re.S);assert m,term
 old=m.group();texts[p]=texts[p].replace(old,'')
 anchorpara='<para>'+spans(old)+f'For the definition of <link document="{destmod}" target-id="{target}">{html.escape(term)}</link>, see its introduction.</para>'
 texts[p]=texts[p].replace('</content>',anchorpara+'</content>')
 # Keep existing source anchors on cross-references instead of bold terms.
 texts[p]=re.sub(r'<term\b([^>]*)>('+re.escape(term)+r')</term>',lambda m:f'<link{m.group(1)} document="{destmod}" target-id="{target}">{m.group(2)}</link>',texts[p],flags=re.I)
 log.append({'term':term,'action':'consolidated','target':destmod+'#'+target})
def move(term,destmod,anchor,wording):
 x=by[term];src=Path(x['source']).parent.name;p=get(src)
 definition(term,wording)
 m=re.search(r'<definition\b[^>]*id="'+x['id']+r'"[^>]*>.*?</definition>',texts[p],re.S);old=m.group()
 # New IDs for destination glossary; retain old IDs as source cross-reference anchors.
 new=re.sub(r'\bid="[^"]+"','',old)
 alias(term,destmod,anchor)
 dp=get(destmod);texts[dp]=texts[dp].replace('</glossary>',new+'</glossary>')

defs={
'resonance':'enhanced oscillation of a system driven periodically at a frequency near one of its natural frequencies',
'electric current':'the rate of flow of electric charge through a surface or past a point',
'potential difference (or voltage)':'the change in electric potential energy per unit charge between two points; measured in volts (joules per coulomb)',
'proton':'a positively charged particle found in atomic nuclei; its charge is equal in magnitude to the electron’s charge',
'activity':'the expected number of radioactive decays per unit time in a sample; also called decay rate',
'normal force':'the component of a contact force perpendicular to the surface of contact',
'voltage drop':'a decrease in electric potential across a circuit component, corresponding to a decrease in electric potential energy per unit positive charge',
'Joule’s law':'the rate of conversion of electrical energy into thermal energy in a resistor: power equals the square of the current times the resistance',
'Faraday cage':'a conducting enclosure that shields its interior from external electrostatic fields',
'electrostatic equilibrium':'a steady distribution of charge with no net macroscopic flow of charge',
'superposition':'the addition of individual wave disturbances to obtain the resulting disturbance where waves overlap, for waves obeying the superposition principle',
'overtones':'frequencies of vibration above the fundamental frequency; when they are integer multiples of the fundamental, they are also harmonics',
'constructive interference':'reinforcement where overlapping wave disturbances add in the same direction',
'destructive interference':'partial or complete cancellation where overlapping wave disturbances have opposite directions',
'SI units':'units of the International System of Units, including base units such as the metre, kilogram, and second, and derived units such as the newton and joule',
'fundamental units':'base units chosen for a system of quantities; other units are formed from combinations of these units',
'metric system':'a system of measurement using decimal multiples and submultiples of units; SI is its modern international form',
'atomic mass':'the mass of an atom, including the effects of the binding of its constituents; it is less than the sum of the masses of its separated protons, neutrons, and electrons',
'nuclear reaction energy':'the energy released or required in a nuclear reaction, determined by the difference between the total initial and final rest energies',
'hadrons':'composite particles whose constituents are bound by the strong interaction',
'leptons':'elementary particles that do not participate in the strong interaction, including electrons, muons, taus, neutrinos, and their antiparticles',
'positron':'the antiparticle of the electron, with the same mass and a positive electric charge; also called an antielectron',
'electron neutrino':'the electrically neutral lepton of electron flavor, associated with the electron in weak interactions',
'neutrino':'an electrically neutral elementary lepton that participates in the weak interaction; neutrinos occur in electron, muon, and tau flavors',
'antielectron':'another name for the positron, the electron’s antiparticle',
'beta ray':'an electron or positron emitted in nuclear beta decay',
'radioactivity':'spontaneous transformation of an unstable nucleus into a different nucleus or a lower-energy nuclear state',
'decay':'a spontaneous transformation of an unstable particle or nucleus; nuclear decay produces a different nucleus or a lower-energy nuclear state',
'gamma decay':'a nuclear transition to a lower-energy state by emission of a gamma-ray photon, without changing the numbers of protons or neutrons',
'scintillators':'materials that emit brief flashes of light when they absorb energy from ionizing radiation',
'Geiger tube':'a gas-filled radiation detector in which ionizing radiation triggers an electrical discharge that can be registered as a count',
'radiation detector':'a device that registers radiation through its interaction with matter',
'time dilation':'the greater time interval measured in an inertial frame between ticks of a clock moving relative to that frame, compared with the interval measured by that clock',
'proper time':'the time interval measured by a clock present at both events; for an inertial clock, the events occur at the same position in its rest frame',
'relativistic Doppler effects':'changes in the observed frequency and wavelength of light due to relative motion of the source and observer, including time dilation; recession produces a redshift and approach a blueshift for motion along the line of sight',
'distance':'a nonnegative measure of separation or path length; the distance between two positions is their straight-line separation, whereas distance traveled is the total path length',
'range':'the horizontal distance traveled by a projectile from launch to landing',
'trajectory':'the path followed by a moving object',
'motion':'a change in an object’s position over time relative to a chosen reference frame',
'centripetal acceleration':'the inward component of acceleration for motion along a curved path; for uniform circular motion, it is the entire acceleration',
'centripetal force':'the inward component of the net force responsible for the curvature of an object’s path; for uniform circular motion, it is the entire net force',
'deformation':'a change in an object’s shape or size',
'restoring force':'a force directed toward a stable equilibrium position when a system is displaced from it',
'spring constant':'a measure of a spring’s stiffness: the ratio of restoring-force magnitude to displacement within the range where Hooke’s law applies',
'static friction':'a contact force parallel to a surface that opposes the tendency of surfaces to slip relative to one another while they remain at rest relative to each other',
'pressure':'normal force per unit area on a surface',
'buoyant force':'the net upward force due to the pressure of a fluid at rest on an immersed object',
'Bernoulli’s equation':'the conservation-of-energy relation along a streamline for steady flow of an incompressible fluid with negligible viscosity: the sum of pressure, kinetic energy per unit volume, and gravitational potential energy per unit volume is constant',
'Bernoulli’s principle':'for steady, incompressible flow with negligible viscosity along a streamline at constant height, pressure is lower where speed is higher',
'heat of sublimation':'the energy per unit mass required to change a substance directly from solid to vapor at specified conditions',
'latent heat coefficient':'the energy transferred per unit mass during a specified phase transition at given temperature and pressure',
'specific heat':'the heat transferred per unit mass per unit temperature change, without a phase change and under specified conditions such as constant pressure or constant volume',
'isobaric process':'a thermodynamic process that occurs at constant pressure',
'reversible process':'an ideal process that can be reversed so that both the system and its surroundings return to their original states',
'field':'a physical quantity assigned to each point in space, and possibly time; a vector field also assigns a direction',
'point charge':'an idealized electric charge concentrated at a point; a useful model when the charged object’s size is negligible for the problem',
'test charge':'a small charge used to probe an electric field, small enough that its effect on the source charges can be neglected',
'electric charge':'a property of matter that determines its electric interactions; charge can be positive or negative',
'law of conservation of charge':'the total electric charge of an isolated system remains constant',
'electron':'an elementary particle with negative electric charge; electrons are constituents of atoms and can also exist freely',
'Curie temperature':'the temperature above which a ferromagnetic material loses its spontaneous magnetization; it can still respond to an applied magnetic field',
'permeability of free space':'the magnetic constant relating currents and magnetic fields in vacuum; approximately 4π × 10<sup>−7</sup> T·m/A',
'Lenz’s law':'an induced current flows in a direction whose magnetic field opposes the change in magnetic flux that induces it',
'AC voltage':'a voltage that periodically reverses polarity; a sinusoidal voltage is a common example',
'AC current':'an electric current that periodically reverses direction; a sinusoidal current is a common example',
'dispersion':'the dependence of a wave’s propagation speed in a medium on frequency; for light, it can cause different colors to refract through different angles',
'focal point':'the point where rays initially parallel to the principal axis converge, or from which they appear to diverge, in the ideal lens or mirror approximation',
'focal length':'the signed distance from the center of a thin lens, or the vertex of a mirror, to its principal focal point',
'converging lens':'a lens that brings rays parallel to its principal axis toward a focus; a convex lens in air is a common example',
'diverging lens':'a lens that causes rays parallel to its principal axis to spread out as if from a focal point; a concave lens in air is a common example',
'converging mirror':'a concave mirror that brings rays close and parallel to its principal axis toward a focus',
'real image':'an image formed where light rays from each object point actually converge; it can be recorded on a screen placed there',
'virtual image':'an image at the apparent origin of diverging rays; the rays do not actually converge at the image location',
'decay constant':'the probability per unit time that an undecayed nucleus will decay; the constant determining the exponential decay rate',
'curie':'a unit of activity equal to exactly 3.7 × 10<sup>10</sup> becquerels (decays per second), originally based on the activity of one gram of radium-226',
'radiopharmaceutical':'a preparation containing a radionuclide and used for medical diagnosis or treatment',
'fission fragments':'the daughter nuclei produced when a heavy nucleus undergoes fission',
'liquid drop model':'a model that treats a nucleus as a drop of nuclear matter to describe collective properties such as binding and deformation',
'nucleons':'protons and neutrons, the constituents of atomic nuclei',
'neutron':'an electrically neutral particle found in atomic nuclei; a free neutron is unstable and undergoes beta decay',
'baryon number':'a quantum number equal to +1 for baryons, −1 for antibaryons, and zero for mesons and leptons; in the quark model, one third of the number of quarks minus antiquarks',
'conservation of total baryon number':'the rule that total baryon number remains unchanged in a reaction or decay; no violation has been observed',
}
for t,w in defs.items():definition(t,w)

# Placement and aliases; existing conceptual introductions supply the anchors.
for mod,term,anchor in [('m71584','hertz','canonical-hertz'),('m71588','standing wave','canonical-standing-wave')]:
 p=get(mod)
 match=re.search(r'<term([^>]*)>'+term+r's?</term>',texts[p],re.I)
 if match:
  if 'id=' in match.group(1):anchor=re.search('id="([^"]+)"',match.group(1)).group(1)
  else:texts[p]=texts[p].replace(match.group(0),match.group(0).replace('<term','<term id="'+anchor+'"',1),1)
 else:
  # A brief formal definition adjacent to the existing discussion.
  prose={'hertz':'The <term id="canonical-hertz">hertz</term> (Hz) is the SI unit of frequency: one cycle per second.','standing wave':'A <term id="canonical-standing-wave">standing wave</term> is a wave pattern with fixed nodes and antinodes, produced by interference of waves traveling in opposite directions.'}[term]
  texts[p]=texts[p].replace('</content>','<para>'+prose+'</para></content>')
 move(term,mod,anchor,{'hertz':'the SI unit of frequency, equal to one cycle per second','standing wave':'a wave pattern with fixed nodes and antinodes, produced by interference of waves traveling in opposite directions'}[term])
res=canonical('resonance','m71586')
alias('resonant','m71586',res);alias('resonate','m71586',res)
alias('current','m67130',canonical('electric current','m67130'))
# Potential difference is marked separately from its parenthetical glossary name.
alias('voltage','m75427',canonical('potential difference','m75427'))
alias('protons','m52381',canonical('proton','m52381'))
alias('second law of motion','m67530',canonical('Newton’s second law of motion','m67530'))
alias('rate of decay','m52471',canonical('activity','m52471'))

# Short consistency corrections at the actual introductions.
content_replace('m71586','the ball’s oscillations increase in amplitude with each oscillation for as long as you drive it.','the ball’s oscillations grow until energy supplied by the driving force balances energy lost through damping.')
content_replace('m71586','The phenomenon of driving a system with a frequency equal to its natural frequency is called','The enhanced response when a system is driven near a natural frequency is called')
content_replace('m71582','The net external force equals the change in momentum of a system divided by the time over which it changes.','The average net external force equals the change in momentum of a system divided by the time interval. For an instantaneous force, the corresponding relation uses the instantaneous rate of change of momentum.')
content_replace('m68329','If the force supporting a load is perpendicular to the surface of contact between the load and its support, this force is called a','The component of a contact force perpendicular to the surface of contact is called a')
content_replace('m42356','the loss of electrical power, called a','the decrease in electric potential, called a')
content_replace('m42356','to use <term id="import-auto-id2017186">Joule’s law</term>,','to use the electrical power relation<span id="import-auto-id2017186"/>,')
content_replace('m42356','into Joule’s law,','into this relation,')
after_para('m42356','fs-id2670805','<para id="joule-law-resistive-heating">For a resistor, these relations give <term id="canonical-joule-law">Joule’s law</term>: the heating power is the square of the current times the resistance.</para>')
content_replace('m75428','All electrical charges will reside on the outside surface of this shield, and there will be no electrical field inside.','In electrostatic equilibrium, a closed conducting shield protects an empty cavity from external electric fields. With no charge inside the cavity, excess charge resides on the shield’s outer surface and the field in the cavity is zero.')
content_replace('m71588','or harmonics are multiples of the fundamental frequency.','are integer multiples of the fundamental frequency and are therefore also harmonics. In general, overtones are frequencies above the fundamental and need not be integer multiples of it.')
replace_para('m67032','import-auto-id2729047','SI uses seven <term>base units</term>, also called fundamental units: the metre, kilogram, second, ampere, kelvin, mole, and candela. These correspond to length, mass, time, electric current, thermodynamic temperature, amount of substance, and luminous intensity. Units for other quantities are formed from combinations of base units and are called derived units. For example, speed has units of metres per second and force has units of kilogram metres per second squared.')
content_replace('m76584','The emission of these rays is called <emphasis>nuclear radioactivity</emphasis>','The spontaneous transformation of unstable nuclei is called <emphasis>nuclear radioactivity</emphasis>')
content_replace('m76584','A nucleus that spontaneously destroys part of its mass to emit radiation is said to','An unstable nucleus that spontaneously transforms into another nucleus or a lower-energy nuclear state is said to')
content_replace('m42531','is the phenomenon of time passing slower for an observer who is moving relative to another observer.','means that, in an inertial frame, a moving clock records less time between its ticks than the elapsed time measured in that frame. Each clock measures time normally in its own rest frame.')
content_replace('m52314','is defined to be <emphasis effect="italics">the magnitude or size of displacement between two positions</emphasis>.','between two positions is their straight-line separation, equal to the magnitude of their displacement.')
content_replace('m67036','Any net force causing uniform circular motion is called a','The inward component of the net force responsible for a curved path is called a')
content_replace('m71624','on any object in any fluid.','on an object immersed in a fluid at rest.')
content_replace('m71626','for an incompressible, frictionless fluid, the following sum is constant:','for steady flow of an incompressible fluid with negligible viscosity, the following sum is constant along a streamline:')
content_replace('m67126','A process by which a gas does work on a piston at constant pressure is called an','A process that occurs at constant pressure is called an')
content_replace('m67126','Since the pressure is constant, the force exerted is constant and the work done is given as','For a gas acting on a piston of fixed area, constant pressure gives a constant force, and the work done is given as')
content_replace('m52410','above which they cannot be magnetized.','above which they lose their spontaneous magnetization, although they can still respond to an applied magnetic field.')
content_replace('m52455','is defined as the spreading of white light into its full spectrum of wavelengths. More technically, dispersion occurs whenever there is a process that changes the direction of light in a manner that depends on wavelength. Dispersion, as a general phenomenon, can occur for any type of wave and always involves wavelength-dependent processes.','is the dependence of wave speed in a medium on frequency. For light, the resulting dependence of refractive index on wavelength can separate white light into colors by refraction. Dispersion also occurs for other types of waves.')
content_replace('m67134','all light rays that enter it parallel to its axis','light rays close and parallel to its axis')
content_replace('m67134','all light rays entering it parallel to its axis','light rays close and parallel to its axis')
content_replace('m67134','Finally, we note that a virtual image is upright and larger than the object,','Finally, we note that the virtual image in this converging-lens example is upright and larger than the object,')
after_para('m67134','import-auto-id1726936','<para id="lens-shape-medium-qualification">These descriptions of convex and concave lenses assume that the lens has a higher refractive index than its surroundings, as glass does in air. The converging or diverging effect depends on both lens shape and the refractive indices.</para>')
after_para('m67622','import-auto-id3400307','<para id="specific-heat-conditions">Specific heat also depends on the conditions of heating. In particular, heating a gas at constant pressure and heating it at constant volume generally require different amounts of heat for the same temperature change.</para>')
after_para('m42674','meson-baryon-quark-definitions','<para id="baryon-number-quark-interpretation">In the quark model, each quark has baryon number +1/3 and each antiquark has baryon number −1/3. A three-quark baryon therefore has baryon number +1, an antibaryon has −1, and a quark–antiquark meson has zero.</para>')

if __name__=='__main__':
 # Validate the complete in-memory patch before any source writes.
 for p,s in texts.items():
  root=ET.fromstring(s);ids=[e.get('id') for e in root.iter() if e.get('id')];assert len(ids)==len(set(ids)),p
  oldroot=ET.fromstring(before[p]);oldids={e.get('id') for e in oldroot.iter() if e.get('id')};assert oldids<=set(ids),(p,oldids-set(ids))
 changes=[]
 for p,s in texts.items():
  a=s.encode('utf-8')
  if a==before[p]:continue
  changes.append(dict(source=p,before_sha256=hashlib.sha256(before[p]).hexdigest(),after_sha256=hashlib.sha256(a).hexdigest(),before=before[p].decode('utf-8'),after=s))
 q='proposals/maintainer-corrections/GLOSSARY-QUALITY-APPROVED-BATCH.json'
 assert not (R/q).exists(),'Already applied'
 (R/q).write_text(json.dumps(dict(status='approved',held_groups=['G17','G33'],changes=changes),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 for c in changes:(R/c['source']).write_bytes(c['after'].encode('utf-8'))
 p=R/'maintained/editorial-changes.json';j=json.loads(p.read_text(encoding='utf-8'));j['changes'].append(q);p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 for name in ['next-release-1.1.md','exercise-revision-1.1.md']:
  with (R/'docs'/name).open('a',encoding='utf-8') as f:f.write('\nGlossary quality batch: applied focused definitions, canonical placements and prose consistency corrections from approved groups. G17 and G33 held for broader prose review. Equations and exercise numbering retained; pending preview refresh.\n')
 (R/'reports/1.1/glossary-quality-applied-batch.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'modules_changed':len(changes),'definition_actions':len(log)}))
