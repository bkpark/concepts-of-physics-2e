"""Prepare exact, reversible preview overlays for approved HE01–HE08."""
from pathlib import Path
import json,re,xml.etree.ElementTree as E,hashlib
ROOT=Path(__file__).resolve().parents[1];C='http://cnx.rice.edu/cnxml';M='http://www.w3.org/1998/Math/MathML';E.register_namespace('',C);E.register_namespace('m',M)
p=ROOT/'maintained/modules/m67127/index.cnxml';root=E.parse(p).getroot();ids={e.get('id'):e for e in root.iter() if e.get('id')};packet=json.loads((ROOT/'proposals/1.1/heat-engine-review.json').read_text(encoding='utf-8'));patches=[]
def xml(id):return E.tostring(ids[id],encoding='unicode').strip()
def body(id):return xml(id).split('>',1)[1].rsplit('</',1)[0]
def proposed(group,id):return next(c['proposed_text'] for i in packet['items'] if i['id']==group for c in i['changes'] if c['source_id']==id)
def put(group,id,content):
 e=ids[id];after='<'+e.tag.split('}')[-1]+' xmlns="'+C+'" xmlns:m="'+M+'" id="'+id+'">'+content+'</'+e.tag.split('}')[-1]+'>';E.fromstring(after)
 patches.append(dict(item=group,module='m67127',source_id=id,source_path=str(p.relative_to(ROOT)),source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),before_xml=xml(id),proposed_xml=after,status='approved-pending-section-preview'))
def replace(group,id,a,b):
 old=body(id);assert a in old,(id,a);put(group,id,old.replace(a,b))
def math(s):return '<m:math>'+s+'</m:math>'
def power(a,n):return '<m:mn>'+a+'</m:mn><m:mo>×</m:mo><m:msup><m:mn>10</m:mn><m:mn>'+str(n)+'</m:mn></m:msup>'
def qty(a,n,unit):return '<m:mrow>'+power(a,n)+'<m:mspace width="0.2em"/><m:mtext>'+unit+'</m:mtext></m:mrow>'
replace('HE01','import-auto-id1169738147207','where one gets hotter and the other gets colder','where the hotter one gets hotter and the colder one gets colder')
second=proposed('HE02','eip-id1423437');put('HE02','eip-id1423437',second)
old=body('import-auto-id1169738234744');put('HE02','import-auto-id1169738234744',old[:old.index('(ii)')]+ '(ii) '+second+old[old.index(' These expressions'):])
put('HE02','fs-id1169738014671',proposed('HE02','fs-id1169738014671'))
replace('HE03','import-auto-id1169737992344','in all processes','in a heat-engine cycle')
old=body('import-auto-id1169737966671');put('HE03','import-auto-id1169737966671','In a heat engine, only part of the heat input is converted to work. '+old[old.index('We define'):])
qh=math('<m:msub><m:mi>Q</m:mi><m:mi mathvariant="normal">h</m:mi></m:msub>');qc=qh.replace('>h<','>c<')
old=body('import-auto-id1169738014694');start=old.index('Note that all');end=old.index(' The direction',start);put('HE03','import-auto-id1169738014694',old[:start]+'Here '+qh+' and '+qc+' are positive amounts of heat transfer.'+old[end:])
co2=math('<m:msub><m:mtext>CO</m:mtext><m:mn>2</m:mn></m:msub>')
reaction=math('<m:mrow><m:mtext>C</m:mtext><m:mo>+</m:mo><m:msub><m:mtext>O</m:mtext><m:mn>2</m:mn></m:msub><m:mo>→</m:mo><m:msub><m:mtext>CO</m:mtext><m:mn>2</m:mn></m:msub></m:mrow>')
old=body('import-auto-id1169737780262');put('HE04','import-auto-id1169737780262',old[:old.index('(c)')]+'(c) For a simplified estimate, treat the fuel as pure carbon, releasing '+math(qty('3.3',7,'J/kg'))+' when burned completely to '+co2+'. The reaction '+reaction+' produces 44 kg of '+co2+' for every 12 kg of carbon. How much '+co2+' is emitted per day in this model?')
put('HE04','eip-825','In the pure-carbon model, the daily consumption of carbon is calculated using the information that each day there is '+math(qty('2.50',14,'J'))+' of heat transfer from combustion. The reaction '+reaction+' produces 44 kg of '+co2+' for every 12 kg of carbon.')
put('HE04','eip-238','The daily carbon consumption is')
put('HE04','eip-792',math('<m:mrow><m:mfrac>'+qty('2.50',14,'J')+qty('3.3',7,'J/kg')+'</m:mfrac><m:mo>=</m:mo>'+qty('7.6',6,'kg')+'<m:mtext>.</m:mtext></m:mrow>'))
put('HE04','import-auto-id1169737739559','For complete combustion of this carbon, the carbon dioxide produced per day is')
put('HE04','eip-975',math('<m:mrow>'+qty('7.6',6,'kg carbon')+'<m:mo>×</m:mo><m:mfrac><m:mrow><m:mn>44</m:mn><m:mspace width="0.2em"/><m:mtext>kg</m:mtext><m:mspace width="0.2em"/><m:msub><m:mtext>CO</m:mtext><m:mn>2</m:mn></m:msub></m:mrow><m:mtext>12 kg carbon</m:mtext></m:mfrac><m:mo>=</m:mo>'+power('2.8',7)+'<m:mspace width="0.2em"/><m:mtext>kg</m:mtext><m:mspace width="0.2em"/><m:msub><m:mtext>CO</m:mtext><m:mn>2</m:mn></m:msub><m:mtext>.</m:mtext></m:mrow>'))
put('HE04','import-auto-id1169738213149',proposed('HE04','import-auto-id1169738213149').replace('CO₂',co2))
put('HE05','eip-567',proposed('HE05','eip-567').replace('CO₂',co2))
old=body('import-auto-id1169736614771');put('HE06','import-auto-id1169736614771',old[:old.index('The four steps shown')]+'The four steps shown complete the engine’s operating cycle, replacing the exhaust gases with a fresh gasoline-air mixture.')
old=body('import-auto-id1169737933345');link=re.search(r'<link\b[^>]*/>',old)[0];put('HE06','import-auto-id1169737933345',proposed('HE06','import-auto-id1169737933345').replace('the figure',link).replace('Otto cycle', '<term id="import-auto-id1169737845754">Otto cycle</term>',1))
old=body('import-auto-id1169738110852');put('HE06','import-auto-id1169738110852',old[:old.index('In an internal combustion engine, this process corresponds')]+ 'In an internal combustion engine, this part of the model represents the exhaust of hot gases and the intake of a cooler air-gasoline mixture. The actual engine carries energy out with the exhaust; the ideal cycle represents this by heat transfer from the gas.')
old=body('import-auto-id1169736654385');link=re.search(r'<link\b[^>]*/>',old)[0];put('HE07','import-auto-id1169736654385',proposed('HE07','import-auto-id1169736654385').replace('[existing figure reference]',link))
for id in ['fs-id1169737907449','fs-id1169737949805']:put('HE08',id,proposed('HE08',id))
# Paragraph/equation IDs and any nested referenced IDs must survive.
for patch in patches:
 before={e.get('id') for e in E.fromstring(patch['before_xml']).iter() if e.get('id')};after={e.get('id') for e in E.fromstring(patch['proposed_xml']).iter() if e.get('id')};assert before<=after,(patch['source_id'],before-after)
assert round(2.5e14/3.3e7/1e6,1)==7.6
assert round((2.5e14/3.3e7)*(44/12)/1e7,1)==2.8
(ROOT/'proposals/1.1/heat-engine-preview-patches.json').write_text(json.dumps(dict(status='HE01–HE08 approved; preview-only overlays',patches=patches),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Prepared',len(patches),'source-preserving HE overlays.')
