"""Read an IMAS JSON export as data; never execute question code or publish answers."""
from pathlib import Path
import collections, hashlib, json, sys

ROOT = Path(__file__).resolve().parents[1]
source = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / 'reference-inputs/phys-10-full-export-2026-09-27.imas'
raw = source.read_bytes()
data = json.loads(raw)
paths = {}

def walk(nodes, parents=()):
    for node in nodes.values():
        if isinstance(node, dict):
            walk(node.get('items', {}), parents + (node.get('name', ''),))
        else:
            paths[str(node)] = list(parents)

def question_ids(node):
    if isinstance(node, dict):
        for child in node.values():
            yield from question_ids(child)
    elif isinstance(node, list):
        for child in node:
            yield from question_ids(child)
    elif isinstance(node, int):
        yield str(node)
    # Pool selector strings such as '3|0' are not question IDs.

walk(data['course']['itemorder'])
assessments = []
usage = collections.defaultdict(list)
groups = collections.defaultdict(lambda: {'assessments': 0, 'question_sets': set()})
for ident, item in data['items'].items():
    if item['type'] != 'Assessment':
        continue
    d = item['data']; name = d['name']; path = paths.get(ident, [])
    if any('ARCHIVED' in p for p in path): group = 'archived'
    elif any('Not Used' in p for p in path): group = 'unused-final'
    elif name.startswith('Lecture'): group = 'lecture'
    elif name.startswith('Question Set') and name.endswith('Assessment'): group = 'weekly-spot-check'
    elif name.startswith('Question Set'): group = 'weekly-homework'
    elif name.startswith('Multiple-Choice'): group = 'timed-multiple-choice'
    elif name.startswith('Essay'): group = 'timed-essay'
    else: group = 'other'
    instances = list(question_ids(d['itemorder']))
    sets = sorted({str(data['questions'][q]['questionsetid']) for q in instances}, key=int)
    for q in sets:
        assert q in data['questionset'], q
        usage[q].append(ident)
    assessments.append(dict(export_item_id=ident, title=name, folder=path, role=group,
                            candidate_instances=len(instances), question_set_ids=sets))
    groups[group]['assessments'] += 1
    groups[group]['question_sets'].update(sets)

questions = []
for ident, q in data['questionset'].items():
    questions.append(dict(export_question_set_id=ident, source_uniqueid=str(q['uniqueid']),
        description=q['description'], qtype=q['qtype'], author=q['author'],
        license_code=q.get('license'), ancestor_authors=q.get('ancestorauthors'),
        other_attribution=q.get('otherattribution'), has_image_flag=q.get('hasimg'),
        assessment_ids=usage[ident],
        payload_sha256=hashlib.sha256(json.dumps(q, sort_keys=True, ensure_ascii=False).encode()).hexdigest()))
result = dict(source_file=source.name, source_sha256=hashlib.sha256(raw).hexdigest(),
    scope='Metadata inventory only. No question execution, rendered-variant validation, or source license-code interpretation.',
    counts=dict(assessments=len(assessments), question_instances=len(data['questions']),
                question_definitions=len(questions)),
    groups={g:dict(assessments=v['assessments'], distinct_definitions=len(v['question_sets'])) for g,v in groups.items()},
    question_types=dict(collections.Counter(q['qtype'] for q in questions)),
    assessments=assessments, questions=questions)
out = ROOT / 'reports/1.1/mom-exercise-planning'
out.mkdir(parents=True, exist_ok=True)
(out/'inventory.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result['counts']))
print(json.dumps(result['groups']))
