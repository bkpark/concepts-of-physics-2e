"""Audit embedded-figure prose and adjacent paragraphs against chapter print HTML."""
from pathlib import Path
from lxml import html
import re, json, copy
ROOT=Path(__file__).resolve().parents[2]
DIST=ROOT/'prototype/dist/course-full'
norm=lambda s: re.sub(r"\s+", "", s)
book=html.fromstring((DIST/'book.html').read_text(encoding='utf-8'))
rows=[]
for renderer in sorted((ROOT/'prototype/tools').glob('render-chapter-*.cjs')):
    if 'trial' in renderer.name: continue
    code=renderer.read_text(encoding='utf-8')
    word=renderer.stem.removeprefix('render-chapter-')
    printed=html.fromstring((DIST/f'chapter-{word}-print.html').read_text(encoding='utf-8'))
    for e in printed.xpath('//*[contains(concat(" ",@class," ")," running ") or contains(concat(" ",@class," ")," folio ") or contains(concat(" ",@class," ")," continuation ")]'): e.drop_tree()
    # Reassemble split blocks by audit key, ignoring interleaved floats and headers.
    groups={}
    for e in printed.xpath('//*[@data-audit-key]'):
        groups.setdefault(e.get('data-audit-key'),[]).append(e.text_content())
    printed_text=norm(printed.text_content())+'\n'+'\n'.join(norm(''.join(parts)) for parts in groups.values())
    ids=set(re.findall(r"[\"'](m\d+)[\"']",code))
    articles=[a for a in book.xpath('//main/article') if a.get('id') in ids]
    slug=re.search(r"origin\+'/exercises/([^/]+)/index.html'",code).group(1)
    review=html.fromstring((DIST/'exercises'/slug/'index.html').read_text(encoding='utf-8'))
    rows_ch=[];neighbors={}
    for origin,tree in [('body',a) for a in articles]+[('review',review)]:
        for para in tree.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," para ")][.//figure]'):
            if origin=='body' and any(set((a.get('class') or '').split()) & {'exercise-set','glossary','section-summary'} for a in para.iterancestors()):continue
            prose=copy.deepcopy(para)
            for f in prose.xpath('.//figure'): f.drop_tree()
            chunks=[t.strip() for t in prose.itertext() if t.strip()]
            missing=[t for t in chunks if norm(t) not in printed_text]
            rows_ch.append(dict(id=para.get('id'),origin=origin,figures=[''.join(f.xpath('.//figcaption/b/text()')) for f in para.xpath('.//figure')],prose=prose.text_content().strip(),missing=missing))
            for axis in ['preceding','following']:
                candidates=para.xpath(f'{axis}::*[self::p or contains(concat(" ",normalize-space(@class)," ")," para ")][not(ancestor::figure) and not(.//figure)]')
                if not candidates:continue
                n=candidates[-1] if axis=='preceding' else candidates[0]
                if n not in tree.iterdescendants():continue
                key=n.get('id') or str(n.sourceline)
                chunks=[t.strip() for t in n.xpath('.//text()[not(ancestor::math)]') if len(norm(t))>=16]
                neighbors[key]=dict(chunks=chunks,missing=[t for t in chunks if norm(t) not in printed_text])
    rows.append(dict(chapter=word,embeddedParagraphs=rows_ch,adjacentParagraphs=neighbors))
report=dict(chapters=len(rows),embeddedParagraphs=sum(len(c['embeddedParagraphs']) for c in rows),proseBearingParagraphs=sum(bool(p['prose']) for c in rows for p in c['embeddedParagraphs']),adjacentParagraphs=sum(len(c['adjacentParagraphs']) for c in rows),missingEmbedded=[p for c in rows for p in c['embeddedParagraphs'] if p['missing']],missingAdjacent=[dict(chapter=c['chapter'],id=k,**p) for c in rows for k,p in c['adjacentParagraphs'].items() if p['missing']],details=rows)
(ROOT/'reports/1.1/embedded-figure-prose-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='details'},ensure_ascii=True,indent=2))
assert not report['missingEmbedded'] and not report['missingAdjacent']
