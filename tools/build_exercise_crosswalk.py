"""Evidence-ranked exercise coverage map. Never executes IMAS code or edits content."""
from pathlib import Path
from collections import Counter, defaultdict
import hashlib, html, json, math, re, shutil, unicodedata
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'reports/1.1/exercise-crosswalk'
OUT.mkdir(parents=True, exist_ok=True)
def load(p): return json.loads(p.read_text(encoding='utf-8'))
raw = (ROOT.parent/'reference-inputs/phys-10-full-export-2026-09-27.imas').read_bytes()
export = json.loads(raw)
inventory = load(ROOT/'reports/1.1/mom-exercise-planning/inventory.json')
assert hashlib.sha256(raw).hexdigest() == inventory['source_sha256']
sections = {s['id']: dict(s) for s in load(ROOT/'maintained/sections.json')['sections']}
labels = {}
for s in load(ROOT/'metadata/numbering-course-2026-07-07.proposed.json')['section_labels']:
    labels[s['label']] = s['section_id']
    sections[s['section_id']]['label'] = s['label']
assessments = {a['export_item_id']:a for a in inventory['assessments']}
qmeta = {q['export_question_set_id']:q for q in inventory['questions']}
active_roles = {'weekly-homework','weekly-spot-check','timed-multiple-choice','timed-essay'}

def norm(s):
    s = html.unescape(s).replace('’', "'")
    return ' '.join(re.findall(r'[a-z0-9]+', unicodedata.normalize('NFKD',s).lower()))

def family_name(s):
    # Group described variants for review, not as proof they are equivalent.
    s = html.unescape(s).replace('’', "'")
    s = re.sub(r'\s*\([^)]*\)', '', s)
    s = re.sub(r'\s*(?:-\s*)?Q\d+\b.*$', '', s)
    s = re.sub(r'^Introduction to Physics\s*-\s*', '', s)
    return s.strip()

week_chapters = {1:[0,1],2:[1],3:[2],4:[3,4],5:[5],6:[6,7],7:[8],8:[9],9:[10,11],10:[12],11:[13],12:[14]}
lecture_chapters = {1:[0],2:[1],3:[1],4:[1,2],5:[2],6:[2],7:[0,1,2],8:[3],9:[3],10:[4],11:[5],12:[5],13:[6],14:[7],15:[3,4,5,6,7],16:[8],17:[8],18:[9],19:[9],20:[10],21:[10],22:[11],23:[10,11],24:[12],25:[12],26:[13],27:[13],28:[14],29:[14],30:[14]}
def chapter_context(a):
    t=a['title']
    m=re.match(r'Question Set (\d+)',t)
    if m:return week_chapters.get(int(m[1]),[])
    m=re.match(r'Lecture (\d+)',t)
    if m:return lecture_chapters.get(int(m[1]),[])
    m=re.search(r'Chapters?\s+(\d+)(?:\s+and\s+(\d+))?',t)
    return [int(v) for v in m.groups() if v] if m else []

C='{http://cnx.rice.edu/cnxml}'; M='{http://www.w3.org/1998/Math/MathML}'
def prose(e):
    if e is None:return ''
    if e.tag in {M+'annotation',M+'annotation-xml'}:return ''
    return (e.text or '')+''.join(prose(c)+(c.tail or '') for c in e)

exercises=[]
for sid,s in sections.items():
    r=ET.parse(ROOT/s['source']).getroot();parents={c:p for p in r.iter() for c in p}
    for e in r.iter(C+'exercise'):
        a=e;kind='unclassified'
        while a is not None:
            t=a.get('type','')+' '+a.get('class','')
            if 'check-understanding' in t:kind='inline-check';break
            if 'conceptual' in t:kind='conceptual';break
            if 'problems' in t:kind='problems';break
            a=parents.get(a)
        ident=e.get('id');url='https://intro-1-1.coaphys.xyz/sections/'+s['slug']+'/index.html#'+sid.split(':')[1]+'--'+ident.encode().hex()
        exercises.append(dict(id=sid+'#'+ident,section_id=sid,kind=kind,url=url,text=' '.join(prose(e.find(C+'problem')).split())))

families={};questions=[]
for ident,q in export['questionset'].items():
    f=family_name(q['description']);fid='mom-family:'+hashlib.sha256(norm(f).encode()).hexdigest()[:16]
    families.setdefault(fid,dict(id=fid,title=f,question_ids=[],sections=set(),roles=set()))
    meta=qmeta[ident]; roles={assessments[a]['role'] for a in meta['assessment_ids']}
    chapters=sorted({c for a in meta['assessment_ids'] if assessments[a]['role'] not in {'archived','unused-final'} for c in chapter_context(assessments[a])})
    text='\n'.join(q.get(k,'') for k in ('control','qcontrol','qtext','solution'))
    evidence=[];direct=set()
    for u in sorted(set(re.findall(r'https?://[^\s<>"\\]+',text))):
        dec=unquote(u);path=urlsplit(dec).path; sid=None;basis=None
        if 'phys.libretexts.org' in dec:
            m=re.match(r'(\d+)\.(\d+):',path.rsplit('/',1)[-1])
            if m:sid=labels.get(str(int(m[1]))+'.'+str(int(m[2])));basis='legacy-section-number-in-hint'
        elif 'intro.coaphys.xyz/sections/' in dec:
            slug=path.split('/sections/')[1].split('/')[0]
            sid=next((k for k,v in sections.items() if v['slug']==slug),None);basis='canonical-slug-in-hint'
        if sid:
            direct.add(sid);evidence.append(dict(section_id=sid,basis=basis,url=u))
    row=dict(id=str(q['uniqueid']),export_question_set_id=ident,family_id=fid,description=q['description'],
        qtype=q['qtype'],roles=sorted(roles),assessment_ids=meta['assessment_ids'],chapter_context=chapters,
        direct_section_ids=sorted(direct),evidence=evidence,section_ids=[],mapping_status='unresolved')
    questions.append(row);families[fid]['question_ids'].append(row['id']);families[fid]['sections'].update(direct);families[fid]['roles'].update(roles)

# Explicit editorial topic-to-section candidates. These do not certify equivalence.
rules=[
 ('force concept|force identification', ['2.2']),('third law|third laws|action/reaction',['2.5']),
 ('first and second law', ['2.3','2.4']),('newton.s first law|inertia description',['2.3']),
 ('newton.s second law',['2.4']),('normal force|apparent weight',['2.6']),('spring force',['2.7']),('friction',['2.8']),
 ('universal gravitation|gravitational acceleration',['2.9']),('centripetal force',['2.10']),
 ('temperature scale|thermometer',['8.2']),('ideal gas',['8.3']),('heat.*transfer method',['8.5']),
 ('heat capacity',['8.6']),('latent heat|phase change',['8.7']),('thermodynamics.*first law',['8.8']),
 ('thermodynamics.*process',['8.9']),('heat pump|refrigerator',['8.12']),
 ('heat engine.*efficiency|thermodynamics.*efficiency',['8.10','8.11']),('heat engine.*example',['8.10']),
 ('thermodynamics.*second law',['8.10']),('entropy',['8.13','8.14']),('heat - definition|heat - description',['8.4'])]
stop=set('the a an of and or in to for from with by is are as on at its it this that which what how why physics introduction description descriptions definitions definition calculation calculations question questions chapter lecture section test bank version updated'.split())
def tokens(s):return {w for w in norm(s).split() if len(w)>2 and w not in stop and not w.isdigit()}
title_tokens={k:tokens(s['title']) for k,s in sections.items() if '.' in s.get('label','') and not s['label'].endswith('.1')}
for q in questions:
    if q['direct_section_ids']:
        q['section_ids']=q['direct_section_ids'];q['mapping_status']='explicit-hint'
    elif families[q['family_id']]['sections']:
        q['section_ids']=sorted(families[q['family_id']]['sections']);q['mapping_status']='family-inherited-candidate'
    else:
        name=q['description'].lower();matches=set()
        for pat,ls in rules:
            if re.search(pat,name):matches.update(labels[l] for l in ls)
        if matches:
            q['section_ids']=sorted(matches);q['mapping_status']='topic-candidate'
        else:
            qt=tokens(q['description']);scores=[]
            for sid,st in title_tokens.items():
                if q['chapter_context'] and int(sections[sid]['label'].split('.')[0]) not in q['chapter_context']:continue
                overlap=len(qt & st); score=overlap/math.sqrt(max(1,len(qt)*len(st)))
                if overlap>=2 and score>=.28:scores.append((score,sid))
            scores.sort(reverse=True)
            if scores:
                q['section_ids']=[sid for score,sid in scores[:3] if score>=scores[0][0]*.8];q['mapping_status']='title-candidate'
            elif q['chapter_context']:q['mapping_status']='chapter-only'
    q['needs_content_review']=True
    # Existing exercises are candidates based on related wording, not verified duplicates.
    rawq=export['questionset'][q['export_question_set_id']]
    qt=tokens(q['description']+' '+re.sub('<[^>]*>',' ',rawq['qtext']))
    ranked=[]
    for e in exercises:
        if e['section_id'] not in q['section_ids'] or e['kind']=='inline-check':continue
        et=tokens(e['text']);common=qt & et
        score=len(common)/math.sqrt(max(1,len(qt)*len(et)))
        if len(common)>=3 and score>=.25:ranked.append((score,e['id']))
    ranked.sort(reverse=True)
    q['existing_exercise_candidates']=[dict(exercise_id=i,score=round(v,3),status='lexical-candidate-not-equivalence') for v,i in ranked[:3]]

for f in families.values():
    f['roles']=sorted(f['roles']);f['explicit_section_ids']=sorted(f.pop('sections'))
section_rows=[]
for sid,s in sections.items():
    if '.' not in s.get('label',''):continue
    qq=[q for q in questions if sid in q['section_ids']]
    ee=[e for e in exercises if e['section_id']==sid]
    section_rows.append(dict(section_id=sid,label=s['label'],title=s['title'],slug=s['slug'],
        existing_exercise_ids=[e['id'] for e in ee if e['kind']!='inline-check'],
        inline_check_ids=[e['id'] for e in ee if e['kind']=='inline-check'],
        explicit_question_ids=[q['id'] for q in qq if q['mapping_status']=='explicit-hint'],
        candidate_question_ids=[q['id'] for q in qq if q['mapping_status']!='explicit-hint'],
        active_family_ids=sorted({q['family_id'] for q in qq if active_roles & set(q['roles'])}),
        lecture_family_ids=sorted({q['family_id'] for q in qq if 'lecture' in q['roles']}),
        coverage_status='mapped-material-needs-review' if qq else 'no-section-match-not-proof-of-gap'))
result=dict(source_sha256=inventory['source_sha256'],scope='Coverage crosswalk, not an approved exercise selection or semantic-equivalence certification.',
    method='Explicit legacy hint targets first; normalized description families second; topic/title candidates third; assessment chapter context otherwise. Never execute question source.',
    mapping_counts=dict(Counter(q['mapping_status'] for q in questions)),families=list(families.values()),
    questions=questions,sections=section_rows,existing_exercises=exercises)
assert len(questions)==1012 and len({q['id'] for q in questions})==1012
assert all(sid in sections for q in questions for sid in q['section_ids'])
(OUT/'crosswalk.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

esc=html.escape
role_order = {r:i for i,r in enumerate(['weekly-homework','timed-multiple-choice','timed-essay','lecture','weekly-spot-check','unused-final','archived'])}
def question_locator(q):
    uses=sorted((assessments[a] for a in q['assessment_ids']), key=lambda a:(role_order.get(a['role'],99),int(a['export_item_id'])))
    if not uses:return '<strong>'+esc(q['description'])+'</strong> — assessment not located'
    a=uses[0]
    location=' → '.join(a['folder']+[a['title']])
    return '<strong>'+esc(q['description'])+'</strong><br><small>Find in: '+esc(location)+'</small>'
question_by_id={q['id']:q for q in questions}
page=['<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Exercise coverage crosswalk</title><style>body{font:17px/1.5 system-ui;max-width:1150px;margin:32px auto;padding:16px;color:#20343c}table{border-collapse:collapse;width:100%}td,th{padding:8px;text-align:left;border-bottom:1px solid #ccd}summary{cursor:pointer;font-weight:600}section{margin:30px 0}a{color:#075e85}code{overflow-wrap:anywhere}.note{background:#eef4f7;padding:16px}li{margin:6px 0}</style><h1>Exercise coverage crosswalk</h1>',
 '<p class="note">Planning only: no textbook or course changes. Explicit hint links identify source sections; family/topic/title matches are candidates. No-match rows are not established gaps. Answer keys and full assessment prompts are not included.</p>',
 '<p>1,012 definitions; '+str(len(families))+' provisional description families. '+esc(str(result['mapping_counts']))+'</p>',
 '<p>Start with the <a href="#ch2">Dynamics</a> and <a href="#ch8">Thermal Physics</a> coverage. Ordinary textbook exercise links open the public 1.1 preview. Pool reuse is deduplicated by question identity.</p>']
chapter_titles=['Introduction','Kinematics','Dynamics','Work and Energy','Impulse and Momentum','Oscillations and Waves','Rotation','Fluids','Thermal Physics','Electricity','Magnetism','Light','Quantum Physics','Special Relativity','Nuclear and Particle Physics']
summary=[]
review_path=OUT/'reviewed-relationships.json'
if review_path.exists():
    page.append('<h2>Initial content-level findings for the pilot</h2><p>These findings compare actual question content; they are proposals for what to examine next, not approved additions.</p><ol>')
    for finding in load(review_path)['items']:
        page.append('<li>'+esc(finding['finding'])+' <strong>Next:</strong> '+esc(finding['next_step'])+'<p>'+question_locator(question_by_id[finding['mom_uniqueid']])+'</p></li>')
    page.append('</ol>')
for ch,title in enumerate(chapter_titles):
    ss=[s for s in section_rows if s['label'].startswith(str(ch)+'.')]
    ff={f for s in ss for f in s['active_family_ids']}
    summary.append(dict(chapter=ch,title=title,ordinary_exercises=sum(len(s['existing_exercise_ids']) for s in ss),active_candidate_families=len(ff),sections_without_matches=[s['label'] for s in ss if s['coverage_status'].startswith('no-section')]))
    page.append(f'<section id="ch{ch}"><h2>{ch}. {esc(title)}</h2><table><tr><th>Section</th><th>Existing ordinary exercises</th><th>Active assessment families</th><th>Lecture families</th></tr>')
    for s in ss:page.append(f'<tr><td><a href="#'+s['section_id'].replace(':','-')+'">'+esc(s['label']+' '+s['title'])+f'</a></td><td>{len(s["existing_exercise_ids"])}</td><td>{len(s["active_family_ids"])}</td><td>{len(s["lecture_family_ids"])}</td></tr>')
    page.append('</table>')
    for s in ss:
        page.append('<details id="'+s['section_id'].replace(':','-')+'"><summary>'+esc(s['label']+' '+s['title'])+'</summary>')
        qq=[q for q in questions if s['section_id'] in q['section_ids']];byfam=defaultdict(list)
        for q in qq:byfam[q['family_id']].append(q)
        page.append('<p>Source families (including separately marked archive/lecture use):</p><ul>')
        for fid,qs in sorted(byfam.items(),key=lambda kv:families[kv[0]]['title']):
            roles=sorted({r for q in qs for r in q['roles']});statuses=sorted({q['mapping_status'] for q in qs})
            page.append('<li>'+esc(families[fid]['title'])+' — '+esc(', '.join(roles))+'; '+esc(', '.join(statuses))+'<details><summary>Question descriptions and assessment locations</summary><ul>'+''.join('<li>'+question_locator(q)+'</li>' for q in qs)+'</ul></details></li>')
        page.append('</ul><p>Existing textbook questions (open to judge actual overlap):</p><ul>')
        for e in exercises:
            if e['section_id']==s['section_id'] and e['kind']!='inline-check':page.append('<li><a href="'+esc(e['url'])+'">'+esc(e['text'][:210])+('…' if len(e['text'])>210 else '')+'</a></li>')
        page.append('</ul></details>')
    page.append('</section>')
page.append('<h2>Chapter-only or unresolved definitions</h2><p>These require topic/context review; no automatic insertion or exclusion.</p><ul>')
for q in questions:
    if not q['section_ids']:page.append('<li>'+question_locator(q)+'<br>Chapters '+esc(str(q['chapter_context']))+'; '+esc(', '.join(q['roles']))+'</li>')
page.append('</ul></html>')
(OUT/'index.html').write_text(''.join(page),encoding='utf-8')
(OUT/'chapter-summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
dest=ROOT/'prototype/dist/review-1.1/exercise-crosswalk';dest.mkdir(parents=True,exist_ok=True)
shutil.copyfile(OUT/'index.html',dest/'index.html')
print(json.dumps(dict(families=len(families),mapping=result['mapping_counts'],textbook_exercises=len(exercises))))
