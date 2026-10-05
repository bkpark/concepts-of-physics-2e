const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');
(async () => {
  const root = path.resolve(__dirname, '..');
  const browser = await chromium.launch({headless:true, executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
  const page = await browser.newPage();
  let checked = 0;
  async function check() {
    const results = await page.locator('.math-with-punctuation').evaluateAll(groups => groups.map(group => {
      const math = group.querySelector('math');
      const range = document.createRange(); range.selectNodeContents(group.lastChild);
      const punctuation = range.getBoundingClientRect();
      const expression = math.getBoundingClientRect();
      return {ok:punctuation.left >= expression.right - 1 && punctuation.top < expression.bottom && punctuation.bottom > expression.top, text:group.textContent};
    }));
    for (const result of results) if (!result.ok) throw Error(JSON.stringify(result));
    checked += results.length;
  }
  for (const width of [320,375,650,712,1024]) {
    await page.setViewportSize({width,height:900});
    for (const slug of ['sections/current','sections/electric-potential-and-potential-energy','exercises/electricity-exercises']) {
      await page.goto(pathToFileURL(path.join(root,'dist/course-full',slug,'index.html')).href);
      await check();
    }
  }
  // Force every possible wrap threshold, including an equation wider than its line.
  await page.setContent('<style>'+fs.readFileSync(path.join(root,'style.css'),'utf8')+'</style><div id="fixture">Some preceding prose <span class="math-with-punctuation"><span data-math-key="test"><math><mi>E</mi><mo>=</mo><mi>P</mi><mi>t</mi></math></span>).</span> More prose.</div>');
  for(let width=30;width<=400;width+=2) {
    await page.locator('#fixture').evaluate((e,w)=>e.style.width=w+'px',width);
    await check();
  }
  console.log(JSON.stringify({checked,viewportWidths:[320,375,650,712,1024],wrapThresholdFixtures:186}));
  await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
