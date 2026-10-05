"""Audit prose number/unit gaps without reserializing XML or touching MathML."""
from pathlib import Path
import re, json, html, argparse, hashlib, collections, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'reports/1.1/prose-unit-space-audit'
symbols=set('Hz Pa J W V A F H C N K s m g Ω kg eV rad sr mol cd lm lx Bq Gy Sv T L h min rpm cal kcal atm bar Ci rem rad d yr y cm mm km nm pm fm μm µm mL kWh'.split())
for prefix in ['y','z','a','f','p','n','u','μ','µ','m','c','d','k','M','G','T','P','E']:
 for base in ['Hz','Pa','J','W','V','A','F','H','C','N','s','m','g','Ω','eV','L','Bq','Gy','Sv','Ci']:
  symbols.add(prefix+base)
words='ohm ampere amp volt watt joule newton coulomb second minute hour meter metre kilometer kilometre centimeter centimetre millimeter millimetre nanometer nanometre kilogram gram milligram liter litre milliliter millilitre degree kelvin pascal calorie kilocalorie mile yard pound ounce day week year revolution cycle'.split()
symbols.update(words);symbols.update(w+'s' for w in words);symbols.update(['hertz','feet','foot','inches','inch','°C','°F','°R','torr','Torr','hp','ft','lb','lbs','oz','mph'])
symbols.update('u G ly yd mi ml rev mrem kT MT Calories kilojoules kilowatts megawatt megawatts femtometer femtometers milliseconds microseconds nanoseconds tons kilotons megatons gallons barrels percent cents fermi'.split())
symbols.update(['light years','light year','light-years','light-year','metric tons','cubic centimeters','Celsius degrees','Fahrenheit degrees','Tev'])
units='(?:'+'|'.join(re.escape(x) for x in sorted(symbols,key=lambda s:(-len(s),s)))+')'
number=r'(?:[−+\-]?\d[\d,]*(?:\.\d+)?(?:[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+)?|one|two|three|four|five|six|seven|eight|nine|ten|hundred|thousand|million|billion|trillion)'
PAT=re.compile(r'(?<![\w.])(?P<number>'+number+r')(?P<space>[ \t\r\n]+)(?P<unit>'+units+r')(?![\w])')
BLOCKS=set('document content para entry row title caption item section note example equation list table tgroup thead tbody footnote problem solution exercise definition meaning glossary'.split())
def scan(source,mid):
 chars=[];pos=[];anchors=[];kinds=[];stack=[]
 def add(t,start,kind='prose',anchor=''):
  for m in re.finditer(r'&(?:#\d+|#x[0-9a-fA-F]+|\w+);|.',t,re.S):
   decoded=html.unescape(m.group())
   for c in decoded:chars.append(c);pos.append((start+m.start(),start+m.end()) if start is not None else None);anchors.append(anchor);kinds.append(kind)
 for token in re.finditer(r'<[^>]+>|[^<]+',source):
  t=token.group(); anchor=next((x[1] for x in reversed(stack) if x[1]),'')
  if t.startswith('<'):
   match=re.match(r'<(/?)([\w:-]+)',t)
   if not match:continue
   closing,name=match.groups();local=name.split(':')[-1]
   if local in BLOCKS or name=='m:math':add('\0',None)
   if closing:
    if stack:stack.pop()
   elif not t.endswith('/>'):
    ident=re.search(r'\bid="([^"]+)"',t);stack.append((name,ident[1] if ident else ''))
   continue
  if any(x[0].startswith('m:') or x[0].split(':')[-1]=='metadata' for x in stack):continue
  add(t,token.start(),anchor=anchor)
 text=''.join(chars); rows=[]
 for m in PAT.finditer(text):
  spans=[pos[i] for i in range(*m.span('space'))]; spans=sorted(set(spans))
  context=text[max(text.rfind('\0',0,m.start())+1,m.start()-85):min(text.find('\0',m.end()) if '\0' in text[m.end():] else len(text),m.end()+100)]
  status='fix';reason='Recognized number and unit in prose.'
  if m['unit']=='as':status='exclude';reason='Ordinary word “as”, not attoseconds.'
  elif m['unit'] in ['H','F','am','pm','at','da','in','Tev']:
   status='review';reason='Unit abbreviation may instead be a label or ordinary prose; verify context.'
  if any(a[1]!=b[0] for a,b in zip(spans,spans[1:])):status='review';reason='Whitespace spans inline markup; needs structural review.'
  if m['unit']=='A' and text[m.end():].startswith('.M.'):
   status='exclude';reason='A.M. denotes time of day, not amperes.'
  # Include internal spaces of a multiword unit in the same protected phrase.
  for i in range(*m.span('unit')):
   if text[i]==' ':spans.append(pos[i])
  spans=sorted(set(spans))
  rows.append(dict(module=mid,id=anchors[m.start()],match=m.group(),unit=m['unit'],context=context,status=status,reason=reason,spans=spans,cross_markup=pos[m.start()][0]+len(m.group())!=pos[m.end()-1][1]))
 # Quantities whose number and unit straddle an inline MathML boundary.
 for mm in re.finditer(r'<m:math\b.*?</m:math>',source,re.S):
  e=ET.fromstring('<root xmlns:m="http://www.w3.org/1998/Math/MathML">'+mm.group()+'</root>')[0]
  visible=''.join(x.text or '' for x in e.iter() if x.tag.split('}')[-1] in ['mn','mi','mtext','mo'])
  gap=None;unit=None
  if re.fullmatch(r'[−+\d.,×⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺ ]+',visible):
   found=re.match(r'(?P<space>[ \t\r\n]+)(?P<unit>'+units+r')(?!\w)',source[mm.end():])
   if found:gap=(mm.end()+found.start('space'),mm.end()+found.end('space'));unit=found['unit']
  if re.fullmatch(units,visible):
   found=re.search(r'\d(?P<space>[ \t\r\n]+)$',source[:mm.start()])
   if found:gap=found.span('space');unit=visible
  if gap:
   ids=list(re.finditer(r'<(?:para|entry|item|caption)[^>]*\bid="([^"]+)"',source[:mm.start()]))
   anchor=ids[-1][1] if ids else ''
   rows.append(dict(module=mid,id=anchor,match=visible+' | '+unit,unit=unit,context=re.sub('<[^>]+>','',source[max(0,mm.start()-80):mm.end()+100]),status='review' if visible=='g' else 'fix',reason='Mixed prose/math boundary; g denotes acceleration relative to standard gravity.' if visible=='g' else 'Protect the prose space at an inline MathML boundary.',spans=[gap],cross_markup=True))
 return rows
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args();allrows=[];changed=[]
 ledger=ROOT/'maintained/editorial-changes.json';ld=json.loads(ledger.read_text(encoding='utf-8'))
 for p in sorted((ROOT/'maintained/modules').glob('*/index.cnxml')):
  before=p.read_text(encoding='utf-8');rows=scan(before,p.parent.name);allrows+=rows
  if not args.apply:continue
  edits=sorted(set(tuple(span) for r in rows if r['status']=='fix' for span in r['spans']))
  after=before
  for start,end in sorted(edits,reverse=True):after=after[:start]+'\u00a0'+after[end:]
  if after==before:continue
  ET.fromstring(after)
  # Only whitespace changes are authorized here.
  assert re.sub(r'\s+',' ',before)==re.sub(r'\s+',' ',after)
  ident='STYLE-PROSE-NUMBER-UNIT-NBSP-'+p.parent.name
  f=ROOT/'proposals/author-corrections'/(ident+'.json');assert not f.exists()
  data=dict(id=ident,status='applied-maintainer-approved',target_release='cp2e-ver1.1',module=p.parent.name,source_path=p.relative_to(ROOT).as_posix(),source_sha256=hashlib.sha256(before.encode()).hexdigest(),after_sha256=hashlib.sha256(after.encode()).hexdigest(),before=before,after=after,reason='Bookwide author-approved nonbreaking prose number-unit spacing; MathML and ambiguous candidates preserved.')
  f.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');p.write_text(after,encoding='utf-8',newline='\n');ld['changes'].append(f.relative_to(ROOT).as_posix());changed.append(dict(module=p.parent.name,gaps=len(edits)))
 OUT.mkdir(exist_ok=True,parents=True)
 (OUT/('applied-inventory.json' if args.apply else 'expanded-inventory.json')).write_text(json.dumps(allrows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 if args.apply:
  ledger.write_text(json.dumps(ld,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');(OUT/'changes.json').write_text(json.dumps(changed,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(dict(counts=dict(collections.Counter(r['status'] for r in allrows)),modules=len(set(r['module'] for r in allrows)),cross_markup=sum(r['cross_markup'] for r in allrows),changed=changed if args.apply else [])))
if __name__=='__main__':main()
