from pathlib import Path
import json,re,pdfplumber
from lxml import html
words='zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen'.split()
results=[]
for i,w in enumerate(words):
 r=json.loads(Path(f'reports/1.1/chapter-{i}-print/layout.json').read_text())
 for k in ['mathPreserved','punctuationGroupsPreserved','protectedWordsPreserved']:
  if k in r:assert r[k],(i,k)
 start=r.get('startPage',1)
 code=Path(f'prototype/tools/render-chapter-{w}.cjs').read_text(encoding='utf-8')
 slug=re.search(r"origin\+'/exercises/([^/]+)/index.html'",code).group(1)
 source=html.fromstring(Path('prototype/dist/course-full/exercises/'+slug+'/index.html').read_text(encoding='utf-8')).text_content()
 expected=sorted(set(map(int,re.findall(r'Exercise (\d+)',source))))
 errors=[];seq=[]
 pdfname=re.search(r"page.pdf\(\{path:path.join\(out,'([^']+)'",code).group(1)
 with pdfplumber.open('output/pdf/'+pdfname) as d:
  assert len(d.pages)==r['pages']
  for n,p in enumerate(d.pages):
   assert (p.width,p.height)==(612,792)
   lo,hi=(72,565.2) if (start+n)%2 else (46.8,540)
   errors.extend((start+n,x['text']) for x in p.extract_words() if x['x0']<lo-1 or x['x1']>hi+1 or x['bottom']>776)
   for a,b in [(lo,lo+237.6),(lo+255.6,hi)]:seq.extend(map(int,re.findall(r'^Exercise (\d+)\s*$',p.crop((a,40,b,750)).extract_text(),re.M)))
   p.close()
 result=dict(chapter=i,pages=r['pages'],startPage=start,endPage=start+r['pages']-1,marginErrors=errors,exercises=seq,expectedExercises=expected,exerciseSequencePreserved=seq==expected)
 results.append(result)
 print(i,'pages',r['pages'],'margins',len(errors),'exercises',len(seq),seq==expected,flush=True)
Path('reports/1.1/definition-style-pdf-check.json').write_text(json.dumps(results,indent=2)+'\n')
assert not any(r['marginErrors'] or not r['exerciseSequencePreserved'] for r in results)
