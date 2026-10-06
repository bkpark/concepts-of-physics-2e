/* All queries stay in the browser; only the static index is downloaded. */
(() => {
  const form = document.querySelector('#book-search');
  if (!form) return;
  const input = document.querySelector('#search-query');
  const status = document.querySelector('#search-status');
  const list = document.querySelector('#search-results');
  const more = document.querySelector('#search-more');
  let indexPromise, generation = 0, timer, results = [], shown = 0, terms = [];
  const fold = s => s.toLocaleLowerCase('en');
  const parse = q => [...q.matchAll(/"([^"]+)"|([^\s"]+)/g)].map(m => fold(m[1] || m[2]));
  function highlight(node, text) {
    const lower = fold(text);
    let pos = 0;
    while (pos < text.length) {
      const matches = terms.map(t => ({at: lower.indexOf(t, pos), length: t.length})).filter(m => m.at >= 0).sort((a,b) => a.at-b.at || b.length-a.length);
      if (!matches.length) { node.append(document.createTextNode(text.slice(pos))); break; }
      const match = matches[0];
      node.append(document.createTextNode(text.slice(pos, match.at)));
      const mark = document.createElement('mark');
      mark.textContent = text.slice(match.at, match.at+match.length); node.append(mark);
      pos = match.at + match.length;
    }
  }
  function showMore() {
    const end = Math.min(shown+20, results.length);
    for (const {record} of results.slice(shown, end)) {
      const li = document.createElement('li'), heading = document.createElement('h2'), link = document.createElement('a'), excerpt = document.createElement('p');
      link.href = '../' + record.url; highlight(link, record.title); heading.append(link);
      const positions = terms.map(t => fold(record.text).indexOf(t)).filter(n => n >= 0);
      let start = Math.max(0, (positions.length ? Math.min(...positions) : 0)-90);
      if (start) { const space = record.text.indexOf(' ', start); if (space >= 0) start = space+1; }
      const finish = Math.min(record.text.length, start+320);
      highlight(excerpt, (start ? '…' : '') + record.text.slice(start, finish) + (finish < record.text.length ? '…' : ''));
      li.append(heading, excerpt); list.append(li);
    }
    shown = end; more.hidden = shown >= results.length;
  }
  async function search() {
    const request = ++generation, query = input.value.trim().slice(0, 200);
    terms = parse(query); list.replaceChildren(); more.hidden = true;
    const url = new URL(location.href);
    if (query) url.searchParams.set('q', query); else url.searchParams.delete('q');
    history.replaceState(null, '', url);
    if (!terms.length) { status.textContent = 'Enter a word or phrase to begin.'; return; }
    status.textContent = 'Searching…';
    try {
      if (!indexPromise) indexPromise = fetch('../search-index.json').then(r => { if (!r.ok) throw Error('index'); return r.json(); }).then(rows => rows.map(record => ({record, title:fold(record.title), text:fold(record.text)}))).catch(error => { indexPromise = null; throw error; });
      const index = await indexPromise;
      if (request !== generation) return;
      results = index.filter(r => terms.every(t => r.text.includes(t) || r.title.includes(t))).map(r => ({...r, score:terms.reduce((n,t) => n+(r.title.includes(t)?5:0)+(r.text.includes(t)?1:0),0)})).sort((a,b) => b.score-a.score);
      shown = 0;
      status.textContent = results.length ? `${results.length} matching passage${results.length === 1 ? '' : 's'}.` : 'No matches. Try another word or a shorter phrase.';
      showMore();
    } catch (_) {
      if (request === generation) status.textContent = 'Search could not load. Check your connection and press Search to retry.';
    }
  }
  input.value = (new URL(location.href).searchParams.get('q') || '').slice(0,200);
  input.addEventListener('input', () => { ++generation; clearTimeout(timer); timer = setTimeout(search, 180); });
  form.addEventListener('submit', e => { e.preventDefault(); clearTimeout(timer); search(); });
  more.addEventListener('click', showMore);
  if (input.value) search();
})();
