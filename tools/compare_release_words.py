"""Reproducible section-prose comparison against the published 1.0 source tag."""
import difflib, hashlib, io, json, re, subprocess, tarfile, unicodedata
from pathlib import Path
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'reports/1.1/revision-word-counts'; OUT.mkdir(parents=True,exist_ok=True)
raw=subprocess.check_output(['git','--git-dir='+str(ROOT/'tmp/v1.0-comparison.git'),'archive','cp2e-ver1.0','maintained/modules'])
with tarfile.open(fileobj=io.BytesIO(raw)) as tf:
    baseline={m.name:tf.extractfile(m).read() for m in tf.getmembers() if m.isfile() and m.name.endswith('/index.cnxml')}
release=json.loads((ROOT/'metadata/releases/cp2e-ver1.0.json').read_text())
expected=release['source_provenance']['maintained_module_sha256']
ns='{http://cnx.rice.edu/cnxml}'
skip={'glossary','metadata','math','media','image','audio','video','label','attribution'}
classes={'section-summary','conceptual-questions','problems-exercises','problem-exercises'}
def prose(e):
    tag=e.tag.split('}')[-1]
    if tag in skip or classes.intersection(e.get('class','').split()) or e.get('type') in classes: return ' '
    title=e.find(ns+'title')
    if tag=='section' and title is not None and ''.join(title.itertext()).strip() in {'Section Summary','Conceptual Questions','Problems & Exercises'}: return ' '
    text=(e.text or '')+''.join(prose(c)+(c.tail or '') for c in e)
    return (' '+text+' ') if tag in {'para','item','entry','row','title','caption','section','note','example','problem','solution'} else text
pattern=re.compile(r"[^\W_]+(?:['’][^\W_]+)*",re.UNICODE)
def words(data):
    root=ET.fromstring(data)
    # Body only: excludes metadata objectives, section title and relocated review material.
    s=prose(root.find(ns+'content'))
    return pattern.findall(unicodedata.normalize('NFKC',s).replace('’',"'").casefold())
rows=[]
for sec in json.loads((ROOT/'maintained/sections.json').read_text())['sections']:
    path=sec['source']; mid=sec['id'].split(':')[-1]
    if path not in baseline: continue
    old=baseline[path]; current=(ROOT/path).read_bytes()
    assert hashlib.sha256(old).hexdigest()==expected[mid],mid
    htmlpath=ROOT/'prototype/dist/course-full/sections'/sec['slug']/'index.html'
    if not htmlpath.exists(): continue
    html=htmlpath.read_text(encoding='utf-8')
    match=re.search(r'<p class="eyebrow">([^<]+)</p>',html)
    label=match.group(1) if match else ''
    if not re.fullmatch(r'\d+\.\d+',label): continue
    a,b=words(old),words(current)
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
    added=sum(j2-j1 for tag,i1,i2,j1,j2 in sm.get_opcodes() if tag in {'insert','replace'})
    rows.append(dict(section=label,title=sec['title'],module=mid,slug=sec['slug'],old_words=len(a),current_words=len(b),new_words=added,percent=100*added/len(b) if b else 0,old_sha256=hashlib.sha256(old).hexdigest(),current_sha256=hashlib.sha256(current).hexdigest()))
rows.sort(key=lambda x:x['percent'],reverse=True)
(OUT/'results.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for row in rows[:15]: print(row['section'],row['title'],row['new_words'],row['current_words'],round(row['percent'],2))
print('Sections compared:',len(rows))
