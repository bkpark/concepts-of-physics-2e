const {chromium}=require('playwright');
const fs=require('fs'),path=require('path'),assert=require('assert');
(async()=>{
const root=process.cwd(),dist=path.join(root,'prototype/dist/course-full');
const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
const page=await browser.newPage();
await page.route('http://preview/**',r=>{let f=path.join(dist,new URL(r.request().url()).pathname);if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');return fs.existsSync(f)?r.fulfill({body:fs.readFileSync(f),contentType:({'.html':'text/html','.css':'text/css','.js':'application/javascript','.jpg':'image/jpeg','.png':'image/png'})[path.extname(f)]||'application/octet-stream'}):r.abort();});

for(const width of [390,1200]){
await page.setViewportSize({width,height:900});await page.goto('http://preview/sections/fusion/');
for(const id of ['eip-789','eip-495','eip-866','eip-983','eip-494','eip-522','eip-540','eip-573','eip-816','eip-291']){
const eq=page.locator('#m52480--'+Buffer.from(id).toString('hex'));
if(!await eq.count())continue; // Summary equations are on the separate review page.
assert.equal(await eq.locator('math').count(),2);
assert((await eq.locator('math').nth(1).textContent()).startsWith('Q='));
await eq.screenshot({path:path.join(root,'reports/1.1/greek-particle-plurals/fusion-'+id+'-'+width+'.png')});
}}
await browser.close();console.log('Fusion Q annotations rendered at 390 and 1200px.');
})().catch(e=>{console.error(e);process.exit(1)});
