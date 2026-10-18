"""Apply the approved Appendix C and thermochemical calorie consistency edits."""
from pathlib import Path
import re, json, hashlib, xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
changes = []
conversions = []
def edit(mid, fn):
    p = ROOT / f'maintained/modules/{mid}/index.cnxml'
    before = p.read_bytes()
    old = before.decode('utf-8')
    new = fn(old)
    ET.fromstring(new)
    assert old != new
    after = new.encode('utf-8')
    changes.append(dict(path=str(p.relative_to(ROOT)).replace('\\','/'), before_sha256=hashlib.sha256(before).hexdigest(), after_sha256=hashlib.sha256(after).hexdigest(), before=old, after=new))
    p.write_bytes(after)

def table(s, tid, fn):
    pat = rf'<table\b[^>]*id="{tid}"[\s\S]*?</table>'
    old = re.search(pat, s).group()
    return s.replace(old, fn(old))

def appendix(s):
    assert 'Supplementary unit' in s
    def avog(t):
        def row(m):
            v=m.group()
            if 'Avogadro' in v:
                v=v.replace('Avogadro’s number','Avogadro constant')
                v=v.replace('</m:math>', '<m:mspace width="0.167em"/><m:msup><m:mtext>mol</m:mtext><m:mn>−1</m:mn></m:msup></m:math>')
            return v
        return re.sub(r'<row>[\s\S]*?</row>',row,t)
    s=table(s,'import-auto-id1211982',avog)
    s=table(s,'eip-903',lambda t:t.replace('9736','9722').replace('376','371'))
    s=s.replace('Metric Prefixes for Powers of Ten and Their Symbols','Common metric prefixes')
    def si(t):
        t=t.replace('three categories: Fundamental units, Supplementary units, and Derived units','two categories: SI base units and derived units').replace('Fundamental units','Base units').replace('Electronic potential','Electric potential').replace('<entry>Abbreviation</entry>','<entry>Symbol</entry>')
        rows=list(re.finditer(r'<row>[\s\S]*?</row>',t))
        for m in reversed(rows):
            r=m.group()
            if 'Supplementary unit' in r:
                extra=''.join(f'<row><entry/><entry>{quantity}</entry><entry align="center">{symbol}</entry><entry>{name}</entry></row>' for quantity,symbol,name in [('Thermodynamic temperature','K','kelvin'),('Amount of substance','mol','mole'),('Luminous intensity','cd','candela')])
                r=extra+r.replace('Supplementary unit','Derived units')
            elif 'Derived units' in r:
                r=re.sub(r'<entry>\s*<emphasis>Derived units</emphasis>\s*</entry>','<entry/>',r)
            t=t[:m.start()]+r+t[m.end():]
        return t
    s=table(s,'import-auto-id1376084',si)
    def british(t):
        t=t.replace(' pound',' pound-force').replace('>lb<','>lbf<')
        def row(m):
            r=m.group()
            if any(x in r for x in ['mile','Force','Energy','Power','Pressure']):
                r=re.sub(r'(<m:mo\b[^>]*>)=(</m:mo>)',r'\1≈\2',r)
                r=r.replace('`=', '` approx ')
                # The mile/yard relation is exact; only the kilometre value is rounded.
                if 'mile' in r:
                    r=r.replace('>≈<','>=<',1)
            return r
        return re.sub(r'<row>[\s\S]*?</row>',row,t)
    s=table(s,'import-auto-id2371652',british)
    def other(t):
        def row(m):
            r=m.group()
            if 'torricelli' in r:
                return '<row><entry/><entry><m:math><m:mrow><m:mn>1</m:mn><m:mspace width="0.167em"/><m:mtext>torr (Torr)</m:mtext><m:mo>=</m:mo><m:mfrac><m:mn>101325</m:mn><m:mn>760</m:mn></m:mfrac><m:mspace width="0.167em"/><m:mtext>Pa</m:mtext><m:mo>≈</m:mo><m:mn>133.3</m:mn><m:mspace width="0.167em"/><m:mtext>Pa</m:mtext></m:mrow></m:math></entry></row>'
            r=r.replace('nautical mile per hour','knot (nautical mile per hour)').replace('>naut<','>kn<').replace('"naut"','"kn"')
            r=r.replace('food calorie','food Calorie').replace('4186','4184')
            if 'calorie' in r or 'Calorie' in r:
                r=r.replace('>186<','>184<').replace('"186"','"184"')
            exact=any(x in r for x in ['nautical mile','knot','angstrom','barn','liter','metric ton','day','minute of arc','second of arc','kilowatt hour','calorie','Calorie','curie'])
            if not exact:
                r=re.sub(r'(<m:mo\b[^>]*>)=(</m:mo>)',r'\1≈\2',r)
            return r
        return re.sub(r'<row>[\s\S]*?</row>',row,t)
    s=table(s,'import-auto-id1528540',other)
    note='<para id="appendix-c-conversion-conventions">Conversion factors marked ≈ are rounded. The calorie used here is the thermochemical calorie: 1 cal = 4.184 J exactly, and 1 food Calorie (Cal) = 1 kcal = 4184 J exactly. A torr is exactly 1/760 of a standard atmosphere; its value is approximately equal to one conventional millimeter of mercury. Sources: <link url="https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b8">NIST conversion factors</link> and <link url="https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html">NASA Earth data</link>.</para>'
    s=s.replace('<table xmlns:m="http://www.w3.org/1998/Math/MathML" id="import-auto-id2371652"',note+'<table xmlns:m="http://www.w3.org/1998/Math/MathML" id="import-auto-id2371652"')
    s=s.replace('>1.609<','>1.609344<')
    for r in re.findall(r'<row>[\s\S]*?</row>',s):
        if 'Avogadro constant' in r:
            unit='<m:mspace width="0.167em"/><m:msup><m:mtext>mol</m:mtext><m:mn>−1</m:mn></m:msup>'
            s=s.replace(r,r.replace(unit,'',1))
        elif 'metric  ton' in r:s=s.replace(r,r.replace('>≈<','>=<'))
    return s

def heat(s):
    para='<para id="import-auto-id2674005">Heat transfers energy, so its SI unit is the joule (J). The calorie (cal) is another unit of energy, historically based on the energy needed to raise the temperature of 1 g of water by 1°C. Because water’s specific heat varies with temperature, several calorie conventions developed. This textbook uses the thermochemical calorie, defined as exactly 4.184 J. A <term id="import-auto-id2679412">kilocalorie</term> (kcal) equals 1000 calories, or exactly 4184 J. Food Calories (Cal), sometimes called “big calories,” are kilocalories: 1 Cal = 1 kcal.</para>'
    s=re.sub(r'<para id="import-auto-id2674005">[\s\S]*?</para>',lambda m:para,s)
    s=s.replace('the best modern value for this equivalence is','the thermochemical convention gives the exact conversion')
    return s.replace('4186','4184')

def converted_tables(s,mid,tid,pairs):
    def convert(t):
        def row(m):
            r=m.group(); entries=list(re.finditer(r'<entry\b[^>]*(?:/>|>[\s\S]*?</entry>)',r))
            updates=[]
            for si,kcal,divisor in pairs:
                if len(entries)<=kcal:continue
                a=entries[si].group(); b=entries[kcal].group()
                # Numeric text at the beginning of ordinary data cells; retain notes.
                av=re.match(r'<entry[^>]*>([\d.]+(?:\s*\([\d.]+\))?)',a)
                bv=re.match(r'<entry[^>]*>([\d.]+(?:\s*\([\d.]+\))?)',b)
                if not av or not bv:continue
                nums=re.findall(r'[\d.]+',av[1]); olds=re.findall(r'[\d.]+',bv[1])
                if len(nums)!=len(olds):continue
                new=bv[1]
                for n,o in zip(nums,olds):
                    sig=len(o.replace('.','').lstrip('0'))
                    value=format(float(n)/divisor,f'#.{sig}g').rstrip('.')
                    new=new.replace(o,value,1)
                if new!=bv[1]:
                    updates.append((entries[kcal].start()+bv.start(1),entries[kcal].start()+bv.end(1),new))
                    conversions.append({'module':mid,'SI':av[1],'before_kcal':bv[1],'after_kcal':new})
            for start,end,new in sorted(updates,reverse=True):r=r[:start]+new+r[end:]
            return r
        t=re.sub(r'<row>[\s\S]*?</row>',row,t)
        return t.replace('580 kcal/kg','581 kcal/kg')
    s=table(s,tid,convert)
    note=f'<para id="{mid}-thermochemical-convention">Kilocalorie values in the table are rounded conversions of the listed SI values using 1 kcal = 4184 J. Specific heats and latent heats are measured material properties and are approximate.</para>'
    pat=rf'(<table\b[^>]*id="{tid}"[\s\S]*?</table>)'
    return re.sub(pat,lambda m:m.group()+note,s)

edit('m78798',appendix)
edit('m52368',heat)
edit('m67622',lambda s:converted_tables(s,'m67622','import-auto-id1921148',[(1,2,4184)]))
edit('m67124',lambda s:converted_tables(s,'m67124','import-auto-id3260303',[(2,3,4.184),(5,6,4.184)]))
proposal='proposals/maintainer-corrections/APPENDIX-C-AND-THERMOCHEMICAL-CALORIE.json'
(ROOT/proposal).write_text(json.dumps(dict(id='APPENDIX-C-AND-THERMOCHEMICAL-CALORIE',status='approved',description='Approved Appendix C corrections and thermochemical calorie consistency in heat prose and tables; SI material-property values and worked calculations preserved.',changes=changes),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=ROOT/'maintained/editorial-changes.json';d=json.loads(p.read_text(encoding='utf-8'));d['changes'].append(proposal);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report=ROOT/'reports/1.1/appendix-c-consistency';report.mkdir(exist_ok=True)
(report/'calorie-conversions.json').write_text(json.dumps(conversions,indent=2)+'\n',encoding='utf-8')
print(json.dumps(conversions,indent=2))
