"""Approved chapter-one organization; retain every existing exercise verbatim."""
from pathlib import Path
import json,re,hashlib,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[1]
orders={
 'm52316':['fs-id1548043','fs-id1364975','fs-id1773292','fs-id1247502'],
 'm71407':['fs-id4081795','fs-id3539434','fs-id1798382','fs-id4059976','fs-id4033346'],
 'm67033':['fs-id4016173','fs-id3526394','fs-id3514238','fs-id1765962','fs-id1780345'],
 'm67038':['fs-id1875651','fs-id1638420','fs-id2183300','fs-id2062475'],
 'm67035':['eip-805','fs-id1348631','eip-479'],
}
ledger_path=ROOT/'maintained/editorial-changes.json';ledger=json.loads(ledger_path.read_text(encoding='utf-8'))
labels=json.loads((ROOT/'metadata/numbering-course-2026-07-07.proposed.json').read_text(encoding='utf-8'))['section_labels']
for x in labels:
 if not x['label'].startswith('1.'):continue
 mid=x['section_id'].split(':')[1];p=ROOT/f'maintained/modules/{mid}/index.cnxml';before=p.read_text(encoding='utf-8');after=before
 def edit(m):
  block=m[0]
  if not re.search(r'<title>(Conceptual Questions|Problems &amp; Exercises)</title>',block):return block
  if mid=='m67034' and 'id="eip-238"' in block:
   block=block.replace('<section id="eip-238"','<section class="conceptual-questions" id="eip-238"',1)
  block=block.replace('<title>Conceptual Questions</title>','<title>Questions and Exercises</title>').replace('<title>Problems &amp; Exercises</title>','<title>Questions and Exercises</title>')
  if mid in orders and 'class="conceptual-questions"' in block:
   hits=list(re.finditer(r'<exercise\b[^>]*id="([^"]+)"[^>]*>.*?</exercise>',block,re.S));parts={h[1]:h[0] for h in hits};assert set(parts)==set(orders[mid])
   block=block[:hits[0].start()]+'\n'.join(parts[i] for i in orders[mid])+block[hits[-1].end():]
  return block
 # Exercise groups are leaf sections; restricting to sections with no nested section avoids body edits.
 after=re.sub(r'<section\b[^>]*>(?:(?!<section\b).)*?</section>',edit,after,flags=re.S)
 if after==before:continue
 path=f'proposals/author-corrections/EX-C1-ORDER-{mid}.json';assert path not in ledger['changes']
 a=E.fromstring(before);b=E.fromstring(after);C='{http://cnx.rice.edu/cnxml}'
 def questions(r):return {e.get('id'):E.tostring(e,encoding='unicode').rstrip() for e in r.iter(C+'exercise')}
 # Compare element content independently of indentation tails.
 def stable(r):
  out={}
  for e in r.iter(C+'exercise'):e.tail=None;out[e.get('id')]=E.tostring(e,encoding='unicode')
  return out
 assert stable(a)==stable(b)
 record=dict(id='EX-C1-ORDER-'+mid,status='applied-maintainer-approved',target_release='cp2e-ver1.1',module=mid,source_path=p.relative_to(ROOT).as_posix(),source_sha256=hashlib.sha256(before.encode()).hexdigest(),after_sha256=hashlib.sha256(after.encode()).hexdigest(),before=before,after=after,reason='Chapter-end organization and topic/progression ordering only. All exercise wording and IDs unchanged; unclassified constant-acceleration question section now tagged for collection.')
 (ROOT/path).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');p.write_text(after,encoding='utf-8',newline='\n');ledger['changes'].append(path)
ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Chapter 1 source groups organized; all exercise content preserved.')
