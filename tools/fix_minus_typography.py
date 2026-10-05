"""Audited minus-sign typography; preserve historical source and non-minus dashes."""
from pathlib import Path
import re,json,hashlib,xml.etree.ElementTree as E,collections
ROOT=Path(__file__).resolve().parents[1];M='{http://www.w3.org/1998/Math/MathML}'
pat=re.compile(r'<(?:m:)?(mo|mn|mi|mtext|ms)\b[^>]*?(?:/>|>([^<]*)</(?:m:)?\1>)')
bad=re.compile(r'[-‐‑‒–—﹣－]');report=[];changed=[]
lp=ROOT/'maintained/editorial-changes.json';ledger=json.loads(lp.read_text(encoding='utf8'))
prose={'m42674':[('is –1 for','is −1 for'),('from –2 to –1','from −2 to −1'),('is –1 before','is −1 before')],'m52384':[('of – 30.0 nC','of −30.0 nC')],'m52454':[('say –1.3','say −1.3')],'m67134':[('about –2.','about −2.'),('length –10.0 cm','length −10.0 cm')],'m67622':[('Ice (average, -50°C to 0°C)','Ice (average, −50°C to 0°C)')]}
for p in sorted((ROOT/'maintained/modules').glob('*/index.cnxml')):
 existing=ROOT/'proposals/author-corrections'/('MINUS-TYPOGRAPHY-'+p.parent.name+'.json');before=json.loads(existing.read_text(encoding='utf8'))['before'] if existing.exists() else p.read_text(encoding='utf8');r=E.fromstring(before);parents={c:e for e in r.iter() for c in e};tokens=[e for e in r.iter() if e.tag in [M+t for t in ('mo','mn','mi','mtext','ms')]];hits=list(pat.finditer(before));assert len(hits)==len(tokens),(p,len(hits),len(tokens));edits=[]
 for hit,e in zip(hits,tokens):
  if not bad.search(e.text or ''):continue
  old=e.text;parent=parents[e];ancestor=e
  while not ancestor.get('id') and ancestor in parents:ancestor=parents[ancestor]
  math=e
  while math.tag!=M+'math':math=parents[math]
  context=' '.join(''.join(x.text or '' for x in math.iter() if x.tag in [M+t for t in ('mo','mn','mi','mtext','ms')]).split())
  if parent.tag==M+'mover' and list(parent)[-1] is e:reason='preserve-overbar';new=old
  elif p.parent.name=='m67039' and old=='–' and ''.join(parent.itertext()) in ('x–net','y–net'):reason='preserve-subscript-label-separator';new=old
  elif '–' in old or (e.tag==M+'mo' and old.strip()=='-'):
   reason='correct-minus';new=bad.sub('−',old)
  else:reason='preserve-word-or-value-unit-hyphen';new=old
  report.append(dict(module=p.parent.name,source_object=ancestor.get('id'),tag=hit[1],before=old,after=new,disposition=reason,context=context))
  if new!=old:edits.append((hit.start(2),hit.end(2),new))
 after=before
 for a,b,t in reversed(edits):after=after[:a]+t+after[b:]
 for a,b in prose.get(p.parent.name,[]):
  assert after.count(a)==1,(p,a);after=after.replace(a,b);report.append(dict(module=p.parent.name,before=a,after=b,disposition='correct-prose-minus'))
 if after==before:continue
 ar=E.fromstring(after);assert [e.get('id') for e in r.iter()]==[e.get('id') for e in ar.iter()]
 # All math structure, attributes, and annotation content are unchanged.
 assert [(e.tag,e.attrib) for e in r.iter()]==[(e.tag,e.attrib) for e in ar.iter()]
 assert [e.text for e in r.iter(M+'annotation')]==[e.text for e in ar.iter(M+'annotation')]
 rid='MINUS-TYPOGRAPHY-'+p.parent.name;rp=ROOT/'proposals/author-corrections'/f'{rid}.json';rel=rp.relative_to(ROOT).as_posix();assert rel not in ledger['changes']
 record=dict(id=rid,status='applied-maintainer-approved',target_release='cp2e-ver1.1',module=p.parent.name,source_path=p.relative_to(ROOT).as_posix(),source_sha256=hashlib.sha256(before.encode()).hexdigest(),after_sha256=hashlib.sha256(after.encode()).hexdigest(),before=before,after=after,reason='Book-wide audited minus typography: correct arithmetic/negative-number/charge signs; preserve bars, label separators, compound hyphens, values, MathML structure and annotations.')
 rp.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8');p.write_text(after,encoding='utf8');ledger['changes'].append(rel);changed.append(p.parent.name)
lp.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
out=ROOT/'reports/1.1/minus-sign-audit';out.mkdir(exist_ok=True);summary=dict(modules_changed=changed,dispositions=dict(collections.Counter(x['disposition'] for x in report)),items=report,followups=[dict(module='m42542',source_object='import-auto-id2719096',note='Existing exercise has a negative base in 4.48 × (−10)^(−19), an apparent source math issue distinct from typography. Sign glyph corrected but mathematical value unchanged; review during Chapter 13 exercise revision.')]);(out/'applied-audit.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(len(changed),'modules',summary['dispositions'])
