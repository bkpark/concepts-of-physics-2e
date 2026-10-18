const {chromium}=require('playwright');
const fs=require('fs'),path=require('path'),assert=require('assert');
(async()=>{
const root=process.cwd(),dist=path.join(root,'prototype/dist/course-full');
const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
const page=await browser.newPage();
await page.route('http://preview/**',r=>{let f=path.join(dist,new URL(r.request().url()).pathname);if(fs.existsSync(f)&&fs.statSync(f).isDirectory())f=path.join(f,'index.html');return fs.existsSync(f)?r.fulfill({body:fs.readFileSync(f),contentType:({'.html':'text/html','.css':'text/css','.js':'application/javascript','.jpg':'image/jpeg','.png':'image/png'})[path.extname(f)]||'application/octet-stream'}):r.abort();});

for(const width of [694]){
await page.setViewportSize({width,height:900});
await page.goto('http://preview/sections/fusion/');
for(const id of ['eip-817']){
const eq=page.locator('#m52480--'+Buffer.from(id).toString('hex'));
assert.equal(await eq.locator('mtr').count(),2);
const xs=await eq.locator('mo').filter({hasText:/^=$/}).evaluateAll(es=>es.map(e=>e.getBoundingClientRect().x));
assert(Math.abs(xs[0]-xs[1])<1,JSON.stringify(xs));
await eq.screenshot({path:path.join(root,'reports/1.1/greek-particle-plurals/'+id+'-'+width+'.png')});
}}
await browser.close();console.log('Energy equation equals signs align at 694 pixels.');
})().catch(e=>{console.error(e);process.exit(1)});
