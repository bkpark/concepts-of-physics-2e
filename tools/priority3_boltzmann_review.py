"""Context-scoped Boltzmann notation audit and preview proposals."""
import re,json,hashlib
from pathlib import Path
import xml.etree.ElementTree as E
M='{http://www.w3.org/1998/Math/MathML}'
C='{http://cnx.rice.edu/cnxml}'
KB='<m:msub><m:mi>k</m:mi><m:mi mathvariant="normal">B</m:mi></m:msub>'

def append_boltzmann_review(items,add,edit,block,raw,ROOT):
 i=add('P3-10','Boltzmann constant notation: k_B','Use k_B consistently for Boltzmann’s constant, preserving numerical values and all other meanings of k. Includes definitions, worked equations, summaries, glossary, and appendix tables.',[],'Coordinated notation preview; maintainer requested book-wide reconciliation')
 i['status']='requested-notation-preview'
 audit=[];total=0
 for path in sorted((ROOT/'maintained/modules').glob('*/index.cnxml')):
  mid=path.parent.name;r=E.parse(path).getroot();parents={c:e for e in r.iter() for c in e};targets={}
  for math in r.iter(M+'math'):
   tokens=[(e.text or '').strip() for e in math.iter() if e.tag in [M+'mi',M+'ci',M+'mtext',M+'mn']]
   if not any('k' in t for t in tokens):continue
   n=math
   while n in parents and not n.get('id'):n=parents[n]
   row=math
   while row in parents and row.tag!=C+'row':row=parents[row]
   is_boltzmann=mid in ['m67122','m67126','m42238'] and any(t in ['k','NkT','kT'] for t in tokens)
   if mid in ['m42709','m78798']:is_boltzmann=row.tag==C+'row' and 'Boltzmann' in ''.join(row.itertext()) and 'Stefan' not in ''.join(row.itertext()) and 'k' in tokens
   audit.append(dict(module=mid,source_id=n.get('id'),tokens=tokens,disposition='Boltzmann: change to k_B' if is_boltzmann else 'Other symbol, unit prefix, or word: unchanged'))
   if is_boltzmann:targets.setdefault(n.get('id'),[]).append(math);total+=1
  # A summary list can contain an equation with its own ID; replace the list once.
  for target in list(targets):
   if any(other!=target and 'id="'+target+'"' in block(mid,other) for other in targets):
    del targets[target]
  for target,maths in targets.items():
   before=block(mid,target)
   # In reference tables, scope substitution to the Boltzmann row only.
   def fix_math(match):
    text=match[0]
    if not re.search(r'<m:(?:mi|ci|mtext)\b[^>]*>\s*(?:k|NkT|kT)\s*</m:',text):return text
    text=re.sub(r'<m:(mi|ci|mtext)\b[^>]*>\s*(k|NkT|kT)\s*</m:\1>',lambda x: KB if x[2]=='k' else '<m:mrow>'+('<m:mi>N</m:mi>' if x[2]=='NkT' else '')+KB+'<m:mi>T</m:mi></m:mrow>',text)
    def annotation(a):
     t=a[0]
     t=re.sub(r'"?(NkT|kT)"?|\bk\b',lambda z: {'NkT':'N k rSub {B} T','kT':'k rSub {B} T'}.get(z[1], 'k rSub {B}') if z[1] else 'k rSub {B}',t)
     return t
    return re.sub(r'<m:annotation\b[^>]*>.*?</m:annotation>',annotation,text,flags=re.S)
   def fix(s):
    if mid in ['m42709','m78798']:
     return re.sub(r'<row\b[^>]*>.*?</row>',lambda z:re.sub(r'<m:math\b.*?</m:math>',fix_math,z[0],flags=re.S) if 'Boltzmann' in z[0] and 'Stefan' not in z[0] else z[0],s,flags=re.S)
    return re.sub(r'<m:math\b.*?</m:math>',fix_math,s,flags=re.S)
   existing=next((p for group in items for p in group['passages'] if p['module']==mid and p['source_id']==target),None)
   if existing:
    existing['proposed_xml']=fix(existing['proposed_xml']);existing['notation_followup']='P3-10: Boltzmann k_B notation applied after the existing prose correction.'
   else:
    after=fix(before);assert before!=after,(mid,target)
    i['passages'].append(dict(module=mid,source_path=str(path.relative_to(ROOT)).replace('\\','/'),source_id=target,source_sha256=hashlib.sha256(raw(mid).encode()).hexdigest(),before_xml=before,proposed_xml=after,status='requested-notation-preview'))
 out=ROOT/'reports/1.1/boltzmann-notation';out.mkdir(parents=True,exist_ok=True)
 (out/'audit.json').write_text(json.dumps(dict(scope='All maintained CNXML modules: MathML token scan, Boltzmann name search, context classification. Raster artwork not OCR-certified.',module_count=len(list((ROOT/'maintained/modules').glob('*/index.cnxml'))),boltzmann_math_expressions=total,entries=audit),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 i['audit_report']='reports/1.1/boltzmann-notation/audit.json'
 print('Boltzmann audit:',total,'math expressions;',len(i['passages']),'new passage overlays')
