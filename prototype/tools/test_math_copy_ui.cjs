// Run against the repository-root server at :8765; uses the bundled Playwright.
const assert=require('node:assert/strict');
const {chromium}=require('playwright');
let browser;
(async()=>{
 browser=await chromium.launch({executablePath:process.env.CHROME_PATH||'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 const page=await browser.newPage({viewport:{width:890,height:895}});
 await page.addInitScript(()=>Object.defineProperty(navigator,'clipboard',{value:{writeText:async t=>{window.copiedText=t;}}}));
 await page.goto('http://127.0.0.1:8765/prototype/dist/course-full/sections/gravitational-potential-energy/');
 const math=page.locator('[data-math-key="m71414-math-0019"] > math');
 await math.scrollIntoViewIfNeeded();const before=await math.boundingBox();await math.hover();const trigger=page.locator('.math-copy-trigger');await trigger.waitFor({state:'visible'});assert.deepEqual(await math.boundingBox(),before);await page.screenshot({path:'output/math-copy-trigger-desktop.png'});assert.equal(await page.locator('dialog').isVisible(),false);await math.click();assert.equal(await page.locator('dialog').isVisible(),false);await math.focus();await page.keyboard.press('Tab');assert(await trigger.evaluate(e=>document.activeElement===e));await page.keyboard.press('Enter');
 const dialog=page.locator('dialog');await dialog.waitFor({state:'visible'});
 assert((await page.locator('#math-copy-text').inputValue()).includes('\\begin{array}'));
 await page.locator('.math-copy-submit').click();
 assert.equal(await page.evaluate(()=>window.copiedText),await page.locator('#math-copy-text').inputValue());
 await page.locator('#math-copy-format').selectOption('asciimath');
 assert((await page.locator('#math-copy-text').inputValue()).startsWith('{:'));
 await page.locator('.math-copy-submit').click();
 assert.equal(await page.evaluate(()=>window.copiedText),await page.locator('#math-copy-text').inputValue());
 await page.keyboard.press('Escape');assert.equal(await dialog.isVisible(),false);
 await page.waitForFunction(()=>document.activeElement?.matches('[data-math-key="m71414-math-0019"] > math'));
 // Selecting textbook text never launches a modal or replaces the selection.
 await math.evaluate(e=>{const range=document.createRange();range.selectNodeContents(e);getSelection().removeAllRanges();getSelection().addRange(range);e.dispatchEvent(new MouseEvent('click',{bubbles:true}));});
 assert.equal(await dialog.isVisible(),false);await page.evaluate(()=>getSelection().removeAllRanges());
 await page.setViewportSize({width:390,height:844});await math.click();assert.equal(await dialog.isVisible(),false);await trigger.click();
 assert(await dialog.isVisible());assert(await dialog.evaluate(e=>e.scrollWidth<=e.clientWidth+1));
 await page.evaluate(()=>navigator.clipboard.writeText=async()=>{throw Error('denied')});
 await page.locator('.math-copy-submit').click();
 assert((await page.locator('[role="status"]').textContent()).includes('Ctrl+C'));
 assert(await page.locator('#math-copy-text').evaluate(e=>e.selectionEnd===e.value.length));
 await page.screenshot({path:'output/math-copy-mobile.png'});
 await page.keyboard.press('Escape');await page.setViewportSize({width:890,height:895});
 await math.click();await trigger.click();await page.screenshot({path:'output/math-copy-desktop.png'});
 const touch=await browser.newPage({viewport:{width:390,height:844},isMobile:true,hasTouch:true});await touch.goto(page.url());const tm=touch.locator('[data-math-key="m71414-math-0019"] > math');await tm.tap();await touch.screenshot({path:'output/math-copy-trigger-mobile.png'});assert.equal(await touch.locator('dialog').isVisible(),false);await touch.locator('.math-copy-trigger').tap();assert(await touch.locator('dialog').isVisible());await touch.locator('.math-copy-close').tap();await touch.locator('h1').tap();assert.equal(await touch.locator('.math-copy-trigger').isVisible(),false);await browser.close();console.log('Passed: hover/click reveal without modal, keyboard Copy button, touch two-step interaction, outside dismissal, both copy formats, clipboard fallback, selection and mobile layout.');
})().catch(async e=>{console.error(e);await browser?.close();process.exitCode=1});
