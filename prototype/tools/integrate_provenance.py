"""Enrich draft mappings with historical PDF evidence; never auto-approve matches."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
path=ROOT/'metadata/upstream-map.proposed.json'
data=json.loads(path.read_text(encoding='utf-8'))
attribution=json.loads((ROOT/'references/cnx-12.1-module-attributions.json').read_text(encoding='utf-8'))
records={r['module_id']:r for r in attribution['modules']}
upstream=set(json.loads((ROOT/'references/college-physics-2e-identifiers.json').read_text(encoding='utf-8'))['module_ids'])
for row in data['mappings']:
    if len(row['local_sections'])!=1:continue
    mid=row['local_sections'][0].split(':')[1]
    if mid not in records:continue
    record=records[mid]
    row['historical_attribution']={**record,'pdf_sha256':attribution['pdf_sha256']}
    for parent in record['direct_ancestors']:
        if parent['module_id'] in upstream and row['status'] in ('candidate','unresolved'):
            target={'work':'college-physics-2e','module_id':parent['module_id'],'source_path':'modules/'+parent['module_id']+'/index.cnxml'}
            if target not in row['upstream_sections']:row['upstream_sections'].append(target)
            evidence=f"Historical PDF page(s) {record['pdf_pages']} directly attributes legacy {parent['module_id']}/{parent['legacy_version']}; ID also occurs in pinned 2e collection. Later-version correspondence remains a candidate."
            if evidence not in row['evidence']:row['evidence'].append(evidence)
            row['status']='candidate'
data['policy']='Historical attribution is evidence of direct legacy ancestry, not approval to merge. All College Physics 2e counterparts remain review candidates. Empty targets mean unresolved.'
path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print('Mappings with candidates:',sum(bool(r['upstream_sections']) for r in data['mappings']))
print('Historical attribution records:',sum('historical_attribution' in r for r in data['mappings']))
