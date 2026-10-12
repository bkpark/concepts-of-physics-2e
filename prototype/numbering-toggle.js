/* Labels are presentation only: URLs, anchors, content, and exercises stay stable. */
(() => {
  const data = window.PHYSICS_NUMBERING;
  if (!data) return;
  const key = 'physics-numbering';
  const valid = value => value === 'course' || value === 'older';
  let mode = 'course';
  try { const saved = localStorage.getItem(key); if (valid(saved)) mode = saved; } catch {}
  const originals = new WeakMap();
  const originalTitle = document.title;
  const escape = value => value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const sectionPattern = new RegExp('(?<![\\d.])(' + Object.keys(data.sections).sort((a,b)=>b.length-a.length).map(escape).join('|') + ')(?=:)', 'g');
  function translate(text) {
    if (mode === 'course') return text;
    return text.replace(/\b(Figure|Equation|Example|Table)\s+(\d+(?:\.(?:\d+|E))+|[A-D]\.\d+(?:\.\d+)*)/g,
      (all,kind,label) => data.labels[kind+' '+label] ? kind+' '+data.labels[kind+' '+label] : all)
      .replace(/\bChapter (\d+)\b/g, (all,n)=>'Chapter '+(data.chapters[n] || n))
      .replace(/\b([Ss]ection) (\d+\.\d+)\b/g, (all,word,n)=>word+' '+(data.sections[n] || n))
      .replace(sectionPattern, label=>data.sections[label]);
  }
  window.physicsNumbering = { translate, get mode() { return mode; } };
  function display(node, original) {
    if (mode === 'course') return original;
    const parent = node.parentElement;
    if (parent.matches('.numbering-note')) return 'CNX-aligned chapter and section numbers follow the 2019 Introduction to Physics PDF. Figures, equations, examples, and tables retain section-based counters in this edition. Chapter introductions use .0 in object labels. Exercise numbers stay the same in both modes. Use the Numbering selector to match the lecture-aligned scheme.';
    if (parent.matches('.eq-label')) {
      const object = data.objects[parent.closest('.equation')?.id];
      if (object && original.trim()) return original.replace('('+object.course+')','('+object.older+')');
    }
    if (parent.matches('.eyebrow')) {
      const module = data.modules[parent.closest('article')?.id];
      if (module && original.trim() === module.course) return original.replace(module.course,module.older);
      if (original === 'Lecture-aligned numbering (July 2026)') return 'CNX-aligned numbering';
    }
    const link = parent.closest('a');
    const fragment = link?.getAttribute('href')?.split('#')[1];
    const object = data.objects[fragment];
    if (object && original.trim() === object.course) return original.replace(object.course,object.older);
    return translate(original);
  }
  let observer;
  function apply() {
    observer?.disconnect();
    const walker = document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
    for (let node; (node=walker.nextNode());) {
      if (node.parentElement.closest('math,svg,script,style,code,pre,textarea,select,#search-results')) continue;
      if (!originals.has(node)) originals.set(node,node.nodeValue);
      const next = display(node,originals.get(node));
      if (node.nodeValue !== next) node.nodeValue = next;
    }
    document.title = translate(originalTitle);
    document.documentElement.dataset.numbering = mode;
    select.value = mode;
    observer?.observe(document.body,{subtree:true,childList:true});
  }
  const label=document.createElement('label');label.className='theme-control numbering-control';label.append('Numbering ');
  const select=document.createElement('select');select.setAttribute('aria-label','Textbook numbering');
  for (const [value,text] of [['course','Lecture-aligned'],['older','CNX-aligned']]) {
    const option=document.createElement('option');option.value=value;option.textContent=text;select.append(option);
  }
  label.append(select);document.querySelector('body > nav')?.append(label);
  function change(value,persist) {
    mode=valid(value)?value:'course';
    if (persist) { try { localStorage.setItem(key,mode); } catch {} }
    apply();document.dispatchEvent(new Event('physics-numbering-change'));
  }
  select.addEventListener('change',()=>change(select.value,true));
  window.addEventListener('storage',event=>{if(event.key===key||event.key===null)change(event.newValue,false);});
  observer=new MutationObserver(()=>apply());
  apply();
})();
