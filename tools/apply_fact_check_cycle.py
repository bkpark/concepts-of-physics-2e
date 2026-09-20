from pathlib import Path
import json,re,hashlib,xml.etree.ElementTree as E,sys
ROOT=Path(__file__).resolve().parents[1]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf-8'))
def save(p,d):(ROOT/p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
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
def pattern(s):
 parts=re.split(r'(\s+|/>)',s)
 return ''.join(r'\s*/>' if p=='/>' else r'\s*' if p.isspace() else re.escape(p) for p in parts)
packet=load('proposals/1.1/fact-check.json'); ledger=load('maintained/editorial-changes.json'); files={}; records=[]
for i in packet['items']:
 assert i['status']=='approved-pending-application',i['id']
 path=i['source_path'];s=files.get(path,(ROOT/path).read_text(encoding='utf-8')); original=s
 for passage in [i]+i.get('related_passages',[]):
  ident=passage.get('source_id') or passage['anchor'];oldblock=block(s,ident);newblock=oldblock;reference=passage['before_xml']
  for edit in passage['edits']:
   matches=list(re.finditer(pattern(edit['before']),newblock))
   expected=len(list(re.finditer(pattern(edit['before']),reference)))
   assert len(matches)==expected and expected>0,(i['id'],ident,len(matches),expected,edit['before'][:100])
   newblock=re.sub(pattern(edit['before']),lambda m:edit['after'],newblock)
   reference=re.sub(pattern(edit['before']),lambda m:edit['after'],reference)
  assert re.sub(r'\s+', ' ',reference)==re.sub(r'\s+', ' ',passage['proposed_xml']),(i['id'],'proposal differs from edit list')
  assert s.count(oldblock)==1
  s=s.replace(oldblock,newblock,1)
 if i.get('structural_proposal'):
  order=i['structural_proposal'];chunks={id:block(s,id) for id in order['before_order']};starts=[s.index(chunks[id]) for id in order['before_order']];assert starts==sorted(starts)
  for a,b in zip(order['before_order'],order['before_order'][1:]):assert not s[s.index(chunks[a])+len(chunks[a]):s.index(chunks[b])].strip()
  a=starts[0];b=starts[-1]+len(chunks[order['before_order'][-1]])
  s=s[:a]+'\n'.join(chunks[id] for id in order['proposed_order'])+s[b:]
 E.fromstring(s)
 assert sorted(re.findall(r'\bid="([^"]+)"',original))==sorted(re.findall(r'\bid="([^"]+)"',s)),('IDs',i['id'])
 n=0
 while n<min(len(original),len(s)) and original[n]==s[n]:n+=1
 z=0
 while z<min(len(original),len(s))-n and original[-1-z]==s[-1-z]:z+=1
 before=original[n:len(original)-z if z else None];after=s[n:len(s)-z if z else None]
 while not before or original.count(before)!=1:
  n=max(0,n-100);z=max(0,z-100)
  before=original[n:len(original)-z if z else None];after=s[n:len(s)-z if z else None]
 record=dict(id=i['id'],status='applied-author-directed',target_release='cp2e-ver1.1',module=i['module'],source_path=path,source_sha256=sha(original),after_sha256=sha(s),before=before,after=after,reason=i['title'],authorization=i['authorization'],sources=i['sources'],review_packet='proposals/1.1/fact-check.json')
 rp='proposals/author-corrections/'+i['id']+'.json';assert not (ROOT/rp).exists();records.append((rp,record));files[path]=s
print('Validated',len(records),'approved items across',len(files),'modules; all existing IDs retained.')
if '--apply' not in sys.argv:sys.exit()
for path,s in files.items():(ROOT/path).write_text(s,encoding='utf-8',newline='\n')
for rp,r in records:save(rp,r);ledger['changes'].append(rp)
save('maintained/editorial-changes.json',ledger)
for i in packet['items']:
 i['status']='applied-author-directed';i['application_record']='proposals/author-corrections/'+i['id']+'.json'
 if i.get('structural_proposal'):i['structural_proposal']['status']='applied-author-directed'
packet['status']='Approved cycle applied to maintained 1.1 preview; additional factual leads remain open.'
packet['applied_date']='2026-09-20';save('proposals/1.1/fact-check.json',packet)
