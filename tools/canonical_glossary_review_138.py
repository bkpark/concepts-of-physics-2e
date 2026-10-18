from pathlib import Path
import re,json,hashlib,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
sections=json.loads((ROOT/'maintained/sections.json').read_text(encoding='utf-8'))['sections']
by_slug={s['slug']:s for s in sections}
before={s['source']:(ROOT/s['source']).read_bytes() for s in sections}
texts={p:b.decode('utf-8') for p,b in before.items()}
rows=[
('amplitude','simple-harmonic-motion-a-special-periodic-motion','the maximum magnitude of an oscillating quantity’s departure from its equilibrium value'),
('frequency','period-and-frequency-in-oscillations','the number of complete cycles of a periodic process per unit time; measured in hertz, or cycles per second'),
('oscillate','introduction-to-oscillatory-motion-and-waves','to vary repeatedly about an equilibrium value or position'),
('transverse wave','waves','a wave in which the disturbance is perpendicular to the direction of propagation'),
('wavelength','waves','the distance between successive points at the same phase of a periodic wave, such as adjacent crests'),
('electric field','electric-field-concept-of-a-field-revisited','a vector field equal to the electric force per unit positive test charge at each point'),
('electric field lines','electric-field-lines','imaginary curves whose tangents show the direction of the electric field. Closer spacing represents a stronger field'),
('magnetic field','magnetic-fields-and-magnetic-field-lines','a vector field that describes magnetic effects on moving charges, electric currents, and magnetic dipoles'),
('magnetic field lines','magnetic-fields-and-magnetic-field-lines','imaginary curves whose tangents show the direction of the magnetic field. Closer spacing represents a stronger field'),
('Maxwell’s equations','maxwells-equations-electromagnetic-waves-predicted-and-observed','four equations relating electric and magnetic fields to charges, currents, and changes in the fields; together they describe classical electromagnetism and predict electromagnetic waves'),
('gamma ray','the-electromagnetic-spectrum-an-overview','a photon emitted in a nuclear transition; in astronomy, the term also includes very high-energy photons produced by other processes'),
('quantum mechanics','introduction-to-quantum-mechanics','the framework describing matter and radiation in terms of quantum states, with probabilistic predictions for measurement outcomes. Its distinctive effects are especially apparent at atomic and subatomic scales'),
('relativity','einsteins-postulates','the framework describing how measurements of space, time, and motion are related between observers. Special relativity concerns inertial observers; general relativity describes gravity through spacetime curvature'),
('lens power','image-formation-by-lenses','the reciprocal of a lens’s focal length, <m:math><m:mrow><m:mi>P</m:mi><m:mo>=</m:mo><m:mfrac><m:mn>1</m:mn><m:mi>f</m:mi></m:mfrac></m:mrow></m:math>; measured in diopters when <m:math><m:mi>f</m:mi></m:math> is in meters. Converging lenses have positive power, and diverging lenses have negative power'),
('polarized light','polarization','light whose electric-field oscillations have a definite directional pattern. For linearly polarized light, the electric field oscillates along a fixed direction perpendicular to propagation'),
('electric polarization','conductors-and-applications-of-electrostatics','separation or displacement of positive and negative charge within a material, without necessarily changing its net charge'),
]
norm=lambda t:re.sub(r'\s+',' ',t).strip().casefold()
def plain(t):return re.sub('<[^>]*>','',t)
def link(mid,anchor,label,attrs=''):return f'<link{attrs} document="{mid}" target-id="{anchor}">{label}</link>'
log=[]
for term,slug,meaning in rows:
 sec=by_slug[slug]; path=sec['source']; mid=sec['id'].split(':')[1]
 anchor='canonical-'+re.sub('[^a-z0-9]+','-',term.lower()).strip('-')
 oldterm={'lens power':'power','polarized light':'polarized','electric polarization':'polarized'}.get(term,term)
 restricted=term in ['lens power','polarized light','electric polarization']
 definitions=[]
 for p,s in texts.items():
  if restricted and p!=path:continue
  for m in re.finditer(r'<definition\b[^>]*>.*?</definition>',s,re.S):
   tm=re.search(r'<term[^>]*>(.*?)</term>',m.group(),re.S)
   if tm and norm(plain(tm.group(1)))==norm(oldterm):definitions.append((p,m.group()))
 assert definitions,term
 chosen=next((d for p,d in definitions if p==path),definitions[0][1])
 canonical=re.sub(r'(<term[^>]*>).*?(</term>)',lambda m:m.group(1)+term+m.group(2),chosen,count=1,flags=re.S)
 canonical=re.sub(r'(<meaning[^>]*>).*?(</meaning>)',lambda m:m.group(1)+meaning+m.group(2),canonical,count=1,flags=re.S)
 for p,d in definitions:
  texts[p]=texts[p].replace(d,'',1)
  if d!=chosen:
   # Preserve previous incoming anchors on an explicit cross-reference outside the glossary.
   ids=re.findall(r'\bid="([^"]+)"',d)
   aliases=''.join(f'<span id="{i}"/>' for i in ids)
   ref=f'<para>{aliases}For the definition of {link(mid,anchor,term)}, see its introduction.</para>'
   texts[p]=texts[p].replace('</content>',ref+'</content>',1)
  elif p!=path:
   # The selected definition moves to a different section; retain its old addresses.
   ids=re.findall(r'\bid="([^"]+)"',d)
   ref='<para>'+''.join(f'<span id="{i}"/>' for i in ids)+'For the definition of '+link(mid,anchor,term)+', see its introduction.</para>'
   texts[p]=texts[p].replace('</content>',ref+'</content>',1)
 if '</glossary>' in texts[path]:texts[path]=texts[path].replace('</glossary>',canonical+'</glossary>',1)
 else:texts[path]=texts[path].replace('</document>','<glossary>'+canonical+'</glossary></document>',1)
 # Select the existing introduction before replacing term markup with references.
 paras=list(re.finditer(r'<para\b[^>]*>.*?</para>',texts[path],re.S))
 candidates=[m for m in paras if re.search(r'<term\b[^>]*>'+re.escape(oldterm)+r'</term>',m.group(),re.I)]
 if not candidates:candidates=[m for m in paras if norm(oldterm) in norm(plain(m.group())) and 'For the definition of' not in m.group()]
 if not candidates and term=='gamma ray':candidates=[m for m in paras if 'shows how the various types of electromagnetic waves are categorized' in m.group()]
 assert candidates,(term,slug)
 intro=candidates[0].group()
 # Formal term marker now lives in the canonical sentence; old defining uses become links.
 for p in list(texts):
  if restricted and p!=path:continue
  def convert(m):
   if norm(plain(m.group(2)))!=norm(oldterm):return m.group()
   return link(mid,anchor,m.group(2),m.group(1))
  content,sep,tail=texts[p].partition('</content>')
  content=re.sub(r'<term([^>]*)>(.*?)</term>',convert,content,flags=re.S)
  texts[p]=content+sep+tail
 intro2=re.sub(r'<term([^>]*)>(.*?)</term>',lambda m:link(mid,anchor,m.group(2),m.group(1)) if norm(plain(m.group(2)))==norm(oldterm) else m.group(),intro,flags=re.S)
 # Definition is phrased as a short standalone paragraph, avoiding changes to worked examples.
 if term=='oscillate':sentence=f'To <term id="{anchor}">oscillate</term> is {meaning}.'
 else:sentence=f'<term id="{anchor}">{term[0].upper()+term[1:]}</term>: {meaning}.'
 assert intro2 in texts[path],term
 texts[path]=texts[path].replace(intro2,f'<para id="{anchor}-introduction">{sentence}</para>'+intro2,1)
 log.append(dict(term=term,section=slug,canonical_anchor=anchor,removed_duplicates=len(definitions)-1))
# Remove the remaining source-only gluon duplicate, already merged in the rendered preview.
gluons=[]
for p,s in texts.items():
 for m in re.finditer(r'<definition\b[^>]*>.*?</definition>',s,re.S):
  if '<term>gluons</term>' in m.group():gluons.append((p,m.group()))
assert len(gluons)==2
keep=next(x for x in gluons if 'm42671/' in x[0]); target=re.search('id="([^"]+)"',keep[1]).group(1)
for p,d in gluons:
 if (p,d)==keep:continue
 texts[p]=texts[p].replace(d,'',1)
 ids=re.findall(r'\bid="([^"]+)"',d)
 ref='<para>'+''.join(f'<span id="{i}"/>' for i in ids)+'For the definition of '+link('m42671',target,'gluons')+', see The Four Basic Forces.</para>'
 texts[p]=texts[p].replace('</content>',ref+'</content>',1)
changes=[]
for p,s in texts.items():
 a=s.encode('utf-8')
 if a==before[p]:continue
 ET.fromstring(a)
 changes.append(dict(source=p,before_sha256=hashlib.sha256(before[p]).hexdigest(),after_sha256=hashlib.sha256(a).hexdigest(),before=before[p].decode('utf-8'),after=s))
for c in changes:(ROOT/c['source']).write_text(c['after'],encoding='utf-8',newline='')
proposal='proposals/maintainer-corrections/TEXTBOOK-CANONICAL-GLOSSARY.json'
(ROOT/proposal).write_text(json.dumps(dict(status='approved',reason='Approved canonical glossary definitions and introduction points; distinguish lens power, polarized light and electric polarization; preserve legacy anchors and links.',introductions=log,changes=changes),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
r=ROOT/'maintained/editorial-changes.json';d=json.loads(r.read_text(encoding='utf-8'));d['changes'].append(proposal);r.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for f in ['docs/next-release-1.1.md','docs/exercise-revision-1.1.md']:
 with (ROOT/f).open('a',encoding='utf-8') as o:o.write('\nTextbook glossary: applied approved canonical definitions and introduction points; distinguished lens power, polarized light and electric polarization; replaced duplicate glossary definitions with canonical cross-references while preserving previous anchors.\n')
print(json.dumps(dict(changed_modules=len(changes),introductions=log),ensure_ascii=False))
