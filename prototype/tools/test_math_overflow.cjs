const assert=require('node:assert/strict');
const {chromium}=require('playwright');
(async()=>{
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 try{
  const page=await browser.newPage();
  await page.goto('http://127.0.0.1:8765/prototype/dist/course-full/sections/magnetic-field-strength-force-on-a-moving-charge-in-a-magnetic-field/');
  await page.evaluate(()=>document.fonts.ready);
  for(const colorScheme of ['light','dark']) for(const width of [390,630,650,651,815]){
   await page.emulateMedia({colorScheme});await page.setViewportSize({width,height:1000});
   await page.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))));
   const bad=await page.locator('[data-math-key]').evaluateAll(es=>es.filter(e=>['auto','scroll'].includes(getComputedStyle(e).overflowY)).map(e=>e.dataset.mathKey));
   assert.deepEqual(bad,[],`${colorScheme} ${width}: vertical scroll containers`);
   const display=await page.locator('[data-math-key]:has(> math[display="block"])').evaluateAll(es=>es.every(e=>getComputedStyle(e).display==='block'));
   assert(display,`${width}: display equations must remain block`);
  }
  // Wide expressions retain horizontal access and recover when space increases.
  await page.setViewportSize({width:390,height:1000});
  await page.evaluate(()=>{const e=document.createElement('span');e.id='overflow-fixture';e.className='math-with-punctuation';e.innerHTML='<span style="display:inline-block;width:500px;height:50px">wide equation fixture</span>.';document.querySelector('main').append(e);});
  await page.addScriptTag({content:'(()=>{ // Keep ordinary math ink visible;'+require('node:fs').readFileSync('prototype/copy-math.js','utf8').split('// Keep ordinary math ink visible;')[1]+'\n})();'});
  await page.waitForFunction(()=>document.querySelector('#overflow-fixture').classList.contains('math-needs-scroll'));
  assert.equal(await page.locator('#overflow-fixture').evaluate(e=>getComputedStyle(e).overflowY),'hidden');
  await page.setViewportSize({width:1000,height:1000});
  await page.waitForFunction(()=>!document.querySelector('#overflow-fixture').classList.contains('math-needs-scroll'));
  console.log('Passed: five widths, light/dark, block layout, horizontal overflow and resize recovery.');
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
