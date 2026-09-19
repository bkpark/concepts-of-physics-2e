"""Create review-only, hash-guarded repair proposals. Never writes source modules."""
from pathlib import Path
import copy, difflib, hashlib, html, json, re, xml.etree.ElementTree as ET
from mathml import math_node

P=Path(__file__).resolve().parent;ROOT=P.parent
OUT=P/'dist/repair-review';OUT.mkdir(parents=True,exist_ok=True)
REVIEW=ROOT/'proposals/fidelity-repairs';REVIEW.mkdir(parents=True,exist_ok=True)
NS='http://www.w3.org/1998/Math/MathML';M='{'+NS+'}'
ET.register_namespace('m',NS)
sha=lambda b:hashlib.sha256(b).hexdigest()
dump=lambda p,d:p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
def parse_fragment(raw):return ET.fromstring('<wrapper xmlns:m="'+NS+'">'+raw+'</wrapper>')[0]
records=[]
def propose(mid,index,case,title,classification,reason,evidence,edit):
    path=ROOT/f'modules/{mid}/index.cnxml';raw=path.read_bytes().decode('utf-8')
    before=list(re.finditer(r'<m:math\b.*?</m:math>',raw,re.S))[index-1].group()
    tree=parse_fragment(before);edit(tree)
    after=ET.tostring(tree,encoding='unicode')
    assert raw.count(before)==1
    records.append({'id':case,'title':title,'status':'proposed-not-applied',
      'classification':classification,'module':mid,'source_path':str(path.relative_to(ROOT)).replace('\\','/'),
      'source_file_sha256':sha(path.read_bytes()),'source_math_ordinal':index,
      'source_object':{'R1':'eip-53','R2':'import-auto-id3143059','R3':'import-auto-id1688908'}[case],
      'before_fragment_sha256':sha(before.encode()),'before':before,'after':after,
      'reason':reason,'evidence':evidence})

def rydberg(e):
    powers=[x for x in e.iter(M+'apply') if len(x)==2 and x[0].tag==M+'power']
    assert len(powers)==2
    for power in powers:ET.SubElement(power,M+'cn').text='2'
propose('m67807',65,'R1','Restore the two missing squares in the Rydberg equation','equation correction',
 'Insert exponent 2 on both n_f and n_i. Preserve the existing coefficient and notation.',
 ['Local m67807 eip-237 already has both squares; eip-854 and eip-59 state the same squared dependence.',
  'Historical PDF page 476, printed 470, equation 13.36 omits both squares; this is a correction to the historical displayed equation.',
  'OpenStax College Physics 2e 30.3 confirms the squared dependence.'],rydberg)

def empty_sup(e):
    found=[]
    for parent in e.iter():
        for child in list(parent):
            if child.tag==M+'msup' and len(child)==1 and not ''.join(child.itertext()).strip():
                found.append(child);parent.remove(child)
    assert len(found)==1
propose('m67807',91,'R2','Remove an empty, malformed superscript','markup-only repair',
 'Remove the trailing msup containing only empty mrows. No visible symbol, coefficient, or exponent changes.',
 ['Historical PDF page 484, printed 478, exercise 46 displays the Bohr-radius formula.',
  'Later local source replaces this invalid msup with an empty mrow.',
  'Pinned upstream m42596 omits the empty branch.'],empty_sup)

def nuclide(e):
    semantics=e.find(M+'semantics');assert semantics is not None
    display=semantics[0]
    # Reuse the original X_N subtree, preserving its lettering style.
    xn=next(x for x in display.iter(M+'msub') if len(x)==2 and ''.join(x[0].itertext()).strip()=='X')
    new=ET.fromstring('<m:mrow xmlns:m="'+NS+'"><m:msubsup><m:mrow/><m:mi>Z</m:mi><m:mi>A</m:mi></m:msubsup></m:mrow>')
    new.append(copy.deepcopy(xn));semantics.remove(display);semantics.insert(0,new)
propose('m42709',345,'R3','Restore the nuclide notation','notation correction',
 'Display A at upper left, Z at lower left, and N at lower right of X. Preserve the original annotation.',
 ['The original StarMath annotation explicitly says lSub Z and lSup A.',
  'Local m76603 import-auto-id3033441 uses Z below A in the same notation.',
  'Historical PDF page 644, printed 638, omits A and places Z above the baseline.',
  'Later local source and pinned upstream glossary reverse A/Z; neither is a safe repair source.',
  'OpenStax College Physics 2e chapter 31 summary agrees with the original annotation.'],nuclide)

mid='m67122';path=ROOT/f'modules/{mid}/index.cnxml';raw=path.read_bytes().decode('utf-8')
before='<link target-id="fs-id1444855"/>';after='<link target-id="fs-id1667893"/>'
assert raw.count(before)==1 and 'id="fs-id1667893"' in raw
records.append({'id':'R4','title':'Retarget the tire-pressure exercise reference','status':'proposed-not-applied',
 'classification':'cross-reference repair','module':mid,'source_path':f'modules/{mid}/index.cnxml',
 'source_file_sha256':sha(path.read_bytes()),'source_object':'import-auto-id2677616',
 'before_fragment_sha256':sha(before.encode()),'before':before,'after':after,
 'reason':'Point to the retained tire-pressure worked example, which explicitly states the same absolute pressure and gauge-pressure comparison. Do not restore the omitted moles example.',
 'evidence':['Historical PDF page 290, printed 284, exercise 10 already prints ??? at this reference.',
 'The retained example is fs-id1667893, historical Example 9.1, PDF page 237 (printed 231).',
 'Pinned upstream m42216 fs-id1444855 is Calculating Number of Moles: Gas in a Bike Tire, absent from the local module.']})

# Make concrete diffs and apply only to generated review copies, with strict guards.
working={};validation=[]
for r in records:
    original=(ROOT/r['source_path']).read_bytes();assert sha(original)==r['source_file_sha256']
    assert sha(r['before'].encode())==r['before_fragment_sha256']
    text=working.get(r['module'],original.decode('utf-8'));assert text.count(r['before'])==1
    changed=text.replace(r['before'],r['after'],1);working[r['module']]=changed
    patch=''.join(difflib.unified_diff(text.splitlines(True),changed.splitlines(True),fromfile='a/'+r['source_path'],tofile='b/'+r['source_path']))
    (REVIEW/(r['id']+'.patch')).write_text(patch,encoding='utf-8',newline='\n')
for mid,text in working.items():
    old=ET.fromstring((ROOT/f'modules/{mid}/index.cnxml').read_bytes());new=ET.fromstring(text)
    assert [e.get('id') for e in old.iter() if e.get('id')]==[e.get('id') for e in new.iter() if e.get('id')]
    assert len(list(old.iter(M+'math')))==len(list(new.iter(M+'math')))
    for e in new.iter(M+'math'):math_node(e)
    if mid=='m67122':
        ids={e.get('id') for e in new.iter()}
        assert all(e.get('target-id') in ids for e in new.iter() if e.tag.endswith('}link') and e.get('target-id') and not e.get('document'))
    dest=OUT/'source'/mid;dest.mkdir(parents=True,exist_ok=True)
    (dest/'index.cnxml').write_text(text,encoding='utf-8',newline='\n')
    validation.append({'module':mid,'all_math_passes_adapter':True,'ids_and_math_count_unchanged':True})
dump(REVIEW/'manifest.json',{'schema_version':1,'policy':'Review proposals only. No historical or maintained source edits have been applied. Apply to a maintained layer only after recording the editorial decision.','repairs':records})
dump(P/'qa/repair-proposals.json',{'dry_run':validation,'source_files_unchanged':all(sha((ROOT/r['source_path']).read_bytes())==r['source_file_sha256'] for r in records)})

def display_math(xml):
    # Native presentation copy: expand mfenced without touching proposed source.
    e=ET.fromstring(math_node(parse_fragment(xml)))
    for parent in list(e.iter()):
        for child in list(parent):
            if child.tag==M+'mfenced':
                children=list(child);op=child.get('open','(');cl=child.get('close',')')
                child.clear();child.tag=M+'mrow'
                if op:ET.SubElement(child,M+'mo').text=op
                child.extend(children)
                if cl:ET.SubElement(child,M+'mo').text=cl
    e.set('display','block');ET.register_namespace('',NS)
    text=ET.tostring(e,encoding='unicode');ET.register_namespace('m',NS);return text
cards=[]
for r in records:
    rendered=display_math(r['after']) if r['id']!='R4' else '<p>…in <a href="../cnx/sections/the-ideal-gas-law/">Example 9.1: Calculating Pressure Changes Due to Temperature Changes: Tire Pressure</a>. Is it?</p>'
    cards.append('<section><h2>'+r['id']+' · '+html.escape(r['title'])+'</h2><p><b>'+r['classification']+'</b> · Proposed, not applied</p><div class="math">'+rendered+'</div><p>'+html.escape(r['reason'])+'</p><ul>'+''.join('<li>'+html.escape(x)+'</li>' for x in r['evidence'])+'</ul></section>')
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Introduction to Physics - four repair proposals</title><style>body{max-width:1000px;margin:40px auto;padding:0 24px;background:#f3f6f5;color:#173b43;font:18px/1.6 Georgia,serif}h1{font-weight:normal}h2{font:600 22px Arial,sans-serif}section{background:white;border:1px solid #cbdada;margin:24px 0;padding:28px}.math{font-size:25px;overflow:auto;padding:20px 0}math{font-family:'Cambria Math',math}li{margin:8px 0}a{color:#165f76}</style></head><body><h1>Introduction to Physics: repair review</h1><p>These are four isolated proposals. Historical source, original PDF, and current textbook preview remain unchanged.</p>'''+''.join(cards)+'</body></html>'
(OUT/'index.html').write_text(page,encoding='utf-8',newline='\n')
print('Prepared four proposals; dry-run XML, IDs, MathML, and local references passed.')
