const {chromium}=require('playwright');
const fs=require('fs'),path=require('path'),assert=require('assert');
(async()=>{
 const dir=__dirname;
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 const page=await browser.newPage();
 const failures=[]; const measurements=[];
 page.on('pageerror',e=>failures.push(String(e)));
 for(const width of [627,1100]){
  await page.setViewportSize({width,height:900});
  await page.goto('file:///'+path.join(dir,'applied.html').replaceAll('\\','/'));
  await page.evaluate(()=>document.fonts.ready);
  const rows=await page.locator('article').evaluateAll(es=>es.map(e=>{
   const b=e.querySelector('.before math'),a=e.querySelector('.after math');
   return {id:e.id,before:b?.getBoundingClientRect().width,after:a?.getBoundingClientRect().width,height:a?.getBoundingClientRect().height,errors:e.querySelectorAll('merror').length};
  }));
  assert.equal(rows.length,611);
  for(const r of rows)assert(r.after>0&&r.height>0&&!r.errors,JSON.stringify(r));
  measurements.push({width,rows});
 }
 // A visual sample spanning every repair category; all 611 render above.
 const ids=['m42238-0034','m52314-0015','m67128-0029','m71411-0038','m71584-0010','m68327-0019'];
 await page.evaluate(ids=>{for(const a of document.querySelectorAll('article'))if(!ids.includes(a.id))a.remove();},ids);
 await page.screenshot({path:path.join(dir,'applied-sample.png'),fullPage:true});
 fs.writeFileSync(path.join(dir,'render-check.json'),JSON.stringify({expressions:611,widths:[627,1100],failures,measurements},null,2));
 assert.equal(failures.length,0);
 await browser.close();console.log('All 611 expressions rendered at 627px and 1100px; no MathML/browser errors.');
})().catch(e=>{console.error(e);process.exit(1)});
