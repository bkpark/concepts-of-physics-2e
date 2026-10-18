// Chapter 0 print proof. Explicit pages preserve recto/verso margins and section starts.
const {chromium}=require('playwright');
const fs=require('fs'),path=require('path'),http=require('http');
const root=path.resolve(__dirname,'../..'),dist=path.join(root,'prototype/dist/course-full');
const out=path.join(root,'output/pdf'),qa=path.join(root,'reports/1.1/chapter-0-print');
fs.mkdirSync(qa,{recursive:true});fs.mkdirSync(out,{recursive:true});
const server=http.createServer((req,res)=>{let f=path.resolve(dist,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));if(!f.startsWith(dist+path.sep)||!fs.existsSync(f)){res.writeHead(404).end();return;}res.setHeader('Content-Type',({'.html':'text/html','.css':'text/css','.js':'text/javascript','.svg':'image/svg+xml'})[path.extname(f)]||'application/octet-stream');fs.createReadStream(f).pipe(res);});
(async()=>{await new Promise(r=>server.listen(0,'127.0.0.1',r));const origin=`http://127.0.0.1:${server.address().port}`;
 const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
 try{const page=await browser.newPage({viewport:{width:1050,height:1200}});await page.goto(origin+'/book.html');
 const reviewPage=await browser.newPage();await reviewPage.goto(origin+'/exercises/introduction-exercises/index.html');const review=await reviewPage.locator('main').innerHTML();await reviewPage.close();
 const result=await page.evaluate(async({review,origin})=>{
  const source=[...document.querySelectorAll('main > article')].filter(e=>['m52309','m52310','m67032'].includes(e.id)).map(e=>e.cloneNode(true));
  const reviewNode=document.createElement('article');reviewNode.innerHTML=review;
  for(const e of reviewNode.querySelectorAll('[src]'))e.setAttribute('src',new URL(e.getAttribute('src'),origin+'/exercises/introduction-exercises/').href);
  const credits=document.createElement('article');credits.innerHTML='<h1>Sources and adaptations</h1>';
  for(const s of source){const f=s.querySelector('.attribution');if(f){const h=document.createElement('h3');h.textContent=s.querySelector('header h1').textContent;credits.append(h,f);}}
  for(const f of credits.querySelectorAll('.attribution h2'))f.remove();
  for(const s of [...source,reviewNode,credits]){
   for(const e of s.querySelectorAll('nav,.reading-navigation,.chapter-navigation,.chapter-return,.section-summary,.glossary,.exercise-set,.math-copy-toolbar,.numbering-toggle,script'))e.remove();
   // Review material already appears in the chapter review, including all exercise numbers.
   if(s!==reviewNode)for(const e of s.querySelectorAll('section'))if(/^(Questions and Exercises|Summary)$/.test(e.querySelector(':scope > h2,:scope > h3')?.textContent.trim()||''))e.remove();
   for(const i of s.querySelectorAll('img')){i.src=new URL(i.getAttribute('src'),origin+'/book.html').href;i.removeAttribute('style');}
   for(const a of s.querySelectorAll('a[href]')){const href=a.getAttribute('href');if(href.startsWith('#'))continue;a.href=new URL(href,'https://intro-1-1.coaphys.xyz/').href;}
  }
  // Relocate table-header footnotes intact, preserving their IDs and wording.
  for(const article of source)for(const table of article.querySelectorAll('table')){
   const notes=[...table.querySelectorAll('th .footnote')];if(!notes.length)continue;
   const footer=document.createElement('div');footer.className='table-notes';footer.append(...notes);table.after(footer);
  }
  for(const article of [...source,reviewNode]){
   for(const term of article.querySelectorAll('.definition .term')){
    const next=term.nextSibling;
    if(next && !(next.nodeType===Node.TEXT_NODE && /^\s/.test(next.textContent)))term.after(document.createTextNode(' '));
   }
   // Preserve equation mathematics; put the prose qualifier on a separate print line.
   for(const box of article.querySelectorAll('.equation > div:first-child')){
    for(const node of [...box.childNodes])if(node.nodeType===Node.TEXT_NODE && /conservative\s+forces\s+only/.test(node.textContent)){
     const line=document.createElement('div');line.className='equation-qualifier';node.replaceWith(line);line.append(node);
    }
   }
  }
  document.querySelectorAll('link[rel=stylesheet],style,script').forEach(e=>e.remove());document.body.replaceChildren();
  const css=document.createElement('style');css.textContent=`
  @page{size:Letter;margin:0}*{box-sizing:border-box}html,body{margin:0;padding:0;background:#fff;color:#111;font-family:Georgia,'Times New Roman',serif;font-size:10.5pt;line-height:1.3}
  .sheet{width:8.5in;height:11in;position:relative;padding:.6in .65in .65in 1in;break-after:page;overflow:hidden}.sheet:nth-child(even){padding-left:.65in;padding-right:1in}.sheet:last-child{break-after:auto}
  .running{font:8pt Arial,sans-serif;letter-spacing:.025em;position:absolute;top:.29in;left:1in;right:.65in;color:#555;border-bottom:.5pt solid #bbb;padding-bottom:5pt}.sheet:nth-child(even) .running{left:.65in;right:1in}
  .folio{position:absolute;bottom:.3in;right:.65in;font:9pt Arial}.sheet:nth-child(even) .folio{right:auto;left:.65in}
  .area{height:9.75in;display:flex;flex-direction:column}.columns{display:flex;gap:.25in;flex:1;min-height:0}.column{width:3.3in;position:relative;display:flow-root;flex:none}.column > :first-child{margin-top:0!important}
  h1,h2,h3,h4{font-family:Arial,sans-serif;font-weight:600;line-height:1.17;break-after:avoid}h1{font-size:18pt;margin:0 0 12pt}h2{font-size:12.5pt;margin:12pt 0 6pt}h3{font-size:11pt;margin:10pt 0 5pt}h4{font-size:10pt;margin:8pt 0 4pt}.section-title{font-size:19pt;margin:0 0 13pt}.section-title small{display:block;font:9pt Arial;letter-spacing:.07em;color:#555;margin-bottom:5pt}
  p,.para{margin:0 0 7pt;text-align:left;orphans:2;widows:2}ul,ol{padding-left:16pt;margin:5pt 0 8pt}li{margin:3pt 0}a{color:inherit;text-decoration:none}strong,b{font-weight:bold}
  figure{padding:0;margin:0 0 12pt;display:flow-root}figure img{display:block;max-width:100%;max-height:1.8in;width:auto;height:auto;object-fit:contain;margin:0 auto}figcaption{font:8.3pt/1.25 Arial,sans-serif;margin-top:6pt}.media{text-align:center}.objectives{font:9pt/1.3 Arial,sans-serif;background:#f1f3f3;padding:8pt;margin:0 0 10pt}.objectives h2{font-size:9pt;margin:0 0 4pt}
  .example,.note,.solution{padding:7pt;background:#f4f4ef;border-top:.7pt solid #bbc2c2;margin:8pt 0}.object-title{font:bold 9pt/1.2 Arial;margin:0 0 6pt}.exercise{margin:0 0 10pt}.exercise header{font-weight:bold}.definition{margin:0 0 6pt}dfn{font-weight:bold;font-style:normal}.definition .term{font-weight:bold;font-style:normal}.meaning{display:inline}.equation{display:flex;align-items:center;justify-content:space-between;gap:5pt;margin:9pt 0}.equation > div:first-child{flex:1;text-align:center;min-width:0;white-space:nowrap}.eq-label{font-size:8pt;white-space:nowrap}math{font-family:'Cambria Math',serif;font-size:1em}mtd{padding:1px 2px}
  mtable[columnalign="right left"] > mtr > mtd:first-child{text-align:right;text-align:-webkit-right}
  mtable[columnalign="right left"] > mtr > mtd:nth-child(2){text-align:left}
  [data-math-key]{display:inline-block;max-width:100%;overflow:visible;vertical-align:baseline}
  [data-math-key]:has(> math[display="block"]){display:block;text-align:center}
  .math-with-punctuation{display:inline-block;white-space:nowrap;max-width:100%;overflow:visible;vertical-align:baseline}
  .math-with-punctuation [data-math-key]{max-width:none;overflow:visible}.sentence-punctuation{display:inline-block}
  .sentence-math-block{display:block;text-align:center}.sentence-baseline{display:inline-block;width:0;height:0}
  .reference-label{white-space:nowrap}
  .table-notes{font:7.5pt/1.2 Arial,sans-serif;margin:3pt 0 9pt}.table-notes .footnote{display:block}
  table{border-collapse:collapse;width:100%;font-size:8.5pt;line-height:1.2;margin:4pt 0 8pt}td,th{border:.5pt solid #b4bebe;padding:4pt;vertical-align:top}th{background:#edf1f2;text-align:left}caption,.table-title{font:9pt/1.25 Arial;text-align:left;margin:0 0 5pt}.table-wrap{margin:0 0 10pt}.wide{margin-bottom:12pt}.wide table{font-size:9pt}.sidebar.wide{font-size:10pt;line-height:1.3;padding:12pt;margin:0 0 14pt}.sidebar.wide h3{margin-top:0}.attribution{font-size:9pt;line-height:1.3;margin-bottom:10pt}.eyebrow{font:9pt Arial;color:#555;margin-bottom:4pt}
  .opener h1{font-size:26pt;line-height:1.1;margin-bottom:9pt}.opener .kicker{font:10pt Arial;letter-spacing:.15em;margin:0 0 8pt}.opener figure{margin:0 0 10pt}.opener figure img{max-height:none;max-width:100%;width:600px}.opener figcaption{font-size:7.8pt}.opener .intro-label{font:9pt Arial;margin:0 0 8pt}.opener .para{font-size:10.5pt;line-height:1.3;margin-bottom:7pt}.mini-toc{float:right;width:2.25in;margin-left:16pt!important;padding:9pt!important;background:#f1f3f3;font:9pt/1.15 Arial;border-top:.7pt solid #aebaba;border-bottom:.7pt solid #aebaba;padding:5pt 0;margin:0 0 8pt}.mini-toc div{margin:2pt 0}.mini-toc strong{display:block;margin-bottom:4pt}.continuation{font:italic 8pt Arial;color:#555;margin-bottom:5pt}
  mtable[columnalign="left"] mtd{text-align:left}
  .equation-qualifier{display:block;white-space:normal;margin-top:4pt;font-size:9pt}
  .equation > div:first-child:not(:has(math)){white-space:normal}
  @media screen{body{background:#ddd}.sheet{background:white;margin:15px auto;box-shadow:0 2px 9px #aaa}}
  `;document.head.append(css);
  // Decode images in an off-page staging area before any layout measurements.
  const staging=document.createElement('div');staging.style.cssText='position:absolute;left:-10000px;width:6.85in';staging.append(...source,reviewNode,credits);document.body.append(staging);
  await document.fonts.ready;await Promise.all([...staging.querySelectorAll('img')].map(i=>i.decode().catch(()=>{})));
  const stats={startPage:1,sections:[],floats:[],splits:[],overflows:[],imageCount:staging.querySelectorAll('img').length};
  const expectedPunctuation=[...staging.querySelectorAll('.math-with-punctuation')].map(e=>e.outerHTML).sort();
  const expectedMath=[...staging.querySelectorAll('math')].map(e=>e.outerHTML).sort();const audited=[];
  function audit(el){el.dataset.auditKey=String(audited.length);audited.push(el.textContent.replace(/\s+/g,''));}
  let sheet,area,columns,col,ci=0,sectionLabel='',pending=[],widePending=[],introPhase=false;
  function newPage(title='Introduction'){
   sheet=document.createElement('div');sheet.className='sheet';sheet.innerHTML='<div class="running">CHAPTER 0 · INTRODUCTION<span style="float:right"></span></div><div class="area"></div><div class="folio"></div>';
   sheet.querySelector('.running span').textContent=title;document.body.append(sheet);sheet.querySelector('.folio').textContent=document.querySelectorAll('.sheet').length;
   area=sheet.querySelector('.area');columns=document.createElement('div');columns.className='columns';columns.innerHTML='<div class="column"></div><div class="column"></div>';area.append(columns);ci=0;col=columns.children[0];if(widePending.length){const w=widePending.shift();w.classList.add('wide');area.insertBefore(w,columns);}return sheet;
  }
  function fits(){return !col.lastElementChild||col.lastElementChild.getBoundingClientRect().bottom<=col.getBoundingClientRect().bottom+.2;}
  function nextColumn(){const headings=[];while(col.lastElementChild&&(col.lastElementChild.matches('h2,h3,h4,.object-title')||(!col.lastElementChild.textContent.trim()&&!col.lastElementChild.querySelector('img,math,table')))){headings.unshift(col.lastElementChild);col.lastElementChild.remove();}if(ci===0){ci=1;col=columns.children[1];}else newPage(sectionLabel);flushFloats();col.append(...headings);}
  function flushFloats(){
   // The opening left column belongs to the objectives and opening prose.
   if(ci===0 && area.querySelector(':scope > .section-title') && col.querySelector('.objectives'))return;
   if(!pending.length||col.querySelector(':scope > figure')||sheet.querySelectorAll('figure:not(.chapter-image)').length>=2)return;
   const f=pending[0];col.prepend(f);if(!fits()){f.remove();return;}pending.shift();stats.floats.push({id:f.id,page:Number(sheet.querySelector('.folio').textContent),column:ci+1});
  }
  function splitBlock(el){
   const walker=document.createTreeWalker(el,NodeFilter.SHOW_TEXT);let n;const points=[];
   while(n=walker.nextNode()){if(n.parentElement.closest('math,.math-with-punctuation,.reference-label,figcaption,table,h1,h2,h3,h4,.object-title,.continuation'))continue;for(const m of n.textContent.matchAll(/[ \t\r\n]+/g))points.push([n,m.index+m[0].length]);}
   if(points.length<12)return null;
   const cut=idx=>{const [node,offset]=points[idx],a=document.createRange(),b=document.createRange();a.selectNodeContents(el);a.setEnd(node,offset);b.selectNodeContents(el);b.setStart(node,offset);const first=el.cloneNode(false),rest=el.cloneNode(false);first.append(a.cloneContents());rest.append(b.cloneContents());rest.removeAttribute('id');return [first,rest];};
   let lo=4,hi=points.length-(introPhase?25:5),best=-1;
   while(lo<=hi){let mid=(lo+hi)>>1;const [first]=cut(mid);col.append(first);const ok=fits();first.remove();if(ok){best=mid;lo=mid+1;}else hi=mid-1;}
   if(best<4)return null;const pair=cut(best);if(el.matches('.example,.note,.solution')){const marker=document.createElement('div');marker.className='continuation';marker.textContent=(el.querySelector('.object-title,h2,h3,h4')?.textContent.trim()||el.dataset.continuedTitle||'Note')+' (continued)';pair[1].dataset.continuedTitle=el.querySelector('.object-title,h2,h3,h4')?.textContent.trim()||el.dataset.continuedTitle||'Note';pair[1].querySelectorAll('.continuation').forEach(e=>e.remove());pair[1].prepend(marker);}return pair;
  }
  function place(el){
   if(el.matches('.example')&&!el.dataset.continuedTitle&&col.children.length){const last=col.lastElementChild.getBoundingClientRect();if(col.getBoundingClientRect().bottom-last.bottom<160)nextColumn();}
   col.append(el);if(fits())return;
   const blockHeight=el.getBoundingClientRect().height;el.remove();
   if(el.matches('.exercise,.note,.solution')&&col.children.length&&blockHeight<columns.getBoundingClientRect().height-10){nextColumn();place(el);return;}
   if(el.matches('.para,p,ul,ol,.example,.note,.solution,.exercise,.attribution')){
    const split=splitBlock(el);if(split){col.append(split[0]);stats.splits.push({id:el.id,page:Number(sheet.querySelector('.folio').textContent)});nextColumn();place(split[1]);return;}
   }
   if(!col.children.length){stats.overflows.push({id:el.id,type:el.className,height:el.getBoundingClientRect().height});col.append(el);return;}
   // Keep a heading with the following block.
   let heading=col.lastElementChild;if(heading?.matches('h2,h3,h4,.object-title'))heading.remove();else heading=null;
   nextColumn();if(heading)col.append(heading);place(el);
  }
  function flatten(parent){const blocks=[];for(const e of [...parent.children]){
   if(e.matches('header')&&e.querySelector('h1'))continue;
   if(e.matches('.para')&&e.querySelector(':scope > figure')){
    // Preserve text nodes and inline formatting when extracting embedded figures.
    const expected=e.textContent.replace(/\s+/g,'');
    const parts=[];let prose=e.cloneNode(false);
    for(const node of [...e.childNodes]){
     if(node.nodeType===Node.ELEMENT_NODE&&node.matches('figure')){
      if(prose.textContent.trim()||prose.querySelector('math,img'))parts.push(prose);
      parts.push(node);prose=e.cloneNode(false);prose.removeAttribute('id');
     }else prose.append(node);
    }
    if(prose.textContent.trim()||prose.querySelector('math,img'))parts.push(prose);
    if(parts.map(x=>x.textContent).join('').replace(/\s+/g,'')!==expected)throw new Error('Embedded-figure paragraph text changed: '+e.id);
    blocks.push(...parts);continue;
   }
   if(e.matches('section,.content'))blocks.push(...flatten(e));else blocks.push(e);
  }return blocks;}
  // Intro prose flows around a corner contents box and continues at full width.
  newPage('Chapter opening');sheet.classList.add('opener');columns.remove();
  const opening=document.createElement('div');opening.style.display='flow-root';opening.innerHTML='<div class="kicker">CHAPTER 0</div><h1>Introduction</h1><div class="intro-label">0.1 · Science and the Realm of Physics, Physical Quantities, and Units</div>';
  area.append(opening);const intro=source[0],fig=intro.querySelector('figure');fig.classList.add('chapter-image');audit(fig);opening.append(fig);
  const toc=document.createElement('div');toc.className='mini-toc';toc.innerHTML='<strong>IN THIS CHAPTER</strong><div>0.1 &nbsp; Science and the Realm of Physics, Physical Quantities, and Units</div><div>0.2 &nbsp; Physics: An Introduction</div><div>0.3 &nbsp; Physical Quantities and Units</div><div>Chapter Review and Exercises</div>';opening.append(toc);
  stats.sections.push({label:'0.1',page:1});
  let introFlow=opening;col=introFlow;introPhase=true;
  // The split routine measures against the full printable page during this phase.
  const normalFits=fits;
  fits=()=>!col.lastElementChild||col.lastElementChild.getBoundingClientRect().bottom<=area.getBoundingClientRect().bottom+.2;
  for(const original of [...intro.querySelectorAll('.content > .para')]){
   audit(original);let p=original;
   while(p){introFlow.append(p);if(fits())break;p.remove();const parts=splitBlock(p);if(parts){introFlow.append(parts[0]);p=parts[1];}
    newPage('Chapter introduction');columns.remove();introFlow=document.createElement('div');introFlow.style.display='flow-root';area.append(introFlow);col=introFlow;
   }
  }
  fits=normalFits;introPhase=false;
  // Section 0.2 starts below the end of the single-column introduction.
  columns=document.createElement('div');columns.className='columns';columns.innerHTML='<div class="column"></div><div class="column"></div>';area.append(columns);ci=0;col=columns.children[0];
  for(const [idx,s] of [...source.slice(1),reviewNode,credits].entries()){
   const label=idx<2?'0.'+(idx+2):idx===2?'Review and Exercises':'Sources and adaptations';const title=idx<2?s.querySelector('header h1').textContent:label;sectionLabel=title;
   if(idx!==0||columns.getBoundingClientRect().height<220)newPage(title);const head=document.createElement('h1');head.className='section-title';head.innerHTML=idx<2?`<small>SECTION ${label}</small>`:'';head.append(document.createTextNode(title));area.insertBefore(head,columns);
   stats.sections.push({label,page:Number(sheet.querySelector('.folio').textContent)});
   if(idx>=2)s.querySelector('h1')?.remove();
   const blocks=flatten(s);const objective=blocks.find(e=>e.matches('.objectives'));if(objective){blocks.splice(blocks.indexOf(objective),1);blocks.unshift(objective);}const figures=blocks.filter(e=>e.matches('figure'));const scheduled=new Set();if(idx===0){for(const f of figures.slice(0,2)){pending.push(f);scheduled.add(f);}}
   for(const e of blocks)audit(e);
   for(const e of blocks){
    if(e.matches('.objectives')){place(e);continue;}
    if(e.matches('figure')){if(!scheduled.has(e)){pending.push(e);scheduled.add(e);flushFloats();}continue;}
    for(const a of e.querySelectorAll('a[href]')){const id=a.getAttribute('href').split('#')[1];const f=figures.find(f=>f.id===id);if(f&&!scheduled.has(f)){pending.push(f);scheduled.add(f);}}
    if(idx===0&&[...e.querySelectorAll('a[href]')].some(a=>a.getAttribute('href').endsWith('#'+figures[1].id))){for(const f of figures.slice(2,4))if(!scheduled.has(f)){pending.push(f);scheduled.add(f);}}
    flushFloats();
    if(e.matches('.note')&&e.textContent.includes('The Scientific Method')){e.classList.add('sidebar');widePending.push(e);continue;}

    const table=e.matches('table')?e:e.querySelector('table');
    if(table){
     // Tables use both columns, with repeated headers if the table spans sheets.
     while(pending.length)nextColumn();
     if(col.children.length||ci){widePending.push(e);continue;}
     e.classList.add('wide');area.insertBefore(e,columns);
     if(columns.getBoundingClientRect().height<100){
      stats.overflows.push({type:'large-table',id:e.id,height:e.getBoundingClientRect().height});
     }
     continue;
    }
    place(e);
   }
   while(pending.length||widePending.length)nextColumn();
  }
  staging.remove();
  // Supply a blank verso when needed so the next chapter starts on a recto.
  stats.blankLastPage=document.querySelectorAll('.sheet').length%2===1;
  if(stats.blankLastPage){const blank=document.createElement('div');blank.className='sheet';blank.innerHTML='<div class="area"></div>';document.body.append(blank);}

  // Mark and report actual horizontal overflow, without changing source mathematics.
  for(const c of document.querySelectorAll('.column'))for(const e of c.querySelectorAll('math,table,img')){const r=e.getBoundingClientRect(),b=c.getBoundingClientRect();if(r.right>b.right+1||r.left<b.left-1)stats.overflows.push({type:'horizontal',id:e.closest('[id]')?.id,text:e.textContent.slice(0,120),width:r.width,available:b.width});}
  stats.objectivePlacementFailures=[...document.querySelectorAll('.section-title')].filter(h=>{
   const a=h.closest('.area'), cols=a.querySelector('.columns'), objective=cols?.querySelector('.objectives');
   if(!objective)return false;
   return h.nextElementSibling!==cols || cols.firstElementChild.firstElementChild!==objective;
  }).map(h=>h.textContent);
  stats.equationLabelCollisions=[...document.querySelectorAll('.equation')].filter(e=>{
   const label=e.querySelector('.eq-label');if(!label?.textContent.trim())return false;
   const b=label.getBoundingClientRect();return [...e.querySelectorAll('math,.equation-qualifier')].some(m=>{const r=m.getBoundingClientRect();return r.right>b.left-3&&r.left<b.right&&r.bottom>b.top&&r.top<b.bottom;});
  }).map(e=>({id:e.id,label:e.querySelector('.eq-label').textContent}));
  stats.contentFailures=[];for(let i=0;i<audited.length;i++){const actual=[...document.querySelectorAll('[data-audit-key=\"'+i+'\"]')].map(e=>{const c=e.cloneNode(true);c.querySelectorAll('.continuation').forEach(x=>x.remove());return c.textContent.replace(/\s+/g,'');}).join('');if(actual!==audited[i])stats.contentFailures.push(i);}
  stats.punctuationGroupsPreserved=JSON.stringify(expectedPunctuation)===JSON.stringify([...document.querySelectorAll('.math-with-punctuation')].map(e=>e.outerHTML).sort());
  stats.tableHeaderFootnotes=document.querySelectorAll('th .footnote').length;
  stats.mathPreserved=JSON.stringify(expectedMath)===JSON.stringify([...document.querySelectorAll('math')].map(e=>e.outerHTML).sort());
  stats.figureAreaByPage=[...document.querySelectorAll('.sheet')].map((p,i)=>({page:i+1,fraction:[...p.querySelectorAll('figure')].reduce((sum,f)=>sum+f.getBoundingClientRect().width*f.getBoundingClientRect().height,0)/(p.querySelector('.area').getBoundingClientRect().width*p.querySelector('.area').getBoundingClientRect().height)}));
  stats.pages=document.querySelectorAll('.sheet').length;stats.renderedImages=document.images.length;stats.brokenImages=[...document.images].filter(i=>!i.naturalWidth).map(i=>i.src);
  // Web transforms were measured before print pagination; remeasure at print size.
  for(const mark of document.querySelectorAll('.sentence-punctuation')){
   const anchor=mark.parentElement.querySelector('[data-sentence-punctuation-anchor]');if(!anchor)continue;
   let baseline=mark.querySelector('.sentence-baseline');
   if(!baseline){baseline=document.createElement('span');baseline.className='sentence-baseline';baseline.setAttribute('aria-hidden','true');mark.append(baseline);}
   mark.style.transform='none';const target=anchor.getBoundingClientRect();
   mark.style.transform=`translate(${target.left-mark.getBoundingClientRect().left}px,${target.top-baseline.getBoundingClientRect().top}px)`;
  }
  return stats;
 },{review,origin});
 await page.emulateMedia({media:'print'});
 fs.writeFileSync(path.join(qa,'layout.json'),JSON.stringify(result,null,2));
 fs.writeFileSync(path.join(dist,'chapter-zero-print.html'),await page.content());
 await page.pdf({path:path.join(out,'v1.1-chapter-0-revised.pdf'),preferCSSPageSize:true,printBackground:true,tagged:true,timeout:240000});
 console.log(JSON.stringify(result));
 }finally{await browser.close();server.close();}
})().catch(e=>{console.error(e);server.close();process.exitCode=1;});
