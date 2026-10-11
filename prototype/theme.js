// Run before styles load to avoid a light flash when dark mode is selected.
(()=>{
 const root=document.documentElement;
 const system=matchMedia('(prefers-color-scheme: dark)');
 const key='physics-color-theme';
 const valid=value=>['system','light','dark'].includes(value);
 let preference='system';
 try{const saved=localStorage.getItem(key);if(valid(saved))preference=saved;}catch{}
 let select;
 function apply(){
  root.dataset.theme=preference==='system'?(system.matches?'dark':'light'):preference;
  if(select)select.value=preference;
 }
 apply();
 system.addEventListener('change',apply);
 window.addEventListener('storage',event=>{
  if(event.key===key||event.key===null){preference=valid(event.newValue)?event.newValue:'system';apply();}
 });
 document.addEventListener('DOMContentLoaded',()=>{
  const nav=document.querySelector('body > nav');
  if(!nav)return;
  const label=document.createElement('label');
  label.className='theme-control';label.append('Theme ');
  select=document.createElement('select');select.setAttribute('aria-label','Color theme');
  for(const [value,text] of [['system','System'],['light','Light'],['dark','Dark']]){
   const option=document.createElement('option');option.value=value;option.textContent=text;select.append(option);
  }
  select.value=preference;
  select.addEventListener('change',()=>{
   preference=select.value;apply();
   try{localStorage.setItem(key,preference);}catch{}
  });
  label.append(select);nav.append(label);
 });
})();
