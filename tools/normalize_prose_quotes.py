"""Approved prose-only quotation typography; preserve XML syntax and all MathML."""
from pathlib import Path
import re,json,hashlib,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[1]
# Reviewed quoted terms/fragments whose final punctuation belongs to the surrounding sentence.
endings=['drinking','On the Electrodynamics of Moving Bodies','highly relativistic','oscillations','natural philosophy','remains','negative','touch','Ohm’s Law: Resistance and Simple Circuits','ventricular fibrillation','short','going into the page','conceptual physics','descriptive physics','introduction to physics','physical optics','ray optics','weights and measures','center seeking','ideally banked curve','perfectly inelastic','phases','root-mean-square','rms','microwave','below red','above violet','banks','ultraviolet catastrophe','wave-particle duality','proportional to','microgravity','losing weight','to the right','probability wave','father of nuclear physics','allowed','point masses','to stretch','apparent weight','action-reaction','reaction force','ballistocardiograph','change in KE','quantity of motion','sweet spots','boat','fat tank','lava lamp','Binding Energy','antimatter drive']
ledger_path=ROOT/'maintained/editorial-changes.json';ledger=json.loads(ledger_path.read_text(encoding='utf-8'));summary=[]
for p in (ROOT/'maintained/modules').glob('*/index.cnxml'):
 before=p.read_text(encoding='utf-8');stack=[];opening=True;parts=[];n=0
 for token in re.split(r'(<!--.*?-->|<[^>]+>)',before,flags=re.S):
  if token.startswith('<'):
   parts.append(token)
   if token.startswith(('<!--','<?','<!')):continue
   name=re.match(r'</?([^\s/>]+)',token)[1]
   if token.startswith('</'):
    assert stack and stack[-1]==name,(p,name,stack[-3:]);stack.pop()
   elif not token.endswith('/>'):stack.append(name)
   continue
  if any(x.startswith('m:') or x=='metadata' or x.startswith('md:') for x in stack):parts.append(token);continue
  new=token.replace('”Weightlessness”','“Weightlessness”').replace("primes (')",'primes (′)')
  new=new.replace("'",'’')
  out=[]
  for c in new:
   if c=='"':out.append('“' if opening else '”');opening=not opening
   else:out.append(c)
  new=''.join(out)
  for ending in endings:
   for punct in [',','.']:new=new.replace(ending+punct+'”',ending+'”'+punct)
  # This comma joins the surrounding sentence; it is not part of the quoted statement.
  new=new.replace('God does not play dice,”','God does not play dice”,')
  new=new.replace('‘thrown’','“thrown”')
  if new!=token:n+=1
  parts.append(new)
 assert opening,(p,'Unpaired straight quote')
 after=''.join(parts)
 if before==after:continue
 a=E.fromstring(before);b=E.fromstring(after);M='{http://www.w3.org/1998/Math/MathML}'
 def maths(r):
  out=[]
  for e in r.iter(M+'math'):e.tail=None;out.append(E.tostring(e,encoding='unicode'))
  return out
 assert maths(a)==maths(b),(p,'MathML changed')
 assert [e.attrib for e in a.iter()]==[e.attrib for e in b.iter()],(p,'Attributes changed')
 mid=p.parent.name;id='TYPE-QUOTES-'+mid;f=f'proposals/author-corrections/{id}.json';assert f not in ledger['changes']
 rec=dict(id=id,status='applied-maintainer-approved',target_release='cp2e-ver1.1',module=mid,source_path=p.relative_to(ROOT).as_posix(),source_sha256=hashlib.sha256(before.encode()).hexdigest(),after_sha256=hashlib.sha256(after.encode()).hexdigest(),before=before,after=after,reason='Approved curly prose quotes/apostrophes and logical punctuation; reversed Weightlessness quote and explanatory prime repaired. MathML, attributes and historical source unchanged.')
 (ROOT/f).write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');p.write_text(after,encoding='utf-8',newline='\n');ledger['changes'].append(f);summary.append(dict(module=mid,changed_text_spans=n))
ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'reports/1.1/quotation-audit/applied.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8');print('Changed modules:',len(summary))
