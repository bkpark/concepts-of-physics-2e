// Appendix C: preserve complete reference tables and their mathematical notation.
const {chromium}=require('playwright');
const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'../..');
const dist=path.join(root,'prototype/dist/course-full');
const qa=path.join(root,'reports/1.1/appendix-c-print');
const previous=JSON.parse(fs.readFileSync(path.join(root,'reports/1.1/appendix-b-print/layout.json'),'utf8'));
const end=previous.startPage+previous.pages-1,startPage=end+1+(end%2);
(async()=>{
 fs.mkdirSync(qa,{recursive:true});
 const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
 try{
 const page=await browser.newPage();
 await page.setContent(fs.readFileSync(path.join(dist,'book.html'),'utf8'),{waitUntil:'domcontentloaded'});
 const report=await page.evaluate(async(startPage)=>{
  const source=document.querySelector('article#m78798').cloneNode(true);
  source.querySelectorAll('script,.math-copy-toolbar,nav').forEach(e=>e.remove());
  const normalize=s=>s.replace(/\s+/g,' ').trim();
  const expected=[...source.querySelectorAll('tbody tr')].map(r=>normalize(r.textContent));
  const blocks=[...source.querySelector('.content').children];
  const attribution=source.querySelector('.attribution');
  source.querySelectorAll('a[href]').forEach(a=>{if(!a.getAttribute('href').startsWith('#'))a.href=new URL(a.getAttribute('href'),'https://intro-1-1.coaphys.xyz/').href;});
  document.head.replaceChildren();const meta=document.createElement("meta");meta.charset="utf-8";document.head.append(meta);document.body.replaceChildren();
  const style=document.createElement('style');style.textContent=`
   @page{size:Letter;margin:0}*{box-sizing:border-box}body{margin:0;color:#111;font:10.5pt/1.3 Georgia,serif}
   .sheet{width:8.5in;height:11in;padding:.6in .65in .65in 1in;position:relative;break-after:page}.sheet:last-child{break-after:auto}.sheet:nth-child(even){padding-left:.65in;padding-right:1in}
   .area{height:9.75in}.running{position:absolute;top:.29in;left:1in;right:.65in;border-bottom:.5pt solid #bbb;padding-bottom:5pt;color:#555;font:8pt Arial}.sheet:nth-child(even) .running{left:.65in;right:1in}
   .folio{position:absolute;bottom:.3in;right:.65in;font:9pt Arial}.sheet:nth-child(even) .folio{right:auto;left:.65in}
   h1{font:600 19pt Arial;margin:0 0 13pt}h2{font:600 11pt Arial;margin:12pt 0 6pt}.eyebrow{font:9pt Arial;color:#555;margin:0 0 5pt}.para,p{margin:0 0 7pt}a{color:inherit;text-decoration:none}
   table{width:100%;table-layout:fixed;border-collapse:collapse;font:9pt/1.2 Georgia,serif;margin:0 0 9pt}td,th{border:.5pt solid #b4bebe;padding:3.5pt 4pt;vertical-align:middle;overflow-wrap:normal}th{background:#edf1f2;font-weight:bold;font-size:9pt;text-align:left}td{text-align:left} .table-wrap{margin-bottom:14pt} ul{font:9pt/1.35 Arial;columns:2;margin:0 0 12pt;padding-left:15pt} li{margin:2pt 0} .objectives{font:9pt/1.3 Arial;margin-bottom:10pt} .objectives h2{display:none} caption .footnote{display:block;font-size:8pt;margin-top:4pt}
   caption{font:9pt/1.25 Arial;text-align:left;margin:0 0 5pt}math{font-family:'Cambria Math';font-size:1em}mtd{padding:0}sup{font-size:.75em}.table-notes{font:9pt/1.3 Arial}.table-notes p{margin-bottom:7pt}.table-notes h3{font:bold 10pt Arial;margin:8pt 0 5pt}.attribution{font:8.5pt/1.3 Arial;margin-top:12pt}.attribution h2{font-size:10pt}
  `;document.head.append(style);
  let area,body,currentTable;const pages=[];
  function newPage(){const sheet=document.createElement('section');sheet.className='sheet';sheet.innerHTML='<div class="running">APPENDIX C · USEFUL INFORMATION</div><div class="area"></div><div class="folio">'+(startPage+pages.length)+'</div>';document.body.append(sheet);area=sheet.querySelector('.area');pages.push(sheet);return area;}
  function fits(){return [...area.children].every(e=>e.getBoundingClientRect().bottom<=area.getBoundingClientRect().bottom+.5);}
  const widths=[[8,25,39,28],[8,22,43,27],[15,45,40],[18,12,20,18,12,20],[13,6,6,13,6,6,13,6,6,13,6,6],[14,31,33,22],[22,78],[22,78],[65,35]];
  source.querySelectorAll('table').forEach((t,i)=>{const cg=document.createElement('colgroup');widths[i].forEach(w=>{const col=document.createElement('col');col.style.width=w+'%';cg.append(col);});t.insertBefore(cg,t.children[1]);});
  newPage();const header=source.querySelector('header');header.querySelector('.eyebrow').textContent='APPENDIX C';area.append(header);
  const objectives=source.querySelector('.objectives');if(objectives)area.append(objectives);
  await document.fonts.ready;
  for(const block of blocks){if(block.querySelector("caption")?.textContent.startsWith("Table C.9."))newPage();area.append(block);if(!fits()){block.remove();newPage();area.append(block);if(!fits())throw Error('Block exceeds page: '+block.textContent.slice(0,100));}}
  area.append(attribution);if(!fits()){attribution.remove();newPage();area.append(attribution);}
  const contentPages=pages.length;if(pages.length%2)newPage();
  const actual=[...document.querySelectorAll('tbody tr')].map(r=>normalize(r.textContent));
  if(JSON.stringify(expected)!==JSON.stringify(actual))throw Error('Table content changed');
  const overflow=[...document.querySelectorAll('td,th')].filter(e=>e.scrollWidth>e.clientWidth+1).map(e=>e.textContent);
  if(overflow.length)throw Error('Overflow cells: '+overflow.join('|'));
  return {startPage,pages:pages.length,contentPages,rows:expected.length,tables:9,tableContentPreserved:true,pageRows:pages.map(s=>s.querySelectorAll('tbody tr').length)};
 },startPage);
 await page.pdf({path:path.join(root,'output/pdf/v1.1-appendix-c.pdf'),printBackground:true,preferCSSPageSize:true});
 fs.writeFileSync(path.join(dist,'appendix-c-print.html'),await page.content());
 fs.writeFileSync(path.join(qa,'layout.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});



