const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{
 const root=path.resolve(__dirname,'../..'),out=path.join(root,'reports/1.1/native-dark-theme');fs.mkdirSync(out,{recursive:true});
 const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
 async function localFiles(context){await context.route('http://127.0.0.1:8766/**',async route=>{let name=decodeURIComponent(new URL(route.request().url()).pathname);if(name.endsWith('/'))name+='index.html';const file=path.join(root,'prototype/dist/course-full',name);await route.fulfill({path:file});});}
 const context=await browser.newContext({colorScheme:'dark',viewport:{width:1024,height:900}});await localFiles(context);
 const page=await context.newPage(),errors=[];
 const base='http://127.0.0.1:8766';
 function assert(ok,message){if(!ok)throw Error(message);}
 for(const url of ['/','/sections/the-photoelectric-effect/','/sections/discovery-of-the-atomic-nucleus/','/exercises/light-exercises/','/search/']){
  await page.goto(base+url);await page.evaluate(()=>document.fonts.ready);
  assert(await page.locator('html').getAttribute('data-theme')==='dark','system dark');
  assert(await page.getByLabel('Color theme').inputValue()==='system','default preference');
  const colors=await page.evaluate(()=>({body:getComputedStyle(document.documentElement).color,main:getComputedStyle(document.querySelector('main')).backgroundColor}));
  assert(colors.main==='rgb(24, 34, 39)'&&colors.body==='rgb(228, 233, 235)','dark palette');
 }
 await page.goto(base+'/sections/the-photoelectric-effect/');
 await page.screenshot({path:path.join(out,'desktop-dark.png')});
 await page.getByLabel('Color theme').selectOption('light');
 await page.reload();assert(await page.locator('html').getAttribute('data-theme')==='light','persist light');
 await page.getByLabel('Color theme').selectOption('dark');
 await page.emulateMedia({colorScheme:'light'});assert(await page.locator('html').getAttribute('data-theme')==='dark','explicit dark overrides system');
 await page.getByLabel('Color theme').selectOption('system');assert(await page.locator('html').getAttribute('data-theme')==='light','system light');
 await page.emulateMedia({colorScheme:'dark'});await page.waitForFunction(()=>document.documentElement.dataset.theme==='dark');
 await page.setViewportSize({width:375,height:850});
 await page.screenshot({path:path.join(out,'mobile-dark.png')});
 assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'mobile overflow');
 const first=page.locator('[data-copy-latex] > math').first();await first.focus();await page.locator('.math-copy-trigger').click();
 assert(await page.locator('.math-copy-dialog').isVisible(),'copy dialog opens');
 assert(await page.locator('.math-copy-dialog textarea').evaluate(e=>getComputedStyle(e).backgroundColor)==='rgb(32, 46, 53)','dark dialog');
 await page.locator('.math-copy-close').click();
 await page.emulateMedia({media:'print'});
 assert(await page.locator('main').evaluate(e=>getComputedStyle(e).backgroundColor)==='rgb(255, 255, 255)','print remains white');
 assert(await page.locator('html').evaluate(e=>getComputedStyle(e).color)==='rgb(23, 43, 53)','print remains dark text');
 await context.close();
 const blocked=await browser.newContext({colorScheme:'dark'});await localFiles(blocked);await blocked.addInitScript(()=>Object.defineProperty(window,'localStorage',{get(){throw new Error('blocked')}}));
 const b=await blocked.newPage();await b.goto(base+'/');await b.getByLabel('Color theme').selectOption('light');assert(await b.locator('html').getAttribute('data-theme')==='light','blocked storage fallback');
 await browser.close();
 const result={status:'passed',checks:['system preference','explicit preference','persistence','system changes','blocked storage','five page types','mobile overflow','copy dialog','print light']};
 fs.writeFileSync(path.join(out,'validation.json'),JSON.stringify(result,null,2));console.log(JSON.stringify(result));
})().catch(e=>{console.error(e);process.exit(1)});
