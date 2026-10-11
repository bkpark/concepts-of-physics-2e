"""Apply the reviewed body-numbering decisions using frozen preview labels/IDs.

Run once. The baseline snapshot, per-object decisions and full corrections are
retained so no heuristic silently edits equation numbers on subsequent builds.
"""
from pathlib import Path
import json,re,hashlib,collections,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'reports/1.1/equation-numbering-audit'
baseline=OUT/'body-review-baseline.json'
if not baseline.exists():baseline.write_bytes((OUT/'inventory.json').read_bytes())
rows=json.loads(baseline.read_text(encoding='utf-8'))['expressions']
# Explicit decisions after inspecting the complete display inventory.
remove_body='''0.3.1 1.2.2 1.2.3 1.4.3
1.6.1 1.6.2 1.6.3 1.6.4 1.6.7 1.6.10 1.6.11 1.6.14 1.6.15 1.6.16 1.6.22 1.6.27 1.6.28 1.6.29 1.6.30 1.6.31
2.4.1 2.4.2 2.4.3 2.4.4 2.4.8 2.6.1 2.6.2 2.6.3 2.8.2 2.8.5 2.9.3 2.9.5 2.9.6 2.10.3
3.2.3 3.3.1 3.3.2 3.3.3 3.3.4 3.4.3 3.5.2
4.2.1 4.2.8 4.2.9 4.2.10 4.2.11 4.4.1 4.4.2 4.4.3
5.8.3 6.3.1 6.3.2 6.3.3 6.4.11 6.5.12 6.5.13 6.5.16
7.3.1 7.4.1 7.5.1 7.5.2 7.5.3 7.5.4 7.5.5 7.6.1 7.6.9 7.7.5 7.7.6 7.8.1 7.8.4 7.8.5 7.8.7 7.8.12
8.9.2 8.9.3 8.9.4 8.10.1 8.10.2 8.10.3 8.11.1 8.13.3 8.13.4 8.14.1
9.2.2 9.4.2 9.6.1 9.6.4 9.6.6 9.9.1 9.9.2 9.10.1 9.10.2 9.11.2 9.11.3 9.11.4 9.11.18 9.11.19
10.6.1 10.11.1 10.11.2
11.7.1 11.7.2 11.9.1 11.9.5 11.9.6
12.4.2 12.7.6 12.7.7 12.8.2
13.3.1 13.3.2 13.3.3 13.3.4 13.3.5 13.3.6 13.3.7 13.3.8 13.3.9
13.4.1 13.4.2 13.4.3 13.4.4 13.4.5 13.5.12 13.7.8 13.7.9 13.7.11 13.7.12 13.7.13 13.7.20
14.4.2 14.8.2 14.8.3'''.split()
remove_body=set(remove_body)
retain_examples={'0.3.2':'Introduces the average-speed definition.', '12.3.5':'Explicitly introduces the reusable photon relation E = hc/lambda.'}
ambiguous={'2.10.8':'Minimum friction coefficient for an unbanked turn: reusable special-case result or example-only algebra?',
 '4.6.4':'Final velocity after capture by an initially stationary body: useful collision result or example-only algebra?',
 '6.4.17':'Rolling solid-cylinder speed: useful special-case result or example-only algebra?',
 '9.6.18':'Speed gained through a potential difference: reusable charged-particle result or example-only algebra?'}
decisions=[];edits=collections.defaultdict(list)
for row in rows:
    if row['summary'] or not row['visible_number']:continue
    label=row['label']
    if row['references']:action='retain';reason='Explicit internal target-ID reference.'
    elif label in ambiguous:action='review';reason=ambiguous[label]
    elif label in retain_examples:action='retain';reason=retain_examples[label]
    elif row['category'].startswith('worked'):action='unnumber';reason='Routine worked-example application, substitution, intermediate step, or answer; not a new general law.'
    elif label in remove_body:action='unnumber';reason='Reviewed intermediate derivation, numerical illustration, repeated formula, or recap.'
    elif row['category'].startswith('approved givens'):action='unnumber';reason='Approved givens list.'
    else:action='retain';reason='Definition, constant, general relationship, distinct physical result, or reaction scheme.'
    decisions.append(dict(row,action=action,reason=reason))
    if action=='unnumber':edits[row['module']].append(row)
ledger_path=ROOT/'maintained/editorial-changes.json';ledger=json.loads(ledger_path.read_text(encoding='utf-8'))
changed=0
for mid,items in edits.items():
    p=ROOT/f'maintained/modules/{mid}/index.cnxml';before=p.read_bytes().decode('utf-8');after=before;actual=[]
    for row in items:
        pattern=r'<equation\b[^>]*\bid="'+re.escape(row['id'])+r'"[^>]*>'
        match=re.search(pattern,after);assert match,row['id'];old=match.group()
        if re.search(r'class="[^"]*\bunnumbered\b',old):continue
        new=re.sub(r'class="([^"]*)"',lambda m:'class="'+m.group(1)+' unnumbered"',old) if 'class=' in old else old[:-1]+' class="unnumbered">'
        after=after.replace(old,new,1);actual.append(row['label'])
    if after==before:continue
    # The only source mutations are unnumbered class tokens on equation wrappers.
    ET.fromstring(after)
    def fingerprint(s):
        r=ET.fromstring(s)
        for e in r.iter():
            if e.tag.endswith('}equation'):
                v=' '.join(x for x in e.get('class','').split() if x!='unnumbered')
                if v:e.set('class',v)
                else:e.attrib.pop('class',None)
        return ET.tostring(r)
    assert fingerprint(before)==fingerprint(after)
    ident='BODY-NUMBERING-POLICY-'+mid;rec=ROOT/f'proposals/author-corrections/{ident}.json';assert not rec.exists()
    rec.write_text(json.dumps(dict(id=ident,status='applied-maintainer-approved',target_release='cp2e-ver1.1',module=mid,source_path=p.relative_to(ROOT).as_posix(),source_sha256=hashlib.sha256(before.encode()).hexdigest(),after_sha256=hashlib.sha256(after.encode()).hexdigest(),before=before,after=after,reason='Apply authorized equation-numbering policy; frozen-preview labels: '+', '.join(actual)),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    p.write_bytes(after.encode());ledger['changes'].append(rec.relative_to(ROOT).as_posix());changed+=len(actual)
ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Recompute summary aliases after body selection, rather than retaining stale targets.
np=ROOT/'maintained/numbering.json';rules=json.loads(np.read_text(encoding='utf-8'));rules['summary_equation_aliases']={};np.write_text(json.dumps(rules,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(OUT/'body-decisions.json').write_text(json.dumps({'newly_unnumbered':changed,'decisions':decisions},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lines=['# Body equations requiring judgment','','Numbers below refer to the unchanged public preview. All four retain their numbers locally pending review.','']
for r in decisions:
    if r['action']=='review':lines += [f"## {r['label']} — {r['title']}",'',f"[View example]({r['url']})",'',r['expression'],'',r['reason'],'','Context: '+r['before'],'']
lines += ['## Unnumbered body displays','','Existing table math, worked calculations, givens, and abbreviated relations remain unnumbered. Two central standalone relations merit consideration for adding numbers: the work-energy theorem W_net = Delta KE in 3.3, and the speed of light c = 3.00 x 10^8 m/s in 11.2. These are not promoted automatically because their current containers are prose; the expanded work-energy relation and the speed-of-light definition in 11.7 already have numbered displays.','']
(OUT/'body-review.md').write_text('\n'.join(lines),encoding='utf-8')
print('Newly unnumbered:',changed,'Modules:',len(edits),'Ambiguous:',len(ambiguous))
