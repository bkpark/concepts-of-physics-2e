"""Local rendered gallery for the unresolved typography audit."""
from pathlib import Path
import json,re,html,collections,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[1]
dest=ROOT/'reports/1.1/math-italic-audit'
audit=json.loads((dest/'audit.json').read_text(encoding='utf-8'))
groups=collections.defaultdict(list)
for f in audit['review_candidates']:groups[(f['module'],f['math_index'])].append(f)
registry=json.loads((ROOT/'prototype/dist/course-full/identity-registry.json').read_text(encoding='utf-8'))
labels=json.loads((ROOT/'prototype/dist/course-full/object-labels.json').read_text(encoding='utf-8'))
M='{http://www.w3.org/1998/Math/MathML}'
def escape(s):return html.escape(str(s))
def order(k):return tuple(int(n) for n in groups[k][0]['section'].split('.'))+(k[1],)
cards=[];inventory=[]
resolutions=json.loads((dest/'resolutions.json').read_text(encoding='utf-8')) if (dest/'resolutions.json').exists() else {}
for i,key in enumerate(sorted(groups,key=order),1):
    mid,index=key;flags=groups[key];f=flags[0];rid=f'R{i:03}'
    source=(ROOT/f'maintained/modules/{mid}/index.cnxml').read_text(encoding='utf-8')
    matches=list(re.finditer(r'<m:math\b[^>]*>.*?</m:math>',source,re.S));raw=matches[index-1][0]
    el=E.fromstring('<root xmlns:m="'+M[1:-1]+'">'+raw+'</root>')[0]
    # Native MathML Core uses CSS text-align rather than legacy columnalign.
    for table in el.iter(M+'mtable'):
        table_align=table.get('columnalign','center').split()
        for row_number,row in enumerate(table):
            row_align=row.get('columnalign','').split() or table_align
            for j,cell in enumerate(row):
                align=cell.get('columnalign') or row_align[min(j,len(row_align)-1)]
                cell.set('style',(cell.get('style','').rstrip(';')+';text-align:'+align).lstrip(';'))
                if align=='right':cell.set('style',cell.get('style')+';text-align:-webkit-right')
                if row_number and table.get('rowspacing')=='0.5em':
                    cell.set('style',cell.get('style')+';padding-top:0.5em')
    # Chromium native MathML does not support legacy mfenced elements.
    for fence in list(el.iter(M+'mfenced')):
        children=list(fence);opening=fence.get('open','(');closing=fence.get('close',')')
        separators=''.join(fence.get('separators',',').split())
        fence.tag=M+'mrow';fence.attrib.clear();fence[:]=[]
        if opening:E.SubElement(fence,M+'mo').text=opening
        for j,child in enumerate(children):
            if j and separators:E.SubElement(fence,M+'mo').text=separators[min(j-1,len(separators)-1)]
            fence.append(child)
        if closing:E.SubElement(fence,M+'mo').text=closing
    fragments={re.sub(r'\s+','',x['fragment']) for x in flags}
    for p in el.iter():
        for ch in list(p):
            if ch.tag==M+'annotation':p.remove(ch)
        if len(p)==0 and re.sub(r'\s+','',p.text or '') in fragments:p.set('mathbackground','#fff0ad')
    rendered=E.tostring(el,encoding='unicode');rendered=re.sub(r'\bns\d+:|m:','',rendered);rendered=re.sub(r' xmlns(?::\w+)?="[^"]*"','',rendered)
    root=E.fromstring(source);parents={c:p for p in root.iter() for c in p};contextel=list(root.iter(M+'math'))[len(re.findall(r'<m:math\b',source[:matches[index-1].start()]))]
    while contextel is not None and contextel.tag.startswith(M):contextel=parents.get(contextel)
    source_id=contextel.get('id',f['source_id']) if contextel is not None else f['source_id']
    ancestor=contextel;location=None
    while ancestor is not None:
        ob=labels.get(mid+'#'+str(ancestor.get('id')))
        if ob and ob.get('label') is not None and ob['kind'] in {'equation','figure','table','exercise','example'}:location=ob['kind'].title()+' '+str(ob['label']);break
        ancestor=parents.get(ancestor)
    if contextel is not None and contextel.tag.rsplit('}',1)[-1]=='equation':
        par=parents.get(contextel)
        if par is not None and par.tag.rsplit('}',1)[-1] in {'para','item'}:contextel=par
        elif par is not None:
            children=list(par);pos=children.index(contextel);contextel=children[pos-1] if pos else contextel
    context=''
    if contextel is not None:
        xml=E.tostring(contextel,encoding='unicode');xml=re.sub(r'<(?:\w+:)?math\b.*?</(?:\w+:)?math>',' [expression] ',xml,flags=re.S);context=html.unescape(re.sub('<[^>]*>',' ',xml));context=' '.join(context.split());context=context[:650]+('…' if len(context)>650 else '')
    location=location or 'Inline expression'
    chapter=f['section'].split('.')[0]
    url='https://intro-1-1.coaphys.xyz/sections/'+registry[mid]['slug']+'/#'+mid+'--'+source_id.encode().hex()
    reasons=sorted(set(x['reason'] for x in flags))
    note='Check which factor the subscript or exponent belongs to.' if any('Compound' in x for x in reasons) else 'Check whether this is a variable product, a label, or mixed text.'
    if rid in resolutions:note='FIXED — '+resolutions[rid]['decision']
    card=f'''<article class="card" id="{rid}" data-chapter="{chapter}" data-search="{escape(f['section']+' '+context+' '+' '.join(fragments))}"><header><b>{rid}</b><span>Section {escape(f['section'])} · {escape(location)}</span><a href="{escape(url)}" target="_blank">Source context ↗</a></header><h2>{escape(root.find('{http://cnx.rice.edu/cnxml}title').text)}</h2><p class="context">{escape(context)}</p><div class="equation">{rendered}</div><p class="note">{escape(note)} <span>Flagged: {escape(', '.join(sorted(fragments)))}</span></p></article>'''
    cards.append(card);inventory.append(dict(review_id=rid,module=mid,math_index=index,section=f['section'],location=location,fragments=sorted(fragments)))
chapters=sorted({x['section'].split('.')[0] for x in inventory},key=int)
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Math typography review</title><style>
*{box-sizing:border-box}body{margin:0;background:#eef2f4;color:#182d37;font:16px system-ui}main{max-width:1080px;margin:auto;padding:24px}h1{font-size:28px;margin:0 0 10px}nav{position:sticky;top:0;background:#eef2f4;padding:15px 0;display:flex;gap:12px;align-items:center;z-index:2;flex-wrap:wrap}select,input{font:inherit;padding:9px;border:1px solid #9faeb5;border-radius:5px}input{flex:1}.card{background:white;border:1px solid #cbd5da;border-radius:8px;padding:20px;margin:18px 0;break-inside:avoid}header{display:flex;gap:14px;align-items:center;font-size:14px}header b{background:#174f61;color:white;padding:5px 9px;border-radius:4px}header a{margin-left:auto;color:#19617b}h2{font-size:18px;font-weight:600;margin:15px 0}.context{color:#485d65;line-height:1.6;font-size:15px}.equation{overflow-x:auto;text-align:center;padding:24px 8px;font-size:23px;background:#fafbfc;border-radius:5px}math{font-family:'Cambria Math',serif}.note{font-size:14px;margin-bottom:0;color:#475a62}.note span{display:block;margin-top:5px;color:#716020}[hidden]{display:none!important}.intro{line-height:1.55;max-width:850px}.count{min-width:90px}button{font:inherit;padding:8px;cursor:pointer}@media print{nav{display:none}main{padding:0}.card{margin:10px 0}}</style><main><h1>Math typography review</h1><p class="intro">190 expressions containing 226 flagged fragments. Yellow marks identify the suspect fragments; they are candidates, not confirmed errors. The expression is rendered from the current local source. Use the R-number when commenting. Source links lead to the published preview, which may not yet contain pending fixes.</p><nav><label>Chapter <select id="chapter"><option value="">All</option>'''+''.join(f'<option value="{c}">{c}</option>' for c in chapters)+'''</select></label><input id="search" type="search" placeholder="Filter by section, symbol, or surrounding text"><span class="count" id="count"></span><button onclick="window.print()">Print</button></nav><div id="cards">'''+''.join(cards)+'''</div></main><script>const ch=document.querySelector('#chapter'),search=document.querySelector('#search'),cards=[...document.querySelectorAll('.card')];function filter(){let n=0;for(const e of cards){e.hidden=!!((ch.value&&e.dataset.chapter!==ch.value)||(search.value&&!e.dataset.search.toLowerCase().includes(search.value.toLowerCase())));if(!e.hidden)n++}document.querySelector('#count').textContent=n+' shown'}ch.value=new URLSearchParams(location.search).get('chapter')||'';ch.onchange=filter;search.oninput=filter;filter();</script></html>'''
(dest/'gallery.html').write_text(page,encoding='utf-8')
(dest/'gallery-index.json').write_text(json.dumps(inventory,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(f'Rendered {len(cards)} review cards, with chapter and text filters.')
