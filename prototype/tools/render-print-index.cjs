// Explicit page layout for the alphabetic subject index.
const {chromium}=require('playwright');
const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'../..'),qa=path.join(root,'reports/1.1/index-print');
const data=JSON.parse(fs.readFileSync(path.join(qa,'entries.json'),'utf8'));
data.assembled=process.env.BOOK_ASSEMBLY==='1';
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
 try{
 const page=await browser.newPage();
 await page.setContent('<!doctype html><html><head><meta charset="utf-8"></head><body></body></html>');
 const report=await page.evaluate(async data=>{
  const style=document.createElement('style');style.textContent=`
   @page{size:Letter;margin:0}*{box-sizing:border-box}body{margin:0;color:#111;font:10pt/1.25 Georgia,serif}
   .sheet{width:8.5in;height:11in;padding:.6in .65in .65in 1in;position:relative;break-after:page}.sheet:last-child{break-after:auto}.sheet:nth-child(even){padding-left:.65in;padding-right:1in}
   .area{height:9.75in;display:flex;flex-direction:column}.running{position:absolute;top:.29in;left:1in;right:.65in;border-bottom:.5pt solid #bbb;padding-bottom:5pt;color:#555;font:8pt Arial}.sheet:nth-child(even) .running{left:.65in;right:1in}
   .folio{position:absolute;bottom:.3in;right:.65in;font:9pt Arial}.sheet:nth-child(even) .folio{right:auto;left:.65in}
   h1{font:600 19pt Arial;margin:0 0 10pt}.intro{font:9pt/1.3 Arial;margin:0 0 12pt}
   .columns{display:flex;gap:.25in;flex:1;min-height:0}.column{width:3.3in;flex:none}h2{font:600 13pt Arial;margin:10pt 0 6pt;border-bottom:.5pt solid #bbb;padding-bottom:3pt}.column>:first-child{margin-top:0}
   .entry{padding-left:12pt;text-indent:-12pt;margin-bottom:3pt;overflow-wrap:normal}.refs{font-variant-numeric:lining-nums}a{color:inherit;text-decoration:none}.see{font-style:italic}
  `;document.head.append(style);await document.fonts.ready;
  const sheets=[];let col,cols,index;
  function nextPage(first=false){const sheet=document.createElement('section');sheet.className='sheet';sheet.innerHTML='<div class="running">INDEX</div><div class="area"></div><div class="folio">'+(data.startPage+sheets.length)+'</div>';document.body.append(sheet);sheets.push(sheet);const area=sheet.querySelector('.area');if(first){const h=document.createElement('h1');h.textContent='Index';const p=document.createElement('p');p.className='intro';p.textContent=data.assembled?'Page numbers point to key discussions, chapter glossary entries, and reference tables. Select a page number to jump to that page within this book.':'Page numbers point to key discussions, chapter glossary entries, and reference tables. Select a page number to open the corresponding chapter or appendix PDF.';area.append(h,p);}const columns=document.createElement('div');columns.className='columns';columns.innerHTML='<div class="column"></div><div class="column"></div>';area.append(columns);cols=[...columns.children];index=0;col=cols[0];}
  function nextColumn(){if(index===0){index=1;col=cols[1];}else nextPage();}
  const ids=new Map(data.entries.map((e,i)=>[e.term,'index-entry-'+i]));
  nextPage(true);let letter='';
  function fits(){return col.lastElementChild.getBoundingClientRect().bottom<=col.getBoundingClientRect().bottom+.5;}
  for(const e of data.entries){const initial=e.term.replace(/^[^A-Za-z0-9]+/,'').charAt(0).toUpperCase();let h=null;if(initial!==letter){h=document.createElement('h2');h.textContent=initial;col.append(h);letter=initial;}
   const row=document.createElement('div');row.className='entry';row.id=ids.get(e.term);row.append(document.createTextNode(e.term));
   if(e.see){row.append(document.createTextNode('. '));const see=document.createElement('span');see.className='see';see.textContent='See ';const a=document.createElement('a');a.href='#'+ids.get(e.see);a.textContent=e.see;row.append(see,a);}
   else {row.append(document.createTextNode(', '));e.refs.forEach((p,i)=>{if(i)row.append(document.createTextNode(', '));const a=document.createElement('a');a.className='refs';a.href='https://book-index.invalid/page/'+p;a.textContent=p;row.append(a);});}
   col.append(row);if(!fits()){row.remove();if(h)h.remove();nextColumn();if(h)col.append(h);col.append(row);if(!fits())throw Error('Entry too tall: '+e.term);}
  }
  const contentPages=sheets.length;if(sheets.length%2)nextPage();
  const pageEntries=sheets.map(s=>s.querySelectorAll('.entry').length);
  if(pageEntries.reduce((a,b)=>a+b,0)!==data.entries.length)throw Error('Missing entries');
  return {startPage:data.startPage,pages:sheets.length,contentPages,entries:data.entries.length,pageEntries,pageLinks:document.querySelectorAll('a.refs').length,seeLinks:data.entries.filter(e=>e.see).length};
 },data);
 await page.pdf({path:path.join(qa,data.assembled?'index-assembled.pdf':'index-unlinked.pdf'),printBackground:true,preferCSSPageSize:true});
 fs.writeFileSync(path.join(root,'prototype/dist/course-full',data.assembled?'index-assembled-print.html':'index-print.html'),await page.content());
 fs.writeFileSync(path.join(qa,data.assembled?'layout-assembled.json':'layout.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});

