"""Compare current display labels with frozen, text-matched reference observations."""
from pathlib import Path
import json,collections,html
root=Path(__file__).resolve().parents[1]
release=json.loads((root/'metadata/release.json').read_text(encoding='utf-8'));site=root/'output/releases'/release['release_id']/'site'
labels=json.loads((site/'object-labels.json').read_text(encoding='utf-8'))
seed=json.loads((root/'references/course-exercise-numbering-matches.json').read_text(encoding='utf-8'))
sections={x['section_id'].split(':')[1]:x['label'] for x in json.loads((root/'metadata/numbering-course-2026-07-07.proposed.json').read_text(encoding='utf-8'))['section_labels']}
rows=[];groups=collections.Counter()
for x in seed['matches']:
 current=labels[x['id']]['label'];mid=x['id'].split('#')[0];chapter=sections[mid].split('.')[0]
 row={**x,'current_label':current,'chapter':chapter,'matches':current==x['reference_label']};rows.append(row)
 if not row['matches']:groups[chapter]+=1
assert labels['m67123#fs-id3224510']['label']=='11'
assert labels['m67123#fs-id2862863']['label']=='12'
result={'release_id':release['release_id'],'reference_sha256':seed['reference_sha256'],'method':seed['method'],'matched':sum(x['matches'] for x in rows),'compared':len(rows),'differences_by_chapter':dict(groups),'policy':'Known exercise-alignment differences are reported for the deferred exercise revision; no prose/question splits or merges are performed. This does not certify all figure/example/equation labels.','observations':rows}
(root/'reports/release-numbering-current.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in result.items() if k!='observations'}))
