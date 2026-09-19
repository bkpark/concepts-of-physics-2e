// Full course PDF, derived from the canonical HTML; source XML is never edited.
const {chromium}=require('playwright');
const fs=require('fs'),path=require('path'),http=require('http'),crypto=require('crypto');
const root=path.resolve(__dirname,'../..');
const release=JSON.parse(fs.readFileSync(path.join(root,'metadata/release.json'),'utf8'));
const releasing=process.argv.includes('--release');
if(releasing){const lock=JSON.parse(fs.readFileSync(path.join(root,'metadata/render-environment.lock.json'),'utf8'));for(const f of lock.files)if(crypto.createHash('sha256').update(fs.readFileSync(f.path)).digest('hex')!==f.sha256)throw Error('Changed locked dependency: '+f.path);if(process.version!==lock.node_version||require('playwright/package.json').version!==lock.playwright_version)throw Error('Renderer runtime version differs from lock');console.log('Locked renderer and fonts verified.');}
const dist=releasing?path.join(root,'output/releases',release.release_id,'site'):path.join(root,'prototype/dist/course-full');
const output=releasing?path.join(root,'output/releases',release.release_id):path.join(root,'output/pdf');fs.mkdirSync(output,{recursive:true});
const qa=path.join(root,'prototype/qa');
const server=http.createServer((req,res)=>{const f=path.resolve(dist,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));if(!f.startsWith(dist+path.sep)||!fs.existsSync(f)){res.writeHead(404).end();return;}const types={'.html':'text/html','.css':'text/css','.js':'text/javascript','.png':'image/png','.jpg':'image/jpeg','.svg':'image/svg+xml'};res.setHeader('Content-Type',types[path.extname(f)]||'application/octet-stream');fs.createReadStream(f).pipe(res);});
(async()=>{
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const origin=`http://127.0.0.1:${server.address().port}`;
 const browser=await chromium.launch({headless:true,executablePath:process.env.PROTOTYPE_CHROME||'C:/Program Files/Google/Chrome/Application/chrome.exe'});
 try{
 const page=await browser.newPage({viewport:{width:688,height:1000}});page.setDefaultTimeout(120000);
 const external=[],errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.route('**/*',r=>r.request().url().startsWith(origin)?r.continue():(external.push(r.request().url()),r.abort()));
 await page.goto(origin+'/book.html',{waitUntil:'networkidle',timeout:120000});await page.evaluate(()=>document.fonts.ready);
 const views=JSON.parse(fs.readFileSync(path.join(dist,'exercise-views.json'),'utf8'));
 const manifest=JSON.parse(fs.readFileSync(path.join(dist,'build-manifest.json'),'utf8'));
 for(const [mid,expected] of Object.entries(manifest.source_sha256)){const actual=crypto.createHash('sha256').update(fs.readFileSync(path.join(root,'maintained/modules',mid,'index.cnxml'))).digest('hex');if(actual!==expected)throw Error('Stale HTML build: rebuild course --all before printing '+mid);}
 const audit=await page.evaluate(({views,manifest})=>{
 const main=document.querySelector('main'),articles=[...main.querySelectorAll(':scope > article')];
 const initialIds=[...main.querySelectorAll('[id]')].map(e=>e.id).sort();
 const initialMath=main.querySelectorAll('math').length,initialImages=main.querySelectorAll('img').length;
 const id=(mid,s)=>mid+'--'+[...new TextEncoder().encode(s)].map(b=>b.toString(16).padStart(2,'0')).join('');
 const moved=[];
 for(const v of views){
  const group=document.createElement('article');group.id=v.id;group.className='chapter-exercises';
  const h=document.createElement('h1');h.textContent=v.label+' '+v.title;group.append(h);
  for(const category of ['conceptual-questions','problems-exercises']){
   const blocks=v.blocks.filter(b=>b.category===category);
   if(category==='conceptual-questions')for(const a of articles.filter(a=>String(manifest.section_labels[a.id]).split('.')[0]===v.chapter_label))for(const section of a.querySelectorAll('section'))if(section.querySelector(':scope > h3')?.textContent.trim()==='Conceptual Questions' && !blocks.some(b=>id(b.module,b.source_id)===section.id))blocks.push({module:a.id,source_id:new TextDecoder().decode(Uint8Array.from(section.id.split('--')[1].match(/../g).map(x=>parseInt(x,16))))});blocks.sort((a,b)=>articles.findIndex(x=>x.id===a.module)-articles.findIndex(x=>x.id===b.module));if(!blocks.length)continue;
   const heading=document.createElement('h2');heading.textContent=category==='conceptual-questions'?'Conceptual Questions':'Problems & Exercises';group.append(heading);
   for(const b of blocks){const e=document.getElementById(id(b.module,b.source_id));if(!e)throw Error('Missing exercise block '+b.source_id);
    const label=document.createElement('h3');label.textContent=manifest.section_labels[b.module]+' '+document.querySelector('#'+b.module+' > header h1').textContent;group.append(label,e);moved.push(b.source_id);}
  }
  const last=articles.filter(a=>String(manifest.section_labels[a.id]).split('.')[0]===v.chapter_label).at(-1);if(!last)throw Error('No chapter for '+v.id);last.after(group);
 }
 const cover=document.querySelector('.cover');cover.innerHTML='<h1>Introduction to Physics</h1><h2>Andrew Park</h2><p>Lecture-aligned numbering (July 2026)</p><p>Underlying content by Bobby Bailey, Andrew Park, OpenStax and James Rittenbach. Historical collection: CC BY 4.0. Original figure credits and section attributions are retained.</p><p>This edition uses the LibreTexts chapter and section numbering preserved in the July 7, 2026 course PDF. It matches the numbering called &ldquo;new LibreTexts chapter and section numbers&rdquo; in the recorded lectures for Physics 10 at College of Alameda. LibreTexts subsequently changed its numbering on September 17, 2026, so its current numbering may differ.</p><p>External videos and simulations require internet access.</p>';
 const credits=document.createElement('article');credits.id='attributions';credits.className='book-attributions';credits.innerHTML='<h1>Attribution and licenses</h1>';
 for(const a of articles){const f=a.querySelector('.attribution');const block=document.createElement('section');block.className='credit-block';const h=document.createElement('h2');h.textContent=(manifest.section_labels[a.id]?manifest.section_labels[a.id]+' ':'')+a.querySelector('h1').textContent;block.append(h,f);credits.append(block);}
 main.append(credits);
 const toc=document.createElement('article');toc.className='contents';toc.id='contents';toc.innerHTML='<h1>Contents</h1>';
 const ol=document.createElement('ol');
 for(const a of main.querySelectorAll(':scope > article')){const li=document.createElement('li'),link=document.createElement('a');link.href='#'+a.id;link.textContent=(manifest.section_labels[a.id]?manifest.section_labels[a.id]+' ':'')+a.querySelector('h1').textContent;li.append(link);ol.append(li);}
 toc.append(ol);cover.after(toc);
 document.title='Introduction to Physics';
 const finalIds=[...main.querySelectorAll('[id]')].map(e=>e.id);
 const lost=initialIds.filter(x=>!finalIds.includes(x));if(lost.length)throw Error('Lost anchors '+lost);
 const duplicates=finalIds.filter((x,i,a)=>a.indexOf(x)!==i);
 const brokenLinks=[...main.querySelectorAll('a[href^="#"]')].filter(a=>!document.getElementById(decodeURIComponent(a.hash.slice(1)))).map(a=>a.getAttribute('href'));
 const inlineExercises=articles.reduce((n,a)=>n+a.querySelectorAll('.exercise').length,0);const endExercises=main.querySelectorAll('.chapter-exercises .exercise').length;if(inlineExercises!==41||endExercises!==954)throw Error('Exercise placement mismatch');
 return {inline_exercises:inlineExercises,chapter_end_exercises:endExercises,modules:articles.length,moved_blocks:moved.length,math:initialMath,images:initialImages,final_math:main.querySelectorAll('math').length,final_images:main.querySelectorAll('img').length,lost,duplicates,brokenLinks};
 },{views,manifest});
 await page.addStyleTag({content:`@media print { .contents ol{list-style:none;padding:0;columns:2;column-gap:24px;font-size:9pt;line-height:1.25}.contents li{break-inside:avoid;margin:0 0 3px}.chapter-exercises > h2{margin-top:18px}.chapter-exercises .exercise{margin:14px 0;padding-top:8px}.attribution{margin-top:5px;padding-top:5px}.credit-block{break-inside:avoid;margin-bottom:16px}.book-attributions h2{font-size:11pt}.print-keep{break-inside:avoid}caption{break-after:avoid}h1,h2,h3{break-inside:avoid}.para{orphans:3;widows:3}math[display=block]{max-width:100%} .equation{overflow:visible} }`});
 await page.emulateMedia({media:'print'});
 await page.evaluate(()=>{for(const e of document.querySelectorAll('.table-wrap'))if(e.getBoundingClientRect().height<750)e.classList.add('print-keep');});
 const layout=await page.evaluate(()=>({brokenImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),overflow:[...document.querySelectorAll('math,table,img')].filter(e=>e.getBoundingClientRect().right>document.querySelector('main').getBoundingClientRect().right+2).map(e=>({tag:e.tagName,id:e.closest('[id]')?.id,key:e.closest('[data-math-key]')?.dataset.mathKey,right:e.getBoundingClientRect().right,width:e.getBoundingClientRect().width})),placeholders:document.querySelectorAll('.math-issue,.unavailable,merror').length}));
 const html=await page.content();fs.writeFileSync(path.join(dist,'print-full.html'),html);
 console.log(JSON.stringify({audit,layout}));
 if(audit.duplicates.length||audit.brokenLinks.length||audit.math!==audit.final_math||audit.images!==audit.final_images||layout.brokenImages.length||layout.placeholders||errors.length)throw Error('Preprint validation failed');
 if(!process.argv.includes('--check'))await page.pdf({path:path.join(output,releasing?release.pdf_filename:'introduction-to-physics-course.pdf'),format:'Letter',preferCSSPageSize:true,printBackground:true,displayHeaderFooter:true,headerTemplate:'<div></div>',footerTemplate:'<div style="font-size:8px;width:100%;text-align:center;color:#54656c">Introduction to Physics · <span class="pageNumber"></span> / <span class="totalPages"></span></div>',tagged:true,outline:true,timeout:240000});
 fs.writeFileSync(path.join(qa,'course-full-print.json'),JSON.stringify({browser:browser.version(),playwright:require('playwright/package.json').version,source_sha256:manifest.source_sha256,external,errors,audit,layout},null,2)+'\n');
 console.log(process.argv.includes('--check')?'Preprint checks passed; existing PDF unchanged.':'Created '+path.join(output,releasing?release.pdf_filename:'introduction-to-physics-course.pdf'));
 }finally{await browser.close();server.close();}
})().catch(e=>{console.error(e);server.close();process.exitCode=1;});
