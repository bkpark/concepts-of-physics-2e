"""Read-only numbering audit; recommendations are editorial triage, not mutations."""
from pathlib import Path
import sys, json, re, collections, xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'prototype'))
from collection import read_sections
from numbering import build_objects
C='{http://cnx.rice.edu/cnxml}'; M='{http://www.w3.org/1998/Math/MathML}'
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf-8'))
sections=read_sections(ROOT,load('maintained/sections.json')['sections'])
roots={s['module_id']:ET.parse(ROOT/s['source']).getroot() for s in sections}
course={x['section_id'].split(':')[1]:x['label'] for x in load('metadata/numbering-course-2026-07-07.proposed.json')['section_labels']}
anchor=lambda mid,id:mid+'--'+id.encode().hex()
objects=build_objects(sections,roots,'course',course,load('maintained/numbering.json'),anchor)
def txt(e):
    if e is None or e.tag==M+'annotation':return ''
    return (e.text or '')+''.join(txt(c)+(c.tail or '') for c in e)
def flat(e):return re.sub(r'\s+',' ',txt(e)).strip()
refs=collections.defaultdict(list); literals=[]
for mid,root in roots.items():
    for e in root.iter():
        if e.get('target-id'):
            refs[(e.get('document',mid),e.get('target-id'))].append({'module':mid,'text':flat(e),'tag':e.tag.split('}')[-1]})
        for value in [e.text,e.tail]:
            if value and re.search(r'\b(?:[Ee]q(?:uation)?s?\.?)[\s\xa0]*(?:\()?\d+\.\d+',value):
                literals.append({'module':mid,'text':value.strip()})
rows=[]
for section in sections:
    mid=section['module_id'];root=roots[mid];parents={c:p for p in root.iter() for c in p}
    def ancestors(e):
        out=[]
        while e in parents:e=parents[e];out.append(e)
        return out
    for e in root.iter():
        chain=ancestors(e)
        equation=e.tag==C+'equation'
        bare=e.tag==M+'math' and e.get('display')=='block' and not any(a.tag==C+'equation' for a in chain)
        if not(equation or bare):continue
        summary=any('section-summary' in a.get('class','').split() or (a.tag==C+'section' and flat(a.find(C+'title')).lower() in ('section summary','chapter summary')) for a in chain)
        example=next((a for a in chain if a.tag==C+'example'),None)
        exercise=any(a.tag in (C+'exercise',C+'solution') for a in chain)
        id=e.get('id');loc=next((a.get('id') for a in [e]+chain if a.get('id')),None)
        obj=objects.get((mid,id),{});label=obj.get('label');incoming=refs.get((mid,id),[]) if id else []
        parent=parents.get(e);siblings=list(parent) if parent is not None else [];idx=siblings.index(e) if parent is not None else 0
        before=' '.join(flat(x) for x in siblings[max(0,idx-2):idx])[-900:]
        after=' '.join(flat(x) for x in siblings[idx+1:idx+3])[:900]
        if bare:
            prose=next((a for a in chain if a.tag==C+'para'),None)
            if prose is not None:before=flat(prose)[:1800];after=''
        numbers=[flat(x) for x in e.iter(M+'mn') if re.search(r'\d',flat(x))]
        if bare and any(a.tag in (C+'table',C+'entry') for a in chain):bucket='table math: keep unnumbered'
        elif summary:bucket='summary: keep unnumbered; exclude from counter'
        elif incoming:bucket='referenced: retain number or revise referring text'
        elif mid=='m67042' and id=='eip-634':bucket='approved givens: remove number'
        elif not label:bucket='unnumbered display: inspect for reusable law/definition'
        elif example is not None or exercise:
            bucket='worked calculation: likely remove number' if len(numbers)>=3 else 'worked symbolic step/result: individual review'
        elif any(re.search(r'\d[.,]\d|[3-9]\d|\d{3}',n) for n in numbers):bucket='numerical body display: individual review'
        else:bucket='body relationship: presumptive retain'
        rows.append(dict(module=mid,section=course.get(mid,mid),title=section.get('title',''),id=id,location=loc,label=label,visible_number=bool(label and not summary),summary=summary,example=flat(example.find(C+'title')) if example is not None else None,exercise=exercise,bare_display=bare,category=bucket,expression=flat(e),before=before,after=after,references=incoming,url='https://intro-1-1.coaphys.xyz/sections/'+section['candidate_slug']+'/#'+anchor(mid,loc) if loc else None))
counts=dict(collections.Counter(r['category'] for r in rows))
stats=dict(modules=len(roots),displays=len(rows),visible_numbered=sum(r['visible_number'] for r in rows),summary_displays=sum(r['summary'] for r in rows),hidden_summary_counter_entries=sum(r['summary'] and bool(r['label']) for r in rows),referenced_displays=sum(bool(r['references']) for r in rows),bare_block_math=sum(r['bare_display'] for r in rows),literal_reference_candidates=len(literals),categories=counts)
out=ROOT/'reports/1.1/equation-numbering-audit';out.mkdir(parents=True,exist_ok=True)
(out/'inventory.json').write_text(json.dumps(dict(summary=stats,expressions=rows,literal_reference_candidates=literals),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
intro=['# Equation-numbering audit','', 'Read-only source inventory. No numbering or preview changes. Current course labels are used throughout.','', 'Classification is triage: numerical-token counts identify likely calculations, not proof that an equation is dispensable. Mathematical snippets flatten fractions/scripts; open the linked source display to inspect notation. Block MathML outside equation containers is included; inline MathML and CSS-only visual displays are not treated as display equations.','', 'Policy: retain important laws, definitions, reusable results and explicit references; usually omit numbers on givens, routine substitutions and repeated summaries. Review derivations and worked results individually.','', '## Counts','']
intro += [f'- {k}: {v}' for k,v in stats.items() if k!='categories']
intro += ['', '## Findings','', '- The renderer hides summary labels, but course numbering currently counts those equations. Exclude summaries at the counter stage when implementing the policy.','- Keep stable XML IDs/anchors when suppressing labels. Internal target-ID links can survive; check their displayed text and literal references before renumbering.','- External references (including MyOpenMath) are outside this audit and remain for the author to check.','']
for category in counts:
    lines=['# '+category,'']
    subset=[r for r in rows if r['category']==category]
    for r in subset:
        lines += [f"## {r['label'] or r['section']+' (unnumbered)'} — {r['title']}",'',f"[Open current preview]({r['url']}) · `{r['module']}#{r['location']}`",'', '**Expression:** '+r['expression'],'','**Before:** '+r['before'],'','**After:** '+r['after'],'', '**Incoming references:** '+str(len(r['references'])),'']
    name=re.sub(r'[^a-z0-9]+','-',category.lower()).strip('-')+'.md'
    (out/name).write_text('\n'.join(lines),encoding='utf-8')
    intro += [f'- [{category} ({len(subset)})]({name})']
(out/'review.md').write_text('\n'.join(intro)+'\n',encoding='utf-8')
print(json.dumps(stats))

