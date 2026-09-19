"""Isolated native MathML selection experiment; leaves the SVG preview intact."""
from pathlib import Path
import json, html, xml.etree.ElementTree as ET
from mathml import math_node

P=Path(__file__).resolve().parent
OUT=P/'dist/native-test';OUT.mkdir(parents=True,exist_ok=True)
NS='http://www.w3.org/1998/Math/MathML'
ET.register_namespace('',NS)
samples=[('m67034-math-0018','Fraction, Greek delta, and overbar'),
 ('m67034-math-0097','Simultaneous subscript and superscript'),
 ('m67034-math-0107','Square root, powers, and units'),
 ('m67034-math-0012','Aligned rows and a stretching brace'),
 ('m67122-math-0045','Multiline temperature calculation'),
 ('m67530-math-0001','Bold vector symbol'),
 ('m67807-math-0064','Greek pi and a symbolic product'),
 ('m42709-math-0020','Nested fraction inside a square root')]
sources={s['key']:s for s in json.loads((P/'dist/cnx/math-source.json').read_text(encoding='utf-8'))}
adaptations=[]
def native(e,key):
    for child in list(e):native(child,key)
    tag=e.tag.split('}')[-1]
    if tag=='mfenced':
        children=list(e);opening=e.get('open','(');closing=e.get('close',')')
        separators=''.join(e.get('separators',',').split())
        e.clear();e.tag='{'+NS+'}mrow'
        def operator(value):
            x=ET.SubElement(e,'{'+NS+'}mo',{'stretchy':'true'});x.text=value
        if opening:operator(opening)
        for i,c in enumerate(children):
            if i and separators:operator(separators[min(i-1,len(separators)-1)])
            e.append(c)
        if closing:operator(closing)
        adaptations.append({'key':key,'kind':'expand-mfenced'})
    if e.get('mathvariant')=='bold':
        e.set('mathvariant','normal');e.set('style','font-weight:700')
        adaptations.append({'key':key,'kind':'bold-vector-css'})
    if e.text is not None and not e.text.strip():e.text=None
    if e.tail is not None and not e.tail.strip():e.tail=None

records=[];cards=[]
for key,title in samples:
    source=sources[key];tree=ET.fromstring(math_node(ET.fromstring(source['xml'])))
    native(tree,key);tree.set('display','block')
    xml=ET.tostring(tree,encoding='unicode')
    records.append({**source,'title':title,'presentation_mathml':xml})
    cards.append(f'''<section id="{key}"><h2>{html.escape(title)}</h2>
<p class="provenance">{key} · source object {html.escape(source['source_object'])}</p>
<div class="expression">{xml}</div>
<div class="controls"><button data-copy="{key}">Copy whole equation as MathML</button>
<span role="status"></span><label>Paste here to inspect the clipboard:
<textarea aria-label="Paste test for {key}" spellcheck="false"></textarea></label></div></section>''')
css='''body{max-width:960px;margin:40px auto;padding:0 24px;color:#193b44;font:18px/1.5 Georgia,serif;background:#f3f6f5}h1{font-weight:normal}h2{font:600 20px Arial,sans-serif}.intro{max-width:800px}section{margin:24px 0;padding:24px;background:white;border:1px solid #cedcdd;break-inside:avoid}.provenance{font:12px Arial,sans-serif;color:#57696d;overflow-wrap:anywhere}.expression{padding:20px 10px;font-size:25px;overflow:auto}math{font-family:'Cambria Math',math}button{padding:9px 12px;background:#165769;color:white;border:0;border-radius:4px;cursor:pointer}label{display:block;font:14px Arial,sans-serif;margin-top:14px}textarea{display:block;width:100%;box-sizing:border-box;min-height:65px;margin-top:6px}span[role=status]{font:13px Arial,sans-serif;margin-left:12px}mtd{padding:3px 6px}mtable[columnalign=left] mtd{text-align:left}@page{size:Letter;margin:18mm}@media print{body{margin:0;padding:0;background:white;font-size:11pt}.controls{display:none}section{margin:14px 0;padding:16px}.expression{font-size:20pt;overflow:visible}section:nth-of-type(2n+3){break-before:page}.web-only{display:none}h1{font-size:24pt}h2{font-size:14pt}.provenance{font-size:8pt}}'''
script='''document.querySelectorAll('[data-copy]').forEach(button=>button.addEventListener('click',async()=>{const card=button.closest('section');const status=card.querySelector('[role=status]');try{await navigator.clipboard.writeText(card.querySelector('math').outerHTML);status.textContent='MathML copied';}catch(e){status.textContent='Copy failed: '+e.message;}}));'''
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Introduction to Physics - native math selection test</title><style>'''+css+'''</style></head><body><header><h1>Native MathML selection test</h1><p class="intro">Eight expressions from Introduction to Physics. Select symbols directly, or use the copy button for structured MathML. This is an isolated rendering experiment, not a textbook revision.</p><p class="web-only">Copying selected text and copying an editable equation are different operations. The button copies MathML XML; it does not guarantee direct equation paste into every application.</p></header>'''+''.join(cards)+'<script>'+script+'</script></body></html>'
(OUT/'index.html').write_text(page,encoding='utf-8',newline='\n')
(OUT/'samples.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
(OUT/'adaptations.json').write_text(json.dumps(adaptations,indent=2)+'\n',encoding='utf-8',newline='\n')
print(f'Created {len(records)} native MathML samples at {OUT}')
