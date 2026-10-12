const {chromium}=require('playwright');
const fs=require('fs'),path=require('path'),assert=require('assert');
const root=path.resolve(__dirname,'../..'),dist=path.join(root,'prototype/dist/course-full');
(async()=>{
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 const context=await browser.newContext({viewport:{width:482,height:716}});
 await context.route('http://preview/**',r=>{
  let f=path.join(dist,decodeURIComponent(new URL(r.request().url()).pathname));
  if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');
  if(!fs.existsSync(f))return r.abort();
  return r.fulfill({body:fs.readFileSync(f),contentType:({'.html':'text/html','.css':'text/css','.js':'application/javascript','.svg':'image/svg+xml','.jpg':'image/jpeg','.png':'image/png'})[path.extname(f)]||'application/octet-stream'});
 });
 const page=await context.newPage(),errors=[];page.on('pageerror',e=>errors.push(String(e)));
 await page.goto('http://preview/sections/simultaneity-and-time-dilation/');
 const snapshot=()=>page.evaluate(()=>({url:location.href,ids:[...document.querySelectorAll('[id]')].map(e=>e.id),math:[...document.querySelectorAll('math')].map(e=>e.outerHTML),text:document.querySelector('main').textContent}));
 const before=await snapshot();
 await page.getByLabel('Textbook numbering').selectOption('older');
 assert.equal(await page.locator('article > header .eyebrow').textContent(),'14.2');
 assert((await page.locator('main').textContent()).includes('Figure 14.2.3'));
 const changed=await snapshot();assert.equal(before.url,changed.url);assert.deepEqual(before.ids,changed.ids);assert.deepEqual(before.math,changed.math);
 const bad=await page.evaluate(()=>[...document.querySelectorAll('.eq-label')].filter(e=>{
  const obj=PHYSICS_NUMBERING.objects[e.closest('.equation')?.id];return obj&&e.textContent.trim()&&e.textContent!==`(${obj.older})`;
 }).map(e=>e.textContent));assert.deepEqual(bad,[]);
 await page.reload();assert.equal(await page.getByLabel('Textbook numbering').inputValue(),'older');
 await page.getByLabel('Textbook numbering').selectOption('course');assert.equal((await snapshot()).text,before.text);
 await page.getByLabel('Textbook numbering').selectOption('older');
 await page.goto('http://preview/exercises/special-relativity-exercises/');
 assert((await page.locator('h1').textContent()).includes('Chapter 14:'));
 assert.equal(await page.locator('.exercise').count(),39);
 assert((await page.locator('#summary').textContent()).includes('14.2:'));
 await page.goto('http://preview/search/?q=simultaneity');
 await page.waitForFunction(()=>document.querySelector('#search-results a'));
 assert((await page.locator('#search-results').textContent()).includes('14.2:'));
 await page.getByLabel('Textbook numbering').selectOption('course');
 await page.waitForFunction(()=>document.querySelector('#search-results').textContent.includes('13.3:'));
 const second=await context.newPage();await second.goto('http://preview/contents/');
 await page.getByLabel('Textbook numbering').selectOption('older');
 await second.waitForFunction(()=>document.documentElement.dataset.numbering==='older');
 assert((await second.locator('main').textContent()).includes('Chapter 15:'));
 // Introduction pages stay reachable through chapter links, while their duplicate
 // section entries are omitted only in CNX-aligned contents.
 assert.equal(await second.locator('.section-links > .chapter-introduction').count(),15);
 assert.equal(await second.locator('.section-links > .chapter-introduction:visible').count(),0);
 assert.equal(await second.locator('a.chapter-link:visible').count(),15);
 for (const entry of ['chapters/quantum-mechanics/','sections/introduction-to-quantum-mechanics/']) {
  await page.goto('http://preview/'+entry);
  const intro=page.locator('.chapter-contents .chapter-introduction');
  assert.equal(await intro.count(),1);assert.equal(await intro.isVisible(),false);
  assert.equal(await page.locator('article .content').isVisible(),true);
  await page.getByLabel('Textbook numbering').selectOption('course');
  assert.equal(await intro.isVisible(),true);
  assert((await intro.textContent()).startsWith('12.1:'));
  await second.waitForFunction(()=>document.documentElement.dataset.numbering==='course');
  assert.equal(await second.locator('.chapter-introduction:visible').count(),15);
  await page.getByLabel('Textbook numbering').selectOption('older');
 }
 await page.goto('http://preview/sections/simultaneity-and-time-dilation/');
 assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
 await page.screenshot({path:path.join(root,'reports/1.1/numbering-toggle/older-mobile.png')});
 const registry=JSON.parse(fs.readFileSync(path.join(dist,'identity-registry.json'),'utf8'));
 let checked=0;
 for(const [mid,section] of Object.entries(registry)) {
  await page.goto('http://preview/sections/'+section.slug+'/');
  const failures=await page.evaluate(mid=>{
   const failures=[],expected=PHYSICS_NUMBERING.modules[mid];
   if(expected&&document.querySelector('article > header .eyebrow').textContent!==expected.older)failures.push('heading');
   for(const e of document.querySelectorAll('.eq-label')){
    const obj=PHYSICS_NUMBERING.objects[e.closest('.equation')?.id];
    if(obj&&e.textContent.trim()&&e.textContent!==`(${obj.older})`)failures.push('equation '+e.textContent);
   }
   for(const [key,value] of Object.entries(PHYSICS_NUMBERING.labels)){
    const kind=key.split(' ')[0];if(physicsNumbering.translate(key)!==kind+' '+value)failures.push(key);
   }
   return failures;
  },mid);
  assert.deepEqual(failures,[],mid);checked++;
 }
 const fallback=await browser.newContext({javaScriptEnabled:false});
 await fallback.route('http://preview/**',async r=>{
  const u=new URL(r.request().url());let f=path.join(dist,u.pathname);if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');
  return fs.existsSync(f)?r.fulfill({body:fs.readFileSync(f),contentType:f.endsWith('.html')?'text/html':'application/octet-stream'}):r.abort();
 });
 const plain=await fallback.newPage();await plain.goto('http://preview/sections/simultaneity-and-time-dilation/');
 assert.equal(await plain.locator('article > header .eyebrow').textContent(),'13.3');
 await fallback.close();
 assert.deepEqual(errors,[]);
 fs.writeFileSync(path.join(root,'reports/1.1/numbering-toggle/browser-check.json'),JSON.stringify({status:'passed',sectionsChecked:checked,checks:['same URL and anchors','unchanged MathML','section headings','all object label translations','figure labels','equation labels','exact round trip','reload persistence','chapter review','39 unchanged exercises','summary headings','search results','cross-tab sync','mobile overflow','no-JavaScript default'],errors},null,2));
 await browser.close();console.log('Numbering toggle browser checks passed.');
})().catch(e=>{console.error(e);process.exit(1);});
