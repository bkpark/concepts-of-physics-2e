const {chromium} = require('playwright');
const assert = require('node:assert/strict');
(async () => {
  const browser = await chromium.launch({headless:true, executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
  try {
    const page = await browser.newPage();
    const errors=[]; page.on('pageerror', e => errors.push(String(e)));
    const base='http://127.0.0.1:8765';
    await page.goto(base+'/search/?q=curie');
    await page.waitForFunction(() => document.querySelector('#search-status').textContent.includes('matching passages'));
    assert.match(await page.locator('#search-results').innerText(), /Marie Curie/);
    assert.ok(await page.locator('mark').count() > 0);
    const first=page.locator('#search-results a').first();
    const href=await first.getAttribute('href');
    await first.click();
    assert.equal(await page.evaluate(() => !!document.getElementById(decodeURIComponent(location.hash.slice(1)))),true);
    await page.goBack();
    await page.locator('#search-query').fill('madame curie');
    await page.waitForFunction(() => document.querySelector('#search-status').textContent.startsWith('No matches'));
    await page.locator('#search-query').fill('"Marie Curie"');
    await page.waitForFunction(() => document.querySelector('#search-status').textContent.includes('matching passage'));
    assert.match(await page.locator('#search-results').innerText(), /Marie Curie/);
    await page.locator('#search-query').fill('noether');
    await page.waitForFunction(() => document.querySelector('#search-status').textContent.startsWith('No matches'));
    await page.locator('#search-query').fill('<img src=x onerror=alert(1)>');
    await page.waitForTimeout(300);
    assert.equal(await page.locator('#search-results img').count(),0);
    await page.locator('#search-query').fill('energy');
    await page.waitForFunction(() => !document.querySelector('#search-more').hidden);
    assert.equal(await page.locator('#search-results li').count(),20);
    await page.locator('#search-more').click();
    assert.equal(await page.locator('#search-results li').count(),40);
    for (const width of [390,1024]) {
      await page.setViewportSize({width,height:800});
      assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth));
    }
    await page.screenshot({path:'prototype/qa/search-mobile.png',fullPage:false});
    await page.locator('#search-query').fill('');
    await page.waitForFunction(() => document.querySelector('#search-status').textContent.startsWith('Enter'));
    assert.equal(await page.locator('#search-results li').count(),0);
    const failed=await browser.newPage();
    await failed.route('**/search-index.json',route => route.abort());
    await failed.goto(base+'/search/?q=curie');
    await failed.waitForFunction(() => document.querySelector('#search-status').textContent.startsWith('Search could not load'));
    await failed.unroute('**/search-index.json');
    await failed.getByRole('button',{name:'Search',exact:true}).click();
    await failed.waitForFunction(() => document.querySelector('#search-status').textContent.includes('matching passages'));
    assert.deepEqual(errors,[]);
    console.log('Search checks passed: Curie, multiword/phrase matching, anchors, empty/no results, safe rendering, pagination, mobile, load retry.');
  } finally { await browser.close(); }
})();
