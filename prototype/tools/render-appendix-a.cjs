// Appendix A: paginate the maintained atomic-mass table without splitting element groups.
const {chromium}=require('playwright');
const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'../..');
const dist=path.join(root,'prototype/dist/course-full');
const qa=path.join(root,'reports/1.1/appendix-a-print');
const previous=JSON.parse(fs.readFileSync(path.join(root,'reports/1.1/chapter-14-print/layout.json'),'utf8'));
const end=previous.startPage+previous.pages-1,startPage=end+1+(end%2);
(async()=>{
 fs.mkdirSync(qa,{recursive:true});
 const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
 try{
 const page=await browser.newPage();
 await page.setContent(fs.readFileSync(path.join(dist,'book.html'),'utf8'),{waitUntil:'domcontentloaded'});
 const report=await page.evaluate(async(startPage)=>{
  const source=document.querySelector('article#m42699').cloneNode(true);
  source.querySelectorAll('script,.math-copy-toolbar,nav').forEach(e=>e.remove());
  const table=source.querySelector('table'), rows=[...table.tBodies[0].rows];
  const normalize=s=>s.replace(/\s+/g,' ').trim();
  const expected=rows.map(r=>normalize(r.textContent));
  const notes=source.querySelector('.table-notes');
  const attribution=source.querySelector('.attribution');
  source.querySelectorAll('a[href]').forEach(a=>{if(!a.getAttribute('href').startsWith('#'))a.href=new URL(a.getAttribute('href'),'https://intro-1-1.coaphys.xyz/').href;});
  document.head.replaceChildren();document.body.replaceChildren();
  const style=document.createElement('style');style.textContent=`
   @page{size:Letter;margin:0}*{box-sizing:border-box}body{margin:0;color:#111;font:10.5pt/1.3 Georgia,serif}
   .sheet{width:8.5in;height:11in;padding:.6in .65in .65in 1in;position:relative;break-after:page}.sheet:last-child{break-after:auto}.sheet:nth-child(even){padding-left:.65in;padding-right:1in}
   .area{height:9.75in}.running{position:absolute;top:.29in;left:1in;right:.65in;border-bottom:.5pt solid #bbb;padding-bottom:5pt;color:#555;font:8pt Arial}.sheet:nth-child(even) .running{left:.65in;right:1in}
   .folio{position:absolute;bottom:.3in;right:.65in;font:9pt Arial}.sheet:nth-child(even) .folio{right:auto;left:.65in}
   h1{font:600 19pt Arial;margin:0 0 13pt}h2{font:600 11pt Arial;margin:12pt 0 6pt}.eyebrow{font:9pt Arial;color:#555;margin:0 0 5pt}.para,p{margin:0 0 7pt}a{color:inherit;text-decoration:none}
   table{width:100%;table-layout:fixed;border-collapse:collapse;font:9pt/1.2 Georgia,serif;margin:0 0 9pt}td,th{border:.5pt solid #b4bebe;padding:3.5pt 4pt;vertical-align:middle;overflow-wrap:normal}th{background:#edf1f2;font-weight:bold;font-size:8pt;text-align:center}td:first-child,td:nth-child(3),td:nth-child(4){text-align:center}
   caption{font:9pt/1.25 Arial;text-align:left;margin:0 0 5pt}math{font-family:'Cambria Math';font-size:1em}mtd{padding:0}sup{font-size:.75em}.table-notes{font:9pt/1.3 Arial}.table-notes p{margin-bottom:7pt}.table-notes h3{font:bold 10pt Arial;margin:8pt 0 5pt}.attribution{font:8.5pt/1.3 Arial;margin-top:12pt}.attribution h2{font-size:10pt}
  `;document.head.append(style);
  let area,body,currentTable;const pages=[];
  function newPage(){const sheet=document.createElement('section');sheet.className='sheet';sheet.innerHTML='<div class="running">APPENDIX A · ATOMIC MASSES</div><div class="area"></div><div class="folio">'+(startPage+pages.length)+'</div>';document.body.append(sheet);area=sheet.querySelector('.area');pages.push(sheet);return area;}
  function fits(){return [...area.children].every(e=>e.getBoundingClientRect().bottom<=area.getBoundingClientRect().bottom+.5);}
  function newTable(){currentTable=table.cloneNode(false);const caption=table.caption.cloneNode(true);if(pages.length>1)caption.append(' (continued)');currentTable.append(caption);const cg=document.createElement('colgroup');[9,17,10,8,19,19,18].forEach(w=>{const c=document.createElement('col');c.style.width=w+'%';cg.append(c);});currentTable.append(cg,table.tHead.cloneNode(true));body=document.createElement('tbody');currentTable.append(body);area.append(currentTable);}
  newPage();const header=source.querySelector('header').cloneNode(true);header.querySelector('.eyebrow').textContent='APPENDIX A';area.append(header,source.querySelector('.content > .para').cloneNode(true));
  await document.fonts.ready;newTable();
  const groups=[];for(const row of rows){if(row.cells[0].textContent.trim()||!groups.length)groups.push([]);groups.at(-1).push(row);}
  for(const group of groups){body.append(...group);if(!fits()){group.forEach(r=>r.remove());newPage();newTable();body.append(...group);if(!fits())throw Error('Element group exceeds a page');}}
  // Notes are preserved as complete paragraphs, with their heading on the first notes page.
  let noteBox=document.createElement('div');noteBox.className='table-notes';noteBox.id=notes.id;area.append(noteBox);
  const noteNodes=[...notes.children];
  for(let i=0;i<noteNodes.length;i++){const node=noteNodes[i];noteBox.append(node);if(!fits()){node.remove();if(!noteBox.textContent.trim())noteBox.remove();newPage();noteBox=document.createElement('div');noteBox.className='table-notes';area.append(noteBox);noteBox.append(node);} }
  area.append(attribution);if(!fits()){attribution.remove();newPage();area.append(attribution);}
  const contentPages=pages.length;if(pages.length%2)newPage();
  const actual=[...document.querySelectorAll('tbody tr')].map(r=>normalize(r.textContent));
  if(JSON.stringify(expected)!==JSON.stringify(actual))throw Error('Table content changed');
  const overflow=[...document.querySelectorAll('td,th')].filter(e=>e.scrollWidth>e.clientWidth+1).map(e=>e.textContent);
  if(overflow.length)throw Error('Overflow cells: '+overflow.join('|'));
  return {startPage,pages:pages.length,contentPages,rows:rows.length,groups:groups.length,tableContentPreserved:true,pageRows:pages.map(s=>s.querySelectorAll('tbody tr').length)};
 },startPage);
 await page.pdf({path:path.join(root,'output/pdf/v1.1-appendix-a.pdf'),printBackground:true,preferCSSPageSize:true});
 fs.writeFileSync(path.join(dist,'appendix-a-print.html'),await page.content());
 fs.writeFileSync(path.join(qa,'layout.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});



