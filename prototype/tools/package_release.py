"""Assemble a static release candidate using a strict public-file allowlist."""
from pathlib import Path
import json,hashlib,shutil,zipfile,html
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
root=Path(__file__).resolve().parents[2];rel=json.loads((root/'metadata/release.json').read_text(encoding='utf-8'))
base=root/'output/releases'/rel['release_id'];src=base/'site';public=base/'public';public.mkdir(exist_ok=True)
allowed=['index.html','style.css','copy-math.js']
allowed += [p.relative_to(src).as_posix() for folder in ('sections','exercises','media','source','contents') for p in (src/folder).rglob('*') if p.is_file()]
for name in allowed:
 p=src/name;target=public/name;target.parent.mkdir(parents=True,exist_ok=True)
 if p.suffix=='.html':
  data=p.read_text(encoding='utf-8');canonical=rel['public_origin']+'/'+('' if name=='index.html' else name.removesuffix('index.html'))
  data=data.replace('</head>','<link rel="canonical" href="'+html.escape(canonical,quote=True)+'"></head>')
  assert not any(x in data for x in ['prototype-notice','Fidelity prototype','author-approved','Labels are provisional','review-items/']),name
  target.write_text(data,encoding='utf-8',newline='\n')
 else:shutil.copyfile(p,target)
shutil.copyfile(base/rel['pdf_filename'],public/rel['pdf_filename'])
# Prefix rule covers this PDF and future cp2e release downloads without wildcards.
robots='# Keep release downloads out of compliant crawlers; HTML pages remain crawlable.\nUser-agent: *\nDisallow: /cp2e-\n'
(public/'robots.txt').write_text(robots,encoding='utf-8',newline='\n')
from urllib.robotparser import RobotFileParser
robot_policy=RobotFileParser();robot_policy.parse(robots.splitlines())
assert not robot_policy.can_fetch('ExampleCrawler',rel['public_origin']+'/'+rel['pdf_filename'])
assert robot_policy.can_fetch('ExampleCrawler',rel['public_origin']+'/sections/gravitation/')
(base/'UPLOAD-INSTRUCTIONS.txt').write_text(
 'Introduction to Physics — '+rel['release_id']+'\n\n'
 'Extract '+rel['site_archive_filename']+' directly into the webroot for intro.coaphys.xyz.\n'
 'Alternatively, extract locally and upload all extracted files and folders, keeping their structure.\n'
 'index.html and robots.txt must be directly in the webroot, not inside a release folder.\n'
 'The ZIP itself and this instruction file do not need to be uploaded.\n\n'
 'This is a static site: no PHP, build tools, database, URL rewrites, or custom .htaccess are required.\n'
 'Standard Apache DirectoryIndex index.html and PDF MIME handling are sufficient.\n'
 'Download PDF in the navigation, including on the home page, links to '+rel['pdf_filename']+'.\n\n'
 'After uploading, check:\n'
 '  '+rel['public_origin']+'/\n'
 '  '+rel['public_origin']+'/contents/\n'
 '  '+rel['public_origin']+'/robots.txt\n'
 '  '+rel['public_origin']+'/'+rel['pdf_filename']+'\n'
 'Open a chapter, follow a section link, and check an equation and image.\n\n'
 'robots.txt asks all compliant crawlers to avoid root paths beginning /cp2e-, including release PDFs.\n'
 'It leaves the HTML textbook crawlable. It is not access control: bots can ignore it, and readers\n'
 'can still download the PDF. Enforced bandwidth limits require hosting/CDN controls.\n',
 encoding='utf-8',newline='\n')
(public/'release.json').write_text(json.dumps({'release_id':rel['release_id'],'title':rel['title'],'status':rel['status'],'numbering':rel['public_numbering_label'],'numbering_creates_separate_release':False},indent=2)+'\n',encoding='utf-8',newline='\n')
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag in ('a','link','script','img'):
   v=a.get('href') if tag in ('a','link') else a.get('src')
   if v:self.links.append(v)
pages={}
for p in public.rglob('*.html'):
 parser=Page();parser.feed(p.read_text(encoding='utf-8'));assert len(parser.ids)==len(set(parser.ids)),p;pages[p.resolve()]=parser
checked=0
for p,parser in pages.items():
 for link in parser.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  target=(p.parent/unquote(u.path)).resolve() if u.path else p
  if target.is_dir():target=target/'index.html'
  assert target.is_file(),(p,link)
  if u.fragment and target.suffix=='.html':assert unquote(u.fragment) in pages[target].ids,(p,link)
  checked+=1
manifest={'release_id':rel['release_id'],'title':rel['title'],'status':'release-candidate','publication_ready':False,'numbering_profile':rel['default_numbering_profile'],'numbering_policy':rel['numbering_policy'],'pdf_sha256':hashlib.sha256((base/rel['pdf_filename']).read_bytes()).hexdigest(),'renderer_lock_sha256':hashlib.sha256((root/'metadata/render-environment.lock.json').read_bytes()).hexdigest(),'source_sha256':json.loads((src/'build-manifest.json').read_text(encoding='utf-8'))['source_sha256'],'static_pages':len(pages),'local_links_checked':checked,'files':{p.relative_to(public).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(public.rglob('*')) if p.is_file()}}
(base/'artifact-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
with zipfile.ZipFile(base/rel['site_archive_filename'],'w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(public.rglob('*')):
  if p.is_file():
   info=zipfile.ZipInfo(p.relative_to(public).as_posix(),date_time=(1980,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,p.read_bytes())
 info=zipfile.ZipInfo('artifact-manifest.json',date_time=(1980,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,(base/'artifact-manifest.json').read_bytes())
(root/'reports/release-package-validation.json').write_text(json.dumps({k:v for k,v in manifest.items() if k!='files'},indent=2)+'\n',encoding='utf-8',newline='\n')
(base/'SHA256SUMS.txt').write_text(''.join(hashlib.sha256((base/name).read_bytes()).hexdigest()+'  '+name+'\n' for name in [rel['pdf_filename'],rel['site_archive_filename'],'artifact-manifest.json']),encoding='utf-8',newline='\n')
print(json.dumps({'pages':len(pages),'links':checked,'pdf':str(base/rel['pdf_filename']),'archive':str(base/rel['site_archive_filename'])}))
