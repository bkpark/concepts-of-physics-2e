"""Prepare factual-audit follow-ups as review overlays, never canonical edits.

Where available, the approved Priority 3 section preview is the base. This
deliberately preserves that review's mathematics, notation and prose decisions.
"""
from pathlib import Path
import copy, hashlib, html, json, math, re, sys, shutil
import xml.etree.ElementTree as E

ROOT=Path(__file__).resolve().parents[1]
C='http://cnx.rice.edu/cnxml'; M='http://www.w3.org/1998/Math/MathML'
E.register_namespace('',C); E.register_namespace('m',M)
items=[]; roots={}; paths={}; touched=set()

def source(title,url,locator):
    return dict(title=title,url=url,locator=locator,checked='2026-09-25',use='Factual verification only; no external prose or artwork imported.')
entropy=source('MIT: Thermodynamics and Climate Change, Chapter 4','https://ocw.mit.edu/courses/res-2-008-thermodynamics-and-climate-change-summer-2020/mitres-2-008su22_ch4.pdf','Microstates, multiplicity and the statistical interpretation of entropy')
compression=source('MIT: Calculation of Entropy Change in Some Basic Processes','https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node41.html','Isothermal compression and free expansion; system and surroundings')
knmi=source('KNMI: Buys Ballot’s Doppler experiment','https://www.knmi.nl/over-het-knmi/nieuws/doppler-experiment-buys-ballot-160-jaar-geleden','3 June 1845 train experiment; Doppler’s 1842 proposal')
wilson=source('Mount Wilson Observatory: Michelson site','https://www.mtwilson.edu/vt-michelson-site/','1924–1926 rotating-mirror measurement; 22-mile baseline')
morley=source('Case Western Reserve: Michelson–Morley experiment','https://case.edu/ech/articles/m/michelson-morley-experiment','1881 and 1887 interferometer experiments; expected ether drift and null result')
broglie=source('Fondation Louis de Broglie: papers of 1923–1924','https://fondationlouisdebroglie.org/AFLB-481/aflb481m1003.pdf','Reprints distinguish the 1923 papers from the 1924 thesis')
shroud=source('Damon et al. (1989), Radiocarbon Dating of the Shroud of Turin','https://doi.org/10.1038/337611a0','Figure 1 and calibrated date: AD 1260–1390, at least 95% confidence; introduction: Lirey in the 1350s')
shroud['accessible_full_text']='https://www.shroud.com/nature.htm'
clausius=source('Clausius’s 1850 paper, English translation','https://www.mdpi.org/lin/clausius/clausius.htm','On the Moving Force of Heat; avoid assigning sole priority for the first law')
dam=source('China Three Gorges: engineering overview','https://tgf.ctg.com.cn/eportal/ui?pageId=720862','Maximum dam height 181 m; crest elevation 185 m; axis length 2309.5 m; installed capacity 22.5 GW')
damdate=source('China Three Gorges: 2012 project milestones','https://www.ctg.com.cn/cypc/zxgg99/sxgc3/index.html','Operator timeline: July 2012, all 32 main generating units in service; total installed capacity 22.5 GW')
cern=source('CERN: Large Hadron Collider','https://home.web.cern.ch/science/accelerators/large-hadron-collider/','27-km ring')
iaea=source('IAEA: Nuclear Technology Review 2025','https://www.iaea.org/sites/default/files/gc/gov-inf-2025-8-gc69-inf-4.pdf','End-2024 operating reactors; distinguish reactors from plants and suspended units')
iea=source('IEA: Global Energy Review 2025 — Electricity','https://www.iea.org/reports/global-energy-review-2025/electricity','Nuclear supplied 9% of global electricity in 2024')
navy=source('US Navy: ELF communications information (1982)','https://www.navy-radio.com/commsta/elf/elf-info-8202.pdf','Historical US Navy system: nominal 76 Hz; archive of Navy publication, used only for engineering frequency')
itu=source('ITU-R V.431-8: frequency and wavelength bands','https://www.itu.int/dms_pubrec/itu-r/rec/v/R-REC-V.431-8-201508-I!!PDF-E.pdf','Radio-band nomenclature; VHF 30–300 MHz and UHF 300–3000 MHz')
am=source('FCC 02-27, AM expanded band','https://docs.fcc.gov/public/attachments/FCC-02-27A1.pdf','117 carrier frequencies from 540 to 1700 kHz')
fm=source('47 CFR 73.310: FM technical definitions','https://www.law.cornell.edu/cfr/text/47/73.310','200-kHz channel; ±75-kHz deviation for 100% modulation; primary regulation reproduced by Cornell LII')
tv=source('47 CFR 73.603: television channels','https://www.law.cornell.edu/cfr/text/47/73.603','US channel frequency table; channels 2–36, with gap at 72–76 MHz and reserved channel 37')
wireless=source('FDA: Wireless Medical Devices','https://www.fda.gov/medical-devices/digital-health-center-excellence/wireless-medical-devices','Radio-frequency interference and coexistence; not a claim that all phones use one band')
shannon=source('Shannon (1948): A Mathematical Theory of Communication','https://web.mit.edu/6.976/www/handout/shannon.pdf','Channel capacity depends on bandwidth and signal/noise, not carrier frequency alone')
jcmt=source('East Asian Observatory: About the JCMT','https://www.eaobservatory.org/jcmt/about-jcmt/','Submillimeter telescope; no ranking by fame')
webb=source('NASA: Webb cryocooler','https://science.nasa.gov/mission/webb/cryocooler/','Passive and active cooling; liquid nitrogen is not a universal requirement')
attenuation=source('NIST: X-ray Mass Attenuation Coefficients','https://physics.nist.gov/PhysRefData/XrayMassCoef/cover.html','Energy- and material-dependent attenuation, including absorption edges')

def root(mid):
    if mid not in roots:
        p=ROOT/f'prototype/dist/review-1.1/priority3-sections/source/{mid}/index.cnxml'
        if not p.exists(): p=ROOT/f'maintained/modules/{mid}/index.cnxml'
        paths[mid]=p; roots[mid]=E.parse(p).getroot()
    return roots[mid]
def node(mid,id):
    if id=='glossary':
        return root(mid).find('{'+C+'}glossary')
    if id=='abstract':
        return root(mid).find('.//{http://cnx.rice.edu/mdml}abstract')
    return next(e for e in root(mid).iter() if e.get('id')==id)
def xml(e):
    e=copy.deepcopy(e); e.tail=None
    return E.tostring(e,encoding='unicode')
def add(title,reason,sources,attention='Small correction; review the wording in context.'):
    i=dict(id=f'P4-{len(items)+1:02}',title=title,reason=reason,sources=sources,attention=attention,status='proposed; not applied',passages=[])
    items.append(i); return i
def edit(i,mid,id,replacements=None,inner=None,caption=None,removed_ids=()):
    assert (mid,id) not in touched,(mid,id)
    touched.add((mid,id)); old=xml(node(mid,id)); new=old
    if replacements:
        for a,b in replacements:
            assert new.count(a)==1,(i['id'],id,a,new.count(a))
            new=new.replace(a,b)
    if inner is not None:
        n=E.fromstring(new); n.text=None
        for c in list(n): n.remove(c)
        wrap=E.fromstring(f'<wrap xmlns="{C}" xmlns:m="{M}">{inner}</wrap>')
        n.text=wrap.text
        for c in wrap:n.append(c)
        new=xml(n)
    if caption is not None:
        n=E.fromstring(new); c=n.find('{'+C+'}caption'); assert c is not None
        c.clear(); c.text=caption; new=xml(n)
    newnode=E.fromstring(new); assert old!=new
    assert {e.get('id') for e in E.fromstring(old).iter() if e.get('id')} <= {e.get('id') for e in newnode.iter() if e.get('id')} | set(removed_ids), (i['id'],id,'lost identity')
    p=paths[mid]
    i['passages'].append(dict(module=mid,source_id=id,source_path=p.relative_to(ROOT).as_posix(),source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),before_xml=old,proposed_xml=new))
    if id=='glossary':
        i['passages'][-1]['source_selector']='glossary'
    if id=='abstract':
        i['passages'][-1]['source_selector']='abstract'
    if removed_ids:i['passages'][-1]['removed_ids']=list(removed_ids)
def links(mid,id):
    return [xml(e) for e in node(mid,id).iter('{'+C+'}link')]

def remove(i,mid,id):
    assert (mid,id) not in touched
    touched.add((mid,id))
    old=xml(node(mid,id));p=paths[mid]
    i['passages'].append(dict(module=mid,source_id=id,operation='remove',source_path=p.relative_to(ROOT).as_posix(),source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),before_xml=old,proposed_xml=None))

i=add('What “disorder” means in the coin model','Keep the coin-counting approach and the word disorder, but identify the relevant meaning: how many microscopic arrangements fit a macroscopic description. A tossed-coin model is an analogy, not a measurement of the coins’ thermal entropy.',[entropy],'Read closely: the conceptual bridge, macrostate definition, and limits of the analogy.')
edit(i,'m42238','import-auto-id1169737762485',replacements=[('heat transfer occur only','heat transfer occur spontaneously only'),('Disorder is simply vastly more likely than order.','There are vastly more microscopic arrangements corresponding to disorder than to order.')])
i['passages'][-1]['status']='approved-pending-application'
i['passages'][-1]['authorization']='Maintainer approved the one-sentence replacement about microscopic arrangements and retained spontaneously in the opening paragraph. Remaining P4-01 passages are still under review.'
edit(i,'m42238','import-auto-id1169738082621',replacements=[('but they never fall in straight, orderly rows','but you might never see them fall in straight, orderly rows')])
i['passages'][-1]['status']='approved-pending-application'
i['passages'][-1]['authorization']='Maintainer supplied the rain-example wording: but you might never see them fall in straight, orderly rows. Retain the following sentence explaining that an orderly pattern is possible but unlikely.'
edit(i,'m42238','import-auto-id1169738137712',replacements=[('an overall property of a system','a description of a system in terms of its macroscopic properties')])
edit(i,'m42238','import-auto-id1169737980730',replacements=[('With any system, the assumption that all microstates are equally probable must be valid, or the analysis will be erroneous.','For this counting argument, the accessible microstates must be equally probable.')])
edit(i,'m42238','import-auto-id1169737927504',replacements=[('So even if you start with an orderly state, there is a strong tendency to go from order to disorder, from low entropy to high entropy.','So even if you start with an orderly arrangement, tossing the coins is likely to produce a less orderly one, illustrating why macroscopic systems left to themselves tend toward higher entropy.')])
i['passages'][-1]['status']='approved-pending-application'
i['passages'][-1]['authorization']='Maintainer approved the replacement connecting likely less-orderly coin arrangements to the tendency of macroscopic systems left to themselves toward higher entropy.'
edit(i,'m42238','import-auto-id1169737780420',inner='Disordered states are more likely than ordered states because there are many more ways for a system to be disordered than ordered.')
i['passages'][-1]['status']='approved-pending-application'
i['passages'][-1]['authorization']='Maintainer approved the concise summary bullet explaining that disordered states are more likely because there are many more ways for a system to be disordered than ordered.'
edit(i,'m42238','fs-id1169736621446',inner='a description of a system in terms of its macroscopic properties')
edit(i,'m42238','fs-id1169736620556',inner='a detailed microscopic description of a system compatible with a given macrostate')
edit(i,'m42238','eip-447',inner='Why does a gas have greater entropy when it occupies a larger volume at the same temperature? Explain in terms of the microscopic arrangements available to its molecules.')
i['exercise_note']='Only the brick-pile question’s unsupported visual-order inference is repaired; this is not the broader exercise revision.'

i=add('Gas compression, expansion, and total entropy','Compression does not necessarily increase the entropy of the universe: reversible compression leaves the total unchanged. Specify isothermal compression and removal of confinement before free expansion. The low-speed arrows in the existing illustration are not an isothermal-compression diagram.',[entropy,compression],'Read closely: coordinated paragraph and caption changes. Existing artwork is retained.')
edit(i,'m42238','import-auto-id1169738209745',replacements=[(' with identical velocities',''),('Indeed, it is so unlikely that we have a law saying that it is impossible, which has never been observed to be violated—the second law of thermodynamics.','Indeed, it is so unlikely that we have a law saying that it is essentially impossible—the second law of thermodynamics.')])
i['passages'][-1]['status']='approved-pending-application'
i['passages'][-1]['authorization']='Maintainer approved removing identical velocities and supplied the concluding sentence retaining the second-law punch line with essentially impossible.'
edit(i,'m42238','import-auto-id1169738137203',caption='(a) The ordinary state of gas in a container is a random distribution of atoms or molecules with a Maxwell-Boltzmann distribution of speeds. (b) A spontaneous concentration of the molecules into one corner is overwhelmingly unlikely for a macroscopic gas. If gas is initially confined to a small part of a container and the confinement is removed, it spreads through the available volume.')
x=links('m42238','import-auto-id1169738060603')[0]
edit(i,'m42238','import-auto-id1169738060603',inner='The gas has greater entropy when more positions are available to its molecules. We can reduce its entropy by compressing it at constant temperature, doing work and transferring heat to the surroundings. The entropy gained by the surroundings equals the gas’s entropy decrease for reversible compression, and exceeds it for irreversible compression. If the compressed gas is then allowed to expand freely into an evacuated part of an insulated container, its entropy increases. A spontaneous return to the concentrated state ('+x+'(b)) is overwhelmingly unlikely. Disorder is vastly more likely than order.')

i=add('Scope of the statistical second law','The existing conclusion incorrectly forbids entropy decrease in any macroscopic system. Apply it to an isolated system and preserve the distinction between overwhelmingly unlikely macroscopic fluctuations and ordinary entropy reduction through heat transfer.',[entropy,compression])
edit(i,'m42238','import-auto-id1169737709995',replacements=[('is proportional to the probability that the macrostate will occur.','is proportional to the probability that the macrostate will occur when the accessible microstates are equally probable.')])
edit(i,'m42238','import-auto-id1169736801299',inner='Thus the second law of thermodynamics is explained on a statistical level: the entropy of an isolated macroscopic system remains constant or increases. Macrostates with greater entropy have vastly more microstates, making a substantial spontaneous decrease overwhelmingly unlikely. A system that exchanges heat with its surroundings can decrease in entropy while the total entropy of the system and surroundings increases or remains constant.')
edit(i,'m42238','import-auto-id1169737967292',replacements=[('For a macroscopic physical system,','For an isolated macroscopic physical system,')])

i=add('Electrical safety: remove one remaining assurance','The brain-current and high-frequency surface-current claims were already corrected under F2-11. An adjacent dry-skin calculation still calls its estimated current harmless. Removing that word leaves the numerical example intact.',[wireless])
i['sources']=[]
i['evidence_note']='The prior electrical review and sources are recorded in proposals/1.1/fact-check-cycle2.json (F2-09–F2-11). This proposal adds no threshold, medical advice, or new numerical assertion.'
edit(i,'m52406','import-auto-id2400011',replacements=[('passes harmlessly through him','passes through him')])

i=add('Doppler proposal versus Buys Ballot experiment','The moving-train demonstration was organized by Buys Ballot in 1845. Credit Doppler with the 1842 proposal and correct the connected question.',[knmi])
edit(i,'m67819','import-auto-id1955117',replacements=[('Christian Johann Doppler (1803–1853), who did experiments with both moving sources and moving observers. Doppler, for example,','Christian Doppler (1803–1853), who proposed the effect in 1842. In 1845, Christophorus Buys Ballot')])
edit(i,'m67819','import-auto-id2441432',replacements=[('Christian Doppler','Christophorus Buys Ballot')])

i=add('Michelson’s early rotating-mirror measurement','Introduce the 1879 measurement with its approximately 600-m baseline, retain the roughly 0.04% difference associated with the commonly reported 299,910 km/s result, and distinguish the later 35-km apparatus illustrated in the figure.',[wilson,source('Michelson: Experimental Determination of the Velocity of Light','https://www.gutenberg.org/files/11753/11753-h/11753-h.htm','1879 apparatus: mirror separation 1986.23 feet, approximately 605 m; angular displacement of the returning image'),source('US Naval Academy: Michelson’s measurements','https://www.usna.edu/Library/sca/blog/posts/michelson_velocity.php','Historical account gives 299,910 ± 50 km/s in 1879; 299,796 ± 4 km/s for the later Mount Wilson work')])
old=xml(node('m52454','eip-406'))
start=old.index('One particularly direct method')
end=old.rfind('</para>')
ref=links('m52454','eip-406')[0]
replacement='One particularly direct method was used in 1879 by the American physicist Albert Michelson (1852–1931). Light reflected from a rotating mirror traveled to a stationary mirror about 600 m away and returned to the rotating mirror. The mirror’s rotation during the round trip displaced the returning image, allowing the travel time and speed of light to be determined. Michelson’s early result differed from today’s value by only about 0.04%. He later conducted the Michelson–Morley experiment of 1887, which we will discuss in connection with special relativity. In 1924–1926, he improved his speed-of-light measurement using a 35-km baseline and a multifaceted rotating mirror, illustrated in '+ref+'.'
edit(i,'m52454','eip-406',replacements=[(old[start:end],replacement)])
i['passages'][-1]['authorization']='Maintainer requested leading with the early rotating-mirror measurement, approximately 600 m and 1879, retaining about 0.04% accuracy and mentioning the later improvement. New wording is displayed for review.'
edit(i,'m52454','import-auto-id1165298806898',replacements=[('A schematic of early apparatus used by Michelson and others to determine the speed of light.','A schematic of the later rotating-mirror method used by Michelson in 1924–1926 to determine the speed of light.'),(' Michelson’s calculated value of the speed of light was only 0.04% different from the value used today.','')])
i['source_caution']='The Naval Academy account gives the early result as 299,910 km/s, about 0.0392% above the modern value. Historical reports also contain a 299,944 km/s result (about 0.05%); the 0.04% retained here refers to the former, not every 1879 measurement series. The figure retains its 35-km label and multifaceted mirror and is explicitly identified as the later apparatus.'

i=add('What the Michelson–Morley experiment established','Distinguish the ether-drift null result from an independent proof of every part of the second postulate. Remove a speculative claim about Einstein’s awareness; preserve the existing transition to his postulate.',[morley],'Read closely: history and the logical connection to the second postulate.')
edit(i,'m42528','import-auto-id2559845',inner='Scientists were already familiar with mechanical waves, such as sound, that traveled through a medium. They therefore assumed that light also traveled through a medium. This proposed aether had to pervade even apparently empty space, since light could travel through a vacuum. Light was assumed to travel at speed <m:math><m:mi>c</m:mi></m:math> relative to the aether. Earth’s motion through a stationary aether should therefore produce differences in light travel times along different directions. In 1881, the American physicist A. A. Michelson used an interferometer to compare light travel times in perpendicular directions. In 1887, he and E. W. Morley repeated the experiment with improved precision. The results of their measurements were startling.')
i['passages'][-1]['authorization']='Maintainer requested replacing the Young’s experiment opening with the mechanical-wave motivation and vacuum-pervading aether, retaining the bridge to the Michelson–Morley measurements. Revised paragraph is pending contextual review.'
for id in ['import-auto-id967087','import-auto-id1946290']:
    edit(i,'m42528',id,inner='The '+('<term id="import-auto-id2688059">Michelson-Morley experiment</term>' if id=='import-auto-id967087' else 'Michelson-Morley experiment')+' found no change in light travel times of the size expected from the Earth’s motion through a stationary light-carrying medium.')
old=node('m42528','import-auto-id2800793'); text=''.join(old.itertext())
# Retain native inline c from the original paragraph rather than adding a new symbol format.
edit(i,'m42528','import-auto-id2800793',inner='The experiment did not reveal the differences in light travel times expected from Earth’s motion through a stationary aether. For a number of years, scientists tried to reconcile this result with the proposed light-carrying medium while retaining the Newtonian understanding of space and time. The difficulty was explaining why Earth’s motion through that medium could not be detected.')
i['passages'][-1]['authorization']='Maintainer accepted the transition that leaves the conflict unresolved until the following Einstein paragraph.'
edit(i,'m42528','import-auto-id2972888',inner='In 1905, Einstein published his first paper on special relativity, “On the Electrodynamics of Moving Bodies.” In this paper, he made the bold assumption that it was not Maxwell’s newer equations of electromagnetism that needed correction, but the assumptions about space and time underlying Newton’s laws. This bold choice was expressed in his <term>second postulate of special relativity</term>.')
i['passages'][-1]['authorization']='Maintainer supplied the replacement contrasting Maxwell’s newer theory with Newtonian foundations and requested grammatical smoothing and the refreshed preview. Specify the underlying assumptions about space and time; pending contextual review.'

# Approved section read-through replacement: retain figure/media identities.
edit(i,'m42528','fs-id3167669',replacements=[('../../media/Figure_29_01_01a.jpg','../../../proposals/1.1/assets/nasa-sdo-sunspots-2014.jpg'),('width="250"','width="450"'),('A calculator is placed on open math books and few papers. Problems on trigonometry are solved on one of the papers.','Colorized orange solar disk against black space, with a large dark sunspot group slightly left of center and smaller spots elsewhere.')],caption='The Sun with a large sunspot group, photographed by NASA’s Solar Dynamics Observatory in October 2014. Light takes about 8.3 minutes to travel from the Sun to Earth through the vacuum of space. We therefore see the Sun as it was about 8 minutes earlier. (credit: NASA/SDO; colorized image)')
i['passages'][-1]['authorization']='Maintainer approved replacing the calculator photo with this NASA/SDO sunspot image and the proposed caption. Introduction prose remains pending review.'
i['passages'][-1]['asset_manifest']='proposals/1.1/assets/nasa-sdo-sunspots-2014.json'
i['sources'].append(source('NASA: Sunspots','https://science.nasa.gov/sun/sunspots/','HMI image of NOAA 12192, October 2014; image credited to NASA'))
i['sources'].append(source('NASA: Images and Media Usage Guidelines','https://www.nasa.gov/nasa-brand-center/images-and-media/','Educational textbook use and NASA acknowledgment; check separately credited third-party works'))

# Introductory prose requested for contextual reading; not yet approved.
edit(i,'m42528','import-auto-id2515454',inner='Mathematics can begin with a small set of basic assumptions, called <term>postulates</term> or <term>axioms</term>, from which other results follow by logical reasoning. In axiomatic set theory, for example, the axioms specify how sets—collections of objects—can be formed and related to one another. These starting assumptions provide a foundation for developing the theory.')
i['passages'][-1]['authorization']='Maintainer requested this set-theory introduction in the section preview for contextual review.'
edit(i,'m42528','import-auto-id3039714',inner='In the preceding chapter, we approached quantum mechanics through experimental observations that challenged classical physics. Here, we begin with two postulates and explore their consequences. In addition to the logical consistency expected of mathematical axioms, the postulates of a physical theory must be consistent with the universe we aim to describe. Einstein proposed the two postulates introduced in this section and developed <term>special relativity</term> from them, making concrete predictions that have since been verified by numerous observations and experiments.')
i['passages'][-1]['authorization']='Maintainer requested the transition contrasting how the textbook introduces quantum mechanics and relativity, retaining the requirement for experimental agreement, for contextual review.'

edit(i,'m42528','import-auto-id2799129',inner='The laws of physics seem to be simplest in inertial frames. For example, when you are in a plane flying at a constant altitude, speed, and direction, physics seems to work exactly the same as if you were standing on the surface of the Earth. Galileo illustrated this <term>principle of relativity</term> by imagining observations below deck on a ship: falling drops, swimming fish, and flying insects behave the same whether the ship is at rest or moving steadily in a straight line. Mechanical experiments within the ship cannot distinguish these states of motion. Einstein extended this principle from mechanics to all laws of physics, including electricity and magnetism, in his <term>first postulate of special relativity</term>.')
i['passages'][-1]['authorization']='Maintainer approved retaining the airplane opening followed by Galileo’s ship example and the connection to Einstein’s first postulate.'
i['sources'].append(source('Galileo: Dialogue Concerning the Two Chief World Systems (1632), ship passage','https://mathshistory.st-andrews.ac.uk/Extras/Galileo_Dialogue/','Below-deck observations of drops, fish, and insects are unchanged by uniform ship motion'))

edit(i,'m42528','import-auto-id3156364',inner='The first postulate does not mean that different observers measure the same values for every physical quantity. An object at rest in one inertial frame can be moving in another, so observers in these frames assign it different velocities, momenta, and kinetic energies. What remains the same is the form of the laws relating these quantities: each observer uses the same laws to describe the motion.')
i['passages'][-1]['authorization']='Maintainer accepted this replacement distinguishing physical laws from frame-dependent measured quantities and requested the updated section preview.'

edit(i,'m42528','import-auto-id1331972',inner='The second postulate of special relativity deals with the speed of light. Late in the 19th century, the major tenets of classical physics were well established. Two of the most important were the laws of electricity and magnetism and Newton’s laws. In particular, Maxwell’s equations predict electromagnetic waves that travel at <m:math><m:mi>c</m:mi><m:mo>=</m:mo><m:mn>3.00</m:mn><m:mo>×</m:mo><m:msup><m:mn>10</m:mn><m:mn>8</m:mn></m:msup><m:mspace width="0.25em"/><m:mtext>m/s</m:mtext></m:math> in a vacuum. Light is one such electromagnetic wave.')
i['passages'][-1]['authorization']='Maintainer requested this smoothed version of their draft in the preview, retaining a paragraph break before Applying this prediction.'
edit(i,'m42528','import-auto-id2762533',inner='Applying this prediction in every inertial frame contradicts the intuitive results that come from our experience with classical relativity. If a baseball pitcher throws a ball backward from the bed of a moving truck, we on the ground expect to see that ball moving more slowly. For example, if the ball is thrown backward at 60 mph relative to the truck and the truck is moving forward at 20 mph relative to the ground, we would see the ball moving backward at 40 mph. But if Maxwell’s equations apply equally in the spaceship’s frame and Earth’s frame, light from a laser pointed backward aboard a spaceship moving forward at <m:math><m:mn>0.2</m:mn><m:mi>c</m:mi></m:math> relative to Earth must still travel backward at <m:math><m:mi>c</m:mi></m:math> relative to Earth, not <m:math><m:mn>0.8</m:mn><m:mi>c</m:mi></m:math>. A common approach at the time was to assign light’s predicted speed to a particular frame: that of a proposed light-carrying medium called the <term>luminiferous aether</term>.')
i['passages'][-1]['authorization']='Maintainer requested this smoothed version of their baseball/spaceship comparison and aether transition in the preview; following paragraphs will be reviewed next.'

edit(i,'m42528','import-auto-id2582129',inner='These two postulates are the starting points from which we derive the results of special relativity. When their consequences conflict with familiar expectations, we retain the postulates and reconsider those expectations. We find that observers in relative motion can disagree about elapsed times and measured lengths, and that mass and energy are related in ways Newtonian physics did not anticipate. The following sections explore these consequences.')
i['passages'][-1]['authorization']='Maintainer approved the concluding paragraph emphasizing derivation from the postulates and reconsideration of familiar expectations.'
edit(i,'m42528','import-auto-id2573975',inner='Special relativity begins with two postulates. Their consequences require us to revise familiar assumptions about space and time, rather than change the postulates to fit those assumptions.')
edit(i,'m42528','import-auto-id2836702',inner='An inertial frame of reference is one in which an object remains at rest or moves at constant velocity when the net external force on it is zero.')
edit(i,'m42528','import-auto-id2502496',inner='The first postulate of special relativity states that the laws of physics have the same form in all inertial frames, although observers can measure different values for quantities such as velocity and kinetic energy. The second postulate states that light in a vacuum travels at the same speed <m:math><m:mi>c</m:mi></m:math> in every inertial frame, regardless of the motion of its source or the observer.')
for passage in i['passages'][-3:]:
    passage['authorization']='Maintainer requested aligning the section summary with the revised exposition. Replaced the misleading acceleration-based special/general-relativity distinction and universal-validity claim with the postulates-first approach; summary pending contextual review.'

edit(i,'m42528','import-auto-id2635772',inner='The speed of light <m:math><m:mi>c</m:mi></m:math> in vacuum is a constant, independent of the relative motion of the source.')
i['passages'][-1]['authorization']='Maintainer supplied the exact second-postulate box wording, adding in vacuum.'

remove(i,'m42528','fs-id1730744')
i['passages'][-1]['authorization']='Maintainer explicitly requested removing the Check Your Understanding comparison of special and general relativity. Remove the complete exercise, including its answer; no incoming maintained cross-references were found.'

# Coordinate the complete glossary in one overlay, preserving existing identities.
glossary=copy.deepcopy(node('m42528','glossary'))
meanings={
    'fs-id1509148':'the theory of space, time, and motion based on the principle of relativity and the constancy of the speed of light in vacuum',
    'fs-id2747444':'a reference frame in which an object remains at rest or moves at constant velocity when the net external force on it is zero',
    'fs-id2912509':'the statement that the laws of physics have the same form in all inertial frames of reference',
    'fs-id2905259':'the statement that the speed of light <m:math><m:mi>c</m:mi></m:math> in vacuum is a constant, independent of the relative motion of the source',
    'fs-id2932463':'an 1887 experiment comparing light travel times in perpendicular directions that found no differences of the size expected from Earth’s motion through a stationary aether',
}
for meaning in glossary.iter('{'+C+'}meaning'):
    if meaning.get('id') in meanings:
        wrapper=E.fromstring(f'<wrap xmlns="{C}" xmlns:m="{M}">{meanings[meaning.get("id")]}</wrap>')
        for child in list(meaning):meaning.remove(child)
        meaning.text=wrapper.text
        for child in wrapper:meaning.append(child)
for key,term,meaning in [
    ('postulate','postulate','a basic assumption taken as a starting point from which the results of a theory are derived'),
    ('axiom','axiom','a basic assumption from which results in a mathematical theory are derived; also called a postulate'),
    ('principle-of-relativity','principle of relativity','the principle that the laws of physics have the same form in all inertial frames; Galileo applied it to mechanics, and Einstein extended it to all laws of physics'),
    ('luminiferous-aether','luminiferous aether','a proposed medium that was thought to fill even empty space and carry light waves'),
]:
    definition=E.SubElement(glossary,'{'+C+'}definition',{'id':'definition-'+key})
    E.SubElement(definition,'{'+C+'}term').text=term
    E.SubElement(definition,'{'+C+'}meaning',{'id':'meaning-'+key}).text=meaning
edit(i,'m42528','glossary',inner=''.join(xml(child) for child in glossary))
i['passages'][-1]['authorization']='Maintainer approved the rest of the section and requested new-term definitions and alignment of the glossary. Complete glossary is pending review; original definition and meaning identities are retained.'

i=add('De Broglie: 1923 proposal and 1924 thesis','Both dates belong in the history; the proposal did not originate in a thesis completed in 1923.',[broglie])
edit(i,'m67803','import-auto-id1558765',replacements=[('made as part of his doctoral thesis','developed further in his 1924 doctoral thesis')])

i=add('Shroud example: history and calibrated dating','Preserve the simplified 92% calculation, but do not attribute that exact value to all three laboratories. The published calibrated interval is not a weighted calendar date of 1320 ± 60. The first display was in Lirey, France, not Turin.',[shroud],'Read closely: the distinction between the classroom calculation and the reported laboratory result. The source’s calibration and confidence interval are explicit, not inferred.')
before=xml(node('m52471','import-auto-id2953168'))
last=before.index('All three laboratories found')
tail=before[last:before.rfind('</para>')]
refs=links('m52471','import-auto-id2953168')
edit(i,'m52471','import-auto-id2953168',replacements=[('This relic was first displayed in Turin in 1354 and was denounced as a fraud at that time by a French bishop.','This relic was first displayed in Lirey, France, in the 1350s.'),('each being given four pieces of cloth, with only one unidentified piece from the shroud, to avoid prejudice','each receiving a shroud sample and control samples'),(tail,'All three laboratories obtained medieval dates. The following example uses a rounded value of 92% to illustrate the dating calculation (see '+refs[-1]+').')])
edit(i,'m52471','import-auto-id2405399',replacements=[('was only recently carbon-14 dated','was carbon-14 dated in 1988')])
edit(i,'m52471','import-auto-id3093652',replacements=[('given that the amount','using the approximation that the amount')])
edit(i,'m52471','import-auto-id2449138',inner='This simplified calculation dates the material to about AD 1300, using 1988 as the measurement year. The published study reported a calibrated date range of AD 1260–1390 with at least 95% confidence. Calibration accounts for changes in atmospheric carbon-14 over time. The medieval date is consistent with the first record of the shroud’s existence and inconsistent with the period in which Jesus lived.')

i=add('Clausius caption: avoid a sole-priority claim','Retain the 1850 historical connection without calling it the first explicit statement of the first law. Rudolph and Rudolf both occur in institutional accounts; the spelling alone is not an established error.',[clausius])
edit(i,'m67126','import-auto-id1169738145359',replacements=[('a mere 61 years after the first explicit statement of the first law of thermodynamics by Rudolph Clausius','61 years after Rudolph Clausius’s 1850 paper on thermodynamics')])

i=add('Three Gorges: capacity milestone','Use the full generating-capacity milestone rather than treating 2008 as completion of the entire project. Replace “22 average-sized nuclear power plants” with installed capacity. Keep 181 m: the operator distinguishes maximum dam height from its 185-m crest elevation.',[dam,damdate])
edit(i,'m71613','import-auto-id1371721',replacements=[('When completed in 2008, this became the world’s largest hydroelectric plant, generating power equivalent to that generated by 22 average-sized nuclear power plants.','Its generating capacity reached 22.5 GW in 2012.')])
i['source_caution']='The operator’s engineering page is in Chinese and did not consistently load directly; its indexed engineering figures distinguish 坝顶高程 (crest elevation) from 最大坝高 (maximum dam height). The operator’s indexed project timeline supplies the July 2012 milestone; direct access to that page is also intermittent. No height correction is proposed.'

i=add('Accelerator size','Replace the nonexistent operating 90-km example with a named existing accelerator.',[cern])
edit(i,'m52410','import-auto-id1464843',replacements=[('a 90-km-circumference particle accelerator','the 27-km-circumference Large Hadron Collider')])

nuclear_shares=source('IAEA: Nuclear Power Reactors in the World, 2025 edition','https://www-pub.iaea.org/MTCD/publications/PDF/RDS-2-45_web.pdf','Table 6, printed page 16 (PDF page 24): 2024 nuclear shares of electricity production, France 67.3%, Slovakia 60.6%; rounded to 67% and 61%')
i=add('Nuclear-power scale and dated counts','Replace the 2009 statistics and sweeping economic/national-development claims with a dated global scale and national examples where nuclear supplies a majority of electricity. Controlled fusion experiments already exist; commercial fusion electricity remains a goal.',[iaea,iea,nuclear_shares],'Read the shortened paragraph. Counts refer to reactors, not power-plant sites; the rounded count avoids mixing operating and suspended categories.')
ref=links('m52479','import-auto-id2402894')[0]
edit(i,'m52479','import-auto-id2402894',inner='<term id="import-auto-id2992737">Nuclear fission</term> is a reaction in which a nucleus is split (or <emphasis effect="italics">fissured</emphasis>). Controlled fission is used to generate electricity, whereas commercial electricity generation from fusion remains a goal. In 2024, more than 400 nuclear fission reactors were in operation around the world, and nuclear power supplied about 9% of the world’s electricity (see '+ref+'). Its share was much higher in some countries: nuclear power generated about 67% of France’s electricity and 61% of Slovakia’s electricity that year.')
i['passages'][-1]['authorization']='Maintainer requested retaining national figures, especially majority shares; France and Slovakia added using the dated IAEA table. Revised wording pending review.'
i['source_caution']='National figures use IAEA RDS-2/45 Table 6 for 2024 (France 67.3%, Slovakia 60.6%). Eurostat reports 61.6% for Slovakia in the same year; datasets have not been reconciled. The textbook uses one identified IAEA source consistently; values refer to electricity production, not all energy use.'

edit(i,'m52479','import-auto-id1575461',replacements=[('About 16% of the world’s electrical power is generated by controlled nuclear fission in such plants.','In 2024, about 9% of the world’s electricity was generated by controlled nuclear fission in such plants.')])
i['passages'][-1]['authorization']='Maintainer requested coordinating Figure 14.10.1 with P4-13’s verified 2024 global electricity share; only the dated generation-share sentence is changed here.'
i['sources'].append(source('IAEA: International Status and Prospects of Nuclear Power, 2010 edition','https://www.iaea.org/sites/default/files/np10.pdf','Printed pages 3–5: slightly less than 14% of world electricity; 2009 output 2558 TWh; share had fallen from 15% as total electricity generation increased'))

i=add('ELF submarine signals and terminology','Replace the 1-kHz ELF example with the historical US Navy 76-Hz system. Retain the seawater-penetration explanation. Frequency-band naming varies, so the glossary uses a descriptive definition instead of an inconsistent numerical boundary.',[navy,itu])
edit(i,'m67133','import-auto-id1169738083772',replacements=[('radio waves of about 1 kHz are used to communicate with submerged submarines.','radio waves have been used to communicate with submerged submarines; the US Navy used a frequency of about 76 Hz.'),(' (much like ultrasound penetrating tissue)','')])
edit(i,'m67133','import-auto-id1169737819824',caption='Very long wavelength radio signals can reach submerged submarines. Lower-frequency signals penetrate farther into conducting seawater than higher-frequency signals.')
edit(i,'m67133','fs-id1169737817235',inner='radio waves near the low-frequency end of the spectrum, such as the 76-Hz signals formerly used to communicate with submerged submarines')

i=add('Broadcast bands and FM modulation','Update the US band examples and correct a physics error: audio frequency is not the FM frequency deviation. Coordinate the VHF/UHF glossary with the general bands rather than defining them only by TV channels.',[am,fm,tv,itu],'Read the FM paragraph closely. The 75-kHz deviation and 200-kHz channel width are explicit in the regulation.')
edit(i,'m67133','import-auto-id1169738257165',replacements=[('in the frequency range from 540 to 1600 kHz',', with carrier frequencies from 540 to 1700 kHz in the United States'),('signals ,','signals,'),('The resulting wave has a constant frequency, but a varying amplitude.','The carrier frequency remains fixed while its amplitude varies.')])
i['passages'][-1]['authorization']='Maintainer requested placing the US qualification with the frequency allocation, rather than with commercial radio use.'
edit(i,'m67133','import-auto-id1169737826252',replacements=[('but in the frequency range of 88 to 108 MHz','but in a different frequency range: 88 to 108 MHz in the United States')])
i['passages'][-1]['authorization']='Maintainer requested placing the US qualification with the frequency allocation, rather than with commercial radio use.'
edit(i,'m67133','import-auto-id1169737711643',inner='Modulating a carrier with an audio signal produces additional frequency components, called sidebands, above and below the carrier frequency. The width of the frequency band needed to carry a signal is its bandwidth. For FM, transmitting higher audio frequencies or using a greater frequency deviation requires more bandwidth. Stations must be sufficiently separated in frequency for a receiver to select one station’s signal. In the United States, FM broadcast channels are spaced 200 kHz apart, with 100% modulation corresponding to a frequency deviation of 75 kHz above or below the carrier frequency. An FM receiver selects the desired channel and responds to variations in frequency, reproducing the audio information.')
i['passages'][-1]['authorization']='Maintainer requested preserving the instructional connection between audio frequencies, sidebands, bandwidth, station spacing, and receiver tuning. Revised paragraph pending review.'
i['sources'].append(source('NTIA Manual, Annex J: Necessary Bandwidth','https://redbookdev.ntia.gov/view/J-19','Analog FM bandwidth depends on both modulating frequency and peak frequency deviation; Carson rule'))
edit(i,'m67133','import-auto-id1169738220149',replacements=[('each channel requires a larger range of frequencies than simple radio transmission.','each channel requires greater bandwidth than an audio-only radio broadcast.'),('TV channels utilize frequencies in the range of 54 to 88 MHz and 174 to 222 MHz. (The entire FM radio band lies between channels 88 MHz and 174 MHz.)','In the United States, TV channels use frequencies from 54 to 72 MHz, 76 to 88 MHz, and 174 to 216 MHz. (The FM radio band lies between the lower and upper groups.)'),('470 to 1000 MHz','470 to 608 MHz')])
i['sources'].append(source('FCC 22-58: digital television transition','https://docs.fcc.gov/public/attachments/FCC-22-58A1.pdf','Historical analog-to-digital transitions; full-power stations in 2009 and low-power stations in 2021'))
edit(i,'m67133','import-auto-id1169737828306',inner='In older analog television broadcasts, the video signal used AM and the audio used FM. Digital television encodes both picture and sound as digital data. The frequency bands listed above are used for over-the-air broadcasts received by an antenna.')
for e in root('m67133').iter('{'+C+'}definition'):
    term=e.find('{'+C+'}term'); meaning=e.find('{'+C+'}meaning')
    if term is not None and meaning is not None:
        t=''.join(term.itertext()).lower()
        if 'very high frequency' in t:edit(i,'m67133',meaning.get('id'),inner='radio frequencies from 30 to 300 MHz; parts of this band are used for FM radio and television')
        elif 'ultra high frequency' in t.replace('-', ' '):edit(i,'m67133',meaning.get('id'),inner='radio frequencies from 300 to 3000 MHz; parts of this band are used for television and other communications')

i=add('Carrier frequency, information rate, and mobile phones','Information capacity depends on bandwidth and noise, not a universal proportionality to carrier frequency. Keep the 1.90-GHz worked example as an example, and remove the implication that all phones operate there.',[shannon,wireless],'Read the information-rate explanation and connected conceptual question together.')
edit(i,'m67133','import-auto-id1169737715318',replacements=[('Since it is possible to carry more information per unit time on high frequencies, microwaves are quite suitable for communications.','Microwave bands offer wide bandwidths, allowing large amounts of information to be transmitted per unit time.')])
# The coordinated overview box is now handled entirely in P4-18.
edit(i,'m67133','import-auto-id1169738251476',inner='Optical fibers can carry far more telephone conversations than a narrow-band radio link because they offer much greater communication bandwidth. Why would the very narrow bandwidth available for ELF communication limit the information sent to submarines?')
edit(i,'m67133','import-auto-id1169737821880',inner='One reason why we are sometimes asked to switch off our mobile phones on airplanes and in hospitals is that important communications or medical equipment can be affected by radio signals from these devices. MRI scanners, for example, are shielded to prevent outside radio signals from interfering with the signals used to form images.')
edit(i,'m67133','import-auto-id1169737825956',inner='Radio waves used in magnetic resonance imaging (MRI) have frequencies on the order of 100 MHz, although this varies significantly depending on the strength of the magnetic field used and the type of nucleus being scanned. MRI is an important medical imaging and research tool, producing highly detailed two- and three-dimensional images. Radio-frequency pulses excite nuclei, usually hydrogen nuclei (protons), and the resulting radio signals depend on the density of these nuclei and their surroundings.')
edit(i,'m67133','import-auto-id1169738200125',inner='The wavelength of 100-MHz radio waves in vacuum is 3 m, yet MRI can image details smaller than a millimeter. By varying the magnetic field strength with position, the scanner makes the resonant frequency depend on location, allowing signals from different locations to be distinguished. This permits imaging of details much smaller than the radio wavelength.')
for passage in i['passages'][-3:]:
    passage['authorization']='Maintainer accepted the coordinated interference-to-MRI revision and explicitly requested omitting the final tissue-heating/burns sentence as unnecessary in this subsection.'
i['sources'].append(source('NIH NIBIB: Magnetic Resonance Imaging','https://www.nibib.nih.gov/science-education/science-topics/magnetic-resonance-imaging-mri','Radio-frequency excitation and tissue-dependent signals'))
i['sources'].append(source('Manufacturer instructions filed with FDA, H190003C','https://www.accessdata.fda.gov/cdrh_docs/pdf19/H190003C.pdf','Electromagnetic compatibility: RF-shielded room for MRI image quality'))

i=add('Astronomy across the electromagnetic spectrum','Reorganize the subsection around wavelength coverage, detector cooling, atmospheric transmission and space observatories. Include Kepler as a concrete example of measuring starlight; omit launch dates and historical detours.',[jcmt,webb])
edit(i,'m67133','fs-id1169738089178',inner='''<title>Astronomy Across the Electromagnetic Spectrum</title>
<para id="import-auto-id1169738052786">The earliest telescopes, developed in the seventeenth century, collected visible light. Astronomers now use the entire electromagnetic spectrum to investigate stars and the universe. As noted earlier, Penzias and Wilson detected the microwave background radiation originating from the Big Bang.</para>
<para id="import-auto-id1169737993666">Radio telescopes such as the Parkes radio telescope in Australia detect radio waves from astronomical sources. The James Clerk Maxwell Telescope in Hawaii observes at submillimeter wavelengths. Infrared telescopes use cooled detectors to reduce thermal noise. Cooling the telescope itself can also reduce infrared radiation that would otherwise obscure the signal being collected.</para>
<para id="import-auto-id1169737991600">Earth’s atmosphere determines which wavelengths can reach telescopes on the ground. It transmits visible light and some radio and infrared wavelengths, but absorbs much of the ultraviolet radiation and prevents direct observations of astronomical X-rays and gamma rays from the ground. Space telescopes observe beyond this atmospheric barrier.</para>
<para id="import-auto-id1169738145792">The Hubble Space Telescope gathers ultraviolet, visible, and near-infrared light. The Kepler Space Telescope discovered planets orbiting other stars by measuring the small, periodic decreases in starlight when planets passed in front of them. The James Webb Space Telescope observes primarily in the infrared, with wavelength coverage of about 0.6 to 28 μm. The Chandra X-ray Observatory and Fermi Gamma-ray Space Telescope extend these observations to higher frequencies.</para>''')
i['passages'][-1]['authorization']='Maintainer approved the reorganized subsection and clearer heading, including the Kepler transit-method sentence immediately after Hubble, and requested refreshing the preview. Consolidated the earlier three telescope patches into one subsection patch, preserving all section and paragraph IDs.'
for title,url,locator in [
 ('NASA: Kepler / K2','https://science.nasa.gov/mission/kepler/','Planet detection through periodic stellar-brightness dips; mission retired in 2018'),
 ('NASA: Hubble Instruments','https://science.nasa.gov/mission/hubble/observatory/design/instruments/','Ultraviolet, visible and near-infrared coverage'),
 ('NASA: Why Have a Telescope in Space?','https://science.nasa.gov/mission/hubble/overview/why-have-a-telescope-in-space/','Atmospheric transmission and absorption; space-based observations'),
 ('NASA: Wavelength Sensitivity of Observatories','https://science.nasa.gov/asset/webb/wavelength-sensitivity-of-hubble-webb-roman-and-other-observatories/','Chandra X-rays and Fermi gamma rays'),
 ('CSIRO: Parkes radio telescope','https://www.csiro.au/en/about/facilities-collections/ATNF/Parkes-radio-telescope-Murriyang','Ground-based radio astronomy in Australia')]:
    reference=source(title,url,locator);reference['checked']='2026-09-27';i['sources'].append(reference)
i['sources'].append(source('NASA: Webb FAQs','https://science.nasa.gov/mission/webb/faqs-full/','Wavelength coverage about 0.6–28 micrometers, visible red through mid-infrared'))
i['sources'].append(source('East Asian Observatory: JCMT instrumentation','https://www.eaobservatory.org/jcmt/instrumentation/','SCUBA-2 designed for 450 and 850 micrometers; these demonstrate coverage far beyond Webb’s wavelength range'))

i=add('Electromagnetic spectrum: useful relationships','Retain a compact overview of bandwidth and imaging resolution. Remove the universal penetration claim and postpone photon energy until quantum mechanics; coordinate the learning objective.',[attenuation,shannon])
edit(i,'m67132','fs-id1169737846496',inner='<label/><title>Electromagnetic Spectrum: Useful Relationships</title><list id="fs-id1169738074012"><item id="import-auto-id1169737855696">Higher-frequency electromagnetic waves allow greater communication bandwidth and faster information transmission.</item><item id="import-auto-id1169738145674">In conventional imaging, shorter wavelengths allow finer details to be resolved.</item></list>',removed_ids=('import-auto-id1169737718925','import-auto-id1169738011754','import-auto-id1169737812361'))
i['passages'][-1]['authorization']='Maintainer approved the two-relationship box without photon references and requested implementing it; removes the introductory three-rules sentence, energy/penetration bullet, and exceptions sentence.'
edit(i,'m67132','abstract',replacements=[('List three “rules of thumb” that apply to the different frequencies along the electromagnetic spectrum.','Describe how communication bandwidth and imaging resolution relate to electromagnetic waves.')])
i['passages'][-1]['authorization']='Maintainer approved the coordinated learning objective.'

# Contextual corrections requested during the full-spectrum section read-through.
i=add('UV exposure: damage and the tanning response','Remove the unsupported backward reference Again; combine the two paragraphs and explain DNA damage before the tanning response. Tanning is pigment production, not a mutation itself.',[source('FDA: The Risks of Tanning','https://www.fda.gov/radiation-emitting-products/tanning/risks-tanning','UV damage, mutations and increased melanin production'),source('FDA: Ultraviolet (UV) Radiation','https://www.fda.gov/radiation-emitting-products/tanning/ultraviolet-uv-radiation','Sunburn, premature aging and skin cancer')],'Maintainer requested this order and a single paragraph during contextual review.')
edit(i,'m67133','import-auto-id1169738116930',replacements=[('Again, treatment is often successful if caught early.','Treatment is often successful if the cancer is caught early.')])
edit(i,'m67133','import-auto-id1169738116932',inner='UV radiation can damage collagen fibers, resulting in an acceleration of the aging process of skin and the formation of wrinkles. Large UV exposures can cause sunburn, and repeated exposure increases the risk of skin cancer. Some studies indicate a link between overexposure to the Sun when young and melanoma later in life. UV-B radiation can damage DNA molecules, leading to mutations and the possible formation of cancerous cells. The tanning response is a defense mechanism in which the body produces the pigment melanin to absorb some of the UV radiation reaching the skin.')
remove(i,'m67133','import-auto-id1169737786070')
# Join the short immune-effects paragraph to the preceding exposure-effects paragraph.
previous=node('m67133','import-auto-id1169738163690')
immune=node('m67133','import-auto-id1169737805853')
edit(i,'m67133','import-auto-id1169738163690',inner=''.join(previous.itertext()).strip()+' '+''.join(immune.itertext()).strip())
remove(i,'m67133','import-auto-id1169737805853')
for passage in i['passages']:
    passage['authorization']='Maintainer requested removing Again, repairing the early-treatment sentence, moving the DNA-damage sentence before tanning, and combining the two paragraphs with necessary smoothing. Removed the misleading low-UV causal clause and description of pigment as confined to inert skin layers; no incoming textbook links target the removed paragraph.'

edit(i,'m67133','import-auto-id1169738076737',inner='Ultraviolet radiation is used to disinfect air, water, and exposed surfaces. UV-C absorbed by microorganisms damages their DNA or RNA, preventing reproduction. This is a chemical effect of the absorbed radiation, rather than simply heating the material. Higher-frequency electromagnetic waves, including X-rays and gamma rays, have similar uses in treating food and sterilizing medical equipment.')
i['passages'][-1]['relocate_before']='import-auto-id1169738181660'
i['passages'][-1]['authorization']='Maintainer approved the UV-disinfection replacement and its extension connecting X-rays and gamma rays to food treatment and medical-equipment sterilization, then requested removing the ionizing-radiation definition to avoid implying that UV disinfection operates through ionization.'
for title,url,locator in [
 ('FDA: Food Irradiation: What You Need to Know','https://www.fda.gov/food/buy-store-serve-safe-food/food-irradiation-what-you-need-know','Gamma rays and X-rays in food irradiation; gamma sterilization of medical products'),
 ('FDA: Germicidal UV Executive Summary','https://www.fda.gov/media/190054/download','Germicidal UV uses non-ionizing radiation; microbial genetic-material damage'),
 ('CDC: About Germicidal Ultraviolet','https://www.cdc.gov/niosh/ventilation/germicidal-ultraviolet/index.html','UV inactivation of microorganisms')]:
    reference=source(title,url,locator)
    reference['checked']='2026-09-27'
    i['sources'].append(reference)

edit(i,'m67133','import-auto-id1169737821647',replacements=[('The UV radiation helps dissociate the CFC’s, releasing highly reactive chlorine (Cl) atoms, which catalyze the destruction of the ozone layer.','In the stratosphere, UV radiation dissociates CFC molecules, releasing highly reactive chlorine (Cl) atoms, which catalyze the destruction of ozone.')])
i['passages'][-1]['authorization']='Maintainer approved the direct photodissociation wording and requested refreshing the contextual preview.'
reference=source('NOAA: South Pole Ozone Hole','https://gml.noaa.gov/dv/spo_oz/doc.html','Solar ultraviolet breaks down stratospheric CFCs, freeing chlorine for catalytic ozone destruction')
reference['checked']='2026-09-27'
i['sources'].append(reference)

edit(i,'m67133','import-auto-id1169737924026',replacements=[('most UVB gets blocked by the atmosphere.','most UVB gets blocked by the atmosphere. UV radiation is also used in the treatment of some skin conditions.')])
i['passages'][-1]['authorization']='Maintainer requested combining the skin-treatment sentence with the health-benefits paragraph.'
edit(i,'m67133','import-auto-id1169738181660',replacements=[('When exposed to ultraviolet,','UV radiation is also used as an analytical tool to identify substances. When exposed to ultraviolet,')])
i['passages'][-1]['authorization']='Maintainer requested combining the analytical-use sentence with the following fluorescence and microscopy paragraph.'
remove(i,'m67133','import-auto-id1169738209359')
i['passages'][-1]['authorization']='Maintainer requested moving the disinfection explanation into Benefits of UV Light. Remove its duplicate here; remove the erroneous UV-jaundice example because neonatal jaundice phototherapy uses visible blue light.'
reference=source('Cambridge University Hospitals: Jaundice in newborn babies','https://www.cuh.nhs.uk/patient-information/jaundice-in-newborn-babies-/','Neonatal phototherapy uses blue light, not UV')
reference['checked']='2026-09-27'
i['sources'].append(reference)

# Standardize UV band notation across the current revision, preserving baseline XML.
edit(i,'m67133','import-auto-id1169737790024',replacements=[('UV-A (315','UVA (315'),('UV-B (280','UVB (280'),('UV-C (100','UVC (100'),('Most UV-B and all UV-C','Most UVB and all UVC'),('is UV-A.','is UVA.')])
for group in items:
    for passage in group['passages']:
        if passage.get('proposed_xml'):
            normalized=re.sub(r'\bUV[-‐‑–]([ABC])\b',r'UV\1',passage['proposed_xml'])
            if normalized != passage['proposed_xml']:
                passage['proposed_xml']=normalized
                passage['notation_note']='Maintainer requested consistent UV-band notation; use UVA, UVB, UVC, following WHO, CDC and FDA.'
i['passages'][-1]['authorization']='Maintainer requested standardizing UV-band notation to the common convention; UVA, UVB and UVC are used by WHO, CDC and FDA.'
reference=source('CDC: Ultraviolet Radiation','https://www.cdc.gov/radiation-health/features/uv-radiation.html','Notation UVA, UVB, UVC for all three bands')
reference['checked']='2026-09-27'
i['sources'].append(reference)

edit(i,'m67133','import-auto-id1169737733747',inner='In 1895, Wilhelm Conrad Röntgen discovered an invisible, penetrating form of radiation while experimenting with high-voltage electrical discharges in tubes filled with rarefied gases. He called this radiation <term id="import-auto-id1169738134377">X-rays</term> because its nature was unknown. X-rays were later established to be very high frequency electromagnetic radiation.')
i['passages'][-1]['authorization']='Maintainer approved replacing the anonymous discovery account with the Röntgen paragraph, distinguishing discovery in 1895 from later identification as electromagnetic radiation.'
reference=source('Nobel Prize: A helping hand from the media','https://www.nobelprize.org/prizes/physics/1901/perspectives/?print=1','Röntgen discovery of X-rays in 1895')
reference['checked']='2026-09-27'
i['sources'].append(reference)

edit(i,'m67133','import-auto-id1169738257444',inner='The first method is illustrated in '+links('m67133','import-auto-id1169738257444')[0]+'. An electron accelerated through a sufficiently large voltage strikes a metal target, such as copper, and ejects an inner-shell electron—one relatively close to and tightly bound to the nucleus—from one of its atoms. An electron from a higher-energy shell then fills the vacancy, releasing the energy difference as an X-ray. Since the electron energy levels are characteristic of the element, so is the energy of the emitted radiation, hence the name characteristic X-ray.')
i['passages'][-1]['authorization']='Maintainer approved the coordinated characteristic-X-ray explanation, caption and following-paragraph corrections.'
edit(i,'m67133','import-auto-id1169738193776',replacements=[('../../media/Figure 25_03_13a.jpg','../../../proposals/1.1/assets/characteristic-xray-revised-draft.png'),('mime-type="image/jpg"','mime-type="image/png"'),('width="200"','width="350"'),(node('m67133','import-auto-id1169738193776').find('{'+C+'}media').get('alt'),'Two-panel schematic of characteristic X-ray production. Above, an incoming electron ejects an inner-shell electron and both leave the atom. Below, a bound electron on an outer shell moves into the inner-shell vacancy; a red wavy arrow represents the emitted X-ray.')],caption='An energetic electron strikes an atom and ejects an inner-shell electron. An electron from a higher-energy shell then fills the vacancy, and the energy released is emitted as an X-ray. (Adapted from OpenStax, College Physics, CC BY 4.0; illustration revised.)')
i['passages'][-1]['asset_manifest']='proposals/1.1/assets/characteristic-xray-revised-draft.json'
i['passages'][-1]['authorization']='Maintainer approved correcting the caption from external electron recapture to an internal shell transition.'
i['passages'][-1]['artwork_status']='Resolved: maintainer approved the revised illustration on 2026-09-27. Preview now uses an outer-shell electron transition; original retained unchanged.'
remove(i,'m67133','import-auto-id1169738013735')
i['passages'][-1]['authorization']='Maintainer requested merging the inner-shell definition and characteristic-X-ray explanation into the first-method paragraph and removing the redundant following paragraph. The figure now separates the first and second methods. No incoming textbook references target the removed paragraph.'
reference=source('Nobel Prize: What are X-rays?','https://educationalgames-staging.nobelprize.org/educational/physics/x-rays/what.php','Characteristic X-rays arise when an electron farther from the nucleus fills an inner-shell vacancy')
reference['checked']='2026-09-27'
i['sources'].append(reference)

edit(i,'m67133','import-auto-id1169738013737',inner='In the second method, energetic electrons entering a material are deflected by the electric fields of atomic nuclei. Accelerated charges radiate electromagnetic waves, so the electrons lose energy by emitting radiation, which can include X-rays. This radiation is called bremsstrahlung (German for “braking radiation”). The electrons can lose different amounts of energy in these encounters, producing a continuous spectrum of X-ray energies rather than the distinct energies of characteristic X-rays.')
i['passages'][-1]['authorization']='Maintainer requested a single flowing explanation of bremsstrahlung, removing the indirect collision-energy-transfer account and references to Figure 11.5.11.'
remove(i,'m67133','import-auto-id1169737728963')
i['passages'][-1]['authorization']='Maintainer requested removing Figure 11.5.11; remove its otherwise empty containing paragraph as well. Its only incoming textbook link was in the replaced second-method paragraph. Historical media remains preserved.'
remove(i,'m67133','import-auto-id1169737918071')
i['passages'][-1]['authorization']='Maintainer requested merging the second-method explanation into a single paragraph before the removed figure.'

edit(i,'m67133','import-auto-id1169737818583',replacements=[('However, questions have risen in recent years as to accidental overexposure of some people during CT scans—a mistake at least in part due to poor monitoring of radiation dose.','In 2009–2010, an FDA investigation documented accidental radiation overexposure during CT brain-perfusion scans, highlighting the importance of appropriate scan settings and dose monitoring.')])
i['passages'][-1]['authorization']='Maintainer approved replacing the vague recent-years claim with the documented 2009–2010 FDA investigation and requested refreshing the preview.'
reference=source('FDA: Working to Prevent Radiation Overdoses During CT Scans (2010 announcement)','https://www.prnewswire.com/news-releases/fda-working-to-prevent-radiation-overdoses-during-ct-scans-106956278.html','FDA-issued announcement: brain-perfusion CT overexposures, improper scanner use and dose-safety improvements')
reference['checked']='2026-09-27'
i['sources'].append(reference)

edit(i,'m67133','import-auto-id1169737830998',replacements=[('Madame Marie Curie','Marie Curie')])
i['passages'][-1]['authorization']='Maintainer approved removing the honorific Madame from this paragraph and requested refreshing the preview.'

edit(i,'m76584','import-auto-id1514494',replacements=[('Marie Curie (1867–1934) began','Marie Skłodowska-Curie (1867–1934), often known as Marie Curie, began')])
i['passages'][-1]['authorization']='Maintainer requested the fuller name and familiar-name clarification in Section 14.2, beside the introduction of Pierre Curie, rather than in the earlier portrait caption.'

edit(i,'m67133','import-auto-id1169737727678',replacements=[('The most penetrating nuclear radiation was called a','The most penetrating of these three types of radiation was called a'),(' (again a name given because its identity and character were unknown), and it was later found to be an extremely high frequency electromagnetic wave.',' , continuing the naming sequence of alpha and beta rays. It was later found to be an extremely high frequency electromagnetic wave.')])
i['passages'][-1]['proposed_xml']=i['passages'][-1]['proposed_xml'].replace('</emphasis> ,','</emphasis>,')
i['passages'][-1]['authorization']='Maintainer approved explaining gamma as continuing the alpha/beta naming sequence, rather than a placeholder for unknown nature; preserve the following identification as electromagnetic radiation.'
reference=source('Leif Gerward: The Discovery of Gamma Rays, IRPS Bulletin 14(1)','https://www.ph.unimelb.edu.au/~chantler/opticshome/irps/pdfs/bulletins/14-1.pdf','Villard discovery and Rutherford alpha/beta/gamma nomenclature')
reference['checked']='2026-09-27'
i['sources'].append(reference)

edit(i,'m67133','import-auto-id1169738118044',inner='Gamma rays have characteristics identical to X-rays of the same frequency—they differ only in source. Gamma rays often have higher frequencies than diagnostic X-rays and can penetrate more deeply into the body. They have many of the same uses as X-rays, including cancer therapy. Gamma radiation from radioactive materials is used in nuclear medicine. '+links('m67133','import-auto-id1169738202131')[0]+' shows a medical image based on '+xml(node('m67133','import-auto-id1169738202131').find('{'+M+'}math'))+' rays.')
i['passages'][-1]['authorization']='Maintainer approved preserving the comparison with diagnostic X-rays while removing the unsupported claim that higher frequency necessarily means greater biological damage.'
reference=source('NIST: X-Ray Mass Attenuation Coefficients — Soft Tissue (ICRU-44)','https://physics.nist.gov/PhysRefData/XrayMassCoef/ComTab/tissue.html','Energy-dependent attenuation and energy absorption in soft tissue; distinguish penetration from deposited energy')
reference['checked']='2026-09-27'
i['sources'].append(reference)

food_before=xml(node('m67133','import-auto-id1169738202131'))
food_prefix=food_before[food_before.index('>')+1:food_before.index('Damage to food cells')]
edit(i,'m67133','import-auto-id1169738202131',replacements=[(food_prefix,'Exposing food to gamma radiation can greatly inhibit spoilage by killing the microorganisms that cause it. '),('Damage to food cells through irradiation occurs as well, and the long-term hazards of consuming radiation-preserved food are unknown and controversial for some groups.','Food irradiation under approved conditions is considered safe by the FDA and does not make the food radioactive.')])
i['passages'][-1]['authorization']='Maintainer approved the food-spoilage sentence replacement and moving the medical-image reference to the end of the preceding nuclear-medicine paragraph; preserve the figure target. Maintainer also approved replacing the unsupported long-term-hazards sentence with: Food irradiation under approved conditions is considered safe by the FDA and does not make the food radioactive.'

edit(i,'m67133','import-auto-id1169736610636',caption='This bone scan shows gamma rays emitted by a radioactive tracer that accumulates in bone, while unbound tracer is eliminated through the kidneys. Differences in tracer uptake reveal patterns of bone activity and help locate abnormalities. (credit: P. P. Urone)')
i['passages'][-1]['authorization']='Maintainer approved the revised bone-scan caption: explain tracer uptake and renal elimination, replacing the unverified cancer diagnosis with patterns of bone activity and abnormalities.'
reference=source('RadiologyInfo: Bone Scan','https://www.radiologyinfo.org/en/info/bone-scan','Injected tracer binds to bones; unused tracer is excreted in urine. Abnormal uptake can reflect fractures, infection, cancer or other conditions.')
reference['checked']='2026-09-27'
i['sources'].append(reference)

edit(i,'m67133','import-auto-id1169738110508',replacements=[('Any electromagnetic wave produced by currents in wires is classified as a radio wave, the lowest frequency electromagnetic waves.','Radio waves occupy the lowest-frequency region of the electromagnetic spectrum and can be produced by oscillating currents in antennas.')])
i['passages'][-1]['authorization']='Maintainer approved the radio-wave summary opening; retain the following sentence about applications and microwaves.'
edit(i,'m67133','import-auto-id1169737805011',replacements=[('X-rays are created in high-voltage discharges and by electron bombardment of metal targets.','X-rays can be produced when energetic electrons are deflected by atomic nuclei or when electrons fill vacancies in inner atomic shells.')])
i['passages'][-1]['authorization']='Maintainer approved aligning the X-ray summary with the two mechanisms explained in the revised subsection; retain the frequency-overlap sentence.'
edit(i,'m67133','import-auto-id1169737814627',inner='Gamma rays are emitted in nuclear processes and other high-energy processes. Their frequencies overlap those of X-rays and extend to the highest-frequency region of the electromagnetic spectrum.')
i['passages'][-1]['authorization']='Maintainer approved the gamma-ray summary replacement, including non-nuclear high-energy sources and overlap with X-rays.'
for title,url,locator in [
 ('NASA: Radio Waves','https://science.nasa.gov/ems/05_radiowaves/','Low-frequency region of the spectrum, radio astronomy and microwaves'),
 ('NASA: Gamma Rays','https://science.nasa.gov/ems/12_gammarays/','Nuclear and astronomical high-energy sources of gamma radiation')]:
    reference=source(title,url,locator);reference['checked']='2026-09-27';i['sources'].append(reference)

# Fold existing glossary-child corrections into one guarded glossary patch so
# additions and revised definitions are applied together without overlapping edits.
spectrum_glossary=copy.deepcopy(node('m67133','glossary'))
glossary_ids={e.get('id') for e in spectrum_glossary.iter() if e.get('id')}
absorbed=[]
for group in items:
    for p in list(group['passages']):
        if p['module']=='m67133' and p['source_id'] in glossary_ids:
            old=next(e for e in spectrum_glossary.iter() if e.get('id')==p['source_id'])
            parent=next(e for e in spectrum_glossary.iter() if old in list(e))
            pos=list(parent).index(old);new=E.fromstring(p['proposed_xml']);new.tail=old.tail
            parent.remove(old);parent.insert(pos,new)
            absorbed.append(dict(review_item=group['id'],source_id=p['source_id']))
            group['passages'].remove(p)
for term,meaning in {
 'radio waves':'electromagnetic waves in the lowest-frequency region of the spectrum, including microwaves',
 'infrared radiation (IR)':'electromagnetic radiation with wavelengths longer than visible red light, extending toward the microwave region',
 'gamma ray':'high-frequency electromagnetic radiation emitted in nuclear processes and other high-energy processes; its frequency range overlaps that of X-rays',
 'amplitude modulation (AM)':'a method of carrying information by varying the amplitude of a carrier wave',
 'frequency modulation (FM)':'a method of carrying information by varying the frequency of a carrier wave while keeping its amplitude constant',
 'thermal agitation':'the random motion of atoms and molecules associated with temperature',
 'radar':'a system that uses reflected radio waves to detect objects and determine their distance or motion',
}.items():
    definition=next(d for d in spectrum_glossary if d.find('{'+C+'}term').text==term)
    meaning_node=definition.find('{'+C+'}meaning')
    for child in list(meaning_node):meaning_node.remove(child)
    meaning_node.text=meaning
for key,term,meaning in [
 ('bandwidth','bandwidth','the width of the frequency band needed to carry a signal'),
 ('sidebands','sidebands','frequency components produced by modulation above and below the carrier frequency'),
 ('characteristic-x-ray','characteristic X-ray','an X-ray emitted when an electron fills an inner-shell vacancy, with an energy characteristic of the element'),
 ('bremsstrahlung','bremsstrahlung','electromagnetic radiation emitted when moving charged particles are deflected or slowed; German for “braking radiation”'),
]:
    definition=E.SubElement(spectrum_glossary,'{'+C+'}definition',{'id':'glossary-'+key})
    E.SubElement(definition,'{'+C+'}term').text=term
    E.SubElement(definition,'{'+C+'}meaning',{'id':'meaning-'+key}).text=meaning
spectrum_glossary[:]=sorted(spectrum_glossary,key=lambda d: ''.join(d.find('{'+C+'}term').itertext()).strip().casefold())
edit(i,'m67133','glossary',inner=''.join(xml(child) for child in spectrum_glossary))
i['passages'][-1]['absorbed_glossary_patches']=absorbed
i['passages'][-1]['authorization']='Maintainer approved seven revised definitions and four new glossary entries, then requested alphabetizing this section glossary; preserve earlier ELF/VHF/UHF corrections and all existing entry IDs.'
for source_id,terms in [
 ('import-auto-id1169737711643',['sidebands','bandwidth']),
 ('import-auto-id1169738257444',['characteristic X-ray']),
 ('import-auto-id1169738013737',['bremsstrahlung']),
]:
    p=next(p for group in items for p in group['passages'] if p['module']=='m67133' and p['source_id']==source_id)
    for term in terms:
        key=term.lower().replace(' ','-')
        assert term in p['proposed_xml']
        p['proposed_xml']=p['proposed_xml'].replace(term,f'<term xmlns="{C}" id="term-{key}">{term}</term>',1)
    p['term_markup_authorization']='Maintainer requested bold first appearances of the four new glossary terms; use semantic CNXML term markup.'

coin_checks={
 'total_100_coin_microstates':2**100,
 '50_heads_microstates':math.comb(100,50),
 '50_heads_probability':math.comb(100,50)/2**100,
 '45_through_55_probability':sum(math.comb(100,k) for k in range(45,56))/2**100,
 '40_through_60_probability':sum(math.comb(100,k) for k in range(40,61))/2**100,
 'all_heads_or_tails_mean_wait_years_at_one_toss_per_second':2**99/(365.25*86400)}
dispositions=[
 dict(topic='Brain-current and high-frequency skin-only claims',disposition='Already corrected',reason='F2-11 is present in maintained m52406: high-frequency heating can occur inside the body and cause burns; the brain/heart assertion is gone. No duplicate correction.',source='proposals/1.1/fact-check-cycle2.json'),
 dict(topic='100-coin numerical examples',disposition='Verified unchanged',reason='Binomial counts reproduce the rounded 8%, 73%, 96%, and 2 × 10^22 years. Independent calculation is stored in this packet.',calculations=coin_checks),
 dict(topic='Clausius spelling',disposition='No established error',reason='The University of Bonn uses Rudolph as well as Rudolf. Preserve the existing name; revise only the priority claim.',url='https://www.uni-bonn.de/en/research-and-teaching/research-profile/transdisciplinary-research-areas/tra-matter/200-years-rudolph-clausius'),
 dict(topic='Three Gorges height',disposition='Verified unchanged',reason='181 m is maximum dam height; 185 m is crest elevation, a different quantity. Do not substitute the latter.',url=dam['url']),
 dict(topic='Arecibo',disposition='No present-operation claim to correct',reason='The existing sentence describes telescopes that “were designed.” No current operational status or superlative is asserted.'),
 dict(topic='1.90-GHz phone calculation',disposition='Retained as a valid example',reason='The frequency is physically valid as an example; the blanket claim about all phones is separately removed.'),
 dict(topic='Entropy/disorder in the preceding section',disposition='Retain the approved Priority 3 wording',reason='Do not remove all association with disorder or reopen the approved macroscopic treatment. The microscopic section now explains the intended statistical meaning.'),
]
# Maintainer completed all P4 comparisons and contextual reading on 2026-09-27.
for item in items:
    if item['id'].startswith('P4-'):
        item['status']='approved-pending-application'
        item['authorization']='Maintainer approved all P4 items and completed the contextual section review on 2026-09-27, including spectrum prose, artwork, summaries and glossary corrections. No P4 review decisions remain; coordinated P3/P4 source application remains pending.'
        for passage in item['passages']:
            passage['status']='approved-pending-application'
            passage.setdefault('authorization',item['authorization'])

for item in items:
    if item['id']=='P4-07':
        item['attention']='Full section and glossary approved, including removal of the Check Your Understanding comparison of special and general relativity.'

packet=dict(date='2026-09-25',status='Review complete and approved 2026-09-27; awaiting coordinated P3/P4 application',scope='Recorded entropy/disorder, electrical-safety, historical and technology leads, plus directly connected inconsistencies. This is not a full-book numerical certification or an exercise revision.',base_policy='Layer these proposals after the approved Priority 3 and heat-engine overlays. Before XML and source hashes guard against overwriting those changes.',items=items,dispositions=dispositions)
(ROOT/'proposals/1.1/priority4-followup-review.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Reuse the book renderer, including native MathML and numbered references.
sys.path.insert(0,str(ROOT/'prototype'));sys.argv=['build.py','course','--all']
ns={'__file__':str(ROOT/'prototype/build.py'),'__name__':'review_renderer'}
s=(ROOT/'prototype/build.py').read_text(encoding='utf-8')
exec(compile(s.split('OUT.mkdir(parents=True,exist_ok=True);')[0],ns['__file__'],'exec'),ns)
out=ROOT/'prototype/dist/review-1.1/priority4-review';out.mkdir(parents=True,exist_ok=True);ns['OUT']=out
for mid,r in roots.items():ns['roots'][mid]=r
ns['parents']={m:{c:e for e in r.iter() for c in e} for m,r in ns['roots'].items()}
ns['objects']=ns['build_objects'](ns['sections'],ns['roots'],'course',ns['course'],ns['load']('maintained/numbering.json'),ns['anchor'])
esc=html.escape
def render(mid,text):
    if text is None:return '<p><em>Removed, including the question and its answer.</em></p>'
    e=E.fromstring(text)
    if e.tag=='{http://cnx.rice.edu/mdml}abstract':e.tag='{'+C+'}content'
    result=ns['Renderer'](mid).render(e)
    if e.tag=='{'+C+'}meaning':result='<p>'+result+'</p>'
    result=re.sub(r'\s+id="[^"]*"','',result)
    slug=ns['registry'][mid]['candidate_slug'];base='/course-full/sections/'+slug+'/index.html'
    result=re.sub(r'href="#([^"]+)"',lambda m:'href="'+base+'#'+m[1]+'"',result)
    return result.replace('href="../','href="/course-full/sections/').replace('src="../../media/','src="media/')
page=['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Priority 4 — factual-audit follow-ups</title><style>body{max-width:1280px;margin:auto;padding:24px;font:18px/1.55 Georgia;color:#233c43}a{color:#075e76;overflow-wrap:anywhere}section{border-top:1px solid #abc;padding-top:16px;margin-top:32px}.compare{display:grid;grid-template-columns:1fr 1fr;gap:20px}.cell{min-width:0;background:#f2f6f7;padding:16px;overflow:auto}.note{background:#fff3d6;padding:14px}math{font-size:1.05em}img{max-width:100%;height:auto}figure{margin:10px 0}.source{font-size:.88em} @media(max-width:750px){.compare{grid-template-columns:1fr}}h3{font-size:1.05em}</style></head><body><h1>Factual-audit follow-ups: Priority 4</h1><p>18 proposed groups. Nothing on this page has been applied to the maintained textbook. “Before” includes approved Priority 3 edits where applicable. Final application of Priority 3 and this batch remains coordinated.</p><p class="note"><strong>Closest reading:</strong> P4-01–03 (entropy), P4-07 (Michelson–Morley), P4-09 (radiocarbon calibration), and P4-15–16 (radio physics). The other groups are mostly local repairs. Source links and precise locations follow each group. External sources support facts; no outside prose or artwork is imported.</p><p><a href="../priority3-sections/">Approved Priority 3 section previews</a> · <a href="#dispositions">Verified or already-resolved leads</a></p><ol>']
for i in items:page.append('<li><a href="#'+i['id']+'">'+i['id']+' — '+esc(i['title'])+'</a></li>')
page.append('</ol>')
for i in items:
    approval='<p><strong>Approved — awaiting coordinated application.</strong></p>' if i['status']=='approved-pending-application' else ''
    page.append('<section id="'+i['id']+'"><h2>'+i['id']+' — '+esc(i['title'])+'</h2>'+approval+'<p class="note">'+esc(i['attention'])+'</p><p>'+esc(i['reason'])+'</p>')
    for p in i['passages']:
        mid=p['module'];slug=ns['registry'][mid]['candidate_slug']
        base='/review-1.1/priority3-sections/' if '/priority3-sections/' in p['source_path'] else '/course-full/'
        context_id='import-auto-id2502341' if p.get('source_selector')=='glossary' else p['source_id']
        url=base+'sections/'+slug+'/index.html#'+mid+'--'+context_id.encode().hex()
        if p.get('source_selector')=='abstract':url=base+'sections/'+slug+'/index.html'
        page.append('<p><a href="'+url+'">'+esc(ns['registry'][mid]['title'])+' — context before this proposal</a></p><div class="compare"><div class="cell"><h3>Before</h3>'+render(mid,p['before_xml'])+'</div><div class="cell"><h3>Proposed for 1.1</h3>'+render(mid,p['proposed_xml'])+'</div></div>')
    for key in ['source_caution','evidence_note','exercise_note']:
        if i.get(key):page.append('<p class="note">'+esc(i[key])+'</p>')
    page.append('<ul class="source">')
    for s in i['sources']:
        page.append('<li><a href="'+esc(s['url'])+'">'+esc(s['title'])+'</a> — '+esc(s['locator'])+(' · <a href="'+esc(s['accessible_full_text'])+'">Accessible paper text</a>' if s.get('accessible_full_text') else '')+'</li>')
    page.append('</ul></section>')
page.append('<section id="dispositions"><h2>Verified or already-resolved leads</h2>')
for d in dispositions:
    page.append('<h3>'+esc(d['topic'])+' — '+esc(d['disposition'])+'</h3><p>'+esc(d['reason'])+'</p>')
page.append('<p>This targeted review does not certify every untouched historical sentence, numerical example, or exercise. The separately planned conceptual-exercise revision remains open.</p></section></body></html>')
report=ROOT/'reports/1.1/priority4-review';report.mkdir(parents=True,exist_ok=True)
shutil.copytree(out/'media',report/'media',dirs_exist_ok=True)
for directory in [out,report]:(directory/'index.html').write_text('\n'.join(page),encoding='utf-8')
print(f'Prepared {len(items)} groups, {sum(len(i["passages"]) for i in items)} comparisons; maintained source untouched.')
