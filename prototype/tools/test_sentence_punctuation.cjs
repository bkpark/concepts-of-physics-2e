const {chromium}=require('playwright');
const fs=require('fs');
const path=require('path');
const {pathToFileURL}=require('url');
(async()=>{
 const root=path.resolve(__dirname,'../..');
 const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
 const page=await browser.newPage();
 let checked=0;
 const errors=[];
 for(const width of [375,768,1280]){
  await page.setViewportSize({width,height:900});
  await page.goto(pathToFileURL(path.join(root,'prototype/dist/course-full/book.html')).href);
  await page.evaluate(()=>document.fonts.ready);
  await page.waitForFunction(()=>window.mathReady);
  const results=await page.locator('.sentence-punctuation').evaluateAll(marks=>marks.map(mark=>{
   const math=mark.parentElement.querySelector('math');
   const anchor=math.querySelector('[data-sentence-punctuation-anchor]');
   const a=(anchor||math).getBoundingClientRect(),p=mark.getBoundingClientRect();
   const expected=anchor?a.left:a.right;
   const table=anchor?.closest('mtable');
   const lastRow=table?.querySelector('mtr:last-child')?.getBoundingClientRect();
   return {key:math.parentElement.dataset.mathKey,mark:mark.textContent,
    outside:!mark.closest('math'), horizontal:Math.abs(p.left-expected)<2,
    vertical:!lastRow||(p.top<lastRow.bottom&&p.bottom>lastRow.top),
    copy:math.parentElement.dataset.copyLatex,coords:{expected,left:p.left,top:p.top,rowTop:lastRow?.top,rowBottom:lastRow?.bottom}};
  }));
  checked+=results.length;
  errors.push(...results.filter(r=>!r.outside||!r.horizontal||!r.vertical).map(r=>({width,...r})));
 }
 const out=path.join(root,'reports/1.1/math-sentence-punctuation');
 await page.setViewportSize({width:768,height:900});
 for(const [slug,id,file] of [
  ['bohrs-theory-of-the-hydrogen-atom','m67807--6569702d383636','bohr'],
  ['uncertainty-principle','m67804--6569702d363639','multiline']]){
  await page.goto(pathToFileURL(path.join(root,'prototype/dist/course-full/sections',slug,'index.html')).href);
  await page.evaluate(()=>document.fonts.ready);
  await page.locator('#'+id).screenshot({path:path.join(out,file+'.png')});
 }
 fs.writeFileSync(path.join(out,'browser-validation.json'),JSON.stringify({checked,widths:[375,768,1280],errors},null,2));
 console.log(JSON.stringify({checked,errors:errors.slice(0,5),errorCount:errors.length}));
 await browser.close();
 if(errors.length)process.exit(1);
})().catch(e=>{console.error(e);process.exit(1)});
