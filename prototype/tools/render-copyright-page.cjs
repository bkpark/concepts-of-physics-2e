const {chromium}=require('playwright');
const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'../..'),qa=path.join(root,'reports/1.1/copyright-page-print');
(async()=>{fs.mkdirSync(qa,{recursive:true});const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
try{const page=await browser.newPage();await page.setContent(fs.readFileSync(path.join(root,'prototype/print-content/copyright-page.html'),'utf8'));
const report=await page.evaluate(async()=>{
 const article=document.querySelector('article'),expected=article.textContent;
 const style=document.createElement('style');style.textContent=`
 @page{size:Letter;margin:0}*{box-sizing:border-box}body{margin:0;color:#111;font:10pt/1.35 Georgia,serif}
 .sheet{width:8.5in;height:11in;padding:.75in 1in .8in .65in;display:flex;flex-direction:column;justify-content:flex-end}
 article{max-width:6.4in}h1{font:600 17pt Arial;margin:0 0 5pt}.edition{font:10pt Arial;margin:0 0 16pt;color:#555}p{margin:0 0 10pt}p:last-child{margin-bottom:0}a{color:inherit;text-decoration:none;border-bottom:.4pt solid #999}.resources{font:9pt/1.5 Arial;margin-top:16pt}
 `;document.head.append(style);const sheet=document.createElement('section');sheet.className='sheet';sheet.append(article);document.body.replaceChildren(sheet);await document.fonts.ready;
 const box=article.getBoundingClientRect();if(box.top<72||box.bottom>980)throw Error('Copyright page overflow');
 if(article.textContent!==expected)throw Error('Content changed');return {pages:1,visibleFolio:false,placement:'verso after title page',contentPreserved:true,links:document.querySelectorAll('a').length};
});
await page.pdf({path:path.join(root,'output/pdf/v1.1-copyright-page.pdf'),printBackground:true,preferCSSPageSize:true});
fs.writeFileSync(path.join(root,'prototype/dist/course-full/copyright-page-print.html'),await page.content());fs.writeFileSync(path.join(qa,'layout.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report));
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exitCode=1;});
