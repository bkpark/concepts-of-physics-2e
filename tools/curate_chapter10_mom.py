"""Apply the October 6 conceptual-gap pass; preserve retained exercise IDs."""
from pathlib import Path
import hashlib, json, re, html
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
C = '{http://cnx.rice.edu/cnxml}'
def read(p): return p.read_bytes().decode('utf-8')
def savejson(p, d): p.write_text(json.dumps(d, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
labels = [x for x in json.loads(read(ROOT/'metadata/numbering-course-2026-07-07.proposed.json'))['section_labels'] if x['label'].startswith('10.')]
before = {x['section_id'].split(':')[1]: read(ROOT/f"maintained/modules/{x['section_id'].split(':')[1]}/index.cnxml") for x in labels}
after = dict(before)
export = json.loads(read(ROOT.parent/'reference-inputs/phys-10-full-export-2026-09-27.imas'))['questionset']
additions = []
def add(mid, slug, text, answer, sources, rationale):
    eid = 'c10-mom-'+slug
    block = f'<exercise id="{eid}"><problem id="{eid}-problem"><para id="{eid}-p1">{html.escape(text)}</para></problem></exercise>'
    s = after[mid]
    match = re.search(r'<section\b[^>]*(?:class|type)="conceptual-questions"[^>]*>', s)
    if match:
        at = s.index('</section>', match.end())
        s = s[:at]+'\n'+block+'\n'+s[at:]
    else:
        s = s.replace('</content>', f'<section id="{mid}-conceptual-additions" class="conceptual-questions" type="conceptual-questions"><title>Questions and Exercises</title>\n{block}\n</section></content>', 1)
    after[mid] = s
    additions.append(dict(id=eid,module=mid,text=text,answer=answer,rationale=rationale,sources=[dict(export_locator=i,uniqueid=str(export[i]['uniqueid']),description=export[i]['description']) for i in sources],provenance='New explanation prompt aligned with the cited frozen-export objectives; no source images reused.' if sources else 'New textbook overview prompt; supported by section introduction.'))

add('m52408','everyday-magnetism','Give one example of a natural phenomenon and one example of a technology involving magnetism that are discussed in this introduction. What role does magnetism play in each?', 'Examples: Earth’s magnetic field shapes auroras; a compass uses a magnet’s response to Earth’s field for navigation. Other examples described in the introduction are acceptable, with an appropriate role.', [], 'Overview question answerable from the introduction, without requiring later mechanisms.')
add('m52412','compass-poles','The north-seeking end of a compass points roughly toward geographic north. Does the region near Earth’s geographic North Pole behave like the north or the south pole of a bar magnet? Explain.', 'Like a south pole: it attracts the compass’s north-seeking pole. Geographic names should not be confused with magnetic polarity.', ['583'], 'Separate geographic direction from magnetic polarity.')
add('m52412','cut-magnet','A bar magnet is cut into two shorter pieces. What magnetic poles would you expect each piece to have? How does this differ from separating positive and negative electric charges?', 'Each piece has both north and south poles; cutting does not isolate one magnetic pole. Objects with net positive or negative electric charge can be separated.', ['585'], 'Concrete application of paired poles, rather than another field-line comparison.')
add('m52410','domains','An unmagnetized iron nail contains magnetic domains. Why does it not necessarily act as a strong magnet? Explain what changes when the nail becomes magnetized and what can happen if it is heated above its Curie temperature.', 'Differently oriented domains largely cancel. Magnetization favors aligned domains. Above the Curie temperature, thermal disorder destroys ferromagnetic order; previous permanent magnetization is lost. Cooling does not necessarily restore the previous magnetization.', ['586'], 'Fill domain and temperature coverage before the retained geology application.')
add('m52417','motor','How can magnetic forces on opposite sides of a current-carrying loop make the loop rotate? Why must the current reverse every half-turn in the simple motor described in this section?', 'Opposite forces acting at different positions provide a torque. Reversing current after each half-turn keeps the torque in the same rotational direction, rather than letting it reverse and drive oscillation.', ['593'], 'Motor mechanism and sustained rotation, without another numerical force calculation.')
add('m52420','wire-field','A straight wire carries a current toward you, out of the page. Sketch the magnetic field lines around the wire and indicate their direction. What changes if the current reverses?', 'Concentric circles centered on the wire, counterclockwise viewed from the stated side; reversing current reverses the circulation to clockwise.', ['595'], 'Distinguish the field produced by current from the force on current.')
add('m52420','coil-field','Compare the magnetic field pattern around a long straight current-carrying wire with the pattern around a current-carrying solenoid. Which resembles the field of a bar magnet? Describe the field inside a long solenoid away from its ends.', 'Straight-wire field lines circle the wire. A solenoid’s exterior field resembles a bar magnet’s; inside a long solenoid, away from its ends, the field is nearly uniform and directed along its axis.', ['594'], 'Field geometry rather than repetitive formula substitution.')
add('m70744','generator','A coil rotates in a steady magnetic field and supplies a current to a connected resistor. Explain why a voltage can be induced even though the magnetic field is steady. Where does the energy dissipated in the resistor come from?', 'Rotation changes the flux through the coil. Mechanical work turning the coil supplies the electrical energy dissipated in the resistor; the steady magnetic field is not a free energy supply.', ['596','597'], 'Clarify that flux, not necessarily field strength, must change; connect induction to energy.')
add('m70744','lenz-change','A closed conducting loop is held fixed while the magnetic field through it increases in strength without changing direction. What is the direction of the magnetic field produced by the induced current relative to the applied field? How does your answer change when the applied field decreases instead?', 'For increasing applied flux, the induced field opposes the applied field; for decreasing flux, it points in the same direction. In both cases it opposes the change, not necessarily the applied field itself.', ['596'], 'Explicit Lenz-law distinction; extends the induction objective using the section’s stated law.')

# Move the retained geology question to the domain/Curie-temperature section.
pattern = r'<exercise\b[^>]*id="fs-id1735677"[^>]*>.*?</exercise>'
block = re.search(pattern, after['m52412'], re.S).group()
after['m52412'] = re.sub(pattern, '', after['m52412'], count=1, flags=re.S)
s = after['m52410']; at = s.index('</section>', s.index('id="m52410-conceptual-additions"'))
after['m52410'] = s[:at]+block+'\n'+s[at:]

# Approved merger of preview-84 Exercises 35 and 37.
s = after['m67131']
pattern = r'(<exercise\b[^>]*id="fs-id1332162"[^>]*>).*?</exercise>'
new = 'A 500-W room heater operates on a 120 V rms AC supply. (a) What is the rms current through the heater? (b) If its heating element is made of nichrome wire, what resistance must the wire have to produce this power?'
s, n = re.subn(pattern, lambda m:m[1]+'<problem id="fs-id1035910"><para id="import-auto-id1500293">'+new+'</para></problem></exercise>',s,count=1,flags=re.S); assert n==1
s, n = re.subn(r'<exercise\b[^>]*id="fs-id1698350"[^>]*>.*?</exercise>', '', s,count=1,flags=re.S); assert n==1
after['m67131'] = s

# Conceptual transformer questions precede its numerical applications.
mid='m52427'; hits=list(re.finditer(r'<exercise\b[^>]*>.*?</exercise>',after[mid],re.S))
blocks={re.search(r'id="([^"]+)"',m[0])[1]:m[0] for m in hits}
order=['fs-id1169737995226','fs-id1169737965228','fs-id1169738257565','fs-id1169738183082']
assert set(blocks)==set(order)
# Replace contents in existing slots, retaining their containing sections.
it=iter(order)
after[mid]=re.sub(r'<exercise\b[^>]*>.*?</exercise>',lambda m:blocks[next(it)],after[mid],flags=re.S)

ledgerpath=ROOT/'maintained/editorial-changes.json'; ledger=json.loads(read(ledgerpath))
for mid,s in after.items():
    root=ET.fromstring(s)
    ids=[e.get('id') for e in root.iter() if e.get('id')]; assert len(ids)==len(set(ids)),mid
    if s==before[mid]: continue
    pid='EX-C10-MOM-CONCEPTUAL-PASS-'+mid
    path=Path('proposals/author-corrections')/(pid+'.json'); assert path.as_posix() not in ledger['changes']
    record=dict(id=pid,status='applied-maintainer-approved',target_release='cp2e-ver1.1',module=mid,source_path=f'maintained/modules/{mid}/index.cnxml',source_sha256=hashlib.sha256(before[mid].encode()).hexdigest(),after_sha256=hashlib.sha256(s.encode()).hexdigest(),before=before[mid],after=s,reason='Authorized Chapter 10 MyOpenMath conceptual-gap pass, topic ordering, and approved heater merger; new wording ready for maintainer review.')
    savejson(ROOT/path,record); (ROOT/record['source_path']).write_bytes(s.encode()); ledger['changes'].append(path.as_posix())
savejson(ledgerpath,ledger)
old=json.loads(read(ROOT/'reports/1.1/chapter10-structure/preview84-question-inventory.json'))
oldnums={q['id']:q['number'] for q in old}; newbyid={q['id']:q for q in additions}
inventory=[]; coverage=[]
for label in labels:
    mid=label['section_id'].split(':')[1]; root=ET.fromstring(after[mid]); count=0
    for e in root.iter(C+'exercise'):
        # Exclude legacy StarMath annotations from readable report text.
        for parent in e.iter():
            for child in list(parent):
                if child.tag.endswith('}annotation'): parent.remove(child)
        eid=e.get('id'); row=dict(number=len(inventory)+1,section=label['label'],module=mid,id=eid,preview84_number=oldnums.get(eid),text=' '.join(''.join(e.itertext()).split()))
        if eid in newbyid: row.update(answer=newbyid[eid]['answer'],sources=newbyid[eid]['sources'])
        if eid=='fs-id1332162': row['answer']='(a) 500/120 = 4.17 A rms. (b) 120^2/500 = 28.8 ohms.'; row['merged_preview84_numbers']=[35,37]
        inventory.append(row); count+=1
    assert count>0,label['label']
    coverage.append(dict(section=label['label'],title=label['title'],count=count))
assert len(inventory)==45
out=ROOT/'reports/1.1/chapter10-structure'
savejson(out/'mom-review-question-set.json',dict(status='Applied to maintained source; pending preview refresh and maintainer review',source_export='phys-10-full-export-2026-09-27.imas',coverage=coverage,additions=additions,questions=inventory))
lines=['# Chapter 10: conceptual additions and reordered questions','', '45 questions: 36 retained after the heater merger, plus 9 conceptual additions. Preview not yet refreshed. Answers below are internal records for the new and merged questions.','', '## Coverage','']
lines += [f"- {c['section']} {c['title']}: {c['count']} questions" for c in coverage]
lines += ['', '## Questions in new order','']
for q in inventory:
    origin=f"preview 84 Exercise {q['preview84_number']}" if q['preview84_number'] else 'new conceptual question'
    lines += [f"### {q['number']}. Section {q['section']} ({origin})",'',q['text'],'']
    if 'answer' in q: lines += ['Internal answer: '+q['answer'],'']
    if q.get('sources'): lines += ['MyOpenMath source unique IDs: '+', '.join(s['uniqueid'] for s in q['sources']), '']
lines += ['## Selection notes','','No extra quantitative questions or right-hand-force drills were added. The introduction gets an overview question. Rock magnetization follows domains in 10.3. Transformer conceptual questions precede calculations. The retained exercise figures and IDs are preserved. The heater retains Exercise 35’s ID; Exercise 37’s separate block is removed.','','The source induction multiple-choice question identifies changing magnetic field as necessary; the adaptation correctly uses changing magnetic flux, allowing a rotating coil in a steady field. No eddy-current demonstration question was added because Section 10.10 does not develop that example. No live MyOpenMath content was changed.']
(out/'mom-review-question-set.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
with (ROOT/'docs/exercise-revision-1.1.md').open('a',encoding='utf-8') as f: f.write('\n- 2026-10-06: Applied Chapter 10 conceptual-gap pass: nine additions (eight aligned with frozen MyOpenMath objectives and one introduction overview), geology moved to 10.3, transformer conceptual-first ordering, and approved heater merger. 45 questions; every section has a conceptual question. See reports/1.1/chapter10-structure/mom-review-question-set.md for numbering, source locators and new/merged internal answers. Pending preview refresh.\n')
print('Applied 45-question Chapter 10 set; XML/IDs and all-section coverage validated.')
