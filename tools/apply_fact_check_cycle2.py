"""Apply approved cycle-2 XML patches with reversible editorial records. Dry run by default."""
from pathlib import Path
import json,re,collections,hashlib,xml.etree.ElementTree as E,sys
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'proposals/1.1/fact-check-cycle2.json';d=json.loads(P.read_text(encoding='utf-8'))
ledger=json.loads((ROOT/'maintained/editorial-changes.json').read_text(encoding='utf-8'));files={};records=[]
def sha(s):return hashlib.sha256(s.encode()).hexdigest()
def block(s,ident):
 m=re.search(r'<([\w:-]+)\b[^>]*\sid="'+re.escape(ident)+r'"[^>]*>',s);assert m,ident
 if m[0].endswith('/>'):return m[0]
 depth=1
 for t in re.finditer(r'</?'+re.escape(m[1])+r'\b[^>]*>',s[m.end():]):
  if t[0].startswith('</'):depth-=1
  elif not t[0].endswith('/>'):depth+=1
  if depth==0:return s[m.start():m.end()+t.end()]
 raise ValueError(ident)
def parse(s):return E.fromstring('<wrap xmlns="http://cnx.rice.edu/cnxml" xmlns:m="http://www.w3.org/1998/Math/MathML">'+s+'</wrap>')[0]
def sig(e):return(e.tag,dict(e.attrib),re.sub(r'\s+',' ',e.text or '').strip(),[(sig(c),re.sub(r'\s+',' ',c.tail or '').strip()) for c in e])
def pat(s):
 s=re.sub(r' xmlns(?::\w+)?="[^"]+"','',s)
 return ''.join(r'\s*/>' if p=='/>' else r'\s*' if p.isspace() else re.escape(p) for p in re.split(r'(\s+|/>)',s))
for i in d['items']:
 assert i['status']=='approved-pending-application',i['id']
 starts={}
 for p in [i]+i.get('related_passages',[]):
  path=p.get('source_path',i['source_path']);s=files.get(path,(ROOT/path).read_text(encoding='utf-8'));starts.setdefault(path,s)
  ident=p.get('source_id') or p['anchor'];old=block(s,ident);sel=p.get('source_selector')
  if p.get('attribute_edit'):
   a=p['attribute_edit'];old=block(s,a['source_id']);assert a['before'] in old;new=old.replace(a['before'],a['after'],1)
  elif p.get('source_insertion_xml'):
   pattern=pat(p['source_insertion_after_xml']);matches=list(re.finditer(pattern,old));assert len(matches)==1
   m=matches[0];new=old[:m.end()]+'\n'+p['source_insertion_xml']+old[m.end():]
  elif sel=='caption':
   m=re.search(r'<caption\b[^>]*>.*?</caption>',old,re.S);assert m
   assert sig(parse(m[0]))==sig(parse(p['before_xml'])),(i['id'],ident)
   new=old[:m.start()]+p['proposed_xml']+old[m.end():]
  else:
   assert sig(parse(old))==sig(parse(p['before_xml'])),(i['id'],ident)
   new=p['proposed_xml']
  assert s.count(old)==1;s=s.replace(old,new,1);E.fromstring(s);files[path]=s
 # Insert new definitions in declared order after an existing stable glossary entry.
 if i.get('glossary_insertions'):
  path=i['source_path'];s=files[path];anchor=i['glossary_insertions'][0]['after_id'];old=block(s,anchor);s=s.replace(old,old+'\n'+ '\n'.join(x['xml'] for x in i['glossary_insertions']),1);files[path]=s
 i['application_records']=[]
 for path,original in starts.items():
  s=files[path];E.fromstring(s)
  oldids=set(re.findall(r'\bid="([^"]+)"',original));newids=re.findall(r'\bid="([^"]+)"',s)
  assert oldids<=set(newids),(i['id'],'lost IDs',oldids-set(newids));assert all(v<=max(1,collections.Counter(re.findall(r'\bid="([^"]+)"',original))[k]) for k,v in collections.Counter(newids).items()),(i['id'],'new duplicate IDs')
  n=0
  while n<min(len(original),len(s)) and original[n]==s[n]:n+=1
  z=0
  while z<min(len(original),len(s))-n and original[-1-z]==s[-1-z]:z+=1
  before=original[n:len(original)-z if z else None];after=s[n:len(s)-z if z else None]
  while not before or original.count(before)!=1:
   n=max(0,n-100);z=max(0,z-100);before=original[n:len(original)-z if z else None];after=s[n:len(s)-z if z else None]
  mid=Path(path).parent.name;rid=i['id'] if len(starts)==1 else i['id']+'-'+mid;rp='proposals/author-corrections/'+rid+'.json';assert not (ROOT/rp).exists()
  record=dict(id=rid,status='applied-author-directed',target_release='cp2e-ver1.1',module=mid,source_path=path,source_sha256=sha(original),after_sha256=sha(s),before=before,after=after,reason=i['title'],authorization=i['authorization'],sources=i['sources'],review_packet='proposals/1.1/fact-check-cycle2.json')
  records.append((rp,record));i['application_records'].append(rp)
print('Validated',len(d['items']),'items,',len(records),'records across',len(files),'modules; existing IDs retained.')
if '--apply' not in sys.argv:sys.exit()
for path,s in files.items():(ROOT/path).write_text(s,encoding='utf-8',newline='\n')
for rp,r in records:
 (ROOT/rp).write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n');ledger['changes'].append(rp)
(ROOT/'maintained/editorial-changes.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
for i in d['items']:
 i['status']='applied-author-directed'
 for p in i.get('related_passages',[]):
  if p.get('status'):p['status']='applied-author-directed'
 i['revision_note']=i.get('revision_note','')+' Applied with author approval on 2026-09-21; earlier draft-only notes describe review history.'
d['applied_source_sha256']={p:sha(s) for p,s in files.items()};d['status']='Priority-1 cycle-2 corrections and glossary alignment applied; numerical audit and exercise revision remain separate.';d['applied_date']='2026-09-21'
P.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
