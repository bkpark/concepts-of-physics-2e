"""Apply the approved 63 retained/revised exercises plus ten separate MOM adaptations."""
from pathlib import Path
import collections,hashlib,html,json,re,xml.etree.ElementTree as E
R=Path(__file__).resolve().parents[1];O=R/'reports/1.1/chapter14-structure';C='{http://cnx.rice.edu/cnxml}'
proposal=json.loads((O/'exercise-review-proposal.json').read_text(encoding='utf-8'))
proposal['source_sha256']={k.replace(chr(92),'/'):v for k,v in proposal['source_sha256'].items()}
old={q['number']:q for q in proposal['exercises']}
sections=json.loads((O/'review.json').read_text(encoding='utf-8'))['sections']
mods={s['section']:s['module'] for s in sections}
before={mid:(R/f'maintained/modules/{mid}/index.cnxml').read_bytes().decode('utf-8') for mid in mods.values()}
for mid,src in before.items():assert hashlib.sha256(src.encode()).hexdigest()==proposal['source_sha256'][f'maintained/modules/{mid}/index.cnxml'],mid
export=json.loads((R.parent/'reference-inputs/phys-10-full-export-2026-09-27.imas').read_bytes())

additions={
 'A1':('14.2',778,'For each source below, suggest a suitable shielding material and explain your choice: (a) a source of alpha particles, (b) a source of beta-minus particles, and (c) a source of gamma rays. Why must the particle energy and shield thickness also be considered?'),
 'A2':('14.2',779,'Match each description to alpha, beta-minus, beta-plus, or gamma radiation: (a) a helium-4 nucleus, (b) an electron, (c) a positron, and (d) a high-energy photon. Give the electric charge of each in units of the positive elementary charge.'),
 'A3':('14.3',780,'A student says, “Gamma rays cannot ionize matter because photons have no electric charge.” Another says, “All radiation damages cells in the same way.” Explain what is wrong with each statement, using the energy transferred in an interaction.'),
 'A4':('14.4',781,'Which statements correctly describe the interaction that binds protons and neutrons in ordinary nuclei? Explain each choice. (a) It is effective only over very short distances. (b) It acts only between protons. (c) It can overcome electric repulsion between neighboring protons. (d) It is the same inverse-square force that binds electrons to nuclei.'),
 'A5':('14.7',782,'Consider a conventional X-ray image, a CT scan, a PET scan, an MRI scan, and an ultrasound image. (a) Which use ionizing radiation? (b) Which of these uses a radioactive substance administered to the patient? (c) Does receiving an X-ray image ordinarily make the patient radioactive? Explain.'),
 'A6':('14.8',783,'A worker must briefly handle equipment near a sealed gamma-ray source. Suggest one change involving time, one involving distance, and one involving shielding that could reduce exposure. Explain why a pair of ordinary disposable gloves cannot substitute for these measures against the gamma rays.'),
 'A7':('14.10',784,'A heavy nucleus splits into two smaller nuclei in one reaction; two light nuclei combine in another. (a) Name the two processes. (b) Which powers the Sun? (c) Can both release energy? (d) When either releases energy, how does the total rest mass of the products compare with that of the reactants?'),
 'A8':('14.13',785,'Using the particle table and the quark model, classify each of these as a lepton, meson, baryon, or gauge boson: electron, tau, muon neutrino, pion, kaon, proton, neutron, photon, and gluon. Which of these are composite particles? Explain why “heavier particle” is not a reliable definition of baryon.'),
 'A9':('14.4',786,'Give the numbers of protons and neutrons in carbon-12, carbon-14, cobalt-60, cesium-137, and uranium-238. The atomic numbers are 6 for carbon, 27 for cobalt, 55 for cesium, and 92 for uranium. Which two listed nuclides are isotopes of the same element, and how do you know?'),
 'A10':('14.6',787,'Carbon-14 has a half-life of 5730 years. Assume that a closed sample initially contains 1600 carbon-14 atoms. (a) About how many remain after 11,460 years? (b) If about 200 remain, how much time has passed? Show your reasoning as a sequence of halvings rather than using logarithms.')}
orders={
 '14.2':[4,1,'A2',6,2,8,'A1',25,9,5],
 '14.3':[12,'A3',11,10],
 '14.4':[16,18,'A9',17,15,'A4'],
 '14.5':[39,33,47,45,35,37,30,32],
 '14.6':[61,60,67,'A10',68,62,83,63],
 '14.7':[90,'A5',88,89,92,93],
 '14.8':[97,98,103,100,'A6'],
 '14.9':[112,113,119,114],
 '14.10':[133,'A7',142,138,136,137,140],
 '14.11':[153,152],
 '14.12':[164],
 '14.13':[166,171,178,169,174,173,'A8',167,170],
 '14.14':[185,184,183]}
chosen=[n for order in orders.values() for n in order];assert len(chosen)==len(set(chosen))==73
assert {n for n in chosen if isinstance(n,int)}=={n for n,q in old.items() if q['action']!='Remove'}

def mi(x):return '<m:mi>'+x+'</m:mi>'
def mn(x):return '<m:mn>'+x+'</m:mn>'
def mo(x):return '<m:mo>'+html.escape(x)+'</m:mo>'
def row(x):return '<m:mrow>'+x+'</m:mrow>'
def sup(x,y):return '<m:msup>'+x+y+'</m:msup>'
def sub(x,y):return '<m:msub>'+x+y+'</m:msub>'
def math(x):return '<m:math xmlns:m="http://www.w3.org/1998/Math/MathML">'+row(x)+'</m:math>'
def isotope(a,s):return '<m:mmultiscripts><m:mtext>'+s+'</m:mtext><m:mprescripts/><m:none/>'+mn(a)+'</m:mmultiscripts>'
def nu(s,bar=False):return sub('<m:mover accent="true">'+mi('ν')+'<m:mo>¯</m:mo></m:mover>' if bar else mi('ν'),'<m:mi mathvariant="italic">'+s+'</m:mi>')
def particle(s,charge):return sup(mi(s),mo(charge))
def sci(v,p,u):return mn(v)+mo('×')+sup(mn('10'),mn(p))+'<m:mspace width="0.167em"/><m:mtext>'+u+'</m:mtext>'
expressions={
 'n → p + e⁻ + ν̄ₑ':mi('n')+mo('→')+mi('p')+mo('+')+particle('e','−')+mo('+')+nu('e',True),
 'μ⁻ → e⁻ + ν̄ₑ + νμ':particle('μ','−')+mo('→')+particle('e','−')+mo('+')+nu('e',True)+mo('+')+nu('μ'),
 'n + ²³⁵U → ⁹²Kr + ¹⁴²Ba + x n':mi('n')+mo('+')+isotope('235','U')+mo('→')+isotope('92','Kr')+mo('+')+isotope('142','Ba')+mo('+')+mi('x')+mi('n'),
 '4p + 2e⁻ → ⁴He + 2νₑ + released energy':mn('4')+mi('p')+mo('+')+mn('2')+particle('e','−')+mo('→')+isotope('4','He')+mo('+')+mn('2')+nu('e')+mo('+')+'<m:mtext>released energy</m:mtext>',
 'E = Δmc²':mi('E')+mo('=')+mi('Δm')+sup(mi('c'),mn('2')),
 'c = 3.0 × 10⁸ m/s':mi('c')+mo('=')+sci('3.0','8','m/s'),
 '5.0 × 10¹³ J':sci('5.0','13','J'),
 '1 MeV = 10⁶ eV':mn('1')+'<m:mspace width="0.167em"/><m:mtext>MeV</m:mtext>'+mo('=')+sup(mn('10'),mn('6'))+'<m:mspace width="0.167em"/><m:mtext>eV</m:mtext>',
 'Lₑ = +1':sub(mi('L'),mi('e'))+mo('=')+mo('+')+mn('1'),
 'Lₑ':sub(mi('L'),mi('e'))}
def markup(text):
 saved=[]
 def stash(v):saved.append(math(v));return '@@M'+str(len(saved)-1)+'@@'
 for phrase,v in sorted(expressions.items(),key=lambda x:-len(x[0])):text=text.replace(phrase,stash(v))
 text=re.sub(r'Z = (\d+)',lambda m:stash(mi('Z')+mo('=')+mn(m[1])),text)
 text=re.sub(r'(?<!\w)([ZA])(?=\b)',lambda m:stash(mi(m[1])),text)
 text=html.escape(text,quote=False)
 text=re.sub(r'(?<=\d) (?=(?:Bq|eV|MeV|mm|cm|kg|g|J)(?:\b|[.,;)]))','\u00a0',text)
 for i,v in enumerate(saved):text=text.replace('@@M'+str(i)+'@@',v)
 assert '@@M' not in text
 return text

def body(text,eid):
 # Standalone paragraphs for lettered parts, preserving the reviewed prose.
 chunks=re.split(r' (?=\([a-d]\) )',text)
 return ''.join('<para id="'+eid+'-p'+str(i+1)+'">'+markup(t)+'</para>' for i,t in enumerate(chunks))
blocks={mid:[] for mid in before};manifest=[]
for sec,seq in orders.items():
 mid=mods[sec]
 for key in seq:
  num=len(manifest)+1
  if isinstance(key,int):
   q=old[key];eid=q['id'];src=before[q['module']]
   match=re.search(r'<exercise\b[^>]*id="'+re.escape(eid)+r'"[^>]*>.*?</exercise>',src,re.S);assert match
   if q['action']=='Keep':
    block=match[0]
    if q['level']=='Optional extension':block=re.sub(r'(<para\b[^>]*>)',r'\1<emphasis effect="bold">Extension.</emphasis> ',block,count=1)
   else:
    prefix='<para id="'+eid+'-extension"><emphasis effect="bold">Extension.</emphasis></para>' if q['level']=='Optional extension' else ''
    block=f'<exercise id="{eid}" type="conceptual-questions"><problem id="{eid}-revised-problem">'+prefix+body(q['proposed'],eid+'-revised')+'</problem></exercise>'
   info=dict(old_number=key,old_module=q['module'],action=q['action'],level=q['level'],prompt=q['proposed'] or q['text'])
  else:
   asec,loc,text=additions[key];assert asec==sec;eid='c14-mom-'+key.lower();block=f'<exercise id="{eid}" type="conceptual-questions"><problem id="{eid}-problem">'+body(text,eid)+'</problem></exercise>'
   q=export['questionset'][str(loc)]
   info=dict(old_number=None,action='Add',level='Core',prompt=text,source_description=q['description'],source_uniqueid=str(q['uniqueid']),source_assessment='Question Set 12: Nuclear and Particle Physics',export_locator=loc,adaptation='New standalone fixed wording aligned with this question family; source code and grading material not published.')
  blocks[mid].append(block);manifest.append(dict(number=num,section=sec,module=mid,id=eid,**info))

group=re.compile(r'<section\b[^>]*>(?:(?!<section\b).)*?</section>',re.S)
def no_groups(src):
 root=E.fromstring(src)
 for parent in root.iter():
  for child in list(parent):
   t=child.find(C+'title')
   if child.tag==C+'section' and t is not None and t.text=='Questions and Exercises':parent.remove(child)
 for e in root.iter():
  if e.text is not None and not e.text.strip():e.text=None
  if e.tail is not None and not e.tail.strip():e.tail=None
 return E.tostring(root,encoding='unicode')
after={}
for mid,src in before.items():
 inserted=[False]
 def change(m):
  b=m[0]
  if '<title>Questions and Exercises</title>' not in b:return b
  if inserted[0]:return ''
  inserted[0]=True
  return b[:b.index('>')+1]+'<title>Questions and Exercises</title>\n'+'\n'.join(blocks[mid])+'\n</section>'
 after[mid]=group.sub(change,src)
 assert not blocks[mid] or inserted[0]
 assert no_groups(src)==no_groups(after[mid]),mid
 root=E.fromstring(after[mid]);ids=[e.get('id') for e in root.iter() if e.get('id')];assert len(ids)==len(set(ids)),mid
 assert len(list(root.iter(C+'exercise')))==len(blocks[mid]),mid

# Detect unresolved internal links caused by removal or movement before writing.
all_text={p.parent.name:p.read_text(encoding='utf-8') for p in (R/'maintained/modules').glob('*/index.cnxml')};all_text.update(after)
ids={mid:{e.get('id') for e in E.fromstring(s).iter() if e.get('id')} for mid,s in all_text.items()}
removed_ids={(mid,i) for mid,s in before.items() for i in {e.get('id') for e in E.fromstring(s).iter() if e.get('id')}-ids[mid]}
bad=[]
for mid,s in all_text.items():
 for e in E.fromstring(s).iter(C+'link'):
  dest=(e.get('document',mid),e.get('target-id'))
  if dest in removed_ids:bad.append((mid,dest))
assert not bad,bad
ledgerpath=R/'maintained/editorial-changes.json';ledger=json.loads(ledgerpath.read_text(encoding='utf-8'))
changes=[]
for mid,src in before.items():
 if src==after[mid]:continue
 rel=f'maintained/modules/{mid}/index.cnxml'
 changes.append({'source':rel,'before_sha256':hashlib.sha256(src.encode()).hexdigest(),'after_sha256':hashlib.sha256(after[mid].encode()).hexdigest(),'before':src,'after':after[mid]})
record='proposals/maintainer-corrections/EX-C14-APPROVED-73-QUESTIONS.json';assert record not in ledger['changes']
(R/record).write_text(json.dumps({'status':'applied-maintainer-approved','reason':'Apply approved 19 keep / 44 revise / 132 remove decisions; add ten separate MyOpenMath-aligned questions; latest maintainer instruction authorizes consecutive renumbering in textbook topic order. Crosswalk is internal.','changes':changes},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for mid,s in after.items():
 if s!=before[mid]:(R/f'maintained/modules/{mid}/index.cnxml').write_bytes(s.encode('utf-8'))
ledger['changes'].append(record);ledgerpath.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(O/'applied-question-set.json').write_text(json.dumps({'count':73,'retained':63,'additions':10,'optional_extensions':18,'status':'applied; pending build and publication','questions':manifest,'removed_prior_numbers':[n for n,q in old.items() if q['action']=='Remove'],'body_prose_unchanged':True,'dangling_links_from_removed_content':bad},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(O/'applied-number-crosswalk.json').write_text(json.dumps([{'old_number':q['old_number'],'new_number':q['number'],'module':q['module'],'id':q['id'],'action':q['action']} for q in manifest],indent=2)+'\n',encoding='utf-8')
for path in ['docs/exercise-revision-1.1.md','docs/next-release-1.1.md']:
 with (R/path).open('a',encoding='utf-8') as f:f.write('\n- Chapter 14: applied the approved exercise review (19 keep, 44 revise, 132 remove), plus ten separate fixed MyOpenMath-aligned questions. Final 73 questions follow textbook topic order and, per the maintainer’s subsequent instruction, are renumbered 1–73. Eighteen optional extensions are marked. Body prose unchanged; internal crosswalk and provenance: reports/1.1/chapter14-structure/applied-question-set.json.\n')
print(json.dumps({'count':len(manifest),'modules_changed':len(changes),'added':10,'retained_revised':63,'dangling_links':bad}))
