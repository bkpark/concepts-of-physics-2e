"""One-time approved ordering pass before the 1.1 exercise-number freeze."""
from pathlib import Path
import hashlib,json,re,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[1]
orders={
 'm52310':['ex-physics-in-other-fields','fs-id2592493','fs-id2966113','fs-id3137988','fs-id2633201','fs-id2629517','fs-id2790873','fs-id1573492','fs-id2757381','fs-id1590524'],
 'm67032':['eip-960','ex-recognizing-units','fs-id3143663','eip-424','ex-why-conversion-works','ex-posted-speed-conversion','ex-plate-motion-over-time'],
}
ledger_path=ROOT/'maintained/editorial-changes.json';ledger=json.loads(ledger_path.read_text(encoding='utf-8'))
mapping=[];old_offset=0;new_offset=0
for mid,order in orders.items():
 record_path=f'proposals/author-corrections/EX-C0-ORDER-{mid}.json'
 assert record_path not in ledger['changes'],'Already applied'
 p=ROOT/f'maintained/modules/{mid}/index.cnxml';before=p.read_text(encoding='utf-8')
 section=re.search(r'<section\b[^>]*class="conceptual-questions"[^>]*>.*?</section>',before,re.S);assert section
 matches=list(re.finditer(r'<exercise\b[^>]*id="([^"]+)"[^>]*>.*?</exercise>',section[0],re.S))
 fragments={m[1]:m[0] for m in matches};assert set(fragments)==set(order)
 old_order=[m[1] for m in matches]
 block=section[0][:matches[0].start()]+'\n'.join(fragments[i] for i in order)+section[0][matches[-1].end():]
 after=before[:section.start()]+block+before[section.end():];E.fromstring(after)
 for i,ident in enumerate(order):mapping.append(dict(module=mid,id=ident,old_number=old_offset+old_order.index(ident)+1,new_number=new_offset+i+1))
 old_offset+=len(order);new_offset+=len(order)
 record=dict(id=f'EX-C0-ORDER-{mid}',status='applied-maintainer-approved',target_release='cp2e-ver1.1',module=mid,source_path=p.relative_to(ROOT).as_posix(),source_sha256=hashlib.sha256(before.encode()).hexdigest(),after_sha256=hashlib.sha256(after.encode()).hexdigest(),before=before,after=after,old_order=old_order,new_order=order,reason='Pre-1.1 ordering: section topics, definitions before comparisons, explanation before applications. Only order changes; question XML and IDs unchanged.')
 (ROOT/record_path).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');p.write_text(after,encoding='utf-8',newline='\n');ledger['changes'].append(record_path)
ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=ROOT/'reports/1.1/chapter0-structure/exercise-order.json';out.write_text(json.dumps(mapping,indent=2)+'\n',encoding='utf-8')
print('Reordered 17 exercises; all question text and stable IDs preserved.')
