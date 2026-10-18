"""Generate a review-only Chapter 14 disposition packet; never edit textbook or export."""
from pathlib import Path
import json, hashlib, html, collections
R=Path(__file__).resolve().parents[1]
OUT=R/'reports/1.1/chapter14-structure'
items=json.loads((OUT/'exercise-inventory-current.json').read_text(encoding='utf-8'))
export=R.parent/'reference-inputs/phys-10-full-export-2026-09-27.imas'
data=json.loads(export.read_bytes())
inv=json.loads((R/'reports/1.1/mom-exercise-planning/inventory.json').read_text(encoding='utf-8'))
assert hashlib.sha256(export.read_bytes()).hexdigest()==inv['source_sha256']
assessments=[a for a in inv['assessments'] if a['export_item_id'] in ['72','73','74','75','76','79','82']]
active=sorted({q for a in assessments for q in a['question_set_ids']},key=int)
assert len(active)==43
snap={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'maintained/modules').glob('*/index.cnxml')}

# Each row has an individually reviewed disposition. Grouped removals share a reason.
D={}
def remove(nums,reason):
 for n in nums:D[n]=dict(action='Remove',reason=reason,level='—',proposed=None,major=False)
def keep(n,reason,level='Core'):
 D[n]=dict(action='Keep',reason=reason,level=level,proposed=None,major=False)
def revise(n,reason,prompt,level='Core',major=False):
 D[n]=dict(action='Revise',reason=reason,level=level,proposed=prompt,major=major)

remove([3],'Collision energy-transfer explanation is a mechanics extension beyond the chapter’s radiation-identification and ionization goals.')
remove([7],'The comparison changes both particle and absorber, making the intended lesson less clear; revised 8 provides a controlled shielding comparison.')
remove([13,14],'Gas heating, current and avalanche-gain calculations add several earlier-course calculation steps without strengthening the required detector concepts.')
remove([19,20,21,22,27],'Nuclear radius/density computation or derivation is outside the export’s isotope-counting level; 18 will supply the missing basic counting practice.')
remove([23,24,26,28],'Unit-precision, velocity, wavelength or relativistic calculations are peripheral here; mass–energy meaning remains in 5 and optional 153.')
remove([29],'Antimatter trapping and hypothetical propulsion are peripheral; 45 and 166 retain more focused antiparticle reasoning.')
remove([31],'Supernova time-of-flight mass limits need assumptions about emission timing and duplicate 169; proposed 169 instead addresses the actively assessed solar-neutrino problem.')
remove([34,36,38,40,41,42,43,44],'Reduce repetitive decay bookkeeping to one supplied-Z example per decay mode in 33, 35, 37 and 39. Reverse-parent identification is not needed for this level.')
remove([46,48,49],'Repeated formal conservation tallies are redundant with the selected decay examples and optional 47.')
remove(list(range(50,60)),'Mass-table Q-value calculations and atomic-versus-nuclear mass bookkeeping exceed the export’s numerical level; representative decay equations remain without energy arithmetic.')
remove([64,65,66],'Detailed binding-energy qualifications are unnecessary here; 63, 112 and 133 retain the conceptual mass–energy and stability connections.')
remove(list(range(69,77)),'Activity-to-mass or half-life inversion requires atom counting, unit conversions and decay-constant calculations beyond the active homework; replace this emphasis with repeated halving in 67–68.')
remove([77,78,79,80,81,82],'Noninteger exponential decay, logarithmic inversion or coupled isotope abundances exceed the repeated-halving level; the same central lesson is covered by 67–68.')
remove([84,85,86,87],'Long activity/mass/power calculations and dated product or mission framing add workload without a new core objective. No need to repair these historical details if the exercises are removed.')
remove([91,94,95,96],'Radiopharmaceutical production energies and activity-to-mass arithmetic are beyond the diagnostic-method and short-half-life goals.')
remove([99],'RBE versus radiation-weighting-factor terminology is beyond the lecture’s stated scope; retain the distinction in prose without requiring this exercise.')
remove([101],'Radon-in-buildings application overlaps 98; retain one focused radon question.')
remove([102],'Differences in tumor radiosensitivity require biological detail beyond the chapter’s physics objectives.')
remove([104,105,106,107],'Detailed Gy/Sv conversion and treatment-dose exercises are not emphasized in the lecture. They also require careful absorbed/equivalent/effective-dose distinctions; do not retain their current generic “dose” framing.')
remove([108],'Repeated-layer attenuation is already retained as optional 25; a second near-identical shielding calculation is unnecessary.')
remove([109],'Remove the dated “maximum allowable” premise and unsupported individualized yearly-cancer/genetic-risk calculation; 100 and 103 retain appropriate conceptual protection/risk reasoning.')
remove([110,111],'Photon-energy or activity-to-mass arithmetic contributes little to the selected biological-effects objectives.')
remove([115],'Detailed capture of energy from a particular radiative fusion channel is peripheral to the fusion comparison and barrier concepts.')
remove([116,117,118],'Full reaction-by-reaction conservation and Q-value accounting is excessive; optional 119 checks the overall process without mass-table calculations.')
remove([120,121,122,123,124,125],'Fuel inventory, neutron-capture energy and solar-flux arithmetic exceed the selected level. Solar-neutrino conceptual coverage is supplied by proposed 169.')
remove([126,127,128],'The full CNO cycle and repeated conservation/energy accounting are additional stellar-nuclear detail beyond this conceptual course.')
remove([129,130,131,132],'Integrated laser, recoil, Coulomb-barrier temperature and global fuel-inventory calculations are substantially above the active homework level.')
remove([134],'Neutron moderation via two-body collision reasoning is an optional mechanics application already omitted at 3; reactor control can be addressed conceptually in 138.')
remove([135],'The dated Chernobyl rain premise invites an underdetermined inference from measured activity to chain reactions; 137–138 teach the intended reactor concepts directly.')
remove([139],'Odd/even neutron-number reasoning is too specialized and should not be presented as a universal fissility rule.')
remove([141,143],'Repeated fission Q-value calculations are beyond scope; 142 retains one simple nucleon/charge balance.')
remove([144,145,146],'Breeding chains, Q-values and neutron-parity rules are extra nuclear-fuel-cycle detail. Exercise 145 also contains the outdated Chernobyl-purpose claim removed from prose.')
remove([147,148],'Multistep reactor thermal power, fission rate, fuel consumption and activity conversions exceed the intended numerical level.')
remove([149,150,151],'Weapon material selection, explosive direction and thermonuclear-fuel production are peripheral to the selected conceptual objectives. Retain fallout reasoning and one optional mass–energy calculation instead.')
remove([154],'Duplicate of the single optional mass–energy example retained at 153.')
remove(list(range(155,164)),'Detailed weapon-yield, fuel-mass, tactical-effect and arsenal-energy calculations are outside the export-guided scope; several also use dated premises. Retain 152–153 as the small conceptual/energy extension.')
remove([165],'Fixed force-strength ratios and assumed strong–electroweak unification should not be reinforced; revised 164 covers interaction identification.')
remove([168],'The blanket statement about stability of all massless particles is a poor introductory prompt. Neutrino flavor change and mass evidence are better addressed in revised 169.')
remove([172],'Inferring a specific meson decay mechanism from lifetime is specialist detail; particle classification is the main assessed objective.')
remove([175,176],'Particle-decay energy calculations duplicate the chapter’s other mass–energy work and are not needed for classification practice.')
remove([177],'A hypothetical grand-unification mass scale is neither an established particle property nor useful core numerical practice.')
remove([179,180],'Detailed tau/sigma decay energetics and spectroscopy are beyond scope; optional 178 supplies one lepton-family conservation check.')
remove([181,182],'Energy–lifetime uncertainty calculations are beyond this chapter’s intended level and introduce distinctions not needed for the retained questions.')
remove(list(range(186,196)),'Integrated cosmic-ray, accelerator, two-body decay, speculative-lifetime and extreme-relativity calculations exceed the export’s level. Earlier selected questions cover their useful conceptual themes; no additional open-ended numerical construction is needed.')

keep(2,'Useful connection to the earlier X-ray/quantum material; distinguish photon origin from energy alone.')
keep(4,'Direct conceptual practice on what makes radioactivity a nuclear process.')
keep(10,'One detector application of the photoelectric threshold provides modest conceptual enrichment.','Optional extension')
keep(17,'Directly matches the isotope homework and Lecture 28.')
keep(60,'Useful decay-chain explanation without calculation; extends half-life reasoning.','Optional extension')
keep(61,'Clarifies the statistical meaning of half-life and avoids interpreting halving as an exact count.')
keep(62,'Useful conceptual distinction between isotope amount and chemical form; no activity formula is required.')
keep(63,'Connects binding energy to mass–energy without mass-table arithmetic.','Optional extension')
keep(88,'Useful qualitative distinction between diagnostic imaging and treatment; no medical dose calculation.')
keep(98,'A focused application of internal exposure and radiation biology.')
keep(103,'Asks what information matters rather than pretending activity alone predicts individual harm; use isotope, radiation, activity, distribution and retention in the eventual explanation.')
keep(112,'Core explanation of why light-nucleus fusion can release energy.')
keep(113,'A modest conceptual contrast that prevents “all fusion releases energy.”','Optional extension')
keep(133,'Core fission/fusion binding-energy comparison; complements 112.')
keep(137,'Important distinction between stopping a chain reaction and eliminating decay heat.')
keep(170,'Strong conceptual question about the role of experiment in testing theoretical predictions.')
keep(171,'A simple particle–antiparticle comparison using the current table.','Optional extension')
keep(183,'Retain as an explicitly hypothetical conceptual extension, not a claim that all four interactions have been unified.','Optional extension')
keep(184,'Already revised; reinforces the Higgs/weak-carrier distinction in Lecture 30.')

revise(1,'Add the missing foundational identification task; retain the statistical-range idea without awkward duplicate “a ray” wording.','(a) Identify the particles emitted as alpha radiation, beta-minus radiation, beta-plus radiation, and gamma radiation. (b) An alpha particle of a given energy has a quoted range of 2.0 mm in a material. Does every such particle stop at exactly 2.0 mm? Explain.')
revise(5,'Use total energy and rest mass directly, without suggesting that energy conservation failed.','Where does the energy released in radioactive decay come from? Explain how the total rest mass of the products can be smaller than that of the parent while total energy is conserved.')
revise(6,'Make the electric-field comparison self-contained and include both beta signs.','Alpha particles, beta-minus particles, beta-plus particles, and gamma rays travel horizontally between two plates. The upper plate is positive and the lower plate is negative. Which beams deflect upward, which deflect downward, and which continue straight? Explain using their charges.')
revise(8,'Replace an under-specified ranking across gases/solids with representative shielding and attenuation reasoning.','For typical radioactive-source energies, explain why paper can stop alpha particles, a suitable thickness of plastic can stop beta particles, and much thicker shielding is usually needed to substantially reduce gamma radiation. Why does “reducing the gamma intensity” describe shielding more accurately than “stopping every gamma photon”?')
revise(9,'Distinguish contamination control from shielding of penetrating radiation.','Workers handling radioactive contamination may wear disposable coveralls and gloves. Explain what these prevent. Why do such garments provide little shielding against penetrating gamma rays?')
revise(11,'Keep one short detector arithmetic extension; avoid implying that all deposited energy becomes ionization.','A gas detector requires an average of 30 eV of deposited energy per ion pair produced. A particle deposits 0.60 MeV in the gas. Estimate the number of ion pairs produced. Use 1 MeV = 10⁶ eV.','Optional extension')
revise(12,'Replace the reverse of 11 with ionization/DNA practice aligned with the active homework.','What does it mean to ionize an atom or molecule? Explain how ionizing radiation can damage living cells even when the incident radiation is electrically neutral.',major=True)
revise(15,'Fix grammar and ask a more precise question about force range and nuclear binding.','Protons repel one another electrically. What interaction helps bind protons and neutrons into nuclei, and why does its short range matter? Which interaction is responsible for beta decay?')
revise(16,'Retain terminology but explicitly separate a nucleon from a neutrino.','Explain the relationships among the terms nucleus, nucleon, proton, neutron, and nuclide. Is a neutrino a nucleon? Explain.')
revise(18,'Replace an elaborate density verification with the isotope counting actually assessed in the course.','For helium-4 (Z = 2), carbon-14 (Z = 6), cobalt-60 (Z = 27), and uranium-235 (Z = 92), give the numbers of protons, neutrons, and total nucleons. Which number identifies the element?',major=True)
revise(25,'Keep a simple repeated-attenuation extension, with the idealized condition stated.','In an idealized narrow-beam measurement, each 1.50-cm layer of lead transmits 10.0% of the gamma rays incident on that layer. What percentage of the original beam remains after two layers? After three? What total thickness leaves 0.100%?','Optional extension')
revise(30,'Use current neutrino terminology and explicitly scope the conservation check to this reaction.','In electron capture, a proton in a nucleus and an electron become a neutron and an electron neutrino. Show that electric charge is conserved. Using Lₑ = +1 for an electron and for an electron neutrino, explain why the emitted neutrino is consistent with electron-family-number conservation in this reaction.')
revise(32,'Use a structured comparison instead of assuming that students know what “three types” means.','For beta-minus decay, beta-plus decay, and electron capture, describe how a neutron or proton changes and how Z and A change. How do those changes differ from alpha decay? What happens to Z and A in gamma emission?')
revise(33,'Retain one beta-minus example, supply atomic numbers and explicitly include the antineutrino.','Tritium, hydrogen-3 (Z = 1), undergoes beta-minus decay. Write the complete decay equation, including the electron and electron antineutrino. Identify the daughter; helium has Z = 2.')
revise(35,'Retain one beta-plus example without mass lookup.','Manganese-50 (Z = 25) undergoes beta-plus decay. Write the complete decay equation, including the positron and electron neutrino. Identify the daughter; chromium has Z = 24.')
revise(37,'Retain one electron-capture example without mass lookup.','Beryllium-7 (Z = 4) captures an electron. Write the complete reaction equation, including the electron neutrino. Identify the daughter; lithium has Z = 3.')
revise(39,'Retain one alpha example; remove the incidental laboratory-preference claim.','Polonium-210 (Z = 84) undergoes alpha decay. Write the complete decay equation and identify the daughter; lead has Z = 82. Check the total charge and number of nucleons.')
revise(45,'Keep the annihilation concept and momentum reasoning; omit the energy arithmetic and “masses are destroyed” wording.','An electron and a positron initially at rest annihilate into two photons. Explain why the photons travel in opposite directions and have equal energies. What supplies their energy?','Optional extension')
revise(47,'Replace the crowded general-nuclide formula with a single understandable conservation check.','A free neutron undergoes beta-minus decay: n → p + e⁻ + ν̄ₑ. Check electric charge and nucleon number before and after the decay. Using Lₑ = +1 for the electron and −1 for the electron antineutrino, check electron-family number as well.','Optional extension')
revise(67,'Bring dating into the same one-to-five whole-half-life range as MyOpenMath; avoid an extreme radiocarbon-age extrapolation.','Carbon-14 has a half-life of 5730 years. Assume a closed sample initially contained 8000 carbon-14 atoms and now contains about 1000. How many half-lives have passed, and what age does this suggest? Explain why this is an estimate rather than an exact clock for each atom.')
revise(68,'Remove curie conversion and logarithmic inversion; add the forward repeated-halving task.','A sealed source has an initial activity of 800 Bq and a half-life of 5.0 years. (a) What activity is expected after 15 years? (b) How long until the expected activity is 50 Bq? Assume the daughter contributes no measured activity and the measurement conditions remain unchanged.')
revise(83,'Preserve count rate versus activity with simple supplied numbers and explicit background subtraction.','A source has an activity of 100 Bq. A detector records an average of 1200 counts per minute above background. What fraction of the decays produces a recorded count? Give two reasons why a detector may register only some of a source’s decays.','Optional extension')
revise(89,'Keep the dose-reduction idea while recognizing the practical need to complete the scan.','Why can a short physical half-life help limit the time a diagnostic radiopharmaceutical remains radioactive? Why must its half-life still be long enough for preparation and imaging?')
revise(90,'Replace neutron-source Q-value arithmetic with a core active-homework topic absent from the existing exercise set.','Which of these imaging methods use ionizing radiation: conventional X-ray imaging, CT, PET, MRI, and ultrasound? For each, identify the kind of radiation or physical signal used. Explain why “does not use ionizing radiation” does not mean that an imaging method has no safety considerations.',major=True)
revise(92,'Keep a medically connected decay example without relying on the preceding removed production question.','Molybdenum-99 (Z = 42) undergoes beta-minus decay to technetium-99, often in the metastable state technetium-99m. Write the beta-minus equation including the electron antineutrino. When technetium-99m emits a gamma photon, do its proton and neutron counts change?','Optional extension')
revise(93,'Replace timing-resolution arithmetic with the conceptual PET mechanism.','In PET imaging, a positron emitted by a radiopharmaceutical annihilates with an electron. Explain why detecting two photons at nearly the same time on opposite sides of the patient helps locate the event. Does one detector pair alone identify a unique point?')
revise(97,'Avoid a blanket safe/unsafe classification of emitters.','Why can an alpha-emitting material be much more hazardous when inhaled or swallowed than when it is outside intact skin? Explain why gamma radiation can contribute to exposure even when its source remains outside the body.')
revise(100,'Make time, distance and shielding self-contained; remove dependency on photographs and their historical claims.','Describe how each change can reduce exposure to a radiation source: (a) spending less time near it, (b) working farther away, and (c) placing suitable shielding between it and the worker. Why must the shielding material and thickness be chosen for the radiation involved?')
revise(114,'Replace the specialized D–T versus D–D comparison with the fusion barrier emphasized in Lecture 29.','Light nuclei can release energy when they fuse. Why is it nevertheless difficult to start and sustain fusion? Explain the roles of electric repulsion, high temperature, and keeping the reacting nuclei together long enough.',major=True)
revise(119,'Use the net particle balance without prescribing an exact photon count for a multistep stellar process.','The net conversion in the proton–proton chain, including positron annihilation, can be written 4p + 2e⁻ → ⁴He + 2νₑ + released energy. Check electric charge and nucleon number. If Lₑ is +1 for an electron and an electron neutrino, check electron-family number too.','Optional extension')
revise(136,'Prevent “fusion produces no radioactivity” while retaining the comparison.','Fission commonly leaves radioactive fission products. Does that mean a fusion facility would necessarily produce no radioactive material? Discuss how neutrons from some fusion reactions can affect surrounding materials.')
revise(138,'Replace the misleading notion of adding isolated “critical masses” with neutron balance and control.','In a steady fission chain reaction, about how many neutrons from each fission must, on average, cause another fission? Explain how neutron absorption and leakage affect whether the chain reaction dies away, stays steady, or grows. How do control rods help regulate it?')
revise(140,'Keep the important distinction without implying that a reactor cannot have dangerous explosions.','Why is a commercial power reactor not a nuclear bomb? Distinguish an explosive nuclear-weapon chain reaction from steam or chemical explosions that can occur in a reactor accident.')
revise(142,'Retain a single accessible reaction balance; remove the mass-data Q-value task.','In the fission reaction n + ²³⁵U → ⁹²Kr + ¹⁴²Ba + x n, determine x by conserving nucleon number. Check electric charge using Z = 92 for U, 36 for Kr, and 56 for Ba. How can the emitted neutrons help sustain a chain reaction?','Optional extension')
revise(152,'Remove dated numerical and historical premises; retain environmental versus physical decay reasoning.','The measured activity of a radioactive contaminant at a particular site can fall faster than radioactive decay alone predicts. Give two physical processes that could cause this. Does a fall in activity at that site necessarily mean the radioactive nuclei have decayed?')
revise(153,'Retain one self-contained mass–energy calculation as optional enrichment.','An event releases 5.0 × 10¹³ J of nuclear energy. Using E = Δmc² and c = 3.0 × 10⁸ m/s, find the corresponding decrease in rest mass. Express the answer in kilograms and grams.','Optional extension')
revise(164,'Replace force-ratio arithmetic with interaction identification aligned with the export.','Identify the interaction chiefly responsible for each: (a) Earth’s orbit around the Sun, (b) the attraction between an electron and a nucleus, (c) binding protons and neutrons into a nucleus, and (d) beta decay. Which of these interactions have a short range at nuclear or subnuclear scales?',major=True)
revise(166,'Drop the overbroad “exactly like normal matter” premise and ask the useful photon/antiphoton question directly.','An antihydrogen atom contains an antiproton and a positron. The photon is its own antiparticle. Could you identify antihydrogen simply because it emits a distinct kind of “antiphoton”? Explain.')
revise(167,'Replace the false blanket premise about massless particles with a clear neutron example already supported by the revised prose.','A neutron has zero net electric charge but has a magnetic moment and interacts electromagnetically. How is this possible? Explain using its internal quark structure.','Optional extension',True)
revise(169,'Replace the duplicated supernova mass-limit question with the solar-neutrino essay actually assessed in MyOpenMath.','Early solar-neutrino experiments detected fewer electron neutrinos than solar models predicted. Explain how neutrino flavor change resolves this discrepancy. Why was a measurement sensitive to all three active neutrino flavors an important test?',major=True)
revise(173,'Add the export’s classification practice, using quark content rather than decay modes as the defining distinction.','(a) Classify the electron, muon, electron neutrino, pion, kaon, proton, neutron, photon, and gluon as leptons, mesons, baryons, or gauge bosons. You may use the particle table. (b) Which categories in this list contain hadrons? (c) Describe the valence-quark content of an ordinary meson and an ordinary baryon. Why does mass alone not determine these categories?')
revise(174,'Separate conserved nucleon count from actual mass and qualify the setting.','In ordinary nuclear reactions without baryon–antibaryon production, how does baryon-number conservation account for conservation of the total number of nucleons? Why does this not require the total rest mass to remain unchanged?','Optional extension')
revise(178,'Keep one lepton-family check without decay-energy arithmetic.','In μ⁻ → e⁻ + ν̄ₑ + νμ, check electric charge, electron-family number, and muon-family number. Use +1 for a lepton in its family, −1 for its antiparticle, and zero for particles outside that family.','Optional extension')
revise(185,'Replace the unclear “ultimate carriers” question with an established-versus-proposed theory distinction.','Which interactions are described by the Standard Model? Which is left out? How does a proposed grand unified theory differ from the already established electroweak theory?',major=True)

assert set(D)==set(range(1,196)),sorted(set(range(1,196))-set(D))

families={
 'radiation':('Radiation identity, ionization and shielding',[778,779,780,880,881,882,883,769,770]),
 'nucleus':('Isotopes and nuclear forces',[781,786,874,876,877,771,789]),
 'decay':('Decay, neutrinos and antiparticles',[771,774,775]),
 'halflife':('Repeated-halving half-life reasoning',[787,873,776]),
 'imaging':('Imaging methods and radiation',[782,875]),
 'protection':('Ionization and radiation protection',[780,783,878,879,883,893,770]),
 'fusion':('Fusion, fission and chain reactions',[784,872,772,773]),
 'particles':('Particle classification and conservation',[785,868,869,870,871,775,777,790,791]),
 'neutrinos':('Solar neutrino problem',[895,774,788]),
 'unification':('Standard Model and testing theories',[791,894])}
secmap={'14.2':'radiation','14.3':'radiation','14.4':'nucleus','14.5':'decay','14.6':'halflife','14.7':'imaging','14.8':'protection','14.9':'fusion','14.10':'fusion','14.11':'fusion','14.12':'nucleus','14.13':'particles','14.14':'unification'}
for x in items:
 x.update(D[x['number']]);x['evidence_family']='neutrinos' if x['number']==169 else secmap[x['section']]
 x['current_url']='https://intro-1-1.coaphys.xyz/exercises/nuclear-and-particle-physics-exercises/#'+x['rendered_id']
counts=dict(collections.Counter(x['action'] for x in items));levels=dict(collections.Counter(x['level'] for x in items if x['action']!='Remove'))
sources=[]
for k in active:
 q=data['questionset'][k]
 sources.append({'export_locator':k,'uniqueid':str(q['uniqueid']),'description':q['description'],'assessments':[a['title'] for a in assessments if k in a['question_set_ids']]})
packet={'status':'proposal-only; awaiting maintainer review','export_file':export.name,'export_sha256':inv['source_sha256'],'source_sha256':snap,'assessments':assessments,'active_definition_count':len(active),'counts':counts,'levels':levels,'numbering_policy':'Retain current exercise numbers and stable IDs. Approved removals leave gaps; never renumber survivors or recycle removed numbers for unrelated later additions. Replacements at existing numbers are individually identified for approval. Implementation must freeze numbering and check all inbound links before removal.','method':'Read all 195 current exercise prompts and all 43 active assessment definitions, including conditional choices and numerical randomization controls. Code was inspected as data, not executed. This is a curriculum/content review, not live MyOpenMath grading validation. Archived assignment 107 is context only.','families':{k:{'title':v[0],'export_locators':v[1]} for k,v in families.items()},'mom_sources':sources,'exercises':items}
(OUT/'exercise-review-proposal.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

esc=lambda s:html.escape(str(s))
cards=[]
for x in items:
 n=x['number'];new='<h4>Proposed wording</h4><p>'+esc(x['proposed'])+'</p>' if x['proposed'] else ''
 major='<strong class="flag">Substantial rewrite — please review</strong>' if x['major'] else ''
 cards.append(f'<article data-action="{x["action"]}" data-level="{x["level"]}" data-major="{str(x["major"]).lower()}" id="q{n}"><h3>Exercise {n} <small>§{x["section"]}</small> <span class="badge {x["action"]}">{x["action"]}</span></h3><p class="meta">{esc(x["level"])} · <a href="#family-{x["evidence_family"]}">Comparison context</a> · <a href="{x["current_url"]}" target="_blank">Current textbook exercise</a></p>{major}<p><b>Reason:</b> {esc(x["reason"])}</p>{new}<details><summary>Current wording</summary><p>{esc(x["text"])}</p><p class="meta">Plain-text source extraction; use the textbook link for formatted equations and figures.</p></details></article>')
familyhtml=[]
for k,(title,ids) in families.items():
 lines=[]
 for i in ids:
  q=data['questionset'][str(i)];uses=[a['title'] for a in assessments if str(i) in a['question_set_ids']]
  lines.append('<li>'+esc(q['description'])+'<small> — '+esc('; '.join(uses))+'</small></li>')
 familyhtml.append(f'<details id="family-{k}"><summary>{esc(title)}</summary><ul>'+''.join(lines)+'</ul></details>')
sectionrows=[]
for sec in dict.fromkeys(x['section'] for x in items):
 subset=[x for x in items if x['section']==sec];c=collections.Counter(x['action'] for x in subset)
 sectionrows.append('<tr><td>'+sec+'</td>'+''.join('<td>'+str(c[a])+'</td>' for a in ['Keep','Revise','Remove'])+'</tr>')
overview=f'''<h1>Chapter 14 exercise review</h1><p class="lead">Proposal only: {counts['Keep']} keep · {counts['Revise']} revise · {counts['Remove']} remove. {levels['Core']} core questions and {levels['Optional extension']} optional extensions would remain.</p>
<p>Based on the September 27, 2026 Physics 10 export: Question Set 12 and its assessment, Lectures 28–30, and the Chapter 14 timed multiple-choice and essay assessments. All 43 distinct active definitions were read, including their randomized branches. The archived Chapter 14 assignment did not determine scope. The public textbook and MyOpenMath export have not been changed.</p>
<p>The 10-question homework emphasizes radiation identification, ionization, shielding, nuclear forces, isotope counts, whole-number half-lives, imaging, fission/fusion and particle classification. The timed variants stay at that level. Lecture 28 explicitly says dose-unit detail and much of the long chapter are optional. The solar-neutrino essay supplies a worthwhile conceptual topic missing from the existing exercise set.</p>
<p><b>Numbers stay fixed.</b> Removed exercises leave gaps. The surviving questions keep their current numbers and IDs. “Revise” includes a few clearly marked replacement prompts at the existing number; those need your approval. Before implementation, check numbering overrides, shared directions, solutions and inbound links. This packet makes no source edits.</p>
<p><b>Optional extension</b> means an exercise worth retaining for extra practice, not a new expectation that students master every late-chapter topic. You can filter these as a group below. No new exercise numbers are proposed.</p>
<h2>Decisions worth reviewing first</h2><ul>
<li><b>Overall size:</b> retain {levels['Core']+levels['Optional extension']} of 195, including {levels['Optional extension']} optional extensions.</li>
<li><b>New conceptual coverage in existing slots:</b> 12 (ionization), 18 (isotope counts), 90 (imaging methods), 114 (fusion barrier), 164 (interactions), 169 (solar neutrinos), 185 (Standard Model versus GUTs). Exercise 167 changes a flawed massless-particle premise into an optional neutron question.</li>
<li><b>Four representative decay equations:</b> 33, 35, 37 and 39. Supply atomic numbers; remove the long series of mass-table energy calculations.</li>
<li><b>Half-life:</b> 67–68 use forward and backward repeated halving, matching the numerical level in the export. No logarithms are required.</li>
<li><b>Weapons subsection:</b> retain environmental transport versus decay in 152 and one optional mass–energy calculation in 153; remove the specialized weapon-effect and fuel calculations.</li>
<li><b>Recently corrected exercises:</b> keep 184; remove 179 and 190 on level/redundancy grounds. Earlier scientific corrections do not oblige us to retain a question.</li></ul>
<h2>MyOpenMath cautions</h2><p>The export guides level, not scientific wording. These are follow-up leads; no live course changes are proposed here.</p><ul>
<li>Radiation essay: remove the blanket “perfectly safe even in large quantities” framing in any adaptation. Non-ionizing radiation can still have harmful effects.</li>
<li>Radiation-safety variants: do not turn the time/distance/shielding mnemonic into a claim that contamination PPE or medically appropriate non-ionizing alternatives can never reduce exposure.</li>
<li>Radioactivity variants: distinguish beta-minus from beta-plus; describe gamma shielding as attenuation, not a guarantee that every photon stops.</li>
<li>Particle classification: hadrons are composite, so “categories of elementary particles” is misleading for proton/pion examples; “omega” needs an explicit symbol to distinguish Ω baryons from ω mesons.</li>
<li>Fission/fusion variants: avoid presenting the iron boundary as an exact universal reaction rule. Use the binding-energy trend. Lecture fusion status is time-sensitive and is not copied into the proposed prompts.</li></ul>
<p>Factual checks used: <a href="https://www.epa.gov/radiation/protecting-yourself-radiation">EPA radiation protection</a>; <a href="https://www.fda.gov/radiation-emitting-products/medical-x-ray-imaging/medical-x-ray-imaging">FDA X-ray imaging</a>; <a href="https://www.fda.gov/radiation-emitting-products/medical-imaging/ultrasound-imaging">FDA ultrasound</a>; <a href="https://www.fda.gov/radiation-emitting-products/mri-magnetic-resonance-imaging/benefits-and-risks">FDA MRI risks</a>; <a href="https://arxiv.org/abs/nucl-ex/0204008">SNO flavor-transformation measurement</a>. The proposal is not clinical or radiation-workplace guidance.</p>
<h2>By section</h2><table><thead><tr><th>Section</th><th>Keep</th><th>Revise</th><th>Remove</th></tr></thead><tbody>{''.join(sectionrows)}</tbody></table>
<h2>Numbered recommendations</h2><div class="controls"><label>Show <select id="filter"><option value="all">All 195</option><option>Keep</option><option>Revise</option><option>Remove</option><option value="major">Substantial rewrites</option><option value="Optional extension">Optional extensions</option><option value="Core">Core retained questions</option></select></label><label> Find <input id="search" placeholder="Number or words"></label><span id="count"></span></div>'''
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Chapter 14 exercise review</title><style>
body{font:17px/1.6 system-ui,sans-serif;color:#162d3b;background:#f2f5f6;margin:0}main{max-width:1050px;margin:auto;padding:32px 24px}h1,h2,h3{line-height:1.25}h2{margin-top:2em}a{color:#006880}article{background:white;border:1px solid #cad6db;border-radius:9px;padding:20px 26px;margin:18px 0}article h3{margin:0}small,.meta{font-size:14px;color:#52666e}.badge{font-size:14px;padding:4px 10px;border-radius:20px;float:right}.Keep{background:#d7eedf}.Revise{background:#fff0bf}.Remove{background:#eee2e2}.flag{display:block;color:#875200}.lead{font-size:21px}.controls{position:sticky;top:0;padding:15px;background:#dce9ee;display:flex;gap:18px;flex-wrap:wrap;z-index:2}select,input{font:inherit;max-width:220px}table{border-collapse:collapse}td,th{padding:5px 25px;border:1px solid #cad6db}details{margin:14px 0}summary{cursor:pointer;font-weight:600}h4{margin-bottom:0}h4+p{margin-top:6px}article[hidden]{display:none}@media(max-width:600px){main{padding:20px 14px}article{padding:18px}td,th{padding:5px 10px}.controls{position:static}a{overflow-wrap:anywhere}}@media print{.controls{display:none}article{break-inside:avoid}details{display:block}} </style><main>'''+overview+''.join(cards)+'<h2>Comparison sources</h2><p>These are topic-level comparisons, not claims that each textbook exercise is a duplicate of a MyOpenMath question. Optional extensions deliberately go beyond the assessed questions. Full descriptions and assessment names are used so you can locate the originals.</p>'+''.join(familyhtml)+'''</main><script>
const cards=[...document.querySelectorAll('article')],filter=document.getElementById('filter'),search=document.getElementById('search');function update(){let n=0;for(const c of cards){const f=filter.value,q=search.value.toLowerCase().trim();const match=f==='all'||c.dataset.action===f||c.dataset.level===f||(f==='major'&&c.dataset.major==='true');const text=/^[0-9]+$/.test(q)?c.id==='q'+q:c.textContent.toLowerCase().includes(q);c.hidden=!(match&&text);if(!c.hidden)n++}document.getElementById('count').textContent=n+' shown'}filter.onchange=search.oninput=update;update();
</script></html>'''
(OUT/'exercise-review-proposal.html').write_text(page,encoding='utf-8')
assert snap=={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'maintained/modules').glob('*/index.cnxml')}
validation={'exercise_count':len(items),'numbers':list(range(1,196)),'all_dispositions_present':True,'all_revisions_have_wording':all(x['proposed'] for x in items if x['action']=='Revise'),'active_definitions':len(active),'textbook_source_unchanged':True,'export_sha256':inv['source_sha256'],'counts':counts,'levels':levels}
(OUT/'exercise-review-validation.json').write_text(json.dumps(validation,indent=2)+'\n',encoding='utf-8')
print(json.dumps(validation,ensure_ascii=False))
