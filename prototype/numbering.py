"""Presentation labels keyed by stable module/XML IDs; source is never renumbered."""
from collections import Counter
C='{http://cnx.rice.edu/cnxml}'
def build_objects(sections,roots,profile,course,rules,anchor):
    groups=[];previous=None;chapter=0
    for section in sections:
        group=section['parents'][-1] if section['parents'] else section['module_id']
        if group!=previous:
            chapter+=bool(section['parents']);groups.append((chapter,[]));previous=group
        groups[-1][1].append(section)
    output={};rule=rules[profile]
    for chapter,group in groups:
        candidates=[];counter=Counter();section_counters={};endmatter_counter=Counter()
        for section in group:
            mid=section['module_id'];root=roots[mid];parents={c:p for p in root.iter() for c in p}
            for e in root.iter():
                if not e.get('id'):continue
                ancestors=[];p=e
                while p in parents:p=parents[p];ancestors.append(p)
                classes={word for a in ancestors for word in a.get('class','').split()}
                category=next((a.get('type') for a in [e]+ancestors if a.tag==C+'exercise' and a.get('type')),None)
                if category is None:category=next((x for x in ('conceptual-questions','problems-exercises') if x in classes),'body')
                relocated=bool(classes.intersection(rule['relocated_ancestor_classes'])) or category in rule['relocated_exercise_types']
                candidates.append((int(relocated),mid,e,classes,category))
        if rule['backmatter_after_body']:
            candidates.sort(key=lambda row:(row[0],{'conceptual-questions':0,'problems-exercises':1}.get(row[4],2) if row[0] and rule.get('chapter_exercise_views') else 0))
        for relocated,mid,e,classes,category in candidates:
            kind=e.tag.split('}')[-1];label=None
            empty=e.find(C+'label');explicit_empty=empty is not None and not ''.join(empty.itertext()).strip()
            suppressed=(kind=='equation' and bool(classes.intersection(rule['unnumbered_equation_ancestor_classes'])))
            if kind in ('figure','example','equation','table','exercise') and 'unnumbered' not in e.get('class','').split() and not explicit_empty and not suppressed:
                key=(kind,category if kind=='exercise' and rule['separate_exercise_counters'] else '')
                active=counter if rule['scope']=='chapter' else section_counters.setdefault(mid,Counter())
                active[key]+=1;prefix=str(chapter) if rule['scope']=='chapter' else course.get(mid,'?')
                use_prefix=kind!='exercise' or rule['exercise_prefix'] or (category=='body' and rule['inline_exercise_prefix'])
                label=f'{prefix}.{active[key]}' if use_prefix else str(active[key])
                if relocated and rule.get('chapter_exercise_views'):
                    endkey=(kind,category if kind=='exercise' else '')
                    endmatter_counter[endkey]+=1
                    chapter_label=course.get(mid,'?').split('.')[0]
                    label=str(endmatter_counter[endkey]) if kind=='exercise' else f'{chapter_label}.E.{endmatter_counter[endkey]}'
            stable=mid+'#'+e.get('id')
            if stable in rules['overrides'][profile]:label=rules['overrides'][profile][stable]['label']
            output[(mid,e.get('id'))]={'kind':kind,'label':label,'anchor':anchor(mid,e.get('id'))}
    return output
