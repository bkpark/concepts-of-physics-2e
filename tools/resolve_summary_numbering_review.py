"""Record individually reviewed summary matches after the body-numbering pass."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'reports/1.1/equation-numbering-audit'
baseline=json.loads((OUT/'body-review-baseline.json').read_text(encoding='utf-8'))['expressions']
bylabel={r['label']:r for r in baseline if r['label'] and not r['summary']}
matches=json.loads((OUT/'summary-matches.json').read_text(encoding='utf-8'))
# Differences reviewed: punctuation, grouping/spacing, notation formatting, or
# omitted applicability label; not inferred by flattened-string equivalence.
mapping={
 '1.2#fs-id2929393':'1.2.1','1.4#import-auto-id4086565':'1.4.2','1.5#import-auto-id2412659':'1.5.1',
 '1.6#import-auto-id2175197':'1.6.5','1.6#import-auto-id2175206':'1.6.6','1.6#import-auto-id2175249':'1.6.12','1.6#import-auto-id2176087':'1.6.17','1.6#import-auto-id2175231':'1.6.23',
 '1.7#import-auto-id3547826':'1.7.1','1.8#import-auto-id1951750':'1.8.1','1.9#eip-440':'1.9.1',
 '2.8#eip-940':'2.8.1','2.10#eip-67':'2.10.1','3.6#import-auto-id3385046':'2.7.1',
 '4.2#eip-123':'4.2.2','4.3#eip-id1637629':'4.3.1','5.6#import-auto-id1525260':'5.6.1',
 '7.4#eip-18':'7.4.2','7.8#eip-id1907714':'7.8.3','7.8#eip-id2688454':'7.8.8',
 '8.3#import-auto-id2564573':'8.3.2','8.14#eip-id1923841':'8.14.2',
 '9.4#eip-652':'9.4.1','9.4#eip-915':'9.4.3','9.10#eip-520':'9.10.4',
 '10.11#eip-779':'10.11.3','11.10#eip-id4368080':'11.10.1',
 '12.6#eip-683':'12.6.1','12.6#eip-612':'12.6.4','12.6#eip-602':'12.6.5',
 '12.7#eip-144':'12.7.2','12.7#eip-472':'12.7.4',
 '12.8#eip-998':'12.8.1','12.8#eip-294':'12.7.4','12.8#eip-874':'12.8.3',
 '13.3#eip-id3262203':'13.3.10','13.5#eip-823':'13.5.6',
 '14.5#eip-10':'14.5.3','14.5#eip-789':'14.5.4','14.5#eip-95':'14.5.10','14.5#eip-696':'14.5.18','14.5#eip-679':'14.5.21','14.5#eip-665':'14.5.22',
 '14.6#eip-693':'14.6.2','14.6#fs-id1328249':'14.6.13','14.6#eip-166':'14.6.25','14.8#eip-538':'14.8.1','14.9#eip-347':'14.9.4'}
unmatched=[];reviewed=[]
for r in matches['review']:
    key=r['section']+'#'+str(r['id'])
    if key in mapping:
        target=bylabel[mapping[key]];source=r['module']+'#'+r['id'];dest=target['module']+'#'+target['id']
        matches['aliases'][source]=dest;reviewed.append({'source':source,'target':dest,'original_preview_label':mapping[key]})
    else:unmatched.append(r)
assert len(reviewed)==len(mapping)
matches['review']=unmatched;matches['individually_reviewed_matches']=reviewed
(OUT/'summary-matches.json').write_text(json.dumps(matches,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=ROOT/'maintained/numbering.json';rules=json.loads(p.read_text(encoding='utf-8'));rules['summary_equation_aliases']=matches['aliases'];p.write_text(json.dumps(rules,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
reasons={
 '1.6':'Notation conventions, not a numbered law; recommend leave unnumbered.',
 '2.6':'Special-case equilibrium results; the body calculation is now unnumbered. Recommend leave unnumbered.',
 '3.2':'Bare MathML in prose; no equation ID. Recommend keep current unnumbered presentation.',
 '7.5':'An intermediate relation removed from the body numbering; recommend leave unnumbered.',
 '7.7':'Combines single-channel and branching continuity relations, with separate originals. Recommend leave unnumbered.',
 '8.7':'Uses generic L rather than the separate fusion/vaporization expressions. Recommend leave unnumbered.',
 '9.11':'Body formula has a malformed R_3 denominator (period included in the source token); inspect/normalize before sharing a number.',
 '10.5':'Bare MathML without an equation ID; corresponding maximum-force relation in the body is also unnumbered. Recommend leave unnumbered.',
 '12.6':'Numerical mismatch: summary proton charge-to-mass ratio is 9.57 x 10^7, body is 9.58 x 10^7 C/kg. Resolve value before linking.',
 '12.7':'Summary uses expanded angular-momentum quantization form derived in Section 12.8; choose whether to reference that later section or leave unnumbered.',
 '13.4':'Combines two separately numbered forms of length contraction. Recommend leave unnumbered or choose one canonical body display.',
 '14.4':'Combines mass conversions and uses 931.46 where the body gives 931.5 MeV/c^2. Recommend leave unnumbered; precision is an editorial choice.',
 '14.6':'Summary has lambda = 0.693/t_half, whereas body includes the exact ln(2) expression and an approximation sign. Recommend link after making the approximation treatment consistent.'}
lines=['# Summary-number matches requiring judgment','','All section/equation references are to the unchanged preview. Clear matches are already linked by stable IDs; the entries below remain unnumbered.','']
for n,r in enumerate(unmatched,1):
    lines += [f"## {n}. Section {r['section']} — {r['title']}",'',f"[View current preview]({r['url']})",'',r['expression'],'',reasons.get(r['section'],r['reason']),'']
(OUT/'summary-review.md').write_text('\n'.join(lines),encoding='utf-8')
print('Linked summaries:',len(matches['aliases']),'Remaining for review:',len(unmatched))
