// Native text selection remains untouched. Structured equation copying is explicit.
let activeMath=null;
const bar=document.createElement('div');bar.className='math-copy-toolbar';
const button=document.createElement('button');button.textContent='Copy selected equation as MathML';
const status=document.createElement('span');status.setAttribute('role','status');
status.textContent='Select or click an equation first.';bar.append(button,status);
document.querySelector('nav').after(bar);
document.querySelectorAll('math').forEach(math=>{
 math.tabIndex=0;
 math.addEventListener('pointerdown',()=>{activeMath=math;status.textContent='Equation selected.';});
 math.addEventListener('focus',()=>{activeMath=math;});
});
button.addEventListener('mousedown',e=>e.preventDefault());
button.addEventListener('click',async()=>{
 const selection=getSelection();const node=selection?.anchorNode;
 const math=(node?.nodeType===1?node:node?.parentElement)?.closest?.('math')||activeMath;
 if(!math){status.textContent='Select or click an equation first.';return;}
 const clone=math.cloneNode(true);clone.removeAttribute('tabindex');
 try{await navigator.clipboard.writeText(clone.outerHTML);status.textContent='MathML copied.';}
 catch(e){status.textContent='Clipboard unavailable. Copy the MathML from the source download.';}
});
window.mathReady=true;
