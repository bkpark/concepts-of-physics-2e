const {chromium}=require('playwright');const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'../..'),qa=path.join(root,'reports/1.1/front-matter-print');
const data=JSON.parse(fs.readFileSync(path.join(qa,'source.json'),'utf8'));
(async()=>{const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
try{const page=await browser.newPage();await page.setContent('<!doctype html><html><head><meta charset="utf-8"></head><body></body></html>');
const report=await page.evaluate(async data=>{
 const roman=n=>{let r='';for(const [v,s] of [[1000,'m'],[900,'cm'],[500,'d'],[400,'cd'],[100,'c'],[90,'xc'],[50,'l'],[40,'xl'],[10,'x'],[9,'ix'],[5,'v'],[4,'iv'],[1,'i']])while(n>=v){r+=s;n-=v;}return r;};
 const style=document.createElement('style');style.textContent=`
 @page{size:Letter;margin:0}*{box-sizing:border-box}body{margin:0;color:#111;font:10.5pt/1.32 Georgia,serif}
 .sheet{width:8.5in;height:11in;padding:.6in .65in .65in 1in;position:relative;break-after:page}.sheet:last-child{break-after:auto}.sheet:nth-child(even){padding-left:.65in;padding-right:1in}
 .area{height:9.75in;display:flow-root}.running{position:absolute;top:.29in;left:1in;right:.65in;border-bottom:.5pt solid #bbb;padding-bottom:5pt;color:#555;font:8pt Arial}.sheet:nth-child(even) .running{left:.65in;right:1in}
 .folio{position:absolute;bottom:.3in;right:.65in;font:9pt Arial}.sheet:nth-child(even) .folio{right:auto;left:.65in}
 h1{font:600 19pt Arial;margin:0 0 14pt}h2,h3{font:600 12pt Arial;margin:13pt 0 7pt}.area>:first-child{margin-top:0!important}p,.para{margin:0 0 9pt}a{color:inherit;text-decoration:none}.attribution{font:8.5pt/1.3 Arial;margin-top:8pt}.attribution h2{font-size:10pt;margin-top:8pt}
 .toc-block{margin-bottom:13pt}.unit{font:bold 10pt/1.3 Arial;margin:14pt 0 8pt;color:#444}.toc-row{display:flex;align-items:baseline;gap:6pt;margin:0 0 4pt;font:10pt/1.25 Georgia}.toc-row .title{flex-shrink:1}.dots{border-bottom:.6pt dotted #aaa;flex:1;min-width:12pt}.num{font-variant-numeric:lining-nums;flex:none;min-width:22pt;text-align:right}.chapter{font:bold 11pt/1.25 Arial;margin-bottom:7pt}.section{margin-left:14pt}.back{font:10.5pt/1.3 Arial}.toc-note{font:9pt/1.3 Arial;margin-bottom:14pt}.signature{margin-top:12pt}.historical .area{font-size:10pt;line-height:1.3}.historical .para{margin-bottom:7pt}
 `;document.head.append(style);await document.fonts.ready;
 const prefaceSource=document.createElement('div');prefaceSource.innerHTML=data.preface;prefaceSource.querySelectorAll('nav,script,.math-copy-toolbar').forEach(e=>e.remove());
 prefaceSource.querySelectorAll('a[href]').forEach(a=>{if(!a.getAttribute('href').startsWith('#'))a.href=new URL(a.getAttribute('href'),'https://intro.coaphys.xyz/').href;});
 const sourceSections=[...prefaceSource.querySelectorAll('.content > section')];const expected=sourceSections.map(s=>s.textContent).join('')+prefaceSource.querySelector('.attribution').textContent;
 let sheets,area,tocPages,prefaceMap;
 function newPage(kind){const sheet=document.createElement('section');sheet.className='sheet';sheet.dataset.kind=kind;sheet.innerHTML='<div class="running">'+(kind==='toc'?'CONTENTS':'PREFACE')+'</div><div class="area"></div><div class="folio">'+roman(3+sheets.length)+'</div>';document.body.append(sheet);sheets.push(sheet);area=sheet.querySelector('.area');return area;}
 const fits=()=>[...area.children].every(e=>e.getBoundingClientRect().bottom<=area.getBoundingClientRect().bottom+.5);
 function row(title,number,href,cls='section'){const a=document.createElement('a');a.className='toc-row '+cls;a.href=href;const t=document.createElement('span');t.className='title';t.textContent=title;const dots=document.createElement('span');dots.className='dots';const n=document.createElement('span');n.className='num';n.textContent=number;a.append(t,dots,n);return a;}
 function place(block,kind){area.append(block);if(!fits()){block.remove();newPage(kind);area.append(block);if(!fits())throw Error('Block too tall: '+block.textContent.slice(0,80));}}
 function layout(guess){document.body.replaceChildren();sheets=[];prefaceMap=[];newPage('toc');area.innerHTML='<h1>Contents</h1>';
 const front=document.createElement('div');front.className='toc-block';front.append(row('Preface',roman(guess.start),'#preface-title','chapter'));
 sourceSections.forEach((s,i)=>front.append(row(s.querySelector('h3').textContent,roman(guess.sections[i]||guess.start),'#'+s.id)));
 place(front,'toc');
 for(const ch of data.chapters){const block=document.createElement('div');block.className='toc-block';if(ch.unit){const unit=document.createElement('div');unit.className='unit';unit.textContent=ch.unit;block.append(unit);}block.append(row('Chapter '+ch.number+' · '+ch.title,String(ch.page),'https://book-front.invalid/body/'+ch.page,'chapter'));for(const sec of ch.sections)block.append(row((sec.label?sec.label+'  ':'')+sec.title,String(sec.page),'https://book-front.invalid/body/'+sec.page));place(block,'toc');}
 const back=document.createElement('div');back.className='toc-block';const h=document.createElement('h2');h.textContent='Appendices and End Matter';back.append(h);data.back.forEach(e=>back.append(row((e.label?'Appendix '+e.label+' · ':'')+e.title,String(e.page),'https://book-front.invalid/body/'+e.page,'back')));place(back,'toc');
 if(sheets.length%2)newPage('toc');tocPages=sheets.length;newPage('preface');area.innerHTML='<h1 id="preface-title">Preface</h1>';
 sourceSections.forEach((src,i)=>{const s=src.cloneNode(true);const children=[...s.children];if(i===1&&area.children.length){newPage('preface');sheets.at(-1).classList.add('historical');}
 const header=children.shift();header.id=s.id;const first=children.shift();const opening=document.createElement('div');opening.className='preface-opening';opening.append(header,first);place(opening,'preface');prefaceMap.push(3+sheets.length-1);
 for(const child of children)place(child,'preface');});
 place(prefaceSource.querySelector('.attribution').cloneNode(true),'preface');const contentPages=sheets.length;
 if(sheets.length%2)newPage('preface');
 return {start:3+tocPages,sections:prefaceMap,contentPages};
 }
 let guess={start:9,sections:[]},passes=0,previous;for(;passes<5;passes++){const result=layout(guess);if(result.start===guess.start&&JSON.stringify(result.sections)===JSON.stringify(guess.sections)){previous=result;break;}guess=result;}
 if(passes===5)throw Error('Front-matter pagination did not stabilize');
 const actual=[...document.querySelectorAll('[data-kind="preface"] .area')].map(a=>{const copy=a.cloneNode(true);copy.querySelector('#preface-title')?.remove();return copy.textContent;}).join('');
 const normalize=s=>s.replace(/\s+/g,'');if(normalize(expected)!==normalize(actual))throw Error('Preface source text changed');
 return {startRoman:3,endRoman:2+sheets.length,pages:sheets.length,tocPages,prefaceStartRoman:3+tocPages,prefacePages:sheets.length-tocPages,prefaceSections:sourceSections.map((s,i)=>({title:s.querySelector('h3').textContent,page:prefaceMap[i],roman:roman(prefaceMap[i])})),passes:passes+1,contentPreserved:true,bodyLinks:document.querySelectorAll('a[href^="https://book-front.invalid/body/"]').length};
},data);
await page.pdf({path:path.join(qa,'toc-preface-unlinked.pdf'),printBackground:true,preferCSSPageSize:true});fs.writeFileSync(path.join(root,'prototype/dist/course-full/toc-preface-print.html'),await page.content());fs.writeFileSync(path.join(qa,'layout.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report));
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exitCode=1;});

