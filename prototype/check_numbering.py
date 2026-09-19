from pathlib import Path
import json
P=Path(__file__).resolve().parent
fixtures=json.loads((P/'numbering-fixtures.json').read_text(encoding='utf-8'));result={}
for profile in ('cnx','course'):
    objects=json.loads((P/'dist'/(profile+'-full')/'object-labels.json').read_text(encoding='utf-8'))
    for f in fixtures[profile]:assert objects[f['id']]['label']==f['label'],(profile,f,objects[f['id']])
    result[profile]={'observed_labels_checked':len(fixtures[profile]),'passed':True}
(P/'qa/numbering-checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(result))
