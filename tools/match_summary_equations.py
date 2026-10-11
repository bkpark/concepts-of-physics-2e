"""Conservative exact-copy matching for displayed summary equations."""
import audit_equation_numbering as audit
from native_math import native_math
from math_copy import copy_formats
import json,re
ROOT=audit.ROOT; M=audit.M
def signature(e):
    # Preserve fractions, scripts, symbols and text; ignore only whitespace and
    # terminal sentence punctuation. A whole display must match, in order.
    result=[]
    for math in e.iter(M+'math'):
        latex=copy_formats(native_math(math)[0])['latex']
        result.append(re.sub(r'\s+','',latex).rstrip('.,;'))
    return tuple(result)
body={}; aliases={}; flagged=[]
for row in audit.rows:
    if not row['id']:continue
    e=next(e for e in audit.roots[row['module']].iter() if e.get('id')==row['id'])
    if not row['summary'] and row['visible_number']:
        body.setdefault((row['module'],signature(e)),[]).append(row)
for row in audit.rows:
    if not row['summary']:continue
    e=next(e for e in audit.roots[row['module']].iter() if e.get('id')==row['id'])
    candidates=body.get((row['module'],signature(e)),[])
    if len(candidates)==1:
        target=candidates[0]
        aliases[row['module']+'#'+row['id']]=target['module']+'#'+target['id']
    else:
        flagged.append(dict(row,candidates=[{'label':r['label'],'id':r['id'],'url':r['url']} for r in candidates],reason='Multiple identical numbered originals' if candidates else 'No exact numbered original in this section'))
out=ROOT/'reports/1.1/equation-numbering-audit'
(out/'summary-matches.json').write_text(json.dumps({'aliases':aliases,'review':flagged},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lines=['# Summary equations requiring judgment','','Only unique exact matches in the same section are assigned automatically. Nonmatches may be mathematically equivalent; they are left unnumbered pending review.','']
for r in flagged:
    lines += [f"## {r['section']} — {r['title']}",'',f"[View]({r['url']}) · `{r['module']}#{r['id']}`",'',r['expression'],'',r['reason']+'.', '', 'Candidates: '+', '.join(str(c['label']) for c in r['candidates']),'']
(out/'summary-review.md').write_text('\n'.join(lines),encoding='utf-8')
print('Unique summary matches:',len(aliases),'Review:',len(flagged))
