from pathlib import Path
import json,hashlib
from lxml import html
ROOT=Path(__file__).resolve().parents[2];qa=ROOT/'reports/1.1/full-book';qa.mkdir(parents=True,exist_ok=True)
parts=[dict(key='cover',pdf='output/pdf/v1.1-cover-and-title-page.pdf',select=[0],pages=1),dict(key='cover-verso',pages=1),dict(key='title',pdf='output/pdf/v1.1-cover-and-title-page.pdf',select=[1],pages=1),dict(key='copyright',pdf='output/pdf/v1.1-copyright-page.pdf',html='copyright-page-print.html',pages=1),dict(key='front',pdf='output/pdf/v1.1-toc-and-preface.pdf',html='toc-preface-print.html',pages=8)]
for i,w in enumerate('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen'.split()):
 r=json.loads((ROOT/f'reports/1.1/chapter-{i}-print/layout.json').read_text(encoding='utf-8'))
 parts.append(dict(key=f'chapter-{i}',pdf=f'output/pdf/v1.1-chapter-{i}.pdf' if i else 'output/pdf/v1.1-chapter-0-revised.pdf',html=f'chapter-{w}-print.html',pages=r['pages'],startPage=r.get('startPage',1)))
for letter in 'abcd':
 r=json.loads((ROOT/f'reports/1.1/appendix-{letter}-print/layout.json').read_text(encoding='utf-8'))
 parts.append(dict(key=f'appendix-{letter}',pdf=f'output/pdf/v1.1-appendix-{letter}.pdf',html=f'appendix-{letter}-print.html',pages=r['pages'],startPage=r['startPage']))
parts += [dict(key='index',pdf='reports/1.1/index-print/index-assembled.pdf',html='index-assembled-print.html',pages=8,startPage=633),dict(key='licensing',pdf='output/pdf/v1.1-licensing-attribution.pdf',html='licensing-attribution-print.html',pages=2,startPage=641)]
offset=0
for p in parts:
 p['offset']=offset;offset+=p['pages']
 if 'pdf' in p:p['sha256']=hashlib.sha256((ROOT/p['pdf']).read_bytes()).hexdigest()
 if 'startPage' in p:assert p['offset']==12+p['startPage']-1
book=html.fromstring((ROOT/'prototype/dist/course-full/book.html').read_text(encoding='utf-8'))
labels={a.find('header/p').text_content():a.get('id') for a in book.xpath('//main/article')}
modules={'m67030':dict(page=10,y=750)}
for i in range(15):
 r=json.loads((ROOT/f'reports/1.1/chapter-{i}-print/layout.json').read_text(encoding='utf-8'))
 for sec in r['sections']:
  if sec['label'] in labels:modules[labels[sec['label']]]=dict(page=12+sec['page']-1,y=750)
for letter in 'ABCD':
 r=json.loads((ROOT/f'reports/1.1/appendix-{letter.lower()}-print/layout.json').read_text(encoding='utf-8'))
 modules[labels[letter]]=dict(page=12+r['startPage']-1,y=750)
sections=json.loads((ROOT/'metadata/sections.proposed.json').read_text(encoding='utf-8'))['sections']
slugs={s['slug']:s['id'].split(':')[-1] for s in sections}
result=dict(parts=parts,pages=offset,bodyOffset=12,modules=modules,slugs=slugs)
(qa/'components.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print('Prepared',len(parts),'components;',offset,'pages')
