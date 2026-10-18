"""Conservative, reversible repairs to the approved operator-audit candidates.

Default is a dry run. Source outside each changed MathML expression is byte-preserved.
"""
from pathlib import Path
import collections, hashlib, html, json, re, sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'reports/1.1/operator-audit'
sys.path.insert(0, str(ROOT / 'prototype'))
from native_math import native_math
M = 'http://www.w3.org/1998/Math/MathML'
audit = json.loads((OUT / 'audit.json').read_text(encoding='utf-8'))
findings = {f['id']: f for f in audit['findings']}
TOKEN = re.compile(r'<m:(mi|mn|mo|mtext)(\s[^<>]*?)?>([^<>]*)</m:\1>')
MATH = re.compile(r'<m:math\b[^>]*>.*?</m:math>', re.S)
OPS = set('+−-±∓×÷=≠≈≃≅≡∝<>≤≥≪≫∈∉⊂⊃⊆⊇→←↔⇒⇔')
NUM = r'[+−-]?\d+(?:\.\d+)?'
local = lambda e: e.tag.rsplit('}', 1)[-1]

def parse(s):
    return ET.fromstring('<wrapper xmlns:m="'+M+'">'+s+'</wrapper>')[0]

def content(s):
    e = parse(s)
    for p in e.iter():
        for c in list(p):
            if local(c) in ('annotation','annotation-xml'): p.remove(c)
    return re.sub(r'\s+', '', ''.join(e.itertext()))

def repair(s):
    actions = collections.Counter()
    # Annotation strings are preserved, and never treated as presentation tokens.
    annotations = []
    def hide(m):
        annotations.append(m[0]); return f'<!--ANNOTATION{len(annotations)-1}-->'
    s = re.sub(r'<m:annotation\b.*?</m:annotation>', hide, s, flags=re.S)
    def tok(m):
        tag, attrs, text = m[1], m[2] or '', m[3]
        t = html.unescape(text).strip()
        newtag = tag
        if tag in ('mtext','mo') and re.fullmatch(NUM, t):
            newtag = 'mn'; actions['numeric-token'] += 1
        elif tag in ('mi','mn','mtext') and (t in OPS or t=='/'):
            newtag = 'mo'; actions['operator-token'] += 1
        elif t == 'ln' and (tag == 'mn' or 'italic' in attrs):
            newtag = 'mi'; attrs = re.sub(r'\s+(?:fontstyle|mathvariant)="[^"]*"', '', attrs)
            attrs += ' mathvariant="normal"'; actions['upright-function'] += 1
        elif tag in ('mi','mn','mtext') and re.fullmatch(r'[=≈][ +−-]*', t):
            actions['separate-relation-and-sign'] += 1
            return ''.join('<m:mo>'+c+'</m:mo>' for c in t if not c.isspace())
        # Embedded equality/arithmetic: split only the operator, retaining other
        # token text and mathematical grouping. Units with slashes stay intact.
        elif tag in ('mtext','mn') and (any(c in t for c in '=≈') or ('+' in t and t!='X+')):
            parts = re.split(r'([=≈+])', text)
            actions['embedded-relation'] += 1
            return ''.join('<m:mo>'+p+'</m:mo>' if p in '=≈+' else '<m:mtext'+attrs+'>'+p+'</m:mtext>' for p in parts if p)
        return '<m:'+newtag+attrs+'>'+text+'</m:'+newtag+'>'
    s = TOKEN.sub(tok, s)
    # Complete adjacent decimal fragments only; never cross grouping boundaries.
    decimal = re.compile(r'<m:(?:mn|mtext)>\s*([+−-]?\d+)\s*</m:(?:mn|mtext)>\s*<m:(?:mn|mo|mtext)>\s*\.\s*</m:(?:mn|mo|mtext)>\s*<m:(?:mn|mtext)>\s*(\d+)\s*</m:(?:mn|mtext)>')
    def dec(m):
        actions['joined-decimal'] += 1
        return '<m:mn>'+m[1]+'.'+m[2]+'</m:mn>'
    s = decimal.sub(dec, s)
    # Normalize newly exposed numeric text beside the separated relations.
    s = TOKEN.sub(lambda m: '<m:mn'+(m[2] or '')+'>'+m[3]+'</m:mn>' if m[1]=='mtext' and re.fullmatch(NUM,html.unescape(m[3]).strip()) else m[0], s)
    # Set explicit infix only when the adjacent outer sibling is an operand.
    # This preserves unary signs after relations, open fences, and other operators.
    root = parse(s); parents = {c:p for p in root.iter() for c in p}
    mo_nodes = list(root.iter('{'+M+'}mo')); forms = {}
    def terminal(e, first=False):
        while len(e) and local(e) in ('mrow','mstyle'):
            children=[c for c in e if len(c) or (c.text or '').strip()]
            if not children: return None
            e=children[0 if first else -1]
        if local(e)=='mspace' or (not len(e) and not (e.text or '').strip()): return None
        return e
    for k,e in enumerate(mo_nodes):
        t=(e.text or '').strip(); p=parents.get(e)
        if t not in '+−-=≈×÷∝<>≤≥' or e.get('form') or p is None or local(p) not in ('mrow','mstyle'): continue
        kids=list(p); i=kids.index(e); gp=parents.get(p)
        if gp is None or local(gp) not in ('mrow','mstyle','math'): continue
        outer=list(gp); j=outer.index(p)
        if i==0 and len(kids)>1 and j>0:
            prev=next((q for q in (terminal(x) for x in reversed(outer[:j])) if q is not None),None)
            if prev is not None and (local(prev)!='mo' or (prev.text or '').strip() in ')]}'):
                forms[k]='infix'
        elif i==len(kids)-1 and i>0 and j<len(outer)-1:
            prev=terminal(kids[i-1]); nxt=terminal(outer[j+1],True)
            if prev is not None and nxt is not None and local(prev)!='mo' and local(nxt)!='mo': forms[k]='infix'
    counter=[-1]
    def form(m):
        counter[0]+=1
        if counter[0] in forms:
            actions['explicit-binary-form']+=1
            return m[0][:-1]+' form="infix">'
        return m[0]
    s=re.sub(r'<m:mo\b[^>]*>',form,s)
    for i,a in enumerate(annotations): s=s.replace(f'<!--ANNOTATION{i}-->',a)
    return s,dict(actions)

records=[]; files=[]
for source in sorted({f['source'] for f in findings.values()}):
    path=ROOT/source; before=path.read_bytes(); text=before.decode('utf-8'); mid=path.parent.name; index=[0]
    def replace(m):
        index[0]+=1; fid=f'{mid}-{index[0]:04d}'
        if fid not in findings or fid in ('m67135-0039','m52466-0102','m52479-0070','m76603-0252'): return m[0]
        after,actions=repair(m[0])
        if after==m[0]: return m[0]
        assert content(after)==content(m[0]),fid
        old=parse(m[0]); new=parse(after)
        # Fractions, scripts, roots, tables, and grouping remain identical.
        structural=lambda e:[local(x) for x in e.iter() if local(x) not in ('mi','mn','mo','mtext')]
        assert structural(old)==structural(new),fid
        rendered,_=native_math(new,False)
        records.append(dict(id=fid,source=source,source_id=findings[fid]['source_id'],section=findings[fid]['section'],actions=actions,before=m[0],after=after,rendered=rendered,url=findings[fid]['url']))
        return after
    after=MATH.sub(replace,text).encode('utf-8')
    if after!=before:
        ET.fromstring(after)
        files.append(dict(path=source,before_sha256=hashlib.sha256(before).hexdigest(),after_sha256=hashlib.sha256(after).hexdigest(),before=before.decode('utf-8'),after=after.decode('utf-8')))
summary=dict(expressions=len(records),modules=len(files),actions=dict(sum((collections.Counter(r['actions']) for r in records),collections.Counter())))
(OUT/'straightforward-fixes.json').write_text(json.dumps(dict(summary=summary,records=records),ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary))
if '--apply' in sys.argv:
    assert files,'Nothing to apply'
    proposal='proposals/maintainer-corrections/OPERATOR-AUDIT-STRAIGHTFORWARD.json'
    pp=ROOT/proposal; pp.parent.mkdir(exist_ok=True)
    assert not pp.exists(),'Avoid overwriting reversal history'
    pp.write_text(json.dumps(dict(status='approved',reason='Maintainer authorized straightforward audit repairs on 2026-10-16; preserve mathematical content and flag ambiguous cases.',summary=summary,files=files),ensure_ascii=False,indent=2),encoding='utf-8')
    for f in files: (ROOT/f['path']).write_bytes(f['after'].encode('utf-8'))
    lp=ROOT/'maintained/editorial-changes.json'; ledger=json.loads(lp.read_text(encoding='utf-8')); ledger['changes'].append(proposal); lp.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Applied with reversible source snapshots.')
