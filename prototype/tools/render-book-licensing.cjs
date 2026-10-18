const {chromium}=require('playwright');
const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'../..'),qa=path.join(root,'reports/1.1/book-licensing-print');
const prev=JSON.parse(fs.readFileSync(path.join(root,'reports/1.1/index-print/layout.json'),'utf8'));
const startPage=prev.startPage+prev.pages;
(async()=>{fs.mkdirSync(qa,{recursive:true});const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
try{const page=await browser.newPage();await page.setContent(fs.readFileSync(path.join(root,'prototype/print-content/book-wide-licensing.html'),'utf8'));
const report=await page.evaluate(async startPage=>{
 const articles=[...document.querySelectorAll('article')];const expected=articles.map(e=>e.textContent);
 const style=document.createElement('style');style.textContent=`
 @page{size:Letter;margin:0}*{box-sizing:border-box}body{margin:0;color:#111;font:10.5pt/1.32 Georgia,serif}
 .sheet{width:8.5in;height:11in;padding:.6in .65in .65in 1in;position:relative;break-after:page}.sheet:last-child{break-after:auto}.sheet:nth-child(even){padding-left:.65in;padding-right:1in}
 .area{height:9.75in}.running{position:absolute;top:.29in;left:1in;right:.65in;border-bottom:.5pt solid #bbb;padding-bottom:5pt;color:#555;font:8pt Arial}.sheet:nth-child(even) .running{left:.65in;right:1in}
 .folio{position:absolute;bottom:.3in;right:.65in;font:9pt Arial}.sheet:nth-child(even) .folio{right:auto;left:.65in}
 h1{font:600 19pt Arial;margin:0 0 13pt}h2{font:600 11.5pt Arial;margin:13pt 0 6pt}p{margin:0 0 8pt}.subtitle{font:10pt Arial;margin-bottom:16pt;color:#555}a{color:inherit;text-decoration:none;border-bottom:.4pt solid #999}.link{font:9pt/1.5 Arial}blockquote{background:#f1f3f3;border-left:2pt solid #b4bebe;margin:0 0 9pt;padding:9pt 12pt}
 `;document.head.append(style);document.body.replaceChildren();
 articles.forEach((article,i)=>{const sheet=document.createElement('section');sheet.className='sheet';sheet.innerHTML='<div class="running">LICENSING AND ATTRIBUTION</div><div class="area"></div><div class="folio">'+(startPage+i)+'</div>';sheet.querySelector('.area').append(article);document.body.append(sheet);});
 await document.fonts.ready;
 const overflow=articles.filter(a=>a.getBoundingClientRect().bottom>a.parentElement.getBoundingClientRect().bottom+.5).length;
 if(overflow)throw Error('Page overflow');
 if(articles.some((a,i)=>a.textContent!==expected[i]))throw Error('Content changed');
 return {startPage,pages:articles.length,contentPreserved:true,overflow,links:document.querySelectorAll('a').length};
},startPage);
await page.pdf({path:path.join(root,'output/pdf/v1.1-licensing-attribution.pdf'),printBackground:true,preferCSSPageSize:true});
fs.writeFileSync(path.join(root,'prototype/dist/course-full/licensing-attribution-print.html'),await page.content());
fs.writeFileSync(path.join(qa,'layout.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report));
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exitCode=1;});
