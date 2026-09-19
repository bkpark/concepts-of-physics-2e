// Render local static builds with network requests blocked. Requires Playwright.
const {chromium}=require('playwright');
const fs=require('fs'), path=require('path'),http=require('http');
const root=path.resolve(__dirname,'..'), dist=path.join(root,'dist');
const qa=path.join(root,'qa');fs.mkdirSync(qa,{recursive:true});
const mime={'.html':'text/html','.css':'text/css','.js':'text/javascript','.json':'application/json','.jpg':'image/jpeg','.png':'image/png','.svg':'image/svg+xml'};
const server=http.createServer((req,res)=>{let name=decodeURIComponent(new URL(req.url,'http://localhost').pathname);let file=path.resolve(dist,'.'+name);if(!file.startsWith(dist+path.sep)){res.writeHead(403).end();return;}if(fs.existsSync(file)&&fs.statSync(file).isDirectory())file=path.join(file,'index.html');if(!fs.existsSync(file)){res.writeHead(404).end();return;}res.setHeader('Content-Type',mime[path.extname(file)]||'application/octet-stream');fs.createReadStream(file).pipe(res);});
(async()=>{
await new Promise(r=>server.listen(0,'127.0.0.1',r));const origin=`http://127.0.0.1:${server.address().port}`;
const browser=await chromium.launch({headless:true,executablePath:process.env.PROTOTYPE_CHROME||'C:/Program Files/Google/Chrome/Application/chrome.exe'});
const context=await browser.newContext({viewport:{width:1280,height:1000},deviceScaleFactor:1,permissions:['clipboard-read','clipboard-write']});
const external=[];await context.route('**/*',route=>{const u=route.request().url();if(!u.startsWith(origin)&&!u.startsWith('data:')){external.push(u);return route.abort();}return route.continue();});
const result={renderer:'native-mathml',browser:browser.version(),playwright:require('playwright/package.json').version,external_requests:external,pages:[]};
try{
for(const profile of ['course-full']){
 const ids=JSON.parse(fs.readFileSync(path.join(dist,profile,'identity-registry.json')));
 const views=JSON.parse(fs.readFileSync(path.join(dist,profile,'exercise-views.json')));
 const targets=[...Object.entries(ids).map(([mid,entry])=>[mid,`sections/${entry.slug}/index.html`]),...views.map(v=>[v.id,`exercises/${v.slug}/index.html`])];
 for(const [mid,relative] of targets){
  const page=await context.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.goto(`${origin}/${profile}/${relative}`);await page.waitForFunction(()=>window.mathReady===true,{},{timeout:60000});
  await page.evaluate(()=>document.fonts.ready);
  const audit=await page.evaluate(()=>({mathWrappers:document.querySelectorAll('[data-math-key]').length,renderedMath:document.querySelectorAll('math').length,mathErrors:[...document.querySelectorAll('merror')].map(e=>({key:e.closest('[data-math-key]')?.dataset.mathKey,message:e.textContent})),unresolved:[...document.querySelectorAll('.math-issue')].map(e=>e.dataset.mathKey),brokenImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),overflow:[...document.querySelectorAll('math,table,img')].filter(e=>e.getBoundingClientRect().right>document.querySelector('main').getBoundingClientRect().right+2).map(e=>({tag:e.tagName,key:e.closest('[data-math-key]')?.dataset.mathKey})),duplicateIds:[...document.querySelectorAll('[id]')].map(e=>e.id).filter((x,i,a)=>a.indexOf(x)!==i)}));
  if(['m78798','m52408','exercise-view:thermal-physics-exercises'].includes(mid))await page.screenshot({path:path.join(qa,'full-'+mid.replaceAll(':','-')+'.png')});
  result.pages.push({profile,module:mid,errors,...audit});await page.close();
 }
}
fs.writeFileSync(path.join(qa,'course-full-browser-audit.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({pages:result.pages.length,external:external.length,findings:result.pages.filter(p=>p.errors.length||p.mathErrors.length||p.brokenImages.length||p.overflow.length||p.duplicateIds.length).map(p=>({module:p.module,errors:p.errors,mathErrors:p.mathErrors,brokenImages:p.brokenImages,overflow:p.overflow,duplicateIds:p.duplicateIds}))},null,2));
}finally{await browser.close();server.close();}
})().catch(e=>{console.error(e);server.close();process.exitCode=1;});
