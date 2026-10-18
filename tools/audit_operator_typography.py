"""Read-only, textbook-wide MathML typography triage; never repairs source."""
from pathlib import Path
import collections, hashlib, html, json, re, sys, unicodedata
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'prototype'))
from native_math import native_math

OUT = ROOT / 'reports/1.1/operator-audit'
M = '{http://www.w3.org/1998/Math/MathML}'
local = lambda e: e.tag.rsplit('}', 1)[-1]
ARITH = set('+−-±∓×÷·⋅∗*/⁄∕∖⊕⊗')
REL = set('=≠≈≃≅≡∼∝<>≤≥≪≫≲≳∈∉∋⊂⊃⊆⊇⊄⊈⊥∥≺≻')
FENCES = set('()[]{}|‖⌈⌉⌊⌋⟨⟩')
LARGE = set('∑∏∐∫∬∭∮⋃⋂')
OTHER = set('∇∂∞∠°′″!%∧∨¬∀∃∅∪∩∴∵∶∷…⋯⋮⋱')
FUNCTIONS = {'sin','cos','tan','cot','sec','csc','sinh','cosh','tanh','arcsin','arccos','arctan','ln','log','exp','lim','max','min','det'}

def family(c):
    if c in ARITH: return 'arithmetic'
    if c in REL: return 'relations and sets'
    if c in FENCES: return 'fences and bars'
    if c in LARGE: return 'large operators'
    if 'ARROW' in unicodedata.name(c, ''): return 'arrows'
    if c in OTHER: return 'other mathematical symbols'
    if unicodedata.category(c) == 'Sm': return 'other Unicode math symbols'
    return None

def visible(e):
    if local(e) in ('annotation','annotation-xml'): return ''
    return (e.text or '') + ''.join(visible(c) + (c.tail or '') for c in e)

def inspect(math):
    parents = {c:p for p in math.iter() for c in p}
    hits = []
    def add(rule, level, e, why):
        hits.append(dict(rule=rule, confidence=level, token=visible(e).strip()[:100],
                         fragment=ET.tostring(e, encoding='unicode')[:1500], reason=why))
    for e in math.iter():
        tag = local(e)
        if tag not in ('mi','mn','mo','mtext','mspace','mrow','mstyle'): continue
        t = (e.text or '').strip()
        if tag in ('mi','mn','mtext') and t:
            chars = [c for c in t if family(c)]
            # Greek letters, differential d, and ordinary identifiers are not operators.
            if chars:
                only = all(family(c) or c.isspace() for c in t)
                risky = any(c in ARITH | REL | LARGE or family(c)=='arrows' for c in chars)
                if only:
                    add('symbol-in-nonoperator-token', 'high' if risky else 'review', e,
                        'Symbol is in '+tag+'; inspect its mathematical role before choosing operator markup.')
                elif risky and (tag != 'mtext' or len(t)<45):
                    add('mixed-text-and-math-token','review',e,
                        'A token mixes an operator with numbers, identifiers, or units; prose and unit slashes may be intentional.')
            if tag=='mtext' and re.fullmatch(r'[0-9]+(?:\.[0-9]+)?',t):
                p=parents.get(e)
                if p is not None and any(local(c)=='mo' and (c.text or '').strip() in ARITH|REL for c in p):
                    add('numeric-text-near-operator','review',e,'Number stored as text beside an operator; can affect spacing and copying.')
            if t in FUNCTIONS and (tag=='mn' or e.get('fontstyle')=='italic' or e.get('mathvariant')=='italic'):
                add('function-typography','review',e,'Named mathematical function has numeric or explicitly italic markup.')
        if tag=='mo':
            if len(t)>8 and re.search(r'[A-Za-z]{3,}',t):
                add('prose-in-operator','high',e,'Operator token appears to contain a prose label or quantity.')
            if re.fullmatch(r'\d+(?:\.\d+)?',t):
                add('number-in-operator','high',e,'A numeric value is tagged as an operator.')
            p=parents.get(e)
            sib=list(p) if p is not None else []
            i=sib.index(e) if e in sib else -1
            # Only flag grouping edges with an operand outside the group. Unary signs
            # and the equals column of an aligned table are not blanket errors.
            if t in ARITH|REL and p is not None and local(p) in ('mrow','mstyle'):
                gp=parents.get(p); outer=list(gp) if gp is not None else []
                j=outer.index(p) if p in outer else -1
                if gp is not None and local(gp) in ('mrow','mstyle','math') and len(sib)>1:
                    edge=(i==0 and j>0) or (i==len(sib)-1 and j<len(outer)-1)
                    if edge and 'form' not in e.attrib:
                        add('operator-at-nested-group-edge','review',e,
                            'Grouping can make an intended binary operator act as a prefix/postfix operator. Check rendered context; unary uses can be valid.')
            if t in ARITH|REL and i>0 and i<len(sib)-1 and e.get('form') in ('prefix','postfix'):
                add('explicit-edge-form-between-operands','review',e,'Explicit prefix/postfix form appears between siblings.')
            if any(k in e.attrib for k in ('lspace','rspace')) and t not in FENCES:
                add('explicit-operator-spacing','low',e,'Manual operator spacing override; aligned equality columns and compact unit slashes are often intentional.')
        if tag in ('mrow','mstyle'):
            children=list(e)
            for a,b,c in zip(children,children[1:],children[2:]):
                if (a.text or '').strip().isdigit() and (b.text or '').strip()=='.' and (c.text or '').strip().isdigit():
                    add('split-decimal','high',e,'Decimal digits and decimal point are separate tokens rather than one number.'); break
        if tag=='mspace':
            match=re.fullmatch(r'(-?[\d.]+)em',e.get('width',''))
            if match and (float(match[1])<0 or float(match[1])>=0.5):
                add('large-or-negative-explicit-space','low',e,'Large/negative explicit space may be layout or an annotation gap; inspect rather than remove automatically.')
    unique = {(h['rule'],h['fragment']):h for h in hits}
    return list(unique.values())

def main():
    identities=json.loads((ROOT/'maintained/sections.json').read_text(encoding='utf-8'))['sections']
    labels={x['section_id'].split(':')[1]:x['label'] for x in json.loads((ROOT/'metadata/numbering-course-2026-07-07.proposed.json').read_text())['section_labels']}
    labels.update(json.loads((ROOT/'maintained/numbering.json').read_text())['course'].get('section_label_overrides',{}))
    findings=[]; inventory=collections.Counter(); total=0; hashes={}; errors=[]
    for section in identities:
        path=ROOT/section['source']; data=path.read_bytes(); hashes[section['source']]=hashlib.sha256(data).hexdigest()
        root=ET.fromstring(data); mid=section['id'].split(':')[-1]
        parents={c:p for p in root.iter() for c in p}
        for index,math in enumerate(root.iter(M+'math'),1):
            total+=1
            for e in math.iter():
                if local(e) in ('annotation','annotation-xml'): continue
                for c in e.text or '':
                    if family(c): inventory[(c,family(c),local(e))]+=1
            hits=inspect(math)
            if not hits: continue
            ancestor=math; context=[]; obj=None; equation=False
            while ancestor is not None:
                equation |= local(ancestor)=='equation'
                if ancestor.get('id') and obj is None: obj=ancestor.get('id')
                if local(ancestor) in ('para','equation','caption','item') and not context:
                    context=[' '.join(visible(ancestor).split())[:1000]]
                ancestor=parents.get(ancestor)
            try: rendered,_=native_math(math,equation)
            except Exception as exc: rendered=''; errors.append(dict(module=mid,index=index,error=str(exc)))
            rank=min({'high':0,'review':1,'low':2}[h['confidence']] for h in hits)
            findings.append(dict(id=f'{mid}-{index:04d}',module=mid,section=labels.get(mid,''),title=section['title'],
                source=section['source'],source_id=obj,math_index=index,confidence=['high','review','low'][rank],
                context=' '.join(context),expression=' '.join(visible(math).split()),
                url='https://intro-1-1.coaphys.xyz/sections/'+section['slug']+'/#'+mid+'--'+(obj or '').encode().hex(),
                source_xml=ET.tostring(math,encoding='unicode'),rendered=rendered,hits=hits))
    # Verify that the audit itself did not alter any maintained source.
    assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in hashes.items())
    OUT.mkdir(parents=True,exist_ok=True)
    counts=collections.Counter(f['confidence'] for f in findings)
    rules=collections.Counter(h['rule'] for f in findings for h in f['hits'])
    summary=dict(modules=len(identities),math_expressions=total,flagged_expressions=len(findings),confidence=dict(counts),rules=dict(rules),render_errors=errors,source_unchanged=True)
    (OUT/'audit.json').write_text(json.dumps(dict(summary=summary,source_hashes=hashes,findings=findings),ensure_ascii=False,indent=2),encoding='utf-8')
    (OUT/'symbol-inventory.json').write_text(json.dumps([dict(symbol=c,name=unicodedata.name(c,'UNNAMED'),family=f,tag=t,count=n) for (c,f,t),n in sorted(inventory.items())],ensure_ascii=False,indent=2),encoding='utf-8')
    payload=json.dumps(findings,ensure_ascii=False).replace('<','\\u003c')
    page='''<!doctype html><meta charset="utf-8"><title>Textbook math typography audit</title>
<style>body{font:17px/1.5 system-ui;margin:30px auto;max-width:1100px;padding:0 20px;color:#18343d;background:#f4f7f7}header{position:sticky;top:0;background:#f4f7f7;padding:12px 0;z-index:1}input,select,button{font:inherit;padding:7px;margin:4px}article{background:white;border:1px solid #cbd8dc;padding:18px;margin:18px 0}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:13px monospace}.formula{overflow:auto;padding:20px;font-size:22px}small{color:#52636b}a{color:#126981}h2{font-size:20px}li{margin:6px 0}</style>
<h1>Textbook-wide math typography audit</h1><p>Read-only candidates, not confirmed errors. No source edits or deployment. Current-renderer previews appear below; the live-page link may still show an earlier publication. Some relocated summary/exercise anchors link onward.</p>
<p>Coverage: arithmetic, relations/sets, arrows, fences/bars, sums/products/integrals, logic, calculus and other Unicode mathematical symbols, plus named functions. Symbols such as ∂, ∞, bars and unit slashes need semantic review; valid unary signs and intentional layout must be preserved. This structural audit cannot prove every spacing defect or mathematical meaning.</p>
<header><select id="level"><option value="high">Higher-confidence candidates</option><option value="review">Needs contextual review</option><option value="low">Low-priority overrides</option><option value="">All confidence levels</option></select><select id="rule"><option value="">All rules</option></select><input id="query" placeholder="Section, module, symbol, text"><button id="prev">Previous</button><button id="next">Next</button><div id="count"></div></header><main id="results"></main>
<script>const data=PAYLOAD;let offset=0;const size=20;const el=id=>document.getElementById(id);const esc=s=>String(s||'').replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
[...new Set(data.flatMap(f=>f.hits.map(h=>h.rule)))].sort().forEach(r=>el('rule').add(new Option(r,r)));
function draw(){const q=el('query').value.toLowerCase(),level=el('level').value,rule=el('rule').value;const rows=data.filter(f=>(!level||f.confidence===level)&&(!rule||f.hits.some(h=>h.rule===rule))&&(!q||[f.section,f.title,f.module,f.expression,f.source_id].join(' ').toLowerCase().includes(q)));offset=Math.min(offset,Math.max(0,Math.floor((rows.length-1)/size)*size));el('count').textContent=`${rows.length} matching expressions; showing ${rows.length?offset+1:0}–${Math.min(offset+size,rows.length)}. Total candidates: ${data.length}.`;el('results').innerHTML=rows.slice(offset,offset+size).map(f=>`<article><h2>${esc(f.section)} ${esc(f.title)} · ${esc(f.id)}</h2><small>${esc(f.confidence)} · source object ${esc(f.source_id)}</small><div class="formula">${f.rendered||esc(f.expression)}</div><ul>${f.hits.map(h=>`<li><b>${esc(h.rule)}</b> [${esc(h.confidence)}]: ${esc(h.reason)} <code>${esc(h.token)}</code></li>`).join('')}</ul><details><summary>Context and original MathML</summary><p>${esc(f.context)}</p><pre>${esc(f.source_xml)}</pre><p>${esc(f.source)}</p></details><a href="${esc(f.url)}" target="_blank">Open textbook context</a></article>`).join('');}
['level','rule','query'].forEach(id=>el(id).addEventListener('input',()=>{offset=0;draw()}));el('prev').onclick=()=>{offset=Math.max(0,offset-size);draw()};el('next').onclick=()=>{offset+=size;draw()};draw();</script>'''.replace('PAYLOAD',payload)
    (OUT/'review.html').write_text(page,encoding='utf-8')
    (OUT/'README.md').write_text('# Operator typography audit\n\nRead-only structural triage of all maintained textbook modules. No textbook source was changed.\n\n'+json.dumps(summary,indent=2)+'\n\nOpen review.html for filterable, paginated current-renderer previews. audit.json contains every finding and exact source hashes. symbol-inventory.json inventories all detected symbols and token types, including those not flagged.\n\nStart with high confidence, especially symbol-in-nonoperator-token, number-in-operator, and split-decimal. Review grouped binary operators next. Low-priority manual spacing is often intentional. All labels denote heuristic confidence, not approval to change. Repeated expressions remain separate because their source contexts differ.\n\nLimitations: no semantic proof, no exhaustive visual detection, and uncommon non-Unicode/custom operators can require manual review. Greek identifiers are not treated as operators. Source annotations are excluded from expression previews and token rules. Browser previews use the current renderer without the textbook page CSS; use the context link for final page layout.\n',encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False))

if __name__=='__main__': main()
