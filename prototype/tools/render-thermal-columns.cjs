// Isolated Letter/two-column experiment; leaves canonical text and math untouched.
const {chromium}=require('playwright');
const fs=require('fs'),path=require('path'),http=require('http');
const root=path.resolve(__dirname,'../..'),dist=path.join(root,'prototype/dist/course-full');
const out=path.join(root,'output/pdf'),qa=path.join(root,'reports/1.1/thermal-two-column');
fs.mkdirSync(qa,{recursive:true});
const server=http.createServer((req,res)=>{const f=path.resolve(dist,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));if(!f.startsWith(dist+path.sep)||!fs.existsSync(f)){res.writeHead(404).end();return;}res.setHeader('Content-Type',({'.html':'text/html','.css':'text/css','.js':'text/javascript','.svg':'image/svg+xml'})[path.extname(f)]||'application/octet-stream');fs.createReadStream(f).pipe(res);});
(async()=>{
 await new Promise(r=>server.listen(0,'127.0.0.1',r));
 const origin=`http://127.0.0.1:${server.address().port}`;
 const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
 try {
 const page=await browser.newPage({viewport:{width:692,height:1000}});
 await page.route('**/*',r=>r.request().url().startsWith(origin)?r.continue():r.abort());
 await page.goto(origin+'/book.html',{waitUntil:'networkidle'});
 const manifest=JSON.parse(fs.readFileSync(path.join(dist,'build-manifest.json')));
 const inventory=await page.evaluate(manifest=>{
  const main=document.querySelector('main');
  for(const el of [...main.children])if(el.tagName!=='ARTICLE'||!String(manifest.section_labels[el.id]).startsWith('8.'))el.remove();
  const inv={sections:main.querySelectorAll(':scope > article').length,math:main.querySelectorAll('math').length,images:main.querySelectorAll('img').length};
  const credits=document.createElement('article');credits.className='credits';credits.innerHTML='<h1>Sources and adaptations</h1>';
  for(const article of main.querySelectorAll(':scope > article')){const f=article.querySelector('.attribution');if(f){const h=document.createElement('h3');h.textContent=article.querySelector('h1').textContent;credits.append(h,f);}}
  main.append(credits);
  return inv;
 },manifest);
 // Add the current chapter review page, which includes the website's exercise relocation.
 const exercise=await browser.newPage();
 // Static server does not resolve directory indexes.
 await exercise.goto(origin+'/exercises/thermal-physics-exercises/index.html',{waitUntil:'networkidle'});
 const review=await exercise.locator('main').innerHTML();await exercise.close();
 const blocks=JSON.parse(fs.readFileSync(path.join(dist,'exercise-views.json'))).find(v=>v.chapter_label==='8').blocks;
 await page.evaluate(blocks=>{for(const b of blocks){const id=b.module+'--'+[...new TextEncoder().encode(b.source_id)].map(x=>x.toString(16).padStart(2,'0')).join('');document.getElementById(id)?.remove();}},blocks);
 await page.evaluate(({review,origin})=>{const a=document.createElement('article');a.className='chapter-review';a.innerHTML=review;for(const el of a.querySelectorAll('[src]'))el.src=new URL(el.getAttribute('src'),origin+'/exercises/thermal-physics-exercises/').href;document.querySelector('.credits').before(a);for(const el of document.querySelectorAll('nav,.reading-navigation,.chapter-navigation,.numbering-toggle'))el.remove();},{review,origin});
 await page.addStyleTag({content:`
 @page{size:Letter;margin:.65in}
 :root{font-size:10.5pt!important;line-height:1.3!important;color:#111!important;background:white!important}
 body{background:white!important}main{width:7.2in;max-width:none!important;margin:0!important;padding:0!important;border:0!important;column-count:2;column-gap:.25in;column-fill:auto}
 article{break-before:auto!important;margin:0 0 14pt!important}h1{font-size:17pt!important;line-height:1.15;margin:12pt 0 8pt}h2{font-size:12pt}h3{font-size:11pt;margin:10pt 0 5pt}h1,h2,h3,.object-title{break-after:avoid;break-inside:avoid}
 .para{margin:6pt 0;orphans:2;widows:2}.example,.note,.objectives,.solution{padding:6pt;margin:9pt 0}.example,.note{box-decoration-break:clone}
 .object-title{font-size:9pt}.objectives{font-size:9pt}figure{padding:4pt;margin:9pt 0;break-inside:avoid}figure img{max-height:3in;max-width:100%!important}figcaption{font-size:8.5pt;line-height:1.25;margin-top:5pt}
 .equation{gap:5pt;margin:8pt 0;break-inside:avoid;overflow:visible}.eq-label{font-size:8pt}math{font-size:1em}mtd{padding:1px 2px}
 table{font-size:8pt}td,th{font-size:8pt;padding:3pt}.table-wrap{overflow:visible}.exercise{margin:8pt 0;padding-top:6pt}.attribution{font-size:8pt;line-height:1.25}
 .reading-navigation,nav,.theme-control,.math-copy-toolbar,.numbering-toggle{display:none!important}
 `});
 await page.emulateMedia({media:'print'});await page.evaluate(()=>document.fonts.ready);
 await page.evaluate(()=>Promise.all([...document.images].map(i=>i.decode().catch(()=>{}))));
 // Measure in a continuous single column of identical width to avoid fragmentation rectangles.
 const measure=await page.addStyleTag({content:'main{column-count:1!important;width:3.475in!important}'});
 const report=await page.evaluate(()=>{
 const math=[...document.querySelectorAll('main math')];
 const failures=math.map(e=>{const box=e.closest('.equation')?.querySelector(':scope > div')||e.closest('.para,td,th,li')||e.parentElement;const b=box.getBoundingClientRect(),r=e.getBoundingClientRect();const over=Math.max(0,b.left-r.left,r.right-b.right);return {key:e.closest('[data-math-key]')?.dataset.mathKey,id:e.closest('.equation')?.id||e.closest('[id]')?.id,label:e.closest('.equation')?.querySelector('.eq-label')?.textContent,text:e.textContent,width_px:r.width,available_px:b.width,overflow_px:over};}).filter(x=>x.overflow_px>1);
 return {math:math.length,display_equations:document.querySelectorAll('.equation').length,overflow:failures,brokenImages:[...document.images].filter(i=>!i.naturalWidth).map(i=>i.src)};
 });
 await measure.evaluate(e=>e.remove());
 fs.writeFileSync(path.join(dist,'thermal-two-column.html'),await page.content());
 await page.pdf({path:path.join(out,'v1.1-thermal-physics-two-column.pdf'),preferCSSPageSize:true,printBackground:true,displayHeaderFooter:true,headerTemplate:'<div></div>',footerTemplate:'<div style="font:8px Arial;width:100%;text-align:center">Thermal Physics · Two-column layout trial · <span class="pageNumber"></span></div>',tagged:true,timeout:240000});
 fs.writeFileSync(path.join(qa,'overflow.json'),JSON.stringify({settings:{paper:'Letter',margin_in:.65,gutter_in:.25,column_in:3.475,font_pt:10.5},inventory,...report},null,2));
 console.log(JSON.stringify({inventory,math:report.math,display_equations:report.display_equations,overflow:report.overflow.length,brokenImages:report.brokenImages}));
 }finally{await browser.close();server.close();}
})().catch(e=>{console.error(e);server.close();process.exitCode=1;});
