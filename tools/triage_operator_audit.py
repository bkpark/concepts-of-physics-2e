"""Route audit candidates for review; writes reports only, never textbook source."""
from pathlib import Path
import collections, hashlib, html, json, re, xml.etree.ElementTree as E

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'reports/1.1/operator-audit'
audit=json.loads((OUT/'audit.json').read_text(encoding='utf-8'))
findings=audit['findings']; by_id={f['id']:f for f in findings}
paths=list((ROOT/'maintained').rglob('*'))
before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths if p.is_file()}
decisions=[
 dict(id='D1',members=['m67135-0039'],title='Specific-heat units in the solar-heating example',
      question='Correct the specific-heat unit to J/(kg·°C), and write the first line as Q/(mc)?',
      recommendation='Yes. Keep 1670 and the stated 162 °C result; change the unit and make the denominator grouping explicit.',
      evidence='Section 11.10, “Solar Electric Generating System,” part (c): the denominator currently contains (0.251 kg)(1670 J·kg/°C). Specific heat must divide by mass for Q/(mc) to have temperature units. The first line Q/mc is also visually ambiguous.',
      check='1130 × 60.0 / (0.251 × 1670) = 161.748… °C, which rounds to the existing 162 °C.',
      proposed='<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mi>Δ</mi><mi>T</mi><mo>=</mo><mfrac><mi>Q</mi><mrow><mi>m</mi><mi>c</mi></mrow></mfrac><mo>=</mo><mfrac><mrow><mo>(</mo><mn>1130</mn><mtext> W</mtext><mo>)</mo><mo>(</mo><mn>60.0</mn><mtext> s</mtext><mo>)</mo></mrow><mrow><mo>(</mo><mn>0.251</mn><mtext> kg</mtext><mo>)</mo><mo>(</mo><mn>1670</mn><mspace width="0.167em"/><mfrac><mtext>J</mtext><mrow><mtext>kg</mtext><mo>·</mo><mtext>°C</mtext></mrow></mfrac><mo>)</mo></mrow></mfrac><mo>≈</mo><mn>162</mn><mtext> °C</mtext></mrow></math>'),
 dict(id='D2',members=['m52466-0102'],title='Missing cube in the nuclear-density unit conversion',
      question='Cube the entire femtometre-to-metre conversion factor?',
      recommendation='Yes. Add an exponent 3 to the whole factor (1 fm / 10⁻¹⁵ m); retain the existing 2.3 × 10¹⁷ kg/m³ result.',
      evidence='Section 14.4, “How Small and Dense Is a Nucleus?”, part (b): the preceding density is 0.138 u/fm³, but the displayed length-conversion factor has no cube. One power leaves the units incorrect and cannot yield the stated result.',
      check='0.138 × 1.66×10⁻²⁷ × (10¹⁵)³ = 2.2908×10¹⁷ kg/m³, consistent with the existing rounded result.',
      proposed='<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mo>(</mo><mn>0.138</mn><mspace width="0.167em"/><mfrac><mtext>u</mtext><msup><mtext>fm</mtext><mn>3</mn></msup></mfrac><mo>)</mo><mo>(</mo><mn>1.66</mn><mo>×</mo><msup><mn>10</mn><mn>−27</mn></msup><mspace width="0.167em"/><mfrac><mtext>kg</mtext><mtext>u</mtext></mfrac><mo>)</mo><msup><mrow><mo>(</mo><mfrac><mrow><mn>1</mn><mtext> fm</mtext></mrow><mrow><msup><mn>10</mn><mn>−15</mn></msup><mtext> m</mtext></mrow></mfrac><mo>)</mo></mrow><mn>3</mn></msup></mrow></math>')]

decision_ids={i:d['id'] for d in decisions for i in d['members']}
mechanical={'numeric-text-near-operator','split-decimal','number-in-operator','function-typography'}
records=[]
for f in findings:
    rules={h['rule'] for h in f['hits']}
    if f['id'] in decision_ids:
        route='maintainer-decision';reason='Potential mathematical/unit correction, not just typography.'
    elif f['id']=='m52479-0070':
        route='already-addressed';reason='Uranium-235/mol factor changed by a separate explicit user request after this audit snapshot.'
    elif rules & mechanical or any(h['rule']=='symbol-in-nonoperator-token' and h['confidence']=='high' for h in f['hits']):
        route='mechanical-review';reason='Normalize token types or numeric fragments while preserving values, operators, unary signs, and grouping; verify rendering before any eventual fix.'
    elif 'mixed-text-and-math-token' in rules:
        route='contextual-technical-review';reason='Distinguish compound unit labels, signed values, and genuine embedded arithmetic. Preserve established notation; escalate only if meaning is ambiguous.'
    elif 'operator-at-nested-group-edge' in rules or 'explicit-edge-form-between-operands' in rules:
        route='contextual-technical-review';reason='Inspect whether the sign is unary or binary and whether the grouping changes browser spacing. Not an automatic spacing change.'
    else:
        route='preserve-unless-rendering-defect';reason='Only manual spacing or conventional non-arithmetic symbols were flagged. Keep existing layout/notation unless visual evidence shows a defect.'
    records.append(dict(id=f['id'],section=f['section'],source_id=f['source_id'],route=route,decision=decision_ids.get(f['id']),reason=reason,rules=sorted(rules)))
counts=dict(collections.Counter(r['route'] for r in records))
assert len(records)==1133 and len({r['id'] for r in records})==1133
assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in before.items())
result=dict(snapshot='audit.json; 1133 original expression candidates',counts=counts,decisions=decisions,records=records,
 limitations='Triage routes are not a claim that all 1133 expressions were individually browser-verified. Unique suspicious token patterns and grouped-operator contexts were inspected; mechanical cases still require technical and rendering checks before edits. Additional semantic ambiguities discovered during those checks will be escalated. No source changes are approved by this report.',source_unchanged=True)
(OUT/'triage.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
esc=html.escape
cards=[]
for d in decisions:
    f=by_id[d['members'][0]]
    cards.append(f'<article><h2>{d["id"]}: {esc(d["title"])}</h2><p>{esc(d["evidence"])}</p><h3>Current expression</h3><div class="formula">{f["rendered"]}</div><h3>Proposed mathematical correction — not applied</h3><div class="formula">{d["proposed"]}</div><p><b>Decision:</b> {esc(d["question"])}</p><p><b>Recommendation:</b> {esc(d["recommendation"])}</p><p><b>Arithmetic check:</b> {esc(d["check"])}</p><a href="{esc(f["url"])}" target="_blank">Read textbook context</a><details><summary>Source evidence</summary><pre>{esc(f["source_xml"])}</pre></details></article>')
page='''<!doctype html><meta charset="utf-8"><title>Math audit: decisions for review</title><style>body{font:18px/1.55 system-ui;background:#f3f7f7;color:#18343d;max-width:1080px;margin:36px auto;padding:0 24px}article{background:white;border:1px solid #cbd8dc;padding:24px;margin:28px 0}h2{font-size:24px}h3{font-size:18px}.formula{overflow:auto;padding:22px 6px;font-size:23px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:13px monospace}table{border-collapse:collapse}td,th{padding:8px 18px;border:1px solid #cbd8dc;text-align:left}a{color:#126981}</style><h1>Two decisions from the math audit</h1><p>No textbook changes have been made during triage. Both decisions concern dimensional consistency; they are grouped here because they change mathematical content, not merely operator spacing.</p><p>The earlier estimate of 20–50 maintainer decisions was too high. Most flags are technical markup issues or intentional notation. These are the two substantive questions identified in this pass; later technical checks could uncover more.</p>'''+''.join(cards)
page+='<h2>Disposition of all 1,133 candidates</h2><table><tr><th>Route</th><th>Expressions</th></tr>'+''.join(f'<tr><td>{esc(k)}</td><td>{v}</td></tr>' for k,v in counts.items())+'</table>'
page+='''<h2>Grouped policies already settled</h2><ul><li>Repair obvious operator/number markup without changing signs, values, exponents, or grouping.</li><li>Keep unary signs tight. Preserve degree signs, percentages, particle charge/excitation labels, and compact unit slashes unless there is an actual defect.</li><li>Preserve explicit table alignment and purposeful spaces. A flagged override alone is not an error.</li><li>Reuse already approved treatment of independent annotations and over-wide calculations; bring back any new editorial tradeoff.</li></ul><p>The mechanical and contextual routes still require technical checks before edits; they are not blanket repair approvals. No claim is made that every candidate has been individually visually verified.</p><p><a href="review.html">Full original audit</a> · <a href="triage.json">Complete per-expression triage ledger</a></p>'''
(OUT/'decisions.html').write_text(page,encoding='utf-8')
(OUT/'TRIAGE.md').write_text('# Operator audit triage\n\nNo textbook edits. Two maintainer decisions, both dimensional-consistency corrections.\n\n'+ '\n\n'.join('## '+d['id']+': '+d['title']+'\n\n'+d['question']+'\n\nRecommendation: '+d['recommendation']+'\n\n'+d['check'] for d in decisions)+'\n\n## Routing counts\n\n'+json.dumps(counts,indent=2)+'\n\n'+result['limitations']+'\n',encoding='utf-8')
print(json.dumps(counts));print('Maintained files unchanged; all 1133 candidates assigned a route.')
