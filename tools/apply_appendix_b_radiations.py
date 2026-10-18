"""Apply approved compact radiation selection and evaluated photon yields."""
from pathlib import Path
import hashlib,json,re,xml.etree.ElementTree as E
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'reports/1.1/appendix-b-consistency'
P=ROOT/'maintained/modules/m42702/index.cnxml';before=P.read_bytes();source=before.decode('utf-8')
assert 'appendix-b-half-life-source' in source and 'appendix-b-emission-sources' not in source
C='{http://cnx.rice.edu/cnxml}';M='{http://www.w3.org/1998/Math/MathML}'
def text(e):
    if e.tag==M+'annotation':return ''
    return (e.text or '')+''.join(text(c)+(c.tail or '') for c in e)
def plain(s):return ''.join(text(E.fromstring('<root xmlns:m="'+M[1:-1]+'">'+s+'</root>')).split())
entry=r'<entry\b[^>]*?/>|<entry\b[^>]*>.*?</entry>'
groups={};current=None
body=re.search(r'<tbody>.*?</tbody>',source,re.S).group()
for row in re.findall(r'<row\b[^>]*>.*?</row>',body,re.S):
    cells=re.findall(entry,row,re.S)
    name=plain(cells[0]);m=re.fullmatch(r'([A-Za-z]+)(\d+)(m?)',name)
    if m:
        current=m[1]+'-'+m[2]+m[3];groups[current]={'isotope':cells[0],'half':cells[1],'rows':[]}
    groups[current]['rows'].append(row)
data=json.loads((D/'selected-emissions.json').read_text('utf-8'));assert set(groups)=={r['isotope'] for r in data}
def math(s):return '<m:math xmlns:m="http://www.w3.org/1998/Math/MathML">'+s+'</m:math>'
modes={'bm':math('<m:msup><m:mi>β</m:mi><m:mo>−</m:mo></m:msup>'),'bp':math('<m:msup><m:mi>β</m:mi><m:mo>+</m:mo></m:msup>'),'a':math('<m:mi>α</m:mi>'),'EC':'EC','IT':'IT'}
def cell(value):
    if value=='≈0.00000001':value=math('<m:mo>≈</m:mo><m:msup><m:mn>10</m:mn><m:mn>−8</m:mn></m:msup>')
    if value=='0.0000765':value=math('<m:mn>7.65</m:mn><m:mo>×</m:mo><m:msup><m:mn>10</m:mn><m:mn>−5</m:mn></m:msup>')
    return '<entry align="center">'+value+'</entry>' if value else '<entry/>'
outrows=[];changes=[]
for r in data:
    g=groups[r['isotope']];lines=[]
    for i in range(max(len(r['charged']),len(r['gamma']))):
        ch=r['charged'][i] if i<len(r['charged']) else ['','',''];ga=r['gamma'][i] if i<len(r['gamma']) else ['','']
        rid=''
        if ch[0]=='EC' and r['isotope'] in {'Na-22','Cl-36','K-40'}:rid=' id="appendix-b-'+r['isotope'].lower()+'-capture"'
        first=g['isotope'] if i==0 else '<entry/>'
        # Historical isotope annotations sometimes name a different isotope.
        first=re.sub(r'<m:annotation\b[^>]*>.*?</m:annotation>','',first,flags=re.S)
        line='<row'+rid+'>'+first+(g['half'] if i==0 else '<entry/>')+cell(modes.get(ch[0],''))+cell(ch[1])+cell(ch[2])+cell(math('<m:mi>γ</m:mi>') if ga[0] else '')+cell(ga[0])+cell(ga[1])+'</row>'
        lines.append(line)
    outrows.extend(lines);changes.append({'isotope':r['isotope'],'source':r['source'],'audit_note':r['audit_note'],'before':'\n'.join(g['rows']),'after':'\n'.join(lines)})
out=source.replace(body,'<tbody>\n'+'\n'.join(outrows)+'\n</tbody>')
intro='<para id="import-auto-id2205639">This table lists selected emissions. Decay modes are alpha decay (α), beta-minus decay (β−), positron emission (β+), electron capture (EC), and isomeric transition (IT). The suffix m identifies a metastable nuclear state. Alpha energies are the kinetic energies of the emitted particles, excluding daughter-nucleus recoil. Beta energies are spectrum endpoints; the mean energy depends on the spectrum and is not generally half the endpoint. EC and IT have no particle energy listed in that column.</para>\n<para id="appendix-b-yield-conventions">Particle yields are emitted particles per 100 decays of the listed isotope; entries beside EC or IT give decays through that mode per 100 decays. Photon yields are gamma photons per 100 parent decays, including the indicated daughter de-excitations, rather than probabilities for transitions that can also produce conversion electrons. Daughter isomers can delay photon emission. The left and right entries on the same line are independent lists, not necessarily coincident emissions. Only selected emissions are shown; yields need not sum to 100. X-rays, conversion electrons, annihilation photons, and later radioactive-daughter emissions are omitted, except for the listed Ba-137m and Mn-52m transitions following Cs-137 and Fe-52 decay.</para>'
out=re.sub(r'<para id="import-auto-id2205639">.*?</para>',lambda m:intro,out,count=1,flags=re.S)
headers=['Isotope',math('<m:msub><m:mi>t</m:mi><m:mrow><m:mn>1</m:mn><m:mo>/</m:mo><m:mn>2</m:mn></m:mrow></m:msub>'),'Decay mode','Particle energy (MeV)','Per 100 decays','Photon','Photon energy (MeV)','Photons per 100 decays']
out=re.sub(r'<thead>.*?</thead>',lambda m:'<thead><row>'+''.join(cell(x) for x in headers)+'</row></thead>',out,count=1,flags=re.S)
note='<para id="appendix-b-half-life-source">Half-lives follow <link url="https://doi.org/10.1088/1674-1137/abddae">NUBASE2020</link>, consistent with Appendix A. Parentheses give uncertainty in the last quoted digits. Emission data are rounded selections from the sources below; they may use a different evaluation of branching fractions from NUBASE2020.</para>\n<para id="appendix-b-emission-sources">Radiation energies and yields follow the <link url="https://www.lnhb.fr/home/nuclear-data/nuclear-data-table/">DDEP evaluated tables</link>, except for potassium-43, rubidium-86, indium-113m, and mercury-197 (<link url="https://www.lnhb.fr/Laraweb/">LNHB Nucléide-Lara</link>) and cesium-129 (<link url="https://mirdsoft.org/products/MIRDspecs/MIRDspecs_HTMLs/Cs-129.htm">ICRP Publication 107 data reproduced by MIRDspecs</link>). Potassium-43 and rubidium-86 beta endpoints are calculated from the LNHB decay-scheme energy differences. Sodium-22 and potassium-40 branching fractions follow DDEP consistently with their emission data. The sources provide full decay schemes, evaluation dates, and uncertainties. These selected, rounded data are intended for teaching.</para>'
out=re.sub(r'<para id="appendix-b-half-life-source">.*?</para>',lambda m:note,out,count=1,flags=re.S)
E.fromstring(out)
oldids=set(re.findall(r'\bid="([^"]+)"',source));newids=re.findall(r'\bid="([^"]+)"',out)
assert oldids<=set(newids) and len(newids)==len(set(newids))
after=out.encode('utf-8');pid='APPENDIX-B-EVALUATED-RADIATION-ENERGIES-AND-YIELDS'
proposal={'id':pid,'status':'approved','description':'Apply evaluated selected particle energies and photon yields after maintainer approved compact selected lines, dominant replacements for ambiguous entries, and DDEP branching consistency while retaining NUBASE half-lives.','changes':[{'path':'maintained/modules/m42702/index.cnxml','before_sha256':hashlib.sha256(before).hexdigest(),'after_sha256':hashlib.sha256(after).hexdigest(),'rows':changes,'intro':intro,'source_notes':note}]}
(D/'source-before-radiation-updates.cnxml').write_bytes(before)
(ROOT/'proposals/maintainer-corrections'/f'{pid}.json').write_text(json.dumps(proposal,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
ledger=ROOT/'maintained/editorial-changes.json';j=json.loads(ledger.read_text('utf-8'));j['changes'].append(f'proposals/maintainer-corrections/{pid}.json')
P.write_bytes(after);ledger.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'isotopes':len(data),'rows':len(outrows),'preserved_ids':len(oldids),'after_sha256':hashlib.sha256(after).hexdigest()}))
