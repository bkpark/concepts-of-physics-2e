"""Apply approved NUBASE2020 half-lives and three decay-mode corrections once."""
from pathlib import Path
from decimal import Decimal
import ast, hashlib, json, re, xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'reports/1.1/appendix-b-consistency'
P=ROOT/'maintained/modules/m42702/index.cnxml'
before=P.read_bytes(); source=before.decode('utf-8')
records=json.loads((D/'comparison.json').read_text('utf-8'))['records']
assert hashlib.sha256(before).hexdigest()==json.loads((D/'comparison.json').read_text('utf-8'))['source_sha256']
# Reuse the already-reviewed Appendix A numerical formatting functions only.
tree=ast.parse((ROOT/'tools/prepare_atomic_mass_corrections.py').read_text('utf-8'))
for node in tree.body:
    if isinstance(node,ast.FunctionDef) and node.name in {'math','number','sci','half'}:
        exec(compile(ast.Module(body=[node],type_ignores=[]),'<formatters>','exec'))
C='{http://cnx.rice.edu/cnxml}';M='{http://www.w3.org/1998/Math/MathML}'
def text(e):
    if e.tag==M+'annotation':return ''
    return (e.text or '')+''.join(text(c)+(c.tail or '') for c in e)
def plain(x):return ''.join(text(E.fromstring('<root xmlns:m="'+M[1:-1]+'">'+x+'</root>')).split())
nb={re.sub(r'\s+','',s[11:17]):s for s in (ROOT/'reports/1.1/atomic-masses-audit/nubase_4.mas20').read_text().splitlines() if not s.startswith('#')}
entry=r'<entry\b[^>]*?/>|<entry\b[^>]*>.*?</entry>'
changes=[]
def update(m):
    old=m.group();cells=list(re.finditer(entry,old,re.S))
    if len(cells)!=8 or not plain(cells[0].group()):return old
    ident=re.fullmatch(r'([A-Za-z]+)(\d+)(m?)',plain(cells[0].group()))
    if not ident:return old
    sym,a,state=ident.groups();label=f'{sym}-{a}{state}';n=nb[a+sym+state]
    vals={1:half({'half_life':n[69:78].strip(),'unit':n[78:80].strip(),'uncertainty':n[81:88].strip()})}
    extra=''
    branches={'Na-22':('90.57(8)%','EC','9.43(6)%'),'Cl-36':('98.1(1)%','EC/'+math('<m:msup><m:mi>β</m:mi><m:mo>+</m:mo></m:msup>'),'1.9(1)%'),'K-40':('89.28(13)%','EC/'+math('<m:msup><m:mi>β</m:mi><m:mo>+</m:mo></m:msup>'),'10.72(13)%')}
    if label in branches:
        first,mode,fraction=branches[label];vals[4]=first
        extra='\n<row id="appendix-b-'+label.lower()+'-capture"><entry/><entry/><entry align="center">'+mode+'</entry><entry/><entry align="center">'+fraction+'</entry><entry/><entry/><entry/></row>'
    new=old
    for i in sorted(vals,reverse=True):
        c=cells[i];attrs=re.match(r'<entry\b([^>]*?)(?:/?>)',c.group())[1].rstrip('/')
        new=new[:c.start()]+'<entry'+attrs+'>'+vals[i]+'</entry>'+new[c.end():]
    changes.append({'isotope':label,'before':old,'after':new+extra})
    return new+extra
out=re.sub(r'<row\b[^>]*>.*?</row>',update,source,flags=re.S)
assert len(changes)==38
note='<para id="appendix-b-half-life-source">Half-lives and the explicitly listed decay-mode fractions for sodium-22, chlorine-36, and potassium-40 follow <link url="https://doi.org/10.1088/1674-1137/abddae">NUBASE2020</link>, consistent with Appendix A. Parentheses give uncertainty in the last quoted digits. The isotope suffix m identifies a metastable nuclear state. EC/<m:math xmlns:m="http://www.w3.org/1998/Math/MathML"><m:msup><m:mi>β</m:mi><m:mo>+</m:mo></m:msup></m:math> denotes a combined electron-capture/positron-emission branch when the evaluation does not separate the contributions. Other radiation energies and emission percentages are not sourced to NUBASE2020.</para>'
out=out.replace('</table>', '</table>\n'+note,1)
E.fromstring(out)
assert set(re.findall(r'\bid="([^"]+)"',source))<=set(re.findall(r'\bid="([^"]+)"',out))
after=out.encode('utf-8')
pid='APPENDIX-B-HALF-LIVES-AND-DECAY-MODES'
proposal={'id':pid,'status':'approved','description':'Synchronize half-lives with the Appendix A NUBASE2020 evaluation, preserve metastable-state assignments, and add approved Na-22, Cl-36 and K-40 branches. Radiation audit remains separate.','changes':[{'path':str(P.relative_to(ROOT)).replace('\\','/'),'before_sha256':hashlib.sha256(before).hexdigest(),'after_sha256':hashlib.sha256(after).hexdigest(),'rows':changes,'added_note':note}]}
(D/'source-before-updates.cnxml').write_bytes(before)
(ROOT/'proposals/maintainer-corrections'/f'{pid}.json').write_text(json.dumps(proposal,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
ledger=ROOT/'maintained/editorial-changes.json';data=json.loads(ledger.read_text('utf-8'));data['changes'].append(f'proposals/maintainer-corrections/{pid}.json')
P.write_bytes(after);ledger.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'updated_isotopes':len(changes),'added_decay_rows':3,'after_sha256':hashlib.sha256(after).hexdigest()}))
