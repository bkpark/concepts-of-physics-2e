from pathlib import Path
from lxml import html
import json
ROOT=Path(__file__).resolve().parents[2];dist=ROOT/'prototype/dist/course-full';qa=ROOT/'reports/1.1/front-matter-print';qa.mkdir(parents=True,exist_ok=True)
book=html.fromstring((dist/'book.html').read_text(encoding='utf-8'))
titles={a.find('header/p').text_content():a.find('header/h1').text_content() for a in book.xpath('//main/article')}
chapters=[]
for i,w in enumerate('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen'.split()):
    report=json.loads((ROOT/f'reports/1.1/chapter-{i}-print/layout.json').read_text())
    doc=html.fromstring((dist/f'chapter-{w}-print.html').read_text(encoding='utf-8'))
    units=doc.xpath('//*[@class="unit-heading"]')
    chapter=dict(number=i,title=doc.xpath('//h1')[0].text_content(),page=report.get('startPage',1),unit=' — '.join(units[0].itertext()) if units else None,sections=[])
    for section in report['sections']:
        label=section['label'];title=titles.get(label,label)
        chapter['sections'].append(dict(label=label if label in titles else '',title=title,page=section['page']))
    chapters.append(chapter)
back=[]
for label,name in [('A','appendix-a'),('B','appendix-b'),('C','appendix-c'),('D','appendix-d'),('','index'),('','book-licensing')]:
    report=json.loads((ROOT/f'reports/1.1/{name}-print/layout.json').read_text())
    title=titles[label] if label else ('Index' if name=='index' else 'Licensing and Attribution')
    back.append(dict(label=label,title=title,page=report['startPage']))
preface=book.xpath('//article[@id="m67030"]')[0]
result=dict(chapters=chapters,back=back,preface=html.tostring(preface,encoding='unicode'))
(qa/'source.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print('Chapters',len(chapters),'sections',sum(len(c['sections']) for c in chapters),'back entries',len(back))
