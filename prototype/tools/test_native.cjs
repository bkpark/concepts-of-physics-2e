const {chromium}=require('playwright');
const path=require('path'),fs=require('fs'),http=require('http');
const root=path.resolve(__dirname,'..');
const server=http.createServer((req,res)=>{res.setHeader('Content-Type','text/html; charset=utf-8');res.end(fs.readFileSync(path.join(root,'dist/native-test/index.html')));});
(async()=>{
 await new Promise(r=>server.listen(0,'127.0.0.1',r));
 const browser=await chromium.launch({headless:true,executablePath:process.env.PROTOTYPE_CHROME||'C:/Program Files/Google/Chrome/Application/chrome.exe'});
 try{
 const context=await browser.newContext({permissions:['clipboard-read','clipboard-write'],viewport:{width:1200,height:1000}});
 const page=await context.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(`http://127.0.0.1:${server.address().port}`);await page.evaluate(()=>document.fonts.ready);
 const result={browser:browser.version(),errors,samples:[],scope:'Chrome native HTML selection and system clipboard; PDF character extraction is checked separately'};
 for(const card of await page.locator('section').all()){
  const key=await card.getAttribute('id');
  const selected=await card.evaluate(el=>{const token=[...el.querySelectorAll('mi,mn')].find(n=>n.firstChild?.nodeType===3&&n.textContent.trim());const text=token.firstChild;const range=document.createRange();range.setStart(text,0);range.setEnd(text,Array.from(text.textContent)[0].length);const s=getSelection();s.removeAllRanges();s.addRange(range);return {expected:range.toString(),selection:s.toString()};});
  await page.keyboard.press('Control+c');selected.clipboard=await page.evaluate(()=>navigator.clipboard.readText());
  if(selected.clipboard!==selected.expected)throw Error('Symbol clipboard mismatch '+key);
  const tokenResults=[];
  for(const token of await card.locator('mi,mn,mo,mtext').all()){
   const content=await token.textContent();if(!content.trim()||content==='\u2062')continue;
   const expectedToken=await token.evaluate(el=>{const r=document.createRange();r.selectNodeContents(el);getSelection().removeAllRanges();getSelection().addRange(r);return el.textContent.trim();});
   await page.keyboard.press('Control+c');const copied=await page.evaluate(()=>navigator.clipboard.readText());
   tokenResults.push({expected:expectedToken,copied,pass:copied.trim()===expectedToken});
  }
  await card.evaluate(el=>{const r=document.createRange();r.selectNodeContents(el.querySelector('math'));getSelection().removeAllRanges();getSelection().addRange(r);});
  await page.keyboard.press('Control+c');const plain=await page.evaluate(()=>navigator.clipboard.readText());
  await card.locator('button').click();await card.locator('[role=status]').filter({hasText:'MathML copied'}).waitFor();
  const mathml=await page.evaluate(()=>navigator.clipboard.readText());
  const expected=await card.locator('math').evaluate(e=>e.outerHTML);
  if(mathml!==expected)throw Error('MathML clipboard mismatch '+key);
  await card.locator('textarea').click();await page.keyboard.press('Control+v');
  if(await card.locator('textarea').inputValue()!==expected)throw Error('Paste mismatch '+key);
  result.samples.push({key,symbol:selected,token_tests:tokenResults,whole_selection_plain_text:plain,whole_mathml_clipboard_and_paste:true});
 }
 // Actual mouse drag over a standalone vector, in addition to DOM-range selection.
 const vector=page.locator('#m67530-math-0001 math mi');await vector.scrollIntoViewIfNeeded();
 const b=await vector.boundingBox();await page.mouse.move(b.x-2,b.y+b.height/2);await page.mouse.down();await page.mouse.move(b.x+b.width+2,b.y+b.height/2,{steps:12});await page.mouse.up();
 await page.keyboard.press('Control+c');result.mouse_drag_vector={selected:await page.evaluate(()=>getSelection().toString()),copied:await page.evaluate(()=>navigator.clipboard.readText())};
 if(result.mouse_drag_vector.copied!=='w')throw Error('Mouse drag vector failed');
 result.layout=await page.evaluate(()=>({nativeMathCount:document.querySelectorAll('math').length,svgCount:document.querySelectorAll('svg').length,overflow:[...document.querySelectorAll('.expression')].filter(e=>e.scrollWidth>e.clientWidth+1).length}));
 await page.setViewportSize({width:390,height:844});result.mobile=await page.evaluate(()=>({pageOverflow:document.documentElement.scrollWidth>innerWidth,scrollableExpressions:[...document.querySelectorAll('.expression')].filter(e=>e.scrollWidth>e.clientWidth+1).length}));
 await page.setViewportSize({width:1200,height:1000});await page.evaluate(()=>getSelection().removeAllRanges());
 await page.screenshot({path:path.join(root,'qa/native-web.png'),fullPage:true});
 await page.pdf({path:path.join(root,'output/native-math-selection-test.pdf'),preferCSSPageSize:true,printBackground:true,tagged:true});
 fs.writeFileSync(path.join(root,'qa/native-browser.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result,null,2));
 }finally{await browser.close();server.close();}
})().catch(e=>{console.error(e);server.close();process.exitCode=1;});
