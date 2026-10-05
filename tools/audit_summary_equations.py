"""Inventory displayed and inline summary relationships against preceding body MathML."""
from pathlib import Path
import sys,json,re,difflib,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'prototype'))
from native_math import native_math
C='{http://cnx.rice.edu/cnxml}';M='{http://www.w3.org/1998/Math/MathML}'
def text(e):
 if e.tag==M+'annotation':return ''
 return ''.join(text(c) for c in e) if len(e) else (e.text or '').strip()
def norm(e):
 try:s=text(E.fromstring(native_math(e)[0]))
 except Exception:s=text(e)
 return re.sub(r'\s+','',s).replace('−','-').replace('⋅','').replace('·','').rstrip('.,;')
labels=json.loads((ROOT/'metadata/numbering-course-2026-07-07.proposed.json').read_text())['section_labels'];rows=[];earlier=[]
for entry in labels:
 mid=entry['section_id'].split(':')[1];r=E.parse(ROOT/f'maintained/modules/{mid}/index.cnxml').getroot();parents={c:p for p in r.iter() for c in p}
 def summary(e):
  while e in parents:
   e=parents[e]
   if 'section-summary' in e.get('class','').split() or (e.tag==C+'section' and (e.findtext(C+'title') or '').lower() in ['section summary','chapter summary']):return True
  return False
 body=[]
 for m in r.iter(M+'math'):
  parent=m
  while parent in parents and not parent.get('id'):parent=parents[parent]
  if not summary(m):body.append(dict(module=mid,id=parent.get('id'),text=norm(m)))
 for m in r.iter(M+'math'):
  if not summary(m):continue
  parent=m
  while parent in parents and parent.tag!=C+'equation' and not parent.get('id'):parent=parents[parent]
  n=norm(m);display=parent.tag==C+'equation'
  if not display and not any(t in n for t in ['=','≈','→','∝','≤','≥']):continue
  matches=[x for x in body if x['text']==n];prior=[x for x in earlier if x['text']==n]
  best=sorted(body,key=lambda x:difflib.SequenceMatcher(None,n,x['text']).ratio(),reverse=True)[:2]
  rows.append(dict(module=mid,section=entry['label'],id=parent.get('id'),display=display,text=n,status='same-section-exact' if matches else 'earlier-section-exact' if prior else 'manual-review',matches=matches or prior,nearest=best if not matches and not prior else []))
 earlier.extend(body)
out=ROOT/'reports/1.1/summary-equation-audit';out.mkdir(exist_ok=True)
(out/'relationships.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Relationships',len(rows),'manual',sum(x['status']=='manual-review' for x in rows))
for x in rows:
 if x['status']=='manual-review':print(json.dumps(x,ensure_ascii=True))
