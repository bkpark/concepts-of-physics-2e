// Copy text is generated from the displayed MathML at build time.
// Ordinary text selection and browser copy remain untouched.
(() => {
 const equations=[...document.querySelectorAll('[data-copy-latex] > math')].filter(m=>m.parentElement.dataset.copyLatex.trim());
 if(!equations.length){window.mathReady=true;return;}
 const dialog=document.createElement('dialog');dialog.className='math-copy-dialog';
 dialog.setAttribute('aria-labelledby','math-copy-title');
 dialog.innerHTML='<div class="math-copy-heading"><h2 id="math-copy-title">Copy equation</h2><button type="button" class="math-copy-close" aria-label="Close equation copying">Close</button></div><label for="math-copy-format">Format</label><select id="math-copy-format"><option value="latex">LaTeX</option><option value="asciimath">ASCIIMath</option></select><label for="math-copy-text">Equation text</label><textarea id="math-copy-text" readonly spellcheck="false"></textarea><p class="math-copy-note"></p><div class="math-copy-actions"><button type="button" class="math-copy-submit">Copy LaTeX</button><span role="status" aria-live="polite"></span></div>';
 document.body.append(dialog);
 const format=dialog.querySelector('select'), output=dialog.querySelector('textarea');
 const note=dialog.querySelector('.math-copy-note'), status=dialog.querySelector('[role="status"]');
 const copy=dialog.querySelector('.math-copy-submit');let active=null;
 function refresh(){
  output.value=active.parentElement.dataset[format.value==='latex'?'copyLatex':'copyAsciimath'];
  copy.textContent='Copy '+(format.value==='latex'?'LaTeX':'ASCIIMath');status.textContent='';
  const notes=active.parentElement.dataset.copyNotes.split(' '), hints=[];
  if(format.value==='latex'){
   hints.push('Use inside math mode. Requires amsmath'+(notes.includes('cancel')?' and cancel':'')+'.');
   if(notes.includes('unicode-latex'))hints.push('Some symbols require a Unicode-capable LaTeX setup.');
  }
  else {
   if(notes.includes('multiline'))hints.push('Multiline layout uses an invisible matrix; alignment may vary by renderer.');
   if(notes.includes('unicode'))hints.push('Unicode preserves symbols without a supported ASCIIMath name.');
  }
  note.textContent=hints.join(' ');note.hidden=!note.textContent;
 }
 function open(math){active=math;refresh();dialog.showModal();format.focus();}
 const trigger=document.createElement('button');trigger.type='button';
 trigger.className='math-copy-trigger';trigger.textContent='Copy';trigger.hidden=true;
 trigger.setAttribute('aria-label','Copy equation');trigger.setAttribute('aria-haspopup','dialog');
 let candidate=null,hideTimer;
 function hide(){clearTimeout(hideTimer);trigger.hidden=true;}
 function reveal(math){
  if(dialog.open||!getSelection()?.isCollapsed)return;
  clearTimeout(hideTimer);candidate=math;
  // One out-of-flow button: no change to equation width or punctuation wrapping.
  math.after(trigger);trigger.hidden=false;
  const r=math.getBoundingClientRect(),w=trigger.offsetWidth,h=trigger.offsetHeight;
  const fitsRight=r.right+w+12<innerWidth;
  trigger.style.left=Math.max(8,Math.min(innerWidth-w-8,fitsRight?r.right+6:r.right-w))+'px';
  trigger.style.top=Math.max(8,Math.min(innerHeight-h-8,fitsRight?r.top:r.top-h-5))+'px';
 }
 function deferHide(){hideTimer=setTimeout(()=>{if(document.activeElement!==trigger&&document.activeElement!==candidate)hide();},250);}
 trigger.addEventListener('pointerenter',()=>clearTimeout(hideTimer));
 trigger.addEventListener('pointerleave',deferHide);
 trigger.addEventListener('focus',()=>clearTimeout(hideTimer));
 trigger.addEventListener('click',()=>{if(candidate)open(candidate);hide();});
 document.addEventListener('pointerdown',e=>{if(e.target!==trigger&&!candidate?.contains(e.target))hide();});
 document.addEventListener('focusin',e=>{if(e.target!==trigger&&e.target!==candidate)hide();});
 document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!dialog.open)hide();});
 document.addEventListener('selectionchange',()=>{if(!getSelection()?.isCollapsed)hide();});
 function reposition(){
  if(trigger.hidden||!candidate)return;
  const r=candidate.getBoundingClientRect();
  if(r.bottom<0||r.top>innerHeight)hide();else reveal(candidate);
 }
 window.addEventListener('scroll',reposition,{passive:true,capture:true});
 window.addEventListener('resize',reposition);
 for(const math of equations){
  math.tabIndex=0;
  math.addEventListener('pointerenter',e=>{if(e.pointerType==='mouse')reveal(math);});
  math.addEventListener('pointerleave',deferHide);
  math.addEventListener('focus',()=>reveal(math));
  math.addEventListener('click',()=>reveal(math));
  math.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();reveal(math);trigger.focus();}});
 }
 dialog.querySelector('.math-copy-close').addEventListener('click',()=>dialog.close());
 dialog.addEventListener('close',()=>active?.focus({preventScroll:true}));
 format.addEventListener('change',refresh);
 copy.addEventListener('click',async()=>{
  try {await navigator.clipboard.writeText(output.value);status.textContent=(format.value==='latex'?'LaTeX':'ASCIIMath')+' copied.';}
  catch {output.focus();output.select();status.textContent='Select and copy the equation text above (Ctrl+C or Command+C).';}
 });
 window.mathReady=true;
})();

// Keep ordinary math ink visible; opt into horizontal scrolling only when the
// unbreakable equation/punctuation group is wider than its available line.
const punctuationGroups=[...document.querySelectorAll('.math-with-punctuation')];
function sizeMathGroup(group){
 group.classList.toggle('math-needs-scroll',group.scrollWidth>group.clientWidth+1);
}
const mathGroupObserver=new ResizeObserver(entries=>{
 for(const {target} of entries)sizeMathGroup(target);
});
for(const group of punctuationGroups){sizeMathGroup(group);mathGroupObserver.observe(group);}
document.fonts.ready.then(()=>punctuationGroups.forEach(sizeMathGroup));
