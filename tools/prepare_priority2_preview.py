"""Prepare reversible priority-2 XML proposals and apply only approved P2-06 on request."""
from pathlib import Path
import json,re,hashlib,xml.etree.ElementTree as E,sys,html
ROOT=Path(__file__).resolve().parents[1]
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def save(p,d):(ROOT/p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
def sha(s):return hashlib.sha256(s.encode()).hexdigest()
def block(s,id):
 m=re.search(r'<([\w:-]+)\b[^>]*\sid="'+re.escape(id)+r'"[^>]*>',s);assert m,id
 depth=1
 for t in re.finditer(r'</?'+re.escape(m[1])+r'\b[^>]*>',s[m.end():]):
  if t[0].startswith('</'):depth-=1
  elif not t[0].endswith('/>'):depth+=1
  if depth==0:return s[m.start():m.end()+t.end()]
 raise ValueError(id)
D=load('proposals/1.1/priority2-review-decisions.json');patches=[]
if all(v['status']=='applied-author-directed' for v in D.values()):
 print('Priority 2 already applied; archived proposals retained.');sys.exit()
files={m:(ROOT/f'maintained/modules/{m}/index.cnxml').read_text(encoding='utf-8') for m in ['m68327','m42649']}
def patch(mid,id,new,item):
 s=files[mid];old=block(s,id);assert old!=new
 files[mid]=s.replace(old,new,1);E.fromstring(files[mid])
 patches.append(dict(item=item,module=mid,source_id=id,before_xml=old,proposed_xml=new))
def replace(mid,id,old,new,item):
 b=block(files[mid],id);assert b.count(old)==1,(id,old);patch(mid,id,b.replace(old,new,1),item)
def table(id,title,rows,note,footid,summary):
 esc=html.escape
 return '<table id="'+id+'" summary="'+esc(summary)+'"><title>'+esc(title)+'<footnote id="'+footid+'">'+note+'</footnote></title><tgroup cols="'+str(len(rows[0]))+'">'+''.join('<colspec colnum="'+str(j+1)+'" colname="c'+str(j+1)+'"/>' for j in range(len(rows[0])))+'<thead><row>'+''.join('<entry>'+esc(c)+'</entry>' for c in rows[0])+'</row></thead><tbody>'+''.join('<row>'+''.join('<entry>'+esc(c)+'</entry>' for c in row)+'</row>' for row in rows[1:])+'</tbody></tgroup></table>'
for item,foot in [('P2-01','eip-id1833605'),('P2-03','eip-id3009353')]:
 t=D[item]['proposed_table'];u=D[item]['sources'][0]
 note=html.escape(t['scope']+' '+t['note'])+' Source: <link url="'+u['url']+'">'+html.escape(u['title'])+'</link>.'
 patch('m68327',t['source_id'],table(t['source_id'],t['title'],t['rows'],note,foot,t['title']),item)
# P2-01 opening paragraph, retaining the real cross-reference.
e=D['P2-01']['proposed_edits'][0]
replace('m68327',e['source_id'],e['before'].replace('[Table reference]','<link target-id="import-auto-id1945981"/>'),e['after'].replace('[Table reference]','<link target-id="import-auto-id1945981"/>'),'P2-01')
# P2-02 suffix, glossary and section summary; preserve all term anchors.
for e in D['P2-02']['proposed_edits']:
 old,new=e['before'],e['after']
 if e['source_id']=='import-auto-id1461313':
  for label,id in [('low dose','import-auto-id2000644'),('moderate dose','import-auto-id2688952'),('high dose','import-auto-id2407214')]:
   old=old.replace(label,'<term id="'+id+'">'+label+'</term>');new=new.replace(label,'<term id="'+id+'">'+label+'</term>')
 replace('m68327',e['source_id'],old,new,'P2-02')
# P2-03 entire background paragraph includes P2-04's approved deletion.
for e in D['P2-03']['proposed_edits']:
 old=e['before'].replace('[Table reference]','<link target-id="import-auto-id1118563"/>');new=e['after'].replace('[Table reference]','<link target-id="import-auto-id1118563"/>')
 replace('m68327',e['source_id'],old,new,'P2-03/P2-04' if e['source_id']=='import-auto-id1462138' else 'P2-03')
for e in D['P2-05']['proposed_edits']:replace('m68327','import-auto-id3154810',e['before'],e['after'],'P2-05')
replace('m68327','import-auto-id1869365','Some immediate radiation effects','Some effects of acute whole-body radiation exposure','P2-01')
replace('m68327','import-auto-id1869365','World-wide average radiation exposure from natural sources, including radon, is about 3 mSv','World-wide average annual effective dose from natural sources, including radon, is about 3 mSv','P2-03')
# P2-06: a deliberately small set of named procedures and label-specific adult activities.
recordpath='proposals/author-corrections/P2-06.json'
if not (ROOT/recordpath).exists():
 start=files['m42649']
 sources=[
 ('DailyMed: DRAXIMAGE MDP-25 (technetium Tc 99m medronate), Dosage and Administration','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3c91d0d8-6cc5-834c-bda0-aa83a873b9fb'),
 ('DailyMed: DRAXIMAGE MAA, section 2.3','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=bbefaa05-1dc0-3ae7-7264-ce1eddf0da2b'),
 ('GE HealthCare: CERETEC prescribing information, section 2.2','https://www.gehealthcare.com/-/jssmedia/GEHC/US/Files/Products/Molecular-Imaging/Ceretec-Cobalt/Ceretec-Cobalt-Prescribing-Information-092018-CERETEC-with-Cobalt-Chloride-BK'),
 ('DailyMed: Sodium Iodide I 123, Dosage and Administration','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=493fa2ab-4eb0-4434-9739-3079b2f0e272'),
 ('DailyMed: Fludeoxyglucose F 18, section 2.1','https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=1deaaa92-1c98-4295-8aa6-7a70bc29f55d')]
 rows=[['Diagnostic use','Radiopharmaceutical','Adult activity (MBq)','Adult activity (mCi)'],['Bone imaging','Tc-99m medronate (MDP)','370–740','10–20'],['Lung perfusion','Tc-99m aggregated albumin (MAA)','37–148','1–4'],['Brain perfusion','Tc-99m exametazime (CERETEC)','555–1110','15–30'],['Thyroid uptake and imaging','Sodium iodide I-123','3.7–14.8','0.1–0.4'],['PET imaging of glucose metabolism','Fludeoxyglucose F-18 (FDG)','185–370','5–10']]
 note='Examples of adult administered activities from the named product labels, not a comprehensive list of imaging protocols. For I-123, the label places uptake-only studies at the lower end and thyroid imaging at the higher end of the range. Activity measures decays per second, not absorbed or effective dose; 1 mCi = 37 MBq. Sources (checked September 2026): '+ '; '.join('<link url="'+u+'">'+html.escape(t)+'</link>' for t,u in sources)+'.'
 patch('m42649','eip-909',table('eip-909','Examples of Diagnostic Radiopharmaceuticals',rows,note,'p2-radiopharmaceutical-sources','Named diagnostic procedures, preparations, and adult administered activities in MBq and mCi.'),'P2-06')
 replace('m42649','import-auto-id1773067','lists certain medical diagnostic uses of radiopharmaceuticals, including isotopes and activities that are typically administered.','lists selected medical diagnostic uses of radiopharmaceuticals, including named preparations and adult activity ranges from their product labels.','P2-06')
 replace('m42649','import-auto-id3004371','lists certain diagnostic uses of radiopharmaceuticals including the isotope and activity typically used in diagnostics.','lists selected diagnostic uses of radiopharmaceuticals, with named preparations and adult activity ranges.','P2-06')
 replace('m42649','eip-316','lists many diagnostic uses','lists several diagnostic uses','P2-06')
 # Remove only the now-inaccurate table pointer in the PET isotope list.
 s=files['m42649'];needle=', as seen in <link target-id="eip-909"/>. This list includes C, N, and O'
 assert s.count(needle)==1
 pos=s.index(needle);pre=s[:pos];id=re.findall(r'<para\b[^>]*id="([^"]+)"',pre)[-1]
 replace('m42649',id,needle,'. This list includes C, N, and O','P2-06')
 # Keep numerical exercise data as hypothetical samples, without implying clinical recommendations.
 replace('m42649','import-auto-id3035339','<link target-id="eip-909"/> indicates that 7.50 mCi of','Consider a sample with an activity of 7.50 mCi of','P2-06')
 replace('m42649','import-auto-id3035339',' is used in a brain scan.','.', 'P2-06')
 replace('m42649','import-auto-id3353285','The activities of','Consider samples of','P2-06')
 replace('m42649','import-auto-id3353285',' used in thyroid scans are given in <link target-id="eip-909"/> to be 50 and',' with activities of 50 and','P2-06')
 replace('m42649','import-auto-id3353285','in such scans','in these samples','P2-06')
 replace('m42649','import-auto-id1488236',', which is used in some heart scans, as seen in <link target-id="eip-909"/>','', 'P2-06')
 replace('m42649','import-auto-id1617247','the needed 5.0-mCi activity','an activity of 5.0 mCi','P2-06')
 D['P2-06']=dict(status='approved-pending-application',title='Named diagnostic radiopharmaceutical examples',review_level='Approved reduced table; full-section reading preview available',findings=['Five named examples replace twenty isotope-only rows; label-specific adult activity ranges are given in MBq and mCi.','The same Tc-99m isotope appears in three different preparations, illustrating how preparation affects diagnostic use. Thyroid and FDG PET examples retain isotope diversity.','Removed-row references in PET prose and numerical exercises are repaired; exercise quantities and calculations are retained as hypothetical samples.'],recommendation='Use the five sourced examples with searchable product-label names and direct source links.',maintainer_review='Reduced scope and implementation approved. Read the full section for flow; no table-scope decision remains.',source_uncertainty='These are specified product-label ranges, not universal or average activities for every protocol. Administered activity is not absorbed or effective dose.',sources=[dict(title=t,url=u,locator='Adult dosage for named indication',checked='2026-09-21') for t,u in sources],proposed_table=dict(source_id='eip-909',title='Examples of Diagnostic Radiopharmaceuticals',scope='Adult label ranges for five specified preparations.',rows=rows,note='1 mCi = 37 MBq. Full source links and scope appear in the textbook table note.'),authorization='Maintainer requested implementation of a smaller set useful to future radiology and allied-health professionals.')
 if '--apply-p206' in sys.argv:
  end=files['m42649'];oldids=set(re.findall(r'\bid="([^"]+)"',start));assert oldids<=set(re.findall(r'\bid="([^"]+)"',end))
  # Full-file replacement is intentionally reversible and validated by the existing ledger verifier.
  rec=dict(id='P2-06',status='applied-author-directed',target_release='cp2e-ver1.1',module='m42649',source_path='maintained/modules/m42649/index.cnxml',source_sha256=sha(start),after_sha256=sha(end),before=start,after=end,reason='Replace isotope-only activity table with five named examples; reconcile references and preserve exercise calculations.',authorization=D['P2-06']['authorization'],sources=D['P2-06']['sources'],review_packet='proposals/1.1/priority2-review-decisions.json')
  save(recordpath,rec);ledger=load('maintained/editorial-changes.json');ledger['changes'].append(recordpath);save('maintained/editorial-changes.json',ledger)
  (ROOT/'maintained/modules/m42649/index.cnxml').write_text(end,encoding='utf-8',newline='\n')
  D['P2-06']['status']='applied-author-directed';D['P2-06']['application_records']=[recordpath]
 save('proposals/1.1/priority2-review-decisions.json',D)
# Overlay only material not already committed to maintained source.
if (ROOT/recordpath).exists():patches=[p for p in patches if p['item']!='P2-06']
save('proposals/1.1/priority2-preview-patches.json',dict(status='Reading preview overlays; P2-06 applied separately. Other priority-2 changes remain staged for coordinated review.',patches=patches,open_checks=[]))
print('Prepared',len(patches),'preview patches; P2-06 applied:',(ROOT/recordpath).exists())
