const {chromium}=require('playwright');
const fs=require('fs'),path=require('path'),assert=require('assert');
(async()=>{
const root=process.cwd(),dist=path.join(root,'prototype/dist/course-full');
const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
const page=await browser.newPage();
await page.route('http://preview/**',r=>{let f=path.join(dist,new URL(r.request().url()).pathname);if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');return fs.existsSync(f)?r.fulfill({body:fs.readFileSync(f),contentType:({'.html':'text/html','.css':'text/css','.js':'application/javascript','.jpg':'image/jpeg','.png':'image/png'})[path.extname(f)]||'application/octet-stream'}):r.abort();});
await page.goto('http://preview/sections/the-photoelectric-effect/');
const figure=page.locator('#m67251--696d706f72742d6175746f2d696431333632373636');
assert((await figure.textContent()).includes('Figure 12.3.2.'));
assert(await figure.locator('img').evaluate(i=>i.complete&&i.naturalWidth===1200&&i.naturalHeight===691));
for(const width of [390,1200]){await page.setViewportSize({width,height:900});await figure.scrollIntoViewIfNeeded();assert(await figure.evaluate(e=>e.getBoundingClientRect().right<=innerWidth));await figure.screenshot({path:path.join(root,`reports/1.1/photoelectric-photo/figure-${width}.png`)});}
await page.getByLabel('Textbook numbering').selectOption('older');assert((await figure.textContent()).includes('Figure 13.2.2.'));
fs.writeFileSync(path.join(root,'reports/1.1/photoelectric-photo/browser-check.json'),JSON.stringify({status:'passed',widths:[390,1200],imagePixels:[1200,691],lectureLabel:'12.3.2',cnxLabel:'13.2.2',captionAndAlt:'updated'},null,2));
await browser.close();console.log('Photo browser checks passed.');
})().catch(e=>{console.error(e);process.exit(1)});
