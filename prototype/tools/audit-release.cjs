// Verify the public release site at desktop and mobile widths, with network blocked.
const {chromium}=require('playwright'),fs=require('fs'),path=require('path'),http=require('http');
const root=path.resolve(__dirname,'../..'),rel=JSON.parse(fs.readFileSync(path.join(root,'metadata/release.json'),'utf8'));
const site=path.join(root,'output/releases',rel.release_id,process.argv.includes('--public')?'public':'site');
const server=http.createServer((req,res)=>{let f=path.resolve(site,'.'+decodeURIComponent(new URL(req.url,'http://local').pathname));if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');if(!f.startsWith(site+path.sep)||!fs.existsSync(f)){res.writeHead(404).end();return;}res.setHeader('Content-Type',({'.html':'text/html','.css':'text/css','.js':'text/javascript','.png':'image/png','.jpg':'image/jpeg','.svg':'image/svg+xml'})[path.extname(f)]||'application/octet-stream');fs.createReadStream(f).pipe(res);});
(async()=>{await new Promise(r=>server.listen(0,'127.0.0.1',r));const origin=`http://127.0.0.1:${server.address().port}`;const browser=await chromium.launch({headless:true,executablePath:process.env.PROTOTYPE_CHROME||'C:/Program Files/Google/Chrome/Application/chrome.exe'});const external=[],results=[];
try{
 const metadata=path.join(root,'output/releases',rel.release_id,'site');
 const registry=JSON.parse(fs.readFileSync(path.join(metadata,'identity-registry.json'),'utf8')),views=JSON.parse(fs.readFileSync(path.join(metadata,'exercise-views.json'),'utf8'));
 const targets=['index.html',...Object.values(registry).map(v=>`sections/${v.slug}/index.html`),...views.map(v=>`exercises/${v.slug}/index.html`)];
 const context=await browser.newContext({permissions:['clipboard-read','clipboard-write']});await context.route('**/*',r=>r.request().url().startsWith(origin)?r.continue():(external.push(r.request().url()),r.abort()));
 for(const width of [1280,390]){
 const page=await context.newPage();await page.setViewportSize({width,height:900});
 for(const target of targets){const errors=[];const error=e=>errors.push(e.message);page.on('pageerror',error);await page.goto(origin+'/'+target);await page.evaluate(()=>document.fonts.ready);
 const data=await page.evaluate(()=>({title:document.title,language:document.documentElement.lang,h1:document.querySelectorAll('h1').length,brokenImages:[...document.images].filter(x=>!x.complete||!x.naturalWidth).map(x=>x.getAttribute('src')),missingAlt:[...document.images].filter(x=>!x.hasAttribute('alt')||!x.alt.trim()).map(x=>x.getAttribute('src')),unnamedLinks:[...document.querySelectorAll('a')].filter(x=>!x.textContent.trim()&&!x.querySelector('img[alt]')).map(x=>x.getAttribute('href')),rootOverflow:document.documentElement.scrollWidth>innerWidth+2,duplicateIds:[...document.querySelectorAll('[id]')].map(x=>x.id).filter((x,i,a)=>a.indexOf(x)!==i),placeholders:document.querySelectorAll('.math-issue,.unavailable,merror').length,prototypeNotice:!!document.querySelector('.prototype-notice'),math:document.querySelectorAll('math').length}));
 results.push({width,target,errors,...data});page.off('pageerror',error);
 }
 await page.close();console.log('Checked '+targets.length+' pages at width '+width);
 }
 const page=await context.newPage();await page.goto(origin+'/sections/uncertainty-principle/index.html');await page.locator('math').first().focus();await page.locator('.math-copy-toolbar button').click();const copied=await page.evaluate(()=>navigator.clipboard.readText());const clipboard=copied.startsWith('<math')&&copied.includes('</math>');
 const failures=results.filter(x=>x.errors.length||x.brokenImages.length||x.unnamedLinks.length||x.rootOverflow||x.duplicateIds.length||x.placeholders||x.prototypeNotice||x.h1!==1||x.language!=='en');
 const report={release_id:rel.release_id,browser:browser.version(),pages:targets.length,widths:[1280,390],external_requests:external,structured_math_copy:clipboard,failures,results};fs.writeFileSync(path.join(root,'reports/release-browser-audit.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({failures,missing_alt:results.filter(x=>x.width===1280).reduce((n,x)=>n+x.missingAlt.length,0),clipboard}));
 if(failures.length||external.length||!clipboard)process.exitCode=1;
}finally{await browser.close();server.close();}
})().catch(e=>{console.error(e);server.close();process.exitCode=1;});
