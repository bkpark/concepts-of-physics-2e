const fs=require('fs'),path=require('path');
const {chromium}=require('playwright');
(async()=>{
 const root=path.resolve(__dirname,'../..');
 const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
 try{
  const page=await browser.newPage();
  const book=fs.readFileSync(path.join(root,'prototype/dist/course-full/book.html'),'utf8');
  const results=[];
  for(const file of fs.readdirSync(__dirname).filter(n=>/^render-chapter-.*\.cjs$/.test(n))){
   const code=fs.readFileSync(path.join(__dirname,file),'utf8');
   const start=code.indexOf('function flatten(parent)'),end=code.indexOf('return blocks;}',start)+'return blocks;}'.length;
   const result=await page.evaluate(({fn,book})=>{
    const flatten=eval('('+fn+')');
    const doc=new DOMParser().parseFromString(book,'text/html');
    const samples=[...doc.querySelectorAll('.para')].filter(e=>e.querySelector('figure')).map(e=>e.outerHTML);
    samples.push('<div class="para" id="fixture">Before <em>formatted text</em> <figure><figcaption>First caption.</figcaption></figure> Between <strong>two figures</strong> <figure><figcaption>Second caption.</figcaption></figure> After the figures.</div>');
    const norm=t=>t.replace(/\s+/g,'');
    for(const sample of samples){
     const holder=document.createElement('div');holder.innerHTML=sample;
     const expected=norm(holder.textContent),flat=flatten(holder);
     if(norm(flat.map(e=>e.textContent).join(''))!==expected)throw new Error('Lost prose: '+sample.slice(0,100));
    }
    return samples.length;
   },{fn:code.slice(start,end),book});
   results.push({renderer:file,cases:result});
  }
  fs.writeFileSync(path.join(root,'reports/1.1/embedded-figure-regression.json'),JSON.stringify({passed:true,results},null,2)+'\n');
  console.log(JSON.stringify({passed:true,renderers:results.length,casesPerRenderer:results[0].cases}));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exit(1)});
