const {chromium}=require('playwright');
const fs=require('fs'),path=require('path'),assert=require('assert');
const root=path.resolve(__dirname,'../..'),dist=path.join(root,'prototype/dist/course-full');
(async()=>{
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 const page=await browser.newPage();
 await page.route('http://preview/**',r=>{
  let f=path.join(dist,new URL(r.request().url()).pathname);
  if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');
  return fs.existsSync(f)?r.fulfill({body:fs.readFileSync(f),contentType:({'.html':'text/html','.css':'text/css','.js':'application/javascript','.svg':'image/svg+xml'})[path.extname(f)]||'application/octet-stream'}):r.abort();
 });
 await page.goto('http://preview/chapters/quantum-mechanics/');
 const results=[];
 for(const width of [320,375,438,482,563,650,768,900,1200,1600]){
  await page.setViewportSize({width,height:800});
  const bounds=await page.evaluate(()=>{
   const rect=s=>{const r=document.querySelector(s).getBoundingClientRect();return {x:r.x,y:r.y,width:r.width,height:r.height};};
   return {links:rect('.header-links'),controls:rect('.header-controls'),numbering:rect('[aria-label="Textbook numbering"]'),theme:rect('[aria-label="Color theme"]')};
  });
  assert(Math.abs(bounds.numbering.y-bounds.theme.y)<1,'toggles share row at '+width);
  for(const r of Object.values(bounds))assert(r.x>=0&&r.x+r.width<=width+1,'fits at '+width);
  if(Math.abs(bounds.links.y-bounds.controls.y)>bounds.links.height){
   assert(Math.abs(bounds.controls.x+bounds.controls.width/2-width/2)<1,'centered controls at '+width);
  }
  const left=Math.min(bounds.links.x,bounds.controls.x),right=Math.max(bounds.links.x+bounds.links.width,bounds.controls.x+bounds.controls.width);
  assert(Math.abs((left+right)/2-width/2)<1,'centered header at '+width);
  results.push({width,...bounds});
  if([375,768,1600].includes(width))await page.screenshot({path:path.join(root,`reports/1.1/numbering-toggle/header-${width}.png`)});
 }
 await page.getByLabel('Textbook numbering').selectOption('older');
 assert.equal(await page.locator('.chapter-introduction').isVisible(),false);
 await page.getByLabel('Color theme').selectOption('dark');
 await page.reload();
 assert.equal(await page.getByLabel('Textbook numbering').inputValue(),'older');
 assert.equal(await page.getByLabel('Color theme').inputValue(),'dark');
 fs.writeFileSync(path.join(root,'reports/1.1/numbering-toggle/header-layout.json'),JSON.stringify({status:'passed',results},null,2));
 await browser.close();console.log('Header layout and both preferences passed.');
})().catch(e=>{console.error(e);process.exit(1);});
