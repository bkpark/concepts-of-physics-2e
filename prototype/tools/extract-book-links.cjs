// Recover all source anchors, including cross-document links Chrome omitted in proofs.
const {chromium}=require('playwright');const fs=require('fs'),path=require('path'),http=require('http');
const root=path.resolve(__dirname,'../..'),dist=path.join(root,'prototype/dist/course-full'),qa=path.join(root,'reports/1.1/full-book');
const plan=JSON.parse(fs.readFileSync(path.join(qa,'components.json'),'utf8'));
const server=http.createServer((req,res)=>{const f=path.resolve(dist,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));if(!f.startsWith(dist+path.sep)||!fs.existsSync(f)){res.writeHead(404).end();return;}res.setHeader('Content-Type',({'.html':'text/html','.png':'image/png','.jpg':'image/jpeg','.svg':'image/svg+xml','.css':'text/css'})[path.extname(f)]||'application/octet-stream');fs.createReadStream(f).pipe(res);});
(async()=>{await new Promise(r=>server.listen(0,'127.0.0.1',r));const origin=`http://127.0.0.1:${server.address().port}`;const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});const output=[];
try{const page=await browser.newPage({viewport:{width:1050,height:1200}});
for(const part of plan.parts.filter(p=>p.html)){
 let source=fs.readFileSync(path.join(dist,part.html),'utf8').replace(/http:\/\/127\.0\.0\.1:\d+/g,origin);
 await page.setContent(source,{waitUntil:'load'});await page.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(i=>i.complete?Promise.resolve():new Promise(r=>{i.onload=r;i.onerror=r;})));});
 const result=await page.evaluate(part=>{
 const sheets=[...document.querySelectorAll('.sheet')];if(sheets.length!==part.pages)throw Error('Page count mismatch '+part.key);
 const ids=[],links=[],badImages=[...document.images].filter(i=>!i.naturalWidth).map(i=>i.src);
 for(let n=0;n<sheets.length;n++){const s=sheets[n],sb=s.getBoundingClientRect(),globalPage=part.offset+n;
  for(const e of s.querySelectorAll('[id]')){const b=e.getBoundingClientRect();if(!b.width&&!b.height)continue;ids.push({id:e.id,page:globalPage,y:792-(b.top-sb.top)*.75});}
  for(const a of s.querySelectorAll('a[href]')){const href=a.getAttribute('href');const rects=[...a.getClientRects()].filter(r=>r.width>.1&&r.height>.1).map(r=>[.75*(r.left-sb.left),792-.75*(r.bottom-sb.top),.75*(r.right-sb.left),792-.75*(r.top-sb.top)]);links.push({page:globalPage,href,text:a.textContent.trim(),rects});}
  if(part.key==='copyright'){const e=[...s.querySelectorAll('strong')].find(e=>e.textContent.includes('Licensing and Attribution'));if(e){const r=e.getBoundingClientRect();links.push({page:globalPage,href:'https://book-front.invalid/body/641',text:e.textContent,rects:[[.75*(r.left-sb.left),792-.75*(r.bottom-sb.top),.75*(r.right-sb.left),792-.75*(r.top-sb.top)]]});}}
 }
 return {key:part.key,ids,links,badImages};
 },part);
 if(result.badImages.length)throw Error('Images not loaded '+part.key+': '+result.badImages.join(','));output.push(result);console.log(part.key,result.ids.length,'targets',result.links.length,'links');
}
fs.writeFileSync(path.join(qa,'dom-links.json'),JSON.stringify(output));
}finally{await browser.close();server.close();}})().catch(e=>{console.error(e);process.exitCode=1;server.close();});
