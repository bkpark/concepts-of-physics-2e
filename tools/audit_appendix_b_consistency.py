"""Read-only Appendix B comparison with Appendix A and its NUBASE2020 source."""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import csv, hashlib, json, re
import xml.etree.ElementTree as E

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / 'reports/1.1/atomic-masses-audit'
OUT = ROOT / 'reports/1.1/appendix-b-consistency'
C = '{http://cnx.rice.edu/cnxml}'
M = '{http://www.w3.org/1998/Math/MathML}'

def text(e):
    if e.tag == M+'annotation':
        return ''
    if e.tag == M+'msup':
        return text(e[0])+'^'+text(e[1])
    return (e.text or '')+''.join(text(c)+(c.tail or '') for c in e)

def plain(e):
    return ' '.join(text(e).split()).replace('\xad', '')

nb = {re.sub(r'\s+', '', s[11:17]): s for s in (D/'nubase_4.mas20').read_text().splitlines() if not s.startswith('#')}
a = {}
z = None
for row in E.parse(ROOT/'maintained/modules/m42699/index.cnxml').findall('.//'+C+'tbody/'+C+'row'):
    cells = [plain(c) for c in row]
    if cells[0].isdigit():
        z = int(cells[0])
    if len(cells) == 7 and cells[2].isdigit():
        a[(z, int(cells[2]), 'metastable' in cells[1])] = cells

path = ROOT/'maintained/modules/m42702/index.cnxml'
before = path.read_bytes()
scales = {k: Decimal(v) for k,v in {'s':'1', 'm':'60', 'min':'60', 'h':'3600', 'd':'86400', 'y':'31557600', 'ky':'31557600000', 'My':'31557600000000', 'Gy':'31557600000000000'}.items()}
records = []
for row in E.fromstring(before).findall('.//'+C+'tbody/'+C+'row'):
    cells = [plain(c) for c in row]
    if not cells[0]:
        records[-1]['continuation_rows'].append(cells)
        continue
    m = re.fullmatch(r'([A-Za-z]+)(\d+)(m?)', cells[0].replace(' ', ''))
    assert m, cells[0]
    sym, mass, state = m.groups()
    n = nb[mass+sym+state]
    ref, unit, unc = n[69:78].strip(), n[78:80].strip(), n[81:88].strip()
    v, u = Decimal(ref), Decimal(unc)
    old = cells[1].replace(' ', '')
    parsed = re.fullmatch(r'([\d.]+)(?:×10\^(-?\d+))?([A-Za-z]+)', old)
    assert parsed, old
    coef, exponent, oldunit = parsed.groups()
    exponent = int(exponent or 0)
    oldvalue = Decimal(coef)*Decimal(10)**exponent
    newvalue = v*scales[unit]/scales[oldunit]
    newunc = u*scales[unit]/scales[oldunit]
    quantum = Decimal(1).scaleb(Decimal(coef).as_tuple().exponent+exponent)
    rounded = newvalue.quantize(quantum, rounding=ROUND_HALF_UP)
    same = oldvalue == newvalue
    status = 'same central value' if same else ('consistent rounding' if oldvalue == rounded else 'update central value')
    overlap = a.get((int(n[4:7]), int(mass), bool(state)))
    records.append(dict(isotope=f'{sym}-{mass}{state}', appendix_b_half_life=cells[1], evaluated_half_life=f'{ref} {unit}', evaluated_uncertainty=unc,
        evaluated_in_b_units=f'{newvalue.normalize()} {oldunit}', uncertainty_in_b_units=f'{newunc.normalize()} {oldunit}', status=status,
        appendix_a_half_life=overlap[6] if overlap else '', appendix_a_modes=overlap[5] if overlap else '', nubase_modes=n[119:].strip(),
        original_cells=cells, continuation_rows=[]))

assert len(records) == 38
assert path.read_bytes() == before
OUT.mkdir(parents=True, exist_ok=True)
payload = dict(scope='Consistency audit; no textbook edits. Radiation energies and photon yields are not validated by this half-life/decay-mode comparison.',
    source_sha256=hashlib.sha256(before).hexdigest(), source='maintained/modules/m42702/index.cnxml',
    reference='https://amdc.impcas.ac.cn/masstables/Ame2020/nubase_4.mas20', records=records)
(OUT/'comparison.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
fields = ['isotope','appendix_b_half_life','appendix_a_half_life','evaluated_in_b_units','uncertainty_in_b_units','status','appendix_a_modes','nubase_modes']
with (OUT/'half-life-comparison.csv').open('w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(records)
print(json.dumps({'isotopes':len(records),'appendix_a_overlap':sum(bool(r['appendix_a_half_life']) for r in records),
    'statuses':{s:sum(r['status']==s for r in records) for s in sorted(set(r['status'] for r in records))}}, indent=2))
for r in records:
    if r['status']=='update central value':
        print(r['isotope'], r['appendix_b_half_life'], '->', r['evaluated_in_b_units'], '(A overlap)' if r['appendix_a_half_life'] else '')
