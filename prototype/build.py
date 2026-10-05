"""Maintained-source fidelity build; canonical XML is never written.
Run: python prototype/build.py [cnx|course] [--all]
"""
from pathlib import Path
import collections, copy, hashlib, html, json, re, shutil, sys
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'prototype'
PROFILE=sys.argv[1] if len(sys.argv)>1 else 'course'
assert PROFILE in ('cnx','course')
FULL='--all' in sys.argv
RELEASE='--release' in sys.argv
release=json.loads((ROOT/'metadata/release.json').read_text(encoding='utf-8'))
if RELEASE and release.get('artifacts_frozen'):raise SystemExit('Release artifacts are frozen. Use a development build or prepare a new release ID; do not overwrite 1.0.')
OUT=(ROOT/'output/releases'/release['release_id']/'site') if RELEASE else P/'dist'/(PROFILE+'-full' if FULL else PROFILE)
if RELEASE:assert FULL and PROFILE==release['default_numbering_profile']
IDS=['m67034','m67530','m71410','m67122','m67807','m42709']
NS={'c':'http://cnx.rice.edu/cnxml','m':'http://www.w3.org/1998/Math/MathML','md':'http://cnx.rice.edu/mdml'}
esc=lambda s:html.escape(str(s),quote=True)
local=lambda e:e.tag.rsplit('}',1)[-1]
text=lambda e:''.join(e.itertext()).strip() if e is not None else ''
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def dump(path,data):path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
from collection import read_sections
identities=load('maintained/sections.json')['sections']
sections=read_sections(ROOT,identities)
registry={s['module_id']:s for s in sections}
if FULL:IDS=list(registry)
SCOPE=f'{len(IDS)}-module review build'
PUBLIC_NUMBERING='Lecture-aligned numbering (July 2026)' if PROFILE=='course' else 'CNX numbering'
NUMBERING_NOTE='This edition uses the LibreTexts chapter and section numbering preserved in the July 7, 2026 course PDF. It matches the numbering called &ldquo;new LibreTexts chapter and section numbers&rdquo; in the recorded lectures for Physics 10 at College of Alameda. LibreTexts subsequently changed its numbering on September 17, 2026, so its current numbering may differ.'
attributions={a['module_id']:a for a in load('references/cnx-12.1-module-attributions.json')['modules']}
roots={s['module_id']:ET.parse(ROOT/s['source']).getroot() for s in sections}
parents={mid:{child:parent for parent in r.iter() for child in parent} for mid,r in roots.items()}
course={x['section_id'].split(':')[1]:x['label'] for x in load('metadata/numbering-course-2026-07-07.proposed.json')['section_labels']}
# Body headings inspected in historical PDF. Only these six labels are asserted.
cnx={'m67034':'2.5','m67530':'3.3','m71410':'3.8','m67122':'9.2','m67807':'13.6','m42709':'D'}
issues=[]; adaptations=[]; math_sources=[]; objects={}; counts=collections.Counter()
review_chapters={'0':'introduction-exercises','1':'kinematics-exercises','2':'dynamics-exercises','3':'work-and-energy-exercises','4':'impulse-and-momentum-exercises','5':'oscillations-and-waves-exercises','6':'rotation-exercises','7':'fluids-exercises','8':'thermal-physics-exercises','9':'electricity-exercises','10':'magnetism-exercises'}
review_modules={mid:review_chapters[label.split('.')[0]] for mid,label in course.items() if label.split('.')[0] in review_chapters}
chapter_relocated=[]
def anchor(mid,ident):return mid+'--'+ident.encode('utf-8').hex()
from numbering import build_objects
objects=build_objects(sections,roots,PROFILE,course,load('maintained/numbering.json'),anchor)
exercise_placements=load('maintained/exercise-placement.json')['placements'] if PROFILE=='course' else []
for placement in exercise_placements:
    source=(placement['module'],placement['exercise_id']);dest=(placement['after_module'],placement['after_exercise_id'])
    chapter=course[source[0]].split('.')[0]
    assert chapter==course[dest[0]].split('.')[0]
    sequence=[key for key,obj in objects.items() if obj['kind']=='exercise' and str(obj['label']).isdigit() and course.get(key[0],'').split('.')[0]==chapter]
    sequence.sort(key=lambda key:int(objects[key]['label']))
    sequence.remove(source);sequence.insert(sequence.index(dest)+1,source)
    for number,key in enumerate(sequence,1):objects[key]['label']=str(number)


from navigation import Navigation
nav=Navigation([registry[m] for m in IDS],course if PROFILE=='course' else cnx,load('maintained/exercise-views.json')['views'] if FULL and PROFILE=='course' else [], review_chapters=review_chapters)

from mathml import UnsupportedMath
from native_math import native_math
from math_punctuation import render_child

class Renderer:
    def __init__(self,mid,book=False,projection=False):self.mid=mid;self.book=book;self.projection=projection;self.math_index=0;self.review_links=set()
    def content(self,e):return esc(e.text or '')+''.join(render_child(x,self.render) for x in e)
    def render(self,e,depth=2):
        tag=local(e); mid=self.mid; ident=e.get('id'); aid=f' id="{anchor(mid,ident)}"' if ident else ''
        kind='glossary' if tag=='glossary' else 'summary' if 'section-summary' in e.get('class','').split() else 'questions' if set(e.get('class','').split()).intersection(('conceptual-questions','problems-exercises')) and tag=='section' else None
        if FULL and PROFILE=='course' and mid in review_modules and not self.book and not self.projection and kind and not getattr(self,'relocating',False):
            self.relocating=True
            if kind=='glossary':
                parts=[{'term':text(x.find('c:term',NS)), 'html':self.render(x)} for x in e if local(x)=='definition']
                result=''.join(x['html'] for x in parts)
            else:
                parts=[];result=self.render(e)
                # The collected category supplies the heading; retain its old anchor.
                result=re.sub(r'<h3([^>]*)>.*?</h3>',r'<span\1></span>',result,count=1,flags=re.S)
            self.relocating=False
            ids=[anchor(mid,x.get('id')) for x in e.iter() if x.get('id')]
            chapter_relocated.append({'module':mid,'kind':kind,'html':result,'parts':parts,'anchors':ids,'review_slug':review_modules[mid],'image_count':sum(local(x)=='image' for x in e.iter())})
            base='../../exercises/'+review_modules[mid]+'/index.html#'
            dest=base+kind
            aliases=''.join('<a class="relocated-anchor" id="'+i+'" href="'+base+i+'">Continue to this item in the chapter review.</a>' for i in ids)
            if dest in self.review_links:return aliases
            self.review_links.add(dest)
            return aliases+'<p class="chapter-review-link"><a href="'+dest+'">Chapter '+{'glossary':'glossary','summary':'section summaries','questions':'questions and exercises'}[kind]+'</a></p>'
        obj=objects.get((mid,ident),{}); label=obj.get('label')
        if e.tag.startswith('{'+NS['m']+'}'):
            if tag!='math':raise ValueError('Top level MathML child outside math: '+tag)
            self.math_index+=1; key=f'{mid}-math-{self.math_index:04d}'
            if not self.book and not self.projection:
                parent=e
                while not parent.get('id') and parent in parents[mid]:parent=parents[mid][parent]
                snapshot=copy.deepcopy(e);snapshot.tail=None
                math_sources.append({'key':key,'module':mid,'xml':ET.tostring(snapshot,encoding='unicode'),'source_object':parent.get('id')})
            try:
                result,native_changes=native_math(e)
                if not self.book and not self.projection and native_changes:adaptations.append({'kind':'native-mathml','key':key,'changes':native_changes})
            except UnsupportedMath as ex:
                if not self.book and not self.projection:issues.append({'kind':'unresolved-math','module':mid,'key':key,'detail':str(ex)})
                return f'<span class="math-issue" data-math-key="{key}">[Expression needs review: {key}]</span>'
            if not self.book and not self.projection and any(local(x) in ('apply','ci','cn','csymbol') for x in e.iter()):
                adaptations.append({'kind':'content-mathml','key':key,'policy':'Presentation adapter; bold vectors, symbolic juxtaposition, grouped composite powers; visual review required'})
            if not self.book and not self.projection and any(local(x)=='mtr' and any(local(y)!='mtd' for y in x) for x in e.iter()):
                adaptations.append({'kind':'math-table-cell-wrapper','key':key})
            return f'<span data-math-key="{key}">{result}</span>'
        if tag=='para' and obj.get('kind')=='exercise':return f'<div class="exercise"{aid}><div class="object-title">Exercise {esc(label)}</div><div class="para">{self.content(e)}</div></div>'
        if tag in ('metadata','label','colspec'):return ''
        if tag=='title':return f'<h3{aid}>{self.content(e)}</h3>'
        if tag=='link':
            doc=e.get('document',mid); target=e.get('target-id'); url=e.get('url'); obj=objects.get((doc,target),{})
            body=self.content(e) or (f'{obj.get("kind","reference").title()} {obj.get("label") or ""}'.strip())
            if url:return f'<a href="{esc(url)}">{body}</a>'
            if doc not in IDS or (target and not obj):
                if not self.book and not self.projection:issues.append({'kind':('reference-outside-book' if FULL else 'reference-outside-prototype') if doc not in IDS else 'source-reference-unresolved','module':mid,'document':doc,'target':target})
                reason=('outside recovered book' if FULL else 'outside preview') if doc not in IDS else 'source target unresolved'
                return f'<span class="unavailable" title="{esc(reason)}">{body} [{reason}]</span>'
            frag=anchor(doc,target) if target else doc
            href='#'+frag if self.book or (doc==mid and not self.projection) else ('../../sections/' if self.projection else '../')+registry[doc]['candidate_slug']+'/index.html#'+frag
            if getattr(self,'relocating',False):
                target_element=next((x for x in roots[doc].iter() if x.get('id')==target),roots[doc])
                chain=[target_element]
                while chain[-1] in parents[doc]:chain.append(parents[doc][chain[-1]])
                is_collected=doc in review_modules and any(local(x)=='glossary' or set(x.get('class','').split()).intersection(('section-summary','conceptual-questions','problems-exercises')) for x in chain)
                href=('../../exercises/'+review_modules[doc] if is_collected else '../../sections/'+registry[doc]['candidate_slug'])+'/index.html#'+frag
            return f'<a href="{href}">{body}</a>'
        if tag=='image':
            src=(ROOT/registry[mid]['source']).parent/e.get('src'); dest=OUT/'media'/src.name;dest.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(src,dest)
            url=('media/' if self.book else '../../media/')+src.name
            return f'<img src="{esc(url)}" alt="{esc(e.get("alt", ""))}" style="max-width:{esc(e.get("width","600"))}px">'
        if tag=='media':
            # Alt belongs to CNXML media, not image. Set only on the derived copy.
            clone=copy.deepcopy(e)
            alt=e.get('alt','')
            if not alt.strip():
                ancestor=e
                while ancestor in parents[mid] and local(ancestor)!='figure':ancestor=parents[mid][ancestor]
                caption=ancestor.find('c:caption',NS)
                if caption is not None:alt=' '.join(text(caption).split())
            for img in clone.findall('c:image',NS):img.set('alt',alt)
            return f'<div class="media"{aid}>'+self.content(clone)+'</div>'
        if tag=='figure':
            cap=e.find('c:caption',NS); body=esc(e.text or '')+''.join(self.render(x)+esc(x.tail or '') for x in e if local(x)!='caption')
            caption=self.content(cap) if cap is not None else ''
            capid=f' id="{anchor(mid,cap.get("id"))}"' if cap is not None and cap.get('id') else ''
            return f'<figure{aid}>{body}<figcaption{capid}><b>Figure {esc(label or "(unnumbered)")}. </b>{caption}</figcaption></figure>'
        if tag=='equation':
            ancestor=e; in_summary=False
            while ancestor in parents[mid]:
                ancestor=parents[mid][ancestor]
                title=ancestor.find('c:title',NS)
                if 'section-summary' in ancestor.get('class','').split() or (local(ancestor)=='section' and text(title).lower() in ('section summary','chapter summary')):
                    in_summary=True;break
            visible_label=None if in_summary else label
            return f'<div class="equation"{aid}><div>{self.content(e)}</div><span class="eq-label">{("("+esc(visible_label)+")") if visible_label else ""}</span></div>'
        if tag in ('example','exercise','note'):
            heading=(tag.title()+' '+str(label)) if label else (tag.title() if tag!='note' else '')
            return f'<div class="{tag}"{aid}>'+ (f'<div class="object-title">{esc(heading)}</div>' if heading else '')+self.content(e)+'</div>'
        if tag=='solution':return f'<div class="solution"{aid}><b>Solution</b>{self.content(e)}</div>'
        if tag=='list':
            ordered=e.get('list-type')=='enumerated';htag='ol' if ordered else 'ul'
            style={'lower-alpha':'a','upper-alpha':'A','lower-roman':'i','upper-roman':'I','arabic':'1'}.get(e.get('number-style'))
            extra=f' type="{style}"' if ordered and style else ''
            return f'<{htag}{aid}{extra}>{self.content(e)}</{htag}>'
        if tag=='emphasis':return f'<{"em" if e.get("effect")=="italics" else "strong"}{aid}>{self.content(e)}</'+('em' if e.get('effect')=='italics' else 'strong')+'>'
        if tag=='iframe':
            url=e.get('src','')
            if not self.book and not self.projection:issues.append({'kind':'external-media','module':mid,'url':url,'detail':'Linked resource; not embedded or archived for offline use'})
            return f'<p class="external-media"{aid}>External interactive/video: <a href="{esc(url)}">{esc(url)}</a></p>'
        if tag=='entry':
            attr=''
            if e.get('namest'):
                group=parents[mid].get(e)
                while group is not None and local(group)!='tgroup':group=parents[mid].get(group)
                columns={x.get('colname'):int(x.get('colnum',i+1)) for i,x in enumerate(group.findall('c:colspec',NS))}
                attr+=' colspan="'+str(columns[e.get('nameend')]-columns[e.get('namest')]+1)+'"'
            if e.get('align') in ('left','right','center'):attr+=' style="text-align:'+e.get('align')+'"'
            if e.get('morerows'):attr+=' rowspan="'+str(int(e.get('morerows'))+1)+'"'
            ancestor=parents[mid].get(e);header=False
            while ancestor is not None and local(ancestor) not in ('table','tgroup'):
                header=header or local(ancestor)=='thead';ancestor=parents[mid].get(ancestor)
            cell='th' if header else 'td'
            if header:attr+=' scope="col"'
            return f'<{cell}{aid}{attr}>{self.content(e)}</{cell}>'
        if tag=='table':
            caption=e.find('c:title',NS)
            if caption is None:caption=e.find('c:caption',NS)
            heading=f'<caption>Table {esc(label or "(unnumbered)")}. {self.content(caption)}</caption>' if caption is not None else ''
            body=esc(e.text or '')+''.join(self.render(x)+esc(x.tail or '') for x in e if local(x) not in ('title','caption'))
            summary=f' aria-label="{esc(e.get("summary"))}"' if e.get('summary') else ''
            return f'<div class="table-wrap"{aid}><table{summary}>{heading}{body}</table></div>'
        if tag=='footnote':return f'<span class="footnote"{aid}> [Note: {self.content(e)}]</span>'
        if tag=='newline':return '<br>'
        tags={'para':'div','content':'div','section':'section','item':'li','term':'dfn','definition':'div','meaning':'div','glossary':'section','problem':'div','tgroup':'tbody','thead':'thead','tbody':'tbody','row':'tr','sub':'sub','sup':'sup','span':'span','div':'div','caption':'caption'}
        if tag=='tgroup':return self.content(e)
        if tag not in tags:raise ValueError('Unsupported CNXML element '+tag)
        htag=tags[tag]; cls=f' class="{tag}"'
        return f'<{htag}{aid}{cls}>{self.content(e)}</{htag}>'
    def module(self):
        mid=self.mid;r=roots[mid];label=(cnx if PROFILE=='cnx' else course).get(mid,'Unnumbered' if mid=='m67030' else 'Label pending')
        abstract=r.find('c:metadata/md:abstract',NS)
        learning=f'<aside class="objectives"><h2>Learning objectives</h2>{self.content(abstract)}</aside>' if abstract is not None and text(abstract) else ''
        a=attributions[mid]
        public_credit=json.loads((ROOT/'metadata/public-attribution.json').read_text(encoding='utf-8'))
        omit=public_credit.get('omit_self_credit',[])
        credit='<footer class="attribution"><h2>Sources and adaptations</h2><p>Adapted from <strong>'+esc(a.get('used_here_as') or a['module_title'])+'</strong>'
        if a['authors'] not in omit:credit+=', by '+esc(a['authors'])
        if a['copyright'] not in omit:credit+=', copyright '+esc(a['copyright'])
        credit+=', licensed under <a href="'+esc(a['license'])+'">CC BY 4.0</a> (<a href="'+esc(a['url'])+'">CNX module '+esc(mid)+', version '+esc(a['legacy_module_version'])+'</a>).</p>'
        if a.get('based_on_text'):
            ancestry=esc(a['based_on_text'])
            match=re.fullmatch(r'(.*?)\s*<(https?://[^<>]+)>\s*by\s+(.+?)\.?',a['based_on_text'])
            if match:
                title,url,author=match.groups()
                # PDF extraction can insert whitespace into the recorded URL.
                url=re.sub(r'\s+','',url)
                ancestry='<a href="'+esc(url)+'">'+esc(title)+'</a>, by '+esc(author)+'.'
            credit+='<p>This source was based on: '+ancestry+'</p>'
        for upstream in public_credit.get('additional_sources',{}).get(mid,[]):
            credit+='<p>Upstream source: '+esc(upstream['credit'])+', <a href="'+esc(upstream['url'])+'">'+esc(upstream['title'])+' (module '+esc(upstream['module_id'])+')</a>. <a href="'+esc(upstream['license_url'])+'">'+esc(upstream['license'])+'</a>.</p>'
        for source in public_credit.get('adapted_passages',{}).get(mid,[]):
            credit+='<p>'+esc(source['label'])+': '+esc(source['credit'])+', <a href="'+esc(source['url'])+'">'+esc(source['title'])+'</a>. <a href="'+esc(source['license_url'])+'">'+esc(source['license'])+'</a>. '+esc(source['changes'])+'</p>'
        credit+='<p>This section was recovered from <em>Introduction to Physics</em>, CNX collection col25183, version 12.1, and subsequently revised. See the <a href="https://github.com/bkpark/concepts-of-physics-2e">source repository and revision history</a>.</p></footer>'
        return f'<article id="{mid}"><header><p class="eyebrow">{esc(label)}</p><h1>{esc(text(r.find("c:title",NS)))}</h1></header>{nav.section_navigation(mid) if FULL and not self.book else ""}{learning}'+''.join(self.render(x) for x in r if local(x) in ('content','glossary'))+credit+'</article>'

def page(title,body,prefix='',website=True):
    site_links=('<a href="'+prefix+'index.html">Introduction to Physics · Home</a> · <a href="'+prefix+'contents/index.html">Full contents</a>') if FULL and website else ''
    if RELEASE:
        canonical=release['public_origin']+'/'
        return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="book-release" content="'+esc(release['release_id'])+'"><title>'+esc(title.replace(' — sample','').replace(' — prototype',''))+'</title><link rel="stylesheet" href="'+prefix+'style.css"><script defer src="'+prefix+'copy-math.js"></script></head><body><nav aria-label="Book navigation">'+(site_links or '<a href="'+prefix+'index.html">Introduction to Physics · Contents</a>')+' · <a href="'+prefix+release['pdf_filename']+'">Download PDF</a></nav><main>'+body+'</main></body></html>'
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(title)+'</title><link rel="stylesheet" href="'+prefix+'style.css"><script defer src="'+prefix+'copy-math.js"></script></head><body><nav>'+(site_links or '<a href="'+prefix+'index.html">Introduction to Physics · Fidelity prototype</a>')+'</nav><div class="prototype-notice">'+esc(SCOPE)+'. Section labels follow the selected reference; object numbers are experimental. Highlighted expressions need review.</div><main>'+body+'</main></body></html>'

OUT.mkdir(parents=True,exist_ok=True);shutil.copyfile(P/'style.css',OUT/'style.css');shutil.copyfile(P/'copy-math.js',OUT/'copy-math.js')
book=[]
for mid in IDS:
    source_dir=OUT/'source'/mid;source_dir.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(ROOT/registry[mid]['source'],source_dir/'index.cnxml')
    target=OUT/'sections'/registry[mid]['candidate_slug'];target.mkdir(parents=True,exist_ok=True)
    body=Renderer(mid).module()
    if FULL:body=nav.previous_next(mid,'top')+body+nav.previous_next(mid,'bottom')
    (target/'index.html').write_text(page(registry[mid]['title'],body,'../../'),encoding='utf-8',newline='\n')
    book.append(Renderer(mid,True).module())

# Relocate approved questions in the chapter view without changing source IDs or module provenance.
if FULL and PROFILE=='course':
    for placement in exercise_placements:
        smid=placement['module'];dmid=placement['after_module']
        ex=next(e for e in roots[smid].iter() if e.get('id')==placement['exercise_id'])
        target_ex=next(e for e in roots[dmid].iter() if e.get('id')==placement['after_exercise_id'])
        # These initial placement entries are prose-only; reject unsupported markup rather than silently changing math keys.
        assert not any(local(e) in ('math','image','link') for e in ex.iter())
        fragment=Renderer(smid).render(ex);target_fragment=Renderer(dmid).render(target_ex)
        source_block=next(b for b in chapter_relocated if b['kind']=='questions' and b['module']==smid and fragment in b['html'])
        target_block=next(b for b in chapter_relocated if b['kind']=='questions' and b['module']==dmid and target_fragment in b['html'])
        source_block['html']=source_block['html'].replace(fragment,'',1)
        target_block['html']=target_block['html'].replace(target_fragment,target_fragment+fragment,1)

exercise_manifest=[]
if FULL and PROFILE=='course':
    for view in load('maintained/exercise-views.json')['views']:
        body='<h1>'+esc(view['label']+': '+view['title'])+'</h1>'+('' if RELEASE else '<p>Generated from the maintained sections. Section links and source-object identities remain canonical. Labels are provisional.</p>')
        blocks=[]
        for category,title in [('conceptual-questions','Conceptual Questions'),('problems-exercises','Problems & Exercises')]:
            body+='<h2>'+title+'</h2>'
            for mid in IDS:
                if course.get(mid,'').split('.')[0]!=view['chapter_label']:continue
                for e in roots[mid].iter():
                    if local(e)!='section':continue
                    heading=e.find('c:title',NS)
                    inferred=load('maintained/numbering.json')[PROFILE].get('relocated_section_titles',{}).get(text(heading))
                    if category not in e.get('class','').split() and inferred!=category:continue
                    source_url='../../sections/'+registry[mid]['candidate_slug']+'/index.html#'+anchor(mid,e.get('id'))
                    renderer=Renderer(mid,projection=True)
                    before=list(roots[mid].iter());renderer.math_index=sum(x.tag=='{'+NS['m']+'}math' for x in before[:before.index(e)])
                    body+='<h3><a href="'+source_url+'">'+esc(course[mid]+': '+registry[mid]['title'])+'</a></h3>'+renderer.render(e)
                    blocks.append({'module':mid,'source_id':e.get('id'),'category':category,'exercise_ids':[x.get('id') for x in e.iter() if local(x)=='exercise']})
        target=OUT/'exercises'/view['slug'];target.mkdir(parents=True,exist_ok=True)
        if view['chapter_label'] in review_chapters:
            collected=[b for b in chapter_relocated if b['review_slug']==view['slug']]
            chapter_title=view['title'].removesuffix(' (Exercise)').removesuffix(' (Exercises)')
            body='<h1>Chapter '+esc(view['chapter_label'])+': '+esc(chapter_title)+' — Review and Exercises</h1><nav aria-label="Chapter review"><a href="#glossary">Glossary</a> · <a href="#summary">Section Summary</a> · <a href="#questions">Questions and Exercises</a></nav>'
            body+='<section id="glossary"><h2>Glossary</h2>'
            terms=[p for b in collected if b['kind']=='glossary' for p in b['parts']]
            body+=''.join(p['html'] for p in sorted(terms,key=lambda p:p['term'].casefold()))+'</section>'
            for kind,title in [('summary','Section Summary'),('questions','Questions and Exercises')]:
                body+='<section id="'+kind+'"><h2>'+title+'</h2>'
                previous_mid=None
                for b in collected:
                    if b['kind']!=kind:continue
                    mid=b['module']
                    if mid!=previous_mid:body+='<h3><a href="../../sections/'+registry[mid]['candidate_slug']+'/index.html">'+esc(course[mid]+': '+registry[mid]['title'])+'</a></h3>'
                    body+=b['html'];previous_mid=mid
                body+='</section>'
            body+='<p>Source sections: '+', '.join('<a href="../../sections/'+registry[mid]['candidate_slug']+'/index.html">'+esc(registry[mid]['title'])+'</a>' for mid in dict.fromkeys(b['module'] for b in collected))+'. Credits and licenses appear with each source section.</p>'
        body=nav.previous_next('exercises:'+view['slug'],'top')+body+nav.previous_next('exercises:'+view['slug'],'bottom')
        page_title = ('Chapter ' + view['chapter_label'] + ': ' + view['title'].removesuffix(' (Exercise)').removesuffix(' (Exercises)') + ' — Review and Exercises') if view['chapter_label'] in review_chapters else view['title']
        (target/'index.html').write_text(page(page_title,body,'../../'),encoding='utf-8',newline='\n')
        exercise_manifest.append({**view,'blocks':blocks})
    dump(OUT/'exercise-views.json',exercise_manifest)
    dump(OUT/'chapter-end-relocations.json',[{k:v for k,v in b.items() if k in ('module','kind','anchors','review_slug','image_count')} for b in chapter_relocated])
intro='<header><p class="eyebrow">'+esc(PUBLIC_NUMBERING)+'</p><h1>Introduction to Physics</h1>'+('<p>'+NUMBERING_NOTE+'</p>' if PROFILE=='course' else '')+'</header>'
intro+=nav.overview() if FULL else '<ul>'+''.join('<li>'+nav.link(registry[m])+'</li>' for m in IDS)+'</ul>'
if FULL:
    contents=OUT/'contents';contents.mkdir(exist_ok=True)
    (contents/'index.html').write_text(page('Full table of contents — Introduction to Physics','<h1>Full table of contents</h1>'+nav.overview(full=True,prefix='../'),'../'),encoding='utf-8',newline='\n')
if not RELEASE:intro+='<p>Historical source remains unchanged. Math source XML and issue logs are included beside the build. The other numbering profile uses exactly the same section paths and anchors.</p>'
if not RELEASE:intro+='<p><a href="review.html">Review flagged expressions and references</a> · <a href="book.html">Complete printable sample</a></p>'
(OUT/'index.html').write_text(page('Introduction to Physics — prototype',intro),encoding='utf-8',newline='\n')
(OUT/'book.html').write_text(page('Introduction to Physics — sample', '<div class="cover"><h1>Introduction to Physics</h1><h2>Fidelity prototype</h2><p>'+esc(str(len(IDS)))+' modules · '+PROFILE+' profile</p><p>Provisional object numbering. Not a student edition.</p><p>Adaptation by Andrew Park; underlying content by Bobby Bailey, Andrew Park, OpenStax and James Rittenbach. Historical collection: CC BY 4.0. Original figure credits are retained.</p></div>'+''.join(book),website=False),encoding='utf-8',newline='\n')
dump(OUT/'object-labels.json',{m+'#'+ident:obj for (m,ident),obj in objects.items() if m in IDS});dump(OUT/'math-source.json',math_sources);dump(OUT/'issues.json',issues);dump(OUT/'adaptations.json',adaptations)
review='<h1>Fidelity review</h1><p>The maintained source includes approved repairs R1–R4. Any remaining findings are listed below.</p>'
for item in issues:
    review+='<section><h2>'+esc(item.get('key',item['module']))+'</h2><p>'+esc(item.get('detail',str(item)))+'</p>'
    if item.get('key'):
        source=next(x for x in math_sources if x['key']==item['key'])
        review+='<p>Source object: '+esc(source['source_object'])+'</p><pre style="white-space:pre-wrap;overflow-wrap:anywhere;font-size:12px">'+esc(source['xml'])+'</pre>'
    review+='</section>'
(OUT/'review.html').write_text(page('Fidelity review',review),encoding='utf-8',newline='\n')
dump(OUT/'identity-registry.json',{m:{'slug':registry[m]['candidate_slug'],'anchors':[anchor(m,e.get('id')) for e in roots[m].iter() if e.get('id')]} for m in IDS})
dump(OUT/'build-manifest.json',{'release_id':release['release_id'] if RELEASE else None,'profile':PROFILE,'renderer':'native-mathml','source_layer':'maintained','exercise_placements':exercise_placements,'approved_repairs':['R1','R2','R3','R4'],'modules':IDS,'math_expressions':len(math_sources),'issues':len(issues),'source_sha256':{m:hashlib.sha256((ROOT/registry[m]['source']).read_bytes()).hexdigest() for m in IDS},'object_numbering_status':'Course section labels and chapter exercise counters implemented; reference fixtures are partial and equation-label visibility remains provisional','section_labels':{m:(cnx if PROFILE=='cnx' else course).get(m) for m in IDS}})
print(json.dumps({'profile':PROFILE,'math':len(math_sources),'issues':dict(collections.Counter(x['kind'] for x in issues)),'adaptations':len(adaptations)}))
