"""Read-only glossary audit of maintained text plus current approved/proposed preview.

Symbol occurrence is evidence, not proof of the intended meaning. No glossary
entries are removed by this script. Image pixels are not searched.
"""
from pathlib import Path
import xml.etree.ElementTree as E
import re,json,html,hashlib
from collections import defaultdict,Counter
ROOT=Path(__file__).resolve().parents[1]
C='{http://cnx.rice.edu/cnxml}'; M='{http://www.w3.org/1998/Math/MathML}'
def text(e):
 if e.tag==M+'annotation':return ''
 return (e.text or '')+''.join(text(c)+(c.tail or '') for c in e)
def plain(e):return ' '.join(text(e).split())
def norm(s):return re.sub(r'\s+','',s).replace('−','-').replace('ϕ','φ').replace('′',"'")
preview=ROOT/'prototype/dist/review-1.1/priority3-sections/source'
docs={}; index=defaultdict(list); passages=[]
for path in sorted((ROOT/'maintained/modules').glob('*/index.cnxml')):
 mid=path.parent.name
 if mid=='m42709':continue
 chosen=preview/mid/'index.cnxml'
 if not chosen.exists():chosen=path
 r=E.parse(chosen).getroot();parents={c:e for e in r.iter() for c in e}
 title=plain(r.find(C+'title'));docs[mid]=dict(title=title,path=str(chosen.relative_to(ROOT)),sha256=hashlib.sha256(chosen.read_bytes()).hexdigest())
 for e in r.iter():
  if e.tag in [C+'para',C+'caption',C+'meaning',C+'item',C+'row',C+'media']:
   passages.append(dict(module=mid,title=title,id=e.get('id'),text=e.get('alt','') if e.tag==C+'media' else plain(e)))
 for math in r.iter(M+'math'):
  q=math
  while q in parents and q.tag not in [C+'para',C+'equation',C+'row',C+'item',C+'caption']:q=parents[q]
  ev=dict(module=mid,title=title,id=q.get('id'),text=plain(q)[:1100])
  keys={norm(text(e)) for e in math.iter() if e.tag.startswith(M) and e.tag not in [M+'annotation',M+'semantics']}
  for key in keys:
   if key and ev not in index[key]:index[key].append(ev)
groups=[
 ('G01','Circuit-analysis leftovers',[56,57,118,136,179,191,264,325,326,331],
  'No RC/RL time-constant treatment, self/mutual-inductance calculation, reactance, impedance, or RLC-series formula remains. A passing mention of inductors does not introduce these symbols.', ['time constant','self-inductance','mutual inductance','reactance','impedance','RLC','RC circuit','RL circuit']),
 ('G02','Removed cosmology and particle topic',[52,59],
  'Critical density and the upsilon meson occur only in the glossary. The rho_c in the buoyancy example means coin density, not cosmological critical density.', ['critical density','upsilon']),
 ('G03','Unintroduced material/transport coefficients',[11,14,35,38,40,97,216,258,327,329],
  'No corresponding coefficient/formula was found. Gaseous diffusion and dielectric heating are mentioned, but neither defines diffusion constant D, x_rms, or dielectric constant kappa.', ['resistivity','volume coefficient','viscosity','contact angle','dielectric constant','diffusion constant','Reynolds','Young\'s modulus']),
 ('G04','Unused trigonometric functions and phase notation',[61,95,96,278],
  'Cotangent, cosecant, secant, and phase angle phi were not found in the course content; retain sine, cosine, and tangent.', ['cotangent','cosecant','secant','phase angle']),
 ('G05','Specialized quantum notation',[166,167,180,181,189,203,208,280],
  'The removed detailed quantization treatment supplied these entries. No K-alpha/K-beta/L-alpha line notation or these orbital/spin projection symbols was found in the retained text. General spin and orbital angular momentum remain.', ['Kα','Kβ','Lα','K-alpha','K-beta','angular momentum projection','spin projection']),
 ('G06','Compound optical instruments',[190,198,201,205],
  'No angular-magnification or compound objective/eyepiece magnification treatment remains. Keep ordinary image magnification m.', ['angular magnification','eyepiece','objective lens','overall magnification']),
 ('G07','Unused capacitor-energy symbol',[114],
  'The parallel-plate capacitor is mentioned, but E_cap and a stored-energy calculation for it were not found.', ['energy stored in a capacitor','Ecap']),
 ('G08','Removed mechanical-advantage treatment',[130,132,200],
  'No mechanical-advantage discussion, input/output force notation, or matching figure alternative text was found. These entries came from a more detailed treatment of machines.', ['mechanical advantage','input force','output force']),
 ('G09','Energy bookkeeping labels no longer used',[117,119,234,235,318],
  'The general concepts of energy input/output and useful work remain, but these particular subscripted labels were not found in text, equations, or figure descriptions. The surviving efficiency treatment uses W, Q_h and Q_c or prose.', ['Ein','Eout','Pin','Pout','Wout']),
 ('G10','Unintroduced wave/charge-density notation',[159,160,214,308],
  'Polarization, electromagnetic waves and current are covered, but these specific symbols and the formulas that introduce them were not found. The polarization section describes field components without Malus-law intensity notation.', ['average intensity','number of free charges per unit volume','total velocity'])
]
judgments=[
 ('J01','Topics mentioned, symbols not established',[18,79,272,283], 'Surface tension, bulk/shear moduli, and superconductivity occur in prose. Their glossary symbols may not be introduced. Recommend removing these symbol entries while retaining the prose. Inspect figure labels if you want to retain them.', ['surface tension','bulk modulus','shear modulus','critical temperature']),
 ('J02','Emf notation',[105], 'Keep epsilon for emf, but remove the Hall-effect alternative: the Hall effect was not found in this book.', ['Hall effect','emf']),
 ('J03','Small terminology corrections',[161,174], 'I_rms is root-mean-square current, not average current. The barred KE entry should describe average kinetic energy, not equate it with all thermal energy. Review these as corrections rather than unused-symbol deletions.', ['root mean square','average kinetic energy']),
 ('J04','Radiation-dose abbreviation',[259], 'The glossary says r or rad. Keep rad; an isolated r is ambiguous and can be confused with the roentgen notation R. The radiation section uses rad. Recommend simplifying the symbol to rad.', ['rad','roentgen']),
 ('J05','Angular momentum and spin symbols',[186,270,271,276], 'The physical concepts remain, but L_orb and capital S / lowercase s quantum-spin notation are not clearly established by the surviving discussion. Check the evidence before removing; L and S have other meanings.', ['orbital angular momentum','intrinsic spin','spin quantum']),
 ('J06','Optical focal point',[124], 'Keep provisionally: focal points are covered and F can occur in diagrams. The automatic F matches mostly refer to force; they do not establish this entry. This needs a targeted figure check only if removal is considered.', ['focal point']),
 ('J07','Notation not established, although the concepts survive',[199,227,233,244,254], 'Atomic masses, absolute/gauge pressure, radiation quality factor and internal resistance are mentioned. These particular labels were not located in their contexts. Recommend removing these symbol entries unless you want to introduce the notation. Keep the topics themselves.', ['atomic mass','absolute pressure','gauge pressure','quality factor','internal resistance'])
]
lookup={n:(key,'remove',reason) for key,title,nums,reason,terms in groups for n in nums}
lookup.update({n:(key,'review',reason) for key,title,nums,reason,terms in judgments for n in nums})
r=E.parse(preview/'m42709/index.cnxml').getroot();rows=[]
for n,row in enumerate(r.iter(C+'row')):
 cells=row.findall(C+'entry')
 if n==0 or len(cells)!=2:continue
 symbol=plain(cells[0]);definition=plain(cells[1]);ev=index.get(norm(symbol),[])
 prose_ev=[]
 if not ev and re.fullmatch(r'[A-Za-z]{2,4}',norm(symbol)):
  prose_ev=[p for p in passages if re.search(r'(?<!\w)'+re.escape(norm(symbol))+r'(?!\w)',p['text'])]
 if prose_ev:ev=prose_ev
 key,status,reason=lookup.get(n,('', 'keep-with-occurrence' if ev else 'keep-provisionally','Retain; review evidence is a symbol occurrence, not a blanket factual certification.' if ev else 'No exact normalized MathML match. Retain pending context/figure check; absence alone does not justify removal.'))
 rows.append(dict(row=n,symbol=symbol,definition=definition,group=key,disposition=status,reason=reason,occurrence_count=len(ev),evidence=ev[:8]))
def hits(terms):
 return [p for p in passages if any(re.search(r'(?<!\w)'+re.escape(term)+r'(?!\w)',p['text'],re.I) for term in terms)][:35]
assert len(rows)==331, 'Audit row references must be reconciled after glossary changes.'
report=dict(scope='All 141 modules, excluding the glossary itself; current preview overlays used where available. MathML, prose, captions, image alternative text and exercises searched. Raster image pixels are not OCR-certified. No changes applied by this audit. P3-09 remains pending.',source_modules=docs,entries=rows,groups=[dict(id=k,title=t,rows=ns,reason=why,search_terms=terms,context=hits(terms),disposition='proposed removal' if k.startswith('G') else 'review') for k,t,ns,why,terms in groups+judgments])
out=ROOT/'reports/1.1/symbol-glossary-audit';out.mkdir(parents=True,exist_ok=True)
(out/'audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
esc=html.escape
page=['<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Symbol glossary audit</title><style>body{font:18px/1.5 Georgia,serif;max-width:1050px;margin:30px auto;padding:0 20px;color:#172b35}table{border-collapse:collapse;width:100%;margin:15px 0}td,th{padding:8px;border:1px solid #ccd;text-align:left;vertical-align:top}th{background:#eef4f4}section{border-top:2px solid #ccd;margin-top:32px}summary{cursor:pointer}code{overflow-wrap:anywhere}input{font:inherit;width:100%;padding:8px}small{color:#456}</style><h1>Symbol glossary audit</h1><p>'+esc(report['scope'])+'</p><p>Review the grouped candidates below. The full inventory includes evidence for every entry and explicitly distinguishes missing matches from verified absence. Nothing in these lists has been deleted automatically.</p><p><a href="../priority3-sections/sections/glossary-of-key-symbols-and-notation/index.html">Current glossary preview</a> · <a href="../priority3-review/#P3-09">Pending P3-09 review</a></p>']
for g in report['groups']:
 page+=['<section id="'+g['id']+'"><h2>'+g['id']+' — '+esc(g['title'])+'</h2><p><b>'+esc(g['disposition'])+'</b>: '+esc(g['reason'])+'</p><table><tr><th>Symbol</th><th>Current definition</th></tr>']
 for row in rows:
  if row['row'] in g['rows']:page+=['<tr><td>'+esc(row['symbol'])+'</td><td>'+esc(row['definition'])+'</td></tr>']
 page+=['</table><details><summary>Search context and potential false positives</summary>']
 for ev in g['context']:page+=['<p><b>'+esc(ev['title'])+'</b> <small>'+esc(ev['module']+' / '+str(ev['id']))+'</small><br>'+esc(ev['text'][:1500])+'</p>']
 if not g['context']:page+=['<p>No matching prose/caption phrases for the listed search terms.</p>']
 page+=['</details></section>']
page+=['<section><h2>Full inventory</h2><input id="filter" placeholder="Filter symbols, definitions, or dispositions"><div id="inventory">']
for row in rows:
 page+=['<details><summary>'+str(row['row'])+'. '+esc(row['symbol'])+' — '+esc(row['definition'])+' <small>['+row['disposition']+']</small></summary><p>'+esc(row['reason'])+'</p>']
 for ev in row['evidence']:page+=['<p><b>'+esc(ev['title'])+'</b> <small>'+esc(ev['module']+' / '+str(ev['id']))+'</small><br>'+esc(ev['text'])+'</p>']
 page+=['</details>']
page+=['</div></section><script>document.getElementById("filter").oninput=e=>{const q=e.target.value.toLowerCase();document.querySelectorAll("#inventory>details").forEach(d=>d.hidden=!d.querySelector("summary").textContent.toLowerCase().includes(q))}</script></html>']
(out/'index.html').write_text('\n'.join(page),encoding='utf-8')
dist=ROOT/'prototype/dist/review-1.1/symbol-glossary-audit';dist.mkdir(parents=True,exist_ok=True);(dist/'index.html').write_text('\n'.join(page),encoding='utf-8')
print(json.dumps(dict(entries=len(rows),dispositions=dict(Counter(r['disposition'] for r in rows))),indent=2))
print('UNMATCHED RETAINED:',[(r['row'],r['symbol'],r['definition']) for r in rows if r['disposition']=='keep-provisionally'])
