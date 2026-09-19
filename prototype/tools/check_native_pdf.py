"""Character-level PDF evidence, not a substitute for PDF viewer clipboard tests."""
from pathlib import Path
from collections import Counter
import json, hashlib, unicodedata, xml.etree.ElementTree as ET
import pdfplumber
P=Path(__file__).resolve().parents[1]
pdf_path=P/'output/native-math-selection-test.pdf'
samples=json.loads((P/'dist/native-test/samples.json').read_text(encoding='utf-8'))
norm=lambda s:unicodedata.normalize('NFKC',s)
pages=[];math_chars=[]
with pdfplumber.open(pdf_path) as pdf:
    for i,page in enumerate(pdf.pages,1):
        chars=[c for c in page.chars if 'CambriaMath' in c['fontname']]
        math_chars.extend(chars)
        pages.append({'page':i,'math_character_count':len(chars),'text':page.extract_text(),
                      'fonts':sorted(set(c['fontname'] for c in page.chars))})
expected=Counter()
for sample in samples:
    tree=ET.fromstring(sample['presentation_mathml'])
    for e in tree.iter():
        if e.tag.split('}')[-1] in ('mi','mn','mo','mtext'):
            expected.update(c for c in norm(e.text or '') if not c.isspace() and c!='\u2062')
actual=Counter(c for glyph in math_chars for c in norm(glyph['text']) if not c.isspace())
missing=expected-actual
result={'pdf_sha256':hashlib.sha256(pdf_path.read_bytes()).hexdigest(),'pages':pages,
        'math_characters':len(math_chars),'missing_token_characters_after_nfkc':dict(missing),
        'text_characters_have_bounding_boxes':all(c['x1']>c['x0'] and c['bottom']>c['top'] for c in math_chars),
        'limitations':['PDF clipboard interactions in Acrobat/Edge not tested',
                      'PDF extraction produces styled Unicode mathematical letters',
                      'Whole-equation plain text loses two-dimensional structure',
                      'NFKC here is diagnostic only; PDF characters are not rewritten']}
(P/'qa/native-pdf.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in result.items() if k!='pages'},ensure_ascii=True))
assert not missing,missing
