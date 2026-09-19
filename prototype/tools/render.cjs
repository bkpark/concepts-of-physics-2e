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
for(const profile of ['cnx','course']){
 const ids=JSON.parse(fs.readFileSync(path.join(dist,profile,'identity-registry.json')));
 for(const [mid,entry] of Object.entries(ids)){
  const page=await context.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.goto(`${origin}/${profile}/sections/${entry.slug}/index.html`);await page.waitForFunction(()=>window.mathReady===true,{},{timeout:60000});
  await page.evaluate(()=>document.fonts.ready);
  const audit=await page.evaluate(()=>({mathWrappers:document.querySelectorAll('[data-math-key]').length,renderedMath:document.querySelectorAll('math').length,mathErrors:[...document.querySelectorAll('merror')].map(e=>({key:e.closest('[data-math-key]')?.dataset.mathKey,message:e.textContent})),unresolved:[...document.querySelectorAll('.math-issue')].map(e=>e.dataset.mathKey),brokenImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),overflow:[...document.querySelectorAll('math,table,img')].filter(e=>e.getBoundingClientRect().right>document.querySelector('main').getBoundingClientRect().right+2).map(e=>({tag:e.tagName,key:e.closest('[data-math-key]')?.dataset.mathKey})),duplicateIds:[...document.querySelectorAll('[id]')].map(e=>e.id).filter((x,i,a)=>a.indexOf(x)!==i)}));
  const expectedSymbol=await page.evaluate(()=>{const e=[...document.querySelectorAll('math mi,math mn')].find(e=>e.textContent.trim());const r=document.createRange();r.selectNodeContents(e);getSelection().removeAllRanges();getSelection().addRange(r);return e.textContent;});
  await page.keyboard.press('Control+c');const copiedSymbol=await page.evaluate(()=>navigator.clipboard.readText());
  if(copiedSymbol.trim()!==expectedSymbol.trim())throw Error('Native symbol copying failed '+mid);
  await page.locator('.math-copy-toolbar button').click();await page.waitForFunction(()=>document.querySelector('.math-copy-toolbar [role=status]').textContent==='MathML copied.');
  const copiedMath=await page.evaluate(()=>navigator.clipboard.readText());
  if(!copiedMath.startsWith('<math')||!copiedMath.includes('</math>'))throw Error('Structured math copying failed '+mid);
  audit.clipboard={symbol:true,whole_mathml:true};await page.evaluate(()=>getSelection().removeAllRanges());
  if(profile==='cnx')await page.screenshot({path:path.join(qa,mid+'-web.png')});
  result.pages.push({profile,module:mid,errors,...audit});await page.close();
 }
 const page=await context.newPage();await page.goto(`${origin}/${profile}/book.html`);await page.waitForFunction(()=>window.mathReady===true,{},{timeout:60000});await page.evaluate(()=>document.fonts.ready);
 const out=path.join(root,'output');fs.mkdirSync(out,{recursive:true});
 await page.pdf({path:path.join(out,`introduction-to-physics-maintained-${profile}.pdf`),format:'Letter',preferCSSPageSize:true,printBackground:true,displayHeaderFooter:true,headerTemplate:'<div></div>',footerTemplate:'<div style="font-size:8px;width:100%;text-align:center;color:#54656c">Introduction to Physics · Fidelity prototype · <span class="pageNumber"></span> / <span class="totalPages"></span></div>',tagged:true,outline:true});
 await page.close();
}
fs.writeFileSync(path.join(qa,'browser-audit.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result,null,2));
}finally{await browser.close();server.close();}
})().catch(e=>{console.error(e);server.close();process.exitCode=1;});
