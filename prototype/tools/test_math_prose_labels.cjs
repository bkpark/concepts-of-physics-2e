const {chromium}=require('playwright');
const fs=require('fs');const path=require('path');const {pathToFileURL}=require('url');
(async()=>{
 const root=path.resolve(__dirname,'../..'),site=path.join(root,'prototype/dist/course-full');
 const registry=JSON.parse(fs.readFileSync(path.join(site,'identity-registry.json'),'utf8'));
 const fixes=JSON.parse(fs.readFileSync(path.join(root,'reports/1.1/math-prose-labels/applied.json'),'utf8'));
 const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
 const page=await browser.newPage();let checked=0;
 for(const width of [375,1024]){
  await page.setViewportSize({width,height:900});
  for(const fix of fixes){
   const url=pathToFileURL(path.join(site,'sections',registry[fix.module].slug,'index.html')).href;
   await page.goto(url);await page.evaluate(()=>document.fonts.ready);
   const key=fix.module+'-math-'+String(fix.math_index).padStart(4,'0');
   const result=await page.locator(`[data-math-key="${key}"]`).evaluate((el,label)=>{
    const norm=s=>s.replace(/\s+/g,' ').trim();
    return {inMath:norm(el.textContent).includes(norm(label)),inCopy:norm(el.dataset.copyLatex).includes(norm(label)),inPage:norm(document.body.textContent).includes(norm(label))};
   },fix.label);
   if(result.inMath||result.inCopy||!result.inPage)throw Error(JSON.stringify({fix,result}));
   checked++;
   if(width===1024&&['m67037','m67124','m78798'].includes(fix.module)){
    const group=page.locator(`[data-math-key="${key}"]`).locator('..');
    await group.screenshot({path:path.join(root,'reports/1.1/math-prose-labels',fix.module+'-'+fix.math_index+'.png')});
   }
  }
 }
 const report={checked,widths:[375,1024],labels:fixes.length,errors:[]};
 fs.writeFileSync(path.join(root,'reports/1.1/math-prose-labels/browser-validation.json'),JSON.stringify(report,null,2));
 console.log(JSON.stringify(report));await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
