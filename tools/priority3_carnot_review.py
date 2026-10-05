"""P3-08 review proposals; called by compile_priority3_review.py. No source writes."""


def append_carnot_review(add, edit, block, source, ent, work):
    carnot = source('MIT: The Carnot Cycle', 'https://web.mit.edu/16.unified/www/SPRING/propulsion/notes/node23.html', 'Four reversible stages; efficiency derived using reversible adiabatic relations')
    ucla = source('UCLA ePhysics: Carnot Cycle', 'https://ephysics.physics.ucla.edu/carnot-cycle', 'Definition as a four-stage reversible sequence')
    limits = source('MIT: Limitations on the Work that Can Be Supplied by a Heat Engine', 'https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node44.html', 'Engine plus two fixed-temperature reservoirs; maximum work, efficiency, and cyclic engine entropy')
    pump = source('MIT: Refrigerators and Heat Pumps', 'https://web.mit.edu/16.unified/www/SPRING/propulsion/notes/node24.html', 'The same reversible cycle run backward preserves heat/work magnitudes')
    irrevers = source('MIT: Muddiest Points on Chapter 4', 'https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node35.html', 'MP 4.4: reversibility requires restoring the surroundings as well as the system')
    bird = source('UCSB Physics Lecture Demonstrations: Drinking birds', 'https://web.physics.ucsb.edu/~lecturedemonstrations/Composer/Pages/52.31.html', 'Evaporative cooling, pressure-driven liquid movement, and pressure equalization on tipping')
    for ref in [carnot, ucla, limits, pump, irrevers, bird]:
        ref['checked'] = '2026-09-22'
    i = add('P3-08', 'Carnot cycles, reversibility, and connected claims',
            'The cited analyses explicitly use reversible Carnot stages. For this textbook, reversibility should be stated where the analysis requires it rather than supplied implicitly by the cycle name. The proposed clarification makes its four stages and physical assumptions explicit: isothermal or adiabatic alone does not guarantee reversibility, and not every reversible engine uses a Carnot cycle. The other comparisons address connected scope and factual problems found during the scan. The opening most-efficient-cycle sentence is retained at the maintainer’s request. Remaining comparisons are proposals, not applied changes.',
            [carnot, ucla, limits, pump, irrevers, bird],
            'Review A–G separately. A clarifies terminology and assumptions; B–G address connected claims. The drinking-bird caption and heat-pump explanation deserve a close read.')
    i['scan_scope'] = 'All maintained CNXML searched: 36 Carnot-related prose/title/glossary hits across m42235, m42236, m67127, m67128; surrounding paragraphs, captions, glossary and linked exercises inspected. Existing P3-05/P3-06 proposals checked for overlap. This is not a full numerical or technology audit.'
    i['terminology_finding'] = 'The maintainer requests context-dependent usage: state reversibility explicitly where required by the analysis. The cited ideal-cycle treatments use reversible stages, but the stage labels alone do not establish reversibility or the efficiency formula.'

    def detail(label, reason, refs):
        p = i['passages'][-1]
        p['review_label'] = label
        p['review_reason'] = reason
        p['sources'] = refs

    edit(i, 'm42235', 'import-auto-id1169738035422', new='The ideal Carnot cycle considered here uses only reversible processes. Irreversible processes involve dissipative factors, such as friction and turbulence. Heat transfer through a finite temperature difference is also irreversible. Reversible processes idealize away these imperfections and maximize the efficiency of the resulting heat engine cycle for given hot and cold reservoir temperatures.')
    detail('A. State the physical assumptions', 'Maintainer-drafted replacement. Correct finite temperature to finite temperature difference, and specify the reservoir temperatures for the maximum-efficiency comparison. Remove the heat-rejection claim and Obviously.', [carnot, ent, limits])
    i['passages'][-1]['status'] = 'maintainer-draft-with-minimal-factual-clarifications; pending-section-preview'
    i['passages'][-1]['authorization'] = 'Maintainer requested this draft with any necessary factual corrections. The two clarifications are temperature difference and fixed hot/cold reservoir temperatures.'
    edit(i, 'm42235', 'import-auto-id1169738035492', [
        ('The cycle comprises two isothermal and two adiabatic processes. Recall that both isothermal and adiabatic processes are, in principle, reversible.', 'The cycle comprises two reversible isothermal and two reversible adiabatic processes.')])
    detail('A. Specify the reversible stages', 'Maintainer requested explicit reversible qualifiers on both pairs of processes and deletion of the Recall sentence. Preserve the existing figure reference.', [carnot])
    i['passages'][-1]['status'] = 'approved-pending-section-preview'
    i['passages'][-1]['authorization'] = 'Maintainer supplied the two reversible isothermal and two reversible adiabatic processes wording and requested deletion of Recall that ... .'
    edit(i, 'm42235', 'fs-id1169738163624', new='an ideal cycle consisting of two reversible isothermal processes and two reversible adiabatic processes')
    detail('A. Matching Carnot-cycle glossary entry', 'Name the four stages explicitly instead of identifying Carnot merely with reversible processes.', [carnot, ucla])

    for passage in i['passages']:
        if passage.get('review_label', '').startswith('A.'):
            passage['status'] = 'approved-pending-section-preview'
            passage['authorization'] = 'Maintainer approved all remaining A comparisons after the paragraph and reversible-stage revisions, including the matching glossary entry. The opening paragraph remains unchanged by earlier decision.'

    university = source('OpenStax University Physics Volume 2, §4.5 (UCF CC BY 4.0 copy)', 'https://pressbooks.online.ucf.edu/uphysicstjb/chapter/the-carnot-cycle/', 'Carnot’s Principle statement; page-end license and attribution')
    university['checked'] = '2026-09-22'
    university['license'] = 'CC BY 4.0'
    university['license_url'] = 'https://creativecommons.org/licenses/by/4.0/'
    statement = 'No engine working between two reservoirs at constant temperatures can have a greater efficiency than a reversible engine.'
    before = block('m42235', 'fs-id1169737792775')
    proposed = '<note id="fs-id1169737792775"><label/><title>Carnot’s Principle</title><para id="import-auto-id1169737776998">'+statement+'</para></note>'
    source_hash = next(p['source_sha256'] for p in i['passages'] if p['module'] == 'm42235')
    i['passages'].append(dict(module='m42235', source_path='maintained/modules/m42235/index.cnxml', source_id='fs-id1169737792775', source_sha256=source_hash, before_xml=before, proposed_xml=proposed,
        operation='replace-and-move', insert_after_id='import-auto-id1169738052034', insert_before_id='import-auto-id1169737804166',
        proposed_following_xml=['<para id="cp2e-carnot-principle-equivalence">This principle can be viewed as another statement of the second law of thermodynamics and can be shown to be equivalent to the heat-transfer and heat-engine statements introduced in the preceding section.</para>'],
        removed_source_ids=['import-auto-id1169737966671','import-auto-id1169738107879'],
        identity_note='Retain the existing box and main-statement identifiers at the new location. Removed introductory paragraph/term identifiers have no inbound links in the maintained book; preserve their retirement in the editorial record.',
        status='approved-structure-and-initial-wording; pending-section-preview',
        authorization='Maintainer requested complete removal of the original Carnot Engine box and a later Carnot’s Principle box with the University Physics wording, before the example-introducing paragraph so its connection to the reactor example is not interrupted. Maintainer also requested the following equivalence sentence, adjusting the named statements to match the local textbook.',
        attribution=dict(title='University Physics Volume 2', section='4.5 The Carnot Cycle', authors=['Samuel J. Ling','Jeff Sanny','William Moebs'], publisher='OpenStax / Rice University', copyright_year=2016, source_url=university['url'], license='CC BY 4.0', license_url=university['license_url'], changes='Principle sentence reproduced verbatim; following equivalence sentence adapted to refer to the unnamed heat-transfer and heat-engine statements already introduced. Box and following paragraph relocated within Introduction to Physics.', attribution_url='https://openstax.org/books/university-physics-volume-2/pages/1-introduction'),
        followup_tasks=['When applying the preview/release, move the replacement box before the entire paragraph beginning It is also apparent and ending Consider the following example; move its proposed_following_xml paragraph with it, outside and immediately after the box; do not perform an in-place text replacement alone.', 'Carry University Physics attribution into the maintained provenance and generated section credits.']))
    detail('B. Replace and relocate the boxed statement', 'Remove the entire early Carnot Engine box, including its introductory paragraph. Insert this Carnot’s Principle box after the paragraph discussing the zero-kelvin efficiency limit and before the paragraph beginning It is also apparent and ending Consider the following example. Preserve the example lead-in, intervening PV figure, and reactor example as a continuous sequence. The box wording is verbatim from the CC BY 4.0 University Physics copy. Its following equivalence sentence refers to the preceding section’s heat-transfer and heat-engine statements because that section does not name them Kelvin and Clausius. Both will be reviewed in the whole-section preview.', [university])
    i['sources'].append(university)
    edit(i, 'm42235', 'fs-id1169736887234', new='the maximum theoretical efficiency for a heat engine operating between two specified heat reservoirs')
    detail('B. Matching efficiency glossary entry', 'Retain the same-reservoir restriction in the definition.', [limits])
    edit(i, 'm67128', 'import-auto-id1169736657076', [
        ('a Carnot engine and its heat reservoirs for one full cycle', 'a reversible Carnot engine and its heat reservoirs for one full cycle')])
    detail('B. Identify the assumption in the entropy calculation', 'Small coordinating addition. P3-06 already supplies the approved conclusion about the reservoirs and then the engine.', [limits])
    edit(i, 'm67128', 'import-auto-id1169738080394', [('for a Carnot engine,', 'for a reversible Carnot engine,')])
    detail('B. Identify the assumption where the heat ratio is used', 'The cancellation uses the reversible heat-ratio equality.', [limits])

    for passage in i['passages']:
        if passage.get('review_label', '').startswith('B.'):
            passage['status'] = 'approved-pending-section-preview'
            passage['group_authorization'] = 'Maintainer approved the remainder of B after the replacement/relocation of Carnot’s Principle and its following equivalence paragraph. The rejected first B question remains unchanged.'

    import re
    old = block('m42236', 'import-auto-id1169738013059')
    opening = old[:old.index('>')+1]
    rest = old[old.index('(Note that'):old.rfind('</para>')]
    maths = re.findall(r'<m:math>.*?</m:math>', old[:old.index('(Note that')], re.S)
    assert len(maths) == 3
    qh = '<m:math><m:msub><m:mi>Q</m:mi><m:mi>h</m:mi></m:msub></m:math>'
    draft = 'Heat pumps, air conditioners, and refrigerators operate by causing heat transfer from cold to hot. Imagine a heat-engine cycle run backward: the system absorbs heat '+maths[0]+' from a cold reservoir, and work '+maths[1]+' is done on it so that it can release heat '+qh+' into a hot reservoir. Over a complete cycle, the work input adds to the energy released as heat, so the first law gives '+maths[2]+'. '
    edit(i, 'm42236', 'import-auto-id1169738013059', new=draft+rest)
    detail('C. Explain the backward heat-engine cycle', 'Maintainer-drafted opening through Q_h = Q_c + W. Smooth the grammar and state the complete-cycle condition for the first-law balance. Preserve the remainder of the paragraph, including the sign note and application descriptions.', [pump])
    i['passages'][-1]['status'] = 'maintainer-draft-with-minimal-clarifications; pending-section-preview'
    i['passages'][-1]['authorization'] = 'Maintainer supplied the new cold-to-hot, backward-cycle explanation and authorized factual/grammatical corrections.'
    edit(i, 'm42236', 'import-auto-id1169737723054', [
        ('Since the efficiency of a heat engine is', 'For a reversible heat-engine cycle run backward as a heat pump, the efficiency of the forward cycle is')])
    detail('C. Scope the reciprocal COP relation', 'The relation uses the same reversible cycle in opposite directions, not arbitrary real devices.', [pump])
    w = '<m:math><m:mi>W</m:mi></m:math>'
    wp = '<m:math><m:msup><m:mi>W</m:mi><m:mo>′</m:mo></m:msup></m:math>'
    edit(i, 'm42236', 'import-auto-id1169737761565', new='Friction and other irreversible processes reduce heat engine efficiency, but they do <emphasis effect="italics">not</emphasis> benefit the operation of a heat pump. This is part of what it means for a process to be irreversible. We can model these losses by letting only a portion '+wp+' of the work input '+w+' reach a reversible heat pump, with the rest dissipated outside the hot reservoir. For the same heat delivery '+qh+' to the hot reservoir at the same reservoir temperatures, greater work input '+w+' is needed.')
    detail('C. Model the loss of effective work input', 'Maintainer-drafted replacement retains the first sentence and models the losses as W reduced to W′ before entering a reversible pump. The model explicitly deposits the remaining energy outside the hot reservoir so it is not also counted in Q_h. Compare equal heat delivery at the same reservoir temperatures; this is an illustrative loss model, not a claim that every real heat pump dissipates losses at that location.', [limits, pump])
    i['passages'][-1]['status'] = 'maintainer-draft-with-minimal-clarifications; pending-section-preview'
    i['passages'][-1]['authorization'] = 'Maintainer supplied the W-to-W′ model and authorized necessary factual and grammatical corrections.'

    for passage in i['passages']:
        if passage.get('review_label', '').startswith('C.'):
            passage['status'] = 'approved-pending-section-preview'
            passage['group_authorization'] = 'Maintainer approved C as it stands, including the revised heat-pump opening, reciprocal COP scope, and W-to-W′ loss model.'
    i['resume_at'] = 'P3-08-D'
    i['attention'] = 'A–C reviewed; approved changes await the whole-section preview. Resume with D (drinking bird), then E–G and P3-09 (SR). The two additional topic reviews follow thermodynamics and SR.'

    edit(i, 'm42235', 'import-auto-id1169736649071', [
        ('But the ideal Carnot engine, like the drinking bird above, while a fascinating novelty, has zero power. This makes it unrealistic for any applications.', 'The ideal Carnot engine transfers heat through infinitesimal temperature differences. In a practical engine, this would make heat transfer extremely slow and give very little power. To deliver useful power, real engines operate with finite temperature differences, at the cost of lower efficiency.')])
    detail('D. Explain the efficiency–power tradeoff', 'Explain why infinitesimal temperature differences limit heat-transfer rates and useful power in a practical engine. Remove the drinking-bird aside from the main text; its caption is reviewed separately. Preserve U3-15’s earlier removal of the unsupported 70%-of-Carnot claim.', [carnot, ent])
    i['passages'][-1]['status'] = 'revised-proposal; pending-review'
    i['passages'][-1]['authorization'] = 'Maintainer requested this revised efficiency–power explanation on the review page, with the caption left for separate review.'
    edit(i, 'm42235', 'import-auto-id1169738209561', [
        ('is an example of Carnot’s engine.', 'is an example of a heat engine.'),
        ('As the water evaporates, fluid moves up into the head,', 'As the water evaporates, the head cools and its vapor pressure falls. Fluid moves up into the head,'),
        ('This cools down the methylene chloride in the head, and it moves back into the abdomen,', 'Tipping allows vapor to pass into the head and equalize the pressure, so the liquid moves back into the abdomen,'),
        ('causing the bird to become bottom heavy and tip up. Except for a very small input of energy—the original head-wetting—the bird becomes a perpetual motion machine of sorts.', 'causing the bird to become bottom heavy and tip up, and the cycle repeats.')])
    detail('D. Repair the connected caption', 'Keep the photograph, credit, working-fluid description, and earlier corrected mechanism. At the maintainer’s request, end the explanation with the bird tipping up and the cycle repeating; omit the concluding explanation that would answer the linked question.', [bird])
    edit(i, 'm42235', 'import-auto-id1169738151626', [
        ('Although the bird enjoys the theoretical maximum efficiency possible, if left to its own devices over time, the bird will cease “drinking.” What are some of the dissipative processes that might cause the bird’s motion to cease?', 'If left to its own devices over time, the bird will cease “drinking.” Why does its dipping motion eventually stop?')])
    detail('D. Minimal repair to the linked conceptual question', 'Preserve the question about why dipping eventually stops; remove the efficiency premise and the prompt toward dissipative processes. The maintainer identifies loss of evaporative cooling as the intended reasoning, which the caption should not give away. Preserve the existing introductory figure reference.', [bird, limits])

    for passage in i['passages']:
        if passage['source_id'] in ['import-auto-id1169738209561', 'import-auto-id1169738151626']:
            passage['status'] = 'maintainer-directed-revision; pending-section-preview'
            passage['authorization'] = 'Maintainer supplied the ending of the caption and requested an open question about why dipping eventually stops, without efficiency or dissipative-process prompts.'

    old = block('m42235', 'import-auto-id1169738052034')
    start = old.index(' But the physical implication is this')
    edit(i, 'm42235', 'import-auto-id1169738052034', new=old[old.index('>') + 1:start])
    detail('E. Remove the all-thermal-energy claim', 'Keep the formula’s unattainable zero-kelvin limit. Delete the additional claim that converting all incoming heat to work means removing all thermal energy; that does not follow from the efficiency equation.', [limits])

    edit(i, 'm67128', 'import-auto-id1169737818788', [
        ('Entropy is <emphasis effect="italics">not</emphasis> conserved but increases in all real processes.', 'The total entropy of a system and its surroundings increases in irreversible processes.'),
        ('Reversible processes (such as in Carnot engines) are the processes in which the most heat transfer to work takes place and are also the ones that keep entropy constant.', 'For engines operating between the same two heat reservoirs, reversible processes yield the most work for a given heat input and keep the combined entropy of the system and its surroundings constant.')])
    detail('F. A connected entropy paragraph missed by the earlier scope edits', 'This paragraph still states general entropy/work claims without identifying whose entropy or what is held fixed. Coordinate it with P3-06 and retain the surrounding energy/work connection.', [limits, ent])

    edit(i, 'm42235', 'eip-id1557992', [
        ('of the Carnot efficiency, which is much higher than the best-ever achieved of about 70%, so her scheme is likely to be fraudulent.', 'of the Carnot efficiency. The claimed efficiency is below the Carnot limit, so these numbers alone do not establish that the scheme is fraudulent.')])
    detail('G. A leftover unsupported exercise-solution conclusion', 'The worked 48%, 50%, and 96% values are unchanged. U3-15 removed the unsupported universal 70% claim from the body, but it survives here. Remove that basis for calling the inventor fraudulent; this does not endorse the device.', [limits])
    i['math_change'] = 'Numbered equations and numeric answers are unchanged. The replacement principle box retains its box/main-statement identifiers but removes the old introductory paragraph and term; its relocation is explicitly recorded. The maintainer’s replacement of the heat-rejection paragraph removes its inline Q_c expression along with the rejected claim; other existing MathML is preserved. The revised heat-pump opening adds an inline Q_h while retaining its existing Q_c, W, and first-law equation. The maintainer’s illustrative loss-model paragraph adds W, W′, and Q_h as native MathML.'
    i['dispositions'] = [
        dict(topic='First B item: reversible-engine efficiency question', disposition='retained unchanged by maintainer decision', reason='Maintainer declined the explicit same-two-reservoir qualification: it can be supplied by context, and students can state reasonable assumptions in their answers. Source target: m67127/import-auto-id1169738189350.'),
        dict(topic='Opening most-efficient-cycle sentence', disposition='retained unchanged by maintainer decision', reason='The maintainer accepts the existing introductory phrasing as sufficiently accurate in context and declined the proposed expansion. This decision concerns import-auto-id1169738108807; the remaining assumption and glossary comparisons are still available for review.'),
        dict(topic='Ideal Carnot terminology', disposition='explicit assumptions proposed', reason='Use explicit reversibility assumptions in this textbook; do not rely on the cycle name alone to supply them.'),
        dict(topic='Carnot engine glossary', disposition='verified unchanged', reason='A heat engine that uses a Carnot cycle remains consistent with the clarified cycle definition.'),
        dict(topic='PV diagram and reversible-stages caption', disposition='verified unchanged', reason='The caption already specifies reversible isothermal/adiabatic paths and the two reservoirs. No redraw or renumbering is needed.'),
        dict(topic='Heat-ratio and efficiency equations; numerical examples', disposition='retained under reversible/two-reservoir assumptions', reason='Illustrative temperatures and numeric solutions are preserved. This is not a new full numerical audit.'),
        dict(topic='Approved P3-05/P3-06 corrections', disposition='preserved', reason='New changes address separate source passages; no replacement of the agreed reservoir/engine conclusion.'),
        dict(topic='Technology prices, COP ranges, and historical wording', disposition='outside this targeted scan', reason='Remain for the planned historical/technology audit; not claimed verified here.')]
    i["status"] = "approved-pending-section-preview"
    i["attention"] = "All letters A–G approved; whole-section reading preview ready for flow review."
    i["authorization"] = "Maintainer approved the remainder of P3-08 (all letters) and requested previews of all affected sections."
    for passage in i["passages"]:
        passage["status"] = "approved-pending-section-preview"
    # Coordinate with the approved HE07 removal of the Otto-efficiency inference.
    old = block('m42235', 'import-auto-id1169737804166')
    revised = old.replace('Just as discussed for the Otto cycle in the previous section, this means that efficiency', 'This means that Carnot efficiency')
    start = revised.index(' (This setup increases the area')
    end = revised.index(' The actual reservoir temperatures', start)
    revised = revised[:start] + revised[end:]
    edit(i, 'm42235', 'import-auto-id1169737804166', new=revised[revised.index('>')+1:revised.rfind('</para>')])
    i['passages'][-1]['review_label']='H. Coordinate the efficiency conclusion with HE07'
    i['passages'][-1]['review_reason']='Remove the superseded Otto-cycle comparison and the loop-area/temperature-difference rationale. Retain the conclusion from the Carnot temperature ratio and the following example lead-in.'
    i['passages'][-1]['status']='maintainer-requested-coordinated-correction'
    edit(i, 'm42235', 'import-auto-id1169737788935', [('Carnot cycles without heat loss may be possible at absolute zero, but this has never been seen in nature.', 'Carnot efficiency approaches 100% as the cold-reservoir temperature approaches absolute zero, but absolute zero cannot be attained.')])
    i['passages'][-1]['review_label']='I. Correct the absolute-zero summary'
    i['passages'][-1]['review_reason']='State the limiting efficiency without suggesting that a cycle at absolute zero can be realized.'
    i['passages'][-1]['status']='approved-pending-section-preview'
    i['passages'][-1]['authorization']='Maintainer approved the replacement sentence and requested the updated preview.'
    edit(i, 'm42236', 'import-auto-id1169738085192', [('(In a cooling cycle, the evaporator and condenser coils exchange roles and the flow direction of the fluid is reversed.)', '(To switch to cooling, a reversing valve changes the refrigerant flow so that the indoor coil acts as the evaporator and the outdoor coil acts as the condenser.)')])
    i['passages'][-1]['review_label']='J. Explain switching a heat pump to cooling'
    i['passages'][-1]['review_reason']='Identify the reversing valve and the roles of the stationary indoor and outdoor coils.'
    i['passages'][-1]['status']='approved-pending-section-preview'
    i['passages'][-1]['authorization']='Maintainer approved the reversing-valve clarification and requested the refreshed preview.'
    i['passages'][-1]['sources']=[source('Natural Resources Canada: Heating and cooling with a heat pump', 'https://natural-resources.canada.ca/energy-efficiency/energy-star/heating-cooling-heat-pump', 'Reversing valve and heating/cooling coil functions')]
    old = block('m42236', 'import-auto-id1169738011941')
    caption = re.search(r'<caption>.*?</caption>', old, re.S).group(0)
    qf = '<m:math><m:msub><m:mi>Q</m:mi><m:mi mathvariant="normal">f</m:mi></m:msub></m:math>'
    revised_caption = '<caption>This figure models losses in a heat pump. Only a portion '+wp+' of the work input '+w+' reaches the reversible heat pump; the remainder is dissipated as heat '+qf+' into the cold reservoir. For the same total work input and reservoir temperatures, these losses reduce the heat delivered to the hot reservoir and therefore reduce the coefficient of performance.</caption>'
    edit(i, 'm42236', 'import-auto-id1169738011941', [(caption, revised_caption)])
    i['passages'][-1]['review_label']='K. Coordinate the Figure 8.12.4 caption with the loss model'
    i['passages'][-1]['review_reason']='Match the approved reversible-pump loss model and retain the diagram; remove the misleading final claim about adiabatic and isothermal processes.'
    i['passages'][-1]['status']='approved-pending-section-preview'
    i['passages'][-1]['authorization']='Maintainer approved the replacement caption and requested its application to the section preview.'
    edit(i, 'm42236', 'import-auto-id1169737796454', [('Heat pumps are most likely to be economically superior where winter temperatures are mild, electricity is relatively cheap, and other fuels are relatively expensive.', 'Heat pumps are most likely to be economically superior where winter temperatures are mild, electricity is relatively cheap, and other fuels are relatively expensive. The mild winters of the San Francisco Bay Area, home to College of Alameda, are well suited to efficient heat-pump heating.')])
    i['passages'][-1]['review_label']='L. Add the Bay Area climate example'
    i['passages'][-1]['review_reason']='Connect the local climate to heat-pump performance without asserting low electricity prices or guaranteed cost savings.'
    i['passages'][-1]['status']='approved-pending-section-preview'
    i['passages'][-1]['authorization']='Maintainer approved the Bay Area sentence and requested its addition and the refreshed preview.'
    i['passages'][-1]['sources']=[source('California Energy Commission: Development and Testing of the Next-Generation Residential Space Conditioning System for California', 'https://www.energy.ca.gov/sites/default/files/2021-11/CEC-500-2021-049_0.pdf', 'Appendix C, Climate Sensitivity of Savings: Oakland heating hours fall in the range favorable to heat-pump efficiency.')]
    edit(i, 'm42236', 'fs-id1169738116696', [])
    i['passages'][-1]['proposed_xml']=''
    i['passages'][-1]['operation']='remove'
    i['passages'][-1]['review_label']='M. Remove the numerical problem-solving checklist'
    i['passages'][-1]['review_reason']='All seven steps match the pinned CC BY upstream and recovered baseline verbatim apart from formatting. Remove this unadapted numerical checklist from the conceptual treatment.'
    i['passages'][-1]['status']='approved-pending-section-preview'
    i['passages'][-1]['authorization']='Maintainer approved removing the box and its two exercise instructions.'
    for mid, ident, document in [('m42235', 'import-auto-id1169736656664', ' document="m42236"'), ('m42236', 'import-auto-id1169737966585', '')]:
        instruction = ' Explicitly show how you follow the steps in the <link'+document+' target-id="fs-id1169738116696">Problem-Solving Strategies for Thermodynamics</link>.'
        edit(i, mid, ident, [(instruction, '')])
        i['passages'][-1]['review_label']='M. Remove the exercise instruction referring to the deleted box'
        i['passages'][-1]['review_reason']='Preserve the actual question and remove only its final checklist instruction and link.'
        i['passages'][-1]['status']='approved-pending-section-preview'
        i['passages'][-1]['authorization']='Maintainer approved this coordinated cleanup with the box removal.'
    edit(i, 'm42236', 'fs-id1169737812802', [('a machine that generates heat transfer from cold to hot', 'a machine that uses work input to transfer heat from a colder region to a warmer region')])
    i['passages'][-1]['review_label']='N. Align the heat-pump glossary with the text'
    i['passages'][-1]['review_reason']='Include the work input and replace the awkward phrase generates heat transfer.'
    i['passages'][-1]['status']='approved-pending-section-preview'
    i['passages'][-1]['authorization']='Maintainer approved the replacement glossary definition and requested the refreshed preview.'
    return i
